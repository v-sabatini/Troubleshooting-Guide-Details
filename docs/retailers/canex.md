# CANEX — Processing Guide

> **Source:** CANEX OneGuide (Google Doc `1WDzRKPmufJBbZBi_S-Ryl9WKI-w8hM5nXKNu8x3WElA`), updated May 16, 2024. Contacts/credentials omitted.

> **Bilingual (EN/FR)** military-community retailer (CFMWS).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#canex` |
| Hosted URL | canex.ca/en/ |
| Flyer types | Bi-Weekly (3491) · Monthly |
| Processing | Auto-stack; Flex (Setup, FQC, Flyer Review); OS (Setup); no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Monday (files sent 1–2 times a month; contact emails when dropped). A "locations file" is also dropped — **ignore it.**
- **Cadence:** Available From Friday · Valid From Friday · Available To Monday · Valid To Tuesday.
- **Preview date:** 2 business days before live (Monday midnight).
- **Linking document:** yes (Excel, provided per flyer). **Split into EN and FR files** (delete FR links → save EN → attach to English vendor tasks; delete EN links → save FR → attach to French vendor tasks). Sometimes you must upload files to the SFTP yourself (page swaps or email attachments).

## Upload & setup (owned by Flex)

- Pages > Edit > Upload FTP → Auto-group → **manually change French pages' language to French.** Zones: EN and FR; add all stores to each.
- **Pre-Setup QC:** Vendor tab — autobox draw; mass-upload the linking doc for both languages. Overview > Details: available everywhere; **preview date 2 business days before live (Monday midnight).** LH 45/35; thumbnails Standard 4.
- **Setup QC:** **ignore the "no french stacks" warning;** mark autostack spotcheck complete.

## ⚠️ Common errors / risk items
- **Links (top risk):** ensure tagged links match the linking document. **After the preview link is sent, the retailer ALWAYS returns revised links (usually <10, highlighted) — update accordingly.**
- **French item type:** OS commonly tags French items as a **Link** when they should be **Item** — if there's a callout (e.g. "Save 20%"), item type must be **ITEM**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- Linking document required (box-specific). **Include:** coupons, packaged deals, special weblinks. **Exclude:** retailer logo, sign-up page, social media.
- Box items with prices/discounts; box deals as a whole box; box pages with URLs.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking document required (tag-specific). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Brand = larger text; Name = smaller text under it. SKUs are a mix of letters and numbers. If item valid dates differ from flyer dates, add them on the item. **URLs from the attached Excel spreadsheet.**

### Image QC
- Prefer PDFs unless unclear/black background.

## FQC (owned by Vendor)
- Geography: nothing added. PZ tab: everything boxed/tagged; horizontal/vertical scroll check.
- **Page Category QC:** choose 1–2 categories; nothing on the first page. **"Points promo pages" get a blank category.**
- Overview Details: available everywhere; typically no theme; internal run name prepopulated; no external name; preview date 2 business days before live. LH 45/35; thumbnails Standard 4; Image QC prefer PDFs.
- **Items Without URL:** try the linking doc; if no link exists, note it in comments (retailer will likely send it after previewing).
- **UTM code (Manage Tracking Codes):** from the linking doc — usually `UTM-d#` (flyers start with D#, matching the UTM). Update all 3 "Campaign" fields with the text after "UTM".

## Out-of-processing / preview
- Ensure preview date = Monday 12:00 AM; Monday morning send EN + FR preview links. Retailer has **one business day** to send corrections (always URL corrections, usually <10).
- **Flyer Review type: Lite.**

---
*Source: CANEX OneGuide (Google Doc `1WDzRKPmufJBbZBi_S-Ryl9WKI-w8hM5nXKNu8x3WElA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
