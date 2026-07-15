# Retailer Processing SOPs — Content Production (CP)

> The Content Production team's per-retailer processing SOPs (distinct from the Vendor OneGuide retailer guides). Contacts/credentials omitted.

**Contains:** Bumper to Bumper — CP Processing SOP;Club Piscine — CP Processing SOP Dulux — CP Processing SOP : Tiderise (V-TR);Grocery Outlet — CP Processing SOP Home Depot CA — CP Processing SOP;Home Depot US — CP Processing SOP [2026] JCPenney — CP Processing SOP : EN & PR Processing;JCPenney — CP Processing SOP Patrick Morin — CP Processing SOP;Sail — CP Processing SOP : V-TR (TideRise) Staples Canada — CP Processing SOP;Staples Canada — CP Processing SOP : Tiderise Previews & Go-Live Clones Tanguay — CP Processing SOP;Voila — CP Processing SOP Walmart CA Flash Deals & Spotlights — CP Processing SOP : TIDERISE;Walmart CA Gaming Guide — CP Processing SOP : TIDERISE Walmart US — CP Processing SOP;Well.ca — CP Processing SOP : AMP

---

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


---

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


---

# Dulux — CP Processing SOP : Tiderise (V-TR)

> **What this covers:** The Tiderise (TR) Content Production processing workflow for
> Dulux (bilingual EN/FR, Agile Storefronts) — asset intake, Cyberduck banner &
> product-image handling, product data + story curation build, Fadmin Edit Details
> with proof triggers, QC, and file delivery. Processed on LAGO 5.
> Source Confluence page id: `13315833857` (CP space; page titled "CP Dulux
> Processing SOP V-TR").
>
> **See also:** no Dulux OneGuide currently exists in `docs/retailers/`.

## At a glance

| | |
|---|---|
| Merchant ID | 4322 |
| Flyer Type ID | 12325 |
| Slack channel | `#dulux-amp-production` |
| Workflow | Agile Storefronts; processed on **LAGO 5** |
| Dataformatter | CA Create Product Data |

## Assets
- **Retailer-supplied:** Marketing Banners & Custom Product Images; Story Curation & SKU List.
- Download assets from email (or receive from the CSI contact) and upload to the Dulux Google Drive.
- Schedule processing in the Direct Processing Schedule (refer to WBS for the day).
- Use the complexity checklist to set the complexity level; if a selected checkbox turns red, add a 🌶️❗️ status to that section (it involves steps not recommended for TR).

## Cyberduck

### Banners
1. Convert all banners to **72 dpi PNG** in the ImageDownloader app.
2. Upload to Cyberduck `Dulux > Assets-Banners`.

### Product images
1. Upload converted/renamed product images to Cyberduck `Dulux > Assets-Product Images`.
2. Run **Auto Image Processing** custom action (**.png and trimming** applied) using the product data created below to upload the rest of the images.
   - You'll get a no-reply email if any images failed. For a flagged image: if the URL works and shows the image, download it manually, convert to `.png`, rename to match the EcomID, upload manually to Cyberduck. If the URL is broken, note the EcomID and send it to the specialist with your review notes.

## Product data
1. Run the **Create Product Data** custom action to receive the Product Data CSV by email.
2. Open the CSV in Google Sheets and paste **Values only** into the Product Data tab of the Story Curation gsheet (cell A2).
3. Scroll to the bottom of the EN data and repeat for FR data, pasting as values only (a coloured border helps separate EN from FR).
4. Check every item has a **"name"** value — add **"TBD"** as a placeholder if needed.
5. Check all current and original prices are in `0000.00` format (no commas or spaces).

## Story curation
1. Open the Story Curation xls; copy everything from the **Page** column in the **EN Curation** tab.
2. Paste **as values** into the Story Curation tab of the Story Curation gsheet (cell B6).
3. Scroll to the bottom and repeat for FR data, pasting as values under the EN data (coloured border to separate).
4. Add **"EN"** in column L for the English data and **"FR"** for the French data.
5. Ensure sale story formats match between the Product Data tab and Story Curation — typically `Page-X` and `Page-X FR`.

## Generate merged datasheet
- After all product images and banners sync in Lago, run **Generate and Process Merged Datasheet**: Merchant ID 4322, Flyer Type ID 12325, Flyer Run ID blank.
- Review output: if banners are missing, check whether the image name matches the received/uploaded asset in Lago; if product images are missing, check the name matches the Product Images folder asset or that the Product Data has a Product Image URL. Note any retailer-data misses for the specialist.

## Fadmin — Edit Details
- **Available dates** (per Workback Schedule):
  - **Proofs 1–2:** available-from through when the next preview files are due from SAIL, at 11:58pm; available-to same day at 11:59pm.
  - **Go-Live:** available and valid dates are the same (the "Go-Live" row).
- Set **valid from/to** to the Go-Live dates.
- **Internal Run name:** `CP_[Valid From Date] Proof #/Go-Live`.
- Preview date = today; **No theme**.
- **Distribution:** Proofs 1–2 → hide on all platforms but Hosted; Go-Live → not hidden anywhere.

### Triggers
- **No triggers needed for the Go-Live Preview.**
- **Proofs:** on the triggers tab, under "Create new Trigger" set Attribute → **Hide in Hosted**; Run At = same day as the **Available from** date at **11:30pm** (hides everywhere before it would go live). Create the trigger and confirm it appears under Current Triggers. Add a comment note to yourself.

## QC
- Add all stores.
- **Images:** uncheck Composites & PDF Images to reveal any without a clean session-extracted image; select PDF images for items with cutouts; use the **Image Override URL** field in tagging to add an image URL if a clean image is missing.
- **Thumbnails (Proofs, Go-Lives, ECR):** `thumbnail_1065_x_600` 3 pages; `stock-premium` 2 pages; `storefront_carousel_premium` 3 pages; `storefront_carousel_organic` 2 pages; `thumbnail` 3 pages.

## Delivery
- Download Low-Res PDF (Pricing Zones → more), rename to the flyer run name without `CP_` and note language (e.g. `March 30 Preview 1 EN`); repeat for FR.
- Send the PDF and flyer run link to the specialist in Slack with your notes (troubleshooting done, SKUs with placeholders, missing items/banners) and fill in the FQC Checklist.
- QC the run in the FQC checklist (spot-check items xls vs PDF/flyer run; spot-check banners/product images from the RAW folder; for go-live also check thumbnails, PDF images, tracking codes, category page, preview). Request revisions if needed.
- Remove your account from the Direct Processing Schedule and send the confirmation email with PDFs.
- **Note:** this account will not have interactive previews to share externally until hosted is set up.

## Retailer-specific troubleshooting
- N/A (none documented).

---
*Source: Confluence "CP Dulux Processing SOP V-TR" (CP, 13315833857). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Grocery Outlet — CP Processing SOP

> **What this covers:** Content Production processing for Grocery Outlet (GO) —
> the current Monday/Tuesday Genesis workflow (custom action report, image
> ingestion, upload, inserts, grid processing, FSA checks, Fadmin) and the DVM
> asset/custom-action process.
> Source Confluence page id: **8666612155** (CP space).
> **See also:** Grocery Outlet OneGuide in `docs/retailers/grocery-outlet.md`.
> Contacts/credentials intentionally omitted.
>
> Note: the page also retains a "DNU! Monday Processing – Old Process" section
> (superseded); that legacy flow is intentionally not reproduced here.

## Account at a glance

| | |
|---|---|
| Merchant ID | 2906 |
| Flyer Type (Genesis) | 3435 |
| Validity | Wednesday → Tuesday |
| Slack (system) | `#amp-system-support` |
| Slack (DVM) | `#wg-grocery-outlet-dvm-flyer` |

## Monday processing (2025/2026 update)

### Run the custom action

- Start work at 1pm. In CP Legacy, run **'Grocery Outlet Report V3'** (5–10 minutes).
- Project name: `GO (flyer run ID) - (Date)` e.g. `GO 875717 - June 28`.
- Select the **CP GENESIS** flyer run (correct Flyer Type with "CP GENESIS" in the name, correct run dates). Provide the flyer available-from/to dates spelled out (e.g. `June 28, 2023- July 4, 2023`; use short forms for long months, e.g. Dec). Ensure dates are Wed–Tues.
- On completion an email arrives; download both `.csv` files.

### Downloading images (new process, Apr 2026)

- Open both `.csv` files as Google Sheets.
- In CP-Legacy, select **'auto image processing'** custom action; attach the images `.csv` in the 'Product Data CSV' spot.
- Message in `#amp-system-support` (@here + @csdelivery) ~15 minutes before running, stating the time and ingestion point (e.g. "I am dropping GO images in ingestion point 2 in 15 minutes").
- Select **ingestion point 2** (unless told to use point 1 by the team). Click **run action**.

### QC data

- The custom-action email lists flags. Alert the processor if any Item Names are flagged. **Empty brand can be ignored.**
- Any stores showing "removed due to less than 5 items" must be flagged to the processor with final assets.
- Rename the results `.csv` as `GO Datasheet MMM DD` (e.g. `GO Datasheet Dec 17`), download as `.xls`, and send to the processor with the images `.csv` and any removed-store flags.

### Checking stores (while report generates)

- Open the grid `.xls` from the GO FTP (`.../merchants/2906/ftp_files`); use the latest file, check for REV files.
- Filter column B for blanks, delete blank rows, unfilter.
- Filter column M (Genesis) for "no" — those are typically new stores that go live one day later (handled Tuesday). Record store numbers that are not found to flag to the processor.

### DVM assets

Upload the GO Datasheet, folder of PDFs from Cyberduck, and grid XLS to the GO Weekly Files drive in a folder `MMM DD DVM Assets`. Once the processing version of the grid is created (Tuesday), add it in `.csv` format.

### Upload process (Aug 2025)

- Once images are in, run Custom Action **"Content Production Flyer Creation"**: flyer type `3435`, current week's flyer run ID, GO Datasheet xls saved as CSV.
- **Set trigger for 9pm.** Check Lago Explorer (~10 min after) that automats picked up the job. If the run stalls, cancel the job, verify cancelled in LAGO, and restart (stalls occur when too many jobs run at once).

## Tuesday processing

- Flyer run should be ready by 9am. Confirm all sessions ran and pricing-zone images populate.

### Add inserts

- In the Flyer Run → Pages tab → Edit; open the go-live-dated folder, select all pages (expand all arrowed sections), Select Files, capture revised files, Add pages, Save and complete, let sessions run.

### Copy PDF tagging

- In the Processing-Only flyer run (created by Ops) → Pages tab → Copy items → add the CP run's flyer run ID as Destination.
- Back in the original run, confirm everything boxed/tagged correctly. **Ensure tagging is correct on loyalty/cover pages.** Verify PDFs are not jumbled/layered incorrectly; check the live/previous run for additional insert-page tagging.

### Grid processing

- Manipulate the grid `.xls`. Duplicate the first tab → rename **Processing** (or Processing 1 if multiple). Filter column B (stores) for blanks, delete blank rows. Change Page # to **Cover Page** (including the email sign-up page), delete all columns after end date and the URL columns (Genesis column can stay). Download the Processing tab as CSV.
- Run **Custom Action – 'grocery outlet insert pages'** (on the original custom action page, not CP-Legacy) with this CSV + flyer run ID. Let sessions run; spot-check pricing zone layout. Create Processing 2, 3 tabs and triggers for pages that come down/up on other days.
- **Light PDF weeks** (e.g. only loyalty page + coupons/covers/sale inserts for select stores): use the layout tab instead of the custom action — insert the "download the deals" page in last position (position 10) for all stores, and note store/zone-specific extra pages (typically position 1).

### Check FSAs

- Pricing Zone tab → Stores/FSAs; sort smallest-to-largest. If any are 0 (typically 2 stores), find the store zip in the grid, find the other store with the same zip, then run custom action **"Fsa Swap"** (from 443 to 469, using those store IDs and `91006` as the FSA).
- Remove unwanted ZIPs via custom action **'remove FSAs'** (Flyer Run ID, no Pricing Zone ID, paste the EAST ZIP list into 'FSAs to Remove').

### Fadmin processing

- Item Image QC — cutouts only if the image is not clear. If clean images are not loading, re-run datapiping, then PDF image extraction at 0x0, then choose all pages and force selection.
- Mark items in store only; check leg. heights.
- **Draw the 5 tiles** (also press Mark Complete): `Thumbnail 1065x600`, `Stock_premium`, `Storefront_carousel_premium`, `Storefront_carousel_organic`, `xw_thumbnail`. (Rarely there is a custom tile.)
- No toggles hidden and no theme (for hosted-only, hidden in Flipp). Spot-check horizontal and vertical preview.
- Notes: every pricing zone has 1 store only; each has the email sign-up page in last position; minimum 6 items; Grand Opening stores start 1 day later; Flyer Sorting — Weekly Ad in 1st position ahead of any standalone ads. New stores without genesis pages / few cover-inserts go hosted-only (staggered dates if enough items to go live on both).
- Complete the verification list on the GO HQ sheet (PDF layering, FSAs fixed, store count, grand-opening stores, triggers applied).

## DVM process

- Upload datasheet + grid XLS to a `MMM DD DVM Assets` folder; add the processing CSV (all versions/tabs). Update the GO team in `#wg-grocery-outlet-dvm-flyer` with expected page/layout changes.
- Once all main-run processing is complete, set triggers:
  - **'Grocery Outlet Publish DVM'** custom action for 12:01am (main-run flyer run ID + the same GO Datasheet CSV; 2–8 min).
  - **'Grocery Outlet Insert DVM Sections'** custom action for 12:05am (flyer run ID + processing version of the grid CSV).
- **DVM error playbook (monitor):**
  - "Failed due to no genesis pages" (lists store number) — happens when the grid says "yes" under Genesis but the store has no genesis pages (no data uploaded). Fix: on the processing tab, find the store and change Genesis to "No".
  - Fails if a filename on the grid is missing its extension — ensure all files include `.pdf`.
  - Fails if there are duplicate pages within one store (one row = one store).
  - Flag unresolved failures in `#wg-grocery-outlet-dvm-flyer`.

---
*Source: Confluence "Grocery Outlet SOP" (CP, 8666612155). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Home Depot CA — CP Processing SOP

> **What this covers:** Content Production processing for Home Depot Canada (DIY
> and the currently-paused PRO publications) — asset prep, banner validation,
> Snicket callsheet generation, Fadmin flyer creation, and proof/go-live steps,
> with the retailer-specific Snicket/Fadmin error playbook.
> Source Confluence page id: **8970174469** (CP space).
> **See also:** Home Depot Canada OneGuide in `docs/retailers/home-depot-canada.md`.
> Contacts/credentials intentionally omitted.

## Account at a glance

| | DIY | PRO (**PAUSED**) |
|---|---|---|
| Cadence | Weekly | Bi-weekly |
| Go-Live | Wednesday (Valid Thursday) | Wednesday (Valid Thursday) |
| Merchant ID | 236 | 236 |
| Proofing Flyer Type ID | 10917 | 9650 |
| Go-Live Flyer Type ID | 9770 | 9274 |
| Merchant Identifier | homedepotcanada | homedepotcanada |

Cyberduck path: `/flipp-snicket/production/1000236/Assets` (passwords/keys obtained per the internal guide — not stored here).

## Types of processing

Each publication week: **First Proof → Final Proof → Confirmation Proof → Go-Lives** (Tuesday retailer preview, Wednesday public preview, Thursday valid).

## Assets

Received via SharePoint (retailer emails notification + link; confirm receipt). Expected: Marketing Datasheet Excel (2 tabs — Main MDS + Marketing Variation Datasheet), marketing banners in JPG (EN + FR), and an XML file. Organize on the Google Drive.

- Convert banners to **72 DPI**: copy into the Universal Image Downloader `images` folder → `convert_images_to_jpg` → converted files land in `images_jpg`.
- If needed, rename banners from `.jpg.jpg` to `.jpg` (find `.jpg.jpg` / replace `.jpg`).

## Marketing Datasheet (MDS) prep

- Delete rows 1–4 and the English/French Template Selection rows.
- Ensure: Pagination (Column A) consecutive; Template size (Column C) matches Template used (Column B) — e.g. `End_09up_02` = size 9; **AdBanner templates have size 0**; Filenames (Column E) contain ".jpg"; Document Template (Column G) and Language (Column H) filled correctly — EN `THDCA-2020-EN-007`, FR `THDCA-2020-FR-007`.
- Repeat for the Marketing Variation Datasheet (MVDS). Ensure MVDS market names (Column A) match the 'Market Reference List' tab.

### PM_AR_ONTARIO_NRTH_1 (single-store breakout)

Store 7102 (PM_AR_ONTARIO_NRTH market) is sometimes broken out as `PM_AR_ONTARIO_NRTH_1`. There is no automatic workflow for single-store breakouts:
- Ensure the page this market is assigned to does not also include a variation for PM_AR_ONTARIO_NRTH. If there is no variation, delete the `-1` from the market (page breaks out into PM_AR_ONTARIO_NRTH; adjusted manually in Fadmin during FQC).
- If the same page already has a PM_AR_ONTARIO_NRTH variation, check whether another market matches the AR-1 banners; if banners match another market (e.g. AG/AD), Lago already produces the page — leave AR-1 as is.

### Banner validation

Use the Banner Validation sheet: paste MDS Master (and Variation) banners into col. A, remove duplicates, sort A–Z; paste the actual `.jpg` filenames into col. B (via an email draft to strip images). Conditional formatting turns matching cells green. White cells in col. A = missing `.jpg` banners; white cells in col. B = received files not on the MDS. Reach out to the retailer for clarification / revised assets. Download both tabs as CSV.

## Snicket

Run the **'Create Home Depot Canada Callsheet'** custom action in CP Legacy (Master + Variation tabs, unzipped XML, converted banners). Project name `HDCA WKXX First/Final/Confirmation Proof or Go Live`. Flag in `#amp-system-support` before dropping images. A callsheet and error log generate.

In Snicket (VPN required), **Create Snicket Run**:
- **Merchant:** Home Depot Canada PMR
- **Publication Run Name:** `CP_DIY_WK#_[Proof # or Go-Live]`
- **Publication Type:** DIY = `cpdiy`; PRO = `cppro`
- **Available / Valid Date Range:** set to one day prior
- **Preview:** DO NOT CHECK OFF
- Drop banners into the Banner Drop area, then upload MDS, MVDS, and XML; click **Go**.
- On successful run, download the callsheet from the **DN** stage. Once DN completes, product images and banners auto-ingest into LAGO — verify ingestion before running the Fadmin custom action.

### Snicket / callsheet error playbook

- **Proofing runs** can contain missing product name and image errors; **Go-Live runs cannot** — reach out to HDCA if encountered on a go-live. **AdBanner templates** produce a "No offers found for page" error that can be ignored.
- **PAM stuck at 49–50%:** check page numbering — a 1-page flyer sent as "Page 5" must be corrected to "Page 1".
- **XML errors:** flagged within Snicket stages (XML cannot be opened directly); communicate to HDCA, send the error log, request a revised XML.
- **DV is RED ("invalid value"):** download the .csv error log; strange characters sometimes appear at the end of URLs (invisible in Google Sheets — open the .csv to delete them). **Do NOT save** the .csv — **Save As** a new .csv prefixed `REV_` and re-upload at the DI stage. If Snicket keeps flagging, create a new run and upload the REV files.
- **PAM is Yellow:** "Failed to retrieve image from API" (broken image URLs in the XML). Proofs may still run the callsheet (send the error log with the proof); go-lives cannot — request a new XML.
- **PAM is RED — "Missing marketing assets":** spelling mismatch between `.jpg` files and the .csv. Common fixes: banner names in datasheet need a dot before jpg (`.jpg`); banners all in jpg (some sent as `.jpg.png` — remove `.jpg` and convert); banners with only one jpg (`XXXjpg.jpg` → remove the first jpg); lowercase `k` in WK (fix in MDS/MVDS).
- **DN flags:** *Placeholder Image Used* (ignore on proofs), *Offer missing in page* (send to HDCA on both proof and go-live), *Missing Image* (ignore on proofs, send error log with proof), *No Offers found for Page* (AdBanner — ignore on both; no need to send if it is the only error).

## Fadmin processing

**Optional — Category Validation:** use the Category Validation doc to verify callsheet categories exist on the merchant page; add any non-green (Column B) categories to Fadmin. If categories are missing, the run errors out (log names only the first missing category — validate all before re-running).

**Callsheet manual edit:** remove `??` symbols from the Name column (Column G) via Find and Replace (typically 255–600 instances); download as CSV again.

1. Custom Action **"Content Production Flyer Creation"**: paste the Flyer Run ID (from 'Flyer Runs' tab), use the correct flyer type (separate types for DIY Proofing, DIY Go-live, Pro Proofing, Pro Go-live), Store Codes N/A, Store Set ID N/A, upload the Snicket callsheet.
2. Backend generates Layout/Output/Image files through Lago; pages pull into the flyer run and pricing zones generate (go-lives can take up to 1 hour).
3. Once sessions run and auto-tagging completes, start FQC.

### Fadmin error playbook

- **Store Items Collector failing** (all stores): an incorrect raster position was used for a template in the MDS. The first line of the error log names the template & raster (e.g. `Inside_9up_02`, raster `910`). Verify template name = filename; verify the correct raster via the Template Document / master MDS / latest PDF; change or delete the raster on `THDCA_MarketingDatasheet.csv` and re-run Snicket for a new callsheet. Note: raster 800 is the background image and should exist on all templates — escalate to solutions/design if missing. Fadmin flags these one at a time.
- **Multiple item blocks missing at end of page:** items out of stock — ask the retailer to update availability or replace.
- **An item block is missing:** check Lago 5 comosoft jobs. Error "value is too large for column Comosoft Art Artbezc" = product name too long (max 80 chars; after 63 the system uses "…") — request the retailer shorten the name. If jobs did not fail, try re-running files and escalate to solutions.
- If rows/columns below data are flagged, select all entry cells and clear them.

## Proofs & Go-Live setup

- **First & Final Proofs:** hidden in Flipp, Distribution, and Hosted (only PDF pages sent to retailer); set the date in the past after exporting PDFs. Dates per WBS (Available = live 1 minute on the feedback/asset-delivery date; Valid = actual live dates). Internal name `Proof_Pro/DIY_WK # Proof`.
- **Confirmation Proof:** distribution Flipp + Distribution ON, Hosted OFF (Hosted must not be hidden for the vertical preview link — set a trigger to hide in hosted the day before "live"). Has a preview; go-live also has a preview.
- **Go-Live:** dates per WBS (Available Wednesday, Valid Thursday); available on all platforms; Internal name `CP_Pro/DIY_WK # Go-Live`; External run name DIY EN `Weekly Flyer` / FR `Circulaire hebdomadaire`, PRO EN `PRO Flyer` / FR `Circulaire PRO`.
- **Thumbnails (Go-Live):** `thumbnail_1065_x_600` (2 pages), `stock-premium` (1 page, include logo), `storefront_carousel_premium` (2 pages), `storefront_carousel_organic` (first page, include logo), `xw_thumbnail` (2 pages).
- **Tracking codes & URL (Go-Live):** apply all tracking codes; add the tracking URL (always the same, Open + Flipp App): `https://ad.doubleclick.net/ddm/trackimp/N226602.2123309FLIPPCOPORATION/B22239215.238551047;dc_trk_aid=435809340;dc_trk_cid=111475379;ord=[[randomn]];dc_lat=;dc_rdid=[[unhashed_device_id]];tag_for_child_directed_treatment=;tfua=?`

### Live Goods & Inserts (Go-Live, if applicable)

OS manually boxes/tags inserts and live-goods pages. On the Friday before go-live, create a new flyer run in the **CPPROC (11731)** flyer type with `TAGGING` in the internal run name (hidden on all platforms; Avail/Valid = the go-live Wednesday; preview = the Tuesday before). Upload live-goods/insert pages, run sessions (apply French to FR pages), mark Flyer Creation complete (no pricing zones needed), mark Setup QC complete. Attach the linking document to all vendor tasks (create your own directing OS to tag EN/FR products with the HDCA homepage if none provided). Once OS finishes, upload the pages into the main DIY/PRO flyer, copy boxes from the tagging run, and insert pages into the corresponding pricing zone/position.

### AR-1 pricing zone (all proofs & go-lives)

If there is a `PM_AR_ONTARIO_NRTH-1` market, Fadmin generates `AR-1_en` / `AR-1_fr` zones (banners only, no product info); create them manually if not auto-generated. Copy layouts from `AR_en`/`AR_fr`; swap AR-1-specific pages with the National pages (confirm national page titles via `AA_en`/`AA_fr`). On go-lives, if there was no PM_AR_ONTARIO_NRTH-1 version, add the AR-1 store set to `AR_en`/`AR_fr`.

### Item Image QC (Confirmation Proof & Go-Live)

Uncheck PDF Images to reveal items without a clean image; open the product link and apply the image URL to the **Override Image URL** tagging field. If that fails, search the SKU in the Item Img QC field, or reuse a PDF image URL that generated for the same SKU in another version; last resort, use the "Upload Files" section under Flyers. Clean images can take ~20 min to appear in preview.

### P1 single-item marketing banners (DIY Go-Live)

P1 banners with single items must be switched to item types and tagged with product info. Multi-item **BLOCK**-format banners must also be tagged as items: redraw boxes, tag each item as an item type, copy the main block URL to all products. Multi-item callout banners (non-block) can be left alone. A Jira ticket can be filed for the CP co-op to manually box/tag (provide the market list from the Marketing Variation tab).

---
*Source: Confluence "Home Depot CA CP SOP" (CP, 8970174469). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Home Depot US — CP Processing SOP [2026]

> **What this covers:** The Content Production processing workflow for Home Depot US
> CON (Consumer) and PRO (Professional) dynamic ads on the Legacy/Snicket workflow —
> asset intake, Snicket runs, the Generate Home Depot USA Callsheet custom action,
> Flyer Creation, previews/failsafes/go-lives with daily refreshes, one-pager
> inserts, store setup, post-processing revisions (page-removal logic), and the
> Flex/Co-op morning QA.
> Source Confluence page id: `11993514005` (CP space; page titled "Home Depot US
> SOP [2026]").
>
> **See also:** Home Depot USA OneGuide at `docs/retailers/home-depot-usa.md`.
> Retailer troubleshooting: HDUS Troubleshooting Guide (Confluence CP 11997315103).

## At a glance

| | |
|---|---|
| Merchant ID | 2135 |
| Flyer Type ID | CON 6120 · PRO 6284 · Standalone 1 (one-pagers) 9976 |
| Store Set ID | CON 251177 (CPNationalCON) · PRO 251178 (CPNationalPRO) |
| Slack channels | `#homedepotus` (account team), `#amp-hdus` (morning QA) |
| Workflow | Legacy — Snicket + Flyer Creation custom action |
| Volume | PRO ~52 flyers/yr (4–5 pages); CON ~30 flyers/yr (6–12 pages, goes dark in some periods) |

## Weekly schedule

| | PRO | CON |
|---|---|---|
| Preview | Wed EOD / Thu morning | Mon EOD |
| Failsafe | Thu 7:00 PM | Tue 7:00 PM |
| Go-Live | Mon 4:00 AM | Thu 3:30 AM |
| Daily refreshes | Daily 4:00 AM | Daily 3:30 AM |

- **Preview dates:** Available window 1 min (e.g. CON Thurs 12:00–12:01 AM); hide on Flipp & Distribution.
- **Go-Live / refresh:** full 24h available (CON 6:00 AM–next 5:59 AM, PRO 7:00 AM–next 6:59 AM); show all; refresh triggers PRO 4:00 AM / CON 3:30 AM.

## Data & workflow
- **Datasource:** the HDUS API pulls product info. Datasheets: the **Market Asset Sheet** (page structure, templates, banners) and the **Product Category Sheet** (product OMSIDs). HDUS should provide **national** OMSIDs.
- **Versioning:** max 1000 pricing zones. Number of versions depends on store-level item availability and page de-duplication. **Page removal logic:** 100 pages/pricing-zone and 1000 pricing-zone limits — when pricing fluctuation pushes past 1000, the page(s) with the most pricing variation are removed and HDUS is asked for new national SKUs.

## Processing

### Folder setup
- In the CP drive: `HomeDepot USA > Assets from THD > Consumer Ad/Professional Ad`. Create a folder with the date + publication type (CON or PRO), with subfolders **Input, Output, RAW, Images**.

### Sheets & raw files
- Monday: the HDUS contact emails "Consumer/PRO Dynamic Ad Upload" — download the Product Category Sheet & Market Asset Sheet, open in Google Sheets.
- Download this week's asset folder from the HDUS OneDrive (verification links in the HDUS Toolbox; request a new link from HDUS if expired). Drop asset folders into RAW.
- In RAW there should be **PODS** and **Headers & Footers** folders — convert all those images to **72 DPI JPG**. Rename images to match the Market Asset Sheet banner names (e.g. capitalize `pro`; add/remove a leading zero on single-digit months like `02.03_Page1_Hero` vs `2.03_Page1_Hero`).
- Open the HDUS PDF mock-up and confirm banner images match; confirm all category banners have text callouts (flag to specialist if missing).

### Market Asset Sheet
- Delete extra columns/rows. Confirm banner names match the banner image files (names include `.jpg`). Confirm the fiscal week column is updated. Compare each page's template to the mock-up.

### Product Category Sheet
- Delete extra columns/rows; delete "Drop" from the "Ad Drop Date" header. Confirm the page count matches the Market Asset Sheet (insert pages have no items and aren't included). Remove duplicate OMSIDs (Column E → Data → Data cleanup → Remove duplicates); if an OMSID is removed, update the Column C ordering.

### Upload sheets
- Download both as CSV to the Input folder, renamed `market_asset_sheet` and `product_category_sheet`.

### Snicket
> Before processing, confirm in `#cp-concierge` that no one else is ingesting images while HDUS processes (Snicket ingests 1000+ images afterward and can delay others).
- Connect to VPN, go to Snicket, **Create Snicket run:** Merchant `Homedepotusa`; Publication name `Date - Preview - CON/PRO Dynamic Ad` (e.g. `2.20 - Preview - CON Dynamic Ad`); Publication Type Flyer; dates = live dates for the week. Create run.
- Upload banner images to **Marketing assets** under Data Ingestor. Drag the market asset sheet, product category sheet and template coordinates into **Run Asset Inputs**. Press **Go**.
- **Download output:** `snicket_backfill.csv`, `snicket_call_sheet.csv`, `Snicket_HDUSA_Master_Image_List_PROCON.txt` → into the Output folder. Rename the call sheet `DATE_PRO/CON_snicket_call_sheet`; remove PRO/CON from the Master Image List name per the publication. In the call sheet, filter "Image Exists" and confirm **no products are Not Found** (if any, see the troubleshooting guide → Call Sheet Errors → Image Exists - Not Found). Upload the Master Image List to the Comosoft Import in Cyberduck.

### Generate Home Depot USA Callsheet custom action
- Run the **Generate Home Depot USA Callsheet** action in CP-legacy: choose the Market Asset Sheet and Product Category Sheet for the run; Marketing assets = all images in the run's Images folder; use **Image Ingestion Point 2** and flag in `#amp-system-support` before dropping images / running.
- On success you get a no-reply email — download all attachments (Master Image List, Callsheet, Backfill, Image List) to Output. Rename call sheet and Master Image List as above; confirm Image Exists has no Not-Found; upload the Master Image List to Comosoft Import in Cyberduck.

### PRO-only call sheet modifications
- In the Call Sheet (banners in Column H) rename (casing exact):
  - `Pro_header.jpg` → `NEW-Pro_header.jpg`
  - `Pro_LDT_Header.jpg` → `NEW-Pro_LDT_Header.jpg`
  - `Pro_delivery.jpg` → `NEW-PRO_delivery.jpg`
  - `Pro_THD_logo.jpg` → `NEW-Pro_THD_logo.jpg`
- In the Master Image List (text editor) make the same replacements **without the `.jpg` extension**. Drop both files into the PRO run Output folder; re-upload the Master Image List to Cyberduck.

### Flyer run shell & processing preview
- Specialists create go-live/preview shells; for a preview, the flyer run ID is shared in advance.
- Create a preview flyer run: Available From = day before go-live 11:58 PM, Available To = day before go-live 11:59 PM; Valid From = now, Valid To = go-live day; Internal Run Name `Go-live Date - Preview - Con/Pro Dynamic Ad`; toggles **Hidden on distribution + Hidden on Flipp**.
- In CP-Legacy → **Flyer Creation:** Flyer Run ID = preview shell; Flyer Type ID CON 6120 / PRO 6284; **Store Codes 121**; attach the callsheet. Run.
- **Fadmin:** QC items/images; set a **hide-in-hosted trigger** at the same time as the available-from date/time (keeps the preview from going live); set preview date; send to specialist for review.
- **Lead review:** assign to lead for final approval; on the HDUS Toolbox "Flyer Review (Preview ONLY)" tab, fill the day of week and assign review. Send the preview email to HDUS once approved (one-store preview — viewers use zipcode **30339**, store **121**).

### Failsafe
- Copy the failsafe shell run ID. In CP-Legacy → Flyer Creation: Flyer Run ID = failsafe shell; Flyer Type ID 6284 (PRO) / 6120 (CON); Store Set ID 251178 (PRO) / 251177 (CON); Run At = 7 PM (Tue CON / Thu PRO); attach callsheet.
- QC the run next morning: search the CP Legacy ID in email for the datasheet email — it flags any pages removed due to page-removal logic or out-of-stock. Rule: a single version of a non-page-1 page removed in a single store usually needn't be flagged; multiple stores/pages, or page 1, must be flagged to HDUS for more national SKUs.
- Confirm **page 1 is present** (PRO: navy "PRO" banner; CON: "How Doers Get More Done" white banner). The failsafe **does** go live. Post in `#hdus-cp` when it looks good (note any removed pages).

### Go-live & daily refreshes
- Copy the go-live shell ID. In CP-Legacy → Flyer Creation per refresh: Flyer Run ID = refresh ID; Flyer Type ID 6284/6120; Store Set ID 251178/251177; Run At = refresh date 4:00 AM (PRO) / 3:30 AM (CON); attach callsheet. Repeat for all refreshes. Tag the specialist on the Toolbox Flyer Runs tab to review triggers.

## One-pager inserts (Grand Openings, Kids Workshops, Tax/Seasonal events)
- These are static or single-link pages sent by the HDUS contact; because they don't meet Flipp content policy they are **hosted only**.
- Download and, if not PDF, convert to PDF. If for a grand opening / new store, add the store to Fadmin first (see Store setup). Good practice: verify the store exists in Fadmin for any one-pager.
- Manually upload to the **Standalone 1** flyer type (9976): create a run (dates per email; internal run name per convention; toggles **Hide in Distribution + Hide in Flipp**; external run name by theme so it doesn't show as "Standalone 1"; No theme). Upload the PDF, Save and Complete. On the Flyer Creation task, start task → name the pricing zone / add the page → save. Add stores in the pricing zone.
- If the page has a store link that isn't available yet, box & tag the full page with the link once the HDUS contact provides it.
- Create a CP Jira ticket for the one-pager review (include the email + flyer run link), assign to the lead, and log it in the Toolbox one-page insert section (flyer run id, name, link, Jira link).

## Post-processing revisions & updates
- **Updated banner:** download (71 DPI JPG, name must match the original), upload to Cyberduck (Marketing block = hero banners; Institutional messaging = footers/headers). In the Master Image List add a unique character to the marketing block name (e.g. add `SL`); update the OMSIDs for banners/headers in the Call Sheet to match. Re-upload the Master Image List; run a 1-store test; delete/re-create the failsafe trigger (pre-live) or all upcoming triggers (post-live) with the new call sheet.
- **Item doesn't match category:** delete the flagged OMSID row in the call sheet, keep item order numerical; a replacement item is already present (extra items in the call sheet), just confirm it matches the category (move a matching item up if needed).
- **Banner link add/update (no new SKUs):** edit the call sheet directly — Column H (Filename) to find the banner, Column I (URL) to set the new link; save; cancel and re-create any triggers built on the old call sheet.

### Page 1 removed (version limit exceeded)
- If page 1 is removed it can cause CUSAT; Flex/co-ops check for page 1 during morning QC and flag in `#hdus-cp`.
- **Early in the week:** the backup/failsafe run should be set live and today's hidden. Find the "Datasheet generated" email to identify OMSIDs causing variation (usually products with 5+ variations). Email HDUS: page 1 removed due to version limit, backup extended, list problem OMSIDs, request additional **national** backup OMSIDs, note 2-business-day timeline. On receiving updated OMSIDs, re-run Snicket from scratch for a new call sheet, run a 5-store test to confirm page 1 exists (e.g. stores 121, 975, 1001, 2412, 4113), then re-make triggers/failsafes.
- **Late in the week** (can't re-process in time): pull ~10 OMSIDs from the backfill file matching page 1's category, email HDUS suggesting backfill OMSIDs for tomorrow's ad; once they confirm, swap them into the top of the call sheet for page 1, run a 5-store test, re-make triggers/failsafes.

## Fadmin flyer set-up (shells)
- **Automated:** in the Toolbox "PASTE CON/PRO Flyer Runs" tab, use Flyer Automation → add schedules; enter the flyer week start date(s) (comma-separated for multiple weeks); the script builds the rows.
- **Manual:** copy/paste a previous week's rows and adjust names/dates (mind the different CON vs PRO end times).
- **Upload to Fadmin:** copy the header `flyer_type_id`…`valid_to` + the new rows into a new sheet, save as CSV, go to the Fadmin merchant schedules page, select Home Depot USA, attach the CSV, upload. Fix any invalid runs (usually date typos) and re-run only the failed rows. For valid runs, download the completed shell CSV, copy the IDs into the PASTE tab, then add rows to the Toolbox Flyer Runs tab with name/ID and drag the URL formula down.

## Store setup
- **Add store (grand opening / new store):** confirm required info from HDUS (Store #, address, zip, city, state). Get lat/long from Google Maps (right-click the pin). Merchant page → Stores/Sets → View Stores → search the store code to confirm it's not present → Create new store. Input info + lat/long into both Latitude/Flipp latitude and Longitude/Flipp longitude (**ensure all digits, and a negative longitude**). Be very careful — incorrect lat/long affects distribution and Foursquare location. **Harmonize** the store after creating.
- Add the store to store sets 251177 (CON) and 251178 (PRO): Stores/Sets → View Store Sets → find the set → Add Stores → Ctrl+F the store code → check → Send (do both sets).
- **Remove store:** View Store Sets → find the CP set → See Stores → Remove.

## Morning QA (Flex & Co-op tasks)
- Both CON and PRO refresh daily; QC each morning starting **9:00 AM EST** (CON go-live 9:00 AM, PRO 9:30 AM). If CON is dark, skip it (no flyer); PRO never goes dark.
- Find today's run in the HDUS Toolbox Flyer Runs (go-live is always the first run of the week; refresh runs list their go-live date after "CP Refresh").
- **Data piping stuck (yellow):** re-run **Generate Sibling Groups** (do this first — it can take a while); then confirm data-piped images = 100%+.
- **Data piping errored (red):** press **Unblock flyer run** (three dots by the comment box).
- **PDF Image Auto Selection errored:** ignore.
- Confirm flyer dates match today and run to next day; confirm **page 1** present for both (PRO navy banner / CON "How doers get more done") — if missing, flag to specialists and follow the "flyer run failed to process" steps.
- Check a pricing zone with a reasonable store count via the **vertical preview** (flyer normal, products clickable, images clean). Set Seasonal Theme = **No Theme**.
- Verify on the HDUS site (Shop All → Savings → Local Ad, or `/c/localad`): CON = "Weekly Ad", PRO = "Shop Pro Ad" — live, clickable, clean images.
- Post in `#amp-hdus` when done (note errors and ping the CP team member on HDUS from the pinned message).
- **If a run failed to process:** set yesterday's run live instead (copy today's available-to and valid-to dates into yesterday's run), hide today's run on all platforms, flag in `#amp-hdus` (ping the CP team; also notify Yao He with the live flyer run id), and annotate the Toolbox. **Co-Ops only:** mark the morning-QA Jira ticket done.

---
*Source: Confluence "Home Depot US SOP [2026]" (CP, 11993514005). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

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


---

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


---

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


---

# Sail — CP Processing SOP : V-TR (TideRise)

> **What this covers:** TideRise (TR) processing steps for Sail (Agile
> Storefronts workflow) — data formatter build, file renaming, Cyberduck
> banner/product-image ingestion, product data + story curation build, flyer
> generation, and Fadmin proof/go-live setup with custom preview links.
> Source Confluence page id: **13312360792** (CP space).
> **See also:** Sail OneGuide in `docs/retailers/sail.md`.
> Contacts/credentials intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 3762 |
| Flyer Type ID | 11755 |
| Slack channel | `#sail-ampproduction` |
| Processed on | **LAGO 5** |
| Workflow | Agile Storefronts |

Retailer-supplied assets: creative (marketing banners + custom product images) and data (Story Curation & Data Template).

## Processing

- Download assets from the email (WeTransfer link) and upload to the Sail Google Drive folder.
- Schedule processing in the Direct Processing Schedule (refer to the WBS for the processing day).

### Data Formatter

1. Open the Dataformatter.
2. Update the **Retailer Data EN** and **Retailer Data FR** gsheet tabs by pasting data from the Data Template xls (`Sail Data EN` / `Sail Data FR` tabs) **as values**.
3. Ensure product images were converted to `.png` using Image Downloader (**no cropping**).
4. Download the **tiles** tab as CSV, rename `tiles`, save in the folder with the `.png` product images.
5. Run the **File Renamer** application on the folder of `.png` product images + `tiles.csv`.
6. Files are renamed to `SAIL0000000000` format.

### Cyberduck

- **Banners:** convert all banners to 72dpi PNG in ImageDownloader; upload to `Cyberduck Sail > Assets-Banners`.
- **Product images:** upload the converted/renamed images to `Cyberduck Sail > Assets-Product Images`; run **Auto Image Processing** Custom Action (**.png and trimming format applied**) using the Product Data created below to upload the rest.
  - After running, a no-reply email flags any images that failed to upload. If the URL works and shows the image, download it manually, convert to `.png`, rename to match the **EcomID**, and upload manually to `Assets-Product Images`. If the URL is broken, note the EcomID and send to the specialist with your review notes.

### Product Data build

1. Copy data from the Dataformatter **EN** tab from cell **A2**.
2. Paste as **Format only** into the Product Data tab of the Story Curation gsheet (cell A2).
3. Re-paste in A2 as **Values only**.
4. Scroll to the bottom of the data and repeat steps 1–3 for **FR** data (format only first, then values only). Optionally use a colored line border to separate EN from FR.
5. Check all items have a "name" (add `TBD` as placeholder if needed).
6. Check all current/original prices are in `0000.00` format (no commas or spaces).

### Story Curation build

1. Open the Story Curation xls; copy everything from the **Page** column in the **EN Curation** tab.
2. Paste **as values** into the Story Curation tab of the gsheet at cell **B6**.
3. Scroll to the bottom and repeat for **FR** data (paste under EN).
4. Add **"EN"** in column L for the English data and **"FR"** (under the line) for the French data.

### Generate flyer

After all product images and banners sync in Lago, run **Generate and Process Merged Datasheet**: Merchant ID `3762`, Flyer Type ID `11755`, Flyer Run ID blank. Review that all banners and images output correctly; investigate name mismatches against uploaded Lago assets and note any retailer-data misses (e.g. missing banners) for the specialist.

## Fadmin — Edit details

1. **Available dates** (refer to WBS):
   - Proofs 1–2: available-from = when the next preview files are due from SAIL, at 11:58pm; available-to = same day, 11:59pm.
   - Go-Live: Available and Valid dates are the same (from the "Go-Live" row).
2. Set **valid from / valid to** to the Go-Live dates.
3. Internal Run name: `CP_[Valid From Date] Proof #/Go-Live`.
4. Preview date: today.
5. No theme.
6. Distribution: Proofs 1–2 hide on all platforms but Hosted; Go-Live not hidden anywhere.

**Triggers:**
- **No triggers needed for Go-Live preview.**
- **Proofs:** create a trigger with attribute **"Hide in Hosted"**, Run At = same day as the Available-from date, time **11:30pm** (hides everywhere before it would "go live").

**Add all Stores.**

## Images (Fadmin)

- Check a couple of product images match the received assets.
- Uncheck **Composites & PDF Images** to reveal items without a clean extracted image; select PDF images for outstanding cutout items; use the **Image Override URL** tagging field to add an image URL where a clean image is missing.

## Thumbnails (Proofs, Go-Lives, ECR)

- `thumbnail_1065_x_600` — 3 pages
- `stock-premium` — 2 pages
- `storefront_carousel_premium` — 3 pages
- `storefront_carousel_organic` — 2 pages
- `thumbnail` — 3 pages

## Download PDF & send for review

- In Pricing Zones → "more" → **Download Low-Res PDF**. Rename it as the flyer run name minus `CP_` plus language (e.g. `March 30 Preview 1 EN`); repeat for FR.
- Send the PDF and flyer run link to the specialist in the Slack channel with your notes (troubleshooting done, placeholder SKUs, missing items/banners). Fill in the FQC Checklist.
- FQC: check a couple of items (xls vs PDF/flyer run) and banners/product images (RAW folder vs PDF/flyer run). For the go-live proofing round, also check thumbnails (2 & 3 pages captured), PDF images, tracking codes, category page, and the preview. Request revisions if needed.
- Remove your account from the Direct Processing Schedule.
- **Custom preview links:** Sail has no Hosted, so interactive previews use custom links of the form `https://f.wishabi.net/arbitrary_files/<id>/<ts>/<id>_SAIL.html?preview_code=<code>&flyer_run_id=<run id>` (EN) and the `..._SAILfrench.html` equivalent (FR); update the preview code / flyer run id for your run.

## Retailer-specific troubleshooting

N/A (none documented on the source page).

---
*Source: Confluence "CP Sail Processing SOP V-TR" (CP, 13312360792). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

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


---

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


---

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


---

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


---

# Walmart CA Flash Deals & Spotlights — CP Processing SOP : TIDERISE

> **What this covers:** TideRise (TR) processing steps for the Walmart CA
> Spotlights and Flash Deals single-page inserts — data formatter + curation
> build, banner/URL handling (incl. Klarna defaults), image ingestion, flyer
> processing, and Fadmin steps (triggers, stores, removing extra pages).
> Source Confluence page id: **13065191547** (CP space).
> **See also:** Walmart Canada OneGuide in `docs/retailers/walmart-canada.md`.
> Contacts/credentials intentionally omitted. This SOP covers previews (all
> previews follow the same steps).

## Account at a glance

| | |
|---|---|
| Merchant ID | 234 |
| Flyer Type ID | 10617 |
| **Flyer height** | **2560** (set via custom action; cannot be changed after processing) |
| Slack channel | `cp-tiderise-pdfsf` |
| Spotlights | 6-item "skinny" insert |
| Flash Deals | 12-item regular-sized page insert |

## Things to note

- The specialist indicates in the Direct Retailer Schedule processing notes which publication (Flash Deals or Spotlights) and which week number (which data-sheet tab) to work on.
- **The data formatter is highly sensitive** (many formulas) — make minimal changes.
- Spotlights and Flash Deals are single-page inserts with EN + FR versions. Fadmin cannot process single pages, so the page is **duplicated** to run; the extra EN and FR pages are deleted afterward.
- If any data is incomplete and blocks processing, notify the specialist.

## Processing (Spotlights and Flash Deals follow the same flow)

- Walmart emails an Excel document and banners (with links) if applicable. If no new banners are provided, use the previous week's **Klarna** banners.
  - Spotlights default banners: `EN_1125x276_Klarna`, `FR_1125x276_Klarna`
  - Flash Deals default banners: `EN_1242x135_Klarna`, `FR_1242x135_Klarna`
- The Excel is named like "Flash deal/Spotlight Wk # - flyer submission or feedback"; tabs are by week number and each tab holds 4 weeks of product data. **Column A** shows which week each set is for — copy the correct week's data.
- Create a drive folder named for the week + flyer type (e.g. `Wk 4 Flash Deals`); drop banners there. Create a preview subfolder (e.g. `Preview 1` / `Go-Live Preview`) and drop the data sheet.
- Create a new week folder in the relevant Flash Deals / Spotlights drive and upload the banners (copy the Klarna banners from a previous week if none provided). Create a preview subfolder and upload the Walmart data sheet.
- Schedule processing in the Direct Processing Schedule. In the processing notes, include the banner links from Walmart; if using the Klarna banner, include:
  - EN: `https://www.walmart.ca/en/cp/klarna-shop-now-pay-later/6000207121456`
  - FR: `https://www.walmart.ca/fr/cp/klarna-achetez-maintenant-payez-plus-tard/6000207121456`
- Upload the banner images to Cyberduck (from this week's folder).
- Open the Excel for the week (Spotlights = 6 items; Flash Deals = 12 items). If multiple tabs, select the week in the processing schedule. Under Column A find your week and, for that section only, copy from **SKU (Column H)** to **Image URL (Column P)**.
- Open the **Data formatter**, go to the Spotlight or Flash Deals retailer-data tab; starting in **SKU (Column F)**, paste the data.
- Go to the Data Formatter **EN** tab (Spotlights or Flash Deals) and copy all data. In the curation sheet's Product Data tab, paste starting from **description**. If there is old data, run the **"clear spotlight cells"** / **"clear flash deals cells"** macro. **Paste the data again right underneath** — you should end with two identical stacked sets. Repeat for **FR**. Result: 2 EN + 2 FR data sets (the duplicate satisfies Fadmin's 2-page minimum).
- In the curation sheet's Story Curation tab (Set A for Spotlights / Flash Deals Story Curation), scroll to columns **J and K** (yellow cells). Under **background image**, replace the banner name in the yellow cell with the exact banner file name from the shared drive (**exact match, no extra spaces**); use the Klarna defaults if none provided. Do this twice for English, then (under the red line) twice for French.
- Under the **URL** column, replace the URL in the highlighted EN/FR cells (new URL comes from the processing schedule or specialist; otherwise use the Klarna URLs above).
- Download the Product Data and Story Curation tabs as CSV.
- Run the product data sheet through **Auto Image Processing** (Merchant ID: 234).

## Flyer processing

- Once images and banners are in, run the product data + curation sheets through **Generate Merged Datasheet**:
  - Merchant ID: **234**
  - Flyer Type ID: **10617**
  - **Flyer height: 2560**

## Fadmin steps

### Flyer details
- Change dates to match the processing notes. Update the flyer run name to `CP_Wk # Spotlights Preview 1` / `CP_Wk # Flash Deals Preview 1` (or go-live preview).
- Hide the flyer in all Flipp apps; set preview date to today.

### Trigger
- Triggers page → Create new trigger → set **attribute to distribution channels, then add Flipp hosted**. Run at 12AM on the available day (e.g. flyer available Feb 4 11:58 PM → trigger runs Feb 4 12AM). Create trigger.

### Stores
- Pricing Zones page → press the "0" under the stores column → add store set **`_CP_CDN_NATIONAL`**. Do this for EN and FR.

### Removing extra pages
- Fadmin needs at least 2 pages per zone (why the data was duplicated). Remove the extras: in the EN pricing zone delete **page 2**; in the FR pricing zone delete **page 4**.

### Hand-off
- Send the Fadmin link to the specialist in the `cp-tiderise-pdfsf` channel.

## Specialist / go-live notes

- Flash Deals and Spotlights get two previews: Proof 1 and Go-Live preview.
- Confirm flyer height is **2560** (Edit details → show rarely used fields). Height cannot be changed after processing — if wrong, TR must re-run via the custom action.
- 4 pages total (2 EN, 2 FR) but only page 1 (EN) and page 3 (FR) appear in the preview (the duplicates satisfy the 2-page minimum and are removed for preview). Check images/banners pull through; QC an item or two against the Walmart datasheet. Confirm dates and triggers (flyer runs 1 min; trigger hides in hosted before available-from).
- Go-Live is always Tuesday; latest go-live approval is 12PM Tuesday.
- After go-live approval: delete the two duplicate pages from the flyer run, re-confirm height is 2560 (Ops cannot copy boxes/tagging otherwise), download the EN and FR pages, and send them plus the flyer run link to Ops by 12PM Tuesday.

---
*Source: Confluence "[TIDERISE] Walmart CA Flash Deals & Spotlights SOP" (CP, 13065191547). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

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


---

# Walmart US — CP Processing SOP

> **What this covers:** Content Production processing steps for Walmart US
> weekly publications — manual/automated curation, banner and product data
> setup, Fadmin processing, tiles, and tracking codes.
> Source Confluence page id: **12102893588** (CP space).
> Credentials, contacts and pod names are intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 2175 |
| Flyer Type ID | 10566 |
| Slack channel | `#walmartus-production` |
| Flyer validity | Wednesday → Tuesday |

Marketing assets (banners) are created weekly by the Walmart team and posted to
the Walmart US SharePoint. Walmart also provides all categories and product URLs
in an Excel sheet on SharePoint each week.

## Data & workflow — what you need

- Manual Collection Sheet
- `[PROD]` Curation Sheet — contains the Story Curation (templates) tab and the Product Data tab
- Marketing Assets (banner images) — sent via SharePoint weekly
- Template Selection (Excel with categories + product URLs, sent weekly)

## Monday processing

1. The Walmart contact sends an email (Monday evening, sometimes Tuesday morning) confirming weekly assets are uploaded to SharePoint. Use the link in that email to download assets.
2. Access the Excel file with product URLs from SharePoint. Download it as an Excel document and drop it in the shared drive under the Go-Live date.
3. Copy the product URLs from the Excel sheet into the **'Walmart USA'** tab of the Manual Collection Sheet. Delete any old info first. DSP collects the info Monday night; it is ready for review Tuesday morning.

## Tuesday processing

- Open the Manual Collection Sheet and review the collected data.
- Scan for products DSP could not collect (item not live at collection time). Open the URL to check availability; if the link is broken or item unavailable, request a replacement.
- Copy the URLs in **Column W** and paste as **values** into **Column K** — this ensures all product URLs have tracking URLs attached.
- Fill the **Lago Custom 21** column: product names collected are SEO-based; convert them into "simpler names" (Gemini prompt instructions are in the referenced Google Doc) so they display properly on the flyer.
- Macros auto-populate the product data sheet. TR takes over processing and tags you for review when done.
- After confirming, send to the PL for review (toolkit or message). Once approved, share the flyer run ID with BD in the Walmart channel.

## Story curation sheet build

Use the `[PROD]` Product Data and Story Curation tabs.

- Locate the WMUS shared-drive folder dated for the upcoming Wednesday. Download the weekly banner zip and convert files to **.png**, then drop into Cyberduck.
- An Excel file contains links for featured pages — use it to build the story curation sheet. Templates are based on the number of items per category (e.g. 8 products = 1 page, 16 products = 2 pages).
- Copy the category-page links from the Excel file into the appropriate position in the SC sheet.
- **Tracking-URL suffix** depending on whether the page URL already contains a `?`:
  - With `?`: `&adid=1500000020090000091548&veh=dsn&wmlspartner=pubw_flp&cn=fy27-pr-pr-rbme-brtr-3p_con_msp_dsn_dis_flp_n_n_n`
  - Without `?`: `?adid=1500000020090000091548&veh=dsn&wmlspartner=pubw_flp&cn=fy27-pr-pr-rbme-brtr-3p_con_msp_dsn_dis_flp_n_n_n`
- Edit the page-level disclaimer dates on Page 1 (flyer is live Wednesday to Tuesday).
- When the Product Data sheet is ready, download as CSV and run **Auto Image Processing** (mark off trim cropping).
- Run **Generate & Process Merged Datasheets**.

## Fadmin processing

- **Add All Stores.**
- **Draw tiles:** `Stock Premium` (2 pages), `Storefront Carousel Premium` (3 pages), `Storefront Carousel Organic` (2 pages), `Thumbnail_1065_x_600` (3 pages).
- Make sure images are **not cut-outs**.
- Flyer valid **Wed → Tues**.
- **Hidden in Hosted.**
- **No theme.**
- Change **Internal run name:** `CP_Walmart US Wk [No.+1] Go-Live`. The week number comes from the Go-Live folder name (e.g. folder "(Mar 11 - Mar 17) Wk 6" → internal run name `CP_Walmart US Wk 7 Go-Live`).
- **Add tracking URLs** (reference an old run): 1 event type = engagement, the other 2 = impressions; channel set to Flipp app:
  - Engagement (Flipp App): `https://ad.doubleclick.net/ddm/trackimp/N300005.2123309FLIPPCOPORATION/B35102418.438418330;dc_trk_aid=632247754;dc_trk_cid=248672531;ord=[[randomn]];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=;gdpr_consent=;ltd=;dc_tdv=1`
  - Impression (Flipp App): `https://d.agkn.com/pixel/10690/?che=[[randomn]]&cmid=35102418&sid=CP3885S__P3CQ972_4494286&pid=438418330&cgid=632247754&cid=248672531&aid=11298113`
  - Impression (Flipp App): `https://imtwjwoasak.com/trk?CNTRY=USA&SID=2500017826&TFID=12021&CMP_ID=179364&PUB_ID=490313&PUB_NM=FlippCorporation&PLC_ID=438418330&CTE=438418330_248672531&RND_NUM=[[randomn]]`
- Send to specialist for review.

---
*Source: Confluence "CP - Walmart US SOP" (CP, 12102893588). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Well.ca — CP Processing SOP : AMP

> **What this covers:** The Content Production processing workflow for Well.ca AMP
> publications on the Agile Storefronts workflow — Cyberduck asset handling, product
> data via custom action, merged datasheet generation, and Fadmin QC/delivery.
> Processed on LAGO 6.
> Source Confluence page id: `13472301057` (CP space; page titled "[AMP] Well.ca
> Processing SOP").
>
> **See also:** no Well.ca OneGuide currently exists in `docs/retailers/`.
>
> **Note:** This SOP is relatively thin/in-progress — several conversion-tool names
> and the Tracking Codes section are left as placeholders on the source page.

## At a glance

| | |
|---|---|
| Merchant ID | 285 |
| Flyer Type ID | 8027 |
| Slack channel | `#wellca-amp-production` |
| Workflow | Agile Storefronts; processed on **LAGO 6** |
| Assets | Retailer-supplied via Cyberduck SFTP |

## Cyberduck
- Protocol SFTP; Server `sftp.flipp.com`; retailer credentials `circulars_wellca` (password not stored here — see the source page / credential store).

## Processing

### Assets (Cyberduck)
- **Banners:** convert to 72dpi PNG; upload to the Cyberduck banners folder.
- **Backgrounds (optional):** convert to 72dpi PNG; upload to the banners folder.
- **Product images:** convert to 72dpi JPG/PNG.

### Custom actions
- Dataformatter: **Create Product Data** / **Upload Data Feed**.
- Image ingestion: **Auto Image Processing**.

### Generate merged datasheet
- After all product images and banners sync in Lago, run **Generate and Process Merged Datasheet**: Merchant ID 285, Flyer Type ID 8027.

## Fadmin
- **Edit Details:** dates, availability.
- Assign stores; add any additional inserts or pricing zones.
- **Images:** uncheck Composites & PDF Images to reveal items without a clean session-extracted image; select PDF images for items with cutouts.
- **Thumbnails (Proofs, Go-Lives, ECR):** `thumbnail_1065_x_600` 3 pages; `stock-premium` 2 pages; `storefront_carousel_premium` 3 pages; `storefront_carousel_organic` 2 pages; `thumbnail` 3 pages.
- **Tracking codes:** (not specified on the source page).

## Delivery
- Download Low-Res PDF (Pricing Zones → more), rename `WKXXX Go-Live/Proof X PDF`. Send the PDF and flyer run link to the specialist and fill in the FQC Checklist.
- QC in the FQC checklist (spot-check items xls vs PDF/flyer run; spot-check banners/product images from the RAW folder; for go-live also thumbnails, PDF images, tracking codes, category page, preview). Request revisions if needed.
- Remove your account from the Direct Processing Schedule; upload the PDF; send the confirmation email.

## Retailer-specific troubleshooting
- None documented.

---
*Source: Confluence "[AMP] Well.ca Processing SOP" (CP, 13472301057). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

