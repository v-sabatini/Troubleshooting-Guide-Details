# Patrick Morin — CP Processing SOP

> **What this covers:** Content Production processing steps for Patrick Morin (AMP)
> publications — XML feed data pull, data formatting, story curation, image
> ingestion, preview/go-live setup, and revision handling.
> Source Confluence page id: **12897943557** (CP space).
> **See also:** Patrick Morin OneGuide in `docs/retailers/patrick-morin.md`.
> Contacts/credentials intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 3564 |
| Flyer Type ID | 12222 |
| Slack channel | `#patrick-morin_amp` |
| Data feed (EN) | `https://patrickmorin.com/media/feeds/feedflipp_en.xml` |
| Data feed (FR) | `https://patrickmorin.com/media/feeds/feedflipp_fr.xml` |

## Data & workflow — what you need

- Data Formatter
- `[PROD]` Curation Sheet — Story Curation (templates) tab + Product Data tab
- Marketing assets (banner image files, received via email)
- Template Selection (received via email)

## Processing

You receive an email with a ZIP of JPEG marketing banners, the 'Curation Sheet Final Template' spreadsheet (SKU list) and the 'Curation Document' for the week.

- Download assets and upload to the Patrick Morin shared drive. Label the folder by go-live date (per the WBS or the email).
- Reference the WBS for preview due dates and schedule TR for weekly processing. TR handles processing and tags the specialist when finished.

## Preparing data sheets

- Locate the shared-drive folder for the processing dates; it should contain a ZIP of JPEG banners and the 'Curation Sheet Template' (SKU list + curation document).
- Unzip, download the JPEG banners, convert to **PNG** using Image Downloader, and upload to Cyberduck.
- Open the 'Curation Sheet Template', go to the **'Sku'** tab, copy columns **A–O** (skip headers), paste as values into the **'SKU List'** tab of the Data Formatter.
- Click **'Pull data from XML feed'** on the SKU list tab and wait for the **'Retailers Data'** tab to populate (5–10 minutes).
- Check the **'Product Data [EN]'** and **'Product Data [FR]'** tabs for SKUs that failed to pull. Check Column C (Name); if blank, flag it.
  - **PRO TIP:** if a name is missing, search the SKU manually in the feed URLs with Ctrl+F. If the SKU is missing from the feed, flag it. Sometimes adding a **`-CH` suffix** to the SKU fixes the pull; if the SKU is in the feed but still won't pull, flag it.
- Copy all data (skip headers) from **'Product Data [EN]'** into the **'Product Data'** tab of the Story Curation Template; copy **'Product Data [FR]'** and paste as values directly below the English data.
- Manually adjust prices if formatting is off. If a price is highlighted after pasting, delete the value and re-type it manually.
- Download the Product Data tab as CSV and run **Auto Image Processing** (mark off trim cropping).
- Open the 'Curation Sheet Template', find the **'5 page curation'** tab, copy columns **B–L** (skip headers), paste as values into the **'5 Page Curation'** tab of the internal Story Curation document (Column A auto-populates). Use Find & Replace on Column J to replace all `.jpg` extensions with blanks.
- Run **Generate and Process Merged Datasheets CA**.
- Assign FSAs to EN & FR PZs (all stores assigned to both PZs).

## Preview setup

- Available from: one day before Go-Live (11:58 PM)
- Available to: one day before Go-Live (11:59 PM)
- Valid From: now
- Valid to: Go-Live day (11:59 PM)
- Internal Run Name: copy from processing notes
- Preview Dates: now
- Distribution toggles: Hidden in all Flipp apps, all third-party apps, and Native X
- Set up a trigger to hide in **"Hosted"** (same date/time as "Available From")

## Go-Live setup

- Available from: Go-Live date (12:00 AM)
- Available to: Go-Live date (11:59 PM)
- Valid From: Go-Live date (12:00 AM)
- Valid to: Go-Live date (11:59 PM)
- Internal Run Name: copy from processing notes
- Preview Dates: N/A
- Distribution toggles: Available everywhere

**Draw tiles:** `Stock Premium` (2 pages), `Storefront Carousel Premium` (3 pages), `Storefront Carousel Organic` (2 pages), `thumbnail_1065_x_600` (3 pages). Ensure all images are PDF, then assign the specialist to review.

## Ad-hoc: inserts

PM may send inserts (via email) to include in the publication. After standard processing:
- Download inserts as PDFs (separate EN/FR, or the same insert for both PZs).
- Pages → Edit and upload; set grouping as required. Upload the page twice if the same insert is used for both EN and FR.
- Mark the **Flyer Creation Task Ops** task complete and wait for system tasks.
- Box the new page, tag if links were specified, and add the page to both PZs.

## Actioning revisions (re-send preview)

- **Updating/replacing a SKU:** paste the new SKU into the Data Formatter, re-run the script, copy that SKU's row into the correct position in the 'Product Data' tab (overwrite old info) for both PZs (mind column order). Download that SKU's image, save as PNG, rename to match the **"Ecom ID"** column value, upload to Cyberduck, verify in Lago, then run 'Generate and Process Merged Datasheets'. Follow all QC steps and set preview.
- **Banner file updates:** convert the new banner to PNG, upload to Cyberduck, and re-run the flyer after confirming ingestion.

---
*Source: Confluence "CP - Patrick Morin SOP" (CP, 12897943557). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
