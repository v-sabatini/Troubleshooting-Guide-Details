# AG Foods — Processing Guide

> **Source:** AG Foods OneGuide (Google Doc `1KFjKk_4dnLxTdObYRc0MlV9smCu5xj2wH1S4Ln7n0Ug`), updated May 9, 2024.
> Covers AG Foods and Safety Foods (two separate publications). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | (per OneGuide) |
| Hosted URL | agfoods.com |
| Flyer types | Weekly (AG Foods + Safety Foods are two separate pubs) |
| Processing | Auto-stack; **Flex = Flyer Review**; **OS = Setup**; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday (dropped to FTP weekly, usually Friday afternoon per the upload steps).
- **Cadence:** Available From Monday, Valid From Sunday (AG Foods zones are staggered — see below).
- **Linking document:** Yes (Box Draw/Box QC specific).

## Upload & setup

- **Safety Foods = manual upload; AG Foods = codesheet upload** (note: at time of writing, AG Foods codesheet upload was temporarily not working → upload manually per the Breakdown file).
- **Safety Foods manual:** Pages → Edit → Expand Root → Expand Week ## → Select Files. Group pages by the trailing number. One "base" pricing zone: order all pages by number, add all stores.
- **AG Foods:** different **page 1s per pricing zone** (usually 3 — Base, BaseFri, BaseMon) and one set of every other page. Use the **Breakdown** spreadsheet (on the FTP, labelled "Breakdown") which defines pricing zones, stores and valid dates. Create zones per the spreadsheet.
- **Codesheet (AG Foods):** insert the page names from the Breakdown "Files name" column into the codesheet template (into the corresponding pricing zones); adjust Start/End dates to match the Breakdown per zone.

### ⚠️ Common errors / risk items (retailer-specific)

- **Every page in the codesheet must end in `.pdf`** or the codesheet will not detect the pages on the FTP.
- Do **not** remove the leading `'` mark on dates in the codesheet — it can corrupt the codesheet.
- **AG Foods staggered dates:** each zone has its own unique dates; the **run must encompass all dates** — start on the EARLIEST date shown, end on the LATEST (e.g. Base Sun–Sat, BaseMon Mon–Sun, BaseFri Fri–Thu → run Friday through Sunday). If you lack the publication schedule, follow the dates on the page 1s.
- **Safety Foods:** double-check dates against page 1.
- Look for multiple products (box each separately).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks. Each item gets its own box (price + name inside). Text-only items (no image) are boxed separately.
- **Tag / Tag QC (Low; Auto-tag OFF):** linking doc required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific.
- **Image QC:** per examples (details not filled in the OneGuide).

## FQC / go-live (owned by DOC)

- **Triple-check valid & available dates** against the publication schedule; double-check store assignment; use the theme from the ad for the sales story; **legibility heights 45/35**.
- AG Foods dates run from earliest staggered date to latest; Safety Foods dates match page 1. Toggles: Flipp / Distribution / Hosted all Available. All tagging + flyer-level tasks complete.
- **Flyer Review type: Lite** (owned by Flex).
- **Out of processing:** page-swap procedures (see OneGuide video).

---
*Source: AG Foods OneGuide (Google Doc `1KFjKk_4dnLxTdObYRc0MlV9smCu5xj2wH1S4Ln7n0Ug`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
