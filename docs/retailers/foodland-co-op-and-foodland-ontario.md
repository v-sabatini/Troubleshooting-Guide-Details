# Foodland Co-op (Atlantic) & Foodland Ontario — Processing Guide

> **Source:** Foodland Coop (Atlantic) & Ontario OneGuide (Google Doc `1L_Jnloomvtd8tPHJGe9XhIvW1oByylFkHKtrupG5eoc`), updated Jul 15, 2024. Contacts/credentials omitted.

Sobeys-family account. Three flyer types: **Foodland ATL Weekly**, **Co-op Advantage Weekly**, and **Foodland ON Weekly**. Coop and Atlantic share the same codesheet (zone code) and distribution.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium (S1C1)** |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URLs | atlantic.foodland.ca/flyer/ · ontario.foodland.ca/flyer/ |
| Flyer types | ATL Weekly · Co-op Advantage Weekly · ON Weekly (FT #3614) |
| Processing | Auto-stack; **3FL Flex**; **Feedel/retailer data services YES**; no coupons |

## Files & schedule
- **Files arrive:** Wednesday.
- **Cadence:** Available From Wednesday **6:00 AM**; Valid From Wednesday → Available To Thursday 6:00 AM; Valid To Tuesday.
- **Preview date: Monday.** Workflow: Upload/Setup (5 days out, DOC) → 3FL Pre-FQC Tasks (Mon) → Inserts/SJC Links/Deep Links/Custom Tiles/Ad-Hoc QC/FQC (Tues).

## ⚠️ Common errors / risk items (per week)
- **SJC Links** — check the week's SJC Links in the Sobeys Insert Tracker and box/tag them.
- **Deep Links** — check the week's Deep Links in the tracker and box/tag them.
- **Custom Tiles** — check Slack for weekly custom tiles. Store/FSA-specific → create new PZs. Triggers → create trigger + file an OPTICS ticket. Apply to Storefront Premium and Storefront Carousel Premium.
- **ATL distribution:** delete store #9272 (Grand Bank, NL) from Zone 2 — it should exist only in Zone 3A.

## Upload & setup

### ATL Weekly (owned by Flex)
1. Download Zone Code → change all pages to FLYER in Media column; delete Size column; empty Pages column (keep the column); change Position → Pages; find "alt" replace with "atl"; un-bold; rename headers "Zone 1", "Zone 1A"…; remove Coop pagination columns; **save as xls.**
2. Download Distribution Recap → delete store #9272 from Zone 2.
3. Upload Zone Code in Codesheets — **config `sobeys_safeway`**, base path from FTP (to last folder), **toggles 3, 4, 5, 6** → Save → Process.
4. Upload Distribution Recap — **config `foodland_atlantic`**, base path `/`, **toggle 1** → Save → Process.
5. Thumbnails: Standard 4, 400W. Edit Details → available everywhere; Available From Wed @ 6am; Key Messages "Weekly Savings"; External Run Name "Weekly eFlyer mm/dd - mm/dd". Setup QC; Vendor priority High.

### Co-op Advantage Weekly (owned by Flex)
- Same zone-code manipulation as ATL (renumber Pages 1,2,3…; rename headers "Zone 2A", "Zone 4"…; remove ATL pagination columns).
- Upload Zone Code — config `sobeys_safeway`, toggles 3,4,5,6.
- Upload Distribution Recap — **config `foodland_coop`**, base path `/`, toggle 1.
- Same thumbnails/details/priority as ATL.
- **Note:** no inserts for the Foodland Coop flyer type.

### ON Weekly (FT #3614, owned by DOC)
1. Download Zone Code → same manipulation (Media FLYER, delete Size, empty Pages, Position → Pages, un-bold, rename "Zone 1", "Zone 1A"…); save as xls.
2. Upload Zone Code — config `sobeys_safeway`, base path from FTP, toggles 3,4,5,6.
3. Download Zone Summary or Distribution Recap; build a generic store codesheet (headers "stores", "pricing zone"; copy store # + PZ name); save as CSV.
4. Upload — **config `generic_stores`**, base path `/`, check **"Store or Store Set Assignment"**.
5. Confirm stores assigned in the Pricing Zones tab.
- **Setup QC:** mark vendor tasks urgent; 4 standard thumbnails; External Run Name "Weekly eFlyer"; no theme; complete Setup QC.

## QC specifics (all banners)
- **Retailer risk items:** Scene+ items (add Scene+ to sale story + [Scene+] category); Scene+ Member Pricing (prefix "Scene+ Member Pricing" incl. the "+", disclaimer "$xx without Scene+ Card", [Scene+] category); Compliments items (Brand = Compliments; Name begins with "COMPLIMENTS").
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **Include** all items and social-media links (MyGroceryOffers, App Store, Google Play); **exclude** coupons and retailer logo.
- **Tag / Tag QC (Low; Auto-tag OFF):** Brand box-draw/QC specific. Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - Brand always included; Compliments → include in both Brand and Name. Name entered as-is, no brand in Name (except Compliments); French name goes to Description, not Name.
  - Price per weight: **/lb in postfix, $$$/kg in Description.**
  - Scene+ sale story format: "xxx Scene+ PTS when you buy x."
  - Valid dates only if they differ from the flyer run.
  - Categories based on page headings; usually one per item; Scene+ items get the corresponding category **plus** [Scene+] (only case of 2 categories).
- **Image QC:** pick cleanest image; use cutout if no clean PDF. **Do not use PDF** for lifestyle images or images with heavy shadows/black outlines.

## Post-processing (Pre-Final QC tasks)
- **Item Image QC** (Vendor, Mondays), **Category QC** (Flex/3FL), **Scene+ Points QC** (Flex), **Page Category QC** (Flex — no categories on page 1), **Compliments QC** (DOC — Compliments in both Brand and Name), **SJC Links** (DOC), **Deep Links** (DOC — red weeks = none), **Custom Tiles** (DOC), **Inserts** (Flex — none for Coop).
- Item search tips for QC: `[Sale Story][Contains][PTS]`, `[Categories][IS NOT][Scene+]`, `[Brand][CONTAINS][compliments]`, etc.; use Export/Import Items for bulk fixes.

## Final QC (owned by Flex)
- Geography check; Vertical Preview; confirm Air Miles highlights; preview all versions; confirm inserts for the week; **legibility heights 40/35.** Complete FQC checklist.
- **Flyer Review type: Lite.** Owned by DOL.

---
*Source: Foodland Co-op (Atlantic) & Foodland Ontario OneGuide (Google Doc `1L_Jnloomvtd8tPHJGe9XhIvW1oByylFkHKtrupG5eoc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
