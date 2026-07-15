# CAL Ranch — Processing Guide

> **Source:** C-A-L Ranch OneGuide (Google Doc `1rQR9-if9AzaUsg0rxjFeCABAlDW6_GkO8Ko6Uox-hs8`). Contacts/credentials omitted.

> **Distinctive flow:** the retailer QCs an **item export** and returns corrections, which are then **re-imported** so that **only Name, Sale Story, and URL are populated** — all other tagging fields must be blank.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (occasional Hosted-only flyers with too few items for Flipp; retailer is aware) |
| Slack channels | `#calranch` |
| Hosted URL | calranch.com |
| Flyer types | Ad-hoc (event-based) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); OS (Setup + FQC); no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday.
- **Preview date:** Monday.
- Files uploaded into **folders matching the event name**; rarely different versions in separate folders.

## Upload & setup (owned by Vendor)

1. Contact emails when files are uploaded to the FTP. Flyer may have **two versions (North / South)** — store assignments are in the email; if one version, email will say "good in all stores" (build one pricing zone, all stores).
2. **Create flyer shell:** run type **StoreAds**; Internal Run Name = event name (email or page 1); External Run Name = event name; live/valid dates from email or page 1; toggles = available everywhere; add theme if applicable.
3. Manual upload — select the event's folder pages in the FTP → Autogroup.
4. **Pricing zones:** typically all stores to base; if two zones, assign per the email.
5. Attach note to all vendor tasks: "No linking document, please proceed with tasks."

## ⚠️ Common errors / risk items
- **Look for multiple products** (multi-item boxes).
- **Tagging is deliberately minimal** — only Name, Sale Story, and URL are ever filled. The only URLs should be the main website and social media (on boxed/tagged logos).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Use text boxes when needed; box each item separately.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON)
- **Only Name, Sale Story, and URL are filled.** Include: name, SKU, sale story, categories, URLs. **Exclude:** pre/postfix, valid dates, description, price, disclaimer, original price. Brand is box/tag-specific.

### Image QC
- Select PDF images chosen; if unclean, use cutout.

## Post-processing (item export → retailer QC → re-import)

**1. Send item export to the CAL Ranch team as soon as vendors finish:**
- Overview > Information/Reports > Export Items → download CSV → open in Google Sheets.
- Delete the "Flyer Items" cell and everything below it; delete the "Page Items" cell.
- Keep only: page, item_id, name, sku, raw_original_price, raw_current_price, sale_story, url. Sort page ascending; rename `raw_original_price`→"original price" and `raw_current_price`→"current price". Only main-website + social URLs should be present.
- Save as `.xls` and send.

**2. Final QC after corrections come back:**
- Read Column A ("Comments") of the returned report and manually apply re-boxing instructions (e.g. group listed item IDs into one box).
- Delete Column A and the Pages column; rename prices back to `raw_original_price`/`raw_current_price`; add columns brand, description, disclaimer_text, pre_price_text, price_text.
- Column order: item_id, sku, brand, description, disclaimer_text, name, pre_price_text, price_text, raw_current_price, raw_original_price, sale_story, url.
- Enter `*blank*` in every cell of: brand, description, disclaimer_text, pre_price_text, price_text, raw_current_price, raw_original_price (retailer wants all fields empty except Name, Sale Story, URL).
- **Save as `.csv` in Google Sheets** (item import fails from Excel). Overview > Information/Reports > Item Import → upload → check Last Session Results for success.
- **Verify via Item Search** — Brand / Description / Disclaimer Text / Price Text / Current Price / Original Price each **IS NOT BLANK should return 0 results.** Clear any offenders.
- Then: confirm logos + social icons boxed/tagged; check dates; page categories; sessions clear (reverify URLs if needed); thumbnails Standard 4; legibility heights 45/35; Item Image QC (PDF chosen, cutout if unclean).

## Flyer review / out-of-processing
- **Flyer Review type: Lite** (owned by Flex).
- **Page swaps are standard** (baseline process).

---
*Source: C-A-L Ranch OneGuide (Google Doc `1rQR9-if9AzaUsg0rxjFeCABAlDW6_GkO8Ko6Uox-hs8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
