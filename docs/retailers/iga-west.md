# IGA West — Processing Guide

> **Source:** IGA West OneGuide (Google Doc `19rBM54T1ql-vUWioGWidz435XUYoeiw0zbZ1T-uiV40`), updated Nov 24, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#sobeys-dataservices`, `#3fl-sobeys` |
| Flyer type(s) & cadence | **Weekly Flyer (3609)** |
| Processing | Auto-stack |
| Who's involved | Flex (3FL); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Wednesday 3:00 AM → Monday 11:59 PM; Valid Thursday 3:00 AM → Tuesday 11:59 PM.

## ⚠️ Risk items (Scene+)
- **Scene+ callout:** every offer with an accompanying Scene+ offer must have **Scene+ tagged in the Sales Story** — including offers that only show points (no "Scene+" text).
- **Scene Member Pricing items:** Prefix "Scene+ Member Pricing" (**don't forget the + sign**); Disclaimer "$xx without Scene+ Card"; Categories add [Scene+].
- Do **not** tag Scene+ in the disclaimer field — only in the sale story.

## Upload & setup (owned by Vendor — manual)
1. Pages → Edit → IGA West → folder with the flyer publication date.
2. Select all pages → select files → autogroup → Save & Complete.
3. FTP → download the **zone codesheet** for pagination & number of zones.
4. Rearrange pages in the pricing zone per the zone codesheet.
5. **Create pricing zones** — use the zone name from the codesheet as the PZ description; follow the codesheet pagination. One zone → one PZ; more than one → create all (zone 2 has unique pages).
6. **Add stores** — the **Distribution Recap** doc in the FTP is the store distribution list. Open the generic stores codesheet (IGA West tab): column A = stores from the Base Run List, column B = pricing-zone name. Save as .csv. In FAdmin, toggle to codesheet, attach the .csv, Save & Complete ("using the root path" warning → OK). Process Codesheet (should run green); confirm store count matches the Base Run List.
7. **If flap pages:** order P01, FLAP 1, FLAP 2, P02, … then Pricing Zones → More → Storefront Summary to merge the skinny flap pages.
8. Overview → Edit Details: Available From & Valid From **3 AM**; available everywhere; no theme; **External run name** "Weekly eFlyer valid [from date] - [to date]"; preview date = the following Monday; Key Messages (long & short) "Weekly Savings".
9. Thumbnail QC — get the logo: `Thumbnail_1065_x_600` (2 pages), `Stock_premium` (1 page), `Storefront_carousel_premium` (2 pages), `Storefront_carousel_organic` (1 page), `Thumbnail` (2 pages), `First_page_thumbnail_400w` (1 page).
10. Mark setup QC checklist complete; once sessions run, mark autostack spotcheck complete.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required)
- **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
- Box all items attached to a price; include as much of the image as possible; multiple items with one price → same box. Box the sign-up promo box as a whole; box Scene point offers as individual items.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude** SKU.
- **Brand/Name:** always enter brand in the brand field and at the start of the name field.
- **Prefix/Postfix/Price:** use drop-downs, exactly as PDF. "Buy ### or more" → prefix text; "Buy ### at $$$" → description with price as Original Price. **Prices under $1 need a leading "0."** (e.g. $0.51).
- **Valid dates:** only add overrides if the item date differs from the flyer; watch Blue Friday dates.
- **Description:** as in flyer; **lb price is the main price** (lb postfix), **kg price goes in the description** for all produce/meat/seafood.
- **Coupons:** display type Coupon; always tag sales story, disclaimer, valid dates; tag Blue and Green coupons separately; Scene+ offers → Scene+ in Categories and Category Highlights.
- **URLs:** N/A during tagging (deep links added post-processing).

### Image QC
- Pick the cleanest image; if none clean, choose the cutout. **Do not use PDF images** for lifestyle shots, heavy shadows/black outlines, or partial images.

## Post-processing / FQC
- **Item Category QC (Flex):** categories include Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, Scene+, Dairy, Deli, Health and Beauty, Seafood (see OneGuide chart for what falls where). Scene+ items get Scene+ as a **second** category.
- **Deep Links QC (multiple parties, new 02/25/2025):** check the Sobeys Insert Tracker → Deep Links tab (dates in red get no deep links); tag the banner/item as a link with SKU + link.
- **Final QC (DOC, by Tuesday 3 PM):** check Scene+ per PZ (Sale Story contains "PTS"); description lb/kg rule; Sessions → Page Stitch (Stitch All); QC Categories for unreviewed items; **Legibility Heights 50/40**; horizontal + vertical preview; merge skinny pages in storefront spotcheck (if flaps in position 1-2, move the cover page to position 1, flaps follow — retailer instructed this, no notification needed).
- **Inserts:** find the week's inserts in the Sobeys Insert Tracker (WEST tab); upload insert pages (Pages → Edit → Year → IGA → WEST → Inserts, or local); Save and Continue → Process Internally → Submit; box & tag using the link in the inserts doc (or copy from prior week if unchanged — verify URL); add insert pages to **all** PZs at the position in the tracker. Flyer sorting: newest first, then current flyer.
- **⚠️ IGA West does NOT receive Voila inserts** even if listed in the Sobeys insert tracker.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Inserts:** same as above; file an **OPTICS ticket** (OPSMR board), move to "Lead Review" lane and assign to the lead. Sobeys inserts can be combined into one ticket.
- **Troubleshoot:** if sessions fail after adding insert pages, remove the pages from the PZ and from Pages, then re-upload.

---
*Source: IGA West OneGuide (Google Doc `19rBM54T1ql-vUWioGWidz435XUYoeiw0zbZ1T-uiV40`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
