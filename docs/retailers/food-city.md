# Food City (My Food City) — Processing Guide

> **Source:** Basha's Food City OneGuide (Google Doc `1lDNuJNflPycw4TSvPi5Y0HVwdl1w99K4dlUT3idulso`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (Basha's) |
| Availability | All platforms |
| Slack channels | `#bashas`, `#flex-processingsupport` |
| Hosted URL | myfoodcity.com/food-city-weekly-ad |
| Flyer types | Weekly (merchant 3541) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); **Yes — Feedel/retailer data services**; no coupons |

## Files & schedule
- **When files arrive:** Monday. **The retailer does not send emails about file deposits.**
- **Publication cadence:** Available From Tuesday, Valid From Wednesday, **Available To Wednesday 1:59am**, Valid To Tuesday.
- **Linking document:** N/A. **Processing type:** Auto-stack.

### ⚠️ Risk items
- **Special Day Sales valid dates** — set item-level valid dates.
- **Donut Day valid date** — the valid date is the FRIDAY with the length of the flyer valid dates.
- **Savings Guide coupons** must be tagged as the coupon display type.

## Upload & setup (owned by Vendor) — codesheet
- Upload codesheet (xlsx from FTP).
- **⚠️ Manipulation: delete any hidden columns or rows** so the codesheet doesn't pull extra unwanted info.
- Download the xlsx as CSV for upload.
  - **Config name: `bashas`** (for all).
  - PDF Base Directory: take path from FTP.
  - **All toggles EXCEPT region assignment and combine zones.**
- Go to the FTP, search the week's path name, and confirm all files uploaded (e.g. Feb 18 publication → `/021826_FoodCity`).
- **⚠️ Reused PDF error workaround:** save the original xlsx as a CSV, upload the CSV to Google Sheets, then re-download as CSV — this should let the codesheet upload successfully.

### Setup QC checklist (owned by Flex)
- **External run name → "Next Week's Ad".** Theme: "no theme". Spotlights/Key Messages: "Our Deals. Your Savings."
- **Set Trigger:** Attribute = External Display Name; Value = **Weekly Ad**; Run at = **Wednesday when the flyer goes live**. Leave a note "trigger done" in the comments box.
- Thumbnails (4 standard).
- Setup QC: check dates at the bottom of the first page; 1-day preview; **"Available to" date is one day after the "valid to" date at 1:59 am** (2 hours after it's no longer valid).

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc required)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks (per the overview table).
- Box every item with a price as shown.
- **Box the social media icons separately** (box & link):
  - foodcity.com → "Food City"; facebook.com/FoodCity → "Facebook"; instagram.com/foodcitygrocery → "Instagram"; twitter.com/foodcity → "Twitter".
- **Box every coupon with a barcode.**
- When boxing an item that also has text, draw the text box too (box the item image + the text box containing all text info).

### Tag / Tag QC (Low complexity — Auto-tag OFF; linking doc required)
- Brand is Box Draw/Box QC specific.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price.
- **Exclude:** SKU, URLs.

### Image QC
- **PDF preferred.**

## Post-processing / Final QC (owned by Vendor)
- Edit details: **Valid from Wednesday 12 AM to Tuesday 11:59 PM; change the "available to" time to Wednesday 1:59 AM.**
- Autostack spotcheck complete.
- Item Image QC: no grey in PDF background (switch to cutout if grey); lifestyle background OK.
- Item search name contains "donut" → make sure valid dates are set.
- **Page categories: page 1 should have no categories.**
- Sales/Specials: go through each page, ensure products under special sales have valid dates set.
- Check previews; **confirm trigger is set** (from "Next Week's Ad" to "Weekly Ad", set for when the flyer is Valid).
- Complete FQC checklist.

## Flyer Review (owned by Flex)
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page Swap:** baseline page-swap process (Jan 2024).

---
*Source: Food City (My Food City) OneGuide (Google Doc `1lDNuJNflPycw4TSvPi5Y0HVwdl1w99K4dlUT3idulso`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
