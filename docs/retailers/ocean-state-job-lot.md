# Ocean State Job Lot — Processing Guide

> **Source:** Ocean State Job Lot OneGuide (Google Doc `1ZO2yur5mgZX6bLrtew4tlIKESKOdBb5BYgTCBoQVlCQ`). OneGuide last updated Jul 14, 2026. Contacts/credentials omitted.
> **High box-draw complexity. ⚠️ Never use Fetch URL when tagging.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Available on all platforms |
| Slack channel(s) | `#osjl`, `#osjl-nativex`, `#flex-ocean-state-job-lot` |
| Hosted URL | http://www.flyertown.ca/flyers/oceanstatejoblot |
| Flyer type(s) & cadence | 6093: Weekly · 12183: Coming Attractions |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS N/A; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |
| Linking document | **Yes — SKU PDF and linking document (.xlsx), used for both Box and Tag** |

## Files & schedule (Weekly)

- **When files arrive:** Thursday (flyer PDFs); **SKU PDF and link document arrive Friday mornings**
- **Publication cadence:** Available From Wednesday, Valid From Wednesday/Thursday; Available To Thursday, Valid To Wednesday
- **Preview date:** Monday
- **Processing type:** Auto-stack
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC)

## Upload & setup

### Weekly (owned by DOC)
- **Manual upload on Fridays** (Pages > Edit).
- **⚠️ Risk item: wait to upload until the SKU PDF and Link Document are sent Friday mornings**, even though the flyer PDFs arrive earlier — **OS cannot box/tag without these documents.** If covering the account, message the DOL when done Friday to flag that the attachments need adding when available.
- Upload and auto-group pages (double-check order). Files are often uploaded with more than a week's lead — use the folder named with the valid date of the upcoming run.
- **⚠️ Risk item — page swaps before upload:** they generally replace the old PDF page asset with the new one (add all pages in the folder), but occasionally there are duplicates — use the newest version per the email instructions. When in doubt, upload both, open them, and decide which to keep/delete (the newer file sometimes has `_REV`; you can also check SFTP upload timestamps).
- **Flyer Creation:** 1 Pricing Zone "Base"; assign all stores. **Attach the URL .xlsx and SKU .pdf to all Vendor Tasks** with a note: "Please use spreadsheet and PDF File for Box Draw and Tag."
- Optional: if files won't attach to the Vendor Tasks, upload to a Google Drive folder and share with the vendors by email (per the OneGuide's template).

### Weekly Setup QC (owned by DOC)
- Pricing Zone: all pages assigned, language English; all stores assigned.
- **Edit Details (important):** Available from **Wednesday 7 PM** to **Wednesday 6:59 PM**; Valid from **Thursday 12 AM** to **Wednesday 11:59 PM**; set **Preview Date to Monday** (two days before go-live) at 12 AM to avoid items not being tagged before the preview link goes out.
- Standard 4 thumbnails. Complete Setup QC checklist.

### Coming Attractions (owned by Vendor)
- **Manual upload on Thursdays:** select the folder containing the date and Coming Attractions (CA) pages.
- Flyer Creation: 1 Pricing Zone "Base"; assign all stores. Note: "No additional linking docs, please box and tag as per pdf."
- Setup QC: same dates/preview/thumbnail rules as Weekly.

## QC specifics

**Box Draw (HIGH complexity — Auto-Box OFF, Box QC bot OFF; SKU PDF + linking .xlsx required)**
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Use the SKU PDF and linking Excel for reference. If information is incorrect, DO NOT stop box draw** — email the Flipp team to alert them and continue boxing/tagging using the sheet.
- If an item is NOT in the linking Excel, box it together with other items in the same section per the SKU PDF.
- **"Asst" lines:** box multiple items together when the links spreadsheet shows an "Asst" line; box items with individual SKUs/unique URLs separately. Treat each line in the links spreadsheet as one item box; use the **Page** and **Placement** columns to locate the box.
- Box each individual item (e.g. 10 rugs = 10 boxes). Multiple sizes/options with individual prices → **box each size as its own item** (no longer boxed as one list). Items without images must still be boxed (box text and price together); watch for items listed under other ad-blocks.
- **⚠️ Risk item — links-spreadsheet discrepancy:** items can be tagged separately if they have specified SKUs; if the sheet lists items separately on one page but together on another, follow the sheet. If no link is available but an item is obviously separate, box it separately and leave the URL blank.

**Tag / Tag QC (MEDIUM complexity — Auto-tag OFF, PDF Image Auto-Selection ON; linking doc required)**
- **⚠️ DO NOT USE FETCH URL WHEN TAGGING.**
- **Include:** brand (most items have none — add if identifiable), name (as it appears in the flyer), pre/postfix, valid dates (override when applicable), description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Prefixes:** use "Sale!", "All Sizes", "Your Choice" when they appear next to a product. **Do NOT** tag "buy for $$$ get $$$" deals using a "buy for" prefix + "get" postfix — only use a `- $$$` postfix when there are multiple prices. Package deals (e.g. "Buy 5 for…") → use "5 for" as the prefix.
- **Price:** singular item → Current Price, regular price in Raw Original Price ("Compare to $$$" goes in the description). List of options with various prices → lowest price in the Price field, postfix `- $$$` with the highest price. Select pre-/post-fixes from the drop-down lists.
- **Description:** multiple sizes/options listed here. If an ad-block has a header AND a list of options AND no per-item images, the description is the list of item details. If each item has its own image, use the header as the Name, box/tag each separately.
- **SKU:** use the attached document; items link by page + placement number. "Asst" SKU = more than one SKU per the SKU PDF — tag as many as possible.
- **Sale Story:** fill in as shown; do not tag "Dollars Off" unless specified. For "Buy a XX for $$… Get a $$ Crazy Deal Gift Card FREE!" include all relevant text. **1 Buy + 2 Get format** → tag as "Buy *Item Name* and get *Amount* Crazy Deal Gift Card Free!"
- **Categories:** use the category in the attached Excel; if an item isn't listed, pick the closest.
- **Disclaimer:** don't include percent-off/dollar-off amounts; only include disclaimers listed with an individual product (not page top/bottom).
- **URLs:** a Links Document is provided weekly (Product Name, SKU, URL, Page, Placement). Add the URL to all listed products. **If there is no URL, leave blank — DO NOT use Fetch URL.**
- **⚠️ Prices without decimals:** prices may print without a decimal (e.g. "$11.99" shown as $11 with a small ⁹⁹). **Always include decimals when tagging, even if the page shows none.**

**Image QC**
- Always check for a PDF image first; uniform backgrounds are OK. **Do not use PDF images with any visible background** (table edge, tiles, fabric, other items) — revert to the cutout even if it cuts off the item. Use cutouts when no PDF is available or when multiple item images are grouped together. If a cutout only shows the item name/price (product not visible), keep the cutout.

## Post-processing

### URL/Links QC (owned by Flex)
- Download the .pdf and .xlsx attached to the Vendor Tasks. Overview → Item Search → Field: URL, Condition: IS ___ (Blank). Sort by Page Grouping Index to go page by page.
- Use the SKU PDF and URL .xlsx to confirm whether each item should receive a URL. **Not all items get URLs** — if not assigned in the linking document, **leave blank, do not fetch.** Copy the URL from the URL column, paste into the URL field, save.
- Notes: if flyer names don't match the .xlsx, copy the name from the linking document. One box may cover many items (retailer preference) — apply the one link. Filter the URL sheet by the PG column; a missing page means no items on that page get URLs (skip it).

### Final QC — Weekly (owned by DOC)
- QC Thumbnails (Standard 4): 1065×600 (remove white border, cover pg 1&2), stock premium (cover pg 1), storefront carousel premium (cover pg 1&2), storefront carousel organic (cover pg 1).
- Edit Details: Available Wed 7 PM → Wed 6:59 PM; Valid Thu 12 AM → Wed 11:59 PM; Preview Date Monday; available everywhere (no toggles); no external run name; no theme unless specified.
- **Manage Tracking Codes → "Apply All Tracking Codes"** (no tracking codes exist, but this forces backend processes so all Shop Now buttons go live).
- Pages: all items QC'd; box/tag any links from the initial file-drop email. Pricing Zone: one "Base", all stores; check previews. Geography: no change WOW unless specified.
- **1 Buy + 2 Get deals:** ensure sale story tagged as "Buy *Item Name* and get *Amount* Crazy Deal Gift Card Free!"
- FQC Checklist — ignore the "some categories don't have thumbnails" warning. **Flyer sorting priority: Weekly, Lookbook (Seasonal), Coming Attractions.**

### Final QC — Coming Attractions (owned by Vendor)
- Same thumbnail/Edit Details rules as Weekly.
- **Override Image URL:** for any pages that do **not** have the "ARRIVED" callout on the product image, select **Do Not Use PDF Images** and enter the Coming Attractions VF logo asset URL in the **Override Image URL** field, then save. Repeat for all such items on all pages.
- Pages/Pricing Zone/Geography checks as above. FQC Checklist (ignore thumbnail warning). **Flyer sorting priority: Weekly, Coming Attractions, Lookbook (Seasonal)** — do not adjust yourself; flag if the order looks off.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- **Preview link:** send the Hosted 2.0 vertical preview link to the retailer contacts (cc DOL) the day before go-live (Wednesday 7 PM live), per the OneGuide's email template.
- **Corrections:** OSJL sends URL corrections Wednesday morning (highlighted in yellow on the sheet); have Flex apply all highlighted changes to the flyer run. Track all changes in the OSJL Change Tracker.
- Page swaps follow the baseline page-swap process.

---
*Source: Ocean State Job Lot OneGuide (Google Doc `1ZO2yur5mgZX6bLrtew4tlIKESKOdBb5BYgTCBoQVlCQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
