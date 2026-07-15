# Price Chopper USA — Processing Guide

> **Source:** Price Chopper USA OneGuide (Google Doc `1UYE6CW4B8lzGFxB0SuOYWj7pvfcxPb_xHJ2bLt3AmZA`). Contacts/credentials omitted.

A US grocery account (Tier 1). Weekly flyer processed via a **generic codesheet**; a secondary "PICS/other" flyer type is manual.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 |
| Availability | All platforms |
| Slack channel(s) | `#pricechopperusa`, `#pricechopperusa-scp` |
| Hosted URL | pricechopper.com/digital-flyer/ |
| Flyer type(s) | Flyer Type 1: Weekly · Flyer Type 2: PICS/other |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Sat, Valid From Sun; Available To Sat, Valid To Sat.
- **Preview:** Saturday.
- **Linking document:** none.
- **Workflow owners:** Upload/Setup = DOC; Image QC = Flex; FQC = Vendor (Flex usually completes but must be bumped).

## Upload & setup (owned by DOC)

### Weekly (config `generic`)
- Open the "Generic Codesheet Price Chopper USA.xlsx" that matches the week's page count.
- **Find & Replace the date** (e.g. filename `092723` → use that date).
- **Copy pages from zone 11 to zone 11c.** Save locally as CSV.
- Upload: **Config `generic`**, PDF Base Directory copied from Stale, **toggles: check 1, 3, 4, 6 (leave 2, 5, 7 unchecked).**
- Flex upload team: check the Geography tab — flag any discrepancy vs. the previous week's distribution to the account DOL.

### PICS / other
- Retailer sends the file or uploads to FTP → manual upload; attach any linking doc to the vendor task, else complete setup QC.

### Setup QC
- **Weekly:** Geography — no stores added; Vendor tab — Box Draw ready, no linking doc; sessions run; pricing zone pages normally ~16–20 (all zones same page count); **Edit Details — available Saturday (one day before valid Sunday), no retailer preview, available everywhere, grocery generally no theme.**
- **PICS:** one pricing zone with all stores; dates from email (else confirm with merchant); **available on Hosted only.**

### ⚠️ Common errors / risk items (retailer-specific)
- **Weekly codesheet:** must copy pages from **zone 11 → zone 11c** and set the correct date via Find & Replace before saving.
- **Toggles 1/3/4/6 only** — checking 2, 5, or 7 is a setup error.
- **Geography discrepancy vs. prior week** → flag to the DOL.
- **Box-draw risk (FQC):** OS sometimes doesn't box smaller sub-items separately — fix manually in Pages.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product with a price individually; in a block with multiple differently-priced items, box individually.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select OFF)
- **Include:** name, brand, pre/postfix, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs. **Valid dates:** include only if different from the publication date.
- Tag all fields as seen on the page; pick the best category.

### Image QC
- Select white-background images where possible, otherwise cutouts.

## Final QC (owned by Vendor)
- Geography — no stores added; Codesheet tab all green; sessions run.
- **Pricing zone:** sort zones most→least items; click "items" and scroll to confirm items are drawn correctly (watch for un-boxed smaller sub-items). Fix incorrect tags manually in Pages.
- Flyer Review type: **Lite.**

## Out-of-processing
- **Flyer sorting:** weekly flyer first unless PICS/other ads exist and the retailer specifies a different order.
- **Checkered email (every Wednesday by EOD):** confirm all files received / no missing pages, stating the number of zones and pages and the Saturday-preview / Sunday-valid setup (recipient list in the OneGuide — not stored here).

---
*Source: Price Chopper USA OneGuide (Google Doc `1UYE6CW4B8lzGFxB0SuOYWj7pvfcxPb_xHJ2bLt3AmZA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
