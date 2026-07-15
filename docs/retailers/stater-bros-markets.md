# Stater Bros Markets — Processing Guide

> **Source:** Stater Bros Markets OneGuide (Google Doc `1hYwjxSERFXqwKsq5jFL4EGUARiFTqqIcSNCY25q_41M`), updated Jun 11, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#staterbros`, `#flex-processingsupport` |
| Hosted URL | staterbros.com/weeklyad |
| Flyer type | Weekly (1474) |
| Processing | Auto-stack; Flex (Processing Support); Strategic Ops (Feedel); no coupons |

## Files & schedule

- **When files arrive:** Wednesday (SKU document sometimes only comes Thursday — do not finish Setup QC until it arrives; if uploading Thursday, file an urgent processing ticket).
- **Cadence:** Available Tue→Tue, Valid Wed→Tue (one-day preview). **Preview date:** Friday (OS must finish tagging by Friday for the Flipp Ads team).
- **Linking document required**, plus a **SKU document** and a **Categories document** — all must be attached.
- Files land in the SFTP: flyer page PDFs, **PAGINATION [date].xlsm**, **Flipp Links Weekly Ad [date].xlsx**, store assignment **MAILER GROUPS ADDRESSES-[date].xls**, and **Stater Bros SKU Template-[date].xlsx**. The Categories doc (**Stater Bros-Categories**) is not in the SFTP — linked in the OneGuide.

## Upload & setup (owned by DOC)

- Manual upload of all pages; assign page numbers per the file-name numeration.
- **Flyer Creation → build pricing zones per the Pagination document:** use the "Group" name as the pricing-zone name; assign pages per the document.
- **Add stores via codesheet:** store assignment doc from SFTP, name "stores", **config `stater_bros_stores`**, PDF base directory `/`, **only the first toggle (Store or store-set assignment) checked**.
- **Edit Details:** Available Tue→Tue, Valid Wed→Tue, preview start Friday, available everywhere, external name **"Weekly Ad"**, no theme.
- Legibility heights **55/45**. Thumbnails Standard 4.
- **Attach vendor documents** (Links, SKU, Categories) and add this note to *all* vendor tasks: use the SKU document to add SKUs to all items (check details match when names are similar); use the link document to box/tag all links; use the category document to add categories.
- Check Geography (should match week-over-week). If a pricing zone has no FSAs assigned, its store was too close to another → use the **FSA Swap** custom action.
- Complete Setup QC and file an Urgent Processing Ticket.

## ⚠️ Common errors / risk items (retailer-specific)

- **SKU list vs page numbers:** if the spreadsheet SKU list doesn't match page numbers, **ignore page numbers and match by SKU / item details** — prioritize SKU accuracy over page order.
- **Do not tag any Spanish-language content.**
- **Sale Story — the word "Save" must NOT appear** (breaks the client side). "Save $xx" → Dollars Off field; "Save %" → Percent Off field. "Mix & Match" and "Buy X Get X Free" are fine — but do not include "Mix and Match" in a "Buy X Get X Free" sale story.
- Image QC: **clean PDF must always be chosen; never select cutouts.** For multi-item boxes, check all applicable PDF images and star the **first-listed** product as Primary.
- Wine items (pink) use % off in a specific way: **no text in Sale Story**, fill Percent Off, Disclaimer = "When you buy (#) or More Mix and Match."

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc required):** Exclude coupons, packaged deals (washers/dryers), retailer logo, sign-up page, social media. **Include special weblinks** — box and add a direct link per the linking document (e.g. "Digital Deals Section: Sign Up Here", CTA buttons, full pages).
- **Tag / Tag QC (Medium; Auto-tag ON; PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs; brand tagged per box-draw specifics.
  - **Name:** bold flyer text; tag both if 2+ bold names; follow flyer capitalization; do not include bullet points.
  - **Prefix:** numbers only (no "Sale"); **Postfix:** e.g. Each, lb, With Digital Deals, When you buy X — never include original price.
  - **Categories:** use the attached Category doc (Meat, Frozen, Service Deli, Bakery, Household Needs, Produce, Grocery, Alcohol). **Page categories** when 3+ same-type products on a page.
- **Image QC:** clean PDF always; multi-item boxes check all PDF images, star first item as Primary; never cutouts.

## Post-processing (owned by Vendor)

- **Item Category QC:** OS sets categories; review page by page. Watch for miscategorized alcohol. All **"Cleo & Leo"** items → Service Deli; verify only those carry the Service Deli category.
- **SKU QC:** Item Search SKU IS blank → find SKUs in the SKU document. If more than one or two items are missing, email the retailer's file-drop contact for additional SKUs.
- **Ad-hoc QC checks (FQC):** Pre Price Text CONTAINS `/` → remove "Sale" from X/Y prefixes; Sale Story CONTAINS "Mix and Match" → remove from "Buy X Get Y Free" items.
- **Final QC:** dates/legibility/thumbnails as above; check pink wine items; check SKUs against the SKU doc; page categories (none on page 1, "Digital Deals" where applicable ~page 3); pricing zones vertical/horizontal; Geography should read "No stores or FSAs/zips were added or removed." Store-not-assigned and missing-thumbnail warnings can be ignored.

## Flyer review & out-of-processing

- **Flyer Review type: Lite** (owned by DOL). Standard checks: dates (1-day preview), available everywhere, item-level valid dates, all items boxed/tagged with **clean PDF images**, multi-product boxes have all products selected with the first product as Primary.
- **Out-of-processing:** the client sometimes flags items appearing incorrectly during the week (usually a wrong SKU applied by OS). Find the item in the live flyer, apply the correct SKU from the SKU doc, save, and reply confirming — cc the Mercatus contacts so they can re-ingest for the Stater Bros website.

---
*Source: Stater Bros Markets OneGuide (Google Doc `1hYwjxSERFXqwKsq5jFL4EGUARiFTqqIcSNCY25q_41M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
