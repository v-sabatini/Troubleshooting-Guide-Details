# JCPenney — CP Processing SOP

> **What this covers:** The full/original Content Production processing SOP for
> JCPenney on the Agile Storefronts workflow, including the data-formatter path for
> filling missing product data, EN and PR (Puerto Rico) processing, image
> processing, Fadmin setup, tracking codes, and category-page inserts. Processed on
> LAGO 5.
> Source Confluence page id: `10789094290` (CP space).
>
> **Currency note:** This is the original/reference SOP. The streamlined current
> variant is `docs/processing-sops/jcpenney-cp-sop-en-pr.md` (id 11470209030), which
> links back to this page as the "Original SOP". Some linked recordings/overviews on
> this page are marked "updated Dec 2023" and note the Dataformatter steps have
> changed — follow the written steps below. Thumbnail specs on this page differ from
> the EN & PR SOP (2 pages here vs 3).
>
> **See also:** JCPenney OneGuide at `docs/retailers/jcpenney.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 2207 |
| Flyer Type ID | EN 11192 · PR 11193 |
| Slack channel | `#jcpenney_mergil` |
| Workflow | Agile Storefronts; processed on **LAGO 5** |
| Delivery | PDFs via Egnyte; EN Go-Live and EN/PR ECR also get an interactive preview |

## Assets
- **Retailer-supplied:** Story Curation xls (Curation Document, Product Data, Story Curation tabs); Marketing Assets (Banners, Product Images, Category page in the banners folder in the zip).
- **Working docs:** PROD Story Curation gsheet; File Re-namer (names product images as SKUs before Cyberduck); WBS; the Data Formatter.
- JCPenney assets download from Egnyte (you'll get an email); PDFs upload via the Egnyte upload link.

## Data formatter (Proof 1 — fill missing product data)
- Open the Data Formatter **SKU List** tab: fill cols B–D from the Story Curation tab in the xls, and col E with SKUs from the Curation Document tab.
- **If the ecom feed needs updating:** download `MARKET_DATAFEED_FULL_MMDDYYYYXXXXXX.txt.gz` from the JCPenney FTP (merchant 2207); double-click to generate the `.txt`; open in Excel; save as **.csv UTF-8 and add `$id=LOT_NUM`** before the `.csv` extension (e.g. `MARKET_DATAFEED_FULL_02022024040117$id=LOT_NUM.csv`); update the ecom feed name in the SKU List tab; upload to Cyberduck Lago 5 (30 min sync).
- Run the formatter via **Generate Ecomm Feed** (if it errors, log in and generate again).
- Copy the missing data (e.g. Brand and url columns) from the formatter into the xls Product Data tab.
- In the Product Data tab, adjust the Curation Document formula that creates the tiles columns: col E `=D2&".jpg"`; col F `="JCPW[week number]"&C2&".jpg"`.
- Adjust Ecom IDs to `="JCPW[week number]"&"[SKU]"`. If the same SKU is used multiple times, add an extra digit (`JCPEN1791969`, `JCPEN17919691`, `JCPEN17919692`).
- Add sale stories via `="Page-"&'Curation Document'!A2`. Highlight missing fields and save.
- (When re-ingesting a data file: download from Cyberduck, open in Excel without converting, save as CSV UTF-8 with `$id=LOT_NUM` added, re-upload to Cyberduck, update the file name in Data Formatter cell F1, wait for ingestion.)

## Processing

### Banners
1. Convert **banners** to 72dpi **PNG** (Universal Image Downloader); upload to Cyberduck in a separate folder.
2. The category banner can be left out here — it's converted to PDF and used as a last-page insert for go-lives/ECRs.

### Product images
1. Convert product images to 72dpi **JPG** — use the new **Universal Image Downloader**, running **only `convert_images_to_jpg`** (to ensure 72dpi; don't use other tools/formats). Images may still appear as `.jpeg` in Lago 5.
2. In the xls Curation Document tab: update F2 to `="JCPW[insert week number]"&C2&".jpg"`; drag E2/F2 down. Expected: col E `=[product image name]&".jpg"`; col F `="JCPW[week number]"&[sku]&".jpg"`. Verify the ecomm ID column includes the week.
3. Create tabs for `WKXX First/Submits/ECR Proof` in PROD story curation; copy product data and story curation from the JCP xls into the PROD tabs; download both tabs; run **Auto Image Processing** — only blank images should be those highlighted on the JCP xls.

### Generate merged datasheet
- Run **Generate and Process Merged Datasheet**: Merchant ID 2207; **EN Flyer Type ID 11192** (PR Flyer Type ID 11193); English Flyer Run ID only for EN Go-Live and ECR (WBS row 14).

## Fadmin — Edit Details (Proofs & Go-Lives)
- Adjust dates + preview day per the JCPenney WBS. For **Proofs**, set available dates back (no preview).
- Internal run name: `CP_Proof X/Go-Live/ECR WK_XXX EN/PR`.
- Visible: **Hidden Everywhere** (proofs); **Only Hosted** (PR Go-Lives/ECR); **Everywhere** (EN Go-Lives/ECR).
- Add a Customer Preview Day for Go-Lives/ECR. External run name N/A; Key Messages N/A.

### Pricing Zones & stores
- Pricing zone: **Base**.
- Stores: **English** — add all, remove the Puerto Rico store set; **PR** — `*Puerto Rico` store set.

### Sessions: clean images
- Item Cutouts; **PDF Image Auto Selection — Force Selection checked**.

### Images
- Uncheck Composites & PDF Images to reveal items without a clean session image. Click into the item, grab the image URL from the product link, apply it to the **Override Image URL** tagging field. Once clean, re-run **Page Level Tile Generation** in sessions, then **Page Stitching**.

### Thumbnails
- `thumbnail_1065_x_600` — 2 pages
- `stock-premium` — 1 page, include logo
- `storefront_carousel_premium` — 2 pages
- `storefront_carousel_organic` — first page, include logo
- `thumbnail` — 2 pages

### Tracking codes (flyer-run level; Go-live & ECR EN pre-created shells only)
Update the bolded week each time:
1. **Hosted 1** — Dynamic Variable / Hosted / `utm_source` / `flipp&cid=store%20ads|flipp|hosted|28B&utm_medium=store%20ads&utm_content=28B&utm_campaign=hosted`
2. **Flipp 1** — Dynamic Variable / Distribution / `utm_source` / `flipp&cid=store%20ads|flipp|app|31A&utm_medium=store%20ads&utm_content=31A&utm_campaign=app`
3. **Flipp 2** — Dynamic Variable / Distribution / `utm_source` / `flipp&cid=store%20ads|flipp|native|28B&utm_medium=store%20ads&utm_content=28B&utm_campaign=native`

### Category page insert (Go-live / ECR only)
- Add the category page to PR and EN go-lives at the end (supplied in the Banners folder; convert to PDF and manually upload in Fadmin). Copy items and images from a previous go-live run (EN and PR have different links), adjust box locations if needed. Add the page in the last position to the pricing zone.
- TR must also convert to PDF and add to Go-Live/ECR proofs: Category Page, Rewards Page, and (if applicable) the app price banner (`22 Viz Nav Category Page 1884 X 4260`, `21 Rewards Page 1884 X 4260`, `App Price Checker Mkt Banner W3 1884 X 387`). Copy tagging from a previous run.

## Delivery
- Download the pricing zone PDF, rename `WKXX EN/PR Proof X/Go-Live PDF`, upload via the Egnyte upload link.
- **Proof 1–2:** PDFs + upload confirmation only.
- **EN Go-Live and EN/PR ECR:** both the interactive preview and the PDF (include flags in the email if any).

## PR processing notes (REV / unique images)
- Update the xls ecomm ID with `WXX`, drag down — **do not override Ecomm fields containing "REV"**.
- Unhide Column A, select remaining columns → unhide all columns.
- Note the ecomm ID for all REV cells; each must match the image name in the PR unique image folder (e.g. `JCPBREV5` or `JCPW26BREV5`).
- Convert/upload banners to PNG; convert REV images to JPG (name matches ecomm ID), upload.
- Copy completed Product Data and Story Curation to the PROD template (name `PR WKXX First Proof` or `Go Live`).
- (Alternate flow) process as normal **except** always run the auto images custom action instead of converting+uploading images; convert/upload banners and backgrounds as usual.

---
*Source: Confluence "JCPenney CP SOP" (CP, 10789094290). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
