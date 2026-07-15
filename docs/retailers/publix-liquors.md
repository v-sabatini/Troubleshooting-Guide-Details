# Publix Liquors — Processing Guide

> **Source:** Publix Liquors OneGuide (Google Doc `1uG78_9frnEnBsj7Wah4U78sZcj3eskSHwmZUlWehpf0`), updated Apr 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | **Flipp only** |
| Slack channels | `#publix` |
| Hosted URL | None |
| Flyer types | Liquor Ad — Weekly |
| Processing | Auto-stack; Flex vendor setup, Vendor upload, Flex FQC, DOC ad-hoc/store additions; no coupons, no Feedel |
| Resources | 2024 recipe-links spreadsheet; Publix Liquors drive |

Files received **Tuesday (late)**; vendor setup Wednesday.

## Files & schedule
- **Cadence:** Available/Valid Wednesday → Wednesday, 1-week run. No preview. **Hidden on Hosted.**

## ⚠️ Common errors / risk items
- **Staggered dates:** pricing zones should have staggered dates — **PZ 1 Wed → Tue**, **PZ 2 Thu → Wed**. Confirm dates match the PDF. (OK to ignore staggered-dates/unassigned-store warnings.)

## Upload & setup
### Vendor setup (Flex)
- Confirm files are in the FTP (search "liq" for the liquor PDFs). Copy the lowercase file path (e.g. `/050924/liquor_pdfs_050924`). Fill out the Vendor Setup & Setup QC Tracker (FlyerID, start date, file path, mark ready for upload).

### Upload (Vendor)
- Manual upload — **LIQUOR_PDFS (lowercase)**, select all 4 pages, Auto Group. Upload the Loyalty insert to the back position of all pricing zones. Make **1 zone (Base)** and add all stores.

### Setup QC (Vendor)
- Dates Wed → Wed, 1-week run, **hidden on Hosted**, no preview, internal run name `Liquor_[Start Date]`, no external name, no theme. Thumbnails Standard 4. Confirm sessions ran and FSAs generated.

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**): **include coupons**, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. **Recipe + QR code** = one box (picture + QR + recipe link). Box secondary items (smaller print, own price).
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **No item URLs** (page callouts only).
  - Brand in Brand **and** Name fields. Description = small-print size info (ml, L). Prefix N/A — include as sales story. Sale story: multi-pricing, BOGO, Save Up To, "Buy # Get $$ Off". Category usually Grocery (Google category beer/spirits/alcohol).
  - **URLs:** social-media publix links; any URL → Display "Link" as written; recipe link.
- **Image QC / Spotchecks:** N/A.

## FQC (Vendor) — pre-FQC insert & link steps
- Ops spotchecks (mainly "Prefix Unavailable" flags → confirm sale pricing is in the Sale Story). Mark Auto-Stack complete.
- **Add loyalty insert page:** download the Weekly.Spanish.Liquor Loyalty insert from the drive → Pages → Edit → Manual Upload → Save & Confirm → Mark Flyer Creation Complete → mark Box QC/Tag/Tag QC complete → wait for sessions → mark Auto-Stack complete. Pages → Box QC → box the entire page. Tag → Display **Link**, Name "Sign Up", URL = the Publix myaccount register link (in the OneGuide). Then Pages → Layout → Loyalty page → Put In → position **99**, all flyers → Process (sessions re-run).
- **Add recipe link:** Pages → open Page 2 → select this week's link from the 2024 Links spreadsheet (filter by date, may be off 1–2). Ensure the recipe is boxed (product image + QR code + URL); Display Type **Link**; add the URL.
- Confirm vendor tasks done; dates match PDF; thumbnails Standard 4; Item Image QC N/A; Tag/Tag QC both green; sessions run + re-verify URLs; vertical preview; geography (DOC note if stores added). Complete FQC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing
- Post-live page swaps per the baseline page-swap process.

---
*Source: Publix Liquors OneGuide (Google Doc `1uG78_9frnEnBsj7Wah4U78sZcj3eskSHwmZUlWehpf0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
