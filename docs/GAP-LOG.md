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

## GAP-001 — "Publish Publications" errors under hosted-only distribution 🔴 Open

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
- **Recommended follow-up:**
  1. For live cases, escalate to **CLSD** (Content Layer service desk) and loop
     the **Hosted team (HS)**; include run ID, the exact reproduction, and steps
     already tried.
  2. When the root cause/fix is confirmed, add a section to
     `publishing-and-go-live.md` and mark this gap 🟢 Resolved.
- **Possible (unconfirmed) area:** CLSD has investigated publication-mapping data
  issues (duplicate `publication_id`s, empty publication maps) — worth checking.

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
