# SuperValu (Shop Easy Food) / Freshmart — Processing Guide

> **Source:** SuperValu / Shop Easy / Freshmart West (SV Clone) OneGuide (Google Doc `1OpCYUmidGoqXxpAve1s7ZG2V5Em9BlKJOWToRcJ60IM`), updated Oct 14, 2025. Contacts/credentials omitted.

> A **Loblaw** family of banners: process **SuperValu** as the primary, then **clone** it to **Shop Easy Foods** and **Freshmart West (SV Clone)**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer type | Weekly (5994) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Wed→Wed, Valid Thu→Wed (NFW starts from **3 AM**). **Preview:** Sunday.
- Codesheets are labeled **WK__ AI FINAL CODES**; download and upload them to the LCL Flex Upload folder and update the Flex Tracker.

## Upload & setup (owned by FLEX)

- **NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded** (Edit Details → show/hide rarely-used fields → Height → 4096.0 px → OK). If pages were already added, flag to Full-Time Ops and continue.
- **Manual upload:** use the **SE SV Online** tab of the codesheet (check page numbers and stores). Upload SuperValu files for the correct week as **English pages**; number per the codesheet (**there are two page 1s — both numbered page 1**; pages usually 1–8). Save & complete; in the pop-up choose **ghostscript 9.06 gamma** and submit.
- **Pricing zones:** `SE SV ONLINE` (English) and `FRESHMART ONLINE` (English; change page 1 to the one with "Y" in the description). Create **cross-language FR zones** by copying the ENG layout and cross-languaging to FR for all PZs.
- **Stores:** add stores **only to SE SV ONLINE** (Add All → store set "SV 5 Stores" = 3 stores). FRESHMART ONLINE has no stores.
- Confirm vendors assigned; preview date 2 days after upload; **External Run Name** = "Weekly Flyer Valid Thursday [date] - Wednesday [date]" (no FR version); no theme; **Key Messages** = "This Weeks Savings" (no FR version).
- After sessions complete, check item view: dates correct, SuperValu/Shop Easy/Freshmart logos on SE SV ONLINE; only Freshmart logo on FRESHMART ONLINE; **merge pages** if items are split between two pages (Page → Merge page → left + right → submit; then place the merged page in the correct PZ position for both zones).
- **Setup QC (FLEX):** Available Wed→Wed (1-day preview), Valid Thu→Wed (**NFW from 3 AM**); Sunday preview start; external run name set; no theme; comment "ran gamma"; mark off Auto Spotcheck.

## ⚠️ Common errors / risk items (retailer-specific)

- **Set Pixel Height to 4096 first** — must be done before uploading pages.
- **Two page 1s** — both must be numbered page 1.
- **Raw meat images:** change any raw-meat image to **Cut Out** — do not select the PDF. Only select PDF images for meat/seafood/cheese when the product is **packaged**.
- **FSA guardrail (NEW):** ensure FSAs **T6C** and **R3P** have NOT been generated (Pricing Zones → Stores/FSAs). If generated (highlighted red), run the **Remove FSAs** custom action (set Flyer Run ID + Pricing Zone ID to the weekly flyer) and re-verify.
- **Page swaps** often cause **page-stitching** issues — always **rerun Page Tile Generation** after swap sessions kick off (especially post-live); if issues remain, rerun and mark complete from Vendor Box Tag onward; confirm the swap in item view for all PZs.
- Live-date flags: URL leading to a different item → Flag; item quantities in the Description → Flag.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include coupons and packaged deals. Exclude retailer logo, sign-up page, social media, special weblinks. Box only the item (unique price), not extra space; box banners containing a nofrills.ca link; do NOT box Facebook/Twitter/etc. or logo banners.
  - **Page-level categories** during box draw for all pages **except the front cover** (Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce).
- **Tag / Tag QC (Medium; Auto-tag OFF; linking doc required):** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.**
  - **Name:** ALL CAPS, format `Brand Product Name, Quantity` (comma before the quantity). **Tag all info in FRENCH AND ENGLISH, separated by "/".**
  - **Description:** plain (non-bold) text, first letter capitalized, metrics as 2.56/kg, "Product of…", "No. 1 grade", "frozen", "selected varieties".
  - **SKU:** only when appearing in the flyer. Multibuy items need Postfix Text + Postfix Amount.
  - **Valid dates:** only include overrides when a promotion sale story indicates it.
  - **PC Optimum:** tag as a normal item; Sale Story includes the PC Optimum points (e.g. "Get 5,000 PC Optimum points when you buy a $25 gift card").
- **Image QC:** cleanest PDF (white/clear background); if shadows/lifestyle, "Do Not Use PDF Images." For meat/seafood/cheese, PDF only if **packaged**.

## Final QC & cloning (owned by Vendor / Flex)

- **Pre-Final QC (Flex, 3FL):** merge flap page(s) to the right (or with the cover if only one); thumbnails Standard 4 (1065x600 = 2pg, stock premium = 1pg, storefront carousel premium = 2pg, storefront carousel organic = 1pg) starting where the logo is, **excluding flap pages** even when merged.
- **Final QC:** confirm dates (Available Wed→Wed, Valid Thu→Wed, 1-week run), available everywhere, no preview date, internal run name "WEEK #", external run name set, no theme; Image QC (clean PDF except raw meat → cutout); thumbnails complete; pages tab item counts match tag QC; categories 1–2 per page except page 1; item view all boxed; Geography no change; run the T6C/R3P FSA guardrail; complete the FQC checklist.
- **Clone to Shop Easy Foods & Freshmart West:** Overview → Ad Hoc Processing → Clone → deselect SuperValu, select the target banner (Shop Easy Foods Weekly Flyer CQ5 / Freshmart Weekly Flyer) → **Copy to existing flyer run** (matching week) → set Copy Tracking Codes/URLs to **YES** → Clone.
  - **Shop Easy Foods clone FQC:** rerun Page Tile Generation; add stores to the SE-identifier PZ (Store Set "Shop Easy Foods", 13 stores as of Nov 2025) + the FR cross-language zone; leg heights 45/20; verify thumbnails/categories copied; sessions complete; item view correct; vertical preview OK; triggers set up; FQC checklist → item cutout generation marked as "Clone".
  - **Freshmart SV Clone FQC:** rerun Page Tile Generation; add stores to the FRESHMART-identifier PZ (Store Set "Freshmart SV Clone", 12 stores as of Nov 2025) + FR cross-language zone; confirm only the Freshmart logo on FRESHMART ONLINE; sessions complete; vertical preview OK; triggers set up; FQC checklist → item cutout generation marked as "Clone".

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- **Page swaps** are standard, but always rerun Page Tile Generation afterward to avoid stitching issues (see risk items).

---
*Source: SuperValu (Shop Easy Food) / Freshmart OneGuide (Google Doc `1OpCYUmidGoqXxpAve1s7ZG2V5Em9BlKJOWToRcJ60IM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
