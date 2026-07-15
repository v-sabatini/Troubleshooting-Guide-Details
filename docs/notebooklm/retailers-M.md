# Retailer Processing Guides — M

> Bundle of 36 retailer-specific processing guides (M). Contacts and credentials are omitted from every guide.

**Contains:** M&M Food Market, Magasin Amira, Magnotta Winery, Manitobah, Marché Adonis, Marché Ami, Marche Ariya, Marche Leo's, Marché Richelieu, Marché Salaberry, Marches Bonichoix, MarchesTAU, Marc's Grocery, Mariana's Supermarket, Mark's, Martin's Super Markets, Mastermind Toys, Materiaux JLS, Matériaux Pont Masson, Materio, Maxi, Mayrand, MB Country Living, McMunn & Yates, Meijer, Menards, Metro Ontario, Metro Quebec, Metropolitan Market, Meubles RD, Mi Tienda, Michaels USA, Mike Dean Local Grocer, Millbank Hardware, Mondou, Moonlight Grocers


---

# M&M Food Market — Processing Guide

> **Source:** M&M Food Market OneGuide (Google Doc `142gmNZ3CkFGdWTRBysr3XoKXtPpB3vveLFiAyAlf8eA`), updated Jul 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#mmmeatshops` |
| Hosted URL | mmfoodmarket.com/en/pages/flyer |
| Flyer type | 139: Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops **Yes (Feedel)**; no coupons |
| Pages | Bilingual (EN/FR on same page) |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Wednesday (5 PM), Valid From Thursday (12 AM) → Available To Monday / Valid To Tuesday. **One-day consumer preview starting 5 PM Wednesday.**
- **Documents:** codesheet (`.csv`), Product Information / URL / tagging document (`.xls`), page/item category spreadsheet.

## Upload & setup (codesheet — owned by DOC)
- FTP: download the product info `.xls` and the codesheet `.csv` (check both off).
- **Codesheet manipulation:** check page numbering; ensure PDF names in the codesheet match the FTP (mismatch → codesheet won't run); add "Versions" to A1 if blank; **rename the version WITHOUT the Quebec zones (PQB Eng, PQU) as `AOC`**; if multiple zones share a name but different store distribution, rename as `AOC_xxx` (xxx = stores). Download as CSV.
- **Codesheet upload:** Config **`m_and_m`**; base path from FTP; **all toggles checked except region assignment AND combine zones**; attach CSV; Save & Process.
- Example week: 3 zones — `AOC`, `PQBEng`, `PQU` (French). Mark flyer creation complete.
- **Setup QC (Flex):** attach the Product Information URL document to every vendor task; confirm dates (bottom of first page); Standard 4 thumbnails; set preview date to the Tuesday before go-live (preview links go to the client).

### Codesheet troubleshooting
- **"page _ not found":** ensure the page name matches exactly in FTP and codesheet; re-save and re-run.
- **"Zone: AOC is missing the following stores…" with no store number:** likely a typo — look for an extra comma in the store list for that zone, delete it, re-run.

## QC specifics
- **Box Draw (Low; Auto-Box ON since May 2025, Box QC bot ON):** **include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box grid items and list items individually; box social media icons.
- **Tag / Tag QC (Medium; Auto-tag OFF; Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **⚠️ Bilingual pages:** when tagging an "English" page, tag **only English** text; on French pages tag **only French** and omit English item info.
  - **Description** = product weight / number of pieces from the PDF. **Price** = bolded Current Price.
  - **SKU:** use the SKU from the tagging spreadsheet (column B), **only in the SKU field**, one SKU per offer, tagged individually. Only use SKUs from the spreadsheet.
  - **URLs:** search product by name in the tagging doc → tag URL from column C. For items not on the site use `mmfoodmarket.com/en/product-not-available` / `.../fr/produit-non-disponible`. Name social media links properly.
  - **Categories:** every item and page needs a category (spreadsheet provides both). Use **Category 1 for the Page Level category** and **Category 2 for the Item category** — all items get only one (Category 2).
  - **Sale Story:** tag "SAVE" info; append Product Sizing info after the Save info if applicable.
- **Image QC:** **cutouts only** (do not use lifestyle images; check for usable PDFs, else cutout).

## ⚠️ Common errors / risk items
- **Inserts:** ensure all pages uploaded.
- **URLs & SKUs:** tag correct SKU and URL based on the product name in the spreadsheet.
- **Social media icons** — box and tag with the correct links (Facebook, Instagram, Foursquare, Twitter, Pinterest — all listed in the OneGuide).
- **Language-specific direct links** — tag per language.
- **Product Sizing** — include in the Sales Story after the "Save" info if applicable.

## Post-processing / FQC
- **URL/Links, SKU, Sale Story QC (DOC/Flex):** item search for blank SKU / Sale Story / URL and fill from the linking doc + M&M website; check description for sizing info (blank OK if URL shows "product not available").
- **FQC (Flex):** geography, sessions, verify URL, PZ/boxing checks; **Custom action — set cutout images, then item image QC** (prioritize cutouts, no lifestyle images); page categories; flyer sorting (weekly > gen merch).
- **Flyer Review type: Lite** — see the M&M Food Market flyer review guide.

## Out-of-processing
- **Add missing FSAs:** geography tab shows 3 missing FSAs → export FSAs → in the CSV delete the "pricing zone name" column, rename columns `flyer_id` and `fsa` (lowercase), add 3 rows with the missing FSAs + AOC pricing-zone id → run "add FSAs from CSV" custom action with the flyer run ID.
- **Preview links:** send preview + direct links to the client a day before go-live (hosted 2.0 preview links renamed Direct EN / Direct FR).

---
*Source: M&M Food Market OneGuide (Google Doc `142gmNZ3CkFGdWTRBysr3XoKXtPpB3vveLFiAyAlf8eA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Magasin Amira — Processing Guide

> **Source:** Magasin Amira OneGuide (Google Doc `1SFIPX0iQhw_V2FhzHWRRJXskaeYSyGZkh86oskl6uiQ`), updated Sep 4, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | magasinamira.ca |
| Flyer type | Weekly (ad-hoc cadence) |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support + Flyer Review) |

## Files & schedule

- **Files received:** ad hoc; available/valid dates all ad hoc.
- Pages may need to be added to the SFTP by the processor if the client sends files over email.

## Upload & setup (owned by FLEX)

- **Manual upload:** Pages → Edit → select all pages from SFTP (usually just 1 page) or upload manually from email → Confirm & Upload. Auto-Group or enter grouping numbers; **language = French.** Save & confirm — **do NOT process internally.**
- **Pricing zone:** create **Base** zone, select all pages, save, add all stores.
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (first/last page); standard-4 thumbnails; preview dates set.

### ⚠️ Common errors (retailer-specific)

- **SFTP page check** — confirm no pages remain in the SFTP that weren't uploaded.
- Watch for **multiple products** requiring separate boxes.
- Spotchecks are often **spelling-related** — French text.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** No linking doc. Include packaged deals; **exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF — cannot text-extract).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; SKU only if on the PDF (rare); **exclude URLs.**
  - Where possible, put **French tags ahead of English** — flyers aren't usually truly bilingual (some items have English, some don't). Tag exactly as shown.
- **Image QC (FLEX):** PDF preferred if clean; otherwise cutouts accepted.

## FQC / flyer review

- **Pre-FQC (DOC):** confirm dates vs PDF, availability toggles, thumbnails incl. logo; all items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (Flex) — flyer dates, sessions complete, previews correct, tagging accurate, geography correct, availability toggles correct.

---
*Source: Magasin Amira OneGuide (Google Doc `1SFIPX0iQhw_V2FhzHWRRJXskaeYSyGZkh86oskl6uiQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Magnotta Winery — Processing Guide

> **Source:** Magnotta Winery OneGuide (Google Doc `1JjkIp7dIUYzEbQ_NtiQ-i_PAAxEPMiyNlEIU8GVY934`), updated Jul 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#magnotta-winery` |
| Hosted URL | N/A |
| Flyer type | Bimonthly (flyer type #12286) |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; flyer review owned by DOL |

## Files & schedule

- **Files received:** ad hoc, first day of every month.
- **Cadence:** Available first day → last day of the month; valid dates span the month (confirm against the PDF).
- **Linking document:** **Yes** — used for both Box Draw and Tag.

## Upload & setup

- **Manual upload:** Pages → Edit → select all pages from SFTP → Confirm & Upload. Auto-Group or manually enter grouping numbers; English only. Save & confirm — **do NOT process internally.**
- **Pricing zone:** create **Base** zone, select all pages, save, add all applicable stores (**14**).
- **Setup QC:** confirm all pages uploaded (Items View); confirm flyer dates (first/last page); standard-4 thumbnails; preview dates set.

### ⚠️ Common errors (retailer-specific)

- **SFTP page check** — confirm no pages remain in the SFTP that weren't uploaded.
- **Social media icons must be boxed separately** and CTAs tagged as direct links per the linking document — a common incorrect item is social icons not boxed separately, or a CTA left without its direct-link URL.

## QC specifics

- **Box Draw (Medium; Auto-Box OFF, Box QC bot OFF).** Linking doc required. Include retailer logo, social media, special weblinks; **exclude** coupons, packaged deals, sign-up page.
  - Box social media icons and CTAs per the linking document.
- **Tag / Tag QC (Medium; Auto-tag OFF).** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude brand and SKU.**
  - CTAs tagged per the linking doc and updated to **DIRECT LINKS**. Each social media icon boxed/tagged separately as a direct link. Listed items with no image tagged separately with links applied per the linking doc.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / flyer review

- **Pre-FQC (DOC):** Links QC — on the overview page select "items with URL"; if any appear, check the linking doc (apply link if required), if none, proceed. Confirm dates vs PDF, availability toggles, thumbnails incl. logo; all items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Magnotta Winery OneGuide (Google Doc `1JjkIp7dIUYzEbQ_NtiQ-i_PAAxEPMiyNlEIU8GVY934`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Manitobah — Processing Guide

> **Source:** Manitobah OneGuide (Google Doc `1v8jocY-_ROLiaAc33hOIcDpcjixIbStv17O9Xn_Idfk`), updated Nov 26, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1p-manitobah` |
| Flyer types | Ad hoc — **two merchants:** Manitobah (Canada, #12171) and Manitobah US (USA, #12193) |
| Hosted URL | USA: manitobah.com/pages/catalog · Canada: not on hosted |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support) |

**Two merchants, processed identically except URLs:** Canada URLs end in **`.ca`**, USA URLs end in **`.com`**.

## Files & schedule

- **Files received:** ad hoc (PDF pages + URL docs via SFTP). Always double-check PDF dates; confirm with client/BD if needed.
- **Linking document:** **Yes** (URLs) — **two separate URL docs**, one for US (`.com`) and one for Canada (`.ca`).
- **Custom action (USA only):** "Assign FSAs from CSV" — assigns FSAs to the single pricing zone; runs post-FQC and after any page swap.

## Upload & setup (owned by DOC)

- Manually upload pages: Pages → Edit → select pages with the country code for that shell (`can` or `us`). Index pages in order; **language = English only.** Save + Save & Complete.
- Create **Base** pricing zone for all pages; add all stores. **USA has 1 dummy store** that must be added so it goes live on Hosted.
- Once sessions run, **attach the URL document as a mass attachment to all vendor tasks.**

### ⚠️ Common errors (retailer-specific)

- **URL QC (top risk):** ensure **all Canada URLs end in `.ca`** and **all USA URLs end in `.com`**. See the Links QC filters below.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** Linking doc (Tag/QC specific). Include special weblinks; **exclude** coupons, packaged deals, retailer logo, sign-up page, social media.
  - Multi-item products boxed **separately** using the text-box feature; box the callout at the bottom; Direct-Link items (gift cards, etc.) are called out in the linking doc.
- **Tag / Tag QC (Low; Auto-tag ON).** Include name, pre/postfix, valid dates, description (use descriptions from the linking/tagging doc), SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude brand.**
  - Callouts/non-product items tagged as **Direct Links** per the linking doc; "Shop Your Way"-type bottom section boxed with links.

## Post-processing (DOC)

- **URL/Links QC** via Item Search:
  - **ALL:** URL "is" blank → 0 items should appear; any that do, check the linking doc.
  - **USA:** URL "contains" `.ca` → 0 results (any → correct to `.com`).
  - **Canada:** URL "contains" `.com` → 0 results (any → correct to `.ca`).
- **Assign FSAs from CSV (USA):** copy the base pricing-zone ID, paste into the `flyer_id` column of the FSA-list template (all rows same number), save as CSV, run the "Assign FSAs from CSV" custom action with the flyer run ID. Repeat for the 2nd flyer run with the correct sheet.

## FQC / flyer review

- **FQC (FLEX):** standard-4 thumbnails; complete FQC checklist in FADMIN.
- **Flyer Review type: Lite.**

---
*Source: Manitobah OneGuide (Google Doc `1v8jocY-_ROLiaAc33hOIcDpcjixIbStv17O9Xn_Idfk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marché Adonis — Processing Guide

> **Source:** Marché Adonis OneGuide (Google Doc `1bk7AhFtCwxrwa7nrlOHQjpuHTwIsB9knwy2XGyjGOTU`), updated Jun 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#ops-metro`, `#flex-processingsupport` |
| Flyer type | Weekly |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support) |

## Files & schedule

- **Files received:** Wednesday (via SFTP, no later than the Wednesday prior to launch).
- **Cadence:** Available Tuesday, Valid Thursday, Available/Valid To Wednesday. Preview date Tuesday.
- **Ops notification:** when files land, check the Processing Support board; if not slotted, post in `#flex-processingsupport` requesting upload. 1–2 days after processing, add flyer runs to the VAST tracker for FQC.

## Upload & setup (owned by Vendor)

- **Weekly flyer:** manual upload of files ending `_p000#.pdf` for the correct date; upload both QC and ON pages. Set **QC pages to FR**, **ON pages to EN**. Auto-Group → Save and Complete.
- **Pricing zones — create 4** with languages:
  - **ON = EN**, **ON CL = FR** (cross-language from EN), **QC = FR**, **QC CL = EN** (cross-language from FR).
- **Stores:** ON = ON store set; ON CL = ON CL store set (Ottawa store only); QC + QC CL = QC store set.
- **Staggered dates:** open the **ON and ON CL versions ONLY** and set **Available From** to the Wednesday before the Valid From date. Make this change to the Available From date only, and only on ON / ON CL zones.
- (Inactive) London flyer: files begin `london flyer`; 1 EN pricing zone; add **only store 564 (London)**.

### ⚠️ Common errors (retailer-specific)

- **Page order** — verify page sequence before completing setup QC and FQC; ensure no pages are repeated. Incorrect page ordering is a documented failure mode.
- Watch for **multiple products** requiring separate boxes.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** No linking doc. Include retailer logo, sign-up page, social media, special weblinks; **exclude** coupons, packaged deals.
  - Box item blocks as one; items with two different descriptions drawn as separate boxes.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON).** Include brand, name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude valid dates.**
  - **Original price:** single price → Original Price field; a **range** → put in the Description field.

## Post-processing / FQC (FLEX)

- **Ad-hoc (FLEX):** Fruits + Veg (Last Minute Deals) insert pages arrive Tues/Wed for a Thursday launch — upload (QC page FR, ON page EN), set a trigger to insert pages into their zones for Thursday 12 AM, file a JIRA ticket for a trigger check and bump the DOC.
- **FQC checklist:** ops spotchecks; thumbnails 1065×600 (storefront carousel premium + organic); edit details (Available Tue, Valid Thu, Available/Valid To Wed, available everywhere, no theme); all priced items and visible sale stories boxed; interactivity via vertical preview; page order matches the tracking sheet in the SFTP; sessions green + MISO; geography unchanged; staggered-date check on ON / ON CL only.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps per the baseline page-swap process.

---
*Source: Marché Adonis OneGuide (Google Doc `1bk7AhFtCwxrwa7nrlOHQjpuHTwIsB9knwy2XGyjGOTU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marché Ami — Processing Guide

> **Source:** Marché Ami OneGuide (Google Doc `1WeFvbbmfg4fW4eWq9nz6N4YR0WOjccdOOXxetVB9y9o`), updated Feb 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#metro`, `#opsmetro`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type | Weekly |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support + Flyer Review) |

## Files & schedule

- **Files received:** Monday (via SFTP, no later than Tuesday 12 PM prior to launch).
- **Cadence:** Available Tuesday, Valid Tuesday, Available/Valid To Thursday. **Set Available From to two days before the Valid Date.**

## Upload & setup (owned by Vendor)

- **Upload:** manually upload all pages, set all pages to **FR**, Auto-Group → Save and Complete.
- **Pricing zones — create 4** (more may be required depending on files received):
  - **AMI = FR**, **AMI CL = EN**, **AMP = FR**, **AMP CL = EN.**
- **Stores:** AMI = AMI store set (CL included); AMP = AMP store set (CL included). Geography unchanged WoW without note.
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates; standard-4 thumbnails; preview dates set; Available From = two days before Valid.

### ⚠️ Common errors (retailer-specific)

- **SFTP page check** — confirm no pages remain in the SFTP that weren't uploaded.
- Watch for **multiple products** requiring separate boxes.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF).** No linking doc. Include packaged deals, retailer logo, sign-up page, social media, special weblinks; **exclude coupons.**
  - Box items that share prices, and item blocks, together under one box; ensure the web link is boxed.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU and URLs.**
  - **Original price:** single price → Original Price field; a **range** → Description field.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / flyer review (Vendor)

- Confirm dates vs PDF; availability toggles (available everywhere); thumbnails incl. logo; all items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (Flex).

## Out-of-processing

- Page swaps per the baseline page-swap process.

---
*Source: Marché Ami OneGuide (Google Doc `1WeFvbbmfg4fW4eWq9nz6N4YR0WOjccdOOXxetVB9y9o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marche Ariya — Processing Guide

> **Source:** Marche Ariya OneGuide (Google Doc `1_f10-jKRj0eIWuuVvmcnQjNti0KKgQe1ha8_VDKkN70`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | N/A |
| Availability | All platforms |
| Slack channels | N/A |
| Hosted URL | marcheariya.com/flyer/ |
| Flyer type | Flyer |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (3FL + Flyer Review) |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available/Valid From Thursday; Available/Valid To Wednesday. No preview date; no linking document.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → select all pages from SFTP. Auto-Group; **French pages only.** Save & confirm — **do NOT process internally.**
- **Pricing zones — create 2:** **French** and **French CL** (toggle "Cross Language" and change language to English). Save & confirm.
- **Stores:** add **Greenfield Park only.**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (first page); standard-4 thumbnails; **no theme / no external run name.**

### ⚠️ Common errors (retailer-specific)

- **SFTP page check** — confirm no pages remain in the SFTP that weren't uploaded.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** No linking doc. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - Ensure all single items have a box drawn.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU and URLs.**
  - Minimum tag: brand, name, description (if available), current price, categories.
- **Image QC (Vendor):** PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** typically pricing discrepancies or uncommon "Name" info.

## FQC / flyer review

- **Pre-FQC (DOC):** confirm dates vs PDF; availability toggles; thumbnails incl. logo; all items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; **geography correct — no stores or FSAs/zips added or removed.**
- **Flyer Review type: Lite** — dates, previews, tagging, **no extra boxes from the autobox process**, geography (may change WoW per retailer distribution), availability toggles.

---
*Source: Marche Ariya OneGuide (Google Doc `1_f10-jKRj0eIWuuVvmcnQjNti0KKgQe1ha8_VDKkN70`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marche Leo's — Processing Guide

> **Source:** Marche Leo's OneGuide (Google Doc `1ByuIWrM-fIEhE8VE174U_vMG7-w0XkZyUeWkMRSOFd0`), updated Jul 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | **Flipp only** |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | N/A |
| Flyer type | Weekly (flyer type #6345/10574); monthly publication cadence, ad-hoc files |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support) |

## Files & schedule

- **Files received:** ad hoc (via email). No preview date; no linking document at the account level (a linking doc is attached under vendor tasks for tagging — see below).

## Upload & setup (owned by FLEX)

- Files sent via email.
- **1 pricing zone, English,** containing all pages and assigned to all stores.
- **Setup QC:** confirm all items in the setup QC checklist are correct.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF).** Linking doc (Tag/QC specific). **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - Box the retailer logo; box all items separately.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude brand and valid dates.**
  - Minimum tag: name, current price, category, brand, description, URL. The linking doc (under vendor tasks) provides categories and URLs.
  - **Spotcheck URLs for accuracy against the linking doc.**
- **Item Category QC (DOC):** use the retailer's linking doc for the appropriate categories.
- **Item Image QC (DOC):** clean PDF image where possible, otherwise cutout is okay.

## FQC / flyer review

- **No special risk items** — use generic flyer review standards.
- **Flyer Review type: Lite** (Flex).

---
*Source: Marche Leo's OneGuide (Google Doc `1ByuIWrM-fIEhE8VE174U_vMG7-w0XkZyUeWkMRSOFd0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marché Richelieu — Processing Guide

> **Source:** Marché Richelieu OneGuide (Google Doc `1PyiXvcJ2C502Y-BE6di9XJ44BnSzs_kU8bMcX4xJMB4`), updated Feb 22. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#opsmetro`, `#flex-processingsupport`, `#vendor-assigned-tasks-retailers` |
| Flyer type | Weekly Ad (merchant #3372) |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex flyer review, OS FQC |

## Files & schedule

- **Files received:** Monday (PDFs via SFTP, no later than the Wednesday prior to launch).
- **Cadence:** Available Tuesday, Valid Thursday, Available/Valid To Wednesday. No preview date; no linking document.
- Coordinator ensures VAST is updated ~3 days out.

## Upload & setup (owned by Vendor)

- Open the **Tracking Sheet** (usually a PDF) to identify page order. Manually upload all pages.
- **Do NOT use files in directories whose base path ends in `BLOCK_ID`** — use the equivalent files without the `BLOCK_ID` suffix.
- Set all pages to **FR**; Auto-Group → Save and Complete.
- **Pricing zones — create 2:** **Base = FR**, **Base CL = EN.** Add all stores to both.
- Check geography (no WoW changes without note); check the SFTP for leftover/unused pages.

### ⚠️ Common errors (retailer-specific)

- **Missing pages** — if any page listed in the Tracking Sheet is missing from the FTP, flag the FT team immediately.
- **Leftover / unused SFTP pages** not listed in the Tracking Sheet → flag the Full Time Ops team.
- **`BLOCK_ID` directory files** must not be used.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** Linking doc (Box Draw/Box QC specific). **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - Multiple items boxed together when one price covers all (e.g. 2 for $3 cantaloupes, or iceberg lettuce); ensure the web link is boxed.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Original price:** single price → Original Price field; a **range** → Description field.

## FQC / flyer review (Vendor)

- Ops spotchecks; thumbnails 1065×600 (storefront carousel premium + organic); edit details (Available Tue, Valid Thu, Available/Valid To Wed, internal run name MM DD, available everywhere, no theme); all priced items and visible sale stories boxed; interactivity via vertical preview; page order matches the tracking sheet in the SFTP; sessions green + MISO; geography unchanged.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps per the baseline page-swap process.

---
*Source: Marché Richelieu OneGuide (Google Doc `1PyiXvcJ2C502Y-BE6di9XJ44BnSzs_kU8bMcX4xJMB4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marché Salaberry — Processing Guide

> **Source:** Marché Salaberry OneGuide (Google Doc `1ltU4_m2aO1063SxrpvTRi8EubgKbbFnIrFXI8imb0PQ`), updated Sep 19, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channels | `#marché-salaberry` |
| Hosted URL | N/A |
| Flyer type | Flyer (typically runs 2 weeks) |
| Processing | Auto-stack; Strategic Ops **yes** (Feedel); no coupons; Flex flyer review |

## Files & schedule

- **Files received:** Tuesday (~2 days before launch) **via email — no FTP for this retailer yet.**
- **Cadence:** Available/Valid From Thursday; Available/Valid To Wednesday. No preview date; no linking document.

## Upload & setup (owned by DOC)

- Download files locally; you will likely need to **split the flyer into individual pages** (Preview on Mac, or a PDF-splitter site on PC).
- Confirm dates on the PDF (edit details from overview if needed).
- Pages tab → upload files manually; conversion library must be **"ghostscript"** and language toggled to **French**. Save and Complete → Submit.
- **Pricing zones — create 2:** **FR** (all pages in order), then **EN** (toggle cross-language, THEN switch language to English; same pages). Add all stores to both.
- **Setup QC (FLEX):** no linking sheet; verify sessions ran; geography unchanged WoW; standard-4 thumbnails.

### ⚠️ Common errors (retailer-specific)

- **Mid-flyer page 3 swap** — about halfway through the flyer a **new page 3** is typically received. The Salaberry team sends the new file on Wednesday; it must be uploaded and processed **in-house** (~9 items, no linking needed). **Set the page swap as a trigger for 12 AM Thursday**, and create the required **JIRA trigger ticket** (see the OneGuide's linked videos).

## QC specifics

- **Box Draw (Low; Auto-Box ON as of May 2025, Box QC bot OFF).** No linking doc. Include retailer logo, sign-up page, social media, special weblinks; **exclude** coupons, packaged deals.
  - Box each item individually; **do not box anything that isn't a product.**
- **Tag / Tag QC (Low; Auto-tag OFF).** Include brand, name, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude pre/postfix, SKU, URLs.**
  - Include brand and name in their fields; include **weight in the description**; select the most relevant categories.
- **Image QC:** standard.

## FQC / flyer review (DOC)

- Check geography; double-check thumbnails; sessions ran correctly; **vertical preview** — check for colour discrepancies between the downloaded flyer and uploaded pages; complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Marché Salaberry OneGuide (Google Doc `1ltU4_m2aO1063SxrpvTRi8EubgKbbFnIrFXI8imb0PQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marches Bonichoix — Processing Guide

> **Source:** Marche Bonichoix OneGuide (Google Doc `1e96XOe_glsWcDyg0yB9z0ujxft8tB2FJyF377-NjjHo`), updated Dec 23, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | S1C1 |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ `#iga_quebec`) |
| Flyer type | Weekly Flyer (flyer type #6267) |
| Processing | Auto-stack; Strategic Ops **yes** (Feedel); OS setup; Flex (Processing Support) |

## Files & schedule

- **Files received:** Monday (via FTP, usually Tue/Wed; if not received by Wednesday, email the merchant contact).
- **Cadence:** Available Tuesday, Valid Thursday, Available/Valid To Wednesday. No linking document.
- Files are marked by the **last date of the publication**.

## Upload & setup (owned by Vendor)

- Pages → Edit → Marche Bonichoix folder → find the correctly dated folder (last date of publication).
- **Select All → upload → auto-group, all English → Save.** Then select the same files again, label **French**, and group manually with a **`0` before the ascending numbers.**
- **Pricing zones — two: French and English.** Add all stores to **both**; both zones must have the same stores/FSAs count.
- Edit details: **no theme.** Thumbnails standard-4 (1065×600 across 2 pages; stock_premium across page 1 — **capture the Bonichoix logo**, move it if needed; storefront carousel premium across 2 pages; organic across page 1).

### ⚠️ Common errors (retailer-specific)

- **Page ordering** — pages sometimes show conflicting numbering; use the page order boxed in **green**, not red.
- **Image QC** — choose PDF images with a **white background** over cutouts; if no clean PDF (grey/black background or shadow), use the cutout. Do not select images with shadows or dark backgrounds.
- **Economic Choices insert is PAUSED (as of June 9, 2025) — DO NOT ADD.**

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** No linking doc. Include special weblinks; **exclude** coupons, packaged deals, retailer logo, sign-up page, social media.
  - Items boxed by price — individual items under the same price banner boxed together. Exclude banners with no specific callouts.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Name:** product names are bolded, French version above the brand and English below. **Brand** usually not bold. **Pre/postfix:** include current price **/lb AND /kg**. **Description:** French description on French flyers, English on English flyers only.
- **Image QC:** clean white-background PDFs preferred, else cutout (see risk items above).

## Post-processing / FQC (DOC / FLEX)

- **Page Category QC (FLEX):** the retailer emails the DOC a category file (spreadsheet); follow it **exactly**. Pages not listed get **no categories**. File is in the Marche Bonichoix Google Drive; if missing, flag the DOC. Match the categories page to the last page name.
- **Item Image QC (DOC):** clean white-background PDFs, no shadows/dark backgrounds; cutout only if no clean PDF.
- **URL/Links QC (DOC):** standard.
- **Inserts (ON PAUSE until Sep 2025):** when active, English + French inserts are added from the Drive Inserts subfolder (Pages → Edit → upload, set toggles EN/FR); Track 2 tasks will look incomplete — box/tag the new insert pages (Track 1 doesn't rerun); tag insert links from the links spreadsheet (Display Type Link); place inserts after the cover/logo page (~position 2).
- **FQC checklist:** Image QC; page categories per the retailer file; pages/vendors/sessions/geography all green; **vertical scroll check** (pages not squished); FQC checklist; **flyer sorting = newest flyer first.**
- **Flyer Review type: Lite.**

---
*Source: Marches Bonichoix OneGuide (Google Doc `1e96XOe_glsWcDyg0yB9z0ujxft8tB2FJyF377-NjjHo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# MarchesTAU — Processing Guide

> **Source:** MarchesTAU OneGuide (Google Doc `1FwwWKHItEnhVx4Tgbp5x6D8NSa5RyQhfACukFQsLECA`), updated Sep 22. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channel | `#marchestau` |
| Hosted URL | N/A (in discussions for Hosted) |
| Flyer types | **Monthly Flyer** (direct, ~1–2/mo) · **Mini Flyer** · **Produce Flyer** (one-pager) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons/Feedel |
| Lead time | **7 business days** required (custom link process) |

## Files & schedule
- **Files received:** Wednesday (Monthly). No email sent when files drop — **check SFTP regularly**.
- **Cadence (Monthly):** Available/Valid From Monday → To Sunday.
- **Produce Flyer:** file usually shared late; **must be uploaded the same day received**. If files arrive Thursday, go live following Monday; if Friday, go live following Tuesday.
- **Linking:** Links are embedded in the PDF (retailer cannot supply a spreadsheet), so a unique mid-process linking procedure is used — see URL/Links QC below.
- Schedule is set at the start of the year and rarely changes; enforce lead time for additions.

## Upload & setup
- **Monthly & Mini:** files in SFTP ≥ 8 business days ahead. Manual upload all pages → Auto group → **FR only**. **2 PZ = base = FR, base cl = EN.** Add all stores.
- **Produce (one-pager):** manual upload page in French; **2 PZ = base FR, base cl EN**; add all stores; mass-attach linking sheet to vendor tasks.
- **Setup QC:** Available/Valid dates match PDF; toggle **Available everywhere**; check theme (else No Theme).
- **External run names:** Monthly = *Monthly Flyer* / *Circulaire*; Mini = *Mini Flyer* / *Mini Circulaire*; Produce = *Fruits and Vegetables Flyer* / *Fruits et Légumes Circulaire*.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item individually.
- **Tag / Tag QC (Low; Auto-tag ON for Monthly/Mini, OFF for Produce):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Produce one-pager:** linking document required for both box & tag; **all items must be tagged with their correct URLs** from the linking doc attached to the pipeline.
- **Image QC:** standard.
- **Spotchecks:** standard.

## ⚠️ Common errors / risk items
- No drop email — **monitor the SFTP** so files aren't missed.
- Links are embedded in the PDF only; missing the mid-process link collection breaks the custom linking.
- FQC: items without a URL should be **< 10%**; investigate missing Produce URLs against the linking sheet.

## URL/Links QC (owned by DOC) — Monthly linking process
- Links are embedded in the PDF pages; DOC clicks into the **raw PDF** (not the FAdmin-uploaded version) and copies links into the URL field.
- **Flow:** DOC files an ARB ticket → Flex completes the link pulls → DOC applies links.
- Rename file **MarchesTAU MM YY Links** and file the ARB ticket for Flex, including the link document, the SFTP path, and the reference video.
- **Post-processing steps (all flyer types):** QC thumbnails Standard 4; confirm external run name; every priced/callout item is boxed; no overlapping boxes; sessions all green; Geography no changes.

## FQC / flyer review
- **Flyer Review type: Lite** (completed by Flex). Dates same as PDF; Available = Valid; available everywhere; external run name set; check pagination order; item boxes; iframe; vertical geography; no change WOW.

## Out-of-processing
- Page swaps and post-live checks handled ad hoc (see OneGuide video reference).

---
*Source: MarchesTAU OneGuide (Google Doc `1FwwWKHItEnhVx4Tgbp5x6D8NSa5RyQhfACukFQsLECA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Marc's Grocery — Processing Guide

> **Source:** Marc's Grocery OneGuide (Google Doc `1ur8X7iuStH_mKFPWGGoSB-fYzu5rLnSPxwdNFMTNrZA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | marcs.com |
| Flyer types | Weekly (merchant #3101/3199); Distribution Category: Grocery |
| Processing | Auto-stack; Strategic Ops **yes** (Feedel); OS setup; Flex flyer review |

## Files & schedule

- **Files received:** via FTP ~two weeks before the flyer run; files marked by the **valid date** of the publication (e.g. `06142017 Flipp`). Live 12 AM Tuesdays; preview date Thursday before live.
- **Linking document:** **Yes** — `Inmar.pdf` and `PageLayout:Inmar.pdf` in the FTP, uploaded per week. Attach each as a mass attachment to all vendor tasks (if `PageLayout:Inmar.pdf` is missing, use `Inmar.pdf`).

## Upload & setup (owned by Vendor)

- **Internal name:** Valid Date (Preview Date); external "Weekly Ad"; Distribution Category **Grocery**.
- **Manual upload** from the corresponding dated folder. M5 pages may be in a separate folder; additional pages should all be uploaded. Page pagination comes from `PageLayout_Inmar.pdf`. Additional pages should match the page index/order they're placed in.
- **Pricing zones:** 5 standard — **M1, M2, M3, M4, M5**. (M6 is used for **NEW STORES only** — get store details from the lead.) Create each manually and assign pages by file name; some pages serve multiple zones (e.g. `P3 M1234` = page 3 for M1–M4). Assign stores via the preset store sets.

### ⚠️ Common errors (retailer-specific)

- **Box every individual item separately** — if multiple items share one box, box each one.
- **Brand on every item** — put the brand in both the name field (before the product name) and the brand field. Every item should have a brand (product or logo).
- **Image selection** — select the correct PDF only when clean/transparent; use the cutout when no clean PDF; **no PDF images for text-line items** (use cutout). For grouped items select the PDF of one item; don't use a single image to represent a group.
- **Coca-Cola products** — verify brand, name, and description are tagged correctly.
- **Coupon ID tagging** — see below; a recurring risk item.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** Linking doc required. Include retailer logo, sign-up page (WIC), social media, special weblinks, store locator, payment policy, digital coupon program, party-tray/gift-card creatives; **exclude coupons.** Boxes must **not overlap**; items with their own description boxed individually; multiple line items boxed each separately.
- **Tag / Tag QC (High; Auto-tag OFF; PDF image auto-selection ON).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Coupon ID (custom field):** tag the **"Manufacturer Offer ID"** from the Inmar PDF into the **Coupon ID** field for the applicable items. Keep **Display Type = "Item"** (NOT Coupon). Use the item name (highlighted blue in the Inmar doc) to verify; the Manufacturer Offer ID is highlighted orange.
  - Name: full name, no special characters (e.g. `•`). Include quantities in the description. Add dollars-off/percent-off where applicable.

## Post-processing / FQC (DOC)

- File a **FAB ticket** to have FLEX complete Image QC, Coupon ID QC, and spotchecks (clone the sample FAB ticket, update due date, flyer run, Inmar doc, assignee, dates, links). If Image + Coupon ID QC will take >30 min, file a FAB ticket for FLEX support.
- **FQC checklist:** Links QC (no links) marked done; check dates (live 12 AM Tue); Distribution Category Grocery; preview date Thursday; shown on all channels; spotlights/key messages; open pricing zones full-screen and click items to confirm pops/links work; confirm all pages in correct zones; Item Image QC (clear PDFs — line items use no PDF images); page-level categories (**no categories on page 1**, check for sub-pages); thumbnails (M1–M6 share thumbnails, **M7 adjusted separately**).
- **Coupon ID QC:** open the `Inmar.pdf` for the run, use Item Search ("Name" "CONTAINS") to find each listed item, and tag the corresponding Manufacturer Offer ID into the Coupon ID field.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps handled per the baseline page-swap process. Black Friday comms exist for 2024/2025.

---
*Source: Marc's Grocery OneGuide (Google Doc `1ur8X7iuStH_mKFPWGGoSB-fYzu5rLnSPxwdNFMTNrZA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mariana's Supermarket — Processing Guide

> **Source:** Mariana's Supermarket OneGuide (Google Doc `1j_zyFFJT8aNyMiobeAnd8GUNMFksel6o03UlQLye0Ns`), updated Jul 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | N/A |
| Flyer type | Flyer #1 (files ad-hoc; monthly cadence) |
| Processing | Auto-stack; Flex (Processing Support); no coupons/Feedel |

## Files & schedule
- **Files received:** ad-hoc. **Cadence:** monthly. **No preview date. No linking document.**
- Files sent via FTP: 1 zone, English, all pages, all stores.

## Upload & setup (owned by Flex)
- **Manual upload:** Pages → Edit → select the flyer's folder dropdown. **Upload individual pages only — do NOT upload the full flyer PDF.**
- Auto-group.
- **Flyer creation:** one pricing zone named **Base**; add all pages; Save and done.
- Add all stores.
- **Setup QC:** confirm all items in the setup QC checklist are correct.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates. Brand: No.**
- **Spotchecks:** standard (reference Tag/Tag QC instructions).
- **Item Category QC / Item Image QC:** owned by DOC (no detailed specs filled in).

## FQC / flyer review
- **No special risk items** — use generic flyer review standards and instructions.
- **Flyer Review type: Lite** (owned by Flex) — see the Mariana's Supermarkets flyer review guide.

> This OneGuide is largely a standard template with few retailer-specific instructions; the key differentiators are Auto-Box/Auto-tag OFF, SKU included, valid dates and brand excluded, and single English "Base" zone with individual-page upload.

---
*Source: Mariana's Supermarket OneGuide (Google Doc `1j_zyFFJT8aNyMiobeAnd8GUNMFksel6o03UlQLye0Ns`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mark's — Processing Guide

> **Source:** Party City CAN / Mark's OneGuide (Google Doc `1r7d4NSK1zUephrsRRNTVFI3yWcEFR-huZ70R72c3SQc`), updated May 11, 2024. Contacts/credentials omitted.

> This OneGuide is shared between **Party City Canada (3632 Local Ad)** and **Mark's / L'Équipeur (LEQ)**. This article covers the Mark's family; Party City CAN specifics are summarized at the end.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#partycitycanada` |
| Hosted URL | partycity.ca (Mark's shares marks.com / lequipeur.com) |
| Flyer types | **Mark's** (weekly, EN) · **L'Équipeur / LEQ** (EN + FR, hosted, then cloned Flipp-only) |
| Processing | Auto-stack; Strategic Ops **Yes (Feedel)**; no coupons |

### Mark's three-flyer structure (all go live together)
- **Mark's merchant → Mark's flyer type** — EN.
- **Mark's merchant → L'Équipeur flyer type** — EN + FR (Hosted).
- **Clone to L'Équipeur merchant → LEQ flyer type** — EN + FR (Flipp only, hide in hosted).
- Two different merchants share the same website.

## Files & schedule (Mark's / LEQ)
- **Files received:** Monday. **Cadence:** Available From Tuesday, Valid From Wednesday → Available/Valid To Tuesday. One-day preview.
- **Linking document:** Yes — SKU "SN" document (pages with SKUs printed on images) + a URL document emailed weekly.

## Upload & setup

### Mark's (EN) — owned by DOC
1. Manually upload pages (select `nat` folder, uncheck `sn`) → Auto-group.
2. **1 PZ: Base.**
3. Assign stores from the **generic codesheet** (Marks tab), download as CSV.
4. **Codesheet upload:** Config **`generic_stores`**, PDF base directory `/`, **check off first toggle only**.
5. **SN process:** upload the "NAT-WK xx -SN" PDF (SKUs on images) to the shared Google Drive. ⚠️ **RISK: FTP breaks it into multiple pages — attach the one large document.**
6. **URL document manipulation:** delete columns *Family ID/Web ID*, *Overarching offer URL - LEQ*, *Product Landing Page URL - LEQ*; delete top rows (Project, Docket Number, contacts); save as `.xlsx`; attach to all vendor tasks with the note referencing pages 31–32 of the OneGuide.
7. **Edit Details:** available everywhere; one-day preview; no theme (Black Friday/Holiday occasionally). 4 standard thumbnails.

### L'Équipeur / LEQ — owned by Flex
- Manually upload pages (select `leq` folder, uncheck `sn`), ENG toggle; upload same pages again toggled FR. ⚠️ **RISK: sometimes LEQ has FR pages only — that's fine, upload FR only (no need to confirm).**
- Auto-group. **PZs: EN + FR** (or just FR if only FR names).
- Assign stores from generic codesheet (LEQ tab). ⚠️ If FR-only zone, delete EN stores/PZ from codesheet.
- Codesheet upload: Config **`generic_stores`**, base `/`, first toggle only.
- SN + URL document process as above (delete Mark's columns, keeping both if LEQ has EN+FR content).
- **Edit Details:** available **only on hosted**; one-day preview; no theme usually. 4 standard thumbnails.

## QC specifics (Mark's / LEQ)
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. **Include** packaged deals, retailer logo, sign-up page, special weblinks; exclude coupons, social media. Also **box the sale-callout section** (prices + callout). Sign-up pages link to marks.com / lequipeur.com.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs** (applied via item import).
  - Name/Brand = bolded text or per SN document. SKU from SN/URL doc. Usually 1 price (Current).
  - **Sale-callout section:** URL = overarching offer URL (column F); tag **ALL** SKUs in the callout.
  - **Regular items:** URL = Product Landing Page URL (column H); tag only individual SKUs. If a Product Landing Page URL is blank/N/A, use the Overarching offer URL.
- **Image QC:** **clean PDF preferred**, cutout otherwise.

## ⚠️ Common errors / risk items
- FTP splits the SN document into many pages — attach the single large file, not the split pages.
- Keep EN pages → EN links and FR pages → FR links (LEQ).
- URL doc: copy/paste as values to remove formulas; delete blank rows (triangle banner, email sign-up); ensure search-link URLs are reflected.

## URL/Links & SKU QC (owned by DOC)
- Build the import: dedupe/clean the URL sheet; replace *Style Number* → *SKU*; add `item_id` column; duplicate into Mark's (`item_id, sku, url`) and LEQ (`item_id, sku, english_url, french_url`); download CSV → item import. If doing a trigger import, mark items in-store after the trigger runs.
- **SKU QC:** item search SKU IS blank — ensure no missing SKUs (cross-reference EN/FR page or SN document).

## FQC / flyer review
- **Mark's FQC:** SKU check (all items have SKUs if applicable); items without URL → fill from URL doc; sign-up page → marks.com/en.html; Image QC clean PDF/datapipe first; page categories skip p.1; mark items in-store via Sessions.
- **LEQ FQC:** as above (EN↔EN, FR↔FR links) then **clone LEQ flyer to the LEQ merchant** (uncheck Clone to Mark's; add "(Flipp)" to name; no tracking codes; hide in hosted + avail in distribution & Flipp; assign stores via codesheet; 4 thumbnails).
- **Post-FQC:** send preview link to retailer (Mark's + LEQ) per email template.
- **Flyer Review type: Lite.**

## Party City Canada (3632 Local Ad) — summary (shared doc)
- **Cadence:** files Monday; Available/Valid From Friday → Available To Monday / Valid To Tuesday. Strategic Ops (Feedel).
- **Upload (Flex):** upload FR pages first (toggle FR, Save & refresh — toggles can revert), then EN pages; auto-group (watch FC=front/BC=back cover); 2 PZs (EN, FR); assign **all regions excluding MB & QC**; Standard 4 thumbnails. Invalid-stores-assigned warning can be ignored.
- **Box Draw (Auto-Box ON, Box QC bot ON):** include retailer logo, sign-up page, special weblinks; exclude coupons, packaged deals, social media. Box last-page banners (Celebrate Life's Moments → partycity.ca; Triangle → triangle.canadiantire.ca; Financing links); box SKU'd items.
- **Tag (Auto-tag OFF):** **no linking doc going forward — search SKUs on partycity.ca** and box/tag per the site. Name matches website; **do not include website description**; URL = the item's page from the SKU search. Exclude description; include SKU.
- **FQC:** Standard 4 thumbnails; mark items in-store; UTM tracking codes for promoted flyer only (reapply after page swaps); Page Level Modifier → Zoom Always Page Fit; check EN/FR last-page banners.
- **Cloning:** Party City has a promoted and a non-promoted version. Clone under ad-hoc processing, prefix `[NOT PROMOTED]`, do not copy tracking codes; set EN & FR stores to **Manitoba and Quebec** only.
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Party City CAN / Mark's OneGuide (Google Doc `1r7d4NSK1zUephrsRRNTVFI3yWcEFR-huZ70R72c3SQc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Martin's Super Markets — Processing Guide

> **Source:** Martin's Super Markets OneGuide (Google Doc `1KpVxoOw2cDqbj8sBOZI3coBMhuOOCg6Wido0DPWV03E`), updated Mar 13, 2026. Contacts/credentials omitted.

> Processed under the SpartanNash banner group (files dropped by the SpartanNash ops contact for all SpartanNash banners).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#spartannash`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type | Weekly |
| Processing | Auto-stack, full processing; Flex (Processing Support + Flyer Review); no coupons/Feedel |
| Stores | 26 |

## Files & schedule
- **Files received:** Monday (dropped to FTP with a Posting Document; email sent when files drop). *(OneGuide also references a Tuesday drop in setup notes.)*
- **Cadence:** Available & Valid From Sunday → To Saturday. **No preview.**

## Upload & setup (owned by Vendor)
- Download the **Posting Document** to confirm page order; upload pages from FTP and order per that document.
- **Pricing Zone:** Name = **Base**; add all (26) stores.
- Wait for sessions; ensure vendor tasks are ready/active.
- **Edit Details:** Available/Valid Sunday→Saturday (no preview); **hidden in hosted**; **no theme**; thumbnails Standard 4.
- **Clear the FTP** (including the Posting Document) when done.
- **Setup QC:** confirm all pages uploaded (Items View) — if uploading from SFTP, confirm no pages left un-uploaded; confirm flyer dates (first/last page); thumbnails; preview dates set.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include** coupons and packaged deals; exclude retailer logo, sign-up page, social media, special weblinks/savings banners. Each item with a unique price gets boxed/tagged as a separate product.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - **Name** should include all items offered in the ad block. Prefix from approved drop-down.
  - **Multiple prices:** put the **Sale Price in Current Price** and the **Coupon/Extra-Savings offer in Sale Story** — do NOT put the second price in Original Price.
  - **Sale Story** captures everything in the blue box (Extra Savings, MFR Rebate, Digital Coupon).
  - **Categories:** every item needs one — Baby → *Health and Beauty*; Pet → *Grocery*.
- **Image QC:** **NOT using PDF images — use item cutouts only.**

## ⚠️ Common errors / risk items
- If client sends files by email, processor may need to add pages to the SFTP.
- **Watch for 2-Day / 3-Day sale banners** — tag all items in that banner with the appropriate unique valid dates.
- Don't put a second/coupon price in Original Price (see Tag rules above).

## FQC / flyer review
- **Pre-FQC:** finish spotchecks; check narrow pages in Storefront Spotcheck per PZ and merge to next page if any (mark Autostack Spotcheck complete); Image QC not required (no client specs); review special-day (e.g., 3-Day) valid dates.
- **FQC:** spot checks; thumbnail QC (Standard 4); legibility heights; geography vs prior week; page order/region; toggles; all items tagged; dates match PDF; no 'real' overview warnings.
- **Flyer Review type: Lite** (owned by Flex): flyer dates, sessions completed, previews correct, tagging accurate, geography, availability toggles.

---
*Source: Martin's Super Markets OneGuide (Google Doc `1KpVxoOw2cDqbj8sBOZI3coBMhuOOCg6Wido0DPWV03E`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mastermind Toys — Processing Guide

> **Source:** Mastermind Toys OneGuide (Google Doc `1sJjK4Wzzz_IfMq-5atAWJBIEMZ-irXjGt1Auffn1mtY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | Flipp + Distribution only |
| Slack channel | `#mastermindtoys` |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex not involved; OS completes standard tasks |
| Vendor guide | Confluence VEN — Mastermind Toys New Vendor Guide |

## Files & schedule
- **Cadence:** Available & Valid **Thursday**.
- **Linking document:** Yes — attach to **all** vendor tasks.

## Upload & setup
- **Manual upload:** Pages tab → Edit → upload from the corresponding FTP folder → Auto-group (do **not** process internally).
- **Pricing Zone:** Base. **Store selection:** add all stores.
- **Vendor tasks:** attach the linking document to all tasks.
- **Linking-document manipulation:** ensure **all links end with `?utm_source=flipp&utm_medium=referral`** (UTM tracking code).
- **Setup QC:**
  - **Toggles:** Hidden in Hosted.
  - **Available dates:** Thursday → Sunday (confirm via client emails / Slack / BD memos); **Valid = Available** unless otherwise stated.
  - External run name: N/A. Theme: N/A unless otherwise stated (Black Friday, Holiday, etc.).
  - **Legibility heights: 40/30.**
  - **Thumbnails: Standard 4 + Custom Tile** (Custom Tile submitted via FTP; added to Storefront Carousel Premium & Storefront Premium).

## QC specifics
- **Box Draw (Low):** **include** social media, sign-up page, special weblinks, retailer logo, packaged deals. **Exclude coupons** (none). Use text boxes if needed for non-clean boxes.
- **Tag / Tag QC (Low):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Linking document used for tagging and item QC.
  - **Name/Brand** = bolded text. **Description** = other (often colour, age range). Usually only 1 price (Current). Pre/postfix rare. Valid dates same for all items. URLs from linking document. Sale Story if applicable ("NEW", "BOGO", "30% off"). Disclaimer on final page bottom.
- **Category QC:** add page categories based on each page's contents.
- **Image QC:** **cutouts only** (all items).

## ⚠️ Common errors / risk items
- **UTM links:** every URL must carry `?utm_source=flipp&utm_medium=referral`.
- **Banner & category links:** if the client provides a link for a specific callout, category, or banner, it must be **boxed, tagged, and listed as a Link**.
- **Flyer not showing on Hosted is a false error** — the flyer should NOT be on Hosted (Hide in Hosted checked).
- Multi-product blocks: box/tag as several products, not one.

## Pre-Final QC
- **Pricing Zone:** all products, banners, logos, callouts in the linking doc are boxed and tagged; review horizontal preview.
- **Pages tab:** QA page categories; spotcheck product links.
- **Overview:** toggles (hidden in Hosted only); dates Thursday–Sunday; external run name N/A; theme N/A unless stated.
- Items without a URL → check linking document; Image QC cutouts only; thumbnails Standard 4 + Custom Tile; leg heights 40/30.

---
*Source: Mastermind Toys OneGuide (Google Doc `1sJjK4Wzzz_IfMq-5atAWJBIEMZ-irXjGt1Auffn1mtY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Materiaux JLS — Processing Guide

> **Source:** Materiaux JLS OneGuide (Google Doc `1HGkRnd8c74A0FrLUCymAcEXaXAlCA7BP5d2IkHrgN_Q`), updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#1plat_materiaux-jls` |
| Flyer type | Flyer #1 (12059) |
| Processing | Auto-stack; no coupons/Feedel |
| Languages | EN + FR |

## Files & schedule
- **Files received:** Thursday.
- **Cadence:** Available From Thursday → Available To Wednesday; flyer can run **one week or two** — always check dates for the proper valid length.
- **Linking document:** N/A (URLs sourced by SKU search on the retailer site).

## Upload & setup (owned by DOC)
- **Manual upload:** Pages tab → Edit → select all pages from the SFTP → Confirm & Upload. **Reselect the same pages and upload twice** (a "pages already uploaded" warning is expected — proceed).
- Add page numbers into the Grouping Number field; set one set of pages **EN** and the other **FR**; Save & Confirm — **do NOT process internally**.
- **Pricing Zones:** create **EN PZ** and **FR PZ** with their applicable pages; add all stores to both.
- **Vendor notes:**
  - EN Tag/Tag QC: *Search SKU on https://materiauxjls.ca/en/ and add URL to each product.*
  - FR Tag/Tag QC: *Search SKU on https://materiauxjls.ca and add URL to each product.*
- **Setup QC:** confirm all pages uploaded (Items View); if uploading from SFTP, confirm no un-uploaded pages remain; confirm dates (top of first page); thumbnails Standard 4; preview dates set.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Linking-doc-specific tagging.
  - **URLs:** FR pages → search SKU on `materiauxjls.ca`; EN pages → search SKU on `materiauxjls.ca/en/`.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing spotchecks in pipeline.

## ⚠️ Common errors / risk items
- **Dates:** confirm whether the flyer runs for one week or two.
- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- Remember to upload pages **twice** (EN + FR sets).

## FQC / flyer review
- **Pre-FQC:** dates correct per PDF; toggles correct; thumbnails include retailer logo; all items boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (owned by DOL): flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: Materiaux JLS OneGuide (Google Doc `1HGkRnd8c74A0FrLUCymAcEXaXAlCA7BP5d2IkHrgN_Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Matériaux Pont Masson — Processing Guide

> **Source:** Matériaux Pont Masson OneGuide (Google Doc `134qnMqtapyFXuwUoIQ8ie5YgF1qq-mNM4mUZOzbwBZE`), updated Feb 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#materiaux-pont-masson`, `#flex-processingsupport` |
| Flyer types | **Weekly** (bi-weekly cadence) · **Seasonal** (ad-hoc) |
| Processing | Auto-stack; Flex (Processing Support); no coupons/Feedel |
| Languages | EN + FR |

## Files & schedule
- **Files received:** Thursday (~11 AM by email): one set of EN pages, one set of FR pages, and a linking `.csv`.
- **Cadence:** Available & Valid From Thursday → To Wednesday.
- **Linking document:** Yes.

## Upload & setup (owned by Vendor)
- **Pre-processing:** open the retailer's `.csv`, add the same headers, save as `.xlsx`. Download all documents and transfer to SFTP. Retailer sometimes sends extra banner/promo links — paste them into the flyer run comment box.
- **Upload:** manually upload files; EN pages set EN, FR pages set FR; Auto-group → **Save**, confirm, then **Save & Complete**.
- Attach the `.xlsx` linking document to vendor tasks.
- **External run names:** EN = *Weekly Flyer*, FR = *Circulaire Hebdomadaire*.
- **Pricing Zones:** 1st PZ = **EN** (English), 2nd PZ = **FR** (French); add all stores to **both**.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc used for both Box/Tag. **Include** packaged deals; exclude coupons, retailer logo, sign-up page, social media, special weblinks. Box each item block.
- **Tag / Tag QC (Low; Auto-tag ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - ⚠️ **DO NOT USE PDF IMAGES** (despite PDF Image Auto Selection being enabled).
  - All visible SKUs tagged in the SKU field; text matches the language version and is pulled from the spreadsheet where possible.
  - **Links:** add a URL to any item that has a SKU — search the SKU on **pontmasson.com**.
- **Image QC:** clean images when available; if no clean PDF image, select the cutout.

## ⚠️ Common errors / risk items
- **Seasonal ad-hoc publications** are uploaded into the "Seasonal" flyer type — new flyer shells must be created.
- **Do NOT use PDF images** even though auto-selection is on.

## Post-processing / FQC (owned by Flex)
- **URL/Links QC:** check the retailer email for special banner links and tag correctly. Item search for items missing URLs → search SKU on pontmasson.com/en (EN) then re-check FR (PZ id `fr`) using pontmasson.com/fr.
- **Ad-hoc QC:** clear remaining spotchecks; review images for black backgrounds; draw QC thumbnails (1065×600, Storefront Carousel Premium, Storefront Carousel Organic); dates match PDF front page; set seasonal theme (even if No Theme); item counts equal across PZs; all prices/sales stories/offers/CTAs boxed; vertical preview clickable; Geography no changes WOW.
- **FQC:** confirm **Flyer Sorting = "Flyer Type Newest First"** (Weekly above Catalogues); dates correct; toggles correct; thumbnails include retailer logo; all items boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography unchanged.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swap process.

---
*Source: Matériaux Pont Masson OneGuide (Google Doc `134qnMqtapyFXuwUoIQ8ie5YgF1qq-mNM4mUZOzbwBZE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Materio — Processing Guide

> **Source:** Materio OneGuide (Google Doc `1nDE68ea1Ui5XXuaSHdT1-gPXnWxsoW8-2kJTQX3lQK0`), updated Jun 16, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#materio`, `#flex-processingsupport` |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons/Feedel |
| Language | French |

## Files & schedule
- **Files received:** Thursday (dropped in SFTP).
- **Cadence:** Available & Valid From Thursday → To Wednesday.
- **Linking document:** Yes.

## Upload & setup (owned by Vendor)
- Manually upload all `_p000#.pdf` pages into the flyer run; **set all pages to French**; Auto-group.
- **Pricing Zone:** 1 PZ = base = FR; add all stores.
- Attach the linking document to all vendor tasks.
- Complete Setup QC; ensure vendor tasks are available.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc used for both Box/Tag. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box items with multiple SKUs/items shown.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON):** include brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.**
  - Tag fields as on the flyer: Name, Description, SKU, Current Price, Original Price (prix courant — in description).
- **Image QC:** **clean images should always be shown** (majority should be PDF images — flagged multiple times by the retailer).

## ⚠️ Common errors / risk items
- **Links:** ensure the linking document is attached and links are boxed and tagged.
- **Image QC:** retailer has repeatedly flagged that the **majority of images should be PDF images** — do not skip this step.

## FQC / flyer review (owned by Flex)
- **Legibility heights: 45 / 25.**
- Item Image QC — majority PDF images.
- **QC Thumbnails:** 1065x600, thumbnail, carousel premium, carousel organic.
- **Item search:** SKU IS NOT blank + URL IS blank → search the SKU on **materio.ca**; if the SKU isn't on the site, skip that item (can be assigned to Flex).
- **Edit Details:** dates match PDF (Available = Valid); available everywhere.
- **Pricing Zone:** Items view — all offers with a sales callout, price, or CTA are boxed; full-screen view — popup, clean image, price/callout, product name; horizontal view — no cut-off/missing pages, interactivity works.
- **Sessions:** all green (rerun any that aren't).
- **Flyer Review type: Lite.**

---
*Source: Materio OneGuide (Google Doc `1nDE68ea1Ui5XXuaSHdT1-gPXnWxsoW8-2kJTQX3lQK0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Maxi — Processing Guide

> **Source:** Maxi OneGuide (Google Doc `10WhIme3hoBHT996KoEt8P-wpFhBZLt6d2t5e28i8GL4`), updated May 18, 2024. Contacts/credentials omitted.

> Loblaw-family (LCL) account — uses the Flex LCL tracker and codesheet upload. **Medium tagging complexity** (SKU + Article Number workflow).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer types | **3800: Weekly** · **9375: Global Foods Flyer** |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops **Yes (Feedel)**; no coupons |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available/Valid From Tuesday → Available To Monday / Valid To Tuesday. **Sunday preview** (2-day consumer preview per codesheet).

## Upload & setup
> Upload is normally completed by FTEs; full-time processors must first put the codesheet into the tracker.

- **Processor prep:** find the final "wk # Maxi" codesheet in email → add to the Maxi folder in Google Drive → toggle the Flex LCL tracker (F25 codesheet dropped, E25 files ready in SFTP).
- **⚠️ NEW 2026: Set Pixel Height to 4096 BEFORE any pages are uploaded** (Edit Details → show/hide rarely-used fields → Height → 4096.0). If pages already uploaded, flag the Full-Time Ops stakeholder and continue.
- **Codesheet manipulation:** unhide all sheets; delete print/dates/store-ledger tabs; clear content of rows 1–7 (pagination starts row 8); on each tab, copy the PZ name into cell A1 and replace the original PZ-name cell with "STORES"; download as XLS.
- **Codesheet upload:** Config **`maxi`**; PDF base directory from stale; **all toggles but second and last**.
- After it runs green, check Maxi's **stale SFTP** for pages not uploaded and manually upload the missing ones (mark them **French**; toggles can revert — re-check).
- **Pricing zones:** cross-reference page counts vs the linking doc; manually add pages back for FR zones (no "EN" in name); then copy layout from the FR counterpart into each **EN** zone (untoggle Cross language → French → select FR version → Copy layout → re-toggle Cross language → English → Save). *Note: 2× PZs as codesheet tabs (each has an FR counterpart).*
- **Edit Details:** check dates (2-day consumer preview); No Theme; set **Sunday preview** start; External Run Name = *Weekly Flyer - Valid [dates]*. Regenerate FSAs on overlapping-FSA warning.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** coupons, packaged deals, sign-up page; exclude retailer logo, social media, special weblinks. Box only when there's a unique price; box "PC Biologique" section as 4 separate items. Exclude banners and social icons.
- **Tag / Tag QC (Medium; Auto-tag OFF):** include everything (brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs).
  - **Name:** ALL CAPS, format `BRAND PRODUCT NAME, Quantity` (**always a comma before quantity**). On bilingual pages include both FR and EN names in the Name field. **Exclude** per-kg metrics, "Product of…", "No 1 Grade", "Frozen", "Selected varieties" (these go in Description).
  - **SKU:** must start with **"2"** (ignore any that don't); include unit of measure (`_KG`, `_EA`, etc.); drop leading zeros; then **Fetch URL**.
  - **URLs:** click **Fetch** after SKU entered; verify the link (wrong item/size → remove and search by name; different flavour or Maxi home page → leave). If no SKU, search on maxi.ca. All items with a SKU will have a URL.
  - **Article Number:** copy the Product SKU into the Article Number field (with unit of measure). Article Number 1 = same as SKU/Fetch URL. Multiple SKUs → Article Number 1–4 in order (only as many as SKUs provided).
  - **PC Optimum Members Pricing** = Current Price with prefix "PC Optimum Members Pricing".
- **Image QC:** clean PDF where possible; cutout if not clean.

## ⚠️ Common errors / risk items
- **Article Number field** (bottom of Tag interface): one SKU per field, include unit of measure, Article Number 1 must match SKU + Fetch URL.
- SKU must start with "2" — ignore others.
- **⚠️ Thumbnail critical-zone check (ATL vs QC):** verify whether ATL (Atlanta) and QC (Quebec) pages have different dimensions. Do NOT apply ATL thumbnail formatting to the whole run if dimensions differ — draw separate thumbnails for the later QC zones to prevent cut-off/distortion.
- Check the SFTP for revised files before go-live and swap in rev pages.

## Post-processing / FQC (owned by DOC)
- **Pagination & store QC:** use the revised codesheet if one arrived after upload; check PZ pagination and that store #s match the codesheet.
- **URL/SKU/Article Number QC:** item search SKU IS NOT blank + URL IS blank → open & Fetch; Article Number 1 IS blank + URL IS NOT blank → add the article number.
- **Ad-hoc QC:** dates (Available Wed→Wed 1-day preview; Valid Thu→Wed); External Run Name; No Theme; thumbnails — 1065×600 (2 pages), stock premium (1), storefront carousel premium (2), storefront carousel organic (1); vertical + horizontal scroll checks; link QC from codesheet.
- **FQC:** confirm newest weekly flyer shows first on the flyer-sorting page.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put flyer run ID in the LCL tracker; run ghostscript 9.06 gamma as needed; flyer sorting (current weekly → ethnic → upcoming → secondary newest-to-oldest); Article # revision. **Page Swap:** standard.

---
*Source: Maxi OneGuide (Google Doc `10WhIme3hoBHT996KoEt8P-wpFhBZLt6d2t5e28i8GL4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mayrand — Processing Guide

> **Source:** Mayrand OneGuide (Google Doc `1qKx7bExVprWGPjE84y9LPOIlg77CttQbpMcQucwNWpg`), updated Oct 21, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#mayrand` |
| Flyer type | Weekly (11319) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons/Feedel |
| Languages | EN + FR |

## Files & schedule
- **Files received:** Thursday.
- **Cadence:** Available From Wednesday → Available To Tuesday; Valid From Tuesday → Valid To Wednesday. **Friday preview.**
- **Linking document:** Yes (English- and French-specific URL/tagging document).

## Upload & setup (owned by Flex)
- **Manual upload:** Pages tab → Edit → select all pages from SFTP → Confirm & Upload. Assign pages with **FR** in the name to French, **EN** to English. Save → Auto-Group (zipper) → Save & Complete (do NOT process internally).
- **Pricing Zones:** create **EN PZ** and **FR PZ**; assign English pages to EN, French to FR; add all stores to both.
- **Setup QC:** confirm all pages uploaded; confirm dates (first/last page); thumbnails Standard 4; **no preview date (Available = Valid)**; no theme.
- **⚠️ IMPORTANT:** before attaching the linking documents to vendor tasks, **delete columns E–AC**, save as `.csv`, then attach.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include** retailer logo and special weblinks; exclude coupons, packaged deals, sign-up page, social media. Box any product block with a price or sales story; box all social media and weblinks.
  - **Only** box and tag these headers (EN or FR): *Nos Heures D'Ouverture / Our Stores*, *Service Personnalisé / Our Services*, *Site Internet / Website*.
- **Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** PDF preferred if clean; otherwise cutouts (owned by Vendor).

## ⚠️ Common errors / risk items — tagging (most valuable)
- **ALWAYS follow the URL/tagging document (EN- and FR-specific), NOT the PDF**, as the tagging guideline.
- **SKU goes ONLY in the SKU field** — never in the Name or Description.
- All text under the document's **Name** column goes in the FAdmin Name field (except the SKU). If a descriptor (e.g., "540 ml") is included under Name by the retailer, put it in the Name (no duplicate in Description).
- Information **not** in the tagging doc (e.g., "9.90$/kg") should not be in the Name but **should still be tagged**.
- Common incorrect examples: Name not following the URL doc; SKU duplicated in the description; brand name omitted from the brand field.

## Post-processing / FQC
- **Pre-FQC Links QC** — **there should be 0 items without URLs:**
  - Item Search → URL → IS → (blank): assign URLs from the linking docs.
  - URL CONTAINS `/en/` with Language French → confirm no French items get English URLs (and vice versa for `/fr/`).
  - URL CONTAINS `%3B%22` → remove that and everything after it from the URL.
- **FQC (owned by DOC):** dates correct per PDF; available on all platforms; thumbnails drawn and include the retailer logo.
- **Flyer Review type: Lite** (owned by DOL) — see the Mayrand flyer review guide.

---
*Source: Mayrand OneGuide (Google Doc `1qKx7bExVprWGPjE84y9LPOIlg77CttQbpMcQucwNWpg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# MB Country Living — Processing Guide

> **Source:** MB Country Living OneGuide (Google Doc `1nSxZtBfsZG-_92dH_hGw0s3ZnUJaYPt4CgSkuE05J80`), last updated May 6, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | S4C3 |
| Availability | **Flipp only** (hidden on hosted; available on Flipp & Distribution) |
| Slack channels | `#mbcountryliving`, `#flex-processingsupport` |
| Hosted URL | mbcountryliving.ca |
| Flyer types & cadence | **Pet (10098)** — monthly / ad hoc |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files: ad hoc / monthly.** No preview. Files are dropped into the FTP by DOC, who also confirms by email — **please confirm receipt.**

## Upload & setup (owned by Flex)

- Flyer shells are mostly already created — you may occasionally need to adjust dates or create a new shell (go into the "pet" flyer type → "create new flyer run").
- **"Hide in hosted" should already be checked.** Confirm dates from the drop email. **No preview, so Available From/To = Valid From/To.** Internal Name = the go-live date. No theme.
- **Manual upload; auto-group. One PZ: Base — add all stores.** Hidden on Hosted (available on Flipp & Distribution). Let sessions run, then start Setup QC.
- Key message / Sale story: grab from the first page or use "pet deals."

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required (Box Draw/Box QC specific).
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** Linking document required (Tag/QC specific).
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude: pre/postfix and valid dates.**

### Image QC
- Standard pricing spotchecks in pipeline.

## Post-processing (owned by Flex)

- Item Image QC: PDF preferred if clean; otherwise cutouts accepted.
- FQC checklist.

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: MB Country Living OneGuide (Google Doc `1nSxZtBfsZG-_92dH_hGw0s3ZnUJaYPt4CgSkuE05J80`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# McMunn & Yates — Processing Guide

> **Source:** McMunn & Yates OneGuide (Google Doc `1eFyVghZuOH-e9X8rztLhexNd03sxHtEjwfhqs46ALZo`), updated Jun 24, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium (merchant 2568) |
| Availability | All platforms |
| Slack channels | `#mcmunn_yates`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | mcmunnandyates.com |
| Flyer type | Flyer 2417 (**biweekly**, runs 2 weeks) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons/Feedel |

## Files & schedule
- **Files received:** Monday (linking document dropped to FTP).
- **Cadence:** Available From Wednesday → Available To Wednesday (biweekly, 2 weeks); Valid From Wednesday → Valid To Thursday. **Monday preview.**
- Retailer refers to ads as e.g. "July #1", "July #2" (reflected in the merchant schedule).

## Upload & setup (owned by Vendor)
- Confirm dates in email; visible everywhere; no theme; no external name.
- **Manual upload:** Pages tab → Edit → select pages that match the **flyer run name** (e.g., "July #1"); select all lowercase pages for all zones labelled with that name (North, SouthA, SouthB, SouthC, SouthD, etc.) → Confirm & Upload.
- Auto-Group or manually number; ensure language = **English**; Save & Confirm (do NOT process internally).
- **Pricing Zone creation:** create PZs based on the **Version List `.xlsm`** in FTP and assign stores accordingly. Add pages labelled with the PZ name to the correct zone (SouthA pages → SouthA zone).
- **Attach the linking doc from the SFTP.**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (first/last page); thumbnails Standard 4; preview dates set.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **include** retailer logo; exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box all items separately (text boxes when necessary); box items with multiple types/models individually.
- **Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU** (tagged in brackets per notes but not the SKU field).
  - **⚠️ Tag-Lite retailer — DO NOT tag Name, Brand, Description, SKU, Sales Story** (auto-tagged). If a Name is missing, tag the name.
  - URLs come from the Links Spreadsheet in the Vendors tab; match SKUs on the linking doc to flyer items and use the URLs **exactly** as provided.
- **Image QC:** **clean images / PDFs must be selected — retailer does not want cutout images (PDF Image mandatory).**

## ⚠️ Common errors / risk items (most valuable)
- **PDF images mandatory** — no cutouts.
- **Linking:** sales banners may have a different link than the products beneath them — tag by matching the SKU. Retailer may email specific links.
- Retailer may note "LINK ENTIRE AD TO WEBSITE" in the linking doc "notes" column for banners — box the banner/lifestyle image accordingly.
- **⚠️ Box QC — combo pages:** if combo pages appear during the Box QC task, **DELETE ALL BOXES & DO NOT DRAW ANY** (pages not cut).

## Post-processing / FQC (owned by Flex)
- **Pre-FQC:** dates per PDF; all items have a URL (fill missing from the linking doc); page names match PZ name (southA → southA pages); toggles (available everywhere); thumbnails include retailer logo (standard 4); all items boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography correct (no stores added/missing).
- **Flyer Review type: Lite:** flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: McMunn & Yates OneGuide (Google Doc `1eFyVghZuOH-e9X8rztLhexNd03sxHtEjwfhqs46ALZo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Meijer — Processing Guide

> **Source:** Meijer OneGuide (Google Doc `1a0dT6vR1xS-lmVgsuA3W4UtsFbIAziCBzc6j9X537Ww`), updated Apr 30, 2026. Contacts/credentials omitted.

> High-complexity, DOC-heavy account with codesheet automation, a Deep Link workflow, and multiple flyer types. See also the Meijer Vendor Guide (Confluence VEN) and "All Things Meijer" working sheet.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium (merchant 2281) |
| Availability | All platforms (**we do NOT power the Meijer hosted**) |
| Slack channels | `#meijer`, `#meijer-scp` |
| Hosted URL | meijer.com/weeklyad.html |
| Flyer types | **Weekly Ad ("One Stop", 542)** · **Pullout (GM)** · **Two-Day Sale (Super Sale)** · **Guides** · **One-Pager (market-specific)** · **Market Format / MeijerDigitalAd** |
| Processing | Auto-stack; Flex N/A; **OS completes coupon processing** (Weekly); no Feedel |
| Tagging document | UPC `.xls` (SKU + Block IDs); Traffic/Placements `.xls` (URLs, Weekly only) |

### Flyer-type quick facts
- **Weekly Ad ("One Stop", `mm/dd`o01):** Avail Fri–Sat, Valid Sun–Sat (2-day preview). **Interstitial inserts** (C1, C2, V1, V2, V3…) are URL link-outs. Page trim 648×864.
- **Pullout (GM):** ad-hoc, ≥1/week, varying duration (dates on PDF), named "X-Pagination" (e.g., Graduation-Pagination). Page trim 648×864.
- **Two-Day Sale:** lives in "Super Sale" flyer type; 2-day sale with 1-day preview.
- **One-Pager (market-specific):** same cadence as Weekly; no page trimming.
- **Market Format / MeijerDigitalAd:** **Flipp only** (we don't power the Meijer hosted); `ALL_SALE_MeijerDigitalAd` is the only publication that does **not** need a linking document.

## Files & schedule (Weekly Ad)
- **Files received:** Tuesday. **Cadence:** Available From Tuesday → Available To Tuesday; Valid From Wednesday → Valid To Tuesday. Preview date Thursday before go-live. Linking document: Yes (Main Weekly only).
- **Pullout:** files Wednesday; Available Fri → Sat, Valid Sun → Sat (varying); preview Thursday.

## Upload & setup (owned by DOC)
- Confirm receipt by email; files in FTP. In the FTP, mark off all `csv` and `UPCGroceryServer` (search "grocery") files as uploaded; search "pagination" to identify unique flyer runs.
  - **⚠️ Repeat-week detection:** if a pagination folder ends in `_Wk2/_Wk3` etc. **and** the file's date does **not** match the highest-level folder date, it is a repeat from a prior week — **do not upload** (search the full basepath and mark all files uploaded). If the pagination file date **matches** the top folder date, it is new (upload).
- Organize files locally (copy template folder, rename to the week; subfolders for Pullouts, Pagination Docs, UPC Docs). **Combine all Weekly UPCs into a Master UPC** for OS tagging.
- **All Things Meijer sheet:** add a new row in the **[Deep Link Working Sheet]** tab for the week (dates, names, Flyer Run ID) — sets up sending Deep Links within ~24h. Create flyer shells and rows for each Pullout.
- **Weekly Google Doc (for the Optics ticket):** use the working template — **[Traffic]** (interstitial URLs → download XLS, attach to all tasks), **[Pagination]** (regular page order), **[Codesheet]** (page list built from pagination docs), **[Revisions]** (page swaps). Attach to the OPTICS ticket for the lead. A Colab automation notebook exists for codesheet creation.
- **Run codesheet:** Config **`meijer`**; **standard toggles (1,3,4,5,6)**; base path one level only (e.g., `/0330_Flipp5/`). Weekly only — after codesheet finishes, **manually upload interstitial pages (track 2)** (C1A, C1B, C2A, V1A, V2A, …).
- **Trim Boxes (after page tile gen, before flyer creation):** apply to **[All Pages] → Assign to All Pages** to kick off Tile Gen/sessions (QA before completing flyer creation so the system doesn't start Auto Box Draw). Dimensions: **Left 0, Bottom 0, Right 648, Top 708** (Weekly, Pullouts, Interstitials). Single stuck pages → nudge boxes 1 pixel.
- **[Traffic]:** from Hailey's "MM.DD Flipp Placements & Links" email — copy PDF name, Placement name, URL into the Traffic tab, download as XLS for OS. (No Pullout info — Pullouts don't get product links.)
- **Inserts:** interstitial pages inserted in **alphanumeric order at the end of all versions** (version "A" before "B").
- **Attachments:** attach the date-URLs XLS + Master UPC to **all tasks, all tracks** (mass-attach from Flyer Creation).
- **Overview:** Standard 4 thumbnails; **preview date = Thursday before go-live**; **external run name = "Weekly ad"** (Pullout = "Callout on page 1", all lowercase); no theme.
- **Setup QC:** standard; **clear stale (no pages remaining)**.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item with a price/sales story; box any product block with a "Shop Now" callout.
- **Tag / Tag QC (Medium; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price.
  - **SKU:** from the UPC XLS **column A** ("UPC") — applied to **track 1** pages (majority).
  - **Block ID:** from the UPC XLS **column M** — applied to track 1 pages (connects the item to the Meijer database — **high priority**).
  - **URLs:** from the Placements/Links XLS — applied **only to track 2** pages (C1, C2, V1, V2…).
  - Linking doc required for Tag/QC (except the `ALL_SALE_MeijerDigitalAd` publication).
  - **Sale Story order matters:** e.g., "BOGO 40% off of equal or lesser value" (not "…of equal or lesser value 40% off"); set Percent Off field.
  - **Images:** single-item block → clean PDF if available; **multi-item block → cutout**; lifestyle images → cutout. Avoid black/gray backgrounds.
- **Spotchecks:** standard pricing spotchecks in pipeline.

## ⚠️ Common errors / risk items
- **Tagging example — AirPods:** do **not** tag price as "3 for $249"; tag Name = Apple AirPods Pro 3, Price = $249.
- **Do not miss a UPC document** when building the Master UPC (would require re-running OS tag).
- **Repeat-week pagination files** (`_Wk2` etc. with a past date) must not be uploaded.
- **Trim boxes** must be applied to **all tracks** before flyer creation, or Auto Box Draw kicks off incorrectly.
- **Page swaps** from the retailer (Kurt) come in through the week — track them but **do not action until after SKU, Block ID, and Offer ID checks**.

## Post-processing / Pre-FQC (owned by DOC)
- **Page reduction** steps for the Weekly (from the Page Reduction email/document; note the affected store set).
- **Add interstitial inserts** (if not done at upload); QA URLs against the Traffic tab (check the URL ending terms).
- **Item searches (using the Master UPC):**
  - **SKU** IS blank / CONTAINS `+` (Item) → copy SKU from Master UPC column A (item-specific deep links, lower priority).
  - **Block ID** IS blank (Item) → copy Block ID from column M (**high priority**).
  - **Offer ID** IS NOT blank (Item) → check if an Offer ID is applicable; remove if not.
- **Offer ID Import (NEW 5/23, Weekly Ad):** pull an item report (after Block IDs fixed), use the OfferID Importer sheet (import Item Report + Master UPC as tabs, run Macros 1–3, remove blank/N/A id_2 rows, download ITEM IMPORT as CSV, run Item Import). GM Pullout uses a manual Offer ID process (filter Offer ID column, add via item search by SKU).
- **Page swaps:** execute the **[Revisions]** tab before go-live.
- **Tracking URLs:** promoted content (currently all ads) uses DoubleClick impression/open URLs (same WOW — no changes needed).
- **Preview links:** send no earlier than **3:30 PM Thursday**; copy the Hosted 2.0 URL into the Deep Link Working Sheet.
- **Flyer sorting:** **Flyer Type Oldest First** (old weekly, new weekly, pullouts, other) — periodically QA it hasn't reset.
- Update the **OPTICS** ticket for the lead (attach the weekly sheet).

## FQC / flyer review
- **FQC checklist** completed by DOC.
- **Flyer Review type: Medium** — Weekly owned by Vendor; Pullout owned by DOL (see the Meijer flyer review guides).

---
*Source: Meijer OneGuide (Google Doc `1a0dT6vR1xS-lmVgsuA3W4UtsFbIAziCBzc6j9X537Ww`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Menards — Processing Guide

> **Source:** Menards OneGuide (Google Doc `1aqf7DDM3TFmEHMxH76QpxpsgLf5a3u-msXOU0e1F-4c`), updated Jan 20, 2026. Contacts/credentials omitted.
>
> **Jan 20, 2026 change:** When tagging URLs, no longer "click through" search pages to the product page — **linking to just the search page is now preferred**, even for single-SKU item blocks.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel | `#menards` |
| Hosted URL | menards.com/main/flyerselectstore.html |
| Publication cadence | See the Flipp Flyer Schedule |
| Processing | Auto-stack |
| Who's involved | **Flex — N/A (not involved)**; OS completes standard tasks |
| Box Draw complexity | **High** (spreadsheets required — Header & Burst document) |
| Tagging complexity | **High** (spreadsheets required) |

## Files & schedule

- **Files usually arrive Wednesday, two weeks before go-live.** Upload can be done Wed–Fri, earlier is better.
- Usually 2 publications ("CUE" and "A"), occasionally 1–2 more.
- **Two codesheets:**
  - **Daybreak** — for staggered dates. Uploaded **but NOT run.**
  - **Pagination** — for page layout. This one **is run.**
- **We FQC very early** — it's a contingency to send Menards their retailer preview, which they expect the **Wednesday before go-live.**

## Upload & setup

**Daybreak sheet.** From FADMIN SFTP, download the "daybreak" file, import to Sheets. Filter the flyer and use the Column D dropdown: if a date there is before the run's Available/Valid From in FADMIN, alter run settings to match the earliest day (this sheet generates staggered dates and the upload **fails** if a listed available/valid-to is earlier than the FADMIN flyer's). Export CSV.

**Pagination sheet.** Download from SFTP, import to Sheets:
- Find store "O'Fallon" → remove the apostrophe ("OFallon").
- On any row-1 cell ending in "-1" or "-2" that has no "DG" page identifier below it, prefix the cell with "OX" (e.g. "OXPage 9.1").
- If there is a page 1.1, delete it and re-upload manually later (the codesheet processor pulls it as page 1 by accident).
- Download as CSV.

**Codesheets in FADMIN.**
- Upload the **daybreak** page. Base Directory from SFTP (no trailing space or slash; the second half of the path is unique per run — A vs CUE). **DO NOT RUN this codesheet.**
- Upload the **pagination** page and run **only** it. It **always runs yellow (processed with warnings) the first time** — this is a false error introduced by CLSD to slow the process and prevent a recurring glitch; **no action needed.** Then **Force Process** the pagination codesheet.

**After codesheets.**
- If you removed a page 1.1 (step above), re-upload it manually into position 2.
- Download the **"Header and Burst" (linking) XLS** from SFTP and attach to all vendor tasks.
- Input External Run Name and Key Messages from the 2nd half of the internal run name (e.g. "Home Essentials").
- Set preview date to Wednesday before go-live.

**Setup QC.** After upload you'll usually have pages named `KEY.pdf` — these are instructional for insert tagging and are **not** uploaded.
1. Spot-check zones: flyer dates on PDFs match **Pricing-Zone-level** FADMIN dates.
2. Pages → Categories: no serious graphical issues.
3. Pricing zones and geo look right (~70–80 zones; FSAs may shift with boundary changes but no major changes).
4. Confirm a handful of zones end in **-2** — the system splits a PZ in two when stores share pagination but have different launch dates. **If none appear, the split process may not have run (rare).**
5. Mark Setup QC complete.

## ⚠️ Common errors / risk items

- **Rebate wording** — many items are "Final Price FREE After $$ Mail-In Rebate" / "each PRICE AFTER REBATE." Use the matching **postfix**; the "after $$ mail-in rebate" phrase always comes **last** in the postfix. If there's no exact-amount matching postfix, use "each PRICE after $$$ Mail-in Rebate*." Do **not** flag these as errors.
- **Multi-version lumber/decking/insulation pages** — pages look identical but prices vary by version. Ensure prices match the exact page; **never copy prices across pages/items**; report if you see copied prices.
- **Box every item with a separate SKU or price SEPARATELY.**
- **Never tag an item using an adjacent item's price** when one isn't present, unless there's a specific callout ("OR", "YOUR CHOICE"). Leave Current Price blank otherwise.
- **Plants not searchable on the site** → link to the garden center (`menards.com/main/garden-center/c-9985.htm`).
- **SKU spaces** — when copying/pasting SKUs, override existing spaces using the keyboard spacebar.
- **Page-link error** — if entering a page number throws "Page destination should be a valid page…", simply enter **1** as the destination.
- **Live-dates / PT notes:** URLs edited by the PC (check "Whodunnit") are usually correct/ad-hoc — don't remove; mark live date false, source = retailer request. SKUs that don't match the flyer pages are per retailer request — don't change (breaks data piping). Some items are intentionally non-clickable — flag to processor before actioning. Post-fix "each" used when there's no matching amount — not an error.

## QC specifics

### Box Draw — High complexity
- **Include:** social media, coupons, sign-up page, special weblinks, retailer logo. **Exclude:** packaged deals.
- **Rule 1 — box all items with a SKU;** each SKU in a product item gets a box; a box with >1 SKU must not have multiple prices (if multiple prices, one box per SKU/item).
- **Rule 2 (May 2025):** box the item, title, and description of "YOUR CHOICE" items as individual boxes; do **not** add a text box to the "YOUR CHOICE" callout/adjacent pricing.
- **Rule 5 (May 2025):** **do NOT box item disclaimers** in a text box (retailer no longer wants disclaimers captured).
- **Sale banners get boxed;** non-sale banners ("Chance to win a car," "Delivery to Canada," "Sales Disclaimers") do **not**, unless in the URL document.
- **Social-media icons** (page footer) boxed & tagged as Direct Links (Pinterest `pinterest.com/menards/`, Instagram `instagram.com/menardshomeimprovement/`, YouTube `youtube.com/user/Menards`, Mobile App `menards.com/main/services/menards-mobile-app/c-13988.htm`).
- **Headers & Bursts** boxed only if specified in the shared Header/Burst doc (all direct links, not item links) — must be consistent on all pages/versions.
- **Rebate disclaimers** — ensure ALL are boxed and tagged as **Page Links** leading to the correct page.

### Tag / Tag QC — High complexity
- **Include:** name, pre/postfix, sale story, disclaimer, original price, categories, images. **Exclude:** brand (put brand in the Brand field, not Name), description. **Risk items:** SKU, price, valid dates, dollars/percent off, URLs.
- **Name order (always):** (Brand) (Model-Name) (Size) (Title of Product) (Sub Heading/Category) — e.g. "Hunter 52\" Fremont Ceiling Fan." Sales banners: enter as it appears in the headline.
- **SKU formats:** Single (`111-1111`); Multiple-range (shared SKU group, e.g. `111-1123-1125`); Combination (multiple families, e.g. `111-1123-1124-1125, 555-6780`). Model numbers entered as shown, without the `#`.
- **Price/prefix/postfix:** prefix = anything before the price, postfix = anything after. Never use "FINAL SALE" as a prefix — always postfix. Do not enter dollars-off / original-price for rebate items. BOGO handled with prefix + current price + postfix. Each item in a chart/group needs its own prefix & postfix.
- **Disclaimers** entered in order: Unique item → Page → Rebate. Rebate disclaimer (only when "Mail-in Rebate *" with an asterisk): `*Mail-in Rebate. Rebate is in form of merchandise credit check. Valid in-store only. Merchandise credit check is not valid towards purchases made on MENARDS.COM®`. **Do NOT duplicate phrases.** Include item disclaimers; do not include page disclaimers.
- **Item categories:** every page needs ≥1 category based on the majority of items; **keep page-level categories identical across all versions of the same page;** first and last pages get **no** category. Mail-in-rebate items also get the **Rebate** analytic category. (A full category chart is in the OneGuide.)
- **Item URLs:** if a SKU has a URL in the linking document, use it; else fetch → visit → copy the site URL. **Retailer does not want generated search URLs.** Remove any `?tid=` from URLs; trim anything after `.htm`. Multi-range SKUs (>9) can't be searched on-site — use the Menards URL Database.
- **Valid dates override:** don't enter unless for 6-Hour Savings items in the Black Friday Sale.
- **Email signup pages** → link to `menards.com/main/preference-center.html`.

## Pre-final QC tasks

1. Finalize pre-live page swaps; add pages not in codesheet.
2. Spot checks.
3. **Inserts** — ops boxes/tags in-house; each has a "link" XLS and a "key" PDF in SFTP (Key PDF = boxing template; link XLS = linking instructions).
4. Ensure ALL rebate disclaimers boxed/tagged as Page Links to the correct page.
5. Thumbnails: rectangles 2 pages, squares 1 page.
6. Re-run data piping.
7. Download the previous week's email insert, upload to the run, copy boxes from last week, insert into the **dead-last** position of all zones.
8. **Tracking codes:** Dynamic Variable, Source=Hosted, Variable=`utm_campaign`, Value=`[FLYER CODE]-[YEAR]` (e.g. 20CUE-2024); and Variable=`utm_content`, Value=external name with hyphens (e.g. home-essentials). Apply all tracking codes.
9. Data piping: link-only misses are fine. For "Item" display-type boxes failing data piping, if the SKU ends in a numerical range >220, reduce the difference between the last two numbers to <220 and re-pipe (may still fail — no further action).
10. Rerun any page whose bottom text is crossed out as **ghostscript**.
11. "See Page _" disclaimers boxed/tagged as page links to the full-disclaimer page.
12. **Flyer sorting:** newest 11% Ad → newest Appliances ad → current 11% Ad → current Appliances ad → catalogs newest→oldest.
13. Add a trigger to rerun data piping at 11:30 pm the night before go-live.
14. Final QC checklist.

## Preview QC (PQC)

- **Category QC:** change Google categories "beer"/"wine"/"seafood" → "building material."
- **SKU blank:** Item Search SKU is blank, type Item → open all and tag with the SKU on the PDF.
- **Items without URL** should be zero (Overview → Information/Reports → Items Without URL).
- Manually click through: single SKUs must NOT be search URLs; multi-SKUs must contain the full SKU range with no `-`.
- Search for URLs containing `-` or "search" and remove the `-` from the SKU in the URL.

## Out of process

- Preview send (Wednesday before go-live).

---
*Source: Menards OneGuide (Google Doc `1aqf7DDM3TFmEHMxH76QpxpsgLf5a3u-msXOU0e1F-4c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Metro Ontario — Processing Guide

> **Source:** Metro Ontario OneGuide (Google Doc `1gwpKzf-Vko1XcRlFZwfsXMshenK1zXZHuGBSWZCGtIo`), last updated Jul 14, 2026. Contacts/credentials omitted.
>
> For French tasks/pages, see the Metro Quebec OneGuide instead.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** (relationship quality: Excellent) |
| Availability | All platforms. **We don't power their hosted, but leave all toggles unchecked.** |
| Slack channels | `#metro`, `#opsmetro`, `#metro-reporting`, `#3fl-metro` |
| Hosted URL | metro.ca/en/flyer (hosted powered by TC) |
| Flyer types | **506: Ontario** (weekly) · **9290: Digital** (vendor ads — P&G, brand-specific — + standard secondary pubs) · Quebec types 5844 / 12207 handled in the QC OneGuide |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (flyer processing only); no coupons; **Strategic Ops — yes (Feedel / retailer data services)** |

> **NOTE:** For any secondary publications, flag the flyer run and dates in `#metro` tagging BD members — they use this to add budget behind the flyers.

## Files & schedule (Ontario 506)

- **Files received:** Friday.
- **Publication cadence:** Available From Wednesday; Valid From Thursday; Available To / Valid To Wednesday (EST).
- **Preview date:** Internal preview only, from Monday.
- **Weekly workflow:** Thursday — codesheet manipulations & upload (DOC); Friday — digital inserts & REV pages (upload 2); Monday — SKU QC (Flex, requires Flex ticket); Tuesday — FQC + SKU custom action (DOC); Wednesday — flyer live; Thursday — Store Manager Specials page upload/processing; Friday (+ Sat & Mon) — Store Manager Specials live check.

## Upload & setup — Standard weekly (owned by DOC)

**Codesheet manipulations.** Required assets: PDFs (standard pages + digital inserts), Digital Codes spreadsheet, the Automatic Codesheet (shows versions, stores per version, page order — inserts not included), and the Store Matrix (store locations × insert distributions).
- Client sends the Digital Codes codesheet; selected data is copy/pasted into the Automatic Codesheet.
- Metro occasionally sends a Store Matrix listing which stores get which inserts. Paste into the Automatic Codesheet ("Flyer Zones_Matrix as of…"). The `1`s under each Insert Code column must be replaced with that column's title (e.g. under `ATT_DEL`, replace each `1` with `DEL`), because those distinctions drive the automated codesheet.

**Upload.**
- **Part 1 — Codesheet:** once manipulated, download as CSV. Upload on the Codesheet tab with **Config: `metro`**, Base path = base folder up to the date only (nothing after the date, so all folders for that date are referenced). The codesheet creates pricing zones by insert and auto-creates English + French versions. Bilingual zones show as French; all others get `FR` in the name and toggle as **cross language**.
- **Part 2 — Digital inserts manual upload:** Pages tab → Edit → folder with matching date + "Digital Inserts." Select all pages **except** secondary-pub pages and pages with **"visible"** in the name (those carry Block-IDs/SKUs layered on top — not wanted). Re-upload inserts needed for bilingual PZs; set correct language toggles; Save & Complete.

**Setup.**
- Search Pages for names with "Block" — only inserts labelled "Block ID - Layered" should appear. If a regular page (e.g. 02_DM/DM2) has "Block ID," it's the wrong page (SKUs visible on top of items) and must be replaced.
- Mark Flyer Creation complete. Confirm EST dates (Avail Wed–Wed, Valid Thu–Wed) match the PDF, especially secondary pubs. Internal preview: Monday before go-live. Toggles: available everywhere. No external run name, no theme. Set vendor tasks to HIGH priority. Complete Setup QC.

## Upload & setup — Secondary publications (owned by DOC)

- Secondary-pub info is at the bottom of the codesheet email, or in the codesheet below all versions (first/second chart).
- Manual upload: select pages for that publication with **"layered"** in the PDF name (only 1 version needed); index by page number; ensure English; Save & Complete.
- Pricing zones: Zone 1 = Base (English); Zone 2 = Base CL (English + cross-language toggle — changed to French during FQC in case of REV pages).
- Setup: Avail/Valid Thu–Wed; preview Monday. External Run Name = main callout on page 1, added to **both EN & FR** fields.

## ⚠️ Common errors / risk items

- **SKUs / Block-IDs** are found in text extractions or on the BLOCKID FTP file — **not on the flyer page.**
- **Incorrect valid dates** on the red banner at the bottom of page 2 are caused by the print flyer's flap — **this is NOT an error.** If unsure, flag it.
- **Wrong image** — many similar products per page look alike but differ in name/quantity. Be careful selecting images; select the image of the **first product** in a list.

## QC specifics

### Box Draw / Box QC — **High complexity** (owned by Vendor)
- **Auto-Box Draw: OFF. Box QC bot: OFF.** No linking document.
- **Include:** coupons, packaged deals.
- **Exclude:** retailer logo, sign-up page, social media, special weblinks.
- **Box each item separately, including inside multi-item boxes**, using text boxes. If a text box would cover an item, that's fine. **Capture the whole product image in the box so text extraction works.**

### Tag / Tag QC — Low complexity (owned by Vendor)
- **Auto-tag: ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Multi-item boxes:** tag using all text in the same box — Name = bold text, Description = non-bold, Price = XL number, Pre/Postfix = small text with price. **SKU = text-extracted** (not always on the same line; e.g. `VF-09`, `FL872-03`, `P-03`, `31-018EL`). **Do NOT tag URL** (tagged automatically later).

### Image QC
- Clean PDF preferred; otherwise a cutout is fine.

## Post-processing (owned by DOC)

- **Insert process** — reference the insert-process videos; complete before marking autostack spotcheck complete.
- **SKU spotcheck / SKU QC** — Item Search for items without a SKU; SKU is an alpha-numeric code with a dash (e.g. `GM07-F01`) found in Text Extraction. If few, add manually; if many, file a Flex/FAB ticket. Then run the custom action **"Set Metro Banners Item URLs"** (Flyer Run ID + Merchant ID + ZDMP filename from SFTP `/ZPO400 + Google Feeds`; use the **CV** file for Ontario). QC via Item Search (SKU is-not-blank; URL is-blank vs is-not-blank).
- **FSA Override** — 3 FSAs are manually added. After FR/CL zones go French, rerun FSA Generation if overlapping (red). On Geography, remove all Quebec FSAs starting with **J** (e.g. J8T, J8V, J9A…) via custom action "Remove FSAs" (FSAs + Flyer Run ID; ignore Pricing Zone ID). Export FSAs, edit in Sheets (delete "Pricing Zone Name"; rename "Pricing Zone ID"→`flyer_id`, "FSA"→`fsa`), find the two flyer IDs containing **L3Y** and add rows for **L0E, L4P, L9P** to each. Download CSV, use "Assign FSAs by CSV." **If new pages are uploaded, re-run this custom action every time.**
- **Page merging** — Storefront Spotcheck one PZ per version; merge skinny pages (positions 1 & 3) to the next page, then rerun Page Tile Gen.
- **Tracking codes** — Overview → Manage Tracking Codes → Apply All Tracking Codes (set at Flyer Type level).

## Flyer review / go-live

- **Flyer Review type: Medium** (owned by DOL).
- **Ontario checks:** thumbnails Standard 4; check notes for errors/warnings; flag items without URL if >10% missing and no note; live 1d prior to valid; available everywhere; pages with 0 tagged items OK only if banner/insert; items-vs-tagged totals equal; interactivity in Item/Horizontal/Vertical preview with no cutoff in vertical scroll; codesheet green; Geography no change WoW; ensure FSAs **L0E, L9P, L4P** assigned.
- **Quebec flyer:** same as ON except live **2d** prior to valid.

---
*Source: Metro Ontario OneGuide (Google Doc `1gwpKzf-Vko1XcRlFZwfsXMshenK1zXZHuGBSWZCGtIo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Metro Quebec — Processing Guide

> **Source:** Metro Quebec OneGuide (Google Doc `1ltuZePeprRCWDNW_k17hMqJVea8E_J4HQCooMC16KBw`), last updated Sep 6, 2024. Contacts/credentials omitted.
>
> If you are working on English tasks/pages, use the Metro Ontario OneGuide instead. (This guide contains both Ontario 506 and Quebec 5844 instructions.)

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** (relationship quality: Excellent) |
| Availability | All platforms. **We don't power their hosted, but leave all toggles unchecked.** |
| Slack channels | `#metro`, `#opsmetro`, `#metro-reporting`, `#3fl-metro` |
| Hosted URL | metro.ca/en/flyer (hosted powered by TC) |
| Flyer types | **506: Ontario** (weekly + standard secondary pubs) · **9290: Digital** (vendor/brand ads) · **7988: Metro Health** (ad hoc) · **5844: Quebec** (weeklies & secondary pubs) |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (flyer processing only); no coupons; **Strategic Ops — yes (Feedel / retailer data services)** |

## ⚠️ Common errors / risk items

- **SKUs / Block-IDs** are found in text extractions or on the BLOCKID FTP file — **not on the flyer page.**
- **Incorrect valid dates** on the red banner at the bottom of page 2 come from the print flyer's flap — **NOT an error.** Flag if unsure.
- **Wrong image** — similar products per page look alike but differ in name/quantity. Select the image of the **first product** in a list.

## Quebec (5844) — files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Tuesday; Valid From Thursday; Available To / Valid To Wednesday (EST).
- **Preview date:** From Monday (preview links aren't sent to the client — they access via Madmin).
- **Workflow:** Wednesday — store-list codesheet & page upload (DOC); Monday — SKU QC (Flex), FQC + SKU custom action (DOC); Tuesday — revisions (DOC).

## Quebec (5844) — upload & setup (owned by DOC)

**Pre-processing / codesheet.** Required assets: Store List (by email), Tracking sheet (by SFTP).
- They send two copies of pages: normal, and ones with the SKU/Block-ID layered on top ("visible"). In SFTP search "blockid"/"block-id"; mark folders labelled "Block ID" as uploaded. This search also catches INSERT pages (dropped in a "block ID" folder) — mark all off, then Ctrl-F "layered" to unmark the insert pages you'll upload ("visible" pages show the SKU).

**Upload.**
- Search "BLOCK" pages in FTP, mark uploaded (not needed for processing — legacy).
- Download the Store Assignment sheet; double-check its versions match the Tracking Sheet (pagination doc). Import to Sheets: unhide and delete unneeded version columns (highlight the ones you need first).
- **Store ID overrides (Site Number column):** **Lachine = 5398**, **Prevost = 5427**.
- Save as CSV, then re-open to confirm no extra/duplicated columns (can create extra PZs).
- **Upload as Codesheet: Config `metro_qc_stores`, PDF Base `/`, toggle store assignment + pricing-zone-creation only.** After upload, check the Pricing Zone tab for extra store-less PZs (system sometimes creates combined zones like "NAT ECO" with no stores — delete them).
- Manually add stores **14** and **387** to the Nat & Nat CL zone store assignments.
- Find the "REV" folder (ignore Block ID). Download / match pages per the Tracking Sheet (page labels may differ slightly, e.g. `-` vs `_`, "Web_01" vs "Web1"; "venir" = French "to come" = sent later). Upload INTER pages (separate folder, labelled with valid date). Update grouping manually (FAdmin can't group these). **Change page language to French**, Save, then Save As, and re-verify all pages are French.
- In Pricing Zones, update pagination per Tracking Sheet (per-zone page differences highlighted red; INTER pages go in position 1 for noted zones).

**Setup.** EST dates: Avail Tue, Avail To Wed, Valid Thu–Wed. Toggles available everywhere; no external run name; no theme; vendor tasks HIGH priority.

## Ontario (506) — upload & setup (owned by DOC)

- **Codesheet:** manipulate the Automatic Codesheet from the client's Digital Codes sheet; download CSV; upload with **Config `metro`**, Base path = base folder up to the date only. Creates EN + FR PZs; bilingual zones show French, others get `FR` + cross-language toggle.
- **Digital inserts:** manual upload from the date + "Digital Inserts" folder; skip secondary-pub pages and "visible" pages; re-upload inserts for bilingual PZs; set language toggles; Save & Complete.
- **Setup:** mark Flyer Creation complete; EST dates Avail Thu, Avail To Wed, Valid Thu–Wed; preview Monday; toggles everywhere; no external run name/theme; vendor tasks HIGH; Setup QC.
- **Secondary pubs:** manual upload of "layered" pages (1 version), index, English, Save & Complete. Zones: Base (EN) + Base CL (EN + cross-language, → French at FQC). External Run Name = main callout on page 1 in **both EN & FR**.

## QC specifics

### Box Draw / Box QC — Low complexity (owned by Vendor)
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required (Box Draw/Box QC specific).
- **Include:** coupons, packaged deals, retailer logo, sign-up page, special weblinks. **Exclude:** social media.
- Box each product block that includes a price; **if multiple items share the same price, group and box them as a single box.**

### Tag / Tag QC — Low complexity (owned by Vendor)
- **Auto-tag: ON.** Linking document required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Name = bold; Description = non-bold; Price = XL number; Pre/Postfix = small text with price. **SKU = text-extracted** (e.g. `VF-09`, `FL872-03`); **do NOT tag URL** (auto later). Tag coupon offers.
- **Original price:** single price → Original Price field; a **range** → Description field.

### Image QC
- Clean PDF preferred; cutout is fine otherwise.

## Post-processing (owned by DOC)

- **SKU QC** — Item Search for items without a SKU; add manually from Text Extraction or file a Flex/FAB ticket. Then run custom action **"Set Metro Banners Item URLs"** (Flyer Run ID + Merchant ID + ZDMP filename from SFTP `/ZPO400 + Google Feeds`; use the **QC** file for Quebec). QC via Item Search.
- **FSA Override** — after FR/CL zones go French, rerun FSA Generation if overlapping. On Geography, remove all Ontario FSAs starting with **K** via custom action "Remove FSAs" (FSAs + Flyer Run ID). Confirm on Geography tab.
- **Tracking codes** — Overview → Manage Tracking Codes at flyer-run level (Dynamic Variable, Hosted, utm_source) → Apply All Tracking Codes; changes per platform/clone.
- **FQC** — normal FQC checklist.

## Flyer review

- **Flyer Review type: Medium** (owned by DOL).
- **Ontario:** Avail Wed–Wed, Valid Thu–Wed; thumbnails Standard 4; flag items without URL if >30% missing; pages with 0 tagged items OK only if banner/insert; codesheet 1× green; Geography no change WoW; ensure FSAs **L0E, L9P, L4P** assigned.
- **Quebec:** as ON except Avail Tue–Wed; flag items without URL if >50% missing.
- **Digital flyer type:** external run name required (custom, EN & FR); items have no URLs; geography may be inconsistent.

---
*Source: Metro Quebec OneGuide (Google Doc `1ltuZePeprRCWDNW_k17hMqJVea8E_J4HQCooMC16KBw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Metropolitan Market — Processing Guide

> **Source:** Metropolitan Market OneGuide (Google Doc `16KBC7H_yetLeXMpn9iTHIQ0h-wou0_60ODBF53VLgYE`), last updated Feb 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | (not specified in guide) |
| Hosted URL | metropolitan-market.com/weekly-grocery-ads-coupons/ |
| Flyer types & cadence | Flyer Type 9672 — **Bi-Weekly** · Flyer Type 2 — Monthly |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); no coupons; **Strategic Ops — yes (retailer data services / Feedel processing)** |

## Files & schedule (Flyer Type #1)

- **Files received:** Tuesday.
- **Publication cadence:** Available From / Valid From = Wednesday; Available To / Valid To = Tuesday.
- **Processing type:** Auto-stack; available on all platforms.
- **Scrummaster note:** Occasionally files arrive by email rather than SFTP. If sent by email, transfer to SFTP using the standard transfer procedure.

## Upload & setup (owned by Vendor)

- Manual upload.
- Autogroup pages.
- **One PZ (Base).**
- **Add all stores (9).**
- Then complete the Setup QC checklist.

## ⚠️ Common errors / risk items

- **Brand name tagged only once** — the brand name of an item should appear only in the Name **or** the Brand field, not both (e.g. "Taylor Farms" goes in Name, not also Brand).
- **Order of Sale Story** — percentage (%) comes *before* the dollar amount the customer saves ($).
- **Item images** — all images should be the PDF and must reflect in the flyer preview. Always double-check; if they aren't reflecting, re-run page stitching, then wait 15–20 minutes before re-checking.

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required (Box Draw/Box QC specific).
- **Include:** retailer logo, sign-up page, social media, special weblinks.
- **Exclude:** coupons, packaged deals (e.g. washers/dryers).
- Avoid overlapping boxes — correct any overlap. The store locations at the bottom do not need to be boxed or tagged.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** Linking document required (Tag/QC specific).
- **Include Name; do NOT include Brand.** Include price/original price, valid dates (if applicable), description, sale story, categories, disclaimer, pre/postfix.
- SKU: N/A.

### Image QC
- **PDF mandatory — retailer does not want cutout images.** Exception only if the PDF is awful/damaged.

## Final QC checklist (owned by Vendor)

1. 4 standard thumbnails (2,1,2,1).
2. Set "no theme."
3. Item image QC → select all available PDFs (click "generate data piping groups" if nothing shows).
4. Any box with two distinct items should have the main item in both Name and Description; confirm no boxes overlap.
5. Check previews + sessions.
6. Complete FQC checklist.
7. On the MM merchant page, put the flyer run ahead of the booklet (under Flyer Sorting).

## Flyer review / out-of-processing

- **Flyer Review type: Lite** (owned by Flex).
- **Out-of-processing:** MM rarely has page swaps; standard page-swap procedure applies when they occur.

---
*Source: Metropolitan Market OneGuide (Google Doc `16KBC7H_yetLeXMpn9iTHIQ0h-wou0_60ODBF53VLgYE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Meubles RD — Processing Guide

> **Source:** Meubles RD OneGuide (Google Doc `1HUqZRg1jTOCrDSGEafR40fjgtU4kAqOMzC3CZb5lm40`), last updated Jul 14, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channel | `#meublesrd` |
| Flyer types & cadence | Flyer Type 1 — Weekly (1-week run) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review + Upload/Setup); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Language | Bilingual — English & French pages/PZs |

## Files & schedule

- **Files received:** Wednesday.
- **Publication cadence:** Available From / Valid From = Monday; Available To / Valid To = Sunday (1-week run).
- **Preview date:** Friday before live (flyers usually go live Mondays; preview Friday ensures FQC is ready).
- **Linking document:** Yes — **separate EN and FR URL link sheets.**

## Upload & setup (owned by Flex)

**Manual upload (EN & FR).** Pages > Edit > find the folder in the FTP.
- Select all **French** pages > change Language to French > Save.
- Select all **English** pages > Auto Group > Save & Complete.
- **Flyer Creation > Start Tasks. Two pricing zones: English & French. Add all stores to both PZs.**

**Link sheet manipulations** (download both EN & FR from the FTP): move the Item Name column (D) to C so the order reads TYPE (A), PAGE (B), NAME (C), URL FLIPP (D); save as Excel; **attach EN file to EN vendor tasks only, FR file to FR vendor tasks only** (remove the opposite language to avoid confusion).

**Setup (Overview > Edit Details):** dates Mon–Sun; available everywhere; preview Friday; Internal Run Name = date; External Run Name EN & FR copied from the Pub Doc; No Theme (unless Holiday/Black Friday/Boxing Day).

## ⚠️ Common errors / risk items

- **Page swaps mid-run** — the retailer often wants pages swapped out partway through the run. **Pay close attention to page numbers;** when auto-grouping, manually change the page to match the page number. If multiple pages exist, the page name includes the dates — use it to decide which page comes first; if unclear, flag to DOC/DOL.
- **URL spreadsheet language** — always attach the EN linking doc to EN tasks and the FR linking doc to FR tasks; double-check they match.
- **Page swaps & triggers** are completed during FQC.

**Triggers (rare).** To trigger a page in/out on set dates: Layout → Put In page → set position → All Flyers → OK (repeat for the French page) → Run as Trigger → set date/time. Removal: Layout → Take Out page → All Flyers → Run as Trigger → set removal date/time. Then create an **OPTICS ticket** (Merchant Request Type: Triggers), move it to the Lead Review lane assigned to the Lead, who schedules the insertion/removal live checks.

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required.
- **Exclude:** coupons, retailer logo, sign-up page, social media. Packaged deals — box items individually. **Special weblinks — include only as indicated on the Link Sheet.**

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF. PDF image auto-selection: ON.** Linking document required.
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates.
- If the product name or description is in the linking document, paste it to the item.

### Image QC
- Use clean PDF images when available; avoid PDFs with black backgrounds or unclear images; lifestyle PDF images are OK.

## Final QC checklist (owned by Flex)

- Confirm vendor tasks complete. Use the **Publication Schedule** (search "schedule" in the Meubles RD FTP) to confirm flyer dates and External Run Name.
- Dates Mon–Sun, available everywhere, preview Friday, no theme.
- **Thumbnail QC — Standard 4:** 1065×600 (2 pg), Stock premium (1 pg), Storefront carousel premium (2 pg), Storefront carousel organic (1 pg).
- Pages: Tag/Tag QC both green; **no page category on page 1** (clear any); up to 4 max categories on remaining pages.
- Sessions run, FSAs generated, re-verify URLs (Overview > Items without URL → add missing per URL docs).
- Geography: no FSAs/stores added.
- Item Image QC: unselect Composites, PDFs, Data Piped; leave groupings as cutout; single item with a clear PDF → use the PDF image. Legibility heights 40/30.

## Flyer review / out-of-processing

- **Flyer Review type: Medium** (owned by Flex).
- **Out-of-processing:** page swaps, triggers, custom tiles, deep links. **Custom Tiles: NO LONGER DONE.**

---
*Source: Meubles RD OneGuide (Google Doc `1HUqZRg1jTOCrDSGEafR40fjgtU4kAqOMzC3CZb5lm40`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mi Tienda — Processing Guide

> **Source:** Mi Tienda OneGuide (Google Doc `1_sNFGRomRguvJ1IX_DRFC06xRWLpBxhOmD-f7DBAEME`), last updated May 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channel | `#heb` |
| Hosted URL | mitiendatx.com/weekly-ad-1630-spencer-hwy.php |
| Flyer types & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Language | Primarily **Spanish** |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available From Tuesday; Valid From Wednesday; Valid To Tuesday.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages tab → Edit → select all pages from SFTP (typically two pages) → Confirm & Upload → Auto-Group or manually enter grouping numbers; ensure all pages English → Save & Confirm. **Do NOT Process Internally.**
- **Pricing zone creation:** create Base pricing zone, select all applicable pages, Save & Confirm, **add all stores.**

**Setup QC:** confirm all pages uploaded (Pricing Zone tab → Items View; confirm no un-uploaded SFTP pages); confirm flyer dates (usually first or last page); complete 4 Standard thumbnails; ensure preview dates are set; complete Setup QC checklist.

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.
- Draw clean boxes around each set of items; box every item with a unique item; remove any boxes that aren't items. **DO NOT box the logo or social-media links** — leave empty.

### Tag / Tag QC — Low complexity
- **Auto-tag: ON. PDF image auto-selection: ON.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, price, categories, disclaimer, original price. **Exclude: SKU, Sale Story, URLs.**
- **Language handling (key):** flyers are primarily Spanish. The **English name is the last line of text → use it for the Item Name.** Put **all Spanish item names + Spanish descriptions in the Description field.** Do NOT include the English name in the description. (Example — Name: "Pork Picnic Roast"; Description: "Carne de Puerco en Trozo / Con hueso. Se vende entera en bolsa.")
- Brand: tag from text-extracted bold text where possible. Current/Original price: enter as-is from the flyer. Categories: best suitable (generally Grocery). Generally no SKU, Sale Story, valid dates, or disclaimer — enter where applicable.

### Image QC
- **Rule:** select a **clean PDF** (clear white background) if possible; if none are clean, use cutouts ("Do not Use PDF Image"). For bundles, choose the cleanest single-item image; may need to click "Generate Data Piping Groups."

## Post-processing / Pre-Final QC (owned by DOC)

- Confirm dates (per PDF); availability toggles correct; thumbnails include retailer logo; standard flyer review checks (items boxed/tagged, spotchecks at 20% of PZs, previews clickable, sessions accurate, geography correct).
- **Geography:** no stores added. **Sessions:** everything run. **Pricing Zone:** everything boxed; check horizontal & vertical scroll.
- **Pages tab / page categories:** page 1 no category; page 2 add categories based on the items shown.
- **Edit Details:** Available Tues–Tues; Valid Wed–Tues; Internal Run Name DD-MM; available everywhere; no theme. QC Thumbnails Standard 4.

## Flyer review

- **Flyer Review type: Lite** (owned by Flex). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Mi Tienda OneGuide (Google Doc `1_sNFGRomRguvJ1IX_DRFC06xRWLpBxhOmD-f7DBAEME`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Michaels USA — Processing Guide

> **Source:** Michaels USA OneGuide (Google Doc `1jhv9wccPLjEWSIWHQ2iXAoxMcokADt-iWuW6JBMS82g`), last updated Jun 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | **Flipp & Distribution only** |
| Slack channels | `#michaels`, `#flex-processing-support` |
| Hosted URL | We do not power their hosted |
| Flyer types & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Related resource | Confluence: "Michaels USA + Canada Account Guide" |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available From / Valid From = Sunday; Available To / Valid To = Saturday (USA). **Canada dates always begin and end 2 days earlier than the US.**
- **Go-live:** Canada goes live **Friday**; USA goes live **Sunday.**

## Upload & setup

### File transfer to FTP (owned by DOC)
1. **Store list** — Thursdays the retailer emails a store list; upload it to the Michaels FTP via CoreFTP/FileZilla (no manipulation, drop directly, no folder needed).
2. **Flyer PDFs** — Fridays the retailer emails flyer files via a third-party file drop (`ecom.michaelsconnect.com`); the subject contains the run name, the body contains login credentials (**credentials in the OneGuide — not stored here**). Select the folder named for the run and download all files (file names identify USA vs Canada).
3. **Merchant FTP credentials** — generate via the `#sftp-automation` Slack channel (AWS lambda command with your ops email). Host `sftp.flipp.com`, username `michaels`, password from the generation email (**credentials in the OneGuide — not stored here**).
4. **Upload** — create a directory named after the run, with sub-directories `usa` and `can`. Drop "US" files in `usa`, "CAN"/"QUE" files in `can`. Files appear in Fadmin within ~1 hour.

### Setup instructions (owned by Vendor)
1. Download the **"Media Store List"** Excel (pricing-zone names + page allocations).
2. **Upload pages** from the weekly folder — CAN (Canada, English), QUE (Quebec, French — set language to French), US (USA pages).
3. **Create pricing zones and assign pages** using the Page Codes document.
4. **Add stores to PZs:**
   - `CAN` / `CA_AD_B` → Canada store set
   - `QUE` / `CA_AD_A` → Quebec store set
   - `US_AD_C` → All Stores (minus stores in `US_AD_E`)
   - `US_AD_E` → usually Kansas City + Pittsburgh store sets (verify in Media Store List)
5. After sessions finish green, complete the standard Setup QC checklist.

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Include:** coupons. **Exclude:** packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Single/multi items:** even if an image shows multiple products (e.g. a pile of sketchbooks), box them as one "item block" if they share a single price/offer.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude: SKU and URLs.**

### Image QC
- Specific items flagged: all photo boxes by Simply Tidy, and all Yarn. Choose clean PDFs wherever possible.

## Post-processing / Final QC (owned by Vendor)

**⚠️ Risk item:** if an **"Update Distributions Error"** appears in the pipeline, **ignore it** — it does not block Final QC or affect go-live.

- Complete any outstanding spotchecks; mark Auto Stack Spot Check complete.
- **Thumbnails — Standard 4:** Thumbnail_1065_x_600 (across first two pages, no whitespace), Stock_Premium (first page), Storefront_Carousel_Premium (first two pages), Storefront_Carousel_Organic (first page).
- Overview > Edit Details: **available on Flipp only, no theme, no external run name**, dates correct.
- **Ensure no item links** — URLs should not be applied to any items.
- Check coupons boxed/tagged (if applicable); check sessions ran.
- For both Michaels Canada and Michaels USA: ignore the listed Final QC warnings and press "Save and Confirm."

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Michaels USA OneGuide (Google Doc `1jhv9wccPLjEWSIWHQ2iXAoxMcokADt-iWuW6JBMS82g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mike Dean Local Grocer — Processing Guide

> **Source:** Mike Dean Local Grocer OneGuide (Google Doc `1DEVGAjapLodeG9ohzdLgv3JlMGf0mydq8Uh4zZfe5kQ`), last updated Jun 20, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | mikedeans.com/pages/weekly-flyer |
| Flyer types & cadence | Flyer Type 1 — Weekly Ad (11787) |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files received:** Wednesday.
- **Publication cadence:** Available From Friday; Valid From Thursday; Available To Thursday; Valid To Friday.
- **Short lead time** — Box QC must be done by Flipp immediately after the task activates.

## Upload & setup (owned by Flex)

- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload → Auto-Group → Save → Save & Confirm. **Do NOT Process Internally.**
- **Pricing zone creation:** create EN pricing zone, select all applicable pages, Save & Next; click "Cross language," then FR; Save & Confirm. **Add all stores to both pricing zones.**

**Setup QC:** confirm all pages uploaded (Pricing Zone tab → Items View; if uploading from SFTP, confirm no un-uploaded pages remain); confirm flyer dates (usually last page, bottom); complete 4 Standard thumbnails; complete Setup QC checklist. **Geography will say FSAs are missing — this is expected.**

## ⚠️ Common errors / risk items

- **Short lead time** — Box QC all items immediately after task activation, paying extra attention to items at the **bottom of page 2.**

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. (Also exclude banners.)

### Tag / Tag QC — Low complexity
- **Auto-tag: ON.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude: SKU and URLs.**

### Image QC
- Standard pricing spotchecks in pipeline.

## Post-processing (owned by Flex)

**⚠️ FSA custom action (Pre-Final QC).** Run the custom action **"Assign FSAs From CSV"**:
- Use the linked "Mike Dean additional FSA's (Sharbot Lake location)" sheet.
- On the flyer run's Pricing Zones page, copy the ID for each Pricing Zone and paste both numbers into the sheet (correct rows).
- Download as CSV, run "Assign FSAs From CSV" with the correct CSV and flyer run ID.
- **Confirm there are 14 FSAs in each pricing zone** once complete.

Then confirm dates (per PDF), availability toggles (all unchecked), thumbnails include the retailer logo, and standard flyer review checks (all items boxed/tagged, spotchecks complete at 20% of PZs, previews published/clickable, sessions accurate, geography correct).

## Flyer review

- **Flyer Review type: Lite** (owned by Flex). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles unchecked, **and 14 FSAs in each pricing zone.**

---
*Source: Mike Dean Local Grocer OneGuide (Google Doc `1DEVGAjapLodeG9ohzdLgv3JlMGf0mydq8Uh4zZfe5kQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Millbank Hardware — Processing Guide

> **Source:** Millbank Hardware (6751) OneGuide (Google Doc `1LLm4b1qrb4y7EStNNxbq2Qlqw31eYfFronXYkt-jrr4`), last updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Hosted URL | N/A |
| Flyer types & cadence | Flyer Type 1 — Flyer (11968), **ad hoc** |
| Processing | Auto-stack |
| Who's involved | Flex (Upload/Setup + FQC); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files received / cadence: ad hoc.** The client typically emails files very late and asks for ASAP processing. They know our timelines — no daytime processing needed. **Happy if live within 4 days; understand if it takes 5.**

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- **Manual upload:** Pages tab → Edit → select all pages from SFTP (or upload manually from email) → Confirm & Upload → Auto-Group **or** manually enter page numbers in the Grouping Number field; ensure language = English → Save & Confirm.
- **Pricing zone creation:** create **Base** pricing zone, select all applicable pages, Save & Confirm, **add all stores.**

**Setup QC:** confirm all pages uploaded (Pricing Zone tab → Items View; confirm no un-uploaded SFTP pages remain); confirm flyer dates (usually first or last page); complete 4 Standard thumbnails; complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **Original Price** — ALWAYS tag the original price if it's listed on the flyer.
- **Multiple items under one name** — they often list many items under the same name with different sizes/prices. **Box every item that has a price**, including unique details (size, code/SKU). Text boxes can be used for the names at the top of the lists.

## QC specifics

### Box Draw / Box QC — **Medium complexity**
- **Auto-Box Draw: OFF. Box QC bot: OFF.** No linking document.
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC — Low complexity
- **Auto-tag: ON. PDF image auto-selection: ON.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, image QC. **Exclude: URLs.**
- **Standard processing:** Brand from logo (if applicable); Name = large title text; Current Price usually red; Original Price as shown; SKU = associated code; other text in description. Tag exactly as shown.
- **List-item processing:** draw a **text box around the title above the list.** Brand from logo or the BRAND column; Name = large title text at top; Original Price from the REG column; SKU = associated code; size/etc. in description.
- **Linking document (when used):** colours group a table where **one URL applies to the whole coloured block** (e.g. the link in row 16 applies down to row 22 for the green rows).

### Image QC
- PDF preferred if clean; otherwise cutouts accepted.

## Post-processing (owned by DOC)

**⚠️ FSA custom action.** FSAs must be overwritten from what Fadmin generates — Millbank is in South/West Ontario and wants only a few select FSAs; a radius large enough to capture them would also capture most of the GTA (not wanted).
- Open the FSA sheet ("FSA Import" tab); copy the flyer's Pricing Zone ID into Column A for ALL FSAs.
- Download as CSV; on the Custom Actions page run **"Assign FSAs from CSV"** with the flyer run ID.
- Confirm all FSAs added via the Geography tab.
- **RISK:** if there is a page swap, FSA Generation re-triggers and this custom action **must be re-run.**

Then confirm dates (per PDF), availability toggles, thumbnails (include retailer logo), and standard flyer review checks (items boxed/tagged, spotchecks at 20% of PZs, previews clickable, sessions accurate, geography correct).

## Flyer review

- **Flyer Review type: Lite** (owned by DOL). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Millbank Hardware OneGuide (Google Doc `1LLm4b1qrb4y7EStNNxbq2Qlqw31eYfFronXYkt-jrr4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Mondou — Processing Guide

> **Source:** Mondou OneGuide (Google Doc `1c1TXrCicnEd8FAJRkfanmcQdd_hwv8qSWxZMtheGBI4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | N/A |
| Availability | All platforms |
| Slack channels | `#mondou`, `#flex-processingsupport` |
| Hosted URL | mondou.com (we power their hosted) |
| Flyer types & cadence | Flyer Type 1 — **Ad-hoc** |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Language | Bilingual — English & French |

## Files & schedule

- **Files: ad-hoc.** Usually sent **7 business days before live** and **5 business days before merchant preview.**
- **Preview:** URLs sent 2 days in advance of the live date.
- **Linking document:** Yes — dropped to FTP.

## Upload & setup (owned by Vendor)

- **Manual upload:** select pages → Edit → select files from FTP (named by live date; `AN` = English, `FR` = French). Group by page number in the file name. Assign English to `AN` files, French to `FR` files. Save and Complete.
- **Pricing zones:** two zones — EN and FR (descriptions "EN"/"FR"). Create EN (English pages, correct order), Save & Next; create FR (Language: French, French pages, correct order), Save & Done. **Add all stores to each PZ.**
- **Vendor attachments:**
  - The FTP has a **"Layout" PDF** telling Vendors how to box pages. Due to its size, **compress it** (pdfcompressor.com) before attaching. Vendors tab → Upload Mass Attachment → All Vendor Assignments → attach the compressed Layout PDF.
  - Attach the **tagging Excel** (e.g. "Flipp_Mondou_…") to Tag/QC — contains both EN + FR links, so upload once.
- **Custom Tiles — ONLY if the flyer is a masthead/promoted publication** (BD will tell you). If not, skip and do Standard 4 thumbnails. If yes, download both custom tiles (AN + FR) and override Storefront Premium + Storefront Carousel Premium on the EN PZ (AN tile) and FR PZ (FR tile).
- **Edit Details:** valid dates match PDF; available 1 day before valid; **preview date 3 business days before the available date**; available everywhere; no theme. Complete Setup QC.

## ⚠️ Common errors / risk items

- **EN vs FR tagging** — use the correct language from the tagging document for each item. **Pay special attention to URLs: EN URLs on the English version, FR URLs on the French version.** Do NOT translate — if only French text is present, tag in French even on an English page.
- **Free-item-with-purchase sale story** — e.g. Brand: OPEN FARM; Name: OPEN FARM Cat Food; Description: 1.81 kg; Sale Story: "FREE Open Farm Cat food pack 156g With the purchase of Open Farm Cat Food 1.81kg."

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** Linking document required (Box Draw/Box QC specific).
- **Include:** social media. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, special weblinks.
- **Box EXACTLY as laid out in the Layout document** (boxes identified by circles/lines with a number each). **Follow the layout document above all other guidelines.** Box banners with overarching stories together.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** Linking document required (Tag/QC specific).
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **URL tagging:** ALL items must have a URL. Use only the URL FR and URL EN columns of the spreadsheet; FR URLs → French pages, EN URLs → English pages. **Direct Link = YES** items: change Display Type to Link, then paste URL and save.

### Image QC
- Select clean PDFs whenever possible; otherwise the cutout image.

## Post-processing (owned by Flex)

**All post-processing must be completed two days before the live date so retailer previews can be sent.**

- **Category QC / Image QC:** standard.
- **URL/Links QC:** Overview → Items without a URL → assign missing URLs from the vendor-tasks doc; **0 items without a URL.**
  - **⚠️ RISK:** FR pages/items need FR URLs; EN pages/items need EN URLs. QC via Item Search: (URL contains `fr-CA`, PZ = EN) should return nothing — fix any that appear; then (URL contains `en-CA`, PZ = FR) should return nothing — fix any that appear.

## Final QC (owned by Vendor)

- 0 items without a URL; Standard 4 thumbnails.
- **Flyer Sorting:** lookbooks always second to primary content (Merchant Page → Flyer Sorting).
- Edit Details: available everywhere, no theme, no external run name, dates correct. Listed warnings may be ignored.

## Cloning — "Flipp App" + "Hosted" links for the same publication

When the retailer provides both link sets: ensure the original flyer has all "FINAL URL FLIPP APP" links applied. Clone to the same flyer type, name it "hosted - clone." On the clone, item export → in Sheets keep only `item_id, sku, url` → find/replace the Flipp utm parameters (e.g. `utm_source=flipp&utm_campaign=…`) with the hosted parameter `origin_page=flippflyerpage` → confirm links match the "FINAL URL HOSTED (ON MONDOU)" column → download CSV → import items to the cloned run → verify via last session results.

## Retailer previews (owned by DOC)

- 2 days before live, send EN + FR preview links (Overview → Ad Hoc Processing → Preview URLs → copy Hosted 2 Preview URLs). Send **only after FQC** with all items URL-tagged. The retailer reviews and returns corrections; update the items.

## Custom URLs / Deep Links (owned by DOC)

- "Deep Links" take a user directly to the live flyer on the hosted page (not preview access) — used in retailer email blasts. Available any time once the flyer shell is built (only the flyer ID is needed). If the flyer ID changes, resend updated deep links. Append the flyer ID to the base URLs:
  - **English:** `mondou.com/en-CA/flyer-c44.html?locale=en&flyer_run_id=<ID>`
  - **French:** `mondou.com/fr-CA/circulaire-c44.html?locale=fr&flyer_run_id=<ID>`

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Mondou OneGuide (Google Doc `1c1TXrCicnEd8FAJRkfanmcQdd_hwv8qSWxZMtheGBI4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Moonlight Grocers — Processing Guide

> **Source:** Moonlight Grocers OneGuide (Google Doc `1XIkTOV3F9QKOgWmOcZ2-2Y9Hg9U6UAxmkVys_xM0TT8`), last updated Jan 21, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | N/A |
| Flyer types & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available From Thursday; Valid From Wednesday; Available To Thursday; Valid To Wednesday.

## Upload & setup (owned by Vendor)

- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- **Manual upload:** Pages tab → Edit → select all pages from SFTP (or upload from email) → Confirm & Upload → Auto-Group or manually enter grouping numbers; ensure language English → Save & Confirm.
- **Pricing zone creation:** create Base pricing zone, select all applicable pages, Save & Confirm, **add all stores.**

**Setup QC:** confirm all pages uploaded (confirm no un-uploaded SFTP pages); confirm flyer dates (usually first or last page); complete 4 Standard thumbnails; complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **Look for multiple products** (box each product individually).

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC — Low complexity
- **Auto-tag: ON. PDF image auto-selection: ON — but DO NOT USE PDF IMAGES.**
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude: SKU and URLs.**
- **Standard processing:** Name = large title text; include price and any other text in description. Tag exactly as shown.

### Image QC
- PDF preferred if clean; otherwise cutouts accepted. (Note the tagging table says do not use PDF images — confirm with the flyer review guide.)

## Post-processing / Pre-Final QC (owned by Flex)

- Confirm dates (per PDF), availability toggles, thumbnails include retailer logo, and standard flyer review checks (items boxed/tagged, spotchecks at 20% of PZs, previews clickable, sessions accurate, geography correct).

## Flyer review

- **Flyer Review type: Lite** (owned by DOL). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Moonlight Grocers OneGuide (Google Doc `1XIkTOV3F9QKOgWmOcZ2-2Y9Hg9U6UAxmkVys_xM0TT8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
