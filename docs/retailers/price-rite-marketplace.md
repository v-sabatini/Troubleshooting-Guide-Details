# Price Rite Marketplace — Processing Guide

> **Source:** Price Rite Marketplace OneGuide (Google Doc `1v1KPVoPdsXjfP62FxT4lJteAX0SO47NZLCQbsbxrMWQ`), updated Jul 23, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#wakefern` |
| Flyer types | Weekly Ad (9342) |
| Processing | Auto-stack; DOC upload, Flex Flyer Review; no coupons/Feedel (coupons still appear in-flyer) |
| Custom action | **Mi9 Sub Item Generator** — creates sub-items per the blowline doc (runs pre-FQC) |

## Files & schedule
- **Files received:** Monday; goes live external Thursday with a 1-day preview.
- **Cadence:** Available Thu → Thu; Valid Fri → Thu.
- **Linking document:** Yes — the **blowline** file (uploaded ~5 days ahead, before all other assets; scroll to the bottom of the SFTP to find it, under the week's .zip).

## Upload & setup (Vendor)
Codesheet is a **.txt** file (separate from an additional .txt file in the PriceRite/circular folder).
- Download it; copy/paste the whole codesheet text into a **new Google Doc** (reduces formatting errors).
- Remove the lines "Online Start Date" and "Circular Type".
- StartDate/EndDate format = **MM/DD/YYYY**. Keep exactly **one blank line** between each section (EndDate↔Name, Name↔Region/pricing zones, Region↔RegionFiles/pages, and between each RegionFiles line). No empty space under the pages.
- Upload the codesheet as **.txt**, config name **`brookshires`**. Verify pricing zones match the codesheet, then mark flyer creation complete.

### Setup QC (Flex) — building the linksheet
- Open the blowline file in Excel/Sheets. Select column A → Text to Columns → fixed width; verify line breaks don't cut off **PROMO_NUM, UPC_13_NUM, BLOW_LINE**. Remove all other columns.
- New tab **"For OS"** = PROMO_NUM + BLOW_LINE (remove UPC_13_NUM); new tab **"mi9"** = PROMO_NUM + UPC_13_NUM (remove BLOW_LINE).
- In "For OS" only, remove duplicates. Save as **.xlsx** and attach to all tracks.

## ⚠️ Common errors / risk items
- **Look for multiple products in a block** — box separately if two prices are listed; keep as one box if only one price for two items.
- **Mi9 sub-item custom action:** clean the mi9 tab first — delete blank rows, delete rows where a promo code exists but UPC_13_NUM is blank, and fix any UPC_13_NUM cell formatted as a formula (search for `E` or `+`). Download as CSV, upload in Fadmin, copy the file ID. System → Custom Actions → **mi9 sub item generator** (NOT subitem report); paste file ID and flyer run ID; run. On error, read the error log, fix the sheet, re-upload for a new file ID, re-run. Confirm some items now have sub-items (not every item will).

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**): **include coupons.** Exclude packaged deals, retailer logo, sign-up page, social media, special weblinks. Blocks with multiple items → box separately if two prices; one box if one price for two items.
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude pre/postfix, valid dates, URLs.**
  - **SKU custom field:** find the item's name in the blowline's `BLOW_LINE` column (col B); the SKU is in `PROMO_NUM` (col A). Paste into the SKU field. Multiple SKUs → use the first. Not found → leave blank. Never enter more than one PROMO_NUM.
  - **Coupons:** display type Coupon; tag brand/name/description/sales story/disclaimer as written.
- **Image QC:** use PDF images whenever possible **except coupons** — coupons always use cutouts.

## FQC / Flyer Review
- Ensure all coupons tagged correctly. Item Image QC tab: if "Generate data piping groups" is shown, click it (otherwise mi9 generator won't run). Thumbnails Standard 4. **Staggered dates:** the codesheet may drop the preview date — if so, select all → apply selected dates → enter the Thursday date in Date Available and save.
- **Flyer Review type: Lite.**

---
*Source: Price Rite Marketplace OneGuide (Google Doc `1v1KPVoPdsXjfP62FxT4lJteAX0SO47NZLCQbsbxrMWQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
