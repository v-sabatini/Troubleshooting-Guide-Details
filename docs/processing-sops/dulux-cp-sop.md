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
