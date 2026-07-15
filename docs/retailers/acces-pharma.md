# Accès Pharma — Processing Guide

> **Source:** Accès Pharma OneGuide (Google Doc `1HB7P2oB…4RzYY`). **Walmart-brand
> merchant.** Bilingual (EN/FR). 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | TBD (Walmart-brand merchant) |
| Availability | All platforms |
| Slack channels | `#acces_pharma-onboarding`, `#flex-processingsupport` |
| Hosted URL | n/a (hidden on hosted) |
| Flyer type / cadence | 10945 — **Monthly**; files received **Friday**; available **Thursday**, valid **Wednesday** |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Upload & setup (owned by Flex)
- **Client sends the PDF by email** (they've been asked to use SFTP but don't). Upload the PDF to the SFTP so FADMIN breaks it into pages — **or** split via pdf2go, then upload from your local drive.
- Pages → Edit → upload all pages **twice**; **set one of each page number to English and the other to French**; Autogroup; Save & Complete.
- **Flyer creation (bilingual):** one pricing zone "**ENG**" with all English pages (correct order); one pricing zone "**FR**" with all French pages (correct order).

## Setup QC
- Add **all stores to both zones**. Open the last page ("Tag") and check the printed dates match the client's email; if not, set the run dates to the PDF and **flag the discrepancy to the DOC**.
- Overview → Edit Details: **hide on hosted**, no external run name, "No Theme." Legibility heights **Scan 60 / Read 40**. Thumbnails: Standard 4.

## QC specifics
- **Box Draw:** Low; Auto-Box **on**, Box QC bot **off**; exclude coupons/packaged deals/logo/sign-up/social/weblinks. Box & tag each item individually; if items share a price but have different names/brands, box separately.
- **Tag / Tag QC:** Low; Auto-tag **off**. Include all fields **except URLs** (excluded).
- **Image QC:** clean PDF where possible; if the PDF image has a black background/defect, use the cutout.

## Final QC (owned by Flex)
- **Geography** green — **no stores or FSAs/zips added or removed.**
- **Sessions** all green **except PDF Image Auto Selection.**
- Pricing Zones: no items missed; all stores added to both zones; **one zone English, one French**; pages ordered correctly.
- Dates correct (check last page of flyer + client email); hide on hosted; no external run name; "No Theme."
- You can **ignore** the "Not all categories that are used in pricing zones have thumbnails" warning.
- **Flyer Review type: Lite.**

---
*Source: Accès Pharma OneGuide (Google Doc `1HB7P2oBL9UczVSClF0F1quqcHP35sMcoVaWiVh4RzYY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
