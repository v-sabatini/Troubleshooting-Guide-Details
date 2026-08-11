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

## Weekly-scan watchlist

Developments surfaced by the automated weekly source scan that need a **human
decision** before they change the Help Center (not auto-applied). Clear these as
you triage them.

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
  **OneGuides/production SOPs refreshed** (ALDI 2.0, FreshCo, others) — still a
  re-conversion candidate.
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
- **⚠️ OneGuides refreshed on Drive.** ALDI "OneGuide 2.0" (2026-07-15),
  PetSmart Canada (2026-07-22), Dierbergs (2026-07-22) were updated. Our
  `docs/retailers/` guides were converted from earlier versions. **Decision:**
  schedule a re-conversion pass for changed OneGuides (contacts still omitted).
  Not auto-applied — full-guide rewrites aren't low-risk.
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
