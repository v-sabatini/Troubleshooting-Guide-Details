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

## Jira — OTS (Ops Troubleshooting) board 315 — **primary source (session 2)**

Ingested **381 tickets** created **2024-01-02 → 2026-07-08** (all statuses incl.
closed), via JQL `project = OTS AND created >= "2024-01-01"`. This is the
front-line help desk and the primary grounding for articles 3–8. Full categorized
breakdown, escalation routing, and representative ticket lists are in
[`ots-ticket-inventory.md`](ots-ticket-inventory.md).

| Article | Backed by OTS tickets (examples) |
|---|---|
| `missing-flyers-and-indexing.md` | 1927,1928,1929,1930,1931,1939,1944,1954,1959,1960,1963,1969,1975,1985,1986,1997 |
| `clipping-and-autobox.md` | 1934,1935,1936,1941,1943,1979,1981,1984,2005,2020,2037 |
| `stores-and-harmonization.md` | 1967,1982,1991,2002,2009,2024,2025,2035,2053,2056 |
| `flyer-dates.md` | 1932,1972,1993,2029,2068,2069,2074 |
| `hosted-and-previews.md` | 1961,1962,1966,1968,1971,1973,1980,1988,1992,1995,2012 |
| `publishing-and-go-live.md` | 1938,1964,1971,1974,1978,1982,1992,1998,2006,2027,2030,2047,2048,2060,2064 |

**Escalation destinations discovered:** FD (indexer), CLSD (store-harmonization
fixes + general content/pipeline), MSC (harmonization *measurement*; "PIA" links
resolve here), HS/Hosted, DOC→account team. *(Session-3 correction: harmonization
fixes go to CLSD, not a "PIA" project.)*

> Note: TOSS (the old "Tactical Operations Support Service" project) is **retired**
> — only 1 ticket since Jan 2024. Its 2018–2019 codesheet tickets still back
> `codesheet-errors.md`. OTS is the current Ops Troubleshooting board.

## Jira — downstream escalation boards (session 3)

Sampled to document what happens **after** OTS escalates (see
`post-escalation-what-happens-next.md`). Turnaround figures are sample-based.

| Project | Name | Role | Sampled |
|---|---|---|---|
| **FD** | Flipp Content Daily Priorities | **Broken Indexer** tickets (missing-flyer fixes) | 100 (Jan 2024), issuetype = Broken Indexer |
| **CLSD** | Content Layer Service Desk | Content-platform engineering: investigations, pipeline/cloning (WES), categorization, tagging, harmonization *fixes* | 100 recent (May–Jul 2026) |
| **MSC** | Marketing Science ("PIA") | Foursquare AAAS measurement, store-trip reporting; harmonization *measurement* | 50 (harmoniz/foursquare, 2024) |

**Key correction:** `PIA-####` links resolve to **`MSC-####`** (Marketing
Science). Harmonization *fixes* are worked in **CLSD** (and historically **HTS**),
not a "PIA" project — earlier session-2 drafts were corrected accordingly.

Verified via `getJiraIssue PIA-8847` → returns `MSC-8847`. FD issue type "Broken
Indexer" = "merchants on Tesseract that didn't gather the latest flyer correctly."

## Slack

| Channel | Used for |
|---|---|
| `#helpme-ops` | Real recurring live-flyer issues & remediation patterns (common-live-flyer-issues) |
| `#flex-processingsupport`, `#helpme-flex`, `#sf-auditor-alerts`, `#content-public` | Referenced in escalation routing |

## Google Drive

- Searched; the flyer-related results were **"DRAW Audit / Automation Scorecard"**
  spreadsheets (workflow-analysis, owned by vanessa.sabatini@flipp.com), not
  troubleshooting docs. Not ingested into the CXE Help Center. Revisit if they contain
  error-handling SOPs.

## Not yet ingested (candidate sources for future sessions)

- **Processing Support ClickUp space** — current source of truth for PS process
  (Confluence KB points here).
- **Data Piping Troubleshooting Guide** — deferred (out of first scope).
- **HDUS Troubleshooting Guide** — storefront/on-call adjacent.
- The legacy **Rob's Troubleshooting Code Sheets** guide on the old
  `confluence.wishabi.com` (referenced by the codesheet guide; may be archived).

*Last updated: 2026-07-14.*
