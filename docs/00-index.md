# Flyer Processing Troubleshooting — CXE Help Center Index

This is the master map of the CXE Help Center that powers the Flyer Processing
Troubleshooting chatbot. Each article is self-contained so it can be uploaded to
NotebookLM (or read by Claude) as an individual source.

## How to use this CXE Help Center

- **A processor with an error** → find the matching article below, paste the
  exact error text, follow the self-serve steps, and escalate if needed.
- **The chatbot** → treat each article as authoritative for its area; always
  prefer the exact error strings and cite the source article.

## Articles

| # | Article | Use it when… |
|---|---|---|
| 1 | [Flyer Processing Overview](knowledge-base/flyer-processing-overview.md) | You need the big picture of how flyers get processed and where things break. |
| 2 | [Content V2 & V2 Publishing](knowledge-base/content-v2-and-publishing.md) | You hit "V2", "publication", "offer", "Nexus/Curator/Flyers-NG", per-channel/zone distribution, or need to know what the V1→V2 shift changes. |
| 3 | [Codesheet Errors](knowledge-base/codesheet-errors.md) | A codesheet won't process, errors with `NilClass`, or files aren't picked up from the FTP. |
| 4 | [Missing Flyers, Indexing & Coverage](knowledge-base/missing-flyers-and-indexing.md) | A flyer/pages are missing, a broken indexer, missing FSA/postal coverage, or a region sees the wrong flyer. |
| 5 | [Clipping, AutoBox & Cutouts](knowledge-base/clipping-and-autobox.md) | Items aren't clippable, boxes are off-center, or cutout generation is failing. |
| 6 | [Stores & Harmonization](knowledge-base/stores-and-harmonization.md) | Store harmonization failures/audits, duplicate/missing stores, or add-store errors. |
| 7 | [Flyer Dates](knowledge-base/flyer-dates.md) | Wrong/expired/invalid valid dates, or a live flyer reading as expired. |
| 8 | [Hosted Sites & Preview Links](knowledge-base/hosted-and-previews.md) | Preview links or the hosted/iframe experience aren't working or render cropped. |
| 9 | [Publishing, Go-Live & Front-End Display](knowledge-base/publishing-and-go-live.md) | A flyer is stuck before go-live, pipelines/clones stuck, or prices/items not showing on the front-end. |
| 10 | [Common Live-Flyer & Processing Issues](knowledge-base/common-live-flyer-issues.md) | Quick reference (from `#helpme-ops`): tile-gen, image import, categorization, masthead. |
| 11 | [Storefront & Publishing Errors](knowledge-base/storefront-publishing-errors.md) | Storefronts failing to load, missing thumbnails, or republish decisions. |
| 12 | [Escalation & Ticketing](knowledge-base/escalation-and-tickets.md) | You've tried self-serve and need to know where to ask, which team, or how to file a ticket. |
| 13 | [After You Escalate: FD, CLSD & MSC](knowledge-base/post-escalation-what-happens-next.md) | You've escalated and want to know which team has it and how long it'll take. |
| 14 | [Glossary](knowledge-base/glossary.md) | You hit an unfamiliar term or acronym (PZ, FADMIN, OTS, V2, Publication, Offer, Nexus, Curator, etc.). |

> **New in session 2:** Articles 3–8 are grounded in **381 real Ops
> Troubleshooting (OTS) tickets** (Jan 2024–Jul 2026). See
> [`sources/ots-ticket-inventory.md`](../sources/ots-ticket-inventory.md).
>
> **New in session 3:** Article 12 documents the downstream escalation boards
> (**FD** indexing, **CLSD** content-platform, **MSC** measurement) with real
> turnaround expectations.

## Retailer-specific processing guides

Per-retailer processing instructions converted from the **OneGuide** docs. See
[`docs/retailers/`](retailers/README.md) — **✅ complete: 489 retailer guides**
(all reachable OneGuides; 2 source docs were unavailable). Full directory in
[`sources/oneguide-retailer-index.md`](../sources/oneguide-retailer-index.md).
Use these when a question is about a **specific retailer** ("how do I process
ALDI / Ace Hardware?"). Contacts/credentials are omitted from every guide.

## Supporting material

- [Help Center Article Template](templates/kb-article-template.md) — use this to add new
  articles consistently.
- [Source Map](../sources/source-map.md) — provenance for every article.
- [Gap Log](GAP-LOG.md) — questions the assistant couldn't fully answer yet + follow-ups.
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
| Post-escalation (FD / CLSD / MSC) | ✅ Boards + turnaround (session 3) |
| Storefront / publishing | ✅ First version |
| Common live-flyer issues | ✅ First version (from `#helpme-ops`) |
| Data piping | ⬜ Deferred (not in first scope) |
| ClickUp process material | 🚫 Known gap — PS space not in connected ClickUp (see session-04 log) |

*Last updated: 2026-07-14.*
