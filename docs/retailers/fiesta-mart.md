# Fiesta Mart — Processing Guide

> **Source:** Fiesta Mart OneGuide (Google Doc `11qOU3wVtcDWnwpcPV0iHG5YOoG1nrAWZlGJbJ0rwU3A`), updated Feb 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#Fiestamart` |
| Hosted URL | fiestamart.com/weekly-ads |
| Flyer types | Weekly Ad |
| Processing | Auto-stack; Flex (Flyer Review); no coupons, no Feedel |
| Account guide | Confluence: Fiesta Mart Account Guide |

## Files & schedule

- **When files arrive:** Tuesday.
- **Publication cadence:** Available/Valid From Wednesday; Available/Valid To Tuesday.
- **Linking document:** No.
- **Processing type:** Auto-stack.

## Upload & setup (owned by Vendor) — codesheet

- Download the Version List (codesheet) from the Fadmin FTP.
- Manipulate the Version List:
  - The Ad Date is written like "3.31.21" — reformat month/day/year with slashes: "3/31/21".
  - Do the same for the "Effective Dates" row (e.g. "3/31/21-04/06/21").
  - Delete the empty page columns and rows.
  - Save as CSV.
- **Upload:** Fadmin → Codesheets tab. Name: Codesheet. Select the CSV. **Config Name: `fiesta_mart`.** Enter the PDF Base Path (from the Fadmin FTP).
- **Toggles:** select **all toggles EXCEPT Region Assignment.**
- Click Save Codesheet → Process Code Sheet.
- Once complete, mark "Flyer Creation" as complete.

### ⚠️ Common errors (retailer-specific)

- **Codesheet date error — `[Codesheet Error] Invalid Value for Integer (): 0#`.** Caused by the retailer-provided dates on the codesheet. Fix by adjusting the "ad date" and "effective date" one day ahead or behind, depending on the number in the error, and temporarily adjust the flyer run dates to match.
  - Example: error `[Codesheet Error] Invalid Value for Integer (): 09` → change ad date and effective date to 8, and change the flyer run from Apr 9–Apr 15 to Apr 8–Apr 15 temporarily.
  - After changing dates, reupload the codesheet. **Once it runs successfully, restore the flyer run dates to the original values.**

### Setup QC checklist (owned by Vendor)
- Thumbnails: Standard four.
- Available & Valid: Wednesday–Tuesday.
- Available everywhere.
- Mark Setup QC complete.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box draw every product block.
- If a product block has multiple items but **one price, box as one item**.
- Box **Buy One Get One Free** items as one box.
- If there are **multiple prices in a product block, box them separately**.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- Brand is Box Draw/Box QC specific. Standard tagging rules apply.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs.
- **Exclude:** SKU.
- **PDF image extraction is NOT enabled for this merchant — leave the cutout image selected for all items.**
- **Page categories:** every page except page 1s must have page categories, **minimum 1 and maximum 3 per page.**

## Post-processing / FQC (owned by Flex)

- Confirm dates against the PDF; available on all platforms.
- Thumbnails drawn (4 standard) and include the retailer logo.
- All items boxed and tagged; previews published and clickable; sessions completed accurately; geography consistent.

## Flyer Review (owned by Flex)
- **Flyer Review type: Lite** (full processing).

## Out-of-processing
- **Page Swap:** baseline page-swap process (Jan 2024).

---
*Source: Fiesta Mart OneGuide (Google Doc `11qOU3wVtcDWnwpcPV0iHG5YOoG1nrAWZlGJbJ0rwU3A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
