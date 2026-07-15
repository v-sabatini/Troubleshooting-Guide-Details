# Patrick Morin — Processing Guide

> **Source:** Patrick Morin OneGuide (Google Doc `1AcJEEw_awSeGF5Wu84XVqeArhU8raI6RtstrJu3lRUI`), updated May 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `patrick-morin3` (private channel) |
| Hosted URL | patrickmorin.com |
| Flyer types & cadence | Flyer Type 1: Weekly · Flyer Type 2: Monthly |
| Processing | Auto-stack; Flex does Flyer Review; **linking document required**; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Tuesday. Preview the day before, on Wednesdays (since April 2024).
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Thursday, Valid To Wednesday.
- **Bilingual account** — EN and FR pages/pricing zones.
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## ⚠️ Risk item — catalogs without pricing
**Catalogs without pricing on the flyer are acceptable as long as the link sheet contains the item pricing.** Advise OS to add the pricing from the link sheet into the tags. Add to all comments under OS tasks: *"PLEASE READ: please add the pricing (prix REG) that's in the linking doc, in the tag in the 'current price' section for all the products. Pricing must be included for all products."*

## Upload & setup (owned by Vendor)

- **Receive files:** retailer sends the PDF via WeTransfer email — download and drop into the Patrick Morin FTP (e.g. `PM CIRC 32`). The link sheet comes in a separate email. Files sync to FADMIN after ~an hour.
- **Upload (once link sheet + PDFs received):** manual upload — **upload the same pages TWICE for EN/FR.** Auto-Group. Toggle first set English, second set French.
- **2 pricing zones: EN & FR — add all stores to both.**
- **Mass attach the link sheet to all vendor tasks** (no manipulation needed). The link sheet is **not in the FTP** — it's in the OS Setup Files drive. Match the tagging document name to the week (e.g. "Circulaire 39.xls" belongs to flyer 39).

### Setup QC (owned by Vendor)
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **Risk:** if uploading from SFTP, confirm no pages were left un-uploaded.
- Confirm flyer dates (first or last page). Thumbnails (4 Standard). Ensure all preview dates are set. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF):**
- **Include:** retailer logo, sign-up page, social media, special weblinks.
- **Exclude:** coupons, packaged deals.
- Box each item with a price.

**Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON; linking doc required):**
- Include everything: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Tag/QC specific.

**Image QC:** choose clean images with white backgrounds (e.g. Sifto Pool Salt, SICO Premium Paint).

## Post-processing (owned by DOC)

- **URL/Links QC:** Overview → information/reports → items without a URL; cross-reference the link sheet and input missing links, keeping language correct (ENG item → ENG link).
- **FQC:** Standard 4 thumbnails; legibility heights 45/35; item image QC (clean PDF preferred, lifestyle images acceptable); check sessions and re-verify URLs; categories on all pages except the first.
- **External Run Name (French):** "Circulaire de la semaine" (or the catalog name if it's a catalog). Available Wednesdays, Valid Thursdays.
- **Tracking codes (must match):**
  - *Weekly Flyer portion:* Dynamic Variable, Source All, `utm_source` = `flipp`; and `utm_medium` = `flyer`.
  - *Flyer run portion:* Dynamic Variable, Source All, `utm_campaign` = `semaine_xx_2025` (xx = the week number being processed).
  - Click **"Apply All Tracking Codes."** Complete FQC checklist.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by Flex): flyer dates, sessions complete, previews correct, all items tagged accurately, geography correct, availability toggles correct.
- **Page swaps:** download the revised page from the email; manually add it **twice** (one EN, one FR); save & complete; complete all vendor tasks; copy the original page boxes to the revised page; update the tag for the required revision (both languages); swap the revised page into the respective pricing zone; re-run page tile generation + page stitching; advise the retailer (reflects within the hour).

---
*Source: Patrick Morin OneGuide (Google Doc `1AcJEEw_awSeGF5Wu84XVqeArhU8raI6RtstrJu3lRUI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
