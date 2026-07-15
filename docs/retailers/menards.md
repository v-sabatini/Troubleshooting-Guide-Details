# Menards — Processing Guide

> **Source:** Menards OneGuide (Google Doc `1aqf7DDM3TFmEHMxH76QpxpsgLf5a3u-msXOU0e1F-4c`), updated Jan 20, 2026. Contacts/credentials omitted.
>
> **Jan 20, 2026 change:** When tagging URLs, no longer "click through" search pages to the product page — **linking to just the search page is now preferred**, even for single-SKU item blocks.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel | `#menards` |
| Hosted URL | menards.com/main/flyerselectstore.html |
| Publication cadence | See the Flipp Flyer Schedule |
| Processing | Auto-stack |
| Who's involved | **Flex — N/A (not involved)**; OS completes standard tasks |
| Box Draw complexity | **High** (spreadsheets required — Header & Burst document) |
| Tagging complexity | **High** (spreadsheets required) |

## Files & schedule

- **Files usually arrive Wednesday, two weeks before go-live.** Upload can be done Wed–Fri, earlier is better.
- Usually 2 publications ("CUE" and "A"), occasionally 1–2 more.
- **Two codesheets:**
  - **Daybreak** — for staggered dates. Uploaded **but NOT run.**
  - **Pagination** — for page layout. This one **is run.**
- **We FQC very early** — it's a contingency to send Menards their retailer preview, which they expect the **Wednesday before go-live.**

## Upload & setup

**Daybreak sheet.** From FADMIN SFTP, download the "daybreak" file, import to Sheets. Filter the flyer and use the Column D dropdown: if a date there is before the run's Available/Valid From in FADMIN, alter run settings to match the earliest day (this sheet generates staggered dates and the upload **fails** if a listed available/valid-to is earlier than the FADMIN flyer's). Export CSV.

**Pagination sheet.** Download from SFTP, import to Sheets:
- Find store "O'Fallon" → remove the apostrophe ("OFallon").
- On any row-1 cell ending in "-1" or "-2" that has no "DG" page identifier below it, prefix the cell with "OX" (e.g. "OXPage 9.1").
- If there is a page 1.1, delete it and re-upload manually later (the codesheet processor pulls it as page 1 by accident).
- Download as CSV.

**Codesheets in FADMIN.**
- Upload the **daybreak** page. Base Directory from SFTP (no trailing space or slash; the second half of the path is unique per run — A vs CUE). **DO NOT RUN this codesheet.**
- Upload the **pagination** page and run **only** it. It **always runs yellow (processed with warnings) the first time** — this is a false error introduced by CLSD to slow the process and prevent a recurring glitch; **no action needed.** Then **Force Process** the pagination codesheet.

**After codesheets.**
- If you removed a page 1.1 (step above), re-upload it manually into position 2.
- Download the **"Header and Burst" (linking) XLS** from SFTP and attach to all vendor tasks.
- Input External Run Name and Key Messages from the 2nd half of the internal run name (e.g. "Home Essentials").
- Set preview date to Wednesday before go-live.

**Setup QC.** After upload you'll usually have pages named `KEY.pdf` — these are instructional for insert tagging and are **not** uploaded.
1. Spot-check zones: flyer dates on PDFs match **Pricing-Zone-level** FADMIN dates.
2. Pages → Categories: no serious graphical issues.
3. Pricing zones and geo look right (~70–80 zones; FSAs may shift with boundary changes but no major changes).
4. Confirm a handful of zones end in **-2** — the system splits a PZ in two when stores share pagination but have different launch dates. **If none appear, the split process may not have run (rare).**
5. Mark Setup QC complete.

## ⚠️ Common errors / risk items

- **Rebate wording** — many items are "Final Price FREE After $$ Mail-In Rebate" / "each PRICE AFTER REBATE." Use the matching **postfix**; the "after $$ mail-in rebate" phrase always comes **last** in the postfix. If there's no exact-amount matching postfix, use "each PRICE after $$$ Mail-in Rebate*." Do **not** flag these as errors.
- **Multi-version lumber/decking/insulation pages** — pages look identical but prices vary by version. Ensure prices match the exact page; **never copy prices across pages/items**; report if you see copied prices.
- **Box every item with a separate SKU or price SEPARATELY.**
- **Never tag an item using an adjacent item's price** when one isn't present, unless there's a specific callout ("OR", "YOUR CHOICE"). Leave Current Price blank otherwise.
- **Plants not searchable on the site** → link to the garden center (`menards.com/main/garden-center/c-9985.htm`).
- **SKU spaces** — when copying/pasting SKUs, override existing spaces using the keyboard spacebar.
- **Page-link error** — if entering a page number throws "Page destination should be a valid page…", simply enter **1** as the destination.
- **Live-dates / PT notes:** URLs edited by the PC (check "Whodunnit") are usually correct/ad-hoc — don't remove; mark live date false, source = retailer request. SKUs that don't match the flyer pages are per retailer request — don't change (breaks data piping). Some items are intentionally non-clickable — flag to processor before actioning. Post-fix "each" used when there's no matching amount — not an error.

## QC specifics

### Box Draw — High complexity
- **Include:** social media, coupons, sign-up page, special weblinks, retailer logo. **Exclude:** packaged deals.
- **Rule 1 — box all items with a SKU;** each SKU in a product item gets a box; a box with >1 SKU must not have multiple prices (if multiple prices, one box per SKU/item).
- **Rule 2 (May 2025):** box the item, title, and description of "YOUR CHOICE" items as individual boxes; do **not** add a text box to the "YOUR CHOICE" callout/adjacent pricing.
- **Rule 5 (May 2025):** **do NOT box item disclaimers** in a text box (retailer no longer wants disclaimers captured).
- **Sale banners get boxed;** non-sale banners ("Chance to win a car," "Delivery to Canada," "Sales Disclaimers") do **not**, unless in the URL document.
- **Social-media icons** (page footer) boxed & tagged as Direct Links (Pinterest `pinterest.com/menards/`, Instagram `instagram.com/menardshomeimprovement/`, YouTube `youtube.com/user/Menards`, Mobile App `menards.com/main/services/menards-mobile-app/c-13988.htm`).
- **Headers & Bursts** boxed only if specified in the shared Header/Burst doc (all direct links, not item links) — must be consistent on all pages/versions.
- **Rebate disclaimers** — ensure ALL are boxed and tagged as **Page Links** leading to the correct page.

### Tag / Tag QC — High complexity
- **Include:** name, pre/postfix, sale story, disclaimer, original price, categories, images. **Exclude:** brand (put brand in the Brand field, not Name), description. **Risk items:** SKU, price, valid dates, dollars/percent off, URLs.
- **Name order (always):** (Brand) (Model-Name) (Size) (Title of Product) (Sub Heading/Category) — e.g. "Hunter 52\" Fremont Ceiling Fan." Sales banners: enter as it appears in the headline.
- **SKU formats:** Single (`111-1111`); Multiple-range (shared SKU group, e.g. `111-1123-1125`); Combination (multiple families, e.g. `111-1123-1124-1125, 555-6780`). Model numbers entered as shown, without the `#`.
- **Price/prefix/postfix:** prefix = anything before the price, postfix = anything after. Never use "FINAL SALE" as a prefix — always postfix. Do not enter dollars-off / original-price for rebate items. BOGO handled with prefix + current price + postfix. Each item in a chart/group needs its own prefix & postfix.
- **Disclaimers** entered in order: Unique item → Page → Rebate. Rebate disclaimer (only when "Mail-in Rebate *" with an asterisk): `*Mail-in Rebate. Rebate is in form of merchandise credit check. Valid in-store only. Merchandise credit check is not valid towards purchases made on MENARDS.COM®`. **Do NOT duplicate phrases.** Include item disclaimers; do not include page disclaimers.
- **Item categories:** every page needs ≥1 category based on the majority of items; **keep page-level categories identical across all versions of the same page;** first and last pages get **no** category. Mail-in-rebate items also get the **Rebate** analytic category. (A full category chart is in the OneGuide.)
- **Item URLs:** if a SKU has a URL in the linking document, use it; else fetch → visit → copy the site URL. **Retailer does not want generated search URLs.** Remove any `?tid=` from URLs; trim anything after `.htm`. Multi-range SKUs (>9) can't be searched on-site — use the Menards URL Database.
- **Valid dates override:** don't enter unless for 6-Hour Savings items in the Black Friday Sale.
- **Email signup pages** → link to `menards.com/main/preference-center.html`.

## Pre-final QC tasks

1. Finalize pre-live page swaps; add pages not in codesheet.
2. Spot checks.
3. **Inserts** — ops boxes/tags in-house; each has a "link" XLS and a "key" PDF in SFTP (Key PDF = boxing template; link XLS = linking instructions).
4. Ensure ALL rebate disclaimers boxed/tagged as Page Links to the correct page.
5. Thumbnails: rectangles 2 pages, squares 1 page.
6. Re-run data piping.
7. Download the previous week's email insert, upload to the run, copy boxes from last week, insert into the **dead-last** position of all zones.
8. **Tracking codes:** Dynamic Variable, Source=Hosted, Variable=`utm_campaign`, Value=`[FLYER CODE]-[YEAR]` (e.g. 20CUE-2024); and Variable=`utm_content`, Value=external name with hyphens (e.g. home-essentials). Apply all tracking codes.
9. Data piping: link-only misses are fine. For "Item" display-type boxes failing data piping, if the SKU ends in a numerical range >220, reduce the difference between the last two numbers to <220 and re-pipe (may still fail — no further action).
10. Rerun any page whose bottom text is crossed out as **ghostscript**.
11. "See Page _" disclaimers boxed/tagged as page links to the full-disclaimer page.
12. **Flyer sorting:** newest 11% Ad → newest Appliances ad → current 11% Ad → current Appliances ad → catalogs newest→oldest.
13. Add a trigger to rerun data piping at 11:30 pm the night before go-live.
14. Final QC checklist.

## Preview QC (PQC)

- **Category QC:** change Google categories "beer"/"wine"/"seafood" → "building material."
- **SKU blank:** Item Search SKU is blank, type Item → open all and tag with the SKU on the PDF.
- **Items without URL** should be zero (Overview → Information/Reports → Items Without URL).
- Manually click through: single SKUs must NOT be search URLs; multi-SKUs must contain the full SKU range with no `-`.
- Search for URLs containing `-` or "search" and remove the `-` from the SKU in the URL.

## Out of process

- Preview send (Wednesday before go-live).

---
*Source: Menards OneGuide (Google Doc `1aqf7DDM3TFmEHMxH76QpxpsgLf5a3u-msXOU0e1F-4c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
