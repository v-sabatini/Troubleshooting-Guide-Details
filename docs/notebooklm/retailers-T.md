# Retailer Processing Guides — T

> Bundle of 21 retailer-specific processing guides (T). Contacts and credentials are omitted from every guide.

**Contains:** T&T Supermarket, TA Appliances, Target USA, Tbaytel, Teletime, Tepperman's, The Brick, The Flooring Warehouse, The Grocery People, The Medicine Shoppe, The Paint Shop, The Sleep Factory, The Source, Thrifty Foods (Sobeys), Timber Mart, Tractor Supply Company USA, Trail Appliance SK/AB, Trail Appliance (BC Flyer), Trevi, Tropicazoo, True Value


---

# T&T Supermarket — Processing Guide

> **Source:** T&T Supermarkets OneGuide (Google Doc `1EUrSSpTCTBQ9B59qpQsiC36zpfzgL9MLd7eLFcXFJJg`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified) |
| Availability | All platforms |
| Slack channels | `#hosted-tnt` |
| Hosted URL | tntsupermarket.com |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | **Trim Stack** |
| Who's involved | Vendor upload/setup; DOC FQC; no Flex; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Wednesday, usually near EOD.
- **Publication cadence:** Available/Valid Friday → Thursday.
- **Preview date:** Friday.
- **Linking documents:** 3 uploaded to FTP — **AB, BC** and **ER**.

### ⚠️ Common errors / risk items
- **Rewards pages:** one box for the whole page, tagged with the correct link from the matching link sheet.
- **Flyer not ready by Friday:** set up a **FLYER COMING SOON** placeholder. Notify DOC & DOL. Reuse the coming-soon run (flyer run 979420); adjust its available/valid dates. Set its available/valid-to time to when the real run is expected live, and adjust the real run's dates/times too.

## Upload & setup (owned by Flex)

- **NEW 2026 — Set Pixel Height to 4096 BEFORE uploading any pages.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → 4096.0 pixels → OK. If pages were already added, flag the Full-Time Ops stakeholder and continue.
- **Manual upload:** pages are submitted Wed afternoon–EOD, referencing **WR** and **ER** pages (sometimes sent separately).
  - **WR** pages → Alberta (**AB**) and British Columbia (**BC**) zones.
  - **ER** pages → Saint Laurent/Quebec (**SL**), GTA, Promenade Mall (**PR**), Ottawa (**OW**), Waterloo (**WL**) zones.
  - Best to wait for all zones' pages before uploading.
- Pages → Edit → select all pages from the most recent folder (open each folder icon so FAdmin grabs all pages). Rename each page so its target Pricing Zone prefixes the name.
- Some **Poster**/**Reward** pages only say "ER"/"WR"/"GTA": you need one per WR region (AB, BC) and per ER region (GTA, OW, WL). SL is the only French region and always gets its own version. If only one ER/WR page is included, upload multiple copies and assign each to a region, renaming accordingly.
- **IMPORTANT:** toggle **all SL pages to French**, Save, then confirm toggles saved or you must reupload in a new track.
- Grouping optional (page 1s = 1, page 2s = 2, etc.; SEA pages = 4, Rewards = 5, PR = 6). Save and Complete.
- **Flyer creation — 6 pricing zones:** AB (Eng), BC (Eng), GTA (Eng), OW (Eng), WL (Eng), SL (French). Page order: positions 1/2/3 = pages 1/2/3; position 4 = SEA/FnV insert; position 5 = Rewards (position 6 for PR zone).
- **Assign stores** via generic codesheet upload (save the codesheet CSV from the previous run). After FSA Generation session, Geography tab should read **No Stores or FSAs/zips were added or removed!**

### Setup QC (owned by DOC)
- Edit Details: no consumer preview; Available/Valid Friday → Thursday; Hide on Distribution and Hosted; no theme.
- Thumbnails Standard 4 (1065 x 600, stock premium, storefront carousel, storefront organic).
- **Vendor tasks — IMPORTANT:** mass-attach ALL URL documents to EVERY vendor task (English and French). Add the note: all items get the same link; reward pages get one link per page; no SKUs; AB doc → AB pages, BC doc → BC pages; ER doc → WL tab for WL, GTA tab for GTA, OW tab for OW, SL tab for SL. Refresh to confirm the note saved to every task.
- File an Urgent Processing Ticket.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc Tag/QC-specific — continue if not attached)**
- Include: coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Draw a box where there's a unique price or a sale story (e.g. 10% OFF). **If an item has a "?" question mark as the image, do NOT box.**
- Posters (e.g. Rewards pages) embedded in the flyer must be tagged as a direct-link display type — URL from "Other Posters" in the item list.

**Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. No brand.
- **Name:** ALL CAPS, format "Brand Product Name, Quantity" (always a comma before quantity, e.g. 60g, 1lb, bunch, pkg of 24). Do NOT include "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — put those in the description.
- **Valid dates:** only apply date overrides when a related promo sale story is present on the item.
- **SKU:** use the "Item Number" column in the linking document.
- **Description:** first letter of first word capitalized; include "Product of…" here. **Categories:** every item needs Google + analytics categories. **Disclaimer:** noted under "remarks" in the link doc.

**Image QC:** select the cleanest PDF; if none, use the relevant cutout.

## Final QC / go-live notes (owned by DOC)

- **Upload category pages:** download the 2 category pages (ENG & FR) from the previous run or from the VTB Drive folder; upload to the current run (correct language each). After upload, delete the auto-boxed boxes (wait until Box QC is enabled to avoid a FAdmin pipeline error). Copy items from the previous run's category pages (Pages → Copy Items; match languages). Layout: add category page as last page (position 99) to all English and French zones.
- Mark Autostack Spotcheck complete. Edit Details: Available/Valid Friday → Thursday; hidden on Distribution and Hosted; no external run name; no theme.
- Complete Item Image QC (PDF where possible, cutouts otherwise). Leg heights 40/30; Standard 4 thumbnails.
- Pages: check outstanding QC; confirm Poster/Reward pages boxed & tagged (add missing links from URL docs if a page shows 0 items); no Page 1 has a category.
- Confirm stores assigned; sessions run correctly and links verified; Geography: **No Stores or FSAs/zips added or removed!**
- **Live-date risk items:** valid dates of Books/Movies/Music (available date often differs from flyer; dates at top of page); description must match page exactly.
- **Flyer Review type: Lite.**

---
*Source: T&T Supermarket OneGuide (Google Doc `1EUrSSpTCTBQ9B59qpQsiC36zpfzgL9MLd7eLFcXFJJg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# TA Appliances — Processing Guide

> **Source:** TA Appliances OneGuide (Google Doc `1mzUF_sxe_LLBeS0MDTNlbgE-aLiU9HAJOJOlS-LoqvU`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Flyer Type 1 — Ad-hoc (Flyer Type #4738) |
| Processing | Auto-stack |
| Who's involved | Vendor upload/setup; DOC FQC; Flex Processing Support + Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Publication cadence:** Available/Valid Tuesday → Tuesday.
- **Linking document:** N/A.

### ⚠️ Risk items
- Look for multiple products (box each product individually).

## Upload & setup (owned by Vendor)

- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- Files uploaded to the SFTP; pages manually uploaded to the flyer run.
- **1 PZ, English only.** Add all stores. Attach linking document to vendor tasks.

### Setup QC
- Thumbnails Standard 4. No theme. External run name = file name / PDF.
- **Valid dates should match dates on page 1.** No sub pages need to be drawn.

## QC specifics

**Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)**
- Include: packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude: coupons.
- Box each item with a price.

**Tag / Tag QC (Low; Auto-tag OFF; no linking doc)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. Brand used for both Box/Tag. (SKU not tagged.)
- Enter brand if applicable; item name as listed in flyer.
- **URL:** tag from the linking document. If a box has a savings offer (% or $ amount), set Display Type = ITEM. If no linking document attached, no URL required.

## Final QC / go-live notes (owned by DOC)

- **Pre-FQC:** confirm dates vs PDF; toggles available on all platforms; thumbnails drawn and include retailer logo. Standard checks: all items boxed/tagged; previews published/clickable; geography correct.
- **FQC:** QC thumbnails — draw "thumbnail 1065x600" (2 pages), "storefront carousel premium" (2 pages), "storefront carousel organic" (1 page). Pages: at least 1 category unless first page or no products. All items boxed & tagged. Item search for items without URL (URL IS BLANK) — update from the doc if needed. Geography: no changes week over week.
- **Flyer Review type:** owned by Vendor (see the TA Appliances 4337/4738 Flyer Review Guide).

---
*Source: TA Appliances OneGuide (Google Doc `1mzUF_sxe_LLBeS0MDTNlbgE-aLiU9HAJOJOlS-LoqvU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Target USA — Processing Guide

> **Source:** Target USA OneGuide (Google Doc `1m3ksvWvVVnqCPrezgSm9kb3IEjxwyU1cZer03jXy5A4`), updated Jun 29, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (hidden in Hosted) |
| Slack channels | `#target` |
| Flyer type(s) & cadence | Weekly Circular — Flyer Type #381 |
| Processing | Auto-stack |
| Who's involved | Vendor setup; OS setup; DOC FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available/Valid Sunday → Saturday.

### ⚠️ Common errors / risk items
- **Valid dates of Books, Movies, and Music:** the available date often differs from the flyer; item valid dates are indicated at the top of the page (e.g. "All movies available March 1st, Books available March 4th").
- **Description:** enter exactly as it appears on the page — a recurring true error.
- Look for multiple products (box separately).

## Upload & setup (owned by Flex)

- **File uploads:** download files from Target USA cloud Windows servers (access provided by the client). If revisions arrive 3–4 days before FQC, sub them into the original content file so OS can process at once. Use an FTP program (Core FTP, FileZilla, etc.).
- **Upload NEW store sets:** clear out all existing store sets in the Store Sets section of Merchant first.
- **Codesheet manipulations (Weekly):** copy only the PDF column to the last Pricing Zone (AK) and page row into a new Excel; save as CSV. Do **not** include the Lettered Ecomm Insert pages (those are uploaded manually if present).
- **Codesheet upload:** Config name = **`target_usa`**; PDF Base Directory from SFTP; toggle **Everything except 2nd & last**; **no Region Assignment or Combine Zones**.
- **Manually upload the Lettered Insert pages** — not in the codesheet; add them during FQC.

### Setup QC (owned by Flex)
- Geography; vendors assigned; sessions running.
- Edit Details: Key Messages Main = "Target Deals"; dates correct; Available = **Hidden in Hosted**; no theme.
- Leg heights preset 60/40. Thumbnails Standard 4. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON)**
- Include: packaged deals, sign-up page, special weblinks. Exclude: coupons, retailer logo, social media.
- Box every item with a price/discount. For items inside a larger image, box the individual product then draw a **text box** around its price/description.
- **Multiple products, one price:** box each product separately (e.g. two different water brands boxed separately = correct; Starbucks + Snapple boxed together = incorrect). Text boxes around each product's name/description.
- **Inserts:** box any call-to-action links; box the entire insert page if a link is present and there are no individual priced items.

**Tag / Tag QC (Low; Auto-tag OFF)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Brand is Box-specific.

**Image QC:** clean PDFs if available, cutouts fine otherwise.

## Final QC / go-live notes (owned by DOC)

- Spotchecks. **Add REV pages:** download from the folder provided by the client contact and upload; prefix with REV 1, REV 2, REV 3, etc. depending on version.
- **Add Lettered pages** per the original email: some go to all PZs (e.g. `pceomal` — "al" = all PZs), some are PZ-specific (e.g. `pgcomhi` — "hi" = that PZ). See instructions video (from 5:20).
- Create a Jira ticket for inserts (example OPSMR ticket in the OneGuide). Check geography; all vendor tasks complete; sessions rerun if needed. Pricing Zone tab horizontal/vertical view. No-page category check. Verify REV pages reflect the client's email.
- Edit Details: dates Sunday → Saturday; Available = Hidden in Hosted; no theme; Key Messages Main = Target Deals. Leg heights preset 60/40; thumbnails Standard 4; Image QC = clean PDFs if available, otherwise cutouts.
- **Flyer Review type: Lite.**
- **Out-of-processing:** pre-live page swap (gather files, then swap) — see videos.

---
*Source: Target USA OneGuide (Google Doc `1m3ksvWvVVnqCPrezgSm9kb3IEjxwyU1cZer03jXy5A4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Tbaytel — Processing Guide

> **Source:** Tbaytel OneGuide (Google Doc `171McxQPaC0tnEUuNWkR9pAH5y6URhtmuFLVzI4OOCkw`), updated Jun 22, 2026. Contacts/credentials omitted.

Retailer has been inactive since before the current owners took on the account; some details are sparse accordingly.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only (not on our Hosted) |
| Slack channels | `#tbaytel`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer Type 1 — Ad-hoc |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup & FQC; Flex Processing Support + Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad hoc.
- **Publication cadence:** Ad hoc (available/valid all ad hoc).
- **Preview date:** N/A.
- **Linking document:** Yes, for URLs.

## Upload & setup (owned by DOC)

- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-group or manually add page numbers; ensure correct language. Save & Confirm — **do NOT Process Internally.**
- **Pricing zone creation:** usually only 1 PZ. Tbaytel is **FSA-based.** Refer to the email for which region set to use (usually referenced by exact name); if not stated, follow up with the retailer to confirm distribution.
- **Linking document:** URLs for each run live in the FAdmin SFTP (Tbaytel merchant page → Details → FTP path → View Files). Download it; upload by selecting a vendor track, ensuring "Mass Attachment" is checked, and adding the file.

### Setup QC
- Confirm all pages uploaded (Pricing Zone tab → Items View). **RISK:** if uploading from SFTP, confirm no pages in the SFTP remain un-uploaded.
- Confirm flyer dates (usually first or last page). Thumbnails Standard 4. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both Box/Tag — use the Excel as reference for what to box)**
- Include: special weblinks. Exclude: coupons, packaged deals, retailer logo, sign-up page, social media.
- Use an item box for the product and a **text box** for text when the product and text aren't easily boxed together (e.g. iPhone images across from their texts).
- Box all callouts/links/banners and reference the spreadsheet for URLs. Follow the Excel for what should/shouldn't be boxed.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box/Tag)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** No brand.
- **Name:** full product name from text extraction (e.g. "iPhone 12 Pro Max – 128GB").
- **Current Price:** the cost per month.
- **Postfix:** the "/month for 24 months, taxes extra, $0 down, 0% APR" callout or "On a 2-year term with any Basic Plan" (no prefix).
- **Original Price:** the "Regular: $____" price.
- **Description:** include GB amount, "$0 down, 0% APR", monthly payment info, device full-price info.
- **Categories:** Google category = Mobile Phones or Mobile Phone Accessories.
- **Sale Story:** the savings callout with SimplePay (e.g. "Save $519.00 with SimplePay").
- **URLs:** provided by retailer as an Excel, laid out by page. If there are no products, tag as a **LINK** instead of ITEM.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## Final QC / go-live notes (owned by Vendor)

- **Pre-FQC:** dates vs PDF; availability toggles; thumbnails include retailer logo. Standard checks: all items boxed/tagged; spotchecks (20% of PZs); previews published/clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** — flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Tbaytel OneGuide (Google Doc `171McxQPaC0tnEUuNWkR9pAH5y6URhtmuFLVzI4OOCkw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Teletime — Processing Guide

> **Source:** Teletime OneGuide (Google Doc `1rsHd4-GZymqVX5dg-9uNa9FSl2zka1rFR98eFyYtyVo`), updated Jul 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified) |
| Availability | All platforms |
| Slack channels | `#helpme-customersuccess`, `#flex-processingsupport`, `#flexflyerreview`, `#teletime` |
| Flyer type(s) & cadence | Flyer Type 1 — Flyer (Ad hoc) |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup & FQC; Flex Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad Hoc.
- **Publication cadence:** Ad hoc (available/valid all ad hoc).
- **Linking document:** Ad hoc.

### ⚠️ Common errors / risk items
- **Late files:** files are sent late, so Available dates likely need adjusting. They're often not listed on the PDF — leave a comment flagging that the dates won't match.

## Upload & setup (owned by Flex)

- **Manual upload:** Pages → Edit → select all pages from the SFTP menu (files are labelled to match the internal run name). Confirm & Upload. Auto-group or manually add page numbers; ensure correct language. Save & Confirm — **do NOT Process Internally.**
- **Pricing zone creation:** create a Base pricing zone, select all applicable pages, Save & Confirm, add all applicable stores.

### Setup QC
- Confirm all pages uploaded (Pricing Zone tab → Items View). **RISK:** if uploading from SFTP, confirm no SFTP pages remain un-uploaded.
- Confirm flyer dates (usually first or last page). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box OFF — pages often not in a grid; Box QC bot ON)**
- Exclude: coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

**Tag / Tag QC (Low; Auto-tag OFF)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Brand is Tag/QC-specific.
- **No linking document by default.** Vendor task notes may be updated if the retailer wants one URL applied to all items. If there's no link doc or note, **OK to proceed** with processing.
- Each item boxed separately despite "one-to-all" pricing/messaging. No price listed is OK.

**Spotchecks:** standard pricing spotchecks included in pipeline.

## Final QC / go-live notes (owned by DOC)

- **Pre-FQC:** confirm dates vs PDF — **if files are sent late, Available From dates will not match valid; a comment should be left, otherwise confirm with the account team.** Confirm availability toggles; thumbnails include retailer logo. Standard checks: all items boxed/tagged; spotchecks (20% of PZs); previews published/clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** — flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Teletime OneGuide (Google Doc `1rsHd4-GZymqVX5dg-9uNa9FSl2zka1rFR98eFyYtyVo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

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

---

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

---

# The Flooring Warehouse — Processing Guide

> **Source:** Ritchie's & The Flooring Warehouse OneGuide (Google Doc `1205hxKGwxGXJ4Bu9uczlVOwYLEFZY2RZAmsAPxCTPAc`), updated Nov 25, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1p-ritchies-and-the-flooring-warehouse` |
| Hosted URL | TBC |
| Flyer types | Flyer (12160) — The Flooring Warehouse (6816); Ritchie's is Flyer 12161 (6815) |
| Processing | Auto-stack; Flex (Processing Support); no coupons, no Feedel |

> **Note:** Ritchie's (6815) and The Flooring Warehouse (6816) are **processed exactly the same and share the same flyer — the only difference is the logo.**

## Files & schedule
- **When files arrive:** ad hoc.
- **Publication cadence:** Available From / Valid From Friday; Available To / Valid To Thursday. **Always double-check the flyer dates on the PDF; if unsure, email the client to confirm.**
- **Linking document:** N/A. **Processing type:** Auto-stack.

## Upload & setup (owned by DOC)
1. Manually upload the pages: **Pages → Edit → Upload Local Files**, select the two pages.
2. Index pages and ensure they're in order.
3. Make sure language is **ENGLISH only**.
4. Save + Save & Complete.
5. Create a **Base pricing zone** for all pages.
6. Add All Stores.
- Complete Setup QC in the pipeline.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price.
- **Exclude:** URLs. Brand not used.

## Post-processing / FQC (owned by Flex)
- Standard 4 thumbnails.
- **Not available in hosted.**
- Complete FQC checklist in Fadmin.

## Flyer Review (owned by Flex)
- **Flyer Review type: Lite.**

---
*Source: The Flooring Warehouse OneGuide (Google Doc `1205hxKGwxGXJ4Bu9uczlVOwYLEFZY2RZAmsAPxCTPAc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# The Grocery People — Processing Guide

> **Source:** The Grocery People OneGuide (Google Doc `1aZek4ch2DbXrECkasLSiTpmnjBhIRolxEd8Jmhpm0Fk`), updated Nov 11, 2025. Contacts/credentials omitted.

Two flyers on one flyer type (**3789**): **Weekly** (codesheet upload) and **Wholesale Market** (manual upload).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#thegrocerypeople` |
| Hosted URL | (Hosted only) |
| Flyer type(s) & cadence | Weekly (+ occasional ad-hocs) and Wholesale Market; Flyer Type 3789 |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup; Vendor FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Cadence — Weekly & Wholesale:** Available Wednesday → Wednesday; Valid Thursday → Wednesday.
- **Linking document:** Weekly generally gets one; Wholesale Market generally does not (see Setup QC).

## Upload & setup (owned by Vendor/DOC)

### Weekly (codesheet upload)
- Email notification that files dropped in the SFTP ("Flipp On Line MediaRun List Ad[#] [Year].xlsx").
- **Codesheet manipulations** (best learned via the upload video):
  1. Copy from cell E5 (File Name) to Q5 (Store Ad Stop Date), down to the bottom text row.
  2. Paste special (values only) into a new tab; delete the two "If Statement" columns (J and K).
  3. Format Store Ad Start/End Date columns (L, M) as MM/DD/YYYY; format Acct column (B) as Automatic.
  4. In column A, Find & Replace "_#" with "_AD_#" (e.g. "_21" → "_AD_21"); file name becomes `TGP_AD_21_AA`.
  5. Insert a column right of F; in B2 enter `=CONCAT(A2," FLIPP")`; apply to all rows.
  6. Copy the filled cells from B2 down; paste special (values only) into A2.
  7. Save the tab as `.csv` and upload — **Config name: `the_grocery_people`**; PDF base directory; **uncheck region and combine zones**.

### Wholesale Market (manual upload)
- Retailer contact provides a 4-page flyer plus 2 unique versions of page 1. Before a new month, you also get 2 Commercial pages (upload with the others only if this is the first publication of the month; otherwise add them Pre-FQC and copy items from the previous run).
- Upload all lowercase-folder pages plus the two PZ-specific cover pages (Lloyd and HP) from the uppercase folder.
- **Flyer creation — 3 pricing zones:** "Wholesale Market" (all lowercase pages + both Commercial pages if applicable), "Lloyd" (Lloyd cover as page 1, then pages 2–4), "HP" (HP cover as page 1, then pages 2–4).
- **Assign 1 store per PZ** (per the distribution doc): Wholesale Market = code **1984**; Lloyd = code **872** ("Cash and Carry"); HP = code **10453** ("High Prairie Super A Foods").
- Holiday-specific Wholesale content (e.g. Ramadan): one Base PZ with all Wholesale stores (1984, 872, 10453), use PDF dates, no links generally sent.
- **FSA generation error?** Check the Pricing Zone tab — if zones exist but no stores are assigned, add stores (task reruns automatically); if zones weren't created, rerun Flyer Creation and create the 3 zones.

### Setup QC (both flyers)
- Attach the linking document, or comment "no linking doc this week" (OS won't tag otherwise). Wholesale Market generally has no linking doc. Weekly usually gets one — but open it first; if blank, comment that there's no linking doc.
- Geography same WOW (compare to the right flyer type). Edit Details: one-day consumer preview; Available everywhere; Weekly no external run name; Wholesale Market external run name "Wholesale Market". Standard 4 thumbnails; leg heights preset 40/20.
- **IMPORTANT (Weekly):** a staggered-dates warning appears in red under Platform Availability — click it, select all PZs, and set the Available From date to the one-day consumer preview (Wednesday).

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc Box-specific — sometimes)**
- Include: special weblinks. Exclude: coupons, packaged deals, retailer logo, sign-up page, social media.
- Box all priced items; text boxes only when necessary. Box callout/contest blocks. Box & tag social icons (Facebook `facebook.com/TGPGrocer/`, Instagram `instagram.com/tgpgrocer/`).

**Tag / Tag QC — Tag Lite retailer (Low; Auto-tag OFF; linking doc Tag-specific)**
- **Do NOT tag Name, Brand, Description, SKU, Sale Story.** Include: pre/postfix, valid dates, price, categories, disclaimer, original price, URLs.
- **Meat/Produce price-per-KG:** where a price is preceded by a number + KG, enter `$###KG` into the **SKU and description** fields (only when the number+KG is in the price box, not the description); the per-pound price is the current price.
- **Valid dates:** tag only if item dates differ from the flyer's (e.g. green-bordered "SAVE — Stock up on Savings!" pages at the end have overriding dates).
- Categories are required for all items (see chart: Floral = Flowers; Grocery = everything else; Meat = non-packaged meats; Produce = fresh fruit/veg).

**Image QC:** select an image for ALL items, PDF where possible; if there are black/grainy shadows, default to the **cutout**.

## Final QC / go-live notes

- Mark Autostack Spotcheck complete. Edit Details (per Setup QC dates/preview/external-name rules). Leg heights 40/20; Standard 4 thumbnails; Item Image QC done by OS.
- **Staggered-dates error** under Platform Availability → click the red text → select all zones → set Available From = Wednesday (so the preview applies at the PZ level).
- Pages: all items QC'd; all linking-doc links added. Pricing Zone: horizontal/vertical + item-view check (watch for 3-Day Sale items — update their valid dates). Sessions: verify links. Geography: no stores/FSAs added/removed (compare same run type).
- **Wholesale Market unique step:** first run of a new month has 2 Commercial pages — confirm both are in the "Wholesale Market" PZ only. If not uploaded, download the relevant commercial pages from the SFTP (lowercase, `_p000#.pdf`), upload manually, copy items from the previous Wholesale run, then add them to the end of the Wholesale Market PZ (positions 5 & 6) and Verify URLs.
- Complete FQC checklist (ignore the "not all categories… have thumbnails" warning).
- **Flyer Review type: Lite.**
- **Out-of-processing:** page swaps (Weekly & Wholesale); Triggers & OPTICS ticket creation for monthly Wholesale Commercial pages; updating the external flyer link sheet ("TGP Direct Links") — create new runs, input IDs in Column D, confirm, send the link to the requesting contact.

---
*Source: The Grocery People OneGuide (Google Doc `1aZek4ch2DbXrECkasLSiTpmnjBhIRolxEd8Jmhpm0Fk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# The Medicine Shoppe — Processing Guide

> **Source:** The Medicine Shoppe OneGuide (Google Doc `1BjxJpALLVFWJGpFSzQRfcoy9UA3tBg0-Gxz9_mz4JbM`). Contacts/credentials omitted.

Serviced via McKesson. Monthly publication.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channels | `#mckesson` |
| Hosted URL | medicineshoppe.ca/en/flyer |
| Flyer type(s) & cadence | Flyer Type 1 — Flyer / **Monthly** content (ad-hoc file drops) |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup & FQC; OS setup; Flex Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad-hoc.
- **Publication cadence:** Available From Monday; Valid From Tuesday. **Monthly** — dates run first of the month to end of the month.
- **Preview date:** none.
- **Linking document:** N/A.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages → Edit → select that month's folder (e.g. August) → select all files → auto-group → Save and Next.
- Once flyer creation is enabled, create the PZ named **"Base"** and add all stores.
- No linking document. Apply **"No Theme."** Finish Setup QC.
- **Setup QC:** it's a monthly publication — make sure the dates are first of the month to end of the month.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; no linking doc)**
- Include: retailer logo, sign-up page, social media, special weblinks. Exclude: coupons, packaged deals.

**Tag / Tag QC (Low; Auto-tag ON; no linking doc)**
- Include: name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude valid dates and URLs.** Brand is Box-specific.

## Final QC / go-live notes (owned by DOC)

- QC thumbnails: Standard 4. Legibility heights 85/65. **No item image QC. No category.** Finish FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: The Medicine Shoppe OneGuide (Google Doc `1BjxJpALLVFWJGpFSzQRfcoy9UA3tBg0-Gxz9_mz4JbM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# The Paint Shop — Processing Guide

> **Source:** The Paint Shop OneGuide (Google Doc `1GR5fSHqhwR7fxkG-E9GmJwKOLUXHSEOyqiS8YWrjdRk`), updated May 29, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#thepaintshop` |
| Flyer type(s) & cadence | Ad Hoc / Monthly |
| Processing | Auto-stack |
| Who's involved | Flex setup (DSP upload support); OS setup + FQC; Flex Image QC & Flyer Review; DOC FQC; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available From Monday; Valid From Tuesday.
- **Linking document:** Yes (attached as XLS from the FTP).

## Upload & setup (owned by Flex — receives DSP upload support)

- **Manual page upload — 3 zones.** Add stores via store sets:
  - V01 → Newfoundland
  - V02 → Labrador
  - V03 → Maritimes
  - Refer to prior flyer runs for which pages get assigned.
- **Attach the linking document (XLS from FTP) to all vendor tasks.**

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc Box-specific)**
- Include: packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude: coupons.
- Box each item with a price. If a product has different sizes/colours, box individually and use text boxes. Box retailer logo and special weblinks.

**Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking doc Tag-specific)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.** Brand is Box-specific.

**Item Image QC (DOC):** clean PDFs if available, cutouts OK otherwise.

## Final QC / go-live notes (owned by DOC)

- **Basic FQC:** Standard 4 thumbnails. Overview → Edit Details: no theme, no external run name, no toggles. Verify live dates using the dates in the linking document attached to all vendor tasks.
- **Content policy check:** a publication 1–3 pages long must have at least **6 shoppable products**; a publication greater than 3 pages must average **3 products per page**.
- **Flyer Review type: Lite** (see The Paint Shop Flex Flyer Review guide).

---
*Source: The Paint Shop OneGuide (Google Doc `1GR5fSHqhwR7fxkG-E9GmJwKOLUXHSEOyqiS8YWrjdRk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# The Sleep Factory — Processing Guide

> **Source:** The Sleep Factory OneGuide (Google Doc `19hkBQHXebTmQ1erBF80fQ3wv4hDZJ27s2oPgzcOEJLY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channel(s) | `#sleepfactory` |
| Hosted URL | https://www.sleepfactory.com/ |
| Flyer type(s) & cadence | Catalogue — monthly (ad-hoc; retailer emails exact dates, no schedule pre-set in Fadmin) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Thursday (weekly cadence noted); publications run monthly ad-hoc.
- **Publication cadence:** Available From Monday · Valid From Sunday.
- **Linking document:** Yes — product-links `.xlsx` downloaded from the FTP.
- **Workflow:** Upload & Setup (Vendor) → FQC (DOC/`flex-sortd`).

## Upload & setup (manual, OS)

- Manually upload all pages for the month; **auto-group pages**.
- Create **one pricing zone called `BASE`** containing all pages.
- **Store assignment:** download the codesheet from the FTP, open the CSV, and assign only the stores it lists.
- **Linking document:** download the product-links `.xlsx` from the FTP and attach it to all vendor tasks.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking document required. **Exclude** coupons, packaged deals (e.g. washers/dryers), retailer logo, sign-up page, social media, special weblinks. Box each item — including different sizes — **together**; different sizes of the same item are **not** boxed separately. Do not box stores or banners.
- **Tag / Tag QC (Low; Auto-tag OFF):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. PDF image auto-selection ON.
- **Image QC:** prioritize PDF images unless not clean (shadows/black backgrounds).

## FQC (PSS)

- Autostack; re-run sessions if there are warnings; confirm vendor tasks complete; check geography.
- Leg heights **60/40**; thumbnail **Standard 4**.
- Open the linking document and spotcheck a few items (at least one item from 3 pages) — name & link match.
- Page categories: **no category on page 1**, one category on the rest. No item category QC. Mark item image QC complete.
- Dates: check FTP > codesheet, or refer to email. Usually **no preview**; **hide in hosted**; no external name; no theme (or per Theme Brief).

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: The Sleep Factory OneGuide (Google Doc `19hkBQHXebTmQ1erBF80fQ3wv4hDZJ27s2oPgzcOEJLY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# The Source — Processing Guide

> **Source:** The Source OneGuide (Google Doc `1W7ipScv6cPpEdADV0bCDFC90BjWFwXW2GlDcVnT7a6w`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel(s) | `#thesource` |
| Flyer type(s) & cadence | Weekly Flyer — ad-hoc schedule |
| Processing | Auto-stack; Flex completes some tasks; OS completes standard tasks |

## Files & schedule

- **Store list** arrives by email (the same document doubles as the codesheet for PDF upload and store distribution). If PDFs arrive without a store list, wait 1 business day then bump the store-list contact.
- **Preview date:** send preview URLs and missing URLs exactly **one week before go-live**.

## Upload & setup

1. Download the store list from email and save as a `.csv`.
2. Upload into Codesheets — **Config name `the_source`**, PDF base directory from the FTP, **toggles 3, 4, 5, 6**. Process Code Sheet.
3. Go to Pricing Zone and rename the pricing zone to **`en`**.
4. Upload the `.xlsx` version of the same codesheet into Codesheets for store distribution — **Config name `the_source_stores`**, PDF base directory `/`, **toggles 1, 4**. Process Code Sheet.
5. Ledge heights **28/18**; thumbnails **Standard 4**; spotlights; Setup QC in pipeline.
6. Overview → Edit Details: available everywhere; preview date 1 week before go-live; theme = no theme unless there is one; key messages = "Weekly Deals" / FR "Aubaines de la semaine".

### ⚠️ Common errors / risk items (retailer-specific)

- **Geography / dealer-direct stores:** geo shouldn't change much week over week; if a store is missing, check whether it closed. The Source also has **"dealer direct" stores** that don't get assigned to flyers — a regular store may have been switched to a dealer store, so cross-reference emails and leave a note in the comments.
- **Disclaimer junk text:** in Item Search, remove stray `seng` and `sfr` strings from disclaimers (typically at the end).
- **Links must use `https://`:** in Item Search, find URLs containing `http:`, export items, find-and-replace `http:` → `https:` (headers `item_id`, `sku`, `url`), re-import via Import Items, and repeat until none remain. Then Sessions → Re-Verify URLs.
- Sometimes a row of phones has no price or sale story — do **not** box/tag unless the retailer emails you to.

## QC specifics

- **Box Draw (Low):** linking document required. **Include** social media, sign-up page, special weblinks, retailer logo, packaged deals; **exclude** coupons. Open the version with the most FSAs to confirm all CTAs and banners are boxed; compare item counts across pricing zones and add/remove boxes if they differ.
- **Tag / Tag QC (Low):** **include** brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories; **exclude** disclaimer and URLs (tagging), though URLs are managed via the `https://` and preview-URL steps.
- **Item Category QC / Item Image QC:** n/a.
- **Categories (Pages → Categories):** search by grouping, enter categories to the first then Copy to Same Index. **No categories on page 1**; cap at **3 categories/page**; for random items (e.g. Fitbit) use "gifts and gadgets".

## Pre-FQC / out-of-processing

- Mark Wayfinding QC and Spotcheck QC complete. Add `utm_campaign` = `monthx` at the Flyer Run level (Manage Tracking Codes → Apply All).
- **Preview URLs:** one week before go-live, send English + French preview URLs (Overview → Preview URLs) plus the "en" pricing-zone vertical preview and the missing-URLs report (Overview → Items without a URL, kept to item ID / page # / item name with a `url` header added). Expect multiple revisions to links/pages.

---
*Source: The Source OneGuide (Google Doc `1W7ipScv6cPpEdADV0bCDFC90BjWFwXW2GlDcVnT7a6w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Thrifty Foods (Sobeys) — Processing Guide

> **Source:** Thrifty Foods OneGuide (Google Doc `1Y6qHHnbuedauneX3OhMoguWmO1fZSsaKtIzB6whaVuI`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · S1C1 (relationship: Good) |
| Availability | All platforms |
| Slack channel(s) | `#sobeys`, `#sobeys-ops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URL | https://www.thriftyfoods.com/ |
| Flyer type(s) & cadence | Weekly Flyer (#774) |
| Processing | Auto-stack; Flex (3FL) owns Upload; Vendor owns Image QC + FQC; Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** Wednesday.
- **Publication cadence** (West-coast timezone): Available From **Wed 3:00 AM** · Available To **Thu 2:59 AM** · Valid From **Thu 3:00 AM** · Valid To **Wed 11:59 PM**.
- **Preview date:** Monday before go-live.
- **Linking document:** linking doc in FTP; **Extract file** sent by email and added to the 3FL Sobeys Google Drive.
- **Workflow:** Upload & Setup (Flex) → Image QC (Vendor) → FQC (Vendor).

## Upload & setup (Flex)

**Before uploading — you need the Extract file.** Do not complete upload without it. It arrives by email to the DOC; if received before upload it is placed in the 3FL Sobeys Google Drive "Thrifty Foods" folder. Download locally and attach to **all vendor tasks**.

1. Pages → Edit → Week → the folder dated for the publication. Select all pages → autogroup → save & complete.
2. From the FTP, download the **zone codesheet** (shows pagination + which linking document). Rearrange pages in the pricing zone per the codesheet.
3. **Pricing zones:** create the zone(s) named in the zone codesheet (one or many). Follow pagination per zone. Note zone 2 can have a unique page and a page removed vs. zone 1.
4. **Adding stores:** use the **Base Run List** (store distribution list) in the 3FL Sobeys Files Drive.
   - Open the generic stores codesheet → **Thrifty Foods** tab. Column A = all stores from the Base Run List; Column B = pricing-zone name. Save as `.csv`.
   - In Fadmin → codesheet, attach the Thrifty Foods generic `.csv`; you'll see "You are using the root path…" → click **OK**. Save & complete, then **Process Codesheet** (should run green). Verify store count = Base Run List count.
5. Wait for sessions to run. Attach **both** the FTP linking document and the Thrifty Foods extract (mass attach → all vendor assignments).
6. Overview → Edit details: theme = **no theme** (unless specified); external run name = `Weekly eFlyer MM/DD - MM/DD`; preview date = following Monday. Key messages (long & short) = "This Week's Deals". Confirm the four dates above.
7. QC thumbnails from page 1 logo: 1065x600 (remove white border, focus pg 1&2), stock premium, storefront carousel premium (pg 1&2), storefront carousel organic (pg 1), thumbnail (pg 1&2), fpt_400w (pg 1). Save & exit.
8. Mark Autostack spotcheck complete (completes the auto-publish task for vertical preview in FQC).

### ⚠️ Common errors / risk items (retailer-specific)

- **Scene+ PTS sale story:** items with a "PTS" callout must have **`Scene+ PTS`** in the sale story — nothing else (not "500 PTS", "500 Scene", "500+ PTS"). Some offers only show points earned; Scene+ still must be tagged in the sale story. Do **not** put Scene+ offers in the disclaimer.
- **Scene+ Member Pricing items:** Prefix = "Scene+ Member Pricing" (**don't forget the `+`**); Disclaimer = "$xx without Scene+ Card"; add category **[Scene+]**.
- **URLs:** high-risk — match links exactly to items via the linking document. When two items share a name, open each URL to confirm which is which (e.g. Yellow Sunlight vs. Blue Purex).
- **Brand:** always enter brand in the brand field **and** at the start of the name field.
- **Base Run List missing** for the week (not in Drive or FTP) → flag to the DOC.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; PDF auto-select ON):** linking document required (used for both box & tag). **Exclude** coupons and packaged deals; **include** retailer logo, sign-up page, social media, special weblinks. Single items: box each priced item separately with text boxes as needed. Multi-items sharing a description: box the item, then a text box for the description, repeating per item.
- **Tag / Tag QC (Low; Auto-tag OFF):** a weekly "Thrifty Foods SKUs" document is attached to Box Draw, Item Tag and Tag QC — use it for SKU and URL (each item has both; SKUs look like `00000_000000000000000000`).
  - **Price:** the standout price (usually /lb or /g) goes in Current Price; the /kg price goes in Description. For produce/meat/seafood the /lb price is main with `lb` postfix; /kg goes in Description.
  - **Sale Story:** all Scene+ / points offers tagged here (see risk items).
  - **Banners:** Grocery → Link, name "Grocery", `mygroceryoffers.ca`; iOS App → Link, name "iOS", App Store URL; Google App → Link, name "Google Play", Play Store URL.
- **Item Category QC (DOC):** category chart — Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, Scene+ (second category when a Scene+ callout is present), Dairy, Deli, Health and Beauty, Seafood. No category for page 1 / links; cap per page.
- **Image QC (Vendor):** prioritize PDF images unless not clean.

## Deep links (new process)

- Check the Sobeys Insert Tracker → **Deep Links** tab for the week's valid dates (dates in **red** get no deep links). Tag the banner/item **as a link** with SKU + link per the tracker.

## Pre-FQC & FQC

- Pre-FQC: QC item categories on Overview (Dairy & Frozen | Meat | Deli & Cheese | Seafood; Floral | Produce | Pet | Bulk Food; Pharmacy | Vitamins & More | Health and Beauty | Baby & Toys; Grocery). Scene+ check across all pages. Description/postfix (/lb main, /kg in description). Re-run page stitching. **Items without a URL must be 0.**
- FQC: legibility height **50/40**; confirm theme = no theme, external run name, and the four dates. **Inserts** (updated Mondays per the West insert tracker): find in the Sobeys FTP by keyword (e.g. "pharmacy"), upload, box each page as one box, tag as Link with the exact tracker name + URL, insert after regular pg 2 per the tracker. The Email Acquisition insert is recurring — pull it from the previous week's run if not in the FTP.
- Flyer sorting: upcoming flyer first, then current.

## Flyer review

- **Flyer Review type: Simple.**

---
*Source: Thrifty Foods OneGuide (Google Doc `1Y6qHHnbuedauneX3OhMoguWmO1fZSsaKtIzB6whaVuI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Timber Mart — Processing Guide

> **Source:** Timber Mart OneGuide (Google Doc `1NQ0Yed95nfbSIN-uN6vG45lVv3bzu6pGXEq-JZ41km0`), updated Mar 13, 2026. Contacts/credentials omitted.

Multiple banners/publications share this account: National Weekly, Lyons, Sherwood, TBMQC, and Quebec (Gabriel Couture / Materiaux Audet).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (plus retailer channel) |
| Publication schedule | weeklyflyer: Weekly · lyons: Bi-Weekly · TBMQC: Bi-Weekly · Sherwood: Ad-hoc |
| Processing | Auto-stack |
| Who's involved | Vendor/Flex setup; DOC FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday (all banners).
- **Cadence — National Weekly:** Available Tuesday → Tuesday; Valid Wednesday → Tuesday.
- **Cadence — Lyons & Sherwood:** Available Wednesday → Wednesday; Valid Thursday → Wednesday.
- **Cadence — Quebec/Gabriel Couture/Materiaux Audet:** Available Tuesday → Tuesday; Valid Wednesday → Tuesday.

## Upload & setup

### National Weekly (Vendor)
- Email confirmation from the retailer contact. The codesheet is in the FMQ ticket (flag processor if no participation list is linked — required for pricing zones, store assignments, and staggered dates).
- **Codesheet manipulations:** delete rows above and below the chart; save as `.csv`. **Risk:** file names must be in column A and spelling must exactly match the FTP files.
- **Config name:** `timber_mart`. **PDF Base Directory:** lowercase base path — highlight everything before `/atl`, `/west`, `/bc`, `/ont`, etc. (e.g. paths `/timber mart national/2026/09_june 11/bc` and `…/atl` → use base path `/timber mart national/2026/09_june 11`).
- **Uncheck "Region Assignment" and "Combine Zones."**
- Check the FTP that ALL pages under the base directory uploaded; cross-reference the participation list for any needing manual upload. Upload POTM pages if in the FTP.
- **Staggered dates (important):** once PZs are created, use the participation list to set staggered dates. The run dates must start at the earliest live date and end at the latest end date (e.g. zone live May 2–14 + zone live May 7–21 → run May 2–21). Adjust per-zone dates in Overview → Edit Dates/Details.

### Lyons & Sherwood (DOC)
- Retailer drops files directly into FTP (no email). Manual upload — all pages from the corresponding folder, inserts included; group pages manually.
- **Lyons:** one PZ ("Lyons") → assign all 3 Lyons stores. **Sherwood:** one PZ ("wSherwood") → assign Sherwood store (#7746).
- 4 standard thumbnails; legibility heights 45/35 (auto); available one day before valid date.

### Quebec / Gabriel Couture / Materiaux Audet (Flex)
- Email confirmation from the retailer contact. Codesheet in the FTP (labelled Participation List): delete rows above/below chart → save as `.csv`. **Risk:** file names in column A must exactly match FTP names; Dealer # (column B) must have decimals.
- **Config name:** `timber_mart`. PDF Base Directory: lowercase base path (highlight all before `atl`/`west`, etc.). **Check all toggles except "Region Assignment" and "Combine Zones."** If there's a Base flyer and a Custom flyer (Quincaillerie Bigras), upload both codesheets.

## QC specifics

**Box Draw (Medium; Auto-Box ON, Box QC bot OFF; linking doc Box-specific)**
- Include: coupons, packaged deals. Exclude: retailer logo, sign-up page, social media, special weblinks.
- **Every item on the first page** is boxed. After page 1, only box items with **prices, SKUs, coupons, %Off callouts, or Online callouts.** Coupons identified by the word "coupon" or scissors/cut-out line.
- Separate box per priced item (a "Valued Price" box still counts as a price). For packages, box elements with different prices separately. Box items that have a SKU but no price.
- **TMBQC (new):** draw boxes around `www.timbermart.ca`, the Fairstone callout, credit-card callout, and Air Miles.
- **Do NOT box** items with no price, no SKU, and that aren't coupons.

**Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **SKUs are no longer needed — do not enter them in any field.** Brand is Box-specific.
- Name/Brand/Description: enter as they appear, only in the language specified for the page. Original price usually has "Reg" before it.
- **Sale story RISK:** large "##% off" callouts sometimes apply only to certain items — do NOT assume the callout applies to every item on the page.
- **Disclaimer:** only enter if within the drawn box (not if at the bottom of the page).
- **Valid dates RISK:** only apply date overrides when a related promo sale story is on the item; ignore Air Miles dates; reference page-level valid dates (e.g. "4 Day Special!" callouts).
- **TMBQC URLs (Quebec only):** tag as LINK — Website `timbermart.ca/fr/`, Fairstone `web.fairstone.ca/timbermart-ol/fr`, Credit Card `timbermart.ca/fr/carte-de-credit/`, Sunroom Solutions `timbermart.ca/fr/solarium/`, Goodstyle `goodfellowinc.com/produit/goodstyle/`, Air Miles `airmiles.ca/megamilles/fr`.
- **Coupons RISK:** all coupons require the word "Coupon" in the name.
- **PDF image selection:** clean PDFs where available, else the corresponding cutout. Do NOT select lifestyle/sample-flooring/product-colour images — use cutouts for those.

**Image QC:** clean PDFs where available, else cutout; no lifestyle/sample images.

## Final QC / go-live notes (DOC)

- **POTM pages:** all flyers **EXCEPT Sherwood** receive POTM pages. Pagination order: regular monthly pages → Spine Wrap pages (only for special events like Father's Day) → POTM pages. Use the URL document to link POTM pages or copy boxes from the previous flyer (search "doc" in the FTP). Manually box/tag URLs/videos; YouTube links → Embed URL → Display Type: Video.
- Page category QC: no category on page 1 or on insert/POTM pages. Image category QC: prioritize PDFs.
- **FQC process is the same for all banners.**
- **Flyer Review type: Lite.**

---
*Source: Timber Mart OneGuide (Google Doc `1NQ0Yed95nfbSIN-uN6vG45lVv3bzu6pGXEq-JZ41km0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Tractor Supply Company USA — Processing Guide

> **Source:** Tractor Supply Company USA OneGuide (Google Doc `18KANpGZw-HJaH1AIcj8nMvlGvx3MCVRNTou8QYtqBls`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#tsc_usa` |
| Hosted URL | https://www.tractorsupply.com/CurrentAdView |
| Flyer type(s) & cadence | Current Ad (#3791) — **holiday flyers only** |
| Processing | Auto-stack; Flex (FAB tickets + Setup) → Image QC (Flex) → FQC (DOC); Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** holiday only. The retailer contact emails avail/valid dates and (usually later) an updated store list + linking document.
- **Publication cadence:** Available From Sunday · Valid From Tuesday · Available To Monday · Valid To Tuesday.

## Upload & setup (Flex)

1. Contact emails avail/valid dates, then sends an updated **store list** (includes the pricing zone for each store) and **linking document**. You'll likely need to add newly-opened stores to Fadmin — ask the contact.
2. Build a **generic codesheet** listing pricing zones, stores, and page names. This is a long manual process: filter the store list by pricing zone, copy/paste stores into the generic codesheet, and copy/paste the PDF page names for each pricing zone.
3. Upload — **Config name `generic`**, **toggles: all except "combine zones" and "region assignment"**.
4. While sessions run: apply the holiday theme (depends on which holiday flyer), external run name = the flyer name, avail/valid dates usually the same unless the client specifies. **4 standard thumbnails.**

### Setup QC checklist (Flex)

- Overview: no warnings **except unassigned stores (normal)**.
- Pricing Zones: all should have the same page count unless specified; each PZ has ≥1 store assigned.
- Sessions: all green. Vendors: linking doc attached to all tasks.
- Geography: usually too much time between flyers to compare; stores likely added by retailer.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking document required. **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box all product information together; handle multiple SKUs.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF auto-select ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories, disclaimer, URLs.
  - Name/brand as in flyer (bold text); description under the bold name/brand.
  - **SKU:** enter in both the SKU field and the Description field when provided.
  - Valid dates: only tag if different from the flyer.
  - **URLs:** add from the spreadsheet; if missing, search tractorsupply.com by SKU + item name.
  - Sale story = e.g. "SAVE $200"; disclaimer = italicized text.
- **Item Category QC (DOC):** categories tagged by OS, no QC needed; usually one clear category per item.
- **Item Image QC (DOC):** clean PDF where possible, cutout when not; no dark shadows around the image.
- **URL/Links QC (DOC):** ensure all items have a URL; if not in the retailer spreadsheet it's OK to leave blank.

## Out-of-processing

- Expect **multiple revisions** to links/pages.

## Flyer review

- **Flyer Review type: Lite** — standard review, no special risk items.

---
*Source: Tractor Supply Company USA OneGuide (Google Doc `18KANpGZw-HJaH1AIcj8nMvlGvx3MCVRNTou8QYtqBls`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Trail Appliance SK/AB — Processing Guide

> **Source:** Trail Appliance SK/AB OneGuide (Google Doc `1EgHKqhYbZB7A3g1_3vF5oVnv74dqPqX-MH455HrCwTE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#trailappliances` |
| Hosted URL | https://www.trailappliances.com/flyer |
| Flyer type(s) & cadence | Weekly Flyer (runs 3–7 days within the week) |
| Processing | Auto-stack; Upload (Vendor) → Image QC (Flex) → FQC (DOC); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Friday.
- **Publication cadence:** Available From Thursday · Valid From Sunday · Available To Thursday · Valid To Sunday (length ranges 3–7 days).
- **Linking document:** Yes.

## Upload & setup (Vendor, manual)

1. Check email for how many **zones/versions** there should be. The retailer sometimes sends Calgary, Edmonton, Saskatoon versions; if none specified, it's one version to all stores.
2. Pages → Edit → select the pages for the publication → Auto-Group → Save and continue.
3. When Flyer creation is available, start the task → create the pricing zone(s) → save and complete.

### Setup QC checklist (Vendor)

- Add stores per the number of versions: **BASE = all stores; Calgary = Calgary stores; Edmonton = Edmonton stores; Saskatoon = Saskatoon stores.**
- From the FTP download the **linking document** and **Layout PDF**; on any vendor task use mass upload to attach both (done twice, once per document).
- Complete the Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **Ensure the Layout PDF and linking document are attached to each flyer run.**
- Box and tag all banners per the linking document; text banners are **Link or Page Link** per the spreadsheet (banners have no product IDs). Box store logos and social/store-location banners **only if in the linking document**. One box for a single-item URL attachment; multiple boxes for multi-item attachments/layout PDFs.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** linking document required. **Exclude** coupons and packaged deals; **include** retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include brand, name, pre/postfix, description, SKU, price, original price, sale story, categories, disclaimer, URLs. **Exclude valid dates.**
- **Item Category QC (DOC):** ensure a category for each shoppable item.
- **Image QC (DOC):** choose white-PDF background images where possible; otherwise select the cutout.
- **URL/Links QC (DOC):** Overview → Items without URL → cross-reference the linking document. If a link exists in the document, paste it into the items page; if none, ignore.

## FQC (DOC)

- Ensure Standard 4 thumbnails complete; check publication dates; ensure **no theme**. Complete the FQC checklist.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Trail Appliance SK/AB OneGuide (Google Doc `1EgHKqhYbZB7A3g1_3vF5oVnv74dqPqX-MH455HrCwTE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Trail Appliance (BC Flyer) — Processing Guide

> **Source:** Trail Appliance (BC Flyer) OneGuide (Google Doc `1Rj3fjjzJvm6Of2MRZOS74X0E6TRPjKu683FtJoi-ZCE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | retailer channel, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Weekly Flyer |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); Upload (Vendor) → Image QC (Flex) → FQC (DOC); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday · Available To Monday · Valid From Tuesday · Valid To Tuesday.
- **Linking document:** Yes.

## Upload & setup (Vendor, manual)

1. Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload.
2. Auto-Group or manually enter grouping numbers; ensure the correct language is selected. Save & Confirm — **do NOT Process Internally.**
3. **Pricing zone:** create a **Base** pricing zone with all applicable pages. Save & Confirm.
4. Add all stores from the **"BC stores" Store Set** unless the retailer specifies otherwise.

### Setup QC checklist (Vendor)

- Confirm all pages uploaded correctly (Pricing Zone → Items View). **RISK:** if uploading from SFTP, confirm no pages in the SFTP were left un-uploaded.
- Confirm flyer dates (usually first or last page of the flyer).
- Complete thumbnails (**4 Standard**). **A custom-tile upload is used for the Storefront Premium and Storefront Carousel Premium thumbnails.**
- Retrieve the linking document uploaded with the files and mass-attach to all vendor tasks. Set preview dates. Complete Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **MSRP handling:** Do **not** put MSRP* prices in the prefix or Current Price. Put the MSRP in the **Sale Story** (e.g. "MSRP $2100"), and for any item with MSRP pricing add the disclaimer: *"MSRP is the Manufacturer's Suggested Retail Price only. This does not equate to a market price or our regular price."* (do not repeat MSRP elsewhere).
- **Banners/logos:** all store logos and some banners must be boxed and tagged **per the linking spreadsheet** (banners have no product IDs). Text banners are boxed/tagged as **Link or Page Link** per the spreadsheet.
- **Multi-version items:** include the model and price of the other version in the description; add color-price variations in the disclaimer (e.g. "Same price for white", "add $50 for stainless steel").

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking document required (used for both box & tag). **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box everything; box store logos and social/store-location banners **only if in the linking document**. One box for a single-item URL attachment; multiple boxes when the URL attachment/layout PDF shows multiple items.
- **Tag / Tag QC (Low; Auto-tag ON; PDF auto-select ON):** include brand, name, pre/postfix, valid dates, description (include SKU), SKU, price, original price (= MSRP), sale story, categories, disclaimer, URLs.
  - **Prefix** usually "sale priced" (never MSRP); for multi-items use the item type as prefix. **Postfix** = anything after the price (e.g. "after 10% instant rebate").
  - Every item needs at least one category (be specific). Tag all store logos and social icons as **Link**. Use every link in the spreadsheet; category items tagged as Link type, page-link rows tagged as Page Links.
- **Image QC:** clean PDF preferred; no black backgrounds/shadows; cutout when no clean PDF; use cutout for packages/multi-item banners.

## Pre-FQC / FQC (DOC)

- Confirm dates vs. PDF and availability toggles. Thumbnails correct with **custom tile applied** (includes retailer logo). No items without links. Standard checks: all items boxed/tagged, spotchecks complete (20% of pricing zones), previews clickable, sessions completed, geography correct.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Trail Appliance (BC Flyer) OneGuide (Google Doc `1Rj3fjjzJvm6Of2MRZOS74X0E6TRPjKu683FtJoi-ZCE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Trevi — Processing Guide

> **Source:** Trevi OneGuide (Google Doc `1KH7fO_13GEJJQ5RJCdnJJtKU_x1V-hWENF0hTK7mycc`). Contacts/credentials omitted.

> Note: the retailer has been inactive since before the current owners took on the account, so some details are sparse.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channel(s) | `#trevi` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Seasonal (3–5 publications a year) |
| Processing | **Trim Stack**; Upload/Setup (OS/DOC) → FQC (DOC); Flex (Flyer Review); Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday.
- **Preview date:** Monday.

## Upload & setup (DOC)

1. Manually upload files via SFTP.
2. Set **all files to French** under Language.
3. Auto-group → Save & Complete.
4. Create **2 pricing zones**: 1st = **Base** = French; 2nd = **Base CL** = cross-language in English.
5. Add all stores to **both** pricing zones.

### Setup QC checklist

- Confirm all pages are French. Confirm dates. Mark Setup QC checklist complete.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** no linking document. **Exclude** coupons, packaged deals, sign-up page; **include** retailer logo, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF auto-select ON):** include brand, name, valid dates, description, SKU, price, original price, sale story, categories, disclaimer. **Exclude** pre/postfix and URLs.

## FQC (DOC)

- QC thumbnails. Edit details: **available on Flipp**. Pricing zones: pages in sequential order; all items with a price and visible sale story boxed; all pages interactive.
- Sessions all green. **Geography: no stores or FSAs/zips added or removed.**

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Trevi OneGuide (Google Doc `1KH7fO_13GEJJQ5RJCdnJJtKU_x1V-hWENF0hTK7mycc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Tropicazoo — Processing Guide

> **Source:** Tropicazoo OneGuide (Google Doc `1Hqqi3g_j0LgI0lmWQ_bp906NEsNn-3miKPlhiYnL5ZI`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | **Flipp only** |
| Slack channel(s) | `#tropicazoo`, `#flex-processing support` |
| Hosted URL | Flipp does not power hosted |
| Flyer type(s) & cadence | Circulaire (#6407) — ad-hoc |
| Processing | Auto-stack; Flex (Processing Support); DOC owns Upload/Image QC/FQC; no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** ad-hoc (confirm dates via email).
- **Publication cadence:** Available From Thursday · Valid From Wednesday · Available To Thursday · Valid To Wednesday.
- **Linking document:** Yes (URL sheet from FTP).

## Upload & setup (Vendor)

1. Confirm dates via the email sent to us.
2. Edit details: **available on Flipp/Dis, no theme, no external run name, hide on hosted.**
3. Manual upload → select pages → change language to **FR** → Save & complete.
4. **Base** zone, add all stores.
5. Download linking documents from the FTP and attach to all vendor tasks.

### ⚠️ Common errors / risk items (retailer-specific)

- **URLs:** ensure all URLs are added from the URL sheet — check "Items without URLs" and add anything on the link sheet that was missed (not every item gets a URL, but everything on the link sheet must be tagged).
- **SKU vs. Description:** the SKU goes in the **SKU field**, never the Description field (e.g. `MIRZ128A`).
- **Brand:** do not tag brand in the Brand field — include all info in the **Name** field, written as on the PDF.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking document required. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. **Include** items with price callouts (and items without price callouts only if specified in the URL attachments — uncommon).
- **Tag / Tag QC (Low; Auto-tag ON; PDF auto-select ON):** include name (all info here), pre/postfix, valid dates, description, SKU, price, original price, sale story, disclaimer, URLs. **Exclude brand and item categories** — but **Google categories are tagged.**
- **Image QC:** select the best clean PDF with no markings; if none, select the best cutout.

## FQC (Flex)

- Complete auto-stacks. **No page categories on the first page.**
- Link QC: check Items without URL against the URL linking sheet; add missed links.
- Overview → Special Actions → **Republish**, wait for sessions.
- Check dates and theme. Thumbnails Standard 4 (1065x800, Stock_premium, Storefront_carousel_premium, Storefront_carousel_organic). Geography: no missing/added stores.

## Out-of-processing

- **Page swaps** follow the standard baseline process.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Tropicazoo OneGuide (Google Doc `1Hqqi3g_j0LgI0lmWQ_bp906NEsNn-3miKPlhiYnL5ZI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# True Value — Processing Guide

> **Source:** True Value OneGuide (Google Doc `18-C-UDThAuL_Sqgr5yWV0NhUD7T3oa5rma5p7BInaH8`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channel(s) | `#truevalue`, `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer — ad-hoc |
| Processing | Auto-stack; Upload/Setup (Flex/Vendor) → FQC (DOC); Flex (Flyer Review); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** ad-hoc.
- **Publication cadence:** Available From Wednesday · Available To Tuesday · Valid From Wednesday · Valid To Tuesday.
- **Linking document:** N/A.

## Upload & setup (Flex, manual)

> Pages may need to be added to the SFTP by the processor if the client sends files over email.

1. Pages tab → Edit → select all pages from the SFTP menu (files labeled with each ad's launch date) → Confirm & Upload.
2. Auto-Group or manually enter grouping numbers — **English pages only**. Save & Confirm — **do NOT Process Internally.**
3. **Pricing zone:** create **Base** with all applicable pages, add all applicable stores. Save & Confirm.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone → Items View). **RISK:** if uploading from SFTP, confirm no pages left un-uploaded.
- Confirm flyer dates (usually first or last page). Complete thumbnails (**4 Standard**). Complete Setup QC checklist.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** no linking document. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories, disclaimer. **Exclude URLs.**

## Pre-FQC / FQC (DOC)

- Confirm dates vs. PDF and availability toggles. Thumbnails correct and include the retailer logo. Standard checks: all items boxed/tagged, spotchecks complete (20% of pricing zones), previews clickable, sessions completed, geography correct.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: True Value OneGuide (Google Doc `18-C-UDThAuL_Sqgr5yWV0NhUD7T3oa5rma5p7BInaH8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
