# Staples Canada — CP Processing SOP : Tiderise Previews & Go-Live Clones

> **What this covers:** The Tiderise (TR) processing SOP for Staples Canada across
> Previews 1 & 2, Final Preview, Confirmation Preview, and Go-Live (including the
> two go-live clones), plus multi-item troubleshooting and post-proof flagging.
> Steps for Proofs 1 and 2 are identical.
> Source Confluence page id: `11650531341` (CP space; page titled "[TIDERISE]
> Staples Canada SOP - Previews 1-2, Final Preview, Confirmation Preview, Go-Live
> (Clones)").
>
> **See also:** Staples (Canada / Professional) OneGuide at
> `docs/retailers/staples.md`, and the full CP processing SOP at
> `docs/processing-sops/staples-canada-cp-sop.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 232 (Staples Canada) · Bureau en Gros clone → flyer type 11605 |
| Flyer Type ID | 10698 |
| Versions (Preview 1 & 2) | ROC, QC EN, NB EN |
| Versions (Final / Confirmation / Go-Live) | + QC FR, NB FR |

> The specialist indicates in the Direct Retailer Schedule processing notes which
> tabs to work in and what steps are required. The data formatter is highly
> sensitive (many formulas) — make minimal changes. If incomplete data blocks
> processing, notify the specialist so they can flag it to Staples.

## Data feeds
- Select the Full EN (and FR for later stages) files from the datafeed SFTP Root folder. Rename: EN → `Staples_Flipp_Full_EN$enc=macRoman`; FR → `Staples_Flipp_Full_FR$enc=Windows-1252`.
- Upload EN and FR to the AWS Data File Upload folder / Cyberduck and wait for ingestion (≥60 min). A warning log is normal; investigate error logs.
- Assets are uploaded to the Drive by the specialist; upload proof outputs to the Drive under WKXX, Preview XX. For clone tasks the specialist provides the main flyer URL in the processing notes.

## Banner QA (Duplicates Check tab)
- On the internal story curation doc, open the **Duplicates Check** tab and clear existing data (keep row 1 headers).
- Paste the banner names from the Story Curation xls ROC tab as values into col A; for Final Preview also paste names from `_NBEN`, `_NBFR`, `_QCEN`, `_QCFR`. Highlight col A → Data → Data Cleanup → Remove Duplicates (turns cells white).
- Paste the actual `.png` banner filenames from the `_ROC` assets folder as values into col B (for Final Preview also the other version folders). Find & Replace `.png` → blank.
- Green rows = exact match; white rows = missing or mismatched (e.g. `WK5` vs `WK4`). Note mismatched filenames and send to the specialist.
- These can be ignored (already in Lago): `Offwhite-Bkg`, `Red_doodle`, `Primary_Charcoal`, `GameZone_OffWhite`, `East_Red_doodle`, `Half page_Kids`, `Y_255_213_50`, `Primary_Red`.

## Banners in Cyberduck & Lago
- Upload banners to Cyberduck **Assets-Banners**. Convert backgrounds (from `_BKGD_Colour` folder if supplied) to 72dpi PNG in the ImageDownloader App before upload.
- After 20–30 min, in Lago Explorer (Asset Light Table tab) filter **Changed on = today** and **Name contains = WK#**; the result count should match the number uploaded.

## Data formatter
- SKU List tab F2 must read `Staples_Flipp_Full_EN$enc=macRoman`.
- Merchant O&S tab: highlight all rows, right-click, **clear rows**. Copy the retailer Merchant O&S data (excluding headers) and **paste as values**.
- Click **Ecomm Feed Generator → Generate Ecomm Feed** (populates Product Data with EN items; if "no data" error, log out/in and retry). Then **Product Data → Staples - Generate Multi-item Price**.
- If in the **Category Validation** tab col B is not all green, flag to the specialist.
- Copy Product Data **ROC** tab items (excluding header rows 1+2), paste **as values** into cell A2 of the internal Story Curation sheet (tabs per processing notes).

### Product data QA (per version)
- **col AB "Store Sets":** apply the version store set to ALL items; fill blank FPO rows manually (blanks break CP Legacy).
- **col I "Sale Story":** every item needs a `Page-#`. Skips are fine if increasing; use Merchant OS col E to resolve blanks.
- **col M "raw_percent_off":** no decimals.
- **price cols D & E:** no `$` signs. Col D turns purple if D ≥ E (or if E is empty — ignore). A value in E with D purple = error: note the SKU, delete both prices, tell the specialist.
- **col AA "Product Grouping":** filled for all rows, `[page]-[position]` (e.g. `3-5`). Items sharing a `parent_name` can share the grouping.
- Repeat: paste **QCEN** items beneath ROC (store set QC EN) and QA; paste **NBEN** beneath QCEN (store set NB EN) and QA.
- **Placeholders:** run macros **Add TBD** (blank names) and **Add Staples Logo** (blank items).

### Final Preview — French versions
- Update SKU List F2 to `Staples_Flipp_Full_FR$enc=Windows-1252`; run Generate Ecomm Feed and Generate Multi-item Price.
- Paste **QCFR** items beneath NBEN (store set QC FR) and QA; paste **NBFR** beneath QCFR (store set NB FR) and QA. Run Add TBD / Add Staples Logo.

## Item count check
- Copy story-curation cols B, C, D (one version only) into the formatter's **Item Count** tab (clear cols A/B/C first, keep header rows 1–2). Col F turns red on mismatch.
- Ignore when Merchant OS has **more** items than expected. When **fewer**, add a placeholder row to ALL versions: col C name (Add TBD), col H ECOMM ID (Add Staples Logo), col I Sale Story (`Page-#` from Merchant OS col D), col T Store_Sets (version), col AA Product Grouping (`page-position`, e.g. `2-7`).

## Story curation
- col A formula (if needed): `=IF(ISNUMBER(SEARCH("FR",$G3)),"Page-"&C3&" FR","Page-"&C3)`.
- **Preview 1 & 2:** ROC banners only → build ROC then copy/paste twice for QC and NB. **Final Preview:** version-specific banners per version.
- Copy col B "Page" to col H "url" from the retailer's Story Curation ROC tab; paste from col B onwards (col A auto-populates). If a version is missing a page, paste in chunks (system won't read blank rows). Apply the ROC store set to col I in all rows.
- QA:
  - **col H "url":** delete "Static" / "See insert document"; run the `<link>` macro to strip default `<link>` text. Cells must be blank or `https://`.
  - **col F "Document Template":** ROC/QCEN/NBEN → `StaplesCA-EN-07`; QCFR/NBFR → `StaplesCA-FR-09`.
  - **col C "Items":** AdBanner templates = 0.
  - **col A "Sale Story":** every row's page matches col B.
- Build the additional versions by copying beneath and setting col AB STORE_SETS (Preview 1-2: QC EN, NB EN with ROC banners; Final Preview: copy each retailer version tab QCEN/NBEN/QCFR/NBFR with version-specific banners). Confirm col A sale stories.
- **NEW — QC-specific pages:** QC versions sometimes have QC-only pages (identified by `_QC` in the Story Curation xls col A). Replace the col A formula for the QC EN version with `Page[]_QC` and the QC FR version with `Page[]_QC FR`.

## Images (product)
- Run the **Auto Image Processing** custom action in CP Legacy (disconnect Flipp VPN only for this step): Merchant ID 232, attach product data CSV, Image Output **png**, Trim cropping **checked**, **Lago version 6**. Wait ~30 min.
- Manual images: convert to png + trim, rename to col H value (e.g. `733088` → `STC733088`), upload per prefix — `1STC` → Assets-Product Image A; `2STC` → B; (`1STC` also listed for) Assets-Product Image C; plain `STC` → Assets-Product Images.
- Confirm ingestion in Lago Explorer: Asset type `staplescanada Product Images`, Changed on today, Name contains `STC`. Allow ~30 min.

## CP Legacy (all previews and go-live)
- Connect Flipp VPN. Run **Generate and Process Merged Datasheet**. Use the Troubleshooting Guide for errors.

## Preparing previews
> The Preparing Proofs training video references "QC EN" and "NB EN" version names — do NOT use those; use **QC** and **NB** as the written steps state.

- Region sets: ROC → CP ROC; QC EN & QC FR → CP QC (**do not assign stores to QC versions for Go-Live Previews**); NB EN & NB FR → CP NB.
- Edit Details (use REV WBS 2026 tab): available from = when next preview files are due, 11:58pm; available to = same day 11:59pm. **Go-Live Preview:** available and valid dates are the same (LIVE DATES row); both from-times 12:00 AM, to-times 11:59 PM.
- Internal Run name `CP_WK# Proof #`; preview date today; **hide in distribution and flipp** — but **do not hide the Go-Live Preview anywhere**.
- Trigger (not for Go-Live Preview): Attribute → Distribution Channels → add Hosted; Run At = available-from date at 11:30pm.
- Export a PDF per version (More → PDF/Print → `flyer.pdf`), rename per version (ROC, QC, etc.), compile into `Staples WK # Proof # PDFs`, zip. Send the flyer run link + notes to the specialist in Slack.

## Go-Live clones
When assigned, you're given a Go-Live flyer URL to clone **twice**.

**First clone (QC Hosted Only):**
1. In the given flyer run, Overview → **Clone**.
2. In the popup select **yes** for Copy Tracking Codes/URLs and add "Hosted Only" to the name → Clone.
3. Wait 15 min for sessions. Open the new run (e.g. `CP_WK24 Go-Live Hosted Only`).
4. Edit details → **hidden on flipp and distribution**.
5. Pricing Zone: **Clear Selection** for ROC, NB EN, NB FR, ROC CL — only **QC EN and QC FR** keep stores.
6. QA: no cutouts (PDFs selected); thumbnails (3 pages for Thumbnail 1065×600 and Storefront Carousel Premium, 2 pages for Storefront Carousel Organic); Flyer Run Tracking Codes present — if missing, add `utm_campaign` = `WeeklyMMMDD`.
7. Log the flyer run link + ID next to the week's "QC Hosted Only" and mark **Ready for Review**.

**Second clone (Bureau en Gros / BEG):**
1. Confirm the first clone has no running sessions.
2. Overview → Clone. In the popup: **unselect Staples Canada**, **select Bureau en gros**, yes for Copy Tracking Codes/URLs → Clone.
3. Wait 15 min. Open the new run (flyer type 11605, e.g. `CP_WK24 Go-Live`).
4. Edit details → **hidden on hosted only**.
5. Pricing Zone: Clear Selection for ROC, NB EN, NB FR, ROC CL — only QC EN and QC FR keep stores.
6. QA images/thumbnails/tracking codes as above.
7. Log the flyer run link + ID next to the week's "BEG" and mark Ready for Review.

## Uploading data feeds (Upload Datafeed custom action)
- Log into the Staples Ecomfeed SFTP (bookmark the connection via Action → New Bookmark; ask a specialist for the password on first login). Select the Full_EN and Full_FR txt files, download, and rename as above.
- Use the **Upload Datafeed** custom action (EN → Datafeed 1, FR → Datafeed 2). Tell the specialist if the action fails.

## Multi-item troubleshooting — "Area Box drawn cannot have zero area"
1. This CP Legacy error log usually includes item name/pricing — use it to find the item in the product data sheet.
2. In **Column AA** of the product data sheet, a position (e.g. `1-1`) listed **once** within a pricing zone = single item; listed **2–3 times consecutively** = multiple items in that position.
3. Find the page's template in the Story Curation sheet (e.g. `ANY=StaplesCA-Cover-09up-05`).
4. Cross-reference the **Template Blueprint** (WIREFRAMES section): only blocks labelled **"Multi-item eligible"** can hold 2–3 items; all others are single-item only.
5. If multiple items are assigned to a non-multi-item-eligible block, the system can't render. **Flag it**; after confirming with a specialist it is a retailer-side error, delete the extra row/item(s) so the block meets multi-item eligibility.

## Things to flag after proof completion
1. **Missing items / mismatched counts:** add TBD filler rows to the product data sheet until counts match; update all pricing zones. Flag: "Page _ has an item count of _ in the story curation sheet; however, only _ items are listed in the product data sheet."
2. **FPO banners (Confirmation Preview only):** review banners for each version — those showing "FPO" (grey background) and/or a neon pink box are incomplete. Record names and share with the specialist. Flag: "The following banners are FPO and need to be updated for the next proof: ___".
3. **Missing data in data feed:** at the data formatter step, after the macros finish, check col G ("Missing SKU's") on the SKU List tab for "Not Found" — note those SKUs for both EN and FR feeds. Flag: "The following SKUs are missing in the EN/FR data feed: ___".

---
*Source: Confluence "[TIDERISE] Staples Canada SOP - Previews 1-2, Final Preview, Confirmation Preview, Go-Live (Clones)" (CP, 11650531341). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
