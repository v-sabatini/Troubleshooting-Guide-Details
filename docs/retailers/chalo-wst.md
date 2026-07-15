# Chalo WST — Processing Guide

> **Source:** FreshCo/Chalo West OneGuide (Google Doc `1hKAnstZeGuR62Q4Mz7QqjHbslsBFwfkehmeg6X1lO_Y`), updated Mar 11, 2026. Contacts/credentials omitted.

> **Note:** This OneGuide covers the Sobeys **FreshCo & Chalo West** banners together (flyer type 9130). FreshCo and Chalo WST **share the same codesheet + distribution recap**.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | freshco.com |
| Flyer type(s) & cadence | Weekly West (9130); files Tuesday, Available From Wednesday / Valid From Thursday |
| Processing | Auto-stack; Flex (Processing Support); **Feedel/retailer data services YES**; no coupons |

> **⚠️ FreshCo & Chalo West main flyers are AVAILABLE EVERYWHERE and AVAILABLE + VALID AT 3AM.**

## Files & schedule

- **When files arrive:** Tuesday.
- **Workflow:** Upload & Setup (Vendor, 5 & 4 days out) → FQC (DOC).

## Upload & setup

### FreshCo West (9130) — codesheet
- In the FTP search "west", hide uploaded. Two files: **codesheet + distribution recap** (shared by both banners).
- **Manipulations:** delete Zone 2 and any other Chalo zones; delete secondary callouts; delete pages column; **rename "Position" → "Pages"**; delete extra items at bottom; column A = "Flyer"; pricing-zone titles → **Zone #**.
- **Upload:** Name `pages`; Config **`sobeys_safeway`**; Base Directory = FTP file path; **Toggles 3, 4, 5, 6**; Save & process. Process Chalo and FreshCo **at the same time** to avoid the "pages already uploaded" warning. Mark Flyer Creation complete.

### Chalo West (9130) — codesheet
- Delete the FreshCo columns; change headers to **Zone #** in chronological order; column A = "flyer"; **flap pages** (FL_1 / FL_2 in the file name) must be moved to after page 1 — cut the row of page-1s in every zone and paste above the flap pages. Save as .xlsx.
- **Upload:** Name `pages`; Config **`sobeys_safeway`**; Base Directory = FTP path; **Toggles 3, 4, 5, 6**; Save & process.

### Stores (Distribution Recap → generic_stores)
- New Excel: A1 = `stores` (lowercase, plural), B1 = `pricing zone` (lowercase); paste store codes per zone under A; write `ZONE #` in B to match the codesheet (**case-sensitive**). Skip Chalo zones for FreshCo. Save as .csv.
- **Upload:** Name `stores`; Config **`generic_stores`**; Base Directory `/`; **first toggle only.**
- **Chalo stores:** add manually into the correct PZ per the distribution recap.

### Setup QC (Flex)
- Let sessions run; add stores (FreshCo via generic codesheet; Chalo manually); set vendor tasks to high; check off unused FTP files; merge pages in storefront spotcheck if applicable; mark autostack spotcheck complete.

## ⚠️ Common errors / risk items
- **"Pages have already been uploaded"** — shared pages with the other banner. If the other banner's pages are up you may Force Processing; otherwise **DO NOT** force — flag.
- **"Files matched multiple files on the FTP"** — duplicate pages uploaded by retailer; confirm in SFTP then force processing.
- **"Undefined method 'merchant' for nil"** — copy Zone Code into a Google Sheet (values only), download xlsx, do a manual upload.
- If **Chalo codesheet errors**, manually upload the pages. Watch for filename mismatches (extra spaces) between codesheet and FTP; **bolded characters won't process in fadmin.**

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price. **Exclude description, SKU, URLs.** Pre/postfix e.g. "Scene+ Member Pricing"; disclaimer e.g. "7.99 without Scene+ Card".

## Post-processing (3FL, Mondays — verify completion)
- **Item Image QC:** clean PDF preferred, else cutout.
- **Category QC:** one category per item; Scene+ category for Scene+ callouts.
- **Scene+ Points QC:** sale stories read "xxx Scene+ PTS when you buy x"; add Scene+ category to missing items.
- **Deep Links:** Sobeys Insert Tracker "Deep Links" tab; tag as a link with SKU + link (red dates = none).
- **Custom Tiles** (DOC): `#sobeys` Slack; Override Thumbnail / Create Trigger on Storefront Premium & Carousel Premium.

## FQC (Flex)
- Available everywhere, **Available + Valid at 3AM**; autostack spotcheck; confirm stores added (Chalo = **7 stores**); no theme; external run name = "FreshCo Weekly eFlyer mm/dd - mm/dd" / "Chalo Weekly eFlyer mm/dd - mm/dd"; leg heights 40/35; item image QC (uncheck composites & PDF); **6 thumbnails** (Standard 4 + thumbnail 2-page + `first_page_thumbnail_400w`); page categories; add inserts to PZ; box/tag "Proudly Canadian" insert if present (link `freshco.com` / `chalofreshco.com`); check sessions/errors; **ensure pages in correct order** (usually the DIG pages; verify PZs against the Zone Code sheet).
- **Flyer Review type: Lite** (DOL).

## Out-of-processing
- **Page swap:** standard REV process (Pages → Edit → new page → add "REV" → Copy Items → box/tag → add to PZ).
- **Cloning:** Chalo WST was cloned weekly to the FreshCo hosted experience — **cloning discontinued as of Jan 20, 2026.**

---
*Source: Chalo WST OneGuide (Google Doc `1hKAnstZeGuR62Q4Mz7QqjHbslsBFwfkehmeg6X1lO_Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
