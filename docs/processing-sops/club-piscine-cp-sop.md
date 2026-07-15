# Club Piscine — CP Processing SOP

> **What this covers:** The Content Production processing workflow for Club Piscine
> AMP publications (bilingual EN/FR) — asset intake, product data & story curation
> build, image processing, CP Legacy, and Fadmin FQC through preview delivery.
> Source Confluence page id: `13186957313` (CP space).
>
> **See also:** Club Piscine OneGuide (vendor processing guide) at
> `docs/retailers/club-piscine.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 5611 |
| Flyer Type ID | 11716 |
| Slack channels | `#clubpiscine_amp_production`, `#clubpiscine` |
| Cadence | Monthly publications, bilingual EN + FR |
| Workflow | Tiderise (TR) build via CP Legacy custom actions |
| SFTP | Request Club Piscine credentials via `#sftp-automation` (credentials not stored here) |

## Assets required

- EN and FR data feed files (retailer-submitted)
- Marketing assets / banner images (retailer-submitted)
- SKU List (retailer, on shared Google Sheet)
- Story Curation Sheet (retailer, on shared Google Sheet)
- `[PROD]` Curation Sheet — contains the Story Curation (templates) tab and the Product data tab

## Workflow

### Download assets & data feeds
- Download the SKU list and story curation sheet from the shared SKU document, plus both data feed files and marketing assets from the SFTP. Upload all downloaded assets to the retailer Google Drive, clearly labelled for TR.
- For a preview, open the relevant run folder in the Drive → open the **Raw** subfolder — this holds the sheets needed to build the preview.
- Open the data feed CSVs in Google Sheets (usually labelled `Circulaire-Month-2026-EN/FR-V1`). **Update the column names in both feeds** so the system accepts them. Required columns, in order:
  `id | title | brand | sale_price | price | product_link | image_link`
- Download the updated feeds and drop them in the shared drive. Convert all marketing assets to **JPG** and upload to Cyberduck.

### Create Product Data
- Run the **Create Product Data** custom action in CP Legacy:
  - SKU list option → the SKU list just downloaded
  - Data Feed 1 → EN feed
  - Data Feed 2 → FR feed
- When complete you receive an email with the product data sheet — download it as a CSV.
- Scan the email for warning messages / missing-SKU flags (look for a warning status on the job). If present, forward the email to the specialist and flag the issue.
- In the product data sheet, missing SKUs (flagged in the email) leave empty rows. If running a preview with missing SKUs at the specialist's direction: apply the relevant store set by language, fill in the correct sale story from the SKU list, and input **"N/A" in the NAME field** so the flyer runs through CP-Legacy.
- PDFSF rules when reviewing product data:
  - URLs must begin with `https://`
  - Current Price must be less than original price
  - ECOMM IDs and Names must be filled for every item

### Story Curation
- In the RAW subfolder, open the story curation template CSV. EN and FR data are in the same tab separated by a heading.
- Copy all data (excluding headers) from **Column B to Column K** for the EN data and paste into the story curation tab of the `[PROD]` Club Piscine Story Curation Template. Repeat for FR, pasting directly beneath the English data.
- Column A contains a formula — `Page-#` / `Page-# FR` sale stories populate automatically; drag the formula down if needed.
- Apply **"English"** to all EN rows and **"French"** to all FR rows in **Column L (`STORE_SETS`)** so automatic language/store assignment works.
- PDFSF rules for story curation:
  - Sale story applied to all rows in column A
  - Correct EN / FR templates applied in column G
  - Marketing banners must match the exact `.jpg` filenames (case-sensitive) — the specialist checks this
  - URLs must begin with `https://`
- Download the Product Data and Story Curation sheets as CSVs.

### Images
- Run the **Auto Image Processing** action in CP Legacy with the Product Data CSV.
- Verify the correct number of images ingests into Lago Explorer. ECOM IDs are the same in EN and FR and Lago will not duplicate files — to confirm the expected count, use the `images` tab on the curation sheet (scroll to bottom, minus 1).
- Marketing banners are uploaded by the specialist.

### CP Legacy
- Once all images are in Lago, run the **Generate and Process Merged Datasheets** custom action.
- For errors, reference the CP Troubleshooting Guide.

## Fadmin FQC
- After the flyer outputs to Fadmin, let sessions finish running.
- Verify no data is missing on the PDFs and that language + store auto-assignment succeeded.
- **Item Image QC:** ensure PDF images are selected for all items; override any items using cutouts.
- **Thumbnail QC (Standard four):**
  - `thumbnail_1065_x_600` — 3 pages
  - `stock_premium` — 2 pages
  - `storefront_carousel_premium` — 3 pages
  - `storefront_carousel_organic` — 2 pages
- In the **English** pricing zone, click the 0 in the FSAs column and **Select All Stores**.
- For the **French** pricing zone, apply the **QC Store set**.
- Flyer name/dates per the specialist's ticket. Flyer is **available everywhere, No Theme** (unless applicable).
- Create a same-day preview link and send the flyer to the specialist for review.

## Common errors / risk items
- **Missing SKUs:** flagged as a warning status on the Create Product Data job and via empty rows in the product data sheet — forward the email to the specialist; only use N/A name placeholders under specialist direction.
- **Banner filename mismatch:** marketing banner names in story curation must match the `.jpg` filenames exactly (case-sensitive) or banners won't output.
- **Language/store mis-assignment:** driven by Column L `STORE_SETS` (English/French) — verify before processing.

---
*Source: Confluence "CP - Club Piscine SOP" (CP, 13186957313). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
