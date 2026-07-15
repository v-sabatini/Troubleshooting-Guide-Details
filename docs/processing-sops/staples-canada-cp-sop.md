# Staples Canada — CP Processing SOP

> **What this covers:** The full Content Production processing workflow for the
> Staples Canada CP weekly flyer — data feeds, the data formatter, product data &
> story curation build across all 5 versions, eco fees, image processing, previews,
> Bureau en Gros (BEG) go-live clones, and 15KM geo-targeting.
> Source Confluence page id: `10534518785` (CP space; page titled "Staples Canada
> [CP] SOP (Updated 01/14/26)").
>
> **See also:** Staples (Canada / Professional) OneGuide at
> `docs/retailers/staples.md`, and the Tiderise clone/go-live SOP at
> `docs/processing-sops/staples-canada-tiderise-golive-sop.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 232 (Staples Canada) · 6617 (Bureau en Gros / BEG, Quebec) |
| Flyer Type ID | 10698 |
| Slack channels | `#staplesca` (full internal team), `#staples-production` (production only) |
| Versions | ROC (Rest of Canada, EN + cross-language zone at go-live), QC EN, NB EN, QC FR, NB FR |
| Preview cadence | 4 previews + go-live: Preview 1, Preview 2, Final Preview, Confirmation Preview, Go-Live |

## Versions & preview stages
- **5 versions** in a regular publication: ROC, QC EN, NB EN, QC FR, NB FR.
- **Preview 1 & 2:** EN versions only (ROC, QC EN, NB EN); ROC marketing banners only. Processed by TR.
- **Final Preview:** all versions/banners; carry-over pages included if relevant (pages unchanged from the previous week, usually highlighted grey on the OS/story curation sheet).
- **Confirmation Preview:** identical to Final Preview, plus flagging **FPO banners** (incomplete, usually highlighted pink) to the retailer for replacement before go-live.
- **Go-Live:** BEG (Bureau en Gros) is the Quebec version — a separate Fadmin merchant for QC EN and QC FR, created only at go-live via cloning (see below).
- For all 4 previews the processor collects **feedback notes** (missing assets, clerical errors in data submission, etc.). Live revisions typically run 1–3 rounds.

## Data feeds
- Data feeds come from a separate SFTP. Select the Full EN and FR files from the Root folder.
- Rename: EN → `Staples_Flipp_Full_EN$enc=macRoman`; FR → `Staples_Flipp_Full_FR$enc=Windows-1252`.
- In the AWS Data File Upload folder on Cyberduck, upload the EN CSV first, wait for ingestion, then the FR CSV. A **warning log** after upload is normal; an **error log** must be investigated. Both feeds need at least 60 min to ingest.
- Confirm col F of the SKU List tab in the data formatter shows the correct data file name (`Staples_Flipp_Full_EN` for English, `Staples_Flipp_Full_FR` for French). Previews 1 & 2 use EN only; Final/Confirmation/Go-Live require switching the feed name from EN to FR mid-process.

## Data formatter
> The data formatter is highly sensitive due to the number of formulas — make minimal changes.

- Merchant O&S tab: highlight all rows, right-click, **clear rows**. Copy the retailer Merchant O&S data (excluding headers) and paste in. Other tabs update automatically. **Do NOT paste as values** — pasting as values can break the eco fees.
- The SKU List tab (col B Page Number, col E SKU, col A List of Items) auto-populates.
- Click **Ecomm Feed Generator → Generate Ecomm Feed**, then **Product Data → Staples - Generate Multi-Item Price**. The Product Data tabs populate once both macros finish.

### Eco fees (QC and NB only)
- Eco fees are small cross symbols on certain items in QC/NB. Merchant OS columns **U + W** hold the values; the formatter adds them to the final price (col F of the product datasheet) and triggers the cross symbol.
- **Current behaviour:** the data formatter picks up only fields with a "Y" value; other values / ghost characters are ignored.
- Legacy risk (ghost characters): if col F shows an unexpected cross symbol, check Merchant OS cols U + W for invisible characters (a red cell corner indicates an invalid value). Fix by highlighting the cell, pressing delete, then re-copy/paste into the formatter; or use `=ISBLANK(N1)` in an added helper column — FALSE on a blank-looking cell means a ghost character. Delete the added helper columns before pasting again. **Do not paste these columns as values.**

## Product data build

### English versions (ROC → QC EN → NB EN)
- Create new product data + story curation tabs on the internal story curation sheet (unique tab colour per week/proof).
- Copy items from the **Product Data ROC** tab in the formatter into the Product Data tab on the story curation sheet — **paste as values**.
- QC the ROC data:
  - **col AB "Store Sets":** apply `ROC` to ALL items — FPO (future product offer) blank rows won't auto-populate and must be filled manually. (At go-live there should be no FPOs — flag immediately if present.)
  - **col I "Sale Story":** every item needs a `Page-#`; blanks break CP Legacy. Page numbers may skip (e.g. 3→8 is fine) as long as they increase; a reversal (Page-8 before Page-3) must go back to Staples. Use Merchant OS col D to find the correct page for a blank cell.
  - **col M "raw_percent_off":** no decimal values.
  - **price cols D & E:** no `$` signs. Col D conditional formatting turns dark purple if D ≥ E (or if E is empty — ignore that case). A value in E with D purple = a real error: in preview, note the SKU and delete both prices (flag to retailer); at go-live, request an updated Merchant OS sheet ASAP naming the SKU(s).
  - **col "Product Grouping":** all rows in `[Page]-[Position]` format (e.g. `1-1`). Multi-items can share the same page/position.
  - **col K "product image URLs":** no `0` or `CA$-` values. At **go-live only**, blank cells mean the Staples pull failed — open the product URL and collect the image URL manually (≤5 times per SLA; more than 5 → notify the Production Lead). In preview, blanks can be left.
  - **Analytic categories** are auto-assigned in Fadmin from the Merchant OS column — auto-assignment fails with special characters (`Laptops & PCs` fails; `Laptops_PCs` works).
- Copy the ROC block, paste directly beneath → this becomes **QC EN**. Find & Replace `ROC` → `QC EN` in col T Store_Sets. Then paste from the formatter's Product Data QC EN tab as values: descriptions (col B), price cols D/E/F, col T (financing callouts), col Y (multi-item parent prices).
- Repeat: paste ROC again beneath → **NB EN**; Find & Replace `ROC` → `NB EN`; paste NB EN descriptions, prices, financing callouts (col T) and parent prices (col Y) as values.

### French versions (Final Preview → Go-Live)
- In the formatter SKU List tab, switch col F to the FR feed name; run Generate Ecomm Feed and Staples - Generate Multi-Item Price again.
- Copy the **Product Data QC FR** tab as values into the story curation Product Data tab; QC the same columns as EN. If image URLs were collected for EN, copy that column across (same data).
- Copy the QC FR block beneath → **NB FR**; Find & Replace `QC FR` → `NB FR`; paste NB FR descriptions, prices, financing callouts (col Q) and parent prices (col Y) as values.

### Placeholders for previews
- If in a preview stage with FPOs: run the **"Add TBD"** macro (adds TBD to blank product name fields) and the **"Add Staples Logo"** macro (adds a Staples logo to the PDF for FPOs).

## Story curation
- To start a fresh sheet for Preview 1, duplicate the previous week's, then delete everything from col B "Page" to col I "Store_Sets" (col A has a formula that resets).
  - col A formula (if needed to re-apply): `=IF(ISNUMBER(SEARCH("FR",$F3)),"Page-"&B3&" FR","Page-"&B3)`
- **Preview 1 & 2:** ROC banners only, assigned to all 3 EN versions — build the ROC zone then copy/paste it twice (ROC, QC EN, NB EN). **Final Preview:** version-specific banners per zone — repeat the build per version, ensuring correct values in col I "STORE_SETS".
- Copy col B "Page" to col H "url" from the retailer's Story Curation ROC tab; paste from col B onwards (col A auto-populates). If a version is missing a page others have, Staples leaves a blank space — paste in chunks, skipping the missing page (the system won't read blank rows).
- QC:
  - **col H "url":** delete phrases like "Static" or "See insert document" (run the `<link>` macro to strip default `<link>` text). Cells must be blank or a `https://` URL for CP Legacy to run.
  - **col F "Document Template":** EN → `StaplesCA-EN-07`; FR → `StaplesCA-FR-09`.
  - **col C "Items":** AdBanner templates should be 0.
  - **col A "Sale Story":** every row's page must match col B (drag formula down; FR uses `Page-# FR`).
- **Banner QA (Duplicates Check tab):** paste banner names from the story curation sheet into col A (sort A-Z), the actual `.png` filenames into col B (Find & Replace `.png` → blank, sort A-Z). Green rows = exact match; white rows = missing or mismatched (e.g. `WK5` vs `WK4`). In preview, note mismatches and flag to Staples; at go-live, confirm correct banners with the retailer.
- **FPO banners (Confirmation Preview & Go-Live only):** scan banner folders for FPOs (bright pink rectangles) or untranslated FR banners. Compile the list and include it in the confirmation-preview delivery email. At go-live, confirm all previously-flagged banners are now accounted for and not FPOs; flag immediately if any remain.
- **Item count check:** compare item count per page on the OS sheet vs the story curation sheet using the formatter's **Item Count** tab (col F turns red on mismatch). Rule of thumb: OS count > template count is fine (multi-items); **OS count < template count** requires action — add a placeholder row across ALL pricing zones (col C name via "Add TBD", col H ECOMM ID via "Add Staples Logo", col I Sale Story `Page-#`, col T Store_Sets, Product Grouping `[Page]-[Position]`).

## Images
- Marketing banners are `.png` at ≥72 DPI — drop directly into the Staples Banners folder on Cyberduck.
- **Product images** go via the **Auto Image Processing** custom action in CP Legacy (disconnect from Flipp VPN only for this step): Action Type Auto Image Processing, Merchant ID 232, attach product data CSV, Image Output **png**, Trim cropping **checked**, **Lago version 6**. Wait ~30 min.
- Manual images: convert to png + trim, rename to the col H value (e.g. `733088` → `STC733088`), upload to Cyberduck per prefix — `1STC` → Assets-Product Image A; `2STC` → B; `3STC` → C; plain `STC` → Assets-Product Images.
- Confirm ingestion in Lago Explorer using filters: Asset type `staplescanada Product Images`, Changed on today, Name contains `STC`. Allow ~30 min.

## CP Legacy (all previews and go-live)
- Connect to Flipp VPN. Run **Generate and Process Merged Datasheet**. Verify product info + banners output correctly in all versions.

## Preparing previews
- Region sets: ROC → CP ROC; QC EN → CP QC; NB EN → CP NB; QC FR → CP QC; NB FR → CP NB.
- Edit Details: set **available from** to when the next preview files are due, at 11:58pm; **available to** same day 11:59pm; valid from/to = expected go-live dates; preview date = today; **hide in distribution and flipp**.
- Set a **trigger to hide the flyer in hosted** on the available-from date at 11:30pm (hides everywhere before it would "go-live").
- Export a PDF per version (Pricing zone → Full Screen preview → More → PDF/Print → `flyer.pdf`), rename per version (ROC, QC EN, etc.), compile into a `WK# Preview #` folder, zip, upload to the Staples SFTP weekly folder.

## Fadmin processing (go-live)
- **Inserts (if applicable):** manually upload PDF inserts; box and tag per the linking document; add to each version at the paginated position.
- **Distribution:** create a CL (cross-language) pricing zone for ROC; region sets ROC + ROC CL → CP ROC, NB EN + FR → CP NB (leave QC for BEG step).
- **Item Image QC:** all images PDF or data-piped; copy the image URL into the Override Image URL tagging field for any cutouts.
- **Thumbnails:** `thumbnail_1065_x_600` 3 pages; `stock_premium` 2 pages; `storefront_carousel_premium` 3 pages; `storefront_carousel_organic` 2 pages.
- **Edit Details:** live Wednesday–Tuesday; available everywhere; preview date today; No Theme (unless applicable).
- **Tracking codes:** two do not change (already on the flyer type); add a third `utm_campaign` named `Weekly[date]`; press **Apply All Tracking Codes**.
- **Flyer sorting:** CP Weekly flyer first, then secondary pubs.
- Export PDFs per version (More → Download Low-Res PDF), compile into `WK# Go-Live`, zip, upload to the SFTP.

## BEG processing (go-live)
Bureau en Gros is a separate merchant for QC EN/FR. Clone the Staples flyer twice (wait for data piping to finish first, or the clone fails):
- **BEG merchant clone:** remove ROC, ROC CL, NB EN, NB FR region sets; add CP QC to QC EN and QC FR; Edit Details → **hidden on hosted**; apply tracking codes.
- **QC Hosted Only clone:** remove ROC, ROC CL, NB EN, NB FR; add CP QC to QC EN/FR; Edit Details → **hidden on flipp and distribution**; apply tracking codes.

## 15KM geo-targeting (go-live, when requested)
- Retailer provides a geo-targeting `.xlsx`, PDF/PNG banners in the SFTP, and timing notes.
- Flyer-run breakdown when 15KM applies: (1) Weekly Go-Live (hidden on hosted; ROC, ROC CL, NB EN, NB FR); (2) BEG (hidden on hosted; QC EN, QC FR); (3) Weekly Hosted-only for ALL versions incl. geo-targets (hidden on flipp + distribution); (4) 15KM Geo-target flyer (hidden on hosted; geo-target versions).
- Use the **Geo Target 15KM (11573)** flyer type; tell BD so budget is applied.
- Clone the main flyer, append "Geo-Target" (+ store codes if few), copy tracking codes/URLs, rename pricing zones by store/city (create cross-language zones if EN-only pages). Box/tag geo-target pages per the geo-target document (links only). Insert pages now or via triggers per the instructions. For cross-language zones, duplicate the PDF with an `FR_` prefix and assign as French to make triggers work.
- **Store/FSA removal:** add the provided store codes to the geo-target run, note the FSAs pulled in via the 15KM radius, and remove them from the Weekly Go-Live flyer via a dedicated region set (e.g. `CP WK# ROC Minus Stores 67 + 150`). Build hosted-only region sets so each geo-targeted store's single FSA is isolated. **Provincial** geo-targeting stays within the Weekly Go-Live flyer (no separate run) using provincial region sets.

## Flyer review checklist (go-live)
Dates match WBS; hidden in hosted / hide trigger set; pricing zones (ROC EN, ON EN with wireless insert, ROC FR + ON FR cross-language, plus store-opening PZs); correct Merch O&S sheet used (spot-check prices); inserts in correct positions; badges appear; analytic categories applied; tracking codes applied (`utm_campaign` date updated); clean images; thumbnails drawn; mark complete on back end.

---
*Source: Confluence "Staples Canada [CP] SOP (Updated 01/14/26)" (CP, 10534518785). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
