# Globo Shoes — Processing Guide

> **Source:** Globo Shoes OneGuide (Google Doc `13HmwPE88iYelRX3nkU02FlOxSg1s-8kmM26BOXUvW04`), updated Oct 23, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#globo` |
| Hosted URL | globoshoes.com |
| Flyer type(s) & cadence | Ad Hoc (flyer 1307) |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Linking document:** Yes — `.xlsx` from the FTP (name varies, e.g. `GLOBO_BTS_LINKS.xls`, `FLIPP BUILDING_JULY.xlsx`). Used for both box draw/box QC and tag/QC.

## Upload & setup (owned by Flex)

- Confirm dates from the contact or the account's BD.
- **Manual upload.** Two separate files for **English** and **French**, labeled accordingly. Take the lower-case (split) files; mark the full PDF as uploaded. Set French pages to French language, Save → Autogroup → Save and Complete.
- **Pricing zones:** two zones — **EN** and **FR** — with language set accordingly. Open Store Sets and add all stores to both zones. (The store warning on the overview page at later stages can be ignored.)
- Download the linking `.xlsx` from FTP and **mass-attach to Vendor Tasks for OS**.

### Setup QC
- Set **External run name** based on callouts on the first pages (EN and FR).
- **Hide on hosted** — this ensures live checks are done on the app instead.

## ⚠️ Common errors / risk items
- **Globo Shoes logo must ALWAYS be tagged** — links to globoshoes.com.
- **Language of links** — make sure English and French links are correct.
- **Colour variations boxed separately** — each colour has its own SKU and URL in the linking document; items may have overlapping text boxes.
- **404 links: LEAVE THE LINK IN THE URL FIELD** — do not remove it. Items are often unavailable, so links may not be live; the retailer is aware.
- **Flagged-word spotchecks:** because of item arrangement and letter labels (A-Name, B-Name), expect many flagged words. Instead of Approve, click **Add as Proper Name** and add a note referencing Tag/Tag QC instructions.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, special weblinks. **Exclude:** coupons, packaged deals, sign-up page, social media.
- Globo uses data piping and image extraction; boxes can overlap a little.
- Box items individually by **colour AND style**. When a product has only ONE colour/SKU, box the shoes together (not separately).
- Use text boxes when needed; link item box to text box via letter labels (A, B, C…). Styles boxed separately may share a text box.
- Be as specific as possible when assigning page categories.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude:** disclaimer.
- **Name:** as on flyer; brand/Globo name identifier entered separately (name identifier in CAPS, e.g. "Solemate Women RATHIEL"). Do not include brand in Name field or letter labels (A-/B-) in the name.
- **Description:** include shoe sizes, demographic (mens/womens/kids), and additional colours.
- **Price:** current price in bold (on item or as a Hero price at top of a section); original price in unbold.
- **SKU field:** enter the item name + colour code combo as on the URL doc (e.g. `FITZSIMON-98`).
- **URLs:** use the URL spreadsheet. Logos link to globoshoes.com (Name: Globo Shoes). Use SKU/item name and **placement number** to match colour variants to correct links (compare images by opening the URL). Match link language.
- **Categories — use ONLY these analytics categories:** Women's Footwear, Men's Footwear, Men's Athletic, Women's Athletic, Kids Footwear, Boys Shoes, Girls Shoes, Bags/Handbags & Wallets.

### Image QC
- Mostly cutout images. PDF images tend to have a black background and are usually not clean enough to use.

## Post-processing / FQC
- Mark Autostack Spotcheck complete.
- **Legibility heights:** Scan 55, Read 45. QC thumbnails: Standard 4.
- Open "Items without a URL" and cross-check the linking document.
- Mark items In-Store Only.
- Pricing zone item view: check dates (may not be present — retailer comms are source of truth), all items boxed, correct languages per zone (EN/FR), pages sequential, page categories accurate.
- Geography should read "No new stores/fsas added or removed" unless noted.
- Ignore the "Some categories do not have thumbnails" error.
- **Flyer Review type: Lite.**

---
*Source: Globo Shoes OneGuide (Google Doc `13HmwPE88iYelRX3nkU02FlOxSg1s-8kmM26BOXUvW04`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
