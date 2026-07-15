# Fairway Market — Processing Guide

> **Source:** Fairway Market OneGuide (Google Doc `1ieeVanQH-60c3jxAqojG2T17dQKgejPIOEPLm7-pWKA`). Contacts/credentials omitted.

> This is a **Wakefern** account processed alongside **ShopRite (SR)** and **The Fresh Grocer (TFG)** — banners referenced here as SR, TFG, and FW (Fairway).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard |
| Availability | All platforms |
| Flyer types | Weekly (SR runs 2 weekly flyers) |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); DOC (FQC); OS — N/A; no coupons; no Feedel/retailer data services |

## Files & schedule

- **Files received:** Friday.
- **Cadence:** Available From Thursday; SR = 1-day consumer + 1-day retailer preview; TFG & FW = 1-day consumer preview.

## Upload & setup (generic codesheet)

- Two text files arrive in the FTP with the PDFs (only 1 for FW & TFG): files with **2 underscores = "manifests"** (build codesheets from these); files with **1 underscore = blowline files** (vendor-task attachment).
- Copy manifest info into the generic codesheet (a tab per banner); save each tab as CSV.
- Codesheet upload per flyer run: **Config `generic`, base path `/`, every toggle checked except the 2nd and last.** Run.
- **⚠️ The ShopRite Sunday flyer will error "files already uploaded" — force processing.**
- **Blowline file** (text in FTP): open in Excel via **Data → Get Data → From Text (Legacy Wizard)**; split columns by removing black separator lines; keep only **`PROMO_NUM`, `BLOWLINE`, `AD_COPY`**. Save as `.xlsx` and attach to **all vendor tasks.**
- Standard 4 thumbnails. **Legibility heights: Fairway 40/30; TFG 50/40; ShopRite 50/40.** Set preview dates for all 4 SR & TFG flyers (Thursday before/on live).
- **⚠️ Submit an urgent processing ticket for the ShopRite Sunday flyer when uploaded on Mondays** — Item Tag must be complete by midday Wed to run the custom action and send previews Thursday.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Do NOT use text boxes.**

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; no linking doc)
- Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.** Brand is used for both box/tag.

### Image QC
- Standard: PDF preferred if clean; otherwise cutouts accepted.

## FQC (owned by DOC)
- Mark AutoStack Spotcheck complete; no Image QC; spot-check items boxed/tagged.
- If you box new items after OS, **Generate Data Piping Groups**; with REV pages, re-run Data Piping **before** the custom action.
- **Mi9 Sub-item Generator custom action:** open the correct-date Blowline text file in Sheets (Friday runs have `FGN` in filename); keep only `PROMO_NUM` and `UPC_13_NUM`; remove blank rows/duplicates; **Ctrl+F "e" and delete rows containing "e"**; save as CSV named e.g. `SR Oct 9 & 16 FQC Blowline`. Upload to "Upload Files" in Fadmin, copy the file ID, then Custom Actions → **Mi9 Sub-item Generator** → paste flyer run ID + Mi9 file ID → Run. (Runs only when Item Tag is complete; usually 15–40s, up to 5 min. Instant completion usually means it didn't run.)
- QC that items with SKUs have sub-items (top-left in tagging interface).
- **⚠️ Item-level valid dates:** ShopRite "Locked In Prices" (blue pages); Fairway "2 day sale"/"1 day sale" at the bottom of page 1 or 2.
- **ShopRite:** box & tag logo top-left of page 1 (Display type = Item); use item search (Name IS blank) to tag all banners quickly; name per the logo copy.
- Check sessions; verify vertical preview shows sub-items (80–90%).

### SKU update process
- After previews go out, the retailer replies with an Updates file (spreadsheet of SKUs to update). Add new SKUs/Promo IDs/UPCs to the FQC Blowline file (delete blank rows; **no commas or letter "e"**). Export items to Sheets, filter by name/brand, update SKU column, keep `item_id, sku, brand, name`, re-import, and re-run the Mi9 Sub-item Generator with the updated Blowline.
- Update SKUs in both ShopRite flyers **and the Friday TFG flyer**; if there are *links* to add, add to both Friday and Sunday flyers.

## Preview links
- Preview all 4 SR and TFG flyers at 9am Thursdays (2 ads each). Draft by EOD Wed, schedule for 9am Thursday. *(Contact list and preview URLs are in the OneGuide — not stored here.)*

## Flyer Review
- **Type: Lite** — flyer dates, sessions complete, previews correct, all items tagged, geography correct, availability toggles correct.

---
*Source: Fairway Market OneGuide (Google Doc `1ieeVanQH-60c3jxAqojG2T17dQKgejPIOEPLm7-pWKA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
