# Flyer Processing Troubleshooting — Knowledge Base Index

This is the master map of the knowledge base that powers the Flyer Processing
Troubleshooting chatbot. Each article is self-contained so it can be uploaded to
NotebookLM (or read by Claude) as an individual source.

## How to use this knowledge base

- **A processor with an error** → find the matching article below, paste the
  exact error text, follow the self-serve steps, and escalate if needed.
- **The chatbot** → treat each article as authoritative for its area; always
  prefer the exact error strings and cite the source article.

## Articles

| # | Article | Use it when… |
|---|---|---|
| 1 | [Flyer Processing Overview](knowledge-base/flyer-processing-overview.md) | You need the big picture of how flyers get processed and where things break. |
| 2 | [Codesheet Errors](knowledge-base/codesheet-errors.md) | A codesheet won't process, errors with `NilClass`, or files aren't picked up from the FTP. |
| 3 | [Missing Flyers, Indexing & Coverage](knowledge-base/missing-flyers-and-indexing.md) | A flyer/pages are missing, a broken indexer, missing FSA/postal coverage, or a region sees the wrong flyer. |
| 4 | [Clipping, AutoBox & Cutouts](knowledge-base/clipping-and-autobox.md) | Items aren't clippable, boxes are off-center, or cutout generation is failing. |
| 5 | [Stores & Harmonization](knowledge-base/stores-and-harmonization.md) | Store harmonization failures/audits, duplicate/missing stores, or add-store errors. |
| 6 | [Flyer Dates](knowledge-base/flyer-dates.md) | Wrong/expired/invalid valid dates, or a live flyer reading as expired. |
| 7 | [Hosted Sites & Preview Links](knowledge-base/hosted-and-previews.md) | Preview links or the hosted/iframe experience aren't working or render cropped. |
| 8 | [Publishing, Go-Live & Front-End Display](knowledge-base/publishing-and-go-live.md) | A flyer is stuck before go-live, pipelines/clones stuck, or prices/items not showing on the front-end. |
| 9 | [Common Live-Flyer & Processing Issues](knowledge-base/common-live-flyer-issues.md) | Quick reference (from `#helpme-ops`): tile-gen, image import, categorization, masthead. |
| 10 | [Storefront & Publishing Errors](knowledge-base/storefront-publishing-errors.md) | Storefronts failing to load, missing thumbnails, or republish decisions. |
| 11 | [Escalation & Ticketing](knowledge-base/escalation-and-tickets.md) | You've tried self-serve and need to know where to ask, which team, or how to file a ticket. |
| 12 | [Glossary](knowledge-base/glossary.md) | You hit an unfamiliar term or acronym (PZ, FADMIN, OTS, FD, PIA, FSA, AutoBox, etc.). |

> **New in session 2:** Articles 3–8 are grounded in **381 real Ops
> Troubleshooting (OTS) tickets** (Jan 2024–Jul 2026). See
> [`sources/ots-ticket-inventory.md`](../sources/ots-ticket-inventory.md).

## Supporting material

- [KB Article Template](templates/kb-article-template.md) — use this to add new
  articles consistently.
- [Source Map](../sources/source-map.md) — provenance for every article.
- [OTS Ticket Inventory](../sources/ots-ticket-inventory.md) — categorized
  analysis of 381 Ops Troubleshooting tickets + escalation routing.
- [Session Prompts](../sessions/prompts.md) — copy-paste prompts to resume/wrap
  up working sessions.
- [Session Logs](../sessions/logs/) — what was done each session + next steps.

## Coverage status

| Area | Status |
|---|---|
| Codesheet errors | ✅ First version (10 real tickets + guide) |
| Core flyer processing / ops | ✅ Overview + urgent processing |
| Missing flyers / indexing / coverage | ✅ From 381 OTS tickets |
| Clipping / AutoBox | ✅ From OTS tickets |
| Stores / harmonization | ✅ From OTS tickets |
| Flyer dates | ✅ From OTS tickets |
| Hosted / previews | ✅ From OTS tickets |
| Publishing / go-live / front-end | ✅ From OTS tickets |
| Storefront / publishing | ✅ First version |
| Common live-flyer issues | ✅ First version (from `#helpme-ops`) |
| Data piping | ⬜ Deferred (not in first scope) |
| ClickUp process material | ⬜ Not yet ingested (current source of truth for PS) |

*Last updated: 2026-07-14.*
