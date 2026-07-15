# Retailer Processing Guides — O

> Bundle of 7 retailer-specific processing guides (O). Contacts and credentials are omitted from every guide.

**Contains:** Ocean State Job Lot, Old Farm Market, Ollie's Bargain Outlet, Olympia Liquor, On The Run (Chevron), Orvilles Appliance, Oxford Mills


---

# Ocean State Job Lot — Processing Guide

> **Source:** Ocean State Job Lot OneGuide (Google Doc `1ZO2yur5mgZX6bLrtew4tlIKESKOdBb5BYgTCBoQVlCQ`). OneGuide last updated Jul 14, 2026. Contacts/credentials omitted.
> **High box-draw complexity. ⚠️ Never use Fetch URL when tagging.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#osjl`, `#osjl-nativex`, `#flex-ocean-state-job-lot` |
| Hosted URL | http://www.flyertown.ca/flyers/oceanstatejoblot |
| Flyer type(s) & cadence | 6093: Weekly · 12183: Coming Attractions |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS N/A; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |
| Linking document | **Yes — SKU PDF and linking document (.xlsx), used for both Box and Tag** |

## Files & schedule (Weekly)

- **When files arrive:** Thursday (flyer PDFs); **SKU PDF and link document arrive Friday mornings**
- **Publication cadence:** Available From Wednesday, Valid From Wednesday/Thursday; Available To Thursday, Valid To Wednesday
- **Preview date:** Monday
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup

### Weekly (owned by DOC)
- **Manual upload on Fridays** (Pages > Edit).
- **⚠️ Risk item: wait to upload until the SKU PDF and Link Document are sent Friday mornings**, even though the flyer PDFs arrive earlier — **OS cannot box/tag without these documents.** If covering the account, message the DOL when done Friday to flag that the attachments need adding when available.
- Upload and auto-group pages (double-check order). Files are often uploaded with more than a week's lead — use the folder named with the valid date of the upcoming run.
- **⚠️ Risk item — page swaps before upload:** they generally replace the old PDF page asset with the new one (add all pages in the folder), but occasionally there are duplicates — use the newest version per the email instructions. When in doubt, upload both, open them, and decide which to keep/delete (the newer file sometimes has `_REV`; you can also check SFTP upload timestamps).
- **Flyer Creation:** 1 Pricing Zone "Base"; assign all stores. **Attach the URL .xlsx and SKU .pdf to all Vendor Tasks** with a note: "Please use spreadsheet and PDF File for Box Draw and Tag."
- Optional: if files won't attach to the Vendor Tasks, upload to a Google Drive folder and share with the vendors by email (per the OneGuide's template).

### Weekly Setup QC (owned by DOC)
- Pricing Zone: all pages assigned, language English; all stores assigned.
- **Edit Details (important):** Available from **Wednesday 7 PM** to **Wednesday 6:59 PM**; Valid from **Thursday 12 AM** to **Wednesday 11:59 PM**; set **Preview Date to Monday** (two days before go-live) at 12 AM to avoid items not being tagged before the preview link goes out.
- Standard 4 thumbnails. Complete Setup QC checklist.

### Coming Attractions (owned by Vendor)
- **Manual upload on Thursdays:** select the folder containing the date and Coming Attractions (CA) pages.
- Flyer Creation: 1 Pricing Zone "Base"; assign all stores. Note: "No additional linking docs, please box and tag as per pdf."
- Setup QC: same dates/preview/thumbnail rules as Weekly.

## QC specifics

**Box Draw (HIGH complexity — Auto-Box OFF, Box QC bot OFF; SKU PDF + linking .xlsx required)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Use the SKU PDF and linking Excel for reference. If information is incorrect, DO NOT stop box draw** — email the Flipp team to alert them and continue boxing/tagging using the sheet.
- If an item is NOT in the linking Excel, box it together with other items in the same section per the SKU PDF.
- **"Asst" lines:** box multiple items together when the links spreadsheet shows an "Asst" line; box items with individual SKUs/unique URLs separately. Treat each line in the links spreadsheet as one item box; use the **Page** and **Placement** columns to locate the box.
- Box each individual item (e.g. 10 rugs = 10 boxes). Multiple sizes/options with individual prices → **box each size as its own item** (no longer boxed as one list). Items without images must still be boxed (box text and price together); watch for items listed under other ad-blocks.
- **⚠️ Risk item — links-spreadsheet discrepancy:** items can be tagged separately if they have specified SKUs; if the sheet lists items separately on one page but together on another, follow the sheet. If no link is available but an item is obviously separate, box it separately and leave the URL blank.

**Tag / Tag QC (MEDIUM complexity — Auto-tag OFF, PDF Image Auto-Selection ON; linking doc required)**
- **⚠️ DO NOT USE FETCH URL WHEN TAGGING.**
- **Include:** brand (most items have none — add if identifiable), name (as it appears in the flyer), pre/postfix, valid dates (override when applicable), description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Prefixes:** use "Sale!", "All Sizes", "Your Choice" when they appear next to a product. **Do NOT** tag "buy for $$$ get $$$" deals using a "buy for" prefix + "get" postfix — only use a `- $$$` postfix when there are multiple prices. Package deals (e.g. "Buy 5 for…") → use "5 for" as the prefix.
- **Price:** singular item → Current Price, regular price in Raw Original Price ("Compare to $$$" goes in the description). List of options with various prices → lowest price in the Price field, postfix `- $$$` with the highest price. Select pre-/post-fixes from the drop-down lists.
- **Description:** multiple sizes/options listed here. If an ad-block has a header AND a list of options AND no per-item images, the description is the list of item details. If each item has its own image, use the header as the Name, box/tag each separately.
- **SKU:** use the attached document; items link by page + placement number. "Asst" SKU = more than one SKU per the SKU PDF — tag as many as possible.
- **Sale Story:** fill in as shown; do not tag "Dollars Off" unless specified. For "Buy a XX for $$… Get a $$ Crazy Deal Gift Card FREE!" include all relevant text. **1 Buy + 2 Get format** → tag as "Buy *Item Name* and get *Amount* Crazy Deal Gift Card Free!"
- **Categories:** use the category in the attached Excel; if an item isn't listed, pick the closest.
- **Disclaimer:** don't include percent-off/dollar-off amounts; only include disclaimers listed with an individual product (not page top/bottom).
- **URLs:** a Links Document is provided weekly (Product Name, SKU, URL, Page, Placement). Add the URL to all listed products. **If there is no URL, leave blank — DO NOT use Fetch URL.**
- **⚠️ Prices without decimals:** prices may print without a decimal (e.g. "$11.99" shown as $11 with a small ⁹⁹). **Always include decimals when tagging, even if the page shows none.**

**Image QC**
- Always check for a PDF image first; uniform backgrounds are OK. **Do not use PDF images with any visible background** (table edge, tiles, fabric, other items) — revert to the cutout even if it cuts off the item. Use cutouts when no PDF is available or when multiple item images are grouped together. If a cutout only shows the item name/price (product not visible), keep the cutout.

## Post-processing

### URL/Links QC (owned by Flex)
- Download the .pdf and .xlsx attached to the Vendor Tasks. Overview → Item Search → Field: URL, Condition: IS ___ (Blank). Sort by Page Grouping Index to go page by page.
- Use the SKU PDF and URL .xlsx to confirm whether each item should receive a URL. **Not all items get URLs** — if not assigned in the linking document, **leave blank, do not fetch.** Copy the URL from the URL column, paste into the URL field, save.
- Notes: if flyer names don't match the .xlsx, copy the name from the linking document. One box may cover many items (retailer preference) — apply the one link. Filter the URL sheet by the PG column; a missing page means no items on that page get URLs (skip it).

### Final QC — Weekly (owned by DOC)
- QC Thumbnails (Standard 4): 1065×600 (remove white border, cover pg 1&2), stock premium (cover pg 1), storefront carousel premium (cover pg 1&2), storefront carousel organic (cover pg 1).
- Edit Details: Available Wed 7 PM → Wed 6:59 PM; Valid Thu 12 AM → Wed 11:59 PM; Preview Date Monday; available everywhere (no toggles); no external run name; no theme unless specified.
- **Manage Tracking Codes → "Apply All Tracking Codes"** (no tracking codes exist, but this forces backend processes so all Shop Now buttons go live).
- Pages: all items QC'd; box/tag any links from the initial file-drop email. Pricing Zone: one "Base", all stores; check previews. Geography: no change WOW unless specified.
- **1 Buy + 2 Get deals:** ensure sale story tagged as "Buy *Item Name* and get *Amount* Crazy Deal Gift Card Free!"
- FQC Checklist — ignore the "some categories don't have thumbnails" warning. **Flyer sorting priority: Weekly, Lookbook (Seasonal), Coming Attractions.**

### Final QC — Coming Attractions (owned by Vendor)
- Same thumbnail/Edit Details rules as Weekly.
- **Override Image URL:** for any pages that do **not** have the "ARRIVED" callout on the product image, select **Do Not Use PDF Images** and enter the Coming Attractions VF logo asset URL in the **Override Image URL** field, then save. Repeat for all such items on all pages.
- Pages/Pricing Zone/Geography checks as above. FQC Checklist (ignore thumbnail warning). **Flyer sorting priority: Weekly, Coming Attractions, Lookbook (Seasonal)** — do not adjust yourself; flag if the order looks off.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- **Preview link:** send the Hosted 2.0 vertical preview link to the retailer contacts (cc DOL) the day before go-live (Wednesday 7 PM live), per the OneGuide's email template.
- **Corrections:** OSJL sends URL corrections Wednesday morning (highlighted in yellow on the sheet); have Flex apply all highlighted changes to the flyer run. Track all changes in the OSJL Change Tracker.
- Page swaps follow the baseline page-swap process.

---
*Source: Ocean State Job Lot OneGuide (Google Doc `1ZO2yur5mgZX6bLrtew4tlIKESKOdBb5BYgTCBoQVlCQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Old Farm Market — Processing Guide

> **Source:** Old Farm Market OneGuide (Google Doc `1Co46oU7q0gFO_Y4pgsJF_1bBsua4v7l83J_9h-ryx-o`), updated Oct 7, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#onboarding`, `#flexflyerreview` |
| Hosted URL | theoldfarmmarket.ca |
| Flyer types & cadence | Weekly Flyer |
| Processing | Auto-stack; Flex does Flyer Review; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Friday.
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Thursday, Valid To Wednesday.
- **Preview date / linking document:** None.
- **Workflow:** Setup QC (Flex, Fri) → FQC (Flex, Tue) → Live (Wed).

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu within the corresponding week's folder.
- **All pages remain Index 1** (only 1 page per version). English pages only. Save & Confirm — **do NOT process internally.**
- **Pricing zones — 3 zones, one per page:**
  - 1 × Courtenay
  - 1 × Duncan
  - 1 × Victoria (**previously Oak Bay — if a page is labelled Oak Bay, assign the Victoria store**)
  - Save & Confirm; add all corresponding stores.

### Setup QC (owned by Vendor)
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **Risk:** if uploading from SFTP, confirm no pages were left un-uploaded.
- Confirm flyer dates (on first page). Thumbnails (4 Standard). **No theme, no external run name.** Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF):**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Ensure all single items have a box drawn. **General callouts do not need to be boxed.**

**Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON):**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand used for both Box/Tag.
- Exclude: SKU, URLs.
- **Do not include general callout information** like "Back to school."

**Image QC (Vendor):** PDF preferred if clean; otherwise cutouts accepted.

**Spotchecks:** standard pricing spotchecks in pipeline (pricing discrepancies / uncommon Name info).

## Post-processing (owned by DOC)

- **Pre-FQC:** confirm dates vs PDF, availability toggles, thumbnails include retailer logo, legibility heights (60, 40); confirm boxing/tagging complete, spotchecks (20% of pricing zones), previews published and clickable, sessions complete, geography correct.
- **FQC:** complete FQC checklist.

## Flyer Review (owned by Flex)

- **Type: Lite.** Check flyer dates, previews showing correctly, all items tagged accurately, no extra boxes from auto-box, geography correct (may change WoW by retailer distribution), availability toggles correct.

---
*Source: Old Farm Market OneGuide (Google Doc `1Co46oU7q0gFO_Y4pgsJF_1bBsua4v7l83J_9h-ryx-o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Ollie's Bargain Outlet — Processing Guide

> **Source:** Ollie's Bargain Outlet OneGuide (Google Doc `1IRqpP6JGQmpvktuqRCnFXSsxlRq-m0ri331IYNiGwKI`), updated Oct 8, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Hosted URL | ollies.us/currentflyer/flyer.html |
| Flyer types | Weekly · Weekly Boosted · Grand Openings — **all 3 processed under the same Weekly flyer type** |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Tuesday.
- **Cadence:** Available From Tuesday, Available To Wednesday; Valid From/To Wednesday.
- **Short lead time (Regular Weekly / "Vanilla"):** upload as Static/Vanilla on hosted only, then follow up 3–5 business days to FQC.

## ⚠️ #1 Risk item — Mark Vanilla
**Must mark Vanilla first (Overview → Make Vanilla → All Pricing Zones) before completing Setup QC.** The Lead must review and mark setup reviewed, otherwise the flyer will not go on hosted.

## Codesheet upload (Weekly & Boosted — 2 codesheets: Pages & Versions)

Open the Ollie's Publication List → File → Make a copy. Use the **Pages** and **Versions** tabs (ensure dates match the flyer run dates).

**Prep the Versions tab:**
- Double-check start/end dates against the flyer run names.
- Confirm start/end times in columns H and J are 24hr `HH:MM` (usually `21:00`); apply the format down the whole column.
- Delete hidden rows with no store assigned. Capitalize all header-row cells. Download as `.csv`.

**Prep the Pages tab:**
- **Risk item:** confirm the pricing-zone names match the Versions tab format exactly (e.g. `W-5100` in Pages = `W-5100` in Versions column F). **Mismatches create duplicate pricing zones (one with pages, one with stores).**
- Delete any "No Pages" text. Download as `.csv`.

**Codesheet #1 — Pages:** Config `ollies`; base directory = SFTP folder path; **toggles 3/4/5/6.** Save & run. Wait until green.

**Codesheet #2 — Versions:** Config `ollies_stores`; base directory `/`; **toggles 1 and 4.** Save & run.

- If it errors, verify the available/valid dates match the Versions tab and the flyer run.
- If a page can't be found, check for typos in the Pages tab and that page names match the SFTP.
- After both run: confirm pricing-zone and page counts, then mark flyer creation complete.

## Setup (Weekly Regular / Vanilla)

- **Mark Vanilla before completing setup** (see risk item above).
- **Edit Details — dates:** Available From Tue 9pm; Valid From Wed 12am; Available To Wed 9pm; Valid To Wed 9pm.
- **< 5 business days lead time:** upload in Vanilla mode, **Available on Hosted only** (un-vanilla and set available everywhere at FQC). **≥ 5 business days:** set available everywhere, no vanilla needed.
- No preview date; Internal Run Name = Date; no external run name; no theme.
- **Thumbnails (Standard 4):** 1065×600 (2 pg), stock premium (1 pg), storefront carousel premium (2 pg), storefront carousel organic (1 pg).
- **Staggered dates (rare):** 9pm available / 9am valid / 9pm end. Wed: avail Tue 9pm, avail-to Tue 9pm, valid Wed 9am, valid-to Tue. Thu: avail Wed 9pm, avail-to Wed 9pm, valid Thu 9am, valid-to Wed.
- Confirm upload in Pricing Zone preview; confirm all sessions ran; geography usually unchanged (except recent grand openings).
- Complete Setup QC checklist, then **mark Auto Stack Spot Check complete (pushes the flyer live in vanilla mode).** Send flyer run to Lead to review. Create an Optics/PSS ticket to follow up FQC & un-vanilla (due in 3–5 days; skip if the pub ends before FQC).

## Setup (Weekly Boosted — yellow-highlighted runs)

- Typically ≥ 5 business days lead time. **No staggered dates since May 2026.**
- Same codesheet process as Weekly. Internal Run Name = Date *Boosted*. Same thumbnails and date rules.

## Setup (Grand Openings — green-highlighted, moving to Flex)

- Short lead time; upload as Static/Vanilla on hosted only, follow up 3–5 business days to FQC. Typically Available 2–4 weeks, Valid 1–3 weeks.
- DOC: create the run from the Publication Tracker dates, add the new store to Fadmin (full address & store code in the Store List tab), harmonize once added.
- **Hidden on Flipp & distribution.** No preview date; Internal Run Name = "City GO"; External Run Name = "City Grand Opening"; no theme.
- Dates: Available From Tue 9pm; Valid From Wed 9am; Available To Wed 9pm; Valid To Wed 9pm; 1-week run.
- **Manual upload:** files are in a folder named after the store — upload all pages in that folder into one base pricing zone. Add the grand-opening store number.
- Mark Vanilla (all pricing zones) before completing Setup QC; mark Auto Stack Spot Check complete.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF):**
- **Include:** packaged deals (washers/dryers), sign-up page, social media, special weblinks. If there's a "web page" at the end of the flyer, box it.
- **Exclude:** coupons, retailer logo, banners.
- Box items as they appear in the flyer; draw text boxes where items require it. **Box brand logos together (not separately).** Box items with several sizes/prices separately.

**Tag / Tag QC (Low; Auto-tag ON):**
- Include everything: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for both Box/Tag. Tag as it appears in the flyer.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

**Spotchecks:** standard pricing spotchecks in pipeline.

## Final QC (owned by DOC)

- Mark AutoStack complete; Sessions → **Mark In Store Only**; un-vanilla all pricing zones; make available everywhere; verify staggered dates (if applicable); confirm thumbnails.
- Pages: confirm all items tagged & tag-QC'd. Pricing Zone tab: confirm all items boxed; vertical preview items clickable. Geography unchanged (unless grand openings).
- Complete FQC checklist and a live check on Flipp & hosted (may take up to an hour to reflect).

## Flyer Review (owned by Flex)

- **Type: Lite.** Checks: risk items, overview tasks, pages, pricing zones, sessions, vendors, geography.

---
*Source: Ollie's Bargain Outlet OneGuide (Google Doc `1IRqpP6JGQmpvktuqRCnFXSsxlRq-m0ri331IYNiGwKI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Olympia Liquor — Processing Guide

> **Source:** Olympia Liquor OneGuide (Google Doc `1cmEadLuD4rCwO0mkYn1Qe6ianve_dyGGNJAs29_qIaQ`). OneGuide last updated Aug 6, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | **Available on Flipp only** |
| Slack channel(s) | `#olympialiquor`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer Type 1: Ad-hoc |
| Processing | Auto-stack |
| Involvement | Flex (Processing Support + Flyer Review); OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc (sent over email; DOC/DOL should add files to SFTP for processing support). Flyers are short — **1–2 pages with no links.**
- **Publication cadence:** Ad-hoc
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC)

### ⚠️ Common errors / risk items
- **Files are often late or received after the flyer live date** — let the retailer contact know the adjusted live date based on processing times and expedite processing where possible.
- **If uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.**

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu on the right → Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure English is selected for all pages. Save & Confirm — **do NOT Process Internally.**
- **Pricing zone:** create Base pricing zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC (owned by Vendor)
- Confirm all pages uploaded correctly (Pricing Zone tab → Items View). Confirm flyer dates (usually first or last page). Complete Thumbnails (Standard 4). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

**Tag / Tag QC (Low complexity — Auto-tag OFF)**
- **Include:** brand, name, description; pre/postfix, valid dates, price, sale story, categories, disclaimer, original price if applicable.
- **Exclude:** SKU, URLs.

**Image QC**
- Standard image QC. Usually no PDF images are available, so cutouts are used; if clean PDF images exist, they are preferred.

## Post-processing (owned by DOC)
- **Pre-Final QC:** confirm dates (per PDF); availability toggles correct; thumbnails include the retailer logo; standard flyer review checks (all items boxed/tagged; spotchecks complete for 20% of pricing zones; previews published and clickable; sessions completed; geography correct).
- **Final QC:** complete FQC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex) — flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Olympia Liquor OneGuide (Google Doc `1cmEadLuD4rCwO0mkYn1Qe6ianve_dyGGNJAs29_qIaQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# On The Run (Chevron) — Processing Guide

> **Source:** On The Run (Chevron) OneGuide (Google Doc `1jibyHxhmZCZfSZD2B9HgNfH3DnX7lnpe8a4rYP1H1H8`). OneGuide last updated Apr 25, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#on-the-run` |
| Hosted URL | https://journie.ca/on-the-run-ca/on-en/flyer |
| Flyer type(s) & cadence | Flyer Type 1: Direct flyer — Ad-hoc |
| Processing | Auto-stack |
| Involvement | Flex N/A; OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc
- **Publication cadence:** Ad-hoc; no preview; no linking document
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (DOC, ~2 days out) → FQC (DOC)

## Upload & setup (owned by DOC)

- **Manual upload:** pages come via email and **need to be uploaded to the SFTP internally.** Once synced: Pages tab → Edit → select all necessary pages from the SFTP menu in **both English and French** → Confirm & Upload. Auto-Group or manually enter grouping numbers; **French pages must be toggled to French.** Save & Confirm — **do NOT Process Internally.**
- **Pricing zones:** create one **English** and one **French** zone; add the appropriate pages to each.
- **Stores (via `generic_stores` codesheet):** the retailer provides a store list; add it to the generic sheet and upload via the Codesheet tab. Build a new Google Sheet with headers `stores` and `pricing_zone`; put store codes in the stores column and `ENG`/`FRE` in the pricing_zone column to match the retailer's English/French designations. Based on previous runs: **535 ENG stores, 165 FRE stores** (may change if the retailer provides a new store list).

### Setup QC (owned by Flex)
- Confirm all pages uploaded correctly (Pricing Zone tab → Items View). **Risk:** if uploading from SFTP, confirm no pages were left un-uploaded.
- Confirm flyer dates (sent via email and/or in the On The Run Slack channel via BD).
- Complete Thumbnails (Standard 4). **No theme, no external run name.** Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)**
- **Include:** social media, special weblinks.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page.
- Box every item individually by offer and/or price.

**Tag / Tag QC (Low complexity — Auto-tag OFF)**
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs.
- **Exclude:** SKU.
- **URLs — always apply this link to all items:** `https://bigboxoutletstore.ca/blogs/flyer?utm_source=flipp`. All PDF information should be included in the item pop.

**Image QC**
- Standard image QC — PDF preferred if clean; otherwise cutouts are accepted.

## Post-processing (owned by DOC)
- **Pre-Final QC:** confirm dates (per PDF, or confirm in the On The Run Slack channel with BD); availability toggles correct; thumbnails include the retailer logo; standard flyer review checks (all items boxed/tagged; spotchecks complete for 20% of pricing zones; previews published and clickable; sessions completed; geography correct).
- **Final QC:** complete FQC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex) — flyer dates, sessions completed, previews correct, all items tagged accurately, **no extra boxes drawn during the auto-box process**, geography correct (may change WoW based on retailer distribution instructions), availability toggles correct.

---
*Source: On The Run (Chevron) OneGuide (Google Doc `1jibyHxhmZCZfSZD2B9HgNfH3DnX7lnpe8a4rYP1H1H8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Orvilles Appliance — Processing Guide

> **Source:** Orvilles Appliance OneGuide (Google Doc `1IPdPt_9sADefBZ_KAcmzjtzHDzzcOePH6LA_e6Vl5Ws`). Contacts/credentials omitted.
> **Note:** This OneGuide is largely a blank template. Only the account facts below were filled in; detailed upload, setup, and QC instructions were not completed in the source doc.

## Account at a glance

| | |
|---|---|
| Publication cadence | Available: Tuesday · Valid: Tuesday |
| Processing type | Auto-stack |
| Platforms / availability | **Available only on Hosted** |
| Involvement | **Flex owns processing**; OS completes Upload + FQC |

## QC specifics (from the filled-in fields)

**Box Draw (Low complexity)**
- **Include:** social media, sign-up page, special weblinks, retailer logo, packaged deals.
- **Exclude:** coupons.
- Linking document required for Tagging and Item QC.

**Tag / Tag QC (Low complexity)**
- **Include:** brand, name, pre/postfix, description, SKU, price, valid dates, sale story, categories, original price.
- **Exclude:** disclaimer, URLs.

## Not documented in the source
Upload steps, config/toggle details, setup QC, image QC, risk items, pre-/final QC, and out-of-processing instructions were left as blank template placeholders in the OneGuide. Refer to the OneGuide directly if these are later filled in.

---
*Source: Orvilles Appliance OneGuide (Google Doc `1IPdPt_9sADefBZ_KAcmzjtzHDzzcOePH6LA_e6Vl5Ws`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Oxford Mills — Processing Guide

> **Source:** Oxford Mills OneGuide (Google Doc `1bAdjinu-pfan549tJBzi0nym970--FCXct2kichzZVA`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#oxford-mills`, `#flex-processingsupport` |
| Hosted URL | oxfordmillsoutlet.com |
| Flyer types & cadence | Flyer Type 1: Weekly · Flyer Type 2: Monthly |
| Processing | Auto-stack; Flex owns processing; no coupons; no Feedel/Strategic Ops |

## Files & schedule (Flyer Type 1)

- **When files arrive:** Ad-hoc.
- **Cadence:** Available From Wednesday, Valid From Tuesday; Available To Wednesday, Valid To Tuesday. **Retailers are regularly late — dates confirmed via email.**
- **Linking document:** N/A.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (owned by Vendor)

- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu (or upload manually from email) → Confirm & Upload. Auto-Group or manually add page numbers into the Grouping Number field. Ensure **English** language selected. Save & Confirm.
- **Pricing zones:** Create Base pricing zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC (owned by Flex)
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **Risk:** if uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.
- Confirm flyer dates (usually first or last page).
- Thumbnails (4 Standard). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON):**
- **Include:** packaged deals (e.g. washers/dryers).
- **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.
- Box all individual items separately. **Mattress with multiple sizes:** box the smaller/top size with the image; box the remaining sizes individually.

**Tag / Tag QC (Low; Auto-tag ON):**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, original price. Brand is Box-Draw/Box-QC specific.
- Exclude: SKU, disclaimer, URLs.

**Image QC:** choose white-background PDF where possible, else cutout.

**Item Category QC (Flex):** page categories for all but the first page (1 per page).

## FQC (owned by Flex)

- Spotchecks if required. QC thumbnails (Standard 4: stock premium, storefront carousel premium, storefront carousel organic).
- Edit Details: available everywhere; no external run name; check run dates match the last page of the PDF.
- **Flag missing pages or geography changes to the full-time team.**
- **Flyer Review type: Lite.**

---
*Source: Oxford Mills OneGuide (Google Doc `1bAdjinu-pfan549tJBzi0nym970--FCXct2kichzZVA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
