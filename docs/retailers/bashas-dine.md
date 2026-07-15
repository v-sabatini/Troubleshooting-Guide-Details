# Bashas/Dine — Processing Guide

> **Source:** Bashas/Dine OneGuide (Google Doc `1qTJFHiRzrtgtvQSZVpz-qW4VSkCuW_HRAttkh9SvdnM`), updated Jun 1, 2026.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#bashas`, `#flex-processingsupport` |
| Hosted URL | https://www.bashas.com/ |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops (retailer data / Feedel) |

## Files & schedule

- **Files received:** Monday (retailer sends no email about file deposits).
- **Publication cadence:** Available From Tuesday → Available To Wednesday 1:59am; Valid From Wednesday → Valid To Tuesday.
- **Preview:** 1-day preview.
- **Linking Document:** N/A.

## Upload & setup (owned by Vendor)

- **Codesheet upload:** codesheet is in the FTP (.xlsx).
  - **Delete any hidden columns/rows** so the codesheet does not pull in extra unwanted information (items shown in pink were hidden and must be deleted).
  - Download the .xlsx as .csv for upload.
  - **Config name:** `bashas` (for all).
  - **PDF Base Directory:** take path from FTP.
  - **Toggles:** all except **region assignment** and **combine zones**.
- Verify in the FTP that all files for that week's path are uploaded (e.g. Oct 2 run → `/100224_Bashas`) after uploading the codesheet.

### Setup QC
- External Run Name → "Next Week's Ad". Theme → "no theme". Spotlights/Key Messages: "Our Deals. Your Savings."
- **Set trigger:** Attribute = External Display Name; Value = "Weekly Ad"; Run at = Wednesday when the flyer goes live. Leave a "trigger done" note in the comments box.
- Thumbnails: Standard 4.
- Check dates at the bottom of page 1; 1-day preview; **"Available To" is one day after "Valid To" at 1:59 AM** (2 hours after it's no longer valid).

## ⚠️ Common errors / risk items (retailer-specific)

- **No alcohol on the Dine flyer.** If any appears, call it out to the retailer.
- **Date-specific sales:** specific items in the publication carry special sale callouts (often Friday–Sunday or specific days). Ensure those items have valid dates set.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- No Linking Document.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box-draw all items sharing a price/description together; box entire promotional banners.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking Document required (Tag/QC-specific).
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, Brand. **Exclude SKU, URLs.**

### Image QC
- **PDF images preferred unless unclear.** No grey in PDF background — if grey, switch to cutout. Lifestyle backgrounds are OK.

## FQC (Flyer Review type: Lite)
- Edit Details: Valid from Wednesday 12 AM, Valid to Tuesday 11:59 PM; change Available To time to Wednesday 1:59 AM.
- Autostack spotcheck complete; standard item image QC.
- Item search — name contains "donut" → ensure valid dates set.
- Page 1 should have no page categories.
- Sales/Specials: go page-by-page and ensure products under special sales have valid dates set.
- Check previews; confirm trigger is set (from "Next Week's Ad" to "Weekly Ad" when flyer is valid).

## Out-of-processing
- Page swaps supported (see OneGuide video).

---
*Source: Bashas/Dine OneGuide (Google Doc `1qTJFHiRzrtgtvQSZVpz-qW4VSkCuW_HRAttkh9SvdnM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
