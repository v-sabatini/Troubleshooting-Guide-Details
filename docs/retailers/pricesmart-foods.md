# PriceSmart Foods — Processing Guide

> **Source:** PriceSmart Foods OneGuide (Google Doc `17yR6XN7LIJZsueNV1Anurx68loDTaoe3KNPdFiU5zYI`), updated Mar 11, 2026. Contacts/credentials omitted.

> Much of this OneGuide is the unfilled template; the notes below capture the real PriceSmart-specific content (the **Additional Deals / MingPao** flyer type).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (retailer channel not specified) |
| Flyer types | Weekly; Monthly. Additional Deals flyer type = MingPao flyers |
| Processing | Auto-stack; Vendor upload, Flex Image QC, DOC FQC; Feedel (retailer data services) yes; no coupons |

## Files & schedule
- **Files received:** Monday (arrive Tuesday afternoon per upload step).
- **Cadence:** Available Mon → Mon; Valid Tue → Tue. FQC dates below use Thu→Wed.
- If files are delayed, push go-live 1–2 days.

## Upload & setup (Vendor)
- **Tuesday upload:** files arrive Tuesday afternoon. Manually upload pages from FTP — **1 Base pricing zone, all stores.** Thumbnails Standard 4. Setup QC.
- (Reference: UF and PSF cheatsheet.)

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **ON**): box all items with a price, without a price, "Happy Hour" items, sales-story items, and "Shop" items. Box **"SHOP NOW"** separately from a priced/sales-story item. Box the entire page for CIBC "Earn points faster" promos. "Load My Offers" with no original price → single box around item + Load My Offers; with an original price → box the item separately from the "Load My Offers" price. Box Mega Deal/More Rewards and Win-Win callouts.
  - **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
  - **⚠️ Do NOT box** promotional banners, footers, or vacation packages.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include name, pre/postfix, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude valid dates, SKU.
  - **All items get the URL:** `https://www.pricesmartfoods.com/weekly-specials?utm_source=flipp&utm_medium=referral&utm_campaign=psf-mingpao-2021`

## FQC (DOC)
- Dates (Edit Details): Available/Valid from **Thu 12am**, to **Wed 11:59pm**; available everywhere; no theme; Key Message: **Additional Deals**.
- Geography: stores never change.
- Item Image QC → Generate Data Piping Groups; select best image, **do not use plated-food images**. QC thumbnails with no white space.
- **URL fix:** Item Search → URL IS blank → Multi-Edit Items → add the pricesmartfoods weekly-specials URL to all items. Run Page Stitching + Tile Generation repeatedly until green, then re-verify URLs.
- **Flyer Review type: Lite.**

---
*Source: PriceSmart Foods OneGuide (Google Doc `17yR6XN7LIJZsueNV1Anurx68loDTaoe3KNPdFiU5zYI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
