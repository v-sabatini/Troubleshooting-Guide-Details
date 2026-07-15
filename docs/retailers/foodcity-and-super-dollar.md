# FoodCity & Super Dollar — Processing Guide

> **Source:** FoodCity & Super Dollar OneGuide (Google Doc `1jGiJ9ff-rQoK6d_QlubD_Kc_QEjD_oBptePL8eHjYiw`), updated Mar 11, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#foodcity` |
| Hosted URL | N/A |
| Flyer types | Weekly (2958) — two banners: **FoodCity** and **Super Dollar** |
| Processing | Auto-stack; Flex (Processing Support); no coupons, no Feedel |

## Files & schedule
- **When files arrive:** Tuesday.
- **Publication cadence (FoodCity):** Available From Tuesday, Valid From Wednesday, Available To Tuesday, Valid To Tuesday.
- **Publication cadence (Super Dollar):** Available From Wednesday, Valid From Wednesday, Available/Valid To Tuesday.
- **Linking document:** Tag/QC specific (used for URLs, mostly banners). **Processing type:** Auto-stack.
- Files come from the external ops contact; inserts and page-swap info are sent separately and posted to the PS Slack channel.

## Upload & setup — FoodCity (owned by Vendor)
1. Download `FCxx.xx.xxManifest.xlsx` from the Fadmin FTP (for the correct week).
2. Manipulate the manifest (open in Google Sheets, unhide all rows, **delete all rows for Stores 987 and 425**).
3. Check the latest FoodCity Slack post — confirm it's for the same flyer run (flyer is linked in the post).
4. In the manifest, **replace any pages mentioned in the post** (e.g. replace all `P09_G206` with `P07_G206`). If the replacement page (e.g. `P10_FC`) is already present, delete the row with the old page (`P12_FC`).
5. Download as CSV.
6. **Upload codesheet:** Name = flyer run name; **Config name = `food_city`**; PDF Base Directory from the SFTP.
7. Check FTP/comments/Slack for **inserts and positioning**; upload inserts manually from the Pages tab. Mark flyer creation complete; add inserts to pricing zones per instructions (e.g. "place after page 6 position 10").
   - Add inserts to all pricing zones at once via **Pages → Layout → find insert → put in → add position → select pricing zones → OK → Submit**.
8. Stores are added to each pricing zone **automatically when the codesheet runs**. Double-check pages & ordering.

### Setup QC — FoodCity
- Edit details: Avail from Tuesday, Avail to Tuesday, Valid From Wednesday, Valid to Tuesday. **NO external run name. No theme.**
- Standard 4 thumbnails.
- **Geography may show stores added/removed — this can be ignored during Setup QC.**
- Complete Setup QC checklist.

## Upload & setup — Super Dollar (owned by Vendor)
1. Download `SD_xx_xx_xx_Weekly.xlsx` from the Fadmin FTP (correct week); open in Google Sheets, download as CSV.
2. **Upload codesheet:** Name = flyer run name; **Config name = `food_city`**; PDF Base Directory from SFTP.
3. Mark flyer creation complete. Stores added automatically when codesheet runs. Double-check pages & ordering.

### Setup QC — Super Dollar
- Edit details: Avail from Wednesday, Avail to Tuesday, Valid From Wednesday, Valid to Tuesday. **NO external run name. No theme.**
- Standard 4 thumbnails. Geography same WoW. Complete Setup QC checklist.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include everything:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box every item with a price as shown; use textboxes to capture all info. **Box every coupon with a barcode.**
- **Social media links** (box & link):
  - foodcity.com → name "Food City"
  - facebook.com/FoodCity → "Facebook"
  - instagram.com/foodcitygrocery → "Instagram"
  - twitter.com/foodcity → "Twitter"

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF image auto-selection ON; linking doc required)
- Brand is Box Draw/Box QC specific.
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Tag BRAND if noticeable in name or image; NAME always as shown in flyer.
- **Price:** "+CRV" can go in price or description; "Per Lb." can go in postfix or description (both correct).
- **URLs:** tag based on the linking document — often only for banners at top/bottom, rarely food/wine items.
- **Categories:** tag both "Categories" AND "Category Highlights" fields. Be mindful of meat and deli. Every item should have a category.
- **Item-level dates:** check for pages with 2–3 day sales — all items on that page need item-level valid from/to.
- **Images:** select a PDF image for every tagged item (cleanest, most relevant).
- **Category chart** (Flipp Category → examples): Toys, Seasonal, Pharmacy, Pets, Outdoor Living, Home Essentials, Health & Beauty, Grocery, Grills, Gifts, Coupon (a page of many coupons), Beverages, Beer/Wine & Liquor.

### Image QC
- Select PDF images if clean (not cut off, no black edges); otherwise use item cutout.

### Spotchecks
- Standard spotchecks in pipeline; reference Tag/Tag QC instructions.

## Post-processing / FQC

### FoodCity FQC (owned by Flex)
- Mark auto-stack off; Ops spot checks; Item Image QC (PDF if clean, else cutout).
- Thumbnails standard 4 (Thumbnail 1065, Stock Premium, Carousel Premium, Carousel Organic).
- Mark items in-store only. Check pages for special sales (add item valid dates if applicable) and items over $100 (double-check prices).
- Edit details: Avail Tue–Tue, Valid Wed–Tue, NO external run name, no theme.
- **Ensure codesheet ran Green.** Search latest FoodCity Slack post (same week) and **add links from it to the inserts** from the tagging interface.
- Geography changes can be ignored if codesheet ran green.
- **FQC errors to ignore:** "not all categories being used in pricing zones have thumbnails"; "Store ___ is not assigned to any flyer".

### Super Dollar FQC (owned by Vendor)
- Same steps as FoodCity, except: Edit details Avail Wed–Tue, Valid Wed–Tue; **Geography: no stores/FSAs added.** Same FQC errors to ignore.

## Flyer Review (owned by Vendor)
- **Flyer Review type: Lite.**

## Out-of-processing
- 2025 BF Comms: FoodCity/Super Dollar Flipp Operations Guidelines (Publication & Ad-Hoc Requests 2025).

---
*Source: FoodCity & Super Dollar OneGuide (Google Doc `1jGiJ9ff-rQoK6d_QlubD_Kc_QEjD_oBptePL8eHjYiw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
