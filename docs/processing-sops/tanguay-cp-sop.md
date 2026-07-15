# Tanguay — CP Processing SOP

> **What this covers:** Content Production processing steps for Tanguay (AMP)
> publications — HTTPS data feeds, SKU list formatting, product data + story
> curation build, image ingestion, Fadmin FQC, and price-refresh runs.
> Source Confluence page id: **11466539020** (CP space).
> Contacts/credentials intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 3877 |
| Flyer Type ID | 11815 |
| Slack channel | `#tanguay-amp-production` |
| EN feed | `https://sftpgo.feedonomics.com/ftp/fdx_95696816170244/tanguay_ca_en_digital_flier.csv.gz` |
| FR feed | `https://sftpgo.feedonomics.com/ftp/fdx_91ff3890170245/tanguay_ca_fr_digital_flier.csv.gz` |

Data feeds are passed through dedicated **HTTPS URLs** (replacing the previous email-based method).

## Data & workflow — what you need

- SKU List (submitted by retailer)
- Story Curation Sheet (submitted by retailer)
- Marketing assets (banner files, submitted by retailer)
- SKU List Formatter
- EN and FR data feeds
- `[PROD]` Curation Sheet — Story Curation (templates) tab + Product Data tab

## Processing

- Tanguay emails when assets are uploaded to the SFTP. Confirm you have: marketing banners (EN + FR), Tanguay Curation Template, SKU List. Download from the SFTP.

### Banner duplicates check

On the internal story curation document, use the **"Duplicates Check"** tab:
- Delete existing data (keep row-1 headers).
- Copy all marketing-banner **names** from the retailer curation sheet (EN + FR) into col. A → Data > Sort Range > A–Z.
- Copy all **.png** banner filenames into col. B (paste as values via a new email draft if needed to strip images), sort A–Z, and use Find & Replace to remove `.png`.
- Conditional formatting turns matching rows **green**. White rows are missing or not an exact match. Request outstanding assets, or fix spelling by best judgement / confirm with the retailer.
- Upload the RAW retailer files to the shared drive.

### Download data feeds

On the day of the flyer build, download and unzip the EN and FR feeds from the HTTPS URLs, renaming to `tanguay_EN_feed` and `tanguay_FR_feed`.

### Upload to CP Legacy

Run the **Upload Datafeed** Custom Action:
- Data Feed 1 → `tanguay_EN_feed`
- Data Feed 2 → `tanguay_FR_feed`
- Can take 5–10 minutes.

### SKU list formatting

- Download the SKU list from the RAW folder (use the folder matching the flyer date — Tanguay uses same-day data pulls).
- Paste into the **Input** tab of the SKU List Formatter. Mind column order: skip the "Images" column and the final product-names column.
- Menu → **'Clean Data' > 'Fix SKU Leading zeroes'**.
- Download the 'Input' tab as CSV, rename to `SKU_List`, upload to the appropriate folder in the shared drive.

### Create product data

- Once feeds finish uploading, run the CA **'Create Product Data'**, select the `SKU_List` file, execute.
- You receive an email with the product data sheet; download it as CSV.
- Scan the email for warnings/flags on missing SKUs (or a warning status on the job) — forward to the specialist and flag.

### Product datasheet edits

- Add a column at the end headed **`STORE_SETS`** (Column S). Update store sets based on Sale Story in Column I: EN pages → `QC_EN`; FR pages → `QC_FR`.
- Delete all values in **Column O (Lago Custom 13)**.
- From the original SKU list (RAW folder), for SKUs with an image link in **Column G**, copy the image link into **Column K** of the Product Data Sheet (replacing old image links).
- Column M **"sale_story"**: ensure the FRENCH data shows the dollar sign after the price. **This check is for French data only** — do not apply to English data.
- **Eco fees:** if the retailer marks an X in column F of the SKU List, add the eco-fee callout to the description column (to appear in the item pop). If missing, add manually:
  - EN: `Applicable ecofees are included in prices.`
  - FR: `Les écofrais applicables sont inclus dans les prix.`
- PDFSF rules: URLs must begin with `https://`; current price < original price; ECOMM IDs and Names filled for every item.
- Download as CSV, rename `[PROD] Tanguay Curation Template - Product Data`.

### Story curation

- Copy columns **B–K** from the retailer's Story Curation EN tab into the `[PROD]` Story Curation Set A tab from col. B; repeat for the FR tab, pasting directly under the English templates.
- Column A auto-populates Page-# / Page-# FR sale stories (drag formula down if needed).
- Update 'Store Sets': EN → `QC_EN`, FR → `QC_FR`.
- PDFSF rules: sale story on all rows in col. A; correct EN/FR templates in col. G; marketing banners must match the exact (case-sensitive) `.png` filenames; URLs begin with `https://`.

## PRICE REFRESH ONLY

When processing notes say "PRICE REFRESH ONLY": download EN & FR feeds and upload to CP Legacy, re-run **'Create Product Data'**, edit the PD sheet as needed, download CSV. Download the Story Curation sheet from the 'Story Curation Set A' tab. **Skip Auto Image Processing** and immediately run **"Generate and Process Merged Datasheet"**, then follow Fadmin FQC as usual.

## Images

- Run **"Auto Image Processing"** on CP Legacy. **Do NOT trim the product images.**
- Verify the correct image count ingests into Lago Explorer (ECOM IDs are identical in EN and FR; Lago will not duplicate files — expected count = images tab total minus 1).
- Marketing banners are uploaded by the specialist.

## CP Legacy

- Once all images are in Lago, run **"Generate and Process Merged Datasheets"**.
- For errors, reference the CP Troubleshooting Guide 3.0 (LAGO section).

## Fadmin FQC

- After output to Fadmin, let sessions finish. Verify no data missing on PDFs and that language/store auto-assignment succeeded.
- **Item Image QC:** ensure PDF images selected for all items; override any cutouts.
- **Thumbnail QC** (standard four): `thumbnail_1065_x_600` (3 pages), `stock_premium` (2 pages), `storefront_carousel_premium` (3 pages), `storefront_carousel_organic` (2 pages).
- In the **QC_en** pricing zone, click the 0 in the FSAs column and select the QC region set; repeat for **QC_fr**.
- Flyer name/dates: refer to the Direct Processing Schedule (name from "Retailer" column, dates from "Processing Notes").
- Flyer available everywhere, No Theme (unless applicable).
- Create a same-day preview link for the retailer; send the flyer to the specialist for review.

---
*Source: Confluence "CP - Tanguay SOP" (CP, 11466539020). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
