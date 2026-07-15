# Retailer Processing Guides — V

> Bundle of 13 retailer-specific processing guides (V). Contacts and credentials are omitted from every guide.

**Contains:** Vallarta Supermarkets, Valley Feeds, Valley Marketplace, VALU-MART, Value Drug Mart, Value Grocer, VG's Grocery, Vie En Vert, Vince's Market, Visions Electronics, Vistek, Vita Health Fresh Market, Vogue Optical


---

# Vallarta Supermarkets — Processing Guide

> **Source:** Vallarta Supermarkets OneGuide (Google Doc `1caY_nXaCSQhnDrDr53KK_TfjAZrtMyFzWemdp94i-RQ`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#vallartasupermarkets` |
| Hosted URL | https://vallartasupermarkets.com/en/weekly-specials/ |
| Flyer types | **Weekly Flyer** (pub 7955) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available From Wednesday · Valid From Wednesday · Available To Tuesday · Valid To Tuesday.
- **Preview date:** N/A. **Linking document:** N/A.
- **Workflow:** Upload & Setup (5 days out, Flex) → add to VAST for FQC (4 days out, DOC) → FQC (2 days out, Vendor) → Retailer Preview time-permitting (live date, DOC).

## Upload & setup

Two documented paths; the older codesheet-manipulation path is marked **OUTDATED – DO NOT USE**. Current process:

1. Download the codesheet from the FTP.
2. Run it through the account's Gemini gem ("Run Vallarta", select **Pro**) to produce the manipulated CSV.
3. Upload the codesheet to the flyer run:
   - Name: `codesheet`; Upload File: manipulated CSV from Gemini.
   - **Config Name: `generic`**.
   - PDF Base Directory: found in FTP (e.g. `/0422`).
   - **Check:** Store Assignment, Page Upload, Allow Pricing Zone Creation, Use Page Pool, Tile Generate Afterwards.
   - **Uncheck:** Region Assignment, Combine Zones.
   - Save & Process.
4. Confirm codesheet page names match the SFTP; pages tagged "common" are often named differently in the SFTP — flag missing pages proactively.

**Setup details:** Mark Flyer Creation complete. Overview → Edit Details: Available/Valid Wed→Tue, all platforms, **External Run Name = "Grocery Savings"**, No Theme. Thumbnail QC = Standard 4 (1065x600 ×2, Stock premium ×1, Storefront carousel premium ×2, Storefront carousel organic ×1). Confirm all sessions ran, then complete Setup QC.

### ⚠️ Common errors (retailer-specific)

- **Stores upload incorrectly / empty zones:** A PZ may be created with stores but no pages, or vice versa. Manually assign stores by PZ name — e.g. a PZ named `(43)(54)` needs stores V43 and V54 added manually.
- **"Files Match Multiple Files on the FTP" yellow warning:** OK to ignore. Close the warning, click **Force Processing**; sheet stays yellow but pages/PZs still upload. Add comment "Ok to ignore Codesheet warning."
- **"Store does not exist" warning — two causes:**
  - *Formatting:* remove spaces before the first store number and after the last, but keep the space after commas between store numbers.
  - *Grand opening (uncommunicated):* Vallarta usually does not announce new store openings. If a store code doesn't exist, delete that row and upload **without** it, then flag the grand opening. Once store info is confirmed, create the store in FAdmin (Merchant → Stores/Store Sets → Create new store; get lat/long from Google Maps). Create a **separate Grand Opening flyer run** (same dates; internal name "Grand Opening - DATE"; hide in Flipp & Distribution if <6 purchasable items; External Run Name "Grocery Savings"; no theme) and upload the new store only.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Include coupons, packaged deals, retailer logo, special weblinks. Exclude sign-up page, social media. Box each product with a price.

**Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand = Tag/QC-specific. **Exclude SKU and URLs** (URL: always box the retailer logo, Display type Link → vallartasupermarkets.com).
- **Name (bilingual):** Tag the large bold English name first; if small Spanish (red/green) text exists it **must** be included, separated by a forward slash ( / ). Multiple items in a box → tag the first item's name; add the rest to description.
- **Description:** all non-bold words/measurements; tag "Fresh" when shown; "from Mexico" and "Chiquita" when the corresponding badge appears.
- **Multi-buy pre/postfix:** watch for "### FOR $$$" and "### LBS. FOR $$$"; postfixes include LB., +CRV, "+CRV when you buy multiples of ### in a single transaction" (blue banner).
- **Disclaimer:** often in blue/yellow banners, e.g. "SINGLE PURCHASE $X.XX EACH" or "W/O COUPON $X.XX +CRV".
- **Valid dates:** watch for special sale dates in blue banners / "TWO DAY SALE" callouts; all items in the banner must get those valid from/to dates.

**Image QC:** PDFs must be clear with white background; lifestyle images are OK. **If more than one product in a box, select "do not use PDF image" — even if the products are identical.** Watch for cut-off / non-white-background images.

## FQC / go-live

- Mark Auto-Stack complete; Pages tab Tagged & Tag QC all green; first page of every version is always empty (add categories as needed); check PZ dates + vertical scroll; confirm special item dates.
- Edit Details as above (Available=Valid dates, all platforms, External Run Name "Grocery Savings", no theme, no preview date).
- OK to ignore "Show Unassigned Stores" warning; if PZs lack stores/FSAs, compare to this week's codesheet and add missing stores.
- Sessions: "Mark items in store only"; verify URLs. Run FQC checklist (dates, pages, external run name, valid-date items, leg heights, categories). OK to ignore Other Errors/Warnings (e.g. "Store # not assigned", "not all categories have thumbnails").
- **Preview (Flex):** Monday, only if files were received the prior Monday.
- **Flyer Review type: Lite.**
- **Out-of-processing:** standard baseline page swap.

---
*Source: Vallarta Supermarkets OneGuide (Google Doc `1caY_nXaCSQhnDrDr53KK_TfjAZrtMyFzWemdp94i-RQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Valley Feeds — Processing Guide

> **Source:** Valley Feeds OneGuide (Google Doc `11qbuJ3lXnN6YQ7P5rhhR72Pgj9e6rSYtX03Q2P72NSo`), updated Sep 6, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | **Flyer** (pub 11829), ad-hoc |
| Processing | Auto-stack; DOC-owned; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Ad hoc.
- **Cadence:** Available/Valid From & To all ad hoc.
- **Preview date:** N/A. **Linking document:** YES (used for both Box and Tag).
- **Workflow:** Upload & Setup (5 days out) → FQC (1 day out), both DOC-owned.

## Upload & setup

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Note: pages may need to be added to the SFTP by the processor if the client sends files by email.
- Once pages are listed, **Auto-Group**, then Save & Confirm. **Do NOT Process Internally.**
- **Pricing Zone creation:** create a base pricing zone with all pages selected, Save & Confirm, add all stores.

### Setup QC
- Confirm all pages uploaded correctly (PZ Tab → Items View); if uploading from SFTP, confirm no SFTP pages were left un-uploaded.
- Confirm flyer dates (usually first or last page).
- Complete Thumbnails (4 Standard). Complete Setup QC checklist.

### ⚠️ Risk items (retailer-specific)

- **Ensure every item has a URL** — reference the linking document to add any missing links.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required — used for both Box/Tag):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

**Tag / Tag QC (Low; Auto-tag ON; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude SKU.**

**Spotchecks:** Standard pricing spotchecks included in pipeline.

## FQC / go-live

- **Pre-Final QC (DOC):** check items without a URL (should be none — use linking doc to fill); confirm dates vs PDF; confirm availability toggles; thumbnails correct and include retailer logo. Standard checks: all items boxed/tagged, spotchecks complete (20% of PZs), previews published & clickable, sessions completed, geography correct.
- **Flyer Review type: Lite** (DOL-owned): flyer dates, sessions completed, items w/o URL near 0, previews showing, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Valley Feeds OneGuide (Google Doc `11qbuJ3lXnN6YQ7P5rhhR72Pgj9e6rSYtX03Q2P72NSo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Valley Marketplace — Processing Guide

> **Source:** Valley Marketplace OneGuide (Google Doc `1aOA_W1iPnBS5ftbmkdYW3rvAXzEGKRZSQD-DYmR2OF8`), updated Jul 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified in doc) |
| Availability | All platforms |
| Slack channels | `#1p-valley-marketplace` |
| Hosted URL | N/A |
| Flyer types | **Flyer** (type 12315) |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From **Tuesday @ 11pm EST** · Valid From **Wednesday 12am EST** · Available To Tuesday · Valid To Wednesday.
- **Linking document:** No.
- **Workflow:** Upload & Setup (5+ days out, DOC) → FQC (1 day out, DOC).

## Upload & setup (Flex-owned)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload.
  - **NOTE:** Files may be dropped labeled with **Wednesday** (the original launch date). The retailer later changed to available Tuesday @ 11pm EST — so files labeled e.g. "the 18th" actually go live/valid on "the 17th."
- Auto-Group or manually enter grouping numbers. Ensure **English only** language is selected. Save & Confirm; **Do NOT Process Internally.**
- **Pricing Zone creation:** 1 BASE pricing zone; add all stores.

### Setup QC
- Confirm all pages uploaded (PZ Tab → Items View); confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (usually first or last page). Complete Thumbnails (4 Standard). Ensure preview dates set. Complete Setup QC checklist.

### ⚠️ Common errors (retailer-specific)

- **Timing is the #1 risk:** Available From **must** be Tuesday @ 11pm EST and Valid From **must** be Wednesday 12am EST — do not use the Wednesday date on the dropped files.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. One box around each item.

**Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand = No. **Exclude SKU and URLs.** Ensure item-level valid dates are applied to each item called out.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

**Spotchecks:** Standard pricing spotchecks in pipeline.

## FQC / go-live

- **Pre-Final QC (Flex):** ensure **Available time = 11pm EST Tuesday**; check pages for item-level valid-date callouts; confirm dates vs PDF (cover page); confirm availability toggles; thumbnails correct + include retailer logo. Standard checks: all items boxed/tagged, spotchecks 20% of PZs, previews published & clickable, sessions completed, geography correct.
- **Final QC checklist:** DOC-owned.
- **Flyer Review type: Lite** (DOL-owned).

---
*Source: Valley Marketplace OneGuide (Google Doc `1aOA_W1iPnBS5ftbmkdYW3rvAXzEGKRZSQD-DYmR2OF8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# VALU-MART — Processing Guide

> **Source:** VALU-MART OneGuide (Google Doc `1UZsT5i7Hdn5sdtCceYdtf05XVpPnwcy7-m8W-ubzym0`), updated Feb 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer types | Weekly; Monthly |
| Processing | **Trim Stack**; Flex (Processing Support); no coupons; **Yes — Feedel / Strategic Ops (retailer data services)** |

This is a Loblaws/LCL banner. Upload is normally completed by FTEs; full-time processors must place the codesheet into the tracker for the FTE to complete.

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday (1-day Sunday preview referenced in setup).
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → FQC (1 day out, DOC).

## Upload & setup

**Processor step (adds codesheet for FTE):** Find the final "wk # Maxi" codesheet in email and download it; add it to the Maxi folder in the Codesheet Drop Box drive; in the Flex LCL tracker toggle off F25 (codesheet dropped) and, once files arrive, E25 (files in SFTP).

**FTE upload:**
1. **NEW 2026 — Set Pixel Height to 4096 *before* any pages are uploaded.** Open flyer run → Edit Details → show rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were already added before this step, flag to the Full-Time Ops stakeholder and continue.
2. Retrieve **both** xls files for the week from the Valu-mart Codesheet Drop Box; the week number must match the flyer number in the tracker.
3. Use only specific tabs: **VM ICM CODE FINAL → "VM online" tab only**; **VM S CODE FINAL → "VM S Online" tab only**. Do **not** use any other tabs.
4. Manual upload: Pages → Edit → under "select files from FTP" expand the correct week folder → check the folder box to select all pages → Select Files. **Set the language toggle to French** for all Valu-mart pages. Save; re-check that toggles did not revert to English (re-apply French and repeat if they did), then Save & Confirm.
5. Flyer Creation → create **4 pricing zones** from the codesheets:
   - VM S (VM S tab, French language)
   - VM S (VM S tab, cross-language English pages)
   - VM (VM tab, French language)
   - VM (VM tab, cross-language English pages)
   - Add pages in the order of the codesheet "file codes" column.
6. Assign stores from store sets: **VM zones → VM store set; VMS zones → VMS store set.**
7. Edit Details: set **Preview start date = the Sunday before the available date**; **External Run Name = "Weekly Flyer Valid Thursday, [date] – Wednesday, [date]"**.
8. Geography shouldn't change — if it does, flag it in the 3FL Loblaws channel. Complete Setup QC (check in item view, ensure dates correct).

### ⚠️ Common errors (retailer-specific)

- **Pixel height must be 4096 before pages are uploaded** — doing it after requires flagging Full-Time Ops.
- **Wrong codesheet tabs:** only VM online / VM S Online tabs may be used.
- **Language reverts to English:** French toggle can revert after saving — re-verify before Save & Confirm.
- **Revised codesheets:** always check email for a revised codesheet after upload; if one exists, use it over the final.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Include retailer logo, sign-up page, social media, special weblinks. Exclude coupons, packaged deals. Draw a box only around the item (with its unique price / multi-item), not surrounding space. **Do not box PC Optimum promos or the retailer logo** (in the exclude examples).

**Tag / Tag QC (Low; Auto-tag OFF):** Include everything — name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand = Box Draw/Box QC specific.
- **Name:** ALL CAPS, format "Brand Product Name, Quantity" (always a comma before the quantity, e.g. "60g", "1 lb", "pkg of 24"); product name is the bold text. Bilingual pages: **only the French name in Name**, English in Description.
- **Description:** flyer info only (never from website); metrics like "6.59/kg", "Product of…", "No 1 Grade", "Frozen", "Selected varieties". No SKU in description.
- **SKU:** from text extraction (not visible on page), starts with "2"; drop leading zeros before the article number; keep unit suffix like `_KG`/`_EA` in both SKU and article-number fields; if multiple SKUs, enter only the first (before the comma).
- **URL:** every item with a SKU must have a URL — click **FETCH** to auto-generate.
- **Article Number:** same values as the SKUs, entered in the order shown; if more than 4 SKUs, enter only the first 4.

**Image QC:** correct = white background, no grey/shadow; incorrect = non-white background.

**Spotchecks:** standard pricing; reference Tag/Tag QC instructions.

## FQC / go-live

- **Pagination & store QC (DOC):** use the revised codesheet if one arrived post-upload; check pagination for each PZ and confirm assigned store #s match the codesheet.
- **URL/SKU/Article # QC (DOC):** item search "SKU IS NOT blank AND URL IS blank" → open item, Fetch. Then "Article Number 1 IS blank AND URL IS NOT blank" → add article number (also in SKU and part of URL).
- **Ad-hoc QC (Flex):** dates Available Wed→Wed (1-day preview), Valid Thu→Wed; External Run Name "Weekly Flyer Valid Thursday, [date] – Wednesday, [date]"; no theme; 4 standard thumbnails; check vertical & horizontal scroll (items clickable in full-screen preview); Link QC (any links in the codesheet must be on the flyer page); check SFTP for revised files and swap in rev pages before go-live.
- **Final QC (DOC):** after the checklist, on the flyer sorting page ensure the newest weekly flyer shows first.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** standard page swap.

---
*Source: VALU-MART OneGuide (Google Doc `1UZsT5i7Hdn5sdtCceYdtf05XVpPnwcy7-m8W-ubzym0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Value Drug Mart — Processing Guide

> **Source:** Value Drug Mart OneGuide (Google Doc `11YMUNZO32_emH3bkPtK85eL3GR7xDrDHXsXHXTs4H1U`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channel(s) | `#value-drug-mart`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | https://valuedrugmart.com/flyer/ |
| Flyer type(s) & cadence | Biweekly Flyer |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); Upload (Vendor) → FQC (DOC); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday · Available To Monday · Valid From Tuesday · Valid To Tuesday.
- **Linking document:** N/A.
- **Workflow:** Upload Wednesday/Thursday, FQC Wednesday, live Sunday.

## Upload & setup (Vendor)

1. Pages → Edit → "Select Files from FTP" → correct folder → upload all pages → Select Files. Auto-group to number the pages. Ensure all pages are **English**. Save & Complete.
2. **Pricing zone:** only one — name it **Base**. Save & Done.
3. **Stores:** in the Pricing Zone tab click the "0/0" Stores/FSAs button. Using the **Store Participation List**, add only stores marked **"1"** for the correct publication date (both Apple Drugs and Value Drug); skip any marked "0". Added stores must total the "TOTAL VALUE AND APPLE PARTICIPATION" cell.

### Setup QC checklist

- Overview → Normal Processing → Setup QC. Confirm dates; alerts should be only 2 (check them off); pricing zones and language correct; store count = TOTAL VALUE AND APPLE PARTICIPATION cell. Save & Done (only enabled once all sessions are complete).

### ⚠️ Common errors / risk items (retailer-specific)

- **Files sometimes won't upload from the FTP** — if this happens, download the files from CoreFTP and upload manually.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot ON):** uses Auto-Box — reference the box-draw instructions for Box QC. Linking document used for both box & tag. **Include** coupons, retailer logo, sign-up page, social media, special weblinks; **exclude** packaged deals. Box items with sale stories even without a price. Box social-media icons and the link banner across the top/bottom of the page.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF auto-select ON):** include pre/postfix, valid dates, description, price, original price, sale story, categories, disclaimer. **Exclude brand, name, SKU, URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## Pre-FQC / FQC

- Confirm dates vs. PDF and availability toggles. Thumbnails correct with retailer logo. Standard checks: all items boxed/tagged, spotchecks complete (20% of pricing zones), previews clickable, sessions completed, geography correct. Complete FQC checklist (DOC).

## Out-of-processing

- **Page swaps** follow the standard baseline process (owned by DOL).

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Value Drug Mart OneGuide (Google Doc `11YMUNZO32_emH3bkPtK85eL3GR7xDrDHXsXHXTs4H1U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Value Grocer — Processing Guide

> **Source:** Value Grocer OneGuide (Google Doc `12XR9ze2HbCXurCW0UPADkKUZ3EitYV4w_dA3WLbZfuY`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#powells-supermarket` |
| Hosted URL | (placeholder in doc) |
| Flyer types | **Weekly** |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available From Wednesday (12am) · Valid From Thursday (12am) · Available To Wednesday · Valid To Wednesday.
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → FQC (1 day out, DOC/Flex).

## Upload & setup (Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from SFTP (or upload from email if needed) → Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure **English** language. Save & Confirm.
- **Pricing Zone creation:** create a Base pricing zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC (Flex)
- Confirm all pages uploaded (PZ Tab → Items View); confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (first/last page). Complete Thumbnails (4 Standard). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item with a different price; items sharing the same price and item block are boxed together.

**Tag / Tag QC (Low; Auto-tag OFF):** Include name, pre/postfix, description, price, sale story, categories, disclaimer, original price. Brand = Box Draw/Box QC specific. **Exclude valid dates, SKU, URLs.**
- Name = bold text; brand as seen in flyer. Description = unbolded text after the name. Enter prices as seen (prefix, current, postfix, original).
- **Every item must have a category.** Category chart (Flipp category → items): Toys; Seasonal; Pharmacy; Pets; Outdoor Living; Home Essentials; Health & Beauty; Grocery; Grills; Gifts; Coupon; Beverages; Beer, Wine & Liquor.
- Select a PDF image for every item — cleanest/most relevant.

**Image QC:** Choose a clean white PDF where possible; otherwise a cutout.

## FQC / go-live

**Final QC checklist (Flex):**
1. Mark auto-stack off.
2. Edit Details / dates: **Available From 12am Wednesday, Available To 11:59pm Wednesday, Valid From 12am Thursday, Valid To 11:59pm Wednesday**; available everywhere; **no External Run Name; no theme.**
3. Page order noted in Comments. Image QC (clean PDFs where possible).
4. **Category QC — both analytical and Google category required for all items.** Overview → item search: "Categories is blank" then "Google Category is blank"; add any missing.
5. Draw 4 standard thumbnails if not done; check previews; check geography (no stores added/removed); complete FQC checklist.

- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** see the shared "Value Grocer & Powell's Supermarket — Publication & Ad-Hoc Requests 2025" guidelines.

---
*Source: Value Grocer OneGuide (Google Doc `12XR9ze2HbCXurCW0UPADkKUZ3EitYV4w_dA3WLbZfuY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# VG's Grocery — Processing Guide

> **Source:** VG's Grocery OneGuide (Google Doc `1ElT5M-uSzPKou36B8Cr1xjYf7NVe1Rty2QS1Th7yydU`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#spartannash`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | https://www.shopvgs.com/ |
| Flyer types | **Weekly** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

A SpartanNash banner (files dropped to FTP with an email notification for all SpartanNash banners).

## Files & schedule

- **Files received:** Monday (files + Posting Document dropped to FTP).
- **Cadence:** Available From Sunday · Valid From Sunday · Available To Saturday · Valid To Saturday.
- **Workflow:** Upload & Setup (5 days out, Flex) → FQC (1 day out, Vendor).

## Upload & setup (Vendor)

- Download the Posting Document to confirm page order; upload pages from FTP and order them accordingly.
- **Pricing Zone:** Base; add all **9 stores** (1920, 1921, 1922, 1925, 1927, 1929, 1930, 1932, 1934).
- Wait for sessions to run; ensure vendor tasks active. Confirm valid dates on first page are Sunday–Saturday.
- Edit Details: Available/Valid From-To Sunday→Saturday; available everywhere; no theme. Thumbnails (Standard 4). Complete Setup QC. **Clear FTP files (including the Posting Document).**

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Include coupons, packaged deals, special weblinks. Exclude retailer logo, sign-up page, social media. Box all items with prices/sale stories (use text boxes when needed); **box coupons with their respective item.**

**Tag / Tag QC (Low; Auto-tag OFF):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Brand = used for both Box/Tag. **Exclude SKU.**
- **Name:** include all items offered in the ad block.
- **Prices:** prefix from the approved drop-down. **For items with multiple prices, do NOT put the second price in the Original Price field** — put the "Sale Price" in Current Price and the "Coupon/Extra Savings" offer in the **Sale Story** field.
- **Sale Story:** tag everything in the blue box (Extra Savings, MFR Rebate Offer, Digital Coupon).
- **Valid dates:** watch for 2-Day / 3-Day sale banners and tag all items in the banner with those unique dates.
- **Categories:** every item needs one; **Baby → Health and Beauty; Pet → Grocery.**

**Image QC:** **Not using PDF images — use item cutouts ONLY.**

## FQC / go-live

- **Pre-Final QC (Vendor):** finish spotchecks; check for narrow pages in "Storefront Spotcheck" per PZ and merge to next page; mark Autostack Spotcheck complete. Image QC not required (no client specs). Review special days (3-Day Sales) — ensure unique valid dates applied. **OK to ignore FQC checklist warnings.**
- **Final QC (Vendor):** available one day before valid; check store tiles/thumbnails; sale story; spotchecks; Thumbnail QC (Standard 4); legibility heights; geography vs previous weeks; pages in correct order/region; toggles; all items tagged; dates match PDF; no "real" overview warnings.
- **Flyer Review type: Lite** (Flex-owned).

---
*Source: VG's Grocery OneGuide (Google Doc `1ElT5M-uSzPKou36B8Cr1xjYf7NVe1Rty2QS1Th7yydU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Vie En Vert — Processing Guide

> **Source:** Vie En Vert OneGuide (Google Doc `1jghN4t2OeIv8-V1WfASIdcWehaP5hN-C1UPTQs_FW7w`), updated Jun 12. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Basic |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A (hidden in Hosted) |
| Flyer types | **Flyer** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

Bilingual account (English + French).

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From Tuesday · Valid From Thursday · Available To Wednesday · Valid To Wednesday. **Available 2 days prior to valid date.**
- **Workflow:** Upload & Setup (4 days out, Flex) → FQC (1 day out, Flex).

## Upload & setup (Flex)

- **Manual upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload. **Set all pages to EN language.** Auto-Group or manually enter grouping numbers (ensure EN). Save & Confirm; **Do NOT Process Internally.**
- **Pricing Zone creation — 2 zones:**
  - **EN** = EN language = all pages.
  - **FR** = FR language, **cross-language from EN** = all pages (set to EN then "Save and Next" or rerun Flyer Creation to add the second zone).
  - Save & Confirm; add all stores to both zones.

### Setup QC (Flex)
- Confirm all pages uploaded (PZ Tab → Items View); confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (first/last page). Complete Thumbnails (4 Standard). **Hide in Hosted.** Available 2 days prior to valid date. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item individually.

**Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand = No. **Exclude SKU and URLs.**
- **Bilingual naming:** include both English and French names in the Title.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

**Spotchecks:** Standard pricing spotchecks in pipeline.

## FQC / go-live

- **Pre-Final QC (DOC):** confirm dates vs PDF (Available 2 days before valid); availability toggles correct (**Hide in Flipp Hosted**); thumbnails correct + include retailer logo; all items boxed/tagged; spotchecks 20% of PZs; previews published & clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** (Flex): available 1 day prior to valid; valid dates match PDF; toggles on Flipp & Distro only (hidden in hosted); pagination chronological; vertical preview interactive; all items tagged accurately; geography unchanged week over week.

---
*Source: Vie En Vert OneGuide (Google Doc `1jghN4t2OeIv8-V1WfASIdcWehaP5hN-C1UPTQs_FW7w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Vince's Market — Processing Guide

> **Source:** Vince's Market OneGuide (Google Doc `1svu5eWXZKb_gFtikqlOdAjlaTfcmaO3mOmGk3bK8cMQ`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Hosted only** |
| Slack channels | `#vincesmarket` |
| Hosted URL | (placeholder in doc) |
| Flyer types | **Weekly** (pub 3757) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup + FQC); no coupons; **Yes — Feedel / Strategic Ops** |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Tuesday · Valid From Tuesday · Available To Monday · Valid To Tuesday.
- **Workflow:** Upload & Setup (5 days out, Vendor) → FQC (1 day out, DOC).

## Upload & setup (Flex)

- **Manual upload:** FAdmin Pages Tab → Edit → upload from the corresponding FTP folder → Autogroup, do **not** process internally. Pricing Zone = Base; add all stores.
- **⚠️ Page order:** the delivered page order is **not** always the intended order. The client specifies the order by email. If it differs, the easiest fix is to rename pages to descriptions (e.g. Grocery/Dairy/Frozen, Meat/Seafood, CocaCola Ad) since that's how the client specifies order. This can be adjusted during Pre-FQC.

### Setup QC (Flex)
- Flyer Run Details: available everywhere; **Available Dates Thursday → Wednesday** (confirm actual dates from first page); Valid Dates same as Available unless stated; no External Run Name; no theme unless stated (Black Friday, Holiday, etc.). Thumbnails: Standard 4.

### ⚠️ Risk items (retailer-specific)

- **Naming:** ALL CAPS, exactly as in the flyer.
- **Descriptions:** watch for missing callouts; the required order is **(1) Red text first** (or RS/HS for the prepared-food section), **(2) green, (3) grey, (4) any weight description**. They are very particular — do this for EACH item on EACH page.
- **Images:** watch for shadows, and PDFs chosen for multi-item boxes.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude coupons.

**Tag / Tag QC (Low; Auto-tag OFF):** Include name, pre/postfix, valid dates, description, price, categories, disclaimer. Brand = Box Draw/Box QC specific. **Exclude SKU, Sale Story, Original Price, URLs.**
- **Name/Brand:** exactly as in flyer, ALL CAPS.
- **Description:** ordered Red (or RS/HS for prepared foods) → green → grey → weight. **Sale story (red text) goes into the Description field only**, as the first line.
- **Price/Original Price:** exactly as shown.
- **Disclaimer:** add to EVERY item: "Sale price not available at our Market & Co Location".
- **Pre/Postfix:** e.g. "170g" is not a postfix — leave postfix blank and put 170g in description; "Your choice" can stay as prefix. For prepared foods, the acronym goes first: "READY TO SERVE" or "HEAT & SERVE".

**Image QC:** avoid shadows / multi-item-box PDFs.

## FQC / go-live

- Mark Autostack Spotcheck complete; spotchecks if required; QC standard 4 thumbnails (stock premium, storefront carousel premium/organic).
- Edit Details: available everywhere; no external run name; run dates match the last page of the PDF.
- Check pages for unique item-level dates; check items without a URL; flag missing pages or geography changes to the full-time team.
- Complete FQC checklist.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** see the 2025 Publication & Ad-Hoc Requests guidelines; **NEW: linking YouTube channel** (youtube.com/@vincesmarketontario).

---
*Source: Vince's Market OneGuide (Google Doc `1svu5eWXZKb_gFtikqlOdAjlaTfcmaO3mOmGk3bK8cMQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Visions Electronics — Processing Guide

> **Source:** Visions Electronics OneGuide (Google Doc `1MUUF_49n2-vvt08zsg-4SBFK-TRpqE8CbXrDblVM10w`), updated Dec 1, 2025. Contacts/credentials omitted.
> **High box-draw complexity.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp & Distribution (**not hosted** — Flipp no longer powers Visions Hosted) |
| Slack channels | `#visions`, `#flex-processing support` |
| Hosted URL | http://www.visions.ca/eFlyer/default.aspx |
| Flyer types | **Weekly** (ID 7184), goes live every **Friday** |
| Processing | Auto-stack; Flex; DOC-owned; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Workflow:** Upload & Setup (5 business days out / Friday before, DOC) → Spotchecks & FQC + send retailer preview (2 days out / Wednesday, DOC) → FQC (1 day out, DOC) → Live (Friday).
- **Dates are NOT on the PDFs** — confirmed by the retailer in file-drop emails.
- **Linking document:** Yes (SKU/URL spreadsheet from FTP) — used for package items and banner (direct-link) tagging. Individual items generate links from the SKU.

## Upload & setup (Flex)

- Manual upload (normally **1 pricing zone — Base**, add all stores). Uploaded to flyer type "Flyer"; select the run with the correct live date (ad goes live every Friday). Pages → Edit → select the folder titled with the live date → select all pages → Select Files.
- **Versioning (less common since 2024):** if the retailer specifies different pricing zones by email, build PZs by page version — e.g. pages ending "AB" = Alberta version; "AOMKTS" = All Other Markets. Email the retailer to confirm discrepancies.
- **Sign-up page** is manually uploaded and placed in the **last position**.
- Download the links spreadsheet from FTP and attach to Tag and Links QC on the pipeline.
- **Setup QC:** confirm all pages uploaded (PZ Tab → Items View); confirm dates; complete 4 standard thumbnails; ensure preview dates set.

## QC specifics

### ⚠️ Box Draw (HIGH complexity; Auto-Box ON, Box QC bot OFF; linking doc required)
Include coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Box every item with a price separately.** If one product has multiple prices, put a **text box** around the lowest price and box the other prices separately as items. If two items share a product name but have different prices, box the prices separately.
- **Banners & links (specific URLs):**
  - Financing banners → link to `http://www.visions.ca/info/finance`.
  - **Sign-Up Page** (last page) → tag as "SHOW URL IN iFrame", URL `https://f.wishabi.net/arbitrary_files/36600/1474489548/36600_Flipp_Visions-Newsletter-Signup.html`, iFrame width 700, height 450.
  - "In-home Setup Solutions" MORE INFO → `http://www.visions.ca/content/homesetup/`.
  - Box promo banners (e.g. "Save up to 50% Off Car Install Labour") **separately** from the item — any promo not tied to the product gets its own box.
  - "Find a Store" button → link `https://www.visions.ca/storelocator/default.aspx`.
  - Rebate "Click Here to Download" banners → link to the rebate-form PDF URL provided.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required)
Include name, pre/postfix, valid dates, **SKU (copy from SKU/URL doc)**, price, categories, disclaimer, original price, **URLs**. Brand = No. **Exclude Description and Sale Story** (description typically blank).
- **Use the URL spreadsheet the DOC attaches** for item URLs and for Banner (Direct Link) names.
- If item dates differ from the run dates, put them in the item pop.
- Current Price = sale price; Original Price = before-sale; discount → designated field. Postfix e.g. "or $XX Monthly".
- **Do NOT include monthly-payment text** in name/description/disclaimer (e.g. "OR $XX.XX MIN. MONTH PMT").
- **Description usually left blank** — only used if no product page (URL) or a TV home-theatre package; never put descriptive subtext before the bold name; never put SKU in description.
- **SKU** = the advertised item's SKU (not the bonus item). TV SKUs: ensure only the TV size is in the SKU. One price with multiple SKUs → tag all SKUs.
- **Cell pages:** Prefix "As low as", Current Price 0, Postfix "Down", Sale Story "and $XX per month", Disclaimer "Full device price $X".
- **Category chart:** TV & Video; Home Audio & Accessories; Camcorders & Digital Cameras; Portable Electronics; Car Audio/Video; Cell Phones & Accessories; Furniture & Accessories (TV stands, media cabinets, massage chairs); Car Electronics & GPS; Smart Home Control & Automation (incl. security cameras); Computers; Laptops & Tablets; Appliances. (Security cameras → Smart Home, not Cameras; Car Audio not under Home Audio.)

### Image QC
Use **cutout images**. Select PDF image only if available and clean, and it must show the actual electronic (e.g. the TV itself, not the program on screen). **Packages/bundles → leave as a cutout** so all products show; never pick a PDF of one item in the package.

## FQC / go-live

- **URL/Links QC (DOC):** "Items without URL" on Overview; compare against the SKU doc; apply any missing URLs.
- **Item Category QC & Item Image QC (DOC).**
- **Final QC (Flex):** Geo, PZs (all stores), all pages tagged, QC thumbnails; Item Image QC; page categories 1–3 per page except page 1; check items without URLs vs linking doc.
- **[Optional] Preview QC (Flex):** spotlights & storefront sale story from front page; Image QC; full category QC; check toggles (all platforms); mark items store-only; **leg height 55/45**; thumbnail QC (custom tile from FTP); geography vs previous week. (Post-PQC clone to a "Buy Online" flyer type is noted as no longer needed.)
- **Post-FQC (DOC):** send preview by Wednesday / Thursday morning at latest; action items from the Visions Corrections Sheet before go-live.
- **Flyer Review type: Lite** (DOL): name from email; dates per PDF; **not available on hosted**; mark store-only; no special tile; one version all stores; email insert as last page; product links & category pages tagged.

### ⚠️ Live-date / PQC common errors
- Search-page results instead of item results.
- Individual item URL instead of the package URL.
- **Flipp no longer powers Visions Hosted — check live dates on flipp.com.**

---
*Source: Visions Electronics OneGuide (Google Doc `1MUUF_49n2-vvt08zsg-4SBFK-TRpqE8CbXrDblVM10w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Vistek — Processing Guide

> **Source:** Vistek OneGuide (Google Doc `1BUF97VUpf0wha4MiQIhF0vwhz-3isVbcdJRLlS78f6g`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (retailer channel not specified in doc) |
| Hosted URL | (placeholder in doc) |
| Flyer types | **Weekly**; Monthly |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday. Files should be uploaded 5 days before publication (may shift during holidays).
- **Cadence:** Available From Friday · Valid From Friday · Available To Friday · Valid To Friday. Preview date = 1 day before Available date.
- **Linking document:** Yes.
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → FQC (1 day out, DOC).

## Upload & setup (Vendor)

- **Flyer run setup:** Flyer type "Flyer" (ID 68) → Create New Flyer Run. Available/Valid dates from Page 1 or Vistek email. Preview Date = 1 day before Available. Distribution Categories = "Electronics" (High Relevance). External Preview Name only if merchant requests. Fully Promoted: Distribution, Hosted & Flipp.
- **Upload:** Pages → Edit → select all new pages → Select Files → Auto-Group → verify page order → Save and Complete.
- **Pricing Zone:** Pricing Zone tab → Stores/FSAs → select **ON & AB Region Set**.
- **Attach links** from FTP to the task notes in Tag and QC; ensure vendors assigned.

### ⚠️ Risk items (retailer-specific)

- **Box drawing:** box every individual item with the info on the flyer; boxes must be drawn cleanly.
- **Banners + Social Media:** box all Vistek logos and individual social logos (Facebook, Twitter) — see URL/linking doc for the links to insert.
- **Sale callouts:** ensure banners and sales callouts are boxed (indicated with corresponding links in the linking document).

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** Include packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude coupons. Box each item individually; box each retailer location, social media, and logo.

**Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** Include everything — name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand = Tag/QC specific.

**Image QC:** see the account image-QC video (Confluence).

## FQC / go-live

**Final QC (DOC):**
- **Ledge heights 25/20.** Spotchecks.
- Check links and items tagged correctly using the linking doc in the Vendors tab.
- **Add disclaimer** via Item Search (Name Contains Blank, Display Type Item): "E&OE. Quantities limited. Prices are effective [dates] unless otherwise stated or while stock lasts, for in-stock items only. Prices and savings claims subject to change based on vendor rebates…". **Before Multi-Edit, unselect items that already have an initial disclaimer** (e.g. "Lens sold separately") and add the extra disclaimer manually — otherwise the first disclaimer is erased.
- Overview → Item Image QC; Sessions → URL Verify; horizontal & vertical preview; Pipeline Final QC.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** standard baseline page swap (DOL-owned).

---
*Source: Vistek OneGuide (Google Doc `1BUF97VUpf0wha4MiQIhF0vwhz-3isVbcdJRLlS78f6g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Vita Health Fresh Market — Processing Guide

> **Source:** Vita Health Fresh Market OneGuide (Google Doc `1lQqO5wSc0wYAJsVce5f0IAtss2Xccb6ROBgCKpvNQQY`), updated Aug 1, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#vitahealth` |
| Hosted URL | https://myvita.ca |
| Flyer types | **Weekly** (pub 3432) |
| Processing | Auto-stack; Flex (3FL + Flyer Review); OS (Setup); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Friday · Valid From Thursday · Available To Thursday · Valid To Thursday.
- **Linking document:** **Yes — required.** Received via SFTP; nomenclature "Vita Health Fresh Market - Linking Doc [month]_[date]_[year].xlsx". **Do NOT proceed with upload if the linking document is unavailable** — request it from the retailer.
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → FQC (1 day out, DOC).

## Upload & setup (Vendor)

- Both PDF files and the linking document are received via FTP and both are needed for upload.
- **Manual upload:** select all files from the appropriate folder (file names should be lowercase) → Auto-Group → Save → Save and Complete.
  - **Note:** if there are both "tabloid" and "insert" pages, group manually — **insert pages follow tabloid pages.**
- Create one pricing zone (Base); assign all stores.
- **Attach the linking document to all vendor tasks.**

### Setup QC (Vendor)
- Draw standard 4 thumbnails (1065x600, Stock premium, Storefront carousel premium, Storefront carousel organic).
- Edit Details: available everywhere; no theme; no preview date.
- **Ensure the linking document is attached to all vendor tasks.** Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required — used for both Box/Tag):** Include special weblinks. Exclude coupons, packaged deals, retailer logo, sign-up page, social media. Watch single items vs. items with multiple sizes.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Brand = Tag/QC-specific. **Exclude SKU.**

**Image QC:** clean PDF images where possible; otherwise cutouts.

## FQC / go-live

- **URL/Links QC (Flex):** open all flyer pages and confirm each item has a URL; if not, cross-reference the linking document and update. If the linking doc is missing a URL for an item, it can be skipped. Alternative: Overview → "Items without a URL".
- **Final QC (Flex):**
  - **⚠️ RISK ITEM — ensure the flyer is NOT hidden on Hosted** (Edit Details: all toggles left unchecked).
  - **⚠️ RISK ITEM — links QC:** every item in the linking document must have a URL; spotcheck every page (grab doc from a vendor task) / use "Items Without a URL".
  - Confirm legibility heights and thumbnails set; Image QC prioritizes PDFs; page/item category QC not necessary.
  - **"ON SALE!" belongs in the Sale Story, not the Prefix** — Item Search "Pre Price Text Contains ON SALE!"; move any results to Sale Story.
  - Confirm no outstanding vendor tasks; rerun outstanding sessions; complete FQC checklist.
- **Page swap:** standard page swap.
- **Flyer Review type: Lite** (Flex-owned).

---
*Source: Vita Health Fresh Market OneGuide (Google Doc `1lQqO5wSc0wYAJsVce5f0IAtss2Xccb6ROBgCKpvNQQY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Vogue Optical — Processing Guide

> **Source:** Vogue Optical OneGuide (Google Doc `11WND6yXHr21m7RuE25DQuxr4UA0ZNkVlh21YVhj_fMA`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | `#1p-vogue-optical` |
| Hosted URL | N/A |
| Flyer types | **Flyer** (ad hoc) |
| Processing | Auto-stack; Vendor-owned; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** ad hoc, **5 business days lead time enforced.**
- **Cadence:** Ad hoc. Preview date: N/A. Linking document: N/A.
- **Workflow:** Upload & Setup (5 days out, Vendor) → FQC (1 day out, Vendor).

## Upload & setup (Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from SFTP (folder named after live/valid date) → Confirm & Upload. Auto-Group or manually enter grouping numbers. Save & Confirm.
- **Pricing Zone:** create a Base pricing zone.

### Setup QC (Vendor)
- Confirm all pages uploaded (no SFTP pages left un-uploaded); confirm flyer dates (usually first page); complete Thumbnails (4 Standard); complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box all products with images; box all websites (vogueoptical.com).

**Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand = used for both Box/Tag. **Exclude SKU and URLs.**
- Original Price = per PDF; Sale Story = the hero CTA at the top of the page; Image = select the clean PDF image.

**Spotchecks:** Standard pricing spotchecks in pipeline.

## FQC / go-live

- **Pre-Final QC (Vendor):** confirm dates vs PDF; platform toggles available everywhere; thumbnails drawn + include retailer logo; all items boxed/tagged; previews interactive; **geography consistent with last week (no stores/FSAs added or removed) — immediately flag 100% of discrepancies to the FT Ops team** (does not block; continue with Final QC).
- **Flyer Review type: Lite** (Vendor-owned).

---
*Source: Vogue Optical OneGuide (Google Doc `11WND6yXHr21m7RuE25DQuxr4UA0ZNkVlh21YVhj_fMA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
