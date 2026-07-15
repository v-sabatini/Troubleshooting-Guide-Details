# The Brick — Processing Guide

> **Source:** The Brick OneGuide (Google Doc `1-LJ4fbKhG5-ZyNT-6IHiUt3nJFsWLPFUkgLIAMwp5LE`), updated Oct 27, 2025. Contacts/credentials omitted. (SFTP password lives in the OneGuide — not stored here.)

## Account at a glance

| | |
|---|---|
| Account tier | **Tier 1 Premium** (bilingual EN/FR) |
| Availability | All platforms |
| Slack channels | `#thebrick` |
| Hosted URLs | thebrick.com, brickenligne.com (FR) |
| Flyer types | **Mainline** (Weekly Ad) · **BMS** (Brick Mattress Store, merchant "The Brick Mattress Store") · **My Brick Home** |
| Cadence | Ad-hoc — does not follow a fixed cadence per flyer |
| Processing | Auto-stack; no Flex/OS in standard pipeline (DOC-owned); no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** ad-hoc, via email (Distribution sheet + PDFs).
- **Linking docs:** 1 Generic Links + 2 PLA reports (EN & FR separate) for Mainline; BMS = 1 Generic Links + 1 PLA (EN only). PLA (product landing) reports downloaded from The Brick's datafeed URLs; OS uses SKU to look up URL/name.
- Flyer run name format (reporting): `Flipp - PUB NAME - Mmm DD YYYY`.
- Wrap pages (first 1–2 "second cover" pages) have special valid dates; always present at go-live, removed when validity ends — set a trigger.

## Upload & setup (owned by DOC)

- **SFTP transfer:** download the two emailed files (Distribution & PDFs). **For FR pages, add a dash between province and FR** (`FPFR→FP-FR`, `NBFR→NB-FR`, `QUFR→QU-FR`). Upload to SFTP (host `sftp.flipp.com`, user `flyers_thebrick`, **password in the OneGuide — not stored here**), into the current year's folder.
- **Codesheet:** open the Distribution sheet; in the Distribution List tab add the same FR dashes; copy QC FR stores into the QC EN stores cell (they add a stray space in QC EN between 3L, EI); save as CSV. In the Links tab, delete the Distribution tab and **download as XLSX** (to keep images).
- Upload the codesheet with config **`the_brick_new`**, full base path, **all toggles except 2 & 7**.
- Attach the Links spreadsheet to all tasks (all languages); attach EN & FR PLA reports to their languages. Thumbnails: Standard 4 + thumbnail. Set vendor tasks to **HIGH** priority.
- **Setup QA:** PZs have similar-but-not-identical page numbers; languages set correctly (FR-named zones set to FR); no stores in multiple zones (confirm with Brick if in distro doc); stale empty; geo consistent week over week.
- **Edit Details:** available everywhere; preview date 2–3 days before go-live (so PS can finish links QC); External Run Name (EN & FR) from the PDF; No Theme. Reply to the email confirming preview/export delivery.
- **BMS (Hosted):** in Distribution List update `Hosted (NAT)→Hosted (AB)` and `App (NAT)→App (AB)`; available hidden in Flippfully & Native X. **BMS (Flipp)** (new merchant "The Brick Mattress Store", Nov 2024 process): clone a shell in the Weekly Flyer type, keep only App zones (App (AB), App (Nat)), delete auto boxes, available hidden in hosted — this version skips vendor processing; copy items from Hosted to Flipp after FQC (cannot clone between merchants).

**Custom actions:** "Set Cutout Images" (+ flyer run ID) once items are URL/SKU-QC'd and ready for data piping; "Remove FSAs & Assign FSAs from CSV" (remove Quebec FSAs from EN/Ontario zones and reassign to Quebec zones) as the final FQC step.

### ⚠️ Common errors / risk items (retailer-specific)

- **Text boxes missed on hero pricing (HIGH RISK):** when one hero price applies to multiple items and a text box isn't drawn for every item box, items with different prices get diffed as identical and the wrong price is pushed to some versions. Draw a text box (overlapping OK) on **every** impacted item box across **all** versions to break diffing; update pricing to match the PDF.
- **TTMs missing on Hosted:** on pages not fully processed within the run (page swaps, recurring inserts, clones), "Shop Now" buttons don't appear even though URLs are tagged. Workaround: press "Apply All" in the flyer-run tracking-codes UI, re-run page stitching, wait up to 30 min.
- **Page links:** always need updating when triggering pages or adding inserts (e.g. "Shop our Digital Flyer" insert).
- **Wrap-removal triggers (page links):** if a page link points to a page number that a trigger later removes, the trigger appears to succeed but the pages stay live with no warning. Workaround: update the page link to the new destination the business day before the trigger.
- **SKU tagging (mattresses, bedroom & dining sets):** SKUs absent from PDFs for alternate sizes/set pieces — OS derives them via SKU-variant logic (see below). Mattresses QA'd 100%; dining/bedroom sets only caught via the Unique-SKU QA process, retailer corrections, or PQC/live-date flags.
- **TV line items:** boxed separately from the hero TV offer; **item-level valid dates apply only to the hero offer, not the line items.**
- **Secondary Content Policy does NOT apply to The Brick** (historical CuSat issue).

## QC specifics

- **Box Draw — Mainline: Low. BMS: High. Auto-Box OFF, Box QC bot OFF. Linking doc required.** Exclude coupons; include packaged deals, retailer logo, special weblinks (sign-up/social N/A). One box per item; text boxes when the price can't sit in the image box, and one per item when multiple images share a price (overlap OK). TVs/mattresses: separate box per SKU/size with its own price. Bedroom/dining set pieces with a price boxed separately; anything with a "+" CTA boxed. Box all banners with savings/promo, contest prizing, financing, delivery, or warranty info. If a Linking-Document banner/CTA is set to an Item display type, change it to **LINK** and use the spreadsheet URL.
- **Tag / Tag QC — Mainline: Low. BMS: High. Auto-tag OFF. Linking doc required. Description excluded (Mainline); Pre/Postfix excluded (BMS).**
  - **Display Type:** anything present in the Linking Document must be a **LINK** display type — regardless of whether it looks like a shoppable product.
  - **Brand:** tag per the logo/Name (curated brand list e.g. LG, Sealy, Samsung, Tempur-pedic…). "Cami/Stripes/Wynn/Garbo/Bogart" are NOT brands (collection/descriptive words).
  - **Name:** if a URL is found, tag the name **as on the thebrick.com landing page** (including SKU/colour variations), NOT as on the flyer. If no landing page, use the PDF name.
  - **SKU:** tag the PDF SKU (copy from text extraction, don't transcribe). Derive missing SKUs by manipulating the related item's SKU (e.g. Queen `…QM` → King `…KM`; dining table `…TL` → 5-pc `…P5`, 7-pc `…P7`, chair `…SC`). SKU-variant table: Queen/Grand=QM, King/Très Grand=KM, Twin/Simple=TM, Full/Double=FM, Set=P.
  - **URL:** must be a **product landing page** (not a search page). EN → thebrick.com, FR → brickenligne.com.
  - **Prices:** enter prefix/current/postfix/original as in flyer (postfix can carry `++ $x/MTH` financing).
  - **Valid dates:** override only when the PDF date differs from the flyer; days-of-week → first instance while valid; do NOT apply hero valid dates to TV line items.
  - **Category chart:** Sofas & Sectionals; Dining; Bedroom; Appliances; TV & Accessories; Electronics (**not for TVs**); Beds & Mattresses; Home Accents; Furniture — each with a defined item list.

## FQC / go-live

- **Flex Links QC:** cross-reference the codesheet "LINKS" tab against PDF CTAs page-by-page (Pages interface, group by page #); box/tag links; CTAs with a SKU but found in the link doc → override to direct link; delete boxes for CTAs with no corresponding link. Confirm on one EN + one FR version, save, refresh (pushes to diffed versions).
- **DOC — Sub-items / valid dates / wrap triggers:** verify mattress/TV sub-items boxed separately and sized correctly (Item Search QA: URL contains queen but item is king → fix name/SKU/URL, etc.); apply special "Starts/Ends" valid dates by SKU (legal); wrap pages — multi-edit valid dates on pages 1–2, create a trigger to remove wraps at 11:59pm end date, and an OPTICS/OPSMR ticket (can combine Mainline + BMS + TBMS).
- **DOC — Links QC:** export items, VLOOKUP against the PLA "Products" tab to populate EN/FR URLs (`brickenligne` = `thebrick` find-replace for FR); rename generic "Brick" items to "Homepage"; fix any URL containing "search"; QA missing URLs then missing SKUs (untoggle "Show One Per Item Group"), doing English first (URLs differ by language). Verify `SAFL600W` lands on the correct product (not `SAFL680W`).
- **Style Guide Rules:** Overview → Special Actions → Style Guide Rules → Apply Rules.
- **Previews:** item reports generated & vertical/horizontal previews sent (Mainline ~5pm EST day before; BMS by 10am), all 4 preview URLs verified (re-run Page Tile Generation if boxes aren't clickable). Clone BMS after Mainline.
- **Flyer Review type:** Mainline/BMS processing owned by DOC; flyer review resources in the OneGuide.

## Out-of-processing

- Page swaps: standard baseline process.
- Wrap triggers as above; page links must be re-checked with every trigger/insert.

---
*Source: The Brick OneGuide (Google Doc `1-LJ4fbKhG5-ZyNT-6IHiUt3nJFsWLPFUkgLIAMwp5LE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
