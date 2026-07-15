# M&M Food Market — Processing Guide

> **Source:** M&M Food Market OneGuide (Google Doc `142gmNZ3CkFGdWTRBysr3XoKXtPpB3vveLFiAyAlf8eA`), updated Jul 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#mmmeatshops` |
| Hosted URL | mmfoodmarket.com/en/pages/flyer |
| Flyer type | 139: Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Strategic Ops **Yes (Feedel)**; no coupons |
| Pages | Bilingual (EN/FR on same page) |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Wednesday (5 PM), Valid From Thursday (12 AM) → Available To Monday / Valid To Tuesday. **One-day consumer preview starting 5 PM Wednesday.**
- **Documents:** codesheet (`.csv`), Product Information / URL / tagging document (`.xls`), page/item category spreadsheet.

## Upload & setup (codesheet — owned by DOC)
- FTP: download the product info `.xls` and the codesheet `.csv` (check both off).
- **Codesheet manipulation:** check page numbering; ensure PDF names in the codesheet match the FTP (mismatch → codesheet won't run); add "Versions" to A1 if blank; **rename the version WITHOUT the Quebec zones (PQB Eng, PQU) as `AOC`**; if multiple zones share a name but different store distribution, rename as `AOC_xxx` (xxx = stores). Download as CSV.
- **Codesheet upload:** Config **`m_and_m`**; base path from FTP; **all toggles checked except region assignment AND combine zones**; attach CSV; Save & Process.
- Example week: 3 zones — `AOC`, `PQBEng`, `PQU` (French). Mark flyer creation complete.
- **Setup QC (Flex):** attach the Product Information URL document to every vendor task; confirm dates (bottom of first page); Standard 4 thumbnails; set preview date to the Tuesday before go-live (preview links go to the client).

### Codesheet troubleshooting
- **"page _ not found":** ensure the page name matches exactly in FTP and codesheet; re-save and re-run.
- **"Zone: AOC is missing the following stores…" with no store number:** likely a typo — look for an extra comma in the store list for that zone, delete it, re-run.

## QC specifics
- **Box Draw (Low; Auto-Box ON since May 2025, Box QC bot ON):** **include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box grid items and list items individually; box social media icons.
- **Tag / Tag QC (Medium; Auto-tag OFF; Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **⚠️ Bilingual pages:** when tagging an "English" page, tag **only English** text; on French pages tag **only French** and omit English item info.
  - **Description** = product weight / number of pieces from the PDF. **Price** = bolded Current Price.
  - **SKU:** use the SKU from the tagging spreadsheet (column B), **only in the SKU field**, one SKU per offer, tagged individually. Only use SKUs from the spreadsheet.
  - **URLs:** search product by name in the tagging doc → tag URL from column C. For items not on the site use `mmfoodmarket.com/en/product-not-available` / `.../fr/produit-non-disponible`. Name social media links properly.
  - **Categories:** every item and page needs a category (spreadsheet provides both). Use **Category 1 for the Page Level category** and **Category 2 for the Item category** — all items get only one (Category 2).
  - **Sale Story:** tag "SAVE" info; append Product Sizing info after the Save info if applicable.
- **Image QC:** **cutouts only** (do not use lifestyle images; check for usable PDFs, else cutout).

## ⚠️ Common errors / risk items
- **Inserts:** ensure all pages uploaded.
- **URLs & SKUs:** tag correct SKU and URL based on the product name in the spreadsheet.
- **Social media icons** — box and tag with the correct links (Facebook, Instagram, Foursquare, Twitter, Pinterest — all listed in the OneGuide).
- **Language-specific direct links** — tag per language.
- **Product Sizing** — include in the Sales Story after the "Save" info if applicable.

## Post-processing / FQC
- **URL/Links, SKU, Sale Story QC (DOC/Flex):** item search for blank SKU / Sale Story / URL and fill from the linking doc + M&M website; check description for sizing info (blank OK if URL shows "product not available").
- **FQC (Flex):** geography, sessions, verify URL, PZ/boxing checks; **Custom action — set cutout images, then item image QC** (prioritize cutouts, no lifestyle images); page categories; flyer sorting (weekly > gen merch).
- **Flyer Review type: Lite** — see the M&M Food Market flyer review guide.

## Out-of-processing
- **Add missing FSAs:** geography tab shows 3 missing FSAs → export FSAs → in the CSV delete the "pricing zone name" column, rename columns `flyer_id` and `fsa` (lowercase), add 3 rows with the missing FSAs + AOC pricing-zone id → run "add FSAs from CSV" custom action with the flyer run ID.
- **Preview links:** send preview + direct links to the client a day before go-live (hosted 2.0 preview links renamed Direct EN / Direct FR).

---
*Source: M&M Food Market OneGuide (Google Doc `142gmNZ3CkFGdWTRBysr3XoKXtPpB3vveLFiAyAlf8eA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
