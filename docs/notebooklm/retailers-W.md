# Retailer Processing Guides — W

> Bundle of 16 retailer-specific processing guides (W). Contacts and credentials are omitted from every guide.

**Contains:** Walgreens, Walmart Canada, Walt's Food Center, Weis Market, West Marine, Westlake Ace Hardware / WL Ace Hardware, Wholehealth Pharmacy, Wholesale Club (RCWC C&C), Wild By Nature, Wild Fork, Willow Park Wines & Spirits, Wine & Beyond, Wine Rack, Winn-Dixie, Woodcraft Supply, Woodmans Food Market


---

# Walgreens — Processing Guide

> **Source:** Walgreens OneGuide (Google Doc `1JnxLguiLaOp1C8YFvWUWFpCPRXszRhuO_vdIcnSUmJs`), updated Dec 1, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | **Flipp only** (hidden in hosted) |
| Slack channels | `#walgreens`, `#flex-walgreens` |
| Flyer types | **Weekly Ad** (2550) · **Monthly Savings Book** (3893) |
| Processing | Auto-stack; Flex (3FL); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Wednesday. **Linking document:** Yes.
- **Cadence (Weekly):** Available From Wednesday · Valid From Sunday · Available To Saturday · Valid To Saturday.
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → Pre-FQC (FTE) → FQC (1 day out, DOC + FTE).

## Upload & setup

### Weekly Ad (2550) — Vendor
- In FTP: use the version xls (**ignore PURERED_WEEKLY.xls**). Linking doc = `Flipp_URL.xlsx`; codesheet = `schematics/version.xlsx`.
- **Codesheet manipulations:** Column A = pricing zones → highlight → "!" → Convert to Number (removes leading 0s). Column B = stores → sort descending, then Convert to Number on numbers with leading 0s. **Remove rows with stores 21237 and 21275.** Save as .csv.
- **Codesheet upload:** cross-reference the last number in the "Adv Event" column against FTP pages to confirm all pages present. **Config name: `walgreens`**; Base path `/mmddyyyy` (no underscore); **NEW — uncheck Region Assignment and Combine Zones; MUST toggle "Use Page Pool".** Note in comments which zones the 5 main pricing zones are in: Houston, Chicago, Dallas, Phoenix, El Paso.
- **Setup QC:** URL doc + PDF page file sent to Tiderise team for an updated URL doc; attach updated linking doc; complete Setup QC; **hide in hosted.**

### Monthly Savings Book (3893) — Vendor
- Manual upload: Pages → Edit → find that month's savings-book pages (file name has the month + "ivc"). Upload all pages. Create one Base pricing zone; assign all stores, then **remove the PR store set**.
- **Setup QC:** crop blank space from the cover page (download → pdfcandy.com crop → re-upload → replace original cover in PZ tab). Hidden in hosted, available Distribution/Flipp. External Run Name "[Month] Savings Book"; no theme. Complete Setup QC.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required):** Include packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude coupons. Items are in a grid — **box each item individually**; reference the Flipp URL doc in the vendor task to ensure all banners and callouts are boxed.

**Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Brand = No; **SKU = N/A**.
- **Gift cards:** e.g. Name "$5 Walgreens Gift Card", Sale Story "$5 Walgreens Gift Card with myWalgreens", Disclaimer "Limit 2. No limits in NM."
- **Store rewards:** Name = "select cosmetics, beauty accessories, skin, sun or hair care"; Description = "Mix & match … thru [date] with myWalgreens"; Sale Story = "Earn $10 In-Store rewards when you spend $25 or more".
- **Walgreens Cash rewards:** Description "Earn $X W Cash rewards on $Y+ … thru [date]"; Sale Story "Spend $50, Get $10 W Cash rewards".

**Image QC:** **Use cutout images.**

## FQC / go-live

### Pre-FQC (FTE)
- **Page Category QC:** all pages get 1–3 categories except **page 1 (0 categories)** — filter grouping = 1, clear categories, "Copy to Same Index". Filter by grouping index for versioned pages; select the categories that appear most on the page.
- **URL/Links QC:** for each URL in the linking doc, Item Search "URL contains [URL]", match banners to the linking-doc image, confirm names/sale stories/categories, multi-edit as needed; banners with no items → Display Type "Link". Direct-Links section of the linking doc → Display Type "Link". **Then add a URL for all items not in the linking doc:** Item Search "URL is blank" per page grouping (usually 25–60), add `https://www.walgreens.com/offers/offers.jsp/weeklyad?enhancedDWA=true`. **No item or link may be left without a URL.**
- Create 4 standard thumbnails.

### Final QC — Weekly (Flex)
- **Geography:** ensure no stores/FSAs added/removed. If stores changed, check with DOC for **store closures**; if confirmed, close the store in FAdmin (Merchant → Stores/Sets → View Stores → set "valid to" = day before the flyer goes live).
- Rerun the **"remove FSAs" custom action** (also on the currently-live flyer). Check "View Item Boxes" for the 5 main PZs — all items boxed/tagged. Add the weekly-ad URL to any items without URLs.
- **Remove FSAs** from the weekly run via the "remove FSAs" custom action — must run in 2 chunks (text exceeds the character limit). Run this on **three flyers**: the one going live, the currently-live one, and the most recent no-longer-live one.
- Edit Details: Available From Wednesday, Available To Saturday, Valid From Sunday, Valid To Saturday; Internal Name = valid dates (e.g. "June 15 - June 21"); available everywhere; no theme.
- Flyer sorting: Weekly Ads, then Monthly Savings Book, then everything else (earliest publication on top).

### Final QC — Monthly Savings Book (Flex)
- All products with a barcode → **Display Type Item** (use item export/import for bulk). All items boxed/tagged; no blank space around the front cover; run dates match front cover. Complete FQC checklist.

- **Ad-hoc QC (DOC):** item correction notices.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** standard baseline page swap.

---
*Source: Walgreens OneGuide (Google Doc `1JnxLguiLaOp1C8YFvWUWFpCPRXszRhuO_vdIcnSUmJs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Walmart Canada — Processing Guide

> **Source:** Walmart Canada OneGuide (Google Doc `1KjkS5_Ijou8f3A_3Xsfb6PM6E-7JkBG2zDzMmijCpxI`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / **Tier 1 Premium**; relationship quality "Excellent" |
| Availability | All platforms |
| Slack channels | `#walmartcanada`, `#cp-walmartcanada`, `#flex-walmartca`, `#walmart-canada-datservices`, `#walmartcanada-ecomfeedsupport`, `#walmartcanada-offapp`, `#walmartcanada-retaileramplification` |
| Hosted URLs | EN: walmart.ca/en/flyer · FR: walmart.ca/fr/flyer |
| Flyer types | **Grocery/Weekly** (weekly) + Digests |
| Processing | Auto-stack; Flex = 3FL; **Strategic Ops: yes** (Feedel/retailer data services); no coupons |
| Flyer review | **Complex** |

## Files & schedule (Weekly)

- **Files received:** Wednesday. **Preview:** Tuesdays (apply preview date = **Thursday** in setup QC).
- **Cadence:** Available Wed→Wed; Valid Thu→Wed.
- **Linking document:** MMS export attached to the pipeline.
- **Workflow:** Upload & Setup (4 days out) → Check tasks (3) → FQC (2) → Send preview (1).

## Upload & setup (owned by DOC)

Assets needed: PDFs, zone chart, MMS export.

1. Copy zone chart to a new tab, paste as values. **If there is a second pagination chart for TARGETED zones, run two separate codesheets.**
2. Manipulate the new tab: insert 1 row above pagination between event code and page; fill blank/merged cells with page values; fix pagination numbering; download as CSV.
3. Upload codesheet — **Config `walmart_sc`**, use a short base path (end before "SC"/"Digital"), **only the second toggle is unchecked**.
4. **Canadianfood page is not pulled by the codesheet** — manually upload it twice (EN + FR) and allocate to QC PZs per the zone summary.
5. External run name = Flyer (EN) / Circulaire (FR); for digests confirm French names. Preview date = Thursday.
6. Thumbnails: Standard 4 + `first_page_thumbnail_400w` (GO versions done separately). Setup-QC thumbnails: 1065×600, `stock_premium`, `storefront_carousel_premium`, `storefront_carousel_organic`.
7. **Geography should not change** week over week (same 11 stores never re-assigned, no overlaps, no missing FSAs). Change all vendor tasks to **urgent** priority.
8. Manipulate MMS: keep only Name, Featured Item (→ SKU for vendors), Copy Description, URL, Department (→ Category); one tab; download XLS; attach to all vendor tasks.

## ⚠️ Common errors / risk items

- **WIN → SKU (add-to-cart):** Walmart's WIN (their SKU) must be in the **SKU field** or the item shows out-of-stock on walmart.ca. After tasks complete, run the **WIN-to-SKU import** to populate SKU and SKU #2 (`id_1` custom field) from the item report/URLs.
- **Stagger west-zone dates:** BC 3 AM, AB & SK 2 AM, MB 1 AM — update Available/Valid From times for all BC/AB/SK/MB zones (and targeted if present).
- **Make tagging updates across ALL versions of a page** — use item search + page-name versioning (Week#, Year, acronym e.g. SC/DIGITAL, page#, language E/B, region). Watch for late REV pages.
- **URL language parameters:** French items must use `/fr/`, English `/en/`; item-search and fix mismatches. Change any `http:` to `https:`.
- **Vendor/LID pages, banners, Rollback:** box banner links, add LID Media Variant; mass-update Rollback/Chute items to "Banner - Rollback" with the correct EN/FR URL.
- **French accents** spot check: œ é è â ê à û î ô ï ë ç.
- Coca-Cola SSD items require specific brand/term tagging (EN/FR) per the SSD category doc.

## QC specifics

- **Box Draw — HIGH complexity; Auto-Box ON, Box QC bot ON.** Include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box **all Walmart banners** (tag via "Banner URLs" section). Multi-items boxed/tagged separately even if same price.
- **Tag / Tag QC — LOW; Auto-tag OFF, PDF image auto-select ON.** Include brand, name, pre/postfix, valid dates, description, SKU (use MMS file), price, sale story, categories (use MMS), disclaimer, original price, URLs (use MMS). SKU from PDF; URL/category looked up in MMS by SKU (EN/FR columns). Banner URLs (front page, Rollback, Subscribe to Save, Everyday Low Prices, Pharmacy) are listed in the OneGuide.
- **Image QC:** clean PDF preferred; cutouts if no clean image. Multi + single items.

## FQC / post-processing (Feedel + DOC)

- Fill missing URLs via MMS/walmart.ca (cross-reference WIN); add pages to PZs; check no tagging missed (copy CES/Klarna/vendor pages from prior week).
- Category QC (Flex): items w/o analytics category (HBA→health/beauty, infant→baby). Page categories: 2 per page.
- Apply **tracking codes** (Claravine — Flipp + Hosted; credentials in the OneGuide — not stored here). Break down UTM/cmpid params.
- **Clone into "WKXX Non-Ad + Print Dark Stores"** (copy tracking codes), swap store sets per province, delete MB PZ for the test, and build the **Dark FSA report** (export prior dark FSAs, rename PZ headers to `flyer_id`/`fsa`, assign via "Assign FSAs From CSV"). Re-run FSA manipulations any time new pages are uploaded.
- **Custom actions:** Remove Stores, Remove FSAs (two batches for character limits), Assign FSAs From CSV.
- **Flyer Review: Complex.**

---
*Source: Walmart Canada OneGuide (Google Doc `1KjkS5_Ijou8f3A_3Xsfb6PM6E-7JkBG2zDzMmijCpxI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Walt's Food Center — Processing Guide

> **Source:** Walt's Food Center OneGuide (Google Doc `1whL74y1kv3lpxFelygVjwVvrfr1LHoONOzru0FTQhcM`). Contacts/credentials omitted.

> **⚠️ ACCOUNT INACTIVE (as of Oct 2025). DO NOT PROCESS any flyers for this banner/account.**

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#walts` |
| Hosted URL | waltsfoods.com |
| Flyer type(s) & cadence | Weekly Ad (41111) |
| Processing | Auto-stack; Flex = Flyer Review; OS = Setup; no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday. Available Mon→Mon; Valid Tue→Tue.

## Upload & setup (owned by Flex)

- Manual upload of all pages → auto-group → Save & confirm.
- Create a **Base** pricing zone, add the pages, assign all stores.
- Confirm PDF dates match the flyer run; complete Standard 4 thumbnails; complete Setup QC checklist.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF, PDF image auto-select ON.** Include name, pre/postfix, description, price, sale story, categories, disclaimer, original price. Exclude valid dates, SKU, URLs.
- **Category QC (Flex):** ensure a Google + analytical category on all items.

## FQC / flyer review

- Pre-FQC: pages ordered as numbered; thumbnail step complete; geography unchanged (flag any change to the full-time team).
- **Flyer Review type: Lite.**

---
*Source: Walt's Food Center OneGuide (Google Doc `1whL74y1kv3lpxFelygVjwVvrfr1LHoONOzru0FTQhcM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Weis Market — Processing Guide

> **Source:** Weis Markets OneGuide (Google Doc `1y184ktYH5iUJFspZrKP_PnglT2dEqvr_5jAgCeZ3KkQ`), updated May 1, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Merchant ID | 2455 |
| Flyer types | **Weekly Circular** (weekly — includes the 1–2 page 3 Day Sale) · **Monthly** (Ad Specials / grocery, HBC / Home, NOS / Natural & Organics) |
| Processing | Auto-stack; DOC upload/setup, Vendor pipeline, DOC FQC; no coupons; **Strategic Ops / Feedel data services: yes** |

## Files & schedule

- **Files received:** Monday.
- **Weekly cadence:** Available From Thursday, Valid From Wednesday; Available To Tuesday, Valid To Wednesday. Weekly flyer runs Thu–Wed; the 3 Day Sale runs Thu–Sun.
- **No preview days.**
- **Linking (tagging) document:** Yes for all flyers **except NOS**.
- All flyers are processed exactly the same.

## Upload & setup

- **Page numbers** are the digits after the underscore in the page name (e.g. `73_7` = page 7).
- **Codesheet** arrives on the SFTP as a `.txt`; open and save locally. There can be **more than one codesheet** — match the `CircularType` name (e.g. "Weekly") to the flyer / external run name.
- **Codesheet config: `weis`**; PDF Base Directory = entire path; **toggle all options except region assignment**.
- **Tagging document** arrives on the SFTP as `.xlsx` ("Weekly/Monthly Sale Items"), split into tabs (Weekly, 3 Day Sale; or HBC, Grocery, 3 Day Sale for monthly). Match tabs to flyers by comparing page numbers in the tab to the pages in the codesheet. If a flyer has more than one tagging tab, note it in the vendor tasks.
  - **Tagging doc manipulations:** delete empty columns G and H; select all and remove duplicates on every tab; save, import to Google Sheets, re-download as `.xlsx`; split tabs into individual `.xlsx` files per flyer; attach to all vendor tasks.
  - **NOS has no tagging document** — leave the note: "No Excel needed for processing, use PDF details."
- **External Run Names** (must be set on Edit Details): Weekly = `Weekly Circular`; 3 Day Sale = `3 DAY SALE`; NOS = `Natural & Organic`; HBC = `Monthly Home`; Grocery monthly = `Ad Specials`.
- No theme. Standard 4 thumbnails.

### ⚠️ Common errors (retailer-specific)

- **DO NOT box or tag the Rewards section** — promos stating "Free with xxx points" or "0.99¢ with xxx points" must not be boxed or tagged. Remove any boxes drawn there.
- **Codesheet typos** are frequent: commas used instead of periods (and vice versa), missing `.pdf` after page names, and page-allocation/order mistakes. If files are named "Region 1", correct to "RegionFiles 1".
- **Liquor pages** and typically **page 7** are not in the tagging document — this is expected. Only escalate if a *regular* page is missing.
- **Small red card** in the corner of a product → postfix must be "With Weis Preferred Shoppers Club."

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals, retailer logo, sign-up page, special weblinks. **Exclude:** coupons, social media.
- Box every item with a price. Multiple products sharing one price can go in one box; small product names under larger products with different prices need their own box. Don't overlap items — use text boxes.
- **Never box the Rewards section.**

### Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON)
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **SKU:** listed under UPC in the spreadsheet; enter up to **12 SKUs max** per item (first 12). Monthly NOS flyers usually have no spreadsheet.
- **Postfix:** add "with Weis Preferred SHOPPERS CLUB" when the card logo appears (including sub-items); combine postfixes where needed; do **not** add postfix to items without a price. **Any points offer goes in the Sale Story, not the postfix.**
- **Discount:** do not enter Dollars Off / Percent Off unless explicitly on the flyer.
- **Valid dates:** found at the bottom of the page unless otherwise specified; enter override dates if applicable.
- **Disclaimer:** only if within the drawn box (not the page-bottom disclaimer).
- **Page categories:** page 1 has none; every other page needs at least 1 (use the header on the page, e.g. Deli/Cheese & Baked Goods, Dairy & Frozen, Snacks & Beverages/Aisles of Savings).

### Image QC
- Prefer PDF. Avoid lifestyle/plated or images with backgrounds — choose the cutout unless it's really bad. Select the packaged item, not the plated item; avoid cutouts with a white border.

## Final QC / go-live notes
- Set the **External Run Name** on Edit Details (list above).
- **SKU corruption check:** Overview → Item Search, "SKU" + "Contains" + "+" and "+" + ",0" — any hits are corrupt SKUs; fix/confirm against the tagging spreadsheet (search by product name).
- Confirm **no boxing/tagging in the Rewards section.**
- **Leg heights 50/30.** Standard 4 thumbnails.
- **Flyer sorting:** weekly → 3 day → monthly flyers.
- Spotchecks handled by OS.
- **Flyer Review type: Lite.**

## Out-of-processing
- SFTP credentials are provisioned via the `#sftp-automation` Slack automation (credentials in the OneGuide — not stored here). Weekly files are dropped into a dated folder under the current year.
- **Vendor setup:** use the VAST spreadsheet, find the Weis Markets row(s) for the current week (multiple flyer run IDs may be needed for one file drop), fill in the flyer run ID and available date, and set to SETUP READY.

---
*Source: Weis Market OneGuide (Google Doc `1y184ktYH5iUJFspZrKP_PnglT2dEqvr_5jAgCeZ3KkQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# West Marine — Processing Guide

> **Source:** West Marine OneGuide (Google Doc `17d0VAnHfcg1C6HTpPOIEFU_ERCfSG1-i-PwoHhaRApU`), updated May 14, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#westmarine`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | westmarine.com/current-ad/ |
| Flyer type(s) & cadence | Flyer (11686) — **Ad hoc** |
| Processing | **Auto-stack + GhostScript**; Flex = Processing Support + Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad hoc (all dates ad hoc). **Preview:** one day before go-live so the client can review.
- **Linking document: YES — required** (used for both Box and Tag).
- Workflow: Upload & Setup → FQC → preview link to client & corrections → post-live revisions (updated URLs).

## Upload & setup (owned by Flex)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages → Edit → select all SFTP pages → Confirm & Upload → auto-group / add page numbers (correct language) → Save & Confirm. **Do NOT process internally.**
- Create a **Base** pricing zone, select all pages, add all stores.
- **Attach the linking document to ALL vendor tasks.**
- Setup QC: confirm all SFTP pages uploaded and look correct; external run name from the front-page callout; preview dates set; Standard 4 thumbnails.

## ⚠️ Common errors / risk items

- **Original Price ranges:** if the original price is a **range**, do NOT use the Original Price field — put it in the **Description** as "Original Price: $xx.xx - $xx.xx".
- **GhostScript:** watch how pages look after upload — text/colours can render wrong; **re-run sessions on GhostScript** if pages look off. Confirm no un-uploaded pages remain in the SFTP.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot ON.** Linking document required. Include packaged deals; exclude coupons, retailer logo, sign-up page, social media, special weblinks (unless included in the linking document).
- **Tag / Tag QC — Low; Auto-tag ON.** Include name, pre/postfix, valid dates, description, SKU (if available), price, sale story, categories, disclaimer, URLs. **Original Price in Description if it's a range.**
- **Image QC:** PDF preferred if clean; cutouts accepted otherwise.

## FQC / preview to client

- Confirm all products have URLs (reference linking doc), dates match PDF, availability toggles correct, thumbnails include the retailer logo, spot checks (20% of PZs), previews clickable, geography correct.
- **Preview link to client:** the day before go-live (before noon) email the **Hosted 2 Preview** link (Overview → Ad Hoc Processing → Preview URL). Client tests URLs and sends revisions; paste the URL without formatting. (Recipient list in the OneGuide — not stored here.)
- **Flyer Review type: Lite.**

---
*Source: West Marine OneGuide (Google Doc `17d0VAnHfcg1C6HTpPOIEFU_ERCfSG1-i-PwoHhaRApU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Westlake Ace Hardware / WL Ace Hardware — Processing Guide

> **Source:** Westlake Ace Hardware OneGuide (Google Doc `155UmcVbOSyiD_Ng4CcuzDGVyQgGccTipCPr5INSVM7Y`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#westlakeace`, `#westlakeace_nativex` |
| Flyer types | Circular, WL Ace Hardware Hosted, Dennis, Circular (Flyer Types 1–4) |
| Processing | Auto-stack; Flex = Flyer Review; OS = Setup; **Strategic Ops: yes** (Feedel); no coupons |

## Files & schedule

- **Files received:** Monday. Available Mon→Mon; Valid Tue→Tue. **No consumer preview.**

## Upload & setup

- When files arrive, open page 1 in the SFTP to check publication dates. Create a new flyer run in the **Circular** flyer type; Valid/Available dates = what's on the publication.
- **Manual upload** all SFTP pages; build a pricing zone **based on the file name** — the location abbreviation sits between the first `_` and `_Final` (e.g. `2241001ml_fn_final_p0005.pdf` → **FN** pricing zone). Confirm all pages uploaded.
- Standard 4 thumbnails; confirm dates match; complete Setup QC checklist.

### Pricing-zone store distribution (from the XLS)

- SFTP → search XLS → open the XLS matching the file name.
- Delete rows down to and including the "Store #" row; delete "Store location", "Store brand", "Ad Market" columns.
- Format column A → Numbers → **Generic** (removes leading zeros). Insert a header row: column A = `stores`, column B = `pricing zone` (lowercase, no quotes).
- **Find-and-replace the pricing-zone name so it EXACTLY matches the flyer-run PZ naming (CA, Core, Dennis, etc.) — otherwise stores will not be assigned.**
- Download as CSV → Codesheet tab → upload with **config `generic_stores`**, PDF base directory `/`, **toggles 1 and 6 only**.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Include **social media**; exclude coupons, packaged deals, retailer logo, sign-up page, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include name, pre/postfix, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude valid dates, SKU.
- **Image QC:** clean white PDF where possible, otherwise cutout. Generate images if none appear, untoggle "data pipped" + "PDF images" and re-check.

## FQC / out-of-processing

- Category QC (DOC): Google category on all items. Ad-hoc: file dates = flyer-run dates (flag mismatch to full-time processor); external run name = publication name on page 1.
- **Out-of-processing — clone 3×:** after FQC, clone the run for **CA FLIPP, CA HOSTED, and Dennis**. For each: verify image QC/thumbnail/category copied; open the PZs NOT being distributed to and remove all stores; re-run the store-distribution XLS + `generic_stores` codesheet; complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Westlake Ace Hardware OneGuide (Google Doc `155UmcVbOSyiD_Ng4CcuzDGVyQgGccTipCPr5INSVM7Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wholehealth Pharmacy — Processing Guide

> **Source:** Wholehealth Pharmacy OneGuide (Google Doc `1mS4U7QJS8aPiD2Bk81zz_eVMKulMvmSqwfV5GauRR_4`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1plat_wholehealth`, `#flex-processingsupport`, `#onboardings` |
| Flyer type(s) & cadence | Weekly — **Ad hoc / monthly** |
| Processing | Auto-stack; Flex = Processing Support; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad hoc; publication cadence **monthly**.
- **Linking document: Yes.** Pages may need to be added to the SFTP by the processor if the client emails files.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages → Edit → select SFTP pages (or upload from email) → Confirm & Upload → auto-group / add page numbers → set language **English** → Save & Confirm.
- Create a **Base** pricing zone, select all pages, add all stores.
- Setup QC: confirm all pages uploaded; **ensure the linking doc is attached to all vendor tasks** (ask the processor if not on ClickUp); confirm flyer dates; Standard 4 thumbnails.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each product block with a price/sale story.
- **Tag / Tag QC — Low; Auto-tag OFF, Brand = No.** Include name, pre/postfix, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Exclude valid dates.

## FQC (owned by Flex)

- **Check URLs:** open the linking doc on the vendor tasks, review every link on each page, then comment "**All links checked**". Also handle items without URLs.
- No theme; spot checks if required; Standard 4 thumbnails (stock premium, storefront carousel premium/organic); category QC (all items have a category).
- **Image QC — do NOT do.** Check pages for missed boxes. Complete FQC checklist.
- **Flyer Review type: Lite.** No special risk items — use generic flyer-review standards.

---
*Source: Wholehealth Pharmacy OneGuide (Google Doc `1mS4U7QJS8aPiD2Bk81zz_eVMKulMvmSqwfV5GauRR_4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wholesale Club (RCWC C&C) — Processing Guide

> **Source:** Wholesale Club (RCWC C&C) OneGuide (Google Doc `1xBi5CeEDQgmzNNbiXOYdH-R85t5j8vgg8BxFKmrJM4g`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer type(s) | Weekly (5994) + Vendor Book/Club Saving (VBT/CSF), Wine Day, Customer Day |
| Processing | Auto-stack; Flex = Flyer Review + Weekly upload; OS = Setup; **Strategic Ops: yes** (Feedel); no coupons |
| Cadence | Files Monday; Available Wed→Wed (1-day preview); Valid Thu→Wed; Sunday preview start |

## Upload & setup

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were already added, flag to the full-time Ops stakeholder and continue.

- **There is NO codesheet** for Vendor Book / Wine Day / Extra / Customer Day publications — **the processor completes those uploads, not Flex.** Manual upload: Pages → Edit → find the vendor-book folder (may be CSF / VENDOR BOOK etc.); upload ATL, ONT, WEST, QUE folders (**QUE files = FRENCH**); create pricing zones **ATL, ONT, WEST, QUE, QUE ENG**; add the store set; thumbnail; no theme unless applicable.
- **Weekly Flyer — Flex completes the upload**, but the processor must add the codesheet to the shared Google Drive by **EOD Thursday** before the Friday shift. If Flex doesn't: ensure Pixel 4096, open the codesheet, manual-upload pages, create a pricing zone per codesheet tab, assign stores per the codesheet.
- Setup QC: Available Wed→Wed (1-day preview), Valid Thu→Wed; **Sunday preview start** (Edit Details → Preview start date = Sunday before available); external run name "Weekly Flyer Valid Thursday, Month date - Wednesday, Month date"; no theme; mark off Auto Spotcheck.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot ON.** Include coupons, packaged deals, special weblinks; exclude retailer logo, sign-up page, social media. Box around the full item + price.
- **Tag / Tag QC — Low; Auto-tag OFF.** Linking doc required (Tag/QC specific). Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, **Coupon, Article Number**. No spreadsheet required.
  - **Name in ALL CAPS** (appears bold); product size after name using a comma.
  - **SKU:** enter the flyer SKU in SKU **and Article Number**; only use a SKU that **starts with "2"**; include the unit of measure (`_EA`, `_KG`, `_CS12`); one SKU only if multiple.
  - **Article Number** field (bottom of tagging interface): copy the SKU in with UoM; multiple SKUs → Article Number 1/2/3/4 in order.
  - **URLs:** after SKU entered, click **Fetch**. If the link goes to a different item/size → remove and search wholesaleclub.ca by product name; if it goes to a different flavour (same item) → leave; if it goes to the WSC home page → leave. Items with no SKU → find URL on wholesaleclub.ca.
  - **Sale Story:** "Optimum" offers tagged as **PC Optimum**; all $/%-off tagged in sale story (and in dollars-off/percent-off). Disclaimer: "limit"/"price after limit" callouts.
  - **Coupons:** Display Type = COUPON; draw all three barcodes.
- **Image QC:** clearest PDF; avoid black around the product; cutout only if no clean PDF.
- **Page categories:** every page except page 1s — min 1, max 3.

## FQC / pre-FQC tasks

- **CSF/Vendor Book:** mark off auto-stack + ops spot check; upload revised pages; build **Burnaby (store 6725)** and **Quebec City (store 8243)** into their own pricing zones (Burnaby, Quebec City Fr, Quebec City CL) — these two stores get unique **7-day FLASH OFFER flaps** to be posted only while valid and swapped weekly; set page removal/insert triggers by flap valid date; merge flaps (storefront spot check). Thumbnails Standard 4, start at logo, do NOT include flap pages.
- URL check: item search SKU IS NOT blank + URL IS blank → open + Fetch. Article Number check: Article Number 1 blank + URL not blank → add article number (also in SKU + part of URL).
- **Weekly:** pagination + store QC against the (revised) codesheet; URL/SKU/Article Number QC; check vertical + horizontal scroll; link QC from codesheet; swap in any revised SFTP pages before go-live.
- **Live-date risk items:** URL leading to a different item → **FLAG**; item quantities in the description → **FLAG**; Article Number field usage (see above).
- **Flyer Review type: Lite.**

---
*Source: Wholesale Club (RCWC C&C) OneGuide (Google Doc `1xBi5CeEDQgmzNNbiXOYdH-R85t5j8vgg8BxFKmrJM4g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wild By Nature — Processing Guide

> **Source:** Wild By Nature OneGuide (Google Doc `1rEV_01XUc3gdVtMpf9l9lvaKo15zysl57FfaYK-fI4o`), updated Apr 29, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` |
| Hosted URL | wildbynature.com/circular/ |
| Flyer type(s) & cadence | Circular (3073) — Weekly |
| Processing | Auto-stack; Flex = Flyer Review; OS = Setup; no coupons; no Feedel |

## Files & schedule

- **Files received:** Wednesday. Available Fri; Valid Thu. **No preview, no linking document.**
- **OS does the upload.** Check the FTP on Wednesday for the correct files (check valid dates). Fill the Vendor Setup tracker (Wednesday tab, by 3:30 PM) with the Flyer Run ID and whether files are ready; `#vendor-setup-retailers` does EOD callouts.

## Upload & setup

- **Manual upload** (files on FTP, ~10-day lead time): Pages → Edit → select files → autogroup → Save & Complete. Wait for "Flyer Creation" in the pipeline, then Start Task.
- Create pricing zone: Description **Base**, Language **EN**. In the Pricing Zones tab assign stores: **Add All (5 stores)**.
- Setup QC: **Legibility heights 40/30**; Standard 4 thumbnails (Thumbnail_1065 2pg, Stock Premium 1pg, Storefront Carousel Premium 2pg, Storefront Carousel Organic 1pg).

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Include packaged deals; exclude coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs** (N/A). Enter brand into brand field even if it repeats in name; include size/volume in description; if the page has a **Wild Card Savings** banner, note "wild card savings" in Sale Story.
- **Image QC:** clean images only; PDF preferred; cutouts allowed if PDF is not clean (shadows, cut-off).

## FQC (owned by DOC/Flex)

- Mark Auto-Stack check complete. Confirm available/valid dates match the flyer; **no external run name; no theme; available everywhere.**
- **Legibility heights 50/45** (note: differs from the 40/30 set at setup). Standard 4 thumbnails. Item Image QC (clean PDFs where possible). Mark items **In-Store Only**.
- Open all pages to confirm everything boxed/tagged; check vertical + full-screen preview for both PZs (items clickable, boxes appear); re-run sessions if needed; **geography must be unchanged** (no stores/FSAs added or removed).
- **Flyer Review type: Lite.**

---
*Source: Wild By Nature OneGuide (Google Doc `1rEV_01XUc3gdVtMpf9l9lvaKo15zysl57FfaYK-fI4o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wild Fork — Processing Guide

> **Source:** Wild Fork Foods OneGuide (Google Doc `16J3HKMaMABoy5qhkdchtfqCwtXVc4wPL-Yi6Cmln8vU`), updated Aug 1, 2024. Contacts/credentials omitted.

> This guide covers **Wild Fork (Canada)**. Wild Fork USA is a separate OneGuide.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | **Flipp only** (not on hosted) |
| Slack channels | `#wildforkfoods`, `#flex-processingsupport` |
| Flyer type(s) & cadence | Weekly (10977) |
| Processing | Auto-stack; Flex = Processing Support; no coupons; no Feedel |
| Linking document | Yes — URLs |

## Files & schedule

- **Files received:** Monday (PDF pages + URL doc via email). Available Thu; Valid Wed→Wed.
- **Custom action:** Assign FSAs from CSV — post-FQC and after any page swap.

## Upload & setup (owned by Vendor)

1. Download PDF + URL doc; split the PDF into individual pages (ilovepdf), download the zip.
2. Manual upload: **Pages → Edit → Upload Local Files** → select the pages; index pages in order (page 1 & 2); **language English only**; Save + Save & Complete.
3. Create a **Base** pricing zone for all pages; **(new Nov 2024) add three stores**.
4. Once sessions run, **attach the URL document as a mass attachment to all vendor tasks**.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Include special weblinks; exclude coupons, packaged deals, retailer logo, sign-up page, social media. Box each item individually; box the **Shop Your Way CTAs** on the bottom of the last page (usually page 3).
- **Tag / Tag QC — Low; Auto-tag OFF, Brand = No.** Include name, description, price, sale story, categories, **URLs**. Exclude pre/postfix, valid dates, SKU, disclaimer, original price. Include the small text above the bold title in the title; all items get a URL from the attached spreadsheet (search by item name).
- **Image QC:** clean PDF where possible, otherwise cutout.

## FQC (owned by Flex)

- **URL/Links QC:** check all items have a URL; add missing ones from the linking doc. Verify the **Shop Your Way** section on the last page is boxed with links (display type: Link) — Shop in Store / Order Online / Shop Online links are listed in the OneGuide.
- **Assign FSA from CSV:** copy the Base pricing-zone ID (Pricing Zone tab), paste into the `flyer_id` column of the FSA template (same ID for all rows), save as CSV, then Custom Actions → "Assign FSAs from CSV" → enter flyer-run ID + upload CSV → Run.
- Standard 4 thumbnails; **not available on hosted**; complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Wild Fork Foods OneGuide (Google Doc `16J3HKMaMABoy5qhkdchtfqCwtXVc4wPL-Yi6Cmln8vU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Willow Park Wines & Spirits — Processing Guide

> **Source:** Willow Park Wines & Spirits OneGuide (Google Doc `1FnbT6eTep7iz2cdsc2q8H7lDXukG4koxwyi9Q0IHCKc`), updated May 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` (+ retailer channel) |
| Flyer type(s) & cadence | Weekly (11840) |
| Processing | Auto-stack; Flex = Processing Support + Flyer Review; no coupons; no Feedel |
| Linking document | Yes — URLs |

## Files & schedule

- **Files received:** Thursday. Available Wed; Valid Tue. **Preview: Friday.**

## Upload & setup (owned by Flex)

Pages are uploaded in **two tracks** and **four pricing zones** (Saskatoon/Regina and Edmonton/Calgary):

- **Track 1:** Pages → Edit → select Saskatoon/Regina pages from the SFTP → Confirm & Upload → auto-group / add page numbers (correct language) → Save & Confirm (**do NOT process internally**). Create **Saskatoon** and **Regina** pricing zones (select applicable pages).
- **Track 2:** repeat for the remaining Edmonton/Calgary pages. Create **Calgary** and **Edmonton** pricing zones.
- **URLs:** product URLs are sent via SFTP — **one product URL for all products per pricing zone** (sometimes per region SK/AB); sometimes event URLs. **Attach URLs to vendor tasks.**
- Setup QC: confirm all SFTP pages uploaded; confirm flyer dates; Standard 4 thumbnails; preview dates set.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Standard tagging rules apply. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude SKU. **Links are in the task comment boxes** (no separate linking doc for tagging).
- **Image QC:** PDF preferred if clean; cutouts accepted otherwise.

## FQC (owned by DOC)

- Pre-FQC: dates correct per PDF; availability toggles correct; thumbnails include the retailer logo; all items boxed/tagged; spot checks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Willow Park Wines & Spirits OneGuide (Google Doc `1FnbT6eTep7iz2cdsc2q8H7lDXukG4koxwyi9Q0IHCKc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wine & Beyond — Processing Guide

> **Source:** Wine & Beyond OneGuide (Google Doc `1PsDjXvhwUBB4IA9898G-vUkW1JklkJkEg08olZd98Tg`), updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#wineandbeyond-new`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer (3261) — Weekly |
| Processing | Auto-stack; Flex = Processing Support + Flyer Review; no coupons; no Feedel |
| Linking document | N/A |

## Files & schedule

- **Files received:** Thursday. Available Wed; Valid Tue. **Preview: Friday.**

## Upload & setup (owned by Flex)

- Pages may need to be added to the SFTP by the processor if the client emails files.
- **Manual upload:** Pages → Edit → select all SFTP pages → Confirm & Upload → auto-group / add page numbers (correct language) → Save & Confirm (**do NOT process internally**).
- Create a **Base** pricing zone, select all pages, add all applicable stores.
- Setup QC: confirm all SFTP pages uploaded; confirm flyer dates; Standard 4 thumbnails; preview dates set.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; cutouts accepted otherwise.

## FQC (owned by DOC)

- Pre-FQC: dates correct per PDF; availability toggles correct; thumbnails include the retailer logo; all items boxed/tagged; spot checks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Wine & Beyond OneGuide (Google Doc `1PsDjXvhwUBB4IA9898G-vUkW1JklkJkEg08olZd98Tg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Wine Rack — Processing Guide

> **Source:** Wine Rack OneGuide (Google Doc `1qAUntAMFBTiF5dOQ4cbncYZyE6PqD0Ro9y2J6Ye4oHA`), updated Jun 14, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 5 Standard |
| Availability | **Flipp only** (not on hosted) |
| Slack channel(s) | `#winerack` |
| Flyer type(s) & cadence | **Ad hoc** |
| Processing | Auto-stack; Flex = N/A; OS = N/A; no coupons; no Feedel |
| Linking document | Yes — URLs only |

## Files & schedule

- **Files received:** Ad hoc (all dates ad hoc). Owned end-to-end by **DOC** (Upload & Setup → FQC).

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client emails files.
- **Manual upload:** Pages → Edit → select all SFTP pages → Confirm & Upload → auto-group / add page numbers (correct language) → Save & Confirm (**do NOT process internally**).
- Create a **Base** pricing zone, select all pages, add all stores.
- Setup QC: confirm all SFTP pages uploaded; confirm flyer dates; Standard 4 thumbnails; preview dates set.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude SKU.
- **Image QC:** PDF preferred if clean; cutouts accepted otherwise.

## ⚠️ Common errors / live-date notes

- **Missing on Hosted:** items may be flagged as "Missing" on hosted — **do NOT mark as missing** (Wine Rack is Flipp-only).

## FQC (owned by DOC)

- Pre-FQC: dates correct per PDF; availability toggles correct; thumbnails include the retailer logo; all items boxed/tagged; spot checks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Wine Rack OneGuide (Google Doc `1qAUntAMFBTiF5dOQ4cbncYZyE6PqD0Ro9y2J6Ye4oHA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Winn-Dixie — Processing Guide

> **Source:** Winn-Dixie OneGuide (Google Doc `10egXq3eXv6XOcZAGhu3z5IhxGtsS9GJlxyPVU8Jf8-w`), updated Mar 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard (SEG / Southeastern Grocers) |
| Availability | All platforms |
| Slack channel(s) | `#segrocers` |
| Flyer types | **Weekly Circular** (3099), **Bi-Weekly In-Store (ISPO)** (3285), **Monthly Liquor (LIQ)** (3284) |
| Processing | Auto-stack; no coupons; no Feedel |
| Account resources | Winn-Dixie Processing Notes; SEG x Flipp Ops Guidelines (in the OneGuide) |

## Files & schedule

- **Weekly Circular:** files Monday; Available Wed→Wed; Valid Tue→Tue; **1-day preview** (Tuesday) with **staggered pricing zones** (some get a 7-day preview).
- **Bi-Weekly ISPO:** files Friday; Available Wed→Wed; Valid Tue→Tue; **no preview** (available = valid).
- **Monthly Liquor:** files Friday; Available Mon→Mon; Valid Sun→Sun; **no preview**.

## Upload & setup — two-codesheet pattern (all flyer types)

When files drop, search the FTP for `.xlsx` — two codesheets appear:
- **Version List / "Versions"** = store information.
- **Manifest** = pricing zone + page order info (and preview/valid dates — **flag if they don't match the run**).

**Order matters — upload the Version List first, then the Manifest.**

1. **Version List:** delete the extra tab; ensure store info is in **Column C** and **rename the header to "Stores"** (weekly deletes the 'Addresses' tab; ISPO deletes the 'QUAD…ISPO' tab; liquor deletes the "LIQUOR STORE #" column and renames "REGULAR STORE #" tab). **If this manipulation isn't made, the codesheet will NOT work.** Save as CSV.
2. Upload the Version List codesheet: **Name `Stores`, config `seg_stores`**, base path from the FTP, **all toggles except 2**. Save — **do NOT press "Process Codesheet."**
3. **Manifest:** no manipulation for weekly/ISPO (liquor only: delete store columns A/B if present). Save as CSV.
4. Upload the Manifest codesheet: **Name `pages`, config `seg`**, base path, **all toggles except 2 and 7**. Save.
5. **Only hit Process on the Manifest codesheet** (never the Version List). Wait for green, then mark "Flyer Creation" complete.

**Base-path identifiers:** Weekly = `WK XX` in path; ISPO always has **ISPO** in file names; Liquor always has **LIQ**. Liquor "FL LIQ" = all stores → "MONTH LIQ" run; "WDs 115 Liq" = **store 115 only** → "MONTH LIQ 115" run.

**Weekly staggered dates:** the run's Available From = 7-day preview. Cross-reference the Manifest (zones highlighted **green** = 1-day preview), select those zones in Edit Dates/Details → "Apply Dates to Selected Flyers" → set Available From to the one-day preview date. Leave a comment "staggered dates have been set."

- Setup QC: confirm all pages uploaded; confirm valid + preview dates; Standard 4 thumbnails; geography — if stores missing, search the Version List (not present → correctly excluded; present → manually add to its pricing zone).

## QC specifics (similar across flyer types)

- **Box Draw — Low.** Weekly: **Auto-Box ON**; ISPO & Liquor: **Auto-Box OFF**; Box QC bot OFF for all. **Include coupons + packaged deals; exclude retailer logo, sign-up, social media, special weblinks.**
  - One box for "Buy This Get These Free" and "Pick Any 5 for 5" (one price = one box). Box vaccine banners. Two products but one picture → box as ONE (second item in description).
  - **DO NOT box retailer logo or rewards banners.** Watch for boxes showing the wrong item's picture.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **URLs = Exclude — THERE IS NO URL LINKING; do NOT box/tag any banners or pages with URLs.**
  - **Name** as on flyer; two bold names → both in name field; one bold + one not → bold in name, rest in description; no price/deal → tagline in name.
  - **Prefix** = text before current price; when there's sale-story info but no current price, put the sale story (e.g. "Buy 1 Get 1 FREE") in **Prefix**, and "save $$ on ## with card" in **Sale Story**.
  - Multi-brand → select "Multi Item?" and separate brands with `|`.
  - **Two prices:** use the LOWEST in current price; put "Buy 1 $x.xx ea." in description. Digital coupon callouts → tag the discounted price.
  - **Discount $/% :** if sale story says "Save up to $$" leave the discount field blank.
  - **⚠️ "2 for the price of 1" ≠ "2 for $1":** no `$` before the "1" means the "1" does NOT go in the price field.
  - **Categories:** required (merchant receives analytics) — **one category only**; use the section banner header; **FLAG, don't guess** if unsure. Coupons → Display Type COUPON, name = sale story, valid dates, category "coupon".
- **Image QC:** always select a clean PDF if available; cutout only if none.

## FQC (owned by Flex — same for all flyer types)

**Retailer-flagged risk items: (1) Sale Story, (2) Staggered Pricing Zone, (3) Item-Level Valid Dates.**

- **Sale Story check:** item search Sale Story IS NOT blank — verify BOGO/sale numbers match the flyer.
- **Staggered PZ dates (WEEKLY only):** if the comment box mentions staggered PZ dates, **DO NOT EDIT.** WD normally has 1–2 zones with a week-early preview, the rest a 1-day preview (per Manifest). Only if ALL zones share the run's available date: Edit Dates → select all, deselect the correct ones, multi-edit per that week's Manifest, or flag to the processor.
- **Item-level valid dates:** look through pricing-zone pages — weekend-sale banners on page 1s, unique valid-date items on pages 3–6, "PRICE HOLD" pages.
- **Switch & Save pages:** ensure they're boxed/tagged (vendors often skip them — no prices, only sale stories); can copy boxes from Harveys or Fresco y Más of the same week, else box/tag in house.
- Category QC (one per item), Item Image QC (PDF if available), page categories (use flyer headings). Standard thumbnails; **Legibility heights 35,25**; no theme; available everywhere.
- **Dates:** Weekly = 1-day preview; Bi-Weekly = no preview (Wed→Tue); Liquor = no preview (Mon→Sun).
- **Flyer sorting:** weekly flyers first (by date), LIQ in the middle, ISPO/bi-weekly last.
- **Flyer Review type: Lite.**

---
*Source: Winn-Dixie OneGuide (Google Doc `10egXq3eXv6XOcZAGhu3z5IhxGtsS9GJlxyPVU8Jf8-w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Woodcraft Supply — Processing Guide

> **Source:** Woodcraft Supply OneGuide (Google Doc `1mvex_-6CDcr-w5-DcFuWXVN2kM8LbzTabgpIC-94nfg`), updated Jul 22, 2024. Contacts/credentials omitted.

> **Note:** This OneGuide is a light/simple-retailer guide — most sections use generic defaults with little retailer-specific detail.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Flyer type / cadence | Direct — **monthly** |
| Processing | Auto-stack; Flex (Processing Support) upload & FQC; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** monthly.
- **Publication cadence:** monthly.
- **Preview / linking document:** N/A.

## Upload & setup (owned by Flex)

- Files are uploaded to the SFTP.
- Set up as **1 zone, English, containing all pages, assigned to all stores.**
- Confirm all items in the Setup QC checklist are correct.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- No linking document. **Exclude everything:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC (Low; Auto-tag OFF)
- No linking document. **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.

### Image QC
- Not specified in the OneGuide.

## Final QC / go-live notes
- Standard FQC items (owned by DOC).
- **Flyer Review type: Lite** — no special risk items; use generic flyer review standards.

---
*Source: Woodcraft Supply OneGuide (Google Doc `1mvex_-6CDcr-w5-DcFuWXVN2kM8LbzTabgpIC-94nfg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Woodmans Food Market — Processing Guide

> **Source:** Woodmans Food Market OneGuide (Google Doc `1-h50Q0j7laZa4OPEDzHaEpAEKZQBRbLadoHHvqeKf-4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Standard |
| Availability | **Flipp only** |
| Merchant ID | 2893 (config `m1000`) |
| Flyer type / cadence | Weekly |
| Processing | Auto-stack; **M1000** (auto-processed); DOC upload/FQC; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Thursday, Valid From Thursday; Available To Wednesday, Valid To Wednesday (Thu–Wed).
- Upload and FQC happen on the **live date** (M1000 retailer, processed post-live-dates).

## Upload & setup

> **Only upload the codesheet if the codesheet processed with errors / did not process.** As an M1000 account it normally auto-processes.

- Create the flyer shell for Thu–Wed, available everywhere.
- Check the codesheet for errors and troubleshoot **before** uploading.
- **Codesheet upload:** Name = `Codesheet`; **Config `m1000`**; PDF Base Directory = `/` (FTP folder where the codesheet was located); **check boxes 1, 3, 4, 5, 6**; Save Code Sheet → Process Code Sheet.
- Mark Flyer Creation and Setup QC as complete.
- Sessions should all run completely; once Setup, Autobox, Autotag and Autopublish are done, FQC can begin.

### ⚠️ Common errors (retailer-specific)
- Because it auto-processes, only touch the codesheet if it errored or didn't process.
- In FQC, mark the **error as `m1000`**.

## QC specifics

- **Box Draw:** box each item. (Auto-box handles this as an M1000 account.)
- Tag / Image QC: not detailed in the OneGuide (auto-processed).

## Final QC / go-live notes (owned by Flex)
- Mark thumbnails complete (nothing to change).
- **Republish the flyer** on the overview page.
- Confirm the flyer published on the Pricing Zones tab.
- Go to FQC checklist and mark **error as `m1000`**.
- **Flyer Review:** Woodmans is an M1000 retailer processed post-live — it rarely (if ever) shows on the Flyer Review panel and goes live without review.

---
*Source: Woodmans Food Market OneGuide (Google Doc `1-h50Q0j7laZa4OPEDzHaEpAEKZQBRbLadoHHvqeKf-4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
