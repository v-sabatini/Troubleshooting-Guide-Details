# Colemans — Processing Guide

> **Source:** Colemans OneGuide (Google Doc `1TBf2jK3Rw1ZmUrHVvwBpenBKUDVbV4Z0gC2L_59ebT8`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#colemans`, `#flex-processingsupport` |
| Hosted URL | shop.colemans.ca |
| Publication | Weekly (Flyer **3258**) |
| Cadence | Files Tuesday. **2-day preview (available Tuesday)**, Valid Thu–Wed |
| Processing | Auto-stack; Flex owns processing; no coupons, no Feedel |

## Files & schedule
- Files + codesheet arrive **weekly via SFTP**; codesheet dropped as a **CSV** named `Colemans Distribution [date-date].csv`.
- Generally no manipulation needed. Rarely, file names don't match codesheet names → fix by expanding month abbreviations (e.g. "Mar" → "March").

## Upload & setup
1. Upload the codesheet to create all pricing zones, assign pages, assign stores:
   - **Config name = `generic`**.
   - **Check all toggles except the second and the last.**
2. Edit Details:
   - Valid Thursday to Wednesday; **2-day preview (available Tuesday)**.
   - **No toggles checked (available everywhere)**; no theme.
3. Complete Setup QC checklist.

## ⚠️ Common errors / risk items
- File names occasionally don't match codesheet names (month abbreviation mismatch) — correct before upload.
- Complete thumbnails for **BASE and BUCHANS pricing zones separately**.
- At FQC you can ignore the "Not all categories that are used in pricing zones have thumbnails" warning.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Single items: box the whole item block, insert a text box where needed. **Items with common pricing: keep them in one box (don't separate).** Don't let boxes overlap.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.

### Item Image QC
- PDF images where possible; cutouts fine for others (e.g. Jell-O Pudding → PDF; graham pie crust → cutout).

## Pre-FQC / FQC (owned by Vendor)
- Pre-FQC: OS spot checks if needed; Image QC; thumbnails Standard 4 (`thumbnail_1065_x_600`, `stock_premium`, `storefront_carousel_premium`, `storefront_carousel_organic`) — **complete for BASE and BUCHANS separately**.
- Edit Details: available 2 days before valid; dates match PDF front page; available everywhere.
- Pages QC'd; categories accurate per page; item view all boxed/tagged; vertical + horizontal preview; vendor tasks done; geography — no store changes week over week.
- Complete FQC; ignore the categories/thumbnails warning.
- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps handled per the baseline page-swap process.

---
*Source: Colemans OneGuide (Google Doc `1TBf2jK3Rw1ZmUrHVvwBpenBKUDVbV4Z0gC2L_59ebT8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
