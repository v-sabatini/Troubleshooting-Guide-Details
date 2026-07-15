# Winn-Dixie — Processing Guide

> **Source:** Winn-Dixie OneGuide (Google Doc `10egXq3eXv6XOcZAGhu3z5IhxGtsS9GJlxyPVU8Jf8-w`), updated Mar 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard (SEG / Southeastern Grocers) |
| Availability | All platforms |
| Slack channel(s) | `#segrocers` |
| Flyer types | **Weekly Circular** (3099), **Bi-Weekly In-Store (ISPO)** (3285), **Monthly Liquor (LIQ)** (3284) |
| Processing | Auto-stack; no coupons; no Feedel |
| Account resources | Winn-Dixie Processing Notes; SEG x Flipp Ops Guidelines (in the OneGuide) |

## Files & schedule

- **Weekly Circular:** files Monday; Available Wed→Wed; Valid Tue→Tue; **1-day preview** (Tuesday) with **staggered pricing zones** (some get a 7-day preview).
- **Bi-Weekly ISPO:** files Friday; Available Wed→Wed; Valid Tue→Tue; **no preview** (available = valid).
- **Monthly Liquor:** files Friday; Available Mon→Mon; Valid Sun→Sun; **no preview**.

## Upload & setup — two-codesheet pattern (all flyer types)

When files drop, search the FTP for `.xlsx` — two codesheets appear:
- **Version List / "Versions"** = store information.
- **Manifest** = pricing zone + page order info (and preview/valid dates — **flag if they don't match the run**).

**Order matters — upload the Version List first, then the Manifest.**

1. **Version List:** delete the extra tab; ensure store info is in **Column C** and **rename the header to "Stores"** (weekly deletes the 'Addresses' tab; ISPO deletes the 'QUAD…ISPO' tab; liquor deletes the "LIQUOR STORE #" column and renames "REGULAR STORE #" tab). **If this manipulation isn't made, the codesheet will NOT work.** Save as CSV.
2. Upload the Version List codesheet: **Name `Stores`, config `seg_stores`**, base path from the FTP, **all toggles except 2**. Save — **do NOT press "Process Codesheet."**
3. **Manifest:** no manipulation for weekly/ISPO (liquor only: delete store columns A/B if present). Save as CSV.
4. Upload the Manifest codesheet: **Name `pages`, config `seg`**, base path, **all toggles except 2 and 7**. Save.
5. **Only hit Process on the Manifest codesheet** (never the Version List). Wait for green, then mark "Flyer Creation" complete.

**Base-path identifiers:** Weekly = `WK XX` in path; ISPO always has **ISPO** in file names; Liquor always has **LIQ**. Liquor "FL LIQ" = all stores → "MONTH LIQ" run; "WDs 115 Liq" = **store 115 only** → "MONTH LIQ 115" run.

**Weekly staggered dates:** the run's Available From = 7-day preview. Cross-reference the Manifest (zones highlighted **green** = 1-day preview), select those zones in Edit Dates/Details → "Apply Dates to Selected Flyers" → set Available From to the one-day preview date. Leave a comment "staggered dates have been set."

- Setup QC: confirm all pages uploaded; confirm valid + preview dates; Standard 4 thumbnails; geography — if stores missing, search the Version List (not present → correctly excluded; present → manually add to its pricing zone).

## QC specifics (similar across flyer types)

- **Box Draw — Low.** Weekly: **Auto-Box ON**; ISPO & Liquor: **Auto-Box OFF**; Box QC bot OFF for all. **Include coupons + packaged deals; exclude retailer logo, sign-up, social media, special weblinks.**
  - One box for "Buy This Get These Free" and "Pick Any 5 for 5" (one price = one box). Box vaccine banners. Two products but one picture → box as ONE (second item in description).
  - **DO NOT box retailer logo or rewards banners.** Watch for boxes showing the wrong item's picture.
- **Tag / Tag QC — Low; Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **URLs = Exclude — THERE IS NO URL LINKING; do NOT box/tag any banners or pages with URLs.**
  - **Name** as on flyer; two bold names → both in name field; one bold + one not → bold in name, rest in description; no price/deal → tagline in name.
  - **Prefix** = text before current price; when there's sale-story info but no current price, put the sale story (e.g. "Buy 1 Get 1 FREE") in **Prefix**, and "save $$ on ## with card" in **Sale Story**.
  - Multi-brand → select "Multi Item?" and separate brands with `|`.
  - **Two prices:** use the LOWEST in current price; put "Buy 1 $x.xx ea." in description. Digital coupon callouts → tag the discounted price.
  - **Discount $/% :** if sale story says "Save up to $$" leave the discount field blank.
  - **⚠️ "2 for the price of 1" ≠ "2 for $1":** no `$` before the "1" means the "1" does NOT go in the price field.
  - **Categories:** required (merchant receives analytics) — **one category only**; use the section banner header; **FLAG, don't guess** if unsure. Coupons → Display Type COUPON, name = sale story, valid dates, category "coupon".
- **Image QC:** always select a clean PDF if available; cutout only if none.

## FQC (owned by Flex — same for all flyer types)

**Retailer-flagged risk items: (1) Sale Story, (2) Staggered Pricing Zone, (3) Item-Level Valid Dates.**

- **Sale Story check:** item search Sale Story IS NOT blank — verify BOGO/sale numbers match the flyer.
- **Staggered PZ dates (WEEKLY only):** if the comment box mentions staggered PZ dates, **DO NOT EDIT.** WD normally has 1–2 zones with a week-early preview, the rest a 1-day preview (per Manifest). Only if ALL zones share the run's available date: Edit Dates → select all, deselect the correct ones, multi-edit per that week's Manifest, or flag to the processor.
- **Item-level valid dates:** look through pricing-zone pages — weekend-sale banners on page 1s, unique valid-date items on pages 3–6, "PRICE HOLD" pages.
- **Switch & Save pages:** ensure they're boxed/tagged (vendors often skip them — no prices, only sale stories); can copy boxes from Harveys or Fresco y Más of the same week, else box/tag in house.
- Category QC (one per item), Item Image QC (PDF if available), page categories (use flyer headings). Standard thumbnails; **Legibility heights 35,25**; no theme; available everywhere.
- **Dates:** Weekly = 1-day preview; Bi-Weekly = no preview (Wed→Tue); Liquor = no preview (Mon→Sun).
- **Flyer sorting:** weekly flyers first (by date), LIQ in the middle, ISPO/bi-weekly last.
- **Flyer Review type: Lite.**

---
*Source: Winn-Dixie OneGuide (Google Doc `10egXq3eXv6XOcZAGhu3z5IhxGtsS9GJlxyPVU8Jf8-w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
