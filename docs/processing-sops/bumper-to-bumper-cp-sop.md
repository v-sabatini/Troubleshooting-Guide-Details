# Bumper to Bumper — CP Processing SOP

> **What this covers:** The Content Production processing workflow for Bumper to
> Bumper AMP publications (bilingual, 7 pricing zones) — asset intake, product
> data & story curation build, image processing, Fadmin setup with the
> hide-in-hosted trigger, and go-live clones.
> Source Confluence page id: `12198019113` (CP space).
>
> **See also:** Bumper to Bumper OneGuide at `docs/retailers/bumper-to-bumper.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 5478 |
| Flyer Type ID | 12052 |
| Slack channel | `#bumper-to-bumper-amp` |
| Tier / cadence | Lite tier; refreshes **monthly** with a **3-day preview** |
| Pricing zones | ON EN, AB EN, QC EN, BC EN, ATL EN (Atlantic), QC FR, ATL FR (Atlantic) |

## Assets required (from retailer, via email from production contact)
- SKU List
- Story Curation Sheet with banners, CTAs, URLs & disclaimers (**Story Curation is built by CP**)
- Banners (72 DPI PNG)
- Data feeds (EN and FR)

Data feed filenames: `bumpertobumper_flipp_en.csv`, `bumpertobumper_flipp_fr.csv`.

## Processing steps

### Curation & banners
- Drop the retailer banners into a banners folder in the Bumper to Bumper drive for TR to convert and upload to Cyberduck.
- In the prod story curation sheet, create a new tab for the month's publication and manually build the story curation template. Copy the data from the retailer's curation sheet into the prod sheet, pasting for **all pricing zones**: ON EN, AB EN, QC EN, BC EN, ATL EN, QC FR, ATL FR.
- Also create a **blank product data tab** for Tiderise.
- In the drive's month folder, convert banners to **72 dpi PNG**, upload to a folder labelled **Banners 72DPI**, upload to Cyberduck, then delete the original unconverted banners.

### Create product data
> Due to feed size, the specialist schedules you to run the Create Product Data custom action the day before processing or the morning of.
- Open the SKU list `.xlsx` in Google Sheets, save as CSV, upload the CSV to the drive.
- Data feeds are already in the shared drive (`bumpertobumper_flipp_en.csv`, `bumpertobumper_flipp_fr.csv`).
- Run the **Create Product Data** custom action in cp-legacy: SKU List → SKU list CSV; Data Feed 1 → EN feed; Data Feed 2 → FR feed.
  - **If re-running with the same feeds, do not re-upload the feeds** — only input the merchant ID and SKU list.
- Download the resulting product data from email (e.g. `bumpertobumper_product_data-2026-02-25`), upload to the drive. You can then delete the large EN/FR feed files.

### Import to curation & process
- In the internal curation sheet, import the product data into the specified month's tab: **Import location = Replace Current Sheet**; **uncheck** "convert text to numbers, dates and formulas".
- If the name field is empty, add **TBD**.
- Download the story curation template and product data as CSVs (save to the shared drive).
- Run the **Auto Image Processing** custom action, then once images are in, the **Generate and Process Merged Datasheets** custom action (Merchant ID 5478, Flyer Type ID 12052).
- Double-check pages — all banners and items present.

### Store assignment
- In the Pricing Zones tab, assign stores for all zones — add all stores for the store set matching the zone name (e.g. zone `QC EN` → store set `CP_QC`).

## Edit Details (preview)
- **Available dates:** 1 minute on the day it goes live (11:58 PM – 11:59 PM) per WBS.
- **Valid dates:** per WBS valid dates (e.g. Mar 1 12:00 AM – Mar 31 11:59 PM).
- **Internal Run Name:** `CP_Month Year Proof/Preview`.
- **Preview Start Date:** current time.
- **Hide in all Flipp apps**; Seasonal Theme = **No Theme**.
- **External Run Name:** EN → `Flyer`; FR → `Circulaire`.

### Hide-in-hosted trigger (before go-live)
- On the triggers page create a new trigger: Trigger on = Flyer Run; Action Type = Update Attribute; Attribute = Distribution Channels; add **Flipp Hosted** to the hide list; Run on = the day it goes live, 12 AM (must be before the available date/time).
- Send the link to the specialist for review.

## Go-live
- Store assignment as above.
- Edit Details: available dates 1 min on go-live day (11:58–11:59 PM); valid dates per WBS; **Internal Run Name** `CP_Month Year Go-Live`; preview start date = current time; No Theme; external run names Flyer / Circulaire.
- **Item Image QC:** no cutouts; image overrides for items without a PDF.
- **Thumbnails:** `thumbnail_1065_x_600` 3 pages; `stock_premium` 2 pages; `storefront_carousel_premium` 3 pages; `storefront_carousel_organic` 2 pages.
- **Tracking codes** are applied at flyer-type level — confirm they match.
- BD books budget ahead, so a flyer run shell is created; once TR completes go-live steps, clone into the flyer run shell. Assign review to the lead in the WBS Flyer Review tab.
- Send the preview email to the retailer (EN/FR horizontal + vertical preview links; a postal code is required to view). Note go-live assets due date.

## Common notes / risk items
- **Feed size:** the create-product-data run is scheduled by the specialist due to the large feeds; delete feed files after use.
- **Re-runs:** do not re-upload feeds when re-running — merchant ID + SKU list only.
- **Blank name fields** default to TBD; a missing **blank product data tab** for Tiderise must be created.
- **Zone → store set mapping** must match zone names exactly (e.g. `QC EN` → `CP_QC`).

---
*Source: Confluence "Bumper to Bumper SOP" (CP, 12198019113). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
