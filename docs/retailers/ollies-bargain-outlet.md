# Ollie's Bargain Outlet — Processing Guide

> **Source:** Ollie's Bargain Outlet OneGuide (Google Doc `1IRqpP6JGQmpvktuqRCnFXSsxlRq-m0ri331IYNiGwKI`), updated Oct 8, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Hosted URL | ollies.us/currentflyer/flyer.html |
| Flyer types | Weekly · Weekly Boosted · Grand Openings — **all 3 processed under the same Weekly flyer type** |
| Processing | Auto-stack; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Tuesday.
- **Cadence:** Available From Tuesday, Available To Wednesday; Valid From/To Wednesday.
- **Short lead time (Regular Weekly / "Vanilla"):** upload as Static/Vanilla on hosted only, then follow up 3–5 business days to FQC.

## ⚠️ #1 Risk item — Mark Vanilla
**Must mark Vanilla first (Overview → Make Vanilla → All Pricing Zones) before completing Setup QC.** The Lead must review and mark setup reviewed, otherwise the flyer will not go on hosted.

## Codesheet upload (Weekly & Boosted — 2 codesheets: Pages & Versions)

Open the Ollie's Publication List → File → Make a copy. Use the **Pages** and **Versions** tabs (ensure dates match the flyer run dates).

**Prep the Versions tab:**
- Double-check start/end dates against the flyer run names.
- Confirm start/end times in columns H and J are 24hr `HH:MM` (usually `21:00`); apply the format down the whole column.
- Delete hidden rows with no store assigned. Capitalize all header-row cells. Download as `.csv`.

**Prep the Pages tab:**
- **Risk item:** confirm the pricing-zone names match the Versions tab format exactly (e.g. `W-5100` in Pages = `W-5100` in Versions column F). **Mismatches create duplicate pricing zones (one with pages, one with stores).**
- Delete any "No Pages" text. Download as `.csv`.

**Codesheet #1 — Pages:** Config `ollies`; base directory = SFTP folder path; **toggles 3/4/5/6.** Save & run. Wait until green.

**Codesheet #2 — Versions:** Config `ollies_stores`; base directory `/`; **toggles 1 and 4.** Save & run.

- If it errors, verify the available/valid dates match the Versions tab and the flyer run.
- If a page can't be found, check for typos in the Pages tab and that page names match the SFTP.
- After both run: confirm pricing-zone and page counts, then mark flyer creation complete.

## Setup (Weekly Regular / Vanilla)

- **Mark Vanilla before completing setup** (see risk item above).
- **Edit Details — dates:** Available From Tue 9pm; Valid From Wed 12am; Available To Wed 9pm; Valid To Wed 9pm.
- **< 5 business days lead time:** upload in Vanilla mode, **Available on Hosted only** (un-vanilla and set available everywhere at FQC). **≥ 5 business days:** set available everywhere, no vanilla needed.
- No preview date; Internal Run Name = Date; no external run name; no theme.
- **Thumbnails (Standard 4):** 1065×600 (2 pg), stock premium (1 pg), storefront carousel premium (2 pg), storefront carousel organic (1 pg).
- **Staggered dates (rare):** 9pm available / 9am valid / 9pm end. Wed: avail Tue 9pm, avail-to Tue 9pm, valid Wed 9am, valid-to Tue. Thu: avail Wed 9pm, avail-to Wed 9pm, valid Thu 9am, valid-to Wed.
- Confirm upload in Pricing Zone preview; confirm all sessions ran; geography usually unchanged (except recent grand openings).
- Complete Setup QC checklist, then **mark Auto Stack Spot Check complete (pushes the flyer live in vanilla mode).** Send flyer run to Lead to review. Create an Optics/PSS ticket to follow up FQC & un-vanilla (due in 3–5 days; skip if the pub ends before FQC).

## Setup (Weekly Boosted — yellow-highlighted runs)

- Typically ≥ 5 business days lead time. **No staggered dates since May 2026.**
- Same codesheet process as Weekly. Internal Run Name = Date *Boosted*. Same thumbnails and date rules.

## Setup (Grand Openings — green-highlighted, moving to Flex)

- Short lead time; upload as Static/Vanilla on hosted only, follow up 3–5 business days to FQC. Typically Available 2–4 weeks, Valid 1–3 weeks.
- DOC: create the run from the Publication Tracker dates, add the new store to Fadmin (full address & store code in the Store List tab), harmonize once added.
- **Hidden on Flipp & distribution.** No preview date; Internal Run Name = "City GO"; External Run Name = "City Grand Opening"; no theme.
- Dates: Available From Tue 9pm; Valid From Wed 9am; Available To Wed 9pm; Valid To Wed 9pm; 1-week run.
- **Manual upload:** files are in a folder named after the store — upload all pages in that folder into one base pricing zone. Add the grand-opening store number.
- Mark Vanilla (all pricing zones) before completing Setup QC; mark Auto Stack Spot Check complete.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF):**
- **Include:** packaged deals (washers/dryers), sign-up page, social media, special weblinks. If there's a "web page" at the end of the flyer, box it.
- **Exclude:** coupons, retailer logo, banners.
- Box items as they appear in the flyer; draw text boxes where items require it. **Box brand logos together (not separately).** Box items with several sizes/prices separately.

**Tag / Tag QC (Low; Auto-tag ON):**
- Include everything: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for both Box/Tag. Tag as it appears in the flyer.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

**Spotchecks:** standard pricing spotchecks in pipeline.

## Final QC (owned by DOC)

- Mark AutoStack complete; Sessions → **Mark In Store Only**; un-vanilla all pricing zones; make available everywhere; verify staggered dates (if applicable); confirm thumbnails.
- Pages: confirm all items tagged & tag-QC'd. Pricing Zone tab: confirm all items boxed; vertical preview items clickable. Geography unchanged (unless grand openings).
- Complete FQC checklist and a live check on Flipp & hosted (may take up to an hour to reflect).

## Flyer Review (owned by Flex)

- **Type: Lite.** Checks: risk items, overview tasks, pages, pricing zones, sessions, vendors, geography.

---
*Source: Ollie's Bargain Outlet OneGuide (Google Doc `1IRqpP6JGQmpvktuqRCnFXSsxlRq-m0ri331IYNiGwKI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
