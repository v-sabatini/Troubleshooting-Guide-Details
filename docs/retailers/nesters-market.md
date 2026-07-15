# Nesters Market — Processing Guide

> **Source:** Nesters Market OneGuide (Google Doc `1s-Du9XY4DYUmZEYHbK0CW7aM5oZFpJQK10ND6wgyZyI`). OneGuide last updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#buylowfoods` |
| Hosted URL | http://www.buy-lowfoods.com/ |
| Flyer type(s) & cadence | 9323: Weekly · Flyer Type 2 (Eat Well Live Well): Monthly |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

## Files & schedule (9323 Weekly)

- **When files arrive:** Thursday
- **Publication cadence:** Available From Wednesday 3 AM, Valid From Thursday 3 AM; Available To Thursday 2:59 AM, Valid To Wednesday 11:59 PM
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC)

## Upload & setup (owned by Vendor) — codesheet build

1. **Download versioning document from the FTP** to check for more than one version (search "NM" to find it).
2. **Manipulate the codesheet:** go to the Store Versioning tab and delete the Store IDs tab; **delete the first 4 rows; delete columns A, G and H.** If applicable, Ctrl+F → Find ".pdf", Replace with nothing. Copy and paste columns A, B, C into a Google Sheet.
3. **Upload codesheet:** Name = `upload`; upload the codesheet CSV; **Config name = `overwaitea`**; PDF Base Directory taken directly from the SFTP.
4. Check the SFTP (search `/NM`) to confirm all pages uploaded.
5. Mark Flyer Creation complete.

*If Monthly pub: manual upload, no preview, available and valid the same — into the Eat Well Live Well flyer type.*

### Setup QC (owned by Vendor)
- Edit Details dates: **Available 3 AM two days before live date; Available To 2:59 AM one day after last live date; Valid From 3 AM; Valid To 11:59 PM.**
- **Do NOT use an external run name.** No theme. Fab 4 thumbnails. **Leg heights 50 × 40.** Scroll through the pub and confirm the logo is prominent. Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- **Valid and Available dates must be set correctly.** Available From: Wed 3:00 AM; Available To: Thu 2:59 AM; Valid From: Thu 3:00 AM; Valid To: Wed 11:59 PM. **The "Available To" date/time is 3 hours AFTER the Valid To — this is correct.** The Available To and Valid To dates should **NOT be the same day.**
- **Alternate pricing per KG** (Weekly & Monthly) goes in the **description**, not the postfix. Example — Name: New York Strip Loin Roast; Description: Canadian AA or Better Grades of Beef, 19.80/kg; Current Price: $8.98; Postfix: lb.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)**
- **Include:** retailer logo, sign-up page, special weblinks.
- **Exclude:** coupons, packaged deals, social media.
- Box all items with prices, using text boxes when necessary. For overlapping products, box the text rather than the image. Items with different prices boxed separately.

**Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Selection ON)**
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. Brand is Box Draw/Box QC specific.
- **Exclude:** URLs.
- Name/Brand = bolded first text; non-bolded text below is the description. Include "ea"/"kg" in postfix; include "_ for" in prefix.

**Image QC**
- Use a clean PDF image if available — **almost all items will have a usable clean PDF** (do not use if the product is cut off). Use the cutout only if no clean PDF is available.

## Final QC (owned by Flex)
- Mark auto-stack off; complete Ops spot checks if applicable.
- Edit Details dates (Available 3 AM Wed 1 day before live; Available To 2:59 AM Thu; Valid From 3 AM Thu; Valid To 11:59 PM Wed).
- Check PDF dates match the flyer run (there is a 1-day preview). **No external run name.** Draw 4 standard thumbnails. Check geography.
- Page categories on all but the first page. Check items for special sale dates.
- **When you see a Rewards page, tag it with** `https://www.nestersmarket.com/morerewards/`.
- Check horizontal and vertical previews. Complete Final QC list.
- **Flyer sorting order: Current WEEKLY, PREVIEW OF NEXT WEEK, MONTHLY.**

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Page swaps / post-live checks per the OneGuide.

---
*Source: Nesters Market OneGuide (Google Doc `1s-Du9XY4DYUmZEYHbK0CW7aM5oZFpJQK10ND6wgyZyI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
