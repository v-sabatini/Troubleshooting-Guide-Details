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
