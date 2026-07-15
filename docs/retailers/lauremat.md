# Lauremat — Processing Guide

> **Source:** Lauremat OneGuide (Google Doc `1gWtvpqK4azfMpe4mvKpBXSCnH8PlkYBuQzXn79qlOXk`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Platforms / availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (plus retailer channel) |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); no OS beyond standard; no coupons; no Feedel |
| Linking document | n/a |

Simple French-language weekly account (setup + FQC owned by Flex).

## Files & schedule

- **Files arrive:** Friday (uploaded to SFTP).
- **Cadence:** Available/Valid From Thursday → To Thursday.

## Upload & setup (owned by Flex)

- **1 pricing zone, French,** containing all pages and assigned all stores.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** no linking doc. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** no linking doc, no brand. **Include** name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates.**

## Post-processing — Custom Action (assign FSAs)

- Create a spreadsheet with columns `flyer_id` and `fsa`, listing FSAs (e.g. G0G, G0H, G4R, G4S, G5B). In the left column, add the flyer's single Pricing Zone ID to those rows. Download as **.csv**.
- Run the custom action **"Assign FSAs from Csv"** with this csv and the Flyer Run ID.
- Confirm the geography tab reads "No Stores or FSAs/zips were added or removed!"

## Final QC / go-live notes (owned by Flex)

- Standard FQC checklist.
- **Flyer Review type: Lite** — no special risk items; use generic flyer review standards.

---
*Source: Lauremat OneGuide (Google Doc `1gWtvpqK4azfMpe4mvKpBXSCnH8PlkYBuQzXn79qlOXk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
