# Storefront & Publishing Errors — Troubleshooting Guide

> **What this covers:** How to triage Storefront load failures and
> publishing/republish issues. Grounded in the "How to troubleshoot Storefront
> errors" runbook (Confluence, space QKB) and the Live Flyer Check alert runbook
> (space CTLR).
>
> **Note on audience:** This area is more engineering / on-call oriented than
> codesheet or day-to-day processing. Some steps require VPN, SSO, and access to
> Datadog, Databricks, and Lenses. If you don't have that access, your job is to
> **identify and clearly report** the affected merchant / flyer run, then hand
> off. See `escalation-and-tickets.md`.

---

## Problem: "Storefront errors exceed healthy threshold"

**Symptom / how it shows up:**
- A **Datadog alert**: *Storefront errors exceed healthy threshold* — meaning
  storefronts are failing to load for one or more merchants.
- Teams reporting in Slack that a storefront won't load.

**Goal of troubleshooting:** find the **affected merchant** and **flyer run ID**,
then decide whether a **republish** is needed.

### Step-by-step

1. **Check `#sf-auditor-alerts` in Slack.** This channel reports publications
   that were expected but haven't published yet.
   - If there's an issue, it reports the `flyer_id` and `flyer_run_id`, in a path
     like `storefronts/v2/<flyer_run_id>/<flyer_id>/...`.
   - If all is well, you'll see: `Audit completed. 0 inaccessible publications found.`

2. **Find the Merchant ID:**
   - Fastest: use the Datadog **App Storefront Errors** monitor/dashboard to see
     which merchant has the most errors (narrow the time window as needed).
   - Alternative: the **Databricks** dashboard (second table) — you may need to
     set the interval to the last 12 hours (Databricks has ingestion lag) and
     ensure the data is refreshed.
   - Whichever merchant shows the highest error count is your prime suspect.

3. **Query beacons in Lenses (Production):** (requires VPN + SSO)
   - Go to <https://lenses.flipp.com/> → Explore.
   - Query beacon `Beacon.FlippApp.StorefrontZeroCaseError`, filtered by the
     `merchantId` from step 2. Example:
     ```sql
     USE `kafka`;
     SELECT *
     FROM Beacon.FlippApp.StorefrontZeroCaseError
     WHERE merchant.merchantId = "2178"
       AND _meta.timestamp > now() - (1hour)
     LIMIT 100;
     ```
   - Switch to Table view. In the error-details column you may see
     `Unable to retrieve SFML error 1`.

4. **Narrow to a flyer run / flyer:** find the specific flyer run or flyer with
   the most errors. Reproduce it on your device using the associated **postal
   code** (available as a column in the query results).

5. **Decide on a republish:** once the `flyer_run_id` is isolated, coordinate
   with the team on whether a **republish on FADMIN** is required.

**Need historical data?** Use the Databricks **Storefront 0 Case Notebook** —
enter the `merchant_id` in the Retailer field, run it, and see "Output 3:
Selected merchants" for the total error count and flyer IDs.

---

## Live Flyer Check (alert runbook)

**Symptom:** an alert that a live flyer isn't behaving — not opening, missing
thumbnails, or not fully processed.

**Common root causes seen in the runbook:**
- **Flyer wasn't finished processing** → message `#content-public` to complete /
  republish.
- **Flyer thumbnails don't exist** in the `Flyers.Thumbnails` topic → message
  `#content-public` to republish the flyer.

**Actions:**
- Check the flyer IDs in the pricing zones for errors on the merchants flyer-runs
  admin.
- Trigger a **republish flyer run** when processing didn't complete or thumbnails
  are missing.

---

## When to escalate

- If you don't have Datadog / Databricks / Lenses access, report the **merchant
  ID and flyer run ID** (and, if you have it, the beacon error detail) to the
  content/on-call team via the appropriate channel and file a **CLSD ticket** if
  it's blocking go-live.
- Storefront-wide failures affecting many merchants are a production incident —
  escalate immediately rather than working ticket-by-ticket.

---

*Sources: Confluence "How to troubleshoot Storefront errors" (QKB, 11540496444);
"Alert Runbook: Live Flyer Check" (CTLR, 11691786294). See
`sources/source-map.md`. Last reviewed: 2026-07-14.*
