# Save-On-Foods (+ Urban Fare) — Processing Guide

> **Source:** Save-On-Foods / Urban Fare OneGuide (Google Doc `1gtUv_cxnYboRD8XVzuMMBGfH1OOrabPo-9uhLhaD3NU`). Contacts/credentials omitted.

Covers **Save-On-Foods (SOF)** and its sibling banner **Urban Fare (UF)**. Setup is the same for both; UF has no My Offers linking doc and files/folders/codesheets are labelled `UF_WK##` instead of `SOF_WK##`.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#overwaitea`, `#3fl-saveonfoods`, `#flexflyerreview` |
| Hosted URL | saveonfoods.com · urbanfare.com |
| Flyer type(s) | Weekly (Flyer type 180) |
| Processing | Auto-stack; 3FL + Flex Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Friday (evening files dropped Thursday; upload complete once files synced Friday).
- **Cadence:** Available From Wed 3:00 AM → Available To Thu 2:59 AM; Valid From Thu 3:00 AM → Valid To Wed 11:59 PM.
- **Preview date:** Sunday before live (link sent Monday, or Tuesday on long weekends).
- **Linking document:** yes — MYO Document; naming `SOF_WK##_SKU_PageName` / `UF_WK##_SKU_PageName`.
- **Day-by-day:** Fri upload → Fri/Sat OS processes → Sun 3FL Item QC → Mon DOC FQC + preview link → Tue corrections → Wed page swaps.

## ⚠️ Common errors / risk items (retailer-specific)

- **$1.49 Sale pages (highest-value risk):** when $1.49 pages are provided to trigger in at a future date, they **must be present during the retailer preview/corrections period**, then **removed before go-live**. History: an April 2024 CuSat incident — revised pages were implemented the same day the $1.49 triggers ran at midnight, so triggers failed to remove the revised pages; $1.49 pages went live briefly, were screenshotted, and leaked online. Mitigation: pages are removed from preview **as early as Noon the day prior to launch** to ensure correct state before EOD/launch.
- **SKU tagging is a risk item** — follow the SKU lookup steps in order; do not use shortcuts (can isolate the wrong SKU/original price).
- **Save-On-Foods: tag ONLY the Regular Price field — do NOT tag Original Price.** If REG_PRICE is blank, leave blank. If item/page not on the spreadsheet, leave SKU/regular price blank. Multiple SKUs → tag both separated by a comma.
- **Mi9 custom action** must run after data-piping groups are generated (else it errors). See troubleshooting below.

## Upload & setup (owned by DOC)

- From the **Save-On-Foods Merchant FTP**: grab the `.xls` codesheet (e.g. `SOF_052523.xls`) and the operations + items `.txt` files uploaded on the same date.
- **Upload the `.xls` codesheet (no manipulation):** Config **`overwaitea`**; PDF base directory = full base path; **uncheck 'region assignment' and 'combine zones'**; Save & Process.
- Build the SKU/PageName spreadsheet from the items `.txt` (Text-to-Columns on `|`; delete PAGE NUMBER, ITEM TYPE, ITEM PRICE, BRAND, CATEGORY ID, DISC PRICE, DISC PRICE UOM — **keep REG PRICE / REG PRICE UOM**; Remove Duplicates → ~25k–40k unique; tab 'SKU'; second tab 'Page Names' = Version + Store# from codesheet). Save as `SOF_Week#_SKU_PageName.xlsx` and mass-attach to all vendor tasks. UF has its own PDF folder, items file, ops file and codesheet.

### Setup QC
- Dates as above; add Sunday preview; available everywhere; no theme; 4 standard thumbnails.
- All pricing zones have stores/FSAs assigned (page counts within 1–3 pages of each other).
- Attach `SOF_Week#_SKU_PageName.xlsx` and MYOffers doc to all vendor tasks; mark vendor tasks high priority; complete Fadmin Setup QC.

## QC specifics

- **Box Draw — Medium; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up, social. **Include My Offers links.** Complete even if linking doc is missing.
  - "Plenty for $20" banner → ONE box, direct link `saveonfoods.com/plenty-for-20/`. Butcher's Box pages → ONE box. Books boxed/tagged as individual items; magazines/cards as LINK type. My Offers callouts boxed **separately** from the item (top box = item, bottom box = My Offers link; no text boxes). Flu/Pharmacy banners → link. "UNREAL DEAL" → 2 boxes (item + My Offers link).
- **Tag / Tag QC — High; Auto-tag ON; PDF image auto-select ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Brand: No.** Tag name exactly as PDF including brand in the name; description = size/weight/country of origin.
  - **Sale story:** More REWARDS points callouts (tag "PC…" wording exactly, e.g. "FREE WITH 1900 More REWARDS POINTS REDEEMED"). BOGO/# for/% off callouts go in **pre_price_text**, not sale story.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## SKU / Item QC (3FL, Pre-FQC)

- Export items → keep `item_id, sku, display_type, name, description, sale_story, pre_price_text, raw_current_price, price_text, url`; sort by name. Reference the attached item QC doc to fill SKUs consistently; when name+description match but SKUs differ, it likely has a My Offers callout → pick ONE SKU. Set link-type items (My Offers, Learn More, Pharmacy, Books, Recipe) to link type. Re-import CSV (col1 `item_id`, col2 `sku`); confirm no blank SKUs and none with multiple SKUs. Screenshot/flag items missing SKUs in `#3fl`.

## Mi9 Custom Action (sub-item generator)

- Format ops file: replace all `"` with nothing and all `,` with `|`; save as `SOF_WK##_Ops.txt`; upload and note the file ID.
- System → Custom Action → **Mi9 Sub Item Generator** (not report). Flyer Run File ID = flyer run ID; ID of uploaded file = ops file ID. Wait (up to ~15 min for SOF). Verify an item shows Sub Items (#) ≥ 1.

### Mi9 troubleshooting
| Issue | Action |
|---|---|
| "Flyer run has no sibling groups" | Item image QC → Generate Data Piping Groups |
| No sub-items on the whole page | Generate data piping groups; re-run page tile gen / page stitching; re-run Mi9; republish |
| No sub-items on a single item | Verify SKU; look up sub-item SKU on saveonfoods.com — if no results, item not live / SKU wrong → flag |
| "Unquoted fields do not allow \r or \n" | In the txt ops file, ensure 3-digit stores have a `.` after them (901 → 901.); re-add file, re-run |

## Post-processing (DOC)

- **Corrections Document (SOF only):** creates custom clickable items with custom circular promotion codes; box the item in each page, tag with the code from the corrections sheet, append ops-file sub-items, re-run Mi9, re-run page stitching (sync up to 3h), live-check.
- **Resyncing SKUs:** corrections often mean the SKU is wrong — verify against `SOF_WK##_SKU_PageName` across all zones, then re-run Mi9.
- **Urban Fare FQC:** fill blank SKUs from the attached doc; generate data-piping groups; upload/format UF ops file; run Mi9; check api products count (~100–200+ for UF).
- Preview links for both banners sent to the retailer (email list in the SOF cheatsheet — not stored here).

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Save-On-Foods OneGuide (Google Doc `1gtUv_cxnYboRD8XVzuMMBGfH1OOrabPo-9uhLhaD3NU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
