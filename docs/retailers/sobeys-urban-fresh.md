# Sobeys Urban Fresh — Processing Guide

> **Source:** Sobeys Urban Fresh OneGuide (Google Doc `1hZjFwxtu5HDNS_STO1nqRPNi_3zSzc-puy95h05uv7I`), updated Aug 11, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 1 Premium (relationship quality: Excellent) |
| Availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeysops`, `#3flf-sobeys`, `#sobeys-dataservices` |
| Flyer type(s) & cadence | Weekly. Available From Wednesday, Valid From Thursday; Available To / Valid To Wednesday. Preview Monday |
| Processing | Auto-stack; Flex (3FL); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

## Files & schedule

- **When files arrive:** Thursday or Friday (flyer goes live Wednesday, 1-day preview Tuesday). Distribution list arrives by email.
- **⚠️ Double-check that the flyer dates match the shell** — if the shell dates are wrong, update the shell to match the PDF.
- Flyer is uploaded manually. There is a codesheet on the SFTP for page/pricing-zone assignments: `URBAN_FRESH_WK#_Code_Sheet.xlsx`. The store list ("Zone Summary") is emailed each week.
- DOC: update the Vendor Assigned Tasks (VAST) tracker and upload the zone-summary document to the Urban Fresh folder; review upload Friday mornings.

## Upload & setup (owned by Vendor)

- **⚠️ Upload ALL files with the current week's path** — even if a page is named "SOBEYS" instead of "UF", it must be uploaded and added to pricing zones. Refer to the Code Sheet when in doubt.
- **Manual upload:** in the SFTP select ONTARIO > URBAN FRESH > that week's files; select ALL files (UF/Sobeys) → Select Files → set the grouping to match the page order in the Code Sheet → Save and Complete.
- **Pricing zones:** use the print code sheet to determine how many zones to create. **Name them exactly "Zone 1" and "Zone 2"** — no all-caps, not "Run", not "ZONE" (only "Zone 1"/"Zone 2" are accepted by the retailer, even if the docs say "Run").
  - **One pricing zone:** add the `[Sobeys Urban Fresh]` store set.
  - **More than one:** add stores using the zone summary emailed on Wednesdays.
- Check the SFTP to confirm all files uploaded.

### Setup QC (owned by Vendor)

- **Edit Details:** External Run Name = "Weekly eFlyer"; no theme; Key Messages — Long: "Weekly Ad. Weekly Savings.", Short: "Weekly Ad." (enter the key message via show/hide rarely-used-fields).
- **QC Thumbnails (1065x600):** remove white border, focus on pg 1, wrap pages and pg 2. Then: **stock premium** (all base/flyers, apply positioning — focus pg 1), **storefront carousel premium** (pg 1&2 + wrap pages), **storefront carousel organic** (pg 1), **thumbnail** (pg 1&2 + wrap pages), and **fpt_400w** (pg 1). Save and exit.
- **⚠️ [NEW] Merge the two skinny FL pages:** Pages → for each pricing zone open Storefront Spotcheck and press **Merge** on FL01; scroll the preview to confirm FL01 and FL02 are side-by-side.
- Set Vendors priority to **High** (short turnaround). After sessions run, complete the Setup QC checklist. Mark the Autostack spotcheck complete (this completes the auto-publish task for vertical preview at FQC).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** include retailer logo and the Scene+ banner (bottom); exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box all items with prices (text boxes when necessary).
- **Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs; **exclude disclaimer** (except the Scene+ note below). Brand only in the brand field — do not double it in the name.
  - **Sale Story / Scene+:** every offer with an accompanying Scene+ offer must have **"Scene+" tagged in the Sale Story** — including offers that only show points earned (no literal "Scene+" text).
  - **KG/LB:** the **/lb price is the main price** with "lb" as postfix; the **kg price goes in the Description** for all produce, meat and seafood items.
  - **Disclaimer:** add the "$$$ without Scene+ Card" callout in the disclaimer.
  - **Categories:** include the most relevant category; Scene+ items also need the Scene+ category.
- **Image QC:** no longer needed for the FLEX team. When done: clean white-background PDF preferred, cutout otherwise; use the first/best product image where multiple exist; no black shadows; text cutout OK when no item image exists; **for banners, do not select a PDF image.**

## Post-processing / Final QC (owned by Vendor)

- **Legibility Heights:** Scan Mode 40, Read Mode 35.
- **QC Categories** (rule of thumb by department — meat/seafood: fresh/raw; deli: cooked/sliced meat/fresh pizza; produce: veggies/salad mix; grocery: everything + frozen veg/fruit + canned tuna; bakery: fresh baked goods; hard cheese: cheese; cream cheese: dairy; no category for direct links). Ensure all Scene+ items have the Scene+ category.
- **Page categories:** every page gets **Scene+ and Grocery** (type on page 1, copy to all pages), then add all remaining categories per page.
- **Scene+ check:** Item Search → Sale Story contains "PTS" (ensure Scene+ tagged); Disclaimer contains "Scene" (ensure it's the "without Scene+ card" price).
- **LB check:** Item Search → Postfix contains "lb" (main price is /lb; kg price in description).
- Do horizontal + vertical previews (EN), check insert links, confirm everything boxed; Pages tab — first two numbers green and matching; Sessions all green (PDF Image Auto Selection may be yellow). Run FQC checklist (the "some categories do not have thumbnails" error can be ignored).

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing — Inserts (updated Mondays)

- Check the Sobeys Insert Tracker for the date/banner. Pages → Edit → find insert pages in ONTARIO > URBAN FRESH > URBAN FRESH INSERTS; select the inserts → Save and Complete.
- When Box Draw becomes available, draw one box around each insert page (complete & next, repeat); tag with the link from the Insert Tracker; complete outstanding vendor tasks. If the inserts match the prior week, Copy Items from the previous flyer run.
- Insert pages into the run: Pricing Zones → pencil tool → add page → select all → arrange per the tracker → Save and Done (repeat for **each** pricing zone).
- **Submit an OPTICS ticket** (OPSMR board) for Urban Fresh: summary "[Due DD/MM EOD] Urban Fresh Inserts" (due the day before go-live), type Page Inserts/Removal, description = run URL + Insert Tracker screenshot, merchant Sobeys, assign then move to Lead Review.

---
*Source: Sobeys Urban Fresh OneGuide (Google Doc `1hZjFwxtu5HDNS_STO1nqRPNi_3zSzc-puy95h05uv7I`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
