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
