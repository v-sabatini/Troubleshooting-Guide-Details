# BMR — Processing Guide

> **Source:** BMR OneGuide (Google Doc `1bjjwerp4SbMsW4ur7blqqq3qIKzfmQdGMFggN-sj4M0`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account | Bilingual (EN/FR) — includes BMR Weekly, Potvin & Bouchard, BMR PRO, Agrizone |
| Availability | All platforms |
| Slack channels | `#bmr` |
| Hosted URL | potvinbouchard.ca (also bmr.ca) |
| Flyer types & cadence | Weekly (Available Wed 1-day preview, Valid Thu–Wed) |
| Processing | Auto-stack; no Flex; no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** Wednesday.
- **Publication:** Available From Wednesday (1 day before Valid); Valid Thursday → Wednesday.
- **Preview:** N/A.
- **Linking document:** BMR "EXTRA URLs" sheet from the FTP — mass-attach to Vendor tasks.

## Upload & setup

**Weekly (new process):**
- Manually upload pages of the week — **label pages `bmr` (not `pb`)**. Auto-group pages and set languages: typically 2 English + 4 French per page. Save & confirm.
- **Create 10 pricing zones:** ENG Z4, ENG Z5, FR Z1, FR Z2, FR Z3, FR Z4, plus cross-language ENG Z1/Z2/Z3 (from FR pages) and FR Z5 (from ENG Z5 pages). **Names must be consistent — the codesheet depends on them.**
- Open the week's Runlist (FTP) in Sheets. Copy Merchant Number, Price Zone, Language. Label the merchant-number header `stores`, add a `pricing zone` column, and build it with `=CONCATENATE(D2," ",C2)`. Paste-values to strip the formula; delete Price Zone/Language columns. Build the cross-language store sheet (delete Z4 rows; replace FR Z1→ENG Z1 etc.; ENG Z5→FR Z5, scoped to "this sheet"), append to the bottom, save as CSV.
- Upload codesheet as **generic store codesheet — 1st toggle only**.
- Standard 4 thumbnails; theme "Proudly Canadian" or No Theme if unavailable.

**Vendor setup (flyer-type routing):** check page 1 — if it says **AGRIZONE** build in the Agrizone flyer type; **BMR PRO** → BMR PRO type; otherwise **Weekly Ad**. Upload from SFTP, auto-group, assign languages (Ctrl+F "FR"), assign up to 4 pricing zones (each with a CL zone) matching the store codesheet.

**Agrizone:** upload pages, assign languages, create EN and FR pricing zones. Build store codesheet from the Agrizone runlist Column A (store list): column `Stores`, column `Pricing Zone` = EN for all; duplicate the store list below with FR. Save CSV, upload with **`generic_stores`** configuration.

### ⚠️ Common errors / risk items (retailer-specific)

- **Every item MUST have a SKU tagged** (exactly one SKU — the first listed).
- **Codesheet errors:** columns must be labelled `stores` and `pricing zone`; pricing-zone names in the codesheet must match the flyer run exactly; **watch EN vs ENG**.
- Tag EN pages in English, FR pages in French; apply English URLs (bmr.ca/en/) to EN pages only and French URLs (bmr.ca/fr/) to FR pages only.
- Items with multiple items/prices: split by size, box/tag as individual items.
- **Flyer tracking code** must be applied at FQC (Dynamic Variable, Source: Distribution, Variable: `utm_campaign`, Value `YYYY_s##-circulaire`); then click "Apply All Tracking Codes."
- **Flyer sorting order:** BMR regular → Flash/Garden Sale → Agrizone.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box multi-item/price groups as individual items.
- **Tag / Tag QC — Low. Auto-tag OFF; PDF image auto-selection ON. Linking document required (Tag/QC-specific).** Include: name, pre/postfix, valid dates, description, one SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for box draw/QC.
- **Image QC:** PDF image preferred.

## FQC / go-live

- **Flyer Review type: Lite** (separate review docs per banner: Weekly, Potvin & Bouchard, PRO, Agrizone).
- Set external run names — **FR: `Circulaire`, EN: `Weekly Flyer`**. Categories max 3, none on page 1. PDF image preferred.
- **SKU review (two checks):** SKU IS blank → open item, find SKU (result should be 0); SKU CONTAINS comma → item should have exactly ONE SKU (result should be 0).
- Verify links from the Linking Sheet (EN URLs on EN pages, FR URLs on FR pages).
- Check dates/theme, thumbnails, legibility heights (35×25), geography, sessions, scroll; apply flyer tracking code.

## Out-of-processing

- Flyer sorting order: BMR regular → BMR PRO → Agrizone regular → Agrizone guides.
- Page swap: standard baseline process.

---
*Source: BMR OneGuide (Google Doc `1bjjwerp4SbMsW4ur7blqqq3qIKzfmQdGMFggN-sj4M0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
