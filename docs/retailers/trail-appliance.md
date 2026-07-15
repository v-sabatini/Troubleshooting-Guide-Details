# Trail Appliance (BC Flyer) — Processing Guide

> **Source:** Trail Appliance (BC Flyer) OneGuide (Google Doc `1Rj3fjjzJvm6Of2MRZOS74X0E6TRPjKu683FtJoi-ZCE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | retailer channel, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Weekly Flyer |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); Upload (Vendor) → Image QC (Flex) → FQC (DOC); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday · Available To Monday · Valid From Tuesday · Valid To Tuesday.
- **Linking document:** Yes.

## Upload & setup (Vendor, manual)

1. Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload.
2. Auto-Group or manually enter grouping numbers; ensure the correct language is selected. Save & Confirm — **do NOT Process Internally.**
3. **Pricing zone:** create a **Base** pricing zone with all applicable pages. Save & Confirm.
4. Add all stores from the **"BC stores" Store Set** unless the retailer specifies otherwise.

### Setup QC checklist (Vendor)

- Confirm all pages uploaded correctly (Pricing Zone → Items View). **RISK:** if uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.
- Confirm flyer dates (usually first or last page of the flyer).
- Complete thumbnails (**4 Standard**). **A custom-tile upload is used for the Storefront Premium and Storefront Carousel Premium thumbnails.**
- Retrieve the linking document uploaded with the files and mass-attach to all vendor tasks. Set preview dates. Complete Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **MSRP handling:** Do **not** put MSRP* prices in the prefix or Current Price. Put the MSRP in the **Sale Story** (e.g. "MSRP $2100"), and for any item with MSRP pricing add the disclaimer: *"MSRP is the Manufacturer's Suggested Retail Price only. This does not equate to a market price or our regular price."* (do not repeat MSRP elsewhere).
- **Banners/logos:** all store logos and some banners must be boxed and tagged **per the linking spreadsheet** (banners have no product IDs). Text banners are boxed/tagged as **Link or Page Link** per the spreadsheet.
- **Multi-version items:** include the model and price of the other version in the description; add color-price variations in the disclaimer (e.g. "Same price for white", "add $50 for stainless steel").

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking document required (used for both box & tag). **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box everything; box store logos and social/store-location banners **only if in the linking document**. One box for a single-item URL attachment; multiple boxes when the URL attachment/layout PDF shows multiple items.
- **Tag / Tag QC (Low; Auto-tag ON; PDF auto-select ON):** include brand, name, pre/postfix, valid dates, description (include SKU), SKU, price, original price (= MSRP), sale story, categories, disclaimer, URLs.
  - **Prefix** usually "sale priced" (never MSRP); for multi-items use the item type as prefix. **Postfix** = anything after the price (e.g. "after 10% instant rebate").
  - Every item needs at least one category (be specific). Tag all store logos and social icons as **Link**. Use every link in the spreadsheet; category items tagged as Link type, page-link rows tagged as Page Links.
- **Image QC:** clean PDF preferred; no black backgrounds/shadows; cutout when no clean PDF; use cutout for packages/multi-item banners.

## Pre-FQC / FQC (DOC)

- Confirm dates vs. PDF and availability toggles. Thumbnails correct with **custom tile applied** (includes retailer logo). No items without links. Standard checks: all items boxed/tagged, spotchecks complete (20% of pricing zones), previews clickable, sessions completed, geography correct.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Trail Appliance (BC Flyer) OneGuide (Google Doc `1Rj3fjjzJvm6Of2MRZOS74X0E6TRPjKu683FtJoi-ZCE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
