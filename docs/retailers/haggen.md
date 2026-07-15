# Haggen — Processing Guide

> **Source:** Haggen OneGuide (Google Doc `1V7azqnU10YBCHuP_pSpQobjYTdcYb_G9xJ5naXMkTDY`), updated Mar 25, 2026. Contacts/credentials omitted.

Albertsons-family banner.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | haggen.com |
| Flyer type(s) & cadence | Weekly Flyer (6071) + Monthly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday (2 weeks lead time).
- **Cadence:** Available From Wednesday / Valid Wednesday → Available/Valid To Tuesday.
- **No linking document** at setup (but Tag/QC references a Tag/QC-specific linking doc).

## Upload & setup (owned by FLEX)

- Codesheet = **"Imposition.xlsx"** → open in Google Sheets. Delete everything except PZ, pages, stores (like a generic codesheet). Rename headers to: `pricing zone`, `stores`, `Page 1`, `Page 2`, … until all pages have headers. Download as CSV.
- Upload — Name = anything, **config `generic`**, base path = full path where files are (e.g. `/2025/072325`), **toggles: 2nd and last unchecked.**
- Setup QC: standard 4 thumbnails; **external run name = "Weekly Flyer".**

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** box each item; box sale story with multi-items. **Include retailer logo, sign-up page, social media**; exclude coupons, packaged deals, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; linking doc Tag/QC-specific):** include brand, Name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.

## Post-processing / FQC (owned by DOC)

- **Offer ID / Digital Coupon tagging:** check the Albertsons FTP for an "Offer ID" xls (search "Haggen", e.g. `010225_Haggen_OfferIDs.xlsx`). If present, download; if none for the dates, skip.
  - Remove "-D" from the **OMS Offer ID** column.
  - Use Item Search (keyword from "Bold Headline" column as name) and tag custom fields:
    - **Just For U (No Barcode):** Y (same for all items).
    - **Digital Coupon URL:** `https://www.haggen.com/foru/coupons-deals.html?event=Weekly%20Ad%20Coupons` (same for all items).
    - **Offer ID:** e.g. `91223945` (from OMS Offer ID with "-D" removed).
- External run name = "Weekly Flyer"; standard 4 thumbnails; **remove categories from all pages.**
- If an Offer ID doc was available, Item Search: Just for you (no barcode) IS NOT / item type Item; Digital coupon URL IS blank; Category contains coupon.
- **Flyer Review type: Lite.**

---
*Source: Haggen OneGuide (Google Doc `1V7azqnU10YBCHuP_pSpQobjYTdcYb_G9xJ5naXMkTDY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
