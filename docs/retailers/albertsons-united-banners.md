# Albertsons United Banners — Processing Guide

> **Source:** United Banners OneGuide (Google Doc `1jlNzR4o76j3MIw4L8p3KNL8Fk0no7shOM3RqT_PWmm8`), updated Apr 8, 2026.
> Covers 4 merchants: **Albertsons Market (2759), Amigos United (2754), Market Street (2755), United Supermarkets (2756)**. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium (Core+) |
| Availability | All platforms |
| Slack channels | `#united-banners`, `#flex-processingsupport` |
| Hosted URLs | coupons.albertsons.com/weeklyad · amigosunited.com/rs/WeeklyAd · marketstreetunited.com/rs/WeeklyAd · unitedsupermarkets.com/rs/WeeklyAd |
| Flyer types | Weekly Flyer (+ standalone monthly) |
| Processing | Auto-stack; **Flex = Processing Support**; **OS completes coupon processing**; no Feedel/data services |

> **Account note:** Store 571 (in the WTX codesheet) is a pharmacy location tied to United Supermarkets store 573 — it does not exist in the merchant and gets no flyer.

## Files & schedule

- **Files received:** Friday.
- **Cadence:** Available From/To Tuesday; Valid From Wednesday, Valid To Tuesday.
- **Preview date:** Friday (1-day early preview before valid).
- **Linking document:** Version List + Promo ID attachments (see setup).

## Upload & setup (owned by Vendor)

- **Codesheet upload for all banners.** Two codesheet families: **WTX** = Albertsons Market, Market Street & United Supermarkets; **AMG** = Amigos United only. Validate you have the right files using valid date + division (AMG) + flyer type.
- **Codesheet manipulations:** add a new column A `circular_name` (value = valid-from date `MMDDYYYY` + `_AMG` or `_WTX`); move Market to column B; paste the header row (`circular_name`, `market_code`, `page_filename`, `included_stores`, `date_modified`, `Special Notes`); in `included_stores` (col D) find/replace dashes `-` with semicolons `;`; in `page_filename` (col C) find/replace `.pdf` with blank.
- **Upload:** Name = codesheet; upload the manipulated `.csv`; PDF Base Directory = the files path (e.g. `/United_02_07_FromRRD`); **Config name: `united_texas_banners`**; **check every box except the 2nd one.**
- **Attach Promo ID + Version List docs to Vendor tasks** — do NOT attach the Offer ID document ("OfferIds" folder) at this stage.

### ⚠️ Common errors / risk items (retailer-specific)

- **Codesheet yellow warning is OK** — press **[Force Processing]** so the codesheet runs. (In FQC: ignore "Page(s) have already been uploaded"; flag any other warning to Ops.)
- **Promo ID file dating:** the date on a Promo ID file = the date it was provided to us (not the flyer's valid date). Always use the file **"Created At" the Tuesday** of the upload week.
- **Digital Deal coupons:** an offer marked "Digital Deal"/"DIGITAL ONLY" with no barcode → Display Type = **Coupon**, Just For U (No Barcode) = **Y**, Digital Coupon URL = banner-specific loyalty URL (Market Street shopmarketstreet.com, Amigos shopamigos.com, United shopunitedsupermarkets.com, Albertsons Market shopalbertsonsmarket.com — all `/loyalty/coupons-deals?event=Weekly%20Ad%20Coupons`). Points multipliers ("#x rewards! points") are **Items**, not coupons.
- **Storefront Carousel Organic thumbnail must include page 1 ONLY** (no adjacent/skinny-flap pages).
- **URL inserts/callouts:** find the URL in the Version List "special notes" column next to the page. **If a unique URL is needed per pricing zone, process but flag to the DOC.**
- **Geography:** must read "No Stores or FSAs/zips were added or removed" — flag any change to Ops (via `#flex-processingsupport`).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** no linking doc. **Include** coupons, packaged deals. **Exclude** retailer logo, sign-up page, social media, special weblinks. Box items with a Name & savings offer (price or sale story), banners with a savings offer, "Dollar Days" pages (all items under one price point as one offer — but a separate-price coupon boxed separately), and "download our new app" banners/inserts.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-select ON):** Tag-specific linking doc + tagging attachment required. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Custom fields (RISK): Just For U (No Barcode) + Digital Coupon URL for digital coupons; **Offer ID** from the "EMJU" spreadsheet.
  - **Dollar Days multi-item:** no brand; include all products/descriptions in PDF order (overflow to description); Current Price = the number, Postfix = "DEALS"; category of first item; Google Category "Food Items"; image of first item named.
  - **Offer ID:** match on BANNER_NM + HEADLINE (banner names: UNITED, ALBERTSONS MARKET, MARKET STREET UTD, AMIGOS). Headline won't be exact — one matching product = a match; then tag the **entire** PROMOTION_ID row (all IDs). If no close match, leave blank.
- **Image QC:** clean PDF preferred → lifestyle/plated → cutout. Dollar Days multi-item: clean PDF of first named product, else next, else cutout.

## FQC / out-of-processing (Vendor-owned FQC)

- QC runs on all pages of the **largest** pricing zone + 100% of page 1s. Steps: Digital Coupon QC, Barcoded Coupon QC (Coupon display type, Coupon + product category, Just For U blank, URL blank), item valid dates, missing boxed shoppable callouts, "Download our New App" insert QC (URL from Version List).
- **FQC checklist:** confirm PDF dates match Valid From/To (flag Ops if not), available on all platforms, 1-day early preview, External Run Name = "Weekly Ad", No Theme, thumbnails (no cutoff; Storefront Carousel Organic = page 1 only), codesheet ran green, geography unchanged.
- **Out of processing:** "Tag OIDs" and "PID QA" required for any flyer with a Promo/Offer ID document.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Albertsons United Banners OneGuide (Google Doc `1jlNzR4o76j3MIw4L8p3KNL8Fk0no7shOM3RqT_PWmm8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
