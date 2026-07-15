# Voila — CP Processing SOP

> **What this covers:** Content Production processing for Voila (Sobeys) —
> cookie/API data pull, story curation build (Wednesday), data formatter and
> product data build (Thursday), image ingestion, FSA assignment, tiles, and
> preview.
> Source Confluence page id: **12003377184** (CP space).
> Contacts/credentials intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 6057 |
| Flyer Type ID | 10594 |
| Slack channel | `#voila_mergil` |
| Validity | Thursday → Wednesday (make available from Friday for review) |
| Product counts | ON-EN/ON-FR = 130 products each; QC-EN/QC-FR = 106 products each |

## Data & workflow — what you need

- Data Formatter
- `[PROD]` Curation Sheet — Story Curation (templates) tab + Product Data tab
- Marketing assets (banners — largely the same week over week, with updates emailed)
- Template Selection (largely the same week over week)
- Voila Weekly Curation doc (URL info + curation direction for TR)

## Updating cookies

- API scripts run on a schedule. Only press the run buttons ad hoc if no data populated in the ON-english, ON-french, QC-english or QC-french sheets.
- If no data populated, the **`global_sid`** cookie likely expired. Go to `https://voila.ca/promotions/`, right-click → Inspect → Application → Cookies → `voila.ca`, copy the `global_sid` value into the "global_sid" page.
  - ON `global_sid`: no login needed if you are in the GTA.
  - QC `global_sid`: log into a Voila account set to Quebec (recommended in incognito; ON in non-incognito).
  - Recommended: paste the global_sid Wednesday afternoon and leave the browser session open so the cookie doesn't expire before the Thursday morning run.
- If not auto-run, click **"Pull data"** for ON or QC (~6 minutes each).

## Wednesday workflow — story curation

- Upload new weekly banners to the Voila Google Drive (sub-folder for the publication dates). Refer to the **'Publication Schedule'** tab in the Voila Weekly Curation doc for direction; the specialist notes required revisions.
- For a replaced asset (e.g. back cover): convert the image to PNG, upload to Cyberduck, and update the curation sheet (banner file name + associated URL).
- All banners are already in Lago unless the retailer provides a new version. Standard banner file names by version:
  - **V1** (ON/QC, EN/FR as noted): `CFC1_AcquisitionOffer_0-4Orders_FreeDelivery_Flipp_1737x600_EN` / `..._FR`
  - **V2:** ON `ON_1737x600-Header_BNR`; QC `QC_1737x600-Header_BNR`
  - **V3:** `NEW-ON_1737x600-Header_BNR_EN` / `_FR`; `NEW-QC_1737x600-Header_BNR_EN` / `_FR`
  - **V4** (different Page 1 template, own tab): `1737x2133-MainBannerA_CFC1_EN` / `_FR` (ON); `1737x2133-MainBannerA_CFC2_EN` / `_FR` (QC)
- TR builds the story curation sheet Wednesday; review it by EOD Wednesday.

## Thursday morning workflow — data formatter + product data

- Open the Data Formatter, check the **Info** tab: if "Last Run Status" shows today's date and "Ran Successfully", proceed; otherwise flag.
- **Categories** tab, Column K: all entries must be TRUE.
- In **'merged-data'**, copy/paste (as values, skip headers) into **'CP merged-data'**. Do not paste anything in column V (auto-populates). This copies to the **Condensed Data Formatter** tab.
- Copy from Condensed Data Formatter into the **Copy/Paste Here** tab as values.
- Ensure all items are on sale / have a sale story (except Farmboy and Longos — ON only, rarely on sale). Ensure EN CTAs = **Shop Now**, FR CTAs = **Magasiner**.
- In the **BABY** section (all 4 versions): delete all BABY items after the 6th, then change the Sale Story of the first 2 items under Health & Beauty to BABY → 8 BABY items total.
- Copy the data into the **'Product Data'** tab of the internal Curation document (as values). Download the Product Data tab as CSV.
- Run **Auto Image Processing** (mark off trim cropping). Voila **always uses Lago Image Ingestion Point 2** — flag in `#amp-system-support` whenever dropping images in Path 2.
- The Story Curation tab (finalized Wednesday EOD) → download as CSV.
- Once images are in, run **Generate and Process Merged Datasheets CA**.
- **Assign FSAs to all PZs:** `ON-english → ON-engligh Updated`, `ON-french → ON-french Updated`, `QC-english → QC-english`, `QC-french → QC-french`.
- Assign a preview date (select NOW). Validity Thurs–Wed (available from **Friday** for review).
- **Draw tiles:** `Stock Premium` (2 pages), `Storefront Carousel Premium` (3 pages), `Storefront Carousel Organic` (2 pages), `XW Thumbnail` (3 pages).
- Ensure all images are PDF, then assign the specialist to review.

## QC / review notes

- Ensure products on a page are not the same product in different sizes (e.g. a 405g and 1.4kg ground beef on the same page is a poor experience). If more than three duplicated products, modify the product data sheet and re-run.
- Assign review to the PL; once approved, send a preview to Voila. Send a second preview if there are changes, or wait for sign-off. Set live and post in `#voila_mergil` that the flyer is live and the tracker updated. (Previews: to view ON use an Ontario postal code; QC uses a Quebec postal code.)

---
*Source: Confluence "CP - VOILA SOP" (CP, 12003377184). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
