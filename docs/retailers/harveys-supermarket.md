# Harveys Supermarket — Processing Guide

> **Source:** Harveys Supermarket OneGuide (Google Doc `1qZ4fwB1tceHtTG6QiA2SLAunvHX5G8cHvpSy05KHhpw`), updated Dec 8, 2025. Contacts/credentials omitted.

SEG (Southeastern Grocers) banner. Rules are largely shared with Winn-Dixie / Fresco y Más.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#segrocers` |
| Hosted URL | harveyssupermarkets.com |
| Flyer type(s) | **Weekly Circular** (ID 3070) · **In-Store Flyer / ISPO** bi-weekly (ID 3292) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday, via **FTP**.
- **Cadence:** Available From Mon / Valid From Tue → Available To Mon / Valid To Tue. Preview: Tuesday.
- Files delivered by external ops via FTP (credentials in the OneGuide — not stored here).

## Upload & setup (owned by FLEX)

Search the FTP by `.xlsx`. **Two codesheets per run:**
1. **"Versions" / "Version List"** = store information.
2. **"Manifest"** = pricing zone + page order info (also outlines preview and valid dates).

- Base path patterns: weekly = `/MMDD+HRV`; bi-weekly ISPO = folder with `ISPO` in the name.
- **Version list first, manifest second.**
  - Open Version List → "Harveys Base AD ALL" tab. Change the "Store"/"Store #" header to **"Stores"** (critical for fadmin to read the codesheet). Save tab as CSV.
  - Upload — Name `Stores`, **config `seg_stores`**, base path per week, **toggles: ALL except 2**, Save codesheet. **DO NOT RUN this codesheet.**
  - Manifest: no manipulation, save as CSV. Upload — Name `pages`, **config `seg`**, base path per week, **toggles: ALL except 2 and 7**, Save. **Preview Start Date = Available From.** Run only the manifest codesheet.

### ⚠️ Common errors / risk items

- **"Pages not found in FTP"** → check FTP for a spelling error / similar name, fix the manifest, re-upload and re-run.
- **"Page already uploaded"** → check if the page is an insert with valid dates beyond the flyer; if so, the error can be ignored.
- If the error persists after investigating, reach out to the processor — may require new files from the retailer.
- **Setup QC:** if uploading from SFTP, confirm no un-uploaded pages remain. Missing stores in Geo → search the Version List for the store code; if not present, the flyer shouldn't get that store; if present, add it manually. Write "Geo is good" in the comment box once confirmed.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** include coupons and packaged deals; exclude retailer logo, sign-up page, social media, special weblinks. One price for all items = ONE BOX (BOGO / "Pick 5 for 5"). Box vaccine banners. Watch box/image alignment.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON):** include Name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs — there is NO URL linking; do not box/tag any banners or pages with URLs.** Use LOWEST price in current price for two-price items.
- **Categories are critical** (retailer receives analytics) — use the section header; do NOT add two categories; flag rather than guess.
- **Image QC:** select CLEAN PDFs when available, else cutout.

## FQC / post-processing (FLEX)

- Tag unique valid dates where pages have them (1-/3-day sales).
- **Switch & Save pages must be boxed and tagged** (often skipped because they have sale stories, not prices) — can copy boxes from the same-week Harveys/Fresco y Más flyers.
- Legibility heights 35,25; no theme; available everywhere; standard thumbnails.
- **Flyer sorting:** weekly flyers first (by date, current then preview), ISPO/bi-weekly last.
- **Flyer Review type: Lite.**

---
*Source: Harveys Supermarket OneGuide (Google Doc `1qZ4fwB1tceHtTG6QiA2SLAunvHX5G8cHvpSy05KHhpw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
