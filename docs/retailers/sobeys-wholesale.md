# Sobeys Wholesale (West & Atlantic) — Processing Guide

> **Source:** Sobeys Wholesale (West & Atlantic) OneGuide (Google Doc `1Z38JDSimxlCQS2ypNnOiyBH1kgOWJGlujgVfxfpCB7Q`), updated Oct 20, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium (S1C1) |
| Availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeysops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URL | sobeyswholesale.com/en |
| Flyer type(s) & cadence | Sobeys Wholesale — **Monthly**, ad-hoc files. Available From Wednesday (**3 AM for West only**), Valid From Wednesday; Available To Thursday (**3 AM for West only**), Valid To Tuesday. Preview Monday |
| Processing | Auto-stack; no Flex; no OS; no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> The process is the **same for West and Atlantic**; the two regions differ only by files, stores, and (for West) the 3 AM availability times.

## Files & schedule

- **When files arrive:** ad-hoc (monthly cadence). Codesheet/PDFs come from the merchant ops contact (credentials in the OneGuide — not stored here).

## Upload & setup (owned by DOC)

1. In the month's flyer run, **manually upload pages** (Pages → Edit): **West** → Wpg files; **ATL** → Atl files. Save and Complete.
2. Flyer Creation → create a **"base" pricing zone**.
3. **Add stores:** **West** → store 5557; **ATL** → all other stores (5 stores) — **do NOT include 5557.**
4. **[Overview] → [Edit Details]:** for **West only**, Avail/Valid From = 3 AM; Hidden in Hosted; **External run name = "Sobeys Wholesale mm/dd – mm/dd"** (valid from/to dates); no theme.
5. Thumbnails: Standard 4 + Thumbnail + 400W. Ledge Heights: 50/40. Setup QC checklist → mark complete. Vendor Tasks → High.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** include retailer logo; exclude coupons and packaged deals. All items boxed and tagged individually.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, description, price, sale story, categories, disclaimer, original price; **exclude valid dates, SKU, URLs.** Brand used for both Box and Tag.
  - **Disclaimer (all items):** "Prices and promotions are only available at Sobeys Wholesale locations."
  - Example tagging: Prefix "3 for", Current Price "0.89", Postfix "When you buy in multiples of 3".
- **Image QC:** pick the cleanest image; cutout if no clean image. Do **not** use PDF images when there are lifestyle shots (product on a cutting board/plate) or too many shadows/black outlines.

## Post-processing / Final QC (owned by DOC)

- **Item Category QC:** one category per item, best judgement. **Note: there are no Scene+ categories, so skip adding Scene+.**
- **Final QC:** **add the disclaimer to all items** ("Prices and promotions are only available at Sobeys Wholesale locations.") via Item Search → Apply Filters → Select All → Multi Edit Items → add disclaimer → Save Changes. Then run the standard FQC checklist.

## Flyer review

- **Flyer Review Type: Lite** (owned by DOL).

---
*Source: Sobeys Wholesale (West & Atlantic) OneGuide (Google Doc `1Z38JDSimxlCQS2ypNnOiyBH1kgOWJGlujgVfxfpCB7Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
