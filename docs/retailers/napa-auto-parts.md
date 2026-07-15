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
