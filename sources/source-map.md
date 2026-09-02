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

## Confluence — Content V2 / publishing platform (session 7)

Backs `content-v2-and-publishing.md` (orientation on the V1→V2 shift + how it
affects processing). All read-only.

| Title | Space | Page ID |
|---|---|---|
| Transitioning to Global-Centric Model: Content V2 & Event V2 Adoption Framework | DATAV | 13022527510 |
| Content V2 Dimensions | DATAV | 13245906978 |
| V1 => V2 Data Pipeline Transition | EN | 12597657799 |
| DET Content V2 Discovery ("flyers distributed to stores, not FSAs") | DATAV | 12291965139 |
| Transitioning from V1 → V2 for Content Retrieval | CTLR | 11268554758 |

Related to Gap Log GAP-001 / GAP-002 (V2 publish/distribution behaviors). These
are architecture/strategy docs — they explain the model, not ops runbooks.

## Slack

| Channel | Used for |
|---|---|
| `#helpme-cxe` | Real recurring live-flyer issues & remediation patterns (common-live-flyer-issues) |
| `#helpme-vs` | Single-executor / FMQ (3FL) vendor-processing issues & resolutions — an FTE runs the flyer end-to-end (e.g. Ops Spotcheck redirect). Note: much of this channel is vendor-assignment/staffing coordination, not troubleshooting — ingest selectively |
| `#flex-processingsupport`, `#helpme-flex`, `#sf-auditor-alerts`, `#content-public` | Referenced in escalation routing |

## ClickUp

Workspace `9003147350`. Read-only; contacts/assignees omitted; ingest selectively
(these boards are mostly ops/assignment coordination — capture only resolved
retailer-processing error→fix patterns, same bar as `#helpme-vs`).

| Space / list | ID | Used for |
|---|---|---|
| VSM – Adhoc Relief Board → `ARBoard` | space `90171177866` / list `901705387041` | Single-executor / FMQ (3FL) ad-hoc relief requests — the retailer-flow board where processing/assignment issues are filed and resolved (e.g. Spotcheck vendor-assignment fixes). Primary ClickUp scan target. |
| CXE – Enablement Project Space → `Projects`, `Collaboration` | space `90176167905` / lists `901714746393`, `901714745856` | Enablement improvement intake / project + collaboration tracking (the "ClickUp intake for improvements" referenced in `escalation-and-tickets.md`). |

Other spaces (CS Accounts, Brand Media Campaigns, Retech Onboarding Trackers,
Opportunity Pipeline, CXE – Training Sandbox) are out of scope for the Help Center.

> **Note:** the read-only ClickUp tools are pre-approved in `.claude/settings.json`,
> but the **weekly-scan trigger prompt still lists only Jira/Confluence/Slack/Drive** —
> add ClickUp (the two boards above) to that prompt from an interactive session for it
> to be swept automatically. Until then it's scanned only when run by hand.

## Google Drive

- Searched; the flyer-related results were **"DRAW Audit / Automation Scorecard"**
  spreadsheets (workflow-analysis, owned by vanessa.sabatini@flipp.com), not
  troubleshooting docs. Not ingested into the CXE Help Center. Revisit if they contain
  error-handling SOPs.

## Team SME review (answer-feedback-log)

Corrections logged by reviewers testing the assistant (see
`sessions/answer-feedback-log.md`). Applied directly to the articles; contacts
omitted.

| Entry | Correction | Article(s) |
|---|---|---|
| FB-002 | `NilClass` cause ordering — filename/SFTP mismatch leads; missing-dates only on date-requiring configs; confirm processor first | codesheet-errors |
| FB-003 | `generic_stores` `NilClass` — PZ-name typo/space top cause; missing store code names itself (not NilClass); Pricing Zone Page / Manage Stores locating technique | codesheet-errors |
| FB-004 | Tile-gen — whole-track-delete workaround (whole track only + backup); Slack-first before CLSD | common-live-flyer-issues, escalation |
| FB-005 | Auto-cat can't be re-run & doesn't block tagging; Vendor/Tag QC error = page/item deleted before Vendor tasks | common-live-flyer-issues |
| FB-006 / FB-007 | Item-import file format — `item_id`/`sku` column order, accepted headers, `english_`/`french_` prefixes, `YYYY-MM-DD` dates, `*blank*`, 3-column minimum | item-import-format (new) |
| FB-008 | Link/URL not reflecting on front-end — re-run Item Cutout Generation (downstream re-kick), Vendor-tasks-as-sessions, republish, `Touch Storefront Objects` custom action | publishing-and-go-live, common-live-flyer-issues, glossary |
| FB-009 | Page swap not on front end — track-ID is an upload-step issue (mis-cited OTS-1954), undo/redo page swap re-kicks sessions, escalate by scope (everywhere → Slack→CLSD; Hosted-only → HS) | missing-flyers-and-indexing, publishing-and-go-live, hosted-and-previews |
| FB-011 | Ops Spotcheck redirecting FTEs to another flyer run — try unblocking the run (which skips the Spotcheck QC), else CLSD (novel issue); corrected an earlier clone-linkage guess | common-live-flyer-issues |

## Weekly source scan (automated)

Additions from the scheduled weekly scan (Jira OTS / Confluence / Slack / Drive,
read-only). Flagged-but-not-applied items live in `docs/GAP-LOG.md` (weekly-scan
watchlist).

| Date | Applied | Source |
|---|---|---|
| 2026-07-22 | AutoBox can't box a website-screenshot retailer (long/skinny pages) → clipping-and-autobox | Jira OTS-2332 |
| 2026-07-22 | `#helpme-cxe` request/escalation flow (self-serve first, post-don't-DM, tag `@enable-cxe`, complete-request checklist, ClickUp intake for improvements) → escalation-and-tickets | Enablement `#helpme-cxe` process deck (Drive, 2026-07-21) |
| 2026-07-27 | Item Cutout Generation errors on items with a blank Name (auto-tag had no text) — find via Item Search Name IS blank, add a Name, unblock/re-run; else urgent CLSD/CPLAT → clipping-and-autobox | `#helpme-cxe` thread (2026-07-27) |

## Not yet ingested (candidate sources for future sessions)

- **Processing Support ClickUp space** — current source of truth for PS process
  (Confluence KB points here).
- **Data Piping Troubleshooting Guide** — deferred (out of first scope).
- **HDUS Troubleshooting Guide** — storefront/on-call adjacent.
- The legacy **Rob's Troubleshooting Code Sheets** guide on the old
  `confluence.wishabi.com` (referenced by the codesheet guide; may be archived).

*Last updated: 2026-07-22.*
