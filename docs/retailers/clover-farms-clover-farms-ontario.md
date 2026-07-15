# Clover Farms + Clover Farms Ontario — Processing Guide

> **Source:** Clover Farms + Clover Farms Ontario OneGuide (Google Doc `1SScC27emf37pTgSFShXv3pGKtMO0h7DAowVFNnyGN2M`), updated Jul 12, 2025. Contacts/credentials omitted.

Part of the Sobeys family (alongside Co-op and ValuFoods), sharing pages and a combined Flex Flyer Review.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | **Flipp only — NOT available on hosted** |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | sobeys.com |
| Publications | This Week's Flyer / Clover Farm (**3794**) · Clover Farm ONT (**8866/8966**) |
| Cadence | Weekly. Files Monday. Available Wed, Valid Thu–Wed (**CF ONT now shares the same dates**) |
| Processing | Auto-stack; Flex (3FL + Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Files received **Monday**. Get the **Zone list** from the merchant email, download and manipulate.
- **Delete the ValuFoods (Zone 3) and Co-op (Zone 4) columns** → should leave **Zone 1, Zone 2, Zone 5, Zone 6**.
- Save/upload the run list to the OS Setup Files folder. Run list end-date names the flyer (e.g. publication ending Oct 2 → run list "October 2nd").

## Upload & setup

### Clover Farm (This Week's Flyer, #3794) — owned by Vendor
1. Code sheets → Name = `upload`, add zone-list codesheet.
2. **Config Name = `clover_farm`**.
3. PDF Base Directory = up to `/Zone` only (e.g. `/April_6_7_2022`).
4. **Toggle = 1,3,4,6**. Save & run codesheet.
   - If it goes yellow saying pages already uploaded, that's fine (pages are shared with other merchants) → **Force processing**.
5. Pricing Zones created for **Zone 1, Zone 2, Zone 6**; mark Flyer Creation complete.
6. **Manually add Zone 5 page 1:** Pages → Edit → upload Zone 5 Page 1 manually → create Pricing Zone "Biggoods Zone 5".

### Clover Farm ONT (#8866) — manual upload
- **CF-ONT files are now under Zone 7 in the sFTP.**
- Pages → Edit → expand **Zone 7** → select files → **Auto-group** (any pop-up/added page goes at the end) → Save & submit.
- Create Pricing Zone **Zone 7** → "add all" beside **clover ontario** stores.

### Setup QC
- Edit Details: **hidden on hosted**, no theme, key message from the rotating Sobeys list (e.g. "Weekly Ad. Weekly Savings.", "Deals of the Week").
- External run name = **Weekly eFlyer + valid dates** (e.g. "Weekly eFlyer 06/20-06/26"). CF ONT gets 1 extra day.
- **Check dates** (bottom of page 1). **Verify page order in Storefront Spotcheck.** New Zone 5 PZ must have the same page count as the others (usually 8 or 4).
- QC thumbnails (Standard 4). **Box & tag the recipe callout on pg 1** → `http://familyfoods.ca/recipes/`; add a vendor note so it isn't missed.

## ⚠️ Common errors / risk items
- **Page order in Pricing Zones:** confirm all pages uploaded (usually 8). PopUp pages go **at the end**.
- **New Zone 5** must match the other zones' page count.
- Shared-page "already uploaded" yellow warning is expected → force processing.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** all items, recipe callouts, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons. Linking doc required.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude:** disclaimer, URLs.
- **Brand** always entered in both the Brand field and the start of the Name field.
- **Price per weight:** `$$$/kg` in Description, `/lb` in postfix.
- **French:** separated from English by a line break; English description first, then French name on its own line followed by French description.
- Categories from page headings / best judgement (Snacks → Grocery; Household → Home Essentials).

### Image QC
- PDF Image Auto Selection is ON — a PDF should be selected automatically.

## FQC (owned by DOC)
- Autostack spotcheck; confirm **4 pricing zones**; verify page order in Storefront Spotcheck; Zone 5/6 page counts match.
- Edit Details as above; QC thumbnails; box/tag recipe callout if not already.
- **Complete FSA removal + addition — the FSA is `A0H`.**
- Rerun page stitching + page tile generation; check vertical/horizontal preview on PZ.
- **Available start time is 6 AM** for Clover Farms, Co-op and ValuFoods.
- Post-FQC: send preview links to the merchant (Clover Farms + CF ONT).
- **Flyer Review type: Lite** (combined Clover Farms | Co-op | ValuFoods review).

## Out-of-processing (page swap)
- Open run → Pages → Edit → select new page from FTP → add "REV" to the name → Save & Complete → **Copy Items** from the old page (same page only), adjust the changed item(s) → box/tag → add to PZ.

---
*Source: Clover Farms + Clover Farms Ontario OneGuide (Google Doc `1SScC27emf37pTgSFShXv3pGKtMO0h7DAowVFNnyGN2M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
