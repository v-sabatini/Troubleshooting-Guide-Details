# Glossary — Flyer Processing Terms & Acronyms

> **What this covers:** Plain-language definitions of the terms, tools, and
> acronyms used across this CXE Help Center. The chatbot should use this to
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
| **Session** | An automated processing step on a run (image/tile generation, categorization, tagging, etc.). "Re-run sessions" is a common first fix. **Vendor tasks can also act as sessions** — re-running them kicks off item-level sessions. |
| **FQC** | **F**inal **Q**uality **C**heck — verification that a run is correct before go-live. |
| **QC** | Quality Check / Quality Control (e.g. tag QC, thumbnail QC). |
| **CLSD** | The escalation ticket type filed for issues needing Content Collection / CI / dev investigation. |
| **TOSS** | The Jira project historically used for Ops Troubleshooting tickets (source of many codesheet error examples in this CXE Help Center). |
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
| **Touch Storefront Objects** | A FADMIN **custom action** that pushes changes to the storefront; worth trying when an item link/URL change isn't reflecting on the front-end. |
| **SFML** | Storefront markup/format referenced in storefront beacon errors (e.g. `Unable to retrieve SFML error 1`). |
| **Beacon** | A telemetry event (queried in Lenses), e.g. `Beacon.FlippApp.StorefrontZeroCaseError`. |
| **Generic codesheet** | A fallback codesheet used to create zones, assign stores, and upload pages manually when a retailer's normal codesheet won't process. |
| **OneGuide** | Per-retailer processing instructions referenced by PS. |
| **OTS** | **Ops Troubleshooting** — the front-line Jira help-desk board (project `OTS`, board 315) where day-to-day flyer issues are raised and triaged. |
| **Indexer** | The automated scraper that pulls an indexed retailer's flyer from their website. A "broken indexer" (wrong URL/dates) is the top cause of missing flyers. |
| **FD** | Jira project **"Flipp Content Daily Priorities"** (board 312), home of **Broken Indexer** tickets — the escalation target for missing/not-gathered flyers. |
| **CLSD** | Jira project **"Content Layer Service Desk"** — the content-platform engineering service desk. Handles investigations, pipeline/cloning errors, categorization, tagging, and store-harmonization *fixes*. The main escalation from OTS. |
| **MSC** | Jira project **"Marketing Science"** — the analytics/measurement function (historically keyed **"PIA"**). Handles Foursquare AAAS feasibility, store-trip reporting, and data submissions. |
| **PIA** | Legacy Jira key prefix that now **resolves to `MSC-` (Marketing Science)**. Not a separate project. Store-harmonization *measurement* is tracked here; the *fix* is done in CLSD. |
| **HTS** | A store/harmonization ticket queue referenced by older harmonization escalations (e.g. HTS-25, HTS-35). |
| **HS / Hosted team** | Jira project (board 67) for the Hosted team — retailer-embedded flyer experience (iframe/preview/front-end rendering). |
| **WES** | The newer flyer-processing engine/flyer-type (vs. "legacy"); "WES Error" appears in cloning/pipeline failures escalated to CLSD. |
| **Nexus** | Internal content API/service (e.g. `UpsertOffers`, `upsert_section`) referenced in CLSD platform tickets. |
| **Foursquare AAAS / 4SQ** | Foursquare "Attribution-as-a-Service" — store-visit measurement for ad campaigns, run through MSC. |
| **PARF / exposure files** | Data files sent to Foursquare for measurement/reporting (MSC). |
| **DOC** | A routing/escalation path to the retailer's account team (e.g. third-party app issues not hosted by Flipp). |
| **CLSD** | (see above) general content escalation ticket type; OTS escalates stuck pipelines/cloning/FQC issues here. |
| **FSA** | **Forward Sortation Area** — the first three characters of a Canadian postal code; used for flyer distribution/coverage. "FSA Missing" = a postal area has no flyer. |
| **Distro** | Distribution — the set of postal codes/ZIPs/stores a flyer run is served to. |
| **Geo-targeting** | Mapping postal codes to the correct regional flyer. Errors show as one region seeing another region's flyer. |
| **AutoBox / auto box draw** | The task that automatically draws clip boxes around flyer items. Completing it kicks off **auto tag**. Poor draws cause unclippable/off-center items; the fix is re-running it or boxing manually. |
| **Auto tag** | The task that tags item data; triggered after AutoBox. |
| **Cutout generation** | Generating item cutout images; can fail/block and need a re-run. |
| **Page stitching** | Assembling flyer pages for display; re-running it + republishing fixes cropped/mis-rendered pages. |
| **Tile / thumbnail generation** | Automated step producing flyer tiles/thumbnails; failures block clipping or display. |
| **Preview link** | A link to view a flyer (often pre/around go-live). Not intended for sharing not-yet-live flyers. |
| **Hosted** | The retailer-embedded flyer experience (e.g. shown in an iframe on the retailer's own site). |
| **Simp pop (simple pop)** | A flyer-type toggle; when on, item detail text (pre-price/price/sale story) is suppressed. Turning it off restores item details. |
| **Preview ready / Ops complete** | Flyer-run states. A run stuck in "preview ready" instead of "Ops complete" won't go live; cloning/re-processing is the common fix. |
| **Clone / cloning** | Copying a flyer run; used to resolve a run stuck between states, and a distinct source of "clone erroring" issues. |
| **Tesseract** | Internal tool for indexing sessions (`tesseract.flippback.com`), used to verify indexing/added flyers. |
| **Track ID** | Identifier a page needs to be included in tile-generation sessions; pages missing it get excluded. |
| **Content V2 / V2** | The newer **Global-Centric** content model (Offers, Products, Promotions, Publications with global IDs), replacing the **Flyer-Centric** V1 model. See `content-v2-and-publishing.md`. |
| **V1 (Flyer-Centric)** | The legacy content model where everything hangs off a flyer (`flyer_id`, `flyer_item_id`). Being migrated to V2. |
| **Publication** | V2 equivalent of a flyer — a curated, dynamic collection of displayable items; can be distributed per channel/place. A **Publication Plan** (queries + rendering) is "hydrated" into a **Publication Payload** (what the user sees). |
| **Section / Section Plan** | V2 equivalent of a flyer page; a subset of a publication that can have its **own distribution** and rendering. |
| **Offer** | V2 equivalent of a flyer item — a price/discount on one or more products for a period, for one retailer/language. **One Offer can map to many V1 flyer items.** |
| **Atom** | Parent type of **Offer** and **Promotion**; replaces the V1 "merchandise/items" concept. |
| **Promotion** | A V2 displayable ad (image + click action) with no specific product/offer (e.g. a store-opening ad). |
| **Product** | A purchasable thing sold at one retailer (V2 dimension). |
| **Global ID** | V2 identifier for content, independent of any flyer (vs V1 `flyer_id`/`flyer_item_id`). |
| **Distribution / Place** | V2 targeting: a **Distribution** targets a **Place** (postal code, **store**, FSA, polygon), a channel, or (future) a user segment. In V2, flyers distribute to **stores, not FSAs**. |
| **Nexus API** | The single V2 **entry point / source of truth** for incoming flyer content; Fadmin produces V2 print content into it. |
| **Curator** | The single V2 **serving source**; pulls items/publications/distributions and feeds all channels. |
| **Flyers-NG** | The V1 **compatibility layer** during the V1→V2 transition; converts V2→V1 on read so legacy App/Web/Hosted keep working. |
| **DVM** | The active V2 distribution path today (NativeX, retailer apps); built on the V2 model. |

*Last reviewed: 2026-07-22. Add terms as new articles are written.*
