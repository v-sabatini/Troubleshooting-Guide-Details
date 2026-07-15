# Rexall — Processing Guide

> **Source:** Rexall OneGuide (Google Doc `1c1aRWvrck5L2B5D3Cr19AZSNAaXzxzseFQN5flf_Flc`), updated May 15, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#rexall` |
| Hosted URL | https://www.rexall.ca/eflyer/ |
| Flyer types | Flyer Type #106 — **Weekly** |
| Processing | Auto-stack; Strategic Ops involved (retailer data services / Feedel); no coupons; no Flex; OS N/A |

## Files & schedule

- **Files received:** Monday
- **Available From:** Thursday · **Valid From:** Friday · **Available To:** Thursday · **Valid To:** Thursday
- **Preview:** One Day Preview — confirm dates
- **Linking document:** Deep Link doc (URL column, SKU/product id, description, Page)
- **Workflow:** Upload & Setup (5 days out) → FQC (1 day out). Owned by DOC.

## Upload & setup (owned by Vendor)

### Codesheet manipulations
1. Open the generic Rexall codesheet and the Rexall pagination file.
2. In Rexall's FTP, copy/paste all rows and columns of the new files into the pagination file.
3. Open the FMQ ticket and open the PDF attachment to get that week's pagination.
4. In the Rexall codesheet, delete all the file names.
5. Follow the pagination from the PDF and copy each file name from the pagination file into the codesheet — paste as **Values only (Ctrl+Shift+V)** in the correct page order.
   - Province/zone codes: M = Manitoba, A = Alberta, B = British Columbia, C = Calgary, E = Edmonton, L = London, OT = Ottawa, O = Ontario, S = Saskatchewan, BC = only B.
6. Save codesheet as **.XLS**.

### Upload codesheet
- Name: anything.
- **Config name: `generic`**.
- PDF base directory: take from FTP.
- **Check all toggles except the 2nd and the last.**
- Ensure all files in the FTP have been used.

### Setup
- One Day Preview — confirm dates.
- From the FMQ ticket, download the XLS spreadsheet and upload it to all vendor tasks.
- **No external run name, no theme.**
- Ensure sessions have run.
- Attach Deep Link doc (URL column, SKU/product id, description, Page only).
- **Four Thumbnails 2121:** Thumbnail 1065x800, Stock_premium, Storefront_carusel_premium, Storefront_carusel_organic.
- Geography: check for missing/added stores.
- Setup QC: complete check boxes.

## ⚠️ Common errors / risk items (retailer-specific)

- **Seniors' Day banner:** use the date on the call-out for valid override dates. **Do NOT tag any items below the Seniors' Day banner** with the 20% off sale story and valid dates. Only tag a percent-off if it applies; do not tag percent-off for BOGO items.
- **3 Day Sales:** tag valid override dates for all items in the 3-day-sale box (e.g. "3 Days Only!", Seniors' Day, Movies).
- **Banners** say "See back page for details" on the PDF — **replace with "See Page 3 for details"** for all banners.
- Watch for multiple products advertised under one price — include all items in the name.
- **First and last page:** every item should be categorized DEAL (page 1 = logo/date banner; last page = disclaimer text).
- **Apply Analytics Category "Deals" to Page 1 and Page 2** (once per page grouping index: filter Item Type = Item, Page Grouping Index 1 then 2, Select All → Multi Edit → Analytics Categories: Deals → Save).

## QC specifics

### Box Draw (Low complexity; Auto-Box ON, Box QC bot ON)
- Requires Box Draw/Box QC-specific linking document.
- **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude coupons.**
- Each price gets its own box around the price, information, and item(s) at that price (can be multiple items).
- **What's New page:** try to get image + item name/description in one box; use a text box if not possible.
- Social media: box each call-out/logo separately.
- Banners with call-outs should be boxed.

### Tag / Tag QC (Low complexity; Auto-tag OFF)
- Requires Tag/QC-specific linking document.
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Brand:** enter in Brand field ONLY if it appears in the Name field, EXACTLY as in Name (typically bolded). If more than one brand, leave brand blank.
- **Name:** write the entire name; include all items when multiple products share one price.
- **Price:** Pre Price Text (e.g. "Starting at", "2 For"), Current Price = sale price, Price Text (e.g. "each"/"set"), Original Price.
- **Sale story:** enter as in the flyer (e.g. "50% OFF", "Buy One Get One Free", "3 Days Only!", "GET 2,500 pts when you buy 2").
- **URL/SKU:** tag from the provided URL document — use Page # (Col D) and Ad Description (Col C) to find the right item, URL from Col B, and the SKU at the end of the URL. If multiple entries for one item, select the first.
- **Disclaimer:** usually marked with `*` or `+`; may include coupon conditions.
- **Categories:** categorize under the page's main heading (Inspired Beauty, Baby Needs, Pharmacy, Daily Living, Health & Wellness, Seasonal). Do NOT categorize page 1. Add "Inspired Beauty" page category to pages with the pink beauty design. Max 4 page categories.
- **Social:** box and tag all media icons (Twitter/Facebook/Instagram).
- **Inserts:** tag as LINKS (bewell, appointment, flu links, app store links, etc.).
- **Images:** prefer PDF image extraction when a clean image is available; if more than one item in the picture, leave the cutout of all images.
- **Spotchecks:** 3-day deals.

### Item Image QC (owned by DOC)
- Run the custom action → Set cutout images.

## Final QC (owned by DOC)
- Mark autostack spotcheck complete; add email links; page categories (4 max, none on page 1); rerun sessions if needed; check dates/theme; thumbnails; geography; vertical & horizontal scroll; mark items in-store only; apply "Deals" to pages 1–2.
- Verify links (appointment, bewell, flu pages, app store, store locator, prescribing, letsbewell).

## Flyer review / out-of-processing
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: Rexall OneGuide (Google Doc `1c1aRWvrck5L2B5D3Cr19AZSNAaXzxzseFQN5flf_Flc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
