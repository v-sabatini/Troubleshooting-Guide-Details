# Tepperman's — Processing Guide

> **Source:** Tepperman's OneGuide (Google Doc `1TopC05KCtwPfSYUC05-p7MnPsoTPK0IA_2A68J7x9qw`), updated Feb 4, 2026. Contacts/credentials omitted.

Complex, multi-publication account: four runs per week (Tepperman's Paid/Hosted + Outlet Paid/Hosted), plus a Catalogue flyer type.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#teppermans` |
| Flyer types | Flyer Type 1 **Tepperman's**; Flyer Type 2 **Outlet** (ID 2894, cloned from Tepperman's); Flyer Type 3 **Catalogue** (ID 6446) |
| Processing | Auto-stack |
| Who's involved | Flex setup + FQC; OS setup; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available Thursday → Friday; Valid Thursday → Thursday.
- **Preview date:** one consumer preview day.

## ⚠️ Common errors / risk items (retailer-specific — high value)

- **Boxing:** box the whole item; all items boxed separately.
- **Pair prices:** do NOT include pair prices in the sale story. Do NOT use pair prices in the current-price field **unless** items have no separate prices. Use **individual prices** in current price; put pair price in the **description** (for both items). Include "AFTER $### ENERGY STAR INSTANT REBATE" in the description with the pair price when items have separate prices.
- **Sale story:** tag callouts like "Save 25%", "50% off", "$50 off". Do **NOT** include "back to campus", "outlet special", or "25% instant rebate".
- **Sale callout banners:** do NOT tag in product fields; only box callouts shown in the retailer spreadsheet; tag separately as **LINK** type (Name + URL minimum).
- **ALIST:** always box the "GET ON THE A LIST" button (usually the last page). Box the entire ad. Display Type = Link; Name = ALIST; URL = `https://mailchi.mp/teppermans.com/alist`.
- **Postfix:** only tag if the postfix is NOT in the product name. Do NOT tag postfixes like "SOFA", "QUEEN SET", "QUEEN".
- **Linking:** links are often cut off or misapplied. Confirm each item by page number, item name, and brand. Copy the whole cell with Cmd+C — do NOT manually highlight the link (risks copying a cut-off link).

## Upload & setup

### Pre-setup: linking document manipulation (Flex)
- Retailer notifies of the URL document drop by email; download from FTP; open in Google Sheets.
- **Isolate the final URL:** copy Column K ("URL FINAL (USE THIS ONE) x FLIPP…", usually red) and paste back as values-only (Cmd+Shift+V) in the same position.
- **Delete all other URL columns** (e.g. columns G–J).
- **Verify UTMs:** Tepperman's links end `Teppermans-W#-Mon-Paid&utm_content=friday`; Outlet links end `Outlet-W#-Mon-Paid&utm_content=friday`.
- Find & Replace "Organic" → "Paid" in the URLs column. Ensure the "Extra UTMs" tab has the matching month/weeks. Save as `.xlsx` to the OS setup OneDrive location.

### Setup: upload (Vendor)
- Pages → Edit → Select files from FTP. **You need two file types per run: (1) Weekly/Tepps and (2) Outlet — in different folders.** Naming includes calendar month/year and week (e.g. `0126_W1 Tepps`, `0126_Outlet_W1`).
- **Handling WLCSK / ASTC versions:** pages labelled WLCSK or ASTC go into **separate pricing zones** (different store groups, can't be combined). Upload manually into their PZs; use the codesheet (`Teppermans_codesheet_W#_MMYY_CODE`) for pagination and store assignment.
- **Upload into the Tepperman's Flyer Typer, NOT the Outlet Flyer Typer.** Select the weekly/tepps folder first (weekly pages first), then the weekly outlet folder second. Grouping sequential (e.g. 1→14). Language English. Save and complete.
- **Flyer Type 2 (Outlet):** do NOT upload anything to the Outlet flyer type — all pages go to the Tepperman's run and are cloned to Outlet during FQC with pagination switched.
- **Flyer Type 3 (Catalogue):** houses runs outside the weekly publications — upload the correct folders directly.
- **Setup QC:** one consumer preview day; attach linking document (manipulated as above); one PZ named "Base"; add all stores.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc Box-specific)**
- Include: packaged deals, sign-up page, special weblinks. Exclude: coupons, retailer logo, social media.
- Box the whole item; all items boxed separately. Box multiple appliances / grouped mirrors / different product sets separately. Use **one** text box when needed; avoid text boxes unless absolutely necessary. Overlapping TVs/appliances boxed individually. Box & tag banners/sale callouts **only** if in the retailer spreadsheet.
- Special cases (holiday/electronics/appliance flyers) have different rules — box TVs individually especially with unique links; if individual sets have links use separate boxes.

**Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking doc Tag-specific)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.** Brand is Box-specific.
- **Name:** use the name from the linking document (Column E – Product), NOT the flyer name. Never tag a price in the name field.
- **Description:** include text near the product name; tag package-deal info for all included products; tag pair prices (both items); tag "# YEARS INTEREST FREE… $## PER MONTH" callouts.
- **Current Price:** tag the red font / price in red boxes, or the highest price when no red text. Do NOT tag price ranges — put them in the description.
- **Prefix:** "Starting At" where applicable. **SKU:** from linking doc. **URLs:** ~95% of products should have a URL — search columns D (page), E (product), F carefully.
- If there's no price, tag as **Link** type.

## Final QC (Flex-owned) — multi-publication cloning

- **Phase 1 – URLs/assets:** download the URL linking sheet; Overview → "Item without URL"; verify each item truly has no URL (URL field should only contain a UTM or "DO NOT LINK"); apply links where present. Clean postfixes ("QUEEN BED", "SOFA"). Verify Standard 4 thumbnails.
- **Phase 2 – custom tiles:** apply manually to "Storefront Premium" and "Storefront Carousel Premium." From the FTP search "customtile"; download Desktop and Outlet `.jpg` for the current week; upload and Override Thumbnail. Set External Run Name (English) to include "Tepperman's: [Custom Tile Callout]".
- **Phase 3 – config/categorization:** set page categories (Tepps Page 1 gets no category); mark In-Store Only items (Sessions or Overview → Ad Hoc); check pagination across PZs; insert revised pages.
- **Phase 4 – cloning:** create a Hosted version (clone "Flyer Name- Hosted"); clone the primary to the pre-existing Outlet run and change PZ page order so the Outlet page is first; repeat thumbnails/custom tiles with Outlet-specific tiles; set External Run Name "Outlet: [Custom Tile Callout]"; clone Outlet → "Outlet- Hosted".
- **Phase 5 – UTM strings:** export items (Overview → Info/Reports → Export Items); keep only Item_id, sku, url; delete "Page Items"/"Flyer Items" rows; Find & Replace "Organic"→"Paid" for Paid runs (and "Paid"→"Organic" for Hosted runs); ensure UTMs match month/week; re-import via Import Items. Double-check: Hosted runs should return 0 for URL contains "paid"; Flipp/non-Hosted runs should return 0 for URL contains "organic".
- **Phase 6 – platform settings:** Hosted flyers = "Hidden in Distro" + "Hidden in Flipp"; non-Hosted = "Hidden in Flipp Hosted." Check sessions and FQC checklist for all runs; rerun Box QC if item cutout generation is incomplete. Merchant Page Flyer Sorting = "Flyer Type Oldest First" (Tepperman's weeklies above Outlet weeklies).

**Flyer Review type: Medium.** Confirm 4 runs/week (2 hosted, 2 Flipp), correct availability toggles, avail Thu–Thu / valid Fri–Thu, external run name present, no theme (unless Black Friday), linking doc attached, leg heights set, Item Image QC complete, custom tiles applied, item count meets content policy (avg 3+ items/page), prominent logo on page 1, no outstanding sessions/tasks, no geography changes, UTMs correct per run type.

---
*Source: Tepperman's OneGuide (Google Doc `1TopC05KCtwPfSYUC05-p7MnPsoTPK0IA_2A68J7x9qw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
