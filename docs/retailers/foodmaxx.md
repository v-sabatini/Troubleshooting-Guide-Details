# FoodMaxx — Processing Guide

> **Source:** Lucky Supermarkets / Save Mart / FoodMaxx OneGuide (Google Doc `1_8NU2MSGSZbdq-2-AcwxeU4IDJrhKFxZID63OExG5G8`), updated Aug 11, 2025. Contacts/credentials omitted.

This guide covers the shared Save Mart family (Save Mart, Lucky Supermarkets, FoodMaxx). FoodMaxx has banner-specific manipulations noted below. Files for all three merchants live in the same FTP folder.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#savemart` |
| Hosted URL | flyertown.ca/flyers/luckysupermarkets-flyer |
| Flyer types | Weekly (FT #238); plus S&D "Online Savings Guide" and "Our Brands" |
| Processing | Auto-stack; Flex (FAB tickets); Image QC by Flex; DOC (FQC); **Feedel/retailer data services YES**; no coupons |

Files are sent by the Quad team (credentials in the OneGuide — not stored here).

## Files & schedule
- **Files arrive:** Tuesday (sometimes Wednesday).
- **Cadence:** Available From Wednesday; Valid From Tuesday → Available/Valid To Tuesday.
- **Flyer-type routing:** flyers tagged **S&D** and **Our Brands** are processed in the **"Online Savings Guide"** flyer type; the regular weekly is processed in the **Weekly** flyer type.

## Upload & setup (owned by Vendor)

**Manifest (codesheet) + Store Version List:** Lucky/Save Mart receive Manifests outlining files/pricing zones. The retailer now requires us to build our own Store List (RunList).

- **Split codesheet LKY vs SM:** the manifest combines Lucky (LKY) and Save Mart (SM) — separate into 2 codesheets. Copy Versions → last page grabbing only that banner's versions; readjust page headings (Page 1, Page 2…); save as CSV. FoodMaxx 10x10 and BW follow the same steps.
- **Manifest upload:** attach each banner's manifest CSV — **config name `save_mart_original`**. Since stores aren't assigned here, leave the **first two toggles unchecked**. FoodMaxx uses the same config (differs only in base directory and CSV). Mark Complete in Flyer Creation and Setup QC.
- **Store List (RunList) build:** new Google Sheet with headers "stores" and "pricing zone"; copy store codes + version names from the manifest; delete any N/A CLOSED rows; save as `RunList.csv`.
- **Store List upload:** base path `/`, **config name `generic_stores`**, leave **Region Assignment and Page Upload toggles unchecked.**
  - **FoodMaxx warning handling:** if a store warning appears — add all stores in the FM section, then **remove stores 405, 402, 410, 447, 480**, and remove MV (250) and OAK (417, 484). Then re-add 405, MV (250) and OAK (417, 484) into their correct pricing zones via the PZ tab.
- **S&D / Our Brands upload:** adjust the manifest to the example and save as CSV. Codesheet settings: type "Pages", add base directory, check **Page Upload, Allow pricing zone creation, Use Page Pool, Tile Generate afterwards, Combine Zones**. Save → Process. Then upload the store RunList (stores in column A, pricing zones in column B).

### Setup QC (owned by Vendor)
- PZ tab → confirm FSAs added; Geography tab → no new stores added/deleted; check sessions.
- **Thumbnails: 4 Standard** (thumbnail_1065_x_600 stock_premium, storefront_carousel_premium, storefront_carousel_organic).
- **Leg heights: 40/35.** Edit Details → no theme → available everywhere. Complete Setup QC.

## ⚠️ Common errors / risk items
- **Alcohol items:** wine & spirits must have the correct sale story (e.g. "Buy 4 Save 10%") and ONLY wine & spirits (not surrounding items or beer). Set item-level valid dates (e.g. 3-day sales) correctly. Box each priced item separately. The **Mix or Match banner must NOT be boxed/tagged** or included in any description/disclaimer/sale story.
- **Coupons** tagged under the 'coupon' display type, not 'item'.
- **Items:** tag Name = bold text; Description = regular text under the name; verify prices and postfix (lb./ea.) match the PDF.
- **Stores must be in the 3rd column ("C")**; Excel may throw a UTF-8 error → upload to Google Sheets and download CSV from there.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Include** coupons and packaged deals; **exclude** retailer logo, sign-up page, social media, special weblinks. Multi-item/multi-price → separate box per item/price; multi-item/one-price → box each item; single items boxed.
- **Tag / Tag QC (Low; Auto-tag OFF):** Brand box-draw/QC specific. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price; **exclude URLs.**
  - **Current Price** = large bold text; **nothing in Original Price.** "+CRV" always goes in the Description (never postfix). Single-purchase price in Description, not postfix. Second Lucky You Digital Coupon price → postfix "-$__ with Lucky You Digital Coupon".
  - **Set item-level valid dates ONLY for 3-day sales.** No URLs.
  - **Categories:** Coke/water/energy drinks = Beverages (not Beer/Wine & Spirits); Deli = prepared-in-store items; select Google Categories.
  - **Sale Story:** "SAVE UP TO ___" goes in sale story, not dollars-off; BOGO and "Buy 4 Save 10%" are sale stories; Mix and Match is NOT.
  - **Disclaimer:** conditions of sale; flower-department notifications go here (not description).
- **Image QC (owned by Flex/DOC):** pick cleanest, most relevant image. Grey/black background or shadow → "do not use PDF image".

## Post-processing (owned by DOC)
- Item Category QC, Item Image QC (same rules as above), URL/Links QC, SKU QC, Ad-hoc QC.

## FQC (owned by Flex)
- **Vertical Preview first** (PZ tab) to confirm the page loads. If it doesn't load → rerun Page Stitching and Page Tile Generation; if still broken → Republish (Overview); if still broken, continue steps and notify Lead/Coordinator.
- Item Image QC quick spot check; Edit Details → no theme → available everywhere → Key Message "For All Your Grocery Needs / For Your Grocery Needs".
- Review valid dates for 3/2-day sale callouts; review alcohol "Buy _ Save _" sale stories; mark wayfinding QC; mark Spotcheck QC; rerun sessions if needed and mark in-store only.
- **Flyer sorting order** — Save Mart / Lucky: current weekly, then S&D (Big Monthly Deals), then Our Brands (Save Even More). **FoodMaxx order:** store-specific 10x10, then BW, then 1-Day Produce Sale.
- External run names: "Weekly Ad" (weekly), "Big Monthly Deals" (S&D), "Save Even More" (Our Brands).
- The FQC checklist warning can be ignored.

## Flyer review
- **Type: Lite.** Owned by Flex.

## Out-of-processing
- Standard page swaps / post-live checks per baseline.

---
*Source: FoodMaxx OneGuide (Google Doc `1_8NU2MSGSZbdq-2-AcwxeU4IDJrhKFxZID63OExG5G8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
