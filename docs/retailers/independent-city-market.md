# Independent City Market — Processing Guide

> **Source:** Independent City Market OneGuide (Google Doc `1ikZpPksToIoNiY-MGLcmyIxnp9NQkU2Vo22b5TJkOOQ`), updated Dec 18, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core · Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | independentcitymarket.ca |
| Flyer type(s) & cadence | **Weekly Flyer** (ICM/LCM) |
| Processing | Auto-stack |
| Who's involved | Flex (3FL + Flyer Review); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available Thursday → Wednesday; Valid Thursday → Wednesday.
- **Preview:** Sunday internal preview (set "Preview start date" to the Sunday before the available date).
- **Linking document:** No.
- **Custom action — Article Corrections:** run the LCL custom action "LCL Article Number Report" to download the Article Corrections report in FAdmin.

## Upload & setup (owned by Flex; DOC drops Final Codes first)

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → show/hide rarely-used fields → Height → select **4096.0 pixels** → OK. If pages are already added, flag to the Full-Time Ops stakeholder and continue.

- DOC must drop the Final Codes into the shared LCL Codesheet Drive before Flex's upload shift.
- Reference the **VM ICM** Final codesheet in inbox for pagination and store changes. **Ignore the PRINT and VM ONLINE tabs**; only process the ICM and LCM tabs (these are the pricing zones).
  - ICM tab only → 1 PZ (ICM), base = 5 stores (all ICM + LCM).
  - ICM + LCM tabs → 2 PZs (ICM, LCM); store sets already separate the stores — confirm assignment.
  - Kosher tab (usually "ICM K") → 3rd PZ (Kosher); confirm store on codesheet. Kosher PZ usually only gets **store #479** (then remove #479 from Base).
- Upload all files under the correct week **as English pages**; number per codesheet (File Code order usually 1, 4, 2, 3, or 1, 4, 2, 3, K).
- Add stores (5 total between zones). Check dates in item view; **no consumer preview**. Check Merchant FTP to confirm all pages pulled in. **No theme.**
- **External Run Name:** "Weekly Flyer - Valid [insert valid dates]".
- Add the weekly codesheet into the shared Google Drive for Flex to complete post-processing.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot OFF)
- **Include** coupons, packaged deals, sign-up page, special weblinks. **Exclude** retailer logo, social media.
- Draw a box only around each item that has a unique price (not additional places). Box interactive "click here" buttons.
- **CON FLAP page:** draw one box over the full page and link out with the PC Optimum digital-coupon load URL provided in the OneGuide.
- **Page-level categories** on every page **except the front cover** (Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce).

### Tag / Tag QC (Medium; Auto-tag ON)
- Include: brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Name:** ALL CAPS, order "Brand Product Name, Quantity" (comma before quantity); product name bolded; English only (French → description). Do **not** put "/kg" metrics, "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — those go in the description.
- **SKU:** enter as shown; **SKU starts with "2"** — if it doesn't, ignore it. Drop leading zeros. Keep unit-of-measure suffixes (`_KG`, `_EA`, etc.) in both SKU and Article Number fields.
- **URLs:** fetch from SKU. If the link goes to a **different item or size**, remove it and find the correct item by name; if it goes to the **Loblaws home page** or the **correct item in a different flavour**, leave the link. All items with a SKU should have a URL.
- **Article Number fields** (bottom of Tag interface): copy the product SKU into Article Number 1 (matches SKU + fetch URL). Multiple SKUs → apply in order to Article Number 1, 2, 3, 4.
- **Joe Fresh callouts:** box and tag as a LINK to joefresh.com/ca.

### Image QC
- Use clean PDF where possible; use cutout if PDF is not clean. Meat/fish must be in a package (else cutout). White background only — no lifestyle backgrounds.

## Post-processing / FQC
- **URL/Links QC (DOC):** reference Final Codes; links are in the Notes section of the final codes; verify Flex's tagging.
- **Pre-FQC (Flex):** spotchecks; merge flap pages to the right page via storefront spotcheck; box/tag codesheet URLs; Legibility Heights 40/30; Image QC; QC thumbnails Standard 4 (start on 2nd/3rd page if flaps at start); Article number check (SKU not blank + URL blank → fetch; Article Number 1 blank + URL not blank → add); no theme; page categories (no category on page 1, 1-3 per page); check geography, vendors tab, vertical scroll; flyer sorting newest at top, secondary pubs last.
- **FQC (DOC):** add flyer ID to LCL Tracker by Tuesday afternoon.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put flyer run ID in the LCL tracker. Flyer sorting: current weekly (regular) → upcoming weekly → secondary pubs newest→oldest.
- **Page swaps** are standard. Completing page swaps often causes **Page Stitching issues** (visible page doesn't match overlaid items) — especially post-live. Best practice: **always rerun Page Tile Generation** after page-swap sessions kick off; if issues remain, rerun and mark complete Vendor Box Tag onward. Open item view of **all** pricing zones to confirm the swap succeeded.

---
*Source: Independent City Market OneGuide (Google Doc `1ikZpPksToIoNiY-MGLcmyIxnp9NQkU2Vo22b5TJkOOQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
