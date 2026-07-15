# Laferte — Processing Guide

> **Source:** Laferte OneGuide (Google Doc `1E3rqftq6rrQakhfM-JA45jdEgxkUo3Ry-u2qQzs0MXk`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Flyer type(s) | Weekly Flyer · Monthly Catalogue |
| Language | **French** |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **FLEX** owns upload & FQC; **Vendor** owns Links/Image QC; **OS** does FQC step |

## Files & schedule

- **Files received:** Wednesday, via **SFTP** (retailer sends a notification email; sometimes files arrive via WeTransfer and must be uploaded). Ad-hoc catalogues are made under the weekly flyer type.
- **Publication cadence:** Available/Valid Thursday–Wednesday.
- **Linking document:** Yes — sent via FTP.

## Upload & setup (owned by Vendor)

- Download the link sheet from the Laferté FTP.
- Pages → Edit → Upload from FTP → select pages from the week folder → **toggle language to FRENCH** → Save → **change Conversion Library to Ghostscript** → Save → Auto-group → Save & Complete.
- Flyer creation: one **French** pricing zone `Base`; add all stores.
- Setup QC: Available/Valid Thu–Wed; toggles **Shown everywhere**; external run name = the front-page main callout (`Laferté` / `Laferté Pro` / etc.); no theme; thumbnails Standard 4 (1065x600 2pg, Stock Premium 1pg, Storefront Carousel Premium 2pg, Storefront Carousel Organic 1pg). **Download the link sheet and attach it to ALL vendor tasks.**

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot ON; linking doc used for both Box & Tag):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box any product with a price; box items with multiple prices/variations separately.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box & Tag):** tag from both the PDF and the linking document (URLs come from the link doc). Include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand handled in Box Draw. **PDF Image Auto Selection is ON, but DO NOT USE PDF IMAGES.**
- **URL/Links QC (Vendor):** Overview → Items without URL must be **0**; add missing links per the attached link sheet.

## ⚠️ Common errors / risk items & troubleshooting

- **Out-of-processing page swaps (every Wednesday, before Thursday go-live):** the retailer sends a WeTransfer link with updated pages and an `.xlsx` listing changes. Rows highlighted **green/yellow** are the items to update — extract the affected page from the new PDF, do the page swap, and update the items.
- **Pages are blurry:** Pages → Edit → confirm pages uploaded with the **gamma** processor → change processor type to **Ghostscript** → Save & Complete → re-run Page Tile Gen system task.
- **Missing special characters (accents):** Pages → Edit → change processor type to **gamma 9.0.6** → Save & Complete → re-run Page Tile Gen → republish.

## FQC / flyer review

- FQC (FLEX): complete Link/Image QC; confirm dates, "Shown everywhere" toggles, external run name, no theme, thumbnails; Vertical Preview (blurry → troubleshooting above); Geo tab — no changes.
- **Flyer Review type: Lite.**

---
*Source: Laferte OneGuide (Google Doc `1E3rqftq6rrQakhfM-JA45jdEgxkUo3Ry-u2qQzs0MXk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
