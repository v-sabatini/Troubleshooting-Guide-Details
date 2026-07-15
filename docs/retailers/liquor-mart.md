# Liquor Mart — Processing Guide

> **Source:** Liquor Mart OneGuide (Google Doc `1qZJOZiLpEwDz1KdAVXnfkL8BLa9pwmbZSlj7jtNwHpY`), updated Mar 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel | `#flexflyerreview` |
| Hosted URL | liquormarts.ca |
| Flyer types | Monthly Flyer · General Flyer |
| Processing | Auto-stack; Flex PSS Upload & FQC; DOL flyer review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad hoc.
- **Cadence:** Available/Valid From 1st of month, Available/Valid To last day of month.
- **Preview date:** internal 1-day preview.
- **Linking document:** Yes — used for both Box Draw and Tag.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → select SFTP files for the month; autogroup (English pages only); Save & Confirm — **do NOT process internally**.
- **Pricing zone:** one zone (can be "Base") per store details in the email; add all applicable stores (all 40).
- **Links:** attach the retailer's linking doc (in SFTP, labelled by month) to all tasks. Ignore other docs (e.g. Product Price List).
- **Image files:** the retailer provides white-background PNGs per item via FTP folders/subfolders. Confirm PNGs exist (auto-marked-off) in a monthly folder broken out by page; if missing, flag to the Coordinator (non-blocking).
- **Image import (white-background):** copy only the **first part** of the SFTP base path (e.g. `/LM May 2025/`, not `/LM May 2025/Page 1`). Sessions tab → paste into FTP URL under "Image Import" → select "From Scratch" → Submit. Then Item Image QC → "Generate Images" → select all white-background images per item.

### Setup QC checklist
- Confirm all pages uploaded (Pricing Zone → Items View; nothing left unuploaded in SFTP).
- Confirm flyer dates on page 1; Standard 4 thumbnails; No Theme, No External Run Name.

## ⚠️ Common errors / risk items

- **Image import base path** — grab only the first part of the path or the import fails.
- **Tagging text case must match** the PDF/linking doc — do not force all-uppercase (see Tag QC).
- **Name-field errors:** bold text = Name field. Watch for truncated names (e.g. "SMIRNO" instead of "SMIRNOFF", "WHISKY" vs "WHISKEY") and for region words like "(Manitoba)"/"(Canada)" wrongly placed in Description when they belong in Name.
- **Item-level valid dates:** "hot buy" pages (usually positions 2 & 3) and any page with dates outside the full flyer validity need item-level valid dates.

## QC specifics

- **Box Draw (Medium; Auto-Box OFF, Box QC bot OFF):** linking doc required. Exclude coupons, packaged deals, retailer logo, sign-up page, social media; **include special weblinks**. Box all single items (text boxes where not in a grid); box non-item CTAs per the link document.
- **Tag / Tag QC (Medium; Auto-tag OFF):** linking doc required. Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Tag from the link document; **copy naming conventions exactly, matching case**.
  - **SKU also goes in the Description field** (e.g. `355 ml | 70449`); description = unbolded text (product size + SKU).
  - Non-item CTAs tagged per the link document.
  - **Bonus Miles** included as the Sales Story for **all items in the bundle**.
  - Item-level valid dates where a page notes dates outside flyer validity.
- **Image QC (owned by Flex):** white-background images required — run the Image Import (see above) and select all white-background images per item.

## Post-processing (owned by Flex)

- **Links QC:** Items Without URL check — apply links from the URL document if items appear.
- **UTM codes:** apply tracking UTMs to every Liquor Mart flyer (Overview → Apply Tracking Codes → Flyer Type tracking codes).
- **Pre-FQC (DOC):** confirm dates vs PDF; availability toggles; thumbnails with logo; legibility heights (60, 40); all boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography correct.

## FQC / flyer review

- **Final QC (Flex):** FQC checklist.
- **Flyer Review type: Medium** (owned by DOL): flyer dates, previews correct, all items tagged, no extra auto-boxes, geography correct, available everywhere, items-without-URL resolved (confirm CTAs on last page), as many white-background images as possible (flag cutouts/non-white), 'hot buy' pages (positions 2 & 3) have item-level valid dates, UTMs applied.

---
*Source: Liquor Mart OneGuide (Google Doc `1qZJOZiLpEwDz1KdAVXnfkL8BLa9pwmbZSlj7jtNwHpY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
