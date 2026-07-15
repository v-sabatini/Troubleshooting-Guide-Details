# Matériaux Pont Masson — Processing Guide

> **Source:** Matériaux Pont Masson OneGuide (Google Doc `134qnMqtapyFXuwUoIQ8ie5YgF1qq-mNM4mUZOzbwBZE`), updated Feb 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#materiaux-pont-masson`, `#flex-processingsupport` |
| Flyer types | **Weekly** (bi-weekly cadence) · **Seasonal** (ad-hoc) |
| Processing | Auto-stack; Flex (Processing Support); no coupons/Feedel |
| Languages | EN + FR |

## Files & schedule
- **Files received:** Thursday (~11 AM by email): one set of EN pages, one set of FR pages, and a linking `.csv`.
- **Cadence:** Available & Valid From Thursday → To Wednesday.
- **Linking document:** Yes.

## Upload & setup (owned by Vendor)
- **Pre-processing:** open the retailer's `.csv`, add the same headers, save as `.xlsx`. Download all documents and transfer to SFTP. Retailer sometimes sends extra banner/promo links — paste them into the flyer run comment box.
- **Upload:** manually upload files; EN pages set EN, FR pages set FR; Auto-group → **Save**, confirm, then **Save & Complete**.
- Attach the `.xlsx` linking document to vendor tasks.
- **External run names:** EN = *Weekly Flyer*, FR = *Circulaire Hebdomadaire*.
- **Pricing Zones:** 1st PZ = **EN** (English), 2nd PZ = **FR** (French); add all stores to **both**.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc used for both Box/Tag. **Include** packaged deals; exclude coupons, retailer logo, sign-up page, social media, special weblinks. Box each item block.
- **Tag / Tag QC (Low; Auto-tag ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - ⚠️ **DO NOT USE PDF IMAGES** (despite PDF Image Auto Selection being enabled).
  - All visible SKUs tagged in the SKU field; text matches the language version and is pulled from the spreadsheet where possible.
  - **Links:** add a URL to any item that has a SKU — search the SKU on **pontmasson.com**.
- **Image QC:** clean images when available; if no clean PDF image, select the cutout.

## ⚠️ Common errors / risk items
- **Seasonal ad-hoc publications** are uploaded into the "Seasonal" flyer type — new flyer shells must be created.
- **Do NOT use PDF images** even though auto-selection is on.

## Post-processing / FQC (owned by Flex)
- **URL/Links QC:** check the retailer email for special banner links and tag correctly. Item search for items missing URLs → search SKU on pontmasson.com/en (EN) then re-check FR (PZ id `fr`) using pontmasson.com/fr.
- **Ad-hoc QC:** clear remaining spotchecks; review images for black backgrounds; draw QC thumbnails (1065×600, Storefront Carousel Premium, Storefront Carousel Organic); dates match PDF front page; set seasonal theme (even if No Theme); item counts equal across PZs; all prices/sales stories/offers/CTAs boxed; vertical preview clickable; Geography no changes WOW.
- **FQC:** confirm **Flyer Sorting = "Flyer Type Newest First"** (Weekly above Catalogues); dates correct; toggles correct; thumbnails include retailer logo; all items boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography unchanged.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swap process.

---
*Source: Matériaux Pont Masson OneGuide (Google Doc `134qnMqtapyFXuwUoIQ8ie5YgF1qq-mNM4mUZOzbwBZE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
