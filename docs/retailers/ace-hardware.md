# Ace Hardware — Processing Guide

> **Source:** Ace Hardware OneGuide (Google Doc `1CQYeYI-…zgwBo`), updated Sep 9, 2024.
> **High box-draw complexity.** 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#acehardware`, `#flex-processingsupport` |
| Hosted URL | acehardware.com |
| Flyer types | **Local Ads** (ad-hoc, incl. RMAs — several/month) · **Corporate Ad** (incl. EVNs/MLs — 1–3/month) |
| Processing | Auto-stack; Flex (Processing Support); no coupons/Feedel |

## ⚠️ #1 Risk item — price tagging
**The smaller price (the price *before* discount, in the black box) always goes in the Current Price field. The discounted (Ace Rewards) price goes in the Sales Story.** Do **not** put the Ace Rewards price in Current Price.

## Local Ad setup (owned by Vendor)
- "Group Submissions" = ad-hoc publications to certain stores (good lead time). Create a shell in the **Local Ad** flyer type.
- Valid/Available dates from the Group Submission form (sometimes Available before Valid). **Set Valid/Available From times to 3:00 AM EST**; internal run name = Group Name, external run name/key messages = Event Name.
- **Manual upload** of pages/pricing zones; name PZs by the versions in the participation form. Store assignment: build a **generic store codesheet** (store number + version) from the participation excel.

### Local Ad setup QC
- Valid/Available From = **3:00 AM**; Available To = **2:59 AM** next day (not Valid To). Add external run name; check **theme** (Ace often falls into the theming carousel).
- **Item View: check no pages are cut off** — Group ads are notorious for cut-off pages, and **OS flags this and stops processing.**

## Corporate Ad setup (owned by Vendor)
- **Gallery codesheet:** delete the entire bottom (2nd) chart, save as CSV. Upload — Config **`ace_hardware`**, base path per the codesheet, **uncheck store assignment, region assignment, combine zones**, Save & Process. Then mark all "Complete Books" as uploaded in the FTP.
- **Store set assignment (monthly):** generic stores codesheet from the OPP + "My Store" docs — Config **`generic_stores`**, FTP path `/`, **uncheck all but store assignment**.
  - The codesheet **will show a "missing stores" warning — this is normal.** Resolve via the MyStores list: if a store isn't there, it's not participating/closed → delete the row; if it's in MyStores but not the OPP, add the store to FADMIN. Re-upload and click "Try Again."
  - Finalized codesheet order: **pricing-zone tab (B&W) first, Gallery tab (colourful) second**; omit the "Market" column; check for blank "Region" cells.

## Box Draw (HIGH complexity — Auto-Box OFF, Box QC bot OFF)
- **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box **every individual item** with its price/SKU/name. **No category on page 1** (logo page). Text boxes when item and text aren't side-by-side. Page categories if **3+ items** on a page share a category. Different SKUs → boxed separately.
- Box the **"FREE STORE PICKUP" banner** as a direct link; box the **logo** → link to acehardware.com.

## Tag / Tag QC (Low; Auto-tag OFF)
- Include: brand, pre/postfix, valid dates, price, sale story, categories, disclaimer. **Exclude description & SKU.** Name, original price, URLs are **risk items**.
- **Prefix** usually "SALE"; **Current Price = the price before the Ace Rewards card** (the black box); the discount goes in **Sale Story** (include the "-"). Postfix e.g. "each"/"gallon."
- **Valid dates:** check above the item image on every page except page 1 (coupons: date after "through" = Item Valid To).
- **URLs only if item name *and* SKU match acehardware.com** — otherwise enter no URL. Social-media links named per the guide.

## Image QC
- Prefer the PDF image; Ace uses lots of lifestyle shots, so clean PDFs are often unavailable → **cutouts are fine** in that case.

## FQC
- **Local Ad:** add/remove stores as directed; mark items **In-Store Only**; categories ≤1 per page; **upside-down pages are OK for local ads**; stores always differ in the Geography tab (don't flag); thumbnails Standard 4; times 3 AM; external run name set.
- **Corporate Ad:** dates 3 AM; **hidden in distribution**; **no image QC**; thumbnails Standard 4; categories one per page (none on page 1); mark In-Store Only; ensure social icons linked.
- **Flyer Review type: Lite.**

---
*Source: Ace Hardware OneGuide (Google Doc `1CQYeYI-c2O2ueoNSrrxZ9Z4yp_qJ8T0PRXSM0RzgwBo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
