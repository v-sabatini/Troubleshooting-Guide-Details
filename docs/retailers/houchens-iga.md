# Houchens IGA — Processing Guide

> **Source:** Houchens IGA OneGuide (Google Doc `12XUi3vutaRNZezmB6d2CwRVu6sYJn5fZV27KNn0oVIQ`), updated Apr 27, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flexflyerreview` |
| Hosted URL | myiga.com |
| Flyer types | Weekly Flyer — **promoted (11852)** and **organic (11913)** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no OS, no coupons, no Feedel/data services |

## Files & schedule

- **When files arrive:** Tuesday.
- **Publication cadence:** Available From Wednesday → To Tuesday; Valid From Wednesday → To Tuesday.
- **Workflow:** Upload & Setup and FQC both owned by FLEX.

## Upload & setup (owned by FLEX)

Codesheet upload. The core task is **splitting one weekly breakdown into a promoted codesheet and an organic codesheet.**

- From the Houchens FTP, search "xls" and download the week's file (e.g. `IGA Ad Breakdown m.dd.xlsx`).
- Open the shared **Houchens IGA codesheets** sheet → File → Import → Upload → insert new sheet.
- Insert a column left of A. `A1` = `Promoted`; `A2` = `=IF(XLOOKUP(B2, IGA!$B$2:$B$45, IGA!$A$2:$A$45, "")="Y", "Y", "")`; fill down the column.
- Delete columns C–J so only **Promoted | Store # | Page Versions** remain; split column C via "Split text to columns"; rename page headers to page numbers; add filter.
- Duplicate the sheet: in one, filter for **Y** → name "promoted" → export CSV; in the other, filter for **Blanks** → name "organic" → export CSV.
- Upload each CSV to the corresponding flyer run: **all codesheet toggles checked except the 2nd and last**; **config name `generic`**; use the week's FTP file path; process.
  - Common error: differently named files — adjust the codesheet to match the FTP.
- Mark Flyer Creation complete, wait for sessions, then do Setup QC.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View); risk: confirm no SFTP pages left un-uploaded.
- Confirm flyer dates (usually top of first page).
- Thumbnails: 4 Standard. Add **"Weekly Flyer"** to the external run name (English).

## ⚠️ Common errors / risk items (retailer-specific)

- **Ensure codesheets are organized correctly — especially regarding the promoted vs organic store split.** This is the main failure point for this account.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF.** Box any product block with a price and/or sale story. **Exclude** coupons, packaged deals, retailer logo, banners, social media.
- **Tag / Tag QC — Low complexity. Auto-tag ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Spotchecks:** standard pricing spotchecks (20% of pricing zones at pre-FQC).

## Final QC / flyer review (owned by FLEX)

- Pre-FQC: dates vs PDF; **all availability toggles should be unchecked**; thumbnails include retailer logo; previews clickable; sessions complete; geography matches last week's flyer.
- **Flyer Review type: Simple** — flyer dates, sessions, previews, spotcheck tagging, geography, availability toggles (all unchecked).

---
*Source: Houchens IGA OneGuide (Google Doc `12XUi3vutaRNZezmB6d2CwRVu6sYJn5fZV27KNn0oVIQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
