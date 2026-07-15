# Retailer Processing Guides — H

> Bundle of 24 retailer-specific processing guides (H). Contacts and credentials are omitted from every guide.

**Contains:** H-E-B, Haggen, Handyman Hardware, Hannaford, Hardwood Design Centre, Harris Teeter (+ Delivery), Hart Stores, Harveys Supermarket, Harvey's (Restaurant), Health First Network (buying group), Health Mart Pharmacy, Healthy Planet, Heinen's Fine Food, Hen House, Henry's, HockeyStickMan, Home Depot Canada, Home Depot USA, Home Furniture Outlet, Home Hardware & Home Furniture, HomeBuys, Horizon Sante, Houchens IGA, Hy-Vee


---

# H-E-B — Processing Guide

> **Source:** H-E-B OneGuide (Google Doc `1DQuZWM8aatVpLrz7_LFAlKz2pX4G3ziySzDR_AYuQ84`), updated Jul 6, 2026. Contacts/credentials omitted.

Two-city account: **Houston (HFD)** and **San Antonio (SAFD)** processed as separate zone sets in one run, plus a weekly Houston digital insert.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Weekly + Monthly |
| Processing | Auto-stack; Flyer Review (Medium); OS setup; no coupons; **Feedel/Strategic Ops: YES** |

## Files & schedule

- **Files arrive:** Monday. Available From **Monday @ 1:00 AM** / Valid Tuesday. 1-day preview.
- **In FTP** (search "xls"): files with **"Recap"** = page codesheet; **"WeeklyAdInfo"** = linking doc. Ad Zone charts held in a shared Drive folder.

## Upload & setup (owned by Vendor)

**Process Houston stores + pages FIRST** (makes it easier to add the Digital Insert during FQC; keeps PZs distinguishable — Houston PZs are numbered **60–85**, San Antonio outside 60–85).

**Pages codesheet manipulation:**
- **Houston:** delete Column E ("Digital Resize" / "Column 4") entirely, save as CSV (fadmin treats it as already-uploaded; re-added later — this is the HEB app insert, required weekly in Houston).
- **San Antonio:** delete any "N/A" cell text (leave blank, don't shift up), save as CSV.

**Codesheet uploads (base dir `/`):**
- Houston/San Antonio **stores:** config **`heb_stores`**, toggles **1,4,5,6** checked (NOT 2,3,7).
- Houston/San Antonio **pages:** config **`heb_original`**, toggles **1,3,4,5,6** checked (NOT 2,7).

**Setup:** download "WeeklyAdInfo" per city, upload via Vendor tab "Upload mass attachments" (Houston + San Antonio). Rerun sessions. Leave "HEB app - Digital Resize.pdf" stale until FQC (Friday PM). Geography: no stores added/removed. LH 40/30; standard 4 thumbnails; available 1am Eastern day before; 1-day preview.

### ⚠️ Common errors / risk items

- **PZ tab (RISK):** confirm all Houston zones (60–85) sit at the top after upload.
- **New versioning (ad zone) list:** always use the most up-to-date; Houston — delete both sister-banner sections (Mi Tienda + Joe V's); San Antonio — delete Blush Pink/blue/green "Subtitle" cells (keep darker pink Ad Zone), Ctrl+F "EFC" and delete EFC store numbers; save as CSV.
- **Promo IDs are zone-specific** — be careful when tagging.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required):** **include** coupons, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. Box every item with a unique item ID; box all coupons; **red italic text = box separately.**
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - Multi-item brands/names separated with **"OR"**; red text before names NOT tagged; BOGO — the product to purchase goes in Name.
  - **Custom fields — Promo ID & Unique Promo ID:** every item on every page has both. Filter the pipeline spreadsheet by AD ZONE (the number after "z" in the page description, e.g. `H0718p01z50` → zone 50; pages with "x" appear across multiple zones — use the first match), then by page, find the item by description, tag Promo ID (Column B) and Unique Promo ID (Column E).
  - **Override Image URL:** for two-line items sharing an ad block with another product, use the arbitrary-files image link in Override Image URL.
- **Image QC:** **only ad blocks with 1 image get a PDF image.** Multi-image / BOGO deals → "Do Not Use PDF Images" (select the cutout). Meal deals can stay cutouts.

## Post-processing / FQC (owned by DOC)

- **File a FAB ticket** (clone the sample) for FLEX to complete Image QC, Coupon ID QC, and Spotchecks.
- **Promo ID QC:** Item Search → Promo ID IS blank → fill from the linking doc for the correct zone (Houston "H" / San Antonio "SA"); zone-specific.
- **Item Image QC:** filter cutouts/no images; pick clean PDFs but beware sale-story mismatch (e.g. BOGO PDF shows only one product). Text-only promos → Override Image URL.
- **Houston Digital Insert:** upload the held page, group as last page, **Process Internally**; add to Houston zones 60–86 (no box draw, static page); mark box draw complete; place in last page position via Pages > Layout; note "HEB insert added" in comments; no page category on the insert.
- **Categories:** 2 categories per page except page 1.
- **Flyer Review type: Medium.**

---
*Source: H-E-B OneGuide (Google Doc `1DQuZWM8aatVpLrz7_LFAlKz2pX4G3ziySzDR_AYuQ84`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Haggen — Processing Guide

> **Source:** Haggen OneGuide (Google Doc `1V7azqnU10YBCHuP_pSpQobjYTdcYb_G9xJ5naXMkTDY`), updated Mar 25, 2026. Contacts/credentials omitted.

Albertsons-family banner.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | haggen.com |
| Flyer type(s) & cadence | Weekly Flyer (6071) + Monthly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday (2 weeks lead time).
- **Cadence:** Available From Wednesday / Valid Wednesday → Available/Valid To Tuesday.
- **No linking document** at setup (but Tag/QC references a Tag/QC-specific linking doc).

## Upload & setup (owned by FLEX)

- Codesheet = **"Imposition.xlsx"** → open in Google Sheets. Delete everything except PZ, pages, stores (like a generic codesheet). Rename headers to: `pricing zone`, `stores`, `Page 1`, `Page 2`, … until all pages have headers. Download as CSV.
- Upload — Name = anything, **config `generic`**, base path = full path where files are (e.g. `/2025/072325`), **toggles: 2nd and last unchecked.**
- Setup QC: standard 4 thumbnails; **external run name = "Weekly Flyer".**

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** box each item; box sale story with multi-items. **Include retailer logo, sign-up page, social media**; exclude coupons, packaged deals, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; linking doc Tag/QC-specific):** include brand, Name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.

## Post-processing / FQC (owned by DOC)

- **Offer ID / Digital Coupon tagging:** check the Albertsons FTP for an "Offer ID" xls (search "Haggen", e.g. `010225_Haggen_OfferIDs.xlsx`). If present, download; if none for the dates, skip.
  - Remove "-D" from the **OMS Offer ID** column.
  - Use Item Search (keyword from "Bold Headline" column as name) and tag custom fields:
    - **Just For U (No Barcode):** Y (same for all items).
    - **Digital Coupon URL:** `https://www.haggen.com/foru/coupons-deals.html?event=Weekly%20Ad%20Coupons` (same for all items).
    - **Offer ID:** e.g. `91223945` (from OMS Offer ID with "-D" removed).
- External run name = "Weekly Flyer"; standard 4 thumbnails; **remove categories from all pages.**
- If an Offer ID doc was available, Item Search: Just for you (no barcode) IS NOT / item type Item; Digital coupon URL IS blank; Category contains coupon.
- **Flyer Review type: Lite.**

---
*Source: Haggen OneGuide (Google Doc `1V7azqnU10YBCHuP_pSpQobjYTdcYb_G9xJ5naXMkTDY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Handyman Hardware — Processing Guide

> **Source:** Handyman Hardware OneGuide (Google Doc `1RvPZwjs2T9Hx4urrrOdcEqG6ADP1Vkhy5Jt7Vq2mHZg`), updated Apr 16, 2026. Contacts/credentials omitted.

Longtail account, fully vendor-owned. Short guide — much of the OneGuide is the unfilled template.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channel(s) | (none listed) |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1, weekly |
| Processing | Auto-stack; no coupons; no Feedel; no linking document |

## Files & schedule

- **Files arrive:** Monday.
- **Cadence:** Available From Friday / Valid From Friday → Available/Valid To Thursday. No preview date.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages > Edit. Select all pages from the SFTP menu — folder named by the flyer's valid date; **always use the lower-case folder, not the Upper Case one.** Confirm & Upload, then "Auto-Group", Save & Complete.
- **Pricing zone:** create one PZ called "Base", add all stores, Save & Complete.
- **Setup QC:** confirm all pages uploaded — the only file that should remain in the SFTP is the multi-page PDF (Upper Case name, not ending in `P####`); flag missed pages to the FT team. Confirm valid dates vs page 1; 4 standard thumbnails; **Geography: 0 changes to stores/FSAs — flag 100% of discrepancies to the FT team**; available on all platforms.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include image (**always select a clean PDF if available**), brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**

## FQC (owned by Vendor)

- Confirm valid dates vs PDF; available everywhere; thumbnails include retailer logo; all boxed/tagged; previews clickable; geography consistent with last week (**flag 100% of discrepancies to FT Ops — non-blocking**).
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Handyman Hardware OneGuide (Google Doc `1RvPZwjs2T9Hx4urrrOdcEqG6ADP1Vkhy5Jt7Vq2mHZg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Hannaford — Processing Guide

> **Source:** Hannaford OneGuide (Google Doc `1G2LxIcwfE6r-QLu1t54b6Bce_4cEYJCwHXRUZZfvhOE`), updated May 7, 2026. Contacts/credentials omitted.

Ahold Delhaize / Royal Ahold banner. **High-risk account** — pixel settings, Ad Block IDs, and a Hosted/Flipp clone all have hard rules.

## Account at a glance

| | |
|---|---|
| Account tier | Core |
| Availability | **Two flyers:** one Hosted-only (original) + one clone available on Flipp/Distro |
| Slack channel(s) | `#3fl-royal-ahold`, `ahold-delhaize`, `ahold-ops` |
| Hosted URL | hannaford.com/savings/weekly-ad/print-view |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; Flex (**3FL**); no coupons; **Feedel/Strategic Ops: YES** |
| Resources | AEM Portal (all files except inserts), Royal Ahold Flex Tracker, Insert Tracker, 3FL Task Instructions |

## Files & schedule

- **Files arrive:** Thursday evening in the **AEM Portal** (FS-member access only); DOC drops them into the Hannaford **SFTP**.
- **Cadence:** Available From Friday / Valid From Saturday; goes **live Friday**, valid Saturday. Preview Friday.
- **Inserts** are dropped in the SFTP almost daily ahead of their week; **triggered on Sunday** when the flyer becomes valid.

## Upload & setup (owned by DOC)

**⚠️ #1 RISK — set the flyer height to 4096 pixels BEFORE any pages enter the page pool or any tile-gen/system task runs, on BOTH the Hosted shell and the Clone.** Pixels cannot be applied afterward — doing so risks breaking the flyer and the clone. If forgotten, make new flyer runs and notify BD.

Three files (all `.txt`, import into Google Sheets rather than open):
- **Locations** = stores codesheet · **Manifest** = pagination codesheet · **Items** = vendor tagging attachment.
- **Upload Manifest first:** Name `Manifest`, **config `food_lion`**, base dir = weekly PDF path, all toggles except the first two, save & **process first** (wait for green).
- **Upload Locations second:** Name `Locations`, **config `food_lion_stores`**, base dir = **`/`**, only 1st and 4th toggle, save & process.

**Items linking document setup (critical):** delete headings, keep Page Number, Item Description/Copy Headline, Overline/Copy Body, Primary UPC, Zone, Date Start. Change Date Start to `yyyymmdd`, then in a new **Ad Block ID** column: `=CONCATENATE(F2,"",E2)` → format `20220914FP24`. Highlight Ad Block ID yellow, Overline pink, move Page Number to column A, save as XLS, attach to all vendors with the note "tag ALL items that have an Ad Module Code — no item should be missed."

- **Setup QC:** dates on page 1 bottom-left; linking doc attached to all vendors; **external run names — "Hannaford Week # Flyer" (Hosted) and "Hannaford Week # Flipp" (Flipp App)**; 4 standard thumbnails drawn across **page 1 only**; add flyer run ID to the Royal Ahold Tracker so 3FL tasks can run before go-live.

### ⚠️ Common errors / risk items

- **Flyer name "Week #" must match the Items document number exactly** (e.g. SFTP `HNBItemsWK01_05_10.txt` → shell must be "Week 01", not "Week 1") or the UPC custom action breaks.
- The week's **Items txt must be in the SFTP** or the SKU auto-populate custom action won't work.
- **Ad Block IDs** must follow `YEARMONTHDAYPAGELETTERNUMBER` (e.g. `20240414FP20`), no extra spaces/characters — they power "related items" on Hosted. If the format looks different, **stop processing and flag immediately.**
- **Style Guide rules** can only run AFTER 3FL tasks (UPC auto-tag + SKU QC) and **only ONCE**. If the UPC custom action finishes with 0 SKUs updated, escalate to engineers as CLSD.
- **Clone risk:** don't clone unless pixels are 4096 on both shells and all processing is complete on the original; don't clone until after Style Guide rules. Tracking codes carry over. Toggles must differ (Hosted-only vs hidden-on-Hosted) or the retailer sees two available flyers in their iFrame.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** **include retailer logo, sign-up page, social media, special weblinks**; exclude coupons, packaged deals. Box each unique price; plated items — box the text/price, text-box the photo; "Or" second item = one box; digital coupon tagged as **Postfix**, not as a coupon. Don't box banners/social icons.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Do NOT enter SKU** (populated by the custom action in FQC).
  - **Brand field = "Hannaford"** for Hannaford own-brand items.
  - **Custom fields:** Ad Block ID (from the yellow column of the Items doc, per page/description/overline/UPC); Line Item = Y when no clean PDF; Sales Tag = Y when a SALE badge is on the PDF.
  - **Categories:** Adult Beverages only for alcohol/spirits, not regular beverages.
- **Image QC:** 1 image in box → select it only if a clean PDF (white bg, not cut off), else "Do not Use PDF Images" + Line Item = Y. Multiple images → first item listed (left-to-right); grey-background items → use the cutout.

## Post-processing / FQC

**3FL tasks (owned by Vendor):** Item Image QC (clean PDFs, left-to-right order); **SKU QC** — run custom action **"Hannaford Upc Auto Tagging"** (input flyer run, Run Action, wait for completion email), then Item Search SKU IS blank and fill from the SFTP Items txt (**use the longer of the two UPCs**); **Ad Block ID QC** — Item Search Ad Block ID IS blank, fill from linking doc; **URL Link QC** — Item Search URL IS blank, multi-edit the TTM print-view URL (`?utm_source=flipp-app…`).

**DOC:** run **Style Guide rules ONCE** (strips leading 0s to 13-digit SKUs for the Hosted API); build **insert triggers** (box/tag inserts as LINK per the Insert Tracker, positioned as a Sunday trigger — repeat for the clone; create an Optics Afterhours ticket); **clone** the run to the Flipp App shell (separate external run names, separate insert triggers, Optics ticket with fadmin name + URL, lead + BD tagged). Tracking codes already applied at flyer level.

- **FQC checklist:** geography; 4 thumbnails on page 1 only; toggles (Hosted-only vs hidden-on-Hosted); external run names; no clean images left; all Ad Block IDs + SKUs tagged; insert triggers in place; vertical scroll works; insert direct links land correctly; tracking codes carried over; Optics ticket created with Afterhours + lead review.
- **Live dates:** if "FLIPP" is in the name it's hidden on Hosted (don't flag); if not, it should show on Hosted (flag if missing). Verify Ad Block ID "related items" function on Hosted.
- **Flyer sorting:** newest preview must not be first on the retailer site (automated).
- **Flyer Review type: Lite.**

---
*Source: Hannaford OneGuide (Google Doc `1G2LxIcwfE6r-QLu1t54b6Bce_4cEYJCwHXRUZZfvhOE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Hardwood Design Centre — Processing Guide

> **Source:** Hardwood Giant & Hardwood Design Centre OneGuide (Google Doc `1x0ZLZ22TCdh2TYHKoLiqrdYW_ZE3Q9MGANdmjgh1z3U`), updated May 29, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Hardwood Design Centre: 11926 Flyer · Hardwood Giant: 11928 Flyer; Ad Hoc |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support, Flyer Review); no OS; no coupons; no Strategic Ops / Feedel |

> Note: shared account — Hardwood Giant (5914) & Hardwood Design Centre (5933).

## Files & schedule

- **Files received:** Ad Hoc (all available/valid dates ad hoc). Pages may need to be added to the SFTP by the processor if the client sends files over email.
- No linking document.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu (or upload from email if needed) → Confirm & Upload → Auto-Group (or manually enter grouping numbers) → ensure language is English → Save & Confirm.
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC
- Confirm all pages uploaded correctly (Pricing Zone → Items View). **RISK:** if uploading from SFTP, confirm no un-uploaded pages remain.
- Confirm flyer dates (usually first or last page).
- Thumbnails: 4 Standard.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a box.
- If uploading from SFTP, confirm no pages remain un-uploaded.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks. No linking doc.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.
- Standard processing: Name usually based on the page title (e.g. "Laminate Floors"), Price, and any other text on the page applying to all products. Tag exactly as shown.

### Image QC
- PDF preferred if clean; otherwise cutouts are accepted.

## Post-processing / FQC (owned by DOC)
- **Pre-FQC:** confirm dates per PDF; availability toggles correct; thumbnails include retailer logo. Standard checks — all items boxed/tagged; spotchecks complete (20% of pricing zones); previews published & clickable; sessions completed; geography correct.
- Complete FQC checklist.
- **Flyer Review type: Lite** (owned by DOL) — checks: flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Hardwood Giant & Hardwood Design Centre OneGuide (Google Doc `1x0ZLZ22TCdh2TYHKoLiqrdYW_ZE3Q9MGANdmjgh1z3U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Harris Teeter (+ Delivery) — Processing Guide

> **Source:** Harris Teeter (+ Delivery) OneGuide (Google Doc `1RX_HDfp-OOrjBNqrHawPWLkho0Hu_tVuQBbO_yiZUaI`), updated Dec 17, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` |
| Flyer types | **Weekly** · **Monthly** (and **Harris Teeter Delivery** as a separate banner) |
| Processing | Auto-stack; Flex (Flyer Review); FTE/Vendor-owned setup & FQC; Feedel/data services — **yes**; no coupons |
| Key resources | HT upload instructions, HT FQC + Risk Items notes, Kroger/HT Flex Team Tracker, HT FSA list |

## Files & schedule

- **When files arrive:** Thursday (usually in the FTP Wed afternoon, latest Friday). Files best processed over the weekend.
- **Publication cadence:** Available From Wednesday → To Wednesday; Valid From Tuesday → To Tuesday.
- **File naming:** file names include the last day the flyer runs (e.g. `fc02 harristeeter_delivery w.e. 09.19`). **`FC02` = Harris Teeter Delivery**; anything before FC02 refers to Harris Teeter only.
- The retailer email includes the page order for inserts/ads and any links — you don't need to wait for it to start uploading pages, but it drives insert placement.

## Upload & setup

### Weekly (Vendor-owned) — codesheet + manual inserts

- From the FTP, download the pagination codesheet (`WEEK mm.dd.yyyy BreakdownSTORE.xls`) and the store master (`HT Flip_Version_Store_Master.xlsx`) for the correct week.
- **Codesheet manipulation:** remove inserts fadmin can't read (BGA, BGB, Outerbank, PO1/PO2, FS1/FS2, e-fly/digital pages) — those get uploaded manually later; keep 1 blank row between pages; find `_[6_6]` and replace with blank; save as CSV; verify page-number order.
- **Store master:** open (auto-opens to most recent tab; confirm the tab date matches the FTP path); remove dashes between letter and number (E-10 → E10); download the tab as CSV.
- **Upload store master** using the base path only (codesheet turns green when processed). **Then upload the pagination codesheet** using the base path (an Outerbank-pages warning is normal — force process again; it stays yellow).
- Pricing zones: expect 6 pages for all PZs and 1 page for the OBX zone. **Manually upload the removed pages** (BGA, BGB, etc.).
- **Build inserts into the PZ** using the original pagination codesheet + the retailer's email order (screenshot lives in the Flex Kroger Tracker HT tab). **BGA is always position #2, BGB always position #3**; e-fly pages go at the very end in breakdown order; the program/ad page goes between the last numbered page (usually page 6) and the e-fly pages. Insert names in the email refer to the file-named pages ("Page 4"/"Page 5"), not stack positions. OBX zone has only 2 pages (page 1 + an OBX page).
- **Attach linking document:** download the week's HT Linking Document as `.xls` (name must match the flyer week) and **mass-attach to ALL vendor tasks/tracks**; manually upload the week's insert files.
- **Weekly Setup QC:** Standard 4 thumbnails; **no external run name**; no theme; dates Wed–Tues; sessions complete; linking doc + inserts added.

### Monthly (FTE-owned)

- Download from the retailer email, drop into FTP, manual upload; Flyer Creation → start; 1 PZ "Base"; add all stores; verify dates.
- **Monthly Setup QC:** Standard 4 thumbnails; **external run name: `Harris Teeter Discovery`**; no theme; dates Wed–Tues; sessions complete.

### Harris Teeter Delivery (custom actions)

- 4 pricing zones — **REG Virtual, REG Physical, NOVA Virtual (B&W pages), NOVA Physical (B&W pages)**. REG Virtual and NOVA Virtual share the same assigned store (correct).
- Assign stores via the `generic_stores` codesheet; assign **FSAs** to all four runs via the `Assign FSAs from CSV` custom action (paste each PZ ID into the template, export tabs as CSV, upload per banner).
- **FSA Swap:** if an "overlapping FSA" error appears, assign `20147` to Virtual Stores (remove-FSAs custom action) and remove `20147` from the Physical PZ.

## ⚠️ Common errors / risk items (retailer-specific)

- **Image risk item (all banners):** PDF images for **seafood and some meats are typically lifestyle or have a strange shadow** — change these to **cutouts**.
- **Banner boxing:** **do NOT box banners in Harris Teeter**; **DO box the HT Plus and HT Delivery banners in Harris Teeter Delivery.**
- **Name and Sale Story fields are CASE SENSITIVE** — match the flyer's capitalization exactly.
- Remove inserts before codesheet upload (fadmin can't read them); watch for differently named files vs the FTP.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot ON.** Linking document required. Box all items separately (text boxes when needed) — any item with a price or sale story gets a box. **Include** retailer logo, sign-up page, social media, special weblinks; **exclude** coupons.
- **Tag / Tag QC — Low complexity. Auto-tag OFF, PDF Image Auto-Selection ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand **not** required (meat/produce often have none) — enter if present.
- **Image QC:** prefer PDF image with white background; select cutout if the PDF has a black background or is lifestyle. **No lifestyle images; no black backgrounds.**

### Final QC highlights

- Weekly: mark autostack spotcheck complete; page categories on all pages except Page 1; verify HT links/tags; **merge BGA and BGB pages** (Overview → pricing zones → storefront spotcheck); banner tagging for HT Delivery + Weekly per the Kroger Flex Team Tracker tab; **sort the weekly flyer above the monthly**.
- Delivery/Monthly: confirm dates (PDF/email); cross-reference the HT tab to confirm banner links; thumbnails include retailer logo; standard checks; sort monthly **after** the weekly.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite** — flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: Harris Teeter (+ Delivery) OneGuide (Google Doc `1RX_HDfp-OOrjBNqrHawPWLkho0Hu_tVuQBbO_yiZUaI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Hart Stores — Processing Guide

> **Source:** Hart Stores OneGuide (Google Doc `1Vzod6nw2Jp_HafBOnuqM1VCPieAOCTuacFmzmedIZkw`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#hart`, `#flex-processingsupport` |
| Hosted URL | hartstores.com/pages/flyers |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing/FQC; OS (upload); no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Friday.
- **Cadence:** Available From Wednesday, Valid From Tuesday; Available To Wednesday, Valid To Tuesday.
- No preview date, no linking document.
- **Custom action:** "Set Cut-out Images" custom action at FQC.

## Upload & setup

- Regular **manual upload**. Two languages: **English (Ontario pages)** and **French (Quebec pages)**.
- **If region is not specified, use the same page for both languages** — this requires uploading the pages twice and assigning each set to an EN and FR pricing zone.
- Region-specific pages are typically the last page. Assign language to pages (English/French).

### Pricing zones
- Create **English and French** pricing zones. If there are separate ON and QB regions, make an EN and FR zone for each: **ON EN, ON FR, QB EN, QB FR** (language + which last page — ON or QB).
- **Add all stores to each pricing zone.** As of Nov 2024 there should be **135 stores per PZ.**
- Double-check dates (left side of the first page) match the flyer run dates.

### Setup QC
- No theme, no external run name; Standard 4 thumbnails; complete setup QC checklist.
- Add the Flyer ID to the VAST tracker for FQC.

## ⚠️ Common errors / risk items
- **If region isn't specified, upload pages twice** (once per language) so both EN and FR zones have them.
- **Item counts must match across all versions** — FR and EN for both Quebec and Ontario should all have the same item count. If counts differ, fix box/tag (often two SKUs were boxed together when they should be separate).
- Ensure **135 stores per PZ**.
- **Image QC: select cutouts only** (not PDF images).

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Draw a box whenever there's a unique price. Box "Your Choice" items separately.
- **Mattresses:** box smallest size (usually twin) with the main photo; box other sizes separately. **Pillows:** box sizes separately.
- If items share a price but have different SKUs, box each separately; if multiple items share a SKU, box together.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude:** URLs. Linking doc required (tag-specific).
- **Name/Brand:** name in larger (sometimes bold) text; if branded, include brand in both brand and name fields; include size in name for mattresses/pillows.
- **SKU:** enter in both the SKU field and below the description.
- **Valid dates:** items typically valid for the full flyer (no item dates needed); enter item dates only if labelled differently.

### Image QC
- **Select cutouts only.**

## Post-processing / FQC (owned by Flex)
- Mark Autostack Spotcheck complete.
- Edit Details: Available/Valid dates match the flyer (page 1); available everywhere; no external run name; no theme.
- Legibility heights: **55/40.** Thumbnails: Standard 4.
- Pages: ensure every SKU has its own box and tag.
- Pricing Zones: same item count across all versions (fix box/tag if not); all stores added (135/PZ); check vertical preview & full screen (items clickable, boxes appear).
- Sessions: none errored/needing rerun; mark items In-Store Only.
- Geography: no stores/FSAs removed.
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Hart Stores OneGuide (Google Doc `1Vzod6nw2Jp_HafBOnuqM1VCPieAOCTuacFmzmedIZkw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Harveys Supermarket — Processing Guide

> **Source:** Harveys Supermarket OneGuide (Google Doc `1qZ4fwB1tceHtTG6QiA2SLAunvHX5G8cHvpSy05KHhpw`), updated Dec 8, 2025. Contacts/credentials omitted.

SEG (Southeastern Grocers) banner. Rules are largely shared with Winn-Dixie / Fresco y Más.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#segrocers` |
| Hosted URL | harveyssupermarkets.com |
| Flyer type(s) | **Weekly Circular** (ID 3070) · **In-Store Flyer / ISPO** bi-weekly (ID 3292) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday, via **FTP**.
- **Cadence:** Available From Mon / Valid From Tue → Available To Mon / Valid To Tue. Preview: Tuesday.
- Files delivered by external ops via FTP (credentials in the OneGuide — not stored here).

## Upload & setup (owned by FLEX)

Search the FTP by `.xlsx`. **Two codesheets per run:**
1. **"Versions" / "Version List"** = store information.
2. **"Manifest"** = pricing zone + page order info (also outlines preview and valid dates).

- Base path patterns: weekly = `/MMDD+HRV`; bi-weekly ISPO = folder with `ISPO` in the name.
- **Version list first, manifest second.**
  - Open Version List → "Harveys Base AD ALL" tab. Change the "Store"/"Store #" header to **"Stores"** (critical for fadmin to read the codesheet). Save tab as CSV.
  - Upload — Name `Stores`, **config `seg_stores`**, base path per week, **toggles: ALL except 2**, Save codesheet. **DO NOT RUN this codesheet.**
  - Manifest: no manipulation, save as CSV. Upload — Name `pages`, **config `seg`**, base path per week, **toggles: ALL except 2 and 7**, Save. **Preview Start Date = Available From.** Run only the manifest codesheet.

### ⚠️ Common errors / risk items

- **"Pages not found in FTP"** → check FTP for a spelling error / similar name, fix the manifest, re-upload and re-run.
- **"Page already uploaded"** → check if the page is an insert with valid dates beyond the flyer; if so, the error can be ignored.
- If the error persists after investigating, reach out to the processor — may require new files from the retailer.
- **Setup QC:** if uploading from SFTP, confirm no un-uploaded pages remain. Missing stores in Geo → search the Version List for the store code; if not present, the flyer shouldn't get that store; if present, add it manually. Write "Geo is good" in the comment box once confirmed.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** include coupons and packaged deals; exclude retailer logo, sign-up page, social media, special weblinks. One price for all items = ONE BOX (BOGO / "Pick 5 for 5"). Box vaccine banners. Watch box/image alignment.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON):** include Name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs — there is NO URL linking; do not box/tag any banners or pages with URLs.** Use LOWEST price in current price for two-price items.
- **Categories are critical** (retailer receives analytics) — use the section header; do NOT add two categories; flag rather than guess.
- **Image QC:** select CLEAN PDFs when available, else cutout.

## FQC / post-processing (FLEX)

- Tag unique valid dates where pages have them (1-/3-day sales).
- **Switch & Save pages must be boxed and tagged** (often skipped because they have sale stories, not prices) — can copy boxes from the same-week Harveys/Fresco y Más flyers.
- Legibility heights 35,25; no theme; available everywhere; standard thumbnails.
- **Flyer sorting:** weekly flyers first (by date, current then preview), ISPO/bi-weekly last.
- **Flyer Review type: Lite.**

---
*Source: Harveys Supermarket OneGuide (Google Doc `1qZ4fwB1tceHtTG6QiA2SLAunvHX5G8cHvpSy05KHhpw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Harvey's (Restaurant) — Processing Guide

> **Source:** Vendor Solutions (QSR) OneGuide (Google Doc `102O_Ia2_J5ULA6P7DFK-y7vpEozhkNeqIa_3X-w7tls`), updated Jan 27, 2025. Contacts/credentials omitted.

Harvey's is processed under the shared **QSR Vendor Solutions OneGuide** (same guide covers Subway, McDonald's, Pizza Pizza, Swiss Chalet, HelloFresh, Taco Bell, KFC). Content-specific instructions come from the BD post in Slack, not this guide.

## Account at a glance

| | |
|---|---|
| Account tier | n/a (QSR account) |
| Availability | Flipp only |
| Slack channel(s) | `#qsr-tacobell` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1: **Direct**, ad-hoc |
| Processing | Auto-stack (sometimes sliced) |
| Involvement | Flex/OS N/A; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files:** ad-hoc, delivered by BD via Slack (`#qsr-tacobell`) — should include regionalization instructions.
- **Preview date / linking document:** sometimes.
- **Process varies heavily by partner** — always refer to the BD post in the Slack channel for the content-specific instructions for the run you're working.

## Upload & setup

- If no regionalization instructions are provided but multiple regional PDF versions are supplied, **follow up before proceeding.**
- Manually upload all pages > Auto group.
- Create pricing zones and add all stores to pricing zones as appropriate.
- Attach any linking instructions provided by the retailer.

## ⚠️ Common errors / risk items

- **Do NOT tag any boxes as coupons**, regardless of creative layout or design.
- Multiple regional PDFs with no regionalization instruction → follow up before uploading.
- Any run-specific risk items will be in the BD message in `#qsr-tacobell`.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include Name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand = No. Valid dates = exclude.
- **Image QC:** not called out.

## FQC / flyer review

- Post-processing (FLEX): thumbnail QC; slice if BD requests; tracking codes if BD requests; check dates vs PDF; available everywhere; all stores added to PZs; all shoppable items boxed; pages in chronological order.
- **Flyer Review type: Lite** — use generic standards; any special risk items come from the BD message in `#qsr-tacobell`.

---
*Source: Harvey's (Restaurant) OneGuide (Google Doc `102O_Ia2_J5ULA6P7DFK-y7vpEozhkNeqIa_3X-w7tls`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Health First Network (buying group) — Processing Guide

> **Source:** Health First Network OneGuide (Google Doc `1dSCloBFD9dTObOhlccfwIKILDkTtMbDbyEq7G7mazpc`), updated Sep 17. Contacts/credentials omitted.

Buying group: one base flyer is processed then **cloned** out to many participant merchants.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only, **except** Gagne en Sante / Win in Health and The Peanut Mill (all platforms) |
| Slack channel(s) | `#healthfirstnetwork`, `#flex-buying-group-processing`, `#healthfirstnetwork-process` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Monthly |
| Processing | Auto-stack; Flex (unique shift type); no coupons; no Feedel |

- **Account note (2025):** system supports a max of 3 banners for linking; expansion needs more lead time and investment.
- **Custom action "Remove Stores"** — removes store 100 from all pricing zones, run as part of Setup QC.

## Files & schedule

- **Files arrive:** Monday (confirm with external ops ~17 days out). Assets land on **SFTP** (PDFs + XLSX codesheet, usually `FLIPP_MMYYYY.xlsx`); email sent on upload.
- **Cadence:** Available Wednesday / Valid Thursday. Timeline runs ~17 days out through post-processing.
- **Linking:** URLs processed only for **Win in Health / Gagne en Sante, Natural Focus, Naterro** (come post-processing).

## Upload & setup (owned by Processor)

- Import the XLSX into the **HFN Workbook**; run the numbered macros (1–5): clear formatting, format dates MM/DD/YYYY, rearrange columns, update headers, set "Store Set" = 100 for all rows, sort by launch date. Download tab as CSV.
- Confirm flyer dates from XLSX: earliest Start (MIN), latest End (MAX).
- Upload to flyer run — **config `health_first_network`**, PDF base dir = XLSX path.
  - **Toggles:** ✅ Store/Store Set Assignment, ❌ Region Assignment, ✅ Page Upload, ✅ Allow PZ creation, ✅ Use Page Pool, ✅ Tile Generate, ❌ Combine Zones.
- Run the codesheet.

### ⚠️ Common errors / risk items

- **"Files not named XX"** → PDFs misnamed vs codesheet; fix in the codesheet and re-run. Flag to retailer if high volume.
- Files present but not in the spreadsheet (or vice-versa) → always reach out to clarify.
- **Setup QC:** check created PZ count vs codesheet; run **Remove Stores** custom action (PZ ID = "all", stores = 100) and confirm 0 stores assigned; check SFTP for `000#.pdf` naming; confirm staggered dates set; spot-check pages aren't cut off.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Multiple images + multiple prices = box each; multiple images + one price = single box.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include Name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.** For uniquely-priced multi-items, include product volume/unit in the name.

## Post-processing

**Processor** completes FQC on the **"processing only"** base flyer (thumbnails, no stores assigned, PZs staggered, hidden everywhere, no theme, Tagged/Vendor QC counts match).

**FLEX** then **clones** the base flyer to active participants:
- Deselect "Clone To Health First Network" for each participant; clone up to 10 at a time (may time out); Copy Tracking Codes/URLs = No; clones take 15–30 min.
- Participant FQC: add stores to each merchant's PZ (Win in Health / Gagne en Sante = same stores); check staggered dates match PDFs (Available From = 1 day before Valid From, **except Ki Nature = 2 days**); QC 3 thumbnails; remove "processing only" from internal run name; availability Flipp + Distribution only (except the 3 all-platform banners).
- **NEW / RISK: Do NOT rerun sessions to clear red FQC warnings** — type **"CLONE"** into the field for each warning to turn it green and proceed.

Also documented: ClickUp workspace setup for Flex tasks, Product URL tagging (send/import to 3 clients), and Flipp Web Direct Links.

- **Flyer Review type: Lite.**

---
*Source: Health First Network OneGuide (Google Doc `1dSCloBFD9dTObOhlccfwIKILDkTtMbDbyEq7G7mazpc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Health Mart Pharmacy — Processing Guide

> **Source:** Health Mart Pharmacy OneGuide (Google Doc `1VvNZItJ8cRufjaGNlWfUR0FHqGBhdyL7NlRf5aUHHXw`), updated Feb 5, 2026. Contacts/credentials omitted.

McKesson account. Ad-hoc monthly-style publication.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | None |
| Hosted URL | fosterandthrive.com |
| Flyer type(s) & cadence | Flyer Type 1, **ad hoc** (Available/Valid 1st→last of month) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); DOC final QC; no coupons; no Feedel |

## Files & schedule

- **Files:** ad hoc. Sometimes sent via email — processor may need to add pages to the SFTP.
- **Linking document: YES — add to ALL tasks.** Contains URLs for the Foster & Thrive products; the direct link for Page 2 is sent via email and added during FQC.

## Upload & setup (owned by FLEX)

- **Manual upload:** Pages tab → Edit. From email, download and upload all pages (Page 2 often sent separately or via a WeTransfer link for Pages 1 & 3). From SFTP, select all pages → Confirm & Upload.
- Auto-Group or manually enter grouping numbers; ensure correct language. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create Base PZ, select applicable pages, add all stores.
- **Linking doc:** download the XLSX with "Links" + current month from the SFTP; add to all vendor tasks.
- **Setup QC:** confirm all pages uploaded (PZ tab → Items View; check SFTP for un-uploaded pages); confirm flyer dates (usually first/last page); 4 standard thumbnails; preview dates set.

### ⚠️ Common errors / risk items

- **Brand name** should only be tagged once — e.g. "Taylor Farms" goes in Name, not Brand.
- **Sale story order:** percentage (%) comes before the dollar amount saved ($).
- **Item images:** all should be the PDF and reflect in the flyer preview. If not, **re-run page stitching** until they show; wait 15–20 min before re-checking.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both box/tag):** box each item with a price; exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; linking doc used for both):** include brand, Name (include brand in Name field too), pre/postfix, valid dates, description (all detail below the name), price, sale story, categories, disclaimer (at bottom of product image), original price. **Exclude SKU and URLs.** Include page categories.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## FQC / go-live (owned by DOC)

- **Add direct link to Page 2:** `https://www.fosterandthrive.com/`.
- Confirm dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite.**
- **Page swaps:** standard/baseline process.

---
*Source: Health Mart Pharmacy OneGuide (Google Doc `1VvNZItJ8cRufjaGNlWfUR0FHqGBhdyL7NlRf5aUHHXw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Healthy Planet — Processing Guide

> **Source:** Healthy Planet OneGuide (Google Doc `12sPumZY6kN6-Xxqdk0xrutWaTL07N6kqsq-ResiqE2A`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#healthyplanet` |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Monthly (6717); also Produce and Sports flyers |
| Processing | Auto-stack; Flex (Flyer Review); OS setup; no coupons; **Feedel/Strategic Ops: YES** |

## Files & schedule

- **Files arrive:** Monday, via **email** (flyer + links). ~18 pages, all English.
- **Cadence:** Available Tuesday / Valid Wednesday. Confirm dates in email and ask if they want a preview.
- **Linking doc:** attach to all vendor tasks (**Monthly flyer only**; **Produce and Sports flyers do NOT get linking docs**).

## Upload & setup (owned by FLEX)

- Manual upload (~18 pages) from email. Add all stores.
- **Thumbnails:** 1065×600, Stock Premium, Storefront Carousel Premium, Storefront Carousel Organic.
- **Edit details:** no theme; available everywhere; valid = flyer dates; confirm preview via email.
- Setup QC: should be no warnings.

### ⚠️ Common errors / risk items

- **Box Draw:** auto-box draw titles may not match the boxed item (top text left out of box). Auto-tag is also on, so may need to readjust and re-tag. Ensure the **entire product name** is captured in the box.
- **URLs:** tend to be incorrect/missed — create a Flex OT ticket to check all items without a URL.
- **Produce page change** mid-flyer (sent ~1 week ahead): run it through processing, create a trigger + OPTICS ticket.
- **Produce flyer no longer active** → hide everywhere and add `[NGL]` to the flyer name.
- **Late/Vanilla files:** turn on Vanilla immediately after upload (30 sec–1 min window): Overview > Special Actions > Make Vanilla > Click all > Submit. Then hide in Flipp + Distribution, assign vendors, attach linking doc, move Available From to today, set vendor priority high + file OS Urgent ticket, do FQC (add `/final_qc` to link if inactive), force mark complete, create JIRA reminder to make interactive during FQC, flag DOL.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc used for both):** box each product block with a price and/or sale story — capture the entire product name. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — TAG LITE retailer (Auto-tag OFF; PDF image auto-select ON):** **DO NOT tag Name, Brand, Description, SKU, Sale Story** (but if Name is missing, tag the name). Include Name, pre/postfix, valid dates, price, categories, disclaimer, original price. **URLs: include (Main Flyer only).** Add **keyword** (first word before the comma) to item description. Every item requires a category.
- **Image QC:** use **cutout images**.

## Post-processing / FQC (owned by DOC)

- **Check URLs:** open the linking doc on vendor tasks, review every link per page, add comment "All links checked."
- Spotchecks if required; standard 4 thumbnails; geo/PZs/pages tagged; FQC checklist.
- **Flyer sorting:** Monthly, then Produce, then Sports Nutrition.
- **Live-dates note:** items sometimes boxed/tagged with the wrong (lower) title → flag to DOC to action.
- **Flyer Review type: Lite.**

---
*Source: Healthy Planet OneGuide (Google Doc `12sPumZY6kN6-Xxqdk0xrutWaTL07N6kqsq-ResiqE2A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Heinen's Fine Food — Processing Guide

> **Source:** Heinen's Fine Foods OneGuide (Google Doc `1jzDekSjUedeXwa8KJ_4-QP1vqF47Fe-lDagPKwobcWE`), updated Feb 19, 2026. Contacts/credentials omitted.

Two-market flyer: **Cleveland (HE)** and **Chicago (CH)** run as two pricing zones.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | Flipp only |
| Slack channel(s) | `#heinens` |
| Hosted URL | heinens.com |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday (retailer emails when files are dropped — respond confirming receipt; update Vendor Setup Tracker / VAST with FlyerID).
- **Cadence:** Available From **Tuesday 12:00 PM** / Valid Wednesday → Available/Valid To Tuesday. 1-week run. No preview date. Hidden on Hosted. No linking document.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages > Edit > select page(s) from FTP > **do not auto-group**. Files are labelled **HE (Cleveland)** and **CH (Chicago)** — two of each page number. Manually set grouping by file name; all English; Save & Complete.
- **Pricing zones:** create two — **HE** (add all HE pages, Cleveland) and **CH** (add all CH pages, Chicago). Add "HE" store set to HE PZ, "CHI" store set to CH PZ.
- **Setup QC:** Available From Tuesday 12:00 PM; Valid From Wednesday; internal run name "Week ##"; no external run name; no theme; standard 4 thumbnails (1065×600 ×2pg, Stock premium ×1, Storefront carousel premium ×2, organic ×1); confirm sessions ran and FSAs generated.

### ⚠️ Common errors / risk items

- **Category mis-tag (RISK):** items tagged as Dairy when they're in the Deli section, etc. — categories are location-based on the page.
- **Auto-box draw errors on certain pages** → pages need re-upload. Fix: set the run as **NGL** (hide all availability toggles, reassign all vendor tasks to Flipp), make a new flyer run, and do a manual upload of the affected pages **with CropBox**.
- **Red sessions in Setup QC** → find **Page Tile Generation** in the WES pipeline, Rerun Task, wait a few minutes; escalate if it persists.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include retailer logo**; exclude coupons, packaged deals, sign-up page, social media, special weblinks. Do not box QR codes or the social/website URL.
- **Tag / Tag QC (Low; Auto-tag ON):** include Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and item URLs.** Brand tagged only if a single brand (leave empty if multiple). BOGO with no price → "BOGO" in Prefix, other sale story in Sale Story. **Coupons: Display Type = Coupon, draw barcode for all three barcodes.**
  - **Categories (location-based):** use the page section header. Page 3s = all Grocery except bottom-right = Wellness. Cheese in "Prepared Foods" = "Artisan Cheese"; "Grab 'n Go"/"Dinner Solutions" = "Prepared Foods".
  - **URLs:** no item URLs; add URL to the retailer **logo** only (Display Type: Link → `https://www.heinens.com/`).
- **Image QC:** always select PDF if available (lifestyle image OK); if PDF cut off, use Cutout; multi-items use 1 image.

## Post-processing / FQC (owned by Vendor)

- Item Category QC and Item Image QC (Generate All, usually <100 items).
- **Link FQC:** confirm page 1 logo linked to `https://www.heinens.com/`, verify URL via Sessions, confirm in preview.
- Spotcheck; mark Auto-Stack completed; confirm vendor tasks; dates/thumbnails; geography stable week-over-week; **OK to ignore "Other Warnings" / stores-not-assigned.**
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Heinen's Fine Foods OneGuide (Google Doc `1jzDekSjUedeXwa8KJ_4-QP1vqF47Fe-lDagPKwobcWE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Hen House — Processing Guide

> **Source:** Hen House OneGuide (Google Doc `1V1atTItytQDp5FYsfF9Jp4tSzzresto0KmPmchXcsl4`), updated Feb 13, 2025. Contacts/credentials omitted.

Balls Foods banner.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#1plat-henhouse` |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Weekly Ad (12051) |
| Processing | Auto-stack; DOC-owned pipeline; no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Wednesday.
- **Cadence:** Available From Wednesday → Available To Tuesday (Valid To Wednesday / Valid From Tuesday per doc). No linking document.

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages > Edit > select all pages from the SFTP menu > Confirm & Upload. Confirm correct pages by referencing dates; page order = the number in the file name. **HHWeb pages go LAST in the publication.**
- Manually add grouping numbers; ensure correct language. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create Base PZ, select applicable pages, add all stores.
- **Setup QC:** confirm all pages uploaded (PZ tab → Items View; no un-uploaded SFTP pages); confirm flyer dates (bottom of page 1); 4 standard thumbnails; preview dates set.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; linking doc Tag/QC-specific):** include brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## Post-processing / FQC (owned by DOC)

- **Pre-Final QC:** dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions completed; geography correct.
- FQC checklist.
- **Flyer Review type: Lite** (owned by DOL) — dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: Hen House OneGuide (Google Doc `1V1atTItytQDp5FYsfF9Jp4tSzzresto0KmPmchXcsl4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Henry's — Processing Guide

> **Source:** Henry's OneGuide (Google Doc `1uSnDdVGj3tHQ-A8ek8LKGsE2WdXQSip5hmS2j9a6m5o`), Vendor Solutions guide. Contacts/credentials omitted.

Camera/photography retailer. Ad-hoc weekly ad with a **linking document** that drives both boxing and tagging.

## Account at a glance

| | |
|---|---|
| Account tier | (Vendor Solutions account) |
| Availability | All platforms |
| Slack channel(s) | `@henrys` |
| Hosted URL | henrys.com |
| Flyer type(s) & cadence | Weekly Ad (9472), ad-hoc |
| Processing | Auto-stack; **Flex not involved**; OS completes standard tasks; no coupons; no Feedel |

## Files & schedule

- **Files:** in the FTP, including the **linking document** (usually a `.csv`).
  - **RISK:** historically (2023) files/assets arrived via **email** instead — split the PDF with an online splitter or upload to the FTP yourself.
- **Cadence:** Available Thursday / Valid Friday.

## Upload & setup

1. Files in FTP incl. linking doc; choose **split PDF pages**.
2. One pricing zone, name = **base**; add all stores.
3. Download the linking document from the FTP, convert to `.xlsx`, attach.
   - **RISK:** linking doc may come via email — attach it.
4. Edit details: no consumer preview date; available everywhere; no theme (unless Black Friday / Christmas); **external run name = the flyer title on page 1.**
5. Standard 4 thumbnails; Setup QC checklist.

### ⚠️ Common errors / risk items

- **URL links:** ensure the correct link is associated with the tagged item.
- **2024 — all banners were missed**, so double-check banners are boxed/tagged.
- Use the linking doc **Product Name** column to know where boxes go and to verify item counts per page.

## QC specifics

- **Box Draw (Low; linking doc required):** **include** social media, sign-up page, special weblinks, retailer logo, packaged deals; exclude coupons. Box **every individual item** using the info on the flyer + linking doc. The **HENRYS.COM** callout should be boxed/tagged on **every page** it appears on.
- **Tag / Tag QC (Low; PDF image auto-select ON):** include brand, Name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, **URLs**.
  - Brand = bold print; Name = unbold capital print; current price = bold orange; sale story = capital bold orange.
  - **URLs:** provided in an Excel/text doc emailed to you; if not attached and high priority, search the webcode on `www.henrys.com`.
  - **Categories:** provided in an Excel; if unsure, visit the item's URL — the category is listed in orange on the website.
  - SKU as seen in flyer where applicable.
- **Image QC:** per item examples in the guide (e.g. Lenspen Cleaning Kit, T200BH Tripod). Multiple-product items also documented.

## FQC

1. Pages > page categories — **page 1 gets no category**; choose the most relevant category using best judgement.
2. **Linking doc check:** confirm all items in the linking doc are boxed/tagged with the correct links; cross-reference item count vs boxed/tagged count per page.
3. Check pages, pricing zone, vendor tasks, geography.
4. FQC checklist.

- **Page swaps:** baseline/standard process.
- **Flyer Review:** Henry's flyer review guide referenced.

---
*Source: Henry's OneGuide (Google Doc `1uSnDdVGj3tHQ-A8ek8LKGsE2WdXQSip5hmS2j9a6m5o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# HockeyStickMan — Processing Guide

> **Source:** HockeyStickMan OneGuide (Google Doc `1GzQig7rPMO79KLLFNPQTWFh6Rkhse0iZ7t2jThcUGuc`), updated Jun 5, 2026. Contacts/credentials omitted.

Longtail hockey-equipment retailer with a **linking document** driving both boxing and tagging.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms (**we do not power hosted**) |
| Slack channel(s) | `#1plat-hockeystickman` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1, weekly |
| Processing | Auto-stack; DOC-owned pipeline; no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday. Available From Tuesday → Available To Monday.
- **Linking document: Yes** — dropped in the FTP with the files.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages > Edit > select all pages from the SFTP (flyer date matches the PDF names) > Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure correct language. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create Base PZ, select applicable pages, add all stores.
- **Attach linking doc:** in the FTP search "XLS", find the file matching the flyer date, attach to all pipeline tasks.
- **Setup QC:** confirm all pages uploaded (PZ tab → Items View; no un-uploaded SFTP pages); confirm flyer dates (first/last page); 4 standard thumbnails; preview dates set.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both box/tag):** **include special weblinks**; exclude coupons, packaged deals, retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both):** include brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude SKU.
  - **⚠️ Linking-document CTA callout:** a CTA with **no item information, only a URL, MUST be tagged as LINK TYPE** (common error is not tagging it as Link).

## Post-processing / FQC (owned by DOC)

- **Pre-Final QC:** dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Links QC:** use "Items without URL" on the Overview page to address any items/CTAs missing a link.
- FQC checklist.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: HockeyStickMan OneGuide (Google Doc `1GzQig7rPMO79KLLFNPQTWFh6Rkhse0iZ7t2jThcUGuc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Home Depot Canada — Processing Guide

> **Source:** Home Depot Canada OneGuide (Google Doc `1vHh5IpsUGvj5xB-LXz0Pzqgkb0U4CuO5VIo_XVA3hv8`), updated Jul 14, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Tier 3 Standard) |
| Availability | All platforms |
| Slack channel(s) | `#homedepotca` |
| Flyer type(s) & cadence | Weekly (315) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); DOC (post-processing QC); Strategic Ops — **yes, Feedel/data services**; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available To / Valid To Monday.
- **Preview date:** set to the upcoming Monday.
- Bilingual account (English + French pricing zones).

## Upload & setup (owned by FLEX / OS)

Two codesheets: a **Pages codesheet** (same file every week) and a **Store assignment codesheet**.

- **Pages codesheet:** run it — a discrepancy in page count between zones is normal. Then Pages → Edit → search "AS" in page name (7087) → mark all as French; switch AS 7087 pricing zone to French and double-check page assignment; rename the pricing zone to **"AS fr"** (there should be **4 French pricing zones**).
- **Store assignment codesheet:** there are two versions — one for when pricing zone **AR-7102** exists and one for when it doesn't.
- **URL list manipulation:** import URL list to Excel; highlight duplicates in column C and number them to differentiate; compress all images; save as `.xls`.

### Setup QC checklist

- Preview date = upcoming Monday; available everywhere.
- Check vendor assignments (Preview QC is English only); set all vendor task priorities **except** Preview QC and Wayfinding QC to **"high"**; attach the URL list to all vendor tasks.
- Leg heights **45/25**; thumbnails: one page for squares, two pages for rectangles.

## ⚠️ Common errors / risk items (retailer-specific)

- **Look for multiple products per box** — a box must be drawn for **each item with a SKU even if its image isn't on the flyer** (e.g. a 6' and a 5' patio door in one visual = two boxes).
- **Banners are box-drawn/tagged from a weekly spreadsheet** attached to the flyer (used across drawing, box QC, tagging, and QC). It indicates which areas to box, the name to tag, and the link. **Do NOT include "HOME DEPOT" in the link or the description; leave description blank.**
- **FREE items bundled with power tools:** do **not** box the free item separately even if it has its own SKU — keep it in the associated item's box.
- **Appliances always boxed separately** (washer/dryer separate).
- **Colour swatches:** box separately only if **each swatch has its own SKU**; if no unique SKUs, one box for item + swatches.
- **Bilingual pages:** one box around the whole item if a single SKU covers both languages — no separate main + text box per language.
- Only box the item area (e.g. exclude "Why Hardwood?" copy); avoid unnecessary text boxes.

### Pre-Final QC tasks (notable)

1. Ensure all pages have at least 1 slice.
2. Search URL CONTAINS "search" and QC links against the URL list.
3. On appliance pages, search index for VALID TO IS NOT Blank (Item display type) — verify whether the item should have a valid date or if it's from a special-offer banner callout.
4. Search CATEGORY CONTAINS "XX" (PRO) and change to the equivalent "D" (DIY) category.
5. Run "Mass Fetch URLs" custom action; verify all URLs in sessions.
6. Regenerate data-piping groups; rerun data piping on items missing images 2–3× until >70% have images.
7. Confirm no linking-doc names are left as "Item" display type.
8. Spot-check regional banner URLs (banners with 2+ regional versions tagged true to region).
9. Add/QC tracking codes and apply (week numbers **and** dates correct).
10. Upload custom tiles if available (EN tiles → EN zones, FR → FR zones); if none by Monday afternoon, reach out to the retailer.
11. Check largest region in vertical preview; set PQC priority "high" in vendor tab.
12. Flyer sorting: **DIY Weekly > Pro Weekly > Other** (current DIY flyer defaults to bottom of stack).
13. Update the Deep Link Tracker.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot ON.** Linking document required (Box Draw/Box QC specific). **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons.
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Linking document required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.**
- **Image QC:** select the cutout if the PDF includes both washer/dryer, if the PDF is reversed, or if there are black shadows on the PDF; otherwise prefer the PDF image.
- **Post-processing (DOC-owned):** Item Category QC, Item Image QC, URL/Links QC, SKU QC, ad-hoc QC, Final QC.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite.**

---
*Source: Home Depot Canada OneGuide (Google Doc `1vHh5IpsUGvj5xB-LXz0Pzqgkb0U4CuO5VIo_XVA3hv8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Home Depot USA — Processing Guide

> **Source:** Home Depot USA OneGuide (Google Doc `1JzFdQSmwhWkaBJmaYF-lsC2bG9eJkgFxnIaFzijgHLA`), updated Apr 10, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 — S1C2 Premium |
| Availability | All platforms (Catalog & Standalone: **Hosted only**) |
| Slack channel(s) | `#homedepotus`, `#flex-processingsupport` |
| Hosted URL | homedepot.com/c/localad |
| Flyer types | Local Ad (248), Puerto Rico (293), Guam (299), Catalog (6868), Standalone 1 (9976) |
| Processing | Auto-stack; Flex (Processing Support / Flyer Review); DOC-owned setup & QC; Feedel/data services on Local Ads; no coupons |

## Files & schedule

- **Local / PR / Guam:** files received Monday or Friday. Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. Preview 1 week before go-live. Setup + Image QC + FQC owned by DOC.
- **Catalog:** files Monday. Available From Monday, Valid From Sunday. Preview 1 week ahead. Hosted only. Linking document (Smartsheet) required.
- **Standalone 1:** ad-hoc, hosted only.
- **Publication timing rule:** Available date = 1 business day prior to Valid date, launch at **3:00 AM**. Set a trigger to flip the Valid date from the preview date to the true Valid date ~24 h before launch.

## Upload & setup (owned by DOC)

- A 3rd-party team (Quad) emails when PDF pages + codesheet are on the SFTP.
- **Codesheet indicators:** National/Print Ad = **ST**; PR/USVI = **SCG** or **TCG** (Market 133 PR, 337 USVI St Thomas, 559 USVI Kingshill); Guam = **SG** (Guam can be a manual upload — only 1 store / 1 PZ).
- Download the `.xls` with the correct indicator → save as `.csv` (no manipulation **unless** there are subpages, e.g. page `02_03` — then delete the "page 3" column). Upload to FAdmin. **Config name: `home_depot_usa`.** Codesheet uploads all pages and pricing zones.
- **Catalog upload:** manually upload all pages & auto-group; 1 PZ = "base"; add all stores then remove PR/USVI and Guam store sets; attach the Smartsheet + LoRes file to all vendor tasks.
- **Setup QC:** preview date = 1 week before Available; change Valid to match preview date; trigger to fix Valid ≥24 h before launch; External Run Name = callout on first page.

## ⚠️ Common errors / risk items (retailer-specific)

- **URLs (all items must have a URL except Live Goods/plants).** Search the SKU on homedepot.com, select the **SINGLE item result — never a bundle item option**, visually confirm the Store SKU # matches, then paste the URL. **Do NOT use Fetch URL, "search" page URLs, or bundle URLs.**
- **OMSID field (critical):** any item with a SKU + URL must also have an **OMSID** = the 9-digit "Internet Number" (last 9 digits of the product URL, or the Internet # on the PDP). **Do NOT use the SKU# or Model# as the OMSID.** Ensure OMSID goes in the OMSID field, **not the Badge field**.
- **Badge field:** items with a **SPECIAL BUY** icon → Badge = `SPECIAL BUYS`; **NEW LOWER PRICE** → `NEW LOWER PRICES`. All caps, tagged exactly.
- **Description:** only add a description if there is **no** URL.
- **Washer/dryer pairs and appliances: always boxed and tagged separately.**
- **Multiple SKUs in one ad block with multiple images → box separately;** multiple SKUs that are just different **colours** of the same item → box together.
- **Box/tag ALL direct links, banners, and "green box" areas:** Home Depot logo, front-page publication name, Free/Fast Delivery, Select Appliances, financing offers, "Behr COLOR OF THE YEAR", "Low Prices. Guaranteed.", and every URL CTA (homedepot.com/lawncare, /ryobi, /milwaukee, /paint, /appliances, etc.). CTAs appear all over the flyer — do not miss any.
- **For PR/USVI/Guam URLs:** change store location by zip — Puerto Rico `00961`, USVI `00961`, Guam `96913`.
- **Catalog-specific:** draw one neat box over the item and its black dot — **no overlapping boxes, no text boxes**; box QR codes with adjacent text; keep Brand in the Brand field (never "Unbranded", never put brand in the Name field); use the **SKU as the OMSID** for Catalog only; Description is data-piped so leave blank; landing-page URLs → set Display Type: Link.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, PDF Image Auto-Selection ON, Box QC bot ON.** (Catalog: linking document required.) **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons and packaged deals.
- **Tag / Tag QC — Low complexity. Auto-tag ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, **OMSID**. Enter brand as shown in flyer, all caps; enter valid dates only if different from the flyer run date (e.g. only the "get 1 free" select tool gets the special valid date).
- **Image QC:** **images are data-piped — select cutouts.** Custom Action → Set Cutout Images (add Flyer Run ID) to force data-piped images; use the clean PDF where no data-piped image exists.
- **Direct-link URL reference:** Delivery, Pick Up, Credit Center, Appliances, Military, "Nobody Beats Our Prices" (price-match), Return Policy, Store Locator (see the OneGuide for the exact URLs).

### Final QC highlights

- Data piping >95% (double-check missing/errored images); thumbnails Standard 4.
- Item Search sweeps: OMSID blank + URL not blank → add OMSID; SKU not blank + OMSID blank → add URL + OMSID; SKU blank → OK only for Live Goods.
- Geography: no change week over week; make URL corrections per the direct-link list.
- **Catalog FQC:** fix boxes/QR codes; export items to confirm brand not in Name field (a `=IFERROR(TRIM(REPLACE(...)))` formula strips brand from name); confirm SKU in OMSID field; CTL+F each Smartsheet URL in Item Search to verify tagging; data-pipe near 100%.
- Send preview ~1 week ahead.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite** (all flyer types).

---
*Source: Home Depot USA OneGuide (Google Doc `1JzFdQSmwhWkaBJmaYF-lsC2bG9eJkgFxnIaFzijgHLA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Home Furniture Outlet — Processing Guide

> **Source:** Home Furniture Outlet OneGuide (Google Doc `1nBNmWNnkwieiP7BQFloiWnn7rT9NMfUnuD7EF7H85t0`), updated Jun 20, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer (11761) — ad-hoc |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no OS, no coupons, no Feedel/data services |

## Files & schedule

- **When files arrive:** ad-hoc; all publication dates ad-hoc. Files may need to be added to the SFTP by the processor if the client sends them over email.
- **Workflow:** Upload & Setup and FQC both owned by FLEX.

## Upload & setup (owned by FLEX)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Then Auto-Group or manually enter grouping numbers, ensure the correct language is selected, Save & Confirm. **Do NOT process internally.**
- **Pricing zone creation:** in Flyer Creation, create a **Base** pricing zone, select all applicable pages, Save & Confirm, add all applicable stores.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View); if uploading from SFTP, confirm no pages remain un-uploaded.
- Confirm flyer dates (usually first or last page of the flyer).
- Thumbnails: 4 Standard.

## ⚠️ Common errors / risk items (retailer-specific)

- **Content policy check:** ensure there is an average of **3 products per page** (for flyers of 3+ pages).

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF.** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Spotchecks:** standard pricing spotchecks; pre-FQC spotchecks cover 20% of pricing zones.

## Final QC / flyer review (owned by FLEX)

- Pre-FQC: dates correct vs PDF; availability toggles correct; thumbnails include the retailer logo; all items boxed/tagged; previews published & clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** — checks flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: Home Furniture Outlet OneGuide (Google Doc `1nBNmWNnkwieiP7BQFloiWnn7rT9NMfUnuD7EF7H85t0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Home Hardware & Home Furniture — Processing Guide

> **Source:** Home Hardware / Home Furniture OneGuide (Google Doc `1X9HDiPthDAM6K59fwtSOqXPCfbQUNiMF4w3SxjaM8L0`), updated Mar 12, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 1 |
| Availability | All platforms |
| Slack channel(s) | `#homehardware`, `#homehardware_sep`, `#homehardware_mergil` |
| Hosted URL | homehardware.ca |
| Flyer types & cadence | **Flyer (504)** bi-weekly (2 flyers) · **LBM (3520)** bi-weekly · **Pro Flyer (9711)** bi-weekly · **Specials (8741)** ad-hoc (incl. Catalogs/Guides) · Mount Forest custom flyers |
| Processing | Auto-stack; Flex 3FL / Flyer Review; DOC-owned setup & QC; Feedel/data services on Flyer (504) & LBM only; no coupons |

Key resource: the **HH Linking Document** (attached to all vendor tasks) — banner names, links, and item names all come from it. No retailer preview; consumer "preview" available each Wednesday.

## Files & schedule

- **Files arrive:** ad-hoc, typically ~2 weeks in advance.
- **Flyer (504) / LBM (3520):** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. Bi-weekly.
- **Pro Flyer (9711):** Available From Monday, Valid From Tuesday; every two weeks.
- **Specials (8741):** ad-hoc; some are Catalogs/Guides (follow dates on the PDF / confirm with external team via shell dates).

## Asset delivery (owned by DOC)

- Download the file packages from the emailed "Link to Download" (use the fallback link if the first fails). HH weekly + HHBC weekly are usually sent together; PRO and special campaigns come in their own folders.
- Unzip so a regular folder is on the desktop, connect to Home Hardware in Filezilla, and **drag the entire folder over** — do **not** transfer the zip, individual pages, or create your own SFTP folder (dropping the whole folder sets the base path correctly for the codesheet). Sync takes up to ~2 hours.

## Upload & setup (owned by DOC)

- Download the codesheet from the emailed distribution list (subject like "Events Starting …"). Codesheet indicator maps to flyer type: **HH → Flyer (504)**, **HHBC → LBM (3520)**.
- Save as CSV and run in the codesheet interface:
  - **Toggles:** select everything **except Region Assignment and Combine Zones**.
  - **Config name: `home_hardware_lbm`** (used for HHBC + HBC + HH).
  - **Base Path:** match the number to the FTP files; use everything up to language/region (English / bilingual / Quebec).
- Thumbnails: Standard 4. External run names (EN + FR):
  - Flyer (504): **Home Hardware** (EN & FR).
  - LBM (3520): **Home Hardware Building Centre** (EN) / **Centre de rénovation Home Hardware** (FR).
- After all PZs are created, mark Flyer Creation complete and QC pagination (PZ correctness, page counts). While QCing, note major CTAs/direct links (usually on the first and last 3 pages), pull their URLs from the HH Linking Document, format the linking doc, and attach it to all vendor tasks.
- **Specials (8741) setup:** manually upload page(s), one pricing zone labelled **Base**, add stores manually (may need to assign FSAs since paid flyers use a different radius — get FSA lists from the account channel or the Store-Level Campaigns sheet; if organic, keep default FSAs). Set external run name from the original email. No linking doc unless links are provided in the email body.
- **Note:** occasionally a zone has no FSAs and must be added manually; 3 stores share an FSA so those warnings can be ignored (rare).

## ⚠️ Common errors / risk items (retailer-specific)

- **Language tagging — tag in ONE language only.** For French pages, tag in **French only** (never both languages). French PDFs must be copied exactly, including all accents (é à è ù â ê î ô û ë ï ü ç / É À Ç).
- **All items with a SKU MUST have a URL.** If an item has no SKU, do **not** enter a URL. Use the **Fetch** button for single-SKU URLs; for multiple SKUs, tag all SKUs then use a homehardware.ca `/en` or `/fr` search-link. SKU format: keep the hyphen (e.g. `3698-218`, not `3698218`). Paired items with no pair SKU → leave SKU blank.
- **Google category** must be tagged on every item.
- **Washer/dryer pairs boxed & tagged separately** (each side linked to its own SKU; pair price goes in the Sale Story field).
- **"Buy X get Y free":** the FREE item is boxed/tagged as its own item box, with the offer in the Sale Story.
- **Multi-item blocks:** every item linked to its price and text (text boxes may stack); box the HERO (largest) image last. Each **size** gets its own box with its own SKU/URL.
- **"Your Choice"** prefix only when items are boxed together — not when boxed separately. Prefix: "Great Price" (EN) / "PRIX SUPERBE" (FR). Postfixes lowercase; skip postfix if "pack of"/count already in the title. "Priced In-Store" → put in prefix with no current price; if both, use "Only Priced In-Store".
- **Lumber pricing:** in a multi-price table, different sizes must NOT share the one-size price.
- **Do NOT** add sale story/prefix/postfix to items not linked with the original item.
- **Valid dates:** enter as on flyer; **do NOT enter the Aeroplan date**.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON (OFF for LBM), Box QC bot OFF** (ON for Specials 8741). Linking document required for Flyer/LBM/Pro. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks, CTAs. **Exclude** coupons. **All SKUs must be item boxes, not text boxes.**
- **Tag / Tag QC — Medium complexity. Auto-tag OFF.** Include brand, name, pre/postfix, description (SKU in description in flyer format), SKU, price, sale story, categories, disclaimer, original price, URLs, valid dates, Google categories. Keep brand in the Brand field only — never in the Name field.
- **Image QC (FLEX-owned post-processing):** select **Cutouts** and **No Images**; choose clean PDFs (clear item, white background, no shadows/lines). Do **not** select an image for items with no applicable flyer image.
- **URL/Links QC (FLEX-owned):** cross-reference the Linking Document against each page's banners; paste the URL and set **Display Type: "Link"**. Item name must match the linking doc exactly. Use Item Search (URL IS blank, type Item) to catch CTAs mistagged as items → change Display Type to Link; and (type Link) to confirm only non-shoppable direct links appear.
- **Spotchecks:** confirm Brand field upper/lower case; defer pre/postfix to the PDF.

## Flyer review

- **Flyer Review type: Lite.** (Flex 3FL / Flyer Review on Flyer, LBM, Pro; FLEX Image + Links QC on most types; Specials 8741 has no Flex flyer review.)

---
*Source: Home Hardware & Home Furniture OneGuide (Google Doc `1X9HDiPthDAM6K59fwtSOqXPCfbQUNiMF4w3SxjaM8L0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# HomeBuys — Processing Guide

> **Source:** HomeBuys OneGuide (Google Doc `1wEhmfmI3rO1egEKk_9qSH8DbDgo0QNqu6VouISx22-w`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channel(s) | `#homebuys` |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer — ad-hoc |
| Processing | Auto-stack; Vendor-owned setup & FQC; no OS, no coupons, no Feedel/data services |

## Files & schedule

- **When files arrive:** Ad-hoc. Assets must be provided by **2 PM Fridays** to hit the committed **4-business-day turnaround** for a **Thursday** launch.
- **Publication cadence:** Available From Thursday → Available To Wednesday; Valid From Thursday → Valid To Wednesday.
- **Workflow:** Upload & Setup Friday; FQC Wednesday; live Thursday. Both owned by Vendor.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu. Folder is named by the flyer's valid date — **always use the lower-case folder; do not upload the Upper-Case folder.** Confirm & Upload.
- Scroll down → **Auto-Group** → Save & Complete.
- **Pricing zone creation:** create a single pricing zone named **"Base"**, add all stores, Save & Complete.

### Setup QC checklist

- Confirm all pages uploaded: open the SFTP and ensure nothing remains except the multi-page PDF (the one with Upper-Case letters in the name that does **not** end in "P####"). If pages were missed, flag the FT team.
- Confirm flyer valid dates match page 1 of the PDF.
- Thumbnails: 4 Standard.
- **Geography tab: expect 0 changes to stores/FSAs.** Any change → flag the FT team (Slack or email), but continue the checklist.
- Platform toggles: available on all platforms.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals (e.g. washers/dryers), retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low complexity. Auto-tag ON.** Include image (always pick a clean PDF if available), brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - **Current Price:** do **NOT** tag the "Theirs" price in any field.
  - **Sale Story:** may include "HOT BUYS!" if present on the PDF.
  - **Image:** always select the clean image (lifestyle / real photographic images are fine).
- **Spotchecks:** standard pipeline spotchecks.

## Final QC / flyer review (owned by Vendor)

- Pre-FQC: confirm valid dates vs PDF; available everywhere; thumbnails drawn with retailer logo; all items boxed and tagged; previews published and clickable; geography consistent with last week (flag 100% of discrepancies to FT Ops, but don't block).
- **Flyer Review type: Lite.**

---
*Source: HomeBuys OneGuide (Google Doc `1wEhmfmI3rO1egEKk_9qSH8DbDgo0QNqu6VouISx22-w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Horizon Sante — Processing Guide

> **Source:** Horizon Sante OneGuide (Google Doc `1R09DkY_i9UU1xB_VEDLFCvzNQUWIjhdjAXAm10I3nxk`), updated Mar 30, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel(s) | `#horizon-sante` |
| Flyer types | **Monthly Flyer (11163)** · **One Pager (11637)** · **Specialty / Encart Saisonnier (12277)** ad-hoc |
| Processing | Auto-stack; Flex 3FL + Flyer Review; FLEX Image QC, DOC FQC; no coupons, no Feedel/data services |

French-language account (all pages tagged in French, with English cross-language zones).

## Files & schedule

- **When files arrive:** Monday. Files may need to be added to the SFTP by the processor if the client sends them over email.
- **Publication cadence:** One Pager and Monthly both start on the **first of the month** and run the entire month.
- **Preview:** 1-day consumer preview (set via Available Date) on Monthly Flyer, One Pager, and Specialty.

## Upload & setup (owned by FLEX)

- **Manual upload** (Monthly & One Pager): open the flyer run → Pages → Edit → select the broken-out numbered files. **When uploading the Monthly, make sure the files do NOT say "One Pager"; for the One Pager, use the files that say "One Pager."** Select files → change language of all files to **French** → Save & Complete.
- **Pricing zones** (each flyer gets a French zone + a cross-language English "FR CL" zone):
  - **Monthly:** FR and FR CL → store set "Monthly Flyer" (12 stores).
  - **One Pager:** FR and FR CL → store set "One Pager" (1 store).
  - **Specialty:** FR and FR CL → store set "Specialty" (12 stores).
- Ensure a 1-day preview is set (Available Date); wait for Setup QC to generate, then mark complete.

### Setup QC checklist

- Available everywhere; **no theme**.
- **External Run Names:** Monthly Flyer → "8 pages (English & French)"; One Pager → "One pager (English & French)"; Specialty → "Encart Saisonnier (English & French)".
- Confirm the 1-day consumer preview on all three flyer types.

## ⚠️ Common errors / risk items (retailer-specific)

- **Look for multiple products** per block.
- **Specialty banners:** ensure these 12 stores are added to **both** PZs — 9007, 9010, 9006, 9011, 9012, 9013, 9014, 9015, 9017, 9023, 9046, 9022.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF.** Linking document used for both Box/Tag. Box all items with prices (text boxes when necessary); **no overlapping boxes**. **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons and packaged deals.
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Include brand (Brand in Brand field, remaining bolded text in Name), name, pre/postfix, valid dates, description (text under the bolded name), SKU, price, sale story (discounts/dollars off, usually in red), categories, original price. **Exclude disclaimer and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts are accepted.
- **Spotchecks:** standard pricing spotchecks.

## Final QC (DOC-owned) / flyer review

- Pre-FQC: entire item name in the Name field; Standard 4 thumbnails; no theme; External Run Names as above; Specialty 12-store check; cutouts OK.
- **Flyer Review type: Lite.**

---
*Source: Horizon Sante OneGuide (Google Doc `1R09DkY_i9UU1xB_VEDLFCvzNQUWIjhdjAXAm10I3nxk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Houchens IGA — Processing Guide

> **Source:** Houchens IGA OneGuide (Google Doc `12XUi3vutaRNZezmB6d2CwRVu6sYJn5fZV27KNn0oVIQ`), updated Apr 27, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flexflyerreview` |
| Hosted URL | myiga.com |
| Flyer types | Weekly Flyer — **promoted (11852)** and **organic (11913)** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no OS, no coupons, no Feedel/data services |

## Files & schedule

- **When files arrive:** Tuesday.
- **Publication cadence:** Available From Wednesday → To Tuesday; Valid From Wednesday → To Tuesday.
- **Workflow:** Upload & Setup and FQC both owned by FLEX.

## Upload & setup (owned by FLEX)

Codesheet upload. The core task is **splitting one weekly breakdown into a promoted codesheet and an organic codesheet.**

- From the Houchens FTP, search "xls" and download the week's file (e.g. `IGA Ad Breakdown m.dd.xlsx`).
- Open the shared **Houchens IGA codesheets** sheet → File → Import → Upload → insert new sheet.
- Insert a column left of A. `A1` = `Promoted`; `A2` = `=IF(XLOOKUP(B2, IGA!$B$2:$B$45, IGA!$A$2:$A$45, "")="Y", "Y", "")`; fill down the column.
- Delete columns C–J so only **Promoted | Store # | Page Versions** remain; split column C via "Split text to columns"; rename page headers to page numbers; add filter.
- Duplicate the sheet: in one, filter for **Y** → name "promoted" → export CSV; in the other, filter for **Blanks** → name "organic" → export CSV.
- Upload each CSV to the corresponding flyer run: **all codesheet toggles checked except the 2nd and last**; **config name `generic`**; use the week's FTP file path; process.
  - Common error: differently named files — adjust the codesheet to match the FTP.
- Mark Flyer Creation complete, wait for sessions, then do Setup QC.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View); risk: confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (usually top of first page).
- Thumbnails: 4 Standard. Add **"Weekly Flyer"** to the external run name (English).

## ⚠️ Common errors / risk items (retailer-specific)

- **Ensure codesheets are organized correctly — especially regarding the promoted vs organic store split.** This is the main failure point for this account.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF.** Box any product block with a price and/or sale story. **Exclude** coupons, packaged deals, retailer logo, banners, social media.
- **Tag / Tag QC — Low complexity. Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Spotchecks:** standard pricing spotchecks (20% of pricing zones at pre-FQC).

## Final QC / flyer review (owned by FLEX)

- Pre-FQC: dates vs PDF; **all availability toggles should be unchecked**; thumbnails include retailer logo; previews clickable; sessions complete; geography matches last week's flyer.
- **Flyer Review type: Simple** — flyer dates, sessions, previews, spotcheck tagging, geography, availability toggles (all unchecked).

---
*Source: Houchens IGA OneGuide (Google Doc `12XUi3vutaRNZezmB6d2CwRVu6sYJn5fZV27KNn0oVIQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Hy-Vee — Processing Guide

> **Source:** Hy-Vee OneGuide (Google Doc `1pJzlGKZDUemnw5OTt66L23SDIYa9-1DRDdKe0yF0M8A`), updated Apr 30, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channel(s) | `#hyvee`, `#flex-processingsupport` |
| Hosted URL | hyvee.com |
| Flyer types | **DigDotCom** (Weekly Ad) · **Dollar Fresh** (Weekly) · **Special Sales** (all ad-hocs, e.g. 3 Day) |
| Processing | Auto-stack; Flex (Processing Support), flyer review owned by DOL; no OS beyond standard, no coupons processing, no Feedel/data services |

## Files & schedule

- **When files arrive:** DigDotCom & Dollar Fresh — Friday; Special Sales — Monday.
- **DigDotCom cadence:** 1 ad break, either Mon–Sun or Wed–Tue. **Available and Valid are always the same (no consumer preview);** dates may be staggered (some versions live Monday, some Wednesday). Preview date set to upcoming Wednesday so OS processes promptly.
- **Dollar Fresh cadence:** Available/Valid From Wednesday → To Tuesday.
- **Special Sales:** each ad-hoc goes live on different dates (3 Day Ads usually Fri–Sun).
- **Universal timing rule:** set **Available From and Valid From to 1 AM**; **Theme: No Theme**.

## Upload & setup

Codesheet upload for all three flyer types. **Config name: `hy_vee_pages`; check all toggles except Region Assignment.**

- From the FTP, search "xls" and hide uploaded; ignore any `RUNLIST` files. DigDotCom → the "Digital DotCom" xls; Dollar Fresh → the "Dollar Fresh" xls; Special Sales → any xls that is NOT a "Weekly Ad" (e.g. "special ad", "3 day", "1 day").
- **⚠️ Hy-Vee file names are case sensitive** — if the codesheet fails, it's usually a missing page, a typo, extra rows/columns, **or spaces when pasting names** (Fadmin errors on spaces). Flag issues to the DOC.
- **DigDotCom external run name: `Weekly Ad`.** Must attach the **Weblinks document** (from the same FTP folder) to all vendor tasks — **do NOT mark Setup QC if the Weblinks is not attached.**
- **Dollar Fresh:** pages usually 5–6 (first PZ may have one fewer page); external run name `Weekly Ad`; no linking doc.
- **Special Sales:** create the flyer run manually per xls/email; dates from the path name (Available/Valid From = start at 1 AM); internal run name e.g. `HV 3 DAY`; external run name = the front-page callout (e.g. "Bourbon & Beer Sale", "3 Day Sale"). Stores always differ — no need to flag.

## ⚠️ Common errors / risk items (retailer-specific)

- **Banners/callouts at the top of pages must be boxed & tagged** — accessibility requirement Hy-Vee flagged. Even if there's no price/promotion, box headers first, with all info.
- **"Try It" badge:** the red dates are part of the **Sale Story**, NOT the item's valid dates.
- **"Fuel Saver" badge:** the red text under the description is the **Sale Story**, NOT the postfix. (Fuel pages: tag as Item type, Name "Fuel Saver", spend/earn tiers in the description.)
- **"PERKS PRICING"** must be added to the postfix for all applicable items, followed by the non-member pricing.
- **Item-level valid dates** are easily missed — look for dates that apply only to a single item.
- **Cut-off pages:** pages with images only (no text) can be ignored/left un-boxed; the corresponding text page is tagged instead (system can't place the pages side-by-side for Vertical Scroll).
- **Weblinks/URLs (DigDotCom Weekly only):** tag only banners listed in the attached spreadsheet; tag as "Link" item type with the exact URL. Coupons with a link are tagged as an **Item** with the URL attached (not as a Link).

## QC specifics

- **Box Draw — Medium complexity. Auto-Box ON, Box QC bot OFF.** Box all items separately (text boxes when needed), **box all headers first**. **Include** coupons, packaged deals, sign-up page, special weblinks; **exclude** retailer logo, social media. Do NOT box CTAs that lead to other apps. Non-grocery items/banners boxed per the Weblinks spreadsheet (Weekly only).
- **Tag / Tag QC — Low complexity. Auto-tag OFF, PDF Image Auto-Selection ON.** Include brand, name, pre/postfix, valid dates (if different from flyer dates), description (include "Use in…" text in quotes), price, sale story, categories, disclaimer (page-level disclaimers applied to items), original price. **Exclude SKU;** URLs only per the attached weblinks. Tag coupons exactly as shown (cutout border, barcode in box).
- **Image QC:** select a clean PDF where possible; use cutouts for any bad PDF (artificial shadow, jagged lines, discoloration, black shadow, odd shapes, grey edges).

### Final QC (FQC) highlights

- **DigDotCom:** verify every weblink page/item is tagged Link (coupons-with-link tagged as Item); ensure all "click here" CTAs are boxed/tagged (else tag `https://www.hyvee.com/`); dates + 1 AM; sessions run; thumbnails; external run name "Weekly Ad". **Add tracking codes in order:** Source=flipp, Medium=cpc, Campaign=circular, Content=mmddyyyy (go-live date).
- **Dollar Fresh / Special Sales:** spotchecks clear; cover dates match run; 1 AM; Standard 4 thumbnails; sessions run. Special Sales: flag to DOC/DOL if fewer than 6 items (content policy); flyer sorting Weekly Ad → Event Sale → Monthlong → Specialty.

## Revisions / page swaps

- Hy-Vee sends an updated codesheet (file with `rev` in the name) highlighting revisions. Just run the new codesheet on the flyer run — it re-paginates automatically (no manual page swapping). Copy items to/from new pages for live flyers, or have OS process net-new pages pre-live. Notify DOC and DOL when done.

## Flyer review (owned by DOL)

- **Flyer Review type: Lite.**

---
*Source: Hy-Vee OneGuide (Google Doc `1pJzlGKZDUemnw5OTt66L23SDIYa9-1DRDdKe0yF0M8A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
