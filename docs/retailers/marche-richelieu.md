# Marché Richelieu — Processing Guide

> **Source:** Marché Richelieu OneGuide (Google Doc `1PyiXvcJ2C502Y-BE6di9XJ44BnSzs_kU8bMcX4xJMB4`), updated Feb 22. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#opsmetro`, `#flex-processingsupport`, `#vendor-assigned-tasks-retailers` |
| Flyer type | Weekly Ad (merchant #3372) |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex flyer review, OS FQC |

## Files & schedule

- **Files received:** Monday (PDFs via SFTP, no later than the Wednesday prior to launch).
- **Cadence:** Available Tuesday, Valid Thursday, Available/Valid To Wednesday. No preview date; no linking document.
- Coordinator ensures VAST is updated ~3 days out.

## Upload & setup (owned by Vendor)

- Open the **Tracking Sheet** (usually a PDF) to identify page order. Manually upload all pages.
- **Do NOT use files in directories whose base path ends in `BLOCK_ID`** — use the equivalent files without the `BLOCK_ID` suffix.
- Set all pages to **FR**; Auto-Group → Save and Complete.
- **Pricing zones — create 2:** **Base = FR**, **Base CL = EN.** Add all stores to both.
- Check geography (no WoW changes without note); check the SFTP for leftover/unused pages.

### ⚠️ Common errors (retailer-specific)

- **Missing pages** — if any page listed in the Tracking Sheet is missing from the FTP, flag the FT team immediately.
- **Leftover / unused SFTP pages** not listed in the Tracking Sheet → flag the Full Time Ops team.
- **`BLOCK_ID` directory files** must not be used.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** Linking doc (Box Draw/Box QC specific). **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - Multiple items boxed together when one price covers all (e.g. 2 for $3 cantaloupes, or iceberg lettuce); ensure the web link is boxed.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Original price:** single price → Original Price field; a **range** → Description field.

## FQC / flyer review (Vendor)

- Ops spotchecks; thumbnails 1065×600 (storefront carousel premium + organic); edit details (Available Tue, Valid Thu, Available/Valid To Wed, internal run name MM DD, available everywhere, no theme); all priced items and visible sale stories boxed; interactivity via vertical preview; page order matches the tracking sheet in the SFTP; sessions green + MISO; geography unchanged.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps per the baseline page-swap process.

---
*Source: Marché Richelieu OneGuide (Google Doc `1PyiXvcJ2C502Y-BE6di9XJ44BnSzs_kU8bMcX4xJMB4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
