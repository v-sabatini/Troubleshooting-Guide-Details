# Indigo — Processing Guide

> **Source:** Indigo OneGuide (Google Doc `1yIqlHCTAcc7YLEtT7bhl0hCBaTl7XRRuYOPqJzHOI_8`), updated May 15, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (Kids Catalogue is **Hidden in Hosted** on the main run; a hosted-only clone handles hosted) |
| Slack channel(s) | `#indigo` |
| Hosted URL | chapters.indigo.ca |
| Flyer types | **Kids Catalogue (1483)** — yearly publication during the holidays |
| Processing | Auto-stack; Flex (Processing Support / setup), FLEX Image QC, DOC FQC; Feedel/data services — **yes**; no coupons |

Linking document (Product Map + Product List) required for both Box and Tag.

## Files & schedule

- **When files arrive:** yearly (holiday season). Dates must be confirmed with the retailer.

## Upload & setup (owned by FLEX)

- **Shell:** create a flyer run in Kids Catalogue; dates confirmed with retailer; internal name per retailer email; **Availability: Hidden in Hosted** (hosted handled by a clone — see Out-of-processing); external run name = the publication callout; apply seasonal theme per campaign.
- **Manual upload:** upload files from the **lowercase folder** (auto-split by Fadmin); do **not** upload the mapping file. Upload as English (default), Auto-Group. If there's a cover page, hold it until the end (cover-page links/category often come later by email).
- **Pricing zones:** Base, English. Create a store set from Indigo's store list — Merchant Page → Store/Sets → CSV with headers `store_set_name`,`merchant_store_code`, upload, add in PZ. **Do not include US stores; remove store 0001** (added to the hosted clone later).
- **Vendor prep:** download the PDF mapping guides from FTP, upload them to a Google Drive; attach the Excel linking document to vendor tasks; email OS the Excel linking document + Google Drive link (recipients in the OneGuide — contacts not stored here).

### Setup QC checklist

- Thumbnails: Standard 4 (plus custom tiles if provided — confirm with BD). **Leg heights 60/50.**

## ⚠️ Common errors / risk items (retailer-specific)

- **Everything is driven by the Product Map + Product List spreadsheet** attached to vendor tasks — box and tag strictly from them.
- **Product Map (boxing):** each product on a page has a letter (A, B, C…). **Box every product separately unless the document says otherwise.**
- **Product List (tagging):** columns give page # (grey), Product ID/letter (red), **Name** (yellow), **UPC/ISBN = SKU** (blue), and **URL** (green). Match each item's letter on the Product Map and tag Name/SKU/URL from the corresponding row.
- **Brand:** enter only in the Brand field — never in any other field.
- **Valid dates:** only add date overrides when an item's sale story indicates it's part of a promotion.
- **Categories:** every item needs one from — Kids, Accessories, Electronics, Toys, Baby, Holiday Home Decor, Gift Ideas, Holiday Gifts, Books, For The Home, Heather's Gifts.
- **Spotchecks:** use the spreadsheet for flagged words; item name must match the spreadsheet (else use the name on the page).

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF.** Linking document required. **Include** packaged deals, sign-up page, social media, special weblinks. **Exclude** coupons, retailer logo.
- **Tag / Tag QC — Medium complexity. Auto-tag OFF.** Linking document required. Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs (all from the Product List).
- **Image QC:** PDF preferred; cutout sufficient if no clean PDF.

### Final QC (DOC-owned) highlights

- Thumbnails Standard 4 (+ custom tiles if provided); leg heights 60/50; **no page categories**.
- Check items without a URL and add if applicable — **Indigo sends updated URL lists; do NOT search their website.** Use PDF images where possible.
- **Tracking codes:** only **one** tracking code allowed (confirm with the lead if more). Overview → Ad Hoc Processing → Manage Tracking Code — Dynamic Variable, Code Source Hosted, variable name/value per the monthly WBS. Click Apply; **re-apply after any page swap.**

## Out-of-processing / hosted clone

- Prefer a preview; link callouts at page bottoms to the website; create a Jira ticket for page-swap triggers.
- **Clone for Hosted 2.0:** clone into the "Guide" flyer type, prefix name with `[Hosted]`, update tracking code per WBS, then Hide in Distribution, Hide in Flipp, Unhide in Hosted; double-check WBS dates; remove all stores and add store 0001.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite.**

---
*Source: Indigo OneGuide (Google Doc `1yIqlHCTAcc7YLEtT7bhl0hCBaTl7XRRuYOPqJzHOI_8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
