# Gosselin Photo — Processing Guide

> **Source:** Gosselin Photo OneGuide (Google Doc `13NvGfP04hY5Ws5ygTTRQ4FhbtHxtS2XFOZPlLvzSUBM`), updated May 5, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#gosselin` |
| Hosted URL | gosselinphoto.ca/en/about-us/flyer |
| Flyer type(s) & cadence | Flyer #8290; Ad-Hoc |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (FQC); no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Ad-Hoc. The contact sends EN + FR flyer PDFs plus a link to the linking document.
- **Cadence:** Available From Friday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **Linking document:** Yes (separate EN and FR linking docs, `.xlsx`).

## Upload & setup

- **Setup (owned by DOC):** download all 3 assets (EN flyer, FR flyer, `.xlsx` linking doc) and upload directly to the SFTP. *(SFTP host/user/password are in the OneGuide — not stored here.)* While files transfer, create/update the flyer run shell.
- **Edit Details:** available everywhere; dates provided via email and printed on the flyer; no theme (unless a seasonal theming brief applies).
- **Upload (owned by Vendor):** once files are in the SFTP, manually upload all EN and FR pages → Auto-Group for pagination → change language to French for all FR pages.
- **Pricing zones:** two zones — **EN** (all English pages) and **FR** (all French pages). Add all stores to both.
- **Attach the linking document to all Vendor tasks** in the Fadmin pipeline, then Setup QC.

## ⚠️ Common errors / risk items — item-level valid dates
- **RISK ITEM:** they have flyer-level valid dates **but also item-level valid dates** (bottom of the flyer). E.g. Canon items valid until the 14th, all others until the 28th. **Ensure item-level valid dates are applied** by reading the disclaimers below — we have been called out before and they were very upset.
- Add these disclaimers to **all** items:
  - **"Limited quantities. Certain conditions apply."**
  - **"Quantités limitées. Certaines conditions s'appliquent."**

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals, retailer logo, sign-up page. **Exclude:** coupons, social media, special weblinks. Linking doc used for both box/tag.
- Box each item; use text boxes as required.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name (include brand and size), pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **URLs** provided in separate EN and FR linking docs.
- **Categories:** normally 2 — Camera Lenses, or Cameras & Camcorders.
- **Disclaimer:** tag each item with its corresponding brand's disclaimer at the bottom of each page.
- **Image QC:** use a clean PDF image whenever possible; select cutouts when clean PDFs aren't available.

## Post-processing / FQC (owned by Vendor)
- **URL/Links QC:** for "Items without a URL", search the linking doc (each item is in its respective Page # tab). Confirm item-level valid dates and adjust tagging. For non-shoppable "items" (banners/CTAs with a link), set **Display Type: Link** and paste the URL.
- **FQC:** Data-Piping → Data Piped Image → filter → Data Pipe All (if items aren't data-piping, verify links aren't leading to 404). Custom Action → Set Cutout Images. Horizontal and Vertical preview (after Auto Publish finishes). Then Final QC.
- **Flyer Review type: Lite.**

---
*Source: Gosselin Photo OneGuide (Google Doc `13NvGfP04hY5Ws5ygTTRQ4FhbtHxtS2XFOZPlLvzSUBM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
