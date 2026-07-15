# Harris Teeter (+ Delivery) — Processing Guide

> **Source:** Harris Teeter (+ Delivery) OneGuide (Google Doc `1RX_HDfp-OOrjBNqrHawPWLkho0Hu_tVuQBbO_yiZUaI`), updated Dec 17, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` |
| Flyer types | **Weekly** · **Monthly** (and **Harris Teeter Delivery** as a separate banner) |
| Processing | Auto-stack; Flex (Flyer Review); FTE/Vendor-owned setup & FQC; Feedel/data services — **yes**; no coupons |
| Key resources | HT upload instructions, HT FQC + Risk Items notes, Kroger/HT Flex Team Tracker, HT FSA list |

## Files & schedule

- **When files arrive:** Thursday (usually in the FTP Wed afternoon, latest Friday). Files best processed over the weekend.
- **Publication cadence:** Available From Wednesday → To Wednesday; Valid From Tuesday → To Tuesday.
- **File naming:** file names include the last day the flyer runs (e.g. `fc02 harristeeter_delivery w.e. 09.19`). **`FC02` = Harris Teeter Delivery**; anything before FC02 refers to Harris Teeter only.
- The retailer email includes the page order for inserts/ads and any links — you don't need to wait for it to start uploading pages, but it drives insert placement.

## Upload & setup

### Weekly (Vendor-owned) — codesheet + manual inserts

- From the FTP, download the pagination codesheet (`WEEK mm.dd.yyyy BreakdownSTORE.xls`) and the store master (`HT Flip_Version_Store_Master.xlsx`) for the correct week.
- **Codesheet manipulation:** remove inserts fadmin can't read (BGA, BGB, Outerbank, PO1/PO2, FS1/FS2, e-fly/digital pages) — those get uploaded manually later; keep 1 blank row between pages; find `_[6_6]` and replace with blank; save as CSV; verify page-number order.
- **Store master:** open (auto-opens to most recent tab; confirm the tab date matches the FTP path); remove dashes between letter and number (E-10 → E10); download the tab as CSV.
- **Upload store master** using the base path only (codesheet turns green when processed). **Then upload the pagination codesheet** using the base path (an Outerbank-pages warning is normal — force process again; it stays yellow).
- Pricing zones: expect 6 pages for all PZs and 1 page for the OBX zone. **Manually upload the removed pages** (BGA, BGB, etc.).
- **Build inserts into the PZ** using the original pagination codesheet + the retailer's email order (screenshot lives in the Flex Kroger Tracker HT tab). **BGA is always position #2, BGB always position #3**; e-fly pages go at the very end in breakdown order; the program/ad page goes between the last numbered page (usually page 6) and the e-fly pages. Insert names in the email refer to the file-named pages ("Page 4"/"Page 5"), not stack positions. OBX zone has only 2 pages (page 1 + an OBX page).
- **Attach linking document:** download the week's HT Linking Document as `.xls` (name must match the flyer week) and **mass-attach to ALL vendor tasks/tracks**; manually upload the week's insert files.
- **Weekly Setup QC:** Standard 4 thumbnails; **no external run name**; no theme; dates Wed–Tues; sessions complete; linking doc + inserts added.

### Monthly (FTE-owned)

- Download from the retailer email, drop into FTP, manual upload; Flyer Creation → start; 1 PZ "Base"; add all stores; verify dates.
- **Monthly Setup QC:** Standard 4 thumbnails; **external run name: `Harris Teeter Discovery`**; no theme; dates Wed–Tues; sessions complete.

### Harris Teeter Delivery (custom actions)

- 4 pricing zones — **REG Virtual, REG Physical, NOVA Virtual (B&W pages), NOVA Physical (B&W pages)**. REG Virtual and NOVA Virtual share the same assigned store (correct).
- Assign stores via the `generic_stores` codesheet; assign **FSAs** to all four runs via the `Assign FSAs from CSV` custom action (paste each PZ ID into the template, export tabs as CSV, upload per banner).
- **FSA Swap:** if an "overlapping FSA" error appears, assign `20147` to Virtual Stores (remove-FSAs custom action) and remove `20147` from the Physical PZ.

## ⚠️ Common errors / risk items (retailer-specific)

- **Image risk item (all banners):** PDF images for **seafood and some meats are typically lifestyle or have a strange shadow** — change these to **cutouts**.
- **Banner boxing:** **do NOT box banners in Harris Teeter**; **DO box the HT Plus and HT Delivery banners in Harris Teeter Delivery.**
- **Name and Sale Story fields are CASE SENSITIVE** — match the flyer's capitalization exactly.
- Remove inserts before codesheet upload (fadmin can't read them); watch for differently named files vs the FTP.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot ON.** Linking document required. Box all items separately (text boxes when needed) — any item with a price or sale story gets a box. **Include** retailer logo, sign-up page, social media, special weblinks; **exclude** coupons.
- **Tag / Tag QC — Low complexity. Auto-tag OFF, PDF Image Auto-Selection ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand **not** required (meat/produce often have none) — enter if present.
- **Image QC:** prefer PDF image with white background; select cutout if the PDF has a black background or is lifestyle. **No lifestyle images; no black backgrounds.**

### Final QC highlights

- Weekly: mark autostack spotcheck complete; page categories on all pages except Page 1; verify HT links/tags; **merge BGA and BGB pages** (Overview → pricing zones → storefront spotcheck); banner tagging for HT Delivery + Weekly per the Kroger Flex Team Tracker tab; **sort the weekly flyer above the monthly**.
- Delivery/Monthly: confirm dates (PDF/email); cross-reference the HT tab to confirm banner links; thumbnails include retailer logo; standard checks; sort monthly **after** the weekly.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite** — flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: Harris Teeter (+ Delivery) OneGuide (Google Doc `1RX_HDfp-OOrjBNqrHawPWLkho0Hu_tVuQBbO_yiZUaI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
