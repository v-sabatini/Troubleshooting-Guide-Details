# Kent / KentPro — Processing Guide

> **Source:** Kent/KentPro OneGuide (Google Doc `1dHVOfwrLfE57KVrC0hOqbmGAA8dN-4Si3F6hshC8Uwc`), updated Mar 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#kent-building-supply` |
| Hosted URL | kent.ca/en/flyer |
| Flyer type(s) & cadence | **Weekly** flyer · **KentPro Monthly** (clone of Kent into the KentPRO retailer) |
| Processing | Auto-stack |
| Who's involved | Flex (Setup, Image QC, FAB tickets); DOC (FQC, category/URL/SKU QC); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

### Weekly
- **Files received:** Friday.
- **Publication cadence:** Available Wednesday → Tuesday; Valid Thursday → Thursday.
- **Preview:** 1-day consumer preview (Wednesday); 2-day merchant preview (Monday).

### Monthly (KentPro)
- **Files received:** Monday.
- **Publication cadence:** Available Friday → Monday; Valid Wednesday → Tuesday.

## ⚠️ Risk items
- **Valid dates:** page/item-level overrides are frequently missed.
- **Sales story** frequently missing.
- **URLs** often go to the correct item but the **wrong colour**.
- **Original price:** watch the original price field — description reads "Was: $$$" / "After flyer price: $$$".
- **Link callouts:** box and tag all "buttons" for Financing, Online-Only Deals, and E-Newsletter flaps with the links in the linking document.
- **SKU:** if multiple SKUs are listed (e.g. `6732406, 401`), include **only the first** (`6732406`).

## Upload & setup (owned by Flex)

### FTP transfer
- Kent sends files to their **external FTP**. Log into the FTP agent (FileZilla/CoreFTP), download Kent's weekly files, then connect to Flipp's FTP and upload them. (See the Kent Processing Notes doc for external FTP access.)

### Codesheet upload
- Download the Digital Plating Document (email); open a Generic Code Sheet Template; copy all page PDFs from the Digital Plating Document → paste as values into the generic codesheet and update store sets.
  - **DPT zones:** `11zones_DPT_NB`, `11zones_DPT_NS` (or `*DPT_NS_WITHMETRO` if a METRO PZ is in the digital plating), `11zones_DPT_PEI` (only if no DPT PEI PZ listed).
  - **COM zones:** `11zones_COM_NB`, `11zones_COM_NS`, `11zones_COM_PEI` (only if no COM PEI PZ listed).
  - **COM BIL zones:** `11zones_COM_BIL`, `11zones_EDM_BIL` (only if no EDM BIL PZ listed).
- Copy pagination into FR zones (same steps); download as .csv.
- Codesheets: choose file, **config name `generic_language`**, path from FTP, **toggles 1, 3, 4, 6**.
- Download the links document; once codesheets/sessions complete, attach the linking document to all vendor tasks.

### Setup QC
- Dates correct; 1-day consumer preview (Wednesday); 2-day merchant preview (Monday); not hidden anywhere; no theme; pages correct. Note "Setup QC complete, Linking document attached".

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF weekly / ON monthly; linking doc required)
- **Include** packaged deals, special weblinks (monthly also includes retailer logo, sign-up page, social media). **Exclude** coupons, retailer logo (weekly), sign-up page (weekly), social media (weekly).
- Box all items with prices or sale stories separately (draw text boxes when needed; match text boxes to image boxes — often several versions in one promotion). Box all **link callouts** for Financing, Online-Only Deals, and E-Newsletter ("Click Here to Apply", "Yes, Sign Me Up", "Shop Now").

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude** disclaimer.
- **Name/Brand/Description:** as in flyer; if no description on the flyer, tag as in the spreadsheet; do not include SKU in the description.
- **Price/Original Price:** as in flyer; if none, use the spreadsheet; **original price is at the end of the description after "was"**.
- **Pre/Postfix:** as in flyer; when EN+FR on the page, English postfix is listed first, French second.
- **SKU:** listed in brackets at the end of each item's description; if none, use the spreadsheet; **only the first SKU** if multiple.
- **Valid dates:** enter override dates if applicable.
- **URLs:** if the spreadsheet has prices, use it; otherwise search the SKU on kent.ca, open the item, copy the URL (correct language for EN/FR); tag all linking-doc links to the callouts on the indicated pages.
- **Sale Story:** generally in a red/yellow banner above the price; on FR pages use French text, but where only English exists (e.g. "Save $150") use the English sale story.
- **Disclaimer:** only if within the drawn box.

### Image QC
- Only select the extracted image that best applies; if no clean images, use the cutout.

## Post-processing / FQC (owned by DOC)
- **Item Category QC:** every item needs a category — use the Kent category matrix (Christmas, In Season, Lighting, Household, Tools & Hardware, Lawn & Garden, Furniture, Roofing, Kitchen, Paint/Stain, Home Décor, Decks, Siding, Heating, Flooring, Bathroom, Building Supplies, Windows).
- **URL/Links QC:** open the linking doc; item search URL IS BLANK + Language English → fill blanks (leave blank if the doc has no link); repeat for French; use Page Grouping Index and SKU filters to edit matching items across versions at once.
- **SKU QC / FQC:** Item Image QC (cutouts/no-images/unreviewed only); Standard 4 thumbnails; categories; Overview → Item check that OS didn't tag multiple SKUs (**SKU CONTAINS ","**); Link QC (item search URL IS BLANK, careful of EN vs FR links — use Page Grouping + Language filters).
- **Flyer sorting:** Current Weekly → Upcoming Weekly → Kent Look Books/Catalogs → **KentPRO publications always last** (Monthly, then any Look Books/Catalogs).
- **Flyer Review type: Lite** (owned by Flex).

## Out-of-processing — KentPro process
- Clone weekly Kent flyers into the **KentPRO** retailer; name "Week __ [KentPro]" once URL corrections are done.
- Edit Details: **Hidden in Flipp/Distro**.
- Add stores (rerun codesheet & process — "Page Already Uploaded" errors are OK); reassign by store sets.
- **Change links to kentpro.ca:** Overview → Special Actions → Style Guide Rules → Apply Rules; verify via item search "URL contains kent.ca".
- **KentPRO flyer sorting:** KentPRO publications first (Monthly, then Look Books/Catalogs) → Kent Weekly → Kent Look Books/Catalogs.
- **Monthly:** after FQC, clone to the "KentPro Monthly" flyer type; change toggles on the clone to available everywhere; add stores.

---
*Source: Kent/KentPro OneGuide (Google Doc `1dHVOfwrLfE57KVrC0hOqbmGAA8dN-4Si3F6hshC8Uwc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
