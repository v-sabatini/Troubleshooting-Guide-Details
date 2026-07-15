# Showcase US / Showcase (CAD) — Processing Guide

> **Source:** Showcase OneGuide (Google Doc `1jXmafS1ukJMBMqCdpWOnWn7KzRIVUnuCuHiwx4m_kQE`), updated May 2, 2024. Contacts/credentials omitted.

Two merchant instances processed the same way: **Showcase (Canada)** and **Showcase US**. Each has its own files, UTM document, and FTP.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` |
| Hosted URLs | shopatshowcaseusa.com/pages/flyer · ca.shopatshowcase.com/pages/flyer |
| Publication | Both CAN & USA; live Monday–Sunday (2–3 pages US, 4–6 pages CAD) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |
| Linking document | Yes |
| Account guide | Confluence "Showcase CAN + US Account Guide" |

## Files & schedule

- **Files received:** Friday, variable times — **normally very short lead time; we push back go-live if delayed.**
- **Cadence:** Available/Valid From Monday → To Sunday.

## Upload & setup (owned by Flex)

- Pages are in the FTP (folder specifies date). **Select the correct files per instance:**
  - **Showcase Merchant** = Canadian → choose files that do **not** contain "USA" in the name.
  - **Showcase US Merchant** → choose the USA files.
  - In both, pick the PDFs numbered page 1, 2, etc.
- Auto-group pages, verify indexing. Create **one** pricing zone named **Base** (only one zone for this publication). Assign all stores.
- **Dates:** the flyer shows "Valid Until" with no start date — **the start date is always the Monday before.**
- **UTM linking doc:** from the FTP, download the file with "UTM" in the name (matching CAN or USA). One manipulation: copy the "Hyperlink w/ UTM" column → Paste Special → **Values Only** into the URL column; delete columns C and D — leaving only the UTM URLs. Download as XLS and attach to all vendor tasks. Mark Setup QC complete.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (Tag specific). Exclude coupons, packaged deals. **Include retailer logo, sign-up, social, special weblinks.** Box items as they appear; use text boxes where needed; **box the banners at the bottom of every page and store-location pages** (links in the linking spreadsheet); box the retailer's logo on each page.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-select ON.** Include brand, name, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix, valid dates, SKU.**
  - **Name/Brand:** tag as in the flyer; if the name is inside the product image and text extraction misses it, type it in full (e.g. "GOLI" → "GOLI APPLE CIDER VINEGAR GUMMIES").
  - **Price / pre-postfix:** **do NOT tag "% off" or "$ off" as pre/postfix — those are the sale story.** Only words like "only" or "pre-order" in the red box are pre/postfix.
  - **Sale Story:** tag the "% off" / "$ off" amounts (red boxes) here.
  - **Valid dates:** tag only if the item has separate valid dates.
  - **URLs:** use all URLs in the provided document. If no banner link is provided: **Showcase CAN** → `https://www.shopatshowcasecanada.com/`; **Showcase US** → the US fallback link in the OneGuide.
- **Image QC:** select the cleanest PDF image without a black background; otherwise use the cutout ("Do not use PDF Image").
- **Spotchecks:** usually "spelling error" flags on brand names — confirm spelling in the PDF.

## Final QC / go-live (owned by DOC)

- Check all items have a URL (find missing links in the linking doc).
- Standard thumbnail QC; Edit Details: no external run name, apply No Theme; all stores added (check geo); available on all platforms.
- **Flyer Review type: Lite** — valid dates from bottom of pages; available-from is ad-hoc (may be after valid-from due to late files); available-to matches valid-to; sales story dates on every page; everything boxed is tagged; page categories set; previews clickable; sessions run; vendor tasks complete; geography consistent.

---
*Source: Showcase OneGuide (Google Doc `1jXmafS1ukJMBMqCdpWOnWn7KzRIVUnuCuHiwx4m_kQE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
