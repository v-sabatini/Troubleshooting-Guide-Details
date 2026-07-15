# Sobeys Liquor Banners — Processing Guide

> **Source:** Sobeys Liquor Banners OneGuide (Google Doc `1AwI1snaXw2jYKC0iSqDyLzygPYK-c-1Yk9TkY6Bc1Vk`), updated Mar 27, 2026. Contacts/credentials omitted.

> Covers the liquor banners processed together — **Sobeys Liquor** and **Sobeys/Safeway Liquor** (the latter cloned from Sobeys Liquor). Related banners in the shared vendor guide: Thrifty Foods Liquor, Safeway Liquor.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#sobeys` |
| Hosted URL | (not specified in OneGuide) |
| Flyer type(s) & cadence | Weekly. Available From Wednesday, Valid From Thursday; Available To / Valid To Wednesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); **OS completes coupon processing**; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Tuesday (Excel file on FTP + distribution file via email).
- Review recap files each week for **new stores** — add them properly and flag any unfamiliar/new stores in the channel.

## Upload & setup (Vendor → Flex)

1. Download the week's Excel file from FTP; **manual page upload** using the Excel as reference; confirm all pages uploaded to FTP.
2. **Create pricing zones; add all stores** (Sobeys Liquor and Sobeys/Safeway Liquor). For **Sobeys/Safeway Liquor do NOT add SK stores.**
3. Download the week's distribution from email; create a **generic code sheet** for Sobeys/Safeway Liquor stores; upload the code sheet.
4. Edit details; QC thumbnails (Standard 4 + thumbnail + `first_page_thumbnail_400w`); box Scene+ callouts (usually page 1); check sessions; Setup QC; auto-stack spotcheck; mark vendors to High.

### ⚠️ Common errors / risk items (retailer-specific)

- **Codesheet column rules (critical):**
  - Any column containing **W6** is exclusive to Alberta and applies **only to Sobeys/Safeway Liquor**.
  - **W4 – SK Base** is designated for **Sobeys Liquor**; the **W4 Clone** is for Sobeys/Safeway Liquor. **Do NOT include W4 – SK Base in the regular weekly Sobeys/Safeway runs.**
- **Special item dates:** always scan the PDF for items with promotional start/end dates that differ from the flyer dates and set the item's valid-from/to to match the PDF.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** include coupons, retailer logo, sign-up page, social media, special weblinks; **exclude packaged deals.** Box all items attached to a price (include as much of the image as possible); multiple items sharing one price go in one box; delete duplicate/overlapping boxes. The bottom callout does **not** need to be boxed.
- **Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc required; PDF image auto-selection ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Brand & Name:** enter brand in the Brand field AND at the start of the Name field.
  - **Disclaimer:** always include (e.g. "Limit of Two", "For limited time only").
  - **Dollars off / percent off:** only if explicitly stated. Do **not** put "Save $X" amounts in the Dollars Off field when savings are conditional on buying multiple items.
  - **Scene+ tagging:** individual item "Scene+" → put in **Sale Story**; "with Scene+ card" → put in **Postfix**. Flyer-level Scene+ callouts (usually wine, e.g. "BUY ANY 6 BOTTLES … GET 250 PTS") go in the Postfix with "MIX & MATCH" in the Sale Story after "Save $". **Individual item callouts take priority over the flyer-level callout.**
- **Image QC:** select a PDF-extracted or composite image where available; clean images for all items.

## Post-processing / Final QC (owned by DOC)

- Tag page categories during box draw (at least one category); ensure Scene+ items are tagged.
- **Sobeys Liquor FQC:** upload inserts (see Insert Tracker + insert-process video), box & tag inserts, confirm Scene+ tagging, no overlapping boxes, check sessions, mark vendor tasks complete, Final QC.
- **Then clone Sobeys Liquor → Sobeys/Safeway Liquor banner:** add all stores under SK, add key messages, Final QC.
- Where AIR MILES appears in older videos, it is now **Scene+**.
- **New process:** on the Jira ticket, add a note to send the preview URLs to the retailer once FQC is complete. External run name for all banners: "Weekly Flyer".

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Sobeys Liquor Banners OneGuide (Google Doc `1AwI1snaXw2jYKC0iSqDyLzygPYK-c-1Yk9TkY6Bc1Vk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
