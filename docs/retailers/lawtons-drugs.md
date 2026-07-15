# Lawtons Drugs — Processing Guide

> **Source:** Lawtons Drugs OneGuide (Google Doc `1xpX9DMPvk-LdDTvSrbBXlsflIIs9FdCLagm3_YOKQRA`). Contacts/credentials omitted.

> Sobeys-family banner (codesheet-driven, Scene+ pricing). High-touch weekly.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ |
| Account tier | Tier 3 Standard |
| Platforms / availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeysops`, `#sobeys-dataservices`, `#3fl-sobeys` |
| Flyer type(s) & cadence | Weekly (9667) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS = Setup; **Feedel/Strategic Ops: yes**; no coupons |
| Linking document | Yes (pre-checked in FTP; mass-attach the correct week) |

## Files & schedule

- **Files arrive:** Monday.
- **Cadence:** Available From Wednesday 6AM (one-day consumer preview; 6AM aligns with Sobeys/Foodland ATL going live 3am ATL); Available To Thursday 12AM; Valid From Friday 12AM; Valid To Thursday.

## ⚠️ Common errors / risk items — Scene+

- **Scene+ callouts** must be expressed in the **Sale Story** field, **not the disclaimer**. Some offers only show points earned — Scene+ still needs tagging in the Sale Story. Format: e.g. **"150 Scene+ PTS"**, not "150 PTS Scene+".
- **Scene Member Pricing items:** Prefix = "Scene+ Member Pricing" (**don't forget the + sign**); Disclaimer = "$xx without Scene+ Card"; Categories = add **[Scene+]**.
- **KG/LB:** lb price is the main price with "lb" as postfix; the kg price goes in the **description** for all produce, meat, and seafood.
- **Every item requires a category selection AND a category highlight selection.**

## Upload & setup (owned by Vendor)

1. Download codesheet from FTP (no edit needed). Flyer run → Code Sheets → Name "upload", upload the xlsx.
   - **Config name: `sobeys_safeway`**; PDF Base = path from FTP; **select toggles 3, 4, 5 & 6**; Save → Process code sheet. Refresh until green.
2. When the codesheet finishes, click the **"Flyer Creation"** task → **"Mark Complete"** (this generates FSAs for the PZs the codesheet built).
   - ⚠️ **RISK:** press **"Mark Complete"** (middle button) — **do NOT click "Start Task"** or it redirects you to manually build the PZs.
3. Sessions begin (page stitching, item cutouts, text extraction, PDF Image Auto Selection, PDF Image Extraction may remain — can be ignored). Add stores per zone combinations, matching store sets (e.g. NS/NB-WELL = NS-WELL + NB-WELL). Resolve any store-in-two-PZs overlap by removing overlapping stores from the larger PZ.
4. **Edit Details / dates** (manually set): Available From = preview day 6AM; Available To = end date 11:59PM; Valid From = start 12AM; Valid To = end 11:59PM. External Run Name = valid date range (e.g. "Weekly eFlyer 03/24 - 03/30"). No theme. Add Key Messages.
5. Check FTP everything uploaded + check off codesheet. Geography: no added stores/FSAs.
6. **Mass-attach linking doc** to all vendor tasks (download correct week's WK(xx) file → Vendor Box QC → check Mass Attachment → + → select file). Confirm attached to all vendor tasks.
7. Merge pages where needed (hard merge: Pages → merge → left/right → mark urgent). Add merged pages back to the PZ (Layout → put in, position 2). Handle skinny pages (first page merge right, last page merge left).
8. Thumbnails: draw with minimal white border. If p.1 has the Lawtons logo cut off, shift the thumbnail to the page with the full logo. thumbnail_1065_x_600 and storefront_carousel_premium span 2 pages; stock_premium and storefront_carousel_organic span 1st page; plus first_page_thumbnail_400w.
9. Re-run required sessions. Complete Setup QC. Mark AutoStack complete.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required (box-specific). **Include** retailer logo, sign-up page, social media, special weblinks; exclude coupons, packaged deals. Box all items separately (draw text boxes when needed). Special weblink: digital page "explore today" button → `https://lawtons.ca/everyday-wellness/`.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** linking doc required (tag-specific). **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Brand:** if more than one brand is listed, leave Brand **blank** (do not pick one). Brand goes in front of the Name.
  - Enter SKU/price as in flyer. Add valid override dates (both from and to) where applicable.
- **Item Category QC** uses a category chart (owned by DOC): Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, Scene+, Dairy, Deli, Health and Beauty, Seafood. Scene+ items get Scene+ as a second category in addition to the product category.

## Final QC / go-live notes (owned by DOC)

- Confirm pages merged (usually pg 2 and 9). Page categories: skip page 1, use labels + items.
- **Scene+ check:** Item Search Sale Story → Contains → "PTS"; ensure Scene+ tagged in Sale Story (not disclaimer); add "$$$ without Scene+ Card" callout in disclaimer.
- KG/LB check. Risk items (usually page 1): 3-day-only columns with specific valid from/to dates.
- Re-run page stitching; PDF Image Auto Selection for Image QC; check previews/interactivity (iframe + vertical preview).
- Add the "explore today" digital-page link.
- **Inserts:** updated Mondays (email from BD). Check the insert tracker, find inserts in the Sobeys FTP by keyword (e.g. "pharmacy"), upload + process, box (one box around page), tag (display type Link, exact name from tracker, URL from tracker), mark vendor tasks complete, insert into PZ after regular pg 2. Note: the Thrifty Foods Email Acquisition insert is recurring — pull from the previous week's run if not in FTP.
- Start FQC checklist; **go live at 11am (available)**. After FQC: Item/URL Verification session; flyer sorting = preview flyer, current live flyer.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Lawtons Drugs OneGuide (Google Doc `1xpX9DMPvk-LdDTvSrbBXlsflIIs9FdCLagm3_YOKQRA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
