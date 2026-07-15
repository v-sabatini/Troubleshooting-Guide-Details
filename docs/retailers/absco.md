# ABSCo (Albertsons Banners) — Processing Guide

> **Source:** ABSCo OneGuide (Google Doc `183GtNwUcM9JLHJpxIRREZrJXAirNAP8ctKJ5I8aFeS8`), updated Oct 14, 2025.
> **Tier 1 Premium multi-banner account.** Contacts/credentials omitted.

Covers all Albertsons-owned banners: Safeway, Albertsons, Vons, Tom Thumb, Randalls, Star Market, Shaw's, Jewel-Osco, Carrs, Kings Food Markets, Balducci's, Acme Markets, Andronico's.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium · relationship quality "Good" |
| Availability | All platforms |
| Slack channels | `#albertsons`, `#albertsons-ops`, `#3fl-absco`, `#albertsons-dataservices` |
| Hosted URLs | Per-banner `/weeklyad` pages (safeway.com, albertsons.com, vons.com, tomthumb.com, randalls.com, starmarket.com, shaws.com, jewelosco.com, carrsqc.com, kingsfoodmarkets.com, balduccis.com, acmemarkets.com, andronicos.com) |
| Flyer types | Weekly Circular ("WC") · GMI (Health, Home & Beauty) · Special Ads (SP) · Big Book of Savings (BBS) · Entertainment/Holiday/Catering Guides & Menus (EG/HG) |
| Processing | Auto-stack; **3FL (Flex) + Flyer Review**; OS does Setup + coupon processing; Strategic Ops / Feedel data services = **Yes** |

## Files & schedule

- **Files received:** Tuesday, sometimes Wednesday.
- **Main Weekly Circular cadence:** Available From Tues (or Thurs), Valid From Wed (or Fri), Valid To following Tues (or Thurs) — confirm against the PDFs.
- **Preview date:** Thursday or Friday depending on merchant/internal run name (see internal chart). Ad-hoc/specialty publications get no consumer preview and follow no predictable cadence.
- **Linking document:** Yes — 2 attachments (URL sheet + Promo/Offer ID sheet) required for pipeline tasks unless a task note says otherwise.
- Weekly tracker tab created per week; flyer run IDs assigned by Scrummaster (Flex).

## Upload & setup

- Follow the **ABSCo: Upload SOP** (linked in the OneGuide) for all Weekly and GMI uploads.
- Some banners require **2 codesheets** — check the Merchant/Division Breakdown asset chart to confirm (e.g. Safeway – Seattle).
- **Upload Step 9 — remove page(s):** for specific merchant/flyer-type combos you must **remove the digital-insert pages with the wrong branding** from the run. A flyer showing a "Safeway" page next to an "Albertsons" page means this step was missed. Follow the removal chart in the Upload SOP (do NOT remove everything with "DIG" in the name — only the pages listed).

### ⚠️ Common errors / risk items (retailer-specific)

- **Digital coupons vs items — high impact.** Points multipliers ("2X POINTS", "3X REWARD POINTS") are **ITEMS, not coupons**. A "Digital"/"forU" coupon says "forU", "points forU", "with digital offer/coupon", or "DIGITAL ONLY" → Display Type = Coupon, Just For U (No Barcode) = Y, Coupon URL = banner-specific URL. Items get all three left blank.
- **Buy X Get X sale stories** are error-prone and extremely high impact — transcribe the numbers exactly as printed.
- **External run names are division- & flyer-type-specific:** default/WC = "Weekly Ad"; GMI = "Health, Home & Beauty" (**except Star Market & Shaw's** = "Additional Savings"); BBS = "Big Book of Savings"; SP = "Specialty Publication" (**except Eastern (EAS), Acme (ACM), Intermountain (IM), Denver (DEN)** = "Bonus Online Savings"); ORG = "Organics Guide".
- **Thumbnails:** Storefront Carousel Organic must include **page 1 only** (no adjacent/skinny-flap pages). Safeway NorCal versions **N5O & N5OI** need thumbnails drawn separately — pagination is unique and needs different dimensions.
- **URL attachment items** (anything pictured in the URL doc) must be Display Type **LINK** with the provided URL — never a Coupon or Item (e.g. Gas Rewards box). Match the **Page** column to the exact PDF name; URLs can differ per page even for the same image.
- **Ad-hoc / Guide identification:** specialty publications and Guides (from retailer email language: "Entertaining Guides", "Holiday Guides", "Catering Menus") arrive in the Tuesday drop or separately. Processor must create shells, add them to VAST and the 3FL tracker on receipt, and flag in `#albertsons-ops`.
- **Multiple codesheets** — see risk above.

## QC specifics

- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** linking doc required (URL sheet). Include coupons, packaged deals, sign-up page ("Fresh Pass" last page = box whole page as one item), special weblinks (per URL sheet). Exclude retailer logo and social media. Box **every item with a unique price/sale story** (even with no image, and even overlapping items) separately. SoCal Vons weekly Catalina flyer: box overlapping products separately even at the same price.
- **Tag / Tag QC (High; Auto-tag ON, PDF image auto-select ON):** linking doc required. Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs (via URL attachment for LINK types). **Exclude SKU.** Brand is box-draw specific.
  - Name = bold text; brand only if in item copy (don't pull from packaging); overflow names continue in Description. "Select Varieties" goes in Name unless at the end. Description = unbolded text; "Mix or Match" callouts go in Description.
  - **Analytics category chart:** Gift Cards, Gas Rewards, Miscellaneous (Seniors' Discount, Military Days, non-category contests), Baby Care, Beverages, Bread & Bakery, Breakfast & Cereal, Canned Goods & Soups, Condiments/Spice & Bake, Cookies/Snacks & Candy, Dairy/Eggs & Cheese, Deli, Flowers, Frozen Foods, Fruits & Vegetables, Grains/Pasta & Sides, International Cuisine, Meat & Seafood, Paper/Cleaning & Home, Personal Care & Health, Pet Care, Wine/Beer & Spirits. Multi-item blocks → category of the first item in the Name.
  - **Offer ID (Custom Field 3):** tag from the Promo ID document using BANNER_NM + HEADLINE columns. Headline won't be exact — a single matching product = a match; then tag the **entire** Promo ID row (all IDs, pipe-separated) even if only one product matches. Up to 3 keyword attempts, else leave blank. **Vons SoCal weekly uses a separate updated Promo ID process** (see the Vons SoCal doc).
- **Image QC:** confirm auto-selected image. Prefer clean PDF (lifestyle/plated preferred over cutouts). BOGO → image of the product you must buy. Multi-item → clean PDF of the FIRST listed item, else next.

## FQC / out-of-processing

- **FQC (Vendor):** multi-step — Item Tagging QC (digital coupon, barcoded coupon, item-level valid dates, gas rewards, missing box), Digital Insert checks (Weekly only), Item Search QC, URL QC (if URL doc attached), Overview checks (external run name, thumbnails), Pricing Zone check, Geography tab, Storefront spotchecks (Safeway/Albertsons Seattle, Carrs). Tagging QC runs on all pages of the **largest pricing zone** + 100% of page 1s.
- **Flyer Review type: Simple** (Full Processing, owned by Flex).
- **Out of processing:** "Tag OIDs" and "PID QA" required for any flyer with a Promo/Offer ID document; track completion in the master tracker.

---
*Source: ABSCo OneGuide (Google Doc `183GtNwUcM9JLHJpxIRREZrJXAirNAP8ctKJ5I8aFeS8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
