# Shoppers Drug Mart / Pharmaprix — Processing Guide

> **Source:** Shoppers Drug Mart / Pharmaprix OneGuide (Google Doc `1TMYtB4aNKGB4YoWCWIN3w5QI6jMuWr3TFFSvAVZ6gmA`), updated Dec 1, 2025. Contacts/credentials omitted.

**Pharmaprix is the Quebec brand for Shoppers Drug Mart (SDM)** — same content, cloned from the SDM run during Pre-FQC (no separate upload) so Quebec users see "Pharmaprix" branding.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#shoppersdrugmart`, `#shoppers-drugmart-amp-prod`, `#loblawops`, `#loblaw-lcl` |
| Flyer type(s) | Weekly (3800) |
| Processing | Auto-stack; Flex Processing Support; Feedel/Strategic Ops **yes**; no coupons |

## Files & schedule

- **Files received:** Tuesday (page PDFs and store distributions come from different sources — see OneGuide).
- **Cadence:** Available From Thursday, Valid From Sunday; Available To Saturday, Valid To Saturday. **2-day consumer preview starting Thursday.**
- **Linking document:** no.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC/Flex).
- **Live-date postal codes:** use **M1B 0A3** for SDM, **G0A 1H0** for Pharmaprix; use an **Ontario pricing zone** for Preview QC.

## Upload & setup (owned by DOC) — two codesheets

### 1. Stores & Pricing Zones
- Download the weekly Store Distribution list (`SDM_StoreZoning_Wk#_202#`), apply a filter to the whole sheet.
- **Delete all "Count" rows** (column J "Version").
- **Rename all "Base" rows to "QC NAT"** — these become the Pharmaprix zones later.
- **Test stores:** filter "Test" and map to regular digital pricing zones using the SDM TEST PZ reference (VLOOKUP the PZ names).
- Download as `.csv` → SDM flyer run → Codesheets tab → upload: Config **`shoppers_drug_mart_stores`**, PDF directory `/`, **all toggles except 2nd and 3rd.**

### 2. Pagination
- Download the weekly Pagination codesheet. Delete Wellwise rows and Store-specific/Grand-Opening (GO) version rows — leave only NAT and QC. Label NAT "National Pagination" and QC "Quebec Pagination"; replace NATIONAL/QUEBEC with "WITH FOOD" / "WITHOUT FOOD" per whether the pagination includes the FOOD page. Delete GO flap tabs.
- Clean each Page Name tab (delete non-page-name columns). In the Wellwise tab keep only **WW 01**.
- Align names to the **Reference Table**: the A1 cell of each Page Name tab (Dates + Page Name — the config reads this cell, not the tab name) and the matching Pagination-tab name must both match. Each page name in the Pagination tab must be followed by a **two-digit** page number (`##`, with leading 0).
- Upload the `.xlsx`: name **`pages`**, Config **`shoppers_drug_mart_pages`**, base path from FTP, **all toggles except 2nd and last.**

### ⚠️ Codesheet error risk items
- **Hidden rows/columns** (should have been deleted by the retailer) make Fadmin read stale data and error on the pages codesheet — check every tab and delete hidden rows/columns carefully.
- Using **"COSMETIC"** from the reference table: Fadmin may read only "COS" and error — switch to a different reference-table word.
- FTP errors: may just be re-flagging previously uploaded Wellwise pages → ignore and Force Processing. Otherwise check the path (no leading/trailing spaces), file names (wrong page/week #, case mismatch — try `WKXX` → `wkxx`), read the error, or escalate to CLSD.
- Ensure all pages uploaded except WW 02, WW 03, and GO. **Upload each page twice — once EN, once FR.** Manually create GO/Store-Specific zones (EN + cross-language FR) if needed.
- **Remove stores from all QC NAT / QC NAT FR zones** (these are the Pharmaprix versions — cloned and re-populated later).

### Setup QC
- Set valid time to start at **3 AM**; remember the 2-day preview from Thursday; confirm valid dates on a Base 01 page (may end Thursday or Friday); ignore the SFTP "pdf pages still present" warning.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Exclude coupons, packaged deals, sign-up, special weblinks. **Include retailer logo and social.**
  - **Products without UPC:** draw ONE box around the ad block; do NOT box individual product images.
  - **Products with a UPC:** box each UPC as a separate item (even if same price); include the UPC via a text box; UPC separated by `/` = one box per product; single UPC = box the block.
  - **Do NOT box/tag Wellwise pages** (Home Health Care Solutions / Wellwise logo) — leave blank.
  - Box special call-outs (gift cards, Seniors Day, flu shots, Health & Pharmacy) — look different each week.
- **Tag / Tag QC — High; Auto-tag OFF.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name/Brand:** enter brand (always bolded) in Brand AND Name only if a single brand; if multiple brands, leave Brand blank; keep flyer casing.
  - **SKU:** UPC has **13 digits**.
  - **URLs:** after entering SKU, click Fetch. If Fetch fails, use base URL `https://shop.shoppersdrugmart.ca/Shop/p/BB_` + SKU. If a fetched link leads to the wrong item, search by product name on shoppersdrugmart.ca and match the size (price may differ). If not found, use the home page.
  - **Special sales (custom tagging):**
    - **1 or 2 Day Sale** (yellow background, circle "1/2 DAY SALE"): postfix = the day of the week (regular postfix like "each" goes *before* the day); sale story = the price for the REST OF THE WEEK after the sale.
    - **3 Day Sale** ("3 DAYS ONLY" red banner): valid dates apply to all items; postfix format `each or $X each with N PC Optimum pts`; **leave sale story blank.**
    - **6 Day Sale / Week Long Sale:** these are the flyer's own valid dates — **do NOT enter into valid to/from fields.**
  - **Sale story:** enter as-is; always tag **"PC Optimum"** (not just "Optimum"); free gift → "YOUR FREE GIFT (gift) with the purchase of (item)"; add page-bottom disclaimer if there's an `*`.
  - **Categories:** if more than 4 on a page, leave blank; valid categories = Pharmacy, Personal Care, Food & Beverage, Beauty & Skincare.
  - **Images:** PDF first, then cutouts; if multiple items, use the first item in the name; **do NOT select PDF images with a black background/shadow or that are cut off.**
  - **French flyers: ONLY include French text** (EN and FR are sometimes mixed in name/description).

## Final QC / go-live

- **Do NOT tag week-long or one-day PC Optimum valid dates in the override fields** — leave blank (these are the flyer's dates).
- Mark Autostack Spotcheck complete; finish Ops spotchecks.
- 2-day preview from Thursday; leg heights auto 40/30; no image QC; thumbnails standard 4 starting on the Base 01 logo page (exclude flap pages; adjust start position per zone if page counts vary).
- Apply Two-Day-Only valid dates (yellow-background items) via Item Search / mass edit across the first few pages.
- Storefront spotcheck: confirm skinny flap pages are merged (check a few zones both languages — e.g. ON NAT, AB NAT, QC NAT). Item view: all items boxed (**last WW01 page is NOT boxed — 0 clickable is OK**). Remove stores from QC NAT / QC NAT FR. Geography generally same WOW (1–3 stores added/missing OK).
- FQC checklist: "Not all PZs have Stores Assigned" → write "SDM only"; click Complete twice to force save past errors. Check flyer sorting. Message DOC when FQC is complete so they can clone.

## Pharmaprix clone (owned by DOC)

- Clone the SDM run into the same-week Pharmaprix run (start early — large run). Recheck thumbnails and page merges.
- **Only QC zones get stores assigned** (these are the Pharmaprix zones): from the uploaded store list, filter column J to QC NAT, paste to a new tab, download as `.csv`, re-upload the stores codesheet (Config `shoppers_drug_mart_stores`, `/`, all toggles but 2nd & 3rd), re-run.
- Confirm only QC zones have stores; check geography (same as prior weeks); recheck previews (may need the Touch Storefront Objects custom action on 404); re-run lagging sessions.
- FQC as normal: "Not all PZs have Stores Assigned" → write "PHX only"; click Complete twice.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Shoppers Drug Mart / Pharmaprix OneGuide (Google Doc `1TMYtB4aNKGB4YoWCWIN3w5QI6jMuWr3TFFSvAVZ6gmA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
