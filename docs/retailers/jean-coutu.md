# Jean Coutu — Processing Guide

> **Source:** Jean Coutu OneGuide (Google Doc `1KXiPmAL_bT6hTFwHewajOlfdYFRyASDynayIjL1OPPs`), updated Jul 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Core+ |
| Availability | All platforms (**not on our Hosted**) |
| Slack channels | `#flex-processingsupport` (retailer channel per OneGuide) |
| Hosted URL | Not on our hosted |
| Flyer type(s) & cadence | **Weekly Flyer** (Flyer Type 1465) · **Health & Beauty Flyer** (weekly) · **Special Insert** (ad-hoc) · **Cosmetics Insert** (ad-hoc). Bilingual EN/FR. |
| Processing | Auto-stack |
| Who's involved | DOC (Upload/Setup + FQC); Flex (Flyer Review); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Wednesday.
- **Publication cadence:** Available Tuesday → Wednesday; Valid Thursday → Wednesday.
- **Linking document:** required for **weekly runs** (attach for tagging).

## ⚠️ Risk items
- **"Missing in Hosted" error (all flyer types):** do NOT mark as missing in hosted — Jean Coutu isn't on our hosted but can't be hidden in hosted due to their app.
- **Supplementary linking in FQC:** the retailer strongly emphasizes ecomm — links are flagged in the codesheets multiple times; adding them is highly important.
- **Weekly ad linking:** links and SKUs are added by vendors during processing — you **must** attach the linking document for tagging.
- **Sale Story (EN):** when the flyer says "**Save x%**", tag it as "**x% Off**" (NOT "Save x%"). When it says "Save $x", tag as "Save $x". Tag dollar-off and percent-off differently.
- **New Jul 13, 2026:** there should be **no staggered dates** — if the codesheet creates staggered dates, update them to match the flyer shell dates.

## Upload & setup (owned by DOC)

### Codesheet setup
- Codesheet arrives via email (attached to the ClickUp task). In the first tab, the headings below the yellow flyer types show which flyers run that week (almost always at least **Weekly Flyer** and **Health & Beauty Flyer**). Shells are pre-built for those two; if there's a "special insert" in the codesheet with no ClickUp task, flag to CXE.
- Copy the full flyer-run names from FAdmin into the matching cells.
- Under "Health & Beauty Flyer", adjust file-name dates from **YYMMDD to DDMMYY** (H&B only), e.g. `PJC_CIRC_SB_NB_260708` → `PJC_CIRC_SB_NB_080726`.
- **Suivi tab:** delete the "No.PDF" cell and the column below "Page No" (shift left) to make one column; ensure page naming matches the sFTP (H&B page names often have dates reversed, e.g. 070319 vs 190307) — any name change must be made on **both the suivi tab and the first tab**; double-check the years in columns B-D. Download as xlsx.

### Running the codesheet
- Same for all flyer types: open each flyer run → codesheet → upload the .xls, **config name `jean_coutu`**, PDF base directory = the date-code file path from the sFTP (e.g. `/241024/`), **check Store Assignment and Page Upload**.

### Linking document
- A "Bottin" file is dropped in the sFTP. Manipulate: delete columns A, B, D, G; rename "Groupe produit F7" to "SKU"; save as XLSX; attach to all vendor tasks.

### Thumbnails
- Standard 4 thumbnails, **1 page only** (no 2-page thumbnails for horizontal layouts), no whitespace.
- **Weekly Flyer only** uses **custom tiles** to replace the Storefront Carousel Organic thumbnail — find them in the sFTP (search THUMB/THUMBNAIL, correct date folder), download locally, and override in Thumbnail QC. Recommended: do ON or NB first, QC thumbnail last.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each item block (one box even if several items share a block); use text boxes when product info isn't neatly aligned; **box all disclaimer text**.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc for weekly runs)
- Include brand, name, pre/postfix, valid dates, description, SKU (new), price, sale story, categories, disclaimer, original price, URLs (new).
- **Brand/Name:** brand as listed (if multiple brands, leave brand field blank); name = Brand + product, brand in ALL CAPS even if lowercase on the flyer; for multi-item boxes also put the brand in the description.
- **SKU (Weekly Flyer only):** from the text-extraction box, a 1-4 digit number (e.g. 205).
- **URL (Weekly Flyer only):** add the appropriate URL for each item from the linking document; not all products get a URL each week.
- **Disclaimer — Pharmaciens propriétaires:** items inside the green "Pharmaciens propriétaires" box get the special pharmacy disclaimer (copy/paste the full EN or FR text from the OneGuide) — applies only to products between the two blocks.
- Tag disclaimer/description text in the correct language only (EN text on EN, FR text on FR).

### Image QC
- Select the image that best matches the product; if multiple products, select one specifically. **If the photo has a black background (not clean), do not use the image extraction — leave it as a cutout.**

## Post-processing / FQC (owned by DOC)
- **Disclaimer QC (QC versions only):** find pages with the "Pharmaciens Propriétaires" heading and ensure all products in the boxed area have the disclaimer.
- **Thumbnail QC:** follow the Thumbnails steps if not done at setup.
- **Flyer sorting:** CIRC REG newest → CIRC REG older → Health & Beauty newest → Health & Beauty older → then inserts newest → oldest.
- **FQC (weekly):** check % of SKUs & URLs added (item search SKU/URL not blank — **over 75% acceptable**); add CTA links from the Feuille de Suivi (Suivi tab column F); check pharmacy disclaimers via storefront spotchecks. H&B and other inserts: add CTA links + check disclaimers.
- Remove any staggered dates (see risk items).
- **Flyer Review type: Lite.**

---
*Source: Jean Coutu OneGuide (Google Doc `1KXiPmAL_bT6hTFwHewajOlfdYFRyASDynayIjL1OPPs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
