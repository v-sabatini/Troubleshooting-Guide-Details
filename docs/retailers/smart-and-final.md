# Smart & Final — Processing Guide

> **Source:** Smart & Final OneGuide (Google Doc `1L8G-SxRyPXwjSsRG5as3y6Wv-74iWO9-TbKoqveJDa4`), updated May 14, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#smartandfinal` |
| Hosted URL | smartandfinal.com/flyers |
| Flyer type(s) & cadence | **Weekly** (type 7853) — receives 2 versions weekly (5-day Wed–Sun + 2-day Mon–Tue); **Business Mailer / Business Saver** (type 8004) — biweekly |
| Processing | Auto-stack; Flex (FAB tickets); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> **Note on timezone:** FAdmin runs on EST; Smart & Final is California-based (PST). All valid-from times must be set to **3 AM** so flyers go live at the correct local time.

## Files & schedule

- **When files arrive:** Monday (weekly codesheet/version list + PDF via email). Interstitial pages ("inserts") arrive Friday/Monday for the flyer going live Tuesday.
- **Weekly cadence:** Available From Tuesday, Valid From Wednesday; Available To Monday, Valid To Tuesday.
- **Consumer preview:** the **2-day sale has a consumer preview; the 5-day sale does not.**

## Upload & setup — Weekly (owned by DOC)

1. Download files from the emailed link and upload to the SFTP. Confirm the codesheet (`.xlsx`) is attached and added to the SFTP.
2. **Codesheet manipulations:** open the **ad recap** tab → delete column A entirely → ensure "In store version" is in column F (move it there if needed) → change "Store No" to "Store #" → unhide any hidden rows/columns → save as **Excel 97-2003 (.xls)**.
3. **Upload codesheet:** name = Week # (e.g. "Week 35"); **config `smart_and_final`**; path taken from the directory; **select all toggles EXCEPT combine zones and region assignment** (exclude #2 and #7).
4. Wait for sessions. **Edit Details:** no theme; toggle **Hidden in Hosted**; set **valid-from = 3 AM**.
5. Leg heights preset 50x25; Standard 4 thumbnails; Setup QC checklist.

### ⚠️ Common errors (retailer-specific)

- **Files arrive early, linking doc arrives a day later.** Either upload files with a vendor note "Linking doc to be attached EOD Tuesday" so OS can start boxing, or wait for all assets.
- **PZ mismatch:** ensure PZ in column F (ad recap tab) matches PZ in the version list tab. For the 2-day vs 5-day flyer you usually need to add **"D"** to the 5-day PZs.
- **Store 350 PZ** often reads `A!NV` but should be `A1NV`.
- Warning *"Version Code A1 not found in first tab for Store 304"* → 5-day steal page 1s have a "D" suffix; add a D to all zones in the Ad Recap "column F – Instore version" so Ad Recap col F matches Version List col A.
- Codesheet errors are usually page name / stray zones: match the codesheet page names to the PDF names in the FTP; delete version-list rows for missing stores the retailer forgot to remove; confirm all pages uploaded to FTP.
- Error *"Could not find file Spreads with …CIR02_C_A1.pdf"* → "Spreads with" sits in column J of the Version List tab (a wide page 2). Remove column J entirely, then rename the Page 4 header to Page 3.
- **Pipeline often gets stuck at Tag QC** — monitor throughout the week.

## Upload & setup — Business Mailer (owned by DOC)

- **Manual upload.** Flyer type: Business Savings (8004). Internal run name: "Business Card WK 1/2". Add all pages (usually 2–8) → Autogroup → Save.
- Create 1–3 pricing zones; add stores using the **generic store codesheet**: from the S&F codesheet, column E = stores → generic column A; column K = PZ name → generic column B (label "Base" if all rows share one name). Download as CSV and upload via FAdmin.
- **Edit Details:** no theme; Hidden in Hosted; valid-from = 3 AM. Leg heights 50x25; Standard 4 thumbnails.

## QC specifics

- **Box Draw (Medium; Auto-Box ON, Box QC bot ON; PDF image auto-selection ON):** include coupons, packaged deals, sign-up page, social media, special weblinks; **exclude retailer logo.** Box all email signup / delivery banners; box & tag the four social icons (Facebook, Twitter, Instagram, Pinterest) separately; box ".com" and phone-number call-outs (usually bottom of last page) and promotional banners. (Business Mailer additionally requires a Box Draw linking document.)
- **Tag / Tag QC (Medium; Auto-tag OFF):** Weekly **excludes SKU and URLs**; Business Mailer **includes SKU** (linking doc required). 
  - **Name/Brand:** one brand → Brand field; multiple brands → leave Brand blank. Name = full product name **excluding sizes**.
  - **Description:** include sizes and text like "Selected Varieties." **If the item has a digital coupon, prefix the description with "with Digital Coupon Savings."**
  - **Price:** larger number = Price, smaller = Original Price.
  - **Pound offers:** do NOT use "3 LBS FOR" prefixes — divide price by pounds, use postfix **LB**, add the sale to the disclaimer.
  - **Disclaimer:** add the day of week if the valid date differs (e.g. "Wednesday Only"). "Buy 4 & Save 4"-type callouts must go fully in the **disclaimer** field (not sale story) for every item under the banner; full text is usually on the last page.
- **Image QC:** prioritize clean PDF images; cutout when not clean (no dark shadows around the image).

## Inserts / interstitial pages (Weekly)

- Sent Monday before go-live via email; placed **after page 1 in positions 2 and 3** in the order listed.
- Download and upload manually; change the conversion library to **ghostscript 9.06** gamma (fixes weird text).
- One box covering the entire page; Display Type: Link; Name = CTA "Shop Now, Save Now"; Link provided in email (blank URL is OK if none given).
- **⚠️ Ensure inserts don't auto-merge to page 1 or other pages** — check each zone via [Pricing Zones] → storefront spotcheck.

## Final QC (owned by DOC)

- **Weekly:** confirm every digital-coupon item has "With Digital Coupon Savings" at the start of the description (identify via the "Weekly Digital Deals" blue background / dotted border on page 1–2; note the same item can have different names, so QA each page). Confirm "Buy 4 Save 4" callouts are in the disclaimer field. Check Pages, Pricing Zone, Sessions, Vendors, Geography tabs. **Ensure valid-from time is 3 AM.**
- **Business Mailer:** mark auto-stack spotcheck complete; check Pages/Pricing Zone/Sessions/Vendors/Geography; run FQC checklist.

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing

- Page swaps follow the baseline page-swap process.
- **Discontinued — Offer ID (A2C):** historically Offer IDs were tagged in the SKU field (one Offer ID per item; match the Offer-ID prefix to the page name — "COVER" = page 1, "BACK" = page 2). Only performed if 200+ SKUs were missing; otherwise re-run tag/tag QC with a vendor note to fill missing SKUs.

---
*Source: Smart & Final OneGuide (Google Doc `1L8G-SxRyPXwjSsRG5as3y6Wv-74iWO9-TbKoqveJDa4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
