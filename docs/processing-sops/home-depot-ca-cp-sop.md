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
