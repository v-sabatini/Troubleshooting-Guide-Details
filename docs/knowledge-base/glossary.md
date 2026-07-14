# Glossary — Flyer Processing Terms & Acronyms

> **What this covers:** Plain-language definitions of the terms, tools, and
> acronyms used across this knowledge base. The chatbot should use this to
> decode jargon in a user's question (e.g. someone pastes a "PZ" or "CLSD" and
> expects the bot to understand).

| Term | Meaning |
|---|---|
| **Codesheet** | The spreadsheet that tells FADMIN how to build a flyer run: uploads pages & pricing zones, orders pages, assigns stores/regions, sets dates and language. |
| **Config name** | Identifies which processor logic runs for a retailer's codesheet. Some retailers have multiple configs for different purposes. |
| **Pricing zone (PZ)** | A grouping tying a set of pages + valid dates + language + stores/regions together within a flyer run. |
| **FADMIN** | Internal admin tool for building, processing, and republishing flyer runs (`fadmin.flippback.com`; legacy `flyers.merchants.wishabi.ca`). |
| **FTP / SFTP** | File servers where retailers deliver source PDFs/images. Filename and folder conventions matter for codesheet processing. |
| **PDF Base Directory** | The FADMIN field pointing the codesheet at the correct FTP folder. A wrong/extra `/` breaks file lookup. |
| **Session** | An automated processing step on a run (image/tile generation, categorization, tagging, etc.). "Re-run sessions" is a common first fix. |
| **FQC** | **F**inal **Q**uality **C**heck — verification that a run is correct before go-live. |
| **QC** | Quality Check / Quality Control (e.g. tag QC, thumbnail QC). |
| **CLSD** | The escalation ticket type filed for issues needing Content Collection / CI / dev investigation. |
| **TOSS** | The Jira project historically used for Ops Troubleshooting tickets (source of many codesheet error examples in this KB). |
| **PS** | **P**rocessing **S**upport — the Flex team that executes uploads, vendor setups, FQCs, page swaps, and revisions for many retailers. |
| **FLEX** | Flexible/vendor staffing org that provides PS Scrum Masters and processors. |
| **FTE** | Full-Time Employee (as opposed to FLEX / DSP hourly staff). |
| **DSP hourly** | Overnight hourly processors (uploads and FQCs only; no Slack access). |
| **COC** | "Completed by Ops Content" / center-of-competence style ownership tag used in PS task-combination charts. |
| **VAST** | A retailer program/segment recently migrated into Processing Support. |
| **Enablement pod (CXE)** | The **Client Experience & Enablement** team that absorbed the former **Skeleton Team**'s troubleshooting/support function. Reachable at `@enable-cxe` in `#helpme-ops`. |
| **Skeleton Team** | Former ops support team (now disbanded); its function moved to the Enablement pod. |
| **Data piping** | The pipeline that feeds retailer data into the system; errors are usually caused by retailer-side changes. Filed via CLSD; generally not urgent since it doesn't block go-live. |
| **Harmonization / 4Square** | Matching a store to the canonical store/location dataset (4Square). Failures block store-level targeting. |
| **Masthead** | The branded header/banner on a storefront; can be tied to promo budget and Storefront Premium placements. |
| **Storefront** | The consumer-facing publication surface; "storefront errors" mean it's failing to load for some merchants. |
| **Republish** | Re-pushing a processed flyer run to storefronts (done in FADMIN); a common fix for missing thumbnails / incomplete processing. |
| **SFML** | Storefront markup/format referenced in storefront beacon errors (e.g. `Unable to retrieve SFML error 1`). |
| **Beacon** | A telemetry event (queried in Lenses), e.g. `Beacon.FlippApp.StorefrontZeroCaseError`. |
| **Generic codesheet** | A fallback codesheet used to create zones, assign stores, and upload pages manually when a retailer's normal codesheet won't process. |
| **OneGuide** | Per-retailer processing instructions referenced by PS. |

*Last reviewed: 2026-07-14. Add terms as new articles are written.*
