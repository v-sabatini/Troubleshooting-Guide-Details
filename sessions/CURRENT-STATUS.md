# CURRENT STATUS — Flyer Processing Troubleshooting KB

> **This is the single, always-current snapshot.** Read this first to resume —
> you don't need to read the individual session logs unless you want detail.
> **Last updated: 2026-07-14 (end of session 3).**

---

## What this project is

A curated **knowledge base** (clean Markdown in this GitHub repo) that will power
a **chatbot to help the flyer-processing team troubleshoot issues and errors** —
prototyped in Claude now, to be **migrated into NotebookLM** later.

- **Repo:** `troubleshooting-guide-details`
- **Branch:** `claude/flyer-chatbot-knowledge-base-yhsxxb`
- **Sources approved:** Confluence + Jira (`flippit.atlassian.net`), Google Drive, Slack.

## How to resume (do this first)

1. Open `sessions/prompts.md` and paste the **Resume prompt** into a new session.
2. Confirm today's focus (see **Next steps** below).
3. Wrap up by pasting the **Wrap-up prompt** so this file + a session log get updated.

---

## What exists now (13 KB articles + scaffolding)

**Knowledge base — `docs/knowledge-base/`:**
1. `flyer-processing-overview.md` — how flyers get processed; where things break.
2. `codesheet-errors.md` — NilClass, file-not-picked-up, config/word-bank (from old TOSS tickets + guide).
3. `missing-flyers-and-indexing.md` — broken indexer→FD, FSA/coverage, geo-targeting.
4. `clipping-and-autobox.md` — unclippable items, AutoBox re-run, cutouts.
5. `stores-and-harmonization.md` — harmonization, lat/long, duplicate stores.
6. `flyer-dates.md` — wrong/expired/invalid valid dates (FADMIN fixes).
7. `hosted-and-previews.md` — preview links, iframe, cropped pages (→ HS/Hosted).
8. `publishing-and-go-live.md` — stuck runs, cloning, FQC, front-end display.
9. `common-live-flyer-issues.md` — quick reference (from `#helpme-ops`).
10. `storefront-publishing-errors.md` — storefront load errors / republish.
11. `escalation-and-tickets.md` — where to ask, which team, how to file.
12. `post-escalation-what-happens-next.md` — FD/CLSD/MSC + turnaround expectations.
13. `glossary.md` — all terms/acronyms.

**Supporting:** `docs/00-index.md` (master index), `docs/templates/kb-article-template.md`,
`sources/source-map.md` (provenance), `sources/ots-ticket-inventory.md` (381-ticket
analysis), `README.md`, `NOTEBOOKLM.md` (migration guide), `sessions/prompts.md`
(copy-paste prompts), `sessions/logs/` (per-session detail).

## Coverage status

| Area | Status |
|---|---|
| Codesheet errors | ✅ |
| Flyer processing overview / ops | ✅ |
| Missing flyers / indexing / coverage | ✅ (from 381 OTS tickets) |
| Clipping / AutoBox | ✅ |
| Stores / harmonization | ✅ |
| Flyer dates | ✅ |
| Hosted / previews | ✅ |
| Publishing / go-live / front-end | ✅ |
| Storefront / publishing | ✅ |
| Escalation + post-escalation (FD/CLSD/MSC) | ✅ (with turnaround estimates) |
| **Processing Support (ClickUp)** | ⬜ **Not yet ingested — current source of truth for PS process** |
| Data piping | ⬜ Deferred (out of first scope) |

---

## Key facts to remember

- **Atlassian:** `flippit.atlassian.net`, cloud ID `5d9c002c-b1cd-47a5-95ba-2565ccb0e5f8`.
- **OTS = Ops Troubleshooting** (project `OTS`, board 315) — the front-line help
  desk. We ingested **381 tickets (Jan 2024–Jul 2026)**. Old **TOSS** project is
  retired (backs only the codesheet article).
- **Escalation routing:** broken indexer → **FD**; content-platform / pipeline /
  cloning (WES) / categorization / harmonization *fix* → **CLSD**; Foursquare
  measurement / store-trip → **MSC**; hosted/front-end → **HS**; third-party app →
  account team (**DOC**).
- **"PIA" is not a project** — `PIA-####` links resolve to **`MSC-####`** (Marketing
  Science). Harmonization *fixes* happen in CLSD.
- **Enablement pod (CXE)** absorbed the former Skeleton Team; reachable at
  `@enable-cxe` in `#helpme-ops`. (You, Vanessa, are on it.)
- **Processing Support KB (Confluence) is retired (Jun 2026)** → current source of
  truth is the **Processing Support ClickUp space** (not yet ingested).

## Conventions / decisions

- Article shape: **symptom (exact error text) → cause → fix → escalate → source.**
- Keep error strings **verbatim**; **one self-contained topic per file** (best for
  NotebookLM); **every claim cited**; plain language for a new processor.
- Large Jira boards are **sampled** (transparently), not exhaustively ingested.

---

## Next steps (priority order)

1. **Subject-matter review** by Vanessa — spot-check the articles for accuracy,
   especially escalation destinations and the post-escalation turnaround framing.
2. **Ingest the Processing Support ClickUp space** (the current source of truth for
   PS process) — carried over from sessions 1–3. *(Use the Add-a-Source prompt.)*
3. **Optional deep dives:** theme-level CLSD articles (categorization gaps,
   cloning/WES errors); retailer-specific quirks; confirm whether **HTS** is still
   an active harmonization queue.
4. **Refresh cadence:** re-run the OTS pull periodically (e.g. monthly) with the
   Gap-Check prompt to catch new recurring issues.
5. **When coverage feels solid:** run the **NotebookLM-prep prompt** (`NOTEBOOKLM.md`)
   and do a test upload with real questions.

---

## Session history

- **Session 1** (`logs/2026-07-14-session-01.md`) — set up repo + first KB from
  Confluence/Slack + prompt system.
- **Session 2** (`logs/2026-07-14-session-02.md`) — ingested 381 OTS tickets → 6
  new articles + inventory.
- **Session 3** (`logs/2026-07-14-session-03.md`) — ingested FD/CLSD/MSC
  post-escalation boards + fixed the PIA→MSC routing.
