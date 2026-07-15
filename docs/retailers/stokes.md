# Stokes — Processing Guide

> **Source:** Stokes Canada OneGuide (Google Doc `1TYqSWUoQjrsc0DK7tFlDeUFEYlJn9H8YFykYdFUEL4c`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#stokes` |
| Hosted URL | stokesstores.com |
| Flyer type | Ad Hoc |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Mon→Mon, Valid Tue→Tue.
- Files usually sent via e-transfer: **EN files, FR files, and a linking document** (must be attached to vendor tasks). Upload files to the SFTP via Cyberduck/CoreFTP/Filezilla.

## Upload & setup (owned by Vendor)

- Confirm dates and times (**sometimes 6am–6pm!**).
- Visible everywhere, no theme, no external name.
- **Manual upload** (files are lowercase in FTP); always choose the **high-rez** option.
- **2 zones: EN and FR.** Assign all stores to each. Change page languages so all stores get English & French pages.
- **Attach the linking document to all vendor tasks.**
- Check pages for design issues and cut out margins.
- After setup: external name = same as flyer name (EN and FR versions); **legibility heights 45/35**; thumbnails Standard 4 (Thumbnail 1065x800, stock_premium, storefront_carousel_premium, storefront_carousel_organic); Geography no missing/added stores.
- Setup QC (FLEX): mark all boxes complete, ignore warnings.

## ⚠️ Common errors / risk items (retailer-specific)

- Not all items have a brand name.
- **Do NOT enter the SKU in the Description field.**
- **General rule:** name = all text **before the first comma**; description = all text **after the first comma** (e.g. 6 L, 14.5 oz, stainless steel, set of 6).
- **Do NOT enter "SAVE %" / "EPARGNEZ %" into the Sale Story field.**
- Original prices given as ranges can go in the Sale Story field instead of the Original Price field.
- SKU, multiple item pictures, and prices are tagged separately.
- **Cut-off margins / text overlay:** troubleshoot via page-level sessions → tile generation → ghost script; or ask a Lead and file an OS ticket; if not resolved, request new pages.
- All Stokes logos are boxed; all social media icons are boxed.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** Include retailer logo (first & last page), sign-up page, social media (Facebook, Twitter, Instagram), special weblinks. Exclude coupons, packaged deals. Box every item with a price separately (text boxes when needed); box items with individual prices separately even within one picture; box all banners with URLs.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand per box specifics. **Exclude pre/postfix and valid dates.** Brand: case-sensitive, as in flyer. Name ends at the first comma; description begins after it.
- **Image QC:** select clean PDFs if available; cutouts OK if no clean PDF.

## Final QC (owned by Vendor)

- Mark Autostack Spotcheck complete.
- **Items without URLs:** download the linking document from vendor tag tasks and add missing links; while open, check all yellow rows for unique instructions.
- Item images: clean if possible, cutouts if not. Thumbnails Standard 4.
- Pages: categories **max 3 per page**; confirm both EN/FR pages uploaded; check/update dates.
- Pricing zone vertical/horizontal; Geography same as last run.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- **Out-of-processing:** send a preview to the retailer at least a few days in advance.

---
*Source: Stokes OneGuide (Google Doc `1TYqSWUoQjrsc0DK7tFlDeUFEYlJn9H8YFykYdFUEL4c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
