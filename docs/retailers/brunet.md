# Brunet — Processing Guide

> **Source:** Brunet OneGuide (Google Doc `1MGjjBVblcCzRDDlh8d_wBjlKr4HpOEtt6Z7crifTr-U`), updated Jun 08. Contacts/credentials omitted. (Metro-family account; includes Brunet Clinique.)

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (bilingual — FR base, EN cross-language) |
| Availability | All platforms |
| Slack channels | `#metro`, `#opsmetro`, `#flex-processingsupport`, `#vendor-assigned-tasks-retailers` |
| Flyer types & cadence | Weekly Flyer (type ID 3478); Clinique flyer (separate flyer type) |
| Processing | Auto-stack; Flex (Flyer Review); OS (FQC); no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** Tuesday (base PDFs sent via SFTP at least 10 days in advance).
- **Publication:** Available From Tuesday; Valid From Thursday; Available/Valid To Wednesday.
- **Preview / linking doc:** N/A (Tag/QC-specific linking doc is required though — see below).
- Coordinator ensures **VAST is updated** ~3 days out.

## Upload & setup (owned by Vendor)

- **Weekly:** Manual upload → select all PDFs sharing the same launch date in the folder name (e.g. `78396_BRU_WEB_01_E10.p1.pdf`); upload all pages that **do not** include CLINIQUE or GUIDE in the name.
- **Clinique (separate flyer type):** Manual upload → select PDFs matching the launch date (e.g. `78811_BCL_01_E10.p1.pdf`); upload all pages that **do not** include BRU in the name. Set all files to FR; ensure chronological order; Save & Complete.
- **Pricing zones (create 2 manually with languages):** **`Base` = FR** and **`Base CL` = EN**. Brunet: add all stores from the Brunet store set to both zones. Clinique: add all stores from the Brunet Clinique store set to both zones.
- Check Geography tab (no store/FSA changes week over week without a note). Check SFTP for leftover/unused pages — if not in the Tracking Sheet, flag Full-Time Ops.

### ⚠️ Common errors / risk items (retailer-specific)

- **File filtering by name is the key upload risk:** Weekly excludes CLINIQUE/GUIDE files; Clinique excludes BRU files. Uploading the wrong set mixes flyers.
- Two pricing zones with correct languages (`Base`=FR, `Base CL`=EN) — mismatched language is a common error.
- Leftover/unused SFTP pages not in the Tracking Sheet must be flagged.
- Holiday books: fixed-price multi-course-meal offers boxed as one; don't box individual items unless they have a clear price/offer/sale story.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot ON. No linking doc.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. One product + one price = box each product; one brand + multiple products named together = one box; multiple products with individual naming = box each. Box links/CTAs.
- **Tag / Tag QC — Low. Auto-tag ON. Linking doc required (Tag/QC-specific). PDF image auto-selection ON. Pre/Postfix excluded.** Include name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Tag fields as seen on the flyer.

## FQC / go-live (owned by Vendor)

- **Inserts:** every Wednesday Brunet emails inserts (files + pagination sheet) for the flyer going live the following Tuesday. Upload insert files to the run, mark Flyer Creation complete, order pages per the pagination in both EN and FR zones, add inserts to zones in the given order, and **box/tag all links called out in the pagination sheet.**
- Confirm page order/regionalization; Ops spotchecks; thumbnails (1065x600, storefront carousel premium & organic); Edit Details (Available Tuesday, Valid Thursday, Available/Valid To Wednesday, Internal Run Name `MM DD`, available everywhere, No Theme); verify all priced items and visible sale stories boxed; page order matches the Pagination Document (`Ordre des pages web_RR`); sessions green, mark In-Store Only; geography unchanged.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swap: standard baseline process.
- ~5 days before launch a WeTransfer link + Pagination document arrive; download inserts, add them, and adjust page order to match the pagination doc.

---
*Source: Brunet OneGuide (Google Doc `1MGjjBVblcCzRDDlh8d_wBjlKr4HpOEtt6Z7crifTr-U`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
