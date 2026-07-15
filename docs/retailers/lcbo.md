# LCBO — Processing Guide

> **Source:** LCBO OneGuide (Google Doc `1qfEkj9qYxfFKg6C_9Gsv4OyGmz0iQSv8bR3Jlj20F9g`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Platforms / availability | All platforms |
| Slack channel(s) | `lcbo` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | FLYERS2025, ad-hoc |
| Processing | Auto-stack |
| Who's involved | Vendor owns setup/FQC; no OS beyond standard; no Flex; no coupons; no Feedel |
| Linking document | Yes (used for both Box and Tag) |

English-language account. Workflow includes an **Internal Preview** at 2 and 1 days out.

## Files & schedule

- **Files arrive:** ad-hoc. Available/Valid From/To all ad-hoc.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages → Edit → select all from SFTP (folders match the internal flyer run name, e.g. "P9"). Auto-Group or manually number pages; **English pages only**. Save & Confirm. Attach the corresponding linking document (usually emailed).
- **Pricing zone:** create PZ based on store details in the email (one version = "Base"). Save & Confirm. Add all applicable stores.

### Setup QC
- Confirm all pages uploaded (PZ → Items View); confirm no un-uploaded pages remain in SFTP; confirm flyer dates (first page); thumbnails Standard 4; **No Theme, no external run name**.

## ⚠️ Common errors / risk items

- **SKU:** every item must have a SKU (from PDF, else from the linking doc). Item Search: SKU is blank → fix from linking doc/PDF.
- **URLs with UTM parameters:** every box must have a URL. Item Search URL is blank → add from linking doc (100% should be provided). Then Item Search URL is NOT blank (note count), update to URL **contains `utm_campaign`** — count must not drop, or UTM params were missed.
- **Aeroplan Bonus Points:** if an "AEROPLAN" callout is on the PDF, tag the **Sale Story** as **"Aeroplan # bonus points"**.
- **Direct links may be missed:** if a URL is provided in the linking doc, ensure the CTA is boxed and tagged.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc used for both Box/Tag. **Include special weblinks**; exclude coupons, packaged deals, retailer logo, sign-up page, social media. Each item or callout gets its **own** individual box.
- **Tag / Tag QC (Medium; Auto-tag OFF):** linking doc used for both. **Include** brand, name, pre/postfix, valid dates, description (from PDF + linking doc), SKU (from linking doc), price, sale story, categories, disclaimer, original price, URLs. CTAs found on the linking doc.

## Final QC / go-live notes (owned by Vendor)

- Confirm dates (per PDF), available on all platforms, thumbnails incl. retailer logo.
- All boxed/tagged; spotchecks 20%; previews clickable; sessions complete; geography consistent (flag changes).
- Run the SKU, URL/UTM, and Aeroplan checks above.
- **Retailer preview (owned by DOC):** once processed, send a preview link to the retailer. Contingent on files arriving **≥5 business days** lead time — otherwise feedback is provided post-live. Set the preview date so the URL functions.
- **Flyer Review type: Lite** (owned by Vendor).

---
*Source: LCBO OneGuide (Google Doc `1qfEkj9qYxfFKg6C_9Gsv4OyGmz0iQSv8bR3Jlj20F9g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
