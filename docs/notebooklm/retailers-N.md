# Retailer Processing Guides — N

> Bundle of 10 retailer-specific processing guides (N). Contacts and credentials are omitted from every guide.

**Contains:** NAPA Auto Parts, Nature's Emporium, Nature's Fare Market, Nature's Source and Nature's Signature, Nebraska Furniture Mart, Nesters Market, No Frills, Notre Dame Home Furnishings, NSLC, Nutters Everyday Naturals


---

# NAPA Auto Parts — Processing Guide

> **Source:** NAPA Auto Parts OneGuide (Google Doc `181Qo0B7I8cN5pAeA8SJuVBEz4OB518qTbbGY60o-mvM`), last updated Feb 13, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Monthly** — all platforms · **Catalogues** — Hosted only |
| Slack channel | `#napaautoparts` |
| Hosted URL | napacanada.com/en/promotions/flyers |
| Flyer types | **Type 1: Monthly** · **Type 2: Quarterly Catalogs** (Real Deals & C-MAX) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); no coupons; **Strategic Ops — yes (Feedel / retailer data services)** |
| Language | Bilingual — EN & FR (versions must be identical) |

## Files & schedule (Monthly)

- **Files received:** Monday. Downloaded from the SharePoint drive and uploaded to the Flipp SFTP by **DOC**.
- **Publication cadence:** Available From Monday (1st of month); Valid From Tuesday (1st); Available To Monday (last day); Valid To Tuesday (last day).
- **Preview date:** set **7 days before go-live** (not counting weekends).
- Retailer doesn't always notify of a file drop — rule of thumb: if no mapping doc / files for the coming month by the first week of the prior month, reach out.
- **Workflow:** ~15 days out — upload & setup; 7 days out — FQC & preview; 3 days out — make corrections.

## Upload & setup — Monthly (owned by DOC)

- Download EN and FR files + the **linking (mapping) documents** from SharePoint and upload to SFTP. **Two linking docs:**
  1. **Mapping Flipp document** (e.g. "March 2025 mapping flipp") — used for **all pages** (edited to focus on Brand, Item Name, Price, URL).
  2. **Category page_Curation** (e.g. "Mar2025 Category page_Curation") — used for the **Categories pages ONLY.**
- Create separate `.xls` docs for EN and FR tagging (e.g. "August 2024 Links EN.xlsx" / "…FR.xlsx"). Attach linking docs to **all** Vendor Tasks — especially the Mapping Flipp doc.
- **Manual upload:** upload the month's pages; change language for French pages (Save and confirm it stayed); Save & Complete.
- **Create 2 pricing zones: EN and FR.**
- **⚠️ DO NOT ADD STORES — stores are added during FQC, not setup.**
- Double-check available/valid dates from the NAPA Store Update Tracker. Set preview 7 days before go-live. Complete the Final QC checklist, then file a **FAB ticket** for support in Brand QC + Links QC (due date = preview date at noon).

## Upload & setup — Real Deals & C-MAX Catalogs (secondary publication)

- Use the **"Catalogue"** flyer type. Manual upload; two PZs (EN, FR); **no mapping document; Hosted only.** Assign stores during FQC, not setup.
- **⚠️ Risk:** watch for FTP folders being combined into one folder. Real Deals / C-MAX guides are **one file per language.** Real Deals receives ALL pages (including CMax pages); **CMax receives only CMax pages** (typically the last 4–7 pages — file names don't separate them; note which page has the CMax title and start there to the end).

## ⚠️ Common errors / risk items

- **Versions:** EN & FR versions must be identical (tagging + image selection). The retailer is very particular.
- **Categories:** page categories tagged if **3+ items** on the page are from that category; on catalogues, match the label on the side of the page.
- **Images:** all items should be PDF images; if not clean, look in the shared image folder; if not there, reach out to the retailer.
- **Group/list items** boxed as 1 — only Name, Description, and price range tagged.
- **"2 for 1" items:** tag in the **PREFIX** price field. **Do NOT put the 1 in the price field.**
- **Errored links:** watch for URLs missing a period — ensure the link is `www.napacanada.com`.

## QC specifics

### Box Draw / Box QC — **High complexity**
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required for **Monthly** flyers; **not** required for CMAX/Real Deals.
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- **Real Deals:** grouped products can be boxed together — enter the price range via current price + prefix/postfix; list all SKUs in the description.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** Linking document required (Tag/QC specific).
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Use the EN tab for English pages, FR tab for French pages.**
- **Monthly:** Name/Brand, Description, SKU, URL all come from the mapping spreadsheet (follow its capitalization) — this does not apply to CMax/Real Deals (which come from the PDF).
- **Prefix examples:** "2 for"/"2/", Starting at, Combo, New, Wow!, Super Sale!, Special. **Postfix examples:** 175g, 1 Litre, ea, /ea, /ch (French: ch./ch, Nouveau, Après Échange). **Do NOT enter a postfix for a price range when all items have the same price.**
- **SKU (Real Deals):** if products are boxed together, enter all SKUs in both Description and SKU fields. **Do NOT tag** "L'article vient dans ces Variations" in the Description.
- **Images:** select PDF if available, but for LISTED items do not select a PDF image.
- **URLs:** only month-long publications receive links; Real Deals / AIM Catalog do not. Use the correct EN/FR spreadsheet — EN URLs only on the EN sheet, FR URLs only on the FR sheet.
- **Categories:** keep simple, following the main items (common: Windshield Wipers, Car Batteries, Brake Systems, Cleaning Supplies, Hand Tools, Power Tools); on catalogues follow the table of contents / side page naming.
- **Sale Story:** enter if present (e.g. "Save __% or $__"). Only add "Up to 45% OFF"-type stories if the discounted price is in the item pop. **Tag ALL sale stories in CAPS**, in the correct language, pulled from item/text extraction; **do NOT include the "-" sign.**
- **List items:** only 3 fields — Name, Description (group description only, not individual), Price Range (lowest–highest, not individual prices).

### Image QC
- Choose a clean PDF; if unavailable, grab a clean image from the shared folder (for multiple items, include all in the photo selection).

## Post-processing / FQC — Monthly (owned by DOC)

1. **Spotchecks** — always reference the linking document; item boxes with PDF text details must have that text in the description; all items have a URL per the mapping doc.
2. **Verify EN and FR are IDENTICAL** (tagging + image selection). QC via Item Search: (URL contains `fr`, Language English) and (URL contains `en`, Language French) — **no French URLs on English pages or vice versa.**
3. **Image QC** — clean PDF.
4. **Sales story QC** — all caps, correct language (Item Search by Language EN then FR).
5. **QC thumbnails** — 4 standard.
6. **Category page** — add if available (regular ads only, not catalogs); confirm with NAPA. NON-ROL zones also receive the category page.
7. **QC page categories.**
8. **Assign stores:** EN PZ → newest store set (Flyer yyyy-mm-dd); FR PZ → newest store set; NON-ROL EN PZ → all stores minus Flyer yyyy-mm-dd; NON-ROL FR PZ → all stores minus Flyer yyyy-mm-dd.
9. **Tracking codes** from the store update tracker: #1 Dynamic Variable / Hosted / `cid` / value from tracker; #2 Dynamic Variable / Distribution / `cid` / value from tracker.
10. Mark items in-store only; finish FQC checklist.
11. **Preview email** (7 days before go-live) to the NAPA team (cc the Flipp NAPA alias). Note in the email if the category page hasn't been provided or if images are missing from the shared folder.

**NON-ROL zones:** after FQC, re-upload all pages with "NONROL" added to page names (correct language per name). Create NONROL EN and NONROL FR pricing zones with the NONROL page versions; once tiles generate, mark Vendor Box Draw complete and copy items from existing pages. Via Item Search on each NONROL zone, select all items → Multi Edit → check the URL box and leave it empty → Save (removes URLs). **End with four pricing zones — identical pages/items, but NON-ROL zones have no URLs tagged.**

## FQC — Real Deals & C-MAX Catalogs

- No image QC; no NON-ROL zones; no tracking codes; no preview emails.
- Use the most recent Catalog store set; live on hosted only; external run name matches the flyer run name (Real Deals or C Max); standard 4 thumbnails.

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: NAPA Auto Parts OneGuide (Google Doc `181Qo0B7I8cN5pAeA8SJuVBEz4OB518qTbbGY60o-mvM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nature's Emporium — Processing Guide

> **Source:** Nature's Emporium OneGuide (Google Doc `1XGFY8wQMJAcjC8AIfqukju7gm4KCQWFU5GBLeRqa9Zk`). OneGuide last updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#flex-processingsupport` |
| Hosted URL | https://naturesemporium.com/ |
| Flyer type(s) & cadence | Flyer Type 1: Weekly · Flyer Type 2: Bi-weekly |
| Processing | Auto-stack |
| Involvement | Flex (Processing Support); no coupons; no Strategic Ops / Feedel; OS N/A |

## Files & schedule (Flyer Type #1)

- **When files arrive:** Monday
- **Publication cadence:** Available From Friday, Valid From Friday; Available To Thursday, Valid To Thursday
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup

Pages may need to be added to the SFTP by the processor if the client sends files over email.

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu on the right (or upload manually from email if needed) → Confirm & Upload. Once pages are listed, Auto-Group or manually enter page numbers in the Grouping Number field. Ensure the correct language is selected (English). Save & Confirm.
- **Pricing zone creation:** Create Base pricing zone, select all applicable pages, Save & Confirm, then add all stores.

### Setup QC (owned by Flex)
- Confirm all pages uploaded correctly (Pricing Zone tab → Items View). **Risk:** if uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.
- Confirm flyer dates (usually first or last page of the flyer).
- Complete Thumbnails (Standard 4). Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- Look for multiple products in a single block.
- Un-uploaded SFTP pages — always verify the SFTP has no leftover pages after upload.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block with a price and/or sales story.

**Tag / Tag QC (Low complexity — Auto-tag OFF)**
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand is Box Draw/Box QC specific.
- **Exclude:** SKU, URLs.

**Image QC**
- Select clean white-background images where possible; otherwise select the cutout.

## Post-processing
- **Item Category QC (Flex):** ensure every item has a Google and Analytical Category.
- **Item Image QC (Flex):** prefer white-background PDF; otherwise cutout.
- **FQC / Ad-hoc checks (Flex):** spotchecks if required; QC thumbnails (Standard 4 — stock premium, storefront carousel premium, storefront carousel organic); Edit Details = available everywhere, no external run name, run dates match last page of PDF; flag missing pages or geography changes to the full-time team.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Refer to the Nature's Emporium Flipp Operations Guidelines: Publication & Ad-Hoc Requests doc for BF/ad-hoc comms.

---
*Source: Nature's Emporium OneGuide (Google Doc `1XGFY8wQMJAcjC8AIfqukju7gm4KCQWFU5GBLeRqa9Zk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nature's Fare Market — Processing Guide

> **Source:** Nature's Fare Market OneGuide (Google Doc `1qLBZJRRcLVoX-wcgkBNBQQB-LBl4goxe0hnlD2QKupQ`). OneGuide last updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#naturesfare` |
| Hosted URL | https://www.naturesfare.com/ |
| Flyer type(s) & cadence | Flyer Type 1: Bi-weekly |
| Processing | Auto-stack |
| Involvement | Flex (Processing Support); OS — Setup; no coupons; no Strategic Ops / Feedel |

## Files & schedule (Flyer Type #1)

- **When files arrive:** Friday
- **Publication cadence:** Available From Thursday, Valid From Wednesday; Available To Thursday, Valid To Wednesday
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (Flex)

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages tab → Edit. The folder is labelled clearly with the publication start date (all the MO pages and the StJ PZ). Auto-group. Save + Complete.
- **Pricing zone:** Create 1 pricing zone — Base. Add all stores.
- Check Geo and ensure "No Stores or FSAs/zips were added or removed!"
- In the SFTP, download the linking document in the DOC format and attach it to all vendor tasks.

### Setup QC (owned by Vendor)
- Check the SFTP to ensure all pages have been uploaded.
- Edit Details: no external run name; available everywhere; no theme; check dates against the dates at the top of the flyer.
- Complete Thumbnails: Standard 4 (thumbnail 1065×600 first two pages; stock premium first page; storefront carousel premium first two pages; storefront carousel organic first page).
- Complete Setup QC.

### ⚠️ Common errors / risk items
- **Available and Valid live time must be set to 3 AM.** Ensure the time is set for 3 AM.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)** — follow the layout document provided by the retailer.
- **Include:** sign-up page, special weblinks.
- **Exclude:** coupons, packaged deals, retailer logo, social media.
- Box each product block with a price and/or sale story. Box any banners with call-outs.

**Tag / Tag QC (Low complexity — Auto-tag ON)**
- **Include:** name, pre/postfix, description, price, sale story, categories, disclaimer, original price. Brand is Box Draw/Box QC specific.
- **Exclude:** valid dates, SKU, URLs.

**Image QC**
- Pick clean white-PDF images where possible.

## Final QC (owned by Flex)
- Spotchecks if required; QC thumbnails (Standard 4 — stock premium, storefront carousel premium, storefront carousel organic); Edit Details = available everywhere, no external run name, run dates match last page of PDF; flag missing pages or geography changes to the full-time team.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Refer to the Nature's Fare Market Flipp Operations Guidelines: Publication & Ad-Hoc Requests doc for BF/ad-hoc comms (page swaps, post-live checks, etc.).

---
*Source: Nature's Fare Market OneGuide (Google Doc `1qLBZJRRcLVoX-wcgkBNBQQB-LBl4goxe0hnlD2QKupQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nature's Source and Nature's Signature — Processing Guide

> **Source:** Nature's Source and Nature's Signature OneGuide (Google Doc `12HVgAJGpncuJPKVCmZbjmrQI8du8uy7DxSzo_MPyuZk`). OneGuide last updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1: Weekly · Flyer Type 2: Monthly |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

## Files & schedule (Flyer Type #1)

- **When files arrive:** Monday
- **Publication cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday
- **Processing type:** Auto-stack
- **Linking document:** sent via email to the processor — flag if not attached to ClickUp.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu on the right → Confirm & Upload. Once pages are listed, Auto-Group or manually enter page numbers in the Grouping Number field. Ensure correct language (English). Save & Confirm.
- **Pricing zones (two, order matters):**
  - **PZ 1: NSIG** — add all NSIG (Signature) pages in order. Save and Next.
  - **PZ 2: NS** — add all NS (Source) pages in order. Save and Done.
  - Assign all Nature's Source stores to the NS zone and Signature stores to the NSIG zone.
- **Attach tagging document to all vendor tasks** (usually via email — reach out to Processor if not attached to ClickUp): Vendors → upload mass attachment → select all vendors and choose the XLS.
- Wait for sessions to run. Thumbnails — Standard 4.

### Setup QC (owned by Flex)
- Check dates match the first page of the PDF; no theme; available everywhere. Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- Look for multiple products in a block.
- **Two separate pricing zones** — keep NSIG and NS pages in order and assign the correct stores to each zone; do not mix them.
- Missing linking/tagging document — flag if not attached to ClickUp.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON, linking document required)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block with a price and/or sale story.

**Tag / Tag QC (Low complexity — Auto-tag OFF, linking document required, PDF Image Auto-Selection ON)**
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Box Draw/Box QC specific.
- **Exclude:** pre/postfix, valid dates.

**Image QC**
- Standard image QC (correct vs. incorrect image selection).

## Post-processing — Final QC (owned by DOC)
- **Check URLs:** open the linking document attached to vendor tasks; review every link on each page (use the correct EN or FR tab). Add a comment "All links checked" when done.
- Spotchecks if required; QC thumbnails (Standard 4); Edit Details = available everywhere, no external run name, run dates match last page of PDF; check items without URL; flag missing pages or geography changes.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex). Checklist covers Edit Details (dates, no theme, no external run name, standard leg heights, thumbnails), Pricing Zones (interactive previews, boxes), Geography (no FSAs/stores added/removed).

## Out-of-processing
- Instructions for page swaps, post-live checks, etc. (per the OneGuide).

---
*Source: Nature's Source and Nature's Signature OneGuide (Google Doc `12HVgAJGpncuJPKVCmZbjmrQI8du8uy7DxSzo_MPyuZk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nebraska Furniture Mart — Processing Guide

> **Source:** Nebraska Furniture Mart OneGuide (Google Doc `1EcO1fTUSazQS82hr6DzGft-GyV1k56Nq0HMGzCoPowE`). OneGuide last updated Oct 22, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Most: all platforms. **Flooring: hosted only** when it doesn't meet content policy |
| Slack channel(s) | `#nebraskafurnituremart` |
| Hosted URL | http://www.flyertown.ca/flyers/nebraskafurnituremart |
| Flyer type(s) & cadence | 2939: Weekly, Bi-weekly & Ad-hoc (4–6 flyers go live most weeks) |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

## Files & schedule (Flyer Type #1)

- **When files arrive:** Tuesday
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available To Wednesday, Valid To Thursday. **Varies publication to publication — always check what the flyer says and the shared client link document.**
- **Processing type:** Auto-stack
- **Linking document (Flipp Direction Document):** *sometimes* in the FTP; mass-attach to vendor tasks if present.
- **Workflow:** Upload & Setup (Flex) → FQC (Vendor)

## Upload & setup

### Full-time processor pre-upload step — building flyer shells
- A [Shared deep link doc] tracker is used to build shells in advance. If columns A–D are filled but column E is blank, you need to build shells.
- To build new runs: open the Flyer Schedule Creator → copy flyer names from column A into the creator's Name column → adjust available/valid dates to match the tracker → download as CSV → in Fadmin, go to Merchant Schedules, search "Nebraska Furniture Mart", upload the CSV and click **Upload Schedule**.
- Confirm the number of shells built matches what the merchant requested. File a Project Management Queue (PMQ) ticket for each run. Populate the deep links back into the tracker (Concat tab → paste flyer id into column B → link auto-populates in column C → paste as value into column G of the Current Ad tab).

### Setup instructions (Weekly flyers)
- Usually 4–6 flyers go live weekly (mostly Wed–Thurs runs). Repeating versions: Online, DM Online, Flooring, Bedding, Mrs B's ROP, etc.
- **Manual upload:** select files from the **lowercase** folder for each run based on its Internal Name. NOTE: Mrs B's ROP is usually only 1 page → appears under the **uppercase** folder (also Lift and Lighting sometimes). Best practice: after uploading all flyers, check the SFTP (Merchant Page > Details > View Files) with "Hide Uploaded" to catch any missed pages.
- Auto-group, then Save and Complete.
- **Flyer Creation task — pricing zones by store:** they have **4 stores: OM, KC, DM, TX**. Store codes are part of the file names. Name each PZ after the store(s) (e.g. a file set for OM/KC/TX → one PZ named `OMKCTX`; region-specific pages → separate OM, KC, TX zones). Files with **"NFM.com ONLY"** in the name display on hosted only — hide on Flipp and distribution (Overview > Edit Details). Flag to DOC if a flyer has no stores referenced in its file names. Save and Done.
- Add the correct store(s) per version based on the PZ name.

### Setup QC (owned by Flex)
- Overview > Edit Details: check valid dates against flyer page assets (usually page 1, occasionally last page); no preview (available and valid dates are the same); give an external name based on the titular messaging on page 1 (e.g. "Memorial Day Sale").
- Generally **No Theme** unless around a holiday.
- Standard 4 thumbnails (thumbnail_1065_x_600, stock_premium, storefront_carousel_premium, storefront_carousel_organic).
- Mass-attach the linking document if present. Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- **Content policy:** Flooring ads generally don't meet content policy (fewer than 6 items total, or under ~3 items/page average). Hide such ads on Flipp and distribution and leave a comment ("Hidden on Flipp/Distribution because this does not meet content policy"). 1-page ads must have at least 6 items.
- **Store assignment source of truth is the page file names** (e.g. "1115 Online Omkc P0001" = OM and KC only; DM and TX correctly left out). Geography is not always the same as another run — verify per run.
- **Inverted/upside-down images:** if an image is inverted, select "Do Not Use PDF Images."
- Cadence dates vary each publication — always confirm against the flyer and shared link document.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc rarely needed for catalogues)**
- **Include:** packaged deals (e.g. washers/dryers).
- **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks, financing options.
- Single item: box the entire image even if it includes different SKUs of the same item type. Use **text boxes** only when you can't avoid including another product. Multi-item/bundles displayed together can be boxed together. **Bundled items with different original/suggested retail prices → box and tag separately.**

**Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Selection ON) — Tag Lite retailer**
- **Do NOT tag:** Brand, Description, SKU, Sale Story.
- **Include:** name, pre/postfix, valid dates, price, categories, original price.
- **Exclude:** brand, description, SKU, sale story, disclaimer, URLs (unless a URL doc is provided).
- **Valid dates:** zoom out of flyers to check for valid dates — must be entered for every item where the availability differs from the run dates (e.g. Doorcrashers, New Releases). "Good Tomorrow"/"Good Through" → valid for that one day only. "Available Tuesday" → put the date in Item Valid From, leave Item Valid To blank.
- **Categories:** every item needs one; most common are Furniture, Beds & Mattresses, Appliances, Electronics.

**Image QC**
- Use clean PDF whenever possible; select cutouts when clean PDFs aren't available. Watch for inverted/upside-down images → "Do Not Use PDF Images."

## Post-processing (owned by DOC/Flex/Vendor)
- **Item Category QC (DOC):** one category per item; most common are Furniture, Beds & Mattresses, Appliances, Electronics.
- **Item Image QC (DOC):** clean PDF where possible; watch for inverted images.

## Pre-/Final QC (owned by Vendor)
- Mark Autostack Spotcheck complete.
- Overview → Edit Details: check external run names set (if not, use page 1 callouts, e.g. "Veterans Day Sale"); avoid duplicate external names (use "More Ways To Shop" or the flyer name); check thumbnails (Standard 4 — for 1-page ads the NFM logo should show in the thumbnail even if at the bottom of the page); under Ad Hoc Processing, open Manage Tracking Codes → Apply All Tracking Codes, and **Mark items in store only**.
- Pages tab: check run dates (usually bottom-right of page 1); apply one category per page (except page 1s).
- Pricing Zone tab: Item View — everything boxed; full-screen/vertical previews scroll and items are functional; stores assigned to all regions; hide ads failing content policy with a comment.
- Geography: source of truth is page file names; geography may differ from other runs.
- Complete FQC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Page swaps happen occasionally. The retailer emails item-update requests and sends new files through the SFTP. Flex team can action with a FAB ticket.

---
*Source: Nebraska Furniture Mart OneGuide (Google Doc `1EcO1fTUSazQS82hr6DzGft-GyV1k56Nq0HMGzCoPowE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nesters Market — Processing Guide

> **Source:** Nesters Market OneGuide (Google Doc `1s-Du9XY4DYUmZEYHbK0CW7aM5oZFpJQK10ND6wgyZyI`). OneGuide last updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#buylowfoods` |
| Hosted URL | http://www.buy-lowfoods.com/ |
| Flyer type(s) & cadence | 9323: Weekly · Flyer Type 2 (Eat Well Live Well): Monthly |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

## Files & schedule (9323 Weekly)

- **When files arrive:** Thursday
- **Publication cadence:** Available From Wednesday 3 AM, Valid From Thursday 3 AM; Available To Thursday 2:59 AM, Valid To Wednesday 11:59 PM
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC)

## Upload & setup (owned by Vendor) — codesheet build

1. **Download versioning document from the FTP** to check for more than one version (search "NM" to find it).
2. **Manipulate the codesheet:** go to the Store Versioning tab and delete the Store IDs tab; **delete the first 4 rows; delete columns A, G and H.** If applicable, Ctrl+F → Find ".pdf", Replace with nothing. Copy and paste columns A, B, C into a Google Sheet.
3. **Upload codesheet:** Name = `upload`; upload the codesheet CSV; **Config name = `overwaitea`**; PDF Base Directory taken directly from the SFTP.
4. Check the SFTP (search `/NM`) to confirm all pages uploaded.
5. Mark Flyer Creation complete.

*If Monthly pub: manual upload, no preview, available and valid the same — into the Eat Well Live Well flyer type.*

### Setup QC (owned by Vendor)
- Edit Details dates: **Available 3 AM two days before live date; Available To 2:59 AM one day after last live date; Valid From 3 AM; Valid To 11:59 PM.**
- **Do NOT use an external run name.** No theme. Fab 4 thumbnails. **Leg heights 50 × 40.** Scroll through the pub and confirm the logo is prominent. Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- **Valid and Available dates must be set correctly.** Available From: Wed 3:00 AM; Available To: Thu 2:59 AM; Valid From: Thu 3:00 AM; Valid To: Wed 11:59 PM. **The "Available To" date/time is 3 hours AFTER the Valid To — this is correct.** The Available To and Valid To dates should **NOT be the same day.**
- **Alternate pricing per KG** (Weekly & Monthly) goes in the **description**, not the postfix. Example — Name: New York Strip Loin Roast; Description: Canadian AA or Better Grades of Beef, 19.80/kg; Current Price: $8.98; Postfix: lb.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)**
- **Include:** retailer logo, sign-up page, special weblinks.
- **Exclude:** coupons, packaged deals, social media.
- Box all items with prices, using text boxes when necessary. For overlapping products, box the text rather than the image. Items with different prices boxed separately.

**Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Selection ON)**
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. Brand is Box Draw/Box QC specific.
- **Exclude:** URLs.
- Name/Brand = bolded first text; non-bolded text below is the description. Include "ea"/"kg" in postfix; include "_ for" in prefix.

**Image QC**
- Use a clean PDF image if available — **almost all items will have a usable clean PDF** (do not use if the product is cut off). Use the cutout only if no clean PDF is available.

## Final QC (owned by Flex)
- Mark auto-stack off; complete Ops spot checks if applicable.
- Edit Details dates (Available 3 AM Wed 1 day before live; Available To 2:59 AM Thu; Valid From 3 AM Thu; Valid To 11:59 PM Wed).
- Check PDF dates match the flyer run (there is a 1-day preview). **No external run name.** Draw 4 standard thumbnails. Check geography.
- Page categories on all but the first page. Check items for special sale dates.
- **When you see a Rewards page, tag it with** `https://www.nestersmarket.com/morerewards/`.
- Check horizontal and vertical previews. Complete Final QC list.
- **Flyer sorting order: Current WEEKLY, PREVIEW OF NEXT WEEK, MONTHLY.**

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Page swaps / post-live checks per the OneGuide.

---
*Source: Nesters Market OneGuide (Google Doc `1s-Du9XY4DYUmZEYHbK0CW7aM5oZFpJQK10ND6wgyZyI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# No Frills — Processing Guide

> **Source:** No Frills OneGuide (Google Doc `1WxiPhTSRu9E6GKprVabRcRWgie01RowLXWkEwhHlLO0`). OneGuide last updated May 31, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Loblaw/LCL) |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#loblawops`, `#loblaw-lcl`, `#3fl-loblaws` |
| Hosted URL | https://www.nofrills.ca/ |
| Flyer type(s) & cadence | 3800: Weekly (three regional versions: **NFO** Ontario, **NFA** Atlantic, **NFW** West). 9375 Global Foods flyer no longer used. |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

> **Note (Jan 19, 2026):** publishing in English and French with Cross-Language zones (retailer request — pending).

## Files & schedule (Weekly)

- **When files arrive:** Thursday
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available To Tuesday, Valid To Tuesday. **NFW (West) version is available & valid from 3 AM.**
- **Preview date:** Sunday
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor, ~4 days out) → FQC (DOC with Vendor Pre-FQC) → Article Number Corrections (live date) → Multiple Page Revisions (post-live)

### Custom action — Article Corrections in FAdmin
- To download the Article Corrections report, run the LCL custom action **"LCL Article Number Report."**

## Upload & setup

### Pre-setup (owned by DOC) — codesheet generation
- Prior to the FTE's upload shift, COC/COL must drop the final codes in the shared LCL Codesheet Drive.
- You receive one codesheet each for **NFA, NFW, NFO** (separate emails). Upload to the LCL Codesheets No Frills folder; move the old week's codesheet to the Old Files folder. **Revisions come in as the week progresses — always update the folder to the most recent version before Friday's upload shift.**
- Use the **Loblaws Codesheet Automations** Colab notebook to generate a **Generic Codesheet** for FTEs:
  - Run the **SFTP List Tool** block; enter the base path matching the codesheet (e.g. `/NOFRILLS_ATLANTIC/WK_20_NFA`) — grab from the FAdmin SFTP page if unsure. Produces `SFTP List.csv`.
  - Upload the codesheet `.xlsx`, run **1. Match Files** → downloads a Translation Key; import into the Google Sheet codesheet.
  - **Review the matched File Codes and File Names for 100% accuracy** — check one version of every unique page; watch complicated flap names (e.g. `FLAP 1D M`) and 10 K-zone page version matches. Some matches report confidence even when wrong. Correct any mismatch across every version and zone.
  - Run **2. Generate Generic Codesheet** → auto-downloads. Upload to the No Frills folder and update the 3FL LCL Processing Tracker so FTEs know it's ready.

### Setup (owned by Vendor)
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded** into the flyer run (Open flyer run → Edit Details → show/hide rarely-used fields → Height dropdown → 4096.0 pixels → OK). If pages were added before this step, flag to the Full-Time Ops stakeholder and continue.
- **Codesheet upload:** identify the week/run from the 3FL LCL Processing Tracker; download the run's `Generic_Codesheet_WKxx_NFx.csv`. Upload to the Codesheet tab using **config name `generic`**, base path from the SFTP (making sure you grab the ON, WEST or ATL folder), and **select all toggles but the second and last.**
- After running, mark Flyer Creation complete. Go to Geography, select the matching flyer (ON/WEST/ATL), and confirm it reads **"No Stores or FSAs/zips were added or removed!"** Flag discrepancies in `#3fl-loblaws`.

### Setup QC (owned by Flex)
- Edit Details: **Preview Start Date** = the Sunday before Available From; Available From Wednesday, Valid From Thursday; Available and Valid To the Wednesday after it starts.
- **NFW (West): Valid From time set to 3:00 AM** (time-zone offset). **NFA and NFO stay Valid From 12:00 AM.**
- No theme unless specified. **External Run Name = `Weekly Flyer - Valid Thursday, MM DD - Wednesday, MM DD`** (must match the VALID date range, not Available).
- Mark Autostack Spotcheck complete. Complete Setup QC checklist.

### ⚠️ Common errors / risk items — codesheet upload
- **Multiple-file FTP match warning:** if the only warnings are "The following files matched multiple files on the FTP," hit **Force Processing** and proceed.
- **Store errors:** if errors mention missing stores, flag to the full-time processor in `#3fl-loblaws` — likely a new store or store-code change; rerun after they update.
- **Missing store (4-digit code) truly absent from FAdmin** → likely a new store opening: remove it from the codesheet and note it in the flyer-run comments for the FT processor to create.
- **Extra row / merged cells** → copy the URL from the 2nd row into the cell above and delete the 2nd row (one page = one row).
- **"Store 8, 9, 10 does not exist"** (1–2 digit store code error) → pagination issue: confirm page order has accurate, non-skipped numbers.
- **Page can't be found in SFTP but you can see it** → name formatting: e.g. codesheet `NFO FLAP 1 D` vs SFTP `FLAP1D` (no spaces) — remove spaces and rerun.
- **NFW Valid From must always be 3:00 AM** (West-coast time difference).

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)**
- **Include:** coupons, packaged deals, sign-up page, social media, special weblinks.
- **Exclude:** retailer logo.
- Box where there is a unique price; box only the item. Box any banner with a `nofrills.ca` link (**do NOT box or tag Facebook, Twitter, etc.**).

**Tag / Tag QC (MEDIUM complexity — Auto-tag OFF, linking document required)**
- **Include everything:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Box Draw/Box QC specific.
- **Name:** ALL CAPITAL letters, order "Brand Product Name, Quantity" (always a comma before the quantity). English only — French goes in the description. Do **not** include in the name: metrics like "6.59/kg", "Product of…", "No 1 Grade", "Frozen", "Selected varieties" (these go in the description).
- **Description:** flyer info only (not from the website); first letter capitalized; do not enter the NG code or SKU here.
- **SKU:** starts with "2"; if it does not start with 2, ignore it. Drop leading zeros before the article number. Include the unit of measure (e.g. `_KG`) in both SKU and Article Number fields.
- **URLs:** after entering the SKU, click **Fetch** to populate the URL. If it leads to a different item or a different size → remove and find the correct item by product name. If it leads to the No Frills home page → leave it. If it leads to the correct item but a different flavour → leave it. **All items with a SKU will have a URL.**
- **Article Number fields** (special tagging fields at the bottom): paste the product SKU into Article Number 1 (matching SKU + Fetch URL), including the unit of measure. Multiple SKUs → Article Number 1/2/3/4 in order.
- **Valid Dates:** include date overrides only when a promotion sales story on the item indicates it.
- **Prices:** watch for MULTIBUY items (prefix + postfix combos); PC Optimum Members Pricing = Current Price with a "PC Optimum Members Pricing" prefix.

**Image QC**
- Use clean PDF where possible; use the cutout if the PDF is not clean.

## Post-processing (Pre-FQC)

- **URL/Links QC (Vendor):** reference the Final Codes — pages with links are noted in the Notes/URLs column (column E). Box the linked area (often the header; look for Click Here / Shop Now buttons).
- **Thumbnail QC (Vendor):** Standard 4 thumbnails, starting on the first page the logo appears (not always page 1).
- **Merge Flaps (Vendor):** in the Storefront Spotcheck of the first Pricing Zone, merge all skinny pages (mostly "FLAP" pages).
- **Article Number/SKU check (Vendor):** Item Search for Article Number 1 IS [BLANK] (Item Type = ITEM) and SKU IS [BLANK]; add any missing values from the PDF and Fetch the URL. Note RWSS (and sometimes RCSS) often print items without article numbers/SKUs — goal is not zero results, only to catch mistags.
- **Pre-FQC (DOC):** mark Autostack Spotcheck complete; leg heights auto-set to 45/25; check thumbnails (Standard 4, start at logo); Image QC needs no re-check (PDFs auto-selected/reviewed in tagging); confirm all items QC'd and URLs added; confirm flap pages merged; **Geography — very common to have a store flip (store code update) or a new store opening; refer to the codesheet submission email and flag missing stores to the Loblaws contact.**
- **Flyer sorting (DOC):** Flyer Type → Newest First — order: Upcoming, Current, then Secondary pubs newest→oldest. Watch `#flyer-sorting-alerts`.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Live-date flags for OS
- **URL** leads to a different item → FLAG.
- **Description** contains item quantities → FLAG.

## Out-of-processing
- **Article # revisions:** run the LCL Article Number Report custom action (see the LCL Article # Report SOP).
- **Deep link requests:** use the Loblaws Deep Link Sheet.
- **Page swap:** standard process — exception: swapping a Flap page requires remerging the revised page in the Storefront Spotcheck of the affected Pricing Zone. Page swaps often cause page-stitching issues (page doesn't match overlaid items), especially post-live; best practice is to **always rerun Page Tile Generation** after the swap sessions kick off, and confirm success across all pricing zones' item views.

---
*Source: No Frills OneGuide (Google Doc `1WxiPhTSRu9E6GKprVabRcRWgie01RowLXWkEwhHlLO0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Notre Dame Home Furnishings — Processing Guide

> **Source:** Notre Dame Home Furnishings OneGuide (Google Doc `1ZZVgnx2Iie-wUUgfRmYDyT-Mvy97JZPbEvET_lC9GX8`). OneGuide last updated Dec 12, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#notre-dame-agencies` |
| Hosted URL | https://www.notredamehomefurnishings.ca/en/pg-flyers |
| Flyer type(s) & cadence | Flyer Type 1: Flyer (11079) — Ad-hoc |
| Processing | Auto-stack |
| Involvement | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc (sent by the retailer contact via email)
- **Publication cadence:** Ad-hoc (available/valid from and to all ad-hoc); no preview; no linking document
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (DOC) → FQC (DOC)

## Upload & setup (owned by DOC)

- Files come in by email; the sender states any versions.
- **Manual upload, English only.**
- Flyer Creation — create whatever pricing zones are needed based on the email; make sure NL/GB versions have the appropriate pages. Complete Setup QC.

### ⚠️ Common errors / risk items — pricing zones
- **Check which zone the email specifies:**
  - **Island of Newfoundland only** = **NL — excluding Goose Bay** store set
  - **Goose Bay** (sometimes "GB") = **Goose Bay** store set
  - **All stores** = all stores

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each item and SKU individually; use text boxes as required.

**Tag / Tag QC (Low complexity — Auto-tag OFF)**
- **Include:** brand, name, price, categories; description / sale story / disclaimer if available.
- **Exclude:** pre/postfix, valid dates, SKU, original price, URLs.

**Image QC**
- Use clean PDF images whenever available; otherwise item cutout images are fine.

## Post-processing
- **Item Image QC:** standard image QC completed by OS — no additional actions.
- **Final QC (DOC):** Standard 4 thumbnails; no theme; available everywhere; complete FQC in pipeline.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

---
*Source: Notre Dame Home Furnishings OneGuide (Google Doc `1ZZVgnx2Iie-wUUgfRmYDyT-Mvy97JZPbEvET_lC9GX8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# NSLC — Processing Guide

> **Source:** NSLC OneGuide (Google Doc `12-GZvxv-XFUm0eLezebG0nTrwWIsBMAq471rVaSLXn0`). OneGuide last updated Feb 23, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | **Available on Flipp only** (hidden on Hosted and Distribution) |
| Slack channel(s) | `#nslc`, `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1: Monthly (9896) — also has ad-hoc publications; cadence changes |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc
- **Publication cadence:** Ad-hoc (typically monthly but varies). No preview — Available From = Valid From, Available To = Valid To.
- **Linking document:** Yes — should be attached to all tasks.
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup (owned by Vendor)

- Files are dropped in the SFTP.
- **Manual upload:** Pages → Edit → select the pages for that publication → Auto-group → Save and continue. When Flyer Creation is available, start the task → create one pricing zone named **`base`** → add all pages → Save and continue.
- **Attach the linking document from the FTP to all vendor tasks.**
- Overview > Edit Details: no preview (Available From = Valid From, Available To = Valid To). **Hide in Hosted will already be checked.** Internal run name can be the same as the start date. No theme.
- Standard 4 thumbnails (thumbnail_1065_x_600, stock_premium, storefront_carousel_premium, storefront_carousel_organic).
- Let sessions run, then begin Setup QC checklist.

### ⚠️ Common errors / risk items
- **Flyer dates: use the Merchant's email as the source of truth, NOT the flyer pages.** The dates on the flyer pages often differ from the posting instructions used to create the run — the merchant frequently gives posting timelines that do not match their print distribution schedule.
- Confirm the linking document is attached to all tasks (used for both Box and Tag).

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF; linking document required for both Box and Tag)**
- **Include:** special weblinks.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Box each item individually. Box any banners with calls to action or links.

**Tag / Tag QC (HIGH complexity — Auto-tag ON, PDF Image Auto-Selection ON; linking document required)**
- **Include:** brand (Tag/QC specific), name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Exclude:** pre/postfix.
- Tag Product Name + Brand. SKU is on the bottom of the product (and on the linking document). Tag URLs per the attached URL sheet.
- **Watch for special sales (2- or 3-day sales):** if item valid dates differ from the flyer's valid dates, enter them in the valid-date override fields.

**Image QC**
- If the **FIRST ITEM** listed has a **clean PDF image with a white background**, select it; otherwise select the cutout. For multiple items, always select the first product listed in the item name; if the first brand's image is unavailable or not clean, select the cutout.

## Final QC (owned by Flex)
- QC thumbnails (Standard 4).
- **All items have URLs** — if any are missing, open the linking document.
- Geography: no change.
- **Flyer dates match the email** (not necessarily the printed flyer dates — see risk item above).
- Complete Final QC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex). Hide in Distribution, Hide on Flipp? — **live when valid (dates on PDF)**; hide on Hosted checked; custom tile (usually); preview items clickable; check a few links; geo consistent.

*(Note: the review table shows "Hide on Hosted" checked while the account overview states Flipp-only — treat the linking-document/email dates and the checked Hosted toggle as authoritative per the run setup.)*

## Out-of-processing
- Page swaps / post-live checks per the OneGuide.

---
*Source: NSLC OneGuide (Google Doc `12-GZvxv-XFUm0eLezebG0nTrwWIsBMAq471rVaSLXn0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Nutters Everyday Naturals — Processing Guide

> **Source:** Nutters Everyday Naturals OneGuide (Google Doc `1MAYyV_xB2nYPgEZKhi8Zp6lsi2GYtY4rPigiv4dKULY`). Instructions updated Jan 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#onboardings`, `#flex-processingsupport` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1: Weekly (files ad-hoc; publication monthly) |
| Processing | Auto-stack |
| Involvement | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **When files arrive:** Ad-hoc (sent via email)
- **Publication cadence:** Monthly; no preview; no linking document
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Flex) → FQC (Flex)

## Upload & setup (owned by Flex)

- Files sent via email.
- Build **1 zone, English, containing all pages, assigned all stores.**
- Complete the Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Single items:** main box contains just the item (minimal white space in the cutout), plus a text box comprising the entire item area.
- **Two-size items:** box each size as its own item (overlap is OK); each instance gets a text box with its size and unique price.
- **Blanket-price half-page items:** box these.

**Tag / Tag QC (Low complexity — Auto-tag OFF)**
- **Include:** name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, URLs.
- **Exclude:** brand, valid dates, original price.
- **Disclaimer risk item:** tag "Made in Canada" or "Product of Canada" in the disclaimer of any item bearing the maple-leaf image.

**Image QC (DOC)**
- Standard image selection (correct vs. incorrect).

## Final QC (owned by Flex)
- No special risk items — use generic flyer review standards. QC thumbnails completed.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex). No special risk items.

---
*Source: Nutters Everyday Naturals OneGuide (Google Doc `1MAYyV_xB2nYPgEZKhi8Zp6lsi2GYtY4rPigiv4dKULY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
