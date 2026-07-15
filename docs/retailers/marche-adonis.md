# Marché Adonis — Processing Guide

> **Source:** Marché Adonis OneGuide (Google Doc `1bk7AhFtCwxrwa7nrlOHQjpuHTwIsB9knwy2XGyjGOTU`), updated Jun 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#ops-metro`, `#flex-processingsupport` |
| Flyer type | Weekly |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support) |

## Files & schedule

- **Files received:** Wednesday (via SFTP, no later than the Wednesday prior to launch).
- **Cadence:** Available Tuesday, Valid Thursday, Available/Valid To Wednesday. Preview date Tuesday.
- **Ops notification:** when files land, check the Processing Support board; if not slotted, post in `#flex-processingsupport` requesting upload. 1–2 days after processing, add flyer runs to the VAST tracker for FQC.

## Upload & setup (owned by Vendor)

- **Weekly flyer:** manual upload of files ending `_p000#.pdf` for the correct date; upload both QC and ON pages. Set **QC pages to FR**, **ON pages to EN**. Auto-Group → Save and Complete.
- **Pricing zones — create 4** with languages:
  - **ON = EN**, **ON CL = FR** (cross-language from EN), **QC = FR**, **QC CL = EN** (cross-language from FR).
- **Stores:** ON = ON store set; ON CL = ON CL store set (Ottawa store only); QC + QC CL = QC store set.
- **Staggered dates:** open the **ON and ON CL versions ONLY** and set **Available From** to the Wednesday before the Valid From date. Make this change to the Available From date only, and only on ON / ON CL zones.
- (Inactive) London flyer: files begin `london flyer`; 1 EN pricing zone; add **only store 564 (London)**.

### ⚠️ Common errors (retailer-specific)

- **Page order** — verify page sequence before completing setup QC and FQC; ensure no pages are repeated. Incorrect page ordering is a documented failure mode.
- Watch for **multiple products** requiring separate boxes.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** No linking doc. Include retailer logo, sign-up page, social media, special weblinks; **exclude** coupons, packaged deals.
  - Box item blocks as one; items with two different descriptions drawn as separate boxes.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON).** Include brand, name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude valid dates.**
  - **Original price:** single price → Original Price field; a **range** → put in the Description field.

## Post-processing / FQC (FLEX)

- **Ad-hoc (FLEX):** Fruits + Veg (Last Minute Deals) insert pages arrive Tues/Wed for a Thursday launch — upload (QC page FR, ON page EN), set a trigger to insert pages into their zones for Thursday 12 AM, file a JIRA ticket for a trigger check and bump the DOC.
- **FQC checklist:** ops spotchecks; thumbnails 1065×600 (storefront carousel premium + organic); edit details (Available Tue, Valid Thu, Available/Valid To Wed, available everywhere, no theme); all priced items and visible sale stories boxed; interactivity via vertical preview; page order matches the tracking sheet in the SFTP; sessions green + MISO; geography unchanged; staggered-date check on ON / ON CL only.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps per the baseline page-swap process.

---
*Source: Marché Adonis OneGuide (Google Doc `1bk7AhFtCwxrwa7nrlOHQjpuHTwIsB9knwy2XGyjGOTU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
