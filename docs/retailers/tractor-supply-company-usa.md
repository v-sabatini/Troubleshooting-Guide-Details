# Tractor Supply Company USA — Processing Guide

> **Source:** Tractor Supply Company USA OneGuide (Google Doc `18KANpGZw-HJaH1AIcj8nMvlGvx3MCVRNTou8QYtqBls`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#tsc_usa` |
| Hosted URL | https://www.tractorsupply.com/CurrentAdView |
| Flyer type(s) & cadence | Current Ad (#3791) — **holiday flyers only** |
| Processing | Auto-stack; Flex (FAB tickets + Setup) → Image QC (Flex) → FQC (DOC); Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** holiday only. The retailer contact emails avail/valid dates and (usually later) an updated store list + linking document.
- **Publication cadence:** Available From Sunday · Valid From Tuesday · Available To Monday · Valid To Tuesday.

## Upload & setup (Flex)

1. Contact emails avail/valid dates, then sends an updated **store list** (includes the pricing zone for each store) and **linking document**. You'll likely need to add newly-opened stores to Fadmin — ask the contact.
2. Build a **generic codesheet** listing pricing zones, stores, and page names. This is a long manual process: filter the store list by pricing zone, copy/paste stores into the generic codesheet, and copy/paste the PDF page names for each pricing zone.
3. Upload — **Config name `generic`**, **toggles: all except "combine zones" and "region assignment"**.
4. While sessions run: apply the holiday theme (depends on which holiday flyer), external run name = the flyer name, avail/valid dates usually the same unless the client specifies. **4 standard thumbnails.**

### Setup QC checklist (Flex)

- Overview: no warnings **except unassigned stores (normal)**.
- Pricing Zones: all should have the same page count unless specified; each PZ has ≥1 store assigned.
- Sessions: all green. Vendors: linking doc attached to all tasks.
- Geography: usually too much time between flyers to compare; stores likely added by retailer.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking document required. **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box all product information together; handle multiple SKUs.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF auto-select ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories, disclaimer, URLs.
  - Name/brand as in flyer (bold text); description under the bold name/brand.
  - **SKU:** enter in both the SKU field and the Description field when provided.
  - Valid dates: only tag if different from the flyer.
  - **URLs:** add from the spreadsheet; if missing, search tractorsupply.com by SKU + item name.
  - Sale story = e.g. "SAVE $200"; disclaimer = italicized text.
- **Item Category QC (DOC):** categories tagged by OS, no QC needed; usually one clear category per item.
- **Item Image QC (DOC):** clean PDF where possible, cutout when not; no dark shadows around the image.
- **URL/Links QC (DOC):** ensure all items have a URL; if not in the retailer spreadsheet it's OK to leave blank.

## Out-of-processing

- Expect **multiple revisions** to links/pages.

## Flyer review

- **Flyer Review type: Lite** — standard review, no special risk items.

---
*Source: Tractor Supply Company USA OneGuide (Google Doc `18KANpGZw-HJaH1AIcj8nMvlGvx3MCVRNTou8QYtqBls`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
