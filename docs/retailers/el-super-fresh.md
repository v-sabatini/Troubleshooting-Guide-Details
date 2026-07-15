# El Super Fresh — Processing Guide

> **Source:** El Super Fresh OneGuide (Google Doc `13e8_z1SNplq7z132Qnyhs9UZIwNH_GL5zdNvHPcMuDc`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#elsuper` |
| Flyer types | Weekly (single flyer type) |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS (Setup); no coupons; no Feedel/retailer data services |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To / Valid To Tuesday.
- Workflow: Upload & Setup (Flex) → Image QC → FQC (Flex).

## Upload & setup (owned by Vendor)

- Pull the codesheet (xlsx) from the SFTP. **Confirm you pull the correct file — El Super vs. El Super Fresh** (they are distinct).
- Open the codesheet and **delete any extra titled columns (Page 5, Page 6, etc.) that have no page data beneath them.** Save as CSV.
- Upload to the Codesheet tab: **Config name `generic`**; PDF base directory pulled from the SFTP.
- **All toggles ON except Region Assignment and Combine Zones.** Run codesheet.
- After it runs, check the pricing-zones page for correct zones/stores/pages. Mark "Flyer Creation" complete. Check Geo shows **"No Stores or FSAs/zips were added or removed!"**

### Setup QC
- Check SFTP that all pages uploaded.
- Edit Details: **no external run name; hide on "Flipp Hosted" only; no theme;** check run dates against the dates at the bottom of the flyer.
- Thumbnails: **Standard 4** (1065×600 first two pages; stock premium first page; storefront carousel premium first two pages; storefront carousel organic first page).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Include** retailer logo. **Exclude** coupons, packaged deals, sign-up page, social media, special weblinks.
- Box each item block. For buy-this-get-that deals, box each item individually.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection OFF)
- **Include** name, pre/postfix, valid dates, description, price, sale story, categories, original price. Brand is box-draw specific. **Exclude** SKU, disclaimer, URLs.
- **⚠️ Item-level valid dates:** items boxed within a dated promo area must carry that promo's item Valid From/To. Example: an item under "2 Días Ofertas De Fin de Semana" dated Nov 23–24 must be tagged Valid From/To Nov 23–24.

### Image QC
- N/A.

### Spotchecks
- Ensure every item has a **Google category and an Analytical category**.

## FQC (owned by Flex)
- Spotchecks if required; QC thumbnails Standard 4 (stock premium, storefront carousel premium/organic).
- Edit Details: available everywhere, no external run name, run dates match the PDF.
- Flag missing pages or geography changes to the full-time team.
- **Flyer Review type: Lite.**

## Out-of-processing
- See the El Super / El Super Fresh 2025 Publication & Ad-Hoc Requests guidelines (in the OneGuide) for BF comms and ad-hoc requests.

---
*Source: El Super Fresh OneGuide (Google Doc `13e8_z1SNplq7z132Qnyhs9UZIwNH_GL5zdNvHPcMuDc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
