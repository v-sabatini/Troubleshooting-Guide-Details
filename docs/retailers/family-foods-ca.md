# Family Foods CA — Processing Guide

> **Source:** Family Foods CA OneGuide (Google Doc `17eQ8dKvCZeKPtck2VN6iGkx1zu6UVgfvE_bhhikQyZM`), updated Nov 24, 2025. Contacts/credentials omitted.

> Sobeys banner (Core+ segment, relationship quality: Good).

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channels | `#sobeys`, `#sobeysops`, `#sobeys-dataservices`, `#3fl-sobeys` |
| Flyer types | Weekly (6367) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Vendor (Setup); DOC (FQC); no coupons; Strategic Ops — yes, Feedel/retailer data services |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Wednesday, Valid From Thursday; Available To Monday, Valid To Tuesday.

## ⚠️ Risk items
- **Missing in Hosted (all flyer types):** do NOT mark as missing in hosted — they are not on our hosted and the toggle is hidden.
- **Page 1 recipes:** ensure OS boxed/tagged the recipe; if not, do it — Pages → each Page 1 version → Box QC → Tag: Display Type **Link**, Name **Recipe of the Week**, URL `http://www.familyfoods.ca/recipes`.

## Upload & setup (owned by Vendor — manual)

- View files: Merchant page → Details → View Files.
- Rename the publication: Overview → Edit Details → Internal Run Name **`Family Foods mm/dd/yyyy`** (dates = the Available From date).
- Pages → Edit → select the week's files → Select Files. **Pop Up, Ribbon, or Family Value pages appear 1–2×/month and always order at the end.** Order: Standard pages, Ribbon, Pop Up, Family Value. **⚠️ Ensure the page folder dates match the flyer run dates.**
- Manually group pages by number, then order the Pop Up pages. Save → Save & Complete → Submit.
- **Create 4–6 pricing zones** by description, adding pages whose names contain the tag: **8AA, 8FF, 8AAFF, 4FF, 4FFBON** (4 pages, effective Sept 4 2025), **4CF** (4 pages). Ribbon/Pop Up/Family Value pages, if present, go in all zones.
- **Add stores/FSAs** by matching PZ name to store-set name (e.g. PZ 8AA → Add All from 8AA). **⚠️ 8AAFF logic:** if only 8AAFF present, use 8AA + 8AAFF store sets; if both 8AA and 8AAFF present, use each PZ's matching set; if 8AA absent but 8AAFF present, use 8AA + 8AAFF sets for the single 8AAFF zone.
- **⚠️ FSA errors:** if FSAs don't generate, re-generate in Sessions **(only during upload — not after FQC)**; if still failing, flag processor/lead.
- Edit Details: **hidden in hosted;** EXTERNAL run name `Weekly eFlyer 1/1 - 1/10`; Key Messages (long & short) = **Weekly Savings.**
- Merge pages if items are cut off (**soft merge**): PZ → Actions → Store Front Spotcheck → Edit Page → Merge Pages.
- Vendors: set all task priority **HIGH**; add comment to box & tag the recipe on all Page 1s if there's a recipe callout. Mark AutoStack Spotcheck complete.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc)
- **Include** packaged deals, special weblinks. **Exclude** coupons, retailer logo, sign-up page, social media.
- Draw clean boxes around items. **Box Recipe of the Week** (first or last page) and **Family Foods website callouts** (first-page footer).

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- Include name, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude SKU, disclaimer, URLs (except the two below).** Brand is box-draw specific.
- **Name:** bold text in product details; include brand in the Name field. **Brand** if applicable.
- **Description:** as in flyer; item descriptions are non-bold under the name. **KG/LB:** lb price is the main price with `lb` as postfix; **kg price goes in the description** for all produce/meat/seafood.
- **Valid dates:** overrides if applicable — pages 9–12 sometimes have monthly valid dates.
- **URLs:** tag only for **Recipe of the Week** and the **Family Foods website callout.**
- **Categories:** every item (full category chart in the OneGuide: Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, **Scene+** as a second category on Scene+ items, Dairy, Deli, Health & Beauty, Seafood).

### Image QC
- Per the Family Foods CA Image QC video (in the OneGuide).

## FQC (owned by DOC — latest done: 3pm the day before live)
- Thumbnails Standard 4 (do not include white trims).
- Sessions → Item/URL Verification → Verify; for Image QC: Page-Level Tasks → **PDF Image Auto Selection → Force Selection → Process All.**
- Page categories: skip page 1; use two tags where possible.
- **⚠️ Risk — Page 1 recipes:** box/tag as above (Link, "Recipe of the Week", familyfoods.ca/recipes) if OS missed them.
- Horizontal & vertical preview; storefront-merge any cut-off text.
- Final QC: warning "Not all categories that are used in pricing zones have thumbnails" is **OK**. Re-run sessions (incl. Auto Selection); may need to re-run Thumbnails and Item Cutouts.

## Flyer Review
- **Type: Lite.**

## ⚠️ Live-date common errors
- **Disclaimer** left blank on items with the deposit symbol → tag: **"Plus deposit and/or environmental levies where applicable."**
- **URL** for Recipe of the Week mis-tagged → correct URL is `http://www.familyfoods.ca/recipes`.
- **Missing in Hosted** → do not mark (hidden toggle, not on our hosted).

## Out-of-processing
- Page swaps — see the baseline page-swap video referenced in the OneGuide.

---
*Source: Family Foods CA OneGuide (Google Doc `17eQ8dKvCZeKPtck2VN6iGkx1zu6UVgfvE_bhhikQyZM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
