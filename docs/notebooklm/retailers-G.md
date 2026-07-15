# Retailer Processing Guides — G

> Bundle of 22 retailer-specific processing guides (G). Contacts and credentials are omitted from every guide.

**Contains:** Gagnon - La Grande Quincaillerie, Gala Supermarket, Gallery1 Furniture, GameStop, Garry's Garden Gallery, Gelson's, Georgia Main Food Groups (Fresh St. Market & Marketplace IGA), Giant Carlisle & Martin's Foods, Giant Eagle, Giant Tiger, Global Pet Foods (Not NL/PE), Globo Shoes, Go Sport, Goemans Appliances, Good Neighbour Pharmacy, Goodness Me, Gordon Food Services, Gosselin Photo, GP Bikes, Green Valley Marketplace, Grocery Outlet, Guardian & I.D.A.


---

# Gagnon - La Grande Quincaillerie — Processing Guide

> **Source:** Gagnon - La Grande Quincaillerie OneGuide (Google Doc `16STfi9ElJ6QuJRalTXckIJ4Z55obYTM6Vxfv9jAG-3k`), updated Mar 13, 2026. Contacts/credentials omitted.

Bilingual (French/English) hardware retailer. Flyer Type 11017.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#gagnon-la-grande-quincaillerie`, `#flex-processingsupport` |
| Hosted URL | gagnonlgq.com/pages/fr-circulaire_promo |
| Flyer types | Weekly (11017) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Thursday (client emails to confirm files added to SFTP).
- **Cadence:** Available/Valid are **Ad Hoc** — client confirms dates in the file-announcement email.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC). Flyer Review owned by DOL.

## Upload & setup

- Manually upload pages (**Language: French**).
- Create **two pricing zones:**
  - **"French"**
  - **"English"** → uses the **Cross-language setting.**
- Ensure all stores are added to **both** zones. Available and valid dates are the same.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** include packaged deals; exclude coupons, retailer logo, sign-up page, social media, special weblinks. Box each product block that has a price and/or sales story.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand is box-draw specific.
  - **SKU:** all products have a SKU visible in the PDF (numbers, or numbers + letters). If multiple SKUs in one ad block, enter only the **first** SKU.
  - **URLs:** every item with a SKU needs a corresponding URL. **URL tagging process:** open gagnonlgq.com, search the SKU in the site search bar, copy the URL from the address bar, paste into the URL field in FAdmin.
- **Image QC:** choose white-background PDF where possible, else cutout.
- **Spotchecks:** N/A.

## Final QC / go-live notes

- Post-processing: mark autostack spotcheck complete; check image QC (uncheck PDF Image); run sessions if needed; confirm boxed & tagged.
- **⚠️ LINK QC:** check that **all items have a URL** — refer to the URL tagging process if any are missing.
- Check dates; no theme; draw standard 4 thumbnails. Client may send direct links via email ahead of go-live.
- **Item Category QC (DOC):** page categories for all pages except the first (1 per page).
- **Flyer Review type: Lite.**

---
*Source: Gagnon - La Grande Quincaillerie OneGuide (Google Doc `16STfi9ElJ6QuJRalTXckIJ4Z55obYTM6Vxfv9jAG-3k`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Gala Supermarket — Processing Guide

> **Source:** Gala Supermarket OneGuide (Google Doc `1NCel4CP401CLWF2r-lrCIx9e0Er33VOdGQimIQ-yQUI`). Contacts/credentials omitted.

Multi-store grocery banner (Flyer 12257). Files arrive per-store with confusing naming conventions — see the store-code reference below.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Basic |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | Weekly (12257) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available/Valid Friday → Thursday.
- **Setup & Pre-FQC owned by** FLEX (pre-FQC checklist owned by Vendor); Final QC by FLEX.

## Upload & setup

- **Manual Upload** (Pages Tab → Edit → select from SFTP). Files sit in multiple folders with confusing names. Manually add the store name to Page Name and page numbers into the Grouping Number field; ensure correct language. Save & Confirm.
- **Store-file naming reference** (`##` = launch date):
  - **Patchogue** — `GC00## P01 PC 02##` (folder contains "patchogue")
  - **Worcester** — `GC00## P01 MA 02##` (folder contains "worcester" or "Mass")
  - **Brentwood** — `01 Gala 2 ##`, no code on filename (folder "flippbrentwood"; add "Brentwood" in FAdmin)
  - **Freeport Baldwin** — `GC00## P01 FB 02##` (folder "fqflippgalafreeportbaldwin", also "nassau", nested under "Gala Foods")
  - **Bridgeport** — `GC00## P01 BR 02##` (folder contains "bridgeport")
  - **Centereach** — `Feb ## P1` (folder "flippgalacentereach"; files lack the name — add in FAdmin; only 2 files, Servlet Email Attachment = Page 2)
  - **Boca Raton** — `4370 Gala Fresh ## ## 26` (store code 4370; folder "boca raton" under GalaFresh)
  - **Lakeworth** — `4371 Gala Fresh ## ## 26` (store code 4371; folder "lakeworth" under GalaFresh)
  - **Riverhead Shirley** — `GC00## P01 RV 02##` (folder contains "riverhead")
- **Pricing Zones:** create a zone per store group (only if files exist) and select applicable pages; add all applicable stores via Store Sets.

### ⚠️ Common errors / risk items
- **Retailer does NOT consistently send files for all stores week over week — missing stores is OK.** Geography will *not* be consistent WoW; a discrepancy is acceptable as long as all FTP files were uploaded.
- Confirm no pages remain unuploaded in the SFTP.
- Centereach has no store code — easier to identify/name that file first.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each product block.
- **Tag / Tag QC (Low; linking doc required; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Basic tagging guidelines apply.
- **Image QC:** PDF preferred if clean, otherwise cutouts.
- **Spotchecks:** standard pricing spotchecks.

## Final QC / go-live notes

- Confirm dates vs. PDF; available on all platforms; thumbnails include logo; all items boxed/tagged; spotchecks complete (20% of zones); previews clickable; sessions complete.
- **Flyer Review type: Lite** (flyer review guide exists per the OneGuide).

---
*Source: Gala Supermarket OneGuide (Google Doc `1NCel4CP401CLWF2r-lrCIx9e0Er33VOdGQimIQ-yQUI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Gallery1 Furniture — Processing Guide

> **Source:** Gallery1 Furniture OneGuide (Google Doc `11pK7LdlQNzYD2hIS5uuKi2u2JFudEkr1xocq97JTtVQ`), updated Jul 22, 2024. Contacts/credentials omitted.

Furniture retailer (part of The Atrium). Ad-hoc, direct publications; linking-document driven.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | Under construction (site: theatrium.ca) |
| Flyer types | Direct (1 type) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad-hoc, sent via email including the linking doc.
- **Cadence:** Ad-hoc. No preview date.
- **Setup & FQC owned by** FLEX; Flyer Review owned by Vendor.

## Upload & setup

- Files sent via email including linking doc.
- **1 zone, English, all pages, all stores assigned.**
- **Attach the linking doc to the vendor tasks.**

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude valid dates.** No brand.
  - Standard tagging: **Product Name, Active Price (as shown in flyer), Link/URL** — refer to the linking document for these details. Capture the Sales Story from the item's image.
  - If no linking doc is found under Vendor tasks, **confirm with DOC.**
- **Item Image QC (DOC):** use **cutout images.**

## Final QC / go-live notes

- Standard 4 thumbnails; no theme; available everywhere.
- **⚠️ Geography: No stores or FSAs/zips were added or removed.**
- Complete FQC checklist.
- **Flyer Review type: Lite** (shared review guide with Ashley Homestore Atlantic & WorldWide Furniture).

---
*Source: Gallery1 Furniture OneGuide (Google Doc `11pK7LdlQNzYD2hIS5uuKi2u2JFudEkr1xocq97JTtVQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# GameStop — Processing Guide

> **Source:** GameStop / EB Games OneGuide (Google Doc `1cU4aPMgOuJkdvrPUK_M5NjjCwg9vhVfBxu__EJ2r6Ps`), updated Feb 3, 2026. Contacts/credentials omitted.

Runs under the EB Games banner in Flipp. Bilingual (EN/FR) with Quebec-specific "ECO" pages.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#ebgames`, `#flex-processingsupport` |
| Hosted URL | N/A |
| Flyer types | Weekly (Type 1) · Monthly (Type 2) |
| Processing | Auto-stack; Flex (Flyer Review), OS (Setup); no coupons; **Feedel processing (yes)** |

## Files & schedule

- **Files received:** Ad-hoc; retailer sends file-drop notifications and instructions by email. Sometimes sends URLs with UTMs.
- **Cadence:** Ad-hoc (Available/Valid Ad-hoc).
- **Setup owned by** DOC; FQC by FLEX.

## Upload & setup

- **Create Flyer run:** Flyer run type = Flyer; Distribution Categories = Electronics; Internal Run Name = Date-Month.
- **Manual Upload:** files in SFTP; change language to **French** for all pages labeled **FR**; Auto Group → Save and Complete.
- **Pricing Zones (English & French versions):** separate zones for English pages, French pages, and **ECO** pages (you won't always receive ECO pages).
- **Store assignment:**
  - All ECO pages (French and English) → **Quebec region.**
  - The rest → **National-excluding-Quebec.**
  - If only ENG and FRE pages are received, distribute both versions **nationally.**
- Setup QC: dates match PDF, hide in hosted, no theme unless specified, Standard 4 thumbnails, mark items In-Store Only, check pages/zones/sessions/vendors. **Attach the linking document to vendor tasks.**

### ⚠️ Common errors / risk items
- Geography can change WoW depending on whether ECO/Quebec pages are present.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot OFF):** include special weblinks; exclude coupons, packaged deals, retailer logo, sign-up page, social media.
  - If a multi-item name has **"or"** and the price says **"ea.,"** box the products separately.
  - If multiple items sit under one banner (e.g. "Available Now," "50% off") and the linking doc has only **one URL**, box and tag the items separately.
- **Tag / Tag QC (Low; linking doc required; Auto-tag OFF; PDF Image Auto Selection ON):** include name, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude pre/postfix and valid dates.** Brand is box-specific.
  - Add SKUs in the **description** field. SKU found alongside certain games; if none, omit. Names are sometimes obscure.
- **Image QC:** select clean PDF when possible, cutouts if none available.

## Final QC / go-live notes

- Mark Auto Stack Spotcheck complete; check dates vs. PDF; hidden in hosted; mark items In-Store Only; Standard 4 thumbnails.
- Pricing zones: ECO → Quebec region, all others → National (excl. Quebec); confirm EN/FR language settings.
- **Ignore** the "Not all categories that are used in pricing zones have thumbnails" warning.
- **Flyer Review type: Lite.**

## Out-of-processing

- Instructions for page swaps / post-live checks live in the OneGuide (not filled in here).

---
*Source: GameStop / EB Games OneGuide (Google Doc `1cU4aPMgOuJkdvrPUK_M5NjjCwg9vhVfBxu__EJ2r6Ps`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Garry's Garden Gallery — Processing Guide

> **Source:** Garry's Garden Gallery OneGuide (Google Doc `1xnstn5QfiND4BR3FJTd0Xq4N11b6qsMBYGJgBUQqR90`), updated Feb 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | Flyer (1 type) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available Thursday → Thursday; Valid Friday → Thursday.
- **Workflow:** Upload & Setup, Image QC, and FQC all owned by FLEX.

## Upload & setup

- **Manual Upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload → Auto-Group (or manually add grouping numbers); ensure correct language → Save & Confirm. **Do NOT Process Internally.**
- **Pricing Zone:** create **Base** zone, select all pages, add all stores.
- Setup QC: confirm all pages uploaded (Items View), confirm flyer dates, Thumbnails (4 Standard), preview dates set.

### ⚠️ Common errors / risk items
- **Storefront Spotchecks — page merging:** **unmerge any merged pages.**
- Confirm no pages remain unuploaded in the SFTP.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Anything with a price should be boxed.**
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Brand used for both box/tag.
- **Spotchecks:** standard pricing spotchecks.

## Final QC / go-live notes

- Pre-FQC (FLEX): confirm dates vs. PDF; availability toggles; thumbnails include logo; all boxed/tagged; spotchecks complete (20% of zones); previews clickable; sessions complete; geography unchanged; **Hidden in Hosted.**
- **Flyer Review type: Lite.**

## Out-of-processing

- **Page Swap:** baseline page-swap process (video in the OneGuide).

---
*Source: Garry's Garden Gallery OneGuide (Google Doc `1xnstn5QfiND4BR3FJTd0Xq4N11b6qsMBYGJgBUQqR90`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Gelson's — Processing Guide

> **Source:** Gelson's OneGuide (Google Doc `14PFsi5gwWEqc_bVP2FC6985PNJQMb4CkXyG7Ifck7Mw`), updated Aug 20, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1p_gelsons` |
| Hosted URL | N/A |
| Flyer types | Weekly flyer (11810) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available Thursday → Wednesday; Valid Wednesday → Thursday. No preview date, no linking document.
- **Setup owned by** FLEX; Pre-FQC & Final QC by DOC.

## Upload & setup

- **Manual Upload:** Pages Tab → Edit → select all from SFTP → Confirm & Upload → Auto-Group → Save & Confirm. **Do NOT Process Internally.**
- **Pricing Zone:** create **Base** zone, select all pages, add all stores.
- Setup QC: confirm all pages uploaded (Items View, and no unuploaded pages in SFTP), confirm flyer dates, Thumbnails (4 Standard).

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item with a unique price. (Retailer logo not required.)
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude SKU.** No brand.
- **Spotchecks:** standard pricing spotchecks.

## Final QC / go-live notes

- Pre-FQC (DOC): confirm dates vs. PDF; availability toggles; thumbnails include logo; all boxed/tagged; spotchecks complete (20% of zones); previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (owned by DOL) — flyer dates, sessions complete, previews correct, items tagged accurately, geography consistent, toggles correct.

---
*Source: Gelson's OneGuide (Google Doc `14PFsi5gwWEqc_bVP2FC6985PNJQMb4CkXyG7Ifck7Mw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Georgia Main Food Groups (Fresh St. Market & Marketplace IGA) — Processing Guide

> **Source:** Fresh St. Market / Georgia Main OneGuide (Google Doc `1L3j0DHPnY6UYGXjn_MwkKxlXCoGsGxbasmC2ONG38xc`), updated Sep 19, 2024. Contacts/credentials omitted.

Covers both **Fresh St. Market** and **Marketplace IGA** banners (Flyer 4283). **OBQB account** — box/tag everything more closely.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#georgia-main-food-group` |
| Flyer types | Weekly (4283) |
| Processing | Auto-stack; Flex (Flyer Review), OS (Setup); no coupons; **Feedel processing (yes)** |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available/Valid Friday → Thursday. No consumer preview.
- **Setup owned by** Vendor; FQC by DOC.

## Upload & setup

- Files uploaded to SFTP; pages manually uploaded to the flyer run.
- **1 PZ, EN only.** Select the lowercase page files matching the week:
  - **Marketplace IGA** receives the **`iga`** lowercase pages.
  - **Fresh St. Market** receives the **`freshstreet`** pages.
- Auto Group Pages → Save & Complete. When Flyer Creation is available, start task → create **one pricing zone named "Base"** with all pages → Save & Done. While tile generation runs, add all stores to the pricing zone.
- Valid dates should match page 1 (ads run Friday → Thursday, no consumer preview).

### ⚠️ Common errors / risk items
- Look for **multiple products** in one ad block.
- OBQB account — verify **all** shoppable items are boxed and tagged (check more closely than usual).

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot ON):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - **Box each item with a different price; one box per offer. Do NOT use text boxes.**
  - Do not box QR codes unless stated.
- **Tag / Tag QC (Low, SIMPLIFIED POP; linking doc required; Auto-tag OFF; PDF Image Auto Selection OFF):** include name, pre/postfix, description, price, categories, original price. **Exclude valid dates, SKU, sale story, disclaimer, URLs.** No brand. Tag the name, price, pre/postfix, and category.
- **Image QC:** N/A per the OneGuide.

## Final QC / go-live notes

- Edit Details: dates Available/Valid Friday → Thursday; no external run name; **Hide in Hosted checked; No Theme.**
- **Leg heights 45/35.** Thumbnails Standard 4. Add all stores to Base pricing zone.
- **Flyer Review type: Lite.**

---
*Source: Georgia Main Food Groups OneGuide (Google Doc `1L3j0DHPnY6UYGXjn_MwkKxlXCoGsGxbasmC2ONG38xc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Giant Carlisle & Martin's Foods — Processing Guide

> **Source:** Giant Carlisle & Martin's Foods OneGuide (Google Doc `1w3auLK-JsRcPzRJgoAwPbIPdJ2-bFu6wGt3h5X3Yflw`), updated May 6, 2026. Contacts/credentials omitted.

Royal Ahold banners processed together (same process). **High-touch account** with a codesheet-heavy setup, high-res page requirements, and many retailer-specific rules.

## Account at a glance

| | |
|---|---|
| Account tier | Core (CXE Core pod) |
| Availability | All platforms |
| Slack channels | `#3fl-royal-ahold`, `ahold-delhaize`, `ahold-ops` |
| Hosted URLs | giantfoodstores.com · martinsfoods.com/savings/weekly-ad/print-view |
| Flyer types | Giant Carlisle Weekly Circular (6405) · Martin's Foods Weekly Circular (5541) |
| Processing | Auto-stack; 3FL Flex (Processing Support); no coupons; **Feedel processing (yes)** |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available Thursday, Valid Friday → Thursday. **Preview: Monday** before go-live.
- **Workflow:** Upload & Setup (Flex), Image QC (Flex), FQC (Flex); files transferred by DOC. Add both runs to the Royal Aholds Flex Processing Tracker.

## Upload & setup

### Transfer files (DOC)
- AEM portal → The Giant Company (GC) → Marketing → Weekly Ad → Weekly Circular → working week → Final Files → download **Final PDFs**.
- Use the **Flipp Digital Pages** folder (verify a C07 page has **no barcodes**).
- **⚠️ Delete the "Page 07" folder entirely** — it has the same pages as Flipp Digital Pages but **with barcodes** (we don't want barcodes).
- **NEW May 2026:** there may be a file named **"MY"** in Flipp Digital Pages (often page 3, not 7). Note its page number, find the corresponding "MY" page **with barcodes** in that page-number folder, and delete it.
- Upload pages to the file-drop software (GC → 2026 Files → new folder). Royal Ahold pages are **very high quality / bulky** and slow to transfer.

### ⚠️ #1 Risk — page height must be set to 4096 pixels BEFORE any upload
- In **[Edit details]**, set page **height to 4096 pixels before ANY upload steps / before running any codesheets.**
- If done after codesheets run (or missed), **the run must be re-uploaded and reprocessed entirely** — a huge go-live/CUSAT risk. **Notify the coordinator immediately if missed.** Royal Ahold sends such high-quality pages they won't render at lower pixel heights.

### Codesheet manipulations & upload
- From SFTP → working week → Recapper → download **both** the **Ad Version Sheet** and **Recapper**.
- **Ad Version Sheet = store distro / pricing-zone codesheet.** Trim to headers (Store #, Ad Version, Giant, Martin's); rename Store # → Store Numbers, Ad Version → Zone (column A), add a "TBD" column; filter; delete blue-highlighted rows down. Duplicate into **GC** and **MF** tabs, then in each keep only that banner's stores (filter the other banner's "X" rows and delete). Download each as CSV.
- **Recapper = pages portion.** Version row starts on row 5; set Row1 "Account:", Row2 "Created:", Row3 "Sales Date:"; add a helper column; copy PZs to column C; duplicate into GC and MF tabs; paste each banner's zones from the Ad Version sheet into column A, remove duplicates, match PZs, delete blank rows and helper column; save as CSV.
- **[Edit details]:** Preview = Monday before go-live; External Run Name = "Weekly Ad"; No theme; **set height to 4096 pixels** (Show/hide rarely-used fields).
- **[Codesheet] Stores:** attach GC or MF Ad Version CSV — **Config: `giant_landover_stores`**, PDF Base Directory `/`, **Toggles 1 & 4** → Save (runs green).
- **[Codesheet] Upload (pages):** attach GC or MF Recapper CSV — **Config: `giant_landover_pages`**, PDF Base Directory from FTP (just before the pages folder), **Toggles 3, 5, 6** → Save. Carlisle runs green; if uploaded first, Martin's Recapper may run yellow ("pages re-uploaded" — mostly "HB/AD" repeat pages, safe to ignore) → **Force processing** for Martin's.
- Flyer Creation → sessions run (~30+ min due to high-res pages). Thumbnails Standard 4 (stretch across page 1 only). Confirm valid dates and that GC pages are in the GC run, MF pages in the MF run.

### ⚠️ Other risk items
- **Items with no price/ABID:** near the end of each flyer there may be a page with 4–5 products (image + name) but no prices/ABIDs — **do not box these.**
- **Recipe pages:** box and tag as a **link** using the URL at the bottom of the page.
- **Liquor mail-in rebate prices:** rebate price (red box) → Current Price with postfix **"Final Cost"**; original price (yellow box) → Original Price; rebate → Sale Story; fine print → Disclaimer.
- **Red arrows:** items with a Sale Tag or Bonus Buy Savings red arrow → put **"Y"** in the **Sales Tag** field.
- **Disclaimer (NEW):** for items with specific valid dates, tag the "Rest of week $$$/lb." text in the **Disclaimer** field. A standard price-update disclaimer applies to **all** items via Style Guide rules (should auto-apply; add manually if missing).
- **Valid dates:** watch for 1-day and 3-day sales — tag item valid dates even if identical to flyer-level dates.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include sign-up page and special weblinks**; exclude coupons, packaged deals, retailer logo, social media.
  - **Sign-up pages:** one box each; Display Type = Link, Name = "Email Sign-up" → Martin's `martinsfoods.com/sign-up`, Giant Carlisle `giantfoodstores.com/sign-up`.
  - **Savory/Recipe items:** Display Type = Link, Name as on page → Martin's `recipecenter.martinsfoods.com`, Giant Carlisle `recipecenter.giantfoodstores.com`.
  - **Peapod banners:** Display Type = Link, Name = "Peapod" → the Peapod OpCo URLs per banner.
  - Regular items: box each individual item with a price (text boxes when needed). Multi-items with no item-specific detail: box as one.
- **Tag / Tag QC (Low; Auto-tag ON for Martin's, OFF for Giant Carlisle; PDF Image Auto Selection OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** Brand box-specific. URLs — see below.
  - **Line Items:** items with no image, or clean-but-dark/grey background, or text-only → tag normally, select a cutout, put **"Y"** in the **Line Item** field.
  - **Ad Block ID:** tag the seven-digit code under each item description in the **Ad Block ID** field where present; leave blank if none.
  - **Description:** do NOT tag the number under the description; do NOT tag "Rest of the Week $$$/lb." in description (goes in Disclaimer).
  - **Sale Story:** do NOT tag "Bonus Buy Savings"; do NOT tag Gas Rewards or cents-off sale stories (dollars-off can be included).
  - **⚠️ Categories:** use ONLY the 15-item list (Baby, Bread & Bakery, Beverages, Adult Beverages, Dairy, Deli & Prepared Food, Floral & Garden, Frozen, Grocery, Laundry/Paper/Cleaning, Meat, Health & Beauty, Pet Store, Produce, Seafood). **ALL alcoholic beverages → "Adult Beverages"** (risk item).
- **Image QC:** single-image box → select only if clean PDF (white bg, not cut off), else "Do not Use PDF Images" + Line Item "Y". Multi-image box → image of first item listed in the tag (fall back to next, or first left-to-right). **⚠️ Avoid grey-background images — use the cutout instead.**

## URL updates (Flex)

- Item Search → URL Is blank → multi-edit and apply the banner grid-view links:
  - **Martin's Foods:** `martinsfoods.com/savings/weekly-ad/grid-view`
  - **Giant Carlisle:** `giantfoodstores.com/savings/weekly-ad/grid-view/`
- Applying to 300–500+ items may time out — refresh and repeat until no results remain.

## Final QC / go-live notes (Flex)

- Ensure all Flex tracker tasks for GC and MF are complete before Thursday go-live.
- **Coupon page (C07):** all items tagged as **items, not coupons**; ensure item-level valid dates. Item Search → Item Type = Coupon → confirm none are mistagged.
- Search flyer for valid dates and apply where needed. Confirm all items have a URL (apply grid-view links if missing). Verify Ad Block IDs (missing ones truly have none).
- **Disclaimer:** Item Search → Disclaimer text is blank → should return **no results.**
- **Adult Beverages check:** find alcohol pages via Storefront spotcheck → note page grouping index → Item Search "Categories IS NOT Adult Beverages" on that page index → fix any alcohol items.

## Insert process (DOC, Wednesday)

- Inserts drop in AEM with an insert placement spreadsheet; retailer emails when dropped.
- **⚠️ RISK 1:** watch for pricing-zone-specific inserts (rare — seen Feb 2025).
- **⚠️ RISK 2:** confirm each insert PDF is a **single page** (multi-page PDFs break FAdmin).
- GC and MF share a pagination xlsx; inserts go in the same page position for both banners. In the "Insert" column, rename each to a **single word with no spaces** (used by BD reporting — crucial).
- Create an Optics ticket, attach the insert spreadsheet. **⚠️** Any post-go-live insert/URL changes: note in the ticket comments and attach the updated spreadsheet.
- After adding inserts, check vertical scroll for 3 PZs each (clickability + page positioning).

- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Giant Carlisle & Martin's Foods OneGuide (Google Doc `1w3auLK-JsRcPzRJgoAwPbIPdJ2-bFu6wGt3h5X3Yflw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Giant Eagle — Processing Guide

> **Source:** Giant Eagle OneGuide (Google Doc `1QOhdRCo_9j_5QVSZPmnrBUgpg_6pGU76xZlaSsOUK-U`), updated Jul 23, 2024. Contacts/credentials omitted.

Two flyer types: the **Weekly Ad (233)** and the **ACE Insert (12167)**. Covers both Giant Eagle and Market District banners. Heavy on **Offer ID** and linking-document work.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Weekly Ad: all platforms · ACE Insert: **Hosted only** |
| Slack channels | `#gianteagle` |
| Flyer types | Weekly Ad (233) · ACE Insert (12167, ad-hoc) |
| Processing | Auto-stack; Flex (FAB Tickets / Processing Support); **Feedel processing (yes)** |

## Files & schedule

- **Weekly Ad:** files Friday; Available Wednesday, Valid Friday → Tuesday, Available To Monday; **Preview Monday (sent by 12pm)**. Yes to linking doc + circular header.
- **ACE Insert:** ad-hoc, no linking doc.
- **Setup owned by** DOC; Image QC by Flex; FQC by DOC (ACE Insert FQC by Flex).
- **Custom Action:** "Assign FSA from CSV" — used for one PZ region (D3) where FSA isn't generated (at Pre-FQC).

## Upload & setup (Weekly Ad)

- Confirm receipt of the **Circular Header** and **Giant Eagle Links** xlsx from the file-drop email.
- Open the **Flipp** version of the recap ("...GE_Recap_**FLIPP**.xlsx"). Copy pages from the RNS tab (version ID down to last page/PZ — typically A6→R64) into the **generic codesheet template**.
- Use `=concat([page], ".pdf")` to append `.pdf` to all page names, paste-as-values over the originals, delete the formula row, download as CSV.
- **⚠️** For pricing zone **D2**, confirm stores read **"682, 1667"** not **"1682, 1667"**.
- **[Code Sheets]:** Name "weekly", upload CSV, **Config: `generic`**, PDF Base Directory from SFTP, **Toggles 1, 3, 4, 5, 6** → Save → Process.
- **[Edit Details]:** available everywhere, no theme, Key Messages (e.g. "Weekly Deals"/"Weekly Savings").
- Manually upload the **last page** ("NEWFINALPAGE_…") into the last position (every week).
- **Thumbnails:** ⚠️ must span **ONLY the first two pages** — for one page do NOT include skinny pages; for two pages include the skinny page.
- Add video links to the **Giant Eagle Links xlsx** (search SFTP for `mp4`, upload via **[Upload File]**; **delete the "+" character** between words or FAdmin won't read the file). Attach the Links xlsx to the **[Vendors]** tab for all tasks.
- **Circular Header (linking doc, drops Monday 11am):** delete extra columns, shift to order **PageName · Price Zone · OfferId · Title · Description**, remove duplicates (by Page Name), download as xlsx, attach to **[Vendors]** tab for all tasks.
- Upload Wrap Pages (if applicable that week — ask retailer where to insert; NOT part of "I"/"Indy" zone) and the Final Page (last position).

### ⚠️ Risk items
- **Every boxed/tagged item AND link MUST have an image** (clean PDF for items and links where available).
- **Offer IDs differ per pricing zone** — Version Q of page 1 has completely different Offer IDs (not applied). Be mindful.
- Do **not** box social media icons. **Include vanity URLs.** Box "Click Here" buttons as **Video** display type.
- Attach the Offer ID document (dropped Wed 11am) to the Vendor tab — the Offer IDs custom field must be tagged/QC'd weekly.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot ON):** include coupons, packaged deals, sign-up page, special weblinks; exclude retailer logo, social media. (No tagging doc for ACE Insert 12167.)
  - Packaged deals boxed as one; box/tag each priced sub-item even with no image; box callouts with a **vanity URL**; Home Health Care ad blocks → `dme.gianteagle.com`; all "CLICK HERE" buttons → Display Type **Video** (use the Links xlsx to locate). Box all promotional callouts listed in the Giant Eagle Links xlsx by matching page name.
- **Tag / Tag QC (Low; linking doc required; Auto-tag OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**, Image QC. **Exclude SKU. Do NOT tag brand.** Offer ID is a custom field.
  - **Name:** tag exactly as on page incl. apostrophes/accents (e.g. "Ben & Jerry's", "Häagen Dazs", "Nestlé"). Multiple items: 2 items separated by "or", 3+ by commas with last "or".
  - **Sale Story:** use **"Giant Eagle Advantage Card"** for both Market District and Giant Eagle; write "Save with your Giant Eagle Advantage Card"; include $ amounts and math equations (e.g. "$2.50 - $1 eOffers"); use the "¢" symbol when on the page.
  - **Pre/Postfix:** prefix = text before the dollar figure; postfix = offer text when no price (e.g. "BUY ONE GET ONE", "WHEN YOU BUY 3").
  - **Categories:** ONE per item, matching the page banner (Bakery; Beer, Wine and Spirits; Beverages; Dairy; Deli; Floral; Frozen; Household Needs; Grocery Aisles; Personal Care & Beauty; Meat & Poultry; Prepared Foods; Produce; Seafood; Miscellaneous; Seasonal).
  - **⚠️ Offer ID (risk item):** search item name in the Circular Header (TITLE column), identify by PRINTZONE (from page name). Put the PRINTZONE-specific Offer ID in **Offer ID**, and **ALL** Offer IDs for that item name in **All Offer IDs Listed** (even a single ID must appear in both fields).
  - **Disclaimer:** exact as on page; include "Giant Eagle Advantage Card" / "Market District Advantage Card" when the Advantage Card icon appears.
  - **Image QC:** select the first item listed in the name; **PDF > Cutout**; clean images, **no black background**; line items may use cutouts.

## Final QC / post-processing

- File a **FAB/ARB ticket** for Pre-FQC tasks so Flex completes Image QC, Coupon ID QC, and Spotchecks (attach the Circular Header from Vendor Tasks).
- **Item Category QC (DOC):** ⚠️ GE uses prepared-meal pics for raw meat — raw ground pork should be **Meat**, not Meals. Search Deli/Meat/Dairy/Bakery/Produce/Frozen/Prepared Food/Grocery Aisle categories.
- **Offer ID QC (DOC):** Offer IDs feed GE's website "Eligible Items". Item Search → Offer ID Is blank (Item Type = Item) → manually add from Circular Header. Then confirm both custom fields filled (All Offer IDs Listed Is blank + Offer ID Is NOT blank). Email a report of remaining missing Offer IDs to the retailer (Monday). For many results, build/import an item sheet (`item_id | sku | name | description | id_1 | id_2`).
- Add the flyer's **final page** (boxed & tagged from prior run or the app-download link); add to last position of all PZs.
- Run custom action **"Assign FSAs from CSV"** for the 1–3 PZs missing FSAs (D3's FSA 16673 is pre-listed); rerun page tile generation.
- **FQC:** oldest first, ACE Hardware Insert last. Baseline page-swap process available.
- **ACE Insert FQC (Flex):** hidden in all apps; no image QC; Standard 4 thumbnails; no categories on page 1, one per page.
- **Flyer Review type: Lite.**

## Out-of-processing

- Black Friday comms docs referenced in the OneGuide.

---
*Source: Giant Eagle OneGuide (Google Doc `1QOhdRCo_9j_5QVSZPmnrBUgpg_6pGU76xZlaSsOUK-U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Giant Tiger — Processing Guide

> **Source:** Giant Tiger OneGuide (Google Doc `1_X0Lg4V0mBJfkosLVvbpr51v8GNVNWl2lHSIHvlQAEQ`). Contacts/credentials omitted.

Tier 1 Premium bilingual (EN/FR) retailer. Codesheet + store-set upload, a Shopify URL-pull step, a logo-appending custom action, and Tuesday link revisions.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#gianttiger` |
| Hosted URL | gianttiger.com |
| Flyer types | Weekly (1 type) |
| Processing | Auto-stack; no Flex; no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday. Upload by Tuesday (Wednesday latest).
- **Cadence:** Available Tuesday, Valid Wednesday → Tuesday. **Preview: Friday before** (set preview to Friday even though preview is not until Monday).
- **Setup owned by** FLEX; Image QC by Flex; FQC by DOC/FLEX.
- **Custom Action:** Giant Tiger Logo Appending (appends logo1/logo2 to page-1 items of the grocery and core pages; runs any point in FQC).

## Upload & setup

- Retailer emails when files land on FTP. Search FTP for `xlsx` → download **codesheet, run list, and SKU file**.
- **Store Set Upload:** in the Run List, rename Column A (Store_Dealer → Merchant Store Code) and Column B (Format → Store_Set_Name); save as CSV. On the Store Sets page → **Clear All Store Sets** → upload the Runlist CSV. **⚠️ Click Upload ONCE** — clicking twice uploads the store sets twice.
- **Codesheet manipulations:** unhide/delete column A; delete everything below the codesheet info (from Code Legend down); in the pink **Language** row, change language-location to just language:
  - French-Quebec → French · Bilingual-Quebec → English · Bilingual-Ontario → French · Bilingual-Atlantic → French · English-Ontario/Atlantic/West → English · Bilingual-West → French
  - Unusual zones: use the VIP_Email page (`VIP_Email_EN` → English, `VIP_Email_FR` → French).
  - Delete superfluous tabs. **Delete the VIP_Email row** (upload the EN/FR VIP pages manually after the codesheet runs). Save as CSV.
- **Banner Links file:** from the ORIGINAL codesheet, delete everything above the Digital Insert URLs section, save as `Week_BannerLinks.xlsx`.
- **Weekly URL document:** copy the SKU file's Grocery tab into the SGHG tab; use the **GiantTigerShopify Pull Product URLs** google sheet (clear WEEK MAPPING, paste SKU data, run "Populate URLs"), download WEEK MAPPING as CSV → `Week_URLs.csv`.
- **Upload with codesheet:** Codesheet tab → upload codesheet.csv → paste FTP path into **PDF Base Directory** (**do not include the last slash or anything after it**) → Save → Process.
- **Add VIP pages manually** after the codesheet runs (French toggle for the FR page); add to all pricing zones per language via Pages → Layout → "Put In". Mark Flyer Creation complete.

### ⚠️ Common errors / risk items
- **Price check items over $100** — scan the flyer and verify prices.
- **Flyer sorting:** weekly ad always first, then lookbooks.
- **Codesheet upload errors:**
  - **"cannot find file":** name/format/spacing in the codesheet must exactly match the FTP (watch for stray spaces).
  - **"pages previously uploaded":** check the naming convention reflects the correct week; clarify files with the retailer. (Also expected/ignorable at overview.)
  - **"NIL":** re-check all codesheet revisions and cell placement.
- Pre-setup: clear FTP; mass-attach Banner Links + URL (WEEK MAPPING) docs to all vendor tasks; no external run name; add theme if applicable.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box OFF, Box QC bot ON):** include sign-up page, social media, special weblinks; exclude coupons, packaged deals, retailer logo.
  - Sign-up page: box **top and bottom in two separate boxes** (per Banner Links doc, consistent WoW). Special weblinks: box ad-match and claw-back areas (per Banner Links doc).
  - **⚠️ Do NOT box individual SKUs as standalone items** — they should be a **text box linked to the product's photo, or not boxed at all.**
- **Tag / Tag QC (Low; linking doc required; Auto-tag OFF):** include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand box-specific.
  - **Brand** in the new Brand field. **Description:** put all SKUs here if multiple; do NOT enter package info; enter the description next to the item.
  - **SKUs & URLs:** reference the attached URL document — use the correct-language URL.
  - **Price:** as on flyer; **if a range, use the higher price.** Shoes get postfix "pair".
  - **Banner Links doc:** use the English-column URL for English pages and French-column URL for French pages.
- **Image QC:** clean PDF images, cutouts OK if none available.

## Final QC / post-processing

- **Item Category QC (Flex):** QC Categories → search "clothing" → verify women's/men's/kids classification (open the page for context).
- **Banner Links QC (Vendor):** cross-reference each Banner Links page's links against the doc; correct any wrong ones.
- **Links/SKU QC (Vendor):** Item Search — SKU blank (Item type Item), URL blank (search EN then FR), and URL contains `/p/` → mass-edit to the correct base URL:
  - **EN:** `gianttiger.com` · **FR:** `gianttiger.com/fr/`
- **Ad-hoc QC (Vendor):** QC prices over $100; Sessions → "Mark items in-store only"; **⚠️ NEW — remove stores 431, 436, 446** (custom action "Remove Stores", all zones); run the **Logo Appending** custom action; set Tracking Codes (`FW##_W##` — note GT's fiscal year differs from ours).
- **Final QC (Flex):** geography should not change; "pages previously uploaded" always shows (ignore); Standard 4 thumbnails (start at logo); dates match PDF; flyer sorting weekly-ad first, lookbook after.
- **Flyer Review type: Lite.**

## Out-of-processing

- **Tuesday link revisions:** the retailer emails link revisions for the Wednesday-valid flyer. Although technically live, TTMs are hidden during the preview day — complete revisions by EOD Tuesday. Swap boxes in Box QC for items needing link swaps; update any new links per email; note completion in run comments.

---
*Source: Giant Tiger OneGuide (Google Doc `1_X0Lg4V0mBJfkosLVvbpr51v8GNVNWl2lHSIHvlQAEQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Global Pet Foods (Not NL/PE) — Processing Guide

> **Source:** Global Pet Foods OneGuide (Google Doc `1PtBZkKGDU24FtEOylJUs3kTM4rImdHJ8G7DPxrYGAFM`). Contacts/credentials omitted.

**⚠️ This guide is for Global Pet Foods — NOT Global Pet Foods [NL/PE]. Confirm you're following the correct guide.** Truly ad-hoc, infrequent publications (Flyer 3465).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Hosted URL | N/A |
| Flyer types | Flyer / Ad-Hoc (3465) |
| Processing | Auto-stack; Flex completes some tasks; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad-hoc — retailer may email files via WeTransfer; DOC drops them in the FTP (new folder with all PDF pages). DOC may also need to build the flyer run per request.
- **Cadence:** Available/Valid **Monday → Monday**, but no consumer preview; **same effective & valid dates**, length of ad varies (set per the retailer email).
- **Workflow:** Upload & Setup (Vendor), Image QC (Flex), FQC (DOC). Flyer Review owned by DOL.

## Upload & setup

- FTP login name: **globalpetfoods** (credentials in the OneGuide — not stored here).
- **Manual Upload:** Pages → Edit → select from SFTP folder → Auto-Group → Save & Confirm.
- **Flyer Creation:** 1 pricing zone, all pages, save & confirm; add all stores.
- Setup QC (Flex): Edit Details dates per retailer email, no preview date, available everywhere, no external run name, apply applicable theme (Holiday/Black Friday). Thumbnails Standard 4 (1065x600 2pg, Stock premium 1pg, Storefront carousel premium 2pg / organic 1pg). **Leg heights 30/25.** Confirm sessions run.

### ⚠️ Common errors / risk items
- **PDF page sizes:** because they publish rarely, the retailer forgets our requirements. **Check PDFs before uploading — watch for extreme page-size (length) variations** that break FAdmin or hurt the front-end experience; ask the team to re-submit files of roughly equal dimensions.
- **Store list:** since content is irregular, confirm the store list is up to date (may not be comparable to past runs).
- **Links:** the retailer has previously asked that **all items be linked to one specific URL** — if so, add a note to ALL vendor tasks.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** include coupons and packaged deals; exclude retailer logo, sign-up page, social media, special weblinks. Box any item with a price.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** Brand box-specific.
  - **URLs — OPTIONAL:** only include a URL if one is provided in a linking document or task note. If none, proceed without a URL.
  - **Name/Description:** don't put size/weight/type in Name — put those (and price variations for different sizes) in Description.
  - **⚠️ Risk:** watch for "Save Up To __ %/$" — do NOT enter an amount in the $/% off field, enter it only as a sale story.
- **Image QC:** select clean PDF if available, otherwise cutout.

## Final QC / go-live notes (DOC)

- Complete Ops spotchecks (if any); mark Auto-Stack complete.
- Re-confirm Edit Details (dates per email, no preview, available everywhere, no external run name, theme if applicable); thumbnails; leg heights 30/25.
- Link QC (if applicable); Image QC; verify URLs; confirm Tag & Tag QC match; confirm all items boxed/tagged.
- **⚠️ Check full-screen & vertical preview** — last chance to catch large page-dimension discrepancies.
- Confirm sessions run; confirm the most up-to-date store list in the GEO tab.
- **Flyer Review type: Lite** (owned by DOL; flyer review guide exists).

---
*Source: Global Pet Foods OneGuide (Google Doc `1PtBZkKGDU24FtEOylJUs3kTM4rImdHJ8G7DPxrYGAFM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Globo Shoes — Processing Guide

> **Source:** Globo Shoes OneGuide (Google Doc `13HmwPE88iYelRX3nkU02FlOxSg1s-8kmM26BOXUvW04`), updated Oct 23, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#globo` |
| Hosted URL | globoshoes.com |
| Flyer type(s) & cadence | Ad Hoc (flyer 1307) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Linking document:** Yes — `.xlsx` from the FTP (name varies, e.g. `GLOBO_BTS_LINKS.xls`, `FLIPP BUILDING_JULY.xlsx`). Used for both box draw/box QC and tag/QC.

## Upload & setup (owned by Flex)

- Confirm dates from the contact or the account's BD.
- **Manual upload.** Two separate files for **English** and **French**, labeled accordingly. Take the lower-case (split) files; mark the full PDF as uploaded. Set French pages to French language, Save → Autogroup → Save and Complete.
- **Pricing zones:** two zones — **EN** and **FR** — with language set accordingly. Open Store Sets and add all stores to both zones. (The store warning on the overview page at later stages can be ignored.)
- Download the linking `.xlsx` from FTP and **mass-attach to Vendor Tasks for OS**.

### Setup QC
- Set **External run name** based on callouts on the first pages (EN and FR).
- **Hide on hosted** — this ensures live checks are done on the app instead.

## ⚠️ Common errors / risk items
- **Globo Shoes logo must ALWAYS be tagged** — links to globoshoes.com.
- **Language of links** — make sure English and French links are correct.
- **Colour variations boxed separately** — each colour has its own SKU and URL in the linking document; items may have overlapping text boxes.
- **404 links: LEAVE THE LINK IN THE URL FIELD** — do not remove it. Items are often unavailable, so links may not be live; the retailer is aware.
- **Flagged-word spotchecks:** because of item arrangement and letter labels (A-Name, B-Name), expect many flagged words. Instead of Approve, click **Add as Proper Name** and add a note referencing Tag/Tag QC instructions.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, special weblinks. **Exclude:** coupons, packaged deals, sign-up page, social media.
- Globo uses data piping and image extraction; boxes can overlap a little.
- Box items individually by **colour AND style**. When a product has only ONE colour/SKU, box the shoes together (not separately).
- Use text boxes when needed; link item box to text box via letter labels (A, B, C…). Styles boxed separately may share a text box.
- Be as specific as possible when assigning page categories.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude:** disclaimer.
- **Name:** as on flyer; brand/Globo name identifier entered separately (name identifier in CAPS, e.g. "Solemate Women RATHIEL"). Do not include brand in Name field or letter labels (A-/B-) in the name.
- **Description:** include shoe sizes, demographic (mens/womens/kids), and additional colours.
- **Price:** current price in bold (on item or as a Hero price at top of a section); original price in unbold.
- **SKU field:** enter the item name + colour code combo as on the URL doc (e.g. `FITZSIMON-98`).
- **URLs:** use the URL spreadsheet. Logos link to globoshoes.com (Name: Globo Shoes). Use SKU/item name and **placement number** to match colour variants to correct links (compare images by opening the URL). Match link language.
- **Categories — use ONLY these analytics categories:** Women's Footwear, Men's Footwear, Men's Athletic, Women's Athletic, Kids Footwear, Boys Shoes, Girls Shoes, Bags/Handbags & Wallets.

### Image QC
- Mostly cutout images. PDF images tend to have a black background and are usually not clean enough to use.

## Post-processing / FQC
- Mark Autostack Spotcheck complete.
- **Legibility heights:** Scan 55, Read 45. QC thumbnails: Standard 4.
- Open "Items without a URL" and cross-check the linking document.
- Mark items In-Store Only.
- Pricing zone item view: check dates (may not be present — retailer comms are source of truth), all items boxed, correct languages per zone (EN/FR), pages sequential, page categories accurate.
- Geography should read "No new stores/fsas added or removed" unless noted.
- Ignore the "Some categories do not have thumbnails" error.
- **Flyer Review type: Lite.**

---
*Source: Globo Shoes OneGuide (Google Doc `13HmwPE88iYelRX3nkU02FlOxSg1s-8kmM26BOXUvW04`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Go Sport — Processing Guide

> **Source:** Go Sport OneGuide (Google Doc `1qwudpPPRMjTzt6dEV3JWhDFeZxzlMmrD_7PJpe56N4c`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#chaussures-pop-go-sport`, `#flex-processingsupport` (FQC only), `#flexflyerreview` |
| Hosted URL | (per OneGuide) |
| Flyer type(s) & cadence | Go Sport — Flyer 10910; Ad Hoc |
| Processing | Auto-stack |
| Who's involved | Flex (3FL); no OS; no coupons; no Strategic Ops / Feedel |

> Note: this is a shared banner with Chaussures Pop (6456/10909); Go Sport is 6457/10910.

## Files & schedule

- **Files received / cadence:** Ad hoc (available/valid dates all ad hoc).
- **Linking document:** Yes, for URLs.
- Pages may need to be added to the SFTP by the processor if the client sends files over email.

## Upload & setup (owned by Flex)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Once listed at the bottom, Auto-Group (or manually enter grouping numbers). **Ensure all pages are set to French only.** Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all stores.
- **Linking document:** ensure the corresponding linking doc from the FTP is attached to all vendor tasks. If none, flag to the Coordinator.

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone → Items View). **RISK:** if uploading from SFTP, confirm no un-uploaded pages remain in the SFTP.
- Confirm flyer dates (usually first or last page).
- Thumbnails: 4 Standard. Legibility heights: 60/40.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a single box.
- Copy the item **name from the URL document** attached in vendor tasks. If no URL doc is attached, flag to the Processor or Lead.
- **Multiple colour options:** ensure the correct link is applied per colour/style. Open the link to double-check the colour/style matches.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude all:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each item individually; use text boxes if necessary. **Multiple colours, one price:** box each image separately.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name (copy from URL doc), pre/postfix, SKU, price, categories, URLs. Include if available: valid dates, description, sale story, disclaimer, original price.

### Image QC
- PDF preferred if clean; otherwise cutouts are accepted.

## Post-processing / FQC (owned by Flex)
- **Pre-FQC:** check URLs — almost all items should have one. If an item has no URL, double-check the link sheet; some items just aren't listed, which is fine. Confirm dates (per PDF) and availability toggles. Thumbnails correct and include retailer logo.
- Standard FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Go Sport OneGuide (Google Doc `1qwudpPPRMjTzt6dEV3JWhDFeZxzlMmrD_7PJpe56N4c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Goemans Appliances — Processing Guide

> **Source:** Goemans Appliances OneGuide (Google Doc `1Ty6_O9jSEe4WXRhjA1vBZQyiz-HFZbWH_YEwx1_rJ6M`), updated May 16, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#goemansappliances` |
| Hosted URL | goemans.com |
| Flyer type(s) & cadence | Flyer Type 1 — Monthly |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

> Note: shared account with Tasco Appliances — Goemans has 7 stores, Tasco has 6.

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Preview date:** No. **Linking document:** No.

## Upload & setup

1. Create flyer run — internal name = the month it goes live.
2. **Manually upload pages** (usually ~8 clearly-marked pages). Do NOT upload the full multi-page PDF — upload the individual pages only.
3. Create **one pricing zone** named **Base**, language English.
4. Add all 7 Goemans stores (and all 6 Tasco stores on that account).
5. Add the linking doc to the pipeline — confirm they provide one; sometimes it comes by email instead of the FTP.
6. Include a pipe note pointing to the Confluence vendor guide (box drawing section).

## ⚠️ Common errors / risk items
- **Look for multiple products** in a box.
- Don't accidentally upload the combined PDF instead of individual pages.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals (washers/dryers), retailer logo, sign-up page. **Exclude:** coupons, social media, special weblinks. Linking doc required (box-specific).
- Box each item separately. **Sign-up page** gets boxed as one item.
- **Categories/promotions:** box the categories at the top of page 1 (they link out to the website); box promotions separately.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates.
- Image QC during tag: prioritize PDF images unless not clean (shadows / black backgrounds).

## Post-processing / FQC
- **Thumbnails (Standard 4):** 1065×600 (remove white border, cover pg 1&2); stock premium (all base/flyers, cover pg 1); storefront carousel premium (cover pg 1&2); storefront carousel organic (cover pg 1).
- Edit Details: confirm Available & Valid dates match the PDF.
- Check all items QC'd; one pricing zone (Base) with all stores; check vertical & horizontal previews.
- Geography: no change WOW unless specified.

## Flyer review
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swaps / post-live checks as needed.

---
*Source: Goemans Appliances OneGuide (Google Doc `1Ty6_O9jSEe4WXRhjA1vBZQyiz-HFZbWH_YEwx1_rJ6M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Good Neighbour Pharmacy — Processing Guide

> **Source:** Good Neighbour Pharmacy OneGuide (Google Doc `1gHiQJYnSkz2m4zJ-XzZNRCBAhqFzCtW4WdBnMXDw84A`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | Hosted only |
| Slack channels | `#goodneighbourpharmacy` |
| Publication schedule | Monthly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing; OS completes Upload + FQC |

- **Cadence:** Available Tuesday, Valid Tuesday.

## Files & schedule

Each month they submit files for **two uploads**: a **manual upload (Flyer Type 1)** and a **codesheet upload (Flyer Type 2)**.

## Upload & setup

### Flyer Type 1 — Manual upload
1. Document name is `gn minicirc`; there should always be **5 zones with the same number of pages per zone**. If there are fewer zones or missing pages, **email the retailer**.
2. Upload the pages.
3. Build the pricing zone: description name = zone #, add the pages, Save and Next.

### Flyer Type 2 — Codesheet upload
1. Download the codesheet from the FTP and manipulate:
   - Sort `GN_TPR_Zone` lowest → highest.
   - Create 2 new columns for Pg 2 & Pg 3.
   - Add `.pdf` to the `GN_Flipp P2 File Name` and `GN_FLIPP P3 Filename` columns after the pages (Find & Replace `P3` → `P3.pdf`); remove the formulas for pg 2 and 3.
2. Save as CSV and upload into the flyer run:
   - **Config name:** `good_neighbor_pharmacy`
   - **Toggles:** all toggles **except region assignment**
   - **Base path** from directory — do NOT include `/FLIPP P1`, only everything before the `/`.

### Setup QC (both flyer types)
1. Upload the **GNP Categories** document to the vendor task (same one all year).
2. Set details: External run name (e.g. "April Circular"), **no theme**, no preview date, **available everywhere (Hosted, Flipp & Distribution)**.
3. Complete Setup QC checklist.

## ⚠️ Common errors / risk items
- **`gn minicirc` must have 5 zones with equal page counts** — if not, email the retailer before proceeding.
- **FSA Dedupe custom action (out-of-process / pre-FQC):** when both runs are READY but NOT yet FQC'd, run the **FSA Dedupe** custom action. Priority: the **codesheet should have more FSAs** (top priority). Flyer Run 1 ID = codesheet; Flyer Run 2 ID = manual. Only complete the FQC checklist after FSA Dedupe is done.
- Include a google category AND an analytical category on each item.

## QC specifics

### Box Draw (Low complexity)
- **Include:** social media, special weblinks, retailer logo, packaged deals. **Exclude:** coupons, sign-up page.
- Linking document required for tagging and item QC.

### Tag / Tag QC (Low complexity)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.
- Tag all fields "as seen on page."

### Image QC
- Select a PDF with a white background where possible; otherwise select the cutout.

## Pre-Final QC
- Legibility heights: 45 × 35. Standard 4 thumbnails.
- Pages → categories: no more than 3 categories per page.
- Recheck details (external run name, no theme, no preview date, available everywhere).
- QC social media boxes/links; ensure bottom social media boxes are tagged.
- Check all pricing zones have a store.
- Run **FSA Dedupe** (see risk items) before completing the FQC checklist.

---
*Source: Good Neighbour Pharmacy OneGuide (Google Doc `1gHiQJYnSkz2m4zJ-XzZNRCBAhqFzCtW4WdBnMXDw84A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Goodness Me — Processing Guide

> **Source:** Goodness Me! OneGuide (Google Doc `11RM_JRMJFQ2xxXXk6oajyOgjCdYI8lSxBfMNTTUD8Es`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#goodnessme`, `#flex-processingsupport` |
| Hosted URL | goodnessme.ca |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review, Image QC); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Friday (retailer emails the flyer PDF attached).
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Tuesday, Valid To Tuesday.
- No linking document.

## Upload & setup (owned by DOC)

- Save the flyer PDF from the email and **split into pages**; add pages to the SFTP.
- **Manual upload:** select all pages from the folder matching the flyer run date, index correctly, all English, Save and Complete.
- Create **1 pricing zone: Base**, all stores.
- Thumbnails: Standard 4.
- **Edit Details:** Available/Valid From Wednesday, Available/Valid To Tuesday; internal run name already set; **Available Everywhere**; no external run name; no theme.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a box.
- **Pages 1 and 2 must be uploaded and fully processed before FQC.**
- If pages haven't been sent by **Tuesday**, bump the retailer and warn that the live date may need to be pushed.
- Disclaimers: check the **bottom of pages for page-level disclaimers** (e.g. tag all items on a page with "WHILE SUPPLIES LAST" if it applies at page level).

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include everything:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Draw clean boxes. Box retailer logo (first page), curbside pickup / other banners, online webinars & education sessions, each individual social media button separately, and special weblinks (ad match, shop online, social media buttons, store locator — typically on/near the last page).

### Tag / Tag QC (Low complexity — Auto-tag ON; PDF Image Auto Selection ON)
- **Include:** brand (with ® / ™ if shown), name (with brand), pre/postfix, valid dates, description, SKU, price, sale story (e.g. "EVERYDAY LOW PRICE", "SAVE $", "SAVE %"), categories, disclaimer, original price, URLs.
- **URLs — use goodnessme.ca.** Tag these categories/pages: Supplements, Grocery page, What's New page, Red Hot Deals page. Exclude: fruits, vegetables, meat, seafood. Specific links: Facebook, Instagram, Pinterest, Shop In Store/Shop Online → `goodnessme.ca`, Curbside Pickup → `/pages/pickup-location`, Home Delivery → `/pages/home-delivery-store`, Education/Classes/Webinars → `education.goodnessme.ca`, Ad Match → `/pages/price-match`, Store Locator → `/tools/store-locator`.

### Image QC
- Select the best possible PDF image. **Do not use a PDF image with a black background.**

## Post-processing / FQC (owned by DOC)
- Spot checks; Item Image QC (PDF priority, no black backgrounds/shadows).
- Thumbnail QC: Standard 4.
- Page category QC (use page headers); mark items In-Store Only.
- Edit Details: Available & Valid the same; dates run Thursday→Wednesday (or match the front page).
- FQC checklist: it's OK to mark "ENSURE Mark Items In Store Only is not checked" as yes (ignore it).

## Flyer review
- **Flyer Review type: Lite.**

---
*Source: Goodness Me! OneGuide (Google Doc `11RM_JRMJFQ2xxXXk6oajyOgjCdYI8lSxBfMNTTUD8Es`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Gordon Food Services — Processing Guide

> **Source:** Gordon Food Service OneGuide (Google Doc `1zZZzbkt_Z2Faf2y-xGEfrk2ePYNALUH-IQOaH-huucM`), updated May 1, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#gordon-food-service-stores`, `#gordon-food-service-stores-nativex` |
| Hosted URL | None |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Wednesday (retailer email contains the Link Sheet, distribution/store list for the week, and confirms dates). DOC forwards the email to PSS for processing.
- **Cadence:** Available From Sunday, Valid From Sunday; Available To Saturday, Valid To Saturday (1-week run).
- **Linking document:** Yes (link sheet + store assignment received by email).

## Upload & setup

- **Manual upload (OS):** Pages → Edit → select page(s) from FTP → Autogroup → Save & Complete.
- Create **pricing zones based on the retailer email & file names** (e.g. GO, NMI, BC, FL). **Select the LOWERCASE folder dropdown** so individual pages display and select all individual pages — do NOT select the uppercase files (those are entire PDFs). Autogroup, then assign pages to their pricing zones.
- **Generic store assignment** (store assignment varies week over week):
  1. Open the GFS_Generic Store Assignment spreadsheet; insert this week's store list.
  2. Duplicate the template tab, rename for this week.
  3. Each store has an "X" beside its version; sort right-to-left A-Z to group Xs per zone.
  4. Copy store numbers into the "stores" column; write the pricing zone name (page version) beside each. **⚠️ The pricing zone name must match Fadmin exactly — case sensitive, remove any spaces.**
  5. Download as `.csv`.
  6. Upload codesheet — **Name:** stores; **File:** the new CSV; **PDF Base Directory:** `/` (no spaces); **Toggles:** only Store Assignment. Save → Process.

### Setup QC
- **Attach link sheet** as a mass attachment to Box QC, Tag & Tag QC.
- Edit Details: dates per retailer email; **Hidden on Hosted**; no preview date; internal run name W01/W02/W03; no external run name; no theme.
- Thumbnails: Standard 4 (1065×600 2pg, stock premium 1pg, storefront carousel premium 2pg, organic 1pg).
- Reassign vendors as Urgent. **Mark Setup QC complete or vendor tasks will NOT be available.**
- Confirm all sessions ran & FSAs generated.
- **Submit 2 Urgent Processing Tickets** (reason: short lead time) — one for Box QC, one for Tag/Tag QC/Spot Check/Image QC.
- Flag any date changes to DOC/Lead, who notifies both GFS Slack channels.

## ⚠️ Common errors / risk items
- **Uppercase vs lowercase folders:** always select the lowercase folder (individual pages); uppercase are full PDFs.
- **Pricing zone names are case-sensitive and space-sensitive** — must match Fadmin exactly or store assignment fails.
- **FSA generation** may take a few minutes; if FSAs don't generate, re-run the "Flyer Creation" task → Mark Complete.
- **URL name mismatch:** product names on the link sheet are not exact matches — **use the closest product name** (e.g. flyer "Liquid Vanilla Bean Paste" → URL "Vanilla Bean").

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include:** special weblinks (links in the spreadsheet, e.g. Shop Online). **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media. Linking doc required.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Brand:** use the product image to identify if not in the name (e.g. "Oishii"). For multi-item/brand boxes, select "Multi-Item" and separate brands with a `|` (pipe).
- Prefix: watch for multi-buy (e.g. `2/$5`). Postfix examples: LB., EA., BAG. Categories usually Grocery.
- **Every item will have a URL** (link sheet attached to all vendor tasks). Use the closest product name.
- **Images:** always choose the cleanest/most relevant; if two+ items in a box, select one image; if no clean image, select "do not use PDF image."

### Image QC (post-processing)
- Overview → Item Image QC → Generate All (usually <100 items). Always select PDF if available; lifestyle image OK; if multiple images, select 1.

## Post-processing / FQC
- **Link QC:** Overview → Items without URLs → add any missing links. Confirm CTA links (Item Display Type → Link → Add Link; Sessions → Verify URLs; Flyer Preview → confirm functioning).
- FQC: confirm vendor tasks complete; Edit Details (dates, hidden on hosted, internal run name, no external run name, no theme); thumbnails Standard 4; Tag/Tag QC both green; page categories none/only 1 page (clear any entered); sessions run & FSAs generated, re-verify URLs.
- Geography: some week-over-week variation is normal; confirm against the store assignment sheet if big variations. OK to ignore "Other Warnings"/stores not assigned.
- **Flyer Review type: Lite.**

---
*Source: Gordon Food Service OneGuide (Google Doc `1zZZzbkt_Z2Faf2y-xGEfrk2ePYNALUH-IQOaH-huucM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Gosselin Photo — Processing Guide

> **Source:** Gosselin Photo OneGuide (Google Doc `13NvGfP04hY5Ws5ygTTRQ4FhbtHxtS2XFOZPlLvzSUBM`), updated May 5, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#gosselin` |
| Hosted URL | gosselinphoto.ca/en/about-us/flyer |
| Flyer type(s) & cadence | Flyer #8290; Ad-Hoc |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (FQC); no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Ad-Hoc. The contact sends EN + FR flyer PDFs plus a link to the linking document.
- **Cadence:** Available From Friday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **Linking document:** Yes (separate EN and FR linking docs, `.xlsx`).

## Upload & setup

- **Setup (owned by DOC):** download all 3 assets (EN flyer, FR flyer, `.xlsx` linking doc) and upload directly to the SFTP. *(SFTP host/user/password are in the OneGuide — not stored here.)* While files transfer, create/update the flyer run shell.
- **Edit Details:** available everywhere; dates provided via email and printed on the flyer; no theme (unless a seasonal theming brief applies).
- **Upload (owned by Vendor):** once files are in the SFTP, manually upload all EN and FR pages → Auto-Group for pagination → change language to French for all FR pages.
- **Pricing zones:** two zones — **EN** (all English pages) and **FR** (all French pages). Add all stores to both.
- **Attach the linking document to all Vendor tasks** in the Fadmin pipeline, then Setup QC.

## ⚠️ Common errors / risk items — item-level valid dates
- **RISK ITEM:** they have flyer-level valid dates **but also item-level valid dates** (bottom of the flyer). E.g. Canon items valid until the 14th, all others until the 28th. **Ensure item-level valid dates are applied** by reading the disclaimers below — we have been called out before and they were very upset.
- Add these disclaimers to **all** items:
  - **"Limited quantities. Certain conditions apply."**
  - **"Quantités limitées. Certaines conditions s'appliquent."**

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals, retailer logo, sign-up page. **Exclude:** coupons, social media, special weblinks. Linking doc used for both box/tag.
- Box each item; use text boxes as required.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name (include brand and size), pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **URLs** provided in separate EN and FR linking docs.
- **Categories:** normally 2 — Camera Lenses, or Cameras & Camcorders.
- **Disclaimer:** tag each item with its corresponding brand's disclaimer at the bottom of each page.
- **Image QC:** use a clean PDF image whenever possible; select cutouts when clean PDFs aren't available.

## Post-processing / FQC (owned by Vendor)
- **URL/Links QC:** for "Items without a URL", search the linking doc (each item is in its respective Page # tab). Confirm item-level valid dates and adjust tagging. For non-shoppable "items" (banners/CTAs with a link), set **Display Type: Link** and paste the URL.
- **FQC:** Data-Piping → Data Piped Image → filter → Data Pipe All (if items aren't data-piping, verify links aren't leading to 404). Custom Action → Set Cutout Images. Horizontal and Vertical preview (after Auto Publish finishes). Then Final QC.
- **Flyer Review type: Lite.**

---
*Source: Gosselin Photo OneGuide (Google Doc `13NvGfP04hY5Ws5ygTTRQ4FhbtHxtS2XFOZPlLvzSUBM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# GP Bikes — Processing Guide

> **Source:** GP Bikes OneGuide (Google Doc `11EtrCra0a1xXRGqHK-peKsUjLaYkAxM6rpUkzngUuc4`), updated Jul 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1 — ad hoc / monthly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); no OS; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Ad hoc (files sent via email). **Cadence:** Monthly.
- No preview date, no linking document.

## Upload & setup (owned by Flex)

- Files sent via email.
- **1 pricing zone**, English, containing all pages, assigned all stores.
- Setup QC: confirm all items in the setup QC checklist are correct.

## ⚠️ Common errors / risk items
- No special risk items — use generic flyer review standards and instructions.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude all:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Box each price separately with all items it applies to (e.g. one price for 3 items → boxed together). Use text boxes to capture all related info.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** brand, valid dates.

## Post-processing / FQC (owned by Flex)
- No special risk items — use generic flyer review standards.
- **Flyer Review type: Lite.**

---
*Source: GP Bikes OneGuide (Google Doc `11EtrCra0a1xXRGqHK-peKsUjLaYkAxM6rpUkzngUuc4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Green Valley Marketplace — Processing Guide

> **Source:** Green Valley Marketplace OneGuide (Google Doc `1gnVdAh4ZHQsyTeH-ZssHnu1vUuWrByWowA38_CuwJwg`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | `#1p-green-valley-marketplace` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer Type 1 — Flyer |
| Processing | Auto-stack |
| Who's involved | Vendor owns processing & FQC; no OS; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Friday, Valid From Friday; Available To Thursday, Valid To Thursday.
- No preview date, no linking document.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu. The folder is named by the flyer's valid date — **always use the lower-case folder, never the Upper Case folder.** Confirm & Upload → Auto-Group → Save & Complete.
- **Pricing zone:** create **1 zone named "Base"**, add all stores, Save & Complete.

### Setup QC
- Confirm all pages uploaded correctly — open the SFTP and ensure nothing remains except the multi-page PDF (Upper Case name not ending in "P####"). If pages were missed, flag to the FT team.
- Confirm flyer valid dates match page 1 of the PDF.
- Thumbnails: 4 Standard.
- **Geography tab: ensure 0 changes to Stores or FSAs** — flag ANY changes to the FT team (via Slack/email) but continue the checklist; flag 100% of discrepancies.
- Platform toggles: Available on ALL platforms.

## ⚠️ Common errors / risk items
- **Upper vs lower case folder:** always upload from the lower-case folder; the Upper Case folder is the combined multi-page PDF.
- **Geography changes:** immediately flag 100% of store/FSA discrepancies to the FT Ops team (doesn't block your work — continue FQC).

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Exclude all:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. No linking doc.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Include:** image (always select a clean PDF if available), brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.

### Image QC
- Always select a clean PDF if available.

## Post-processing / FQC (owned by Vendor)
- **Pre-FQC:** confirm valid dates per PDF; platform toggles available everywhere; thumbnails drawn incl. retailer logo. Standard checks — all items boxed/tagged, previews published & clickable, geography consistent with last week (no stores/FSAs added or removed; flag 100% of discrepancies to FT Ops).
- Complete FQC checklist.
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Green Valley Marketplace OneGuide (Google Doc `1gnVdAh4ZHQsyTeH-ZssHnu1vUuWrByWowA38_CuwJwg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Grocery Outlet — Processing Guide

> **Source:** Grocery Outlet OneGuide (Google Doc `1EzffOf-05f3qL83D-a0seRlpzpi7H0JtA__19qJnYhs`), updated May 7, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#groceryoutlet`, `#cp-groceryoutlet` |
| Hosted URL | groceryoutlet.com |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly (Ops, 10970); Flyer Type 2 — Weekly (CP, 3435) |
| Processing | Auto-stack |
| Who's involved | Content Production (CP uses processed content); no Flex; no OS extra; no coupons; no Strategic Ops |

> **IMPORTANT — hybrid Ops/CP account.** Ops uploads the pages sent by the retailer via FTP for OS to process; CP then uses those processed pages to create further content. **The Weekly - Ops flyer type is the ONLY one Operations touches — do not use any other flyer type.** Ops must ensure pages (and revised pages) are uploaded and processed, and URLs added by **Tuesday morning** before go-live, for CP to take over.

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Tuesday, Valid To Tuesday.
- **Linking document:** Yes — attached to vendor tasks.

## Upload & setup (owned by DOC)

### "Processing Only" flyer runs
1. Download the grid (`.xls`, e.g. `GroceryOutlet_Flipp_07.17.24.xlsx`) from FTP. Delete all columns except **Email Sign Up page** and **URL**, remove duplicate rows, save as the URL document.
2. Upload → Pages → Edit → select folder with correct date → upload all files (check all).
3. **Ensure the "download the deals" page is uploaded** if outlined in the grid (if missing from the FTP but in the grid, download from the shared drive folder).
4. Select files → **no autogrouping, no pricing zones** → wait for sessions to run.
5. Attach the URL document to the vendor tasks.
6. Complete flyer completion and Set Up so vendors are assigned.
7. Note "pages uploaded, URLs attached" in comments.
8. **Hidden on all platforms.**
9. **Set Preview date to Monday.**
10. Send the flyer run ID to `#cp-groceryoutlet` and confirm there are no standalone publications that week.

### Standalone publications
When the grid contains "additional content", follow all Processing-Only steps first, then clone for standalone content:
1. Let the Processing-Only run be processed by OS.
2. Make a NEW flyer run per relevant page, titled "Standalone - (type of content)".
3. Create a PZ (name Base or as fits).
4. Set external run name per retailer / first page.
5. Copy items from the processed Processing-Only upload; **confirm they meet content policy — escalate if not** (and hide on Flipp network depending on outcome).
6. Let sessions run, check off vendor tasks up to FQC.
7. Add all stores, or only the select stores in the grid (via generic stores codesheet), split by region (East, CANV, OR ID WA).
8. Send flyer run IDs to `#groceryoutlet` as early as possible.

## ⚠️ Common errors / risk items
- **Only touch the Weekly - Ops flyer type** — never any other flyer type.
- **Boxing/tagging different sections on one page:** pages have a top section and a bottom section; per the URL doc both sections need their own URL. Ensure boxing matches the URL document.
- **Item-level valid dates:** some items have different valid dates than the flyer — tag accurately.
- **Standalone content may not meet content policy** (short 1–3 page promos like a Summer Blowout / Mother's Day sale) — alert BD, DOL, CP and either push back on go-live or file an exception ticket.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include everything:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Linking doc required.
- Box separate sections per the URL sheet; anything with a price gets a box; box sign-up page and social media.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Linking doc used for both box/tag.
- Watch item valid dates and coupons.

## Post-processing / FQC (owned by DOC)
- **On Mondays:** confirm boxing/tagging is accurate per the URL document (e.g. top-of-page and bottom-of-page URLs boxed/tagged separately).
- **"Processing Only" flyers:** no need to FQC — just ensure they're hidden everywhere.
- **Standalone publications:** confirm content policy (flag to BD/lead + get exception if needed), confirm dates & external run name, all items tagged with URL if provided, add stores from the Standalone `.xls` tabs (generic stores codesheet). Standard thumbnails, standard FQC. **Flyer sorting:** Weekly (CP Genesis Ad) first, then standalones.
- **Flyer Review type: Lite** — not formally reviewed by Ops (owned by DOL).

---
*Source: Grocery Outlet OneGuide (Google Doc `1EzffOf-05f3qL83D-a0seRlpzpi7H0JtA__19qJnYhs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Guardian & I.D.A. — Processing Guide

> **Source:** Guardian & I.D.A. OneGuide (Google Doc `1mbyu9utChEpXbzbMhRs_FsOY-_elP0sMhLnBngWCJ7Q`), updated Jun 11, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#mckesson` |
| Hosted URL | guardian-ida-remedysrx.ca/en/flyer-search |
| Flyer types | Promotional Flyer 25 km (4978) · Promotional Flyer 5 km (6376, clone of 4978) · Prescription Centre Flyer 25 km (5128) · Prescription Centre Flyer 5 km (6381, clone of 5128) |
| Processing | Auto-stack |
| Who's involved | DOC owns processing; Flex (Flyer Review); no coupons; no Strategic Ops |

## Files & schedule

- **Files:** arrive well ahead of time via FTP (can be uploaded early), but watch for new inserts via email. Store list also arrives early — **always double-check for an updated version on the FTP before go-live.**
- **Cadence:** Available From Wednesday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **Preview date:** set an internal preview date of **Monday** to allow extra FQC time — this retailer's process is finicky and shouldn't be left to the last minute.
- No linking document.

## Overview & cloning (KEY structural rule)

Guardian and I.D.A. get a **Weekly** flyer (with **Plus** and **Pro** versions) plus a **Monthly** flyer (**Prescription Center**). Same processes/codesheets (with manipulations) apply to both. **Every version is uploaded to a 25 km flyer type, then cloned into a 5 km flyer type** so the shorter-range version can be promoted independently.
- Clone all 25 km flyers to 5 km. Weekly only → **4 flyers total**; with the Monthly → **8 total.** Open all 4 (or 8) in separate tabs for FQC and store-adding.

## Upload & setup (owned by DOC)

**Pricing zones & pages (codesheet):**
- Download the **Tracking Sheet** from email/FTP (search "tracking" or the cycle date, e.g. "1018").
- Use the **Guardian & I.D.A. Pages Codesheet Template**; name it by valid date. Paste page names into matching slots; **copy the PLUS page 1s into the PRO zone page-1 cells** (codesheet won't run if blank — extra pages removed later). Paste the "size" column from the Tracking Sheet (every cell needs a number or the codesheet won't run). Add/delete rows for extra/fewer pages. Update cells B4–B6 per the Tracking Sheet. Download as `.csv`.
- **Weekly:** create the shell from the **Plus 25 km** flyer type (6786) — **NOT** the Promotional 25 km type. Use dates from cell B6 (Valid Friday–Thursday; Available From = Wednesday, two-day preview). Upload with config **`guardian_pages`** and the **3rd, 4th, 5th and 6th toggles**. Process and wait for sessions (done when Flyer Creation task becomes available — don't mark complete yet). This creates the 4 Plus pricing zones.
- **Switch flyer type** to the **Promotional 25 km** type (4978): Overview → Edit Details → move flyer run to "Promotional Flyer 25 km" → OK. **Rerun the codesheet** (ignore "pages already uploaded" — hit **Force Processing**). Now 8 pricing zones exist.
- **Delete all PZs with "FR" in the name**, then kick off flyer creation.
- **Delete the first PPLUS page** from each PRO pricing zone (`####_01_PPLUS…`).
- **BIL** zones set to English → cross-language to French during Pre-FQC.
- **Monthly:** upload the codesheet as above but **no need to switch flyer type or rerun** — only 2 PZs (one English, one Bilingual), uploaded once to the **Prescription Center 25 km** type (5128).
- **Option+ pages** (Weekly): if the Tracking Sheet name includes `OPTION+` (and has an OPTION+ WEB tab), manually upload both pages listed (English), mark Flyer Creation complete, and manually add to all pricing zones per the tab instructions.

**Setup QC:** confirm dates on page 1 of a PZ; No Theme applied (unless seasonal); thumbnails Standard 4; legibility heights Scan 35 / Read 25. The orange codesheet warning can be ignored.

## ⚠️ Common errors / risk items
- **Upload to the Plus 25 km flyer type first — NOT the Promotional type** — then switch type and rerun to generate the Pro zones.
- **Codesheet won't run if PRO page-1 cells or any size cell is blank** — fill PRO page 1s with the PLUS page 1s and put a number in every size cell.
- **Delete FR zones and the first PPLUS page from PRO zones**; cross-language BIL zones to French.
- **Store filtering (Pre-FQC):** in the Digital Posting Run List, filter Flipp Km = **25** and Flipp Zone to Guardian zones (start with "G:"). **Do NOT include PCN zones** (e.g. `GPC_OAW`) in Weekly runs — those go to the Monthly (PCN) tabs.
- **Boxing:** Guardian doesn't use data piping; images are mainly cutouts — box **every individual item** with the info on the flyer; **one box per item** even if boxes overlap. Don't merge items into one box.
- Look out for **item- or page-level valid date overrides** — rare and easy to miss.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals. No linking doc.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates.
- **Name/Brand:** tag brand as it appears (multiple brands → both in brand field); Name = BRAND NAME + NAME + ITEM (often bold full caps).
- **Description:** fully bilingual (English + French) as in flyer; include any quantity/number.
- **Pre/Postfix:** most often "CH./EA."
- **SKU:** generally none; if present, enter as shown.
- **Disclaimer:** enter item exclusions into disclaimer.

### Image QC
- Use clean PDFs wherever possible. If a clean PDF is unavailable, select **Do Not Use PDF Images**.

## Post-processing / FQC (owned by DOC)

**Assign stores (Pre-FQC):**
- Download the **Digital Posting Run List** from email/FTP. Duplicate the GuarIDA store codesheets TEMPLATE, name by valid date.
- Filter the Run List (Flipp Km = 25; Flipp Zone = Guardian "G:" zones; isolate PCN "GPC_" for the Monthly tabs). Build generic codesheets in the Guar 25 km tab (SAP codes → stores header; isolated Flipp Zones → pricing zone header). Repeat for 5 km.
- Find & Replace `PPLUS` → `PLUS` so PZ names match Fadmin. Download tabs as `.csv`.
- Upload codesheet — config **`generic_stores`**, **first toggle only**. If a store can't be found, add it at the merchant level with the SAP# as the merchant code, then rerun.
- Delete PZs with no stores (0/0); cross-language remaining BIL zones to French.

**Inserts:** Guardian, I.D.A. and RemedysRx get the same insert style; McKesson emails monthly which 2–3 of 5 to post at the end of each live flyer. Download that month's inserts, upload in English, and add them as the last pages in all PZs in the order listed (Pages → Layout tab).

**FQC:** mark Auto-Stack Spotcheck complete; Edit Details (Weekly: Available From Wed, Valid From Fri, both To next Thursday — check page 1; Monthly: confirm against assets; no theme, available everywhere, no external run name); thumbnails Standard 4; legibility Scan 35 / Read 25; verify PPLUS removed from PRO zones and BIL zones cross-languaged; Geography — stores opt in/out so vary slightly (1–4 store difference OK; investigate larger gaps against the Run List). Ignore categories and unassigned-stores warnings.

**Post-FQC clone:** clone all 25 km flyers into the 5 km types (Weekly → Promotional 5 km; Monthly → Prescription Centre 5 km). On the cloned run remove all stores from all PZs, upload the **Guar 5 km** `.csv` codesheet, confirm stores added, delete 0/0 zones, and re-complete FQC.

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Guardian & I.D.A. OneGuide (Google Doc `1mbyu9utChEpXbzbMhRs_FsOY-_elP0sMhLnBngWCJ7Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
