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
| 3 | [Common Live-Flyer & Processing Issues](knowledge-base/common-live-flyer-issues.md) | Tile-generation, image import, stale pricing/prefix, categorization, harmonization, or masthead issues. |
| 4 | [Storefront & Publishing Errors](knowledge-base/storefront-publishing-errors.md) | Storefronts failing to load, missing thumbnails, or republish decisions. |
| 5 | [Escalation & Ticketing](knowledge-base/escalation-and-tickets.md) | You've tried self-serve and need to know where to ask or how to file a CLSD ticket. |
| 6 | [Glossary](knowledge-base/glossary.md) | You hit an unfamiliar term or acronym (PZ, FADMIN, CLSD, FQC, etc.). |

## Supporting material

- [KB Article Template](templates/kb-article-template.md) — use this to add new
  articles consistently.
- [Source Map](../sources/source-map.md) — provenance for every article.
- [Session Prompts](../sessions/prompts.md) — copy-paste prompts to resume/wrap
  up working sessions.
- [Session Logs](../sessions/logs/) — what was done each session + next steps.

## Coverage status

| Area | Status |
|---|---|
| Codesheet errors | ✅ First version (10 real tickets + guide) |
| Core flyer processing / ops | ✅ Overview + urgent processing |
| Storefront / publishing | ✅ First version |
| Common live-flyer issues | ✅ First version (from `#helpme-ops`) |
| Data piping | ⬜ Deferred (not in first scope) |
| ClickUp process material | ⬜ Not yet ingested (current source of truth for PS) |

*Last updated: 2026-07-14.*
