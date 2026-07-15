# 2001 Audio Video — Processing Guide

> **Source:** 2001 Audio Video OneGuide (Google Doc `1W-GzfCn…cPI_F0`), updated Feb 17, 2026.
> Electronics retailer. 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#2001-a_v` |
| Hosted URL | flyertown.ca/flyers/2001audiovideo-flyer |
| Flyer type / cadence | 2616 Weekly — files received **Monday**; available/valid **Friday→Thursday** |
| Processing | Auto-stack; Flex (Processing Support); DOC does post-processing QC; Feedel data services: yes; no coupons |

## ⚠️ Risk item
- **One picture, two prices:** draw **two item boxes** (one per price/SKU) even when only one image is present.

## Upload & setup (owned by Vendor)
- Retailer uploads files to SFTP + a Google Drive link (usually Fri); **wait for the linking document (Mon/Tues) before uploading** — vendors need it.
- Pages → Edit → select the broken-up pages → Auto-group → Save → Save and Complete.
- Create pricing zone (description "base"); add **all stores (~20)**; let Sessions finish; check **Geography** (no stores/FSAs added/removed).
- Vendors tab: assign tasks + **attach the "FLYER PRICING" linking doc** (mass attachment → all vendor assignments); comment "linking document attached."
- Overview → Edit Details: available everywhere, no theme. Thumbnails: Standard 4. **Clear FTP files** when done.

## QC specifics
- **Box Draw:** Low; Auto-Box **on**, Box QC bot **on**. **Include** coupons, packaged deals, retailer logo, special weblinks (exclude sign-up/social). Box all items separately; multiple prices boxed individually.
- **Tag / Tag QC:** Low; Auto-tag **off**. Include everything (name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs). Put **SKU + brand + size in the name**; most items categorize as **Electronics**; disclaimer only if inside the drawn box.
  - **URLs:** search the SKU in the attached spreadsheet, use the "Specific Links" column; **do NOT use URLs containing "searchterm."**
- **Item Image QC (DOC):** run **Data Piping** (aim 95–96%, 83% acceptable; some items won't pipe if not yet live on the site — hit "Generate Data Piping Groups" if none load). Select data-piped image → else PDF → else cutout.

## Final QC (DOC)
- Every SKU boxed & tagged individually. SKUs with "/" boxed as 1 item; a "2-room set" with two prices is OK as 1 item.
- **Items without a URL** (Overview → Items without a URL): copy SKU, find in the Flyer Pricing linking doc; if absent, search 2001audiovideo.com by SKU (bundles → Package Deals). Price mismatch vs. site → check the "SALE ENDS" date. Remove any "search" links (Item Search → URL contains "search").
- **Include the SKU / model number in every item name.** Re-run Data Piping after any live page swap.
- **Flyer Review type: Lite.**

---
*Source: 2001 Audio Video OneGuide (Google Doc `1W-GzfCn30LPxhEKA9LqbWgcDh7e0Nt8B1jLXMcPI_F0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
