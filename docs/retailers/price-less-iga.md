# Price Less IGA — Processing Guide

> **Source:** Price Less IGA OneGuide (Google Doc `1nzDnoGoU5JyvGErhCGy2wC-3crvgJo9wXRPL0Pf-yQk`), updated Apr 27, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flexflyerreview` |
| Hosted URL | myiga.com |
| Flyer types | Flyer — promoted (11877) · Flyer — organic (11912) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons, no Feedel |

## Files & schedule
- **Files received:** Tuesday.
- **Cadence:** Available Wed → Tue; Valid Tue → Wed. No preview, no linking document.

## Upload & setup (Flex)
- **Codesheet build** from the Price Less IGA codesheets sheet: File → Import → Upload → new sheet. Copy the "promoted" column from last week; add a filter.
- Compare column B (store #) week-over-week for changes. Filter column A for "Y" (promoted stores) → paste store numbers (col B) into the "Promoted" tab (cols A & B); replace page names from column K, split text to columns. Repeat filtering "N" for the "Organic" tab.
- Download each (promoted, organic) as CSV and upload to the matching flyer run.
  - Config name **`generic`**; use the corresponding week's FTP file path.
  - **All codesheet toggles checked except the 2nd and last.**
  - Common error: differently named files — adjust the codesheet to match what's in the FTP.
- Mark flyer creation complete, wait for sessions, then Setup QC.

### Setup QC
- Confirm all pages uploaded — **check no pages remain in the SFTP** (Pricing Zone → Items View).
- Confirm flyer dates (usually top of first page). Thumbnails Standard 4. Add "**Weekly Flyer**" to the external run name (English).

## ⚠️ Common errors / risk items
- **Codesheet organization** — organize correctly, especially regarding promoted stores.
- **Store #40:** Always remove store **#40** (its entire row) from the codesheet — this store is manually uploaded into the biweekly flyer runs named "FL".
- FQC geography: compare **FL flyers against other FL flyers**.

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**): box each product block with a price and/or sales story. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**

## FQC / Flyer Review
- Confirm dates vs PDF; all availability toggles unchecked; thumbnails include retailer logo. All items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography matches last week.
- **Flyer Review type: Simple.**

---
*Source: Price Less IGA OneGuide (Google Doc `1nzDnoGoU5JyvGErhCGy2wC-3crvgJo9wXRPL0Pf-yQk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
