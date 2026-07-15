# Axep / Intermarché / Intermarché International — Processing Guide

> **Source:** Axep/Intermarché/Intermarché International OneGuide (Google Doc `1OqBJfSMaaF1ehUichTWDQkf1SFEYv7RNk1xMVkfGWeU`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URLs | axep.ca/circulaire · lintermarche.ca/flyer-fr · intermarcheinternational.ca/circulaire |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; Flex (3FL + Flyer Review: upload, pre-FQC); **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Tuesday (Axep), Tuesday (L'Inter-Marché), Friday (L'Inter-Marché International).
- **Cadence:** Available From Wednesday / Valid From Thursday / Valid To Wednesday. **Preview:** Monday before. No linking document.
- **Workflow:** Upload by Vendor; FQC by DOC; Corrections post-live. Part of the Loblaw/LCL codesheet program.

## Upload & setup (owned by Flex)
- **Pre-setup:** find the week's code sheets (labelled `WK__ QC FINAL CODES`), download and upload to the LCL Flex Upload Folder, and update the Flex Tracker.
- **Axep-specific:** the flyer run won't appear in Legacy Pipeline. Open it via the Axep flyer-runs URL; it will show "Flyer Run Not Found" and no pipeline — **disregard**; once pages are uploaded the message clears and the pipeline generates.
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded.** Edit Details → show rarely-used fields → Height dropdown → 4096.0 px → OK. If pages were added first, flag Full-Time Ops and continue.
- **Manual upload:** select all files under the correct week → Autogroup → **change language toggle to French, Save** → Save & Complete. Check the Merchant FTP to confirm all pages pulled in.
- **Pricing zones (2):** **F** (French files — confirm layout from the week's code sheet ONLINE tab) and **F EN** (copy layout from F, tick cross-language box, cross-language to English, save).
- **Stores:** select the corresponding store set by zone name — do **NOT** "Select All Stores" (all three banners share one store database). Confirm the store count matches the code sheet; check weekly Loblaws emails for added/removed stores.
- Setup QC: Available Wed–Wed (1-day preview) with **Sunday preview start date**; Valid Thu–Wed; external run name "Weekly Flyer Valid [dates]"; no theme; confirm FTP fully uploaded; geography unchanged week over week.

## ⚠️ Common errors / risk items (retailer-specific)
- **Do not "Select All Stores"** — it pulls stores across all three banners (shared database).
- **Name field must include BOTH French and English product names** (e.g. "CROUSTILLES | POTATO CHIPS, 200 - 235 g"), ALL CAPS, format "Product Name, Quantity" with a **comma before the quantity**. Don't add "$" to quantities.
- **Do not put in the Name:** unit-price metrics ("6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties" — those go in the Description.
- **Brand only in the Brand field** — nowhere else. Do not enter brand, NG Code or SKU in the description.
- **URL leads to a different item → Flag.** Item quantities in the description → Flag.
- **Page swap final step (NEW):** page swaps often cause page-stitching issues (visible page doesn't match overlaid items), especially post-live. **Always rerun Page Tile Generation** after the page-swap sessions kick off; if issues remain, rerun and mark complete Vendor Box Tag onward; confirm via item view of all pricing zones.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons, retailer logo, sign-up page, social media, special weblinks. **Include** packaged deals. Draw a box only where there's a unique price for an item — nothing extra; do not box banners or social icons.
- **Tag / Tag QC (Medium; Auto-tag OFF):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU, URLs, Article Number.** Linking doc is Tag/QC specific; brand is Box-specific. Watch multibuy items (prefix + postfix combos). Valid-date overrides only when a promo sales story indicates it. Every item needs a category.
- **Image QC:** clean PDF where possible; use **cutout if PDF isn't clean and for meat items without packaging.**

## FQC / post-processing (owned by DOC)
- **Pre-FQC (3-FL Flex):** merge flap pages to the right (two flaps → merge together; single flap → merge with cover/P01). Thumbnails Standard 4, starting where the logo is; do not include flap pages even when merged.
- **Final QC:** confirm dates (Available Wed, Valid Thu–Wed, 1-week run), available everywhere, no preview date, internal run name "WEEK #", external run name "Weekly Flyer Valid …", no theme. Image QC clean PDFs except raw meat → **Cut Outs** (never the PDF). Confirm thumbnails complete; items-tagged matches Tag QC; 1–2 categories per page except page 1; check all items boxed and boxes line up (re-run tile-gen if not); geography unchanged; update store codes per note/retailer email.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put the flyer run ID in the LCL tracker; run ghostscript 9.06 gamma as needed; flyer sorting (current weekly, upcoming weekly, secondary pubs newest→oldest); article-# revision.
- Standard page swap (per training video) — plus the mandatory Page Tile Generation rerun noted above.

---
*Source: Axep/Intermarché/Intermarché International OneGuide (Google Doc `1OqBJfSMaaF1ehUichTWDQkf1SFEYv7RNk1xMVkfGWeU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
