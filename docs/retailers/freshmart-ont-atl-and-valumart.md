# Freshmart ONT/ATL & Valumart — Processing Guide

> **Source:** Freshmart ONT & ATL OneGuide (Google Doc `1oSrqQWkOYj_zdBARs0E7TTHWNwJAMsaaRcYMAU1nBKU`), updated Oct 14, 2025. Contacts/credentials omitted.

Loblaw-family (LCL) account. Bilingual (English/French). Two upload variants — **Freshmart ONT (FMO)** and **Freshmart ATL (FMA)** — plus a **SuperValu (SV) West clone** at FQC.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer types | Weekly (FT 5994) |
| Processing | Auto-stack; Flex (Flyer Review); **OS — Setup**; **Feedel/retailer data services YES**; no coupons |

## Files & schedule
- **Files arrive:** Monday.
- **Cadence:** Available From Wednesday; Valid From Thursday → Available/Valid To Wednesday (1-week run).
- **Preview date: Sunday.** Workflow: Upload/Setup (Vendor, 5 days out) → FQC (DOC, 2 days out) → Corrections.

## Pre-setup (owned by DOC)
- Codesheet file names: search "WKXX AI FINAL CODES" in email — `WKXX_AI FM ATL CODES FINAL.xls`, `WKXX_AI FM ONT CODES FINAL.xls`.
- Download all codesheets to the SuperValu/Shop Easy Food/Freshmart Flex folder; update the Flex Tracker; note any store changes from the email as a comment on the flyer run.

## Upload & setup (owned by Flex)

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded** (Edit Details → show/hide rarely-used fields → Height → 4096.0 → OK). If pages already added, flag to Full-Time Ops and continue.

**Set a Sunday preview:** Overview → Edit Details → "Preview start date" = the Sunday before the available date.

### Freshmart ONT (FMO)
- Manual upload: Pages > Edit > select the FMO folder for the correct week (e.g. FMO WK42) > upload as **English** pages.
- Use the codesheet **Online tab** for page order; match Page Name to File Codes name.
- **RISK:** Freshmart often doesn't resend pages repeated across multiple weeks (e.g. HOTM Flap, Thanksgiving pages running weeks 40–42) — confirm with DOC, then re-upload from the original week's folder.
- Flyer Creation: create **1 English PZ** (FMO - English) + **1 French PZ** (FMO FR, check "Cross Language Box", switch language to French). Add the FMO store set to both PZs; confirm store count matches the codesheet.

### Freshmart ATL (FMA)
- Same pixel-height + manual upload (FMA folder). Note: **2 distinct front pages** labeled MN and R by pricing zone.
- Create **4 PZs**: MNLD-ENG, MNLD-FR (cross-language French), R-ENG, R-FR (cross-language French); confirm the correct page 1 in each. Add MNLD store set to both MNLD PZs and R store set to both R PZs. Confirm store counts match both codesheet tabs.
- Zone naming (per codesheet): sometimes separate zones for M and N; **change PAGE 01 to the version matching the codesheet.**

### Setup QC (owned by Flex)
- Geo tab: no added/removed stores unless specified.
- Edit Details: Sunday preview; External Run Name "Weekly Flyer Valid Thursday [date] - Wednesday [date]" (no FR version); no theme.
- Check flyers in item view: dates correct; correct Freshmart logos at top (FMO / FMA MN / FMA R / FMA SQ). **Merge pages** if items are split across two pages (Page > Merge page → left + right → Submit → wait for sessions → place merged page in the PZ at the correct position).

## ⚠️ Common errors / risk items
- **Pixel height must be 4096 before pages are uploaded** (2026 change).
- **Repeated pages not resent** — re-upload from the original week's folder (see FMO/FMA risk above).
- **URL leads to a different item** → FLAG. **Item quantities in the description** → FLAG.
- **Raw meat images:** change any raw-meat image to a Cut Out — do not select the PDF.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking document required):** **Include** coupons and packaged deals; **exclude** retailer logo, sign-up page, social media, special weblinks. Box where there's a unique price; box only the item. Box banners with a nofrills.ca link — **do NOT box/tag Facebook, Twitter, etc.**
- **Tag / Tag QC (Medium; Auto-tag OFF; linking document required):** Brand box-draw/QC specific. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price; **exclude URLs.**
  - **Name** all caps: Brand Product Name, Quantity (comma before quantity); **tag all information in FRENCH AND ENGLISH separated by "/".**
  - Description = plain (non-bold) descriptive text; metrics like 2.56/kg.
  - SKU only when it appears in the flyer.
  - **Images — Rule 1:** cleanest PDF (white, clear background); shadows/lifestyle → do not use PDF. **Rule 2:** for meat/seafood/cheese, only use a PDF image if the product is **packaged**; unpackaged → do not use PDF.
  - **PC Optimum:** tag as normal item; sale story includes PC Optimum points.
  - **Page-level categories** during box draw for all pages except the front cover (Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce).
- **Image QC:** clean PDF preferred except raw meat products (→ cutouts).

## Post-processing / FQC (owned by Flex)

**Pre-Final QC (3FL Flex):** merge flap pages (two flaps → merge together; one flap → merge with cover/P01) and complete thumbnails (Standard 4 — 1065x600 2pg, stock premium 1pg, storefront carousel premium 2pg, storefront carousel organic 1pg; start at the logo, do NOT include flap pages).

**ON & ATL Final QC:** confirm dates (Available From Wed, Valid From Thurs, Available/Valid To Wed, 1-week run); available everywhere; no preview date; Internal Run Name "WEEK #"; External Run Name "Weekly Flyer Valid Thursday…"; no theme. Image QC (clean PDFs except raw meat → cutouts); thumbnails marked complete; pages tab items tagged = tag QC; 1–2 categories/page except page 1; PZ item view (re-run tile-gen if boxes don't line up); geography no week-over-week changes; update store codes per retailer email. Complete FQC checklist.

**SV Clone Final QC:** open the Freshmart West flyer run; re-run page tile generation; add stores only to Zone Y (all next to the Y store set — ~10 stores as of Nov 2024, confirm in the SESV WEST Code file); wait for sessions; item view (dates correct, Zone Y has only the Freshmart logo, boxes copied over); ignore the "Zone B no stores/FSAs" warning; FQC checklist (geography unchanged, run item cutout generation); check vertical scroll.

## Flyer review
- **Type: Lite.** Owned by Flex.

## Out-of-processing
- **Page Swap:** standard baseline page swap.
- **NEW page-swap final step:** page swaps often cause **Page Stitching** issues (visible page doesn't match overlaid items) — **always rerun Page Tile Generation** after the swap sessions kick off; if issues remain, rerun and mark complete from Vendor Box Tag onward; confirm the swap in item view across **all** pricing zones.

---
*Source: Freshmart ONT/ATL & Valumart OneGuide (Google Doc `1oSrqQWkOYj_zdBARs0E7TTHWNwJAMsaaRcYMAU1nBKU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
