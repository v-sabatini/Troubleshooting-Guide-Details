# Walmart CA Flash Deals & Spotlights — CP Processing SOP : TIDERISE

> **What this covers:** TideRise (TR) processing steps for the Walmart CA
> Spotlights and Flash Deals single-page inserts — data formatter + curation
> build, banner/URL handling (incl. Klarna defaults), image ingestion, flyer
> processing, and Fadmin steps (triggers, stores, removing extra pages).
> Source Confluence page id: **13065191547** (CP space).
> **See also:** Walmart Canada OneGuide in `docs/retailers/walmart-canada.md`.
> Contacts/credentials intentionally omitted. This SOP covers previews (all
> previews follow the same steps).

## Account at a glance

| | |
|---|---|
| Merchant ID | 234 |
| Flyer Type ID | 10617 |
| **Flyer height** | **2560** (set via custom action; cannot be changed after processing) |
| Slack channel | `cp-tiderise-pdfsf` |
| Spotlights | 6-item "skinny" insert |
| Flash Deals | 12-item regular-sized page insert |

## Things to note

- The specialist indicates in the Direct Retailer Schedule processing notes which publication (Flash Deals or Spotlights) and which week number (which data-sheet tab) to work on.
- **The data formatter is highly sensitive** (many formulas) — make minimal changes.
- Spotlights and Flash Deals are single-page inserts with EN + FR versions. Fadmin cannot process single pages, so the page is **duplicated** to run; the extra EN and FR pages are deleted afterward.
- If any data is incomplete and blocks processing, notify the specialist.

## Processing (Spotlights and Flash Deals follow the same flow)

- Walmart emails an Excel document and banners (with links) if applicable. If no new banners are provided, use the previous week's **Klarna** banners.
  - Spotlights default banners: `EN_1125x276_Klarna`, `FR_1125x276_Klarna`
  - Flash Deals default banners: `EN_1242x135_Klarna`, `FR_1242x135_Klarna`
- The Excel is named like "Flash deal/Spotlight Wk # - flyer submission or feedback"; tabs are by week number and each tab holds 4 weeks of product data. **Column A** shows which week each set is for — copy the correct week's data.
- Create a drive folder named for the week + flyer type (e.g. `Wk 4 Flash Deals`); drop banners there. Create a preview subfolder (e.g. `Preview 1` / `Go-Live Preview`) and drop the data sheet.
- Create a new week folder in the relevant Flash Deals / Spotlights drive and upload the banners (copy the Klarna banners from a previous week if none provided). Create a preview subfolder and upload the Walmart data sheet.
- Schedule processing in the Direct Processing Schedule. In the processing notes, include the banner links from Walmart; if using the Klarna banner, include:
  - EN: `https://www.walmart.ca/en/cp/klarna-shop-now-pay-later/6000207121456`
  - FR: `https://www.walmart.ca/fr/cp/klarna-achetez-maintenant-payez-plus-tard/6000207121456`
- Upload the banner images to Cyberduck (from this week's folder).
- Open the Excel for the week (Spotlights = 6 items; Flash Deals = 12 items). If multiple tabs, select the week in the processing schedule. Under Column A find your week and, for that section only, copy from **SKU (Column H)** to **Image URL (Column P)**.
- Open the **Data formatter**, go to the Spotlight or Flash Deals retailer-data tab; starting in **SKU (Column F)**, paste the data.
- Go to the Data Formatter **EN** tab (Spotlights or Flash Deals) and copy all data. In the curation sheet's Product Data tab, paste starting from **description**. If there is old data, run the **"clear spotlight cells"** / **"clear flash deals cells"** macro. **Paste the data again right underneath** — you should end with two identical stacked sets. Repeat for **FR**. Result: 2 EN + 2 FR data sets (the duplicate satisfies Fadmin's 2-page minimum).
- In the curation sheet's Story Curation tab (Set A for Spotlights / Flash Deals Story Curation), scroll to columns **J and K** (yellow cells). Under **background image**, replace the banner name in the yellow cell with the exact banner file name from the shared drive (**exact match, no extra spaces**); use the Klarna defaults if none provided. Do this twice for English, then (under the red line) twice for French.
- Under the **URL** column, replace the URL in the highlighted EN/FR cells (new URL comes from the processing schedule or specialist; otherwise use the Klarna URLs above).
- Download the Product Data and Story Curation tabs as CSV.
- Run the product data sheet through **Auto Image Processing** (Merchant ID: 234).

## Flyer processing

- Once images and banners are in, run the product data + curation sheets through **Generate Merged Datasheet**:
  - Merchant ID: **234**
  - Flyer Type ID: **10617**
  - **Flyer height: 2560**

## Fadmin steps

### Flyer details
- Change dates to match the processing notes. Update the flyer run name to `CP_Wk # Spotlights Preview 1` / `CP_Wk # Flash Deals Preview 1` (or go-live preview).
- Hide the flyer in all Flipp apps; set preview date to today.

### Trigger
- Triggers page → Create new trigger → set **attribute to distribution channels, then add Flipp hosted**. Run at 12AM on the available day (e.g. flyer available Feb 4 11:58 PM → trigger runs Feb 4 12AM). Create trigger.

### Stores
- Pricing Zones page → press the "0" under the stores column → add store set **`_CP_CDN_NATIONAL`**. Do this for EN and FR.

### Removing extra pages
- Fadmin needs at least 2 pages per zone (why the data was duplicated). Remove the extras: in the EN pricing zone delete **page 2**; in the FR pricing zone delete **page 4**.

### Hand-off
- Send the Fadmin link to the specialist in the `cp-tiderise-pdfsf` channel.

## Specialist / go-live notes

- Flash Deals and Spotlights get two previews: Proof 1 and Go-Live preview.
- Confirm flyer height is **2560** (Edit details → show rarely used fields). Height cannot be changed after processing — if wrong, TR must re-run via the custom action.
- 4 pages total (2 EN, 2 FR) but only page 1 (EN) and page 3 (FR) appear in the preview (the duplicates satisfy the 2-page minimum and are removed for preview). Check images/banners pull through; QC an item or two against the Walmart datasheet. Confirm dates and triggers (flyer runs 1 min; trigger hides in hosted before available-from).
- Go-Live is always Tuesday; latest go-live approval is 12PM Tuesday.
- After go-live approval: delete the two duplicate pages from the flyer run, re-confirm height is 2560 (Ops cannot copy boxes/tagging otherwise), download the EN and FR pages, and send them plus the flyer run link to Ops by 12PM Tuesday.

---
*Source: Confluence "[TIDERISE] Walmart CA Flash Deals & Spotlights SOP" (CP, 13065191547). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
