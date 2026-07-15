# Home Depot Canada DVM Module — On-Call Runbook

> **What this covers:** On-call troubleshooting for the **Home Depot Canada
> (HDCA) DVM module** — daily feed ingestion, DVM rendering, and the recurring
> late-feed incident pattern. Source Confluence page ids: 13565427824 (space RT,
> "Playbooks to troubleshoot issues" — an empty index/parent page) and its child
> 13564379282 ("Home Depot Canada DVM Module — On-Call Runbook"), which holds the
> actual content.
>
> **Audience:** On-call engineers / content-feeds support.
> **Escalation path:** See the escalation steps below and
> `escalation-and-tickets.md`.

---

## Overview

The HDCA DVM module delivers dynamically rendered promotional content on Flipp's
**Hosted** and **App** channels. Two phases:

- **Phase 1 – Top Offers:** live since **March 26, 2026** (Hosted).
- **Phase 2 – Weather Signals:** live since **April 16, 2026** (Hosted & App).

Data flows daily: **retailer-supplied local feed → AMP Production ingestion → DVM
rendering.** Hourly audits post to **#dvm-rendering-incidents**; feed ingestion
failures surface in **#content-feeds-support** via Datadog alerts. Project
channel: **#thdca-dvm**.

## Module schedule (times EST)

| Job | Scheduled time | Notes |
|---|---|---|
| PRODUCT ingestion | ~10:10 AM | Must complete before OFFERS |
| OFFERS ingestion | ~10:30 AM | Depends on PRODUCT run |
| Feed file expected | ~10:00–10:15 AM | Late delivery is the #1 cause of incidents |
| Audit checks | Hourly | Results post to #dvm-rendering-incidents |

## Monitoring & alerts

| Signal | Channel | Meaning |
|---|---|---|
| Datadog alert fires | #content-feeds-support | Feed ingestion failed or feed file not received |
| Audit check fails | #dvm-rendering-incidents | Module has missing or 0 offers; may indicate ingestion didn't run |

---

## Troubleshooting playbook

### Step 1 — Identify the alert

Check **#dvm-rendering-incidents** for hourly audit failures and
**#content-feeds-support** for Datadog feed ingestion alerts tagged to HDCA.

### Step 2 — Check if the feed file was delivered

- **Symptom:** Audit failing / module showing missing or 0 offers.
- **Most common root cause:** HDCA delivered the feed file **after** the
  ingestion scheduler already ran (file expected by ~10:00–10:15 AM EST).
- **Actions:**
  - Check whether the feed file exists in the expected **S3 location** (ask
    content-feeds support or AMP engineering if you lack AWS access).
  - If the file is **not yet present:** wait and monitor; ping the Partner
    Technology Manager or the HDCA contact if it is more than **2 hours late**.
  - If the file **is present but ingestion didn't pick it up:** go to Step 3.
- **Known pattern:** HDCA often uploads after the scheduled ingest time (10:47 AM
  observed on May 28, 2026). The job has already run and missed the file — a
  **manual re-run** is required.

### Step 3 — Manually restart ingestion

In **#content-feeds-support**, tag **@amp-prod-eng** (or the AMP feed-ingestion
engineers):

1. Restart **PRODUCT ingestion** first.
2. Once PRODUCT completes, restart **OFFERS ingestion**.
3. Confirm the feed configs are re-run (reply to the Datadog alert thread with
   confirmation).

### Step 4 — Verify the module is live

After ingestion completes, check the **next hourly audit** in
**#dvm-rendering-incidents** to confirm the module is populating with offers. You
can also verify via the module URL / test environment.

### Step 5 — Check the module schedule

If the module should be live but isn't, verify the current flyer-run dates and
schedule on the **DVM Partner: Home Depot CA Modules** page (Confluence RT
13052313621). The module is only live during **active flyer periods** — expired
offers won't show even if ingestion is healthy.

> **Note:** If the module is currently **not scheduled to be live** (between
> flyer runs), missing offers have **no user impact**. Confirm before escalating
> externally.

### Step 6 — Escalate if unresolved

1. Summarize what was tried in **#thdca-dvm** and tag the **Partner Technology
   Manager**.
2. Loop in the **Engineering Manager** if engineering investigation is needed.
3. If HDCA data is the issue **and** the module is live, have **Customer Success**
   reach out to the HDCA contact.

---

## Recurring pattern & past incidents

The predominant root cause across all recorded incidents is **late feed file
delivery by HDCA**. Files are expected before ~10:15 AM EST but have arrived as
late as 10:47 AM or not at all. The AMP team is investigating a longer-term
**event-driven ingestion trigger** (vs. fixed schedule) to address this.

Representative incidents (all resolved when files arrived or after a manual
re-run):

- **Jun 1–2, 2026:** Feed not received; module between flyer runs (no live
  impact). Arrived Jun 2, re-ran at the 10:30 window.
- **May 28–29, 2026:** Files arrived 10:47 AM after schedulers (10:10 / 10:30)
  had run; engineering **manually restarted PRODUCT and OFFERS ingestion**.
- **May 19 / Apr 14–15 / Mar 29–31 / Mar 21 / Mar 13 / Mar 10, 2026:** Datadog
  alerts from late/missing files; resolved when files appeared. (Apr 14–15 had a
  secondary issue: on-call engineer's **AWS access had changed**, blocking initial
  investigation.)

---

## Useful links

- **DVM Partner: Home Depot CA Modules** (Confluence RT 13052313621) — schedule,
  scope, contacts.
- **PPP-1119** — feed ingestion ticket (AMP/CCOL).
- **DR-358 / DR-280** — DVM Rendering epics.
- Channels: **#content-feeds-support**, **#dvm-rendering-incidents**,
  **#thdca-dvm**.

---

## See also

- `home-depot-us-troubleshooting.md` — HDUS flyer pipeline errors.
- `escalation-and-tickets.md` — escalation and ticketing.

---

*Source: Confluence "Playbooks to troubleshoot issues" (RT, 13565427824) and its child "Home Depot Canada DVM Module — On-Call Runbook" (RT, 13564379282). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
