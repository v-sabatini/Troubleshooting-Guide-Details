# Retailer Processing Guides — A

> Bundle of 28 retailer-specific processing guides (A). Contacts and credentials are omitted from every guide.

**Contains:** ABSCo (Albertsons Banners), Academy Sports + Outdoors, Accès Pharma, Ace Hardware Canada, Ace Hardware, Acme Fresh Market, AG Foods, Al Arsh Halal Meat, Alaska Commercial, Albertsons United Banners, ALDI, Alf Curtis, Amazon Fresh, Ambrosia Natural Foods, ANBL (New Brunswick Liquor Corporation), Andres Electronics, Andy's Quality Market, Animo Etc, Ares Cuisine, Ashley Furniture Homestore, Ashley Homestore Atlantic, Asian Food Centre - Wanless, Atlantic Superstore (RASS), Atlas Tool & Machinery, Atmosphere Quebec & Sports Experts, Atwoods Ranch & Home, Avril Supermarché Santé, Axep / Intermarché / Intermarché International


---

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

---

# Academy Sports + Outdoors — Processing Guide

> **Source:** Academy Sports + Outdoors OneGuide (Google Doc `1azkr8dL…nymsA`).
> 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel | `#academysports` |
| Cadence | **Ad-hoc** — a schedule is provided but **very often changed at the last minute** |
| Processing | Auto-Stack; **Flex not involved**; OS does standard tasks |

> **Note:** shells are made ahead of time, but **follow the PDF dates over the shell dates.**

## Upload
1. Files arrive by email; a linking doc (URL/SKU list) is requested from the retailer.
2. Codesheet dropped in **PDF, XLSX, and CSV** in the SFTP — mark off PDF/XLSX, **download the CSV**.
   - Open and check for issues/disclaimers; **delete any disclaimers in the top 3 rows**.
   - If a **Store Tile column** is in Column B, delete it.
   - Pages sometimes out of order (e.g. "PAGE 2" is `page_10`) — **reorder**.
3. Upload codesheet — **Config: `academy_sports`**; **every toggle checked *except* Region Assignment and Combine Zones.**

## Setup QC
- Confirm all pages picked up (FTP open). Attach the linking document to box, box QC, tag, tag QC, and PQC. Set preview date; external run name from the folder (e.g. "Hunting Ad," "Active Ad").

## Box Draw / Tag (Low complexity)
- **Box Draw:** include social media, sign-up page, special weblinks, retailer logo, packaged deals; **exclude coupons**. **All "SHOP NOW"/"SHOP ALL"/"SHOP ___" call-outs boxed separately** (and tagged as **links** with the same URL as the connected product). Bottom banners boxed & tagged. Boots often have **2 prices on one image = 2 items**; a grouping of shoes with **1 price = 1 item**.
- **Tag:** include all fields (brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs). SKU & URL provided in an attached spreadsheet; if not found, search academy.com.
- **Image selection:** single item in image → clean **PDF**; multiple items in image → **leave as Item Cutout** (do not select PDF).

## Pre-final / out-of-process
- Download **custom tiles** from FTP. Thumbnails: **Standard 4 + custom tile** (override 2nd & 3rd) **and** draw the tile labeled "thumbnail" (shows on their website).
- Action any page swaps / custom-tile swaps from email. Check "Shop Now" boxed separately as direct links; **re-run tile gen on a different script if strange text artifacts appear.**
- Image QC (uncheck data piped); Wayfinding QC; Spotcheck QC; page categories; mark items **In-Store Only**.
- **Tracking codes** (Hosted + Distribution): reference a previous flyer — UTM campaign changes by date, `utm_term` is always `__SKU__`; add **OGMAP** codes; click **Apply All Tracking Codes**.
- FQC, then send a **preview email** (ad dates, custom tile, items without URL, flyer sorting — Active then Hunt, newest at top; separate email per flyer).
- **Flyer Review type: Lite.**

---
*Source: Academy Sports + Outdoors OneGuide (Google Doc `1azkr8dL_5TnYMhHKYbLZyBNlwVk1jGbhpQfUCRnymsA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Accès Pharma — Processing Guide

> **Source:** Accès Pharma OneGuide (Google Doc `1HB7P2oB…4RzYY`). **Walmart-brand
> merchant.** Bilingual (EN/FR). 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | TBD (Walmart-brand merchant) |
| Availability | All platforms |
| Slack channels | `#acces_pharma-onboarding`, `#flex-processingsupport` |
| Hosted URL | n/a (hidden on hosted) |
| Flyer type / cadence | 10945 — **Monthly**; files received **Friday**; available **Thursday**, valid **Wednesday** |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Upload & setup (owned by Flex)
- **Client sends the PDF by email** (they've been asked to use SFTP but don't). Upload the PDF to the SFTP so FADMIN breaks it into pages — **or** split via pdf2go, then upload from your local drive.
- Pages → Edit → upload all pages **twice**; **set one of each page number to English and the other to French**; Autogroup; Save & Complete.
- **Flyer creation (bilingual):** one pricing zone "**ENG**" with all English pages (correct order); one pricing zone "**FR**" with all French pages (correct order).

## Setup QC
- Add **all stores to both zones**. Open the last page ("Tag") and check the printed dates match the client's email; if not, set the run dates to the PDF and **flag the discrepancy to the DOC**.
- Overview → Edit Details: **hide on hosted**, no external run name, "No Theme." Legibility heights **Scan 60 / Read 40**. Thumbnails: Standard 4.

## QC specifics
- **Box Draw:** Low; Auto-Box **on**, Box QC bot **off**; exclude coupons/packaged deals/logo/sign-up/social/weblinks. Box & tag each item individually; if items share a price but have different names/brands, box separately.
- **Tag / Tag QC:** Low; Auto-tag **off**. Include all fields **except URLs** (excluded).
- **Image QC:** clean PDF where possible; if the PDF image has a black background/defect, use the cutout.

## Final QC (owned by Flex)
- **Geography** green — **no stores or FSAs/zips added or removed.**
- **Sessions** all green **except PDF Image Auto Selection.**
- Pricing Zones: no items missed; all stores added to both zones; **one zone English, one French**; pages ordered correctly.
- Dates correct (check last page of flyer + client email); hide on hosted; no external run name; "No Theme."
- You can **ignore** the "Not all categories that are used in pricing zones have thumbnails" warning.
- **Flyer Review type: Lite.**

---
*Source: Accès Pharma OneGuide (Google Doc `1HB7P2oBL9UczVSClF0F1quqcHP35sMcoVaWiVh4RzYY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ace Hardware Canada — Processing Guide

> **Source:** Peavey Mart, Mainstreet Hardware & Ace Hardware Canada OneGuide (Google Doc `19y-BkwPR479HcTFVZhE3QFSionUCTTC2gqYQ8OTNrAw`), updated May 11, 2024.
> One guide covers three banners (Peavey Industries). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#peaveyindustries` |
| Hosted URLs | flyertown.ca/flyers/peaveymart-peaveymartm1000 · flyertown.ca/flyers/mainstreethardware-flyer · peaveymart.com/flyer |
| Flyer types | Peavey Mart (type 2685, weekly) · Ace Hardware Canada (type 2685, weekly) · Mainstreet Hardware (type 9970) |
| Processing | Auto-stack; **Flex = FAB Tickets**; no OS, no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Monday.
- **Peavey Mart cadence:** Available From Monday, Valid From Friday; Available To Monday, Valid To Tuesday. Valid dates normally Fri–Wed but rotate — **always check the PDFs**.
- Available dates = **four days before** valid dates.
- **Linking document:** No.
- Set internal preview date to the **following Monday**; OS processing takes 1–2 business days — do not skip setting the preview date.

## Upload & setup (owned by Flex)

- **Peavey Mart — codesheet upload:** open the flyer run; confirm the code in the run name matches the FTP files (e.g. 1A/1B/1C). Find the `.csv` codesheet in the FTP, copy its name and its path (use the path affiliated with the codesheet — there are subfolders). Name = "base". **Config name: `generic`. Toggles: 1, 3, 4, 6.** Process.
  - Internal run name convention: `04D_Peavey Mart_2022`. External run name = main callout on page 1. Seasonal theme: no theme. Standard 4 thumbnails.
  - Once OS tagging is complete, an Item Export is sent to Peavey (see post-processing — owned by DOC, Flex does not do this).
- **Ace Hardware Canada — codesheet upload:** create codesheet (name "flyer"), base path, upload local codesheet, **Config name: `generic_language`**, set PDF base directory from Merchant → Details → FTP Path → View Files. **Toggles: 1, 3, 4, 6.** Save, process, check sessions. Update preview date to **four full days after upload**.
- **Mainstreet Hardware — manual upload:** Pages → Edit → select the **MainStreet** folder (case-insensitive) → select all (usually 4 pages). Autogroup, cross-referencing the file name so indexing is correct. Save & complete. Create **one** pricing zone "Base", language English. Pricing zone → Stores/FSAs → add all. External run name = main callout on page 1; no theme; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- **Valid dates rotate weekly** — verify against the PDFs, don't assume Fri–Wed.
- **Available dates must be exactly 4 days before valid dates.**
- **Logo/banner boxing is Peavey-Mart-only.** Do NOT box logos/banners for Mainstreet Hardware. Only box the large logos (front/last page), not the small corner logos on interior pages.
- **Multi-size/dimension items:** box each size separately and ensure the correct text box is associated with the correct item — mis-association breaks tagging.
- Don't put a weekly flyer under a catalog in flyer sorting — the catalog would show before the preview flyer on the hosted experience.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Box every item with a price; use text boxes when item and price can't be boxed together; box items with SKUs even without a price; keep disclaimers inside the box. Box footers (with or without a link), top/mid banners, the "Proudly Serving Rural Communities" banner (last page, whole area), social-media logos (last page, each separately). Single-page banners = one box around the whole page; Gift Card page = box the Peavey logo separately then the rest.
- **Tag / Tag QC (Low; Auto-tag ON, PDF image auto-select ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. Brand is box-draw specific. **URLs = risk item.** Do Image QC for all three banners during the tag process.
- **Image QC:** use PDF image extraction. Prefer a clean PDF image for single items; do not use images with black background, shadow, curvy borders, or lifestyle background. If multiple images in one box, use the **cutout**. If no clean PDF image, use the cutout.

## Post-processing / FQC

- **Item Export (owned by DOC — Flex skips):** export items, trim to 10 columns (item_id, flyer_name, page, display_type, brand, name, description, sku, sale_story, url), split a tab per region, upload to SFTP (credentials in the OneGuide — not stored here), then notify the retailer. Separate export emails exist for Peavey Mart, Mainstreet Hardware (one tab) and Ace Hardware (seven tabs). Note "export sent" + date in the flyer comments. When the export is returned, keep only item_id, sku (delete all skus), and url.
- **FQC (Flex):** set external run name (from Key Message), theme (usually No Theme), thumbnails — Thumbnail 1065×600: 2 pages (logos); Stock premium: 1; Storefront Carousel Premium: 2; Storefront Carousel Organic: 1 (apply to all). Insert/swap pages if needed. Flyer sorting: weekly above catalogs, preview below live.
- **Flyer Review type: Lite.**
- Preview links (DOC-owned) sent per banner.

---
*Source: Ace Hardware Canada OneGuide (Google Doc `19y-BkwPR479HcTFVZhE3QFSionUCTTC2gqYQ8OTNrAw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

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

---

# Acme Fresh Market — Processing Guide

> **Source:** Acme Fresh Market OneGuide (Google Doc `1QL4dQjicbnqam0zqfX0Ez0nc4iAWKeqH1D4x5FChnKs`), updated Nov 27, 2025.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#onboardings`, `#flex-processingsupport`, `#1plat-acmefreshmarkets` |
| Hosted URL | acmestores.com/weeklyspecials |
| Flyer types | Weekly · Secondary Content (one-pagers / promotional) · Specialty Publications · GMI/SAV |
| Processing | Auto-stack; **Flex = Processing Support**; no OS-outside-standard, no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday and Monday.
- **Cadence:** Available From Tuesday **7 AM**, Valid From Wednesday; Available To Thursday 12 AM, Valid To Wednesday.
- **Preview date:** None.
- **Linking document:** Provided by the retailer — attach to OS tasks.

## Upload & setup (owned by Vendor)

- **Change the "Available From" time from 12:00 AM to 7:00 AM.**
- **Manual upload:** upload all pages in the SFTP whose name/folder carries the "Valid From" date.
- Typically **2 regional versions — "Buffy" and "Buck"**. The retailer sometimes adds a **"Medina"** zone (labelled accordingly).
- **Manually create one pricing zone per regional version** and assign each its store set. **If a "Medina" zone is required, add store `22` to it and remove store `22` from the Buffy and Buck zones** so there's no overlap.
- Attach the linking document to vendor tasks if found in the SFTP; if not, flag to the Ops account team.

### ⚠️ Common errors / risk items (retailer-specific)

- Forgetting to change Available From to **7 AM** (default is 12 AM).
- **Store 22 overlap** — if Medina is used, store 22 must be in Medina only (removed from Buffy/Buck).
- **Geography discrepancy:** [Flex Upload team] check the Geography tab against the previous week's distribution; flag any discrepancy to Ops.
- **External name must match exactly** (public-facing): Specialty Publications = "Bonus Online Savings"; GMI/SAV = "Health, Home & Beauty".

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** linking doc required (used for both box & tag). Exclude coupons, packaged deals, retailer logo, sign-up page, social media. **Include special weblinks.** Box items individually; box banners where a link is provided in the linksheet.
- **Tag / Tag QC (Low; Auto-tag OFF):** linking doc required. Exclude brand. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Apply URLs per the linksheet.

## FQC / go-live (owned by DOC)

- Thumbnails, legibility heights, check geography vs. previous week, standard FQC checks.
- **Weekly Ad only — add UTM code at the Flyer Run level:** Manage Tracking Codes → Add Code (Flyer Run section) → Type: **Dynamic Variable**, Code Source: **All**, Variable Name: **`utm_campaign`**, Variable Value: **`mmddyyWeeklyAd`** (updated to the flyer live date each week) → confirm → **Apply All Tracking Codes**.
- **Flyer sorting:** weekly ad displayed first.
- **Flyer Review type: Lite** (owned by DOL).

## One-pagers / promotional flyers (e.g. 3-Day Meat Sale)

- Create a new flyer run in the **Secondary Content** flyer type with the correct date. Most are **Hosted Only** (confirm with Lead if unsure).
- Upload pages into pricing zones (Meat sales: multiple page-1 versions assigned to single stores per version's file name as their own zones; other promos follow the contact's distribution instructions).
- Complete Setup QC → select **"Mark As Vanilla"** (bottom-right of Overview) → notify Lead to review.

---
*Source: Acme Fresh Market OneGuide (Google Doc `1QL4dQjicbnqam0zqfX0Ez0nc4iAWKeqH1D4x5FChnKs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# AG Foods — Processing Guide

> **Source:** AG Foods OneGuide (Google Doc `1KFjKk_4dnLxTdObYRc0MlV9smCu5xj2wH1S4Ln7n0Ug`), updated May 9, 2024.
> Covers AG Foods and Safety Foods (two separate publications). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | (per OneGuide) |
| Hosted URL | agfoods.com |
| Flyer types | Weekly (AG Foods + Safety Foods are two separate pubs) |
| Processing | Auto-stack; **Flex = Flyer Review**; **OS = Setup**; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday (dropped to FTP weekly, usually Friday afternoon per the upload steps).
- **Cadence:** Available From Monday, Valid From Sunday (AG Foods zones are staggered — see below).
- **Linking document:** Yes (Box Draw/Box QC specific).

## Upload & setup

- **Safety Foods = manual upload; AG Foods = codesheet upload** (note: at time of writing, AG Foods codesheet upload was temporarily not working → upload manually per the Breakdown file).
- **Safety Foods manual:** Pages → Edit → Expand Root → Expand Week ## → Select Files. Group pages by the trailing number. One "base" pricing zone: order all pages by number, add all stores.
- **AG Foods:** different **page 1s per pricing zone** (usually 3 — Base, BaseFri, BaseMon) and one set of every other page. Use the **Breakdown** spreadsheet (on the FTP, labelled "Breakdown") which defines pricing zones, stores and valid dates. Create zones per the spreadsheet.
- **Codesheet (AG Foods):** insert the page names from the Breakdown "Files name" column into the codesheet template (into the corresponding pricing zones); adjust Start/End dates to match the Breakdown per zone.

### ⚠️ Common errors / risk items (retailer-specific)

- **Every page in the codesheet must end in `.pdf`** or the codesheet will not detect the pages on the FTP.
- Do **not** remove the leading `'` mark on dates in the codesheet — it can corrupt the codesheet.
- **AG Foods staggered dates:** each zone has its own unique dates; the **run must encompass all dates** — start on the EARLIEST date shown, end on the LATEST (e.g. Base Sun–Sat, BaseMon Mon–Sun, BaseFri Fri–Thu → run Friday through Sunday). If you lack the publication schedule, follow the dates on the page 1s.
- **Safety Foods:** double-check dates against page 1.
- Look for multiple products (box each separately).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks. Each item gets its own box (price + name inside). Text-only items (no image) are boxed separately.
- **Tag / Tag QC (Low; Auto-tag OFF):** linking doc required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific.
- **Image QC:** per examples (details not filled in the OneGuide).

## FQC / go-live (owned by DOC)

- **Triple-check valid & available dates** against the publication schedule; double-check store assignment; use the theme from the ad for the sales story; **legibility heights 45/35**.
- AG Foods dates run from earliest staggered date to latest; Safety Foods dates match page 1. Toggles: Flipp / Distribution / Hosted all Available. All tagging + flyer-level tasks complete.
- **Flyer Review type: Lite** (owned by Flex).
- **Out of processing:** page-swap procedures (see OneGuide video).

---
*Source: AG Foods OneGuide (Google Doc `1KFjKk_4dnLxTdObYRc0MlV9smCu5xj2wH1S4Ln7n0Ug`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Al Arsh Halal Meat — Processing Guide

> **Source:** Al Arsh Halal Meat OneGuide (Google Doc `15Yh5663UU6tehVqGiYYx8fyL7scLVyp9NTOguJ0WBDY`), updated Apr 16, 2026.
> Simple Longtail retailer. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | (none listed) |
| Hosted URL | n/a |
| Flyer types | Flyer (single type) |
| Processing | Auto-stack; **Vendor-owned** (upload → FQC → Flyer Review); no OS, no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Friday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **Preview date / linking document:** None.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu. Folder is named by the flyer's valid date — **always use the lower-case folder, never the Upper-Case folder.** Confirm & Upload → Auto-Group → Save & Complete.
- **Pricing zone:** create one zone called **"Base"**, add all stores, Save & Complete.

### ⚠️ Common errors / risk items (retailer-specific)

- **Use the lower-case SFTP folder** (not the Upper-Case one) for upload.
- After upload, confirm no pages remain in the SFTP except the multi-page PDF (the Upper-Case-named file that does not end in `P####`). Missed pages → flag to the FT team.
- **Geography tab: ensure 0 changes** to Stores or FSAs. Flag 100% of discrepancies to the FT team (continue the checklist — it doesn't block).
- Confirm valid dates match page 1 of the PDF.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** no linking doc. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** no linking doc. Include image (always a clean PDF if available), brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- Spotchecks: standard, included in pipeline.

## FQC / go-live (owned by Vendor)

- **Pre-FQC:** confirm valid dates vs. PDF; platforms available everywhere; thumbnails drawn and include the retailer logo; all items boxed & tagged; previews published and clickable; geography consistent with last week (flag discrepancies to FT Ops immediately — non-blocking).
- Complete FQC checklist.
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Al Arsh Halal Meat OneGuide (Google Doc `15Yh5663UU6tehVqGiYYx8fyL7scLVyp9NTOguJ0WBDY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Alaska Commercial — Processing Guide

> **Source:** North West Company and Banners OneGuide 2.0 (Google Doc `1TF9Y76uIwFGCAel6X5d_RgzhFQPW5ZPnJ9Ah3u064Gw`), updated Nov 27, 2025.
> This article covers the **Alaska Commercial** section; the same doc also covers The North West Company (weekly + general merchandise) and a monthly Astro Hill banner. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#northwestco_banners` |
| Hosted URL | alaskacommercial.com |
| Flyer types | Weekly (type 6437) |
| Processing | Auto-stack; Vendor upload/setup; DOC-owned FQC; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From Wednesday, Valid From Tuesday; Available To Wednesday, Valid To Tuesday.
- **Preview date / linking document:** None for setup (Tag/QC has a Tag-specific linking doc).

## Upload & setup (owned by Vendor)

- **Manual upload:** select files broken into individual pages (names carry `_01`, `_02`, …). Set indexes (page # is in the description name).
- **Create pricing zones** based on page names via Flyer Creation; assign all pages to the corresponding zone.
- **Assign stores** per pricing zone from the last page's store names.

### ⚠️ Common errors / risk items (retailer-specific)

- **Interchangeable store names** (know these mappings when assigning): Craig = Thompson House; Skagway = Fairway Market; Barrow = Utqiagvik; AC Lakeside Sitka = CCC; AC Bethel = Bethel; AC Nome = Nome.
- **Sitka insert pages** go at the **end** of the Sitka pricing zone.
- **Staggered flyer dates:** check page 1 of every zone. If a zone has different dates, edit that zone's dates; the run's overall date range must extend to the **farthest-future** date (e.g. zones ending on the 21st or 28th → run to the 28th). A warning should appear on the Overview tab. Any date concern → contact the account DOC.
- **Two-week runs are split:** PDFs often show a two-week run but are split into two weekly runs for budget/analytics — weeks are labelled.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Tag-specific linking doc. **Include** coupons, packaged deals, social media. **Exclude** retailer logo, sign-up page, special weblinks. Box all items with prices and 1L-media callouts. **Do NOT box** footer banners (except social-media banners/icons) or anything without a price (Daily Specials / Menu Items).
- **Tag / Tag QC (Low; Auto-tag ON, PDF image auto-select ON):** Tag-specific linking doc. Exclude brand. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Name is always bolded. Prefix uses `###/`; postfix usually `ea.` or `lb.`. Sale story/discount if applicable. Item valid dates: if a page's dates differ from the run, apply that page's dates to all items on it.
  - **Facebook callout URLs** (Display Type: Direct Link, pick the right one): facebook.com/AlaskaCommercialCompany or facebook.com/ACLAKESIDESITKA.
  - **Page categories:** every page except page 1 needs a category (usually "Grocery" for food flyers — use judgment). Apply item + Google categories.
- **Image QC: cutouts only — do NOT use PDF images.**

## FQC / go-live (owned by DOC)

- Spot-check French and English; check dates (mind the split two-week runs); **legibility heights 55/45**; standard 4 thumbnails; page categories; re-verify Item URL Verification session; all tasks complete.
- Toggles: available on all platforms, primary publication. Theme: No Theme unless Black Friday/holiday.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Alaska Commercial OneGuide (North West Company and Banners OneGuide 2.0, Google Doc `1TF9Y76uIwFGCAel6X5d_RgzhFQPW5ZPnJ9Ah3u064Gw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

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

---

# ALDI — Processing Guide

> **Source:** ALDI OneGuide (Confluence VEN → Google Doc `1YUO2oxv…bFTtk`).
> **OneGuide last updated:** Oct 6, 2025.
> **What this covers:** Retailer-specific processing instructions for ALDI so the
> bot can help with "how do I process ALDI / what's special about it?"
>
> 🔒 The source doc includes a file-transfer password, staff contacts, and staff
> emails — **all contacts and credentials are omitted here**. For who to contact
> and any passwords, open the ALDI OneGuide directly (FTP creds via the
> `#sftp-automation` Slack channel).

## Account at a glance

| | |
|---|---|
| Account segment | Core+ |
| Availability | All platforms |
| Slack channels | `#aldi`, `#aldi-ops` |
| Hosted URL | aldi.us/weekly-specials/weekly-ads |
| Flyer types | **1) Weekly Ad** (Insert, weekly) · **2) In Store Ad** (Handbill, weekly) |

## Files & schedule (Weekly Ad / Insert)

- **When files arrive:** Monday.
- **Publication cadence:** Available from Wednesday; Valid from Tuesday (→ valid to following Tuesday).
- **Preview date:** Monday.
- **Processing type:** Auto-stack.
- **Involvement:** Flex — FAB tickets sometimes (Image QC support); no coupons; Strategic Ops does retailer data services (Feedel).
- **Handbill / In Store Ad:** always goes **live 1 week *before* its valid dates** (e.g. handbill valid Oct 8 launches Oct 1). Only **one** In Store Ad should be live at a time (the Sneak Peek version).

## Files delivered

- The retailer's file contact sends files via a **secure file-transfer link**
  (password in the OneGuide — not stored here).
- A separate retailer contact sends the **Store Matrix** doc (used to build the
  generic codesheet) plus digital-page instructions.
- Download locally and re-upload to the ALDI SFTP (Flipp FTP creds via
  `#sftp-automation`). You should end up with 4 folders: Insert PDFs, Insert Images
  (Page 1/2/3 subfolders), Handbill PDFs (next week), Handbill Images (Page 1/2).

## Upload & setup (codesheet build)

> ⚠️ **Codesheet manipulation instructions were updated effective Jan 2026** — see
> the "[12.10.25] ALDI Codesheet Update Instructions" doc linked in the OneGuide.

**Insert — Pages codesheet:** headers `zones, page 1, page 2`. From the Store
Matrix Insert tab: `Ad Version → zones` and `→ page 1`; `Back Ad Code → page 2`
(add `page 3` from *Additional Digital Ad Code* if present). Concatenate
`_Front.pdf` onto page-1 names and `_Back.pdf` onto page-2 names (`.pdf` for page
3). Remove duplicates; find/replace `"_ "` → `"_"` to kill stray spaces. Download
CSV → upload to the code sheet tab in FADMIN.

**Insert — Stores codesheet:** headers `stores, pricing zones`. `Flipp Store
Identifier → stores`; `Ad Version → pricing zones`. Download CSV → upload.

**Handbill:** manual page upload (front = position 1, back = position 2); create
Pricing Zones from the back-page names (usually 2 PZs, ~2 pages each; page 1
applies to both). Stores codesheet same as Insert but uses Handbill-tab Back Ad
Codes.

### ⚠️ Common errors (ALDI-specific)

- **Wrong date in page name** — the date prefix is sometimes a previous week;
  ensure the correct date (e.g. `092122i`).
- **Front/back swapped** — a front page listed as back (or vice versa); page 1 =
  Front, page 2 = Back.
- **Case sensitivity** — FADMIN is case-sensitive; if the FTP filename capitalizes
  `Front`/`Back`, match it in the skins list.
- **Wrong versions paired** — keep matching versions together (e.g. `ODGRN_Front`
  with `ODGRN_Back`).
- **Underscore typos** — missing/extra underscore (e.g. `Lox48` vs `Lox_48`); if
  pages don't upload or FADMIN says a page is missing, check underscores.
- **Missing stores (yellow error on Stores codesheet)** — ALDI frequently adds
  stores. Use the FADMIN error to find the missing store code in the Store Matrix,
  then create the store (ALDI merchant tab → stores → create new store) with store
  code, address, city, name ("ALDI, <city>"), zip, and lat/long (from Google Maps
  → right-click pin). Leave a note in the comments tab so the lead has visibility.
- **Duplicate pages** — remove duplicates from the skins list.

## Image import (⚠️ risk item — critical to account success)

- Page 1 images come in the secure-transfer "LINKS" folder; Page 2 (and Digital
  Page 3) come from the SFTP (download via FileZilla).
- Re-upload to SFTP with subfolders (`…/Page 1`, `…/Page 2`, `…/Page 3`).
- Run **Sessions → Image Import**; FTP url = base path up to the `/`; toggle
  **"From Scratch" off** and submit.
- ⏳ Takes ~30–40 min — **do not** complete setup/leave the run until the import
  finishes with no error.

## QC specifics

- **Box Draw:** complexity Low; Auto-Box **enabled**; Box QC bot **enabled**.
  **Exclude:** coupons, packaged deals (e.g. washers/dryers), retailer logo,
  sign-up page, social media, special weblinks. Box each product block (with
  price/sale story) individually; if one price covers multiple items in a block,
  box them together.
- **Tag / Tag QC:** complexity Low; Auto-tag **disabled**. **Include:** name,
  description, price, sale story, categories, disclaimer. **Exclude:** pre/postfix,
  valid dates, SKU, original price, URLs. PDF image auto-selection **on** (select
  clean PDFs for all items).
- **⚠️ Category tagging is a risk item** — use the retailer's category chart in the
  OneGuide (Meat & Seafood, Fresh Produce, Cheese, Bread/Bakery, Deli, Grocery,
  Dairy, Beverage, Frozen, Household) to tag/QC item categories correctly.
- **Image QC:** prioritize PDFs; **prioritize clean product images over flat-lays
  for produce**. Item Image QC is a **risk item — aim for 100% PDF image selection**;
  ensure the same image across all versions of a produce item.

## Post-processing & FQC

- **Pre-price text QC:** via item export — check `PRICE DROP`/`PRICE DROPS`
  pre-price callouts are applied to all relevant items.
- **Category QC:** via item export — verify each category's items belong (use the
  category chart).
- **FQC:** on "Edit Date/Details," compare valid dates to the flyer (check Grand
  Opening "GO" zones for unique dates); QC all Handbill zones' dates. For the
  "Not all pages have slicing validated?" error, type `n/a` and submit.

## Flyer review risk items

- **Flyer sorting:** Weekly Ad (Insert) in **Position 1**, followed by Handbill
  (In Store Ad).
- Only **one** Handbill live at a time (the Sneak Peek version).
- All flyers available on all platforms.
- Insert: ~50 pricing zones/week (~2–5 pages each); watch for digital pages
  (labelled "digital") with possibly different dates. Handbill: 1–2 PZs/week.

## Known recurring issues (from the issue log)

- Weekly Ad not in position 1 (flyer sorting); multiple In Store Ads live at once;
  page-ordering / publishing errors; Weekly Ad hidden in hosted; digital insert
  distributed regionally instead of nationally (manual error).
- Product images sometimes not clean/isolated (cutouts) due to PDF formatting not
  being compatible with PDF Image Extraction.

---
*Source: ALDI OneGuide (Confluence VEN, Google Doc `1YUO2oxv0MbeQe7BAEAFwe_7TlA0bdR_DPDhgqzbFTtk`),
last updated Oct 6, 2025. Credentials/personal emails omitted. Last reviewed: 2026-07-15.*

---

# Alf Curtis — Processing Guide

> **Source:** Alf Curtis OneGuide (Google Doc `1StNp8FYO2XhLYDtEDmnXG0sORDx40_SVvUSEySeUO4Y`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Hosted URL | https://www.alfcurtis.com/ |
| Flyer type(s) & cadence | Flyer Type 1 — Monthly (Flyer, 6747; ad hoc) |
| Processing | Auto-stack; Flex (Flyer Review); OS Setup + FQC; no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad hoc. No preview date. **Linking document:** Yes.
- **Workflow:** Setup owned by M1000/Vendor; FQC owned by DOC/Flex.

## Upload & setup (owned by Vendor) — Codesheet, Config `m1000`
- PDFs, codesheet and linking document are uploaded to the SFTP.
- Download the codesheet locally and open it to identify the flyer-run dates.
- Create the flyer run under the **Flyer** flyer type (**6747**).
- Code Sheets tab → upload codesheet: **Config Name `m1000`**, PDF Base Directory = where the CSV is found, set the toggles per the OneGuide → Save Code Sheet → Process.
- Setup QC: mark Flyer Creation complete; confirm the pricing zones created match the codesheet (# of PZs, # pages per PZ, # stores); ensure vendors assigned and linking doc attached to **all** tasks.

## ⚠️ Common errors / risk items (retailer-specific)
- **URLs from the spreadsheet, matched by SKU.** If the spreadsheet says "In-Store Only" instead of a link, enter that into the **Disclaimer** field (not a URL).
- **Store-location links** (tag as LINK display type): Lindsay → alfcurtis.com/contact/lindsay/ · Peterborough → alfcurtis.com/contact/peterborough/ · Belleville (Quinte West) → alfcurtis.com/contact/quinte_west/.
- **Social media** (tag as LINK): Instagram → instagram.com/alfcurtishomeimprovements/ · Facebook → facebook.com/AlfCurtisHomeImprovements/.
- **Items with multiple dimensions:** if a different price applies to a different dimension, box each dimension separately.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons, packaged deals, retailer logo, sign-up page, special weblinks. **Include social media.** Box all priced items (use text boxes when item + price can't be boxed together); box the three store locations on the back page; box the Facebook/Twitter logos on the last page. Linking doc is Box-specific.
- **Tag / Tag QC (Low; Tag Lite; Auto-tag ON):** Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.** Brand is Box-specific — tag Name & Brand as in the flyer; if no brand called out, leave blank. Leave any field blank when the info isn't present.
- **Image QC:** standard.

## FQC / flyer review (owned by Flex)
- Confirm Item Image QC complete (green). Thumbnails (1065x600, storefront carousel premium, organic). Edit Details: dates match the PDF (last page), available everywhere, seasonal theme set. Pricing zones: pages chronological, all priced items with a visible sales story boxed, all pages interactive. Sessions: mark items In-Store Only, all green. **Geography: no stores or FSAs/zips added or removed.**
- **Flyer Review type: Lite.**

---
*Source: Alf Curtis OneGuide (Google Doc `1StNp8FYO2XhLYDtEDmnXG0sORDx40_SVvUSEySeUO4Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Amazon Fresh — Processing Guide

> **Source:** Amazon Fresh OneGuide (Google Doc `1KxIuRftJ_8KqdkdtJ4keo9IRk9WFpQ10Bh1W-5XU1fM`), updated Nov 6, 2025.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified) |
| Availability | All platforms |
| Slack channels | `amazonfresh-nativex` |
| Hosted URL | (none listed) |
| Flyer types | Weekly Flyer |
| Processing | Auto-stack; **DOC** owns upload/setup & FQC; **Flex** owns Image QC & Flyer Review; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From/To Wednesday; Valid From/To Tuesday. Dates are **not printed on the PDF** — always follow the Wed–Tue cadence (specific item date ranges may appear on the front/back page).
- **Linking document:** No.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages → Edit → select all pages from the SFTP; Confirm & Upload the pages dated for the upcoming flyer. Auto-Group (only ~2 pages per version, grouped into 1–2), English only. Save & Confirm — **do NOT Process Internally.**
- **Pricing zones:** each set of pages carries its version in the PDF name (e.g. LA1, MD1, NY1) — that is the **pricing zone AND store name**. Assign each version its matching store set.

### ⚠️ Common errors / risk items (retailer-specific)

- **Do NOT Process Internally** after upload.
- After SFTP upload, confirm no un-uploaded pages remain in the SFTP (Pricing Zone tab → Items View).
- Dates aren't on the PDF — enforce the Wed–Tue cadence.
- **Every item must be tagged with the Amazon Fresh deals URL** (`https://www.amazon.com/fmc/deals/?...almBrandId=QW1hem9uIEZyZXNo...`). This is checked again in FQC/Flyer Review.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** no linking doc. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** no linking doc. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** **URLs: always tag every item with the Amazon Fresh deals URL.**
- **Image QC (Flex):** standard — clean PDF preferred, otherwise cutouts accepted.

## FQC / go-live

- **Pre-FQC (DOC):** confirm dates vs. PDF; availability toggles; thumbnails include retailer logo; all items boxed & tagged; spotchecks (20% of pricing zones); previews published & clickable; sessions complete; geography correct.
- **FQC (DOC):** complete checklist.
- **Flyer Review type: Lite** (owned by Flex) — verify dates, sessions, previews, tagging accuracy, geography, availability toggles, and that **all items carry the Amazon Fresh deals URL**.

---
*Source: Amazon Fresh OneGuide (Google Doc `1KxIuRftJ_8KqdkdtJ4keo9IRk9WFpQ10Bh1W-5XU1fM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ambrosia Natural Foods — Processing Guide

> **Source:** Ambrosia Natural Foods OneGuide (Google Doc `1vYLvssbWXcw6mgIv9HQ_iJ8tf-0I34vRlIbaO0nh_z4`), updated Mar 13, 2026.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | **Flipp only** |
| Slack channels | `#ambrosianaturalfoods` |
| Hosted URL | None |
| Flyer types | **Monthly (9701)** · **Bi-Weekly (10165)** — both Ad-Hoc |
| Processing | Auto-stack; **Flex owns processing & comms**; OS completes upload; no coupons, no Feedel/data services |

## Files & schedule

- **Monthly (9701):** Ad-hoc files. Available/Valid From = 1st of the month; Available/Valid To = last day of the month (1-month run). No preview date.
- **Bi-Weekly (10165):** Ad-hoc; dates based on the retailer email (confirmed by DOC). No preview date. Retailer sends files directly to SFTP and emails to confirm; Flex confirms receipt (flag to `#flex-processingsupport` if no email reply; flag to DOC if files not uploaded to FTP), then adds run details to VAST and marks ready for Setup.
- **Linking document:** No.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → Upload from FTP → select pages from the corresponding Month folder → Auto-group → Save & Complete.
- **Pricing zone:** Flyer Creation → one zone **"Base"** → add all stores.

### Setup QC / dates

- **Monthly:** Available/Valid From = 1st, To = last day; **hidden on hosted**; no preview date; Internal Run Name = "Month"; External Run Name = "Month Specials" (e.g. May Specials); No Theme.
- **Bi-Weekly:** dates confirmed by DOC; **available on Flipp & Distribution, hide on hosted**; Internal Run Name = e.g. "July Bi-Weekly"; no external run name; No Theme.
- Thumbnails Standard 4 (1065×600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, storefront carousel organic – 1pg). Confirm sessions run; Geography = no stores added/removed.

### ⚠️ Common errors / risk items (retailer-specific)

- **Flipp-only account** — check the availability toggles carefully (monthly: available everywhere; bi-weekly: Flipp & Distribution only, hide on hosted).
- **Watch multi-buy prefixes** (e.g. `##/$$` = 2/$5).
- **"Save Up To"** goes in the **Sale Story** field only — do NOT enter it in the Dollars Off field.
- Page categories: **none** — remove any that were added.
- Do NOT box/tag product ads that have **no sale price**.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** no linking doc. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box any item with a price; exclude items without prices.
- **Tag / Tag QC (Low; Auto-tag ON):** no linking doc. Include brand (if easily identifiable), name, pre/postfix, valid dates, description (small/unbolded print), SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.** Postfix examples: LB., EA., BAG. Item category usually **Grocery** or **Health & Pharmacy**.
- **Image QC: none — cutouts only** (no image extraction). No URL/Link QC (no links).

## FQC / out-of-processing (Vendor-owned FQC)

- Ops spotchecks; mark Auto Stack Spot Check complete; confirm vendor tasks done. Verify dates/run name/theme per above; thumbnails; Tag QC items green; page categories none; vertical preview items clickable; sessions run & FSAs generated; geography unchanged.
- **Flyer Review type: Lite** (owned by Flex).
- **Out of processing:** page swaps are standard (baseline page-swap video).

---
*Source: Ambrosia Natural Foods OneGuide (Google Doc `1vYLvssbWXcw6mgIv9HQ_iJ8tf-0I34vRlIbaO0nh_z4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# ANBL (New Brunswick Liquor Corporation) — Processing Guide

> **Source:** ANBL OneGuide (Google Doc `1GE_oRs_xrglC9JbFqLotxEAa3PumKEwN81fBBNCwY5Y`), updated May 9, 2024.
> Bilingual (EN/FR) retailer. Contacts/credentials omitted (SFTP login and password are in the OneGuide — not stored here).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#anbl` |
| Hosted URL | anbl.com |
| Flyer types | Weekly |
| Processing | Auto-stack; **Flex = Flyer Review**; **OS = Setup**; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday. The retailer emails a WeTransfer link **or** a PDF attachment (one big English PDF + one big French PDF) plus a linking document; you upload them to Core FTP/FileZilla yourself (creds in the OneGuide — not stored here). The two big PDFs break out into individual pages.
- **Cadence:** Available From Monday, Valid From Sunday. Dates are pre-set in the flyer shells.
- **Linking document:** Yes.

## Upload & setup (owned by Flex; manual upload)

- Create a new folder in the FTP and upload the EN + FR PDFs.
- Pages → Edit → Select files. **Upload the French files → mark FR language → Save → refresh** to confirm all FR. Then **upload the English files → mark EN language → Save.** Auto-group → Save & Complete.
- **Pricing zones:** EN (English files) and FR (French files). Ignore the "stores in another zone" warning.
- Wait for sessions to run.
- **Attach the linking doc as `.xlsx`.**
- Edit Details: no theme, available everywhere. Legibility heights (pre-set) **45/35**. Thumbnails Standard 4. Geography: no stores added/removed.

### ⚠️ Common errors / risk items (retailer-specific)

- **Split the linking doc into EN and FR** — create 2 separate `.xlsx` files. Attach the English linking doc to English vendor tasks and the French linking doc to French vendor tasks.
- **Beer case size in Item Description is usually inaccurate** — verify against the flyer during FQC.
- **Unique item valid dates** — verify Valid From/To against the flyer.
- Setup QC: confirm the linking document ("Flyer pricing") is attached; double-check dates against the publication schedule.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks. Box each item per the spreadsheet (single or multi-item); use a text box for the text next to each item.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-select ON):** linking doc required. Include name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific. **Exclude pre/postfix.** Tag items with multiple versions separately; tag the bottom banner on each page as a **Link** type.
- **Image QC:** tends to be all cutouts — double-check.

## FQC / go-live (owned by DOC)

1. **Items without URL** (Overview) should be 0 — if not, cross-reference the linking doc.
2. Pricing Zone tab → Item QC: # of boxes and tags equal/similar.
3. Pages tab: first page(s) no categories; **RISK** — verify unique valid dates against the flyer; **RISK** — recheck beer case size in item descriptions.
4. Image QC: usually cutouts, double-check.
5. Pages tab all 3 numbers green & equal; sessions run; vendor tasks complete.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: ANBL OneGuide (Google Doc `1GE_oRs_xrglC9JbFqLotxEAa3PumKEwN81fBBNCwY5Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Andres Electronics — Processing Guide

> **Source:** Andres Electronics OneGuide (Google Doc `1w71qbPPpYwvD7Ta8JWMaHnQDttqxARZiTTlhIogYz1U`), updated Sep 23, 2025.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#processingsupport` |
| Hosted URL | andreselectronicexperts.com/en/pg-flyer |
| Flyer types | Weekly (4346) · Monthly |
| Processing | Auto-stack; **Flex = Processing Support**; **OS = FQC**; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Monday (inconsistent). The retailer submits files; they often reply slowly (bump or occasionally call) and often send the **URL document as an email attachment** rather than through the SFTP. Lead time is 5 days — push back on timelines when needed.
- **Cadence:** Available/Valid From & To Thursday — **varies; confirm against the flyer PDF** (dates called out in the retailer email and/or on the first/last page).
- **Linking document:** Yes (required before OS can begin — download from the retailer email; bump if not sent).
- Occasional page swaps due to price updates.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → select the folder dropdown for the flyer. **Do not upload the full flyer PDF — only the individual pages.** Auto-group.
- **Flyer Creation:** one pricing zone named **"Base"**, add all pages, Save & Done. Add all stores.
- While sessions run, attach the links spreadsheet — **check "Mass attach"** to apply it to all Vendor tasks (OS cannot begin without it).
- **Setup QC (Flex):** Edit Details — dates from the email/PDF, available everywhere, External run name from the email, No Theme (unless holiday). QC thumbnails (include the Andres logo).

### ⚠️ Common errors / risk items (retailer-specific)

- **Special valid dates:** if items have special valid dates, they MUST be tagged (override dates).
- **Financial plans / financing options:** do NOT reference or tag financing anywhere (price, prefix/postfix, discount).
- **Bad image extraction:** many extracted PDF images have "grease marks" — in those cases always use the **cutout**.

## QC specifics

- **Box Draw (HIGH complexity; Auto-Box OFF, Box QC bot ON):** linking doc required. **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box pages, single items, washer/dryers, and groups of appliances.
- **Tag / Tag QC (Low; Auto-tag ON):** Tag-specific linking doc. Include name, pre/postfix, valid dates, description, SKU (on the linking doc), price, sale story, categories, disclaimer, original price, URLs. Brand is Tag-specific — brand name is usually inside the item box in a different/standout font above the item name.
  - **Do NOT tag financing pricing.** Copy sale-story punctuation exactly (uppercase/lowercase/numbers). Include a disclaimer only if it's inside the box. Every item needs a category.
  - **URLs come from an Excel sheet in Tagging/Tag QC; items without a link are marked "Mark In Store Only."**
- **Image QC:** prefer a clean PDF image; use cutout where the PDF isn't clean (e.g. grease marks).
- **Item Category QC (Flex) — page category chart** (no page category on page 1): Audio Video Furniture; Car Stereo; Communication; Computers; Front Page Deals; Home Audio; Kitchen; Laundry; Marine Electronics; Photo and Imaging; Portable Electronics; TV and Video; Whole Home Audio. Choose by the theme of items on the page.

## FQC / out-of-processing (Vendor-owned FQC)

- Mark Autostack Spotcheck complete. Overview → dates (checkable on the last-page fine text), available everywhere, external run name from the email, No Theme. Thumbnails (1065×600, stock prem, storefront carousel premium/organic). Image QC. Pricing Zone: everything boxed, special valid dates tagged, previews load & item pops generate. Pages: all QC'd. Sessions: verify URLs. Geography: no week-over-week store changes. Ignore the "Not all categories … have thumbnails" warning.
- **Flyer Review type: Lite** (owned by Flex).
- **Out of processing:** standard page swaps.

---
*Source: Andres Electronics OneGuide (Google Doc `1w71qbPPpYwvD7Ta8JWMaHnQDttqxARZiTTlhIogYz1U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Andy's Quality Market — Processing Guide

> **Source:** SpartanNash Independent Partnership OneGuide (Google Doc `11nBej2Mg5fQvG_SWCt8pMfJQfbWkJx5SmLXd-lluPv4`), updated Jun 24, 2026.
> This article covers **Andy's Quality Market**; the same doc covers the SpartanNash independent-partnership banners (Metcalfe's, Harding's/Remke, Andy's Quality Market, Park Street Market, Midtown Fresh Market, Garden Fresh Marketplace, Food Town Toledo, Dash's Market, Bueche's Food World, Oleson's Farm Fresh Markets, Heartland Marketplace). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#spartannash-independent-partnership`, `#flex-processingsupport` |
| Hosted URL | (per banner) |
| Flyer types | Direct (Weekly) |
| Processing | Auto-stack; **Flex = Processing Support**; no OS-outside-standard, no coupons, no Feedel/data services |

## Files & schedule

- **Files received / cadence:** Weekly.
- **Preview date / linking document:** N/A (see Metcalfe's exception below for a Tag linking doc).

## Upload & setup (owned by Vendor)

- Files uploaded to SFTP. **Manually upload all pages → Auto-group → English only.** Add all stores.
- Setup: thumbnails (Standard 4). Edit Details — Available/Valid From & To match the PDF dates, available on all platforms, **No Theme** (grocery).
- **Banner exceptions:**
  - **Bueche's Food World:** 2 zones, 104 and 105 — each uses the pages with its number and is applied to its single store by store number.
  - **Dash's Market:** *no longer processing* — pages were to be ordered P1, Flap P1, P2, Flap P2, P3…

### ⚠️ Common errors / risk items (retailer-specific)

- **Metcalfe's SKU tagging (Metcalfe's only):** every item must be tagged with its SKU from the linking document. **Remove any special characters — SKU must be numbers only, and no spaces between SKUs.** Correct: `0002840031404,0002840051777`; incorrect: `"0002840031404, 0002840051777"`.
- **Pages in chronological order**, all shoppable items boxed, all stores added.
- **Geography:** no stores or FSAs/zips added or removed.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** no linking doc. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item with a price and/or sale story.
- **Tag / Tag QC (Low; Auto-tag OFF):** no linking doc (**except Metcalfe's — Tag-specific linking doc, Yes**). Exclude brand. Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates.**
- Image QC: none specified.

## FQC / go-live (Vendor-owned)

- Thumbnail QC. Edit Details: check dates against PDF pages, available everywhere. Pricing Zones: all stores added, all shoppable items boxed, pages chronological. Geography unchanged. Complete FQC checklist.
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Andy's Quality Market OneGuide (SpartanNash Independent Partnership, Google Doc `11nBej2Mg5fQvG_SWCt8pMfJQfbWkJx5SmLXd-lluPv4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Animo Etc — Processing Guide

> **Source:** Animo Etc OneGuide (Google Doc `1NcVu39V49xZf6074e9wjJbjA-f4I59JHoKCqBsSWjlA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#animoetc`, `#flex-processingsupport` |
| Hosted URL | https://animoetc.com/circulaire |
| Flyer type(s) & cadence | Flyer Type 1 — Monthly (ad hoc) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad hoc (available/valid dates all ad hoc).
- **Linking document:** Yes — used for both Box and Tag.

## Upload & setup (owned by Vendor)
- **Manual upload:** Pages → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group (or key in grouping numbers). **Set all pages to FRENCH language.** Save & Confirm — do **NOT** process internally.
- **Pricing zones:** create Base PZ, select all applicable pages, Save & Confirm, add all stores.
- Add the linking doc to all vendor tracks (mass upload).
- Setup QC: confirm all SFTP pages were uploaded (none left behind), confirm flyer dates (usually first/last page), thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)
- **Item count / content policy:** flyers sometimes can't meet the 6-items-per-page average. If so, box some grouped items as separate items to meet the threshold.
- **SFTP leftovers:** if uploading from SFTP, confirm no pages remain un-uploaded.
- **URLs:** almost all items should have a URL — cross-check the link sheet for any item missing one. Some items are simply not listed on the link sheet, and it's OK for those to have no URL.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** Exclude coupons, packaged deals and special weblinks. Retailer logo, sign-up page and social media are excluded **unless they appear in the link sheet** (then include).
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name, price, categories, URLs; brand/pre-postfix/valid dates/description/sale story/disclaimer/original price included if applicable. **Exclude SKU.** Linking doc required.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / flyer review
- Pre-FQC (Flex): dates vs PDF, availability toggles, thumbnails include retailer logo, standard flyer-review checks, URL check against link sheet.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Animo Etc OneGuide (Google Doc `1NcVu39V49xZf6074e9wjJbjA-f4I59JHoKCqBsSWjlA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ares Cuisine — Processing Guide

> **Source:** Ares Cuisine OneGuide (Google Doc `1j0ReciWcWynjiXR5ot2PBM77cjPpktg4F5Q6JfamLD0`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Plus |
| Availability | All platforms |
| Slack channels | N/A |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer Type 1 — Flyer (ad hoc) |
| Processing | Auto-stack; no Flex involvement; no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad hoc (available/valid all ad hoc).
- **Linking document:** Yes.
- **Workflow ownership:** Upload/Setup by Vendor; Image QC by Flex; FQC by DOC.

## Upload & setup (owned by Flex)
- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages → Edit → select all pages from SFTP → Confirm & Upload. Auto-Group (or key grouping numbers); ensure correct language selected. Save & Confirm — do **NOT** process internally.
- **Pricing zones:** create Base PZ, select all pages, Save & Confirm, add all applicable stores, attach linking doc.
- Setup QC: confirm all SFTP pages uploaded, confirm flyer dates, thumbnails Standard 4, ensure preview dates set.

## ⚠️ Common errors / risk items (retailer-specific)
- **Look for multiple products** in a single offer/image.
- **SFTP leftovers:** confirm no pages remain un-uploaded in the SFTP.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc required for boxing.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields (name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs). Linking doc is Tag/QC specific.
- **Image QC (Flex):** PDF preferred if clean; otherwise cutouts accepted.

## FQC / flyer review
- Pre-FQC / FQC (owned by DOC): dates vs PDF, availability toggles, thumbnails with retailer logo, standard flyer-review checks.
- **Flyer Review type: Lite.**

---
*Source: Ares Cuisine OneGuide (Google Doc `1j0ReciWcWynjiXR5ot2PBM77cjPpktg4F5Q6JfamLD0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ashley Furniture Homestore — Processing Guide

> **Source:** Ashley Furniture Homestore OneGuide (Google Doc `1gHwRvKATecE2W6jjULExiZy9F5HGS65oM-vOGF32_ac`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#ashleycanada` |
| Hosted URL | flyertown.ca/flyers/ashleyfurniturehomestore-west |
| Flyer type(s) & cadence | 4149: West Flyer (ad-hoc) · Flyer Type 2 (Monthly) |
| Processing | Trim Stick; Flex (FAB Tickets); OS Setup; **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** ad-hoc. **Cadence:** Available From Monday / Valid From Tuesday.
- **Workflow:** Upload/Setup by Vendor; Image QC by Flex; FQC by DOC.

## Upload & setup (owned by Flex)
1. Pages → Edit → select correct files for the week → Autogroup → Save and complete.
2. Create pricing zone: **Base**. Add all stores.
3. Check sessions — all green **except** PDF Image Auto Selection. Clear remaining FTP files.
4. If no linking doc in FTP, add vendor note "No linking doc, proceed with tasks"; if present (FTP or email), upload as mass attachment to all vendor tasks.
5. Overview → Edit Details → Available everywhere, No theme.
6. Check the Flipp × Ashley Homestore sheet to see whether a **UTM code** should be applied.
- Setup QC: thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)
- **URL domain (top risk):** always use the **`.ca`** URL (`ashleyhomestore.ca`). Do **NOT** use `.com` (`ashleyfurniture.com`).
- **Disclaimers:** found at bottom of each page; tag the disclaimer matching the symbol beside the price/name. Every item with a symbol (`*`, `**`, †, ††) must have a disclaimer.
- **Data piping:** some items won't pipe because they aren't live on the website yet — spot-click items to confirm. **Data-piping should not fall below 90%.**
- **SKUs must be prefixed `AFHS-`** (e.g. `AFHS-M71131`, not `M71131`); add the prefix if missing. For multiple SKUs, enter the package-deal SKU first, then individual items.
- Only search SKUs on the Ashley **Canada** website (ashleyhomestore.ca).

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Linking doc is Box-specific.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields. Brand entered EXACTLY as in the name field, name as-is with significant words capitalized. Price/original price as-is; do **not** put sale story in postfix. Valid-date override only for 1–2 day sales differing from flyer dates. Confirm each URL (flag to Ops if wrong). Categories = appropriate Google category.
- **Image QC:** data-piped image > pdf > cutout. If piped + pdf images are bad, delete the URL to enable cutout selection, then re-insert the URL.
- **Post-processing (DOC):** Item Category QC, Item Image QC, URL/Links QC, SKU QC.

## FQC / go-live (owned by DOC)
- Apply all tracking codes. Item Search for missing SKUs (`SKU IS BLANK`, Item Type = Item) and missing URLs (`URL IS BLANK`) — appliance pages often left blank. Saving a URL auto-runs data-piping.
- Data Piping → aim near 100% Data Piped Image. Image QC (piped > pdf > cutout).
- Page categories by Grouping #/Page Name; **pages 1 and 4 get no categories**; categories must match the page; ON/WEST share categories but WEST APPLIANCES uses **Home Appliance**.
- Open Additional Links xlsx and confirm every link is boxed/tagged. Wayfinding QC, Spotcheck QC, mark items In-Store Only, re-verify URLs. Check horizontal (Flipp Web) and vertical (App/Hosted) previews.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swaps / post-live checks as directed.

---
*Source: Ashley Furniture Homestore OneGuide (Google Doc `1gHwRvKATecE2W6jjULExiZy9F5HGS65oM-vOGF32_ac`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ashley Homestore Atlantic — Processing Guide

> **Source:** Ashley Homestore Atlantic OneGuide (Google Doc `155SJO0VK30PwC9M3pKfhDgTV_SBZjQ6NbFGh7kGJ_IA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | Under construction (site: theatrium.ca) |
| Flyer type(s) & cadence | Flyer Type 1 — Direct (ad hoc) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad hoc. No preview date. No linking document.
- **Workflow:** Upload/Setup and FQC by Flex.

## Upload & setup (owned by Flex)
- Files sent via email including linking doc.
- **1 zone, English,** containing all pages and assigned all stores.
- Attach linking doc to vendor tasks.
- Setup QC: confirm all setup-QC checklist items correct.

## ⚠️ Common errors / risk items (retailer-specific)
- **Geography:** no stores or FSAs/zips should be added or removed — confirm at FQC.
- Use **cutout images** for this account (see Image QC).

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc required.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates.** No brand. Standard tagging: name, current price (flyer price), URL from the linking doc; include sale story from item image. If no linking doc found, confirm with DOC.
- **Item Image QC (Flex):** **use cutout images.**

## FQC / flyer review (owned by Flex → Vendor for review)
- Standard 4 thumbnails, no theme, available everywhere, geography unchanged, complete FQC checklist.
- **Flyer Review type: Lite** (shared flyer-review guide covering Ashley Homestore Atlantic, WorldWide Furniture & Gallery1 Furniture).

---
*Source: Ashley Homestore Atlantic OneGuide (Google Doc `155SJO0VK30PwC9M3pKfhDgTV_SBZjQ6NbFGh7kGJ_IA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Asian Food Centre - Wanless — Processing Guide

> **Source:** Asian Food Centre - Wanless OneGuide (Google Doc `1HGaPwyqzNy-3C_2CbOqBhPG_DE491TThCQdp6cKoYW4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Weekly Flyer (11810) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received:** Tuesday (often late, via email). **Cadence:** Available From Thursday / Valid From Wednesday — see risk note.
- No preview date. No linking document.
- **Workflow:** Upload/Setup and FQC by DOC.

## Upload & setup (owned by Vendor)
- **Files arrive late.** Valid dates are Thursdays, which is usually when the flyer arrives via email. **If the flyer comes in Thursday, set the available date to Saturday; if it comes in Wednesday, set available to Friday.**
- Pages come via email, so add to SFTP or upload directly from computer.
- **Manual upload:** download the PDF, split it with an online tool, Pages → Edit → Upload Local Files → upload from computer → Auto-Group → Save & Confirm — do **NOT** process internally.
- **Pricing zones:** create Base PZ, select all pages, Save & Confirm, add all stores.
- Setup QC: confirm all pages uploaded, confirm flyer dates (first/last page), thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)
- **Late file delivery** is the main recurring issue — adjust the available date per the rule above.
- **SFTP leftovers:** confirm no un-uploaded pages remain.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Box all items individually.** No linking doc.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** No linking doc.
- **Image QC:** standard pricing spotchecks included in pipeline.

## FQC / flyer review (owned by DOC)
- Pre-FQC: dates vs PDF, availability toggles, thumbnails with logo, standard flyer-review checks.
- **Flyer Review type: Lite** (owned by DOL).

## Notes
- 2025 Black Friday comms are tracked in a separate retailer operations-guidelines doc.

---
*Source: Asian Food Centre - Wanless OneGuide (Google Doc `1HGaPwyqzNy-3C_2CbOqBhPG_DE491TThCQdp6cKoYW4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Atlantic Superstore (RASS) — Processing Guide

> **Source:** Atlantic Superstore OneGuide (Google Doc `1VIwdBqsAqZbewJcGryrTA0vT5Rm7fZDxXc3OfJP_Flc`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (relationship quality: Excellent) |
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer type(s) & cadence | 5892: Weekly · 10549: General Merchandise (owned by Docs) |
| Processing | Auto-stack; Flex (Flyer Review); OS Setup; **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Tuesday / Valid From Thursday / Valid To Wednesday. **Preview:** Sunday.
- **Workflow:** Upload/Setup by Vendor; Article Numbers by Flex; FQC by DOC. Part of the Loblaw/LCL codesheet program (RASS = Real Atlantic SuperStore; DOM = Dominion).

## Upload & setup (owned by Flex) — Config `atlantic_superstore`
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded.** Edit Details → show rarely-used fields → Height dropdown → 4096.0 px → OK. If pages were added first, flag the Full-Time Ops stakeholder and continue.
- **Codesheet manipulation:** open the RASS DOM Final Codesheet; delete the hidden Date, Store Ledger and Print tabs (leave only pricing-zone tabs). For each tab: copy the PZ name into A1 (replacing "Effective Date:"), delete the `#ERROR!`/formula in B1, convert the `=TODAY()` date to plain text. Add **"& BASE ENGLISH"** to zone names. Unmerge any merged pagination cells and delete blank rows (prevents pages not pulling in). Download as .xlsx.
- Split into RASS (delete Dominion PZs, subtotals/totals) and DOM (delete RA PZs; drop a tab if it only has RA PZs) code sheets.
- Codesheet upload: **Config `atlantic_superstore`**, correct base path, **checks = all but the second and last**. Common error: "file codes match multiple files" → force process, then manually upload anything missing.

## ⚠️ Common errors / risk items (retailer-specific)
- **Shared pages between banners:** because RASS and DOM share certain pages (e.g. FLAP CON or GM pages), pulling a page for one banner marks it uploaded in the FTP. **Remember to manually upload those shared pages for BOTH RASS and DOM.**
- **Store assignments pulled incorrectly (RISK):** stores may appear assigned but the count won't match the codesheet, with overlaps. Fix: delete all stores from all zones, build a generic-stores codesheet and upload it.
- **French cross-lang zones:** naming often has a space between the dash and "FR", which errors when running codesheets. EN stores will run; copy the FR zone name from the individual PZ interface and paste it into the codesheet.
- **Tag all "PC Optimum" buttons** with the pcoptimum.ca link. **Tag all Joe Fresh pages** as ONE box / direct link with the joefresh.ca link.
- Check the correct pages pulled in (RASS: RA or RA/DA only; DOM: DA or RA/DA only). Geography shouldn't change week over week.
- External Run Name: "Weekly Flyer - Valid [dates]". Set a **Sunday preview** start date.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot ON):** **Include** coupons, packaged deals, special weblinks (draw a box over any PC offers with a URL). Exclude retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields; linking doc is Tag/QC specific. Name in ALL CAPS as "Brand Product Name, Quantity" (comma before quantity), English only; French verbiage → description. Do not put unit-price metrics ("6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — those go in description. **Article Number fields:** copy the product SKU (with unit of measure suffix e.g. `_KG`, `_EA`, `_LB`) into Article Number 1 (= SKU/Fetch URL); multiple SKUs map to Article Number 1/2/3/4 in order.
- **URL/Links QC (DOC):** reference Final Codes, links live in the Notes/URL column (col E). Box the linked area (usually the page header or a Shop Now/Click Here button) and tag as **Direct Link, not Item.**
- **Image QC:** PDF preferred unless unclear; meat/fish must be in a package or use the cutout; white background only, no lifestyle backgrounds.

## FQC / go-live (owned by DOC)
- Spotchecks; add codesheet URLs (PC Express / Joe Fresh); merge flap pages via storefront spotcheck; mark AutoStack Spotcheck complete; no overlapping FSAs (re-generate if needed); leg heights 45/20; thumbnails Standard 4 (start on 2nd/3rd page if flaps lead); spotlight "This Week's Savings".
- **Article-number check:** Item Search `SKU IS NOT blank` + `URL IS blank` → open item, Fetch to populate URL; then `Article Number 1 IS blank` + `URL IS NOT blank` → add article number. Spot-check 2nd Article Number fields.
- Page categories: page 1 gets none, each page 1–3 categories. Open the LCL Tracker (done by 2:30 Monday), enter flyer IDs for RASS and DOM. Check sessions, vertical scroll, vendor assignments, boxing, red warnings, flyer sorting (most recent on top, secondary pubs last).
- **Flyer Review type: Lite.**
- **Additional publications:** create a run in the GM/Specialty Grocery flyer type, manual-upload English pages (Provigo = French), 1 EN zone + 1 cross-lang FR zone (Provigo needs all pages French for vendor tasks + cross-lang to EN), assign stores per codesheet.

## Out-of-processing
- Standard page swap (per training video).

---
*Source: Atlantic Superstore OneGuide (Google Doc `1VIwdBqsAqZbewJcGryrTA0vT5Rm7fZDxXc3OfJP_Flc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Atlas Tool & Machinery — Processing Guide

> **Source:** Atlas Tool & Machinery OneGuide (Google Doc `1upxsU_m0Gr4oiduFMU-fvd5U6_3A9IV5aaTtKhuo-AU`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | Flipp only |
| Slack channels | None |
| Flyer type(s) & cadence | 11006: Flyer — Monthly / Ad-Hoc (1st → last of month) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received:** ad-hoc; monthly flyer usually submitted late/after the 1st. Confirm live date with the team (typically 5 business days after files arrive).
- **Cadence:** Valid From 1st of month → Valid To last day of month; Available From subject to late submissions.
- **Linking document:** Yes (Monthly Flyer Flipp Links.xlsx).
- Add the flyer run to VAST (mark Setup Ready; mark FQC ready once processing complete).
- **Workflow:** Setup by DOC/Vendor; FQC by Vendor (Flyer Review by DOL).

## Upload & setup
- Download files and upload PDF pages to SFTP. **(SFTP credentials in the OneGuide — not stored here.)**
- **Manual upload:** Pages → Edit → select pages from the Monthly folder → Autogroup → Save & Continue. Flyer Creation → Base pricing zone → Save & Done → Add All Stores.
- Overview → Edit Details: Available From ~5 days after submission, Available/Valid To end of month, Valid From 1st, no preview date, **available only on Flipp & Distribution**, no external run name, no theme.
- **Leg heights = 40, 35.** Thumbnails Standard 4 (1065x600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, organic – 1pg). Confirm sessions run. Download link sheet from SFTP and attach to all vendor tasks.

## ⚠️ Common errors / risk items (retailer-specific)
- **Boxing per the link sheet:** if there's only one line item & link for a promo, box as one large box; if multiple line items share the same link, box separately and reuse the link for each item.
- **Bare Tool & Kit** priced items are boxed **separately**.
- **FREE ITEM promos:** Name = the main product that has the sale price; Sale Story = "+ FREE! Item".
- **Indexed items:** carefully match the product image to the corresponding item name & SKU.
- Do **not** box headings with no link provided; do not box/link website URLs.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** **Include** coupons, packaged deals, special weblinks. Exclude retailer logo, sign-up page. Linking doc used for both Box and Tag.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields. Brand in Brand & Name fields; **add URL to the description field**; add SKU to SKU field. Sale Story e.g. "Save $", "Pre-Order Now!", "FREE ITEM". Category = most applicable Google category (e.g. Hardware > Tools). Match URLs from the link sheet by page number, ItemCode (SKU) and/or promo description — some items share a URL.
- **Image QC (Vendor):** generate piping groups, unselect PDF images → Filter, select clean PDFs with white background when available (do **not** use unclean PDF images).
- **Link QC (Vendor):** Overview → items without URLs → add missing links from the week's link sheet.

## FQC / flyer review (owned by Vendor)
- Mark AutoStack complete; confirm vendor tasks complete. Edit Details: Available From per DOC note/retailer email, monthly dates, **hidden on Hosted**, no preview date, internal run name = month, no external run name, no theme.
- Thumbnails Standard 4; Item Image QC done; items-without-URLs = 0; Tag/Tag QC both green; page categories N/A; check full-screen preview; sessions + FSAs generated; re-verify URLs; geography no change; complete FQC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swap (per training video). Black Friday ad-hoc comms tracked in a separate operations-guidelines doc.

---
*Source: Atlas Tool & Machinery OneGuide (Google Doc `1upxsU_m0Gr4oiduFMU-fvd5U6_3A9IV5aaTtKhuo-AU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Atmosphere Quebec & Sports Experts — Processing Guide

> **Source:** Atmosphere Quebec & Sports Experts OneGuide (Google Doc `182c2hoW1eaRrOBKWfKJS5zzGkzqJ80xlSzkQ4Xrgjjw`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fglsports-banners` |
| Hosted URL | sportsexperts.ca/en-CA/flyers-promotions/flyers-deals/flyer-sportsexperts |
| Flyer type(s) & cadence | Bi-weekly / ad hoc — 7973 Sports Experts · 9196 Atmosphere Quebec · 10403 Sports Experts Local |
| Processing | Auto-stack; Flex (Flyer Review); **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Monday; dates called out in the file-delivery email. **Cadence:** Available/Valid Wednesday → Tuesday. **Preview:** usually the Monday before (email specifies).
- **Linking document:** Yes (bilingual EN/FR). **Workflow:** owned by DOC (Upload/FQC/Preview Links/Revisions).

## Upload & setup (owned by DOC)
- **Standard flyers (7973 / 9196):** manual upload from the corresponding FTP folder → Autogroup, don't process internally. If bilingual, upload twice and set the second set to French (they sometimes send EN and FR versions). Pricing zones **EN & FR**.
- **Linking doc manipulation:** combine Name/Brand, Modele, Description; remove unnecessary columns. Once done for EN & FR, upload as a mass attachment to all vendor tasks.
- **Local flyers (10403):** upload, Autogroup, don't process internally; pricing zones **Laval and/or Repentigny** (per email); **absolutely no linking document** — add vendor note "no URLs, please do not add any".
- **Setup QC (standard):** Available everywhere; Available Wed→Tue; Valid = Available unless stated; **internal preview date 1 week before live**; external run name per email; theme N/A unless stated; **legibility heights 55/40**; thumbnails Standard 4.
- **Setup QC (Local):** **RISK** — local flyers often fail content policy due to too few items; confirm enough items before Setup QC. Toggles **Hidden on Hosted**; **deep link** required for the retailer's Facebook ads (only works once live and if the customer's postal code matches; add the flyer run ID to the Links document to generate it).

## ⚠️ Common errors / risk items (retailer-specific)
- **Brand field must be EMPTY.** Brands appear as logos on the PDF (not caught by text extraction), so tag the brand as part of the **Name**, at the **front** (e.g. "THE NORTH FACE VENTURE 2 …"). Never append the brand at the end.
- **Name** must match the link sheet **verbatim** (copy/paste, same casing) — do not use the PDF name.
- **Original Price is never tagged** in the Original Price field — put it in the **Description** ("Regular Price $x.xx" / "Prix régulier: 0,00$").
- **Description** must contain the **SKU** and the regular/original price.
- **Price postfix must always be blank** (no "each"/"per pair"/"chaque"/"la paire") — new ask as of Dec 13 2024.
- **Sale Story** always ALL CAPS, as in the flyer; don't use "Dollars Off"/"Percent Off" fields.
- **Images:** PDF or Data-Piped images only — **cutouts must never be used.** Colour variant images must match the tagged colour.
- **URLs:** use the link sheet; English pages get English URLs (`sportsexperts.ca/en-CA/`), French pages get French URLs (`sportsexperts.ca/fr-CA/`).

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Box single-item offers individually; box multiple items of the same style/colour together in ONE box. On bilingual pages, only box English text on English pages and French text on French pages. Box coupons/general sales callouts (usually red) and Triangle Rewards call-outs. Linking doc used for both Box/Tag (local 10403 has no links).
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name (from link sheet verbatim), valid dates, description, SKU, price, sale story, categories, disclaimer, URLs. **Exclude pre/postfix and original price** (see risk items). Brand is Tag/QC specific — kept out of the Brand field.
- **Image QC:** PDF & data-piped images only; if the image doesn't match the colour variant, override via the merchant page (copy image address → paste into "Override Image URL" → save → reselect in Image QC).

## FQC / post-processing (owned by DOC)
- **Standard flyer:** General Tagging QC (missing URL / missing reg price / missing brand in title / postfix text via `Price Text IS NOT blank` / missing sale story). Item Image QC (clean PDF or data-piped; colour variants match; never cutouts). **Preview links:** format an item-details sheet (keep flyer_name, page, display_type, name, description, sale_story, raw_current_price, url; rename name→Name & description→SKU & Reg Price; EN/FR tabs), then generate preview links from the preview-code sheet and email them (attach the item-details sheet).
- **Local flyer:** standard FQC, no links, no image QC; apply the retailer's campaign **disclaimer to all items** via multi-edit; deep link as above.
- **Final QC checklist:** check flyer boxing (grouped items in one box), mass-update EN/FR URLs from retailer email, apply direct links, verify brand at front of name, one SKU per product, run custom action to set all products to cut-outs, tag missing sale stories; via flyer export, import-blank the pre-price text / descriptions / original prices / price_text fields; generate Amazon preview links for EN + FR and send to the retailer.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swap (per training video).

---
*Source: Atmosphere Quebec & Sports Experts OneGuide (Google Doc `182c2hoW1eaRrOBKWfKJS5zzGkzqJ80xlSzkQ4Xrgjjw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Atwoods Ranch & Home — Processing Guide

> **Source:** Atwoods Ranch & Home OneGuide (Google Doc `1wLtiirDZu3icD7Gxsfb5VtMSiIFkzie2oStE--ClFTE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 |
| Availability | All platforms |
| Slack channels | `#atwoods` |
| Hosted URL | www.atwoods.com |
| Flyer type(s) & cadence | Scheduled + ad-hoc (regular flyer; plus Bargain Barn monthly) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad-hoc. **Linking document:** Yes.
- **Workflow:** Upload/Setup by Vendor; FQC by DOC. Track the run in the VAST spreadsheet (fill flyer run ID + available date, set SETUP READY).

## Upload & setup (owned by Vendor) — Codesheet, Config `m1000`
- Download files from the emailed transfer link (pages, codesheet, linking doc). Upload **only the PDF pages** to the FTP (not the codesheet/linking doc). **(FTP credentials in the OneGuide — not stored here.)**
- **Code Sheets** upload: Name = Weekly, choose file, **Config Name `m1000`**, PDF Base Directory from FTP, **Toggles 1, 3, 4, 5, 6** → Save Code Sheet → Process Code Sheet.
- Overview → Edit Details: available everywhere, theme (e.g. Black Friday) or none, key messages (page-1 callout or generic e.g. Weekly Savings), **external run name from the codesheet/emails**.
- Thumbnails Standard 4; Pricing Zones → Spotlights to QC key messages; attach the linking doc via Vendors → Upload Mass Attachment (all tasks). Pipeline: Setup QC.

## ⚠️ Common errors / risk items (retailer-specific)
- **Ad-hoc publications** (Bargain Barn, Salina, Siloam) arrive randomly — create an empty flyer-run shell, confirm dates with the retailer, and bump the new flyer in `#atwoods` to BD. (Reference existing runs in the "Flyer" flyer type for setup.)
- **Bargain Barn** is a 2-page clearance flyer with **NO retailer logo** → cannot go on Flipp (content policy: needs the Atwoods name/logo on the front). Set it **available only on Hosted**, external run name & key messages "Bargain Barn".
- **Atwoods logo** on page 1 links to atwoods.com. **Facebook** is the only social to tag. **Email Signup** (last page) must be tagged — box only the top half (exclude the "JOIN" text).
- **Credit-card / Slice / Summary-of-credit-terms** links must be tagged (URLs listed in the OneGuide). **Summary of Credit Terms has an UPDATED URL** — do not miss tagging it.
- **Image QC:** most regular-flyer images are cutouts (PDFs aren't clean); watch for OS selecting items with a **black background**.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box the Credit Card & Slice pages/boxes and the summary-of-credit-terms (usually bottom of page 9). Linking doc is Box-specific.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF Image Auto Selection ON):** Include all fields. Linking doc is Tag/QC specific; brand is Box-specific.
- **Item Category QC (DOC):** food → Home & Outdoor Living; guns → Outdoor Recreation.

## FQC / go-live (owned by DOC)
- Legibility heights 50/40 (pre-set). Item Image QC (mostly cutouts; avoid black backgrounds). Category QC via "Items Without Analytics Categories". Page categories: page 1 none; guns = Outdoor Recreation.
- Tag the risk-item links (logo, Facebook, email signup, summary of credit terms). Links QC for items without a URL: pull the CSV from Vendors, reformat to item import (delete "item name"/"Error", rename `links` → `english_url`, drop rows with no URL), Import Items. Check horizontal & vertical previews.
- Pipeline: Final QC. **Update Flyer Sorting** so the newest weekly flyer shows first (confirm via emails/retailer if unsure).
- **Flyer Review type: Lite.**

---
*Source: Atwoods Ranch & Home OneGuide (Google Doc `1wLtiirDZu3icD7Gxsfb5VtMSiIFkzie2oStE--ClFTE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Avril Supermarché Santé — Processing Guide

> **Source:** Avril Supermarché Santé OneGuide (Google Doc `1ksg2EiOJfqD0S7NoGQJbqrZGHgxqsFy2VivXFXJMeXE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#avril-supermarche-sante`, `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly (Circulaire, 10471) · Flyer Type 2 — Monthly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Wednesday / Valid From Thursday / Valid To Wednesday. **Preview:** Wednesday.
- **Linking document:** Yes. **Workflow:** Setup by DOC; additional FL upload by DOC; Link QC & FQC by Flex.

## Upload & setup (owned by Flex) — Circulaire (10471)
- Files uploaded to SFTP; pages manually uploaded to the flyer run.
- **2 pricing zones: FR and EN.** Upload files twice (mark one set English, one French). Prefix English pages with `EN_` so OS knows which link sheet to use.
- Add all stores. Attach linking docs to vendor tasks with note: "Please tag Links as outlined for their specific languages (EN for EN pages and FR for FR pages)."
- Setup QC: valid dates must match page 1; no sub-pages need to be drawn.

## ⚠️ Common errors / risk items (retailer-specific)
- **Link QC (EN/FR):** ensure the correct URLs by page language. Check EN pricing zone for links containing `fr/` and the FR zone for `en/`; the entire link must be updated per the linking doc.
- **"2 pour 1" items:** tag in the **Sale Story**, not in current pricing.
- **"Taxes en sus":** put in the **Description**, never in the post-fix.
- **Regular price range:** tag a range in the Description as "Reg. 9.59-9.99"; a single regular price goes in Original Price (e.g. "Original Price: 7.29").
- **Validity dates** (usually pg 1): Jeudi+Vendredi = Thu & Fri; Samedi+Dimanche = Sat & Sun; Lundi = Mon; Mardi+Mercredi = Tue & Wed.
- **Brand field "Avril":** any item whose brand just says "Avril" must be updated to Avril Cuisiné, AVRIL SÉLECTIONNÉ, or avril gourmet.
- **Fruit & Vegetable (FL) pages:** placeholder pages must be swapped IN; on Monday the FL page is added to both PZ (an `EN_` version plus the base French), in position 2 of the flyer.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks, and the banners at the bottom of most pages (**box the ENTIRE banner**). Use items + text boxes so the whole area is clickable — don't box just the text or just the item. Linking doc is Tag/QC specific.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF Image Auto Selection ON):** Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates** (tag validity dates as noted in risk items). Brand is Tag/QC specific.
- **Image QC:** clean images if available.

## FQC / links QC (owned by Flex / multiple parties)
- **Complete Links QC before Final QC:** Overview → items without URL (cross-reference linking sheet; a page of 5 fruits/vegetables is tagged with the last line under page 1 labelled FL); Item Search `URL CONTAINS /en/` in FR zone (deselect Show One Per Item Group) → input correct FR link; repeat for `/fr/` in EN zone.
- FQC: Item Search `Price Text CONTAINS Taxes` → move "Taxes en sus" to Description; Item Search `Brand CONTAINS Avril` → fix bare "Avril" brands. Check box accuracy (banners at end of all pages except page 1; all items incl. photos clickable). Ensure Fruit & Veg pages swapped in.
- Thumbnails (1065x600 x2, storefront carousel premium x2, organic x1); image QC marked off; available everywhere; EN + FR zones all stores; geography no change; no items without URL before FQC.
- **Flyer Review type: Lite.**
- **Post-live:** apply corrections from the retailer's emailed corrections document.

---
*Source: Avril Supermarché Santé OneGuide (Google Doc `1ksg2EiOJfqD0S7NoGQJbqrZGHgxqsFy2VivXFXJMeXE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Axep / Intermarché / Intermarché International — Processing Guide

> **Source:** Axep/Intermarché/Intermarché International OneGuide (Google Doc `1OqBJfSMaaF1ehUichTWDQkf1SFEYv7RNk1xMVkfGWeU`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URLs | axep.ca/circulaire · lintermarche.ca/flyer-fr · intermarcheinternational.ca/circulaire |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; Flex (3FL + Flyer Review: upload, pre-FQC); **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Tuesday (Axep), Tuesday (L'Inter-Marché), Friday (L'Inter-Marché International).
- **Cadence:** Available From Wednesday / Valid From Thursday / Valid To Wednesday. **Preview:** Monday before. No linking document.
- **Workflow:** Upload by Vendor; FQC by DOC; Corrections post-live. Part of the Loblaw/LCL codesheet program.

## Upload & setup (owned by Flex)
- **Pre-setup:** find the week's code sheets (labelled `WK__ QC FINAL CODES`), download and upload to the LCL Flex Upload Folder, and update the Flex Tracker.
- **Axep-specific:** the flyer run won't appear in Legacy Pipeline. Open it via the Axep flyer-runs URL; it will show "Flyer Run Not Found" and no pipeline — **disregard**; once pages are uploaded the message clears and the pipeline generates.
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded.** Edit Details → show rarely-used fields → Height dropdown → 4096.0 px → OK. If pages were added first, flag Full-Time Ops and continue.
- **Manual upload:** select all files under the correct week → Autogroup → **change language toggle to French, Save** → Save & Complete. Check the Merchant FTP to confirm all pages pulled in.
- **Pricing zones (2):** **F** (French files — confirm layout from the week's code sheet ONLINE tab) and **F EN** (copy layout from F, tick cross-language box, cross-language to English, save).
- **Stores:** select the corresponding store set by zone name — do **NOT** "Select All Stores" (all three banners share one store database). Confirm the store count matches the code sheet; check weekly Loblaws emails for added/removed stores.
- Setup QC: Available Wed–Wed (1-day preview) with **Sunday preview start date**; Valid Thu–Wed; external run name "Weekly Flyer Valid [dates]"; no theme; confirm FTP fully uploaded; geography unchanged week over week.

## ⚠️ Common errors / risk items (retailer-specific)
- **Do not "Select All Stores"** — it pulls stores across all three banners (shared database).
- **Name field must include BOTH French and English product names** (e.g. "CROUSTILLES | POTATO CHIPS, 200 - 235 g"), ALL CAPS, format "Product Name, Quantity" with a **comma before the quantity**. Don't add "$" to quantities.
- **Do not put in the Name:** unit-price metrics ("6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties" — those go in the Description.
- **Brand only in the Brand field** — nowhere else. Do not enter brand, NG Code or SKU in the description.
- **URL leads to a different item → Flag.** Item quantities in the description → Flag.
- **Page swap final step (NEW):** page swaps often cause page-stitching issues (visible page doesn't match overlaid items), especially post-live. **Always rerun Page Tile Generation** after the page-swap sessions kick off; if issues remain, rerun and mark complete Vendor Box Tag onward; confirm via item view of all pricing zones.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons, retailer logo, sign-up page, social media, special weblinks. **Include** packaged deals. Draw a box only where there's a unique price for an item — nothing extra; do not box banners or social icons.
- **Tag / Tag QC (Medium; Auto-tag OFF):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU, URLs, Article Number.** Linking doc is Tag/QC specific; brand is Box-specific. Watch multibuy items (prefix + postfix combos). Valid-date overrides only when a promo sales story indicates it. Every item needs a category.
- **Image QC:** clean PDF where possible; use **cutout if PDF isn't clean and for meat items without packaging.**

## FQC / post-processing (owned by DOC)
- **Pre-FQC (3-FL Flex):** merge flap pages to the right (two flaps → merge together; single flap → merge with cover/P01). Thumbnails Standard 4, starting where the logo is; do not include flap pages even when merged.
- **Final QC:** confirm dates (Available Wed, Valid Thu–Wed, 1-week run), available everywhere, no preview date, internal run name "WEEK #", external run name "Weekly Flyer Valid …", no theme. Image QC clean PDFs except raw meat → **Cut Outs** (never the PDF). Confirm thumbnails complete; items-tagged matches Tag QC; 1–2 categories per page except page 1; check all items boxed and boxes line up (re-run tile-gen if not); geography unchanged; update store codes per note/retailer email.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put the flyer run ID in the LCL tracker; run ghostscript 9.06 gamma as needed; flyer sorting (current weekly, upcoming weekly, secondary pubs newest→oldest); article-# revision.
- Standard page swap (per training video) — plus the mandatory Page Tile Generation rerun noted above.

---
*Source: Axep/Intermarché/Intermarché International OneGuide (Google Doc `1OqBJfSMaaF1ehUichTWDQkf1SFEYv7RNk1xMVkfGWeU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
