# Big Y — Processing Guide

> **Source:** Big Y OneGuide (Google Doc `12T2BKJJ18_9pOj0CHFXS6c_8QSVa5ZqXOUVt-VLQ4jg`), updated Jun 11, 2026.
> Retailer is onboarding (flyers were tests as of Sept 10). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard |
| Availability | All platforms |
| Slack channel(s) | `#bigy-onboarding`, `#onboarding` |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Weekly Ad (#11839); other flyer types are indexed and can be ignored |
| Processing | Auto-stack; Flex not involved; OS only completes flyer processing; no coupons; Strategic Ops (Feedel — integrating with Mercatus, high priority) |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available From Wednesday → Available To Wednesday; Valid From Thursday → Valid To Wednesday.
- **Preview date:** Wednesday.
- **Linking Document:** REQUIRED — built via a custom action (see pre-processing).

## Pre-processing: tagging document & custom action (owned by Vendor)

- Engineering built a custom action ("**Big Y SKU Mapping**") that reads several Mercatus spreadsheets and combines them into one tagging spreadsheet.
- Open the merchant's SFTP page and the Custom Actions page; run "Big Y SKU Mapping" either by entering SFTP filenames or clicking Run Action (auto-selects newest files). A spreadsheet is emailed to whoever ran it.
- Download the CSV containing "flyerPromoItems" (matching flyer date) from the SFTP. Import both sheets into Google Sheets/Excel with **"Convert text to numbers, dates and formulas" NOT checked**.
- Promo Items sheet: filter the Offer ID column for blanks (SKUs without an Offer ID weren't pulled), then copy UPC & Item Description into the custom-action sheet's SKU & Name columns. Download as CSV and add to all vendor tasks.
- **Troubleshooting (custom action returns blank):** import the PromoItems sheet and, in a 2nd sheet, use VLOOKUP/TEXTJOIN formulas (documented in the OneGuide) to map Offer ID / Name / SKU.

## Upload & setup (owned by Vendor)

- All files on SFTP. Page order is in the **JSON file** on the SFTP (enable "Pretty-print" to read).
- **Pricing Zones are based on the page file name.** Format: `<date>_by<page#>_<ZONE>_...pdf` — e.g. `by01` = page 1; zone codes BY (Base), CT, EAS, OLM, PTF. **BY pages go into all zones unless additional versions of those pages are received.**
- **Codesheet build:** download the most recent JSON (with flyer date), rename `.json` → `.csv` (do not open first). In the **Big Y Codesheet Generator** sheet: File → Import → Upload the CSV (Convert-to-text checkbox **NOT** selected) → copy Row A → Paste Special-Transposed into the JSON Import sheet → data populates the Generator. Download "Generic Codesheet" as CSV.
- **Fadmin upload:** Config **`generic`**; PDF Base Directory copied from FTP (search "pdf"); **Toggles: everything except 2 & 7**; Save Codesheet; Process Codesheet.
  - **Codesheet troubleshooting (Error File Not Found):** find the correct page name in the SFTP, replace the incorrect page name in a values-only copy of the Generic Codesheet, save as CSV, re-run.
- **Setup:** confirm # pricing zones = # Page 1 versions; attach the manipulated custom-action spreadsheet to ALL vendor tasks; confirm dates per PDF; add an internal preview date; available everywhere; no theme; confirm pages aren't blurry; confirm no stores added/removed. Complete Setup QC. Then add inserts.
- **Promo banners & inserts:** download the "webFlyerPromos" xlsx (contains links + pagination for ~3-4 banner inserts). Download insert JPGs, open in Preview, **Export as PDF via "Export" (NOT "Export as PDF")** to avoid white space. Manual-upload into Fadmin; rename pages to include pagination; run Box QC (entire banner = 1 box); mark Tag & Tag QC complete; tag links manually on the Pages tab.
  - **Insert placement:** "After page 2" means the page with "02" in the name, not the 2nd page in the flyer (the EXDIG page usually goes 2nd). Page tab → Layout → Insert → select pagination, all zones. Rerun Page Tile Gen & Republish; check Vertical Preview of ALL zones (inserts can merge with other pages). If an insert follows Page 1, update wide thumbnails to only include page 1.

## ⚠️ Common errors / risk items (retailer-specific)

- **SKUs & Offer IDs:** most items have a SKU in the tagging document, and most items with a SKU have a corresponding Offer ID. Every item with a SKU should have an Offer ID (verify via item search).
- **Insert placement confusion:** "After page X" refers to the page code (e.g. by02), not the sequential page number.
- **Vertical preview merges:** inserts sometimes merge/stretch in a single pricing zone while others look fine — always check ALL zones.
- Use "Export" (not "Export as PDF") when converting insert JPGs, or extra white space is added.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- Linking Document required (Box Draw/Box QC-specific).
- **Include:** coupons, packaged deals, standard items. **Exclude:** retailer logo, sign-up page, social media, special weblinks, items without prices/promotions, employee callouts, page headers, non-product/community pages.

### Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection ON)
- Linking Document required (Tag/QC-specific).
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, Brand. **Exclude:** URLs.
- **Custom field — Offer ID:** reference the tagging document column A (Offer Code); field is at the bottom of the tagging interface.
- **SKU:** reference tagging document; add as many as fit (on "too many characters, truncate?" click Yes and remove the last SKU if cut off). Do NOT add SKUs to the Description field. **All SKUs should be 14 digits, including leading 0's.** If no SKUs in the document, leave blank.
- **MyBigY offers:** add disclaimer "Available myBigY Offers must be loaded in the myBigY Offers section of your myBigY account to redeem."
- **Digital coupons:** Item Type = Item (NOT Coupon); Pre-Text "Price with loaded MYBIGY Offer"; Post-Fix "Without Offer $x.xx"; disclaimer per listed details.
- Move description items to the Description field (don't leave in the Name).

### Image QC
- The PDF image of the main item in the name should ALWAYS be chosen; use a cutout when unavailable.

## FQC (owned by Vendor; Flyer Review Lite, owned by DOL)
- **Spotchecks (DOC):** coupons, page-level sale stories, item-level valid dates, reg. prices in the description.
- **Custom QC:** item search — SKU IS NOT blank + Offer ID IS blank (and the inverse) — all items with a SKU should have an Offer ID.
- **Ad-hoc QC:** page-level sale stories; confirm MyBigY disclaimers; item valid dates; Image QC; Standard thumbnails; vertical preview of ALL PZs (check for merged/stretched inserts); tagging QC (items without a description shouldn't have details in the name).
- **Pre-Launch — flyer sorting:** they do NOT want newest first — if a flyer is still live, leave it first (e.g. June 4, then June 11, then Taste of Home, then others).
- **Tracking codes (weekly flyers only):** Tracking Codes page → Add Code → add codes individually; all fields stay the same except the 4th line, whose value changes weekly by the **valid** date (e.g. `flipp-jan-29-26`). Add only 4 codes now, then "apply all tracking codes".
- Standard 4 thumbnails; check Vertical Preview for all PZs; geography; complete checklist.
- **Post-FQC (DOC):** retailer occasionally sends revised SKUs/Offer IDs (adjust manually); rerun Page Tile Gen + Republish; keep someone from Mercatus on the email so they re-pull the flyer.

---
*Source: Big Y OneGuide (Google Doc `12T2BKJJ18_9pOj0CHFXS6c_8QSVa5ZqXOUVt-VLQ4jg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
