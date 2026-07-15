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
