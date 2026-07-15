# Retailer Processing Guides — C

> Bundle of 55 retailer-specific processing guides (C). Contacts and credentials are omitted from every guide.

**Contains:** C Town, Cabela's Canada, CAL Ranch, Calendar Club Canada, Calgary Co-op & Calgary Co-op Wine Spirits Beer, Canac, Canadian Tire, CANEX, Canon Canada, Cardenas Markets, Tony's Fresh Market, El Rancho Supermercado, Carquest Auto Parts, Carter's Osh Kosh, Castle Atlantic, Centre de Jardin, Centre du Travail, Centre Hi-Fi, Chalo ON, Chalo WST, Chatters Salon, Chaussures Pop, Chevron / On The Run, Chico, Choices Market, Chuck's Fresh Markets, Clore Beauty, Clover Farms + Clover Farms Ontario, Club Piscine, Co-op AG, Co-op Essentials, Co-op Food, Co-op Gas Bar, Co-op Home, Co-op Liquor, Co-op (Sobeys), Coast Appliances, Coastal Farm, Cohen's Home Furnishing, Colemans Brandsource Home Furniture, Colemans, Commisso's Fresh Foods, Community Natural Foods, Concept Piscine Design, Cool & Simple, Coppa's Fresh Market, Copp's Buildall, Corbeil Electromenagers, Corner Market MS, Cosmaroma, Costello's Ace, Couche-Tard, Country Grocer, Cub Cadet, Cub, Curtis Lumber, CVS Pharmacy (incl. Longs Drugs & Y Mas)


---

# C Town — Processing Guide

> **Source:** C Town OneGuide (Google Doc `1P5MMd4MANKEAsToKNU5k9_vZPkZAN_UrHlxmAVRwKto`), updated Aug 15, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#alpha1` |
| Hosted URL | ctownsupermarkets.com |
| Flyer type(s) | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons |
| Strategic Ops | Yes — retailer data services (Feedel processing) |

## Files & schedule

- **When files arrive:** Monday. **Upload Friday** (afternoon recommended — see risk items).
- **Publication cadence:** Available From Thursday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **No linking document.**
- **Owners:** Upload & Setup = Vendor; Image QC = Flex; FQC = DOC.

## Upload & setup (owned by Vendor) — same as Bravo Supermarket NE upload

- C Town is a **manual upload** account. Files are in the FTP — upload **ALL U41 and PU41 pages** (except any containing "AKO"). Double-check the FTP to confirm all files uploaded.
- **Create pricing zones (Flyer Creation):**
  - Create **Base u41** zone; add pages labelled **U41 B.** Save & Next.
  - Next zone **003** — change page one to **U41 003**, keep the rest the same. Save & Next.
  - Next zone **022** — change page one to **U41 022**, keep the rest the same… and so on through **ALL** remaining pages. Do the same for **ALL Base pu41** zones.
- Add individual stores to their new zones; add all remaining stores to the Base zones. **If a zone has 5 pages, remove the base page 4 to account for the store-specific page 4.**
- Proceed with Setup QC. Once the processor runs, check the FTP for skipped pages — the processor knows to skip stores **"062" and "032"**, and .ako files are excluded. Upload any missed revised pages manually and assign to the correct pricing zone.

## ⚠️ Common errors / risk items

- **New stores:** the processor may flag a file with no matching store. If clearly a new store (e.g. "Grand Opening" on the page), add it to fadmin.
- **Updated stores:** if a store code exists in fadmin but the U43/PU43 prefix doesn't match the FTP file, it likely switched from U↔PU. On the Merchant page → stores, search the numeric code (e.g. 315) and update the store to the opposite prefix.
- **Late-syncing pages:** not all pages sync at once — some arrive later, requiring manual pricing zones. **This is why upload is recommended for Friday afternoon.**
- **JPGs uploaded with PDF pages:** the pre-processor can't distinguish PDF from JPG and errors that no store is associated. Create a new store (merchant store code from the error, name DELETE, city New York, state NY, address 1, zip 10153), retry on the codesheet, force processing on the "already uploaded" error, generate sessions, then delete the PZ, the store, and the JPG from the page assortment.
- **COVID "Open for Business" PZ** process documented in the OneGuide (manual PDF upload, do not check Process Internally, copy stores from the prior live week).

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. Box all items separately (anything with a price gets a box); use text boxes when needed. **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
  - For **multiple related items** (e.g. cuts of turkey) box only the main picture (one box; no text box). Draw ONE box per different item. Only one box per item even if the price gets cut off. **Box QC: no duplicated boxes on an item.**
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-selection ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU. Always include category.**
  - **Name:** as in flyer, ALWAYS CAPITALIZED; no measurements (those go in Description); never non-bolded words.
  - **Description:** as in flyer; include all non-bolded words and measurements; do **not** include "With Card"/"Without Card" (that goes in Postfix).
  - **Postfix:** "With Card. Without Card $xx.xx" if applicable.
  - **Prices not inside the drawn box (e.g. 2.99 lb / LB.) must still be tagged.**
  - **Valid date overrides:** use the dates on page 1 of the publication. A theme banner (e.g. "4th of July") does **not** set valid dates — always use the front-page valid dates.

## FQC (owned by DOC)

- Mark autostack spotcheck complete; **legibility heights 60/40**; dates correct per page 1.
- Thumbnails — Standard 4 + `first_page_thumbnail_400w` (write complete in comments).
- Page categories.
- **Flyer Review type: Lite.**

---
*Source: C Town OneGuide (Google Doc `1P5MMd4MANKEAsToKNU5k9_vZPkZAN_UrHlxmAVRwKto`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cabela's Canada — Processing Guide

> **Source:** Cabela's Canada OneGuide (Google Doc `1tuSU7voGl0teP9Ef_b9m7Xafiomk8URUw_eq5sid19g`), updated Sep 5, 2025. Contacts/credentials omitted.

> **Note:** Bass Pro Shops Canada and Cabela's Canada versions are **both processed in the Cabela's Canada merchant** (single codesheet).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | Two versions — one **Flipp-only**, one **Hosted-only** |
| Slack channels | `#cabelascanada`, `#flex-processingsupport` |
| Hosted URL | basspro.ca/pages/flyer |
| Flyer types | Weekly + ad-hoc (per the Publication Schedule) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday (ad-hoc varies).
- **Cadence:** Available From Wednesday · Valid From Wednesday · Available To Thursday · Valid To Wednesday (ad-hoc varies).
- **Preview date:** yes — **set it per the Publication Schedule** and send the preview link to the retailer for review.
- **Linking document:** yes — used for both Box and Tag; attach to all vendor tasks.

## Upload & setup (owned by DOC)

- **Codesheet:** download the `(Run Name)_Pagination_Flipp.xls` from the FTP. It contains both Bass Pro CAN and Cabela's CAN versions. There is a **"Stores" tab (Hosted)** and a **"Flipp.com" tab (Flipp-only)** — the difference is inserts (inserts display poorly on Flipp Web).
- **Workflow:** upload the Hosted version (with inserts), then clone to a Flipp-only run and remove inserts from all zones.
- **Upload config:** save Stores tab as CSV → upload to the **Hosted** flyer run. **Config = `cabelas_canada`**; PDF base directory copied from FTP; **check everything except Region Assignment and Combine Zones.** Save & Process.
- **Budget is assigned to the Flipp-only run ID** — always confirm the Hosted and Flipp-only run IDs match the Publication Schedule; do NOT swap which version is which.
- **Language handling:** codesheet uploads "Ottawa English" as English, "Ottawa Bilingual" as French, "Moncton" as English only. Manually add NB pages unique to Moncton and upload **French versions**. Create a new **Moncton FR** pricing zone (marked French) and add **store 84** to it.
- Attach the run's Linking Document (`…Flipp+Links.xlsx`) to all vendor tasks.

### Setup QC
- Add preview date per the Publication Schedule; confirm all pages uploaded (check SFTP for stragglers); confirm dates on the flyer vs schedule; thumbnails 4 Standard; add external run names from the schedule / page 1; confirm link sheet attached.

## ⚠️ Common errors / risk items
- **Codesheet inserts are the #1 upload failure.** If the codesheet errors (even with inserts in the SFTP), remove insert rows (usually highlighted orange), rerun, then upload inserts manually and place them via Pages > Layout. The shopbycategory page usually uploads fine. Reference CLSD-4543 for help.
- Upload **English AND French** versions of inserts going into **Ottawa Bilingual** and/or **Moncton** zones; others can be English-only.
- **Moncton uploading English-only is a known AOO** — file a CLSD ticket to have the codesheet processor treat Moncton like Ottawa (EN + FR).
- **Tag in the correct language.**
- **Links are the biggest tagging risk — almost every item should have a link.** The retailer expects very high link accuracy and has flagged even small error counts.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- Linking document required (box + tag).
- **Include (if in Linking Document):** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- All items get one box. **Top-of-page and bottom-of-page links are often missed by Auto-Box — add them in Box QC per the link sheet.** Box the front-page Cabela's logo. Banners → boxed and tagged as a direct link (if no link, tag as an item with a relevant name).

### Tag / Tag QC (Medium; Auto-tag ON)
- Linking document required (box + tag). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Set banners to **Link** display type; find links in the Linking Document. Flag any box with no link. **Most items have a link** — use Cmd+F on the item's full name (some names are similar, so match the full name). Add SKUs comma-separated.

### Image QC
- PDF preferred if clean; otherwise cutouts. No extra retailer Image QC.

### Link QC (post-processing, can be filed to Flex via FAB ticket)
- **New process:** Overview > Items Missing URLs (fill from Linking Document); then Export Items → Google Sheets, keep only Item ID/Name/SKU/URL, sort by SKU, and investigate outliers (multiple versions of an item usually share a link — a differing link flags an error). Correct via Overview > Item Search → open item → fix in Tagging Interface.

## FQC / go-live
- Work in the **Hosted-only run** (has inserts; hidden on Flipp + Distribution). Confirm dates vs PDF + schedule; availability toggles; thumbnails Standard 4 with logo.
- Check **Items Without URLs** and apply from the link sheet. **C runs often have Category pages linked out that Auto-Box missed and OS didn't add** — box them yourself, apply links from the Linking Document, add to all versions of the page.
- Ensure no pages merged; spotcheck largest English + French previews (clickable); geography same WoW; confirm **store 84 in Moncton FR** zone.
- **Flipp-only clone:** copy Hosted run to the matching Flipp run name; when sessions run, Pages > Layout remove all inserts except the Category page; set toggles (hidden on Hosted only, available on Flipp + Distribution); run FQC.
- **Ad corrections:** apply the correct correction to each pricing zone (match file name to stores per Pagination doc; watch EN/FR versions).
- **Flyer Review type: Lite.**
- **Page copying from Bass Pro is no longer done** (historical only).

---
*Source: Cabela's Canada OneGuide (Google Doc `1tuSU7voGl0teP9Ef_b9m7Xafiomk8URUw_eq5sid19g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# CAL Ranch — Processing Guide

> **Source:** C-A-L Ranch OneGuide (Google Doc `1rQR9-if9AzaUsg0rxjFeCABAlDW6_GkO8Ko6Uox-hs8`). Contacts/credentials omitted.

> **Distinctive flow:** the retailer QCs an **item export** and returns corrections, which are then **re-imported** so that **only Name, Sale Story, and URL are populated** — all other tagging fields must be blank.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (occasional Hosted-only flyers with too few items for Flipp; retailer is aware) |
| Slack channels | `#calranch` |
| Hosted URL | calranch.com |
| Flyer types | Ad-hoc (event-based) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); OS (Setup + FQC); no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday.
- **Preview date:** Monday.
- Files uploaded into **folders matching the event name**; rarely different versions in separate folders.

## Upload & setup (owned by Vendor)

1. Contact emails when files are uploaded to the FTP. Flyer may have **two versions (North / South)** — store assignments are in the email; if one version, email will say "good in all stores" (build one pricing zone, all stores).
2. **Create flyer shell:** run type **StoreAds**; Internal Run Name = event name (email or page 1); External Run Name = event name; live/valid dates from email or page 1; toggles = available everywhere; add theme if applicable.
3. Manual upload — select the event's folder pages in the FTP → Autogroup.
4. **Pricing zones:** typically all stores to base; if two zones, assign per the email.
5. Attach note to all vendor tasks: "No linking document, please proceed with tasks."

## ⚠️ Common errors / risk items
- **Look for multiple products** (multi-item boxes).
- **Tagging is deliberately minimal** — only Name, Sale Story, and URL are ever filled. The only URLs should be the main website and social media (on boxed/tagged logos).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Use text boxes when needed; box each item separately.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON)
- **Only Name, Sale Story, and URL are filled.** Include: name, SKU, sale story, categories, URLs. **Exclude:** pre/postfix, valid dates, description, price, disclaimer, original price. Brand is box/tag-specific.

### Image QC
- Select PDF images chosen; if unclean, use cutout.

## Post-processing (item export → retailer QC → re-import)

**1. Send item export to the CAL Ranch team as soon as vendors finish:**
- Overview > Information/Reports > Export Items → download CSV → open in Google Sheets.
- Delete the "Flyer Items" cell and everything below it; delete the "Page Items" cell.
- Keep only: page, item_id, name, sku, raw_original_price, raw_current_price, sale_story, url. Sort page ascending; rename `raw_original_price`→"original price" and `raw_current_price`→"current price". Only main-website + social URLs should be present.
- Save as `.xls` and send.

**2. Final QC after corrections come back:**
- Read Column A ("Comments") of the returned report and manually apply re-boxing instructions (e.g. group listed item IDs into one box).
- Delete Column A and the Pages column; rename prices back to `raw_original_price`/`raw_current_price`; add columns brand, description, disclaimer_text, pre_price_text, price_text.
- Column order: item_id, sku, brand, description, disclaimer_text, name, pre_price_text, price_text, raw_current_price, raw_original_price, sale_story, url.
- Enter `*blank*` in every cell of: brand, description, disclaimer_text, pre_price_text, price_text, raw_current_price, raw_original_price (retailer wants all fields empty except Name, Sale Story, URL).
- **Save as `.csv` in Google Sheets** (item import fails from Excel). Overview > Information/Reports > Item Import → upload → check Last Session Results for success.
- **Verify via Item Search** — Brand / Description / Disclaimer Text / Price Text / Current Price / Original Price each **IS NOT BLANK should return 0 results.** Clear any offenders.
- Then: confirm logos + social icons boxed/tagged; check dates; page categories; sessions clear (reverify URLs if needed); thumbnails Standard 4; legibility heights 45/35; Item Image QC (PDF chosen, cutout if unclean).

## Flyer review / out-of-processing
- **Flyer Review type: Lite** (owned by Flex).
- **Page swaps are standard** (baseline process).

---
*Source: C-A-L Ranch OneGuide (Google Doc `1rQR9-if9AzaUsg0rxjFeCABAlDW6_GkO8Ko6Uox-hs8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Calendar Club Canada — Processing Guide

> **Source:** Calendar Club Canada OneGuide (Google Doc `1ihgxa15Xv197bu6J8AEpSWd6tL5MG9H2BDyXtbQBMrI`), updated Jun 22, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#1p-calendar-club` |
| Hosted URL | N/A |
| Flyer types | Seasonal (ad-hoc) |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **Files received:** ad-hoc. **Pages must be added to the SFTP by the processor if the client sends over email.**
- **Cadence:** Available From Thursday · Available To Wednesday · Valid From Wednesday · Valid To Thursday.
- **Preview date:** 1 day before go-live (preview sent to retailer). **Linking document:** yes (used for box + tag).

## Upload & setup (owned by DOC)

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload. Auto-Group or add page numbers (English pages only) → Save & Confirm.
- **Pricing Zone Creation:** create Base pricing zone, select all applicable pages, Save & Confirm, add all applicable stores.

### Setup QC
- Confirm all pages uploaded (Items View); check SFTP for un-uploaded pages. Confirm dates (usually first/last page). Thumbnails 4 Standard. **Set preview date 1 day before Available date.**

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- Linking document required (box + tag). **Include:** retailer logo, social media, special weblinks. **Exclude:** coupons, packaged deals, sign-up page.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking document required (box + tag). **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**

### Image QC
- PDF preferred if clean; otherwise cutouts accepted.

## FQC (owned by DOC)
- **Check Items Without URL** — if flagged, confirm via the linking spreadsheet whether the item was intentionally left without a link; otherwise apply the link.
- **Check all items are boxed**, including **last-page CTAs** and images throughout; confirm against the link document and fix anything missing/unclickable.
- Confirm dates vs PDF; availability toggles; thumbnails include logo; standard checks (boxed/tagged, spotchecks 20% of pricing zones, previews clickable, sessions complete, geography).
- **Flyer Review type: Simple.**

---
*Source: Calendar Club Canada OneGuide (Google Doc `1ihgxa15Xv197bu6J8AEpSWd6tL5MG9H2BDyXtbQBMrI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Calgary Co-op & Calgary Co-op Wine Spirits Beer — Processing Guide

> **Source:** Calgary Co-op & Calgary Co-op Wine Spirits Beer Liquor OneGuide (Google Doc `1aeV6bYo274O3vstEtpwkQ6XfUvQAq9OhNpL5ZEDF8xA`), updated Mar 11, 2026. Contacts/credentials omitted.

> **Two banners, one shared linking doc** that must be split: Calgary Co-op (food, flyer type **480**) and Calgary Co-op Wine Spirits Beer / WSB (flyer type **3441**).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#calgarycoop` |
| Hosted URLs | calgarycoop.com · coopwinespiritsbeer.com |
| Flyer types | 480 Weekly (Co-op food) · 3441 Weekly (WSB) |
| Processing | Auto-stack; Flex (Setup, FQC, Flyer Review); OS (Setup); no coupons; no Feedel |

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From Wednesday · Valid From Thursday · Available To Wednesday · Valid To Wednesday.
- **Linking document:** yes (shared between the two banners — see below).

## Upload & setup (owned by Flex)

**Shared linking-doc manipulation (do once):** They send **2 linking docs in the FTP — use the `coded.xlsx` file.** Select all → **paste as plain text** (Ctrl/Cmd+Shift+V) to strip formulas. Delete columns Name, Page, Shortened URL. The doc mixes **Co-op Weekly AND WSB** content, so split it: new sheet with headers Flyer, Dates to display, Name Code, URL; move the WSB rows into the new sheet. Save two docs — `Wk___ (Weekly)` and `Wk___ (WSB)`.

**Calgary Co-op Food (480):**
1. Manually upload all pages → 1 pricing zone → all stores.
2. Attach the **Weekly** linking doc to all vendor tasks.
3. Overview > Edit Details: no theme; available everywhere. Thumbnails 4 standard. Setup QC.

**Calgary Co-op WSB (3441):**
1. Pages > Edit > select files. **Page order follows natural pagination (e.g. 1, 1A, 2, 2A).**
2. Pricing zone: Base; assign all stores. Wait for sessions.
3. Attach the **WSB** linking doc to all vendor tasks.
4. Overview > Edit Details: no theme; available everywhere. Thumbnails 4 standard. Setup QC.

## ⚠️ Common errors / risk items
- **Valid dates only on 'Price Drop' items** — do not add valid dates elsewhere.
- **Product links** must be boxed and tagged correctly.
- **Meat and deli categories usually have errors** — verify they are categorized correctly.
- **Unique valid dates in the linking doc are a recurring risk.** During FQC, check the linking doc for unique valid dates; if present, create an **Optics ticket (OPSMR)** and trigger accordingly (add DOC + DOL, assign to 1DOC). WSB **always has one (a 4-day sale)** and can also have unique dates on specific pages.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- Linking document required (box-specific).
- **Include:** coupons, packaged deals, sign-up page, social media, special weblinks. **Exclude:** retailer logo, percent-off sales.
- Single items: box the whole item block. **Multi-items: box separately even if pictured together** (different pricing → cannot be combined).

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON)
- Linking document required (tag-specific). **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- Tag branding only in the branding field (don't double in name). Enter fields as seen in flyer. URLs from the linking doc — usually only top/bottom banners, not food/wine items.
- **Categories: tag both "Categories" AND "Category Highlights" fields; be mindful of meat and deli.**

### Image QC
- Use PDF whenever possible; cutout if no clean PDF. **Co-op food PDFs often have black around the edges.** WSB is essentially all cutouts.

## FQC (owned by Flex)

**Co-op Food:** mark autostack + spotchecks complete; Category QC (meat/deli); Linking Doc QC (insert names + URLs match attached doc) — **check for unique valid dates → Optics ticket**; all vendor tasks/sessions complete; FQC checklist.
- **Ad-hoc:** if a PDF page has a weird shadow, run **"ghostscript 9.06 gamma"** in sessions at the page level.

**WSB:** mark autostack complete; Linking Doc QC — **there is always 1 unique valid date (4-day sale) → Optics ticket**; also check unique valid dates on specific pages; sessions/tasks complete; FQC checklist.

- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps are standard (baseline process).

---
*Source: Calgary Co-op & Calgary Co-op Wine Spirits Beer OneGuide (Google Doc `1aeV6bYo274O3vstEtpwkQ6XfUvQAq9OhNpL5ZEDF8xA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Canac — Processing Guide

> **Source:** Canac OneGuide (Google Doc `1aBXgXrDOfOUZbdZU1Y0Vic4FBCP414BE0l0b0LYr5NA`), updated May 12, 2026. Contacts/credentials omitted.

> **Bilingual (EN/FR) Québec retailer.** Two flyer versions: **C** and **CP**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#canac` |
| Flyer types | Weekly (versions C and CP) |
| Processing | Auto-stack; Flex (Unique Shift Type 3FL + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday. **Preview date:** Sunday (live date one day before valid date).
- **Cadence:** Available From Wednesday · Valid From Thursday · Available To Wednesday · Valid To Wednesday.
- **Linking/tagging document:** yes — found in the SFTP; search "xls" and download the XLS matching the flyer run name (e.g. flyer run c17 → `c17.xls`; c17p → `c17p.xls`). Attach to all vendor tasks via **mass attachment** ("+").

## Upload & setup (owned by Vendor)

**Version C:** select ONLY the version-C file name (check the upper-case file folder for additional pages). Manual upload into the correct run; ensure correct language (EN + FR); live date one day before valid; attach tagging doc to all vendor tasks.

**Version CP:** select ONLY the CP file name. Manual upload; select language French. Pricing zones — **French: include all pages; English: toggle "cross language" → select English → upload all pages.** Live date one day before valid; attach the CP tagging doc.

## ⚠️ Common errors / risk items
- **Unique Page 1 for additional locations (top risk):** when setting up zones for both versions, check for a unique Page 1 for other locations. **Do NOT bundle additional zones into the base pricing zones** — create two dedicated zones per additional location (e.g. `Salaberry EN`, `Salaberry FR`). Store assignments for additional zones are in the ClickUp task; each cover page names its store (except the base cover).
- **During FQC, verify (against the ClickUp task) the correct number of pricing zones were created and each zone has the correct version of Page 1 with NO DUPLICATES** — zones have been missed and multiple Page-1 versions assigned to the same zone. Flag to processor if wrong.
- **Look for multiple products** — box each SKU separately when a product block has multiple SKUs.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- Linking document required (box-specific). **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each individual SKU separately within a multi-SKU product block.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select OFF)
- Linking document required (tag-specific). **Include:** name, pre/postfix, description, SKU, price, sale story, categories, original price, URLs. **Exclude:** valid dates, disclaimer. Brand is box/tag-specific.
- **Include the SKU in BOTH the description and the SKU box.**

### Image QC (data-piped check)
- Overview > Item Image QC → **untoggle "data piped"** → filter. Items that appear need a data-piped URL — fix them; if an item is not on the merchant website or there is any concern, reach out to the DOC.

## Post-processing / FQC (owned by Flex; complete by EOD Monday)

- **Item Category QC (DOC):** ensure items have Google Categories.
- **Item Image QC:** Monday morning, send the flyer link to the Flex-Canac channel for image QC. To verify: Image QC → unselect data piped → search → per item, copy SKU → search canac.ca. If the item exists, copy the white-background image URL into **Override Image URL**; if not, select the white PDF, else a cutout (retailer may flag missing images — if not on the website, tell them so). Ensure data-piped images are selected.
  - **Workaround if image QC won't push to front end:** confirm an override image URL exists, refresh "generate sibling groups" (retriggers data pipping), and wait ~1 hour after the task finishes.
- **URL/Links QC (DOC):** Overview > Items Without URL → check appearing items against the retailer's linking document.
- **External run name:** Overview > Edit Details. C## flyers → EN "Help for Real" / FR "Aide Pour Vrai"; CP## → use the publication name on page 1.
- Standard 4 thumbnails; confirm valid date matches publication and there's a 1-day preview.
- **Preview links** sent before 1PM Tuesdays.

## Ad-hoc — Canac New Brunswick (CNB) cloning
1. Clone the regular weekly run into the CNB run.
2. Remove all stores from each pricing zone.
3. Via Custom Action, assign FSAs **E3V, E4P, E7A, E7B, E7C, E8E** to the Rivière-du-Loup pricing zone.
4. Proceed with standard QC. **(NB processing ends May 20, 2026.)**

- **Flyer Review type: Lite.**

---
*Source: Canac OneGuide (Google Doc `1aBXgXrDOfOUZbdZU1Y0Vic4FBCP414BE0l0b0LYr5NA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Canadian Tire — Processing Guide

> **Source:** Canadian Tire OneGuide (Google Doc `1iuZdREyNZy9MnGw4vsDTnSFpNFtlpysLlpMW2oedD_4`), updated Apr 29, 2026. Contacts/credentials omitted.

> **Complex bilingual (EN/FR) account** with heavy codesheet manipulation, a two-drop weekly cadence (main pages, then Digital Ad inserts), and per-zone FSA/UTM custom actions.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium |
| Availability | **Flipp only** |
| Slack channels | `#canadian-tire`, `#cantire-ssd-testing`, `#ct-nativex` |
| Flyer types | Weekly Flyer (1488) · Catalogue (3436) · Grand Opening/GO (3845) |
| Processing | Auto-stack; Flex via FAB tickets; no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Tuesday (Weekly). **Weekly is a two-drop cadence:** main flyer pages ~2 weeks out; **Digital Ad inserts a week later** (Tue/Wed, ~1 week from live). Catalogue is similar. GO files arrive just within the 5-business-day window.
- **Cadence:** Available From Tuesday · Valid From Thursday · Available To Thursday · Valid To Thursday. Some weeklies run to Sunday.
- **Preview date:** set to the upcoming Tuesday (1 week before live) so OS isn't slammed doing both uploads at once.
- **Linking documents:** Header link sheet + Basebar link sheet (in the VTB Drive folder); the weekly **Digital Ad "Digital Direction" link sheet** is emailed only (not in SFTP).
- **Historical note:** data piping is **defunct** (confirmed Mar 7, 2025 — consistently errors out).

## Upload & setup (owned by DOC)

### Weekly / Catalogue — main pages (codesheet)
Two codesheets: **BIL** (bilingual) and **ENG**. **Do the BIL codesheet first.** Files are read-only — switch to edit mode.
- **Update Date:** set cell B2 to the Available From date. Temporarily set the run's Available From & Valid From to Tuesday and Available To & Valid To to Friday (so the staggered Sale Dates all validate), then revert after.
- **RL Codes:** delete "-BIL" from all zone names (Find & Replace) so they match FAdmin store sets. Move any Sub-Zone text into the RL Codes column.
- **Delete "é" from "Québec"** everywhere (usually B72, B76) — otherwise an **"Invalid byte sequence"** error.
- **Delete pages listed but not in SFTP** (typically 200-series 201–204 and 80-series 81–82 — these come in the second drop).
- **Delete extra text in 70-series page names** (remove "pop "); cells should read only "pg. " + number.
- **Delete pages with a different SFTP base path** (multiple events in one codesheet); upload those manually and place via Pages > Layout.
- **Check for `_REV` pages:** search SFTP "rev"; add "_Rev" to those page names in the codesheet.
- **Upload:** save as CSV → Codesheet tab. Name = `BIL`; **Config = `canadian_tire`**; PDF base directory from SFTP (BIL and ENG base paths differ!); **toggles: all except 2nd (Region Assignment) and last (Combine Zones).** Save & run.
  - **Do NOT process the ENG codesheet until all BIL sessions finish** — back-to-back uploads cause race conditions and errors.
- BIL codesheet makes one English + one French version of each zone; ENG makes one version each.
- After both: manually upload any deleted 100-series pages (upload ENG + BIL, then BIL again set to FR); mark Flyer Creation Complete; insert 100-series pages into zones via Pages > Layout per file names.

### Weekly / Catalogue — Digital Ad inserts (second drop)
- Manually upload all DB + DE pages from the Digital Ads folder, then upload DB pages again set to **French**. Mark Flyer Creation complete.
- **Digital Direction link sheet:** hide rows where Asset Type is "Print"/"FC"/"Print P#" (already-uploaded pages), save, mass-attach to all new vendor tasks. Update Preview Date to the following Monday.

### Grand Opening (GO)
- Manual upload, **no codesheet** — use the schedule from the GO contact. One flyer run per date range; each TC Code = its own folder = its own pricing zone. **Upload GB25 files twice (EN + FR).** Assign page groupings from file names (P01…). Create zones per Schedule; add stores from the GO Store # / Part Store # columns.

### Setup QC (all types)
- **Remove Stores in Multiple PZs:** WAWA, CASSELMAN, SHEDIAC get both English-only and English-bilingual assignments — remove them from the English-Bilingual zones (Overview > Manage Stores).
- Confirm dates on page 1 (watch wrong-Sunday end dates → fix in Staggered Dates); revert Available/Valid dates to originals; set Preview Date to upcoming Tuesday.
- Mass-attach Header + Basebar link sheets to all vendor tasks (attach to Flyer Creation task to cover all tracks). Thumbnails Standard 4.

## ⚠️ Common errors / troubleshooting
- **"Invalid byte sequence"** → an "é" (almost always "Québec", cells B72 & B76). The error flags only the first instance — fix both.
- **"Valid dates" error** → extend the run's valid dates, rerun the codesheet, then revert.
- **"File not found"** → the codesheet processor may dislike multiple Event Names in B2 (and in Format B4 / Page Position B12); delete "/D###" from B2 and clear B4/B12, rerun. File names draw from Plant Code + row-15 page numbers + version text — check those for typos. Last resort: remove the offending page column, run, upload those pages manually, place via Page Layout.
- **BIL vs ENG base paths differ** — grab the correct one.
- **Never upload ENG codesheet before BIL sessions complete** (race conditions).

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- Linking document required (box-specific). **Include:** special weblinks. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Box Headers/Footers listed in the linking docs; box anything saying **"Triangle"** or with a **"Learn More"** callout. Box all items with prices (text boxes when needed); don't overlap adjacent boxes; box black-bolded sub-items separately.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking document required (tag-specific). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Use text extraction** to minimize spelling errors (careful with numbers); **French flyers must use correct accents (é, è, ê…).**
- **Name:** no ©/™ symbols; capitalize the first letter of the brand (e.g. "simoniz" → "Simoniz"); if the name isn't on the PDF, search the SKU on the CT website.
- **SKU:** enter in BOTH the Description and the SKU field, exactly as printed. **Original Price:** if a range, enter the LOWER number only.
- **URLs:** search the SKU on canadiantire.ca (EN `/en/`, FR `/fr/`) and tag the product URL. **If a SKU ends in X, search WITHOUT the X.** If two SKUs have Xs, only do the first. **All Tires items (no SKU)** get the fixed tires-category URL (EN/FR). Otherwise use the linking document.

### Image QC
- Choose a clean PDF where possible; cutout if none.

## Post-processing / Pre-FQC (owned by DOC; Links/SKU QC can go to Flex via FAB ticket)

- **Insert Digital Ads into zones first** (long sessions run in background). Use the **Insert Breakdown** sheet (duplicate Template tab, match page count, map from the Digital Direction column B). Add **DB inserts to French zones first**, submit, let sessions finish; then **DB inserts to English-Bilingual zones** (carefully add the `DB03##` inserts to DB/English-bilingual zones — both DB and DE appear under the English toggle); then **DE inserts to English-only zones** (0- vs 1- zones; `0(Ex…)` = all 0-zones except those named, where "Mar" = Maritime provinces NS/NB/PEI/Nfld; `0_x_x…` = only 0-zones sharing that name element; never select `1_NWTRky`). Confirm all zones have equal page counts.
- **Direct Links QC:** review each page in the Digital Direction sheet has the correct link (links are often sibling-grouped; grab from URL ENG vs URL FRE column).
- **SKU QC:** Item Search → SKU IS blank, Item Type Item → fill SKU from PDF (skip Tires).
- **Links QC:** Item Search → URL IS blank. Multi-Edit all Tires with the fixed tires URL (EN then FR), then search remaining SKUs on canadiantire.ca (drop trailing X; skip flowers/plants — not posted online).
- **Categories:** none on page 1 (no longer required as of 07/25). **Mark items in store only** (only after Links QC — it blocks saving new links). Thumbnails Standard 4 (add NativeX thumbnail if a NativeX campaign runs).
- **Manage Tracking Codes (Weekly only):** add Flyer Run Tracking Code — Dynamic Variable, Source All, `utm_campaign`, value `2026_03XX-Weekly-Flyer` (change 3XX by week) → Apply All.
- Expect and review **PZs have Staggered Dates** error (verify dates vs page 1). Add revised pages as they arrive.
- **Assign FSAs from .csv custom action:** copy the `1_NwtRky` pricing-zone ID into the CT FSAs sheet, download CSV, FAdmin > System > Custom Actions > "Assign FSAs from .csv", enter the **flyer run ID** (not the PZ ID), upload, run.

### GO Pre-FQC specifics
- Follow the GO contact's email on ecomm links: if links should NOT be added, export items, remove all URLs, re-import; if approved, QC per above. Complete SKU QC; no categories on page 1; mark in-store only (after Links QC); thumbnails Standard 4; add revised pages; verify dates/stores vs Print Schedule.

## FQC / go-live
- Complete Final QC Checklist. Expected ignorable errors: items not QC'd (spot-checked items → "Ignore"); pricing zones without stores (redundant English-Bilingual zones → "Ignore"); Categories without an Image.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page revisions are standard**, but **re-run the "Assign FSAs via .csv" custom action after every revision** (FSAs reset). Use OPTICS tickets as needed.

---
*Source: Canadian Tire OneGuide (Google Doc `1iuZdREyNZy9MnGw4vsDTnSFpNFtlpysLlpMW2oedD_4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# CANEX — Processing Guide

> **Source:** CANEX OneGuide (Google Doc `1WDzRKPmufJBbZBi_S-Ryl9WKI-w8hM5nXKNu8x3WElA`), updated May 16, 2024. Contacts/credentials omitted.

> **Bilingual (EN/FR)** military-community retailer (CFMWS).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#canex` |
| Hosted URL | canex.ca/en/ |
| Flyer types | Bi-Weekly (3491) · Monthly |
| Processing | Auto-stack; Flex (Setup, FQC, Flyer Review); OS (Setup); no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Monday (files sent 1–2 times a month; contact emails when dropped). A "locations file" is also dropped — **ignore it.**
- **Cadence:** Available From Friday · Valid From Friday · Available To Monday · Valid To Tuesday.
- **Preview date:** 2 business days before live (Monday midnight).
- **Linking document:** yes (Excel, provided per flyer). **Split into EN and FR files** (delete FR links → save EN → attach to English vendor tasks; delete EN links → save FR → attach to French vendor tasks). Sometimes you must upload files to the SFTP yourself (page swaps or email attachments).

## Upload & setup (owned by Flex)

- Pages > Edit > Upload FTP → Auto-group → **manually change French pages' language to French.** Zones: EN and FR; add all stores to each.
- **Pre-Setup QC:** Vendor tab — autobox draw; mass-upload the linking doc for both languages. Overview > Details: available everywhere; **preview date 2 business days before live (Monday midnight).** LH 45/35; thumbnails Standard 4.
- **Setup QC:** **ignore the "no french stacks" warning;** mark autostack spotcheck complete.

## ⚠️ Common errors / risk items
- **Links (top risk):** ensure tagged links match the linking document. **After the preview link is sent, the retailer ALWAYS returns revised links (usually <10, highlighted) — update accordingly.**
- **French item type:** OS commonly tags French items as a **Link** when they should be **Item** — if there's a callout (e.g. "Save 20%"), item type must be **ITEM**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- Linking document required (box-specific). **Include:** coupons, packaged deals, special weblinks. **Exclude:** retailer logo, sign-up page, social media.
- Box items with prices/discounts; box deals as a whole box; box pages with URLs.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking document required (tag-specific). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Brand = larger text; Name = smaller text under it. SKUs are a mix of letters and numbers. If item valid dates differ from flyer dates, add them on the item. **URLs from the attached Excel spreadsheet.**

### Image QC
- Prefer PDFs unless unclear/black background.

## FQC (owned by Vendor)
- Geography: nothing added. PZ tab: everything boxed/tagged; horizontal/vertical scroll check.
- **Page Category QC:** choose 1–2 categories; nothing on the first page. **"Points promo pages" get a blank category.**
- Overview Details: available everywhere; typically no theme; internal run name prepopulated; no external name; preview date 2 business days before live. LH 45/35; thumbnails Standard 4; Image QC prefer PDFs.
- **Items Without URL:** try the linking doc; if no link exists, note it in comments (retailer will likely send it after previewing).
- **UTM code (Manage Tracking Codes):** from the linking doc — usually `UTM-d#` (flyers start with D#, matching the UTM). Update all 3 "Campaign" fields with the text after "UTM".

## Out-of-processing / preview
- Ensure preview date = Monday 12:00 AM; Monday morning send EN + FR preview links. Retailer has **one business day** to send corrections (always URL corrections, usually <10).
- **Flyer Review type: Lite.**

---
*Source: CANEX OneGuide (Google Doc `1WDzRKPmufJBbZBi_S-Ryl9WKI-w8hM5nXKNu8x3WElA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Canon Canada — Processing Guide

> **Source:** Canon Canada OneGuide (Google Doc `1lnQgXOk6RnQ25h0hnJrn7E0e_mrz8aRg0JrCJ38IiL8`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Flyer types | Flyer |
| Processing | Auto-stack; Vendor-owned end to end; no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday. **Preview date:** N/A. **Linking document:** N/A.
- **Cadence:** Available From Friday · Available To Thursday · Valid From Friday · Valid To Thursday.

## Upload & setup (owned by Vendor)

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP. Folder is named by the flyer's valid date — **always use the lower-case folder; do NOT upload the Upper Case folder.** Confirm & Upload → Auto-Group → Save & Complete.
- **Pricing Zone Creation:** one zone called "Base"; add all stores.

### Setup QC
- Confirm all pages uploaded — the SFTP should have nothing left except the **multi-page PDF** (upper-case name not ending in "P####"). Flag missed pages to the FT team.
- Confirm valid dates match page 1. Thumbnails 4 Standard. Platform toggles: all platforms.
- **Geography tab: ensure 0 changes to Stores or FSAs — flag 100% of discrepancies to the FT team** (via Slack/email; continue the checklist, but always flag).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Exclude everything special:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs. Always select a clean PDF image if available.

## FQC (owned by Vendor)
- Confirm valid dates vs PDF; toggles available everywhere; thumbnails include logo.
- Standard checks (all boxed/tagged, previews clickable). **Geography consistent with last week (no stores/FSAs added or removed) — immediately flag 100% of discrepancies to the FT Ops team** (does not block work).
- **Flyer Review type: Lite.**

---
*Source: Canon Canada OneGuide (Google Doc `1lnQgXOk6RnQ25h0hnJrn7E0e_mrz8aRg0JrCJ38IiL8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cardenas Markets, Tony's Fresh Market, El Rancho Supermercado — Processing Guide

> **Source:** Cardenas Market / El Rancho Supermercado / Tony's Fresh Market OneGuide (Google Doc `1S5VFYJ1dI7hckrHl1evB8ffNTXhJgxzMsPIhlo_d-Q4`), updated Jun 16, 2026. Contacts/credentials omitted.

> **Three banners under one parent (Heritage Grocers).** Spanish-language grocery. Weekly Ad + Monthly Savings Guide.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#cardenas`, `#flex-processingsupport`, `#flex-flyer-review` |
| Hosted URL | cardenasmarkets.com/shop/weekly-ad/ |
| Flyer types | Weekly (3563) · Monthly Savings Guide (same flyer type as weekly) |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup); no coupons/Feedel |

## Files & schedule

- **Files received:** Tuesday. **Cadence:** Available From Tuesday · Valid From Tuesday · Available To Wednesday · Valid To Tuesday. Available From = 1 day before Valid From (1-day preview).
- **SFTP path prefixes** (files for all 3 banners land in each SFTP — upload to the correct banner, mark the others off): Cardenas `/CMKTS_`, El Rancho `/ers_` (lowercase, **not** `/ERS_`), Tony's `/TFM_`.

## Upload & setup — Weekly (owned by Vendor, codesheet generator)

- Use the correct **Codesheet Generator** per banner (Cardenas / El Rancho / Tony's).
- **Backend tab, cell A1 = flyer date (MMDD)** matching the FTP folder. If MMDD starts with 0, prefix an apostrophe (`'0629`). If they use YYYYMMDD (e.g. 20260627), use that.
- **NEW (Jun 16 2026):** use the retailer's Gemini gem — attach the image saved from the email (nothing else), send, and copy the plain-text table it outputs. Paste as plain text into cell A1 of the **EXPORT** tab to fill zone/store info. (If the gem doesn't return the table, ask it for "the table in a code block plaintext format".)
- Check the FTP for how many pages each version (V##) receives. Copy the EXPORT tab → paste **Values Only** into the CODESHEET tab. Adjust Page # columns to match the FTP: if all zones get 4 pages, keep columns C–F and delete G & H; if any zone gets 5–6 pages, keep the Page 5/6 data only for those zones.
- Download CODESHEET tab as CSV → flyer run > Code Sheets. **Name = `codesheet`; Config = `generic`; toggles = ALL except 2 and 7; PDF Base Directory** from the FTP (e.g. `/cmkts_062426` — grab only the first directory after "/" and before the second "/", no `/v34` etc). Save Code Sheet → Process Codesheet → mark Flyer Creation Done.
- Edit Details: valid dates match PDF; Available From = 1 day before Valid From; No theme; no external run name.

## Upload & setup — Monthly Savings Guide (owned by Flex)
- Manually upload the versions (e.g. Cardenas V1, V2, V5), paginating via the version code + page number in each file name; create pricing zones. Add stores via store sets (Tony's: add all stores for distribution). Edit Details: **External Run Name = "Monthly Savings Guide"; No theme.** Thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **Flyer sorting:** the **weekly ad must always appear before the sales guide** on the website. Correct order: Oldest Weekly, Newest Weekly, Monthly. (A flyer only appears on the sorting page after autostack spot check is marked complete.)
- **Multiple items in one ad block** — box separately; watch small sub-items embedded in larger boxes.
- **1/2/3-day special sales appear most weeks** — every item under those headers needs **both** a Valid From and Valid To date. On page 3, watch for unique valid dates (Tuesday/Thursday Specials) in the top section and coupons in the bottom section.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Include:** coupons, packaged deals. **Exclude:** retailer logo, sign-up page, social media, special weblinks.
- Every item gets its own box; draw embedded sub-items separately.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates (except special-sale items — see below).
- **Name = the BOLDED name, in Spanish;** the **English name goes in the Description** (tag as it appears). Enter price/prefix/SKU/sale story as in flyer.
- **Valid Dates:** tag Valid From/To when applicable; **all items under 1/2/3-day sale headers get both dates.**
- **URLs:** box links, tag with "Link" display type and the link in the callout.
- **Categories:** every item requires a category selection.
- **Disclaimer:** only if within the drawn box (not page-bottom disclaimers). Coupons may have disclaimers; leave blank if illegible.

### Image QC
- Select clean PDFs whenever available; cutout if no clean PDF.

## FQC (Weekly owned by DOC; Monthly owned by Flex)
- Mark Autostack complete; Edit Details (No theme, no external run name — Monthly: "Monthly Savings Guide"); thumbnails Standard 4; mark items in-store only.
- Categories: **none on the first page of each version**; tag the rest by items on the page.
- Open all pages: verify coupons (display type Coupon, valid dates tagged) and all special-sale-date items are boxed/tagged correctly; Image QC.
- **Geography must read "No Stores or FSAs/zips were added or removed!"** Check all sessions ran. Complete FQC checklist.
- **Check Flyer Sorting** on the merchant page: Weekly (current) before Monthly.
- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps are standard (baseline process).

---
*Source: Cardenas Markets / Tony's Fresh Market / El Rancho Supermercado OneGuide (Google Doc `1S5VFYJ1dI7hckrHl1evB8ffNTXhJgxzMsPIhlo_d-Q4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Carquest Auto Parts — Processing Guide

> **Source:** Carquest Auto Parts OneGuide (Google Doc `1-C6wxfGw_Flvg6fsUzYwYuy_C0aWwz3xFy5aifbKNM8`), updated Jun 22, 2026. Contacts/credentials omitted.

> **Bilingual (EN/FR):** English zone → ON stores, French zone → QC stores.

## Account at a glance

| | |
|---|---|
| Slack channels | `#1p-carquest-canada` |
| Flyer types | Direct (12203) |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **Files received:** ad-hoc. **Linking document:** no.
- **Cadence:** Available From Saturday · Available To Friday · Valid From Friday · Valid To Saturday.

## Upload & setup (owned by DOC)

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP. Auto-Group or add page numbers; **ensure correct language (English AND French pages).** Save & Confirm — **do NOT process internally.**
- **Pricing Zone Creation:** 1 English zone (add all **ON** store set) + 1 French zone (add all **QC** store set).

### Setup QC
- Confirm all pages uploaded (Items View); check SFTP for un-uploaded pages. Confirm dates (usually first/last page). Thumbnails 4 Standard; set preview dates.

## ⚠️ Common errors / risk items
- **Look for multiple products** (multi-item boxes).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Exclude everything special:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC (Low; Auto-tag OFF)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.**

### Image QC
- PDF preferred if clean; otherwise cutouts accepted.

## FQC (owned by DOC)
- Confirm dates vs PDF (listed on the cover page); availability toggles; thumbnails include logo.
- Standard checks (all boxed/tagged, spotchecks 20% of pricing zones, previews clickable, sessions complete, geography correct).
- **Flyer Review type: Lite.**

---
*Source: Carquest Auto Parts OneGuide (Google Doc `1-C6wxfGw_Flvg6fsUzYwYuy_C0aWwz3xFy5aifbKNM8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Carter's Osh Kosh — Processing Guide

> **Source:** Carter's OshKosh OneGuide (Google Doc `1PPAMSSJ3iKdId2tGIbtQGjCufxBTnaf9LWNXN_Fql7c`), updated Dec 18, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#carters-osh-kosh`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer (7601) — **ad hoc** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |
| Linking document | Yes — used for both Box and Tag |

## Files & schedule

- **When files arrive:** ad hoc. Files usually sent to BD contact; pages may need to be added to the SFTP by the processor if the client sends over email.
- **Cadence:** Available/Valid From/To all ad hoc.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (Flex)

- **Manual Upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure the correct language is selected. Save & Confirm. **Do NOT process internally.**
- **Pricing Zone Creation:** create English and French pricing zones, select all applicable pages, Save & Confirm, then add all stores to both zones.

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **RISK:** if uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.
- Confirm flyer dates (usually first or last page). Complete thumbnails (4 Standard). Ensure all preview dates are set.

## ⚠️ Common errors / risk items
- Look for **multiple products** in one image (box/tag separately).
- URL risk: a URL provided in the linking sheet but **not tagged** is an incorrect tag/QC issue.

## QC specifics

- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Medium; Auto-tag OFF):** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Include name, description, URL, sale story and percent off wherever applicable; tag URLs (links) using the URL linking document attached to vendor tasks.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- Standard pricing spotchecks in pipeline.

## Post-processing / FQC
- Item Image QC (Flex) — PDF preferred, else cutouts.
- Pre-FQC (DOC): dates match PDF, availability toggles correct, thumbnails include retailer logo, all items boxed/tagged, spotchecks (20%), previews clickable, sessions complete, geography correct.
- **Flyer Review type: Lite** (Flex).

---
*Source: Carter's Osh Kosh OneGuide (Google Doc `1PPAMSSJ3iKdId2tGIbtQGjCufxBTnaf9LWNXN_Fql7c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Castle Atlantic — Processing Guide

> **Source:** Castle Atlantic OneGuide (Google Doc `1ATIjAxVEwsI3r1Cg3vbTEjD6wG1UndYETTcLcZtG65M`), updated Oct 24, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#1plat_castleatlantic` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly (files ad hoc) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |
| Linking document | N/A |

## Files & schedule

- **When files arrive:** ad hoc. Pages may need to be added to the SFTP by the processor if the client sends over email.
- **Cadence:** Available/Valid From/To all ad hoc.
- **Workflow:** Upload & Setup (Flex) → FQC (Flex).

## Upload & setup (Flex)

- **Manual Upload:** Pages Tab → Edit → select all pages from the SFTP menu (or upload manually from email if needed) → Confirm & Upload. Auto-Group or manually enter grouping numbers; **language = English.** Save & Confirm.
- **Pricing Zone Creation:** create Base pricing zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **RISK:** if uploading from SFTP, confirm no SFTP pages were left un-uploaded.
- Confirm flyer dates (usually first or last page). Complete thumbnails (4 Standard).

## ⚠️ Common errors / risk items
- Look for **multiple products** in one image (box/tag separately).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **Include** packaged deals. **Exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON, PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, Image QC. **Exclude URLs.** Standard: large title text = Name; then Price; any other text in Description — tag exactly as shown.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- Standard pricing spotchecks in pipeline.

## Post-processing / FQC
- Pre-FQC (Flex): dates match PDF, available on all platforms, thumbnails include retailer logo.
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Castle Atlantic OneGuide (Google Doc `1ATIjAxVEwsI3r1Cg3vbTEjD6wG1UndYETTcLcZtG65M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Centre de Jardin — Processing Guide

> **Source:** Centre de Jardin OneGuide (Google Doc `1cxZpONbMSt94nWNnfR-ho3V9MAcL5xNft3gSpCnkIV8`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#centre-de-jardin` |
| Hosted URL | centredejardinbrossard.com |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |
| Linking document | No (but a Tag/QC-specific linking document is used at box/tag time) |

## Files & schedule

- **When files arrive:** Thursday (often late — live date can be pushed forward). Files arrive by email with links you must add during upload; respond to confirm receipt.
- **Cadence:** Available/Valid From/To — Thursday.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC). Out-of-processing: page swaps.

## Upload & setup

- **Manual Upload:** Pages Tab → Edit → select pages from SFTP (or upload from email) → Confirm & Upload. Auto-Group or enter grouping numbers; language = English. Save & Confirm.
- **Pricing Zones:** PZ 1 = ENG (all English pages in order); PZ 2 = FR (add all ENG pages then toggle "Cross-Language" and select French). Save & Done. **Add all stores to both PZs.**
- **Attach tagging document** to all vendor tasks (Vendors → upload mass attachment → select all vendors, choose the xls). Usually sent via email — flag processor if not attached to ClickUp.
- Wait for sessions to run. **Ensure the same number of pages in the ENG and FR PZs.** Thumbnails — Standard 4.

### Setup QC
- Dates match first page of PDF; No Theme; available everywhere.

## ⚠️ Common errors / risk items
- ENG and FR pricing zones must have the **same page count** — a frequent slip.
- Every link must be checked at FQC using the correct EN or FR tab of the linking doc.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Tag/QC-specific linking document required.
- **Image QC:** standard.

## Post-processing / FQC (DOC)
- **Check URLs:** open linking document attached to Vendor Tasks, review every link on each page using the correct EN/FR tab, then add comment "All links checked".
- QC thumbnails (Standard 4 — stock premium, storefront carousel premium/organic).
- Edit Details: available everywhere; no external run name; run dates match last PDF page.
- Check items without URL. Flag missing pages or geography changes to the full-time team.
- **Flyer Review type: Lite** (Flex).

## Out-of-processing
- Page swaps (see video reference in OneGuide).

---
*Source: Centre de Jardin OneGuide (Google Doc `1cxZpONbMSt94nWNnfR-ho3V9MAcL5xNft3gSpCnkIV8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Centre du Travail — Processing Guide

> **Source:** Centre du Travail OneGuide (Google Doc `1Vg5lIVKqJz_-PbZ5tIpQrl7dwAT5tAezn2pPpYh3Q-c`), updated Jun 1, 2026. Contacts/credentials omitted.

> **Note:** This OneGuide covers the Chaussures Pop / Go Sport processing family (Flyer 10910). Content mirrors the Chaussures Pop guide.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | `#chaussures-pop-go-sport`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer Type 1 — Go Sport — Flyer 10910; **ad hoc** |
| Processing | Auto-stack; 3FL; no coupons; no Feedel |
| Linking document | Yes — for URLs |

## Files & schedule

- **When files arrive:** ad hoc. Pages may need to be added to the SFTP by the processor if the client sends over email.
- **Cadence:** Available/Valid From/To all ad hoc. Preview date N/A.
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## Upload & setup (Flex)

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload. Auto-Group or enter grouping numbers; **all pages French only.** Save & Confirm. **Do NOT process internally.**
- **Pricing Zone Creation:** create Base pricing zone, select all applicable pages, Save & Confirm, add all stores.
- **Linking Document:** ensure the corresponding linking document from the FTP is attached to all vendor tasks; if none, flag to Coordinator.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View); **RISK:** confirm no SFTP pages left un-uploaded.
- Confirm flyer dates. Thumbnails (4 Standard). **Leg Heights 60/40.**

## ⚠️ Common errors / risk items
- Look for **multiple products** per image.
- **Copy the item name from the URL document** attached in vendor tasks. If no URL document is attached, flag to Processor or Lead.
- For items with **multiple colour options**, ensure the correct link is applied — open the link and confirm the colour/style matches.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** Box each item individually; use text boxes if necessary. **Multiple colours, one price:** box each image separately. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. (Chaussures Pop and Go Sport handled the same way.)
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include brand, name (copy from URL doc), pre/postfix, SKU, price, categories, URLs; include valid dates / description / sale story / disclaimer / original price if available.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- Standard pricing spotchecks in pipeline.

## Post-processing / FQC (Flex)
- **Check URLs:** almost all items should have a URL; if an item has none, double-check the link sheet. Some items are simply not listed — no URL is fine then.
- Confirm dates vs PDF, availability toggles, thumbnails include retailer logo.
- **Flyer Review type: Lite.**

---
*Source: Centre du Travail OneGuide (Google Doc `1Vg5lIVKqJz_-PbZ5tIpQrl7dwAT5tAezn2pPpYh3Q-c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Centre Hi-Fi — Processing Guide

> **Source:** Centre Hi-Fi OneGuide (Google Doc `1TbItc_0yRM6EpHA1KwV9QPTF9tS_vMzTc3ZCOoYu_DA`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#centrehifi` |
| Hosted URL | centrehifi.com/en/flyer |
| Flyer type(s) & cadence | Weekly Flyer (files Tuesday; Available Friday, Valid Thursday) |
| Processing | Auto-stack; DOC-owned processing; no coupons; no Feedel |
| Resources | Centre Hi-Fi Codesheet Generator |

## Files & schedule

- **When files arrive:** Tuesday. Available From Friday / Valid From Thursday.
- **Workflow:** Upload & Setup (DOC, 3 days out) → FQC (DOC, 1 day out).

## Upload & setup — codesheet build (via Codesheet Generator)

- Files received via email → download → upload to SFTP. Split-Out Upload can begin once files are in the SFTP.
- In the **Codesheet Generator**: from the Stale, copy the **ENG** ("ANG") file name from the beginning to the second underscore; paste into cell **B3** of the Start Here tab. Copy the corresponding **French** file-name portion into **B4**. **Verify the files' run dates match the flyer run.**
- Determine total pages (highest broken-out page number, or open the main SFTP doc). In the "Codesheet" tab, copy Column A down to the required page count. Create a new tab named the Valid-From date and paste **values only** (Cmd+Shift+V). Download as **.CSV**.
- **Upload codesheet:** Name `Codesheet`; Config Name **`generic_language`**; PDF Base Directory = stale path of the pages broken out.
- **Toggles: all EXCEPT 2 (Region Assignment) and 7 (Combine Zones).**
- Save → Run/Process Codesheet. Confirm **two separate pricing zones** with identical page and store counts, then mark "Flyer Creation" complete.

### Linking document manipulation
- Download the linking doc from the SFTP (e.g. `EXPORT_PROMO_SAVE_CA...xlsx`). Hide the `PROMO_TEXT_FR` and `LINK_FR` columns, save with **ENG** in front of the name. Undo, then hide the ENG columns and save with **FR** in front. Attach both documents to all vendor tasks.

### Setup QC (Vendor)
- Leg heights **40/30**; thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **TV Stands must be boxed and tagged separately** — often pictured with/over a TV but are separate items with separate pricing.
- **EN vs FR boxing differs:** the EN flyer boxes+tags **every Centre Hi-Fi logo** on top of each page and links them; the FR does not (no website linking on top). Expect EN to have many more boxed items — this is normal.
- **Both versions:** first page → tag top website; last page → website, store locator, social media links.
- **TVs with multiple items but no pics:** tag the TV as an item and the main text as a Text Box; the remaining items are items.
- Categories: FR pages usually have categories but EN often won't (stereos = home audio; main categories: portable audio, home audio, TV). Leave last page and financing page blank.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Include** packaged deals, sign-up page (box Store Locator, usually last pages), special weblinks (box "Locate your nearest store" and the "Register to Receive Our Bargains…" text). Box all items with a price; use text boxes when necessary. **Exclude** coupons, retailer logo, social media.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Tag MSRP pricing in the Description field.** URLs: match item to the Excel by PAGES and SPECIAL_PRICE; enter `LINK_FR` for French pages, `LINK_EN` for English. Sign-up page uses `centrehifi.com/en/pg-courriels` (EN) / `centrehifi.com/fr/pg-courriels` (FR). Store Locator: EN `centrehifi.com/en/store-locator/`, FR `centrehifi.com/magasin-electronique/`.
- **Image QC:** no PDFs — **item cutouts** only.
- **Item Category QC (Vendor):** every item needs a category; most items here = "Electronics".

## FQC (DOC) / go-live
- Overview details: no external run name; no theme generally; hidden-in-hosted no longer applies (unhidden July 2023); call-outs = front page.
- Leg heights 40/30; thumbnails Standard 4; item images all cutouts.
- **Flyer Review type: Lite** (Flex).

## Out-of-processing
- Ad-hoc page swaps (DOC) — standard "baseline" process.

---
*Source: Centre Hi-Fi OneGuide (Google Doc `1TbItc_0yRM6EpHA1KwV9QPTF9tS_vMzTc3ZCOoYu_DA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chalo ON — Processing Guide

> **Source:** FreshCo/Chalo (ON) OneGuide (Google Doc `1qc79CgJuSoczAJXmum4YTGmWxqt_ODwgZWALMaZGCTM`), updated Oct 24, 2025. Contacts/credentials omitted.

> **Note:** This OneGuide covers the Sobeys **FreshCo & Chalo (Ontario)** banners together. FreshCo = flyer type 502; Chalo = flyer type 3654. They **share pages**.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | freshco.com |
| Flyer type(s) & cadence | FreshCo 502 Weekly · Chalo 3654 Weekly |
| Processing | Auto-stack; 3FL; OS setup; **Feedel/retailer data services YES**; no coupons |

## Files & schedule

- **When files arrive:** Tuesday or Wednesday. Available From Wednesday / Valid From Thursday.
- **Workflow:** Upload & Setup (Vendor) → FQC (Vendor).

## Upload & setup

### FreshCo ON (502) — codesheet upload
- Search "code" in the FTP, download the xls (e.g. `FreshCo ONT_WK07_Zone Code_REV_fordigital.xlsx`).
- Delete the **Zone 2** column (Chalo) and any other Chalo column; delete secondary publication callouts; delete the pages column; **rename the "Position" column to "Pages"**; delete extra items at the bottom; set everything in column A to "Flyer"; rename pricing-zone titles to **Zone #** (Zone 1, Zone 3…). Save/download.
- **Upload:** Name `pages`; Config Name **`sobeys_safeway`**; Base Path = FreshCo ON FTP path; **unmark the first 2 boxes and the last box (only 4 selected)**; Save & process.

### Chalo ON (3654)
- Open the Zone Code sheet from the SFTP; **manually upload pages** using the zone code sheet. **Make sure all pages are added for all Chalo zones.** Save & complete → Flyer Creation. Create pricing zones per the Zone Code doc (e.g. Zone 2). Mark Flyer Creation complete.

### Setup QC
- **FreshCo:** pricing zones = Zone 1, Zone 3, Zone 5…; verify pages against the Zone Code doc (highlighted pages after Zone 1 are zone-specific). Build a **generic stores codesheet** from the Distribution Recap — Name `Stores`, Config **`generic_stores`**, Base Directory `/`, **first box only**, Save & process. External Run Name = "Weekly eFlyer + valid dates"; No Theme; Key Messages = "Weekly Specials"; set vendors to High.
- **Chalo:** add all stores (confirm via Zone Summary/Distribution Recap if >1 PZ); check page 1 for dates; vendors High; No Theme; external run name + Weekly Specials; verify page order.

## ⚠️ Common errors / risk items
- **"Pages have already been uploaded"** — usually because Chalo (Z2) shares pages and is already uploaded. If Chalo pages are up you may **Force Processing**; if not, **DO NOT** force — flag the issue.
- **"The following files matched multiple files on the FTP"** — retailer uploaded the same page multiple times. Confirm duplicates in the SFTP, then force processing; verify pricing zones have correct pages before completing.
- **"Undefined method 'merchant' for nil"** — copy the Zone Code sheet into a Google Sheet (paste values only), name it the flyer run, download as xlsx, then do a **manual upload**.
- Store codesheet errors → check for overlapping stores; if two zones (Zone 1 + Zone 3) error, delete Zone 3 and add those stores manually. If stores can't be added, flag and continue — flyer can process without stores.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** box all items attached to the price, include as much of the image as possible; multiple items with one price go in the same box. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price. **Exclude description, SKU, URLs.** Pre/postfix e.g. "Scene+ Member Pricing"; disclaimer e.g. "7.99 without Scene+ Card".

## Post-processing (3FL, Mondays — verify completion)
- **Item Category QC:** one category per item; add **Scene+** category to items with Scene+ callouts.
- **Item Image QC:** clean PDF preferred; use cutout only if no clean PDF.
- **Scene+ Points QC:** all Scene+ sale stories read "xxx Scene+ PTS when you buy x"; add Scene+ category to any missing items (Item Search: Sale Story contains "PTS").
- **Deep Links** (new process 02/25/2025): check the Sobeys Insert Tracker "Deep Links" tab; tag the banner/item **as a link** with SKU + link; dates in red get no deep links. Watch for store/FSA/PZ-specific tiles and specific valid dates (use Create Trigger for later go-live; file an OPTICS ticket if you create triggers).
- **Custom Tiles** (DOC): check `#sobeys` Slack; Override Thumbnail (or Create Trigger) on Storefront Premium / Storefront Carousel Premium.

## FQC (Flex/DOL)
- Autostack spotcheck; **confirm stores added** (Chalo should total **7 stores**); storefront spotcheck; leg heights 40/35; item image QC (uncheck composites & PDF); QC thumbnails (4 standard + `first_page_thumbnail_400w`); page categories (all but page 1); add inserts from the Sobeys Insert Tracker and add to PZ; if a "Proudly Canadian" insert is present, box and tag it (link `chalofreshco.com`). Check sessions/errors. **Ensure pages are in correct order** (verify PZs against the Zone Code sheet).
- **Flyer Review type: Lite** (DOL).

## Out-of-processing
- **Page swap:** Pages tab → Edit → select new page from FTP → add "REV" to the name → Save & Complete → Copy Items from old page (same page only, adjust changed items) → box/tag → add to PZ.
- **Cloning:** Chalo ON was cloned weekly to feature on the FreshCo hosted experience — **cloning discontinued as of Jan 20, 2026.**

---
*Source: Chalo ON OneGuide (Google Doc `1qc79CgJuSoczAJXmum4YTGmWxqt_ODwgZWALMaZGCTM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chalo WST — Processing Guide

> **Source:** FreshCo/Chalo West OneGuide (Google Doc `1hKAnstZeGuR62Q4Mz7QqjHbslsBFwfkehmeg6X1lO_Y`), updated Mar 11, 2026. Contacts/credentials omitted.

> **Note:** This OneGuide covers the Sobeys **FreshCo & Chalo West** banners together (flyer type 9130). FreshCo and Chalo WST **share the same codesheet + distribution recap**.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | freshco.com |
| Flyer type(s) & cadence | Weekly West (9130); files Tuesday, Available From Wednesday / Valid From Thursday |
| Processing | Auto-stack; Flex (Processing Support); **Feedel/retailer data services YES**; no coupons |

> **⚠️ FreshCo & Chalo West main flyers are AVAILABLE EVERYWHERE and AVAILABLE + VALID AT 3AM.**

## Files & schedule

- **When files arrive:** Tuesday.
- **Workflow:** Upload & Setup (Vendor, 5 & 4 days out) → FQC (DOC).

## Upload & setup

### FreshCo West (9130) — codesheet
- In the FTP search "west", hide uploaded. Two files: **codesheet + distribution recap** (shared by both banners).
- **Manipulations:** delete Zone 2 and any other Chalo zones; delete secondary callouts; delete pages column; **rename "Position" → "Pages"**; delete extra items at bottom; column A = "Flyer"; pricing-zone titles → **Zone #**.
- **Upload:** Name `pages`; Config **`sobeys_safeway`**; Base Directory = FTP file path; **Toggles 3, 4, 5, 6**; Save & process. Process Chalo and FreshCo **at the same time** to avoid the "pages already uploaded" warning. Mark Flyer Creation complete.

### Chalo West (9130) — codesheet
- Delete the FreshCo columns; change headers to **Zone #** in chronological order; column A = "flyer"; **flap pages** (FL_1 / FL_2 in the file name) must be moved to after page 1 — cut the row of page-1s in every zone and paste above the flap pages. Save as .xlsx.
- **Upload:** Name `pages`; Config **`sobeys_safeway`**; Base Directory = FTP path; **Toggles 3, 4, 5, 6**; Save & process.

### Stores (Distribution Recap → generic_stores)
- New Excel: A1 = `stores` (lowercase, plural), B1 = `pricing zone` (lowercase); paste store codes per zone under A; write `ZONE #` in B to match the codesheet (**case-sensitive**). Skip Chalo zones for FreshCo. Save as .csv.
- **Upload:** Name `stores`; Config **`generic_stores`**; Base Directory `/`; **first toggle only.**
- **Chalo stores:** add manually into the correct PZ per the distribution recap.

### Setup QC (Flex)
- Let sessions run; add stores (FreshCo via generic codesheet; Chalo manually); set vendor tasks to high; check off unused FTP files; merge pages in storefront spotcheck if applicable; mark autostack spotcheck complete.

## ⚠️ Common errors / risk items
- **"Pages have already been uploaded"** — shared pages with the other banner. If the other banner's pages are up you may Force Processing; otherwise **DO NOT** force — flag.
- **"Files matched multiple files on the FTP"** — duplicate pages uploaded by retailer; confirm in SFTP then force processing.
- **"Undefined method 'merchant' for nil"** — copy Zone Code into a Google Sheet (values only), download xlsx, do a manual upload.
- If **Chalo codesheet errors**, manually upload the pages. Watch for filename mismatches (extra spaces) between codesheet and FTP; **bolded characters won't process in fadmin.**

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price. **Exclude description, SKU, URLs.** Pre/postfix e.g. "Scene+ Member Pricing"; disclaimer e.g. "7.99 without Scene+ Card".

## Post-processing (3FL, Mondays — verify completion)
- **Item Image QC:** clean PDF preferred, else cutout.
- **Category QC:** one category per item; Scene+ category for Scene+ callouts.
- **Scene+ Points QC:** sale stories read "xxx Scene+ PTS when you buy x"; add Scene+ category to missing items.
- **Deep Links:** Sobeys Insert Tracker "Deep Links" tab; tag as a link with SKU + link (red dates = none).
- **Custom Tiles** (DOC): `#sobeys` Slack; Override Thumbnail / Create Trigger on Storefront Premium & Carousel Premium.

## FQC (Flex)
- Available everywhere, **Available + Valid at 3AM**; autostack spotcheck; confirm stores added (Chalo = **7 stores**); no theme; external run name = "FreshCo Weekly eFlyer mm/dd - mm/dd" / "Chalo Weekly eFlyer mm/dd - mm/dd"; leg heights 40/35; item image QC (uncheck composites & PDF); **6 thumbnails** (Standard 4 + thumbnail 2-page + `first_page_thumbnail_400w`); page categories; add inserts to PZ; box/tag "Proudly Canadian" insert if present (link `freshco.com` / `chalofreshco.com`); check sessions/errors; **ensure pages in correct order** (usually the DIG pages; verify PZs against the Zone Code sheet).
- **Flyer Review type: Lite** (DOL).

## Out-of-processing
- **Page swap:** standard REV process (Pages → Edit → new page → add "REV" → Copy Items → box/tag → add to PZ).
- **Cloning:** Chalo WST was cloned weekly to the FreshCo hosted experience — **cloning discontinued as of Jan 20, 2026.**

---
*Source: Chalo WST OneGuide (Google Doc `1hKAnstZeGuR62Q4Mz7QqjHbslsBFwfkehmeg6X1lO_Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chatters Salon — Processing Guide

> **Source:** Chatters Salon OneGuide (Google Doc `1ISxN1zpMO800op67GfbkfrYRB9485hHXn94wIeAmG1E`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#chatters`, `#flex-processingsupport` |
| Hosted URL | chatters.ca/flyer |
| Flyer type(s) & cadence | Flyer Type 1 (4215); files Monday, Available/Valid From Thursday, Valid/Available To Wednesday |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |
| Linking document | Yes |

## Files & schedule

- **When files arrive:** Monday. Live Thursday–Wednesday.
- **Workflow:** Upload & Setup (Flex) → FQC (Flex).

## Upload & setup (Flex, manual)

1. **One pricing zone** — apply all stores.
2. Ensure the correct front page is in and **create triggers** for any page with special valid dates.
3. Attach the linking doc to all vendor tasks.
4. No theme; Standard 4 thumbnails.
5. Content-policy check: on average ~3 items per page × number of pages — compare to what's there.
6. Setup QC checklist.

## ⚠️ Common errors / risk items
- **Triggers are heavy on this account.** There will be several pages requiring triggers: (1) trigger page inserts, (2) trigger page removals, (3) trigger page swaps. The files outline date validity and page position. An **OPTICS ticket** must be created and assigned to the Lead + Coordinator for visibility.
- **Linking-doc manipulation:** delete the URL column; include only the **Campaign URLs** column as **plain text** (it is often concatenated).
- **URLs:** check the item **name** before adding a URL; after adding, confirm the link leads to the correct item — if incorrect, remove and leave blank. Ensure descriptions include the PDF info (size if available) plus the linking-document info.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** box **only items that are in the linking document.** **Include** social media (icons, usually last page) and special weblinks — box "Find a location" and the website text (usually last page). **Exclude** coupons, packaged deals, retailer logo, sign-up page.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.**
- **Known URL/name pairs (link → name):** `chatters.ca/` → Chatters; `locations.chatters.ca/` → Find a location; Facebook, Twitter, Instagram, Pinterest, TikTok links each named accordingly.
- **Image QC (DOC):** select the PDF image; if the item is cut off or has a non-white background, use the cutout.

## Post-processing / FQC (DOC)
- Mark Autostack complete; page categories (pick closest, skip p.1); Item Search **URL is blank** → use the linking doc to add missing URLs (leave blank only if truly none; socials from vendor guide); images PDF where available (scan cutout vs PDF); **spot-check linking-doc item count vs items on page**; **delete any boxed items not on the linking document**; verify descriptions from linking doc were added; check link-outs on Vertical & Horizontal Scroll; **set page triggers for new pages**; check pages/vendor tasks/sessions.
- Flyer shell dates are pre-set — you often won't see valid dates on the actual pages; that's fine to ignore.
- **Flyer Review type: Lite** (Flex).

---
*Source: Chatters Salon OneGuide (Google Doc `1ISxN1zpMO800op67GfbkfrYRB9485hHXn94wIeAmG1E`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chaussures Pop — Processing Guide

> **Source:** Chaussures Pop OneGuide (Google Doc `1egaNObG7EelYBBI-yV5Od5a29_VJSOnmhQIGshYpu-Y`), updated Mar 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#chaussures-pop-go-sport`, `#flex-processingsupport` (FQC only), `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer Type 1 — Go Sport — Flyer 10910; **ad hoc** |
| Processing | Auto-stack; 3FL; no coupons; no Feedel |
| Linking document | Yes — for URLs |

## Files & schedule

- **When files arrive:** ad hoc. Pages may need to be added to the SFTP by the processor if the client sends over email.
- **Cadence:** Available/Valid From/To all ad hoc. Preview date N/A.
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## Upload & setup (Flex)

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload. Auto-Group or enter grouping numbers; **all pages French only.** Save & Confirm. **Do NOT process internally.**
- **Pricing Zone Creation:** create Base pricing zone, select all applicable pages, Save & Confirm, add all stores.
- **Linking Document:** ensure the corresponding linking document from the FTP is attached to all vendor tasks; if none, flag to Coordinator.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View); **RISK:** confirm no SFTP pages left un-uploaded.
- Confirm flyer dates. Thumbnails (4 Standard). **Leg Heights 60/40.**

## ⚠️ Common errors / risk items
- Look for **multiple products** per image.
- **Copy the item name from the URL document** attached in vendor tasks. If no URL document is attached, flag to Processor or Lead.
- For items with **multiple colour options**, ensure the correct link is applied — open the link and confirm the colour/style matches.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** box each item individually; use text boxes if necessary. **Multiple colours, one price:** box each image separately. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. (Chaussures Pop and Go Sport handled the same way.)
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include brand, name (copy from URL doc), pre/postfix, SKU, price, categories, URLs; include valid dates / description / sale story / disclaimer / original price if available.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- Standard pricing spotchecks in pipeline.

## Post-processing / FQC (Flex)
- **Pre-FQC:** check URLs — almost all items should have one; if an item has none, double-check the link sheet (some items are simply not listed, which is fine). Confirm dates vs PDF, availability toggles, thumbnails include retailer logo. Standard checks: all items boxed/tagged, spotchecks complete, previews clickable, sessions complete, geography correct.
- **Flyer Review type: Lite.**

---
*Source: Chaussures Pop OneGuide (Google Doc `1egaNObG7EelYBBI-yV5Od5a29_VJSOnmhQIGshYpu-Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chevron / On The Run — Processing Guide

> **Source:** Chevron / On The Run OneGuide (Google Doc `1El0hORzuV4-hzYT9pbk-0Zg3tRV7co7zwBVjpcW94d0`), updated May 6, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (**currently not powering Hosted**) |
| Slack channels | N/A |
| Hosted URL | N/A |
| Flyer type(s) | Direct Flyer (ID 11571) — **ad-hoc** |
| Processing | Auto-stack; DOC owns setup & FQC; no Flex; no coupons; no Feedel |

## Files & schedule
- **Files received:** ad-hoc. Pages may need to be added to the SFTP by the processor if the client sends files over email.
- No preview date, no linking document.

## Upload & setup (owned by DOC)
- **Manual upload:** Pages → Edit → select all pages from SFTP → Confirm & Upload → Auto-Group or manual grouping numbers → ensure correct language per page → Save & Confirm. **Do NOT process internally.**
- **Pricing zones:** create **one English (title "ENG") and one French (title "FRE")** zone; add all pages to each.
- **Stores:** add per retailer store documentation using a **Generic Stores Codesheet**. In a blank sheet, column "stores" = store codes from the retailer list, column "pricing zone" = ENG/FRE. If no new store list is provided, reuse the previous run's codesheet and bump the processor.
- **Setup QC:** confirm all pages uploaded (Pricing Zone → Items View; **RISK — check no un-uploaded SFTP pages remain**); confirm flyer dates (usually first/last page); Standard 4 thumbnails; preview dates set.

## Box Draw (Low — Auto-Box OFF, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box individual items separately; separate items in banners are boxed individually.
- Risk item: **look for multiple products.**

## Tag / Tag QC (Low; Auto-tag OFF)
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs. Brand used for both Box/Tag.

## Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted.

## Pre-FQC / FQC (owned by DOC)
- Confirm dates (defer to email if not on PDF); availability toggles — available everywhere (**Hosted URL error is OK**); thumbnails include retailer logo; all items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions complete; Geography correct.
- **Flyer Review type: Lite.**

---
*Source: Chevron / On The Run OneGuide (Google Doc `1El0hORzuV4-hzYT9pbk-0Zg3tRV7co7zwBVjpcW94d0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chico — Processing Guide

> **Source:** Chico OneGuide (Google Doc `1DLEp1Fo9TUUdaUyWDFUDzL6w96tlDiiBSpW6bxqOchY`), updated Nov 28, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#chico` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer 10874 — Monthly ad hoc |
| Processing | Auto stack; Flex/OS N/A; no coupons; no Feedel |
| Linking document | In FTP (URL document per week's flyer) |

## Files & schedule

- **When files arrive:** ad hoc. Available From Tuesday / Valid From Thursday; Available/Valid To Sunday. **Always set a 2-day preview.**
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC).

## Upload & setup (Vendor)

> **As of Mar 31, 2025:** separate English and French PDF files — **no more cross-language for the EN PZ.**

1. **Manual Upload:** Pages Tab → Edit → select relevant files. Language: **French** (pages with FR in name), **English** (pages with EN in name). Save only → Autogroup → Save & Continue.
2. **Pricing Zones:** PZ 1 — Name `FR`, Language French; PZ 2 — Name `EN`, Language English. Save & Continue.
3. **Stores:** add all to both zones.
4. Wait for sessions to run and vendor tasks to load.
5. Check the merchant FTP for a **URL document** for that week's flyer; if present, attach to all vendor tasks with the note: "Please use attached URL document to tag specified banners/items with corresponding URLs."
6. Edit Details: **2-day preview**, available on all platforms.
7. Standard 4 thumbnails → Setup QC.

## ⚠️ Common errors / risk items
- **One-page flyers must have at least 6 boxed/tagged shoppable items** or they fail content policy and cannot go live. If vendors tagged multiple flavours/sizes together (e.g. a can of cat food with several flavours), **re-box so each flavour/size is tagged separately** (mark all vendor tasks complete + "Autostack Spotcheck" complete, then Pages tab → Box QC). Flavour/size names come from the item titles/descriptions on the PDF.
- **Always check both vendor tasks AND the FTP for a URL document** — easy to miss; if present, confirm the specified items/banners were tagged with the corresponding URLs.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** box all sales callouts and priced items; exclude the retailer logo and any banner without pricing. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price; URLs if a linking document is attached. **Exclude disclaimer.** Tag deals (e.g. "3 for $8") correctly.
- **Item Category QC (Flex):** EN/FR pairs — Dogs/Chien, Cats/Chat, Rodents/Rodents, Fish/Poisson.
- **Image QC:** select clean PDF images; cutout if no clean image.

## FQC (Flex)
- Autostack spotcheck complete; item image QC (usually cutouts, better PDF if available); item + page category QC; thumbnail QC; available on all platforms; **2-day consumer preview**; check vendor tasks and FTP for the URL document; enforce the **6+ shoppable items** rule for one-page flyers.
- **Flyer Review type: Lite** (Flex).

## Out-of-processing
- Page swaps (DOL) — standard "baseline" process.

---
*Source: Chico OneGuide (Google Doc `1DLEp1Fo9TUUdaUyWDFUDzL6w96tlDiiBSpW6bxqOchY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Choices Market — Processing Guide

> **Source:** Choices Market OneGuide (Google Doc `1pD10BZQQkOkAhbJ7Xh8UH7mA2u38SOX6PSnNmJqXOOs`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#choicesmarkets`, `#flex-processingsupport` |
| Hosted URL | shop.choicesmarkets.com/sm/pickup/rsid/20000/circular |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly (plus a Monthly newsletter) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |
| Linking document | N/A |

## Files & schedule

- **When files arrive:** Friday, straight into the SFTP. Live Thursday–Wednesday (no preview). 4–6 pages, one version.
- **Workflow:** Upload & Setup (Flex) → FQC (Flex).

## Upload & setup (Vendor)

**Weekly flyer:**
1. Manual Upload (mark off the main PDF in the FTP after uploading all pages).
2. **Two pricing zones:** **Base** = all stores except Parksville, assign all **LM** pages; **Parksville** = Parksville store only, assign all **PV** pages.
3. Available everywhere; no theme; mark setup QC complete.

**Monthly flyer:** same as weekly except **Hosted only** and **External Run Name** = the month's newsletter name (e.g. "September Heartbeet").

## ⚠️ Common errors / risk items
- **Two pricing zones required** — Base (all stores except Parksville, LM pages) and Parksville (Parksville only, PV pages). Don't collapse them.
- **One item with two prices/sizes must be boxed and tagged as two separate items** (e.g. Natural Laundry Detergent at $5.99 for 1.4L and $12.99 for 4.43L → one box per price).
- **RISK — Flyer Sorting** must be completed on the merchant's main page: ensure the **weekly newsletter sorts before the monthly newsletter** (drag line items into the correct order).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Include** retailer logo; draw a separate box for each item price. **Exclude** coupons, packaged deals, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Include name, description, price, sale story, disclaimer, original price. **Exclude pre/postfix, valid dates, SKU, categories, URLs.**
- **Spotchecks:** pricing discrepancies — always defer to the PDF.

## FQC (Flex)
- Autostack spotcheck complete; Standard 4 thumbnails; Monthly Newsletter — logo boxed and tagged; in Pricing Zone tab use item view to confirm every item is boxed (split any item with two prices into two boxes/tags); confirm geography consistent; **confirm two pricing zones (Parksville + Mainland)**; complete **Flyer Sorting** (weekly before monthly).
- **Flyer Review type: Lite** (Flex).

## Out-of-processing
- Page swaps — standard "baseline" process.

---
*Source: Choices Market OneGuide (Google Doc `1pD10BZQQkOkAhbJ7Xh8UH7mA2u38SOX6PSnNmJqXOOs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Chuck's Fresh Markets — Processing Guide

> **Source:** Chuck's Fresh Markets OneGuide (Google Doc `1eAf5Q6EE7XXEcHHA8c51AhJCyYcglWhTTq678inmTdA`), updated October 03. Contacts/credentials omitted.

> **Note:** Chuck's Fresh Markets (CFM) and Roth's Fresh Markets (RFM) files are uploaded to the SFTP together. **Chuck's pages are labeled CFM; Roth's pages are labeled RFM.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms — **MUST be available on all platforms (potential CUSAT issue)** |
| Slack channels | `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack; **Flex owns processing** (external comms, upload, FQC, flyer review); OS only completes flyer processing; no coupons; no Feedel |
| Linking document | N/A |
| Account context | Coordinator steps in for page swaps; all communication via the team alias |

## Files & schedule

- **When files arrive:** Thursday. Available From Wednesday / Valid From Thursday; Available/Valid To Wednesday (should match PDF dates).
- **Workflow:** Upload & Setup (Flex, 4 days out) → FQC (Flex).

## Upload & setup (Vendor)

1. Receive files via SFTP + retailer email.
2. **Manually upload all pages** → Auto group → **EN only**.
3. **1 pricing zone = base.**
4. Add all stores.

### Setup QC
- Edit Details: Available/Valid From Thursday, Available/Valid To Wednesday (match PDF); **available on all platforms**; grocery → **NO THEME**.

## ⚠️ Common errors / risk items
- **MUST be available on all platforms — not hidden on Hosted.** This is flagged as a potential CUSAT issue.
- CFM (Chuck's) and RFM (Roth's) share the SFTP — upload only the CFM-labeled pages for this account.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** box all items with prices, including multiple-item blocks. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.**
- **Image QC:** standard.

## FQC (Flex)
- Thumbnail QC; Edit Details — check dates against PDF pages, **available everywhere**; Pricing Zones — all stores added, **1 pricing zone**, all shoppable items boxed, pages in chronological order; Geography — no stores or FSAs/zips added or removed.
- **Flyer Review type: Lite.** Checks: dates same as PDF; available dates = valid dates; available everywhere; pagination order; item boxes; iframe; vertical geography; no change WOW.

## Out-of-processing
- Page swaps — standard "baseline" process (Coordinator steps in).

---
*Source: Chuck's Fresh Markets OneGuide (Google Doc `1eAf5Q6EE7XXEcHHA8c51AhJCyYcglWhTTq678inmTdA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Clore Beauty — Processing Guide

> **Source:** Clore Beauty OneGuide (Google Doc `1vcJqEtEivblv_ZNcA7eQFm_Rp64sFHYXwX3y-d0RFSE`), updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1 — Monthly (11788) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |
| Linking document | N/A |

## Files & schedule

- **When files arrive:** Tuesday. Available From Monday, Available To Sunday; Preview Wednesday.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (Flex)

- **Manual Upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure the correct language is selected. Save & Confirm. **Do NOT process internally.**
- **Pricing Zone Creation:** create Base pricing zone, select all applicable pages, Save & Confirm, add all applicable stores.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View); **RISK:** confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (usually first or last page). Thumbnails (4 Standard). Ensure all preview dates are set.

## ⚠️ Common errors / risk items
- Look for **multiple products** in one image (box/tag separately).
- This OneGuide is largely the standard template — it carries few retailer-specific risk items beyond the generic ones.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- Standard pricing spotchecks in pipeline.

## Post-processing / FQC
- Item Image QC (Flex) — PDF preferred, else cutouts.
- Pre-FQC (DOC): dates match PDF, availability toggles correct, thumbnails include retailer logo, all items boxed/tagged, spotchecks (20%), previews clickable, sessions complete, geography correct.
- **Flyer Review type: Lite** (Flex).

---
*Source: Clore Beauty OneGuide (Google Doc `1vcJqEtEivblv_ZNcA7eQFm_Rp64sFHYXwX3y-d0RFSE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Clover Farms + Clover Farms Ontario — Processing Guide

> **Source:** Clover Farms + Clover Farms Ontario OneGuide (Google Doc `1SScC27emf37pTgSFShXv3pGKtMO0h7DAowVFNnyGN2M`), updated Jul 12, 2025. Contacts/credentials omitted.

Part of the Sobeys family (alongside Co-op and ValuFoods), sharing pages and a combined Flex Flyer Review.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | **Flipp only — NOT available on hosted** |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | sobeys.com |
| Publications | This Week's Flyer / Clover Farm (**3794**) · Clover Farm ONT (**8866/8966**) |
| Cadence | Weekly. Files Monday. Available Wed, Valid Thu–Wed (**CF ONT now shares the same dates**) |
| Processing | Auto-stack; Flex (3FL + Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Files received **Monday**. Get the **Zone list** from the merchant email, download and manipulate.
- **Delete the ValuFoods (Zone 3) and Co-op (Zone 4) columns** → should leave **Zone 1, Zone 2, Zone 5, Zone 6**.
- Save/upload the run list to the OS Setup Files folder. Run list end-date names the flyer (e.g. publication ending Oct 2 → run list "October 2nd").

## Upload & setup

### Clover Farm (This Week's Flyer, #3794) — owned by Vendor
1. Code sheets → Name = `upload`, add zone-list codesheet.
2. **Config Name = `clover_farm`**.
3. PDF Base Directory = up to `/Zone` only (e.g. `/April_6_7_2022`).
4. **Toggle = 1,3,4,6**. Save & run codesheet.
   - If it goes yellow saying pages already uploaded, that's fine (pages are shared with other merchants) → **Force processing**.
5. Pricing Zones created for **Zone 1, Zone 2, Zone 6**; mark Flyer Creation complete.
6. **Manually add Zone 5 page 1:** Pages → Edit → upload Zone 5 Page 1 manually → create Pricing Zone "Biggoods Zone 5".

### Clover Farm ONT (#8866) — manual upload
- **CF-ONT files are now under Zone 7 in the sFTP.**
- Pages → Edit → expand **Zone 7** → select files → **Auto-group** (any pop-up/added page goes at the end) → Save & submit.
- Create Pricing Zone **Zone 7** → "add all" beside **clover ontario** stores.

### Setup QC
- Edit Details: **hidden on hosted**, no theme, key message from the rotating Sobeys list (e.g. "Weekly Ad. Weekly Savings.", "Deals of the Week").
- External run name = **Weekly eFlyer + valid dates** (e.g. "Weekly eFlyer 06/20-06/26"). CF ONT gets 1 extra day.
- **Check dates** (bottom of page 1). **Verify page order in Storefront Spotcheck.** New Zone 5 PZ must have the same page count as the others (usually 8 or 4).
- QC thumbnails (Standard 4). **Box & tag the recipe callout on pg 1** → `http://familyfoods.ca/recipes/`; add a vendor note so it isn't missed.

## ⚠️ Common errors / risk items
- **Page order in Pricing Zones:** confirm all pages uploaded (usually 8). PopUp pages go **at the end**.
- **New Zone 5** must match the other zones' page count.
- Shared-page "already uploaded" yellow warning is expected → force processing.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** all items, recipe callouts, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons. Linking doc required.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude:** disclaimer, URLs.
- **Brand** always entered in both the Brand field and the start of the Name field.
- **Price per weight:** `$$$/kg` in Description, `/lb` in postfix.
- **French:** separated from English by a line break; English description first, then French name on its own line followed by French description.
- Categories from page headings / best judgement (Snacks → Grocery; Household → Home Essentials).

### Image QC
- PDF Image Auto Selection is ON — a PDF should be selected automatically.

## FQC (owned by DOC)
- Autostack spotcheck; confirm **4 pricing zones**; verify page order in Storefront Spotcheck; Zone 5/6 page counts match.
- Edit Details as above; QC thumbnails; box/tag recipe callout if not already.
- **Complete FSA removal + addition — the FSA is `A0H`.**
- Rerun page stitching + page tile generation; check vertical/horizontal preview on PZ.
- **Available start time is 6 AM** for Clover Farms, Co-op and ValuFoods.
- Post-FQC: send preview links to the merchant (Clover Farms + CF ONT).
- **Flyer Review type: Lite** (combined Clover Farms | Co-op | ValuFoods review).

## Out-of-processing (page swap)
- Open run → Pages → Edit → select new page from FTP → add "REV" to the name → Save & Complete → **Copy Items** from the old page (same page only), adjust the changed item(s) → box/tag → add to PZ.

---
*Source: Clover Farms + Clover Farms Ontario OneGuide (Google Doc `1SScC27emf37pTgSFShXv3pGKtMO0h7DAowVFNnyGN2M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Club Piscine — Processing Guide

> **Source:** Club Piscine OneGuide (Google Doc `1LYN1e-YorL7xiokFDooOuNnCPFVy9C3tAinMXzABnqU`), updated May 16, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (**we don't power their hosted**) |
| Slack channel | `#clubpiscine` |
| Hosted URL | clubpiscine.ca |
| Publication | Monthly (**7979**) |
| Cadence | Files Monday. Available Mon, Valid Tue–Mon |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Files received **Monday**; linking document provided. Two flyer runs run at once (split for budget): **Generic** and **Nepean (ON)**.

## Upload & setup (manual; owned by Flex)
1. Pages → Edit → select files. Upload **EN + FR** files to the Generic run; upload **ON** files to the Nepean run.
2. Mark files French → Save → refresh to confirm all FR. Then re-upload same files → mark EN → Save.
3. Autogroup → Save & complete.
4. **Pricing Zones:** Generic run → EN (English) + FR (French); Nepean run → ON (English).
5. Assign stores: Generic EN → add all QC stores; Generic FR → add all QC stores (ignore warning); Nepean Base → add one "ON" store.
6. **Linking document:** split into 1 English, 1 French, 1 ON doc; attach to all vendor tasks.
7. Edit Details: available everywhere, no theme. **Dates are on the back-page disclaimer — client tends to ignore these and follows the dates in their email; if no email, confirm dates.**
8. Leg heights **55/45** (pre-set); thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a single callout.
- **FR linking doc:** sometimes the column headers (Page, Description) are in French → change subtitles to English if needed.
- **FSA overlap between the two runs** — must be manually deduped at FQC (see below).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** special weblinks only. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Draw clean boxes (use the grid). **Do not box any callout without a specific SALE callout.** Linking doc required.

### Tag / Tag QC (Low; Auto-tag OFF)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.
- Name/Description/Categories/URLs come from the attached spreadsheet; price from the item image. Apply unique valid dates and disclaimers where shown.

### Image QC
- Select clean PDF images; most have **black backgrounds**.

## FQC (owned by DOC)
1. Complete outstanding spotchecks.
2. Item Image QC — clean PDFs.
3. Ensure all items boxed/tagged; spotcheck items against the linking doc.
4. Pages → Categories: best judgement.
5. Check pages, vendors, sessions, geography.
6. **Perform FSA Dedupe before completing the checklist** (see below).

### FSA Dedupe (why & how)
- Because the two runs (Generic + Nepean) run simultaneously, some FSAs overlap → a customer in an overlap FSA would see both flyers, so they must be manually deduped.
- Create a **`[DO NOT USE] Club Piscine FSA Dedupe Run`** shell (past date, hidden all channels; upload any 1-page PDF, process internally). Create 2 PZs mirroring the live runs (Nepean → all ON stores; Generic → all QC stores).
- Wait for the "FSA generation" session; this run produces the real FSA distribution. Compare the real run's breakdown-zone FSAs ("unadjusted") against the dedupe run's ("adjusted") in Excel; use `=countif($A$1:$B$999,A1)>1` conditional formatting to flag duplicates. Non-highlighted FSAs are the ones to remove.
- Use FAdmin **Custom Actions → "Remove FSAs"** with the real run's Flyer ID + Pricing Zone ID; paste the non-highlighted FSAs; reload and confirm FSA counts match the test run. Note "custom action to remove FSAs completed." **Repeat for the Generic run.**

- **Flyer Review type: Lite.**

---
*Source: Club Piscine OneGuide (Google Doc `1LYN1e-YorL7xiokFDooOuNnCPFVy9C3tAinMXzABnqU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op AG — Processing Guide

> **Source:** Co-op AG OneGuide (Google Doc `1aEUtJIKIoqA-dzuSL5roMs0mZOpvnGRanNTjbsGnqGg`), updated Jun 1, 2026. Contacts/credentials omitted.

Federated Co-op (FCL) banner. Two flyer types: **Rural Routes (3359, Weekly)** — the detailed one — and a **Guide** flyer type (largely a template stub in the source).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | co-op.crs/flyers |
| Publications | Rural Routes Weekly (**3359**); Guide |
| Cadence (Rural Routes) | Files Monday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Rural Routes files received **Monday**; linking document provided.

## Upload & setup — Rural Routes (owned by Vendor)
1. **Manually upload all pages**; group according to page number.
2. **Flyer Creation → create 6 pricing zones:** Version 1 (NA) N. Alta, Version 2 (SA) S. Alta, **Version 3 (BCPR)**, Version 6 (MB) Manitoba, Version 7 (SS) S. Sask, Version 8 (NS) N. Sask.
   - **Combine Versions 3–5 into Version 3 (BCPR).**
   - Add the correct pages to each zone — **light-grey highlight = store-specific pages**.
3. Add the relevant store set to each pricing zone.
4. If there are inserts, add them manually.

### Setup QC
- **Attach the linking document to vendor tasks via "Mass attachment?"** (e.g. `Wk 06 Rural Routes urls.xlsx`).
- Available everywhere; no theme; 4 standard thumbnails; key message from front page. Setup QC.

## ⚠️ Common errors / risk items
- **6 pricing zones by region** — combine Versions 3–5 into BCPR; watch store-specific (grey-highlighted) pages.
- **Look for multiple products** in a callout.
- Special weblink `https://www.agro.crs/`.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; Box Draw/Box QC linking doc)
- **Include:** special weblinks (e.g. `https://www.agro.crs/`). **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.

### Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** pre/postfix, valid dates.
- Example: Brand "STP", Name "Octane Booster", Description "…Treats up to 79 L. 155 mL. (5041 025)", Current Price "5.97", Postfix "EACH", Original Price "8.99", Sale Story "SAVE OVER 30%".
- Clean PDF preferred (avoid black/gray backgrounds → use cutout). Handles sub-items (e.g. "LIPHATECH ROZOL RTU FIELD RODENT BAIT").

## FQC (owned by multiple parties)
1. Autostack spotcheck; Ops Spot Checks.
2. Image QC (PDF preferred; generate data-piping groups if needed; review cutouts).
3. 4 standard thumbnails (2,1,2,1).
4. Add page categories (2–3 on all pages **except page 1's**).
5. **Item Search → URL IS NOT `_`** and compare to the linking doc for missing/incorrect URLs; open the linking docs and confirm pages/inserts tagged correctly.
6. Check dates + external run name (**external run name = page-1 callout**).
7. Pricing Zones → open a PZ via the Items column → confirm all items boxed.
8. Geography (flag changes without a note); **Vertical Preview on the PZ with the most stores**; Final QC.
- **Flyer Review type: Lite.**

---
*Source: Co-op AG OneGuide (Google Doc `1aEUtJIKIoqA-dzuSL5roMs0mZOpvnGRanNTjbsGnqGg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op Essentials — Processing Guide

> **Source:** Co-op Essentials OneGuide (Google Doc `1tfIZInIzcxw8duodvZhM7qae44Wijf404rSkywH-mTE`), updated Feb 5, 2025 — **marked INACTIVE in the source doc**. Contacts/credentials omitted.

Federated Co-op banner (FCL). This guide is flagged inactive in the OneGuide; details below reflect the last documented process.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | essentials.crs |
| Publication | Weekly (**11740**) |
| Cadence | Files Thursday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; no coupons, no Feedel |

## Files & schedule
- Files received **Thursday** (download from sFTP if not in FAdmin). Only **one store** — **1954-68 Co-op Essentials Surrey**.

## Upload & setup (owned by Vendor)
1. Manual upload: Pages → Edit → select the week's pages → Auto-group → Save & Complete.
2. Flyer Creation: description / Pricing Zone name = **Base**.
3. Stores/FSAs → **Add All stores**.

### Setup QC (owned by Flex)
- Download the linking document from sFTP (e.g. `Week 07 Essentials urls`); **attach to vendor tasks via "Mass attachment?"**.
- Edit Details: **no theme, available everywhere, Key Messages = Essentials**.
- Check page 1 for dates (top-right corner).
- Complete Setup QC; mark Autostack Spot Check complete; file a ClickUp ticket for FQC.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a callout.
- Only one store (Surrey) — verify geography reflects it.
- If words/images look jumbled, **rerun tile generation for that page with Ghostscript 9.06 gamma**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; Box Draw/Box QC linking doc)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, description, price, sale story, categories, disclaimer, original price. **Exclude:** valid dates, SKU, URLs (N/A).
- Example: Brand "Our Certified"; Name "Our Certified Lean Ground Chuck Beef"; Description "2.27 kg, sold by the tube"; Current Price "20.00 ea"; Sale Story "WORKS OUT TO BE $4 PER POUND"; Category Meat.

### Image QC
- PDF always, as long as the image is clean.

## FQC (owned by Flex)
1. Edit Details: available everywhere; no theme; Key Messages = Essentials (or the page-1 callout if different).
2. Item Image QC → **click "Generate data piping"**, then return to overview and back to Image QC.
3. Draw thumbnails — Standard 4; complete page categories.
4. Check geography — only 1 store (Surrey).
5. Ensure pages in correct order and fully tagged; check vertical preview; **confirm dates correct**; if jumbled, rerun tile generation (Ghostscript 9.06 gamma).
6. Complete Final QC.
- **Flyer Review type: Lite.**

---
*Source: Co-op Essentials OneGuide (Google Doc `1tfIZInIzcxw8duodvZhM7qae44Wijf404rSkywH-mTE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op Food — Processing Guide

> **Source:** Co-op Food OneGuide (Google Doc `1ZTTdhlBPmcBJLfRbAM4WL5uagn0Cybu_wDjtI4K2H1M`), updated Apr 29, 2026. Contacts/credentials omitted.

Federated Co-op (FCL) banner. Five flyer types; the **Weekly (3277)** has the full documented process. The others — Pharmacy (7886, ad-hoc), SK/Saskatoon Liquor (6305, monthly), Saskatchewan Liquor (9942, monthly), Dormant Guide (9427, ad-hoc) — are largely template stubs in the source doc (standard QC tables, no filled-in setup steps).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport`, `#content-team-federated-coop` |
| Hosted URL | food.crs / co-op.crs/flyers |
| Publications | Weekly (**3277**) · Pharmacy (**7886**) · SK Liquor (**6305**) · Saskatchewan Liquor (**9942**) · Dormant Guide (**9427**) |
| Cadence (Weekly) | Files Thursday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule — Weekly (3277)
- Files received **Thursday**. Codesheet + versioning downloaded from FTP (e.g. `Week 27 Food.xlsb`).

## Upload & setup — Weekly (owned by DOC)

### Codesheet
1. Open `Week __ Food.xlsx`, enable editing; go to the **Wk __ Food Flyer** tab; delete the buttons in column A.
2. **Copy that tab to a new book** (right-click → Move or Copy → To book: (new book) → Create a copy) and **save as CSV**.
3. Upload the codesheet: **Config Name = `coop_food`**; PDF Base Directory e.g. `/Weekly/2026/Week 21 Food`; **uncheck the 2nd and last toggle**.
4. **⚠️ Remove any stores added during page upload** — otherwise incorrect stores get added to distribution.

### Stores codesheet
1. Open the Version document from FTP (e.g. `Week 27 Food Flyer Version.xlsx`); create "con"/"clean" columns and **concatenate** column A + B (e.g. `=concatenate(16,"-",1)`); find-and-replace "Food Store -" with nothing.
2. **Watch for stores with incorrect #s:** `2486-64`→**2486-67**, `2872-610`→**2872-61**, `2749-3`→**2749-1**, `2002-2`→**2002-6**. Check the **Omissions tab** to include/exclude stores that week.
3. Save as CSV → upload: **Config Name = `generic_stores`**; PDF Base Directory `/`; **ONLY Store or Store Set Assignment**.

### Links, inserts, setup QC
- Build a linking document: from `Week __ Food.xlsx`, copy rows from each tab into one sheet, delete empty-URL rows, save as **Co-op Food URLs CSV**.
- Add **store-specific digital inserts** if present (check sFTP for "Digital Insert" paths). International inserts have a separate process.
- No theme; 4 standard thumbnails; key message from front page or "Weekly Ad".
- **Attach Co-op Food URLs to Box Draw, Box QC, Tag, Tag QC.** Manually upload insert pages per the associated .xls / client email.
- Setup QC: check the sFTP has no leftover pages.

### International publications (ad-hoc)
- Download the Locations URL.xlsx and the last page (with the location callout); count included stores; use the Coop Foods Generic Codesheet; manually upload pages; create 1 PZ using the first store #/name from the location xlsx; Setup QC.

## ⚠️ Common errors / risk items
- **Remove stores added during page upload** before running the stores codesheet.
- **Store-number corrections** (2486-64→2486-67, 2872-610→2872-61, 2749-3→2749-1, 2002-2→2002-6) and the **Omissions tab**.
- **Date-specific sale items** (usually page 1) must be tagged with **Valid From + Valid To** dates.
- **Co-op Centsibles brand:** any item named "Co-op Centsibles" must have "Co-op Centsibles" in the **Brand** field.
- Watch for pricing zones with an **insert as the first page** — draw specific thumbnails.

## QC specifics — Weekly

### Box Draw (Low; Auto-Box ON, Box QC bot ON; Box Draw/Box QC linking doc)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Each item gets its own box; box banners with links and gift-card callouts.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, **URLs**.
- **Co-op Centsibles** → brand in the Brand field (e.g. Brand "Co-op Centsibles", Name "Co-op Centsibles English Muffins", "### FOR 2", Current Price 5, category Grocery).
- Clean PDF preferred (avoid black/gray backgrounds → cutout).

### Item Category / SKU / URL QC
- Each page gets 1–4 categories (best judgement).
- **URL QC:** Item Search → URL IS NOT `_` per pricing zone; `food.crs` items tagged `http://www.food.crs/`.
- **SKU QC:** use the Links Sharing document to find which item/page gets the SKU; add it on the corresponding page.

## FQC — Weekly (owned by DOC)
1. Autostack spotchecks; Category QC (add page categories if incomplete).
2. Draw thumbnails Standard 4 (special thumbnails for PZs with an insert as first page).
3. Confirm key messages (page-1 callout); confirm inserts added (reference the insert .xls).
4. **Item Search → URL IS NOT `_`** per PZ vs. linking doc; `food.crs` → `http://www.food.crs/`.
5. **Item Search → NAME CONTAINS "Centsibles"** (make Brand visible) → confirm "Co-op Centsibles" in Brand.
6. Check geography vs. the versioning document (stores added/missing).
7. Complete Final QC; **complete flyer sorting — main weekly flyer first**.
- **Flyer Review type: Lite.**

---
*Source: Co-op Food OneGuide (Google Doc `1ZTTdhlBPmcBJLfRbAM4WL5uagn0Cybu_wDjtI4K2H1M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op Gas Bar — Processing Guide

> **Source:** Co-op Gas Bar (C-Store) OneGuide (Google Doc `1rehrXOORXHDQtyTsyk3RNhQIQ-gTvgbi0_SDoKMZw2w`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | co-op.crs/flyers |
| Flyer type(s) | Monthly C-Store deals (pub 10718) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel/retailer data services |

## Files & schedule

- **When files arrive:** Thursday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday.
- **Linking document:** Digital Inserts xlsx from the FTP (e.g. "Wk 46–49 C-Store Digital Inserts.xlsx"). If multiple URL links in the xlsx, mass-attach the linking document to vendor tasks; if only one link, leave a comment in the vendor task with the link.
- **Owners:** Upload & Setup = Vendor; FQC = DOC.

## Upload & setup (owned by Flex)

- Open the xls document from sFTP to find the order of pages. "Already Up" refers to pages that have **CSTORE Quick Deals** (usually 2 pages).
- **Manual upload** of the pages in the shared xls document; manually complete grouping; Save and Complete.
- **Setup QC:** Flyer Creation → create 1 pricing zone called **Base** → add all stores. Edit Details: **no theme, no external run name, Key Messages = Monthly Deals.** Complete Setup QC checklist and mark autostack spotcheck complete.

## ⚠️ Common errors / risk items

- **Triggers.** Certain pages are only meant for certain weeks (found under Duration on the Digital Inserts overview / Triggers tab). If triggers are needed, **create a JIRA ticket to remind the team to review the removal/addition of those pages.**
- Look for multiple products within a single deal.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** Linking document required (Box-specific). Box each item individually. **Include** retailer logo, sign-up page, social media, special weblinks (banners with calls to action). **Exclude** coupons and packaged deals.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-selection ON.** Linking document required. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Image QC:** prefer a clean PDF when available; avoid images with black/gray backgrounds or that don't match the item.
- **Item Category QC (DOC):** Categories = Snacks & Beverages; Google Category by best judgement of the PDF item. Use a clean PDF; if items have different names, use the clean PDF from the first item.

## FQC (owned by DOC)

- Complete spot checks; Standard 4 thumbnails (drawn on the page with the run dates).
- Edit Details: run dates correct, available everywhere, no theme, **External Run Name = Monthly Deals.**
- Confirm all items boxed and links attached (mass attachment or comments).
- **Check the Triggers tab** on the Digital Inserts overview — create a JIRA ticket if trigger review is required.
- Unblock the flyer if Publish Publications is red; complete Vertical Preview and Final QC checklist.
- **Flyer Review type: Lite.**

---
*Source: Co-op Gas Bar OneGuide (Google Doc `1rehrXOORXHDQtyTsyk3RNhQIQ-gTvgbi0_SDoKMZw2w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op Home — Processing Guide

> **Source:** Co-op Home OneGuide (Google Doc `1VYnI7mG6lHx7maS-OK2-gp2I5jwz9cn2fdqrsZJ3hSE`), updated Jul 14, 2026. Contacts/credentials omitted.

Federated Co-op (FCL) banner. Three flyer types documented: **Home Centre (3361, Weekly)** — the active/detailed one — plus **ProGrade (11604, Bi-Weekly) — NO LONGER RUNNING** and **Guide (7798, Ad-Hoc, mini-magazines)**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | co-op.crs/flyers |
| Publications | Home Centre Weekly (**3361**); Guide ad-hoc (**7798**); ProGrade (**11604** — retired) |
| Cadence (Weekly) | Files Monday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Home Centre (Weekly) files received **Monday**. Guide is ad-hoc; mini-magazines currently fall under the Home Centre flyer type.

## Upload & setup — Home Centre Weekly (owned by Vendor)
1. Download the Flipp codesheet (search xls; find the **HC_TC** page, e.g. `Week 09 HC_TC.xls`).
2. Upload: Name = `upload`; **Config name = `coop_home`**; PDF base from FTP (e.g. `/Weekly/2025/Week 08 HC`); **select all toggles except 2 and 7**; Save & run.
3. Open the URL linking document (FTP) → **Digital Inserts tab** → see the week's inserts → go to the flyer run and **manually add the inserts** → mark Flyer Creation complete.

### Codesheet error handling
- **"Error Backtrace = Found a reused PDF file within the same pricing zone layout":** copy the called-out page directly from the sFTP into the codesheet; if it persists, remove the reused page and add it manually.
- **"Error Backtrace = Page cannot be found in sFTP":** make the codesheet page name match the sFTP page name.

### Setup QC
- Edit Details: no theme; dates match PDF; **key message = the title on page 1** (e.g. "Canada Day"); available everywhere.
- 4 standard thumbnails; attach the links doc if in FTP (e.g. `Wk 37 HABS Flyer urls.xlsx`); Setup QC; Autostack spotcheck.

### ProGrade (retired) & Guide (ad-hoc) — brief
- **ProGrade** (11604, no longer running): manual upload → auto-group → 1 PZ, all stores; key message "Pro-Grade Savings"; **hide on Flipp + distribution only if it fails content policy**.
- **Guide** (7798): create run in Guide type; manual upload all pages; 1 PZ, all stores (match the corresponding week's HABS weekly stores); key message = page-1 title; attach links + items list; **highlight items with a tag symbol for the vendor team**.

## ⚠️ Common errors / risk items
- **Reused-PDF and page-not-found codesheet errors** (see error handling above).
- **Digital inserts** must be manually added and placed in the correct position (usually at upload; if not, add at FQC). Check "Pages not in PZ" and the sFTP for un-uploaded inserts (Details → View Files → "hide uploaded").
- **URLs:** anything with `www.home.crs` gets the `https://www.home.crs/` link only; bottom links tagged `https://www.build.crs/`.
- **Do not box/tag** an item with no sale callout or price — **unless it has a specific link**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals, retailer logo (Weekly). No linking doc (Weekly).
- Box all items separately; **box priced sizing variants separately**; box all URLs; box all items with **tag symbols**.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand, name, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** pre/postfix, valid dates, SKU (Weekly).
- Clean PDF example: Name "BE BOOSTER CABLES, 20-FT.", Description "Two gauge. Copper-coated aluminum cable. (5041 298)". No clean PDF → cutout (avoid black/gray backgrounds).

### Image / Category QC
- Single items → clean PDF if available; multi-item → cutout so all options show. **All pages get categories (1–4); none on Page 1.**

## FQC (owned by DOC)
1. Autostack spotcheck; spotchecks if applicable.
2. **Confirm insert pages were added** in the correct position; check "**Pages not in PZ**" is empty (add missing inserts from the URL doc, box/tag them); check sFTP for un-uploaded inserts.
3. Review details (no theme, no external name, key message = page-1 callout); page categories (1–4, none on page 1).
4. **Item Search → URL IS NOT `_`** and compare to the linking docs for missing/incorrect URLs; `home.crs` → `https://www.home.crs/`.
5. Review boxes (don't box priceless/callout-less items unless they have a link); geography; thumbnails Standard 4 (2,1,2,1) — check zones with an insert in first position; thumbnail on the page with the date/callout banner.
6. Sessions; dates on page 1; Storefront Spotchecks (pages not merged); complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Co-op Home OneGuide (Google Doc `1VYnI7mG6lHx7maS-OK2-gp2I5jwz9cn2fdqrsZJ3hSE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op Liquor — Processing Guide

> **Source:** Co-op Liquor OneGuide (Google Doc `1I5tXYVpqgyE78HtNgDRhd2TsCurLGI6V0GxV4Tr7oy4`), updated Jun 2, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport`, `#content-team-federated-coop` |
| Hosted URL | northcentralliquor.crs |
| Flyer types | **Wine Spirits Beer** (pub 12121, weekly) · **Liquor Outlet** (pub 12122 — store closed, see out-of-processing) |
| Processing | Auto-stack; Flex (Flyer Review / Processing Support) |
| Strategic Ops | Yes — retailer data services (Feedel processing) for the Outlet type; WSB has no Feedel |

## Files & schedule

- **When files arrive:** Thursday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. WSB gets a **1-day preview.**
- **Owners:** Upload & Setup = Vendor; Image QC = Flex; FQC = DOC.

## Upload & setup — Wine Spirits Beer (owned by Vendor)

- **Manual upload** of all pages. Create one pricing zone in chronological page order, named **Base**; add stores via the WSB store set (6 stores).
- Flyer run dates = page dates + 1 preview day; **no theme**; set legibility heights to **40/30**; draw all 4 standard thumbnails (1065×600, Stock Premium, Storefront Carousel Premium, Storefront Carousel Organic).
- **Setup QC:** check dates; download the **Click Throughs xlsx** from the FTP (e.g. "Wk 33 WSB Click Throughs.xlsx") and attach it to the vendor tasks; complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **Ignore the Auto Tag Enhanced error.**
- Confirm the **1-day preview** date is right — e.g. a June 26–July 2 run is available June 25.
- Geography: no stores/FSAs should be missing week over week unless told otherwise.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** No linking document. Box items individually. **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons and packaged deals. Social icons link to the retailer's Facebook/Instagram pages (URLs in the OneGuide).
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix, valid dates, SKU.**
- **Image QC (Flex, day 2):** standard.
- **Item Category QC (DOC):** add 1 category per page except page 1.

## FQC (owned by DOC)

- Mark autostack spotcheck complete; **ignore the Auto Tag Enhanced error.**
- Check run dates on the bottom of page 1 (1-day preview).
- Confirm WSB store set (6 stores) added; Geography unchanged.
- Add external run name; draw 4 standard thumbnails; review page categories (none on page 1).
- Confirm links added per the Click Throughs xlsx (from vendor tasks or SFTP; WSB → "Wk ## WSB Click Throughs.xlsx", Liquor Outlet → "Wk ## Liquor Outlet Click Throughs.xlsx").
- Available everywhere; check Storefront Spotcheck and Vertical Preview; complete Final QC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing

- **Co-op Liquor Outlet (pub 12122) is no longer valid — the store is closed.** If it returns, process exactly like the WSB flow above.

---
*Source: Co-op Liquor OneGuide (Google Doc `1I5tXYVpqgyE78HtNgDRhd2TsCurLGI6V0GxV4Tr7oy4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Co-op (Sobeys) — Processing Guide

> **Source:** Co-op (Sobeys) OneGuide (Google Doc `1SpnaoIR3JG0iUVrbUPpYT0IeDki7LzPE6K7jvljpVU8`), updated May 7, 2025. Contacts/credentials omitted.

Part of the Sobeys family (shares pages with Clover Farms; combined Flex Flyer Review with Clover Farms + ValuFoods). This is the Sobeys-banner "Co-op" — distinct from Federated Co-op (Food/Home/AG).

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channels | `#sobeys`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | sobeys.com |
| Publication | This Week's Flyer (**3796**) |
| Cadence | Files Monday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (3FL + Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Files received **Monday**. Open the flyer run + FTP and confirm all files present.
- Open the **Run List** in the shared folder — it gives the Zone title, stores, and which pages to add. **Page 1 is always the Co-op zone; other pages are shared with Clover Farms (Zone 1).**
- **Do not Autogroup** — manually add the page order. Either **4 or 8 pages**.

## Upload & setup (manual; owned by Vendor)
1. Complete flyer run creation — **Pricing Zone = Zone 4**.
2. Add stores per the run list in the shared folder.
3. Edit Details: **hidden on hosted**, no theme; key message from the rotating Sobeys list (e.g. "Weekly Ad. Weekly Savings.", "Deals of the Week"); **external run name = Weekly eFlyer + valid date**.
4. QC thumbnails (Standard 4); **box & tag recipe callout on pg 1** → `http://familyfoods.ca/recipes/`.
5. Spotlights; Setup QC; Autostack spotcheck; check sessions; vendors to high.

## ⚠️ Common errors / risk items
- **Confirm all pages uploaded** (usually 8). **Regular pages go before PopUp pages** at the end.
- Pre-FQC: **item search** for description containing `/lb`, `/kg`, `/g` — any additional pricing must be added to the **postfix** under Current Price.
- Check sessions → **verify links and Force selection for PDF Image Auto Selection**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; Box Draw/Box QC linking doc)
- **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons.
- Box all items with prices, using text boxes when necessary. The CTA at the bottom does not need boxing.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude:** disclaimer, URLs.

### Image QC
- PDF Image Auto Selection ON — should auto-select a PDF.

## FQC (owned by DOC)
1. Autostack spotcheck; review pages in Storefront Spotcheck; **regular pages before PopUp pages**.
2. Edit Details as above (hidden on hosted, no theme, rotating key message, external run name).
3. QC thumbnails Standard 4; box/tag recipe callout on pg 1.
4. Spotlights; check sessions → verify links; vertical + horizontal preview on PZ.
5. **Final QC — available start time is 6 AM** (shared with Clover Farms, ValuFoods, CF ONT).
- **Flyer Review type: Lite** (combined Clover Farms | Co-op | ValuFoods review).

## Out-of-processing (page swap)
- Open run → Pages → Edit → select new page from FTP → add "REV" to the name → Save & Complete → Copy Items from the old page (same page only), adjust changed item(s) → box/tag → add to PZ.

---
*Source: Co-op (Sobeys) OneGuide (Google Doc `1SpnaoIR3JG0iUVrbUPpYT0IeDki7LzPE6K7jvljpVU8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Coast Appliances — Processing Guide

> **Source:** Coast Appliances OneGuide (Google Doc `16-r7dOi0LFObohSoLBdN_L9NCzEEc0XWu-xT89Pw-UU`), updated Sep 4. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#coastappliances` |
| Hosted URL | N/A |
| Flyer type(s) | Flyer — weekly |
| Processing | Auto-stack; Flex = Processing Support; OS = FQC; no coupons; no Feedel |

## Files & schedule
- **Files received:** Thursday; should be in the SFTP **at least 5 business days before launch**.
- **Publication:** Available/Valid From Thursday → Available/Valid To Wednesday (match PDF).
- **Linking document:** Yes — provided by the retailer; **must be attached to all tasks.**

## Upload & setup (owned by Flex)
- Manual upload all pages → Auto Group → **EN only**.
- **One pricing zone: base = EN.** Add all stores.
- **Setup QC:** Available/Valid From Thursday, To Wednesday (match PDF); available everywhere; check theme and apply if available; ensure linking document attached; all stores added.

## Box Draw (Low — Auto-Box OFF, Box QC bot ON; linking-doc required)
- **Include:** retailer logo. **Exclude:** coupons, packaged deals (washers/dryers), sign-up page, social media, special weblinks.
- Risk item: **look for multiple products.**

## Tag / Tag QC (Low; Auto-tag OFF; linking-doc required)
- **Include** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude** pre/postfix and valid dates. Brand used for Box/Tag.

## Image QC / Links QC
- Standard item image QC.
- **URL/Links QC:** check for any items/products **without a link against the provided linking document.**

## FQC (owned by DOC)
- QC thumbnails; check items without a URL; ensure every item with a price/sale story/callout has a box (no overlaps); **all items, page banners (e.g. "BUY MORE AND SAVE UP TO $$$") and back-page stores must have links — items without a URL should be 0**; sessions all green; Geography unchanged campaign over campaign.
- **Flyer Review type: Lite.**

---
*Source: Coast Appliances OneGuide (Google Doc `16-r7dOi0LFObohSoLBdN_L9NCzEEc0XWu-xT89Pw-UU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Coastal Farm — Processing Guide

> **Source:** Coastal Farm OneGuide (Google Doc `1qU6874NurYkV57tlFMTOGfWcsV9az7b4VHqtBFiDWKY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#coastalfarm` |
| Hosted URL | coastalcountry.com |
| Flyer type(s) | Weekly Ad (ID 4175) — **ad-hoc** |
| Processing | Auto-stack; Flex = Processing Support; no coupons; no Feedel |

## Files & schedule
- **Files received:** ad-hoc (all dates ad-hoc; ~10-day workflow).
- **Preview date:** set **5–6 days ahead of live date** depending on retailer lead time (confirm with processor if unsure). This preview drives the item-export/import correction loop.
- No linking document.
- **~5 days out:** send item report to retailer; **~2 days out:** retailer returns updated report and item import is completed.

## Upload & setup (owned by Flex)
- Manual upload in FTP → Pages → Edit → select pages → Auto-group.
  - **Wrap pages:** place in the **last position** after all main pages, and **manually group wrap pages in consecutive order.**
- **One pricing zone; add all stores.**
- Edit Details: Available/Valid dates match the PDF; **External Run Name = the main Page-1 title** (e.g. "Early Bird Black Friday"); available everywhere; no theme.

## Box Draw (Low — Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals, retailer logo, sign-up page. **Exclude:** coupons, social media, special weblinks.
- Box all items individually (draw as large as possible without overlap); use text boxes as needed.
- **Multiple sizes:** box together if one description; box separately if different descriptions.
- **Coastal Farm logo:** always box, Link display type, tag URL coastalcountry.com.

## Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)
- **Include:** name, valid dates, sale story, categories. **Exclude:** brand, pre/postfix, description, SKU, **price, original price**, disclaimer(mostly), URLs.
- **Name:** as it appears; include weight (lb) in Name; don't put brand in the Brand field if it's in the name.
- **DO NOT tag** prefix/current price/postfix/original price/SKU.
- Sale story & disclaimer: enter as seen when applicable.
- **Retailer logo:** Link display type → coastalcountry.com.

## ⚠️ Common errors / risk items (retailer-specific)
- **NO pricing in the item pop.** The retailer communicates all deals/prices via **Sale Story**. Original price, current price, price text, and pre-price text must be **ALL BLANK**. Use Item Search (`Current Price is not [blank]` and `Original Price is not [blank]`) to find and clear any pricing tagging.
- **Item export loop:** export items → keep only `item_id, page, name, sale_story, url` → clear all pricing → send `.xlsx` to the retailer. On import back, keep `item_id, sku, brand, name, sale_story, url`; brand column all blank; add empty SKU column; delete page/comments columns; save `.csv` → Import Items.
- **Logos/QR codes** must be boxed and tagged on the **first and last pages** before sending the export; delete boxing on pages with the bottom banner.
- Wrap pages: include the wrap-page numbering in the page column of the export.

## Image QC
- PDF images preferred; use cutout when not clean (non-white background, half-cut) or when no image exists.

## FQC (owned by DOL; Lite)
- Mark Autostack Spotcheck complete; Edit Details dates correct; external run name = Page-1 title; available everywhere; no theme (watch for carousel themes during Black Friday/Christmas). Leg heights 50/40; Standard 4 thumbnails.
- **Confirm all current/original prices are blank via Item Search.** Items without a URL = 0. Check sessions.
- **FQC checklist quirk:** a red warning that the pricing zone has no items with a current price is expected — override with "current prices not tagged for this retailer". On Save & Complete you'll hit the content-policy warning again; click OK and Save & Complete once more.

---
*Source: Coastal Farm OneGuide (Google Doc `1qU6874NurYkV57tlFMTOGfWcsV9az7b4VHqtBFiDWKY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cohen's Home Furnishing — Processing Guide

> **Source:** Cohen's Home Furnishing OneGuide (Google Doc `1A0gDh0m2QAmY_d2T8a-ndZ3ZXuGtqfEUfqoLP1U4Wsk`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#cohens-furniture` |
| Hosted URL | cohens.ca |
| Publication | Monthly (Flyer **5160**) |
| Cadence | Files Wednesday. Available Wed, Valid Tue–Tue; consumer preview 1 day before |
| Processing | Auto-stack; Flex (Processing Support); no OS, no coupons, no Feedel |

## Files & schedule
- Files (pages + linking doc) arrive **Wednesday via email**; upload assets to the SFTP.

## Upload & setup (English only, manual)
1. Manual file upload (English only) — files come by email; upload to SFTP.
2. Create **one pricing zone "base"** → add all stores.
3. Edit Details: available everywhere; consumer preview 1 day before.
4. Standard 4 thumbnails.
5. **Attach the linking doc** (e.g. "Month 2023 Flyer Listings URLs.xlsx") to all vendor tasks.
6. Setup QC checklist.

## ⚠️ Common errors / risk items
- **SKU / Model # in the Name field:** for **appliances and TVs only**, use the **Model #** column to tag the name field. The Name field = product name **then** the Model #. Model # goes in **Name, Description, and SKU** fields.
- **All other items:** Model #/SKU must NOT appear in the Name field.
- If there is no Model #, leave the name field empty of a model number.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Linking doc required.
- Items with image + info together → box as one. For a "set"/"suite": box the image + a text box for the info, and draw a separate box around any item sold separately (e.g. "Queen BED").

### Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU field (except appliances/TVs per risk item), URLs.
- **URLs:** find product by name or SKU and apply the URL from the linking doc; if none listed, don't add one.

### Image QC
- Standard: **PDF preferred if clean; otherwise cutouts accepted.**

## Pre-FQC / FQC (owned by DOC)
- Pre-FQC: confirm dates (from PDF), availability toggles, thumbnails include retailer logo; all items boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions complete; geography correct.
- FQC: mark autostack spotcheck complete; check vertical preview for clickable items.
  - **RISK:** all pages boxed/tagged; appliances/TVs have Model # in Name + Description + SKU; all others don't.
  - **No page categories** (remove if present).
  - Check "items without URL" on the overview page — open linking doc to verify.
  - Check Pages, Pricing Zone, Vendors, Geography tabs.
- **Flyer Review type: Lite.**

---
*Source: Cohen's Home Furnishing OneGuide (Google Doc `1A0gDh0m2QAmY_d2T8a-ndZ3ZXuGtqfEUfqoLP1U4Wsk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Colemans Brandsource Home Furniture — Processing Guide

> **Source:** Colemans Brandsource Home Furniture OneGuide (Google Doc `1XSrDntdVfKQ-4b4li6xbrOtoK461PgOlzV6Y6oqPJ9U`), updated Nov 26, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (**not on hosted**) |
| Slack channel | (none listed) |
| Publication | Flyer **7166** |
| Cadence | **Ad hoc** — all dates ad hoc |
| Processing | Auto-stack; Flex (Processing Support); no OS, no coupons, no Feedel |

## Files & schedule
- Files delivered **ad hoc via SFTP** (PDF pages + URL docs).
- **Always double-check PDF dates** and confirm with client/BD if needed. Client confirms customer preview dates (usually 2–3 days) in the file-delivery email.

## Upload & setup (manual; owned by DOC)
1. Manually upload pages → Pages → Edit → select all applicable pages.
2. Index pages, ensure correct order.
3. Language = **ENGLISH only**.
4. Save + Save & Complete.
5. Create a **Base pricing zone** for all pages → **add all stores (only 1 store)**.
6. Complete Setup QC in the pipeline.

## ⚠️ Common errors / risk items
- Ad-hoc dates — verify against the PDF and confirm with client/BD.
- Only one store; not on hosted.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks. No linking doc.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude:** URLs.

## Post-processing / FQC (owned by Flex)
- Standard checks — all items boxed/tagged, hosted previews, geography (no missing FSAs).
- **Standard 4 thumbnails.**
- Complete FQC checklist in FADMIN.
- **Flyer Review type: Lite.**

---
*Source: Colemans Brandsource Home Furniture OneGuide (Google Doc `1XSrDntdVfKQ-4b4li6xbrOtoK461PgOlzV6Y6oqPJ9U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Colemans — Processing Guide

> **Source:** Colemans OneGuide (Google Doc `1TBf2jK3Rw1ZmUrHVvwBpenBKUDVbV4Z0gC2L_59ebT8`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#colemans`, `#flex-processingsupport` |
| Hosted URL | shop.colemans.ca |
| Publication | Weekly (Flyer **3258**) |
| Cadence | Files Tuesday. **2-day preview (available Tuesday)**, Valid Thu–Wed |
| Processing | Auto-stack; Flex owns processing; no coupons, no Feedel |

## Files & schedule
- Files + codesheet arrive **weekly via SFTP**; codesheet dropped as a **CSV** named `Colemans Distribution [date-date].csv`.
- Generally no manipulation needed. Rarely, file names don't match codesheet names → fix by expanding month abbreviations (e.g. "Mar" → "March").

## Upload & setup
1. Upload the codesheet to create all pricing zones, assign pages, assign stores:
   - **Config name = `generic`**.
   - **Check all toggles except the second and the last.**
2. Edit Details:
   - Valid Thursday to Wednesday; **2-day preview (available Tuesday)**.
   - **No toggles checked (available everywhere)**; no theme.
3. Complete Setup QC checklist.

## ⚠️ Common errors / risk items
- File names occasionally don't match codesheet names (month abbreviation mismatch) — correct before upload.
- Complete thumbnails for **BASE and BUCHANS pricing zones separately**.
- At FQC you can ignore the "Not all categories that are used in pricing zones have thumbnails" warning.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Single items: box the whole item block, insert a text box where needed. **Items with common pricing: keep them in one box (don't separate).** Don't let boxes overlap.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.

### Item Image QC
- PDF images where possible; cutouts fine for others (e.g. Jell-O Pudding → PDF; graham pie crust → cutout).

## Pre-FQC / FQC (owned by Vendor)
- Pre-FQC: OS spot checks if needed; Image QC; thumbnails Standard 4 (`thumbnail_1065_x_600`, `stock_premium`, `storefront_carousel_premium`, `storefront_carousel_organic`) — **complete for BASE and BUCHANS separately**.
- Edit Details: available 2 days before valid; dates match PDF front page; available everywhere.
- Pages QC'd; categories accurate per page; item view all boxed/tagged; vertical + horizontal preview; vendor tasks done; geography — no store changes week over week.
- Complete FQC; ignore the categories/thumbnails warning.
- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps handled per the baseline page-swap process.

---
*Source: Colemans OneGuide (Google Doc `1TBf2jK3Rw1ZmUrHVvwBpenBKUDVbV4Z0gC2L_59ebT8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Commisso's Fresh Foods — Processing Guide

> **Source:** Commisso's Fresh Foods OneGuide (Google Doc `1QRJ2IVboypgXSgKW96iW-UAsuxRBkA1dQxN3XIoodBQ`), updated Dec 3, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#commissos`, `#flex-processingsupport` |
| Hosted URL | commissosfreshfoods.com |
| Publications | **commissonsweekly (11543)** · **twoweekwellness (11547)** · **3daynew (11760)** |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup + FQC; no coupons, no Feedel |

## Files & schedule
- Files received **Thursday**; dates referenced in the client's confirmation email and on the flyer PDF.
- Cadence per flyer type (every flyer gets a **1-day preview**):
  - **Weekly:** Available Thu, Valid Fri–Thu.
  - **3 Day New:** dates communicated by client; generally Available Sun, Valid Mon–Wed.
  - **Two Week Wellness:** Available Thu, Valid Fri–Thu (2-week run).

## Upload & setup (manual; owned by Vendor)
1. Pages → Edit → select pages — **upload from the folder matching the flyer type** (Weekly, Wellness, or Three Day New).
2. Autogroup → Save & Complete.
3. Flyer Creation: **one pricing zone, description "Base"**, all pages; confirm correct page order; Save & Complete.

### Setup QC
- Pricing Zone: one Base zone, add all stores.
- Pages: open page 1 ("Tag") and check dates printed on the PDF.
- Vendors assigned; **no attachment needed** for this merchant.
- Edit Details: dates match email/PDF page 1; available everywhere; **no external run name; no theme**.
- Thumbnails Standard 4 (`thumbnail_1065_x_600`, `stock_premium`, `storefront_carosel_organic`, `storefront_carosel_premium`).
- Complete Setup QC; mark Autostack Spotcheck complete.

## ⚠️ Common errors / risk items
- **Make sure categories are tagged.**
- **⚠️ Add the Last Page for Weekly & Wellness before the FQC checklist** (see FQC). Download last page from the prior week's run of the correct flyer type; upload to this week's run; copy items across.
- **Meals available only on specific days** (e.g. Tuesdays/Wednesdays) — tag their valid dates carefully.
- **Update flyer sorting** to "Flyer Type Newest First" after FQC.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; PDF Image Auto Selection ON)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Box must capture product image + price + unit of measure (e.g. "$12.99 lb"). **Multi-buy offers** (e.g. "2/$4.88", "Buy 1 Get 1 FREE") — capture the entire promo text and all related images inside the box.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc required)
- **Include:** brand (in both Brand + Name fields), name, pre/postfix, valid dates, description (incl. sizes/weights), price, sale story (e.g. "BUY 3 GET 1 FREE"), categories (Grocery/Meat/Bakery best fit), disclaimer, original price. **Exclude:** SKU, URLs.
- Watch for meals valid only specific days of the week.

### Image QC
- **Select clean PDF when available; use cutout when no clean PDF.**

## FQC (owned by DOC)
### ⚠️ Add Last Page (Weekly & Wellness) — do BEFORE the FQC checklist
- Download the last page from the previous week's run of the matching flyer type (Pages → Edit → download `cff_lastpage_REV.pdf` for Weekly or `lastpage_for_wellness.pdf` for Wellness).
- Upload that PDF to this week's run (Pages → Edit → Upload Local Files → Save & Complete).
- Mark **Flyer Creation** complete; wait for sessions; mark Box Draw/Box QC complete **before** copying items (you'll get an error otherwise); mark Tag/Tag QC complete as they become available.
- From the previous week's run: Pages → **Copy Items**, update the flyer ID, click "From" next to the last-page PDF and "To" next to this week's PDF.
- **Insert the last-page PDF into the Base pricing zone (last position).**

### Then
- Geography green — **no stores/FSAs added or removed**.
- Vendors complete; PZ item view (no missed items), vertical + full-screen preview, all stores, pages ordered.
- Pages all QC'd (green). Legibility heights: **Scan 50, Read 40**. Thumbnails Standard 4. Image QC (clean PDF, else cutout).
- Complete FQC (ignore the categories/thumbnails warning).
- **Update flyer sorting → "Flyer Type Newest First"** (newer Weekly first, older Weekly next, 2-Wk Wellness last).
- **Flyer Review type: Lite.**

## Out-of-processing
- Occasional page swaps come in (baseline page-swap / last-page-addition process).

---
*Source: Commisso's Fresh Foods OneGuide (Google Doc `1QRJ2IVboypgXSgKW96iW-UAsuxRBkA1dQxN3XIoodBQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Community Natural Foods — Processing Guide

> **Source:** Community Natural Foods OneGuide (Google Doc `1-VBH3vPRpT_upHzMuqhu_3K_HNLyZMg7MMIyRVpMlWA`), updated Jun 22, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channel | `#community-natural-foods` |
| Hosted URL | communitynaturalfoods.com |
| Publication | Monthly (**9708**), with weekly page swaps |
| Cadence | Files ad hoc. Available Thu, Valid Tue → Tue a month later |
| Processing | Auto-stack; Flex (3FL + Flyer Review); no OS, no coupons, no Feedel |

## Files & schedule
- **One base file set** arrives at the **start of each month** and runs for the month (first flyer's pages are labelled by number only).
- **Each week after**, updated pages (generally new **Page 1 "front"** and **Page 9 "produce"**) are submitted, uploaded to the monthly run and **swapped in via a trigger** on the client-requested date.
- Stores split by **Calgary** and **Edmonton** zones when two zones are used.

## Upload & setup

### New monthly publication (owned by Flex)
- Create a new flyer run (dates from client email); Pages → Edit → upload from that month's FTP path → Autogroup → Save & Complete.
- Flyer Creation: usually one Base PZ, all pages. Stores — one zone: add all + wait for FSAs; two zones: Calgary stores → Calgary zone, Edmonton stores → Edmonton zone.
- Setup QC: thumbnails Standard 4 (always get logo + retailer name). **Attach the MONTHLY URL document from FTP to *all* vendor tasks** (check "Mass Attachment?") — ensure the **monthly** links (not the updated weekly links) are used. Setup QC checklist + Autostack Spotcheck.

### Weekly page swaps (owned by Vendor)
- Pages → Edit → upload the week's new pages from FTP → Save & Complete.
- **Attach the newest URL document** to all new vendor tasks (sometimes one doc, sometimes two — one Edmonton, one Calgary). Autostack Spotcheck.
- **Set a trigger to swap in the new pages for the upcoming Thursday:** Pages → Layout → swap out current Page 1 + Produce Page for the new ones → **"Run as Trigger"** → select the next Thursday at 12:00 am.
- **Make a Jira ticket to verify the trigger ran** the morning after; notify the DOC + DOL.

## ⚠️ Common errors / risk items
- **Page swaps:** Flex uploads the monthly file; **weekly Page 1 + Page 9 updates must be uploaded by DOC, processed by OS, and trigger-swapped** on go-live week. Verify the trigger ran.
- **URLs:** use the attached spreadsheet to add URLs; check the URL section carefully.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; Box Draw/Box QC linking doc)
- **Include:** special weblinks. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- **Box each item individually.**

### Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand (in both Brand + Name), name, pre/postfix, valid dates, description (incl. sizes/weights), price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** SKU.
- Price: include `/lb` and `/kg` price in the postfix.
- **URLs from the spreadsheet** (page #, product name, URL). **Items highlighted yellow = Direct Links** — box and tag as Link type.

### Image QC
- Use PDFs whenever possible; use cutout when the PDF image isn't clean (watch for grainy backgrounds).

## FQC (owned by DOC)
### New monthly publication
- Autostack Spot Check; OS Spot Checks (usually none; occasionally approve a Name or check a Price).
- Overview: legibility heights (preset Scan 40, Read 25); Image QC; thumbnails Standard 4; Edit Details (Available = Valid, Thu → Wed a month later; dates match PDF; available everywhere; no external run name; no theme).
- Pages QC'd; categories accurate per page.
- **URL/Links QC:** open "Items Without URL"; cross-check the attached URL doc (names aren't exact matches — search by brand, e.g. Ctrl+F "CanPrev"). Yellow-highlighted items are direct links — box/tag with correct URL and item type Link.
- PZ item view boxed/tagged; vertical + full-screen preview; sessions green (PDF Image Auto Selection may be yellow); vendors done; geography — no week-over-week changes.
- Complete FQC (ignore the categories/thumbnails warning).
- **Flyer Review type: Lite.**

## Out-of-processing
- Weekly page swaps as above (trigger-based).

---
*Source: Community Natural Foods OneGuide (Google Doc `1-VBH3vPRpT_upHzMuqhu_3K_HNLyZMg7MMIyRVpMlWA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Concept Piscine Design — Processing Guide

> **Source:** Concept Piscine Design OneGuide (Google Doc `1mZD1zVNfBaCH_iVlW0JHPDRrSlFsNRi8DI_wHZNejuY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Publication | Flyers and Catalogs (**11758**) |
| Cadence | Files Friday. Available Mon, Valid Sun–Mon |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no OS, no coupons, no Feedel |
| Language | **French** |

## Files & schedule
- Files received **Friday**; linking document provided. Pages may need to be added to the SFTP by the processor if the client sends files over email.

## Upload & setup (manual; owned by DOC)
1. Pages → Edit → select all pages from the SFTP menu → Confirm & Upload.
2. Once pages list at the bottom, **Auto-Group**.
3. **Ensure FRENCH language is selected** → Save → confirm the French setting saved → Save & Confirm. **Do NOT Process Internally.**
4. Create **Base pricing zone**, select **French** + all pages → Save & Confirm → add all stores.

### Setup QC
- Confirm all pages uploaded (PZ → Items View). **RISK:** if uploading from SFTP, confirm no un-uploaded pages remain in the SFTP.
- Confirm flyer dates (usually first or last page).
- Thumbnails Standard 4. Complete Setup QC checklist.

## ⚠️ Common errors / risk items
- **Ensure all items have a URL** — reference the linking document; at FQC there should be **no items without a URL**.
- Confirm no leftover pages in the SFTP before completing.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc used for both Box/Tag)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Also exclude the **disclaimer on the bottom of the last page**.

### Tag / Tag QC (Low; Auto-tag ON; linking doc used for both Box/Tag)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** SKU.

### Spotchecks
- Standard pricing spotchecks included in pipeline.

## Pre-FQC / FQC (owned by DOC)
- Check "Items without a URL" — should be none; if any, use the linking doc to add links.
- Confirm dates (from PDF) and availability toggles; thumbnails correct + include retailer logo.
- Standard flyer-review checks: all boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions complete; geography correct.
- Complete FQC checklist.
- **Flyer Review type: Lite** (checks: flyer dates, sessions complete, previews correct, all items tagged accurately, geography correct, availability toggles correct).

---
*Source: Concept Piscine Design OneGuide (Google Doc `1mZD1zVNfBaCH_iVlW0JHPDRrSlFsNRi8DI_wHZNejuY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cool & Simple — Processing Guide

> **Source:** Cool & Simple (Vendor Solutions) OneGuide (Google Doc `1Hbgi93jsuG6KcbWYJpbamr3CmjvKV0CA2ULppC8PREc`), updated Jul 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Basic |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | We do not power their hosted |
| Flyer type(s) | Flyer (pub 11620) — ad-hoc |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **When files arrive:** ad-hoc; follow the dates on the PDF for available/valid from/to.
- **Owners:** Upload & Setup = DOC; Image QC = Flex; FQC = DOC.

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Once listed, **Auto-Group** or manually add grouping numbers; ensure the correct language is selected. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create **Base**, select all applicable pages, Save & Confirm, add all applicable stores.
- **Setup QC (Flex):** confirm all pages uploaded (Pricing Zone → Items View); **risk — if uploading from SFTP, confirm no pages were left in the SFTP.** Confirm flyer dates (usually first/last page). Complete 4 standard thumbnails; ensure preview dates set; complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **If uploading from SFTP, verify no pages remain un-uploaded.**
- Look for multiple products in a single box.

## QC specifics

- **Box Draw — Low complexity; Auto-Box OFF, Box QC bot OFF.** No linking document. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts are accepted.

## FQC (Pre-Final owned by DOC; Item Image QC owned by Flex)

- Confirm dates (per PDF) and availability toggles; thumbnails correct and include retailer logo.
- Standard checks: all items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** — checks flyer dates, sessions completed, previews showing correctly, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Cool & Simple OneGuide (Google Doc `1Hbgi93jsuG6KcbWYJpbamr3CmjvKV0CA2ULppC8PREc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Coppa's Fresh Market — Processing Guide

> **Source:** Coppa's Fresh Market OneGuide (Google Doc `1cTpAM-mZDo84FQpxOgp-HpNyRIEvGVphyJTsoVwePho`), updated Feb 18, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp & Distribution only |
| Slack channels | `#coppasfreshmarket`, `#flex-processingsupport` |
| Flyer type(s) | Weekly (pub 2684) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |

## Files & schedule

- **When files arrive:** Friday (files typically uploaded directly into SFTP by the retailer on Thursdays, but occasionally late — bump if necessary).
- **Publication cadence:** Available From Thursday, Valid From Wednesday; Available To Thursday, Valid To Wednesday. Live Thurs–Wed, **no preview.**
- **No linking document.**
- **Owners:** Upload & Setup = Flex; FQC = Flex.

## Upload & setup (owned by Vendor)

- 4–6 pages; one version. **Manual upload** (mark off the main PDF in the FTP after uploading all pages).
- One pricing zone: **Base**; add all stores.
- **Hidden in hosted; no theme.** Mark Setup QC complete.

## ⚠️ Common errors / risk items

- Files are occasionally late — bump if necessary.
- Spotchecks: on pricing discrepancies, **always defer to what is on the PDF.**

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** No linking document. Draw a box for each item. **Include** retailer logo. **Exclude** coupons, packaged deals, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, description, price, sale story, disclaimer, original price. **Exclude pre/postfix, valid dates, SKU, categories, URLs.**

## FQC (owned by Flex)

- Mark autostack spotcheck complete; Standard 4 thumbnails.
- In the pricing zone tab → Item View, confirm all items are boxed.
- Confirm geography is consistent.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps: follow the baseline page-swap procedure (video in the OneGuide).

---
*Source: Coppa's Fresh Market OneGuide (Google Doc `1cTpAM-mZDo84FQpxOgp-HpNyRIEvGVphyJTsoVwePho`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Copp's Buildall — Processing Guide

> **Source:** Copp's Buildall OneGuide (Google Doc `1ggGyhMsstF-p9AMgeIMFp55V22yZ9Y1v2y4wYvaAEwA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#copps-buildall` |
| Hosted URL | coppsbuildall.com |
| Flyer type(s) | Flyer — ad-hoc |
| Processing | **Trim Stack**; Flex (Flyer Review); OS (Setup); no coupons |
| Strategic Ops | Yes — retailer data services (Feedel processing) |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday. **Preview date: Monday (1 day).**
- **Owners:** Upload & Setup = Flex; Image QC = Flex; FQC = DOC; Flyer Review = DOL.

## Upload & setup (owned by Flex)

- Files are uploaded into FTP folders that match the **event name** — select all pages in the event. Occasionally different versions are separated into different folders. Notification email confirms files are uploaded in the FTP.
- **Create flyer shell:** run type = Flyer; **Internal Run Name = the month name**; live/valid dates from the notification email or page 1; **set a 1-day preview date**; toggle available everywhere; add theme if applicable.
- **Manual upload** the corresponding event pages → **Auto-Group.**
- **Pricing zones:** typically add all stores to Base.
- Attach the linking doc added on the FTP; complete basic Setup QC questions.

## ⚠️ Common errors / risk items

- Boxing sometimes doesn't capture the full title — **zoom out during tagging** if the entire title isn't visible. Put the main title in Name, extra details in Description, SKUs (in brackets) in the SKU field, and reg. price in the original-price field.
- Look for multiple products.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** Linking document required (Box-specific). Box and tag each item individually. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON; PDF image auto-selection ON.** Linking document required. Include brand, name, description, **SKU**, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix, valid dates.**
- **Image QC:** select the chosen .pdf images; if unclean, use a cutout.

## FQC (owned by DOC)

- Check that logos and social-media icons are boxed/tagged appropriately; check flyer dates; page categories.
- Ensure sessions are clear / reverify URLs if needed.
- QC thumbnails — **Standard 4** (Stock Premium, Storefront Carousel Premium, Storefront Carousel Organic).
- **Legibility heights: 45/35.**
- Item Image QC: confirm .pdf images selected; use cutout if unclean.
- **Flyer Review type: Lite (owned by DOL).** Available ad-hoc PDF with 1-day consumer preview; **hidden in hosted.** Item search checks: SKU/URL/item-type combinations should return 0 (flag to processor if not). Images may all be cutouts (OK). Thumbs Standard 4. If pages are named "compressed files," zoom in on the preview to confirm image quality. Geography: no changes.

---
*Source: Copp's Buildall OneGuide (Google Doc `1ggGyhMsstF-p9AMgeIMFp55V22yZ9Y1v2y4wYvaAEwA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Corbeil Electromenagers — Processing Guide

> **Source:** Corbeil Electromenagers OneGuide (Google Doc `1ZplpIdlCOkD_zIYkMr9S7eoPEBiYcqWgrbd30f-bRyw`), updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1plat-corbeil` |
| Flyer type(s) | Flyer (pub 7491) — ad-hoc |
| Processing | Auto-stack; no coupons; no Feedel |
| Notes | Bilingual — English (EN) and French (FR) versions |

## Files & schedule

- **When files arrive:** ad-hoc (available/valid from/to are ad-hoc).
- **Linking document:** Yes — attach to all tasks.
- **Owners:** Upload & Setup, Image QC, and FQC all = DOC.

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages tab → Edit → select all pages from the SFTP. There is an **English (AN)** and **French (FR)** version. Select all EN and FR pages that fadmin has split out (file names ending 0001, 0002, etc.) — **do NOT upload the combined file.** Confirm & Upload (page order follows the file-name number). Auto-group; ensure the correct language (AN / FR) is selected. Save & Confirm — **do NOT process internally.**
- **Pricing zones:** create an **EN** pricing zone (all applicable pages), Save & Next; create an **FR** pricing zone (all applicable pages), Save & Confirm. Add all stores to **both** zones.
- Attach the linking document to all tasks.
- **Setup QC:** confirm all pages uploaded (Pricing Zone → Items View) — **risk: confirm no pages left in the SFTP except the combined file.** Confirm flyer dates (provided by the retailer); 4 standard thumbnails; ensure preview dates set.

## ⚠️ Common errors / risk items

- **Upload / Tile Gen:** ensure the first page uses the **Ghost Script conversion library.**
- **Do NOT upload the combined file** — only the fadmin-split EN/FR pages.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** Linking document required (used for both Box/Tag). **Include** packaged deals (e.g. washers/dryers), retailer logo, social media, special weblinks. **Exclude** coupons and sign-up page.
- **Tag / Tag QC — Medium; Auto-tag ON.** Linking document required. Include everything: brand, name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** PDF preferred if clean; otherwise cutouts are accepted.

## FQC (Pre-Final owned by DOC; Item Image QC owned by Flex)

- Confirm dates (per PDF) and availability toggles; thumbnails correct and include retailer logo.
- Standard checks: all items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- **Flyer Review type: Lite (owned by DOL)** — flyer dates, sessions completed, previews showing correctly, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Corbeil Electromenagers OneGuide (Google Doc `1ZplpIdlCOkD_zIYkMr9S7eoPEBiYcqWgrbd30f-bRyw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Corner Market MS — Processing Guide

> **Source:** Corner Market MS OneGuide (Google Doc `1acIiKr5II4kACy0hzfybgY4CnD_8foZSH3ubndpAyF4`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | N/A |
| Flyer type(s) | Flyer (weekly) |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Wednesday, Valid From Wednesday; Available To Tuesday, Valid To Tuesday. **No preview.**
- **No linking document.**
- **Owners:** Upload & Setup = Vendor; FQC = Vendor.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP. The folder is named by the flyer's valid date — **always use the lower-case folder; do not upload the Upper Case folder.** Confirm & Upload → **Auto-Group** → Save & Complete.
- **Pricing zone:** create one zone called **Base**; add all stores; Save & Complete.
- **Setup QC:** confirm all pages uploaded — open the SFTP and ensure no pages remain except the **multi-page PDF** (the file with Upper Case letters that does not end in "P####"). Flag missed pages to the FT team. Confirm valid dates match page 1 of the PDF; 4 standard thumbnails; **Geography: ensure 0 changes to Stores or FSAs — flag ANY change to the FT team via Slack/email** (continue the checklist, but flag 100% of discrepancies). Platform toggles: available on ALL platforms.

## ⚠️ Common errors / risk items

- **Use the lower-case SFTP folder, never the Upper Case folder** (do not upload the multi-page PDF).
- **Geography must have 0 changes week over week** — flag 100% of store/FSA discrepancies to the FT team.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. Always include the **"Ad Price" badge in the same box as the main price.** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Include image (always select a clean PDF if available), brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Include "Ad Price" from the PDF in the **Description** if listed; common postfix "WITH APP"; disclaimers e.g. "LIMIT 2."

## FQC (owned by Vendor)

- Confirm valid dates (per PDF); platform toggles available everywhere; thumbnails drawn and include retailer logo.
- Standard checks: all items boxed and tagged; previews published and clickable.
- **Geography consistent with last week (no stores/FSAs added or removed) — immediately flag 100% of discrepancies to the FT Ops team** (does not block your work).
- **Flyer Review type: Lite (owned by Vendor).**

---
*Source: Corner Market MS OneGuide (Google Doc `1acIiKr5II4kACy0hzfybgY4CnD_8foZSH3ubndpAyF4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cosmaroma — Processing Guide

> **Source:** Cosmaroma OneGuide (Google Doc `1BRFlADo7O7zOD50Es3jwYrPTcBSeeuUeIjDbFV-L_2E`), updated Mar 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#cosmaroma`, `#flexflyerreview` |
| Flyer type(s) | Flyer — ad-hoc |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |

## Files & schedule

- **When files arrive:** ad-hoc (available/valid from/to are ad-hoc).
- **Linking document:** Yes.
- **Owners:** Upload & Setup = Flex; FQC = DOC.

## Upload & setup (owned by Flex)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP (clearly labelled with the valid date and promo name). Confirm & Upload. **Auto-Group** or manually add grouping numbers; ensure the correct language is selected. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create **Base**, select all applicable pages, Save & Confirm; add all applicable stores.
- **Setup QC:** confirm all pages uploaded (Pricing Zone → Items View) — **risk: confirm no pages left in the SFTP.** Confirm flyer dates (usually first/last page); complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **Late delivery:** files can arrive with 3 or fewer business days of lead time, which pushes out the available dates.
- **If uploading from SFTP, verify no pages remain un-uploaded.**

## QC specifics

- **Box Draw — Low complexity; Auto-Box OFF, Box QC bot ON.** Linking document required (used for both Box/Tag). **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF; brand = No.** Linking document required. Include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** standard pricing spotchecks included in pipeline.

## FQC (Pre-Final and Final owned by DOC)

- Confirm dates (per PDF) and availability toggles; thumbnails correct and include retailer logo.
- Standard checks: all items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- **Flyer Review type: Lite (owned by Flex).**

---
*Source: Cosmaroma OneGuide (Google Doc `1BRFlADo7O7zOD50Es3jwYrPTcBSeeuUeIjDbFV-L_2E`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Costello's Ace — Processing Guide

> **Source:** Costello's Ace OneGuide (Google Doc `1Fb0TAZIVBsDg-1BVVvH6Owh2XG-drx07WynFipr9vZQ`), updated May 28, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Flyer type(s) | Direct — ad-hoc, monthly × 2 |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **When files arrive:** ad-hoc; **monthly × 2.**
- **No preview; no linking document.**
- **Owners:** Upload & Setup = DOC; FQC = Flex.

## Upload & setup (owned by DOC)

- Setup instructions not filled in beyond the Setup QC checklist. **Setup QC:** confirm all items in the Setup QC checklist are correct.

## ⚠️ Common errors / risk items — URL tagging (most important)

**Tag each item's URL as follows:**
1. Copy the item's SKU if it has one.
2. Search the SKU in the top search bar of **acehardware.com**.
3. If an item shows up, copy its link and tag it as the URL.
4. If there is no item, the item has no SKU in the PDF, it has multiple SKUs, or the SKU starts with **"AR"** → search the **item name** on acehardware.com and add the search-result URL to the URL field.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. **Use text boxes where needed.** When boxing 2 items, **each SKU gets its own tag based on the overarching offer.** **Include** packaged deals. **Exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF; brand = No.** Include name, pre/postfix, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs** (see URL tagging above). **Exclude valid dates.**

## FQC (owned by Flex)

- **No special risk items** — use generic FQC review standards and instructions.
- **Flyer Review type: Lite (owned by Flex)** — no special risk items; use generic flyer-review standards.

---
*Source: Costello's Ace OneGuide (Google Doc `1Fb0TAZIVBsDg-1BVVvH6Owh2XG-drx07WynFipr9vZQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Couche-Tard — Processing Guide

> **Source:** Couche-Tard OneGuide (Google Doc `1cGPKJI87lLNpZ6OF20V7ph4f6Dc0XZ9c9HFS2amGC18`). Contacts/credentials omitted.
> Note: the source doc is labelled a mock-up; real account facts are captured below.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#circlek` |
| Flyer type(s) | Flyer (pub 7958) — ad-hoc, good lead time (~2 weeks in advance) |
| Processing | Auto-stack; **Flex not involved**; OS completes flyer processing only; no coupons; no Feedel |
| Language | **French only** |

## Files & schedule

- **When files arrive:** ad-hoc, ~2 weeks lead time.
- **Publication cadence:** varies; available 1 day before Live date; sometimes short run (e.g. Friday–Sunday).
- **Preview date:** set for **5 processing/business days after files are received** (files come with lots of lead time but the retailer requests the preview well in advance).
- **Owners:** Upload & Setup = Vendor; Image QC = Flex; FQC = DOC (plus send retailer preview).

## Upload & setup (owned by Flex)

- Retailer is not currently set up on the FTP — will need to be added. If the client sends files over email, pages may need to be added to the SFTP (flag to processor).
- Download pages from email (typically 3 pages).
- **Manual Upload:** Pages → Edit → select the PDFs → Upload → **toggle language to FRENCH** → Save → Auto-Group → Save & Complete.
- **Flyer Creation:** Start Task → 1 pricing zone (**Base**) → **language FRENCH** → Save & Done → Pricing Zones → add all stores.
- **⚠️ RISK: pages must be uploaded in French.**
- **Setup QC:** Available From = 1-day preview; Valid From / Available To / Valid To confirmed by retailer email (ad-hoc times). **Hidden on hosted, available on Flipp & Distribution.** Preview date = 5 days after files received. Internal Run Name = month; no external run name; no theme. Thumbnails Standard 4 (1065×600 ×2pg, Stock Premium ×1, Storefront Carousel Premium ×2, Storefront Carousel Organic ×1). Confirm sessions ran; no geography changes.

## ⚠️ Common errors / risk items

- **Pages must be uploaded in French** and the pricing zone language set to French.
- Retailer not on FTP — needs to be added.
- **Preview URL is in English but the flyer is French** — before sending, copy the URL, change `=en` to `=fr`, use a Montreal/Quebec postal code, review, then send the full URL to the retailer for review.

## QC specifics

- **Box Draw — Low complexity; Auto-Box OFF, Box QC bot OFF.** No linking document. Use text boxes when appropriate. **Milk page: box the entire page** (Sale Story = "Au prix minimum permis par la loi."). **Include** coupons and packaged deals. **Exclude** retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - Tag brand from extracted text / PDF / product images; **most items are Multi-Item** — select this and enter all brands. Name as on PDF; put quantity/amount in Description. Prefix = Multi-Buy; **watch for asterisks (\*) tied to disclaimers** (include as a postfix). Categories = Groceries — Food, Beverages (most appropriate sub-category). Choose a clean PDF image if available.
- **Image QC:** avoid PDFs with black shadows; select clear PDFs if available.

## FQC (owned by DOC)

- Edit Details: available/valid dates per retailer email; preview 5 days after setup; **hidden on Flipp**; no external run name; no theme.
- Thumbnails Standard 4; **legibility heights = 40/30.**
- Item Image QC: select clear PDFs, de-select images with black shadows.
- Pages tab: confirm tag & tag QC match; no page categories. Pricing Zone → Item View: all items boxed & tagged; full-screen preview. Geo tab: no changes.
- **Send preview link:** Overview → Ad-Hoc Processing → Preview URL — change `=en` to `=fr`, use a Montreal/Quebec postal code, send the full URL, wait for retailer approval, fix any corrections.
- **Flyer Review type: Lite (owned by DOL).**

## Out-of-processing

- Post-live page swaps, post-live checks, late links as needed.

---
*Source: Couche-Tard OneGuide (Google Doc `1cGPKJI87lLNpZ6OF20V7ph4f6Dc0XZ9c9HFS2amGC18`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Country Grocer — Processing Guide

> **Source:** Country Grocer OneGuide (Google Doc `1Hizvi4T3pJtXi1KyirQX5RK5LuoFdL8NY-UHcuznSfo`), updated Feb 18, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#countrygrocer`, `#flex-processingsupport`, `#flex-flyer-review` |
| Flyer type(s) | Flyer (pub 10740) — weekly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **When files arrive:** Monday (retailer typically uploads directly into SFTP Thursday/Friday).
- **Publication cadence:** Available From Wednesday, Valid From Wednesday; Available To Thursday, Valid To Thursday. **Base pricing zone gets a 2-day preview before the valid date.**
- **No linking document.**
- **Owners:** Upload & Setup = Flex; FQC = Flex.

## Upload & setup (owned by Vendor)

- Pages → Edit → select all pages for the dates you're working on → Auto sort → Save and complete.
- Flyer Creation → **add all pages to 2 pricing zones: Salt Spring and Base.**
- **⚠️ Salt Spring has different dates — set staggered dates by pricing zone.** Verify dates on page 1.
  - **Base** ("All Stores" on PDF page 1): Available from = **2 days before Valid from** (2-day consumer preview); Valid from / Available to / Valid to per PDF.
  - **Salt Spring:** Available from = same as Valid from (per PDF); Valid to / Available to per PDF (no extra preview).
- Add stores: Base gets the 'base' store set, Salt Spring gets the 'salt spring' store set. Wait for sessions; thumbnails Standard 4 (make sure logo shows); **hidden in hosted.**

## ⚠️ Common errors / risk items

- **Staggered dates by pricing zone** — Base gets a 2-day preview; Salt Spring does not. Verify against page 1.
- Assign the correct store set to each zone (base vs salt spring).
- Geography: no change in store geography week over week.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot ON.** No linking document. Box-draw all items with prices or sales stories (use text boxes when necessary); **box all visible URLs.** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price. **Exclude URLs.**
- **Image QC:** PDF images unless black background or unclear; prefer white-background PDF over cutout.

## FQC (owned by Flex)

- Check all pages and items boxed and tagged; Image QC per above.
- **Ensure staggered dates set by pricing zone** (Base = 2-day preview; Salt Spring per PDF).
- No change in store geography week over week.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps: follow the baseline page-swap procedure (video in the OneGuide).

---
*Source: Country Grocer OneGuide (Google Doc `1Hizvi4T3pJtXi1KyirQX5RK5LuoFdL8NY-UHcuznSfo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cub Cadet — Processing Guide

> **Source:** Cub Cadet OneGuide (Google Doc `1RdJHhBGa5Su4EvhQem4UXwggHiyRcnVhQdm_Z511OrE`), updated May 9, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#cub-cadet` |
| Hosted URL | cubcadet.ca |
| Flyer type(s) | Flyer (ID 11137) — monthly |
| Processing | Auto-stack; Flex = Processing Support; OS = Setup; no coupons; no Feedel |

## Files & schedule
- **Files received:** Monday. Available/Valid dates are on Page 1 or emailed by the retailer.
- **Linking document:** Yes — attach FTP links to task notes in Tag & QC.
- **Preview:** external preview name not needed unless the merchant requests it.

## Upload & setup (owned by Flex)
- Flyer run: "View Runs" in the **Flyer** flyer type (ID 11137) → Create New Flyer Run. Enter Available & Valid dates.
- **Upload:** Pages → Edit → Select Files → **Auto-Group** to sort → verify page order → Save and Complete.
- **Pricing zones:** EN and FR — **add all 236 stores to both**.
- Attach FTP links to task notes; confirm vendors are assigned.

## Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals (washers/dryers), retailer logo, sign-up page, social media, special weblinks. **Exclude coupons.**
- Linking document required (Box Draw/Box QC specific).

## Tag / Tag QC (Low; Auto-tag OFF; linking-doc required)
- **Name:** bolded, capitalized text. **Description:** the bullet-point details. **Brand field stays empty.**
- **SKU:** all items have a SKU — populate from the PDF.
- **URLs:** every item with a SKU gets a URL. Search the SKU in the linking document (attached to the vendor tasks per run) and copy the URL into the URL field.

## Image QC
- Standard item image QC (correct vs. incorrect image selection).

## FQC (owned by DOC)
- Ledge heights 45/35; run spotchecks; verify links/items tagged against the linking Word doc in the Vendors tab; item image QC; verify URLs in Sessions; horizontal & vertical preview; Pipeline → Final QC.
- **Flyer Review type: Lite.**

---
*Source: Cub Cadet OneGuide (Google Doc `1RdJHhBGa5Su4EvhQem4UXwggHiyRcnVhQdm_Z511OrE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Cub — Processing Guide

> **Source:** Cub OneGuide (Google Doc `1IGQXiDsT5h_9Ru8PIY1-9OYi5Tr-OjA0i1xDB0icJgw`), updated May 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#supervalu` |
| Hosted URL | cub.com/savings/view-ads.html |
| Flyer types | **Weekly Savings** (pub 2416) · **Special Savings / LTD** (pub 10563) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons |
| Strategic Ops | Yes — retailer data services (Feedel processing) |

## Files & schedule

- **When files arrive:** Monday (upload Wed/Thurs after the codesheet + PDF emails are received).
- **Publication cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday. **Staggered dates — always confirm against the PDFs.**
- **Linking document:** Yes — URLs on the insert page (only required for the insert page; proceed without it if not attached, as inserts/links often arrive late).
- **Owners:** Upload & Setup = DOC; Image QC = Flex; FQC = Flex.

## Upload & setup (owned by DOC)

- Download files from the emailed codesheet/PDFs and upload to SFTP with the manipulated **.txt** file.
- Save the codesheet(s) as **.csv**. Usually no manipulation needed, **but** check for pages named **GATE** or **INSERT** — rename so all pages are labelled **PAGE 1, PAGE 2, PAGE 3**, etc.
- **Codesheet upload:** config name **`farm_fresh_supermarkets`**; PDF base directory = entire base path; **uncheck region assignment and combine zones.**
- **Setup QC — staggered dates (always check against the PDFs):**
  - **Available from:** earliest date in the email, **1:00 AM**
  - **Available to:** one day **after** the last date in the email, **12:59 AM**
  - **Valid from:** one day **after** the earliest date in the email, **3:00 AM**
  - **Valid to:** final date in the email, **11:59 PM**
  - Available everywhere; no theme; four standard thumbnails.

## ⚠️ Common errors / risk items

- **Staggered dates** — always confirm against the PDFs (see the AM/PM times above).
- Rename **GATE**/**INSERT** pages to PAGE 1, 2, 3… before codesheet upload.
- **Banners / Cub rewards callouts are excluded during Box Draw** — Cub tells the Ops team when they need to be boxed/tagged, done during FQC with retailer-provided URLs (not every week).
- Linking spreadsheet is only for the insert page — process without it if not attached (inserts/links often late).

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. Box all items; **draw sub-items separately** when small items with different prices are embedded in a larger box. **Include** coupons and packaged deals. **Exclude** retailer logo, sign-up page, social media, special weblinks — and **exclude** the Cub / My Cub Rewards logo, brand logos, banners, and Cub reward callouts (handled at FQC when needed).
- **Tag / Tag QC — Low; Auto-tag ON; PDF image auto-selection ON.** Linking document required (insert page only). Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude SKU (no longer required), disclaimer, URLs.**
  - Tag the **BOLDED** name. Postfixes include "lb with myCUB rewards", "with my Cub rewards", "when you buy any ### or participating item" (all in the dropdown). Every item requires a category. If multiple items sit under a header, ensure they **all** have Valid From/To dates. Insert page items → tag as **Links** (name + URL only).
- **Image QC:** **PDF image preferred over cutout** (e.g. California Jumbo Cherries, 80% Lean Ground Beef).

## FQC (owned by Flex)

- **Staggered dates** (recheck against PDFs, times as above).
- Thumbnails correct and include retailer logo.
- Standard checks: all items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- **Doable Dinners banners:** tag as items with URL `cub.com/sm/pickup/rsid/1612/meals` (if a QR code with no products, tag as a link). **Digital coupons:** tag as items with URL `cub.com/coupon-gallery`.
- **Flyer Review type: Lite.**

## Out-of-processing — Digital Inserts

- Refer to the "digital inserts" email and add inserts into each pricing zone.
- Manually upload the insert pages (split first if multiple pages). Mark Flyer Creation complete — **do not create new PZs.**
- Box and tag the insert page(s) with the URLs from the email — all items tagged as **Links** (name + URL; URLs from the email, names at processor discretion).
- Confirm whether inserts are version-specific (noted in the email); add inserts to all pricing zones **always after** the main flyer pages.
- After sessions re-run: verify URLs and re-run page tile generation.
- Page swaps: follow the baseline page-swap procedure (video in the OneGuide).

---
*Source: Cub OneGuide (Google Doc `1IGQXiDsT5h_9Ru8PIY1-9OYi5Tr-OjA0i1xDB0icJgw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Curtis Lumber — Processing Guide

> **Source:** Curtis Lumber OneGuide (Google Doc `1ru6RyzaNCH812gBbi3cZeG20_z_Vhiky5WhDOoxlHBI`), updated Sep 23, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms (**Hosted only if no pricing**) |
| Slack channels | `#curtis-lumber` |
| Hosted URL | None |
| Flyer type(s) | Sales Flyer (ID 3801) — **ad-hoc** |
| Processing | Auto-stack; multiple parties set up/upload; Flex = FQC; no coupons; no Feedel |

## Files & schedule
- **Files received:** ad-hoc. Retailer emails PSS that files are in the FTP; Flex sets up for Vendor upload; Vendor uploads.
- **Publication:** ad-hoc; **no consumer preview — Valid & Available dates are the same.**
- **Store assignment:** applied per a Word doc uploaded to the FTP that outlines dates + store assignment.
- No linking document.

## Upload & setup
- Manual Upload → Pages tab → Edit → Select Files from FTP → Save & Complete.
- Flyer Creation → Start Task. **One pricing zone: Base** → Save & Done.
- Apply stores per the retailer's instructions doc.
- **Setup QC — Edit Details:** confirm dates match the PDF (no preview date); available all platforms (Hosted only if no pricing); Internal Run Name = first-page callout; external run name = none; no theme. Thumbnails Standard 4. Confirm sessions ran; Geography unchanged.

## Box Draw (Low — Auto-Box OFF, Box QC bot OFF)
- **Include:** coupons, packaged deals, retailer logo. **Exclude:** sign-up page, social media, special weblinks.
- **Logo** (page 1) → box + link to curtislumber.com. **Locations** (last page) → link to curtislumber.com/locations/.
- Box **doors separately**. **Super coupons** → box and tag as coupons (change Display Type to Coupon).

## Tag / Tag QC (Low; Auto-tag ON)
- **Include** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs** (no item URLs). Brand: no.
- **Name:** item name is bold; include the brand (if any) in Brand and Name. Price-chart descriptors beside/above the price should be included with the item name.
- **Description:** usually unbolded text (occasionally some bold).
- **SKU:** if present, enter in SKU field. **Prefix** e.g. "STARTING AT"; **postfix** e.g. "Lin. Ft."
- **Valid dates:** tag item-level overrides if different from the flyer.
- **Categories:** mostly Home & Garden.
- **Images:** PDF preferred; use cutout when no clean image; choose best available.

## FQC (owned by Vendor/Flex; Lite)
- Ops spotcheck; mark Auto Stack Spot Check complete; confirm vendor tasks done.
- Edit Details: dates match flyer; available everywhere; no preview date; internal run name = 1st-page callout; no theme. Thumbnails Standard 4.
- Tag/Tag QC both green; remove page categories from Pg 1 (judgment elsewhere); confirm Store Logo & Store Locator URLs added; sessions ran & FSAs generated; verify URLs; **mark items In-Store Only**; Geography unchanged.
- **"Not all categories used in pricing zones have thumbnails" warning — OK to ignore.**

## Out-of-processing
- Page swaps are standard (baseline page-swap video).

---
*Source: Curtis Lumber OneGuide (Google Doc `1ru6RyzaNCH812gBbi3cZeG20_z_Vhiky5WhDOoxlHBI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# CVS Pharmacy (incl. Longs Drugs & Y Mas) — Processing Guide

> **Source:** CVS OneGuide 2.0 (Google Doc `1IHjYNkHXNY6nLtOa_oKs2ZSrKa41BWveiKrzBAU2B9w`), updated Jun 23, 2026. Contacts/credentials omitted.

CVS has **four flyer types — CVS Weekly, Y Mas, Longs Drugs, and Navarro** — processed differently. The Weekly flyer is the complex one (Ad Block IDs, tagging & pagination documents attached to tasks); Navarro and Y Mas are simpler and get no attachments.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard |
| Availability | Weekly / Y Mas — all platforms · **Longs Drugs — Hosted only** · Navarro — all platforms (one Flipp version in the Navarro merchant + one Hosted-only version in the CVS merchant) |
| Slack channels | `#cvs` |
| Hosted URLs | cvs.com/weeklyad/pageview · longs.com/weekly-ad.html · navarro.com/weekly-ad |
| FAdmin merchants | CVS Pharmacy 2264 (Weekly, Y Mas, Longs, Navarro Hosted-only) · Navarro Discount Pharmacy 3026 (Navarro Flipp version) |
| Processing | Auto-stack; **no Flex**; OS completes coupon processing; no Feedel |

## Files & schedule (publication)

| Flyer | Available/Valid | Files & processing |
|---|---|---|
| **CVS Weekly** | Avail From Thu · Valid From Sun · Avail/Valid To Sun @ 2:59 AM | PDFs received well in advance (v23.47 may arrive separately). Tagging doc 5–8 days prior (can upload but not process). Ad Block URLs Mon–Wed before Thu go-live. Coupon doc Wednesdays; coupon corrections Mondays. |
| **Longs** | Avail/Valid From Sun @ 6 AM · To Sun @ 5:59 AM | Files Wednesday evenings; upload & FQC Thu/Fri. |
| **Y Mas** | Avail/Valid From Wed · To Tue (2-week run) | Files 5+ business days ahead; processing day set by processor. |
| **Navarro** | Avail/Valid From Wed · To Tue | Files 2–5 business days ahead; latest upload Mon, latest FQC Tue. |

**Weekly workflow:** Mon = upload Week 2 + coupon corrections · Wed = upload Week 1 + full FQC + flyer review · Thu = Longs upload/FQC · Fri = Ad Block URLs imported + Longs/Y Mas flyer review.

## Upload & setup — Weekly (owned by Vendor; Flyer Type 498)
PDFs arrive via a OneDrive link (email login code to the processor or the CVS alias). Download all files/folders, then log into the CVS SFTP (**username is "CVS" — all caps; lowercase fails**). Non-Weekly banners load into the SFTP as-is; **Weekly requires file prep first.**

**Weekly file prep:**
- Unzip and rename the folder `MM-DD Ad Event`. If v23.47 arrived separately, copy that folder into the main folder (skip the PVT_Zone_Memo).
- In folders **v65, v57, v91, v23-47**, confirm the naming convention `MM-Dp0#v[PZrange]` — page numbers under 10 must have a leading zero (`p01`, not `p1`); `v` always sits between page number and version. v65/v57 have no range.
- In **Core-Zoned**: files like `p02v3-99` are fine as-is. **"All except" files must be renamed.** "All except" = a base page delivered to all zones except those covered by alternate pages (zone sequence runs 1–134). E.g. `p01AllExceptv3-99` → base goes to zones 1 and 134 → rename `p01v1-134`. If 1 or 134 are listed, use the codesheet to find the base sequence's first/last (commonly v3-75). Transfer the folder into "CVS Weekly" in the SFTP.

**Codesheet (Zone Memo) manipulation:** import ZoneMemo `.xlsx` to Google Sheets. Zone groups split into tabs by shared pages (Base v3-75, v23.47, v54, v65 Manhattan, v91, etc.). FAdmin reads the page number (left column) for pagination and the version sequence (second column) for zone placement — it uses the **first and last** number in the sequence as the page-name identifier.
- **Core Ad tab:** scroll to the red "For Flipp Processing" section, delete data between the `page, version, base pricing` headers and the first line under "for flipp processing" (**keep the headers**).
- Duplicate the tab for v23.47, v57, v65, v91, and any other unique folder; put the version under VERSION; delete duplicate page rows created by the duplication.
- Save `.xlsx`, upload to the flyer run.
- **RISK:** a PZ left out of the middle of a version sequence means the page won't be added to that zone. Errors are usually a typo or a wrong page name in the SFTP.
- **After upload — DO NOT change Available/Valid To dates** (early changes cause excessive item-validity spotchecks); adjust in Pre-FQC.
- Sort PZ pages low→high to verify page counts (v65/54/23/47), then high→low to catch double pages.

**Common codesheet errors:** "No page with version x and page number # was found" — check the PDF name vs the codesheet (a page may be mislabeled, e.g. codesheet says p03 but file is p02v43-78), or the leading "0" after "p" is missing. A duplicated row (or a PZ listed in the middle of two rows) also errors — check the page-PDF bottom edges for the source of truth and delete the extra row.

**Setup QC — attach Vendor attachments:** Tagging Document (no manipulation); Table of Contents Category Pagination (update each tab with each category's page #, download `.xlsx`); Ad Block IDs (merge the Core Zone PDFs into one document and attach).

## ⚠️ Common errors / risk items (retailer-specific)
- **Featured product headers** (groups at the top of category pages): use a **cutout** of the whole selection; unless a specific product name is listed, use the category name (e.g. "Shave & Deodorant") and capture "See below for additional details" in the Sale Story.
- **Large item spreads under one product name:** box together when possible (all items share the same name and tagging); when layout prevents it, box separately but keep the **same name and identical tagging.**
- **Two items with different prices must NOT be boxed as one.**
- **Auto-Tag gets many CVS rules wrong** — you must review and adjust EVERY item. Pay extra attention to Descriptions and Name typos.

## Box Draw (Medium — Auto-Box OFF, Box QC bot ON; linking-doc required)
- **Include:** disclaimers, coupons, packaged deals; special weblinks (Weekly only). **Exclude:** sign-up page, social media.
- Box the "Find it Quick" header and its categories separately; **box the capitalized section headers** (HEALTH, BEAUTY, PERSONAL CARE, FOOD & HOUSEHOLD, OTHER OFFERS). Box "Back to Find it Quick" icons and category headers.
- **Box ALL text on the page even if not for sale** (for text-to-speech) — for Weekly, refer to the Tagging Document `.xlsx` for the list. **Avoid text boxes** — prefer two separate default boxes.
- Box the small black "Go to… for…" URL banners.

## Tag / Tag QC (Medium; Auto-tag ON; PDF image auto-selection ON)
- **Include** all fields (name, brand, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs).
- **Name** contains ALL identifying text **including sizes** and any "ANY"/"ALL"; put exclusions with the name text (not the disclaimer). **All sale info other than Current Price goes in the Sale Story** (include the full discount text and any `*`/`††` symbols).
- **SKU = Ad Block Numbers** from the attached "MM-DD Ad Block IDs" PDF (the number in the black box). Almost all items have one; a few (v57/v65/v23-47 unique SKUs) won't appear in the merged PDF — add missing SKUs via Google Sheets during/after Pre-FQC.
- **Description:** sizes and **all badge/banner text** (Same day pickup, New at CVS, Mix & Match, Send to Card, red-box/circle text).
- **Custom fields:** `Extrabucks` (write "Extrabucks" when the word appears — powers a Hosted front-end integration); `Print MFR Coupon` (amount when a Digital mfr coupon is referenced; fill both if it also references Extrabucks).
- **Table of Contents:** "Find it quick!" header tagged as an Item; TOC directions and headers tagged as **Page Links** per the Pagination `.xlsx`. Category page headers tagged as Items.

## Image QC
- Select a **clean PDF image** (lifestyle/plated preferred over cutouts). **Multi-item:** use a clean PDF of the FIRST listed item (move down the list if needed).
- **Cutout only** for text-only items and for **category page header groups** (items directly under a category header like Household); all other items on that page get a PDF.

## Post-processing (owned by DOC)
- **Item Category QC:** select a category for every item; for multi-item names use the first item's category.
- **FQC codesheets:** run the **Staggered Dates codesheet** (unchanged week over week) and the **Eventmaster store codesheet** (paste the header row from an old eventmaster; delete all "Puerto Rico" rows in column I; save `.xlsx`/`.csv` and upload).
- **Pre-FQC:** mark spotcheck complete; standard thumbnails; leg heights 55/35. Edit Details → update Available/Valid To to Sun @ 2:59 AM; External Preview Name "Sneak Peek"; no theme.
- **Item Search QC automation (as of July 2026):** Export Items → drag the `.csv` into the **CVS Automation** Google Colab notebook → run → Import the cleaned `.csv` (~10 min). The automation: (1) flips PAGE_LINK→ITEM for page > 7 non-nav rows; (2) clears stray categories where sale_story + current price are blank; (3) moves ct./pk./oz. sizing from description into name; (4) moves parenthetical "(excludes …)" exclusions into the name; (5) sets the Extrabucks flag from sale_story and renames the column `id_1`. Then manually check for PAGE_LINK-vs-ITEM outliers ("Back to Find it quick" boxes should be Page Links to the TOC page; black-background category names are Page Links).
- **Ad Block URLs** imported Friday (post-processing).

## Flyer Review
- **Weekly:** Wednesday. **Longs/Y Mas:** Friday. Coupon QC checks Thursdays & Sundays; coupon revisions Mondays.

---
*Source: CVS OneGuide 2.0 (Google Doc `1IHjYNkHXNY6nLtOa_oKs2ZSrKa41BWveiKrzBAU2B9w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
