# Hart Stores — Processing Guide

> **Source:** Hart Stores OneGuide (Google Doc `1Vzod6nw2Jp_HafBOnuqM1VCPieAOCTuacFmzmedIZkw`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#hart`, `#flex-processingsupport` |
| Hosted URL | hartstores.com/pages/flyers |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing/FQC; OS (upload); no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Friday.
- **Cadence:** Available From Wednesday, Valid From Tuesday; Available To Wednesday, Valid To Tuesday.
- No preview date, no linking document.
- **Custom action:** "Set Cut-out Images" custom action at FQC.

## Upload & setup

- Regular **manual upload**. Two languages: **English (Ontario pages)** and **French (Quebec pages)**.
- **If region is not specified, use the same page for both languages** — this requires uploading the pages twice and assigning each set to an EN and FR pricing zone.
- Region-specific pages are typically the last page. Assign language to pages (English/French).

### Pricing zones
- Create **English and French** pricing zones. If there are separate ON and QB regions, make an EN and FR zone for each: **ON EN, ON FR, QB EN, QB FR** (language + which last page — ON or QB).
- **Add all stores to each pricing zone.** As of Nov 2024 there should be **135 stores per PZ.**
- Double-check dates (left side of the first page) match the flyer run dates.

### Setup QC
- No theme, no external run name; Standard 4 thumbnails; complete setup QC checklist.
- Add the Flyer ID to the VAST tracker for FQC.

## ⚠️ Common errors / risk items
- **If region isn't specified, upload pages twice** (once per language) so both EN and FR zones have them.
- **Item counts must match across all versions** — FR and EN for both Quebec and Ontario should all have the same item count. If counts differ, fix box/tag (often two SKUs were boxed together when they should be separate).
- Ensure **135 stores per PZ**.
- **Image QC: select cutouts only** (not PDF images).

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks. No linking doc.
- Draw a box whenever there's a unique price. Box "Your Choice" items separately.
- **Mattresses:** box smallest size (usually twin) with the main photo; box other sizes separately. **Pillows:** box sizes separately.
- If items share a price but have different SKUs, box each separately; if multiple items share a SKU, box together.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude:** URLs. Linking doc required (tag-specific).
- **Name/Brand:** name in larger (sometimes bold) text; if branded, include brand in both brand and name fields; include size in name for mattresses/pillows.
- **SKU:** enter in both the SKU field and below the description.
- **Valid dates:** items typically valid for the full flyer (no item dates needed); enter item dates only if labelled differently.

### Image QC
- **Select cutouts only.**

## Post-processing / FQC (owned by Flex)
- Mark Autostack Spotcheck complete.
- Edit Details: Available/Valid dates match the flyer (page 1); available everywhere; no external run name; no theme.
- Legibility heights: **55/40.** Thumbnails: Standard 4.
- Pages: ensure every SKU has its own box and tag.
- Pricing Zones: same item count across all versions (fix box/tag if not); all stores added (135/PZ); check vertical preview & full screen (items clickable, boxes appear).
- Sessions: none errored/needing rerun; mark items In-Store Only.
- Geography: no stores/FSAs removed.
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Hart Stores OneGuide (Google Doc `1Vzod6nw2Jp_HafBOnuqM1VCPieAOCTuacFmzmedIZkw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
