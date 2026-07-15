# Walmart CA Gaming Guide — CP Processing SOP : TIDERISE

> **What this covers:** TideRise (TR) processing steps for the Walmart CA Gaming
> Guide — converting retailer files into Story Curation + Product Data,
> image/banner ingestion, flyer creation, and Fadmin processing for Proof 1 and
> Go-Live.
> Source Confluence page id: **13231095811** (CP space).
> **See also:** Walmart Canada OneGuide in `docs/retailers/walmart-canada.md`.
> Contacts/credentials intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 234 |
| Flyer Type ID | 9152 |
| Go-Live | Thursday → Wednesday (spans 2 weeks) |
| Availability | Flipp / Distribution / Hosted: Available (exception: Proof 1 hidden on all platforms) |
| Cadence | No regular cadence; 5–6 publications per year |

Retailer-supplied assets: Banners, Item Submissions Sheet, Template Details. This SOP covers **Proof 1** and **Go-Live**.

## Pre-processing

You build the final **Story Curation** and **Product Data** sheets from the working sheet.
- Duplicate a previous **Product Data** tab and a previous **Story Curation** tab; rename both for the week/proof.
- **Important rule: do NOT modify or delete any columns with headings in red** — they contain formulas. You may delete the data in all other columns.

### Item Submissions → Product Data

- Open the retailer Item Submissions Sheet; confirm the correct tab (WK #, confirmed by the specialist).
- Copy product info into the Product Data tab by matching column headings. Keep in mind:
  - Do not modify/delete red-heading (formula) columns; paste only into non-formula columns.
  - The "Platform" column can be ignored.
  - The retailer's "Sale Story" column may be highlighted red but is not a formula column in Product Data, so copy it normally. Do **not** confuse it with **Column O – "sale_story"** in Product Data, which IS a formula column (red) and must not be edited.
  - From **Column P onward**, map badge values:

| Retailer Column | Product Data Column |
|---|---|
| Top Left Badge | Lago Custom 12 |
| Top Right Badge | Lago Custom 13 |
| Bottom Right Badge | Lago Custom 15 |

  - **CTA Text** → Column T (Lago Custom 16) AND Column U (Lago Custom 17) — same text in both.
- After copying, confirm all red-heading formula columns still have formulas on every row (drag down if missing).

### Product Image URLs

Retailers usually do not provide image URLs (required). For each SKU, either open the product page and Copy Image Address, or use the **Image Downloader** Chrome extension; paste into the Product Image URL cell.

### Template Details → Story Curation

- Clear existing data from **Columns B–L**; do NOT modify **Column A** (formula).
- Template Details lists Page Number, Template Name, and banner(s) per page. Build page-by-page in chronological order.
- Find each page's template in the **Template Library** tab (e.g. `WalmartCA-DOTW-Cover-08up-04`); copy/paste the layout into the Story Curation tab.
- **Page disclaimer:** replace "DATE – DATE" with the correct flyer dates.
- **Banners:** white (non-greyed) cells under **"Lago Custom 2"** require banners — enter banner names per Template Details.
- If URLs are provided in Template Details, fill the URL section, placing each link next to the appropriate banner to be tagged.

## Image ingestion

- Banners upload via **CyberDuck**. The specialist specifies **Lago 6A** or **Lago 6B** — banners and product images must be uploaded to the **same path**.
- Check banners are PNG with **trim cropping** applied; convert if not. Manually upload banners to the requested path.
- Product images: run the **Auto Image Processing** Custom Action in CP Legacy:
  1. Attach the CSV of the Product Data tab.
  2. **Merchant ID: 234**.
  3. Check off **Trim Cropping**.
  4. Select the correct **Lago Ingestion Point (6A or 6B)**.
  - ~20–25 minutes to ingest.
- **Important:** if production spans two or more days, re-run Auto Image Processing on each day you generate a new run (allow 20–25 min). Running once is enough if completed the same day.

## Flyer creation

Run **Generate and Process Merged Datasheets** in CP Legacy: **Merchant ID: 234**, **Flyer Type ID: 9152**, attach the CSV versions of the Product Data and Story Curation tabs.

## Fadmin processing — Proof 1

**Edit Details:**
- Available dates: set to the day feedback is due, for 1 minute (11:58 PM – 11:59 PM)
- Valid dates: actual go-live dates
- Preview start date: current time
- Hide in all channels except Flipp Hosted
- Internal run name: `CP [flyer name] - [Date of flyer Proof 1]` (e.g. `CP Gaming Guide - Feb 29 Proof 1`)
- External run name: `Gaming Guide`

**Hide in Hosted trigger:** set to hide in hosted 30 minutes before the available-from date/time.

**Pricing Zone tab:** spot check product images, details (pricing, description, CTA), and banners display correctly; flag anything off. **Store Set: `_CP_CDN_No QC_2`**.

## Fadmin processing — Go-Live

Repeat Proof 1 steps with these differences (refer to the WBS):
- Available From = Go-Live date in WBS
- Valid From = Pricing Validity date in WBS
- Available/Valid To = End Date in WBS

**Additional steps:**
- Item Image QC: ensure images are PDFs; capture image URLs if needed.
- **Thumbnails:** `thumbnail_1065_x_600` (3 pages), `storefront_carousel_premium` (2 pages), `storefront_carousel_organic` (3 pages), `xw_thumbnail` (2 pages).
- Notify the specialist when all tasks are done; the specialist handles tracking codes and remaining go-live steps.

---
*Source: Confluence "[TIDERISE] Walmart Gaming Guide SOP" (CP, 13231095811). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
