# Piggly Wiggly Carolina — Processing Guide

> **Source:** Piggly Wiggly Carolina OneGuide (Google Doc `1uGGMKqF9BYcbA9UnmGQVWv1hJGq6phD8MwbWZBZAGRM`). Contacts/credentials omitted.

A Vendor Solutions grocery account with a codesheet built from an `.ods` versions file.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | (not specified) |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Publication cadence:** Available From Mon, Available To Mon; Valid From Tue, Valid To Tue.
- **Linking document:** N/A.
- **Workflow owners:** Upload/Setup = Vendor; Image QC = Flex; FQC = DOC.

## Upload & setup (config `generic`)

1. In the Piggly Wiggly Carolina FTP, find the `.ods` file whose name matches the run live date (e.g. `VERSIONS.6.11.25.ods` for the June 11 publication).
2. Import the `.ods` into a new spreadsheet. Delete any rows/columns with no pages.
3. **Codesheet manipulation:**
   - Ensure every page ends with `.pdf` so the codesheet uploads properly.
   - **Delete duplicate rows** — e.g. if there are 5 rows of Kinston stores, note the deleted stores and delete 4 of them **for now.**
4. Save as CSV and upload: Name = anything, **Config = `generic`**, PDF base directory = basepath from the `.ods`, **2nd and last box unchecked.**
5. Once processed, mark off flyer creation and **add back the deleted rows** from step 3.
6. Set the flyer run as **hidden in hosted.** Complete Setup QC.

### ⚠️ Common errors / risk items (retailer-specific)
- **"Reused PDFs in multiple zones" backtrace error:** caused by NOT deleting the duplicated pricing-zone rows during step 3. Delete duplicates before processing, then add them back after.
- **Look for multiple products** in a block.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box OFF, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block individually. If a block has multiple prices for an item, box individually and use text boxes as required.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** pre/postfix, valid dates, price, categories, disclaimer, original price. **Exclude:** brand, name, description, SKU, sale story, URLs.
- **Description:** enter as it appears in the flyer (unless it would violate the "Name" rules). When there are multiple brands, do **NOT** enter in the Brand field — put into the Name field.

### Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted.

## Final QC (owned by DOC)
- Confirm dates (per PDF) and availability toggles; thumbnails include retailer logo.
- All items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions complete.
- **Geography changes week over week — this can be ignored.**
- Flyer Review type: **Lite.**

---
*Source: Piggly Wiggly Carolina OneGuide (Google Doc `1uGGMKqF9BYcbA9UnmGQVWv1hJGq6phD8MwbWZBZAGRM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
