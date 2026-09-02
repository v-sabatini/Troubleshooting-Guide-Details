# 🗒️ Sticky-note: making the automatic scans lighter

**What this is:** a ready-to-go plan to reduce how much the automatic scans weigh on
Vanessa's computer. Nothing here is done yet except item 0. The rest has to be done
from a **normal (interactive) Claude window** — see "Why not now?" at the bottom.

---

## The plain-English version

A little robot does two automatic jobs: a **quick peek** for reviewer notes, and a
**weekly look-around** of the helper apps (Jira, Confluence, Slack, Google Drive).
It runs in the cloud, not on your computer — but your computer has to hold the
**one giant notebook** it keeps writing in, and that notebook has grown for weeks.
That heavy notebook is what makes the computer feel slow. Three fixes:

1. **Fresh notebook each time** — every run starts small instead of piling onto one
   endless conversation.
2. **Peek less often** — the "any notes?" check runs every few hours today; once a
   day is plenty.
3. **Look in fewer rooms** — the weekly look-around searches too widely and drags
   back big piles; point it at the rooms that actually matter.

You can also just **close the tab** — the robot keeps working without you watching.

---

## 0. ✅ Already done
- `.claude/settings.json` (commit `b2e709b`) pre-approves the **read-only** scan
  tools so scheduled runs stop getting blocked by approval prompts. Because it's
  committed to the branch, any fresh scan session picks it up automatically.

## 1. Fresh session per run  (the big RAM win)
Recreate both scheduled routines so each firing **spawns a new session**
(`create_new_session_on_fire: true`) instead of resuming this one forever.
- Weekly scan routine — `trig_01Pe8qut4Y7LCpWwSYKRdXu1` ("CXE Help Center — weekly source scan")
- Feedback-check routine — `trig_01RExVR8zQoTkVH37ieD1ivc` ("Process CXE Help Center feedback log")

How: `list_triggers` (copy each one's exact cron + prompt) → `create_trigger` with
the same prompt/schedule **plus** `create_new_session_on_fire: true`, and for the
weekly scan add `connectors: ["Atlassian", "Slack", "Google Drive"]` → then
`delete_trigger` the old one (delete last, after the new one is confirmed).

⚠️ **Heads-up:** with fresh sessions, each run's summary no longer lands in this
chat — it comes back through the routine's completion notification (push/email).
The feedback check stays silent when there's nothing new, same as today.

## 2. Peek less often
- **Feedback check:** change from ~every 4 hours to **once a day** (suggest ~21:00
  UTC / ~5 pm ET, after reviewers have logged during the day). Cron: `0 21 * * *`.
- **Weekly scan:** keep weekly (Mondays) — that cadence is fine.

## 3. Trim the weekly look-around
Edit the weekly-scan routine's prompt so the queries are narrower:
- **Confluence:** scope to the relevant spaces instead of an org-wide `text ~ "flyer"`
  search — e.g. `space in (CTLR, RT, VEN, CP, CS)` with tighter terms
  (codesheet / QC / OneGuide / publishing). Cuts a ~30-page noisy result to a handful.
- **Google Drive:** make it lean — `excludeContentSnippets: true`, small `pageSize`,
  or downgrade to a lightweight "did any OneGuide's "Last Updated" change?" check,
  since OneGuide re-conversions are flagged for a human, not auto-applied. (One recent
  Drive result came back at 162 KB — that's the kind of pile to avoid.)
- **Slack:** leave `#helpme-cxe` and `#helpme-vs` as-is — highest signal, small output.

---

## 4. Fold ClickUp into the weekly scan
Read-only ClickUp tools are already pre-approved in `.claude/settings.json`, and the
boards are registered in `sources/source-map.md`. The remaining step is to **add
ClickUp to the weekly-scan trigger prompt** so it's swept automatically — scan the
**VSM – Adhoc Relief Board → `ARBoard`** (single-executor/FMQ retailer relief) and
**CXE – Enablement Project Space → `Projects`/`Collaboration`**, applying the same
"resolved error→fix patterns only, contacts omitted, ingest selectively" bar as
`#helpme-vs`. This edits the trigger prompt, so it needs an interactive session (see
below).

## Why not now?
Items 1–3 all change the scheduled **routines**, and the routine-management tools are
**approval-gated** in the automatic (remote) session — the "yes" can't be given from
there. They need a **normal interactive Claude window** on the computer. From one of
those, just say *"do the scan cleanup"* and all of the above can be applied in one pass.
