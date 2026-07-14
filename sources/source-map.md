# Source Map — Where This Knowledge Came From

This file records the provenance of every knowledge-base article so answers stay
trustworthy and can be re-verified as sources change. All Atlassian content is
from the `flippit.atlassian.net` instance (cloud ID `5d9c002c-…-2565ccb0e5f8`).

## Confluence pages

| Title | Space | Page ID | Used in |
|---|---|---|---|
| Code sheet Troubleshooting Guide | XPTCXE (Client Experience & Enablement) | 3129146347 | codesheet-errors, escalation |
| Flyer Troubleshooting Guide | CX (Customer Experience) | 2259652718 | flyer-processing-overview |
| Processing Support - Knowledge Base ⚠️ *superseded by ClickUp (Jun 2026)* | FLX (Flex Hub) | 11717181547 | flyer-processing-overview, escalation |
| Urgent Flyer Processing | XPTCXE | 3129139207 | flyer-processing-overview |
| How to troubleshoot Storefront errors | QKB (Quality Knowledge Base) | 11540496444 | storefront-publishing-errors |
| Alert Runbook: Live Flyer Check | CTLR | 11691786294 | storefront-publishing-errors |
| Data Piping Troubleshooting Guide | XPTCXE | 3129145084 | escalation (referenced; article deferred) |
| HDUS Troubleshooting Guide | CP | 8666612725 | *not yet used* |
| Operations Skeleton Team #helpme-ops | XPTCXE | 3129131716 | context |

## Jira tickets (TOSS project) — codesheet error examples

| Ticket | Summary | Root cause / fix captured |
|---|---|---|
| TOSS-494 | BestBuy codesheet not picking up file | Trailing space in FTP filenames |
| TOSS-6360 | Wk32 new versions throwing config | Add new pricing zones to config |
| TOSS-7059 | w13 new versions to add to config | Add new pricing zones to config |
| TOSS-7012 | Weis Markets NilClass | PDF base path mistake + PZ missing pages |
| TOSS-7020 | Rexall `gsub for nil` | FTP file renamed (FLAP→FD); add lookup logic |
| TOSS-7027 | SDM word-bank/exception error | Workaround: remove erroring PZs & re-run |
| TOSS-7029 | No Frills ATL pages not picked up | Week-number & version-substring matching bug |
| TOSS-7030 | Freshmart warning + missing pages | New-year WK55→WK01 collided with page numbers |
| TOSS-7033 | Save A Lot `split for nil` | Codesheet row (line 131) missing start/end dates |
| TOSS-7042 / 7043 | Rent A Center not processing | Filename delimiter mismatch (`_` vs `-`); trailing page numbers |

## Slack

| Channel | Used for |
|---|---|
| `#helpme-ops` | Real recurring live-flyer issues & remediation patterns (common-live-flyer-issues) |
| `#flex-processingsupport`, `#helpme-flex`, `#sf-auditor-alerts`, `#content-public` | Referenced in escalation routing |

## Google Drive

- Searched; the flyer-related results were **"DRAW Audit / Automation Scorecard"**
  spreadsheets (workflow-analysis, owned by vanessa.sabatini@flipp.com), not
  troubleshooting docs. Not ingested into the KB. Revisit if they contain
  error-handling SOPs.

## Not yet ingested (candidate sources for future sessions)

- **Processing Support ClickUp space** — current source of truth for PS process
  (Confluence KB points here).
- **Data Piping Troubleshooting Guide** — deferred (out of first scope).
- **HDUS Troubleshooting Guide** — storefront/on-call adjacent.
- The legacy **Rob's Troubleshooting Code Sheets** guide on the old
  `confluence.wishabi.com` (referenced by the codesheet guide; may be archived).

*Last updated: 2026-07-14.*
