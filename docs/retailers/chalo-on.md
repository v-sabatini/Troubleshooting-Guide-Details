# Chalo ON — Processing Guide

> **Source:** FreshCo/Chalo (ON) OneGuide (Google Doc `1qc79CgJuSoczAJXmum4YTGmWxqt_ODwgZWALMaZGCTM`), updated Oct 24, 2025. Contacts/credentials omitted.

> **Note:** This OneGuide covers the Sobeys **FreshCo & Chalo (Ontario)** banners together. FreshCo = flyer type 502; Chalo = flyer type 3654. They **share pages**.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | freshco.com |
| Flyer type(s) & cadence | FreshCo 502 Weekly · Chalo 3654 Weekly |
| Processing | Auto-stack; 3FL; OS setup; **Feedel/retailer data services YES**; no coupons |

## Files & schedule

- **When files arrive:** Tuesday or Wednesday. Available From Wednesday / Valid From Thursday.
- **Workflow:** Upload & Setup (Vendor) → FQC (Vendor).

## Upload & setup

### FreshCo ON (502) — codesheet upload
- Search "code" in the FTP, download the xls (e.g. `FreshCo ONT_WK07_Zone Code_REV_fordigital.xlsx`).
- Delete the **Zone 2** column (Chalo) and any other Chalo column; delete secondary publication callouts; delete the pages column; **rename the "Position" column to "Pages"**; delete extra items at the bottom; set everything in column A to "Flyer"; rename pricing-zone titles to **Zone #** (Zone 1, Zone 3…). Save/download.
- **Upload:** Name `pages`; Config Name **`sobeys_safeway`**; Base Path = FreshCo ON FTP path; **unmark the first 2 boxes and the last box (only 4 selected)**; Save & process.

### Chalo ON (3654)
- Open the Zone Code sheet from the SFTP; **manually upload pages** using the zone code sheet. **Make sure all pages are added for all Chalo zones.** Save & complete → Flyer Creation. Create pricing zones per the Zone Code doc (e.g. Zone 2). Mark Flyer Creation complete.

### Setup QC
- **FreshCo:** pricing zones = Zone 1, Zone 3, Zone 5…; verify pages against the Zone Code doc (highlighted pages after Zone 1 are zone-specific). Build a **generic stores codesheet** from the Distribution Recap — Name `Stores`, Config **`generic_stores`**, Base Directory `/`, **first box only**, Save & process. External Run Name = "Weekly eFlyer + valid dates"; No Theme; Key Messages = "Weekly Specials"; set vendors to High.
- **Chalo:** add all stores (confirm via Zone Summary/Distribution Recap if >1 PZ); check page 1 for dates; vendors High; No Theme; external run name + Weekly Specials; verify page order.

## ⚠️ Common errors / risk items
- **"Pages have already been uploaded"** — usually because Chalo (Z2) shares pages and is already uploaded. If Chalo pages are up you may **Force Processing**; if not, **DO NOT** force — flag the issue.
- **"The following files matched multiple files on the FTP"** — retailer uploaded the same page multiple times. Confirm duplicates in the SFTP, then force processing; verify pricing zones have correct pages before completing.
- **"Undefined method 'merchant' for nil"** — copy the Zone Code sheet into a Google Sheet (paste values only), name it the flyer run, download as xlsx, then do a **manual upload**.
- Store codesheet errors → check for overlapping stores; if two zones (Zone 1 + Zone 3) error, delete Zone 3 and add those stores manually. If stores can't be added, flag and continue — flyer can process without stores.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** box all items attached to the price, include as much of the image as possible; multiple items with one price go in the same box. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price. **Exclude description, SKU, URLs.** Pre/postfix e.g. "Scene+ Member Pricing"; disclaimer e.g. "7.99 without Scene+ Card".

## Post-processing (3FL, Mondays — verify completion)
- **Item Category QC:** one category per item; add **Scene+** category to items with Scene+ callouts.
- **Item Image QC:** clean PDF preferred; use cutout only if no clean PDF.
- **Scene+ Points QC:** all Scene+ sale stories read "xxx Scene+ PTS when you buy x"; add Scene+ category to any missing items (Item Search: Sale Story contains "PTS").
- **Deep Links** (new process 02/25/2025): check the Sobeys Insert Tracker "Deep Links" tab; tag the banner/item **as a link** with SKU + link; dates in red get no deep links. Watch for store/FSA/PZ-specific tiles and specific valid dates (use Create Trigger for later go-live; file an OPTICS ticket if you create triggers).
- **Custom Tiles** (DOC): check `#sobeys` Slack; Override Thumbnail (or Create Trigger) on Storefront Premium / Storefront Carousel Premium.

## FQC (Flex/DOL)
- Autostack spotcheck; **confirm stores added** (Chalo should total **7 stores**); storefront spotcheck; leg heights 40/35; item image QC (uncheck composites & PDF); QC thumbnails (4 standard + `first_page_thumbnail_400w`); page categories (all but page 1); add inserts from the Sobeys Insert Tracker and add to PZ; if a "Proudly Canadian" insert is present, box and tag it (link `chalofreshco.com`). Check sessions/errors. **Ensure pages are in correct order** (verify PZs against the Zone Code sheet).
- **Flyer Review type: Lite** (DOL).

## Out-of-processing
- **Page swap:** Pages tab → Edit → select new page from FTP → add "REV" to the name → Save & Complete → Copy Items from old page (same page only, adjust changed items) → box/tag → add to PZ.
- **Cloning:** Chalo ON was cloned weekly to feature on the FreshCo hosted experience — **cloning discontinued as of Jan 20, 2026.**

---
*Source: Chalo ON OneGuide (Google Doc `1qc79CgJuSoczAJXmum4YTGmWxqt_ODwgZWALMaZGCTM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
