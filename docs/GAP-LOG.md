# CXE Help Center — Gap Log

Known gaps in the CXE Help Center: real questions the assistant **couldn't fully
answer** from the current content, or where we found no documented fix. Each entry
records what was asked, what the Help Center currently offers, what a source scan
turned up, and the recommended follow-up.

**How to use this:** When testing (or in real use) the bot hits something it can't
resolve, add an entry. When someone learns the actual root cause/fix, turn it into
a proper article (or add to an existing one) and mark the gap **Resolved**.

**Status key:** 🔴 Open · 🟡 Investigating · 🟢 Resolved (content added)

---

## GAP-001 — "Publish Publications" errors under hosted-only distribution 🟡 Investigating

- **V2 context added 2026-07-15:** `content-v2-and-publishing.md` now explains
  *why* per-channel distribution ("hidden except hosted") is a first-class concept
  — in V2, Publications and their Sections are each distributed per channel/store.
  This is the *background*; the specific publish-error root cause/fix is still open.

- **Logged:** 2026-07-15 (test session)
- **Scenario:** The **Publish Publications** task keeps erroring. Unhiding the
  flyer on **all** channels makes the error disappear; re-applying the
  distribution toggles (**hidden everywhere except hosted**) makes it reappear.
  Already tried: **cloning** the flyer, **re-running system tasks**, and
  **unblocking** — issue persists.
- **What the Help Center currently says:** Nearest match is
  `knowledge-base/publishing-and-go-live.md` (stuck runs / clone errors → try
  clone / re-run / unblock, then escalate to **CLSD**). There is **no entry** for
  a publish error tied specifically to a **hosted-only distribution** config, and
  no confirmed root cause/fix.
- **Confluence scan (2026-07-15):** No troubleshooting/fix doc found. Related
  **background only** (mechanics, not a fix):
  - *DVM Runbook* (RT) & *DVM Weekly Preparation Guide* (RT) — creating/publishing
    publications via Publication Builder.
  - *DVM in App Phase 1 — Post-Launch Distribution Migration Plan* (RT) — channel
    distribution & "publication explicitly hidden from that channel."
  - *Distribution Context for Shell flyers* (personal space) — distribution types.
  - *Fadmin Data Model — Flyer Publishing* — FlyerRun = one publication cycle.
  - *Old Navy Dark Week DVM Flyers* (RT) — app-only unhide/distribute runbook (a
    similar single-channel distribution setup, for reference).
- **Diagnostic clue:** Error is reproducible **only** with the hosted-only
  distribution toggle → points at the hosted/distribution config or the
  **publication mapping**, not general processing.
- **Hypotheses to test (educated, from the V2 model — NOT confirmed fixes):**
  - **Empty/invalid hosted distribution:** in V2, a publication (and each section)
    is distributed per channel to a Place/store set. Under hosted-only, verify the
    publication actually has a **valid hosted distribution target** — an empty or
    unmapped hosted Place set could be what the Publish task chokes on.
  - **Isolate the trigger:** re-apply the channel toggles **one at a time** to find
    whether it's the hosted-only state specifically (or one channel) that breaks it.
  - **Section-vs-publication distribution mismatch:** if a section's distribution
    isn't a subset of the publication's, hosted-only may create an invalid state —
    check section-level distribution against the publication's.
- **Recommended follow-up:**
  1. For live cases, escalate to **CLSD** (Content Layer service desk) and loop
     the **Hosted team (HS)**; include run ID, the exact reproduction, and steps
     already tried.
  2. When the root cause/fix is confirmed, add a section to
     `publishing-and-go-live.md` and mark this gap 🟢 Resolved.
- **Possible (unconfirmed) area:** CLSD has investigated publication-mapping data
  issues (duplicate `publication_id`s, empty publication maps) — worth checking.

---

## GAP-002 — V2 Publishing fails for one pricing zone; pipeline task errored with no logs 🟢 Resolved (guidance documented)

- **Resolved 2026-07-15 via processing-team (SME) feedback.** Documented in
  `publishing-and-go-live.md` → "V2 Publishing fails for one pricing zone (V1 still
  succeeds)" and `content-v2-and-publishing.md`. Residual open item is purely
  engineering: the *root cause* of why V2 publish fails for a zone (a CLSD matter).

- **V2 context added 2026-07-15:** `content-v2-and-publishing.md` explains the V2
  publishing flow (Fadmin → Nexus API → Item/Publication/Distribution APIs →
  Curator) and that Sections/zones are distributed independently — so a single
  zone/section failing publish is consistent with the V2 model. Still open: the
  confirmed answer to "does it block the whole flyer or just that zone's coverage?"
  and the exact re-run procedure.

- **Logged:** 2026-07-15 (test session)
- **Scenario:** **V2 Publishing** failed for **one pricing zone but not others**.
  The pipeline task shows **errored but with no logs** explaining why. User asks:
  *will the flyer still go live, and how do I re-run publishing?*
- **What the Help Center currently says:** General republish/rerun path is
  covered (`storefront-publishing-errors.md`, `publishing-and-go-live.md`,
  glossary "Republish") and stuck/errored pipelines → escalate **CLSD**. **Not
  covered:** "V2 Publishing" as a named task, **per-pricing-zone** publish
  failure, an **errored task with empty logs**, and a definitive answer to
  "**will a partial-zone failure still go live?**"
- **Working answer given (needs confirmation):** Zones that published should go
  live for their stores; the failed zone likely won't be live for the stores
  mapped to it (partial go-live). Try **republish in FADMIN** → re-run system
  tasks → clone/re-process; the no-logs error is a backend failure → **CLSD**
  (urgent if go-live close), with run ID + the specific zone.
- **Source scan:** Not yet scanned (Confluence/Slack). Likely overlaps with
  GAP-001 (V2 / publish-pipeline behavior).
- **SME-confirmed facts (2026-07-15) — corrections to the earlier educated guesses:**
  - **Go-live:** V2 failed but V1 didn't, so the zone **still went live on
    V1-powered experiences — just not V2-powered ones.** (Earlier guess "won't be
    live for its stores" was **wrong**.)
  - **Real impact:** the errored pipeline task was **blocking other flyer sessions
    from kicking off** — that's the actual urgency.
  - **Can't republish one zone** — republishing is all-or-nothing, and a **manual
    republish just repeated the error**. (Earlier "re-publish just the zone" was
    **not possible**.)
  - **Setup/diff-the-zone was NOT the culprit**, and setup is typically already
    verified before it reaches the help desk. (Earlier "diff the zone" guess was
    **off**.)
  - **Cloning:** *possibly* would resolve it, but the error might also block the
    clone — untested here. (Earlier "clone" guess was **plausible**.)
  - **UX lesson:** the "will it go live" engineer-level reasoning would **confuse a
    processor** — keep processor-facing answers at the processor's level.
  - **CLSD escalation was correct.**
- **Recommended follow-up:** Confirm with engineering/CLSD (a) whether a
  single-zone V2 publish failure blocks the whole flyer or just that zone's
  coverage, and (b) the standard way to re-run V2 publishing for one zone. Then
  add a "V2 Publishing" section to `publishing-and-go-live.md` and mark 🟢.

---

## GAP-003 — Why Fadmin doesn't always pull clean images when they're "available" 🔴 Open

- **Logged:** 2026-08-11 (test session)
- **Scenario:** "Why doesn't Fadmin always pull clean images if they are
  available?" — i.e. a clean product image is visibly present on the flyer page,
  but the item ends up with a non-clean cutout (or no clean image auto-selected).
- **What the Help Center currently says:** No dedicated image-extraction /
  Image-QC article. The answer has to be stitched together from:
  - `clipping-and-autobox.md` — covers **Item Cutout Generation failing/blocked**
    (a re-run / CLSD matter), i.e. whether a cutout generates *at all*, not the
    *quality* of what's pulled.
  - Per-retailer Image QC notes — e.g. `retailers/aldi.md` ("product images
    sometimes not clean/isolated (cutouts) because the **PDF formatting isn't
    compatible with PDF Image Extraction**"; "aim for ~100% PDF image selection");
    `retailers/dierbergs.md` (use clean PDFs; white-background cutouts OK; avoid
    dark/lifestyle backgrounds).
  - `glossary.md` — one-line "Cutout generation" definition only.
  So the KB can say *that* clean pulls depend on PDF/extraction compatibility and
  *what to do at Image QC*, but **not the mechanism**: which specific PDF
  characteristics (vector vs. rasterized/flattened, layered art, overlapping
  elements, embedded color profiles, etc.) defeat extraction, whether
  "PDF image auto-selection" has a confidence threshold, or why auto-selection
  skips a clean image that's present.
- **Source scan (2026-08-11):** No processing-side troubleshooting/mechanism doc
  found in the weekly scan window. The recurring pattern is documented only as a
  retailer-level "known recurring issue" (ALDI), framed as a **source-format
  limitation, not a processing bug**.
- **Recommended follow-up:** Get SME confirmation (processing/Image-QC or CLSD) of
  the real mechanism, then create a small **Image QC / PDF Image Extraction**
  knowledge-base article capturing: (a) why a visibly-present image may not be
  extractable cleanly (PDF-format compatibility), (b) how "PDF image
  auto-selection" decides, (c) the processor playbook (aim for ~100% PDF image
  selection, clean product image over flat-lay, same image across versions,
  white-bg cutout as fallback, no dark/lifestyle), and (d) the cutout-generation
  fail/block vs. quality distinction. Then mark 🟢 and add it to the index + KB
  bundle.

---

## Weekly-scan watchlist

Developments surfaced by the automated weekly source scan that need a **human
decision** before they change the Help Center (not auto-applied). Clear these as
you triage them.

### 2026-09-02 scan (weekly; fired 2026-08-31)
- **✅ All four sources reached** — the read-only-tool allowlist (`.claude/settings.json`,
  commit `b2e709b`) worked: Jira / Confluence / Drive are no longer approval-gated
  in the scheduled run.
- **✅ Applied — 1 additive update.** Enriched the "Ops Spotcheck opens / redirects
  to another flyer run" entry in `common-live-flyer-issues.md` with its **most common
  root cause**: when a merchant has **no Spotcheck assignment**, the task defaults to
  "Vendor 1" and misroutes FTEs → fix by adding the Spotcheck assignment at the
  **merchant level** and re-routing the run's task to the correct vendor. Source:
  `#helpme-vs` 2026-08-26 (Wholehealth Pharmacy, run 1194448) — a second instance of
  the Dunham's issue, with the underlying cause.
- **⚠️ Needs Vanessa — indexed vs. direct FSA removal.**
  [OTS-2339](https://flippit.atlassian.net/browse/OTS-2339) (Summit Tools, "no French
  version"): SME notes you **can't remove FSAs on *indexed* runs the way you can on
  *direct* runs** — the fix is to **update the indexer** to exclude the unwanted FSAs
  (e.g. Quebec) going forward. Good candidate to add to
  `missing-flyers-and-indexing.md` (Cause 2 / FSA coverage) as an indexed-vs-direct
  note routed to the indexer/FD team — held because it's a single, still-open ticket.
- **ℹ️ New OTS tickets — unresolved, no fix to capture yet (watch):**
  [OTS-2342](https://flippit.atlassian.net/browse/OTS-2342) (Pattison/Overwaitea SFTP
  syncing), [OTS-2341](https://flippit.atlassian.net/browse/OTS-2341) (Tops Friendly
  Markets), [OTS-2340](https://flippit.atlassian.net/browse/OTS-2340) (Marche C&T wrong
  dates). [OTS-2327](https://flippit.atlassian.net/browse/OTS-2327) auto-tag evidence
  log got new Giant Food / Loblaws examples — still no fix.
- **⚠️ V2-tagging / indexing-migration / Turbo themes still moving (Confluence, watch).**
  V2 Tagging Tool test plan + UI overview + "V2-only offers in search"; Crawler-API,
  Flipp Indexed Content Migration, and "Manual Indexed Flyer Ingestion Validation";
  "What is Turbo" / "DVM Flyer in Turbo". Continues the V2 (GAP-001) and
  Tesseract→bots-crawlee watch — nothing changes processing guidance yet.
- **⚠️ OneGuide re-conversion candidates (Drive, not auto-applied).** Changed in-window:
  **ALDI** (again), **Sharpe's Food Market**, **Value Grocer**, **Rouses Supermarkets**,
  **Red Apple / The Bargain Shop**. Verify each doc's own "Last Updated" before any
  rewrite — prior passes show Drive bumps are frequently metadata-only.

### 2026-08-24 scan
- **⚠️ Partial run — only Slack was reachable this pass.** The **Jira OTS,
  Confluence, and Google Drive** connectors were **approval-gated in this
  scheduled run** (no interactive approver), so they were not scanned. Re-run
  those three when the session can approve connector calls. Slack `#helpme-cxe`
  and `#helpme-vs` were scanned (08-17 → 08-24).
- **ℹ️ Nothing auto-applied.** The Slack window surfaced only **Sessions errors
  escalated to CLSD** — no self-serve fix beyond the existing "stuck sessions →
  CLSD" guidance:
  - [OTS-2337](https://flippit.atlassian.net/browse/OTS-2337) — Grocery Outlet
    (run 1223672): pipeline logs showed **"Diffing succeeded but the WES request
    to connect upstream failed"** (a GO-system run) → escalated to CPLAT via a CLSD
    ticket. Distinctive Sessions error signature; watch for recurrence / a
    documented root cause before writing an article.
  - [OTS-2338](https://flippit.atlassian.net/browse/OTS-2338) — United
    Supermarkets (run 1049580): a Sessions issue that **couldn't be unblocked on
    the CXE side** → CLSD. (A past similar case reportedly needed a backend unblock
    for a page issue.)
- **ℹ️ `#helpme-vs`:** only the Dunham's Ops Spotcheck thread (already captured as
  FB-011) plus staffing/permissions coordination (FTE trigger/Jira-filing rights,
  London Drugs task movement) — nothing new to ingest.

### 2026-08-17 scan
- **✅ Applied — 3 additive, low-risk KB updates:**
  - **Intentional de-indexing** as a "flyer not up" cause → added **Cause 5** to
    `missing-flyers-and-indexing.md` (rule out a deliberate NBD de-indexing before
    filing an FD broken-indexer ticket). Source:
    [OTS-2336](https://flippit.atlassian.net/browse/OTS-2336) (Freson Bros,
    closed — no longer indexed as an NBD strategic move: organic → promoted).
  - **`No fields to update!` item-import error** → named it in
    `item-import-format.md` as the symptom of a sub-3-column file (rule 2 + the
    common-failures table). Source: Slack `#helpme-cxe` 2026-08-12 (SKU-update
    with only `item_id` + `sku`). Confirms/extends the existing FB-007 rule.
  - **FSA count drops after a store-code/store change** → added an entry to
    `stores-and-harmonization.md`: bulk-recreated stores with **inaccurate
    lat/longs** shrink the FSA-generation area; fix the lat/longs and re-run FSA
    generation. Source: Slack `#helpme-cxe` 2026-08-11 (Princess Auto, resolved).
- **ℹ️ Closed OTS with no documented resolution (nothing to capture):**
  [OTS-2335](https://flippit.atlassian.net/browse/OTS-2335) "expired flyer still
  live (Foody Mart)" moved to Done with **no resolution comment**. Watch for
  recurrence; if it repeats with a fix, add an expired-still-live entry to
  `flyer-dates.md` / `publishing-and-go-live.md`.
- **ℹ️ [OTS-2327](https://flippit.atlassian.net/browse/OTS-2327) auto-tag tracking
  ticket — still open, no fix.** New in-window examples (Dollar General
  "inappropriate word" 08-10; M&M Food Markets wrong prices/prefix 08-12). **SME
  note (08-12):** some of these are auto-tag transcribing text *correctly* but
  **picking the wrong option** — that's a **Vendor QC miss (file vendor feedback),
  not an auto-tag bug.** Keep as an evidence log; no KB change yet.
- **⚠️ Confluence "Unify Flyer Ingestion (🕷️Crawler-API) — Delivery Plan" (space
  CTLR).** New microservice unifying crawled-flyer ingestion across Flipp /
  Shopfully / Offerista (validates crawled content, adds flyers to Fadmin via the
  Flyer API). Extends the indexing-migration theme already tracked (GAP-001;
  Tesseract→bots-crawlee). **Decision:** watch for when it changes indexing/ingestion
  behavior, then update `missing-flyers-and-indexing.md` / glossary.
- **⚠️ OneGuide re-conversion candidates carried forward (still NOT auto-applied).**
  From the 08-11 scan: **Kroger, Pharmachoice & RxHealthMed, Familiprix 2.0,
  Timber Mart 2.0.** ALDI OneGuide 2.0 shows another Drive "modified" bump
  (2026-08-11) — prior passes show these are frequently metadata-only, so verify
  each doc's own "Last Updated" before any rewrite. Contacts still omitted.
- **ℹ️ Sources reached this run:** Jira OTS ✓ · Confluence ✓ · Slack `#helpme-cxe`
  ✓ (`#flex-processingsupport` returned no messages in-window) · Google Drive ✓.

### 2026-08-11 scan
- **ℹ️ Nothing auto-applied this scan.** No closed OTS tickets with documented
  resolutions, and no new Slack/Confluence processing fixes. The Slack scan only
  re-surfaced the Item Cutout Generation / blank-Name thread already captured in
  the 2026-07-27 scan. (The 08-10 pass just below already re-verified the ALDI /
  PetSmart Canada / Dierbergs OneGuides and applied the JYSK / OTS-2334 note.)
  Everything below is watch/flag only.
- **⚠️ More OneGuides refreshed on Drive (08-11) — re-conversion candidates (NOT
  auto-applied; full-guide rewrites aren't low-risk).** Changed *after* the 08-10
  re-conversion pass: **Kroger** (2026-08-11), **Pharmachoice & RxHealthMed**
  (2026-08-11), **Familiprix 2.0** (2026-08-11), **Timber Mart 2.0** (2026-08-11).
  (ALDI 2.0's 2026-08-04 touch was already covered by the 08-10 pass — no material
  change.) **Decision:** schedule a re-conversion check for these four; prior
  passes show Drive "modified" bumps are frequently metadata-only, so verify each
  doc's own "Last Updated" before rewriting. Contacts still omitted.
- **ℹ️ New OTS tickets — unresolved, no fix to capture yet (watch for resolution):**
  - [OTS-2335](https://flippit.atlassian.net/browse/OTS-2335) — "expired flyer
    still live (Foody Mart)" (created 08-09, untriaged). Distribution/expiry
    visibility; watch for the root cause.
  - [OTS-2327](https://flippit.atlassian.net/browse/OTS-2327) — Enablement
    auto-tag issue **tracking** ticket; new examples in-window (Stop & Shop
    phantom original price 07-28; Dollar General "inappropriate word" 08-10).
    Ongoing evidence log for the known auto-tag hallucination problems — no fix yet.
  - [OTS-2334](https://flippit.atlassian.net/browse/OTS-2334) (Jysk tagging-blocked)
    was addressed in the 08-10 pass via the JYSK FR-URL risk-item note in `jysk.md`.
- **⚠️ V2 tagging / V1 deprecation movement (Content Layer).** "V2 Tagging Tool —
  Manual Test Plan" and "CDIS-4467 Parity Scope: Phase 2 Decisions" (V1
  `flipp-search` → V2 Curator interface parity, staged rollout starting with ecom
  items), plus a "V1 Deprecation" caller-inventory page and a "Legacy Crawler-php
  Consolidated Discovery Report." Extends the V2 / indexing-migration themes
  already tracked (GAP-001; 2026-07-22 Tesseract→bots-crawlee). Watch for when
  these actually change tagging or indexing behavior.
- **⚠️ New CXE source — "Content Classification SOP (Primary vs Secondary)"** (space
  XPTCXE / Client Experience and Enablement — a **team space**, updated ~2026-08-10):
  classification rules + escalation path for primary vs secondary content.
  **Decision:** candidate to ingest — overlaps our existing secondary-publication
  toggle guidance (e.g. `dierbergs.md` ad-hoc runs), so review before it changes
  existing content.
- **⚠️ Additional OneGuide refreshed on Drive (08-11):** **M&M Food Market 2.0**
  (in addition to the Kroger / Pharmachoice & RxHealthMed / Familiprix / Timber Mart
  list above). Same re-conversion-candidate handling — verify the doc's own "Last
  Updated" before rewriting.
- **ℹ️ Whole Foods Market US onboarding on DVM** (space CustomerSuccess, ~2026-08-10):
  net-new retailer Production SOP / Technical Setup / DVM Implementation. **Decision:**
  watch; may warrant a retailer guide once it goes live.

### 2026-08-10 scan
- **✅ OneGuide re-conversion pass (ALDI, PetSmart Canada, Dierbergs).** Re-read all three
  live OneGuides against our guides. **No material content changes** since the last conversion —
  the Drive "modified" timestamps (Aug 4–7) were metadata/re-share touches; the docs' own
  "Last Updated" dates are unchanged (ALDI Oct 6 2025; Dierbergs Jun 1 2026; PetSmart Canada
  matches). Re-verified and stamped `Last reviewed: 2026-08-10`. One genuine gap fixed: added
  **Flyer Review type: Simple** to `aldi.md` (was missing). Contacts/credentials still omitted.
  This clears the carried re-conversion watchlist item.
- **✅ Applied — JYSK FR-URL manipulation lesson** (source: `#helpme-cxe`,
  [OTS-2334](https://flippit.atlassian.net/browse/OTS-2334)). Skipping the French
  `&___store=fr` URL manipulation — or QC'ing against the *raw* links doc instead of the
  manipulated version — causes upload/save failures. The manipulation itself was already
  documented in `jysk.md`; added it as an explicit **risk item** with the ticket reference.
- **TE Hosted/integration troubleshooting SOP** — re-checked: still a **personal-space draft**
  (not moved to a team space), so still **held** per the publish-first rule. Not ingested.

### 2026-07-27 scan
- **✅ Applied:** Item Cutout Generation erroring on items with a **blank Name**
  (auto-tag had no text to pull) → added a fix to `clipping-and-autobox.md`
  (source: `#helpme-cxe` 2026-07-27).
- **⚠️ New development — Turbo flyer-curation automation.** Confluence
  "Automating Flyer Curation in Turbo" (requirements draft): curating a flyer
  automatically from an uploaded curation sheet, per-section rules. Forward-
  looking; watch for when it lands and changes the curation workflow.
- **Still-open watchlist items (carried from 2026-07-22), now with movement:**
  categorization epic now has a solution-design doc (**CDIS-4314**); the **TE
  Hosted/integration troubleshooting SOP** is still a personal-space draft (has
  grown — candidate to ingest into `hosted-and-previews.md` once finalized);
  **OneGuides/production SOPs refreshed** (ALDI 2.0, FreshCo, others) — 🟢
  **Resolved** by the 2026-08-10 re-conversion pass (ALDI / PetSmart Canada /
  Dierbergs re-verified — no material changes; see the 2026-08-10 scan). FreshCo
  is a CS-side production SOP (not a OneGuide Google Doc) → out of scope.
- **ℹ️ No new OTS tickets** in the window; the CTLR "Content Sieve unpublished
  items" alert runbook was touched but we already cover it in `alert-runbooks.md`.

### 2026-07-22 scan
- **⚠️ Indexing migration (Tesseract/flyer-indexing → bots-crawlee).** Confluence
  "Flipp Indexed Content Migration Delivery Plan" (space CTLR): ~130 Premium /
  select Top-50 merchants are being migrated off the legacy **Tesseract**
  indexer to **bots-crawlee**. Our `missing-flyers-and-indexing.md` and glossary
  still describe Tesseract as the indexer. **Decision:** treat like the V2 shift
  — worth a short "how indexing is changing" note / new article once the
  migration behavior is confirmed. Not yet applied (in-progress plan).
- **🟢 OneGuides refreshed on Drive — RESOLVED (2026-08-10).** ALDI "OneGuide 2.0"
  (2026-07-15), PetSmart Canada (2026-07-22), Dierbergs (2026-07-22) were updated.
  Our `docs/retailers/` guides were converted from earlier versions. **Resolution:**
  the 2026-08-10 re-conversion pass re-read all three live OneGuides against our
  guides — **no material content changes** (Drive "modified" bumps were metadata/
  re-share touches; the docs' own "Last Updated" dates were unchanged). Re-verified
  and stamped `Last reviewed: 2026-08-10`; added the missing **Flyer Review type:
  Simple** to `aldi.md`. Bundles `retailers-A/-D/-P` regenerated. Contacts omitted.
- **⚠️ TE Hosted/integration troubleshooting SOP.** A "TE Troubleshooting SOP for
  Common Hosted and Integration Issues" (draft, personal space) covers Hosted,
  integration, store-selection, print, feed, and shoppability triage. **Decision:**
  candidate source to ingest into `hosted-and-previews.md` once it's finalized /
  moved to a team space.
- **⚠️ Categorization Productionization epic** (Data Science): categorization
  model/stack rework. **Decision:** watch for impact on the auto-categorization
  guidance in `common-live-flyer-issues.md`.
- **ℹ️ OTS-2283 "Flyer Tile Generation Failure: Error: Killed"** closed **with no
  documented resolution/comments** — no fix to capture. Watch for recurrence; if
  it repeats with a resolution, add the "Error: Killed" variant to the tile-gen
  guidance.

---

## Entry template (copy for new gaps)

```
## GAP-00X — <short title> 🔴 Open
- **Logged:** YYYY-MM-DD
- **Scenario:** <what was asked / the symptom>
- **What the Help Center currently says:** <nearest article + why it's insufficient>
- **Source scan:** <Confluence/Jira/Slack findings, or "not yet scanned">
- **Recommended follow-up:** <escalation + what article to add when resolved>
```
