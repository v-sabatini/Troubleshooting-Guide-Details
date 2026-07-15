# NSLC — Processing Guide

> **Source:** NSLC OneGuide (Google Doc `12-GZvxv-XFUm0eLezebG0nTrwWIsBMAq471rVaSLXn0`). OneGuide last updated Feb 23, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | **Available on Flipp only** (hidden on Hosted and Distribution) |
| Slack channel(s) | `#nslc`, `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1: Monthly (9896) — also has ad-hoc publications; cadence changes |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc
- **Publication cadence:** Ad-hoc (typically monthly but varies). No preview — Available From = Valid From, Available To = Valid To.
- **Linking document:** Yes — should be attached to all tasks.
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup (owned by Vendor)

- Files are dropped in the SFTP.
- **Manual upload:** Pages → Edit → select the pages for that publication → Auto-group → Save and continue. When Flyer Creation is available, start the task → create one pricing zone named **`base`** → add all pages → Save and continue.
- **Attach the linking document from the FTP to all vendor tasks.**
- Overview > Edit Details: no preview (Available From = Valid From, Available To = Valid To). **Hide in Hosted will already be checked.** Internal run name can be the same as the start date. No theme.
- Standard 4 thumbnails (thumbnail_1065_x_600, stock_premium, storefront_carousel_premium, storefront_carousel_organic).
- Let sessions run, then begin Setup QC checklist.

### ⚠️ Common errors / risk items
- **Flyer dates: use the Merchant's email as the source of truth, NOT the flyer pages.** The dates on the flyer pages often differ from the posting instructions used to create the run — the merchant frequently gives posting timelines that do not match their print distribution schedule.
- Confirm the linking document is attached to all tasks (used for both Box and Tag).

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF; linking document required for both Box and Tag)**
- **Include:** special weblinks.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Box each item individually. Box any banners with calls to action or links.

**Tag / Tag QC (HIGH complexity — Auto-tag ON, PDF Image Auto-Selection ON; linking document required)**
- **Include:** brand (Tag/QC specific), name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Exclude:** pre/postfix.
- Tag Product Name + Brand. SKU is on the bottom of the product (and on the linking document). Tag URLs per the attached URL sheet.
- **Watch for special sales (2- or 3-day sales):** if item valid dates differ from the flyer's valid dates, enter them in the valid-date override fields.

**Image QC**
- If the **FIRST ITEM** listed has a **clean PDF image with a white background**, select it; otherwise select the cutout. For multiple items, always select the first product listed in the item name; if the first brand's image is unavailable or not clean, select the cutout.

## Final QC (owned by Flex)
- QC thumbnails (Standard 4).
- **All items have URLs** — if any are missing, open the linking document.
- Geography: no change.
- **Flyer dates match the email** (not necessarily the printed flyer dates — see risk item above).
- Complete Final QC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex). Hide in Distribution, Hide on Flipp? — **live when valid (dates on PDF)**; hide on Hosted checked; custom tile (usually); preview items clickable; check a few links; geo consistent.

*(Note: the review table shows "Hide on Hosted" checked while the account overview states Flipp-only — treat the linking-document/email dates and the checked Hosted toggle as authoritative per the run setup.)*

## Out-of-processing
- Page swaps / post-live checks per the OneGuide.

---
*Source: NSLC OneGuide (Google Doc `12-GZvxv-XFUm0eLezebG0nTrwWIsBMAq471rVaSLXn0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
