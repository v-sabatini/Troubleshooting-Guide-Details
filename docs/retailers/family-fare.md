# Family Fare — Processing Guide

> **Source:** Family Fare OneGuide (Google Doc `1xdqDuSnai1CeuJigXGTvUnuRZ3l_VsMHppW2-Zx_ZjA`). Contacts/credentials omitted.

> SpartanNash banner.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#rspartannash`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer types | **Weekly Ad – West** · **Weekly Ad – Michigan** |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); DOC (Setup + FQC); OS N/A; no coupons; no Feedel/retailer data services |

## Files & schedule

- **Files received:** Monday, dropped to FTP (email sent when files drop for all SpartanNash banners).
- **Cadence:** Available From Saturday, Valid From Saturday; Available To Sunday, Valid To Saturday. Preview date Saturday.

## Upload & setup (owned by DOC)

- In the FTP, search `.xlsx` for "Posting"/"Posting Plan" documents (used to build pricing zones).
  - **West flyer:** download the **6 Posting Plans** — Wisconsin, Rapid City, Outlier, Omaha, Minnesota, Fargo (path `/Family Fare West`).
  - **Michigan flyer:** download the **1–2 Posting Plans** labeled Michigan (path `/Family Fare Michigan`).
- **⚠️ Risk:** ensure you download the posting plans for the flyer you're on — the base path includes the flyer's Valid From date (e.g. `04-14-24`).
- Open the posting plans and the codesheet generator; use the matching sheet (West/Michigan). Zones/stores stay consistent week over week — update the page columns with page names from the posting plans (zone number is in the posting plan). Some zones share pages except a few (highlighted in the posting plan).
- Download the sheet as CSV → flyer run → Codesheet upload. **PDF base directory: `/Family Fare West` (West) or `/Family Fare Michigan` (Michigan).** Save & Run.
  - **⚠️ Typical error:** pages already uploaded / multiple matching FTP files → usually force-process.

### Setup QC (DOC)
- Mark Flyer Creation complete. Edit Details: Available From Saturday, Available To (following) Saturday, Valid Sunday–Saturday; internal run name `Month Day - [West/Michigan]`; available everywhere; no external run name; no theme. Standard 4 thumbnails.
- **⚠️ IMPORTANT: mark FTP files (including Posting Documents) as uploaded.**

## ⚠️ Risk item — coupons
- **All coupons require the word "Coupon" in the name.**

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc)
- **Include** coupons, sign-up page, social media, special weblinks. **Exclude** packaged deals, retailer logo.
- **"Available on Flipp" banner** → box and link to `https://app.flipp.com/?utm_source=flipp&utm_medium=flyer&utm_campaign=familyfare`, name it **"Flipp".**
- When a sales story covers multiple items in one block, box each separately (use text boxes). Two prices in a block → box separately.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection OFF)
- Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for both box/tag.
- **Name** should include all items in the ad block. **Description** as it appears.
- **Sale Story:** special-banner items get the banner in the Sale Story (e.g. Price Freeze → "Price Freeze").
- **URLs — Yes Club Ads:** green banners are boxed/tagged as **Link** type; name/URL are the same each week — e.g. "Yes Reward Savings" → `shopfamilyfare.com/yes-card`; "Family Fare Loyalty Clubs" / "Yes Savings" → `shopfamilyfare.com/account/clubs`. Box/tag coupons separately.
- **⚠️ Valid dates:** apply item-level dates only when the top banner states the sale days (e.g. 3-Day Sale, Seafood Sale, 1 Day Sale, Mix & Match). **Price Freeze pages** — ALL items need a Valid To date (found top/bottom/side; pages generally yellow/blue/white) even when the page isn't explicitly titled "Price Freeze".
- **Coupons/Digital coupons:** Display Type = **Coupon**, include expiry dates + disclaimer (box has expiry date, barcode, usually says "coupon"). Digital download coupons: Valid To/From = download date; "Must redeem by" date in the disclaimer.

### Spotchecks
- Standard pricing spotchecks in the pipeline.

## Post-processing

### Item Category QC
- **Every item requires a category.** Baby → Health & Beauty; Pet → Grocery. Full department→example chart in the OneGuide (Bakery, Beverages, Dairy, Deli, Floral, Frozen, Grocery, Health & Beauty, Holidays, Home Essentials, Meat, Price Freeze, Produce, Seafood, Snacks, Beer/Wine/Liquor, Back to School).

### Item Image QC
- No image QC preferences given by the client — not required.

## FQC (owned by DOC)
- Complete leftover spotchecks; check narrow pages in Storefront Spotcheck per PZ and merge to next page; mark Autostack Spotcheck complete.
- Page categories: no category on page 1; use page headers for others (can copy page index).
- QC thumbnails **Standard 4** (1065×600 = 2 pages; stock premium = 1; carousel premium = 2; carousel organic = 1).
- **⚠️ Review each PZ at item level for unique valid dates** (e.g. 3-Day Sales); apply correct dates on those pages.
- Edit Details: available everywhere; valid dates match the flyer; 1-day consumer preview; no theme; no external run name.

## Flyer Review
- **Type: Lite.**

---
*Source: Family Fare OneGuide (Google Doc `1xdqDuSnai1CeuJigXGTvUnuRZ3l_VsMHppW2-Zx_ZjA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
