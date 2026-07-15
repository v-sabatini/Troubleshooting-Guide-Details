# Price Chopper KC — Processing Guide

> **Source:** Price Chopper KC OneGuide (Google Doc `1AK2yfM6Vba_zjNRBImCJ_Kf7da4pUY6DgQIC8lGy9m4`). Contacts/credentials omitted.

A US grocery account with a distinct **St. Joseph (StJ)** pricing zone alongside the main (MO) zone.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Standard |
| Availability | All platforms |
| Slack channel(s) | `#pricechopper-kc`, `#flex-processingsupport` |
| Hosted URL | (not specified) |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex (Processing Support); OS involved in Setup; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Wed, Valid From Wed; Available To Tue, Valid To Tue.
- **Linking document:** N/A per account info, but Box/Tag QC reference a Box-specific and Tag-specific linking doc.
- **Workflow owners:** Upload/Setup = Vendor; FQC = DOC/Flex.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → the folder is labelled with the publication start date (all MO pages + the StJ PZ). **You cannot auto-group — manually number the pages** to match the page name/number. Save + Complete.
- Download the **Publication Schedule** from the FTP to help build pricing zones.
- **Create 2 pricing zones:**
  - **Base** → all MO pages.
  - **StJ** → some MO pages + all StJ pages (e.g. pages 1, 2, 4, 8 = StJ, the rest = MO).
- **Stores:** Base PZ = all base stores; StJ PZ = all St. Joseph stores. Check Geo → "No Stores or FSAs/zips were added or removed!"
- **Setup QC:** confirm all pages uploaded from SFTP; **no external run name, hidden on Flipp Hosted only, no theme**; check dates against the bottom of the flyer; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)
- **St. Joseph unique pages:** the retailer sends unique pages for the St. Joseph price zone — ensure the unique page is added **only** to the StJ pricing zone, **not** in the other (Base) zone.
- Pages cannot be auto-grouped — number them manually to match the page name/number.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- Linking document required (Box Draw/Box QC specific).
- **Include:** packaged deals, retailer logo, special weblinks. **Exclude:** coupons, sign-up page, social media.
- Draw clean boxes around every item with prices; do not box sign-up promos.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude:** SKU, disclaimer, URLs.

### Image QC
- Standard (PDF preferred where reflective of the page).

## Final QC (owned by Flex)
1. Spotchecks; mark Autostack Spotcheck complete.
2. Standard 4 thumbnails.
3. **Edit Details:** no theme, no external run name, **hidden in Hosted**, dates correct, no preview.
4. Item Image QC (checking for PDFs); page categories.
5. **Double-check StJ pages** — order and correct page numbers.
6. **Geography:** if the Geo tab is green with "No Stores or FSAs/zips were added or removed!" the warning is safe to ignore; if that message is absent, email the full-time team.
7. Verify links (if any); no errors on front page.
- Flyer Review type: **Lite.**

## Out-of-processing
- See the Price Chopper KC 2025 Black Friday operations guidelines (linked in the OneGuide) for publication & ad-hoc requests.

---
*Source: Price Chopper KC OneGuide (Google Doc `1AK2yfM6Vba_zjNRBImCJ_Kf7da4pUY6DgQIC8lGy9m4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
