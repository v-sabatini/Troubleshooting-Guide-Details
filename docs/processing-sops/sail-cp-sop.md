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
