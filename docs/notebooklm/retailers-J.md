# Retailer Processing Guides — J

> Bundle of 6 retailer-specific processing guides (J). Contacts and credentials are omitted from every guide.

**Contains:** JB's Power Center, JCPenney, Jean Coutu, Joe Fresh, Joe V's Smart Shop, JYSK


---

# JB's Power Center — Processing Guide

> **Source:** JB's Power Center OneGuide (Google Doc `14ReNG8IV5IY4MZ9L4mq4fYoK90f1T1TQD9FyaFG6CVg`). Contacts/credentials omitted.
>
> ⚠️ This OneGuide is largely an unfilled template. The real account facts captured below are limited; detailed step-by-step instructions were not filled in.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#JBs-power` |
| Flyer type(s) & cadence | Flyer Type 1: **Weekly** · Flyer Type 2: **Monthly** |
| Processing | Trim Stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Monday → Monday; Valid Tuesday → Tuesday.

## Upload & setup (owned by Flex)
- Create shells for each flyer that comes in (dates are not always start-to-end of month).
- Manual upload all pages.
- Create **one pricing zone** and assign all stores.

### Setup QC
- Vendor task → mass attachment: upload the flyer link file to all vendors (no manipulation).
- Check dates; no theme or external run name; available everywhere.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required)
- **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- **Include** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude** pre/postfix, valid dates.

### Image QC
- Choose white-background PDF image where possible; else use cutout.

## Post-processing / FQC
- **Item Category QC (Flex):** confirm items have a Google and analytical category.
- **Item Image QC (Flex):** prefer white-background PDF; else cutout.
- **URL/Links QC (Flex):** for items without a URL, check against the tagging document and add the link where needed; otherwise leave blank.
- **Ad-hoc QC (DOC):** complete Standard 4 thumbnails; check PDF dates match the flyer run.
- **Flyer Review type: Lite.**

---
*Source: JB's Power Center OneGuide (Google Doc `14ReNG8IV5IY4MZ9L4mq4fYoK90f1T1TQD9FyaFG6CVg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# JCPenney — Processing Guide

> **Source:** JCPenney OneGuide (Google Doc `1ls1tJRSfaZ_xgJHcU7xP-YZY4HvZsGrs-BNTDBZqzNo`), updated Feb 10, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard / Core+ |
| Availability | Hosted only (2501); Flipp & Distro clone (7729) |
| Slack channels | `#jcpenneyops`, `#jcpenney`, `#jcpenney_mergil`, `#jcpenney-sep`, `#jcpenney-gma` |
| Hosted URL | jcpenney.com/m/digital-books |
| Flyer type(s) & cadence | **Mailer (2501)** — Hosted, all processing done here · **Mailer (7729)** — Flipp/Distro clone. **Ad-hoc** cadence. |
| Processing | Auto-stack |
| Who's involved | DOC does all processing; no Flex; Strategic Ops (retailer data services) |

## Files & schedule
- **Files received:** Ad-hoc (dates confirmed in the assets email). Store Ads / Circular publications are managed and processed by CP, not here.
- **Publication cadence:** all dates ad-hoc. **No customer preview** — internal/client preview set for **5 business days after files received**.
- **SKU document** is included in the assets email — it must be manipulated, emailed to OS, and attached to vendor tasks.
- **Schedule:** an emailed monthly schedule drives shell creation. Create flyer shells under **both** flyer types using the schedule dates (add " - Flipp" to the internal name of Flipp/Distro shells). Populate Flyer Run ID and Direct URL columns; return the updated schedule.

## Upload & setup

- **Assets** delivered via Egnyte: PDFs, pagination instructions, event code (= external run name), coupons (0-3 PDF versions), optional data sheet. Types: Mailer = hosted, Mailerflipp = flipp (**upload the hosted version first**).
- If Page 2 has coupons / an online-coupon link, it's often moved to the end of the flyer before the standard last pages.
- **Upload:** manual-upload all individual pages, index per instructions. One PZ "Base"; assign all stores and **remove Puerto Rico stores**.
- **Setup — dates (CST):** Available from 1 AM; Available to 12:59 AM the next day; Valid from 1 AM EST; Valid to unchanged. Confirm PDF dates match the schedule.
- **Toggles:** Hide on Flipp & Distro (Hosted only). **Theme: never apply to the Hosted clone (no theme always).** Set vendor tasks to HIGH.
- **SKU doc manipulation:** keep headers `page_name, sub, lot, feature_description` (delete other columns); remove rows with no sub/lot or description; add a `sku` column with `=TEXT(B2,"000") & "-" & TEXT(C2,"0000")` and paste as values; delete blank/0-SKU rows; rename pages if desired; save as `JCP_<adname>_skulist`; attach to tag & QC; email OS if there are special tagging instructions.

## QC specifics

### ⚠️ Risk items
- **Coupons:** "JCPenney" must be tagged in the **Brand field** so the coupon appears in the JCPenney search-results dashboard on Flipp Web.
- **Vertical publishing:** confirm vertical published via the Storefront Summary page.
- **Flyer sorting:** most recent on top; Store Ads over Puerto Rico over Mailers.

### Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required)
- **Include** coupons, packaged deals, sign-up page, special weblinks. **Exclude** retailer logo, social media.
- Box: JCPenney App, Shop 24/7 at jcp.com, Fast + Free Same-Day Pickup, Special Financing, Coupon Direct Link, barcoded coupons (text box required for disclaimers/fine print). Exclude the JCPenney logo and Viznav/category pages.
- **Jewelry flyers:** if unclear what image relates to which price → box together; multiple prices lumped despite indexed items → box each pricing group; one price / multiple item sets → box each set with a "text" box over the price.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Jewelry:** one image / price range → tag prices as a RANGE listing all SKUs; multiple items in one box with one price → tag the price + title and add SKUs; one price / multiple items → tag by center title and price, SKUs from the images.
- **Coupons spotcheck:** item type Coupon; Brand JCPenney; Name "Featured Coupon"; apply override dates for Hosted; Categories = coupons & coupon; Category highlights = coupons; Google Category = Not Available.

### Image QC
- No image QC (Hosted 2.0); leg heights inconsequential.

## Post-processing (DOC)
- **Back cover line items:** if present, make front-cover images interactive using the back-cover tagging info.
- **Disclaimers:** ensure flyer-level "book disclaimers" aren't applied to adjacent items.
- **Coupons:** upload hosted image to S3 (OLPP, JPG); QA copy vs. PDF, "82" in Hosted barcode, discoloration; tag by copy/paste of the hosted image URL + apply override dates; add category copy to the right coupon's sale story. SFSC: 1 page/slice; include online code in the MAIN slice (do not hide in disclaimer); last page products on top, app callouts on bottom.
- **Item Category QC:** iFrame preview — QA that listed categories are actually in the ad and each links correctly.
- **Original Price QC:** item search Original Price is not blank — remove manually (small) or via item export/import (large).
- **SKU QC:** item search SKUs containing "/" → remove the "/" and the 3 numbers following (e.g. `272/472-8099` → `272-8099`); large batches via export/import find-and-replace.
- **URL/Links QC:** standard week-over-week URLs (Financing home/mattress, Jewelry financing, App, Curbside Pickup, Rewards — full URLs in the OneGuide); **Viznav page** category URLs change by mailer type — copy items from the most recent flyer of the same type via Pages → Copy Items.
- **Tracking codes:** Overview → Manage Tracking Codes at flyer-run level, dynamic variable, hosted, `utm_source`; change the two highlighted URL portions to match the pub name; Apply All Tracking Codes. **Must put `utm_source` in the tracking codes** or the utm code inserts in the wrong spot.
- **FQC:** normal checklist; **ignore "tracking URLs applied" and MISO**.

## Post-FQC → JCP review → clone
- **Item export:** remove flyer items; keep item_id, page, name, sku, url, description; **remove all coupons**; QA page numbers; add vertical preview URL to the top; save as XLS.
- **Preview link to JCP:** send export + preview link with the URL due date (in red/bold); note that changes in other columns must be highlighted.
- **Item import:** ~2 days to action & clone; changes highlighted yellow; item import (item_id, sku, url) as CSV with sku column cleared; re-verify URLs; re-apply tracking codes; confirm direct links become "Link" format.
- **Clone (2501 hosted → 7729 flipp):** into existing shell; check dates, toggles (Hidden in Hosted), external run name (EN only, from "event name"), theme (not applied to Hosted). Clone coupon if Flipp/Distro-specific (different barcode) — override images for all 3 platforms with the Flipp (84) JPEG, draw barcodes per interactive area, add valid override dates, tag "JCPenney" in Brand. Clone tracking codes (code #1 app, code #2 native). Clone FQC: normal checklist + confirm vertical published via Storefront Summary.
- **Flyer Review type: Lite.**

---
*Source: JCPenney OneGuide (Google Doc `1ls1tJRSfaZ_xgJHcU7xP-YZY4HvZsGrs-BNTDBZqzNo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Jean Coutu — Processing Guide

> **Source:** Jean Coutu OneGuide (Google Doc `1KXiPmAL_bT6hTFwHewajOlfdYFRyASDynayIjL1OPPs`), updated Jul 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Core+ |
| Availability | All platforms (**not on our Hosted**) |
| Slack channels | `#flex-processingsupport` (retailer channel per OneGuide) |
| Hosted URL | Not on our hosted |
| Flyer type(s) & cadence | **Weekly Flyer** (Flyer Type 1465) · **Health & Beauty Flyer** (weekly) · **Special Insert** (ad-hoc) · **Cosmetics Insert** (ad-hoc). Bilingual EN/FR. |
| Processing | Auto-stack |
| Who's involved | DOC (Upload/Setup + FQC); Flex (Flyer Review); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Wednesday.
- **Publication cadence:** Available Tuesday → Wednesday; Valid Thursday → Wednesday.
- **Linking document:** required for **weekly runs** (attach for tagging).

## ⚠️ Risk items
- **"Missing in Hosted" error (all flyer types):** do NOT mark as missing in hosted — Jean Coutu isn't on our hosted but can't be hidden in hosted due to their app.
- **Supplementary linking in FQC:** the retailer strongly emphasizes ecomm — links are flagged in the codesheets multiple times; adding them is highly important.
- **Weekly ad linking:** links and SKUs are added by vendors during processing — you **must** attach the linking document for tagging.
- **Sale Story (EN):** when the flyer says "**Save x%**", tag it as "**x% Off**" (NOT "Save x%"). When it says "Save $x", tag as "Save $x". Tag dollar-off and percent-off differently.
- **New Jul 13, 2026:** there should be **no staggered dates** — if the codesheet creates staggered dates, update them to match the flyer shell dates.

## Upload & setup (owned by DOC)

### Codesheet setup
- Codesheet arrives via email (attached to the ClickUp task). In the first tab, the headings below the yellow flyer types show which flyers run that week (almost always at least **Weekly Flyer** and **Health & Beauty Flyer**). Shells are pre-built for those two; if there's a "special insert" in the codesheet with no ClickUp task, flag to CXE.
- Copy the full flyer-run names from FAdmin into the matching cells.
- Under "Health & Beauty Flyer", adjust file-name dates from **YYMMDD to DDMMYY** (H&B only), e.g. `PJC_CIRC_SB_NB_260708` → `PJC_CIRC_SB_NB_080726`.
- **Suivi tab:** delete the "No.PDF" cell and the column below "Page No" (shift left) to make one column; ensure page naming matches the sFTP (H&B page names often have dates reversed, e.g. 070319 vs 190307) — any name change must be made on **both the suivi tab and the first tab**; double-check the years in columns B-D. Download as xlsx.

### Running the codesheet
- Same for all flyer types: open each flyer run → codesheet → upload the .xls, **config name `jean_coutu`**, PDF base directory = the date-code file path from the sFTP (e.g. `/241024/`), **check Store Assignment and Page Upload**.

### Linking document
- A "Bottin" file is dropped in the sFTP. Manipulate: delete columns A, B, D, G; rename "Groupe produit F7" to "SKU"; save as XLSX; attach to all vendor tasks.

### Thumbnails
- Standard 4 thumbnails, **1 page only** (no 2-page thumbnails for horizontal layouts), no whitespace.
- **Weekly Flyer only** uses **custom tiles** to replace the Storefront Carousel Organic thumbnail — find them in the sFTP (search THUMB/THUMBNAIL, correct date folder), download locally, and override in Thumbnail QC. Recommended: do ON or NB first, QC thumbnail last.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each item block (one box even if several items share a block); use text boxes when product info isn't neatly aligned; **box all disclaimer text**.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc for weekly runs)
- Include brand, name, pre/postfix, valid dates, description, SKU (new), price, sale story, categories, disclaimer, original price, URLs (new).
- **Brand/Name:** brand as listed (if multiple brands, leave brand field blank); name = Brand + product, brand in ALL CAPS even if lowercase on the flyer; for multi-item boxes also put the brand in the description.
- **SKU (Weekly Flyer only):** from the text-extraction box, a 1-4 digit number (e.g. 205).
- **URL (Weekly Flyer only):** add the appropriate URL for each item from the linking document; not all products get a URL each week.
- **Disclaimer — Pharmaciens propriétaires:** items inside the green "Pharmaciens propriétaires" box get the special pharmacy disclaimer (copy/paste the full EN or FR text from the OneGuide) — applies only to products between the two blocks.
- Tag disclaimer/description text in the correct language only (EN text on EN, FR text on FR).

### Image QC
- Select the image that best matches the product; if multiple products, select one specifically. **If the photo has a black background (not clean), do not use the image extraction — leave it as a cutout.**

## Post-processing / FQC (owned by DOC)
- **Disclaimer QC (QC versions only):** find pages with the "Pharmaciens Propriétaires" heading and ensure all products in the boxed area have the disclaimer.
- **Thumbnail QC:** follow the Thumbnails steps if not done at setup.
- **Flyer sorting:** CIRC REG newest → CIRC REG older → Health & Beauty newest → Health & Beauty older → then inserts newest → oldest.
- **FQC (weekly):** check % of SKUs & URLs added (item search SKU/URL not blank — **over 75% acceptable**); add CTA links from the Feuille de Suivi (Suivi tab column F); check pharmacy disclaimers via storefront spotchecks. H&B and other inserts: add CTA links + check disclaimers.
- Remove any staggered dates (see risk items).
- **Flyer Review type: Lite.**

---
*Source: Jean Coutu OneGuide (Google Doc `1KXiPmAL_bT6hTFwHewajOlfdYFRyASDynayIjL1OPPs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Joe Fresh — Processing Guide

> **Source:** Joe Fresh OneGuide (Google Doc `1e9nT1andXst6-dpFYmTpyCLbSESr-q8mt8d9KAMtZiU`), updated Jul 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | **Flipp only** (we do not power their Hosted) |
| Slack channel | `#joefresh-lcl` |
| Flyer type(s) & cadence | **Lookbook** — ad-hoc ads, normally Thursday → Wednesday |
| Processing | Auto-stack |
| Who's involved | DOC / Flex; no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Tuesday (sent directly by the retailer contact — **not uploaded to the SFTP**, download locally).
- **Publication cadence:** Available/Valid roughly Thursday → Wednesday; refer to the file-drop email for accurate dates (some pages have varying valid dates — run starts at the earliest date mentioned and ends at the latest).
- **Content Calendar** holds available/valid dates + pagination (logo page always indexed #1). BD requests shells be built once budget is confirmed (usually a month or two at a time).

## Upload & setup (owned by DOC / Flex)
- Manual upload; reference the Content Calendar for pagination (page order top → bottom).
- **Back page** is applied week-over-week but the retailer does **not** resend it — download from the Joe Fresh drive and manually upload as the **last** page.
- Flyer Creation: one **Base** pricing zone with all pages, order per the Content Calendar. Some pages have different valid dates — add all pages now and set **triggers** for removal. Add all stores.
- **Link Tagging Sheet:** build from the Content Calendar (each page has its own tab). Headers: Page #, Item Name, Produce URL, UTM. **Use only the UTM column** (has tracking codes) — not the URLs column. Copy Page #, Item Name, UTMs into the Joe Fresh Linking Document; adjust Page #s to match the PZ order; include the Backpage tab links. Download as .xlsx and attach to all vendor tasks.
- **Custom tiles ("App Tile", .jpg in the submission email):** upload to Storefront Premium and Storefront Carousel Premium on the QC Thumbnails page (**override** the thumbnail). Timeline may differ from run dates — set live from the first date with a trigger; file a ticket if it must come down early. If more than one tile, use triggers to alternate. Create tickets for yourself/Flex to check triggers.
- **Content policy:** 3 items per page; custom tile must have a sales story + logo + 2 shoppable items/product imagery.

## ⚠️ Risk items
- **Items without a URL / non-UTM links:** all items need a link and all links must be UTMs. Item search "URL does not contain UTM" — investigate any results. (Skip if you only gave OS the UTM column.) Links must correspond to the right item pages on joefresh.com/ca.
- **Back page:** included at the end of each publication; each category clipped and given a link.

## QC specifics

### Box Draw (Low; Auto-Box ON)
- **Include** special weblinks. **Exclude** social media, coupons, sign-up page, retailer logo, packaged deals.
- In Box QC, confirm boxes exist for all items and links in the Linking Document — **especially Shop Now links**.

### Tag / Tag QC (Low)
- **Include** brand, name, description, price, sale story, categories, original price, URLs, valid dates (if applicable), pre/postfix (if on PDF), SKU (if provided). **Exclude** disclaimer (unless inside the drawn box).
- **URLs:** use the UTM from the Tagging Document. If no URL is provided, find the item on joefresh.com/ca and use that link; if not found, leave blank.
- Original price included if the flyer marks down the item; every item needs a category.

### Image QC (Pre-FQC)
- PDF image where possible (PDF extraction often has a black background — do not select those); if cutout, avoid awkwardly boxed cutouts. Standard 4 thumbnails (ensure JF page-1 logo included; center the logo on 1-page tiles).

## Post-processing / FQC (DOC / Flex)
- Leg Heights **45/25**; quick Image QC; assign Standard 4 thumbnails; verify custom tile applied; item search for UTM links (skip if only UTM column sent to OS); "Items Without a URL" check (assign from the UTM column); check the email for promo inserts with specific dates and create triggers; **Available on Flipp only** (Hosted not set up — hide on hosted to avoid a Live Check flag); no theme (except Black Friday / Holiday).
- **Flyer Review type: Lite** (owned by Vendor).

## Out-of-processing
- **Page swaps** are standard (baseline page-swap video), owned by DOL.

---
*Source: Joe Fresh OneGuide (Google Doc `1e9nT1andXst6-dpFYmTpyCLbSESr-q8mt8d9KAMtZiU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Joe V's Smart Shop — Processing Guide

> **Source:** Joe V's Smart Shop OneGuide (Google Doc `1V4MazvRLm8vXaKKDwiao_SPIuoOPe1bebYZiYio3k7o`), updated May 23, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channel | `#heb` |
| Hosted URL | joevsmartshop.com/weekly-ad/antoine-dr-houston |
| Flyer type(s) & cadence | **Weekly** |
| Processing | Auto-stack |
| Who's involved | DOC (Upload/Setup + FQC); Flex (Processing Support + Flyer Review); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Thursday.
- **Publication cadence:** Available Tuesday → Wednesday; Valid Tuesday → Tuesday.

## Upload & setup (owned by DOC)
- **Manual upload:** Pages → Edit → select all pages from the SFTP → Confirm & Upload → auto-group or manually number (ensure correct language) → Save & Confirm. **Do NOT Process Internally.**
- **Pricing zones:** create **2 PZs — 100 and 200**. Add the two "100" pages to the 100 PZ and the two "200" pages to the 200 PZ. "Add all" stores in store set 100 → 100 PZ; store set 200 → 200 PZ.

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone → Items View) — **RISK:** if uploading from SFTP, confirm no SFTP pages were missed.
- Confirm flyer dates (usually first/last page); complete Standard 4 thumbnails; download the `WeeklyAdInfo.xlsx` file (e.g. `0522_WeeklyAdInfo_JoeVREV.xlsx`) from SFTP and mass-attach to all vendor tasks; set preview dates; complete Setup QC checklist.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc used for Box+Tag)
- **Include** packaged deals. **Exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- Clean boxes around each set of items; every unique item boxed.
- **Red italic text:** if another product is listed in red italics (product-text comparison), box the text separately.

### Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude** URLs.
- **Name/Brand:** product names in Name, brand names in Brand. Multi-item: separate names/brands with "OR". **BOGO deals:** the product that must be purchased to get the free item goes in the Name.
- **Description:** as on the flyer; text in (brackets) → **Disclaimer**, not description; correct misspelled "assorted varieties".
- **Price/Prefix/Postfix:** as in flyer (e.g. Prefix "2 for", Postfix "with in-store coupon").
- **Sale Story:** items with a generic "save" message (no price) → Sale Story. BOGO → full text in sale story (don't also add "Save up to…"). "SAVE UP TO" → include in sale story but leave dollars/percent-off blank.
- **Valid dates:** if printed dates match the flyer valid date, leave item valid from/to blank; **watch for 1-3 day sales** and enter those in valid dates.
- **Disclaimer:** enter only if within the drawn box; limits go in Disclaimer (not description); do **not** include "Look for H-E-B PRIMO PICKS tag at the shelf".
- **Promo ID & Unique Promo ID:** every item on every page has a Promo ID and a Unique Promo ID — from the pipeline spreadsheet, filter by the PAGE column, match the item via the DESCRIPTION (Column C), tag the PROMO ID (Column B), then find the Unique Promo ID (Column E).
- **Incorrect:** red text before names should **NOT** be tagged.

### Image QC
- **Predominantly cutout images used.** PDF preferred otherwise; for bundles, choose the cleanest single-item image.

## Post-processing / FQC (owned by DOC)
- **Pre-FQC:** confirm dates (from PDF), availability toggles, thumbnails (include retailer logo), all items boxed/tagged, spotchecks (20% of PZs), previews published & clickable, sessions complete, geography correct.
- **FQC:** Geography (no stores added); Vendor tab (linking doc attached); Sessions run; Pricing Zone (everything boxed, check horizontal & vertical scroll); Pages tab page categories (page 1 no category, page 2 add categories seen). Edit Details: Available Tues-Tues, Valid Wed-Tues, Internal Run Name DD-MM, Preview Start Date n/a, available everywhere, no theme. Leg heights 40/30 (preset); QC thumbnails Standard 4; Item Image QC (PDF preferred, else cutout — sometimes need "Generate Data Piping Groups").
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Joe V's Smart Shop OneGuide (Google Doc `1V4MazvRLm8vXaKKDwiao_SPIuoOPe1bebYZiYio3k7o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# JYSK — Processing Guide

> **Source:** JYSK OneGuide (Google Doc `1uw47tJzpdnJWYUPBNPOpSug3xv06RaTpoMg7a06r2bs`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | **Flipp only** (Flipp does not power JYSK's Hosted) |
| Slack channel | `#jysk` |
| Flyer type(s) & cadence | Flyer Type 1: **Flyer** · Flyer Type 2: **Grand Opening**. Bilingual EN/FR. |
| Processing | Auto-stack |
| Who's involved | Vendor (Upload/Box/Tag); DOC (Links QC, FQC); Flex (FAB tickets / Flyer Review); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Thursday.
- **Publication cadence:** Available Thursday → Wednesday; Valid Thursday → Wednesday. No preview dates (Available = Valid).
- **Linking document:** yes.

## ⚠️ Risk items
- **Linking errors:** many items share the same name — ensure links are added properly. **Check links during FQC.**
- **"Flyer not available on Hosted" is always a FALSE error** — Flipp doesn't power JYSK's Hosted; do not check their Hosted webpage.
- **Missing the French `&___store=fr` URL manipulation is a known cause of upload/save failures** (ref [OTS-2334](https://flippit.atlassian.net/browse/OTS-2334)). Before upload, confirm the FR URLs actually carry `&___store=fr` — QC against the **manipulated** links doc, not the raw file from the SFTP (comparing against a previous week's *raw* doc is a common trap). See "URL document manipulation" below.

## Upload & setup (owned by Vendor)

### Before upload — URL document manipulation
- Download the links file from SFTP (usually .csv); open in Google Sheets; rename the sheet to "[FLYER NAME] URLs" (e.g. "1089 JYSK URLs").
- In column D, add **EN** after "Flipp" to indicate English URLs.
- For French links, add **`&___store=fr`** to all FR links: paste `&___store=fr` into column E beside FR URLs; in column G use `=CONCAT(D2, E2)` to combine; autofill down; copy the new FR URLs and paste **Values Only** into column F; delete columns F and G.
- Save as **.xlsx** and attach to all vendor tasks during upload.

### Upload
- Manual upload; change language for French files (indicated by "F" in the name); Save (not Save and Complete). Then Auto-Group → Save and Complete (should look like a zipper).
- **2 PZs — English and French**; add all stores for both. Check sessions. Upload the links xlsx as a mass attachment to all vendors.

### Setup QC
- Ensure hidden in hosted; PDF dates match FAdmin; no preview dates (Available = Valid); Legibility Heights **40/30**; mark Setup QC complete.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc for box)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Box/tag separately** items advertised together but with separate names (e.g. a chair and a table in a set) — check the linking doc has 2 links.
- Items that share a name but have **different prices** must be boxed/tagged separately (e.g. FYN 3 tiroirs / 5 tiroirs / 4 tiroirs; COLTON at 3 prices). Some items don't have a corresponding image on the flyer — **still box and tag them**.

### Tag / Tag QC (Medium; Auto-tag OFF; PDF image auto-selection ON; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **⚠️ NEW 6/20/25 — Name rules (drive automations):**
  - Always tag the **bold word first** in the Name (EN and FR) — may mean adjusting the text-extraction box. E.g. "SUNI Outdoor placemat" / "SUNI Napperon extérieur".
  - When there's a slash in the name, **include the space** around it: "HEDEENGE / KELDMOSE Coussin de chaise".
  - Always include the **Brand name first** in the Name even if not visible in the box: "DUNBAR NIGHTSTAND" (not "2 Price NIGHTSTAND").
  - Use the brand printed **alongside** the item name, not text from another brand logo image.
  - Lists of names: **space after the comma** ("Hallgerd, Inhome").
- **URLs:** watch items with the same name but different numbers — the link may carry the matching number.

## Post-processing / FQC
- **URL/Links QC (DOC):** check for FR links on EN flyers (item search URL contains `&___store=fr` + Language English → swap to EN links). Check for name repetition in the link sheet using conditional formatting `=countif(B:B,B1)>1`; verify links for repeated names against page numbers in the URL.
- **Ad-hoc QC (DOC):** check all items are boxed.
- **FQC (DOC):** Standard 4 thumbnails; check items without URL; **mark items in-store only**; complete standard FQC checklist.
- **Flyer Review type: Lite** (owned by Flex).

## Out-of-processing
- **Day of go-live:** the external ops contact sends any link changes — make the adjustments and confirm. See the JYSK Clipping Instructions doc.

---
*Source: JYSK OneGuide (Google Doc `1uw47tJzpdnJWYUPBNPOpSug3xv06RaTpoMg7a06r2bs`). Contacts/credentials omitted. Last reviewed: 2026-08-10.*
