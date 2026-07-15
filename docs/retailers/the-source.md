# The Source — Processing Guide

> **Source:** The Source OneGuide (Google Doc `1W7ipScv6cPpEdADV0bCDFC90BjWFwXW2GlDcVnT7a6w`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel(s) | `#thesource` |
| Flyer type(s) & cadence | Weekly Flyer — ad-hoc schedule |
| Processing | Auto-stack; Flex completes some tasks; OS completes standard tasks |

## Files & schedule

- **Store list** arrives by email (the same document doubles as the codesheet for PDF upload and store distribution). If PDFs arrive without a store list, wait 1 business day then bump the store-list contact.
- **Preview date:** send preview URLs and missing URLs exactly **one week before go-live**.

## Upload & setup

1. Download the store list from email and save as a `.csv`.
2. Upload into Codesheets — **Config name `the_source`**, PDF base directory from the FTP, **toggles 3, 4, 5, 6**. Process Code Sheet.
3. Go to Pricing Zone and rename the pricing zone to **`en`**.
4. Upload the `.xlsx` version of the same codesheet into Codesheets for store distribution — **Config name `the_source_stores`**, PDF base directory `/`, **toggles 1, 4**. Process Code Sheet.
5. Ledge heights **28/18**; thumbnails **Standard 4**; spotlights; Setup QC in pipeline.
6. Overview → Edit Details: available everywhere; preview date 1 week before go-live; theme = no theme unless there is one; key messages = "Weekly Deals" / FR "Aubaines de la semaine".

### ⚠️ Common errors / risk items (retailer-specific)

- **Geography / dealer-direct stores:** geo shouldn't change much week over week; if a store is missing, check whether it closed. The Source also has **"dealer direct" stores** that don't get assigned to flyers — a regular store may have been switched to a dealer store, so cross-reference emails and leave a note in the comments.
- **Disclaimer junk text:** in Item Search, remove stray `seng` and `sfr` strings from disclaimers (typically at the end).
- **Links must use `https://`:** in Item Search, find URLs containing `http:`, export items, find-and-replace `http:` → `https:` (headers `item_id`, `sku`, `url`), re-import via Import Items, and repeat until none remain. Then Sessions → Re-Verify URLs.
- Sometimes a row of phones has no price or sale story — do **not** box/tag unless the retailer emails you to.

## QC specifics

- **Box Draw (Low):** linking document required. **Include** social media, sign-up page, special weblinks, retailer logo, packaged deals; **exclude** coupons. Open the version with the most FSAs to confirm all CTAs and banners are boxed; compare item counts across pricing zones and add/remove boxes if they differ.
- **Tag / Tag QC (Low):** **include** brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories; **exclude** disclaimer and URLs (tagging), though URLs are managed via the `https://` and preview-URL steps.
- **Item Category QC / Item Image QC:** n/a.
- **Categories (Pages → Categories):** search by grouping, enter categories to the first then Copy to Same Index. **No categories on page 1**; cap at **3 categories/page**; for random items (e.g. Fitbit) use "gifts and gadgets".

## Pre-FQC / out-of-processing

- Mark Wayfinding QC and Spotcheck QC complete. Add `utm_campaign` = `monthx` at the Flyer Run level (Manage Tracking Codes → Apply All).
- **Preview URLs:** one week before go-live, send English + French preview URLs (Overview → Preview URLs) plus the "en" pricing-zone vertical preview and the missing-URLs report (Overview → Items without a URL, kept to item ID / page # / item name with a `url` header added). Expect multiple revisions to links/pages.

---
*Source: The Source OneGuide (Google Doc `1W7ipScv6cPpEdADV0bCDFC90BjWFwXW2GlDcVnT7a6w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
