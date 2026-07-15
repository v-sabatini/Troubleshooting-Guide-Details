# Alert Runbooks — On-Call Reference

> **What this covers:** On-call/alert runbooks for three content-pipeline
> alerts: **Content Sieve — flyer items unpublished > 1 day**, the **Home Depot
> Canada (HDCA) DVM module**, and the **Live Flyer Check**. For each: what the
> alert means, how to investigate, and how to resolve. Grounded in Confluence
> pages 12697240306 and 11691786294 (space CTLR) and 13564379282 (space RT).
>
> **Audience:** On-call engineers and content-platform staff. This is more
> engineering/on-call oriented than the processor-facing articles.
>
> **See also:** `storefront-publishing-errors.md` (holds a shorter Live Flyer
> Check summary), `content-v2-and-publishing.md`, `publishing-and-go-live.md`,
> `missing-flyers-and-indexing.md`, `escalation-and-tickets.md`.

---

## 1. Content Sieve — Flyer Items unpublished for more than a day

**Alert name:** `Content Sieve - Flyer Items are unpublished for more than a day`
**Priority:** P2 — lost revenue from missing searchable flyer items.

**What it means:** Content Sieve continuously polls for eligible flyer items to
publish to the `Eventification.FlyerItems` topic, joining `Merchants`,
`Flyer Runs`, `Flyers`, `Page Items` and `CrowdCuration Flyer Items` from their
Kafka topics. When items sit at `READY_FOR_PUBLISHING` for more than a day, the
Datadog monitor fires (there is also a **Content Sieve Lag** monitor).

**Potential impact:** Flyer items would not be available in Search and IMS.

**Key references:** service repo `wishabi/content-sieve`; event emitter
`app/lib/jobs/flyer_run_check.rb`; Prime Radiant service
`content-sieve-consumer`; consumer group in Lenses
(`content-sieve-consumer`). (Dashboard/monitor/log links in the source doc.)

### Investigation

1. **Verify the alert** by running the `FlyerRunCheck` query. Note the
   `flyers.available_to >= NOW()` filter — only currently-active flyers are
   returned; items with expired flyers can never be published and should not be
   investigated here.

   ```sql
   SELECT DISTINCT `flyer_items`.`flyer_run_id`
   FROM `flyer_items`
       INNER JOIN `page_items` ON `page_items`.`id` = `flyer_items`.`page_item_id`
       INNER JOIN `flyer_runs` ON `flyer_runs`.`id` = `flyer_items`.`flyer_run_id`
       LEFT OUTER JOIN `flyers` ON `flyers`.`id` = `flyer_items`.`flyer_id`
   WHERE `flyer_runs`.`state` = 'ops_complete'
     AND `flyer_runs`.`available_to` >= CURDATE()
     AND `flyer_items`.`publish_status` = 'READY_FOR_PUBLISHING'
     AND `flyer_items`.`updated_at` < DATE_SUB(NOW(), INTERVAL 1 DAY)
     AND `flyers`.`id` IS NOT NULL
     AND `flyers`.`available_to` >= NOW();
   ```

2. **Check publishing lag** — this query should return **no** row with
   `flyer_items.updated_at >= 1 day ago`:

   ```sql
   SELECT count(*) FROM flyer_items FORCE INDEX(index_flyer_items_on_publish_status)
   INNER JOIN `flyers` ON `flyers`.`id` = `flyer_items`.`flyer_id`
   INNER JOIN `flyer_runs` ON `flyer_runs`.`id` = `flyer_items`.`flyer_run_id`
   INNER JOIN `page_items` ON `page_items`.`id` = `flyer_items`.`page_item_id`
   INNER JOIN `merchants` ON `merchants`.`id` = `flyer_items`.`merchant_id`
   WHERE `flyer_items`.`publish_status` = 'READY_FOR_PUBLISHING'
     AND `flyer_runs`.`state` = 'ops_complete'
     AND `flyers`.`available_to` >= NOW() LIMIT 2000;
   ```

   (A fuller row-level variant selecting the joined item/page/flyer/merchant
   columns is in the source doc.)

3. **Confirm recent output** — messages published to `Eventification.FlyerItems`
   in the last few hours:

   ```sql
   USE `kafka`;
   SELECT * FROM Eventification.FlyerItems where _meta.timestamp > NOW() - '4h' LIMIT 100;
   ```

4. **Confirm the consumer has active connections** to the cluster (Lenses
   consumer group `content-sieve-consumer`).

5. **Identify missing joins** — each of these should ideally return **no**
   results. Missing rows mean upstream content never landed:
   - **Merchants:** `LEFT JOIN merchants ... WHERE merchants.id IS NULL`
   - **Flyer Runs:** `LEFT JOIN flyer_runs ... WHERE flyer_items.flyer_run_id IS NULL`
   - **Flyers:** `LEFT JOIN flyers ... WHERE flyer_items.flyer_id IS NULL`
   - **Page Items:** `LEFT JOIN page_items ... WHERE flyer_items.page_item_id IS NULL`

   (Full SQL for each in the source doc; all filter on
   `publish_status = 'READY_FOR_PUBLISHING'` and active flyers.)

### Resolution

1. Use the join queries above to determine if upstream content is missing.
2. Republish the missing upstream content (see the Rails-console section below).
3. If a topic/partition has stalled, follow **Stuck partition / consumer
   offset** below.
4. **Missing merchant record** (Step 5 Merchants returns IDs with no
   `merchants` row): the `Merchants.Merchant` Kafka message was never published
   or failed to upsert.
   - Check whether the merchant exists in fadmin.
   - Verify it is a Canadian or American merchant (merchant-admin edit page).
   - If it exists, trigger a **republish of the merchant** to the
     `Merchants.Merchant` topic **from merchant-admin** (not fadmin — fadmin has
     no `Merchants.Merchant` producer). content-sieve-consumer will ingest it,
     and the poller publishes the affected flyer items on the next cycle.
   - If the merchant does **not** exist in fadmin, the content cannot be
     recovered. Silence the alert by moving the items to a terminal status:

     ```sql
     UPDATE flyer_items
     SET publish_status = 'UNPUBLISHABLE'
     WHERE merchant_id IN (<affected_ids>)
       AND publish_status = 'READY_FOR_PUBLISHING';
     ```

5. Republish the affected flyer items.

### Republishing from the fadmin production Rails console

Several resolution steps ("republish page items / flyer items") run from the
**fadmin production Rails console**. It re-emits upstream content to the topics
content-sieve consumes (`Flyers.PageItem`, `Flyers.FlyerItem`).

The console runs on the `fadmin` web pods in the `services-eks-prod` EKS cluster
(us-east-1, namespace `fadmin`). Exec into a `fadmin-*` pod (container `fadmin`)
via k9s or kubectl and start the console. `RAILS_ENV` is **not** set in the
container, so pass it explicitly or Rails won't boot as production:

```shell
POD=$(kubectl --context fadmin-prod get pods -l app=fadmin -o jsonpath='{.items[0].metadata.name}')
kubectl --context fadmin-prod exec -it "$POD" -c fadmin -- env RAILS_ENV=production bundle exec rails console
# or, once shelled into the pod:
RAILS_ENV=production bundle exec rails console
```

This is **production** (`fadmin_production`): reads are safe; any producer call
or write hits live data. Use the `fadmin-*` web pods, **not** `delayed-jobs-*`
pods. For read-only poking, `rails console --sandbox` rolls back on exit. (The
staging console uses a different pod label and `RAILS_ENV` — see the source
doc's staging-access page.)

**Republish page items** (content-sieve joins on page items, so this is the
usual recovery lever). Producer `Kafka::Producers::PageItemProducer` → topic
`Flyers.PageItem`. `send_events` always emits for the records passed (no
dirty-check), so it is safe for manual recovery:

```ruby
# one or more page items by id
Kafka::Producers::PageItemProducer.send_events(PageItem.where(id: PAGE_ITEM_IDS))

# every page item in a flyer run, batched
PageItem.where(page_id: FlyerRun.find(FLYER_RUN_ID).page_ids).ids.in_groups_of(100) do |group|
  Kafka::Producers::PageItemProducer.send_events(PageItem.where(id: group.compact))
end
```

**Republish flyer items.** Producer `Kafka::Producers::FlyerItemsProducer` →
topic `Flyers.FlyerItem`:

```ruby
# one or more flyer items by id
Kafka::Producers::FlyerItemsProducer.send_events(FlyerItem.where(id: FLYER_ITEM_IDS))

# all flyer items on a flyer, batched
Flyer.find(FLYER_ID).flyer_items.in_groups_of(100) do |group|
  Kafka::Producers::FlyerItemsProducer.send_events(group.compact)
end
```

### Stuck partition / consumer offset

A partition can get pinned on a single offset that never advances — the
**Content Sieve Lag** monitor fires, and Lenses shows the consumer group's
committed offset on one partition not moving.

**How to recognize it:**
- In Lenses, one partition's committed offset is frozen while lag climbs.
- In CloudWatch, the **same entity** (same `id` / `message_id`) is reprocessed
  every few minutes, each time on a **different** `container_id`, often
  interleaved with a rebalance storm (`Timed out while waiting for response` on
  `join_group`/`sync_group`, `Kafka::RebalanceInProgress`).

**Root-cause pattern:** The consumer only republishes flyer items when a
**monitored attribute** of the incoming message differs from the stored row
(`app/lib/utils/flyer_item_updater.rb#monitored_attributes`):

| Model | Monitored attributes |
| --- | --- |
| `Merchant` | `large_image_path`, `storefront_logo_url`, `translations` |
| `Fadmin::Flyer` | `language`, `available_to`, `available_from`, `valid_to`, `valid_from` |
| `Fadmin::FlyerRun` | `state` |

The whole batch is consumed in **one transaction**. If a monitored attribute
differs, the consumer fires `republish_flyer_items`. If that republish can't
commit (lock contention / deadlock / the member is kicked mid-batch and
rebalances), the **entire batch rolls back** — so the differing attribute is
never persisted, the diff never resolves, and the offset never advances. The
redelivered message hits the same diff and loops indefinitely.

**Resolution:**
1. From Lenses, get the message at the stuck offset; pull the corresponding row
   from the Content Sieve DB.
2. Diff the **monitored attributes** for that model (table above) — find the
   field that differs between the Kafka message and the DB row.
3. Align the DB row to the message so the diff disappears, e.g. (merchant
   translations diff):

   ```sql
   UPDATE merchants
   SET translations = '<exact JSON from the Kafka message>'
   WHERE id = <merchant_id>;
   ```

   On the next consume the dirty-check comes back empty → no republish → the
   batch commits cheaply → the offset advances.

4. **If you get** `Lock wait timeout exceeded`, a long-running consumer
   transaction (the stuck batch itself) is holding the row lock. Find and kill
   it, then immediately re-run the `UPDATE`:

   ```sql
   SELECT trx_id, trx_state, trx_started,
          TIMESTAMPDIFF(SECOND, trx_started, NOW()) AS age_s,
          trx_mysql_thread_id AS thread_id,
          trx_rows_locked, trx_rows_modified, LEFT(trx_query, 200) AS query
   FROM information_schema.innodb_trx
   ORDER BY trx_started ASC;          -- oldest / highest rows_locked is the culprit
   KILL <thread_id>;
   ```

   Killing it just rolls back the batch that was failing anyway. After the kill,
   Kafka must rebalance before another consumer re-reads the offset — that's
   your window.

A heavy `republish_flyer_items` (large merchant/flyer/run) is what makes this
loop likely. PR #68 switched `republish_flyer_items` from per-row `update!` to
bulk `update_all` to shrink the deadlock window.

**Verify:** publishing lag reduced; consumer lag on ingested topics reduced;
messages appear on `Eventification.FlyerItems`; the Lenses offset advances past
the stuck offset; the `Changed attributes <Model> <id>` / `Updating flyer items`
CloudWatch lines for that entity stop recurring.

**Notable past occurrences:**
- *2026-05-11* — flyer_runs 1207647/1207648: missing merchant 7321 (absent from
  fadmin and Kafka). flyer_runs 1062812/1139066: flyer expired Sept 2025.
  Fixed the verification query and Step 5a SQL bug, and tightened the
  `FlyerRunCheck` window from `6.months.ago` to `Time.zone.now`.
- *2026-06-09* — `Merchants.Merchant` partition 3 stuck at offset 1695430 on
  merchant 1976 (Familiprix): DB `translations` carried a stale `es` locale
  absent from the message → merchant flagged "changed" on every redelivery →
  per-row `update!` republish deadlocked against the poller and never committed
  → offset looped + rebalance storm. Aligned `merchants.translations` to the
  message (after `KILL`-ing the transaction holding the row lock). Root-cause
  fix: PR #68.

---

## 2. Home Depot Canada (HDCA) DVM module — On-Call Runbook

**Module type:** Top Offers + Weather Signals (Phase 2). Slack channel
`#thdca-dvm`.

**Overview:** The HDCA DVM module delivers dynamically rendered promotional
content on Flipp's Hosted and App channels. Phases:
- **Phase 1 – Top Offers:** live since 2026-03-26 (Hosted).
- **Phase 2 – Weather Signals:** live since 2026-04-16 (Hosted & App).

Data flows daily: retailer-supplied local feed → **AMP Production ingestion** →
**DVM rendering**. Hourly audits post results to `#dvm-rendering-incidents`;
feed-ingestion failures surface in `#content-feeds-support` via Datadog alerts.

**Module schedule (EST):**

| Ingestion job | Scheduled time | Notes |
| --- | --- | --- |
| PRODUCT ingestion | ~10:10 AM | Must complete before OFFERS |
| OFFERS ingestion | ~10:30 AM | Depends on the PRODUCT run |
| Feed file expected by | ~10:00–10:15 AM | Late delivery is the #1 cause of incidents |
| Audit checks | Hourly | Results post to `#dvm-rendering-incidents` |

**Monitoring:**
- Datadog alert in `#content-feeds-support` → feed ingestion failed or feed file
  not received.
- Audit check fails in `#dvm-rendering-incidents` → module has missing or 0
  offers; may indicate ingestion didn't run.

### Troubleshooting playbook

1. **Identify the alert.** Check `#dvm-rendering-incidents` for hourly audit
   failures and `#content-feeds-support` for Datadog feed-ingestion alerts
   tagged to Home Depot Canada.
2. **Check if the feed file was delivered.** The most common root cause is HDCA
   delivering the feed file *after* the ingestion scheduler ran (expected by
   ~10:00–10:15 AM EST).
   - Check whether the feed file exists in the expected S3 location (ask AMP eng
     / feeds support if you lack AWS access).
   - **Not yet present:** wait and monitor; escalate to the Partner Technology
     Manager or the HDCA contact if the file is more than 2 hours late.
   - **Present but not picked up:** proceed to step 3.
   - **Known pattern:** HDCA often uploads after the scheduled ingest time
     (10:47 AM observed on 2026-05-28); the job has already run and missed the
     file, so a manual re-run is required.
3. **Manually restart ingestion.** Tag `@amp-prod-eng` (or the AMP feed-ingestion
   engineers) in `#content-feeds-support`:
   - Restart **PRODUCT ingestion** first.
   - Once PRODUCT completes, restart **OFFERS ingestion**.
   - Confirm the feed configs are re-run (reply to the Datadog alert thread).
4. **Verify the module is live.** Check the next hourly audit in
   `#dvm-rendering-incidents` to confirm the module is populating with offers;
   you can also verify via the module URL / test environment.
5. **Check the module schedule.** If the module is expected live but isn't,
   verify the current flyer-run dates/schedule on the *DVM Partner: Home Depot
   CA Modules* page (Confluence RT 13052313621). The module is only live during
   active flyer periods — expired offers won't show even if ingestion is
   healthy. If the module isn't scheduled to be live (between flyer runs),
   missing offers have **no user impact** — confirm before escalating
   externally.
6. **Escalate if unresolved.** If the issue persists after re-running ingestion:
   tag the Partner Technology Manager in `#thdca-dvm` with what was tried; loop
   in the Engineering Manager if eng investigation is needed; if HDCA data is
   the issue and the module is live, have Customer Success reach out to the HDCA
   contact.

**Recurring pattern:** HDCA feed delivery is inconsistent — files expected
before ~10:15 AM EST have arrived as late as 10:47 AM or not at all. Across
recent incidents (Mar–Jun 2026) the predominant root cause is **late feed-file
delivery by HDCA**. The AMP team is investigating a longer-term event-driven
ingestion trigger (vs. a fixed schedule).

**Reference tickets/links:** PPP-1119 (feed ingestion, AMP/CCOL); DR-358 / DR-280
(DVM Rendering epics); channels `#content-feeds-support`,
`#dvm-rendering-incidents`, `#thdca-dvm`. (Contacts in the source doc — not
stored here.)

---

## 3. Live Flyer Check

**Alert name:** `Live Flyer Check failed`. **Priority:** P2.

> A shorter version of this runbook already lives in
> `storefront-publishing-errors.md`. This section is the fuller reference.

**What it means:** Live flyers are not available in **FMS** (Flyer Metadata
Service). The alert fires when the live-flyer-check script detects a flyer is
not available in FMS.

**Potential impact:** Missing/unavailable flyers, potentially leading to lost
revenue.

**Reference:** GitHub Actions workflow `missing_flyers.yml` in
`wishabi/flyer-metadata-service-api`.

### Investigation

1. **Rerun** the *Missing Flyer Check* GitHub Actions workflow.
2. Check whether the alerted flyer IDs are **already known / intentionally
   ignored** — see *Suppressing known flyers* below before investigating
   further.
3. **Verify the flyer IDs are not in** the `production_fms_flyer_metadata`
   DynamoDB table. To show in the FMS dynamo table, a flyer must exist in both
   Kafka topics below:

   ```sql
   SELECT * FROM Eventification.Flyers
     WHERE _meta.timestamp > NOW() - "7d"
       AND _value.flyer.id IN ( 7972679, 7972680, 7972687, 7972688 );
   ```

   ```sql
   SELECT * FROM Flyers.Thumbnail
     WHERE _meta.timestamp > NOW() - "7d"
       AND _value.flyer_id IN ( 7972679, 7972680, 7972687, 7972688 );
   ```

   (The IDs above are examples — substitute the alerted flyer IDs.) A flyer
   missing here may need the Ops team pinged (`@enable-cxe`).
4. Investigate the flyer **eventification pipeline**.

### Resolution

1. **If the flyer is not in the database**, reduce the flyer run's `valid_to`
   and `available_to` in fadmin, then republish. Find the flyer run id:

   ```sql
   select id, flyer_run_id, available_to from flyers where id in () group by flyer_run_id;
   ```

   Then edit and **republish** the run at
   `fadmin.flippback.com/flyer_runs/{FLYER_RUN_ID}`.
2. **Check the flyer IDs in the pricing zones for errors** at
   `flyers.merchants.wishabi.ca/flyer_runs/{FLYER_RUN_ID}/pricing_zones`. If
   errors are found, notify the `content-public` channel.
3. Re-confirm the flyer now exists in both `Eventification.Flyers` and
   `Flyers.Thumbnail` topics (queries as in Investigation step 3).
4. **If it is in the database**, it's a **code issue** — investigate/escalate to
   engineering.

### Suppressing known flyers

Use when a flyer run is intentionally being ignored (mid-migration, known
processing delay) and the alert is expected noise. The check supports an
`IGNORED_FLYER_IDS` allowlist; any flyer ID in the list is excluded from the
missing-metadata check and will not alert.

**To add IDs:** in `wishabi/flyer-metadata-service-api`, go to **Settings →
Secrets and variables → Actions → Variables**, edit `IGNORED_FLYER_IDS` (a JSON
array of integers, e.g. `[7945656, 7945657]`), and save. The next hourly run
skips those IDs.

**To remove IDs:** edit `IGNORED_FLYER_IDS` and remove them (or set `[]` to
clear). **Always clear the allowlist once the issue is resolved** — suppressed
IDs will never alert even if they go missing for a different reason.

**Verify:** rerun the failing instance of the Live Flyer Check job.

**Notable past occurrences:** most resolutions were "edit dates with no real
change and resubmit/republish," which made the flyer appear in DynamoDB; some
were flyers still processing (message `content-public`); one (2026-05-22) was
intentional suppression via `IGNORED_FLYER_IDS` for flyers `7945656`/`7945657`
(allowlist feature added in PR #62).

---

*Source: Confluence "Alert Runbook: Content Sieve - Flyer Items are unpublished
for more than a day" (CTLR, 12697240306); "Home Depot Canada DVM Module —
On-Call Runbook" (RT, 13564379282); "Alert Runbook: Live Flyer Check" (CTLR,
11691786294). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
