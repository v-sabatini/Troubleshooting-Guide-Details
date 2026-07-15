# JCPenney — CP Processing SOP : EN & PR Processing

> **What this covers:** The current streamlined Content Production workflow for
> JCPenney EN (national) and PR (Puerto Rico) processing on the Agile Storefronts
> workflow — asset intake, product data & story curation build, PR alternate
> images, image processing, Fadmin setup, tracking codes, category/rewards page
> inserts, and delivery. Processed on LAGO 5.
> Source Confluence page id: `11470209030` (CP space).
>
> **See also:** JCPenney OneGuide at `docs/retailers/jcpenney.md`, and the fuller
> JCPenney CP SOP (data-formatter reference) at
> `docs/processing-sops/jcpenney-cp-sop.md`.

## At a glance

| | |
|---|---|
| Merchant ID | 2207 |
| Flyer Type ID | EN 11192 (PR 11193 on the companion SOP) |
| Slack channel | `#jcpenney_mergil` |
| Workflow | Agile Storefronts; processed on **LAGO 5** |
| Delivery | PDFs uploaded via Egnyte; EN Go-Live also gets an interactive preview |

## Assets
- **Retailer-supplied:** Story Curation xls (Curation Document, Product Data and Story Curation tabs); Marketing Assets (Banners, Product Images, optional Backgrounds). Assets arrive via email/Egnyte.
- **Working docs:** PROD Story Curation gsheet; File Re-namer script (names product images as SKUs before Cyberduck upload); WBS (proof schedule + final EN go-live flyer runs).
- Upload the assets zip to the JCPenney Drive folder by week number and proofing round; rename the created folder **"RAW"**. Add the account to the Direct Processing Schedule (merchant details, link this SOP as processing notes, add yourself as reviewer).

## Processing

### Banners & backgrounds
1. Convert **banners** to 72dpi **PNG** (Universal Image Downloader); upload to Cyberduck banners folder.
2. Convert **backgrounds** to 72dpi PNG; upload to the banners folder.

### Product images (EN)
- In the retailer xls **Curation Document** tab:
  - Update the F2 formula to `="JCPW[insert week number]"&C2&".jpg"`.
  - Select E2 and F2 and drag down to apply to all rows. Expected format: col E `=[product image name]&".jpg"`; col F `="JCPW[week number]"&[sku]&".jpg"`.
- Create tabs for `WKXX First / Go Live / Go Live Final Proof` in PROD story curation. Copy product data and story curation from the JCP xls into the PROD product data / story curation tabs. Download both tabs and run **Auto Image Processing** for images — only blank images should be those highlighted on the JCP xls.
- No item image folders are required for EN — run the auto images custom action in CP Legacy after moving data to the PROD Product Data sheet.

### PR (Puerto Rico)
- Duplicate the EN product data or story curation tab and rename with **"PR"** in front.
- **PR alternate images:** in the images folder, note the file names; manually rename to add **"JCP"** to the start. When dragging down the Ecomm ID on the product data tab, **do not override cells that contain an alternate image name** — skip those cells and continue after them. Do not re-download images in cp-legacy; PR uses the EN images except for the overrides.

### ECOMM ID notes
- If the same SKU is used multiple times, add an extra digit to the ECOM Id (e.g. `JCPW221791969`, `JCPW2217919691`, `JCPW2217919692`).
- If the SKU column in the product data tab is blank, use SKUs from the Curation Document tab.

### Generate merged datasheet
- Run **Generate and Process Merged Datasheet**: Merchant ID 2207; Flyer Type ID 11192; Flyer Run ID — Proof 1 & 2 leave blank; **Go-Live** = the ID in WBS row 14 (column matches week number).
- **Review output:** in Pricing Zones tab click "view item boxes" to confirm no missing product images/banners (flag to specialist if any).

## Fadmin — Edit Details

### Proofs
- Internal run name: `CP_WKXXX Proof X`.

### Go-Live
- Adjust dates per the JCPenney WBS (column matches week number); add a preview date for **today**.
- Internal run name: `CP_WK_XXX Go-Live`; Visible **Everywhere**; External run name N/A; Key Messages N/A.

### Pricing Zones stores
- **NATIONAL:** add all stores, **remove Puerto Rico**.
- **PR runs:** add only Puerto Rico stores.

### Images (Proofs, Go-Lives, ECR)
- Uncheck Composites & PDF Images to reveal items without a clean session-extracted image; select PDF images for items with cutouts.

### Thumbnails (Proofs, Go-Lives, ECR)
- `thumbnail_1065_x_600` — 3 pages
- `stock-premium` — 2 pages
- `storefront_carousel_premium` — 3 pages
- `storefront_carousel_organic` — 2 pages
- `thumbnail` — 3 pages

### Tracking codes (flyer-run level; NONE on PR runs)
Add three codes; update the bolded week number (`28B` shown):
1. **Hosted 1** — Dynamic Variable / Hosted / `utm_source` / `flipp&cid=store%20ads|flipp|hosted|28B&utm_medium=store%20ads&utm_content=28B&utm_campaign=hosted`
2. **Flipp 1** — Dynamic Variable / Distribution / `utm_source` / `flipp&cid=store%20ads|flipp|app|28B&utm_medium=store%20ads&utm_content=28B&utm_campaign=app`
3. **Flipp 2** — Dynamic Variable / Distribution / `utm_source` / `flipp&cid=store%20ads|flipp|native|28B&utm_medium=store%20ads&utm_content=28B&utm_campaign=native`

### Category & Rewards page inserts (Go-live / ECR only)
- In the banners folder convert the category and rewards pages to PDF (last banners). TR must also convert to PDF for Go-Live/ECR proofs: Category Page, Rewards Page, and (if included) the App Price Checker banner — filenames like `22 Viz Nav Category Page 1884 X 4260`, `21 Rewards Page 1884 X 4260`, `App Price Checker Mkt Banner W3 1884 X 387`.
- Upload the rewards/category PDFs to the flyer run; mark "Flyer Creation" sessions complete; use the copy-pages tool to select Category Page from/to and Reward Page from/to → Submit. In the flyer run, Pricing Zones → Edit Details → Add Page (twice) → Save so the category and reward pages appear in the pricing zone.

## Delivery
- Download Low-Res PDF (Pricing Zones → more), rename `WKXXX Proof X PDF` / `WKXX Proof X PR` / `WKXXX Go-Live PDF`. Upload the PDF via the Egnyte upload link. Send the PDF and flyer run link to the specialist and fill in the FQC Checklist.
- Confirmation email — Proof 1 & 2: PDF uploaded via Egnyte only. Go-Live: EN preview link + PDF via Egnyte.
- Remove your account from the Direct Processing Schedule.

## PR processing notes (REV / unique images)
- Update the xls ecomm ID with `WXX`, drag down — **do not override Ecomm fields containing "REV"**.
- Unhide Column A, select remaining columns → unhide all columns.
- Note the ecomm ID for all REV cells; each must match the image name in the PR unique image folder (e.g. `JCPBREV5` or `JCPW26BREV5`).
- Convert/upload banners to PNG; convert REV images to JPG (image name matches ecomm ID) and upload.
- Copy completed Product Data and Story Curation to the PROD template (name `PR WKXX First Proof` or `Go Live`).

---
*Source: Confluence "JCPenney CP SOP - EN & PR Processing" (CP, 11470209030). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
