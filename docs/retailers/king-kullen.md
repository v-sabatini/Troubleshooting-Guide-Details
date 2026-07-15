# King Kullen — Processing Guide

> **Source:** King Kullen OneGuide (Google Doc `1SSkywo4lwKqLjB_FCNUBXpvbTR2wOKhVJ0o2CnU41no`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified in guide) |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flex-flyer-review` |
| Hosted URL | kingkullen.com |
| Flyer type(s) | Weekly Flyer (flyer type **3253**) |
| Processing | Auto-stack; no coupons; no Feedel/retailer data services |
| Involvement | **OS** does the upload; **FLEX** owns FQC & post-processing |

## Files & schedule

- **Files received:** Tuesday.
- **Publication cadence:** Available Thursday–Friday, Valid Friday–Thursday, 1-day consumer preview.
- **Linking document:** N/A.

## Upload & setup

- **OS uploads** for King Kullen. Check the FTP on Tuesday to confirm correct files (verify valid dates).
- Fill out the Vendor Setup & Setup QC Tracker (Tuesday tab) by 3:30 PM with the Flyer Run ID and file-readiness; `#vendor-setup-retailers` posts EOD callouts.
- **Manual upload (if run by vendor):** Pages > Edit > select the week's pages > Autogroup (Covchain is always page 1). Page language English. One pricing zone **Base**, English, Add All (32 stores).
- **Setup QC:** Leg heights **30/20**; Thumbnails Regular 4 (thumbnail_1065 2pg, Stock Premium 1pg, Storefront Carousel Premium 2pg, Storefront Carousel Organic 1pg). Available Thu–Thu with 1-day preview, Valid Fri–Thu, Available Everywhere, No Theme.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Brand handled in Box Draw.
  - Sale-story patterns: "SAVE $X.XX" → tag Dollars Off. "Save X¢ On Each" / "Save Up to $X" → **DO NOT tag Dollars Off.** Beer: "MFR'S REBATE" and mail-in-rebate story/disclaimer patterns.
- **Image QC:** clean PDFs preferred; cutouts if no clean PDF. For multi-image boxes pick the best/main image, no cut-off products.

## ⚠️ Common errors / risk items (FQC — owned by FLEX)

- **Deli items (page 3):** apply the disclaimer **"Deli Items Not Available At All Stores"** to ALL deli items. If many are missing it, copy the Page 3 Page ID, use Item Search on that Page ID, multi-edit the deli items, add the disclaimer.
- **Beer items (page 4/5):** every beer item needs a sale story. **No red/yellow banner → "MFR's rebate"**; **red/yellow banner present → "$X.XX DIGITAL SCAN CODE, MFR'S REBATE"** (substitute the flyer price).
- **Floral (last page):** all flowers/flower items need the disclaimer **"Floral Items Not Available At All Stores"**.
- Open all pages to confirm disclaimers/sale stories are tagged. Check both pricing zones' Vertical Preview + Full Screen so item boxes are clickable. Re-run any failed sessions.

## FQC / flyer review

- Edit Details: valid dates match flyer (check page 1); Available from = 1 day before Valid from; Available everywhere; no external run name; no theme.
- **Flyer Review type: Lite.**
- **Out-of-processing:** N/A.

---
*Source: King Kullen OneGuide (Google Doc `1SSkywo4lwKqLjB_FCNUBXpvbTR2wOKhVJ0o2CnU41no`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
