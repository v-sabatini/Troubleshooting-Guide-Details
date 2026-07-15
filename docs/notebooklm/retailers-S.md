# Retailer Processing Guides — S

> Bundle of 43 retailer-specific processing guides (S). Contacts and credentials are omitted from every guide.

**Contains:** Safeway Canada, Sobeys West, Sobeys Ontario & Sobeys Atlantic, SAIL, SAQ, Save A Lot, Save-On-Foods (+ Urban Fare), Savers Junction, Sephora Canada, Sharpe's Food Market, Sheridan Nurseries, Shop Sante, Shopper+, Shoppers Drug Mart / Pharmaprix, Shoppers (SuperValu), Showcase US / Showcase (CAD), Sklar Peppler, Slumberland, Smart & Final, Smiths Furniture and Appliances, Sobeys Liquor Banners, Sobeys Urban Fresh, Sobeys Wholesale (West & Atlantic), Source Office Furnishings, Sport Chek & Atmosphere, Sports Excellence (Canada & USA), Spring Market, Sprouts, Staples USA (Manual Indexed), Staples (Canada / Professional), Starsky, Stater Bros Markets, STIHL, Stokes, Strack and Van Til, Super C, Super King Markets, Superior Grocers, Supermarche Aures, Supermarche PA, Supermercado Nuestra Familia, SuperValu (Shop Easy Food) / Freshmart, SuperValu Liquor, Surplus Furniture & Mattress Warehouse, Sutherlands


---

# Safeway Canada, Sobeys West, Sobeys Ontario & Sobeys Atlantic — Processing Guide

> **Source:** Safeway Canada / Sobeys OneGuide (Google Doc `1FaE9uwvdrTb4ehSxRXGC0ZmfAMOHf-MpMro_hMJNVis`), updated Oct 20, 2025. Contacts/credentials omitted.

> **Scope:** One OneGuide covering four banners — **Safeway Canada, Sobeys West, Sobeys Ontario, Sobeys Atlantic.** Upload/setup differs per banner (below); OS pipeline processing and post-processing QC are shared across all banners.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium (S1C1) |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URLs | Safeway Canada: safeway.ca/flyer · Sobeys: sobeys.com/en/flyer |
| Publications | Safeway Canada Weekly Flyer; Sobeys Weekly Flyer — West / Ontario / Atlantic |
| Processing | Auto-stack; Flex (3FL — Pre-FQC image/category QC, Mondays); no coupons; Strategic Ops involved (Feedel / retailer data services) |
| Key trackers | Sobeys Insert Tracker · Sobeys 3fl Weekly Tracker · Rachelle Bery (RB) Store List |

## Files & schedule (all banners: files Wed, preview Mon, live Wed)

- **Safeway Canada:** Available From Wed 3:00AM, Valid From Wed, Available To Thu 3:00AM, Valid To Tue.
- **Sobeys West:** Available From Wed 3:00AM, Valid From Wed, Available To Thu 3:00AM, Valid To Tue.
- **Sobeys Ontario:** Available From Wed, Valid From Wed, Available To Thu, Valid To Tue.
- **Sobeys Atlantic:** Available From Wed 6:00AM, Valid From Wed, Available To Thu, Valid To Tue 10:59PM.
- **Workflow:** Upload & Setup (DOC, Wed) → 3FL Pre-FQC (FLEX, Mon: Image QC & Category QC) → Inserts / Image QC / Category QC / Scene+ / Page Categories / Compliments / SJC Links / Deep Links / Custom Tiles / FQC (DOC, Tue) → Live (Wed).

## Upload & setup (owned by DOC) — per banner

**Common to all banners:** files arrive in an SFTP subfolder; download the PDF codesheet and the store distribution file. Manipulate the codesheet, save as CSV, upload. Then build a generic store codesheet from the distribution file's Digital tab, save as CSV, upload. Edit Details: Preview Date Monday before go-live, available everywhere, external run name "Weekly eFlyer mm/dd - mm/dd", no theme. Thumbnails Standard 4 + Thumbnail 400W. Merge skinny "flap" pages (FL01 → merge into FL02 so pages are side-by-side). Attach the week's Embedded Links doc (`SobeysWkxx_Embedded Flyer Links.xlsx` — shared by all banners) to all vendor tasks via Mass Attachment on "Vendor Box QC". Set all vendor tasks to Urgent. Check `#sobeys` Slack for special campaigns (may need Urgent Processing Tickets to hit data-service deadlines).

- **Safeway Canada:** files in `/SOBEYS WEST/`. Codesheet: **DELETE "Sobeys" zones, KEEP ON and BC zones** (those are Safeway-only); rename Safeway zones to letter+number (AB1, SK1, ON1, BC1, etc.); change DIGITAL/FLAP01/FLAP02 → FLYER; move P01 above FL01; delete hidden columns; clear rows 2–5. Stores from the `[GROCERY Digital]` tab (paste top-down in the same order as the codesheet left-to-right).
- **Sobeys West:** files in `/WEST/`. Codesheet: **DELETE ON and BC zones (Safeway-only), DELETE "Safeway" zones**; keep/rename Sobeys zones (AB1, SK1, MB1, etc.). Same DIGITAL/FLYER, P01, hidden-column steps. Stores from `[GROCERY Digital]` tab.
- **Sobeys Ontario:** files in `/ONTARIO/`. Codesheet: rename zones to Zone# (Zone 1, Zone 1B, Zone 2); cut/paste the Bilingual zone so all zones are in one row and delete extra bilingual cells. Stores from `[Digital]` tab (**Zone 1A = Zone 1**).
- **Sobeys Atlantic:** files in `/ATLANTIC/`. Codesheet: rename zones to Zone#; cut/paste Bilingual zone into one row. Stores from `[Digital]` tab, zones renamed to match Fadmin.
- **Highlighted rows** in a codesheet → the Store Code needs updating in Fadmin (Stores/Sets → change old code to new, e.g. St. Anne's 5302 → 4048).

## ⚠️ Common errors / risk items (retailer-specific)

- **Rachelle Bery (RB) pages** are store-specific: let the codesheet pull them in (OS still boxes/tags), but **remove them from all pricing zones during Setup QC** and note the position — they get re-added to their own store-specific pricing zones during the Inserts process.
- **Scene+ items:** Sale Story must read "*xxx* **Scene+** PTS when you buy x" (**no space** between "Scene" and "+"); add the **[Scene+]** category (the only case where an item has 2 categories).
- **Scene+ Member Pricing items:** Prefix "Scene+ Member Pricing" (don't forget the "+"); Disclaimer "$xx without Scene+ Card"; category [Scene+].
- **Verified items:** must have "Verified" in the prefix (e.g. "Verified" or "Verified Scene+ Member Pricing").
- **HOT PRICE items:** Prefix "HOT PRICE" and delete "HOT PRICE" from the Sale Story.
- **Compliments items:** "Compliments" in the Brand field AND "COMPLIMENTS" (caps) at the start of the Name field; French name goes in Description, not Name.
- **Item SKUs (NEW Dec 1 2025):** if there are NO SKUs on the PDF, tag the items as one item block (as usual) — **do NOT flag to OS.** One SKU per item; delete extra SKUs Fadmin pulled in; if multiple, search sobeys.com / safeway.com to match SKU to item.
- **SJC Links / Deep Links / Embedded Links / Custom Tiles:** check the week's entries in the Sobeys Insert Tracker / Slack and box/tag; ensure the Embedded Links doc is attached to vendor tasks.

## QC specifics

### Box Draw (Low complexity; Auto-Box ON, Box QC bot OFF)
- No linking document required. **Exclude** coupons and retailer logo; **Include** social media.
- Item block with 1 item → one item box over image and text. Item block with 2+ items → **stack the Text Boxes on top of one another**.
- Box social media links (Digital Exclusive, App Store, Google Play) and Embedded Links CTAs (Learn More, Order Online, Recipe).

### Tag / Tag QC (Low complexity; Auto-tag ON — Tag Lite)
- No linking document. Include brand, name, pre/postfix, valid dates, description, SKU (new Dec 2025), price, sale story, categories, disclaimer, original price, URLs, image selection (PDF preferred, new Apr 2025).
- **Brand:** always include; for Compliments items include "COMPLIMENTS" in both brand and name. **Name:** as-is, brand NOT in name (exception: Compliments). French name → Description.
- **Pre/Postfix:** use the drop-down, match the PDF. Price-per-weight → `/lb` in postfix, `$$$/kg` in Description. Scene+ / Verified / HOT PRICE prefixes as above.
- **Valid dates:** only include if they differ from the flyer run dates.
- **Categories:** based on page headings; one per item, plus [Scene+] where applicable (Category and Category Highlights should match). Detailed category guide: Meat (raw/ground, no boxed/plant-based meats), Produce, Seafood (fresh/frozen, no canned/boxed), Deli, Bakery, Grocery, Dairy, Floral, Home, Baby & Pet Care, Pharmacy, Baby, Health & Beauty, Beverages (no instant coffee), Scene+.
- **URLs:** Digital Exclusive (Safeway: safeway.ca/mobile-app; Sobeys: sobeys.com/en/promotions/mobile), App Store, Google Play (Foodland app), plus Embedded Links CTAs (use Sobeys vs Safeway URLs correctly).

### Image QC (completed during Tag/Tag QC; also FLEX/3FL on Mondays)
- **Rule of thumb: pick the cleanest image.** If no clean PDF image, choose the cutout / "Do not use PDF images". Multiple options → the image best matching the product name.
- **Do NOT use PDF images** for lifestyle shots (products on a cutting board/plate) or images with too many shadows / black outlines.

## Post-processing QC (all banners)

- **Inserts (DOC):** find inserts in the Sobeys Insert Tracker (correct banner tab); RB pages via the RB Store List. Conditional-formatting formula to highlight store-specific inserts: `=COUNTIF($B$1:$C$1000, B1)>1`. (Process is video-documented — too complex to write out.)
- **Item Image QC / Category QC / Page Category QC (FLEX — 3FL, Mondays):** verify via the Sobeys 3fl Weekly Tracker. Categories one per item + Scene+ where applicable. Page categories: none on page 1, use as many as visible, include [Scene+] on predominantly-Scene+ pages.
- **Scene+ Points QC (DOC):** Item Search Sale Story contains "PTS" (must read "xxx Scene+ PTS when you buy x"); add [Scene+] category to any items with Scene+ callouts missing it (export/import if many); Scene+ Member Pricing items → Prefix "Scene+ Member Price", Disclaimer "xx without Scene+ Card", category [Scene+].
- **Compliments QC (DOC):** Item Search Brand contains "compliments" → ensure "compliments" in Name; Brand is-not "compliments" + Name contains "compliments" → add "Compliments" to Brand (export/import if many).
- **Verified QC (DOC):** Page Grouping Index 1 + Prefix is-not "Verified" → ensure Verified items have Prefix "Verified".
- **HOT PRICE QC (DOC):** Sale Story contains "hot price" → set Prefix "Hot Price" and delete "HOT PRICE" from the Sale Story.
- **Embedded / SJC / Deep Links (DOC):** tag CTAs from the Embedded Links doc (correct Sobeys vs Safeway URLs); box/tag SJC Links and Deep Links per the week's Sobeys Insert Tracker tabs (Deep Links: red weeks = none).
- **Custom Tiles (DOC):** check `#Sobeys` Slack; apply via QC Thumbnails → Storefront Premium & Storefront Carousel Premium → Override Thumbnail on the right zones. Store-specific → duplicate pricing zones ("AB1 - Custom Tile") and move the store; FSA-specific → duplicate zones + Assign/Remove FSAs custom actions. Date-specific tiles → Create Trigger (remove manually — no removal trigger) and file an OPTICS ticket.

## FQC / go-live (owned by DOC)
- **⚠️ NEW (Apr 28 2026) Safeway Canada ONLY:** after post-FQC steps, **clone the Safeway Canada AB/MB/SK ad into the Safeway Canada ON/BC ad.** From the AB/MB/SK version remove stores and delete PZs containing BC/ON (incl. BC1/BC2/ON1/ON2); from the ON/BC version remove stores and delete PZs containing AB/MB/SK. Re-run tile generation and page stitching, and complete FQC for the cloned ad.
- Basic checks: geography, vertical preview, then the pipeline FQC checklist.

## Flyer review
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Safeway Canada / Sobeys OneGuide (Google Doc `1FaE9uwvdrTb4ehSxRXGC0ZmfAMOHf-MpMro_hMJNVis`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# SAIL — Processing Guide

> **Source:** SAIL OneGuide (Google Doc `1R_8uughtXaTKKM9AcGUzIJm2s7wYpvI-g9PPZHJc-rc`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1plat_sail`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | https://www.sail.ca/en/sales/online-flyer |
| Flyer types | Flyer Type 1 — Weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); **linking document required**; no coupons; no Feedel; OS N/A |

## Files & schedule

- **Files received:** Monday
- **Available From:** Monday · **Valid From:** Tuesday · **Available To:** Monday · **Valid To:** Tuesday
- **Linking document:** YES — REQUIRED (also contains the weekly UTM code).
- **Workflow:** Upload & Setup (Vendor, 5 days out) → Image QC (FLEX, 2 days out) → FQC (DOC, 1 day out).

## Upload & setup (owned by Vendor)

- **⚠️ Pages may need to be added to the SFTP by the processor if the client sends files over email.**

**Ontario flyer run:**
- Manual upload of **English** pages from SFTP; Auto-Group or manually paginate; ensure correct language. Save & Confirm; **do NOT Process Internally.**
- Create Base pricing zone, select all pages, add **all Ontario stores**.
- Linking doc: before uploading, ensure only Ontario-specific URLs are visible.

**Quebec flyer run:**
- Manual upload of **ALL** pages; Auto-Group or paginate; ensure correct language (English vs French). Save & Confirm; do NOT Process Internally.
- Create **English & French** pricing zones, select all pages, add **all Quebec stores to both**.
- Linking doc: before uploading, ensure only Quebec-specific URLs are visible.

### Setup QC
- Confirm all pages uploaded (Items View); **RISK:** confirm no un-uploaded pages remain in SFTP. Confirm dates (first/last page); 4 Standard thumbnails; preview dates set.

## ⚠️ Common errors / risk items (retailer-specific)

- **Cloning + UTM codes:** original flyer runs are for **Flipp & Distribution only**. Flyers must be **cloned** and labelled "- Hosted" in the new name, and **all URLs updated with that week's UTM code** (found in the linking document). **Ontario and Quebec UTMs are different.**

## QC specifics

### Box Draw (Low complexity; Auto-Box OFF, Box QC bot OFF)
- Linking document required (used for both Box and Tag).
- **Include:** coupons, packaged deals, retailer logo, sign-up page, special weblinks. **Exclude** social media.
- Box each item with a price; box the retailer logo; box any sale-story banners.

### Tag / Tag QC (Low complexity; Auto-tag OFF)
- Linking document required (used for both Box and Tag).
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Tag logo, promotions, category callouts, standard items, callouts, rewards program.

### Image QC
- Standard — PDF preferred if clean; otherwise cutouts accepted.

## Cloning (owned by DOC)

SAIL has platform-specific URLs with UTM codes at the end. Clone the original runs into 2nd versions so there are **FOUR** runs total:
- Ontario – Flipp & Distro (hidden on Hosted) + Ontario – Hosted only
- Quebec – Flipp & Distro (hidden on Hosted) + Quebec – Hosted only

For each clone, retrieve the UTM from the original linking document (Ontario and Quebec UTMs differ) and add it to all URLs:
- Export Items → delete the 2nd/lower section → keep only Item_id, SKU, URL → add the UTM to ALL URLs → save as CSV → import updated URLs. Repeat for the 2nd clone.
- Confirm UTMs added: Overview → Item Search → Apply Filters (all items populate) → Ctrl+F the specific UTM. Then complete the FQC checklist for both clones.

## FQC / Flyer review
- Pre-FQC (FLEX) / FQC (DOC): confirm dates vs PDF, availability toggles, thumbnails incl. logo; all items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: SAIL OneGuide (Google Doc `1R_8uughtXaTKKM9AcGUzIJm2s7wYpvI-g9PPZHJc-rc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# SAQ — Processing Guide

> **Source:** SAQ OneGuide (Google Doc `1UO7UwIqrMZVCRK5SapOO1SAyNRGb9PdYNjTChST04c0`), updated May 14, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms (we do **not** power their hosted) |
| Slack channels | `#saq` |
| Flyer type(s) | Flyer (bilingual EN/FR) |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |
| Agency | External comms go through the agency Cossette (contacts in the OneGuide — not stored here) |

## Files & schedule

- **Files received:** ad-hoc.
- **Cadence:** Available/Valid From Thursday → To Monday.
- **Preview date:** 2 days before launch (if files arrive on time); preview sent to retailer.
- **Linking document:** yes.
- **Workflow:** Upload & Setup (DOC) → Preview 2 days out → FQC + feedback (DOC).

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP. **Pages are labelled `P#` to match the internal run name — upload accordingly.** Upload **both English and French pages**. Auto-Group (or manual grouping numbers), ensuring the correct language is selected. Save & Confirm — do NOT Process Internally.
- **Pricing Zones:** create **1 English and 1 French** pricing zone for each set of pages; add all applicable stores. **Add the base pricing zone to both English and French.**
- Attach the linking document (labelled with a matching `P#`) to **all processing tasks**.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View). Confirm flyer dates. Thumbnails: 4 Standard.
- **Set all preview dates 2 days prior to the available date.**

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot ON.** Linking doc required (used for both Box/Tag). Exclude coupons, packaged deals, retailer logo, sign-up, social. **Include special weblinks only if called out on the linking document.**
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** **Price: include only if listed on the PDF.**
  - ⚠️ Include **ALL flyer text in the title, exactly as written** (description can be empty).
  - ⚠️ **Sale Story must match the PDF exactly** — if it reads "Bonus 250 points" do not rewrite as "250 Bonus Points"; if "BONI 500 PTS" do not rewrite as "500 PTS BONI". Description text must include the `|` separators as on the PDF.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## Final QC / go-live (owned by DOC)

- Confirm dates vs PDF and availability toggles; thumbnails include logo.
- **Both English and French zones have the right pages.**
- **Links QC:** use the "Items Without URL" button and cross-reference the link document so no linked item is missed.
- **Tracking Codes:** Overview → Ad Hoc Processing → Manage Tracking Codes. Add — Code type **Dynamic Variable**, Source **Distribution**, Variable Name blank, Variable Value `?utm_campaign=saq-circulaires-alwayson&utm_medium=display&utm_source=flipp&utm_content=1x1-circulaire-fr`; then "Apply all tracking codes".
- Standard checks: items boxed & tagged; spotchecks (20% of pricing zones); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**

---
*Source: SAQ OneGuide (Google Doc `1UO7UwIqrMZVCRK5SapOO1SAyNRGb9PdYNjTChST04c0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Save A Lot — Processing Guide

> **Source:** Save A Lot OneGuide (Google Doc `1eEEuBTChFf1hsW7JZvBM_bOBLX8pSbOWJwegGjvkZDw`), updated Jan 22, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#savealot` |
| Flyer type(s) | Weekly Flyer |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** ad-hoc.
- **Publication cadence:** Available/Valid From Wednesday → To Wednesday.
- **Preview date / linking document:** none.
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC).

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu (files labelled with MONTH and WEEK) → Confirm & Upload. Pages may need to be added to the SFTP by the processor if the client sends files by email.
- Once pages are listed, Auto-Group (or manually enter Grouping Numbers). **English pages only.** Save & Confirm — **do NOT Process Internally.**
- **Pricing Zone creation:** create a **Base** pricing zone, select all applicable pages, Save & Confirm. **Add only the BASE pricing zone (6 stores).**

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **Risk:** if uploading from SFTP, confirm no pages remain un-uploaded.
- Confirm flyer dates (usually first or last page).
- Thumbnails: 4 Standard. Complete the Setup QC checklist.

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.**

## Final QC / go-live (owned by DOC)

- Confirm dates vs PDF and availability toggles.
- Thumbnails correct and include the retailer logo.
- Standard flyer review: all items boxed & tagged; spotchecks (20% of pricing zones); previews published & clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Save A Lot OneGuide (Google Doc `1eEEuBTChFf1hsW7JZvBM_bOBLX8pSbOWJwegGjvkZDw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Save-On-Foods (+ Urban Fare) — Processing Guide

> **Source:** Save-On-Foods / Urban Fare OneGuide (Google Doc `1gtUv_cxnYboRD8XVzuMMBGfH1OOrabPo-9uhLhaD3NU`). Contacts/credentials omitted.

Covers **Save-On-Foods (SOF)** and its sibling banner **Urban Fare (UF)**. Setup is the same for both; UF has no My Offers linking doc and files/folders/codesheets are labelled `UF_WK##` instead of `SOF_WK##`.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#overwaitea`, `#3fl-saveonfoods`, `#flexflyerreview` |
| Hosted URL | saveonfoods.com · urbanfare.com |
| Flyer type(s) | Weekly (Flyer type 180) |
| Processing | Auto-stack; 3FL + Flex Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Friday (evening files dropped Thursday; upload complete once files synced Friday).
- **Cadence:** Available From Wed 3:00 AM → Available To Thu 2:59 AM; Valid From Thu 3:00 AM → Valid To Wed 11:59 PM.
- **Preview date:** Sunday before live (link sent Monday, or Tuesday on long weekends).
- **Linking document:** yes — MYO Document; naming `SOF_WK##_SKU_PageName` / `UF_WK##_SKU_PageName`.
- **Day-by-day:** Fri upload → Fri/Sat OS processes → Sun 3FL Item QC → Mon DOC FQC + preview link → Tue corrections → Wed page swaps.

## ⚠️ Common errors / risk items (retailer-specific)

- **$1.49 Sale pages (highest-value risk):** when $1.49 pages are provided to trigger in at a future date, they **must be present during the retailer preview/corrections period**, then **removed before go-live**. History: an April 2024 CuSat incident — revised pages were implemented the same day the $1.49 triggers ran at midnight, so triggers failed to remove the revised pages; $1.49 pages went live briefly, were screenshotted, and leaked online. Mitigation: pages are removed from preview **as early as Noon the day prior to launch** to ensure correct state before EOD/launch.
- **SKU tagging is a risk item** — follow the SKU lookup steps in order; do not use shortcuts (can isolate the wrong SKU/original price).
- **Save-On-Foods: tag ONLY the Regular Price field — do NOT tag Original Price.** If REG_PRICE is blank, leave blank. If item/page not on the spreadsheet, leave SKU/regular price blank. Multiple SKUs → tag both separated by a comma.
- **Mi9 custom action** must run after data-piping groups are generated (else it errors). See troubleshooting below.

## Upload & setup (owned by DOC)

- From the **Save-On-Foods Merchant FTP**: grab the `.xls` codesheet (e.g. `SOF_052523.xls`) and the operations + items `.txt` files uploaded on the same date.
- **Upload the `.xls` codesheet (no manipulation):** Config **`overwaitea`**; PDF base directory = full base path; **uncheck 'region assignment' and 'combine zones'**; Save & Process.
- Build the SKU/PageName spreadsheet from the items `.txt` (Text-to-Columns on `|`; delete PAGE NUMBER, ITEM TYPE, ITEM PRICE, BRAND, CATEGORY ID, DISC PRICE, DISC PRICE UOM — **keep REG PRICE / REG PRICE UOM**; Remove Duplicates → ~25k–40k unique; tab 'SKU'; second tab 'Page Names' = Version + Store# from codesheet). Save as `SOF_Week#_SKU_PageName.xlsx` and mass-attach to all vendor tasks. UF has its own PDF folder, items file, ops file and codesheet.

### Setup QC
- Dates as above; add Sunday preview; available everywhere; no theme; 4 standard thumbnails.
- All pricing zones have stores/FSAs assigned (page counts within 1–3 pages of each other).
- Attach `SOF_Week#_SKU_PageName.xlsx` and MYOffers doc to all vendor tasks; mark vendor tasks high priority; complete Fadmin Setup QC.

## QC specifics

- **Box Draw — Medium; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up, social. **Include My Offers links.** Complete even if linking doc is missing.
  - "Plenty for $20" banner → ONE box, direct link `saveonfoods.com/plenty-for-20/`. Butcher's Box pages → ONE box. Books boxed/tagged as individual items; magazines/cards as LINK type. My Offers callouts boxed **separately** from the item (top box = item, bottom box = My Offers link; no text boxes). Flu/Pharmacy banners → link. "UNREAL DEAL" → 2 boxes (item + My Offers link).
- **Tag / Tag QC — High; Auto-tag ON; PDF image auto-select ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Brand: No.** Tag name exactly as PDF including brand in the name; description = size/weight/country of origin.
  - **Sale story:** More REWARDS points callouts (tag "PC…" wording exactly, e.g. "FREE WITH 1900 More REWARDS POINTS REDEEMED"). BOGO/# for/% off callouts go in **pre_price_text**, not sale story.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## SKU / Item QC (3FL, Pre-FQC)

- Export items → keep `item_id, sku, display_type, name, description, sale_story, pre_price_text, raw_current_price, price_text, url`; sort by name. Reference the attached item QC doc to fill SKUs consistently; when name+description match but SKUs differ, it likely has a My Offers callout → pick ONE SKU. Set link-type items (My Offers, Learn More, Pharmacy, Books, Recipe) to link type. Re-import CSV (col1 `item_id`, col2 `sku`); confirm no blank SKUs and none with multiple SKUs. Screenshot/flag items missing SKUs in `#3fl`.

## Mi9 Custom Action (sub-item generator)

- Format ops file: replace all `"` with nothing and all `,` with `|`; save as `SOF_WK##_Ops.txt`; upload and note the file ID.
- System → Custom Action → **Mi9 Sub Item Generator** (not report). Flyer Run File ID = flyer run ID; ID of uploaded file = ops file ID. Wait (up to ~15 min for SOF). Verify an item shows Sub Items (#) ≥ 1.

### Mi9 troubleshooting
| Issue | Action |
|---|---|
| "Flyer run has no sibling groups" | Item image QC → Generate Data Piping Groups |
| No sub-items on the whole page | Generate data piping groups; re-run page tile gen / page stitching; re-run Mi9; republish |
| No sub-items on a single item | Verify SKU; look up sub-item SKU on saveonfoods.com — if no results, item not live / SKU wrong → flag |
| "Unquoted fields do not allow \r or \n" | In the txt ops file, ensure 3-digit stores have a `.` after them (901 → 901.); re-add file, re-run |

## Post-processing (DOC)

- **Corrections Document (SOF only):** creates custom clickable items with custom circular promotion codes; box the item in each page, tag with the code from the corrections sheet, append ops-file sub-items, re-run Mi9, re-run page stitching (sync up to 3h), live-check.
- **Resyncing SKUs:** corrections often mean the SKU is wrong — verify against `SOF_WK##_SKU_PageName` across all zones, then re-run Mi9.
- **Urban Fare FQC:** fill blank SKUs from the attached doc; generate data-piping groups; upload/format UF ops file; run Mi9; check api products count (~100–200+ for UF).
- Preview links for both banners sent to the retailer (email list in the SOF cheatsheet — not stored here).

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Save-On-Foods OneGuide (Google Doc `1gtUv_cxnYboRD8XVzuMMBGfH1OOrabPo-9uhLhaD3NU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Savers Junction — Processing Guide

> **Source:** Savers Junction OneGuide (Google Doc `16dx8jngNvTpskTySPz8pOTW8ZGvDxt3f6aKRRY07FVI`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Flyer type(s) | Flyer |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available/Valid From Friday → To Thursday.
- **Preview date / linking document:** none.
- **Workflow:** Upload & Setup (Vendor) → FQC (Vendor).

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP; folder is named by the flyer valid date — **always use the lower-case folder, never the Upper Case folder** → Confirm & Upload.
- Auto-Group → Save & Complete.
- **Pricing Zone:** create one zone called **Base**, add all stores, Save & Complete.

### Setup QC
- Confirm all pages uploaded — open the SFTP and ensure nothing remains except the multi-page PDF (Upper Case name, not ending in `P####`). If pages were missed, flag the FT team.
- Confirm flyer valid dates match page 1 of the PDF.
- Thumbnails: 4 Standard.
- **Geography Tab: ensure 0 changes to Stores or FSAs.** If there are ANY changes, flag the FT team (continue QC, but flag 100% of discrepancies).
- Platform toggles: available on ALL platforms.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up, social, special weblinks.
- **Tag / Tag QC — Low; Auto-tag ON.** Always select a clean PDF image if available. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**

## Final QC / go-live (owned by Vendor)

- Confirm valid dates vs PDF; available everywhere; thumbnails include retailer logo.
- Standard checks: all items boxed & tagged; previews clickable; **geography consistent WOW (no stores/FSAs added or removed)** — immediately flag 100% of discrepancies to the FT Ops team (does not block).
- **Flyer Review type: Lite.**

---
*Source: Savers Junction OneGuide (Google Doc `16dx8jngNvTpskTySPz8pOTW8ZGvDxt3f6aKRRY07FVI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sephora Canada — Processing Guide

> **Source:** Sephora Canada OneGuide (Google Doc `1F0IZjrb2HS2Re2wpf08tK3Oux5uQK_43mbRgyEpgk_M`), updated Jan 28, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#sephora-canada` |
| Hosted URL | sephora.com/ca |
| Flyer type(s) | Holiday — bi-weekly, October–December (bilingual EN/FR) |
| Processing | Auto-stack; Feedel/Strategic Ops **yes**; no coupons |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available From Friday, Valid From Monday → Available To Friday, Valid To Monday.
- **Preview date:** Wednesday.
- **Workflow:** Upload & Setup (Vendor) → FQC + preview link → review corrections (DOC).

## Upload & setup

- Download and **manually upload files in both English and French** (you may need to split PDFs into individual files).
- Add all stores for **both pricing zones**. Use standard 4 thumbnails. Set the external run name from the flyer for both EN and FR.
- **Attach the linking document, split into English and French.** When building the **French** file, delete the English product name; when building the **English** file, delete the French product name.
- **Confirm dates with the client — they are not always clearly communicated.**

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot ON.** Linking doc required (Box Draw specific). Exclude coupons and packaged deals. **Include retailer logo, sign-up page, social media, special weblinks.**
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-select ON.** Linking doc required (Tag specific). Include brand, name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates.**
  - **Name, Brand, Description, SKU, and URL all come from the linking doc** (client-facing name/brand/description; SKU e.g. `2902054`; the full product URL from the doc).

## Final QC / go-live (owned by DOC)

- Double-check thumbnails; review image QC (clean PDF where possible).
- **Send preview links well in advance** — they typically provide feedback; include the feedback tracker pinned in the account channel in the email.
- Remove quotation marks from all descriptions; complete item searches on their behalf.
- **Check for items without URLs — all items should have links unless otherwise called out.**
- Complete the FQC checklist.
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Sephora Canada OneGuide (Google Doc `1F0IZjrb2HS2Re2wpf08tK3Oux5uQK_43mbRgyEpgk_M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sharpe's Food Market — Processing Guide

> **Source:** Sharpe's Food Market OneGuide (Google Doc `1Me9hKIEFqF58KPq9T4p8y8Zmn60dL0r_HkJ65ZHiRvA`), updated Aug 20, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) | Weekly Flyer (11810) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available From Thursday → Available To Wednesday; Valid From Wednesday → Valid To Thursday.
- **Preview date / linking document:** none.
- **Workflow:** Upload & Setup (Flex) → FQC (DOC).

## Upload & setup (owned by Flex)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP → Confirm & Upload. Pages may need to be added to the SFTP by the processor if the client sends files by email. Auto-Group → Save & Confirm — do NOT Process Internally.
- **Pricing Zone:** create a Base zone, select all pages, Save & Confirm, add all stores.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View; confirm nothing left in the SFTP). Confirm flyer dates. Thumbnails: 4 Standard.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up, social, special weblinks. Box each item with unique prices; box the chocolate promo.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**

## Final QC / go-live (owned by DOC)

- Confirm dates vs PDF and availability toggles; thumbnails include logo.
- Standard checks: items boxed & tagged; spotchecks (20% of pricing zones); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** (owned by DOL): flyer dates, sessions completed, previews correct, items tagged accurately, geography consistent, availability toggles correct.

## Notes

- Black Friday / ad-hoc requests: see the 2025 "Sharpe's Food Market Flipp Operations Guidelines: Publication & Ad-Hoc Requests" doc.

---
*Source: Sharpe's Food Market OneGuide (Google Doc `1Me9hKIEFqF58KPq9T4p8y8Zmn60dL0r_HkJ65ZHiRvA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sheridan Nurseries — Processing Guide

> **Source:** Sheridan Nurseries OneGuide (Google Doc `1WXN0y-diqP2ZGWu1ZVTSW_MsXzlsCN8p3_IXKJqSgR0`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | `#sheridannurseries` |
| Hosted URL | sheridannurseries.com |
| Flyer type(s) | Flyer (10666) |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** 5 days before launch.
- **Cadence:** Available/Valid From Thursday → To Wednesday.
- **Preview date / linking document:** none.
- **Workflow:** Upload & Setup (Vendor) → FQC (Vendor).

## Upload & setup (owned by Vendor)

- Manually upload all pages in the folder matching the flyer valid dates — **ignore the upper-case folder ("2026 FLYERS").** Auto-group → Save and complete.
- Create one pricing zone **Base**, add all stores.
- Overview → Edit Details: dates on PDF match Available & Valid dates; available on all platforms. Thumbnails: Standard 4.
- **Geography Tab: ensure 0 changes to Stores or FSAs.** If there are ANY changes, flag the FT team (continue QC but flag 100% of discrepancies).

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (Box Draw specific). Exclude coupons, packaged deals, retailer logo, sign-up, special weblinks. **Include social media.** Box pictured products separately if they have unique names; use overlapping text boxes for adjacent pricing. Banners do not need to be boxed.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Image selection (risk item):** always select the correct product image when available. **"Lifestyle" images (photos of real flowers/scenery) should be selected if available** — do NOT default to "Do Not Use PDF Images".

## Final QC / go-live (owned by Vendor)

- Confirm dates vs PDF; available everywhere; thumbnails include logo.
- Standard checks: items boxed & tagged; previews clickable; **geography consistent WOW** — immediately flag 100% of discrepancies to the FT Ops team (does not block).
- **Flyer Review type: Lite.**

---
*Source: Sheridan Nurseries OneGuide (Google Doc `1WXN0y-diqP2ZGWu1ZVTSW_MsXzlsCN8p3_IXKJqSgR0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Shop Sante — Processing Guide

> **Source:** Shop Sante OneGuide (Google Doc `1I_MRAhC5D47aGDbyc8edt-PDiS-Ycap_-qQL8vAbkW4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Plus |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) | Flyer |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** ad-hoc.
- **Cadence:** ad-hoc (Available From / To, Valid From / To all ad-hoc).
- **Linking document:** yes.
- **Workflow:** Upload & Setup (Flex) → Image QC (Flex) → FQC (Flex).

## Upload & setup (owned by Flex)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP → Confirm & Upload. Pages may need to be added to the SFTP by the processor if the client sends files by email. Auto-Group (or manual grouping numbers), ensuring correct language. Save & Confirm — do NOT Process Internally.
- **Pricing Zone:** create a Base zone, select all applicable pages, Save & Confirm, add all applicable stores.

### Setup QC
- Confirm all pages uploaded (Pricing Zone Tab → Items View; nothing left in SFTP). Confirm flyer dates. Thumbnails: 4 Standard. Ensure preview dates set.
- **Mass-attach the URL document to all processing steps (Box, Tag, Tag QC).**

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (used for both Box/Tag). Exclude coupons, packaged deals, retailer logo, sign-up, social, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Linking doc required. Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## Final QC / go-live (owned by Flex)

- Confirm dates vs PDF and availability toggles; thumbnails include logo.
- Standard checks: items boxed & tagged; spotchecks (20% of pricing zones); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** — flyer dates, sessions completed, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Shop Sante OneGuide (Google Doc `1I_MRAhC5D47aGDbyc8edt-PDiS-Ycap_-qQL8vAbkW4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Shopper+ — Processing Guide

> **Source:** Shopper+ OneGuide (Google Doc `1WJz0nJ_QVtbqbYIMEGEnFDzM_sc4J3MC6MDWY88TbD4`). Contacts/credentials omitted.

Shopper+ is an **online-only** retailer processed alongside two sibling banners, **Primecables** and **123ink**. There are two flyer types (Weekly and Friday), and the Weekly flyer is **cloned** into four additional versions.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Varies by version — see cloning (some Hosted-only, some Flipp/Distribution-only) |
| Slack channels | `#shopperplus`, `#flex-processingsupport` |
| Hosted URLs | shopperplus.ca · primecables.ca · 123ink.ca |
| Flyer types | **Weekly** (Tue–Tue) with 4 clones (Primecables x2 hosted+app, 123ink x2 hosted+app); **Friday** (Fri–Sun) in 3 versions (Shopper+, Primecables, 123ink) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |
| Linking document | Yes, always |

> **Historical context:** 3 "fake" store locations are set up in FAdmin with large distribution ranges so shoppers in those FSAs are served the flyer — there are no physical storefronts.

## Weekly flyer

- **Files received:** Tuesday (email when files are in). **Cadence:** Available From Tue 9:30 AM, Available To Tue 9:59 AM; Valid From Tue 10:00 AM, Valid To Tue 9:59 AM. **Preview date:** Thursday before go-live (important — enables the preview email). Tue–Tue, no customer preview.
- **Setup (DOC):** upload all page versions/languages to one main Shopper+ run; set page order per the **Pagination doc in the SFTP** (Shopper+ 1–4, Primecables 5–8, 123ink 9–12, Common 13–15). Create two pricing zones (EN / FR) each in correct page order; add all stores to **both**.
- **Setup QC:** dates as above; internal run name = valid dates; preview date Thursday; available everywhere (toggles blank); no external run name; no theme (unless seasonal carousel requested). Thumbnails: standard 4 (1065x600, stock_premium, storefront_carousel_premium, storefront_carousel_organic). **Attach the linking document to all tasks (Mass Attach)** — file `flyer url raw-Flipp_Shopper+WeeklyFlyer[Dates].xlsx` in the SFTP. **If uploading on a Wednesday, file an Urgent Processing ticket.**
- Occasionally a new page 1 arrives to be swapped in on a specific date — leave it out of the pricing zones and set a trigger.

## Friday flyer

- **Files received:** Tuesday (separate email). **Cadence:** Friday 12:00 AM → Sunday 11:59 PM; no preview. Available on **Hosted only**.
- **Setup (Flex):** three separate uploads — one each to the Shopper+, Primecables, and 123ink flyer types; each run gets **only** its own banner's pages (both languages) per the Pagination doc; common pages added where indicated. Two pricing zones (EN / FR), all stores in both.
- **Setup QC:** Friday–Sunday times; internal run name = "Friday + dates"; **Hide on Flipp and Distribution (check toggles); check off Secondary publication**; no external run name; no theme; standard 4 thumbnails; attach linking doc `flyer url raw-Flipp_Shopper+FridayFlyer[Dates].xlsx`.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Linking doc required (used for both Box/Tag). Exclude coupons, packaged deals, retailer logo, sign-up, social. **Include special weblinks** (per linking doc).
- **Tag / Tag QC — Medium; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, **description (tag the PLUS price in the description)**, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** use PDF images wherever possible; cutouts only if the PDF is unavailable or looks bad.
- **URL/Links QC:** Overview → Items Without a URL — generally all items get a link; find missing links in the linking doc and **apply the correct language link (EN/FR)**.

## Final QC / go-live

- Items missing URL: should be none. Leg height 60/40. No item image QC. 4 standard thumbnails. All items QC'd; check tagging on the last 2 pages (known error spot). Pages in correct order per zone; languages set. Sessions ran; vendor tasks complete; **geography same WOW** ("No Stores or FSAs/zips were added or removed"). "Not all categories have thumbnails" and "stores not assigned" warnings can be ignored.
- **Weekly FQC must be done Thursday** so the preview link goes out on time; Flex messages DOC when done.

## Cloning (Weekly flyer only)

After the Shopper+ Weekly flyer is FQC'd and page swaps are completed (typically Monday), make **4 clones** via Overview → Ad Hoc Processing → Clone. Do **not** copy tracking codes/URLs; clone into the prebuilt shell (same "Month + Day" name). For each:

1. **Primecables (Hosted only):** hide on Flipp & Distribution; delete all Shopper+ & 123ink pages — keep only Primecables + Common (~7 pages/zone); rerun sessions; redo FQC.
2. **123ink (Hosted only):** hide on Flipp & Distribution; delete all Shopper+ & Primecables pages — keep only 123ink + Common; rerun; redo FQC.
3. **Primecables (Flipp/Distribution only):** hide on Hosted; keep only Primecables + Common; add all stores to both zones; rerun; redo FQC.
4. **123ink (Flipp/Distribution only):** hide on Hosted; keep only 123ink + Common; add all stores to both zones; rerun; redo FQC.

Then send the retailer the two Hosted-only preview links (Primecables & 123ink, flyer types 10612 / 10613) — verify they load first.

## Flyer review / out-of-processing

- **Flyer Review type: Lite.**
- Post-live page swaps: reviewed Monday (sometimes Friday); a FAB ticket can route swaps to Flex; complete in time to re-clone and re-send previews.

---
*Source: Shopper+ OneGuide (Google Doc `1WJz0nJ_QVtbqbYIMEGEnFDzM_sc4J3MC6MDWY88TbD4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Shoppers Drug Mart / Pharmaprix — Processing Guide

> **Source:** Shoppers Drug Mart / Pharmaprix OneGuide (Google Doc `1TMYtB4aNKGB4YoWCWIN3w5QI6jMuWr3TFFSvAVZ6gmA`), updated Dec 1, 2025. Contacts/credentials omitted.

**Pharmaprix is the Quebec brand for Shoppers Drug Mart (SDM)** — same content, cloned from the SDM run during Pre-FQC (no separate upload) so Quebec users see "Pharmaprix" branding.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#shoppersdrugmart`, `#shoppers-drugmart-amp-prod`, `#loblawops`, `#loblaw-lcl` |
| Flyer type(s) | Weekly (3800) |
| Processing | Auto-stack; Flex Processing Support; Feedel/Strategic Ops **yes**; no coupons |

## Files & schedule

- **Files received:** Tuesday (page PDFs and store distributions come from different sources — see OneGuide).
- **Cadence:** Available From Thursday, Valid From Sunday; Available To Saturday, Valid To Saturday. **2-day consumer preview starting Thursday.**
- **Linking document:** no.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC/Flex).
- **Live-date postal codes:** use **M1B 0A3** for SDM, **G0A 1H0** for Pharmaprix; use an **Ontario pricing zone** for Preview QC.

## Upload & setup (owned by DOC) — two codesheets

### 1. Stores & Pricing Zones
- Download the weekly Store Distribution list (`SDM_StoreZoning_Wk#_202#`), apply a filter to the whole sheet.
- **Delete all "Count" rows** (column J "Version").
- **Rename all "Base" rows to "QC NAT"** — these become the Pharmaprix zones later.
- **Test stores:** filter "Test" and map to regular digital pricing zones using the SDM TEST PZ reference (VLOOKUP the PZ names).
- Download as `.csv` → SDM flyer run → Codesheets tab → upload: Config **`shoppers_drug_mart_stores`**, PDF directory `/`, **all toggles except 2nd and 3rd.**

### 2. Pagination
- Download the weekly Pagination codesheet. Delete Wellwise rows and Store-specific/Grand-Opening (GO) version rows — leave only NAT and QC. Label NAT "National Pagination" and QC "Quebec Pagination"; replace NATIONAL/QUEBEC with "WITH FOOD" / "WITHOUT FOOD" per whether the pagination includes the FOOD page. Delete GO flap tabs.
- Clean each Page Name tab (delete non-page-name columns). In the Wellwise tab keep only **WW 01**.
- Align names to the **Reference Table**: the A1 cell of each Page Name tab (Dates + Page Name — the config reads this cell, not the tab name) and the matching Pagination-tab name must both match. Each page name in the Pagination tab must be followed by a **two-digit** page number (`##`, with leading 0).
- Upload the `.xlsx`: name **`pages`**, Config **`shoppers_drug_mart_pages`**, base path from FTP, **all toggles except 2nd and last.**

### ⚠️ Codesheet error risk items
- **Hidden rows/columns** (should have been deleted by the retailer) make Fadmin read stale data and error on the pages codesheet — check every tab and delete hidden rows/columns carefully.
- Using **"COSMETIC"** from the reference table: Fadmin may read only "COS" and error — switch to a different reference-table word.
- FTP errors: may just be re-flagging previously uploaded Wellwise pages → ignore and Force Processing. Otherwise check the path (no leading/trailing spaces), file names (wrong page/week #, case mismatch — try `WKXX` → `wkxx`), read the error, or escalate to CLSD.
- Ensure all pages uploaded except WW 02, WW 03, and GO. **Upload each page twice — once EN, once FR.** Manually create GO/Store-Specific zones (EN + cross-language FR) if needed.
- **Remove stores from all QC NAT / QC NAT FR zones** (these are the Pharmaprix versions — cloned and re-populated later).

### Setup QC
- Set valid time to start at **3 AM**; remember the 2-day preview from Thursday; confirm valid dates on a Base 01 page (may end Thursday or Friday); ignore the SFTP "pdf pages still present" warning.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, sign-up, special weblinks. **Include retailer logo and social.**
  - **Products without UPC:** draw ONE box around the ad block; do NOT box individual product images.
  - **Products with a UPC:** box each UPC as a separate item (even if same price); include the UPC via a text box; UPC separated by `/` = one box per product; single UPC = box the block.
  - **Do NOT box/tag Wellwise pages** (Home Health Care Solutions / Wellwise logo) — leave blank.
  - Box special call-outs (gift cards, Seniors Day, flu shots, Health & Pharmacy) — look different each week.
- **Tag / Tag QC — High; Auto-tag OFF.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name/Brand:** enter brand (always bolded) in Brand AND Name only if a single brand; if multiple brands, leave Brand blank; keep flyer casing.
  - **SKU:** UPC has **13 digits**.
  - **URLs:** after entering SKU, click Fetch. If Fetch fails, use base URL `https://shop.shoppersdrugmart.ca/Shop/p/BB_` + SKU. If a fetched link leads to the wrong item, search by product name on shoppersdrugmart.ca and match the size (price may differ). If not found, use the home page.
  - **Special sales (custom tagging):**
    - **1 or 2 Day Sale** (yellow background, circle "1/2 DAY SALE"): postfix = the day of the week (regular postfix like "each" goes *before* the day); sale story = the price for the REST OF THE WEEK after the sale.
    - **3 Day Sale** ("3 DAYS ONLY" red banner): valid dates apply to all items; postfix format `each or $X each with N PC Optimum pts`; **leave sale story blank.**
    - **6 Day Sale / Week Long Sale:** these are the flyer's own valid dates — **do NOT enter into valid to/from fields.**
  - **Sale story:** enter as-is; always tag **"PC Optimum"** (not just "Optimum"); free gift → "YOUR FREE GIFT (gift) with the purchase of (item)"; add page-bottom disclaimer if there's an `*`.
  - **Categories:** if more than 4 on a page, leave blank; valid categories = Pharmacy, Personal Care, Food & Beverage, Beauty & Skincare.
  - **Images:** PDF first, then cutouts; if multiple items, use the first item in the name; **do NOT select PDF images with a black background/shadow or that are cut off.**
  - **French flyers: ONLY include French text** (EN and FR are sometimes mixed in name/description).

## Final QC / go-live

- **Do NOT tag week-long or one-day PC Optimum valid dates in the override fields** — leave blank (these are the flyer's dates).
- Mark Autostack Spotcheck complete; finish Ops spotchecks.
- 2-day preview from Thursday; leg heights auto 40/30; no image QC; thumbnails standard 4 starting on the Base 01 logo page (exclude flap pages; adjust start position per zone if page counts vary).
- Apply Two-Day-Only valid dates (yellow-background items) via Item Search / mass edit across the first few pages.
- Storefront spotcheck: confirm skinny flap pages are merged (check a few zones both languages — e.g. ON NAT, AB NAT, QC NAT). Item view: all items boxed (**last WW01 page is NOT boxed — 0 clickable is OK**). Remove stores from QC NAT / QC NAT FR. Geography generally same WOW (1–3 stores added/missing OK).
- FQC checklist: "Not all PZs have Stores Assigned" → write "SDM only"; click Complete twice to force save past errors. Check flyer sorting. Message DOC when FQC is complete so they can clone.

## Pharmaprix clone (owned by DOC)

- Clone the SDM run into the same-week Pharmaprix run (start early — large run). Recheck thumbnails and page merges.
- **Only QC zones get stores assigned** (these are the Pharmaprix zones): from the uploaded store list, filter column J to QC NAT, paste to a new tab, download as `.csv`, re-upload the stores codesheet (Config `shoppers_drug_mart_stores`, `/`, all toggles but 2nd & 3rd), re-run.
- Confirm only QC zones have stores; check geography (same as prior weeks); recheck previews (may need the Touch Storefront Objects custom action on 404); re-run lagging sessions.
- FQC as normal: "Not all PZs have Stores Assigned" → write "PHX only"; click Complete twice.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Shoppers Drug Mart / Pharmaprix OneGuide (Google Doc `1TMYtB4aNKGB4YoWCWIN3w5QI6jMuWr3TFFSvAVZ6gmA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Shoppers (SuperValu) — Processing Guide

> **Source:** Shoppers (SuperValu) OneGuide (Google Doc `1va8K8acYuieM_ay1401jB6E4AES06ivBwwGnGlkn_b4`), updated Apr 28, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Hosted URL | shoppersfood.com |
| Flyer type(s) | Weekly |
| Processing | Auto-stack; Flex Flyer Review; OS Setup; Feedel/Strategic Ops **yes**; no coupons |

## Files & schedule

- **Files received:** Thursday (assets normally arrive ~2 weeks in advance).
- **Cadence:** Available From Wednesday → Available To Wednesday; Valid From Thursday → Valid To Wednesday (available 1 day before valid).
- **Preview:** 1-day preview; go live Wednesday.
- **Linking document:** no.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).
- Keep the **Shoppers URL tracker** updated with correct dates and the flyer run link/ID.

## Upload & setup

- **Codesheet upload:** download the DIG version list `.xlsx` for the week; import into Google Sheets and download the first page as a `.csv`. Upload with **Config `farm_fresh_supermarkets`**, PDF base directory = week's FTP path, **all toggles checked except the 2nd toggle.**
- Mark Flyer Creation complete — stores are added automatically from the `.csv`. Run Setup QC to activate Box Draw.
- Overview → Edit Details: **no theme; Hide in Distribution, Flipp, and Hosted** (toggles); internal run name = `WK #`; **external run name = "Weekly Savings"**; leg heights preset 55/45; thumbnails Standard 4.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (Box Draw specific). Exclude coupons, packaged deals. **Include retailer logo, sign-up, social, special weblinks.** Box all items separately (anything with a price gets a box); use text boxes when needed. Box coupons cleanly including the perforated edges.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-select ON.** Include name, description, price, sale story, categories, disclaimer, original price. **Include SKU and URLs per overview, but this merchant has no SKU or URL** (N/A). **Exclude pre/postfix and valid dates** (enter valid override dates only if applicable). **Always include Category.** Tag brand, names, sale story, prefix/current price/postfix/original price, and discount **as-is in the flyer.**
- **Image QC:** always choose the most relevant & cleanest image.

## Final QC / go-live (owned by DOC)

- Spot checks: relatively low — use judgment (name, offers, valid dates).
- Leg heights 55/45; thumbnails standard 4.
- Item image QC: PDF > cutout, but select cutout if meat/seafood is not packaged.
- Categories: **no categories on page 1; all other pages should have at least "grocery".**
- Key message "Grocery Savings"; external run name "Weekly Savings"; available 1 day before valid.
- **Flyer Review type: Lite.**

## Out-of-processing — Digital Inserts

- You may get an email indicating a **digital insert** with the file and position. Inserts usually arrive as JPG → convert to PDF before uploading (page size "Fit").
- Upload the digital ad — **no linking, boxing, or tasks required.** Almost always **position 2** of the ad (confirm in the email).
- **Create a trigger to remove the digital insert** for the requested timeframe: Pages → Layout → take out (digital insert) → All Flyers → Run as a trigger → OK.

---
*Source: Shoppers (SuperValu) OneGuide (Google Doc `1va8K8acYuieM_ay1401jB6E4AES06ivBwwGnGlkn_b4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Showcase US / Showcase (CAD) — Processing Guide

> **Source:** Showcase OneGuide (Google Doc `1jXmafS1ukJMBMqCdpWOnWn7KzRIVUnuCuHiwx4m_kQE`), updated May 2, 2024. Contacts/credentials omitted.

Two merchant instances processed the same way: **Showcase (Canada)** and **Showcase US**. Each has its own files, UTM document, and FTP.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Hosted URLs | shopatshowcaseusa.com/pages/flyer · ca.shopatshowcase.com/pages/flyer |
| Publication | Both CAN & USA; live Monday–Sunday (2–3 pages US, 4–6 pages CAD) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |
| Linking document | Yes |
| Account guide | Confluence "Showcase CAN + US Account Guide" |

## Files & schedule

- **Files received:** Friday, variable times — **normally very short lead time; we push back go-live if delayed.**
- **Cadence:** Available/Valid From Monday → To Sunday.

## Upload & setup (owned by Flex)

- Pages are in the FTP (folder specifies date). **Select the correct files per instance:**
  - **Showcase Merchant** = Canadian → choose files that do **not** contain "USA" in the name.
  - **Showcase US Merchant** → choose the USA files.
  - In both, pick the PDFs numbered page 1, 2, etc.
- Auto-group pages, verify indexing. Create **one** pricing zone named **Base** (only one zone for this publication). Assign all stores.
- **Dates:** the flyer shows "Valid Until" with no start date — **the start date is always the Monday before.**
- **UTM linking doc:** from the FTP, download the file with "UTM" in the name (matching CAN or USA). One manipulation: copy the "Hyperlink w/ UTM" column → Paste Special → **Values Only** into the URL column; delete columns C and D — leaving only the UTM URLs. Download as XLS and attach to all vendor tasks. Mark Setup QC complete.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (Tag specific). Exclude coupons, packaged deals. **Include retailer logo, sign-up, social, special weblinks.** Box items as they appear; use text boxes where needed; **box the banners at the bottom of every page and store-location pages** (links in the linking spreadsheet); box the retailer's logo on each page.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-select ON.** Include brand, name, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix, valid dates, SKU.**
  - **Name/Brand:** tag as in the flyer; if the name is inside the product image and text extraction misses it, type it in full (e.g. "GOLI" → "GOLI APPLE CIDER VINEGAR GUMMIES").
  - **Price / pre-postfix:** **do NOT tag "% off" or "$ off" as pre/postfix — those are the sale story.** Only words like "only" or "pre-order" in the red box are pre/postfix.
  - **Sale Story:** tag the "% off" / "$ off" amounts (red boxes) here.
  - **Valid dates:** tag only if the item has separate valid dates.
  - **URLs:** use all URLs in the provided document. If no banner link is provided: **Showcase CAN** → `https://www.shopatshowcasecanada.com/`; **Showcase US** → the US fallback link in the OneGuide.
- **Image QC:** select the cleanest PDF image without a black background; otherwise use the cutout ("Do not use PDF Image").
- **Spotchecks:** usually "spelling error" flags on brand names — confirm spelling in the PDF.

## Final QC / go-live (owned by DOC)

- Check all items have a URL (find missing links in the linking doc).
- Standard thumbnail QC; Edit Details: no external run name, apply No Theme; all stores added (check geo); available on all platforms.
- **Flyer Review type: Lite** — valid dates from bottom of pages; available-from is ad-hoc (may be after valid-from due to late files); available-to matches valid-to; sales story dates on every page; everything boxed is tagged; page categories set; previews clickable; sessions run; vendor tasks complete; geography consistent.

---
*Source: Showcase OneGuide (Google Doc `1jXmafS1ukJMBMqCdpWOnWn7KzRIVUnuCuHiwx4m_kQE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sklar Peppler — Processing Guide

> **Source:** Sklar Peppler OneGuide (Google Doc `1tmSHI_PE5Nl5qJw-MI43XPVwphScr6TFCa8RRb_SHVc`), updated Jul 22, 2024. Contacts/credentials omitted.

Simple retailer — no special risk items; use generic flyer review standards.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Flyer type(s) | Weekly (published monthly) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |

## Files & schedule

- **Files received:** ad-hoc, **via email.**
- **Publication cadence:** monthly.
- **Preview date / linking document:** none.
- **Workflow:** Upload & Setup (Flex) → FQC (Flex).

## Upload & setup (owned by Flex)

- Files sent via email.
- **One zone, English, containing all pages and assigned all stores.**
- Confirm all items in the Setup QC checklist.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Exclude coupons, packaged deals, retailer logo, sign-up, social, special weblinks. **Box all items separately; use text boxes only if necessary.**
- **Tag / Tag QC — Low; Auto-tag OFF.** Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude brand and valid dates.**

## Final QC / go-live (owned by Flex)

- **No special risk items — use generic flyer review standards and instructions.**
- **Flyer Review type: Lite.**

---
*Source: Sklar Peppler OneGuide (Google Doc `1tmSHI_PE5Nl5qJw-MI43XPVwphScr6TFCa8RRb_SHVc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Slumberland — Processing Guide

> **Source:** Slumberland OneGuide (Google Doc `1pP1_CCSb2Paqok-WKk0Bm89UFJuzinCsMaithB1XeR4`), updated May 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#slumberland` |
| Hosted URL | slumberland.com |
| Flyer type(s) & cadence | Flyer (type #791) — ad-hoc; Available/Valid From Sunday, Available/Valid To Saturday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

## Files & schedule

- **When files arrive:** ad-hoc.
- **Publication cadence:** Available From / Valid From = Sunday; Available To / Valid To = Saturday.
- **Preview date:** set the Friday before go-live (2 days before go-live).

## Upload & setup (owned by Flex)

- **If a codesheet is provided (from FTP):** use the **[Master]** tab — Column A = first letter of the file names (change on the codesheet if it doesn't match before uploading); Column B = store code (assigns those stores to the base pricing zone). Save as CSV.
  - Always **1 pricing zone created**, but store assignments vary week-over-week.
- **If NO codesheet (manual upload):** **[Pages]** → manually upload pages and create a base pricing zone. **[Add All]** stores to the base pricing zone, then use the **[Geography]** tab to check which new stores (shown in green) were added and remove them from the base pricing zone.
- **[Overview] → [Edit Details]:** Available everywhere; Key Message from front page; External run name = same as KM; Preview date = Friday before go-live; **no theme**.
- Thumbnails: Standard 4. Spotlights: QC Key Message.
- **Setup QC:** check date on bottom of last page (only end date shows — start date is always the Sunday before).

### ⚠️ Common errors (retailer-specific)

- Codesheet "store not found" error → likely a new store; add manually to FAdmin.
- "Not all files uploaded" error at Setup QC → **safe to ignore as long as you've checked the FTP.**
- At Final QC, "slicing not checked" error → write "slicing checked" in notes; **[Force Mark Complete]** if it occurs, otherwise you won't be able to access the preview.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** packaged deals (e.g. washers/dryers); **exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs; exclude disclaimer. Include brand + size in the name. URLs provided in separate linking docs (EN & FR). Categories are typically Living Room, Bedroom, Dining Room, Beds and Mattresses.
- **Image QC:** prefer clean PDF image; cutouts otherwise.

## Post-processing / Final QC (owned by DOC)

- Ledge Heights: 40/30.
- Confirm all items boxed — all SKUs, all logos, event callouts (tag as item + disclaimer if applicable).
- **Check links** (search SKUs on website for any missing): Slumberland home, "No interest/financing", Free Shipping, Mattress category, "120 Night", Price Match, Financing Terms disclaimer (bottom of last page), and social links (Facebook, Pinterest, Twitter, Instagram, YouTube).
- **[Pages] → [Categories]:** skip page 1, 1–3 per page. Use **[Beds/mattresses]** for a mattress or bed frame vs. **[Bedroom]** for bedroom sets. Then **[Draw Category Thumbnails]**.
- **[Manage Tracking Codes]:** mmdd = the available-from date. Code #1: source [All], var `utm`, value `WEB_AD_FLIPP_yyyymmdd`. Code #2: source [Mobile], var `utm`, value `WEB_MOB_AD_FLIPP_yyyymmdd`. Then **[Apply All Tracking Codes]**.
- Verify **[Sessions]** URL, horizontal & vertical previews, then run Final QC pipeline (available everywhere).

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing

- **Weekly preview links** (sent Friday before): Hosted preview, Vertical preview, and Direct link (direct link won't work until ads are live) — see the OneGuide for the exact URL construction.
- **Multi-week "Memorial Day"-style events:** new pages are inserted on the Sunday of each week — file an After-Hour Trigger Check ticket. Manually upload the new pages; verify no stores added/removed against the prior week's codesheet; update preview date; after OS boxes/tags, redo page categories (skip page 1), redraw category thumbnails, check missing links, check **[Sessions]**, set the trigger to place new pages in positions 1–4, and create OPTICS trigger-check tickets (Ops + After-Hours).
  - **Note:** a specific store (e.g. Batavia) may be on hold — do not include it in the base pricing zone until cleared.
- **After the trigger runs:** confirm pages inserted into positions 1–4, redraw thumbnails (Standard 4), delete old tracking codes and create new ones (Apply All), re-generate Data-Piping Groups, toggle the Auto-Stack spotcheck Incomplete→Complete, check **[Sessions]**, verify live on slumberland.com and the Flipp app, then close the OPTICS tickets.

---
*Source: Slumberland OneGuide (Google Doc `1pP1_CCSb2Paqok-WKk0Bm89UFJuzinCsMaithB1XeR4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Smart & Final — Processing Guide

> **Source:** Smart & Final OneGuide (Google Doc `1L8G-SxRyPXwjSsRG5as3y6Wv-74iWO9-TbKoqveJDa4`), updated May 14, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#smartandfinal` |
| Hosted URL | smartandfinal.com/flyers |
| Flyer type(s) & cadence | **Weekly** (type 7853) — receives 2 versions weekly (5-day Wed–Sun + 2-day Mon–Tue); **Business Mailer / Business Saver** (type 8004) — biweekly |
| Processing | Auto-stack; Flex (FAB tickets); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> **Note on timezone:** FAdmin runs on EST; Smart & Final is California-based (PST). All valid-from times must be set to **3 AM** so flyers go live at the correct local time.

## Files & schedule

- **When files arrive:** Monday (weekly codesheet/version list + PDF via email). Interstitial pages ("inserts") arrive Friday/Monday for the flyer going live Tuesday.
- **Weekly cadence:** Available From Tuesday, Valid From Wednesday; Available To Monday, Valid To Tuesday.
- **Consumer preview:** the **2-day sale has a consumer preview; the 5-day sale does not.**

## Upload & setup — Weekly (owned by DOC)

1. Download files from the emailed link and upload to the SFTP. Confirm the codesheet (`.xlsx`) is attached and added to the SFTP.
2. **Codesheet manipulations:** open the **ad recap** tab → delete column A entirely → ensure "In store version" is in column F (move it there if needed) → change "Store No" to "Store #" → unhide any hidden rows/columns → save as **Excel 97-2003 (.xls)**.
3. **Upload codesheet:** name = Week # (e.g. "Week 35"); **config `smart_and_final`**; path taken from the directory; **select all toggles EXCEPT combine zones and region assignment** (exclude #2 and #7).
4. Wait for sessions. **Edit Details:** no theme; toggle **Hidden in Hosted**; set **valid-from = 3 AM**.
5. Leg heights preset 50x25; Standard 4 thumbnails; Setup QC checklist.

### ⚠️ Common errors (retailer-specific)

- **Files arrive early, linking doc arrives a day later.** Either upload files with a vendor note "Linking doc to be attached EOD Tuesday" so OS can start boxing, or wait for all assets.
- **PZ mismatch:** ensure PZ in column F (ad recap tab) matches PZ in the version list tab. For the 2-day vs 5-day flyer you usually need to add **"D"** to the 5-day PZs.
- **Store 350 PZ** often reads `A!NV` but should be `A1NV`.
- Warning *"Version Code A1 not found in first tab for Store 304"* → 5-day steal page 1s have a "D" suffix; add a D to all zones in the Ad Recap "column F – Instore version" so Ad Recap col F matches Version List col A.
- Codesheet errors are usually page name / stray zones: match the codesheet page names to the PDF names in the FTP; delete version-list rows for missing stores the retailer forgot to remove; confirm all pages uploaded to FTP.
- Error *"Could not find file Spreads with …CIR02_C_A1.pdf"* → "Spreads with" sits in column J of the Version List tab (a wide page 2). Remove column J entirely, then rename the Page 4 header to Page 3.
- **Pipeline often gets stuck at Tag QC** — monitor throughout the week.

## Upload & setup — Business Mailer (owned by DOC)

- **Manual upload.** Flyer type: Business Savings (8004). Internal run name: "Business Card WK 1/2". Add all pages (usually 2–8) → Autogroup → Save.
- Create 1–3 pricing zones; add stores using the **generic store codesheet**: from the S&F codesheet, column E = stores → generic column A; column K = PZ name → generic column B (label "Base" if all rows share one name). Download as CSV and upload via FAdmin.
- **Edit Details:** no theme; Hidden in Hosted; valid-from = 3 AM. Leg heights 50x25; Standard 4 thumbnails.

## QC specifics

- **Box Draw (Medium; Auto-Box ON, Box QC bot ON; PDF image auto-selection ON):** include coupons, packaged deals, sign-up page, social media, special weblinks; **exclude retailer logo.** Box all email signup / delivery banners; box & tag the four social icons (Facebook, Twitter, Instagram, Pinterest) separately; box ".com" and phone-number call-outs (usually bottom of last page) and promotional banners. (Business Mailer additionally requires a Box Draw linking document.)
- **Tag / Tag QC (Medium; Auto-tag OFF):** Weekly **excludes SKU and URLs**; Business Mailer **includes SKU** (linking doc required). 
  - **Name/Brand:** one brand → Brand field; multiple brands → leave Brand blank. Name = full product name **excluding sizes**.
  - **Description:** include sizes and text like "Selected Varieties." **If the item has a digital coupon, prefix the description with "with Digital Coupon Savings."**
  - **Price:** larger number = Price, smaller = Original Price.
  - **Pound offers:** do NOT use "3 LBS FOR" prefixes — divide price by pounds, use postfix **LB**, add the sale to the disclaimer.
  - **Disclaimer:** add the day of week if the valid date differs (e.g. "Wednesday Only"). "Buy 4 & Save 4"-type callouts must go fully in the **disclaimer** field (not sale story) for every item under the banner; full text is usually on the last page.
- **Image QC:** prioritize clean PDF images; cutout when not clean (no dark shadows around the image).

## Inserts / interstitial pages (Weekly)

- Sent Monday before go-live via email; placed **after page 1 in positions 2 and 3** in the order listed.
- Download and upload manually; change the conversion library to **ghostscript 9.06** gamma (fixes weird text).
- One box covering the entire page; Display Type: Link; Name = CTA "Shop Now, Save Now"; Link provided in email (blank URL is OK if none given).
- **⚠️ Ensure inserts don't auto-merge to page 1 or other pages** — check each zone via [Pricing Zones] → storefront spotcheck.

## Final QC (owned by DOC)

- **Weekly:** confirm every digital-coupon item has "With Digital Coupon Savings" at the start of the description (identify via the "Weekly Digital Deals" blue background / dotted border on page 1–2; note the same item can have different names, so QA each page). Confirm "Buy 4 Save 4" callouts are in the disclaimer field. Check Pages, Pricing Zone, Sessions, Vendors, Geography tabs. **Ensure valid-from time is 3 AM.**
- **Business Mailer:** mark auto-stack spotcheck complete; check Pages/Pricing Zone/Sessions/Vendors/Geography; run FQC checklist.

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing

- Page swaps follow the baseline page-swap process.
- **Discontinued — Offer ID (A2C):** historically Offer IDs were tagged in the SKU field (one Offer ID per item; match the Offer-ID prefix to the page name — "COVER" = page 1, "BACK" = page 2). Only performed if 200+ SKUs were missing; otherwise re-run tag/tag QC with a vendor note to fill missing SKUs.

---
*Source: Smart & Final OneGuide (Google Doc `1L8G-SxRyPXwjSsRG5as3y6Wv-74iWO9-TbKoqveJDa4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Smiths Furniture and Appliances — Processing Guide

> **Source:** Smiths Furniture and Appliances OneGuide (Google Doc `1tkcRT-s5aEqy8bKS-UhsNjGQ8jzUVF58YXf2pFc2TbA`), updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#1p_smiths-furniture` |
| Hosted URL | (not specified in OneGuide) |
| Flyer type(s) & cadence | Flyer (type #12154) — ad-hoc |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel. Processing largely owned by DOC. |

## Files & schedule

- **When files arrive:** ad-hoc (available/valid dates all ad-hoc).
- No linking document.
- Pages may need to be added to the SFTP by the processor if the client sends files over email.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → auto-group to fill the Grouping Number field (ensure the correct language is selected) → Save & Confirm. **Do NOT process internally.**
- **Pricing zone:** create a Base pricing zone, select all applicable pages, Save & Confirm, then add all applicable stores.

### ⚠️ Common errors / risk items (retailer-specific)

- **Setup QC — confirm all pages uploaded:** Pricing Zone tab → Items View. If uploading from SFTP, confirm no pages remain in the SFTP that were not uploaded.
- Confirm flyer dates from the bottom of the first flyer page.
- Watch for multiple products in a single block during tagging.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc required):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU and URLs.** Brand used for both Box and Tag.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## Final QC (owned by DOC)

- Confirm dates (per PDF) and availability toggles.
- Thumbnails correct and include the retailer logo.
- All items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed accurately; geography correct.

## Flyer review

- **Flyer Review Type: Lite** (owned by DOL): flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Smiths Furniture and Appliances OneGuide (Google Doc `1tkcRT-s5aEqy8bKS-UhsNjGQ8jzUVF58YXf2pFc2TbA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sobeys Liquor Banners — Processing Guide

> **Source:** Sobeys Liquor Banners OneGuide (Google Doc `1AwI1snaXw2jYKC0iSqDyLzygPYK-c-1Yk9TkY6Bc1Vk`), updated Mar 27, 2026. Contacts/credentials omitted.

> Covers the liquor banners processed together — **Sobeys Liquor** and **Sobeys/Safeway Liquor** (the latter cloned from Sobeys Liquor). Related banners in the shared vendor guide: Thrifty Foods Liquor, Safeway Liquor.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#sobeys` |
| Hosted URL | (not specified in OneGuide) |
| Flyer type(s) & cadence | Weekly. Available From Wednesday, Valid From Thursday; Available To / Valid To Wednesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); **OS completes coupon processing**; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Tuesday (Excel file on FTP + distribution file via email).
- Review recap files each week for **new stores** — add them properly and flag any unfamiliar/new stores in the channel.

## Upload & setup (Vendor → Flex)

1. Download the week's Excel file from FTP; **manual page upload** using the Excel as reference; confirm all pages uploaded to FTP.
2. **Create pricing zones; add all stores** (Sobeys Liquor and Sobeys/Safeway Liquor). For **Sobeys/Safeway Liquor do NOT add SK stores.**
3. Download the week's distribution from email; create a **generic code sheet** for Sobeys/Safeway Liquor stores; upload the code sheet.
4. Edit details; QC thumbnails (Standard 4 + thumbnail + `first_page_thumbnail_400w`); box Scene+ callouts (usually page 1); check sessions; Setup QC; auto-stack spotcheck; mark vendors to High.

### ⚠️ Common errors / risk items (retailer-specific)

- **Codesheet column rules (critical):**
  - Any column containing **W6** is exclusive to Alberta and applies **only to Sobeys/Safeway Liquor**.
  - **W4 – SK Base** is designated for **Sobeys Liquor**; the **W4 Clone** is for Sobeys/Safeway Liquor. **Do NOT include W4 – SK Base in the regular weekly Sobeys/Safeway runs.**
- **Special item dates:** always scan the PDF for items with promotional start/end dates that differ from the flyer dates and set the item's valid-from/to to match the PDF.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** include coupons, retailer logo, sign-up page, social media, special weblinks; **exclude packaged deals.** Box all items attached to a price (include as much of the image as possible); multiple items sharing one price go in one box; delete duplicate/overlapping boxes. The bottom callout does **not** need to be boxed.
- **Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc required; PDF image auto-selection ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Brand & Name:** enter brand in the Brand field AND at the start of the Name field.
  - **Disclaimer:** always include (e.g. "Limit of Two", "For limited time only").
  - **Dollars off / percent off:** only if explicitly stated. Do **not** put "Save $X" amounts in the Dollars Off field when savings are conditional on buying multiple items.
  - **Scene+ tagging:** individual item "Scene+" → put in **Sale Story**; "with Scene+ card" → put in **Postfix**. Flyer-level Scene+ callouts (usually wine, e.g. "BUY ANY 6 BOTTLES … GET 250 PTS") go in the Postfix with "MIX & MATCH" in the Sale Story after "Save $". **Individual item callouts take priority over the flyer-level callout.**
- **Image QC:** select a PDF-extracted or composite image where available; clean images for all items.

## Post-processing / Final QC (owned by DOC)

- Tag page categories during box draw (at least one category); ensure Scene+ items are tagged.
- **Sobeys Liquor FQC:** upload inserts (see Insert Tracker + insert-process video), box & tag inserts, confirm Scene+ tagging, no overlapping boxes, check sessions, mark vendor tasks complete, Final QC.
- **Then clone Sobeys Liquor → Sobeys/Safeway Liquor banner:** add all stores under SK, add key messages, Final QC.
- Where AIR MILES appears in older videos, it is now **Scene+**.
- **New process:** on the Jira ticket, add a note to send the preview URLs to the retailer once FQC is complete. External run name for all banners: "Weekly Flyer".

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Sobeys Liquor Banners OneGuide (Google Doc `1AwI1snaXw2jYKC0iSqDyLzygPYK-c-1Yk9TkY6Bc1Vk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sobeys Urban Fresh — Processing Guide

> **Source:** Sobeys Urban Fresh OneGuide (Google Doc `1hZjFwxtu5HDNS_STO1nqRPNi_3zSzc-puy95h05uv7I`), updated Aug 11, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 1 Premium (relationship quality: Excellent) |
| Availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeysops`, `#3flf-sobeys`, `#sobeys-dataservices` |
| Flyer type(s) & cadence | Weekly. Available From Wednesday, Valid From Thursday; Available To / Valid To Wednesday. Preview Monday |
| Processing | Auto-stack; Flex (3FL); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

## Files & schedule

- **When files arrive:** Thursday or Friday (flyer goes live Wednesday, 1-day preview Tuesday). Distribution list arrives by email.
- **⚠️ Double-check that the flyer dates match the shell** — if the shell dates are wrong, update the shell to match the PDF.
- Flyer is uploaded manually. There is a codesheet on the SFTP for page/pricing-zone assignments: `URBAN_FRESH_WK#_Code_Sheet.xlsx`. The store list ("Zone Summary") is emailed each week.
- DOC: update the Vendor Assigned Tasks (VAST) tracker and upload the zone-summary document to the Urban Fresh folder; review upload Friday mornings.

## Upload & setup (owned by Vendor)

- **⚠️ Upload ALL files with the current week's path** — even if a page is named "SOBEYS" instead of "UF", it must be uploaded and added to pricing zones. Refer to the Code Sheet when in doubt.
- **Manual upload:** in the SFTP select ONTARIO > URBAN FRESH > that week's files; select ALL files (UF/Sobeys) → Select Files → set the grouping to match the page order in the Code Sheet → Save and Complete.
- **Pricing zones:** use the print code sheet to determine how many zones to create. **Name them exactly "Zone 1" and "Zone 2"** — no all-caps, not "Run", not "ZONE" (only "Zone 1"/"Zone 2" are accepted by the retailer, even if the docs say "Run").
  - **One pricing zone:** add the `[Sobeys Urban Fresh]` store set.
  - **More than one:** add stores using the zone summary emailed on Wednesdays.
- Check the SFTP to confirm all files uploaded.

### Setup QC (owned by Vendor)

- **Edit Details:** External Run Name = "Weekly eFlyer"; no theme; Key Messages — Long: "Weekly Ad. Weekly Savings.", Short: "Weekly Ad." (enter the key message via show/hide rarely-used-fields).
- **QC Thumbnails (1065x600):** remove white border, focus on pg 1, wrap pages and pg 2. Then: **stock premium** (all base/flyers, apply positioning — focus pg 1), **storefront carousel premium** (pg 1&2 + wrap pages), **storefront carousel organic** (pg 1), **thumbnail** (pg 1&2 + wrap pages), and **fpt_400w** (pg 1). Save and exit.
- **⚠️ [NEW] Merge the two skinny FL pages:** Pages → for each pricing zone open Storefront Spotcheck and press **Merge** on FL01; scroll the preview to confirm FL01 and FL02 are side-by-side.
- Set Vendors priority to **High** (short turnaround). After sessions run, complete the Setup QC checklist. Mark the Autostack spotcheck complete (this completes the auto-publish task for vertical preview at FQC).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** include retailer logo and the Scene+ banner (bottom); exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box all items with prices (text boxes when necessary).
- **Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs; **exclude disclaimer** (except the Scene+ note below). Brand only in the brand field — do not double it in the name.
  - **Sale Story / Scene+:** every offer with an accompanying Scene+ offer must have **"Scene+" tagged in the Sale Story** — including offers that only show points earned (no literal "Scene+" text).
  - **KG/LB:** the **/lb price is the main price** with "lb" as postfix; the **kg price goes in the Description** for all produce, meat and seafood items.
  - **Disclaimer:** add the "$$$ without Scene+ Card" callout in the disclaimer.
  - **Categories:** include the most relevant category; Scene+ items also need the Scene+ category.
- **Image QC:** no longer needed for the FLEX team. When done: clean white-background PDF preferred, cutout otherwise; use the first/best product image where multiple exist; no black shadows; text cutout OK when no item image exists; **for banners, do not select a PDF image.**

## Post-processing / Final QC (owned by Vendor)

- **Legibility Heights:** Scan Mode 40, Read Mode 35.
- **QC Categories** (rule of thumb by department — meat/seafood: fresh/raw; deli: cooked/sliced meat/fresh pizza; produce: veggies/salad mix; grocery: everything + frozen veg/fruit + canned tuna; bakery: fresh baked goods; hard cheese: cheese; cream cheese: dairy; no category for direct links). Ensure all Scene+ items have the Scene+ category.
- **Page categories:** every page gets **Scene+ and Grocery** (type on page 1, copy to all pages), then add all remaining categories per page.
- **Scene+ check:** Item Search → Sale Story contains "PTS" (ensure Scene+ tagged); Disclaimer contains "Scene" (ensure it's the "without Scene+ card" price).
- **LB check:** Item Search → Postfix contains "lb" (main price is /lb; kg price in description).
- Do horizontal + vertical previews (EN), check insert links, confirm everything boxed; Pages tab — first two numbers green and matching; Sessions all green (PDF Image Auto Selection may be yellow). Run FQC checklist (the "some categories do not have thumbnails" error can be ignored).

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing — Inserts (updated Mondays)

- Check the Sobeys Insert Tracker for the date/banner. Pages → Edit → find insert pages in ONTARIO > URBAN FRESH > URBAN FRESH INSERTS; select the inserts → Save and Complete.
- When Box Draw becomes available, draw one box around each insert page (complete & next, repeat); tag with the link from the Insert Tracker; complete outstanding vendor tasks. If the inserts match the prior week, Copy Items from the previous flyer run.
- Insert pages into the run: Pricing Zones → pencil tool → add page → select all → arrange per the tracker → Save and Done (repeat for **each** pricing zone).
- **Submit an OPTICS ticket** (OPSMR board) for Urban Fresh: summary "[Due DD/MM EOD] Urban Fresh Inserts" (due the day before go-live), type Page Inserts/Removal, description = run URL + Insert Tracker screenshot, merchant Sobeys, assign then move to Lead Review.

---
*Source: Sobeys Urban Fresh OneGuide (Google Doc `1hZjFwxtu5HDNS_STO1nqRPNi_3zSzc-puy95h05uv7I`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sobeys Wholesale (West & Atlantic) — Processing Guide

> **Source:** Sobeys Wholesale (West & Atlantic) OneGuide (Google Doc `1Z38JDSimxlCQS2ypNnOiyBH1kgOWJGlujgVfxfpCB7Q`), updated Oct 20, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium (S1C1) |
| Availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeysops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URL | sobeyswholesale.com/en |
| Flyer type(s) & cadence | Sobeys Wholesale — **Monthly**, ad-hoc files. Available From Wednesday (**3 AM for West only**), Valid From Wednesday; Available To Thursday (**3 AM for West only**), Valid To Tuesday. Preview Monday |
| Processing | Auto-stack; no Flex; no OS; no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> The process is the **same for West and Atlantic**; the two regions differ only by files, stores, and (for West) the 3 AM availability times.

## Files & schedule

- **When files arrive:** ad-hoc (monthly cadence). Codesheet/PDFs come from the merchant ops contact (credentials in the OneGuide — not stored here).

## Upload & setup (owned by DOC)

1. In the month's flyer run, **manually upload pages** (Pages → Edit): **West** → Wpg files; **ATL** → Atl files. Save and Complete.
2. Flyer Creation → create a **"base" pricing zone**.
3. **Add stores:** **West** → store 5557; **ATL** → all other stores (5 stores) — **do NOT include 5557.**
4. **[Overview] → [Edit Details]:** for **West only**, Avail/Valid From = 3 AM; Hidden in Hosted; **External run name = "Sobeys Wholesale mm/dd – mm/dd"** (valid from/to dates); no theme.
5. Thumbnails: Standard 4 + Thumbnail + 400W. Ledge Heights: 50/40. Setup QC checklist → mark complete. Vendor Tasks → High.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** include retailer logo; exclude coupons and packaged deals. All items boxed and tagged individually.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, description, price, sale story, categories, disclaimer, original price; **exclude valid dates, SKU, URLs.** Brand used for both Box and Tag.
  - **Disclaimer (all items):** "Prices and promotions are only available at Sobeys Wholesale locations."
  - Example tagging: Prefix "3 for", Current Price "0.89", Postfix "When you buy in multiples of 3".
- **Image QC:** pick the cleanest image; cutout if no clean image. Do **not** use PDF images when there are lifestyle shots (product on a cutting board/plate) or too many shadows/black outlines.

## Post-processing / Final QC (owned by DOC)

- **Item Category QC:** one category per item, best judgement. **Note: there are no Scene+ categories, so skip adding Scene+.**
- **Final QC:** **add the disclaimer to all items** ("Prices and promotions are only available at Sobeys Wholesale locations.") via Item Search → Apply Filters → Select All → Multi Edit Items → add disclaimer → Save Changes. Then run the standard FQC checklist.

## Flyer review

- **Flyer Review Type: Lite** (owned by DOL).

---
*Source: Sobeys Wholesale (West & Atlantic) OneGuide (Google Doc `1Z38JDSimxlCQS2ypNnOiyBH1kgOWJGlujgVfxfpCB7Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Source Office Furnishings — Processing Guide

> **Source:** Source Office Furnishings OneGuide (Google Doc `1QtAzcD3PaHDEVdF-A2HISPc4ZkXNPfCRaiHOBPdyM3s`), updated Oct 9, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Hosted URL | (not specified in OneGuide) |
| Flyer type(s) & cadence | Flyer (type 10434) — **monthly**, ad-hoc files. Usually first of the month to last of the month |
| Processing | Auto-stack; Flex (some tasks + Flyer Review); OS (upload); no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** ad-hoc; retailer submits via FTP.
- **Publication cadence:** Available/Valid From = 1st of the month; Available/Valid To = last day of the month (1-month run).
- **Preview date:** set for **5 days after files have been received**.
- **Linking Document:** yes — all items receive product links + CTA.

## Upload & setup

- **Vendor setup (Flex):** confirm files received via FTP; mark the run ready for OS upload in the Vendor Setup & Setup QC Tracker.
- **Upload:** Manual Upload → Pages → Edit → select PDFs from FTP → Upload → Auto Group → Save & Complete. Flyer Creation → 1 Pricing Zone (Base) → Save & Done → Pricing Zones → Add All Stores.
- **Setup QC (Flex):** Edit Details — Available/Valid From = 1st of month, Available/Valid To = last day; all platforms; Preview = 5 days after files received; Internal Run Name = month; External Run Name = none; no theme. Thumbnail QC: Standard 4 (1065x600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, storefront carousel organic – 1pg). Confirm sessions ran; no geo changes; complete checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **Linking sheet must be on all vendor tasks.** Download the link sheet `.xlsx` from the SFTP and add it to "Vendor Box Draw" via the Mass Attachment checkbox. **Then double-check that the link sheet is also attached to Vendor Tag & Tag QC** — if not, add it manually.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required for Box + Tag):** include coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Follow the linking document — box any item with a price or listed in the linking doc (e.g. if page 1 has one link, box the entire page). Also box Collections and Store Locations.
- **Tag / Tag QC (Low; Auto-tag ON; linking doc required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name:** priced items and category items → use the flyer name; **all other items → use the name in the spreadsheet provided.**
  - SKU, pricing, sale story, disclaimer as written on the PDF (if applicable); valid to/from only if different from the flyer run; select the most applicable category.
  - **URLs per the spreadsheet.** For non-priced items, select the **link** item type.
- **URL/Links QC:** Item Search → URL → IS → (Blank); download the link sheet from vendor tasks or FTP and add any missing product links.

## Final QC

- **FINAL QC checklist** owned by Flex.

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing

- Page swaps follow the baseline page-swap process.

---
*Source: Source Office Furnishings OneGuide (Google Doc `1QtAzcD3PaHDEVdF-A2HISPc4ZkXNPfCRaiHOBPdyM3s`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sport Chek & Atmosphere — Processing Guide

> **Source:** Sport Chek / Atmosphere OneGuide (Google Doc `1nOsi_qfa0RIx9gAXmgXWdlid7AtBxyniunec8Qs3nWo`), updated Mar 28, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | (not specified in OneGuide) |
| Flyer type(s) & cadence | Flyer Type 1: Weekly; Flyer Type 2: Monthly — ad-hoc files/dates. Preview available 1 day before Valid From |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; no Strategic Ops / Feedel |
| Linking document | Yes (used for both Box and Tag) |

## Files & schedule

- **When files arrive:** ad-hoc. The merchant emails to confirm files are on the SFTP, sends the link sheet, and states whether there is an Atmosphere flyer that week (usually there is not).

## Upload & setup (owned by Vendor)

- **Pages Tab → Edit:** select all pages from the SFTP menu → Confirm & Upload → Auto-Group or manually enter grouping numbers → Save & Confirm. **Do NOT Process Internally.**
- **Pricing Zone:** create a Base pricing zone with all applicable pages → Save & Confirm. Store set is **region-based** — use **"National (Excluding Quebec)"** for both Sport Chek and Atmosphere.
- **Attach linking documents to all vendor tasks:** from the Sport Chek merchant page → Details → view files from the SFTP section; download the link sheet matching the week name of the files and attach to all tasks.
- **Setup QC:** confirm all pages uploaded (Pricing Zone → Items View; check none left in SFTP); confirm flyer dates (usually first or last page); Standard 4 thumbnails; complete checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **Dates in the email sometimes differ from the PDF.** Confirm with the Ops team (Ops will send a screenshot of the dates to confirm).
- **Multi-product boxes must be split.** Boxes with multiple items (even just colour variations) must be tagged separately because each has a different URL on the link sheet. **Any item with a URL listed must be boxed separately.**
- **[NEW Apr 17 2025] PRODUCT PHRASE LINK:** if the link sheet includes a PRODUCT PHRASE link, box the **"SAVE" red text separately**. Any box requiring the text boxed separately is labelled **"PRODUCT PHRASE LINK"** in the link sheet; the box number (e.g. FLYER 1-1) identifies the ad block. The SAVE text box is a **direct link** (display type LINK).

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required):** include retailer logo, social media, special weblinks; exclude coupons, packaged deals, sign-up page. Follow the "statements" tab in the link sheet for special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** include brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude pre/postfix and valid dates.**
  - **Name:** exactly as shown in the flyer; include brand in the name even if repeated in the brand field.
  - **Description:** exactly as shown; **no SKU in the description.** Always include the SKU (its own field).
  - **Sale Story:** e.g. "BUY 1 GET 1 FREE", "BUY 1 GET 1 50% OFF", "Save up to 50%".
  - **[NEW Mar 28 2025] Multi-colour/variation items:** box the item name (gets tagged + URLs); the SAVE box gets the URL labelled **PRODUCT PHRASE LINK** and is a direct link (display type LINK). Links in the "PPL" tab of the link sheet belong to items.
  - **Statements tab:** set up as display type LINK with the URL.
  - **Social media links:** tag as links using the URLs in the OneGuide (Sport Chek home, Instagram, Facebook, TikTok).
- **Image QC:** clean PDFs when available; cutout otherwise.
- **URL/Links QC (Flex):** check all items have a URL; if missing, cross-reference the link sheet.

## Final QC

- **FINAL QC checklist** owned by Flex.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Sport Chek & Atmosphere OneGuide (Google Doc `1nOsi_qfa0RIx9gAXmgXWdlid7AtBxyniunec8Qs3nWo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sports Excellence (Canada & USA) — Processing Guide

> **Source:** Sports Excellence Canada & USA OneGuide (Google Doc `1zo7pdJwhcKFnLRaWur26WYUxLMXwXlj-nXyjH5h5hC4`), updated May 25, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#sports-excellence` |
| Flyer type(s) & cadence | **Canada** (merchant 2665 / type 2614) and **USA** (merchant 3409 / type 3445). Files Monday; publication dates ad-hoc, heavily dependent on file delivery. Available From Monday, Valid From Tuesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |
| Linking document | Yes (used for both Box and Tag) |

## Files & schedule

- **When files arrive:** Monday, but see the lead-time risk below.

### ⚠️ Common errors / risk items (retailer-specific)

- **Lead time:** the client ALWAYS sends files late (often the day before they want it live) and is hard to reach. Push back — they know 5 business days' lead time is required. Their flyers have no dates and they rarely push back after we set dates.
- **Linking document:** usually messy / supplied incompletely (rows meant to be hidden or deleted). Before uploading, confirm it has links and no crossed-out rows. If broken, fix if possible, otherwise request a new document — processing cannot begin without it and the live date may slip.
- **Items with multiple sizes** (Junior/Intermediate/Senior, each with its own link): there's no room to box each cleanly. **For Senior items, box the image and use a text box for the price; for all other sizes in that space, box only the price.**

## Upload & setup (owned by Flex)

### Canada (merchant 2665, type 2614) — manual upload
- **First confirm whether French pages were received** (Merchant → Details).
  - **Bilingual files:** upload the bilingual folder, select all, mark language **French**, click SAVE (not Save & Complete); confirm it stays French; then re-select the bilingual folder AND the English Canada folder and select the files (a re-upload warning is expected). Manually group pages by PDF name.
  - **French only:** Pages → Edit → upload from the corresponding FTP folder; ensure French pages have the language set to French.
  - **No French:** upload as standard (Pages → Edit → upload from FTP folder; Autogroup; do not process internally).
- **Pricing Zones (Canada = 3 PZs):** English (all stores except QC); Bilingual: English (QC only); Bilingual: French (QC only). Varies with files received — English-only files → no QC stores; French pages not bilingual → only 2 zones (EN for rest of Canada, FR for QC only).
- **Linking document:** confirm supplied correctly, then upload to all tasks with a note telling vendors to refer to the columns labelled for the language needed.

### USA (merchant 3409, type 3445) — manual upload
- Pages → Edit → upload from FTP folder; Autogroup; do not process internally.
- **Pricing Zone: Base; Store Selection: Add All Stores.** Same linking-document confirmation and upload steps as Canada.

### Setup QC (owned by Flex)
- Toggles: Hidden in Hosted. Available/Valid dates per client (only if 5 business days' lead time; otherwise push back — confirm via client email/Slack/BD and notify BD of finalized dates). External Run Name = N/A; no theme (unless Black Friday/Holiday, etc.). Legibility Heights 50/30; Standard 4 thumbnails.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box all items with prices (text boxes when needed); box social icons and website callouts on each page; box store locators next to items.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Brand/Name as stated in the linking document or at the top of the page.
  - **Price colours:** Current Price = green, Postfix = red, Original Price = pink.
  - **Price range:** put the **highest** price in Current Price, add the designation (JR/INT/SR) in the Prefix, and the other range prices in the Description. If more than one price per item, the lower goes in the Description.
  - URLs as stated in the linking document; every item requires a category; disclaimer only if within the drawn box (not if at bottom of page).
- **Image QC:** usually cutouts only.

## Pre-Final QC / Final QC (owned by DOC)

- **Spot checks:** verify no postfixes (prefixes only); use the linking doc to confirm banners/links are actually boxed; check language.
- **Leg Heights:** scan 50 / read 30. **Thumbnails:** Standard 4 applied to all zones; custom tiles (from merchant FTP) applied via QC thumbnails to storefront premium + storefront carousel premium, one by one, per pricing zone (both EN and FR; for French update both BIL FR and BIL ENG). If a "thumbnail too big" error occurs, resize in Paint (uncheck maintain aspect ratio; match FAdmin's size, e.g. 1065x600) and save with "updated" in the filename.
- **Image QC:** click data-pipe images so images appear; PDF over cutout; cutout if PDF not clean.
- **Mark items In-Store Only** (Ad Hoc Processing → confirm the completed count matches page count).
- **Categories:** all pages except page 1; tag French in English (auto-translates on front end); last page (usually links) gets "Sports" category.
- **Tagging check:** prefixes correct with no postfixes; descriptions correct; **page 1 — box only the website (do not tag the whole logo; English site should have `en_ca`); only the URL to the website is tagged on page 1 across all zones**; last page prefix correct (JR/SR); URLs correct and tagged as links (not items); use the correct link for English Canada / French / USA English per zone; Instagram and Facebook tagged.
- **Previews:** check horizontal and vertical.
- **Final QC:** check dates; geography unchanged; the "pages uploaded twice" warning can be ignored.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Sports Excellence (Canada & USA) OneGuide (Google Doc `1zo7pdJwhcKFnLRaWur26WYUxLMXwXlj-nXyjH5h5hC4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Spring Market — Processing Guide

> **Source:** Spring Market OneGuide (Google Doc `18dVairXtTmpIUdWnZ8MrSa6aqj6XZAkpdkuNgAsFKnU`), updated Dec 8, 2025. Contacts/credentials omitted.

> Spring Market is a **Brookshire's** banner (config `brookshires`, Slack `#brookshires`).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#brookshires` |
| Hosted URL | spring-market.com |
| Flyer type(s) & cadence | **Weekly** (type 7939) + **Monthly** (type 10561). Files Monday; Available From Tuesday, Valid From Wednesday; Available To Monday, Valid To Tuesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> **Timezone:** FAdmin runs on EST; Brookshire's is Texas-based (CST). Set valid-from = **1 AM** so it goes live at the right time.

## Files & schedule

- **When files arrive:** Monday.
- One-day consumer preview for both weekly and monthly publications.

## Upload & setup (owned by Flex)

1. **Codesheet:** search the FTP for the `.txt` manifest file matching the flyer's naming convention and save it locally.
2. **Codesheet tab → upload the manifest:** Name = flyer naming convention; Config name **`brookshires`**; **PDF Base Directory = `/flyer_zone_pages_pdfs`** (always this base path). Save → Process codesheet.
3. **Deals file:** from the FTP, save the correct deals `.txt` file. Copy its text into Excel and manipulate: Data → Text to Columns → Delimited → uncheck all → check "Other" = `|` → Finish; filter the first row; change columns A & G from general to whole numbers; highlight cells A1, C1, G1 for OS. (6a–6d can be done via macro.) Save as `.xlsx` using the FTP file name.
4. **Vendor tab → Upload Mass Attachment:** attach the Deals Excel file **and** the Blowline file to all vendor tasks.
5. **Edit Details:** no theme; available everywhere; **valid-from = 1 AM**. PZs have staggered dates → adjust all zones to a 1-day preview.
6. Leg heights 40/30; Standard 4 thumbnails; complete Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **"Missing page" codesheet error:** make sure the naming convention in the manifest matches the FTP; correct it in the manifest → save → reupload.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** include coupons, retailer logo, sign-up page, social media; exclude packaged deals and special weblinks. Draw a box wherever there's a unique price.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required; PDF image auto-selection ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Name:** enter as "Brand Product Name" (appears in larger, bold text). **Description:** smaller text below the name; first letter of the first word MUST be capitalized (e.g. "100% natural", weight, "Selected Varieties").
  - **Pre/Postfix:** do NOT use a postfix for "When you Buy ### In a Single Transaction" — put that in the disclaimer. eCoupon offers → postfix "FINAL PRICE WITH COUPON".
  - **Valid dates:** apply date overrides only if a related sales story indicates the item is part of a promotion.
  - **URLs:** Spring Market banner links to the merchant landing page; social icons link to their platforms.
  - **Categories:** label page categories by products/headers; if multiple categories on a page, label those with 3+ products.
  - **Sale Story:** e.g. "BUY ONE GET ONE FOR $0.01" goes in the sale story.
  - **Image QC:** apply clean PDF images where possible (no shadows); use cutouts if no clean PDF.

## Final QC (owned by DOC)

1. Mark Autostack complete.
2. Item Search: **UPC → Is → (blank)** — fill missing UPCs from the linking doc (vendor tab), leave note "UPC checked".
3. Page Categories (page 1 can have categories).
4. Pricing Zones — regions should have the same/similar items per flyer. Check Geography.
5. Re-run outstanding sessions; check outstanding vendor tasks.
6. **Flyer Sorting:** older flyer first, preview second, monthly last.
7. Complete FQC Checklist.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Spring Market OneGuide (Google Doc `18dVairXtTmpIUdWnZ8MrSa6aqj6XZAkpdkuNgAsFKnU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sprouts — Processing Guide

> **Source:** Sprouts OneGuide (Google Doc `1Vj5THG-kTJpJ-LsTTj5a44oFrKhurtmkSi2ali132k8`), updated Apr 7, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier S2C2 (Standard 2) |
| Availability | All platforms |
| Slack channel(s) | `#sprouts` |
| Hosted URL | sprouts.com/weekly-ad |
| Flyer type(s) & cadence | **Weekly Ad** (files Wed; live Tue) + **Monthly Deals / DOTM** (type 2; files Tue) |
| Processing | Auto-stack; no Flex; no OS-outside-standard; no coupons; no Strategic Ops / Feedel. Owned by DOC |
| Linking document | **Sprouts Linking Document** — OS has direct access to tag links (must use their @flipp email) |

> **Timezone:** Available/Valid From = **3 AM** for both publications.

## Files & schedule

- **Weekly:** PDF files & codesheet sent Tuesday night (all info in the email); upload to FAdmin Friday once the data sheet is received (or upload earlier with a vendor note not to begin tagging until the data sheet is added). If a new store appears, reply to the email for store info and add to FAdmin. If the codesheet has missing pages / incorrect file names, request a revised codesheet from the files contact.
- **Monthly (DOTM):** files arrive Tuesday, ~2 weeks out; preview Monday.

## Upload & setup — Weekly (owned by DOC)

- **⚠️ "Pg00 INSERT ONLY, NO AD" callout:** this pricing zone is a **separate hosted-only ad** (one page, tagged with two links). Delete that PZ from the codesheet and create a new flyer shell named "**Month Date - Store# Hosted Only**"; manual-upload the one page; add the single store to that zone; mark **Available in Hosted Only**. FQC = standard steps + confirm links tagged.
- **Edit Details:** Available & Valid From @ 3 AM; available everywhere; no external run name; no theme.
- **Codesheet manipulation (in Google Sheets):** delete extra rows at the bottom; delete extra columns on the rightmost end (including any unusual characters); save as CSV (no other manipulation unless a hosted-only version is needed).
- **Upload codesheet:** Name = "Codesheet"; Config name **`sprouts`**; **Toggles 1, 3, 4, 5, 6.**
- Check Pricing Zones (# pages matches the email). Ledge Heights 30/20; Standard 4 thumbnails; Setup QC checklist.
- **URL vendor attachments:** URL document is attached to the email. For Vendor Tag & Tag QC, add a comment telling OS to use their Flipp email and scroll to the flyer name in the Sprouts Linking Document — **OS tags links directly from the source; do NOT copy the original sheet.**

## Upload & setup — Monthly / DOTM (owned by DOC)

- Create a flyer shell ("*Month* DOTM"). Edit Details: Avail/Valid @ 3 AM; available everywhere; **Secondary publication = checked; External Run Name = "Deals of the Month".**
- Manually upload pages; create base pricing zone; **add all stores → remove store 0**; Standard 4 thumbnails.
- Vendor comment: use Flipp email, DOTM tab, correct month for links.

## QC specifics

- **Box Draw (Low; Weekly Auto-Box ON / DOTM Auto-Box OFF; Box QC bot OFF; linking doc for Box + Tag):** exclude coupons, packaged deals, retailer logo, sign-up page, social media; **include special weblinks.** All items boxed. For special weblinks, use the Sprouts Linking Document (Weekly tab / DOTM tab), Image column (G), to see what to box.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, URLs; **exclude SKU.** DOTM additionally includes a **Page Link** field.
  - Brand/Name/Prefix/Postfix/Price/Sale Story/Description/Disclaimer as on the flyer. Items with only a deal (no price) → leave pricing blank.
  - **URLs:** use the Sprouts Linking Document — **Link Title must be used in the Name field** (risk item). Do NOT check "Link Title Double Checked" (processors do that).
  - Every item needs an Analytics Category **and** a Google Category.
  - **DOTM Page Link:** display type Page Link; Name = Link Title; Page Destination per the linking document.
- **Image QC:** choose a valid PDF image per item (one image for multi-item boxes); clean PDFs only (no weird backgrounds/shadows/cutoff) — cutout when the PDF isn't clean.

## Links QC / Final QC (owned by DOC)

- **⚠️ Links QC is a promise to the retailer:** open the Sprouts Linking Document (Weekly Ad / DOTM tab), go through each item confirming (1) the **Link Title** is in the name field and (2) the URL is applied correctly (OS sometimes doesn't copy the whole link). Then **mark off the "Link Title Double Checked" column** for each QC'd item.
- For URLs on many pages, use Item Search (Item Type = Link, Page Grouping Index) → Multi Edit Items to mass-update Name + URL, then mark off the column.
- Complete the FQC Checklist.

## Out-of-processing — Weekly Live SKU corrections

- Tuesday morning "Weekly Flipp Report" email lists SKU corrections. Download → keep only "Name" and "Problem" columns → Remove Duplicates → sort Problem ascending. Action each issue using the SKU datasheet:
  - **Empty SKU field** → add missing SKU.
  - **Bad SKU value** → fix formatting (usually add/remove a comma).
  - **SKU does not match a product / could not match to collection** → verify against the datasheet.
  - **Ignore** "SKU matches product but not a valid store-product" (Sprouts-owned).

## Flyer review

- **Flyer Review Type: Lite** (owned by DOL).

---
*Source: Sprouts OneGuide (Google Doc `1Vj5THG-kTJpJ-LsTTj5a44oFrKhurtmkSi2ali132k8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Staples USA (Manual Indexed) — Processing Guide

> **Source:** Staples USA OneGuide (Indexed) (Google Doc `11FB5Jqu8c_YYwnfGY-QKMZkG37Rdv5TwkzAwqnF8npE`), updated May 6, 2024. Contacts/credentials omitted.

> **Flipp has NO external relationship with Staples USA — the flyer is Indexed.** Flyer type: Flyer (10472). Owned by FLEX.

## Account at a glance

| | |
|---|---|
| Account tier | Indexed |
| Availability | Flipp only |
| Slack channels | `#flex-processingsupport` |
| Hosted URL (for Flex to retrieve flyer) | staples.com/stores/weeklyad (also staplesconnect.com/weeklyad) |
| Processing | Auto-stack; FLEX owns processing; no coupons; no Feedel/Strategic Ops |
| Cadence | Available/Valid **Saturday → Friday** |

## Files & schedule

- **When files arrive:** the next week's ad is retrieved from the website (available Thu/Fri/Sat). They should have it up Fridays but it sometimes slips to Saturday — retrieve and upload when available.
- SOP: Confluence "Staples USA Indexing Processes / Manual Indexed Content."

## Upload & setup (indexing workflow — owned by FLEX)

**Collect the flyer:**
- Open the weekly-ad link (shows current ad). Scroll to "Browse Other Ads" and click the ad with the red **"Upcoming Ad"** badge.
- Click **"Print ad"** → set destination to **Save as PDF** → save.
- **Check ad pages:** scroll all pages to confirm product images loaded correctly. If pages have large blank space or text/prices with no product, wait 5 minutes and re-download; if it persists, contact the Skeleton Team.

**Crop + separate pages (uses [GIMP](https://www.gimp.org/downloads/)):** the flyer has white-space edges and is a single PDF; Fadmin needs one PDF per page.
- Enable the setting **"delete cropped pixels."**
- Open each page individually at **resolution 300** (default is 100; it resets to 100 when GIMP closes).
- Crop slightly inside the grey page square so the grey line isn't on the page; press Enter. Undo with CTRL+Z if needed.
- **Export each page individually** as PDF, adding the page number to the filename to preserve order.

**Upload & setup in Fadmin:**
- Open the pre-made flyer run for the correct valid dates (Staples USA merchant → Weekly Flyer type 10472).
- **Edit details → show/hide rarely-used fields → enable "Automation enabled?"** Confirm valid/available dates match the downloaded ad.
- Upload cropped pages, number them under "grouping" 1..N, Save and complete → submit. **Do not** check "process internally" or change the conversion library.
- **Flyer creation:** create a single pricing zone (description e.g. "weekly"); confirm all pages are listed.
- **Add FSAs:** on the pricing-zone tab, click the FSA count → select **"weekly indexed ad"** (pre-built list; adds ~17,721 FSAs). Reload to confirm.
- Draw thumbnail; set legibility heights (first number smaller than second).
- Setup QC checklist owned by FLEX.

## ⚠️ Common errors / risk items (retailer-specific)

- **Upload timing:** the flyer is often published Friday but can slip to Saturday — retrieve and upload as soon as it's available.
- Saved-PDF pages sometimes drop product images — always scroll all pages before uploading (re-download if a page looks blank/misaligned).

## QC specifics

- **Pipeline tasks (Box Draw, Box QC, Tag, Tag QC)** run automatically after Setup QC.
- **Auto Spot Check:** if it appears as "available," run it to let tasks finish and make FQC available.

## Final QC (owned by FLEX)

- Fill the top dates with the flyer's live/valid start & end dates.
- Add "n/a" to the flag "not all tagged items have been QC'd" (not needed for this content). Save and complete; the "errors of missing fields" warning is expected due to the n/a — click OK.

## Flyer review

- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Staples USA (Manual Indexed) OneGuide (Google Doc `11FB5Jqu8c_YYwnfGY-QKMZkG37Rdv5TwkzAwqnF8npE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Staples (Canada / Professional) — Processing Guide

> **Source:** Staples Canada/Professional OneGuide (Google Doc `1O11mnxwQZGBYewJgG5L35J2-FYkTW3xcowA7sntsqvE`), updated Oct 1, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#staplesca` |
| Processing | Auto-stack; Strategic Ops (Feedel/retailer data services); no Flex, no OS, no coupons |
| Banners / flyer types | **Staples Canada / Core (PREF)** — Business Flyer (2802), file type PCAM, codesheet "Pref" · **Staples Professional** — Cross Category (5782, "Pro"), Cross Category Supreme (11147, "Sup"), Cross Category Denis (11909, "Den") · **Staples Preferred** (2797, "PrefCA") — **inactive/no longer processed as of April 2025** |
| Hosted URLs | Staples Canada EN staples.ca / FR bureauengros.com · Staples Professional eway.ca (EN/FR), Denis eway.ca/denis |

## Files & schedule

- **When files arrive:** schedule / ad-hoc.
- **Cadence:** typically monthly; dates usually on the front page, else on the publication schedule/tracker.
- **Preview date:** week before go-live.
- **Linking document:** n/a.
- Files are dropped by the retailer into the **"Ops Flyers"** folder in the SFTP (SFTP credentials in the OneGuide — not stored here). If files land elsewhere, ask the retailer to correct.

## Upload & setup

- Create flyer shells when the retailer emails about a file drop. Put "Pref", "Pro", "Sup", "Den" in the shell name to identify banners; add the flyer ID to the publication tracker.
- **Use the codesheet (Pref / Pro / Sup) that matches the flyer run name.**
- Manual upload of pages + store sets, OR codesheet upload. Download the codesheet CSV per banner.
- In codesheet **column B (Zones):** if there are duplicate zone names, append "EN"/"FR" so Fadmin can differentiate languages.
- If uploading via codesheet, verify French pages uploaded as French pages — if not, a Language or Zones column error (extra space, or ROC EN vs ROC FR not differentiated).
- Thumbnails: **Standard 4**.
- **Edit Details:** no preview days. **Staples Canada:** hosted only, Secondary publication, no theme. **Staples Professional / Supreme / Denis:** hosted only, no theme.
- For **Staples Canada**, add a reminder note in the **Tag** and **Tag QC** vendor tasks: EN → search SKUs on staples.ca for URLs; FR → search on bureauengros.com.

## ⚠️ Common errors / risk items (retailer-specific)

- **URL sourcing (most important):** For **Staples Canada & Staples Preferred**, URLs must be found by **manually searching each SKU on the website** and copy/pasting from the address bar — **DO NOT FETCH URLS.** EN → staples.ca, FR → bureauengros.com. For **Staples Professional / Supreme / Denis**, URLs **can be fetched**.
- If a Staples Canada URL search returns items via `URL CONTAINS AffixedCode`, those URLs must be fixed manually (or, for 30+ items, submit an OS reprocessing ticket — check with DOC).
- Cross-language check: EN items must not carry `bureauengros` URLs and FR items must not carry `staples.ca` URLs — search and correct.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include the retailer logo (page 1). **Box all items** — some items have pricing but no image; box the item name/description + price. Exclude coupons.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Enter fields "as is."
  - **Categories:** every item must have a category; if unsure use **Office Products**.
  - Enter valid dates only when a callout differs from the flyer dates.
- **Image QC:** select a clean PDF image if available (most items have one); use a cutout only if no clean PDF.

## Post-processing (owned by DOC)

- **Item Category QC:** every item must have a category — Item Search → Categories IS blank → multi-edit → add **Office Products**.
- **URL/Links QC:** check email for any additional retailer links. **Box and tag the Staples logo(s) on page 1 as Display: Link** with the banner URL (Staples Canada EN staples.ca / FR bureauengros.com; Professional EN eway.ca/en / FR eway.ca/fr). Ensure a majority of items have links; add missing ones per the manual/fetch rules above.
- **Final QC:** check Geography for added/missing stores (add missing stores via Merchant → Stores/Sets); ledge heights **45/35**; thumbnails Standard 4.

## Flyer review

- **Flyer Review type: Lite.** EWAY = Staples Professional, PCAM = Staples Canada (Business); content usually identical between them except the logo. Check dates/external run names per the publication tracker, hosted-only, normally 2 pricing zones (EN & FR), all items boxed (visible-price CP non-enforceable since hosted only), pages chronological, geography no change.

---
*Source: Staples (Canada, Professional) OneGuide (Google Doc `1O11mnxwQZGBYewJgG5L35J2-FYkTW3xcowA7sntsqvE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Starsky — Processing Guide

> **Source:** Starsky OneGuide (Google Doc `1i8-Y5ZltoCiqe8qUj8zdZfwzAN20XrcXINySRfqffAQ`), updated May 9, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | **Flipp only** |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | starskycanada.com |
| Flyer type(s) & cadence | Weekly (type 2523 / flyer 2615). Files Monday; Available/Valid Thursday 12 AM – Wednesday 11:59 PM |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; no Strategic Ops / Feedel |

> **Simple Publication:** only cutouts are used in the pop-ups — no images are selected and no text is entered into the tagging fields, so tagging will look "weird." This is expected.

## Files & schedule

- **When files arrive:** Monday. Two sets of files are uploaded each time — you'll usually have to chase the IT/ops contact for them.
- **Only 2 stores: HAM and MIS.** Do **NOT** add the AUR store.
- Has only been 2 pages since COVID began.

## Upload & setup

- **Vendor setup:** in the VAST spreadsheet, find the FLEX tab for the current week, locate the Starsky row, fill in the flyer run ID + available date, and set it to SETUP READY.
- **[Overview] → [Edit Details]:** Hidden in Hosted; no theme; Key Messages = "This Week's Deals".
- **Pages → Edit:** select the lower-case folder and select the files. Create a pricing zone (Description: base). **Add all stores for HAM and MIS only** (not AUR). Thumbnails: Standard 4. Pricing Zones → Spotlights to QC Key Messages. Run Setup QC; check Sessions and Vendor tab.
- **Setup (Flex):** Legibility Heights **45/35**. Make sure the price and text are fully boxed (some image cut-off is OK; sometimes it's fine to box just one item fully — preference is text + price). **[Sessions] → [Verify Links]:** there are no links, but press it anyway. Check horizontal and vertical previews.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** include retailer logo; exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box products with their supporting info together; box separately-priced items separately.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude pre/postfix and valid dates.** (Tagging is minimal — Simple Publication.) Prioritize PDF images unless not clean (shadows/black backgrounds).

## Final QC (owned by DOC)

- **Final QC pipeline:** you'll get an error that tagged items haven't been QC'd — just write "**simp pop**".
- Check dates match the first page of the flyer. Check Sessions (re-run anything with a red warning). Mark FQC complete.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Starsky OneGuide (Google Doc `1i8-Y5ZltoCiqe8qUj8zdZfwzAN20XrcXINySRfqffAQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Stater Bros Markets — Processing Guide

> **Source:** Stater Bros Markets OneGuide (Google Doc `1hYwjxSERFXqwKsq5jFL4EGUARiFTqqIcSNCY25q_41M`), updated Jun 11, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#staterbros`, `#flex-processingsupport` |
| Hosted URL | staterbros.com/weeklyad |
| Flyer type | Weekly (1474) |
| Processing | Auto-stack; Flex (Processing Support); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Wednesday (SKU document sometimes only comes Thursday — do not finish Setup QC until it arrives; if uploading Thursday, file an urgent processing ticket).
- **Cadence:** Available Tue→Tue, Valid Wed→Tue (one-day preview). **Preview date:** Friday (OS must finish tagging by Friday for the Flipp Ads team).
- **Linking document required**, plus a **SKU document** and a **Categories document** — all must be attached.
- Files land in the SFTP: flyer page PDFs, **PAGINATION [date].xlsm**, **Flipp Links Weekly Ad [date].xlsx**, store assignment **MAILER GROUPS ADDRESSES-[date].xls**, and **Stater Bros SKU Template-[date].xlsx**. The Categories doc (**Stater Bros-Categories**) is not in the SFTP — linked in the OneGuide.

## Upload & setup (owned by DOC)

- Manual upload of all pages; assign page numbers per the file-name numeration.
- **Flyer Creation → build pricing zones per the Pagination document:** use the "Group" name as the pricing-zone name; assign pages per the document.
- **Add stores via codesheet:** store assignment doc from SFTP, name "stores", **config `stater_bros_stores`**, PDF base directory `/`, **only the first toggle (Store or store-set assignment) checked**.
- **Edit Details:** Available Tue→Tue, Valid Wed→Tue, preview start Friday, available everywhere, external name **"Weekly Ad"**, no theme.
- Legibility heights **55/45**. Thumbnails Standard 4.
- **Attach vendor documents** (Links, SKU, Categories) and add this note to *all* vendor tasks: use the SKU document to add SKUs to all items (check details match when names are similar); use the link document to box/tag all links; use the category document to add categories.
- Check Geography (should match week-over-week). If a pricing zone has no FSAs assigned, its store was too close to another → use the **FSA Swap** custom action.
- Complete Setup QC and file an Urgent Processing Ticket.

## ⚠️ Common errors / risk items (retailer-specific)

- **SKU list vs page numbers:** if the spreadsheet SKU list doesn't match page numbers, **ignore page numbers and match by SKU / item details** — prioritize SKU accuracy over page order.
- **Do not tag any Spanish-language content.**
- **Sale Story — the word "Save" must NOT appear** (breaks the client side). "Save $xx" → Dollars Off field; "Save %" → Percent Off field. "Mix & Match" and "Buy X Get X Free" are fine — but do not include "Mix and Match" in a "Buy X Get X Free" sale story.
- Image QC: **clean PDF must always be chosen; never select cutouts.** For multi-item boxes, check all applicable PDF images and star the **first-listed** product as Primary.
- Wine items (pink) use % off in a specific way: **no text in Sale Story**, fill Percent Off, Disclaimer = "When you buy (#) or More Mix and Match."

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required):** Exclude coupons, packaged deals (washers/dryers), retailer logo, sign-up page, social media. **Include special weblinks** — box and add a direct link per the linking document (e.g. "Digital Deals Section: Sign Up Here", CTA buttons, full pages).
- **Tag / Tag QC (Medium; Auto-tag ON; PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand tagged per box-draw specifics.
  - **Name:** bold flyer text; tag both if 2+ bold names; follow flyer capitalization; do not include bullet points.
  - **Prefix:** numbers only (no "Sale"); **Postfix:** e.g. Each, lb, With Digital Deals, When you buy X — never include original price.
  - **Categories:** use the attached Category doc (Meat, Frozen, Service Deli, Bakery, Household Needs, Produce, Grocery, Alcohol). **Page categories** when 3+ same-type products on a page.
- **Image QC:** clean PDF always; multi-item boxes check all PDF images, star first item as Primary; never cutouts.

## Post-processing (owned by Vendor)

- **Item Category QC:** OS sets categories; review page by page. Watch for miscategorized alcohol. All **"Cleo & Leo"** items → Service Deli; verify only those carry the Service Deli category.
- **SKU QC:** Item Search SKU IS blank → find SKUs in the SKU document. If more than one or two items are missing, email the retailer's file-drop contact for additional SKUs.
- **Ad-hoc QC checks (FQC):** Pre Price Text CONTAINS `/` → remove "Sale" from X/Y prefixes; Sale Story CONTAINS "Mix and Match" → remove from "Buy X Get Y Free" items.
- **Final QC:** dates/legibility/thumbnails as above; check pink wine items; check SKUs against the SKU doc; page categories (none on page 1, "Digital Deals" where applicable ~page 3); pricing zones vertical/horizontal; Geography should read "No stores or FSAs/zips were added or removed." Store-not-assigned and missing-thumbnail warnings can be ignored.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by DOL). Standard checks: dates (1-day preview), available everywhere, item-level valid dates, all items boxed/tagged with **clean PDF images**, multi-product boxes have all products selected with the first product as Primary.
- **Out-of-processing:** the client sometimes flags items appearing incorrectly during the week (usually a wrong SKU applied by OS). Find the item in the live flyer, apply the correct SKU from the SKU doc, save, and reply confirming — cc the Mercatus contacts so they can re-ingest for the Stater Bros website.

---
*Source: Stater Bros Markets OneGuide (Google Doc `1hYwjxSERFXqwKsq5jFL4EGUARiFTqqIcSNCY25q_41M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# STIHL — Processing Guide

> **Source:** STIHL OneGuide (Google Doc `1cY2XQ1DXwKXYpIdxyOgfxQkvv3T9QYFv9o5-ogeYVHE`). Contacts/credentials omitted.

> Note: this OneGuide is largely on the standard template; the facts below are the real account details that were filled in.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#stihl`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type | Catalogue (Flyer type #1) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** ad-hoc, usually via BD. They don't always send with enough lead time, **but processing can be pushed back 3–5 business days**.
- **Cadence:** ad-hoc; dates communicated through BD — confirm against the actual PDFs and reach out to BD if they differ.
- **Linking document required.**

## Upload & setup (owned by FLEX)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages → Edit → select all pages from the SFTP. They usually send **only 1 page for English and 1 for French**, which need to be **sliced into multiple pages later** (see Page Slicing). Auto-group or manually number; ensure correct language selected. Save & Confirm — **do NOT process internally**.
- **Pricing zones:** create a base pricing zone with all applicable pages; add all applicable stores.
- **Attach the linking document to ALL vendor tasks.**
- Setup QC: confirm pages uploaded correctly (no un-uploaded SFTP pages), confirm flyer dates (usually first/last page), thumbnails Standard 4, preview dates set.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required):** Include packaged deals, retailer logo, social media, special weblinks. Exclude coupons and sign-up page. Use the linking document to determine what else to box (logos, social media, etc.).
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand used for both box/tag.
- **Image QC:** PDF preferred if clean; otherwise cutouts are accepted.

## Post-processing

- **Page Slicing (owned by DOC):** the client sends all pages as one PDF; reslice for vertical optimization. Edit the current slice to the far-left page, then Draw slices for the other pages, ensuring all space is covered and slices don't cross page markings. Repeat for both English and French versions.
- **Pre-Final QC (DOC):** confirm dates from the PDF, availability toggles, thumbnails include the retailer logo, all items boxed/tagged, spotchecks (20% of pricing zones), previews clickable, sessions complete, geography correct.
- **Final QC (DOC):** complete the FQC checklist.

## Flyer review

- **Flyer Review type: Lite** (owned by FLEX). Checks: flyer dates, sessions completed, previews showing correctly, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: STIHL OneGuide (Google Doc `1cY2XQ1DXwKXYpIdxyOgfxQkvv3T9QYFv9o5-ogeYVHE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Stokes — Processing Guide

> **Source:** Stokes Canada OneGuide (Google Doc `1TYqSWUoQjrsc0DK7tFlDeUFEYlJn9H8YFykYdFUEL4c`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#stokes` |
| Hosted URL | stokesstores.com |
| Flyer type | Ad Hoc |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Mon→Mon, Valid Tue→Tue.
- Files usually sent via e-transfer: **EN files, FR files, and a linking document** (must be attached to vendor tasks). Upload files to the SFTP via Cyberduck/CoreFTP/Filezilla.

## Upload & setup (owned by Vendor)

- Confirm dates and times (**sometimes 6am–6pm!**).
- Visible everywhere, no theme, no external name.
- **Manual upload** (files are lowercase in FTP); always choose the **high-rez** option.
- **2 zones: EN and FR.** Assign all stores to each. Change page languages so all stores get English & French pages.
- **Attach the linking document to all vendor tasks.**
- Check pages for design issues and cut out margins.
- After setup: external name = same as flyer name (EN and FR versions); **legibility heights 45/35**; thumbnails Standard 4 (Thumbnail 1065x800, stock_premium, storefront_carousel_premium, storefront_carousel_organic); Geography no missing/added stores.
- Setup QC (FLEX): mark all boxes complete, ignore warnings.

## ⚠️ Common errors / risk items (retailer-specific)

- Not all items have a brand name.
- **Do NOT enter the SKU in the Description field.**
- **General rule:** name = all text **before the first comma**; description = all text **after the first comma** (e.g. 6 L, 14.5 oz, stainless steel, set of 6).
- **Do NOT enter "SAVE %" / "EPARGNEZ %" into the Sale Story field.**
- Original prices given as ranges can go in the Sale Story field instead of the Original Price field.
- SKU, multiple item pictures, and prices are tagged separately.
- **Cut-off margins / text overlay:** troubleshoot via page-level sessions → tile generation → ghost script; or ask a Lead and file an OS ticket; if not resolved, request new pages.
- All Stokes logos are boxed; all social media icons are boxed.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** Include retailer logo (first & last page), sign-up page, social media (Facebook, Twitter, Instagram), special weblinks. Exclude coupons, packaged deals. Box every item with a price separately (text boxes when needed); box items with individual prices separately even within one picture; box all banners with URLs.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand per box specifics. **Exclude pre/postfix and valid dates.** Brand: case-sensitive, as in flyer. Name ends at the first comma; description begins after it.
- **Image QC:** select clean PDFs if available; cutouts OK if no clean PDF.

## Final QC (owned by Vendor)

- Mark Autostack Spotcheck complete.
- **Items without URLs:** download the linking document from vendor tag tasks and add missing links; while open, check all yellow rows for unique instructions.
- Item images: clean if possible, cutouts if not. Thumbnails Standard 4.
- Pages: categories **max 3 per page**; confirm both EN/FR pages uploaded; check/update dates.
- Pricing zone vertical/horizontal; Geography same as last run.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- **Out-of-processing:** send a preview to the retailer at least a few days in advance.

---
*Source: Stokes OneGuide (Google Doc `1TYqSWUoQjrsc0DK7tFlDeUFEYlJn9H8YFykYdFUEL4c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Strack and Van Til — Processing Guide

> **Source:** Strack and Van Til + Town & Country Fresh Food Market OneGuide (Google Doc `1V-O0xk9rAH0Ei_J8MWghuXQasJr9i7OuZzM3GHIL2FU`), updated Apr 7, 2026. Contacts/credentials omitted.

> Covers two banners: **Strack and Van Til (SVT)** and **Town & Country Fresh Food Market (T&C)**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#strackandvan` |
| Hosted URL | strackandvantil.com |
| Flyer types | 6018 Weekly **(SVT)** · 5926 Weekly **(T&C)** · 6018 Monthly (SVT, lives under Weekly Ad); ad-hocs |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops (Feedel); no coupons; **no linking document** |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** weekly (2 pubs) + ad-hocs. Available Tue→Tue, Valid Wed→Tue.

## Upload & setup (owned by Vendor)

**Weekly (SVT & T&C — same upload process):**
- **Manual upload:** Pages → Edit → select the ad folder → select all files → Auto group → Save & Complete.
- **Flyer Creation:** create a pricing zone (description "Base", language English), add all pages.
- **Important — SVT page order:** Page 01, **Front Gate, Back Gate**, Page 02, 03, 04, 05, 06, 07, 08, **Online**.
- Save & Complete, add all stores.
- **Thumbnails (Standard 4).** Note: for SVT, when drawing thumbnails for `thumbnail_1065x600` and `storefront_carousel_premium`, draw over the first 3 pages (instead of the usual 2).
- Mark Autostack Spotchecks complete.
- From Overview → **Make Vanilla → click Flyer Run → OK** to save.
- **Flyer sorting:** adjust so the **oldest flyer shows first** (the retailer is strict about this).
- File an Urgent Processing Ticket (reason: "Short Lead Time"). **One form per vendor** — if Box QC/Spotchecks and Tag QC are done by different vendors, submit a separate form for each.

**Monthly (SVT):** manual upload the monthly ad folder; pricing zone "Base" (English), all pages **in order**, add all stores; thumbnails Standard 4; Autostack Spotchecks complete; Edit Details → preview start = 1 day before available-from, **no theme**; complete Setup QC.

## ⚠️ Common errors / risk items (retailer-specific)

- **This merchant is simplified pop** — only item boxes appear in the item pop. **No text boxes**; every item with a unique price must be boxed separately (even same brand); box around item name + pricing info.
- **SVT page order** must be maintained (Page 01, Front Gate, Back Gate, Page 02…08, Online) — check again at FQC.
- **Flyer sorting** must be oldest → newest → monthly.
- **Tag Lite retailer — do NOT tag Name, Brand, Description, SKU, Sale Story** (but if the name is missing, tag the name).
- Items under **2 Day / 3 Day Sale** banners must be tagged with the appropriate dates.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; no linking doc):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Simplified pop — draw clean item boxes; box groups sharing one price together; box separately-priced secondary products separately.
- **Tag / Tag QC (Low; Auto-tag OFF; no linking doc):** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price. **Exclude brand, description, SKU, URLs.** If bullet points/multiple items, don't include bullets — separate with a comma + capitalized word. Multiple items sharing a price → box together. Watch for 3-day-sale callouts (tag accordingly).
- **Image QC: cutouts only.**

## Post-processing / Final QC

- **Pre-Final QC:** ensure all items under 2 Day / 3 Day Sale banners are tagged with correct dates.
- **SVT page order check** (as above).
- **Turn off/uncheck Vanilla flyer** (Overview → Make Vanilla → unselect flyer run → OK) so items are clickable on the front end, and **create an OPTICS ticket** (set due date to the FQC day, update flyer runs in the description, add the Notify User, assign to the DOC, move to the live-check row when complete).
- **FQC checklist:** write "no" for the two red warnings (1) "Spot checking words is not complete" and (2) "Not all tagged items have been QC'd", then force mark complete (Save and Complete a second time).
- **Check flyer sorting:** oldest Weekly first, then newer Weekly, then Monthly.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- **Out-of-processing:** Monthly Savings Guides also come in — short lead times, confirm dates on the front page, manual upload same as Weekly, **external run name "Monthly Ad"**, and it should be 2nd/3rd in flyer sorting behind the weekly flyers.

---
*Source: Strack and Van Til OneGuide (Google Doc `1V-O0xk9rAH0Ei_J8MWghuXQasJr9i7OuZzM3GHIL2FU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Super C — Processing Guide

> **Source:** Super C OneGuide (Google Doc `1_gzIS8CZR04JYcgBjeBtMIXnJyyw64-e_385NSvVd8o`), updated Feb 10, 2026. Contacts/credentials omitted.

> Super C is a **Metro banner** (French, Quebec). We do not power their hosted site.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#metro-ops` |
| Hosted URL | N/A (we do not power their hosted) |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Thursday. **Cadence:** Available Tue→Thu, Valid Wed→Wed.
- **No linking document.** Store codesheet arrives via email; pages and tracking sheet come via SFTP.

## Upload & setup (owned by DOC)

**Store codesheet upload (creates pricing zones only — no page info):**
- Open the store-assignment spreadsheet; recolor the currently-visible version headings, then unhide and delete all hidden columns (delete every orange-heading column).
- Rename heading "site number" → **"No site"**; delete blank column A. Save as .csv.
- Upload: **only toggles 1 & 4 checked** (Store or Store Set Assignment and Allow Pricing Zone Creation), **config `super_c`**, PDF base directory `/` (the pop-up warning is OK).
- Verify pricing zones — there will be two of each: one **base French** and one **cross-language**.

**Page upload:**
- Upload all pages from the **PDF_FINAUX** folder for the week (labeled by date code). **Do NOT use the BlockID folder.**
- Mark all as **French pages**; auto-group page numbers; Save and confirm.

**Page order:** find the "tracking" sheet in the SFTP for the week and use it as reference in Flyer Creation. Confirm the zone at the top of each tracking-sheet section matches the Fadmin zone; repeat for all base zones. For **CL (cross-language)** zones: unselect the cross-language toggle, switch language English→French, copy the base zone layout (e.g. NAT → NAT CL), then re-check cross-language and switch French→English. Repeat for all CL zones.

**CAHIER (booklets):** occasional extra 4–7 page publications (pages labeled CAHIER in the SFTP); page order is in the tracking sheet under the weekly flyer. No codesheet — create a new flyer run under the weekly flyer type, upload all pages as French, create two zones (base French + "base cl" cross-language), assign all stores.

## ⚠️ Common errors / risk items (retailer-specific)

- **Names are tagged FRENCH first, ENGLISH second.** The English name is found in the description on the last line in **bold**. **Do not tag the Brand field.** Multiple items: first name in Name field, additional names in Description separated by line breaks.
- **"Voir prix en magasin" is a Sale Story, NOT a description.** "Voir variétés en magasin" IS a description — keep it in line with the last item, **do not separate with a line break**.
- **ECONO PACK** ("Format écono") goes in the Description field, not the name.
- **Block ID goes in the SKU field** (from the text-extraction field), upper case, multiples separated by commas. If cut off or "NOBLOCKID", leave SKU **blank**. **If no Block IDs appear in the text extraction at all, notify the Flipp team immediately.**
- "Buy One Get One" deals: include "À l'achat d'un…" + the required product in the Name field, and "Obtenez pour…" + the get-item info in the Description field.
- Keep capitalization exactly as on the page.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box single items with a price; box multi-items sharing a price in one box; BOGO in one box.
- **Tag / Tag QC (Low; Auto-tag OFF; no linking doc):** Include name, description, **SKU (Block ID)**, price, sale story, categories, disclaimer, original price. **Exclude brand, pre/postfix, valid dates, URLs.** Retailer does not include original pricing.
- **Image QC:** clean PDFs when available; cutouts if none.

## Post-processing (owned by DOC)

- **Box & add links from the Tracking Sheet** in the SFTP as Display: Link (page names are in the tracking sheet's second column).
- Check pages for points callouts (tag in sale story); Item Search SKU blank → add SKUs from text extraction.
- Run the **Metro Links custom action** ("Set Metro Banners Items URLs"): find the file in the FTP under `/ZPO400 + Google Feeds`, copy the file name **without** ".csv", then add the tracking code from the Metro Banners Tracking codes sheet.
- **Final QC:** thumbnails Standard 4; SKU QC (add SKUs from text extraction, "NOBLOCKID" left blank); run the Metro custom action after SKU QC; add supplementary links from the tracking sheet; add the Super C tracking code last.

## Corrections & flyer review (owned by DOC / FLEX)

- **Corrections:** Super C uses Madmin for preview links; **FQC should be completed Monday morning** (they access previews by noon). Corrections come by email + SFTP by EOD Monday / early Tuesday and should be actioned within 24 hours (usually name/description updates via item search). ARB can be filed for this task.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Super C OneGuide (Google Doc `1_gzIS8CZR04JYcgBjeBtMIXnJyyw64-e_385NSvVd8o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Super King Markets — Processing Guide

> **Source:** Super King Markets OneGuide (Google Doc `168CmPhqguU7Xu8oqwks8aZ5siCvMXlOZBfK2Iv1rlhg`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only (no hosted) |
| Slack channels | `#superkingmarkets`, `#flexprocessingsupport` |
| Flyer type | Weekly Ad |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup); no coupons; no Feedel/Strategic Ops |
| Account resources | Confluence Account Guide (OP) & Vendor Guide (VEN) |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Wed→Wed, Valid Tue→Tue. Flyer goes live Wednesday, ends Tuesday. **Dates are on the last page of the flyer.** No linking document.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → "Select files from FTP" → find the correct dated folder → upload all pages (usually 8). Auto-group; language **English**; Save and complete → Submit.
- **Pricing zones — depends on the pages:**
  - 1 set of pages (or 1 version) → **1 pricing zone** (add all stores).
  - Multiple versions of each page → **one pricing zone per version**, named after the version, with stores assigned by the numbers in the page names.
  - Example (3 versions): V1 = stores 2, 5, 6, 8; V2 = stores 1, 4, 7; V3 = store 3.
  - Two-version file naming example: "SK 1,2,3,5,6,7,8" and "SK 4" (SK + store code) — upload all pages for both versions, name pricing zones per the file naming (e.g. "1-8" and "4"), and assign stores accordingly.

## ⚠️ Common errors / risk items (retailer-specific)

- **Analytics Categories MUST be tagged on ALL items.**
- **Pricing zones / stores follow the page (version) file names** — assign stores by the numbers in the page names, not "add all", when there are multiple versions.
- **Image QC must be all cutout images** — run the "Set Cutout Images" custom action (System → Custom Actions → Action Type "Set Cutout Images" → paste Flyer Run ID → Run Action).
- The **Super King Markets logo on page 1 must be boxed and tagged to the retailer website.**
- If there is a coupon in the flyer, ensure its **display type = "coupon".**
- "Not all categories that are used in pricing zones have thumbnails" — safe to ignore, continue with FQC.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Include retailer logo. Exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box all items separately; use text boxes where necessary.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand per box specifics.
- **Image QC:** all cutout images (see risk items).

## Post-processing / Final QC

- **URL/Links QC (DOC):** ensure the Super King Markets logo is linked on page 1.
- **Final QC (Vendor):** preview start date = the Friday before go-live; no seasonal theme; thumbnails Standard 4. Mark Wayfinding QC complete (ignore wayfinding — no longer done); mark spotcheck complete. Image QC: all cutouts via the custom action. Confirm the page-1 logo is boxed and tagged to the retailer website; confirm any coupon display type is "coupon".

## Flyer review

- **Flyer Review type: Lite** (owned by DOL). Checks: pricing zones (pages named after the PZ; stores per PZ name, e.g. Store 1–7, Store 8); item-specific valid dates from the bottom of the last page; available & valid Wednesday.

---
*Source: Super King Markets OneGuide (Google Doc `168CmPhqguU7Xu8oqwks8aZ5siCvMXlOZBfK2Iv1rlhg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Superior Grocers — Processing Guide

> **Source:** Superior Grocers OneGuide (Google Doc `19g80rubvdkX1IAyi8TPe649_G-VQXmT8zMwIYQ3QVCc`), updated Jun 12, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Standard |
| Availability | All platforms |
| Slack channels | `#superiorgrocers` |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup + FQC); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Wednesday. **Cadence:** Available Wed→Wed, Valid Tue→Tue (times set to **1:00 AM**).
- Linking document: **Yes — Tag/QC specific.**

## Upload & setup (owned by Vendor)

**Build the codesheet from the "Version List" Excel file:**
- Create a new tab (this becomes the generic codesheet). Headers: A1 `Zones`, B1 `Stores`, C1 `Page 1`, D1 `Page 2`, … one column per flyer page.
- From the main tab, copy each version's Version Code → Zones, Store # → Stores, and each Page column into the matching Page columns of the new tab.
- Append **".pdf"** to each page name to match the FTP file names (use `=CONCATENATE(pagecells,".pdf")`, then paste as values and delete the formula helper).
- Save as CSV and upload in Fadmin. Ignore the PDF Base Directory (changes weekly — taken from the FTP).

**Setup / dates:**
- Available From & Valid From times = **1:00 AM**. Verify dates (comes up Wednesday, down the following Tuesday) via Overview → Edit Details; **all toggles off** (hidden nowhere).
- Setup QC: verify dates on page 1, verify each page and correct pagination (1, 2, 3, 4…).

## ⚠️ Common errors / risk items (retailer-specific)

- **Section-level valid dates are often missed:** the "SATURDAY & SUNDAY Specials!" section on Page 1 (~8 items) must have correct **Item Valid From/To** dates and the **Sale Story** applied. Save after each item.
- **Section-level sale stories** (e.g. Weekend Specials) are often missed.
- **Prefix/Postfix errors:** e.g. Coffeemate Creamer → current price $4.99, postfix "EA WHEN YOU BUY 2"; ensure the number following "WHEN YOU BUY" is correct. Postfix tagging must include the text following the price **AND** the text in the black box.
- **Specified-day sale stories** ("Thursday only", "Wednesday only", Red Tag specials) advertised at the top of a page apply **only to items up until the next header**. Items below the next header follow the overall flyer valid dates unless otherwise specified.
- **VOID coupons:** do **not** box or tag any coupon marked VOID (should not be interactive).
- **Images:** black-background images → check "Do not Use PDF images"; do not use images that correlate to other products. Meat/seafood/pop-up products often need cutouts.
- **No overlapping boxes**; box each price individually; don't miss small items (e.g. ice cubes); ensure item pops don't include images from other items.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include packaged deals, retailer logo. Exclude coupons, sign-up page, social media, special weblinks. Box all priced items (text boxes where needed), no overlaps.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; brand per box specifics. **Exclude SKU (no SKUs) and URLs.** Name/Brand/Description as in flyer. Disclaimer only if within the drawn box (not bottom-of-page). Every item needs a category — if unsure, Grocery.
- **Image QC:** do NOT tag items with a black background; check "Do not Use PDF images" as needed.

## Post-processing / Final QC (owned by Vendor)

- Mark Autostack Spotcheck complete.
- **Sessions tab:** Mark items in-store only (Flyer Level Run Tasks) → "Pgs Marked In-Store 4/4".
- **Pricing Zone tab — Key Messages:** rotate between blank/"Weekly Specials" and "Red Tag Deals" (per stage; final FQC = none).
- **Page tab — Category QC:** no categories on page 1; for the rest, apply categories per the sections on each page (1–2 per page).
- **Item-level dates:** re-check the Page 1 Saturday & Sunday Specials for Item Valid From/To + Sale Story; save each.
- **Coupons:** confirm no VOID coupons are boxed.
- **Dates:** Available Wed 1:00am → Tues 11:59pm; Valid Wed 1:00am → Tues 11:59pm. Available everywhere, no theme.
- **Legibility heights 35/25**; thumbnails Standard 4 (Thumbnail_1065_600 & storefront_carousel_premium = first 2 pages; stock_prem & storefront_carousel_organic = first page).
- **Geography:** no changes week over week; 1–3 FSAs added/removed can be ignored.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- Black Friday / seasonal comms are tracked in the linked Flipp Operations Guidelines docs.

---
*Source: Superior Grocers OneGuide (Google Doc `19g80rubvdkX1IAyi8TPe649_G-VQXmT8zMwIYQ3QVCc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Supermarche Aures — Processing Guide

> **Source:** Supermarche Aures OneGuide (Google Doc `1ixgAZDr5ZaGEbQcBNP0J4msyQrpjo74slSKDyKqhRQ4`), updated Nov 26, 2025. Contacts/credentials omitted.

> Single-store, French-language grocery banner.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (not on hosted) |
| Slack channels | `#1p-supermarche-aures` |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Thu→Wed, Valid Thu→Wed. **Always double-check the PDF dates** and confirm with client/BD if needed.
- Files provided via SFTP (PDF pages and URL docs). No linking document.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages → Edit → select all applicable pages.
- Index pages and ensure they're in order.
- **Set language to FRENCH only.**
- Save + Save & Complete.
- Create a **Base pricing zone** for all pages; add all stores (**only 1 store**).
- Setup QC: complete the checklist in the pipeline.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low):** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** **Auto-tag is enabled but usually only works in English — use text extraction to get French content.**

## Post-processing / Final QC

- Standard checks: all items boxed and tagged; hosted previews; Geography tab (no FSAs missing).
- **Final QC (FLEX):** Standard 4 thumbnails; complete FQC checklist in Fadmin.

## Flyer review

- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Supermarche Aures OneGuide (Google Doc `1ixgAZDr5ZaGEbQcBNP0J4msyQrpjo74slSKDyKqhRQ4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Supermarche PA — Processing Guide

> **Source:** Supermarche PA OneGuide (Google Doc `1Y3nsoo_toFQzFlvimccaZq6FMgBV-pGicYWDkHhKnUQ`), updated Jul 9, 2026. Contacts/credentials omitted.

> French-language grocery banner. Runs **two flyer types** (Weekly + Nature) and up to **3 weekly versions** (V1/V2/V3).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | supermarchepa.com |
| Flyer types | Weekly Flyer (11930) · Nature Flyer (12205) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Thursday (always short notice — upload right away so files process overnight).
- **Cadence:** Available Mon→Sun, Valid Mon→Sun. Nature Flyer runs **2 weeks**.
- No linking document. **Full-Time Ops creates any additional flyer shells (V2, V3)** weekly per the retailer's email.

## Upload & setup (owned by Vendor)

**Weekly Flyer — same steps for V1, V2, V3 (only pages and stores differ; V1 gets V1 pages, etc.):**
- Flyer-run dates may differ between V1/V2/V3 — do not edit dates if the common section notes they're correct.
- **Manual upload:** Pages → Edit → select all pages (except whole-flyer files) from the SFTP. **Do NOT upload "PA Nature" files to the Weekly Flyer type** (they go to the Nature Flyer type). Auto-group or number pages; ensure language = **French**. Save & Confirm — do NOT process internally.
- **Pricing zones:** create a **Base** zone (toggle French to see pages); then create **"Base CL"** — select French so all pages get added, then toggle Cross Language + English. Save & Confirm.
- **Stores:** V1 → Add All; V2 → Add All; **V3 → add only Ave Donegani & de Courtrai.**
- Setup QC: confirm pages uploaded (no un-uploaded SFTP pages), confirm dates (Mon→Sun), thumbnails Standard 4, preview dates set.

**Nature Flyer:** navigate to the "Nature Flyer" type; manual-upload only pages labeled **"pa nature"** (dates on file name must match the run). Auto-group, French language. Create Base + "Base CL" (Cross Language) zones; **add 2 stores only — "du parc" and "Park Ave."** Nature flyer runs for 2 weeks.

## ⚠️ Common errors / risk items (retailer-specific)

- **Always short notice** with pages (usually Thursdays) — upload immediately.
- **Do NOT mix flyer types:** "PA Nature" files → Nature Flyer type only; other pages → Weekly Flyer type only.
- **Names:** all pages are French, but some items also include English on the PDF. For those, include the English name in the Name field using **French Name | English Name** (e.g. `FILETS DE MORUE FRAÎCHE | Fresh Cod Fillets`).
- **Page merging:** check that no pages have been merged (Storefront Spotcheck) — click "don't merge" to fix.
- **V3 stores** are limited to Ave Donegani & de Courtrai; Nature stores to "du parc" & "Park Ave."

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Include packaged deals. Exclude coupons, retailer logo, sign-up page, social media, special weblinks. For single and multi items, box the whole item block.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON):** Include name, pre/postfix, valid dates (if different from the main flyer), description, price, sale story, categories, disclaimer, original price; brand used for both box/tag. **Exclude SKU and URLs.** Use the French | English name format above.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing; usually a lot of spelling-related spotchecks.

## Post-processing / Final QC (owned by Vendor)

- **Pre-Final QC:** confirm dates (from PDF) and availability toggles; spotcheck pages for the French | English name format; thumbnails Standard 4 (include retailer logo); confirm no merged pages (Storefront Spotcheck); check the Cross-Language PZ has been cross-languaged to English with the same pages/stores as the French zone; standard flyer-review checks (all boxed/tagged, spotchecks 20% of PZs, previews clickable, sessions complete, geography correct).
- **FSA Check (owned by DOC):** Full-Time Ops checks FSAs match the retailer's email (common V1/V2/V3/Nature breakdowns are in the linked sheet); run the **Assign FSAs from CSV** custom action if needed.

## Flyer review

- **Flyer Review type: Lite** (owned by FLEX). Checks: flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Supermarche PA OneGuide (Google Doc `1Y3nsoo_toFQzFlvimccaZq6FMgBV-pGicYWDkHhKnUQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Supermercado Nuestra Familia — Processing Guide

> **Source:** Supermercado Nuestra Familia OneGuide (Google Doc `1MkfyV7F21rJR1GpeuFVyWdRN-aXL9GZ6sOSpYnsh4EU`), updated Sep 2, 2025. Contacts/credentials omitted.

Part of the SpartanNash group.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#spartannash`, `#flex-processingsupport` |
| Hosted URL | Not powered by us (no Hosted) |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing; OS completes flyer processing; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available/Valid Sunday → Saturday.
- **Preview date:** Thursday before go-live (e.g. Saturday live → Thursday preview).
- **Linking document:** No.

## Upload & setup

- Files and Posting Document drop to the FTP on Mondays.
- Download the Posting Document to confirm page order; upload pages from FTP and order them per the Posting Document.
- **Create pricing zones based on the Posting Document; add stores and pages.**
- Wait for sessions to run; confirm vendor tasks are ready/active.
- Confirm valid dates are Sunday → Saturday. Edit Details: Available/Valid From/To Sunday–Saturday.
- **No theme.** Thumbnails Standard 4. Leg heights 40/30.
- Complete Setup QC checklist; mark FTP files (including the Posting Document) as uploaded.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF)**
- Include: coupons, packaged deals, special weblinks. Exclude: retailer logo, sign-up page, social media.
- Anything with a price gets a box; box image and text together as one; don't overlap boxes.
- Do **not** box the CTA banner at the bottom of specific pages.

**Tag / Tag QC (Low; Auto-tag ON)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.** Brand is Box-specific.

**Image QC**
- Not a priority for this retailer — default cutout images are acceptable. **Not currently using PDF images — use item cutouts only.**

## Final QC / go-live notes

- Complete any outstanding spot checks. Check for narrow pages in "Storefront Spotcheck" per pricing zone; merge to next page if any. Mark "Autostack Spotcheck" complete.
- Review each page for special-day sales (e.g. 3-Day Sales); apply unique valid dates where items are part of a sale with different dates.
- FQC checklist: spot checks, thumbnails (Standard 4), legibility heights, geography matches prior weeks, page order/region correct, toggles correct, all items tagged, dates match PDF, no "real" warnings on overview.
- **Flyer Review type: Lite.**

---
*Source: Supermercado Nuestra Familia OneGuide (Google Doc `1MkfyV7F21rJR1GpeuFVyWdRN-aXL9GZ6sOSpYnsh4EU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# SuperValu (Shop Easy Food) / Freshmart — Processing Guide

> **Source:** SuperValu / Shop Easy / Freshmart West (SV Clone) OneGuide (Google Doc `1OpCYUmidGoqXxpAve1s7ZG2V5Em9BlKJOWToRcJ60IM`), updated Oct 14, 2025. Contacts/credentials omitted.

> A **Loblaw** family of banners: process **SuperValu** as the primary, then **clone** it to **Shop Easy Foods** and **Freshmart West (SV Clone)**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer type | Weekly (5994) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Monday. **Cadence:** Available Wed→Wed, Valid Thu→Wed (NFW starts from **3 AM**). **Preview:** Sunday.
- Codesheets are labeled **WK__ AI FINAL CODES**; download and upload them to the LCL Flex Upload folder and update the Flex Tracker.

## Upload & setup (owned by FLEX)

- **NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded** (Edit Details → show/hide rarely-used fields → Height → 4096.0 px → OK). If pages were already added, flag to Full-Time Ops and continue.
- **Manual upload:** use the **SE SV Online** tab of the codesheet (check page numbers and stores). Upload SuperValu files for the correct week as **English pages**; number per the codesheet (**there are two page 1s — both numbered page 1**; pages usually 1–8). Save & complete; in the pop-up choose **ghostscript 9.06 gamma** and submit.
- **Pricing zones:** `SE SV ONLINE` (English) and `FRESHMART ONLINE` (English; change page 1 to the one with "Y" in the description). Create **cross-language FR zones** by copying the ENG layout and cross-languaging to FR for all PZs.
- **Stores:** add stores **only to SE SV ONLINE** (Add All → store set "SV 5 Stores" = 3 stores). FRESHMART ONLINE has no stores.
- Confirm vendors assigned; preview date 2 days after upload; **External Run Name** = "Weekly Flyer Valid Thursday [date] - Wednesday [date]" (no FR version); no theme; **Key Messages** = "This Weeks Savings" (no FR version).
- After sessions complete, check item view: dates correct, SuperValu/Shop Easy/Freshmart logos on SE SV ONLINE; only Freshmart logo on FRESHMART ONLINE; **merge pages** if items are split between two pages (Page → Merge page → left + right → submit; then place the merged page in the correct PZ position for both zones).
- **Setup QC (FLEX):** Available Wed→Wed (1-day preview), Valid Thu→Wed (**NFW from 3 AM**); Sunday preview start; external run name set; no theme; comment "ran gamma"; mark off Auto Spotcheck.

## ⚠️ Common errors / risk items (retailer-specific)

- **Set Pixel Height to 4096 first** — must be done before uploading pages.
- **Two page 1s** — both must be numbered page 1.
- **Raw meat images:** change any raw-meat image to **Cut Out** — do not select the PDF. Only select PDF images for meat/seafood/cheese when the product is **packaged**.
- **FSA guardrail (NEW):** ensure FSAs **T6C** and **R3P** have NOT been generated (Pricing Zones → Stores/FSAs). If generated (highlighted red), run the **Remove FSAs** custom action (set Flyer Run ID + Pricing Zone ID to the weekly flyer) and re-verify.
- **Page swaps** often cause **page-stitching** issues — always **rerun Page Tile Generation** after swap sessions kick off (especially post-live); if issues remain, rerun and mark complete from Vendor Box Tag onward; confirm the swap in item view for all PZs.
- Live-date flags: URL leading to a different item → Flag; item quantities in the Description → Flag.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include coupons and packaged deals. Exclude retailer logo, sign-up page, social media, special weblinks. Box only the item (unique price), not extra space; box banners containing a nofrills.ca link; do NOT box Facebook/Twitter/etc. or logo banners.
  - **Page-level categories** during box draw for all pages **except the front cover** (Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce).
- **Tag / Tag QC (Medium; Auto-tag OFF; linking doc required):** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.**
  - **Name:** ALL CAPS, format `Brand Product Name, Quantity` (comma before the quantity). **Tag all info in FRENCH AND ENGLISH, separated by "/".**
  - **Description:** plain (non-bold) text, first letter capitalized, metrics as 2.56/kg, "Product of…", "No. 1 grade", "frozen", "selected varieties".
  - **SKU:** only when appearing in the flyer. Multibuy items need Postfix Text + Postfix Amount.
  - **Valid dates:** only include overrides when a promotion sale story indicates it.
  - **PC Optimum:** tag as a normal item; Sale Story includes the PC Optimum points (e.g. "Get 5,000 PC Optimum points when you buy a $25 gift card").
- **Image QC:** cleanest PDF (white/clear background); if shadows/lifestyle, "Do Not Use PDF Images." For meat/seafood/cheese, PDF only if **packaged**.

## Final QC & cloning (owned by Vendor / Flex)

- **Pre-Final QC (Flex, 3FL):** merge flap page(s) to the right (or with the cover if only one); thumbnails Standard 4 (1065x600 = 2pg, stock premium = 1pg, storefront carousel premium = 2pg, storefront carousel organic = 1pg) starting where the logo is, **excluding flap pages** even when merged.
- **Final QC:** confirm dates (Available Wed→Wed, Valid Thu→Wed, 1-week run), available everywhere, no preview date, internal run name "WEEK #", external run name set, no theme; Image QC (clean PDF except raw meat → cutout); thumbnails complete; pages tab item counts match tag QC; categories 1–2 per page except page 1; item view all boxed; Geography no change; run the T6C/R3P FSA guardrail; complete the FQC checklist.
- **Clone to Shop Easy Foods & Freshmart West:** Overview → Ad Hoc Processing → Clone → deselect SuperValu, select the target banner (Shop Easy Foods Weekly Flyer CQ5 / Freshmart Weekly Flyer) → **Copy to existing flyer run** (matching week) → set Copy Tracking Codes/URLs to **YES** → Clone.
  - **Shop Easy Foods clone FQC:** rerun Page Tile Generation; add stores to the SE-identifier PZ (Store Set "Shop Easy Foods", 13 stores as of Nov 2025) + the FR cross-language zone; leg heights 45/20; verify thumbnails/categories copied; sessions complete; item view correct; vertical preview OK; triggers set up; FQC checklist → item cutout generation marked as "Clone".
  - **Freshmart SV Clone FQC:** rerun Page Tile Generation; add stores to the FRESHMART-identifier PZ (Store Set "Freshmart SV Clone", 12 stores as of Nov 2025) + FR cross-language zone; confirm only the Freshmart logo on FRESHMART ONLINE; sessions complete; vertical preview OK; triggers set up; FQC checklist → item cutout generation marked as "Clone".

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by FLEX).
- **Page swaps** are standard, but always rerun Page Tile Generation afterward to avoid stitching issues (see risk items).

---
*Source: SuperValu (Shop Easy Food) / Freshmart OneGuide (Google Doc `1OpCYUmidGoqXxpAve1s7ZG2V5Em9BlKJOWToRcJ60IM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# SuperValu Liquor — Processing Guide

> **Source:** SuperValu Liquor OneGuide (Google Doc `18XyazsArRftkPRYSvZTvAKxN8Nw1VZ07myO209LwVdE`). Contacts/credentials omitted.

> Note: this OneGuide is largely on the standard template; the facts below are the real account details that were filled in.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Plus |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type | Flyer (Ad Hoc) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** ad-hoc. **Cadence:** ad-hoc (Available/Valid all ad-hoc).
- **Linking document required.**

## Upload & setup (owned by FLEX)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages → Edit → select all pages from the SFTP → Confirm & Upload. Auto-group or number pages; ensure correct language. Save & Confirm — do NOT process internally.
- **Pricing zones:** create a base pricing zone with all applicable pages; add all applicable stores.
- **Setup QC:** confirm all pages uploaded (no un-uploaded SFTP pages); confirm dates (usually first/last page); thumbnails Standard 4; preview dates set; **mass-attach the URL/linking document to all processing steps (Box, Tag, Tag QC).**

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot ON; linking doc used for both box/tag):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Box each product block with a price.**
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both box/tag):** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## Post-processing / Final QC (owned by FLEX)

- Item Image QC: PDF preferred if clean, cutouts otherwise.
- **Pre-Final QC:** confirm dates (from PDF) and availability toggles; thumbnails correct (include retailer logo); all items boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions complete; geography correct.
- **Final QC:** complete the FQC checklist.

## Flyer review

- **Flyer Review type: Lite** (owned by FLEX). Checks: flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: SuperValu Liquor OneGuide (Google Doc `18XyazsArRftkPRYSvZTvAKxN8Nw1VZ07myO209LwVdE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Surplus Furniture & Mattress Warehouse — Processing Guide

> **Source:** Surplus Furniture & Mattress Warehouse OneGuide (Google Doc `1vDL1vyWg7vQLt8oYjk_Ge9e6EAQizmz7dCPgpb9lT74`), updated Feb 17, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#surplusfurniture` |
| Hosted URL | surplusfurniture.com |
| Flyer type(s) & cadence | Weekly #1 |
| Processing | Auto-stack |
| Who's involved | Vendor owns upload/setup & FQC; Flex Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available Monday → Monday; Valid Sunday → Sunday.
- **Preview date:** Set preview 2 business days before live date.
- **Linking document:** Yes (used for both Box and Tag/QC).

## Upload & setup

- Download the codesheet, link sheet, and custom tile from the FTP (search "xls" for files, "jpg" for the custom tile).
- **Codesheet manipulations:** remove the first row and any pictures; save as `.csv`; upload using the full FTP path.
- **Codesheet errors:** ensure page names in the codesheet match the PDF names. Search the erroring name in the FTP: if not found, flag to retailer; if found, correct the name in the codesheet to match the PDF (and still flag so the mistake doesn't repeat).
- Mass-attach the link sheet to all vendor tasks (no manipulation). Attach the tagging doc to all vendor guides (no manipulation).
- **Custom tile (JPEG):** send in `#surplusfurniture` for BD as soon as received; used as custom thumbnails for premium.

### ⚠️ Common errors (retailer-specific)
- **Before Setup QC you MUST force all pages different:** Flyer Run Overview → Special Actions → "Force All Pages Different." All store locations receive a different flyer with some different prices. Confirm you get the notification that pages were forced different.

### Setup QC
- Available = Everywhere; external name from the email callout or link sheet; no theme.
- Leg heights 55/45. Thumbnails Standard 4 **plus custom tile** for Storefront Carousel Premium & Storefront Premium (apply the custom tile to all PZs; refresh to see the new thumbnail).

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required)**
- Include: retailer logo, sign-up page, social media, special weblinks. Exclude: coupons, packaged deals.
- **Special weblinks/banners:** box any banners/callouts noted in the linking document (e.g. "Don't Pay Until 2027!", "Same Day Delivery!", HOT BUY recliners, etc.).
- **Social media:** box and tag all social icons (usually at the end of the linking document). Facebook/Instagram/YouTube/TikTok links per the guide.
- 1 price / 1 SKU / 1 image → 1 box. Multiple prices, 1 image → 1 box.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required)**
- Include: name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates.** No brand.
- **Tagging steps:** check the page description → open the attached spreadsheet, find the tab matching the page name → match by Name or SKU → tag all product info directly from the spreadsheet (not the flyer), **except price**.
- **Price:** tag from the flyer. If the PDF price differs from the spreadsheet, use the PDF price.
- Special weblinks/banners: Display Type = Link; Name and URL per linking document.
- **Common error:** Current Price must reflect the "main" advertised price, not one of the listed size/price options — those go in the sale story.

**Image QC:** No image QC for this retailer.

## Final QC / go-live notes

- **URL/Links QC:** Overview → items without URL; work through them with the link sheet (one PZ's links apply across all PZs — they're the same).
- **FQC (Flex-owned):** vendor tasks complete; run **Set Cutout Images** custom action (Custom Actions → Set Cutout Images → enter Flyer Run ID → Complete Action).
- Check items without URL against the link sheet; link the rest to the retailer website. Verify URLs; **Mark Items In-Store Only** only after checking items without a URL.
- Horizontal/vertical checks; page categories (OS can't tag — add at least 1/page: Mattresses = Bedding; Bed Frames & Dressers = Bedroom).
- Dates per email; Available = Everywhere; external name = callout in link sheet; no theme (usually). Leg heights 55/45; thumbnails Standard 4 + custom tiles.
- **Flyer Review type: Lite.** Page swaps are standard (baseline video).

---
*Source: Surplus Furniture & Mattress Warehouse OneGuide (Google Doc `1vDL1vyWg7vQLt8oYjk_Ge9e6EAQizmz7dCPgpb9lT74`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Sutherlands — Processing Guide

> **Source:** Sutherlands OneGuide (Google Doc `1Ppz_xRoey75RYpEdbCm8ZOC5tuv_bN1ovnWezX0NOkY`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | N/A |
| Availability | All platforms |
| Slack channels | `1plat_sutherlands` |
| Hosted URL | sutherlands.com |
| Flyer type(s) & cadence | Flyer Type 1 — Biweekly |
| Processing | Auto-stack |
| Who's involved | Vendor upload/setup; DOC FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available From Wednesday; Valid From Tuesday.
- **Preview date:** N/A.
- **Linking document:** Yes (used for both Box and Tag).

### ⚠️ Risk items
- **Links QC:** QR codes must be boxed and tagged per the linking document.
- **Image QC:** select as many white-background images as possible; if images are lifestyle, prefer those over cutouts.

## Upload & setup

- Files drop directly into the SFTP with a "READ ME" document breaking down the versioning (usually the same each ad).
- Folders include the **month and year** of the ad (e.g. `/2408 kccamyjj books`). The linking document is an XLS labelled **Tab #** (e.g. `Tab 8 Links`); all FAdmin flyer runs include the Tab # in the name.
- Download the corresponding linking document. In the flyer run: Pages → Edit → find the folder for the weekly files. Each file set is labelled by the store set it serves (**CAMY, JJ, KSGP, SUHU**); some ads don't include all 4 versions — upload whatever versions are provided.
- Upload all pages → Auto-group → English only → Save + Save As (once indexing is confirmed).
- **Flyer creation:** separate zones per page set (CAMY, JJ, KSGP, SUHU); upload the corresponding pages into each version; assign stores to matching store sets.
- Attach the linking document to all tasks.

## QC specifics

**Box Draw (Medium; Auto-Box OFF, Box QC bot OFF; linking doc used for both Box/Tag)**
- Include: special weblinks. Exclude: coupons, packaged deals, retailer logo, sign-up page, social media.
- Box QR codes: Family & Friends, Credit Card/Financing, In-store Pickup, and general QR codes.

**Tag / Tag QC (Low; Auto-tag OFF)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for both Box/Tag.
- Tag "After Reward" pricing. Tag QR codes with their URLs:
  - Family & Friends → `sutherlands.com/friends`
  - Credit Card/Financing → `sutherlands.com/credit-card`
  - In-store Pickup → `sutherlands.com/in-store-pick-up`

## Final QC / go-live notes

- **URL/Links QC (DOC):** open the linking document (attached to vendor tasks or from FTP). Overview → "Items without a URL"; cross-reference by SKU or item name. If an item isn't on the doc, leave URL blank; otherwise apply the link.
- **Pre-FQC (DOC):** confirm dates vs PDF; availability toggles; thumbnails include the retailer logo; legibility heights 60/40. Standard checks: all items boxed/tagged; spotchecks (20% of PZs); previews published/clickable; sessions complete; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Sutherlands OneGuide (Google Doc `1Ppz_xRoey75RYpEdbCm8ZOC5tuv_bN1ovnWezX0NOkY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
