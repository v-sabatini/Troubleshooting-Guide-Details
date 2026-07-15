# Coastal Farm — Processing Guide

> **Source:** Coastal Farm OneGuide (Google Doc `1qU6874NurYkV57tlFMTOGfWcsV9az7b4VHqtBFiDWKY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#coastalfarm` |
| Hosted URL | coastalcountry.com |
| Flyer type(s) | Weekly Ad (ID 4175) — **ad-hoc** |
| Processing | Auto-stack; Flex = Processing Support; no coupons; no Feedel |

## Files & schedule
- **Files received:** ad-hoc (all dates ad-hoc; ~10-day workflow).
- **Preview date:** set **5–6 days ahead of live date** depending on retailer lead time (confirm with processor if unsure). This preview drives the item-export/import correction loop.
- No linking document.
- **~5 days out:** send item report to retailer; **~2 days out:** retailer returns updated report and item import is completed.

## Upload & setup (owned by Flex)
- Manual upload in FTP → Pages → Edit → select pages → Auto-group.
  - **Wrap pages:** place in the **last position** after all main pages, and **manually group wrap pages in consecutive order.**
- **One pricing zone; add all stores.**
- Edit Details: Available/Valid dates match the PDF; **External Run Name = the main Page-1 title** (e.g. "Early Bird Black Friday"); available everywhere; no theme.

## Box Draw (Low — Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals, retailer logo, sign-up page. **Exclude:** coupons, social media, special weblinks.
- Box all items individually (draw as large as possible without overlap); use text boxes as needed.
- **Multiple sizes:** box together if one description; box separately if different descriptions.
- **Coastal Farm logo:** always box, Link display type, tag URL coastalcountry.com.

## Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)
- **Include:** name, valid dates, sale story, categories. **Exclude:** brand, pre/postfix, description, SKU, **price, original price**, disclaimer(mostly), URLs.
- **Name:** as it appears; include weight (lb) in Name; don't put brand in the Brand field if it's in the name.
- **DO NOT tag** prefix/current price/postfix/original price/SKU.
- Sale story & disclaimer: enter as seen when applicable.
- **Retailer logo:** Link display type → coastalcountry.com.

## ⚠️ Common errors / risk items (retailer-specific)
- **NO pricing in the item pop.** The retailer communicates all deals/prices via **Sale Story**. Original price, current price, price text, and pre-price text must be **ALL BLANK**. Use Item Search (`Current Price is not [blank]` and `Original Price is not [blank]`) to find and clear any pricing tagging.
- **Item export loop:** export items → keep only `item_id, page, name, sale_story, url` → clear all pricing → send `.xlsx` to the retailer. On import back, keep `item_id, sku, brand, name, sale_story, url`; brand column all blank; add empty SKU column; delete page/comments columns; save `.csv` → Import Items.
- **Logos/QR codes** must be boxed and tagged on the **first and last pages** before sending the export; delete boxing on pages with the bottom banner.
- Wrap pages: include the wrap-page numbering in the page column of the export.

## Image QC
- PDF images preferred; use cutout when not clean (non-white background, half-cut) or when no image exists.

## FQC (owned by DOL; Lite)
- Mark Autostack Spotcheck complete; Edit Details dates correct; external run name = Page-1 title; available everywhere; no theme (watch for carousel themes during Black Friday/Christmas). Leg heights 50/40; Standard 4 thumbnails.
- **Confirm all current/original prices are blank via Item Search.** Items without a URL = 0. Check sessions.
- **FQC checklist quirk:** a red warning that the pricing zone has no items with a current price is expected — override with "current prices not tagged for this retailer". On Save & Complete you'll hit the content-policy warning again; click OK and Save & Complete once more.

---
*Source: Coastal Farm OneGuide (Google Doc `1qU6874NurYkV57tlFMTOGfWcsV9az7b4VHqtBFiDWKY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
