# Retailer Processing Guides — K

> Bundle of 13 retailer-specific processing guides (K). Contacts and credentials are omitted from every guide.

**Contains:** Kent / KentPro, Key Food Supermarket, Kim Phat, King Kullen, Kinney Drugs, Kitchen Stuff Plus, Kj's Market, Kohl's, Korna Natural Pet Supplies, Korvette, Kosher (Sobeys), Kroger, Kubota Canada


---

# Kent / KentPro — Processing Guide

> **Source:** Kent/KentPro OneGuide (Google Doc `1dHVOfwrLfE57KVrC0hOqbmGAA8dN-4Si3F6hshC8Uwc`), updated Mar 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#kent-building-supply` |
| Hosted URL | kent.ca/en/flyer |
| Flyer type(s) & cadence | **Weekly** flyer · **KentPro Monthly** (clone of Kent into the KentPRO retailer) |
| Processing | Auto-stack |
| Who's involved | Flex (Setup, Image QC, FAB tickets); DOC (FQC, category/URL/SKU QC); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

### Weekly
- **Files received:** Friday.
- **Publication cadence:** Available Wednesday → Tuesday; Valid Thursday → Thursday.
- **Preview:** 1-day consumer preview (Wednesday); 2-day merchant preview (Monday).

### Monthly (KentPro)
- **Files received:** Monday.
- **Publication cadence:** Available Friday → Monday; Valid Wednesday → Tuesday.

## ⚠️ Risk items
- **Valid dates:** page/item-level overrides are frequently missed.
- **Sales story** frequently missing.
- **URLs** often go to the correct item but the **wrong colour**.
- **Original price:** watch the original price field — description reads "Was: $$$" / "After flyer price: $$$".
- **Link callouts:** box and tag all "buttons" for Financing, Online-Only Deals, and E-Newsletter flaps with the links in the linking document.
- **SKU:** if multiple SKUs are listed (e.g. `6732406, 401`), include **only the first** (`6732406`).

## Upload & setup (owned by Flex)

### FTP transfer
- Kent sends files to their **external FTP**. Log into the FTP agent (FileZilla/CoreFTP), download Kent's weekly files, then connect to Flipp's FTP and upload them. (See the Kent Processing Notes doc for external FTP access.)

### Codesheet upload
- Download the Digital Plating Document (email); open a Generic Code Sheet Template; copy all page PDFs from the Digital Plating Document → paste as values into the generic codesheet and update store sets.
  - **DPT zones:** `11zones_DPT_NB`, `11zones_DPT_NS` (or `*DPT_NS_WITHMETRO` if a METRO PZ is in the digital plating), `11zones_DPT_PEI` (only if no DPT PEI PZ listed).
  - **COM zones:** `11zones_COM_NB`, `11zones_COM_NS`, `11zones_COM_PEI` (only if no COM PEI PZ listed).
  - **COM BIL zones:** `11zones_COM_BIL`, `11zones_EDM_BIL` (only if no EDM BIL PZ listed).
- Copy pagination into FR zones (same steps); download as .csv.
- Codesheets: choose file, **config name `generic_language`**, path from FTP, **toggles 1, 3, 4, 6**.
- Download the links document; once codesheets/sessions complete, attach the linking document to all vendor tasks.

### Setup QC
- Dates correct; 1-day consumer preview (Wednesday); 2-day merchant preview (Monday); not hidden anywhere; no theme; pages correct. Note "Setup QC complete, Linking document attached".

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF weekly / ON monthly; linking doc required)
- **Include** packaged deals, special weblinks (monthly also includes retailer logo, sign-up page, social media). **Exclude** coupons, retailer logo (weekly), sign-up page (weekly), social media (weekly).
- Box all items with prices or sale stories separately (draw text boxes when needed; match text boxes to image boxes — often several versions in one promotion). Box all **link callouts** for Financing, Online-Only Deals, and E-Newsletter ("Click Here to Apply", "Yes, Sign Me Up", "Shop Now").

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude** disclaimer.
- **Name/Brand/Description:** as in flyer; if no description on the flyer, tag as in the spreadsheet; do not include SKU in the description.
- **Price/Original Price:** as in flyer; if none, use the spreadsheet; **original price is at the end of the description after "was"**.
- **Pre/Postfix:** as in flyer; when EN+FR on the page, English postfix is listed first, French second.
- **SKU:** listed in brackets at the end of each item's description; if none, use the spreadsheet; **only the first SKU** if multiple.
- **Valid dates:** enter override dates if applicable.
- **URLs:** if the spreadsheet has prices, use it; otherwise search the SKU on kent.ca, open the item, copy the URL (correct language for EN/FR); tag all linking-doc links to the callouts on the indicated pages.
- **Sale Story:** generally in a red/yellow banner above the price; on FR pages use French text, but where only English exists (e.g. "Save $150") use the English sale story.
- **Disclaimer:** only if within the drawn box.

### Image QC
- Only select the extracted image that best applies; if no clean images, use the cutout.

## Post-processing / FQC (owned by DOC)
- **Item Category QC:** every item needs a category — use the Kent category matrix (Christmas, In Season, Lighting, Household, Tools & Hardware, Lawn & Garden, Furniture, Roofing, Kitchen, Paint/Stain, Home Décor, Decks, Siding, Heating, Flooring, Bathroom, Building Supplies, Windows).
- **URL/Links QC:** open the linking doc; item search URL IS BLANK + Language English → fill blanks (leave blank if the doc has no link); repeat for French; use Page Grouping Index and SKU filters to edit matching items across versions at once.
- **SKU QC / FQC:** Item Image QC (cutouts/no-images/unreviewed only); Standard 4 thumbnails; categories; Overview → Item check that OS didn't tag multiple SKUs (**SKU CONTAINS ","**); Link QC (item search URL IS BLANK, careful of EN vs FR links — use Page Grouping + Language filters).
- **Flyer sorting:** Current Weekly → Upcoming Weekly → Kent Look Books/Catalogs → **KentPRO publications always last** (Monthly, then any Look Books/Catalogs).
- **Flyer Review type: Lite** (owned by Flex).

## Out-of-processing — KentPro process
- Clone weekly Kent flyers into the **KentPRO** retailer; name "Week __ [KentPro]" once URL corrections are done.
- Edit Details: **Hidden in Flipp/Distro**.
- Add stores (rerun codesheet & process — "Page Already Uploaded" errors are OK); reassign by store sets.
- **Change links to kentpro.ca:** Overview → Special Actions → Style Guide Rules → Apply Rules; verify via item search "URL contains kent.ca".
- **KentPRO flyer sorting:** KentPRO publications first (Monthly, then Look Books/Catalogs) → Kent Weekly → Kent Look Books/Catalogs.
- **Monthly:** after FQC, clone to the "KentPro Monthly" flyer type; change toggles on the clone to available everywhere; add stores.

---
*Source: Kent/KentPro OneGuide (Google Doc `1dHVOfwrLfE57KVrC0hOqbmGAA8dN-4Si3F6hshC8Uwc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Key Food Supermarket — Processing Guide

> **Source:** Key Food Supermarket OneGuide (Google Doc `10V8r5Gnc8VpPDWg8R8JMr7bv9QfplSp5hsG_N2bdfRw`). Contacts/credentials omitted.
>
> ⚠️ This OneGuide is largely an unfilled template. Real account facts are captured below; detailed step-by-step instructions were not filled in.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (hide in Hosted at FQC) |
| Slack channel | `#keyfood` |
| Flyer type(s) & cadence | Flyer Type 1: **Weekly** · Flyer Type 2: **Monthly** |
| Processing | Trim Stack |
| Who's involved | Vendor (Upload/Setup); Flex (Image QC, FQC, Flyer Review); OS (Setup); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Monday → Monday; Valid Tuesday → Tuesday.

## Upload & setup (owned by Vendor)
- Manual upload all pages.
- Create **one pricing zone** → add all pages → add all stores.
- Check PDF dates match the flyer run.
- Complete the Standard 4 thumbnails.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- For single and multi-items that share a price, process the whole item block.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)
- **Include** brand, name, pre/postfix, description, price, sale story, categories, disclaimer, original price. **Exclude** valid dates, SKU, URLs.

## Post-processing / FQC (owned by Flex)
- Category QC: confirm items have both a Google and analytical category.
- **FQC:** mark auto-stack off; complete Ops spot checks (if applicable); Edit Details → no theme, **hide in Hosted**, dates match the PDF; check geography (no stores/FSAs added or removed); draw thumbnails if not done (4 standard — ensure complete even if already checked off); complete Final QC checklist.
- **Flyer Review type: Lite.**

---
*Source: Key Food Supermarket OneGuide (Google Doc `10V8r5Gnc8VpPDWg8R8JMr7bv9QfplSp5hsG_N2bdfRw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kim Phat — Processing Guide

> **Source:** Kim Phat OneGuide (Google Doc `1mMp0SMkLioggDYUWhDLefVWukD-8SDsFmgoUrOcso0o`), updated Apr 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#sobeys-dataservices`, `#3fl-sobeys` |
| Flyer type(s) & cadence | **Weekly (10739)** — bilingual EN/FR |
| Processing | Auto-stack |
| Who's involved | DOC (Upload/Setup + FQC); Flex (Setup QC / Flyer Review); OS/Invensis & DSP (vendor tasks); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Tuesday.
- **Publication cadence:** Available Thursday → Wednesday; Valid Thursday → Wednesday.
- **Linking document:** No.

## ⚠️ Risk items
- **Item-level unique valid dates:** e.g. "Jeudi, Vendredi, Samedi, Dimanche Seulement" = Valid Thursday → Sunday. Apply to **both** English and French pages.
- **"Missing in Hosted" error:** do NOT mark as missing in hosted — the flyer goes live "vanilla" on Thursdays and is made interactive on Flipp platforms and Hosted later that day.
- During box draw, some items have **no image** — still box them; a later set of final version files has all images.

## Upload & setup (owned by DOC — all tasks by Coordinator)

**Upload (manual), Tuesday ~4 PM:**
1. Upload final page-version files from the SFTP **twice** (once EN, once FR): Pages → Edit → Select files.
2. Pricing Zones → Flyer Creation → **EN** (English files) and **FR** (French files).
3. Assign all stores to both pricing zones; wait for sessions to run.
4. Overview → Edit Details: **no theme**; External French Run Name "Circulaire Hebdomadaire"; Key Messages EN "Weekly Savings" / FR "Offres Hebdomadaires" (show/hide rarely-used fields to input).
5. Thumbnails → Standard 4; complete setup; mark autostack complete.
6. **Submit an Overnight Processing Ticket** for OS to complete vendor tasks: one ticket for Invensis (Box Draw, Spot Check, Tag, Tag QC) and one for DSP (Box QC).
7. Check all pages for unique dates and set them accordingly.
8. Once vendor tasks are done on Wednesday, complete FQC.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; no linking doc)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box all items with prices, using text boxes when necessary. Box items even when no image is present (images arrive in a later file drop).

### Tag / Tag QC (Low; Auto-tag OFF; no linking doc)
- **Include** brand, name, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude** SKU, disclaimer, URLs.
- **Name/Brand:** brand as applicable (usually not bold); product names are bold, with the French version above the brand and English below.
- **Description:** the non-bold verbiage — French description on FR flyers, English on EN flyers only.
- **Original Price:** tag if "Regular Price" text is on the page.
- **Valid dates:** apply item-level unique dates to both EN and FR pages (see risk items).

### Image QC / Category QC
- Item categories: Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, Dairy, Deli, Health and Beauty, Seafood (see OneGuide chart for what falls where).

## Post-processing / FQC (owned by DOC)
- Basic checks: Geography, PZs (all stores), all pages tagged, QC 4 thumbnails.
- **Check item valid dates on all pages** and update per the flyer if OS missed any.
- Complete the FQC checklist.
- **Flyer Review type: Lite** (owned by Flex).

## Out-of-processing
- **Page swaps** are standard (baseline page-swap video).

---
*Source: Kim Phat OneGuide (Google Doc `1mMp0SMkLioggDYUWhDLefVWukD-8SDsFmgoUrOcso0o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# King Kullen — Processing Guide

> **Source:** King Kullen OneGuide (Google Doc `1SSkywo4lwKqLjB_FCNUBXpvbTR2wOKhVJ0o2CnU41no`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified in guide) |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flex-flyer-review` |
| Hosted URL | kingkullen.com |
| Flyer type(s) | Weekly Flyer (flyer type **3253**) |
| Processing | Auto-stack; no coupons; no Feedel/retailer data services |
| Involvement | **OS** does the upload; **FLEX** owns FQC & post-processing |

## Files & schedule

- **Files received:** Tuesday.
- **Publication cadence:** Available Thursday–Friday, Valid Friday–Thursday, 1-day consumer preview.
- **Linking document:** N/A.

## Upload & setup

- **OS uploads** for King Kullen. Check the FTP on Tuesday to confirm correct files (verify valid dates).
- Fill out the Vendor Setup & Setup QC Tracker (Tuesday tab) by 3:30 PM with the Flyer Run ID and file-readiness; `#vendor-setup-retailers` posts EOD callouts.
- **Manual upload (if run by vendor):** Pages > Edit > select the week's pages > Autogroup (Covchain is always page 1). Page language English. One pricing zone **Base**, English, Add All (32 stores).
- **Setup QC:** Leg heights **30/20**; Thumbnails Regular 4 (thumbnail_1065 2pg, Stock Premium 1pg, Storefront Carousel Premium 2pg, Storefront Carousel Organic 1pg). Available Thu–Thu with 1-day preview, Valid Fri–Thu, Available Everywhere, No Theme.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Brand handled in Box Draw.
  - Sale-story patterns: "SAVE $X.XX" → tag Dollars Off. "Save X¢ On Each" / "Save Up to $X" → **DO NOT tag Dollars Off.** Beer: "MFR'S REBATE" and mail-in-rebate story/disclaimer patterns.
- **Image QC:** clean PDFs preferred; cutouts if no clean PDF. For multi-image boxes pick the best/main image, no cut-off products.

## ⚠️ Common errors / risk items (FQC — owned by FLEX)

- **Deli items (page 3):** apply the disclaimer **"Deli Items Not Available At All Stores"** to ALL deli items. If many are missing it, copy the Page 3 Page ID, use Item Search on that Page ID, multi-edit the deli items, add the disclaimer.
- **Beer items (page 4/5):** every beer item needs a sale story. **No red/yellow banner → "MFR's rebate"**; **red/yellow banner present → "$X.XX DIGITAL SCAN CODE, MFR'S REBATE"** (substitute the flyer price).
- **Floral (last page):** all flowers/flower items need the disclaimer **"Floral Items Not Available At All Stores"**.
- Open all pages to confirm disclaimers/sale stories are tagged. Check both pricing zones' Vertical Preview + Full Screen so item boxes are clickable. Re-run any failed sessions.

## FQC / flyer review

- Edit Details: valid dates match flyer (check page 1); Available from = 1 day before Valid from; Available everywhere; no external run name; no theme.
- **Flyer Review type: Lite.**
- **Out-of-processing:** N/A.

---
*Source: King Kullen OneGuide (Google Doc `1SSkywo4lwKqLjB_FCNUBXpvbTR2wOKhVJ0o2CnU41no`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kinney Drugs — Processing Guide

> **Source:** Kinney Drugs OneGuide (Google Doc `1GZy25c3s1wdcAvj7tDzRhYgVrHe3edArLkrsDPsLmsA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | **Flipp only** |
| Slack channels | N/A |
| Hosted URL | kinneydrugs.com |
| Flyer type(s) | Weekly · Monthly · Quarterly · Seasonal · EDLP (always-on) |
| Processing | Auto-stack; no coupons; no Feedel |
| Involvement | **Vendor** owns upload; **DOC** owns post-processing & FQC; **FLEX** owns Flyer Review |

## Files & schedule (Weekly)

- **Files received:** Monday/Tuesday — via **email** (combined PDF + linking document).
- **Publication cadence:** Available/Valid Sunday–Saturday.
- **Linking document:** Yes (XLS, labelled `DATE WEEKLY`, e.g. `11.17 WEEKLY`).

## Upload & setup (owned by DOC)

- PDFs must be dropped into the SFTP to split; the link doc is attached from local.
- Pages are labelled with the go-live/valid date (e.g. `11-17-24 Digital Circular`).
- Pages Tab → Edit → find the corresponding weekly folder → upload all pages → Auto-group → **English only** → Save (once indexing is confirmed).
- One pricing zone (name it `Base`). **Attach the linking document to all tasks.**

## QC specifics

- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF; linking doc used for both Box & Tag):** **include special weblinks**; exclude coupons, packaged deals, retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box & Tag):** include brand, name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**.

## ⚠️ Common errors / risk items (Links QC)

These must be boxed and tagged **separately as Links** from the items:

- **"Digital Coupon" callouts** → box/tag separately as a Link → URL `https://www.kinneydrugs.com/thrive/coupons/`.
- **Front-page logo** → box/tag as a Link → URL `https://www.kinneydrugs.com/`.
- **Front-page social media icons** (bottom) → link to the corresponding Instacart / Facebook / Instagram / YouTube Kinney Drugs pages (per the OneGuide).
- **Bottom coupon CTA** → box and link on **every page** → URL `https://www.kinneydrugs.com/thrive/coupons/#`.

## FQC / flyer review

- FQC checklist and detailed step content were not filled in beyond the links above in the source doc.
- **Flyer Review type: Lite.**

---
*Source: Kinney Drugs OneGuide (Google Doc `1GZy25c3s1wdcAvj7tDzRhYgVrHe3edArLkrsDPsLmsA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kitchen Stuff Plus — Processing Guide

> **Source:** Kitchen Stuff Plus OneGuide (Google Doc `1t-3B1OBO2UOtz-AP2RXHLxezdjH7WeXkfy0Da10RLyk`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | kitchenstuffplus.com |
| Flyer type(s) | Weekly Flyer |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **DOC** owns setup & post-processing; **Flex** owns Flyer Review |

## Files & schedule

- **Files received:** Thursday (via FTP: publication files + a CSV tagging/linking document).
- **Publication cadence:** Available/Valid Monday–Sunday.
- **Linking document:** Yes (CSV attached to Tag & QC).

## Upload & setup (owned by DOC)

- Receive files via FTP (publication PDFs + CSV tagging doc).
- **Manual upload:** select the split pages, language English, auto-number pages.
- One pricing zone (**Base**) — add all stores.
- Attach the `.csv` to Tag & QC in the Vendors tab.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** **include** coupons, sign-up page, social media, special weblinks; exclude packaged deals and retailer logo. Box all items with price/sale story; text boxes where needed; box callouts.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** **include SKU, name, description, price, sale story, categories, disclaimer, original price, URLs.** Exclude pre/postfix and valid dates. PDF image auto-selection ON.
  - Original Price examples: "Reg. from $99.99 ea." → 99.99; "Compare at $70" → 70.
- **Image QC:** prioritize clean PDF images; for multi-items use a clean individual image if no group image. Avoid images with shadows/black backgrounds.

## ⚠️ Common errors / risk items

- **Missing URLs:** OS sometimes doesn't tag a URL (accident, or none on the CSV). Use Overview > "Items Without a URL" to catch these.
- **Last page** must be boxed and tagged (% off info).
- **[Item Types → Hosted Link clone]** After the "Flipp – Item Types" run completes, **clone it into a separate "Hosted – Link Items" flyer** because hosted properties require direct links only for this retailer — display type must be **Link** (not Item) for all ad cells:
  - Overview > Export Items → open the emailed export.
  - Delete the "Page Items" header row; delete the "Flyer Items" header row and all flyer-item rows below it; delete unnecessary columns; swap "ITEM" → "LINK" under Display Type; move the SKU column to column B; save as `.csv`.
  - Overview > Import → upload the file. Verify via Item Search: Display Type = ITEM should return **0 results**.
  - **RISK:** ensure the "Flipp – Items" run is **hidden in Hosted**, and the "Hosted – Links" run is **hidden in Flipp**.

## FQC / flyer review

- Final QC: spot check; thumbnails drawn; item preview (last page % off boxes); report items without URL (fix via spreadsheet/website); verify category thumbnail generation; check flyer sorting.
- **Flyer Review type: Lite.**

---
*Source: Kitchen Stuff Plus OneGuide (Google Doc `1t-3B1OBO2UOtz-AP2RXHLxezdjH7WeXkfy0Da10RLyk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kj's Market — Processing Guide

> **Source:** Kj's Market OneGuide (Google Doc `1Bp0igzugTTpK5lJlt1_nzt1AQOedxDmofHYkT0puNuE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (Longtail) |
| Availability | All platforms |
| Slack channels | `#kjsmarket` |
| Flyer type(s) | Weekly Flyer |
| Processing | Auto-stack; no coupons; no Feedel/retailer data services |
| Involvement | **Vendor** owns upload; **DOC** owns FQC; **FLEX** owns Setup QC & Flyer Review |

## Files & schedule

- **Files received:** Wednesday.
- **Publication cadence:** Available Wednesday–Tuesday, Valid Thursday–Wednesday.
- **Linking document:** N/A.

> **Shared banner:** Kj's and **IGA Southeast** share files. The version document includes **both** IGA and Kj's info — for this upload use **only the Kj's information**.

## Upload & setup (owned by Vendor)

- **Build the Generic Codesheet:** download the retailer version document from the FTP (search XLS, e.g. `031126_WLF_VERSIONS_FLIPP`). In a blank sheet add headers: Version, Stores, Page 1, Page 2, … (one per page listed). Copy/paste the Kj's data across. Save as `Kjs _date_` (e.g. `Kjs 3.04`).
- **Upload the generic codesheet:** in the flyer-run shell open the Codesheet interface. Name: `codesheet`. **Config name = basepath from the FTP where files were dropped** (e.g. `/3.11`). Toggles to **include:** Store or Set Assignment, Page Upload, Allow Pricing Zone Creation, Tile Generate afterwards. Process; complete flyer setup once the run is GREEN.

## ⚠️ Common errors / risk items

- **Shared FTP with IGA:** when uploading from SFTP, confirm no pages are left unuploaded. Pages remain in the FTP because it's shared with IGA — **ensure ALL Kj-labelled files are uploaded** (don't upload IGA files).
- Confirm all pages uploaded (Pricing Zone tab → Items View) and flyer dates (usually first/last page).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Brand handled in Tag/QC.
- **Image QC:** standard — PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing (20% of pricing zones).

## FQC / flyer review

- Confirm dates (vs PDF) and availability toggles; thumbnails (Standard 4) include retailer logo; all items boxed/tagged; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (shared review guide with IGA Southeast).

---
*Source: Kj's Market OneGuide (Google Doc `1Bp0igzugTTpK5lJlt1_nzt1AQOedxDmofHYkT0puNuE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kohl's — Processing Guide

> **Source:** Kohl's OneGuide (Google Doc `1WOS9edh6DgggwtwGBQosiIvoKp04FDThhHmfv4vk56c`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | **Tier 1 Premium** (account 2470) |
| Availability | All platforms |
| Slack channels | `#kohls`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | kohls.com/feature/flipp.jsp |
| Flyer type(s) | Weekly Flyer (2525) |
| Processing | Auto-stack; **coupons processed by OS**; no Feedel |
| Involvement | **DOC** owns setup & FQC; **FLEX** owns Image QC, Processing Support & Flyer Review |

## Files & schedule

- **Files received:** Monday (via **email** from Prepress — download and upload to CORE FTP).
- **Publication cadence:** Available Tuesday–Friday, Valid Friday–Tuesday.
- **Preview date:** Tuesday the week before available.
- **Linking document:** for **Little Co Books** only.

## Upload & setup (owned by FLEX)

- Pages may need to be added to SFTP by the processor if files come via email. **Manual upload.**
- **Reading page names / versioning:** upload all pages **unless a numerical value follows the letter** (revised pages) — e.g. `01A2B2C2D2` is used instead of `01ABCD`; ignore the superseded version. Letter combos can be any of A/B/C/D (AB, CD, ABCD, BCD…). `R` before the number (e.g. `r01`) = goes to all regions. Format is Date/PageNumber/Stores. Tip: look at the last page to see which versions to build.
- **4 store sets:** AA, BB, CC, DD (on FADMIN) — match to page file names. Pages shared across zones can be combined into one pricing zone; a zone with its own page gets its own zone.
- **Config name: `kohls`.** (Codesheet upload used only if they resume sending Version Memos; currently manual.)

## ⚠️ Common errors / risk items

- **Page-level valid dates:** check the top of each page for separate valid dates (e.g. "3-Day Door Busters"). Dates may be **cut off and split across two pages**.
- **Original price:** always choose the **highest price in a range**.
- **Sale Story:** apply a banner's sale to the Sale Story of **all items listed under it**.
- **Box QC:** confirm coupons are boxed; **two prices sometimes get boxed together — separate them**. Auto-stack spotcheck: merge spread pages in the spotcheck tool.
- **Versioning:** confirm page file names align with assigned store sets (AB pages → AB store sets, etc.).
- **Little Co Books:** lookbook content with no items/prices — always has a linking document defining box placement and tagging.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Stock Premium: use Flipp-created or generic sale story (usually from page 1); include the Kohl's logo in Stock Premium and both Storefront Carousels.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** Only enter a disclaimer if it's inside the drawn box (not page-bottom disclaimers).
- **URLs — always enter:** search kohls.com for the item, copy the item-page link into the URL field. If no direct URL, use the search-page URL; for assortments use any item's direct link. If none found, use `http://www.kohls.com`. Coupons must be **link type** pointing to Kohl's sales/deals page.
- **Image QC:** PDF preferred if clean; cutouts otherwise; cleanest image possible.

## FQC / flyer review

- FQC checklist: pricing zones have correct pages per naming convention; box-draw items with price/coupons/social icons; **leg heights 45/35**; view warnings; add missing URLs; store tiles/sale story; check valid dates by page; coupons all link-type with URL; dates on PDFs match run dates; all stores assigned; items clickable; Item Image QA 100% complete.
- **Flyer Review type: Simple.**

---
*Source: Kohl's OneGuide (Google Doc `1WOS9edh6DgggwtwGBQosiIvoKp04FDThhHmfv4vk56c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Korna Natural Pet Supplies — Processing Guide

> **Source:** Korna Natural Pet Supplies OneGuide (Google Doc `126tFKSQDWbPwKbkhpfkW2K6My-2Ny8LHT9Ny2Vut_lA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#kornapets` |
| Flyer type(s) | Monthly / ad-hoc (flyer 9068) |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **Vendor** owns upload; **FLEX** creates the shell & does Image QC; **DOC** owns FQC |

## Files & schedule

- **Files received:** ad-hoc. The retailer drops files into FTP with an Excel document giving available/valid dates, flyer run name, page count and page order.
- **Publication cadence:** ad-hoc.

## Upload & setup

- **FLEX creates** the flyer run for Vendor upload.
- **Vendor upload:** Pricing Zone **Base**, Stores **All**, upload pages per the Excel document.
- **Setup QC (FLEX):** check off all boxes; ignore any warnings.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** retailer logo, sign-up page, social media, special weblinks; exclude coupons and packaged deals. Box products with supporting info together; items with a separate price are boxed separately.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, valid dates, price, sale story, categories. **Exclude** pre/postfix, description, SKU, disclaimer, original price, URLs. Brand handled in Box Draw. For % or $ off, use the **Sale Story** field.

## FQC / flyer review

- Final QC (DOC): draw **4 standard thumbnails**; **leg heights 50/35**; **Image QC: cut-outs only**; **mark items In-Store Only**.
- **Flyer Review type: Lite.**

---
*Source: Korna Natural Pet Supplies OneGuide (Google Doc `126tFKSQDWbPwKbkhpfkW2K6My-2Ny8LHT9Ny2Vut_lA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Korvette — Processing Guide

> **Source:** Korvette OneGuide (Google Doc `1TtRpz-p-TRXAxwZeLjgslvlzUMB-hF7ln8DFa5SGtk4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Plus |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type(s) | Flyer (bilingual EN/FR) |
| Processing | Auto-stack; no coupons; no Feedel |
| Involvement | **FLEX** owns upload and FQC |

## Files & schedule

- **Files received:** ad-hoc.
- **Publication cadence:** ad-hoc (available/valid all ad-hoc).
- **Linking document:** Yes.

## Upload & setup (owned by FLEX)

- Pages may need to be added to SFTP by the processor if files come via email. **Manual upload.**
- Pages Tab → Edit → select all SFTP pages → Confirm & Upload. **Upload pages TWICE** (one EN set, one FR set — same PDFs). Auto-Group or add page numbers; set the correct language per set. Save & Confirm — **do NOT process internally.**
- **Pricing zones:** create an EN zone (select all pages), Save & Next, toggle French to create the FR zone, Save & Confirm. **Add all stores to both zones.**
- Setup QC: confirm all pages uploaded (Pricing Zone tab → Items View); confirm flyer dates; thumbnails Standard 4; preview dates set.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each product block with a price/sale story; box each SKU separately (text boxes as needed).
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box & Tag):** include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**.
- **Image QC:** PDF preferred if clean; cutouts otherwise.

## FQC / flyer review

- Pre-FQC (FLEX): dates vs PDF; available on all platforms; thumbnails include retailer logo; all items boxed/tagged; spotchecks (20%); previews clickable; sessions complete; **geography consistent week over week (unchanged)**.
- **Flyer Review type: Lite.**

---
*Source: Korvette OneGuide (Google Doc `1TtRpz-p-TRXAxwZeLjgslvlzUMB-hF7ln8DFa5SGtk4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kosher (Sobeys) — Processing Guide

> **Source:** Sobeys Kosher OneGuide (Google Doc `1DCXIowBsbdI9QOaf8zO468HCd_v-L8UpscrVDb5igOo`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · S1C1 |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeys-ops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URL | sobeys.com |
| Flyer type(s) | Weekly Flyer — Kosher |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **Vendor** owns upload & Image QC; **FLEX/3FL** owns FQC & Flyer Review; **OS** setup |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available Wednesday–Wednesday, Valid Thursday–Wednesday.
- **Linking document:** No.

## Upload & setup (owned by FLEX)

1. Pages → Edit → Week → select **ONTARIO → Kosher →** dated folder → drill to individual pages. Select all → Select files → Auto-group → save & complete → submit.
2. Pricing zone: Desc `base`, Language English (confirm pagination/index) → save & done.
3. Add stores for the Sobeys Kosher pricing zone; refresh.
4. Sessions: confirm running (page level then flyer level). **RISK:** an "update distributions" warning can be ignored as long as stores/FSAs are assigned to the zones.
5. Merchant page → details → FTP path → "hide uploaded" → search → check off the Kosher codesheet (keeps FTP clear).
6. Edit Details: **External Run Name = `MM/DD - MM/DD` valid range** (e.g. `Weekly eFlyer 03/24 - 03/30`); no theme; Key Messages Long "Weekly Ad. Weekly Savings." Short "Weekly Ad."
7. Confirm next steps assigned to OS, priority **High** (short turnaround).
8. Thumbnails: 1065x600 (pg 1&2), Stock Premium (pg 1), Storefront Carousel Premium (pg 1&2), Storefront Carousel Organic (pg 1), thumbnail (pg 1&2), fpt_400w (pg 1).
9. Mark Autostack spotcheck complete (completes the vertical-preview auto-publish task in FQC).

## ⚠️ Common errors / risk items — Scene+

- **Scene+ callouts:** every offer with an accompanying Scene+ offer must have **"Scene+" in the Sales Story** — even if the flyer only shows points, tag Scene+ in the Sales Story (NOT the disclaimer).
- **Scene+ PTS sale story** must read exactly **"### Scene+ PTS"** (e.g. `500 Scene+ PTS`) — not "500 PTS", "500 Scene", or "500+ PTS".
- **Scene+ Member Pricing items:** Prefix "Scene+ Member Pricing" (keep the **+**); Disclaimer "$xx without Scene+ Card"; Categories add `[Scene+]`.
- **Pepsi/Coca-Cola soft drinks** flagged as a risk item (grocery).
- **Inserts (updated Mondays):** find them in the Sobeys FTP under folder path **"kosher" OR "Ontario"** (use whichever is present); box one box per page, tag as display type **Link** with file name + URL from the insert tracker; add into pricing zones per the tracker; then create an Optics ticket for the lead.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** retailer logo and special weblinks; exclude coupons, packaged deals, sign-up page, social media. Exclude Kosher Market banners.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** brand/name in the branding field only (don't duplicate in name). Include pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU**; URLs excluded unless it's an insert.
  - **KG/LB:** lb price is the main price with `lb` as postfix; **kg price goes in the description** for all produce/meat/seafood.
- **Item Category QC** uses a fixed category chart (Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, **Scene+** [second category on Scene+ items], Dairy, Deli, Health & Beauty, Seafood). Page categories: **all pages get Scene+ and Grocery**, plus all remaining relevant categories.

## FQC / flyer review

- **Leg height 40/35.** Item Image QC (clean PDFs, white background, no shadows — else cutout). Re-run page stitching. QC categories + page categories. Scene+ check via Item Search: Sale Story contains "PTS". Confirm inserts added (note in comments). Other red errors/warnings can be ignored.
- **Flyer Review type: Lite.**

---
*Source: Sobeys Kosher OneGuide (Google Doc `1DCXIowBsbdI9QOaf8zO468HCd_v-L8UpscrVDb5igOo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kroger — Processing Guide

> **Source:** Kroger OneGuide (Google Doc `1vMpgwKQXwOGb4w3AOvlxT84QVEBib0zC_oPnftF_xw4`). Contacts/credentials omitted.
> **Large, complex Tier 1 Premium account** with many banners and 8+ flyer types.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** |
| Availability | Most flyer types all platforms; some Hosted-only (see per-type notes). **Kroger does NOT use the Flipp hosted iframe.** |
| Slack channels | `#kops` (FT Kroger ops), `#kroger` (full team), `#3fl-kroger` (Flex processing), `#flex-processingsupport` |
| Hosted URL | n/a (no Flipp hosted iframe) |
| Processing | Auto-stack (Ocado = Trim Stack); no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **Unique Shift Type 3FL**; DOC + FLEX split across the multi-day workflow |
| Flyer types | Weekly Ad · Weekly Ad [F4L 704 / Foods Co 704 / Mariano's 531] · Bi-Weekly [Ruler Foods 090] · Weekly Ad [Ocado] · Marketplace · Gen Merch · Ship to Home · Ad Hoc Content · Adult Beverage · (Discontinued: New Releases) |

## Account-wide risk items

- **Flyer sorting:** set Flyer Type **Newest First** for all weekly flyers (Flipp no longer powers Kroger's hosted).
- **Item valid dates — "2 Day Sale":** 2-day-sale items (often boxed on the first page TB01, e.g. "2 DAY SALE" callout) need **unique valid dates** matching the days on the page. **The item directly above the "2 DAY SALE" banner also needs those valid dates.**
- **B#G# / Final Cost deals:** any B#G# deal ("BUY # GET # FREE of Equal or Lesser Value With Card") **must** have a Sale Story; an accompanying limit ("LIMIT # TOTAL WITH CARD") goes in the disclaimer. Any **"FINAL COST" / "FINAL PRICE"** callout must be added to the Sale Story.
- **Boxing/pages appear off after reordering:** if pages are reordered via a second codesheet, some system tasks must be re-run manually or boxes/pages render incorrectly. After forced processing finishes, **re-run Page Tile Generation** (per track) — this cascades Flyer Tile Gen, Low Res PDF Gen, PDF Text Extraction, Flyer Thumbnail Gen. If pages still look off, re-run **Page Stitching**.

## Custom action — FSA Swap (Weekly Ad)

During FQC, if a pricing zone has 0 FSAs and 1 store: identify the store(s), find the zip (Merchant page > stores/store sets), then run the **FSA Swap** custom action with Flyer run ID, Pricing Zone ID FROM (find current zone via Ctrl+F in Geography), Pricing Zone ID TO, and the list of FSAs (store zip).

---

## Flyer type 1 — Weekly Ad

**Merchants:** all Kroger banners **except** Ruler Foods 090, Food 4 Less 704, Foods Co 704, Mariano's 531, Ocado.

- **Files:** sent on different days per banner (see "Asset Drop Date"). Multi-day workflow (files 9→5 days out; Image/Category QC; FQC 1 day out).
- **Cadence:** Available Tuesday, Valid Wednesday–Tuesday; preview Tuesday. Linking document: Yes.

**Upload & setup (DOC):**
- Confirm receipt of the **Jenkins email** (search "Jenkins", reply-all confirming). Identify the codesheet (search "xls" in the banner's STALE).
- **Codesheet manipulations** (3 kinds): (1) Standard — delete heading row, blacked-out rows, and the last two total rows; reorder per the latest posting plan / ENT doc. (2) IA05 & special pages — break out unique per-store pages into their own pricing zones. (3) Separating shared codesheets for divisions that share one file: **615** (Dillons/Bakers/Gerbes — Gerbes = 100s store #s, Bakers = 300s, Dillons = the rest), **024** (Louisville "LV…"/JayC "JC…"), **021** (Central/Pay Less = zone CEAND only), **531** (Metro Market = zone RS3SP only / Pick N Save), **620** (City Market = 400s store #s / King Soopers). A **Kroger Codesheet Manipulation Tool** (Colab) automates all three (single-user — toggle "currently in use").
- **Codesheet upload: config `kroger`**, PDF Base Directory from STALE, **toggles: all but the second.** For split shared codesheets, process simultaneously to avoid shared-file errors. After processing, check STALE and manually upload any missed pages (Boost inserts, credit-card pages, "IABoost", etc.). Mark Flyer Creation complete.
- **Thumbnails (5):** the standard 4 (Thumbnail 1065x800, Stock_premium, Storefront_carusel_premium, Storefront_carusel_organic) **plus first_page_thumbnail_400w**. Exception: if page 2 is a wide/short banner insert, draw the 1065x800 and Storefront_carusel_premium over page 1 only. Typically No Theme.

**QC:**
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **include** Retailer Logo (front cover always boxed) and **"Shop Now" callouts**; also box Retailer Offers. Boxes drawn over each item's text + image (no text boxes). Multiple items sharing a sale story → box each separately (box around name, text box around image). Exclude coupons and packaged deals.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
  - **Retailer Offer** (top-right of BD01/TB01): tag as a **Link** to the banner's own site (each banner has its own domain, e.g. ralphs.com, kingsoopers.com, frysfood.com — see OneGuide list). Change display type Item → **Link**.
  - **Fuel Points on Page 1:** tag with the banner-specific `…/pr/fuel-event?cid=dm.pro.weeklyad_ENTAd` link (list in OneGuide; Ruler/F4L not applicable). Fuel banners **not** on page 1: use the link shown on the PDF.
  - Also tag Bakery/Deli, Boost, Gift Card, Military/Senior discount, Cocinalatina banners with the link shown on the banner.
- **Image QC (Vendor):** clean PDF images; use cutout if the PDF is cut off / has an odd background.

---

## Flyer type — Weekly Ad [Food 4 Less 704, Foods Co 704, Mariano's 531]

- Same account-wide risk items. **Config `kroger`** for all. **Toggles to check:** Store or Store Set Assignment, Page Upload, Allow pricing zone creation, Use Page Pool, Tile Generate afterwards; copy PDF base directory from FTP. **Do not add stores to pricing zones after the codesheet runs.**
- **Food 4 Less 704** has two flyers in separate flyer types: California Weekly Ad (2951, use codesheet version **FL1HL** / prefix `F4LCA`) and Chicago Weekly Ad (9307, codesheet **F4LMW** = Midwest).
- **Foods Co 704** (Weekly Ad 2952) uses the F4LCA codesheet, keeping only the Foods Co versions (FL2… pages). **Mariano's 531** (Weekly Ad 3626) — delete the "Flipp Store #" column.
- F4L Cali and Foods Co share pages → a **yellow "already uploaded" codesheet warning is normal**; click Force Processing (it stays yellow).
- **IA16 / IA15 / IA99 alcohol-only pages:** until the posting plan is received, **assume they stay in the weekly ad**; the posting plan (Wed/Thu) determines whether a page is moved to the Adult Beverage flyer.
- Check Geography = "No Stores or FSAs/zips were added or removed!" (else flag). Set preview date to the Wednesday before go-live.
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — Bi-Weekly Ad [Ruler Foods 090]

- Setup owned by FLEX. **Box Draw:** Auto-Box ON. **Tag:** Auto-tag ON. Image QC / Category QC / FQC owned by FLEX.

## Flyer type — Weekly Ad [Ocado]  (Trim Stack)

- **Merchants:** Kroger Ocado FC03 (Groveland Clone), Kroger Atlanta 011 (Ocado Groveland, Birmingham), Kroger Dallas 035 (Ocado Oklahoma City). Files Tuesday; preview Wednesday.
- **Different live dates:** Groveland & Groveland-Cloned live Monday (must be FQC'd by Friday); Birmingham & Oklahoma City live Tuesday (FQC Mondays). Groveland Clone = **Hosted only**.
- **Risk:** build the Ocado-specific linking doc — add `&cid=dm.pro.weeklyad_ENTAd` to the end of all Deeplinks, share edit access with Flipp, attach to the Kroger Flex Team Tracker (Ocado section, column J). **Adjust FSAs during FQC** via the "Assign Fsas from Csv" custom action (4 Ocado flyers).
- **Box Draw:** Auto-Box **OFF**. **Tag:** Auto-tag **OFF**.

## Flyer type — Marketplace

- **Merchants:** most Kroger banners (Dillons 615, Fry's 660, King Soopers 620, Kroger Atlanta/Central/Cincinnati/Columbus/Dallas/Delta/Houston/Louisville/Michigan/MidAtlantic/Nashville, Smith's 706). Files Monday; Available Tuesday, Valid Tuesday–Tuesday.
- **Setup: config `kroger_mp`**, PDF base directory from FTP, **toggles all but the second**; Save & Run codesheet; mark Flyer Creation complete. **Do not add stores to pricing zones after the codesheet runs.**
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **OFF**.

## Flyer type — Gen Merch Ads

- **Merchants:** Smith's 706, Fred Meyer 701. Files Wednesday; Available Tuesday, Valid Wednesday–Tuesday.
- **Setup (FLEX): config `kroger`**, path from FTP, **check all toggles except the second and last**. Manipulations: delete top row + bottom two rows; save as CSV. Note: Smith's codesheet now comes with Fred Meyer's — for the Smith's upload remove the Fred Meyer pricing zones (Smith's zones start **S**, Fred Meyer start **F**). Manual upload looks for the **SM_GEN** folder (not Smith's_MP).
- **⚠️ Risk — "Save ##%" deals:**
  - **Multi-item deal** (multiple items/categories under one "Save ##%", each with its own price or a price range): **one box**; item Name starts with the % promo text ("SAVE 40% With Card on …"); everything else in the description; no current price; tag Percent Off.
  - **Single item** with a "Save ##%" callout: Name is just the item/brand (NOT "save on…"); the "SAVE ##% With Card" goes in the **Sale Story**.
- **Box Draw:** Auto-Box **OFF**, Box QC bot **OFF**. **Tag:** Auto-tag **OFF**.

## Flyer type — Ship to Home

- **Merchants:** all Kroger banners except Kroger Ocado FC03 and Ruler Foods 090. Files Monday. **Availability: Hosted only.**
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — Ad Hoc Content

- Files Monday; all platforms. **Box Draw:** Auto-Box **ON**, Box QC bot **ON**. **Tag:** Auto-tag **OFF**.

## Flyer type — Adult Beverage Ad

- **Merchants:** Ralphs 703 (files Monday), Food 4 Less 704 (Friday), Foods Co 704 (Friday). All platforms.
- Receives the alcohol-only IA15/IA16/IA99 pages split off from the corresponding weekly ads (per posting plan).
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — New Releases (marked Discontinued)

- Fred Meyer 701; Hosted only. Auto-Box OFF, Auto-tag OFF. **This flyer type is discontinued in the OneGuide.**

---
*Source: Kroger OneGuide (Google Doc `1vMpgwKQXwOGb4w3AOvlxT84QVEBib0zC_oPnftF_xw4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Kubota Canada — Processing Guide

> **Source:** Kubota Canada OneGuide (Google Doc `1gOvZUUXCQeuAQF0WQz2xb7Xn3aZqS8mI-bI9sCRiDZs`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#kubotacanada`, `#flex-processingsupport` |
| Flyer type(s) | Ad-hoc |
| Processing | Auto-stack; no coupons; no Feedel |
| Involvement | **DOC** owns setup & FQC; **FLEX** owns Processing Support, Item Image QC & Flyer Review |

## Files & schedule

- **Files received:** ad-hoc. Files come through **BD**, so DOC/DOL adds files to the SFTP if processing support is uploading.
- **Publication cadence:** ad-hoc.
- **Linking document:** Yes — for URLs.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → select all SFTP pages → Confirm & Upload → Auto-Group or add page numbers → set correct language → Save & Confirm (**do NOT process internally**).
- **Pricing zone:** create **Base**, select all pages, Save & Confirm, add all stores.
- **Add the link sheet to all vendor tasks** (mass upload).
- Setup QC: confirm all pages uploaded; confirm flyer dates; thumbnails Standard 4.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both Box & Tag):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box & Tag):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude SKU.**
- **Image QC:** PDF preferred if clean; cutouts otherwise.

## ⚠️ Common errors / risk items

- **URLs:** every item should have a URL. If missing, check the link sheet for a listed URL.
- **YouTube video links must use the EMBED link** (not the watch URL): open the YouTube link, right-click the video → "Copy embed code", extract the embed URL, and use it as the video URL in FADMIN with display type **Video**.

## FQC / flyer review

- Pre-FQC (DOC): dates vs PDF; availability toggles; thumbnails include retailer logo; all items boxed/tagged; spotchecks (20%); previews clickable; sessions complete; geography correct; verify all URLs (including embed links for videos).
- **Flyer Review type: Lite.**

---
*Source: Kubota Canada OneGuide (Google Doc `1gOvZUUXCQeuAQF0WQz2xb7Xn3aZqS8mI-bI9sCRiDZs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
