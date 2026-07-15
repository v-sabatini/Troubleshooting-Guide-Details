# Co-op Gas Bar — Processing Guide

> **Source:** Co-op Gas Bar (C-Store) OneGuide (Google Doc `1rehrXOORXHDQtyTsyk3RNhQIQ-gTvgbi0_SDoKMZw2w`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | co-op.crs/flyers |
| Flyer type(s) | Monthly C-Store deals (pub 10718) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel/retailer data services |

## Files & schedule

- **When files arrive:** Thursday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday.
- **Linking document:** Digital Inserts xlsx from the FTP (e.g. "Wk 46–49 C-Store Digital Inserts.xlsx"). If multiple URL links in the xlsx, mass-attach the linking document to vendor tasks; if only one link, leave a comment in the vendor task with the link.
- **Owners:** Upload & Setup = Vendor; FQC = DOC.

## Upload & setup (owned by Flex)

- Open the xls document from sFTP to find the order of pages. "Already Up" refers to pages that have **CSTORE Quick Deals** (usually 2 pages).
- **Manual upload** of the pages in the shared xls document; manually complete grouping; Save and Complete.
- **Setup QC:** Flyer Creation → create 1 pricing zone called **Base** → add all stores. Edit Details: **no theme, no external run name, Key Messages = Monthly Deals.** Complete Setup QC checklist and mark autostack spotcheck complete.

## ⚠️ Common errors / risk items

- **Triggers.** Certain pages are only meant for certain weeks (found under Duration on the Digital Inserts overview / Triggers tab). If triggers are needed, **create a JIRA ticket to remind the team to review the removal/addition of those pages.**
- Look for multiple products within a single deal.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** Linking document required (Box-specific). Box each item individually. **Include** retailer logo, sign-up page, social media, special weblinks (banners with calls to action). **Exclude** coupons and packaged deals.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-selection ON.** Linking document required. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Image QC:** prefer a clean PDF when available; avoid images with black/gray backgrounds or that don't match the item.
- **Item Category QC (DOC):** Categories = Snacks & Beverages; Google Category by best judgement of the PDF item. Use a clean PDF; if items have different names, use the clean PDF from the first item.

## FQC (owned by DOC)

- Complete spot checks; Standard 4 thumbnails (drawn on the page with the run dates).
- Edit Details: run dates correct, available everywhere, no theme, **External Run Name = Monthly Deals.**
- Confirm all items boxed and links attached (mass attachment or comments).
- **Check the Triggers tab** on the Digital Inserts overview — create a JIRA ticket if trigger review is required.
- Unblock the flyer if Publish Publications is red; complete Vertical Preview and Final QC checklist.
- **Flyer Review type: Lite.**

---
*Source: Co-op Gas Bar OneGuide (Google Doc `1rehrXOORXHDQtyTsyk3RNhQIQ-gTvgbi0_SDoKMZw2w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
