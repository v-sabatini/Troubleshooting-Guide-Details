# El Super — Processing Guide

> **Source:** El Super OneGuide (Google Doc `19Yb4MZrCF7GM7-yByg7tJPIouKLn_1BR_j_ZUxJRcW4`), updated Jun 1, 2026. Contacts/credentials omitted. (Chedraui USA banner; note the related **El Super Fresh** codesheet.)

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#elsuper` |
| Flyer type(s) & cadence | **Weekly** |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup); no coupons processing; no Feedel/retailer data services |

## Files & schedule

- **When files arrive:** Thursday. Available From Wednesday · Valid From Wednesday · Available To Tuesday · Valid To Tuesday.

## Upload & setup (owned by Vendor)

1. Pull the codesheet (.xlsx) from the SFTP — **confirm El Super vs. El Super Fresh** (correct file).
2. Open the codesheet → **Output tab**:
   - If already populated: delete any extra columns that have a title (e.g. Page 5, Page 6) but no page data beneath them.
   - If not populated: fill `=Input!B4` in Column C row 2 and keep applying the formula down; verify each page name matches its zone (e.g. Zone ABQ should have "ABQ" in the page name); then delete empty titled columns.
   - Save as **.csv**.
3. Codesheet upload tab: **Config name = `generic`**; PDF Base directory pulled from the SFTP.
4. **All toggles ON except Region Assignment & Combine Zones.** Run codesheet.
5. Confirm zones/stores/pages uploaded correctly; mark **Flyer Creation Complete**; check Geo reads "No Stores or FSAs/zips were added or removed".

**Setup QC:** confirm all SFTP pages uploaded; Edit Details — no external run name, available everywhere, no theme, check dates against the bottom of the flyer; thumbnails **Standard 4** (1065x600 first two pages; stock premium first page; storefront carousel premium first two pages; storefront carousel organic first page).

### ⚠️ Common errors / risk items (retailer-specific)

- **Date checking — ABQ and ELP pricing zones run for TWO weeks** while other zones run one week. **Do NOT check valid/available dates against ABQ or ELP** (they'll look wrong) — check dates against any other pricing zone.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** No linking doc. Box each product block individually. Multiple items with one price → one box; multiple items with different prices → box separately and use text boxes to link info to image. **Box coupons** (recognizable by a barcode). **Include** retailer logo. **Exclude** packaged deals, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection OFF).** No linking doc. Include name, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude SKU, disclaimer, URLs.** Brand handled via Box Draw/Box QC.
- **Image QC:** N/A.
- **Spotchecks:** ensure a **Google and Analytical category** is added to all items.

## Final QC / go-live (owned by FLEX)

- Spotchecks (if required); QC thumbnails Standard 4; Edit Details — available everywhere, no external run name, run dates match the PDF.
- **If pages are missing or geography changes, flag to the full-time team.** Complete FQC checklist.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: El Super OneGuide (Google Doc `19Yb4MZrCF7GM7-yByg7tJPIouKLn_1BR_j_ZUxJRcW4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
