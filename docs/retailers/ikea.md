# IKEA — Processing Guide

> **Source:** IKEA OneGuide (Google Doc `1p2g6USLb7wopGIMZ8kkp-09dL7gwWf2bELSWF85OJOs`), updated Aug 21, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#ikeacanada`, `#flex-processingsupport` |
| Flyer types | Event (1079) — ad-hoc |
| Processing | Auto-stack; Vendor/DOC setup, DOC FQC, Flex Flyer Review; **FSA-based** (no stores); no coupons, no Feedel/data services |

Bilingual account (English + French pricing zones). Linking document used for both Box and Tag.

## Files & schedule

- **When files arrive:** ad-hoc; all publication dates ad-hoc.
- **Workflow:** Upload & Setup owned by Vendor/DOC; FQC owned by DOC.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group or manually add grouping numbers; **ensure correct languages** (English for EN pages, French for FR pages). Save & Confirm. **Do NOT process internally.**
- **Pricing zones:** create a **Base pricing zone for EN and one for FR**, select applicable pages, Save & Confirm.
- **IKEA is FSA-based — do NOT add any stores.** Assign FSAs via the **`Assign FSA from CSV` custom action** using the IKEA template: copy the EN pricing-zone ID into the blue `flyer_id` cells and the FR pricing-zone ID into the yellow cells, download as CSV, run the custom action for both zones.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View); no un-uploaded SFTP pages.
- Confirm flyer dates (usually first/last page); Thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)

- **Category tagging (recurring confusion):** when unsure of an item's category, **visit ikea.ca and search the item** — use the site's general category. Reference examples: Bathroom (sink, faucet, towel), Bedroom (duvet, mattress, PAX/closet storage, nightstand, bed frame), Decorations (potted plant, picture, poster, Ribba frame, vase, candle holder), Home Accents (vase, candle holder, candle), Kitchen (countertop, step stool, plates, sinks, faucets, cutlery), Living Room (coffee table, bookcase, shelf unit, basket, sofa), Textile (carpets, rugs, curtains).
- **Page links:** some first-page links in the linking document must be set as **Display Type: Page Link**, linking to the page number specified.
- **URLs:** almost all items should have a URL — if an item lacks one, check the link sheet.
- **Brand should NOT be tagged on any item.**

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON (enabled May 2025), Box QC bot OFF.** Linking document required. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media; **include special weblinks only if listed on the link sheet.**
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Linking document required. Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude brand, pre/postfix, and valid dates.**
- **Image QC:** clean PDFs preferred; use cutouts if no clean PDF.
- **Spotchecks:** reference Tag/Tag QC; confirm brand is not tagged.

## Final QC (DOC-owned) / flyer review

- Pre-FQC: verify URLs (almost all items have one; check link sheet for any missing); confirm first-page page-link items set as Display Type: Page Link; dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite.**

---
*Source: IKEA OneGuide (Google Doc `1p2g6USLb7wopGIMZ8kkp-09dL7gwWf2bELSWF85OJOs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
