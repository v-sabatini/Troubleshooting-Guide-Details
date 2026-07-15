# Fresh Thyme — Processing Guide

> **Source:** Fresh Thyme Market OneGuide (Google Doc `1buraEVN8p7ks_M0Df0p70GLcRykDIlYsmgEfwZoYdc8`), updated May 25, 2024. Contacts/credentials omitted.

Two flyer types: **Weekly** and **Monthly**. Digital inserts are tracked in the Fresh Thyme Digital Insert Tracker.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Flyer types | Weekly · Monthly |
| Processing | Auto-stack; Flex (Flyer Review); **OS — Setup**; **Feedel/retailer data services YES**; **linking document YES**; no coupons |

## Files & schedule
- **Files arrive:** Monday.
- **Cadence:** Available From Tuesday; Valid From Wednesday → Available To Monday; Valid To Tuesday.
- Merchant 3552. Weekly run tracked in the tracker (Monthly is not).

## Upload & setup (owned by Vendor)

**Weekly & Monthly:**
1. Open the retailer's xls codesheet from the FTP; create a new sheet with rows Zones, Stores, Page 1, Page 2, etc.
2. Copy the "version" column into the zones/stores columns; copy pages into the page columns.
3. **Check that each page name ends in `.pdf`** (flag to Coordinator if missing).
4. Save as CSV.
- **Vendor uploads:** use the vendor setup/upload spreadsheet (flyer run id, path, codesheet); toggle off "ready for DSP upload".
- **Manual upload:** Codesheet upload — file type CSV, **config `generic`**, **toggles 1, 3, 4, 5, 6**; run codesheet.
- **Important:** attach the Digital Insert Tracker links to all vendor tasks.

### Setup QC (owned by Vendor)
- Weekly: no theme (unless specified), available everywhere; **set Available From and Valid From to 1:00 AM.**
- Monthly: no theme, available everywhere; **Available/Valid From to 1:00 AM.**

## ⚠️ Common errors / risk items
- **Codesheet upload:** ensure ALL page names end with ".pdf"; after the codesheet runs, check the FTP that all files uploaded.
- **Available From / Valid From TIMES must be 1:00 AM** (unique-time risk at FQC).
- **Unique item dates:** some pages have their own run dates — set those dates on the items (e.g. a Digital Produce Sale starting 7/25 must not be added to zones with pages starting 7/24 → create a page-layout trigger to insert it at Page Position 1 on 7/25).
- **Inserts (Friday afternoons):** when the "WES Track name" prompt appears while uploading insert pages, just hit "Submit". Adding insert pages to the existing codesheet returns **Yellow "pages already uploaded"** errors — this is fine, **FORCE PROCESSING.**

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking document required):** **Include** social media and special weblinks; **exclude** coupons, packaged deals, retailer logo, sign-up page. Draw clean boxes around all priced items; box social-media icons; box banners with sale stories.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking document required):** Brand box-draw/QC specific. Include name, pre/postfix, valid dates (only if unique), description, price, sale story (only if on flyer), categories, original price; **exclude SKU, disclaimer, URLs.** Include "when you buy" text in pre/postfix.
- **Image QC:** prefer clean (white background) PDF; otherwise leave the cutout.

## Post-processing (owned by DOC)
- **Item Category QC:** all items have a Google category.
- **URL/Links QC:** links added to all pages listed in the Digital Insert Tracker.
- Tracking URLs added at pre-FQC: Overview → ad hoc process → managing tracking URLs → Add Tracking URLs (Impression + Open events, Flipp App channel — DoubleClick URLs in the OneGuide).
- Thumbnails: Standard 4 (thumbnail_1065_x_600, stock_premium, storefront_carousel_premium, storefront_carousel_organic).

## FQC (owned by DOC)
- Ensure all digital insert pages align with the Digital Insert Tracker.
- Pages tab: page categories (no categories on first page(s)); item QC (# boxes ≈ # tags); **RISK — unique Available/Valid From TIMES set to 1:00 AM**; **RISK — item dates** (pages with their own run dates set correctly).
- Image QC tends to be all cutouts — double-check. Confirm pages tab #s green and equal; sessions run; vendor tasks complete.

## Flyer review
- **Type: Lite.** Owned by Flex. Separate review docs for Weekly and Monthly.

## Out-of-processing
- **Page Swap:** standard baseline page swap.

---
*Source: Fresh Thyme OneGuide (Google Doc `1buraEVN8p7ks_M0Df0p70GLcRykDIlYsmgEfwZoYdc8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
