# Superior Grocers — Processing Guide

> **Source:** Superior Grocers OneGuide (Google Doc `19g80rubvdkX1IAyi8TPe649_G-VQXmT8zMwIYQ3QVCc`), updated Jun 12, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Standard |
| Availability | All platforms |
| Slack channels | `#superiorgrocers` |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup + FQC); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Wednesday. **Cadence:** Available Wed→Wed, Valid Tue→Tue (times set to **1:00 AM**).
- Linking document: **Yes — Tag/QC specific.**

## Upload & setup (owned by Vendor)

**Build the codesheet from the "Version List" Excel file:**
- Create a new tab (this becomes the generic codesheet). Headers: A1 `Zones`, B1 `Stores`, C1 `Page 1`, D1 `Page 2`, … one column per flyer page.
- From the main tab, copy each version's Version Code → Zones, Store # → Stores, and each Page column into the matching Page columns of the new tab.
- Append **".pdf"** to each page name to match the FTP file names (use `=CONCATENATE(pagecells,".pdf")`, then paste as values and delete the formula helper).
- Save as CSV and upload in Fadmin. Ignore the PDF Base Directory (changes weekly — taken from the FTP).

**Setup / dates:**
- Available From & Valid From times = **1:00 AM**. Verify dates (comes up Wednesday, down the following Tuesday) via Overview → Edit Details; **all toggles off** (hidden nowhere).
- Setup QC: verify dates on page 1, verify each page and correct pagination (1, 2, 3, 4…).

## ⚠️ Common errors / risk items (retailer-specific)

- **Section-level valid dates are often missed:** the "SATURDAY & SUNDAY Specials!" section on Page 1 (~8 items) must have correct **Item Valid From/To** dates and the **Sale Story** applied. Save after each item.
- **Section-level sale stories** (e.g. Weekend Specials) are often missed.
- **Prefix/Postfix errors:** e.g. Coffeemate Creamer → current price $4.99, postfix "EA WHEN YOU BUY 2"; ensure the number following "WHEN YOU BUY" is correct. Postfix tagging must include the text following the price **AND** the text in the black box.
- **Specified-day sale stories** ("Thursday only", "Wednesday only", Red Tag specials) advertised at the top of a page apply **only to items up until the next header**. Items below the next header follow the overall flyer valid dates unless otherwise specified.
- **VOID coupons:** do **not** box or tag any coupon marked VOID (should not be interactive).
- **Images:** black-background images → check "Do not Use PDF images"; do not use images that correlate to other products. Meat/seafood/pop-up products often need cutouts.
- **No overlapping boxes**; box each price individually; don't miss small items (e.g. ice cubes); ensure item pops don't include images from other items.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include packaged deals, retailer logo. Exclude coupons, sign-up page, social media, special weblinks. Box all priced items (text boxes where needed), no overlaps.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; brand per box specifics. **Exclude SKU (no SKUs) and URLs.** Name/Brand/Description as in flyer. Disclaimer only if within the drawn box (not bottom-of-page). Every item needs a category — if unsure, Grocery.
- **Image QC:** do NOT tag items with a black background; check "Do not Use PDF images" as needed.

## Post-processing / Final QC (owned by Vendor)

- Mark Autostack Spotcheck complete.
- **Sessions tab:** Mark items in-store only (Flyer Level Run Tasks) → "Pgs Marked In-Store 4/4".
- **Pricing Zone tab — Key Messages:** rotate between blank/"Weekly Specials" and "Red Tag Deals" (per stage; final FQC = none).
- **Page tab — Category QC:** no categories on page 1; for the rest, apply categories per the sections on each page (1–2 per page).
- **Item-level dates:** re-check the Page 1 Saturday & Sunday Specials for Item Valid From/To + Sale Story; save each.
- **Coupons:** confirm no VOID coupons are boxed.
- **Dates:** Available Wed 1:00am → Tues 11:59pm; Valid Wed 1:00am → Tues 11:59pm. Available everywhere, no theme.
- **Legibility heights 35/25**; thumbnails Standard 4 (Thumbnail_1065_600 & storefront_carousel_premium = first 2 pages; stock_prem & storefront_carousel_organic = first page).
- **Geography:** no changes week over week; 1–3 FSAs added/removed can be ignored.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- Black Friday / seasonal comms are tracked in the linked Flipp Operations Guidelines docs.

---
*Source: Superior Grocers OneGuide (Google Doc `19g80rubvdkX1IAyi8TPe649_G-VQXmT8zMwIYQ3QVCc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
