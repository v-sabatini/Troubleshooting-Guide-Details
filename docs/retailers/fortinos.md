# Fortino's — Processing Guide

> **Source:** Fortinos OneGuide (Google Doc `1QyBENb3RH4866Cqyz4gCUAwUjSOuagRlFMkk65mnkdI`), updated Aug 28, 2024. Contacts/credentials omitted.

Loblaw-family (LCL) account. Pricing zones are built from the retailer's OLS codesheet and change week to week.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer types | Weekly (FT 3800) |
| Processing | Auto-stack; Flex (Flyer Review); **OS — Setup**; **Feedel/retailer data services YES**; no coupons |

## Files & schedule
- **Files arrive:** Monday.
- **Cadence:** Available From Wednesday; Valid From Thursday → Available To Monday; Valid To Tuesday.
- **Preview date: Sunday.** Workflow: Upload/Setup (Vendor, 5 days out) → FQC (DOC, 2 days out) → Corrections (1 day out).

## Upload & setup (owned by Flex)

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → show/hide rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were already added, flag to the Full-Time Ops stakeholder and continue.

**Codesheet manipulation:**
- Retrieve that week's xls from the Codesheet Drop Box → Fortinos folder (week # on the xls matches the flyer number on the Flex LCL tracker).
- Open the **Online OLS tab** — top = flyer run dates; middle = pagination + which stores get each page (every unique page combination = its own PZ, changes weekly); bottom = store list + which inserts each store receives.
- Determine PZs from the store-assignment section (e.g. a typical week: Base with no inserts; CI with 4 PZs; SA with 1; VT with 3 → 9 PZs total).
- Copy from Row 8 to the last row with pages listed into a new week tab (e.g. "WK 4") of the Fortinos Manipulation Document at Row 8.
  - **Delete Kosher / Eastern Euro pages** — they don't share the same PDF path and will cause a codesheet error.
  - In cell A8, delete "OLS" and copy those rows; paste the block **9 times** (one per PZ), leaving a blank row between each, then manipulate each to match the required PZs.
- After uploading, **attach the linking document to all vendor tasks.**

### Setup QC (owned by Flex)
- Set a **Sunday preview**: Overview → Edit Details → "Preview start date" → the Sunday before the available date → OK.

## ⚠️ Common errors / risk items
- **Pixel height must be 4096 before pages are uploaded** (2026 change).
- **Kosher / Eastern Euro pages** must be deleted from the codesheet before upload (different PDF path → codesheet error).
- **URL leads to a different item** → FLAG. **Item quantities in the description** → FLAG.
- **SKU** must start with "2"; ignore any SKU that doesn't; keep unit-of-measure suffix (e.g. `_KG`) in both SKU and Article Number fields; strip leading zeros before the article number.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking document required):** **Include** coupons, packaged deals, retailer logo; **exclude** sign-up page, social media, special weblinks. Box each unique price; box only the item (not banners/social icons); box items/sections with a URL on the linking document; box PC offers with a URL.
- **Tag / Tag QC (Medium; Auto-tag OFF; linking document required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name** all caps: Brand, Product Name, Quantity (comma before quantity); product name = bold text.
  - **Description** = non-bold descriptive text; do not include NG code or SKU.
  - **URLs:** enter SKU then click **Fetch**. If the link goes to a different item/size, remove it and find the correct one on nofrills.ca; No Frills home page → leave link; correct item different flavour → leave link. All items with a SKU will have a URL.
  - **PC Optimum:** tag as normal item, sale story includes PC Optimum points. **PC Financial:** tag as Link with the PC Financial URL.
  - **Article Number** fields: copy Product SKU into Article Number 1 (incl. unit of measure); multiple SKUs → Article Number 2, 3, 4.
  - Link-only items: item type = **"link"**, not "item".
- **Image QC:** use clean PDF where possible; cutout if PDF not clean.

## Post-processing (owned by DOC)
- **Pagination QC:** check for a revised codesheet in email; use it; on the OLS tab, expand versions from the yellow-boxed columns.
- **SKU QC:** item search — SKU blank (add back if on flyer); SKU not blank + URL blank (Fetch + save); SKU not blank + Article #1 blank (add SKU to Article #1).
- **Link QC:** check the codesheet OLS tab URL column; ensure links added and item type = LINK.
- **Ad-hoc:** before FQC, rerun Page Tile Generation and Page Stitching.
- **FQC checklist** (DOC): risk items, overview tasks, pages, pricing zones, sessions, vendors, geography.

## Flyer review
- **Type: Lite.** Owned by Flex.

## Out-of-processing
- Put flyer run ID in the LCL tracker; run ghostscript 9.06 gamma as needed; flyer sorting (current weekly — regular then ethnic; upcoming weekly; secondary pubs newest→oldest); Article # revision.
- **Page Swap:** standard baseline page swap.

---
*Source: Fortino's OneGuide (Google Doc `1QyBENb3RH4866Cqyz4gCUAwUjSOuagRlFMkk65mnkdI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
