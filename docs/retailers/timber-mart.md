# Timber Mart — Processing Guide

> **Source:** Timber Mart OneGuide (Google Doc `1NQ0Yed95nfbSIN-uN6vG45lVv3bzu6pGXEq-JZ41km0`), updated Mar 13, 2026. Contacts/credentials omitted.

Multiple banners/publications share this account: National Weekly, Lyons, Sherwood, TBMQC, and Quebec (Gabriel Couture / Materiaux Audet).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (plus retailer channel) |
| Publication schedule | weeklyflyer: Weekly · lyons: Bi-Weekly · TBMQC: Bi-Weekly · Sherwood: Ad-hoc |
| Processing | Auto-stack |
| Who's involved | Vendor/Flex setup; DOC FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday (all banners).
- **Cadence — National Weekly:** Available Tuesday → Tuesday; Valid Wednesday → Tuesday.
- **Cadence — Lyons & Sherwood:** Available Wednesday → Wednesday; Valid Thursday → Wednesday.
- **Cadence — Quebec/Gabriel Couture/Materiaux Audet:** Available Tuesday → Tuesday; Valid Wednesday → Tuesday.

## Upload & setup

### National Weekly (Vendor)
- Email confirmation from the retailer contact. The codesheet is in the FMQ ticket (flag processor if no participation list is linked — required for pricing zones, store assignments, and staggered dates).
- **Codesheet manipulations:** delete rows above and below the chart; save as `.csv`. **Risk:** file names must be in column A and spelling must exactly match the FTP files.
- **Config name:** `timber_mart`. **PDF Base Directory:** lowercase base path — highlight everything before `/atl`, `/west`, `/bc`, `/ont`, etc. (e.g. paths `/timber mart national/2026/09_june 11/bc` and `…/atl` → use base path `/timber mart national/2026/09_june 11`).
- **Uncheck "Region Assignment" and "Combine Zones."**
- Check the FTP that ALL pages under the base directory uploaded; cross-reference the participation list for any needing manual upload. Upload POTM pages if in the FTP.
- **Staggered dates (important):** once PZs are created, use the participation list to set staggered dates. The run dates must start at the earliest live date and end at the latest end date (e.g. zone live May 2–14 + zone live May 7–21 → run May 2–21). Adjust per-zone dates in Overview → Edit Dates/Details.

### Lyons & Sherwood (DOC)
- Retailer drops files directly into FTP (no email). Manual upload — all pages from the corresponding folder, inserts included; group pages manually.
- **Lyons:** one PZ ("Lyons") → assign all 3 Lyons stores. **Sherwood:** one PZ ("wSherwood") → assign Sherwood store (#7746).
- 4 standard thumbnails; legibility heights 45/35 (auto); available one day before valid date.

### Quebec / Gabriel Couture / Materiaux Audet (Flex)
- Email confirmation from the retailer contact. Codesheet in the FTP (labelled Participation List): delete rows above/below chart → save as `.csv`. **Risk:** file names in column A must exactly match FTP names; Dealer # (column B) must have decimals.
- **Config name:** `timber_mart`. PDF Base Directory: lowercase base path (highlight all before `atl`/`west`, etc.). **Check all toggles except "Region Assignment" and "Combine Zones."** If there's a Base flyer and a Custom flyer (Quincaillerie Bigras), upload both codesheets.

## QC specifics

**Box Draw (Medium; Auto-Box ON, Box QC bot OFF; linking doc Box-specific)**
- Include: coupons, packaged deals. Exclude: retailer logo, sign-up page, social media, special weblinks.
- **Every item on the first page** is boxed. After page 1, only box items with **prices, SKUs, coupons, %Off callouts, or Online callouts.** Coupons identified by the word "coupon" or scissors/cut-out line.
- Separate box per priced item (a "Valued Price" box still counts as a price). For packages, box elements with different prices separately. Box items that have a SKU but no price.
- **TMBQC (new):** draw boxes around `www.timbermart.ca`, the Fairstone callout, credit-card callout, and Air Miles.
- **Do NOT box** items with no price, no SKU, and that aren't coupons.

**Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **SKUs are no longer needed — do not enter them in any field.** Brand is Box-specific.
- Name/Brand/Description: enter as they appear, only in the language specified for the page. Original price usually has "Reg" before it.
- **Sale story RISK:** large "##% off" callouts sometimes apply only to certain items — do NOT assume the callout applies to every item on the page.
- **Disclaimer:** only enter if within the drawn box (not if at the bottom of the page).
- **Valid dates RISK:** only apply date overrides when a related promo sale story is on the item; ignore Air Miles dates; reference page-level valid dates (e.g. "4 Day Special!" callouts).
- **TMBQC URLs (Quebec only):** tag as LINK — Website `timbermart.ca/fr/`, Fairstone `web.fairstone.ca/timbermart-ol/fr`, Credit Card `timbermart.ca/fr/carte-de-credit/`, Sunroom Solutions `timbermart.ca/fr/solarium/`, Goodstyle `goodfellowinc.com/produit/goodstyle/`, Air Miles `airmiles.ca/megamilles/fr`.
- **Coupons RISK:** all coupons require the word "Coupon" in the name.
- **PDF image selection:** clean PDFs where available, else the corresponding cutout. Do NOT select lifestyle/sample-flooring/product-colour images — use cutouts for those.

**Image QC:** clean PDFs where available, else cutout; no lifestyle/sample images.

## Final QC / go-live notes (DOC)

- **POTM pages:** all flyers **EXCEPT Sherwood** receive POTM pages. Pagination order: regular monthly pages → Spine Wrap pages (only for special events like Father's Day) → POTM pages. Use the URL document to link POTM pages or copy boxes from the previous flyer (search "doc" in the FTP). Manually box/tag URLs/videos; YouTube links → Embed URL → Display Type: Video.
- Page category QC: no category on page 1 or on insert/POTM pages. Image category QC: prioritize PDFs.
- **FQC process is the same for all banners.**
- **Flyer Review type: Lite.**

---
*Source: Timber Mart OneGuide (Google Doc `1NQ0Yed95nfbSIN-uN6vG45lVv3bzu6pGXEq-JZ41km0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
