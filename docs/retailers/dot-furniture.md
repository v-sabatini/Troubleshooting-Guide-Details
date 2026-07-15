# DOT Furniture — Processing Guide

> **Source:** DOT Furniture OneGuide (Google Doc `1sNp-tknAPZ7-tiIwW3dNC6IoA-hV8oKpmYuBwaI8vuU`), updated Apr 25, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | **Flipp only** (Flipp & Distribution; hidden on Hosted) |
| Slack channel(s) | `#dot_furniture` |
| Hosted URL | dot-furniture.com |
| Flyer type(s) & cadence | **Flyer** (11078) — **ad hoc** |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/retailer data services |

## Files & schedule

- **When files arrive:** ad hoc. Dates (Available/Valid From/To) confirmed by DOC per the retailer email. **No preview date.**
- **Linking document:** Yes — a Link Sheet (.xls) from the FTP, used for both Box and Tag.

## Upload & setup

**Pre-setup (DOC):** DOC builds the flyer runs from the retailer email, drops files into the FTP, and requests PSS Ad-Hoc support. (SFTP credentials in the OneGuide — not stored here.)

**Manual upload (Vendor):** Pages → Edit → find the FTP folder → Select All Pages → Autogroup → Save & Complete. Flyer Creation → Start Task → **1 Pricing Zone (Base)**, ensure all pages added → Save & Complete → Add All Stores → wait for sessions.

**Setup (Vendor):**
- Download the Link Sheet (.xls) from the FTP and **Mass Attach** to Vendor Tasks; click through Tag, Box QC, Tag QC to confirm links attached to all tasks.
- Edit Details: dates confirmed by DOC; No preview date; **not available on Hosted**; External Run Name None; no theme.
- Legibility heights = **45, 35**. Thumbnails Standard 4; confirm sessions run.

### ⚠️ Common errors / risk items (retailer-specific)

- **Thumbnail QC — logo MUST be visible** (risk item).
- **Follow the Link Sheet order** — items are listed top-of-page to bottom-of-page; match links to product by name & price.
- Some items have **no sale price** and/or **no product image** (e.g. Sunnyvale/Orion collections) — box the **title and/or lifestyle image** as listed on the Link Sheet.
- **Last-page links are NOT on the Link Sheet.** Box and tag them with display type **Link**: Shop In-Store → `dot-furniture.com/20272/`; Shop Online → `dot-furniture.com/store/`.
- **Spotcheck pricing discrepancies — especially Original Price.**

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF).** Linking doc required. **Include** the Shop Online / Shop In-Store weblinks (last page); coupons/packaged deals rarely occur but include. **Exclude** retailer logo (unless indicated on the Link Sheet), sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include the bolded title as Name (**Brand field not required**), price, original price (strikethrough), categories, URLs. Description/pre/postfix/sale story/disclaimer/valid dates only **if applicable** (most items lack them). **Exclude SKU.**
  - **Sale Story:** include extra sale info shown on the page (e.g. "Market Umbrellas — Up to 20% off").
  - **Valid dates:** only tag if items fall outside the flyer valid dates.
  - **URLs:** every item should have a URL from the Link Sheet. If a page is a lifestyle image titled "___ Collection Shop Now" with no specific price, change the item title to "Link". Where a link has no associated product image, box the name and change item type to **Link**.
- **Image QC:** select the PDF image when available; choose clean/clear PDFs over lifestyle images, but lifestyle images are OK when clean PDFs aren't available.

## Final QC / go-live (owned by Vendor)

- Mark Autostack complete; confirm dates (per retailer email); hidden on Hosted; internal & external run name = flyer callout; no theme.
- Item Image QC (Overview → generate → unselect PDFs → filter; ensure clear white-background PDFs). Link QC via Overview → Items without URL → fill from Link Sheet.
- Confirm Tag/Tag QC items match (both green); confirm last-page Shop Online/Shop In-Store boxed & tagged.
- Page categories: remove from page 1, apply the most appropriate; check vertical preview; use the Link Sheet to confirm no boxes missed.
- Confirm sessions run and FSAs generated; re-verify URLs; Geography tab green; complete FQC checklist.
- **Flyer Review type: Lite** (owned by FLEX).
- **Out-of-processing:** standard page swap. Note the annual **Black Friday** operations-guidelines comms.

---
*Source: DOT Furniture OneGuide (Google Doc `1sNp-tknAPZ7-tiIwW3dNC6IoA-hV8oKpmYuBwaI8vuU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
