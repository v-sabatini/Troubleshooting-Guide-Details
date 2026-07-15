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

## GAP-002 — V2 Publishing fails for one pricing zone; pipeline task errored with no logs 🟡 Investigating

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
- **Hypotheses to test (educated, from the V2 model — NOT confirmed fixes):**
  - **Re-publish scoped to the failed section/zone:** V2 sections/zones distribute
    independently, so try re-triggering publish for just that zone rather than the
    whole run.
  - **Diff the failing zone vs. a good one:** the zone-specific difference
    (distribution/store mapping, dates, pages, or a missing attribute) is the
    likely culprit for a per-zone publish failure.
  - **Clone / re-process for a fresh pipeline run:** may surface logs the errored
    task didn't emit (the run flows Fadmin → Nexus API → Item/Publication/
    Distribution APIs → Curator; a fresh run can re-emit at a stage that logged).
  - **Will it go live? (educated):** zones that reached Curator should serve their
    stores; the failed zone likely **won't** be live for its stores until it
    re-publishes → **partial go-live** is the probable outcome. Confirm before
    promising the retailer.
- **Recommended follow-up:** Confirm with engineering/CLSD (a) whether a
  single-zone V2 publish failure blocks the whole flyer or just that zone's
  coverage, and (b) the standard way to re-run V2 publishing for one zone. Then
  add a "V2 Publishing" section to `publishing-and-go-live.md` and mark 🟢.

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
