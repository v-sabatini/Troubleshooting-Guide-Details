# Fresco y Mas — Processing Guide

> **Source:** Fresco y Mas OneGuide (Google Doc `1EwDtDYvNQOXX-6rZKUHbk0JUgnfSVDemdUfKju0UzqM`), updated Dec 8, 2025. Contacts/credentials omitted.

SEG (Southeastern Grocers) family. Bilingual (English/Spanish) tagging. Two flyer types: **Weekly** and **Liquor**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (Liquor: Hosted only) |
| Slack channels | `#segrocers` |
| Hosted URL | frescoymas.com |
| Flyer types | Weekly · Liquor |
| Processing | Auto Stack; Flex (Processing Support + Flyer Review); DOC (FQC); **Feedel/retailer data services YES**; no coupons |

## Files & schedule
- **Files arrive:** Monday (retailer sends via FTP).
- **Cadence:** Available From Wednesday; Valid From Tuesday → Available To Wednesday; Valid To Tuesday.
- **Preview date: Wednesday.**

## Upload & setup (owned by Flex)

Two codesheets appear in the FTP (search ".xlsx"): a **Version List** (store info) and a **Manifest** (pricing zone + page order).

### Weekly flyer
- Open Version List → **delete the 'Store Addresses' tab**. In the "Fresco y Mas" tab, ensure store info is in **Column C** and rename the header to **"Stores"** (not "Store Number"). **If this manipulation isn't made, the codesheet will not work.** Save as CSV.
- Upload the **version list first** (do NOT process it): Name "Stores", **config `seg_stores`**, base path from FTP, **toggles ALL except 2**, Save codesheet — then leave it (do NOT press Process).
- Open the Manifest (no manipulation), save as CSV. Upload **after** the version list: Name "pages", **config `seg`**, base path from FTP, **toggles ALL except 2 and 7**, Save.
- **Process ONLY the Manifest codesheet.** Wait for it to turn green; mark "Flyer Creation" complete.
- PZ tab → confirm all PZs have stores assigned (**the version list sometimes fails to run** — if PZs have no stores, manually assign from the version list document).
- Geography tab → no stores missing/removed. Check the FTP that all pages were pulled in; manually upload any missing pages using the manifest for position.

### Liquor flyer
- Liquor files always have **LIQ** in the file names.
- Version List: **delete the "LIQUOR STORE #" column** entirely; rename the "REGULAR STORE #" tab to **"Stores"** (now in column C). If not done, the codesheet won't work. Save as CSV.
- Upload version list first (config `seg_stores`, toggles ALL except 2, do NOT process).
- Manifest: if there is store info in columns A and B, delete those columns; save as CSV. Upload (Name "pages", config `seg`, toggles ALL except 2 and 7).
- **Process only the Manifest.** Confirm stores assigned; assign manually from the version list if needed.

## ⚠️ Common errors / risk items
- **Stores must be in the 3rd column ("C")** or the codesheet fails.
- **Excel UTF-8 error** → upload to Google Sheets and download the CSV from there.
- **Do NOT process the versioning document** — only process the manifest.
- **Switch & Save pages** are often skipped by vendors (no prices, only sale stories) — box and tag them in-house if missing.
- **Bilingual tagging:** names, descriptions and disclaimers must be tagged in **English and Spanish** (name separated by "/").

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **Include** coupons and packaged deals; **exclude** retailer logo, sign-up page, social media, special weblinks. **Do not box the retailer logo or rewards banners.**
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** include name (EN/ES), pre/postfix, valid dates, description (EN/ES), price, sale story, categories, disclaimer (EN then ES), original price, URLs; **exclude SKU.**
  - **BOGO items:** don't put the "Save From" $ in Dollars Off; put "BUY ONE GET ONE FREE / COMPRE 1, RECIBA 1 GRATIS" in the PREFIX, remainder in Sale Story.
  - Categories: use the banner above the item group as a reference.
- **Image QC:** use PDF whenever possible; use cutout when PDF isn't clean.

## Post-processing (owned by Flex)
- **Item Category QC:** every item needs a category (this merchant receives customer-behavior analytics — wrong categories skew their data). Category examples: Grocery, Dairy, Frozen Food, Meat, Packaged Meat, Bakery, Deli, Seafood, Produce, Home Essentials, Health & Beauty, Alcohol.

## FQC (owned by Flex)
### Weekly
- Check FTP for a Linking Document (usually 1 URL to box/tag on an insert); QC categories; scan pages for unique valid dates and tag accordingly; page categories from flyer headings; ensure Switch & Save pages are boxed/tagged.
- Standard 4 thumbnails; **legibility heights 35/25**; dates per PDF (Wed–Tue); no previews, no theme; available everywhere; **flyer sorting — weekly first, LIQ last.**
### Liquor
- QC categories; page categories; box/tag the first-page logo/header and all bottom rewards banners with the rewards UTM link `https://www.frescoymas.com/rewards?utm_source=referral&utm_campaign=flippcampaign` (rewards banners only).
- Standard 4 thumbnails; legibility 35/25; dates per PDF; no previews; no theme; **HIDDEN on Flipp and Distribution, only available on Hosted**; flyer sorting weekly first, LIQ last.

## Flyer review
- **Type: Lite.** Owned by Flex.

---
*Source: Fresco y Mas OneGuide (Google Doc `1EwDtDYvNQOXX-6rZKUHbk0JUgnfSVDemdUfKju0UzqM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
