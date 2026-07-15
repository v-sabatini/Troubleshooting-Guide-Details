# Co-op Food — Processing Guide

> **Source:** Co-op Food OneGuide (Google Doc `1ZTTdhlBPmcBJLfRbAM4WL5uagn0Cybu_wDjtI4K2H1M`), updated Apr 29, 2026. Contacts/credentials omitted.

Federated Co-op (FCL) banner. Five flyer types; the **Weekly (3277)** has the full documented process. The others — Pharmacy (7886, ad-hoc), SK/Saskatoon Liquor (6305, monthly), Saskatchewan Liquor (9942, monthly), Dormant Guide (9427, ad-hoc) — are largely template stubs in the source doc (standard QC tables, no filled-in setup steps).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport`, `#content-team-federated-coop` |
| Hosted URL | food.crs / co-op.crs/flyers |
| Publications | Weekly (**3277**) · Pharmacy (**7886**) · SK Liquor (**6305**) · Saskatchewan Liquor (**9942**) · Dormant Guide (**9427**) |
| Cadence (Weekly) | Files Thursday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule — Weekly (3277)
- Files received **Thursday**. Codesheet + versioning downloaded from FTP (e.g. `Week 27 Food.xlsb`).

## Upload & setup — Weekly (owned by DOC)

### Codesheet
1. Open `Week __ Food.xlsx`, enable editing; go to the **Wk __ Food Flyer** tab; delete the buttons in column A.
2. **Copy that tab to a new book** (right-click → Move or Copy → To book: (new book) → Create a copy) and **save as CSV**.
3. Upload the codesheet: **Config Name = `coop_food`**; PDF Base Directory e.g. `/Weekly/2026/Week 21 Food`; **uncheck the 2nd and last toggle**.
4. **⚠️ Remove any stores added during page upload** — otherwise incorrect stores get added to distribution.

### Stores codesheet
1. Open the Version document from FTP (e.g. `Week 27 Food Flyer Version.xlsx`); create "con"/"clean" columns and **concatenate** column A + B (e.g. `=concatenate(16,"-",1)`); find-and-replace "Food Store -" with nothing.
2. **Watch for stores with incorrect #s:** `2486-64`→**2486-67**, `2872-610`→**2872-61**, `2749-3`→**2749-1**, `2002-2`→**2002-6**. Check the **Omissions tab** to include/exclude stores that week.
3. Save as CSV → upload: **Config Name = `generic_stores`**; PDF Base Directory `/`; **ONLY Store or Store Set Assignment**.

### Links, inserts, setup QC
- Build a linking document: from `Week __ Food.xlsx`, copy rows from each tab into one sheet, delete empty-URL rows, save as **Co-op Food URLs CSV**.
- Add **store-specific digital inserts** if present (check sFTP for "Digital Insert" paths). International inserts have a separate process.
- No theme; 4 standard thumbnails; key message from front page or "Weekly Ad".
- **Attach Co-op Food URLs to Box Draw, Box QC, Tag, Tag QC.** Manually upload insert pages per the associated .xls / client email.
- Setup QC: check the sFTP has no leftover pages.

### International publications (ad-hoc)
- Download the Locations URL.xlsx and the last page (with the location callout); count included stores; use the Coop Foods Generic Codesheet; manually upload pages; create 1 PZ using the first store #/name from the location xlsx; Setup QC.

## ⚠️ Common errors / risk items
- **Remove stores added during page upload** before running the stores codesheet.
- **Store-number corrections** (2486-64→2486-67, 2872-610→2872-61, 2749-3→2749-1, 2002-2→2002-6) and the **Omissions tab**.
- **Date-specific sale items** (usually page 1) must be tagged with **Valid From + Valid To** dates.
- **Co-op Centsibles brand:** any item named "Co-op Centsibles" must have "Co-op Centsibles" in the **Brand** field.
- Watch for pricing zones with an **insert as the first page** — draw specific thumbnails.

## QC specifics — Weekly

### Box Draw (Low; Auto-Box ON, Box QC bot ON; Box Draw/Box QC linking doc)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Each item gets its own box; box banners with links and gift-card callouts.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, **URLs**.
- **Co-op Centsibles** → brand in the Brand field (e.g. Brand "Co-op Centsibles", Name "Co-op Centsibles English Muffins", "### FOR 2", Current Price 5, category Grocery).
- Clean PDF preferred (avoid black/gray backgrounds → cutout).

### Item Category / SKU / URL QC
- Each page gets 1–4 categories (best judgement).
- **URL QC:** Item Search → URL IS NOT `_` per pricing zone; `food.crs` items tagged `http://www.food.crs/`.
- **SKU QC:** use the Links Sharing document to find which item/page gets the SKU; add it on the corresponding page.

## FQC — Weekly (owned by DOC)
1. Autostack spotchecks; Category QC (add page categories if incomplete).
2. Draw thumbnails Standard 4 (special thumbnails for PZs with an insert as first page).
3. Confirm key messages (page-1 callout); confirm inserts added (reference the insert .xls).
4. **Item Search → URL IS NOT `_`** per PZ vs. linking doc; `food.crs` → `http://www.food.crs/`.
5. **Item Search → NAME CONTAINS "Centsibles"** (make Brand visible) → confirm "Co-op Centsibles" in Brand.
6. Check geography vs. the versioning document (stores added/missing).
7. Complete Final QC; **complete flyer sorting — main weekly flyer first**.
- **Flyer Review type: Lite.**

---
*Source: Co-op Food OneGuide (Google Doc `1ZTTdhlBPmcBJLfRbAM4WL5uagn0Cybu_wDjtI4K2H1M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
