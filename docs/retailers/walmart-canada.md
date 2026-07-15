# Walmart Canada — Processing Guide

> **Source:** Walmart Canada OneGuide (Google Doc `1KjkS5_Ijou8f3A_3Xsfb6PM6E-7JkBG2zDzMmijCpxI`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / **Tier 1 Premium**; relationship quality "Excellent" |
| Availability | All platforms |
| Slack channels | `#walmartcanada`, `#cp-walmartcanada`, `#flex-walmartca`, `#walmart-canada-datservices`, `#walmartcanada-ecomfeedsupport`, `#walmartcanada-offapp`, `#walmartcanada-retaileramplification` |
| Hosted URLs | EN: walmart.ca/en/flyer · FR: walmart.ca/fr/flyer |
| Flyer types | **Grocery/Weekly** (weekly) + Digests |
| Processing | Auto-stack; Flex = 3FL; **Strategic Ops: yes** (Feedel/retailer data services); no coupons |
| Flyer review | **Complex** |

## Files & schedule (Weekly)

- **Files received:** Wednesday. **Preview:** Tuesdays (apply preview date = **Thursday** in setup QC).
- **Cadence:** Available Wed→Wed; Valid Thu→Wed.
- **Linking document:** MMS export attached to the pipeline.
- **Workflow:** Upload & Setup (4 days out) → Check tasks (3) → FQC (2) → Send preview (1).

## Upload & setup (owned by DOC)

Assets needed: PDFs, zone chart, MMS export.

1. Copy zone chart to a new tab, paste as values. **If there is a second pagination chart for TARGETED zones, run two separate codesheets.**
2. Manipulate the new tab: insert 1 row above pagination between event code and page; fill blank/merged cells with page values; fix pagination numbering; download as CSV.
3. Upload codesheet — **Config `walmart_sc`**, use a short base path (end before "SC"/"Digital"), **only the second toggle is unchecked**.
4. **Canadianfood page is not pulled by the codesheet** — manually upload it twice (EN + FR) and allocate to QC PZs per the zone summary.
5. External run name = Flyer (EN) / Circulaire (FR); for digests confirm French names. Preview date = Thursday.
6. Thumbnails: Standard 4 + `first_page_thumbnail_400w` (GO versions done separately). Setup-QC thumbnails: 1065×600, `stock_premium`, `storefront_carousel_premium`, `storefront_carousel_organic`.
7. **Geography should not change** week over week (same 11 stores never re-assigned, no overlaps, no missing FSAs). Change all vendor tasks to **urgent** priority.
8. Manipulate MMS: keep only Name, Featured Item (→ SKU for vendors), Copy Description, URL, Department (→ Category); one tab; download XLS; attach to all vendor tasks.

## ⚠️ Common errors / risk items

- **WIN → SKU (add-to-cart):** Walmart's WIN (their SKU) must be in the **SKU field** or the item shows out-of-stock on walmart.ca. After tasks complete, run the **WIN-to-SKU import** to populate SKU and SKU #2 (`id_1` custom field) from the item report/URLs.
- **Stagger west-zone dates:** BC 3 AM, AB & SK 2 AM, MB 1 AM — update Available/Valid From times for all BC/AB/SK/MB zones (and targeted if present).
- **Make tagging updates across ALL versions of a page** — use item search + page-name versioning (Week#, Year, acronym e.g. SC/DIGITAL, page#, language E/B, region). Watch for late REV pages.
- **URL language parameters:** French items must use `/fr/`, English `/en/`; item-search and fix mismatches. Change any `http:` to `https:`.
- **Vendor/LID pages, banners, Rollback:** box banner links, add LID Media Variant; mass-update Rollback/Chute items to "Banner - Rollback" with the correct EN/FR URL.
- **French accents** spot check: œ é è â ê à û î ô ï ë ç.
- Coca-Cola SSD items require specific brand/term tagging (EN/FR) per the SSD category doc.

## QC specifics

- **Box Draw — HIGH complexity; Auto-Box ON, Box QC bot ON.** Include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box **all Walmart banners** (tag via "Banner URLs" section). Multi-items boxed/tagged separately even if same price.
- **Tag / Tag QC — LOW; Auto-tag OFF, PDF image auto-select ON.** Include brand, name, pre/postfix, valid dates, description, SKU (use MMS file), price, sale story, categories (use MMS), disclaimer, original price, URLs (use MMS). SKU from PDF; URL/category looked up in MMS by SKU (EN/FR columns). Banner URLs (front page, Rollback, Subscribe to Save, Everyday Low Prices, Pharmacy) are listed in the OneGuide.
- **Image QC:** clean PDF preferred; cutouts if no clean image. Multi + single items.

## FQC / post-processing (Feedel + DOC)

- Fill missing URLs via MMS/walmart.ca (cross-reference WIN); add pages to PZs; check no tagging missed (copy CES/Klarna/vendor pages from prior week).
- Category QC (Flex): items w/o analytics category (HBA→health/beauty, infant→baby). Page categories: 2 per page.
- Apply **tracking codes** (Claravine — Flipp + Hosted; credentials in the OneGuide — not stored here). Break down UTM/cmpid params.
- **Clone into "WKXX Non-Ad + Print Dark Stores"** (copy tracking codes), swap store sets per province, delete MB PZ for the test, and build the **Dark FSA report** (export prior dark FSAs, rename PZ headers to `flyer_id`/`fsa`, assign via "Assign FSAs From CSV"). Re-run FSA manipulations any time new pages are uploaded.
- **Custom actions:** Remove Stores, Remove FSAs (two batches for character limits), Assign FSAs From CSV.
- **Flyer Review: Complex.**

---
*Source: Walmart Canada OneGuide (Google Doc `1KjkS5_Ijou8f3A_3Xsfb6PM6E-7JkBG2zDzMmijCpxI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
