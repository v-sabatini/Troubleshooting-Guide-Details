# Retailer Processing Guides — P

> Bundle of 36 retailer-specific processing guides (P). Contacts and credentials are omitted from every guide.

**Contains:** PartSource, Party Expert, Pasquier, Passion Jardins, Patrick Morin, PEI Liquor, Pet Supermarket, Pet Valu, Pete's Frootique, Petland, PetSmart Canada, Pharmachoice & RxHealthMed, Pharmasave, Piggly Wiggly Carolina, Piggly Wiggly Midwest, Pisces Pet Emporium, Plomberie Mascouche, Potvin & Bouchard, Powell's Supermarket, Première-Moisson, President's Choice, Preston Hardware New, Price Chopper KC, Price Chopper USA, Price Less IGA, Price Rite Marketplace, PriceSmart Foods, Princess Auto, Pringle Creek Market, Pro Hockey Life, Product of the Year, ProNature, Provigo, Proxim, Publix Liquors, Publix (Weekly, Spanish, Extra Savings)


---

# PartSource — Processing Guide

> **Source:** PartSource OneGuide (Google Doc `1TI-N_pxk8qLc-Gm78UvQzNUtFpPoHJq6R7IRio4ja3c`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#partsource` |
| Hosted URL | partsource.ca/pages/flyer |
| Flyer types & cadence | 3540: Weekly (Inserts / "Evergreen" and Deals flyers) |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Background / files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Thursday, Valid From Friday; Available To Monday, Valid To Tuesday.
- **~90% of content comes from quarterly inserts** provided with a schedule, so many flyers can be uploaded in advance. The insert schedule marks with an "x" which insert belongs to each publication and its pagination.
- **Non-insert (Deals) flyers:** files sent via WeTransfer over email.
- **All insert flyers get a 1-day consumer preview** — send the item export 2 days before going live.
- **Watch content policy:** occasionally PartSource has fewer than 5 shoppable items — keep a lookout.

## Upload & setup

### Inserts / Evergreen (owned by Flex)
1. Check the flyer schedule to find which insert is needed for the week (marked "x").
2. Open the flyer run shell. Pages → Edit → upload files for that insert → Auto-group.
3. Pipeline → start **Flyer Creation**. Pricing Zone: **Base**, add all stores. Wait for sessions.
4. Edit Details: 1-day consumer preview; set preview date for the Monday before go-live; no theme; available everywhere.
5. **Standard 4 thumbnails** — if the PartSource logo sits in the bottom-right corner, shift the thumbnail to cover it. Complete Setup QC checklist.

### Deals flyers (owned by Flex)
- Same base steps (Pages → Edit → select all → Auto-group; Flyer Creation; Base PZ, all stores; sessions).
- Edit Details: 1-day consumer preview; preview date Monday before go-live; no theme; available everywhere.
- **Deals go live on hosted only first, then must go available everywhere on the valid date.** Create **2 triggers** (Overview → Triggers): one to display on Distribution, one to display on Flipp — both set to run on the valid date.
- Create an Optics ticket for a live check that it's available everywhere.
- Standard 4 thumbnails (cover the logo if needed). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc required):**
- **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Draw a box whenever there is a unique price for an item. Box banners containing a `.com`/`.ca` address. Box social-media icons (Facebook, Twitter, Instagram).

**Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON; linking doc required):**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. Brand is Box-specific.
- Exclude: disclaimer, URLs.
- **Price range:** enter the first price in Current Price; enter the second by selecting `- $$$` from the postfix dropdown and putting the price in the postfix amount field.
- **Prefix/Postfix:** select from dropdown; if missing, flag to PC to update the list.
- **URLs:** do **not** enter URLs unless it's a social-media banner. Social icons = direct-link display type, named for the platform (e.g. "Facebook"); Email Sign Up links to the partsource.ca email signup page.

**Image QC:** select a PDF image for all items; prioritize clean white backgrounds. **If the PDF image has a black shadow, use the cutout image instead.**

## Post-processing (owned by DOC)

**Item Category QC** (category chart):

| Category | Example items |
|---|---|
| Car Care | Risers, ramps, jacks, inflators, polishing sets, cleaners, Armour All / Turtle Wax, WD-40 |
| Tools | Tire rack, assemblies, shocks/struts, compressors, drills |
| Accessories | Filters, cushions, wipers, gas cans, seat/wheel covers, trouble lights |
| Hard Parts | Chassis components, rotors, brake pads, spark plugs, calipers, headlights, alternators |
| Electronics | Batteries, code readers, chargers, GPS, phones, cameras |
| Fluids & Additives | Transmission fluid, lubricants, antifreeze, coolants, engine oils |

- **Page categories:** include categories on the first page too; coupon pages don't need categories.
- **SKU QC:** Item Search SKU → IS → blank; apply from the PDF all that are blank.
- **⚠️ RISK:** go through each item and confirm the product name and SKU as tagged match the flyer page.

**Item URL export process (DOC):**
- Overview → export items; keep only Item ID, Page, Name, SKU, URL (URLs blank for the retailer to fill). Sort by name, save `.xlsx`.
- Email/schedule the item export for 9 AM the day before the available date, including the preview URL (1st English URL under ad-hoc processing).
- When the retailer returns the URL spreadsheet: keep only `item_id, sku, url`, save `.csv`, Overview → Import Items. Verify via Item Search URL → IS → blank.
- Mark items in store. Generate the email-blast URL from the merchant Generate URLs page (Type: Full Screen; Locale: English; Generate HTML) and add it to the external schedule sheet ASAP.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by DOL).
- **Out-of-processing:** baseline page-swap process available (see OneGuide video).

---
*Source: PartSource OneGuide (Google Doc `1TI-N_pxk8qLc-Gm78UvQzNUtFpPoHJq6R7IRio4ja3c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Party Expert — Processing Guide

> **Source:** Party Expert OneGuide (Google Doc `1xBXI2AWrqSlV7dKiB-yHrXOfjiTsuL-8SBHaLP6tc8w`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Flyer types & cadence | Flyer Type 1: Seasonal |
| Processing | **Trim Stack**; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Bilingual account** — EN and FR pages/pricing zones.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (owned by DOC)

- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu (or upload from email) → Confirm & Upload. Auto-Group or add page numbers into the Grouping Number field. Ensure **English** language selected. Save & Confirm.
- **Create pricing zones:**
  - PZ 1: **ENG** — add all English pages in order. Save & next.
  - PZ 2: **FR** — add all French pages in order. Save & Done.
  - Add all stores to both PZs.
- **Attach the tagging document to all vendor tasks** (usually sent via email; ask the Processor if not attached in ClickUp): Vendors → upload mass attachment → select all vendors, choose the xls.
- Wait for sessions. **Confirm the same number of pages in the ENG and FR PZs.** Thumbnails — Standard 4.

### Setup QC (owned by Flex)
- Check dates match the first page of the PDF; no theme; available everywhere; complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF; linking doc required):**
- Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Use the Reference document** attached to each flyer — it has numbers on each item corresponding to where a box should be drawn.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required):**
- Include: name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, image selection, URLs. Brand is Box-specific. **Exclude valid dates.**
- **One-to-many relationship:** the flyer indicates the listed price applies to all items within a box unless there are multiple item types. URLs come from the **Reference** document (via email).
- **"Costume Walls" pages:** numbered with product name, price, description and SKU per product — tag the correct language per the PDF and the Reference doc URL.
- When tagging, select the PDF image on the left-hand side for the item.

## Final QC (owned by DOC)

- **Check URLs:** open the linking document attached to vendor tasks; review every link on each page using the correct EN or FR tab; add a comment "All links checked."
- Spotchecks if required. QC thumbnails (Standard 4: stock premium, storefront carousel premium, storefront carousel organic).
- Edit Details: available everywhere; no external run name; run dates match the last page of the PDF. Check items without URL.
- **Flag missing pages or geography changes to the full-time team.** Complete FQC checklist.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by DOL). Confirm dates on PDF or email, legibility heights, item image QC, thumbnails, items-without-URL link check, pagination order, all shoppable items boxed, iframe & vertical previews interactive, geography no change WoW.
- **Out-of-processing:** see the retailer's 2025 BF / Publication & Ad-Hoc Requests guidelines for page swaps and post-live checks.

---
*Source: Party Expert OneGuide (Google Doc `1xBXI2AWrqSlV7dKiB-yHrXOfjiTsuL-8SBHaLP6tc8w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pasquier — Processing Guide

> **Source:** Pasquier OneGuide (Google Doc `169oQ-o6j_08l_FzIYtK9slrxuoaMeK0aAZfxQJ25Tdo`), updated Jun 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | **Flipp only** |
| Hosted URL | pasquier.qc.ca/circulaire |
| Flyer types & cadence | 11608: Weekly (direct) |
| Processing | Auto-stack; **Flex: 3FL + Flyer Review** ("SIMP POP" account); OS does Setup; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Friday.
- **Cadence:** Available From Tuesday, Valid From Wednesday; Available To Thursday, Valid To Wednesday. (Setup notes Valid From Thursday to match PDF.)
- **Bilingual account** — FR and CL EN pricing zones.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (owned by Vendor)

- **Edit Details:** Available From Tuesday, Valid From Thursday, Available/Valid To Wednesday (all should match PDF dates). Toggles: **hidden on Flipp Hosted**; no theme. Ensure the **2 pricing zones have the same number of pages** and are **FR and CL EN.** Add all stores.
- **Manual upload (Flex):** upload all pages in **French** for the week. Flyer Creation → 2 pricing zones:
  - **Base** — toggle as **French**
  - **Base CL** — toggle as **English** (cross-language)
  - Add all stores to both.
- **Set preview date to the following Sunday** (e.g. flyer going live Tue June 16 → preview date Sun June 14).
- Complete Setup QC.

## QC specifics (SIMP POP account)

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON):**
- Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box single items and items with multiple sizes.

**Tag / Tag QC (Low; Auto-tag ON):**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. Brand is Tag/QC specific. **Exclude SKU.**
- Name/Brand = bolded text; price/original price/pre-postfix/SKU only if shown in the PDF; valid dates only if different from the rest of the flyer (coupons, etc.).

**Image QC:** select clean PDF images where possible; if none, select cutouts.

## Post-processing

**Final QC (owned by Flex):**
- Draw the standard 4 thumbnails.
- Edit Details: **hidden in hosted and distribution**; no theme.
- Check that all items with prices, sales stories or callouts have a box drawn. **Important: it is OK if items are not tagged correctly or not tagged at all.** Ensure no boxes overlap.
- Geography: no change week over week.
- FQC checklist — for all red flags, write "N/A."

**Page swap (owned by Flex):** standard page swap.

## Flyer Review

- **Type: Lite** (owned by Flex).

---
*Source: Pasquier OneGuide (Google Doc `169oQ-o6j_08l_FzIYtK9slrxuoaMeK0aAZfxQJ25Tdo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Passion Jardins — Processing Guide

> **Source:** Passion Jardins OneGuide (Google Doc `1y_rPdVLGDUdV_dp4Sy1e4Ch4WzSumKzuWBv78biRA1A`), updated May 08. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | No retailer channel; `#flex-processingsupport`, `#flex-flyer-review` |
| Flyer types & cadence | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday. (FQC checklist notes Available = Tuesday, Valid = Thursday, Available/Valid To = Wednesday.)
- **Bilingual account** — EN and FR pages/pricing zones.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup (owned by Flex)

- Manually upload files from the SFTP.
- **Upload once in EN and once in FR** — two sets of the same file, each assigned a different language → Auto-Group → Save & Complete.
- **Create pricing zones:** EN = all pages = all stores; FR = all pages = all stores.
- Attach the store-tagging link sheet to tasks.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc required):**
- **Include:** retailer logo, sign-up page, social media, special weblinks.
- **Exclude:** coupons, packaged deals.
- All items with a visible price or sales story should be boxed. **On the back page, box every store separately.**

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required):**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. Brand is Box-specific. **Exclude SKU.**
- **English text only on EN pages; French text only on FR pages.**
- All text in blue within the boxed area should be boxed and tagged with links matching the store-tagging spreadsheet.

## Post-processing (owned by DOC)

- **URL/Links QC:** open the last page of the flyer; ensure all listed stores are direct links driving to specific store locations.
- **FQC:** Ops spotchecks; QC thumbnails (1065×600, storefront carousel premium, storefront carousel organic).
  - Edit Details: Available = Tuesday, Valid = Thursday, Available/Valid To = Wednesday; Internal Run Name = MM DD; available everywhere; no theme.
  - Pricing Zones: all priced items and visible sales stories boxed; check interactivity via vertical preview; **page order should match the tracking sheet .xls in the SFTP.**
  - Sessions all green; mark items In Store Only.
  - Geography: no stores or FSAs/zips added or removed.

## Flyer Review

- **Type: Lite** (owned by Flex). Overview thumbnails; Edit Details (Available and Valid the same, dates match PDF, hidden on hosted, seasonal theme set); pagination order; item boxes; iframe & vertical previews; geography unchanged; **risk item — last page should have direct link-outs for each store.**

---
*Source: Passion Jardins OneGuide (Google Doc `1y_rPdVLGDUdV_dp4Sy1e4Ch4WzSumKzuWBv78biRA1A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Patrick Morin — Processing Guide

> **Source:** Patrick Morin OneGuide (Google Doc `1AcJEEw_awSeGF5Wu84XVqeArhU8raI6RtstrJu3lRUI`), updated May 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `patrick-morin3` (private channel) |
| Hosted URL | patrickmorin.com |
| Flyer types & cadence | Flyer Type 1: Weekly · Flyer Type 2: Monthly |
| Processing | Auto-stack; Flex does Flyer Review; **linking document required**; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Tuesday. Preview the day before, on Wednesdays (since April 2024).
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Thursday, Valid To Wednesday.
- **Bilingual account** — EN and FR pages/pricing zones.
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## ⚠️ Risk item — catalogs without pricing
**Catalogs without pricing on the flyer are acceptable as long as the link sheet contains the item pricing.** Advise OS to add the pricing from the link sheet into the tags. Add to all comments under OS tasks: *"PLEASE READ: please add the pricing (prix REG) that's in the linking doc, in the tag in the 'current price' section for all the products. Pricing must be included for all products."*

## Upload & setup (owned by Vendor)

- **Receive files:** retailer sends the PDF via WeTransfer email — download and drop into the Patrick Morin FTP (e.g. `PM CIRC 32`). The link sheet comes in a separate email. Files sync to FADMIN after ~an hour.
- **Upload (once link sheet + PDFs received):** manual upload — **upload the same pages TWICE for EN/FR.** Auto-Group. Toggle first set English, second set French.
- **2 pricing zones: EN & FR — add all stores to both.**
- **Mass attach the link sheet to all vendor tasks** (no manipulation needed). The link sheet is **not in the FTP** — it's in the OS Setup Files drive. Match the tagging document name to the week (e.g. "Circulaire 39.xls" belongs to flyer 39).

### Setup QC (owned by Vendor)
- Confirm all pages uploaded correctly (Pricing Zone Tab → Items View). **Risk:** if uploading from SFTP, confirm no pages were left un-uploaded.
- Confirm flyer dates (first or last page). Thumbnails (4 Standard). Ensure all preview dates are set. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF):**
- **Include:** retailer logo, sign-up page, social media, special weblinks.
- **Exclude:** coupons, packaged deals.
- Box each item with a price.

**Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON; linking doc required):**
- Include everything: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Tag/QC specific.

**Image QC:** choose clean images with white backgrounds (e.g. Sifto Pool Salt, SICO Premium Paint).

## Post-processing (owned by DOC)

- **URL/Links QC:** Overview → information/reports → items without a URL; cross-reference the link sheet and input missing links, keeping language correct (ENG item → ENG link).
- **FQC:** Standard 4 thumbnails; legibility heights 45/35; item image QC (clean PDF preferred, lifestyle images acceptable); check sessions and re-verify URLs; categories on all pages except the first.
- **External Run Name (French):** "Circulaire de la semaine" (or the catalog name if it's a catalog). Available Wednesdays, Valid Thursdays.
- **Tracking codes (must match):**
  - *Weekly Flyer portion:* Dynamic Variable, Source All, `utm_source` = `flipp`; and `utm_medium` = `flyer`.
  - *Flyer run portion:* Dynamic Variable, Source All, `utm_campaign` = `semaine_xx_2025` (xx = the week number being processed).
  - Click **"Apply All Tracking Codes."** Complete FQC checklist.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by Flex): flyer dates, sessions complete, previews correct, all items tagged accurately, geography correct, availability toggles correct.
- **Page swaps:** download the revised page from the email; manually add it **twice** (one EN, one FR); save & complete; complete all vendor tasks; copy the original page boxes to the revised page; update the tag for the required revision (both languages); swap the revised page into the respective pricing zone; re-run page tile generation + page stitching; advise the retailer (reflects within the hour).

---
*Source: Patrick Morin OneGuide (Google Doc `1AcJEEw_awSeGF5Wu84XVqeArhU8raI6RtstrJu3lRUI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# PEI Liquor — Processing Guide

> **Source:** PEI Liquor OneGuide (Google Doc `1gSZ0yMwyhHc0uBiA5-2NAZ5QY7Khx96Vx6Lfg819jeo`), updated Apr 29, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Flipp only** |
| Slack channels | `#pei-liquor` |
| Flyer types & cadence | Flyer Type 1: Flyer — ad hoc |
| Processing | Auto-stack; Flex does Processing Support & Flyer Review; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Ad hoc.
- **Cadence:** all ad hoc (Available/Valid From/To and preview date all ad hoc).
- **Linking document:** No.
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## Upload & setup (owned by Flex)

- Files are uploaded to the SFTP.
- Manually upload pages → Auto-Group.
- **Create 1 pricing zone: base = EN**, add all stores.
- Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF):**
- **Include:** special weblinks. Box each item individually; box category callouts.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.

**Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection OFF):**
- Include: name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Tag/QC specific. **Exclude pre/postfix.**
- **Tag items as links using the "all products on sale" URLs by product type** — Spirits, Wine, Beer (beer-and-ciders), Coolers — on liquorpei.com.

**Spotchecks:** check all items are boxed.

## Final QC (owned by Flex)

- 4 standard thumbnails; check all vendor tasks complete; check vertical and horizontal preview; mark FQC complete.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by Flex).
- **Page swaps:** standard baseline page-swap process.

---
*Source: PEI Liquor OneGuide (Google Doc `1gSZ0yMwyhHc0uBiA5-2NAZ5QY7Khx96Vx6Lfg819jeo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pet Supermarket — Processing Guide

> **Source:** Pet Supermarket OneGuide (Google Doc `1iHExKLdvzerUUolta3MlnmTYuwjZ9j4sQLcjk3o8Qdg`), updated May 30, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#petsupermarket` |
| Hosted URL | petsupermarket.com/local-ads |
| Flyer types | 3785: In-store Ads · Flyer Type 2: Monthly |
| Processing | Auto-stack; Flex does FAB Tickets; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Thursday, Valid From Thursday; Available To Monday, Valid To Tuesday.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## ⚠️ Risk item — social media links
**Social media links always need to be tagged and linked.**

## Upload & setup (owned by Flex)

- **Manual upload:** Fadmin Pages tab → Edit → upload from the corresponding FTP folder → Auto-group, **do not process internally.**
- **Pricing Zone: Base.** Add all stores. Attach the linking document to ALL vendor tasks.

### Setup QC (owned by Flex)
- Toggles: available everywhere. Available dates Thursday → Sunday (confirm from client email); valid dates same as available (unless stated). External run name as noted in the client email; theme N/A (unless Black Friday / Holiday / etc.).
- **Legibility heights 65/40. Thumbnails Standard 4.**

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc required):**
- **Include everything:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box "Yes" items per the linking document.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required):**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Box-specific.
- Name/Brand = bolded text; Description = non-bolded text; price/original price/pre-postfix/SKU only if shown in the PDF; valid dates only if different from the rest of the flyer; URLs from the linking document; sale story = emphasized text; disclaimer only if on the page.
- **Categories:** based on product/page — Dog, Cat, Fish, Bird, Small Animals.

**Image QC:** PDF preferred unless there are shadows, etc.

## Final QC (owned by DOC)

- **Pre-FQC:** Pricing Zone → Items — ensure all products, banners, logos and callouts in the linking document are boxed and tagged; review horizontal preview. Pages tab — QA page categories, spotcheck product links. Overview — available everywhere; dates Thursday–Sunday (unless stated); external run name from email; theme N/A.
  - Items without a URL — check against the linking document. Image QC PDF-preferred. Thumbnails Standard 4. Legibility heights 65/40.
- Complete FQC checklist.

### Cloning — Monthly flyers only
- If clones are required (stated in the client email; usually 2: **"Dog & Cat"** and **"Small Animal"**): the **original monthly flyer is hidden in hosted; clones are hidden in Flipp/Distribution.**
- Overview → Ad-hoc Processing → Clone → create two new runs, **copy tracking codes.** On the new runs confirm legibility heights, thumbnails, item image QC, categories, stores, and external run name (from email).

## Flyer Review / live dates

- **Flyer Review type: Lite** (owned by Flex).
- **Live-date notes:** include all related text when boxing. On page 1 there are boxes along the top showing page categories that need to be boxed.

---
*Source: Pet Supermarket OneGuide (Google Doc `1iHExKLdvzerUUolta3MlnmTYuwjZ9j4sQLcjk3o8Qdg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pet Valu — Processing Guide

> **Source:** Pet Valu OneGuide (Google Doc `1cnCzKzcNPsvax7nX-nrzxz6WMC3RHflPuPHYiYn6oq4`). Contacts/credentials omitted.
> Covers banners: **Pet Valu, Bosley's, Paulmac's Pets, Total Pet, Tisol.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#petvalu` |
| Hosted URL | petvalu.ca/flyer |
| Flyer types | Flyer (types 63, 2459, 6118, 4223, 4635) |
| Processing | Auto-stack; Flex (FAB tickets); no coupons; Strategic Ops (Feedel/retailer data services) |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available From Wed, Valid From Thu; Available To Mon, Valid To Tue.
- **Preview:** 1-day consumer preview, 2-day merchant preview (set preview start 2 days before available date). Preview not required if files arrive at 5-business-day lead time.
- **Linking document:** Evergreen linking doc, attached to all vendor tasks (Setup QC task → toggle Mass attachment → attach). Box Draw/Box QC-specific and Tag/QC-specific linking docs also required.
- **Workflow owners:** Upload/Setup = Vendor; FQC = DOC.

## Upload & setup (owned by Flex)

**READ ME:** After confirming with the retailer/processor that all banners are the same, only send the **Pet Valu** banner to OS for processing. You must still upload the other banners but delete their boxes in the Box QC interface — boxes get copied from Pet Valu to the other banners after FQC/corrections.

- On the run's Pages tab → Edit → select the FTP folder → upload all pages. Page naming by banner:
  - Pet Valu: `pvon`, `pvbc`, `pvabmbsk` (sometimes just one PV version)
  - Tisol: `ti` · Total Pet: `tp` · Bosley's: `bos` · Paulmac's Pets: `pm`
- **Check the shared insert tracker** for additional inserts to upload; missing pages → confirm with their team.
- **Pricing zones:** Pet Valu zones match page names (PVON, PVBC, PVABMBSK); if only one PV version, zone = BASE. Tisol/Total Pet/Bosley's/Paulmac's each get one BASE zone.
- **Store sets:** PVBC zone → PVBC set; PVON zone → PVON set; PVABMBSK zone → PVABMBSK set. If only one PV version → assign all three sets. If no PVABMBSK version → PVON flyer gets both PVON and PVABMBSK sets. Tisol/Total Pet/Bosley's/Paulmac's each get all stores.
- Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- **TOTM (Treat of the Month) page** refreshes on the **1st of every month.** If a flyer spans two months you must upload the next month's TOTM page and **set a trigger** (Pages → Layout → swap page → "Run as Trigger", date = 1st of month, time = 12 AM). Create a ticket if needed.
- **Custom tiles** must be added, along with triggers for any replacements.
- **Flyer sorting** (check at FQC): monthly flyers ALWAYS first, followed by any catalogs.
- **Social media / URLs** must be boxed; in tagging set item display type = "Link" and insert links.
- **Page 1 links** must be complete and present on **all banners** (display type "Page Link"; destinations in the linking doc, same across banners).
- Linking doc attached to all vendor tasks; pages added to the appropriate banner.
- If all banners are the same, **hold off** on copying boxes from Pet Valu to the other banners until after previews are sent and corrections made.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box the product image and use a **text box** to reference item info when needed.
- Box any **call to action** (Explore More, See More, Learn More, Shop All, Shop Now).
- Box "Shop your locally owned & operated store, part of Canada's leading pet retailer."
- Box the logo; box call-outs (usually pages 1–2).
- Box each **"Get the Xth bag free with Your Rewards"** separately from the product it refers to.
- If an offer has different pricing, box separately and use text boxes to tie price to the correct image.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates (valid dates included only if stated).
- **Brand:** enter into brand field even if it repeats in the name field.
- **Price/Original Price fields are ONLY for regular pricing.** Any red text (dollar/percentage discount or sale price) goes in **Sale Story** — add the sale-story call-out first, then the sale pricing.
- **Price Text:** if a price range, put the second half of the range here.
- **Multiple items:** box ~10 products + supporting info together; box related products with a common description together; include all items in the description. Include all text under the product name except disclaimers.
- **Every item gets a URL.** Easiest method: copy the item name, search on petvalu.ca, use the search-results URL. Brand direct links used where there's a CTA (Shop All/Shop Now).
- **Lookbooks:** if SKUs appear in brackets on the PDF, search the SKU on the website to get the correct product link.
- **Standing direct links** (per banner logo and recurring banners): Pet Valu petvalu.ca, Tisol tisol.ca, Total Pet totalpet.ca, Bosley's bosleys.ca, Paulmac's paulmacs.com; Your Rewards, AutoShip, TOTM titles, Dog Wash, Raw Food, Grooming, Adoption, Find Your Store, and "Lower Price. Locked In." all have fixed collection links (in the OneGuide).
- **Categories:** Dog/Cat/Small Pet × feed/treat/train/protect/play, plus Events/Ads.
- **Disclaimer:** include per the linking doc (e.g. "Must be of equal size and value").

### Image QC
- Prefer PDF image (PDF Image Auto-Selection enabled).

## Post-processing / FQC (owned by DOC)
- Page categories (Pages tab), Page 1 links present/boxed/tagged for **all banners** — verify in hosted preview.
- **Items without URLs:** Overview → Information/Reports → "items without a URL"; fill in from the banner's linking doc.
- **Disclaimers:** item search compared against the linking doc.
- **RISK ITEM:** do a thorough spot-check — incorrect links are likely.
- Flyer Review type: **Lite.**

## Out-of-processing
- TOTM page swap + trigger (see Common errors above); repeat for any inserts needing swap (use the shared insert tracker).
- **Merchant preview:** if all banners are the same, only send Pet Valu's. Send 2 days before available date (only when assets arrive >5 business days from go-live). Preview links: Overview → Ad Hoc Processing → Preview URL → Hosted 2 Preview Link (EN); a preview start date on/before today is required.
- After corrections, copy boxes from Pet Valu to other banners; update logos to each banner's hosted name; confirm item counts match across banners.

---
*Source: Pet Valu OneGuide (Google Doc `1cnCzKzcNPsvax7nX-nrzxz6WMC3RHflPuPHYiYn6oq4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pete's Frootique — Processing Guide

> **Source:** Pete's Frootique OneGuide (Google Doc `1fVCt2A4Dan7sjJbt2k_rb9BQwwkFV-Hu2zbeTN7DG5w`), updated May 13, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys` |
| Hosted URL | petes.ca |
| Flyer types & cadence | Flyer Type 1: Weekly (Wednesday to Wednesday) |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** files come in Wednesday or Thursday (email usually Fridays when files are uploaded to the FTP/shared drive). Confirm receipt by replying to the email; the email also provides links to add during FQC.
- **Cadence:** Available From Wednesday, Valid From Thursday; Available To Wednesday, Valid To Wednesday. 1-day consumer preview.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).

## Upload & setup

- Manual upload. **1 pricing zone = Base.**
- Details: **hidden in hosted and distribution**; no theme; 1-day consumer preview. Check sessions. Add all stores.
- Click Items in the pricing zone to check dates and make sure nothing is cut off. **Mark vendors High.** Complete Setup QC.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON):**
- **Include:** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Exclude:** packaged deals.
- Box all items attached to a price; include as much of the image as possible. **If multiple items share one price, put them all in the same box.** The last page usually requires boxing with URLs.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc required):**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is Box-specific.
- **Name ONLY in the name field — the description should be left blank there.** Whatever is described below the bolded name can be used as the Description.

## Post-processing (owned by DOC)

- **URL/Links QC — last page links:** TikTok, Local Grocery (delivery/pick-up), Lunchline (lunch pick of the week), Gift (shop), Cooking (get_cooking). The middle item on the last page sometimes changes.
  - **⚠️ The "RECIPE HERE" image URL is updated week over week** — refer to the Pete's Frootique link document each week for the current URL. Tag as "Link."
- **FQC:** mark autostack spotcheck complete; ensure Key Messages contain **"Weekly Specials"** in the EN fields (Overview → Edit Details → show/hide rarely-used fields).
  - Legibility heights 40/35; item image QC (clean images for all items); thumbnails Standard 4 + `first_page_thumbnail_400w` (note "complete" in comments); page categories; QC categories; add links from URL/Links QC.
  - Check sessions and verify links.
  - **⚠️ lb price must be the main price with "lb" as the postfix; the kg price must go in the description for all produce, meat and seafood items.**

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by Flex).
- **Out-of-processing:** page swaps (see OneGuide video folder).

---
*Source: Pete's Frootique OneGuide (Google Doc `1fVCt2A4Dan7sjJbt2k_rb9BQwwkFV-Hu2zbeTN7DG5w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Petland — Processing Guide

> **Source:** Petland OneGuide (Google Doc `1Bz3wUl_aFf_wBMICMXvm0eMkd0DgybzDLkqL_yWB4ow`), updated Jul 22, 2024. Contacts/credentials omitted.

> **Note:** This OneGuide is largely an unfilled template (placeholder Slack channels, hosted URL, and QC examples). Only the real, filled-in account facts are captured below.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (retailer channel not filled in) |
| Flyer types & cadence | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex does Flyer Review & Setup; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Workflow:** Upload & Setup (Flex) → FQC (Flex).

## Upload & setup (owned by Flex)

- Files sent via email.
- **1 zone, English, containing all pages and assigned all stores.**
- Confirm all items in the Setup QC checklist are correct.

## QC specifics

**Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF):**
- Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

**Tag / Tag QC (Low; Auto-tag OFF):**
- Include: name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **No brand. Exclude valid dates.**

## Flyer Review

- **Type: Lite** (owned by Flex). No special risk items — use generic flyer review standards.

---
*Source: Petland OneGuide (Google Doc `1Bz3wUl_aFf_wBMICMXvm0eMkd0DgybzDLkqL_yWB4ow`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# PetSmart Canada — Processing Guide

> **Source:** PetSmart Canada OneGuide (Google Doc `1L6F2uSm19mIlJnoqA6oRca72oMCnxSzwxn4TRgdl5uM`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | **Tier 1 Premium** |
| Availability | All platforms |
| Slack channels | `#petsmart-can` |
| Hosted URL | pets.petsmart.com/local-ad/canada.shtml |
| Flyer types | Monthly Flyer (8047) · Weekend Flyer (131) · Lookbooks (109) |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Files & schedule

- **When files arrive:** Monday. All 3 publications get a 1-day preview (communicated via email).
  - **Monthly (ML)** = the "weekly" · **Lookbooks** = ad-hocs · **Weekend flyer** = anything that isn't ML or Lookbook.
- **Bilingual account** — EN and FR pages/pricing zones (**163 stores total**).
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## Upload & setup (owned by DOC)

- Pages → Edit → select the ad folder → add English pages → **re-upload the same pages and mark them French** → auto-group all pages → save and complete.
- Create **EN** and **FR** pricing zones; add all 163 stores.
- **Linking document (via email):** open in Google Sheets, add a column to the right of "offer"; label the offer column "English" and the new column "FR translation." Use `=GOOGLETRANSLATE(cell,"en","fr")` down the column, then copy/paste as values. Replace any text in the JBP column with "Y" (leave blank cells blank). Append "EN and FR" to the document name, download as `.xlsx`, attach to all vendor tasks.
- Apply tracking codes and tracking URLs (can be done at FQC).

### Setup QC (owned by DOC)
- Standard 4 thumbnails.
- **UTM campaign codes** vary per publication (tracked in the campaign sheet; ad types colour-coded: green = Monthlong Planners, yellow = ad-hoc Lookbooks, blue = Weekend Events). To find the code, copy the last code for that flyer type and increment the trailing digit (e.g. `ca-mplan-fy25p2` → `ca-mplan-fy25p3`). Apply as: Code Type Dynamic Variable, Source Distribution, Variable `utm_campaign`, Value from the sheet.
- **Tracking URLs (do NOT change):** apply the Impression, Open, and Engagement DoubleClick URLs (Flipp App) — grab them from a previous live flyer.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF; linking doc required):**
- **Include:** retailer logo, sign-up page, social media (Instagram/TikTok/Facebook PetSmart Canada), special weblinks.
- **Exclude:** coupons, packaged deals.
- Items with "Y" in the JBP offer column get one box around every item. **Treats Rewards pages:** one item box around the image and one text box around the product description, consistently across the page; a "5X points" callout on a new line in the linking doc must be boxed itself. Ecomm flyers that don't meet content policy — box so they do and tag using the linking-doc links (Display Type Item).

**Tag / Tag QC (Low; Auto-tag ON; linking doc required):**
- Include: name, description, price, sale story, categories, disclaimer, original price, URLs. Brand is Box-specific. **Exclude pre/postfix, valid dates, SKU.**
- **JBP Offer custom field:** for all item names with "Y" in the JBP Offer column, tag "Y" in the JBP field at the bottom of the tagging interface (EN and FR); Display Type Item even if it's just a URL.
- **Brand:** from the linking doc; if "N/A" don't tag; if "Various" don't tag the brand field.
- **Name:** use English Item Name for EN pages and French Translation Item Name for FR pages — **the PDF shows English but FR pages must be tagged with the French translation.**
- **Description:** add the measurement (kg, g, lb, etc.) from the linking doc.
- **⚠️ #1 risk — price ranges:** tag the *lower* value as Current Price and *-upper* value in the postfix. **Do NOT put the range in the sale story** (e.g. $14.99–19.99 → Current Price $14.99, Postfix -19.99).
- **Sale Story (Ecomm Event only):** for shop-animal banners at the bottom, tag with the big sale story ("Spend $100+ Save…") plus the disclaimer to meet CP (Display Type Item).

**Image QC:** use cutouts for ad blocks with multi-items; clean PDFs where available for single-item ad cells.

## Final QC (owned by DOC)

- Item Search — Name Contains "Dog"/"Cat"/"Small Pet"/"Fish"/"Bird"/"Reptile", Language French: ensure no truly-English item names (brand names like "Tiki Dog" are OK to skip); fix true English results via Google Translate.
- Item Search — Sale Story Contains "-", all languages: **ensure no price ranges are tagged in the sale story** (must use Current Price + Postfix).
- QC categories complete; image QC (cutouts for multi-item cells); tracking codes (Dynamic Variable → Distribution → `utm_campaign`); tracking URLs (same 3 for all pubs). Apply any triggers for alternate covers/pages/inserts.
- **Assign FSAs from CSV:** System → custom actions → assign FSAs from CSV, using the template; update flyer_id columns with EN and FR PZ IDs, download each as its own CSV, **run the custom action twice** (both zones; should yield 1675 FSAs). **Re-run after any page swaps.**
- Complete FQC; send a preview email listing publication + preview link, live/valid dates, and ad title (external run name); action revisions.

### Monthlong Planners only
- For the Week 1 / Hosted flyer, create triggers to **hide in Flipp** and **hide in distribution**, effective the first Sunday at 11:59 pm after week 1. Don't change valid dates (Hosted runs the full duration).
- Every Friday, **clone** the monthly publications (name them week 2, 3, 4…), select **copy tracking codes**, change available dates Monday–Sunday, hide hosted for clones (valid dates unchanged), and create triggers for the clones (they don't copy over). Reassign FSAs if page changes are made.

## Flyer Review

- **Type: Lite** (owned by Flex).

---
*Source: PetSmart Canada OneGuide (Google Doc `1L6F2uSm19mIlJnoqA6oRca72oMCnxSzwxn4TRgdl5uM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pharmachoice & RxHealthMed — Processing Guide

> **Source:** Pharmachoice & RxHealthMed OneGuide (Google Doc `1QsQpcHFXqJDGClOjRRRsMiGNC4ASXY5yQTb50l-8-n8`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms — **except** flyers labelled "No Promo" and/or with fewer than 6 items, which are **Hosted only** |
| Slack channel(s) | `#pharmachoice` |
| Hosted URL | Pharmachoice via merchant portal; RxHealthMed rxhealthmed.ca |
| Flyer types | **Pharmachoice:** Flyer (#3167), Health Centre Flyer (#5691) · **RxHealthMed:** Weekly Flyer (#7272) |
| Processing | Auto-stack; Flex (Processing Support / FAB tickets); no coupons; Strategic Ops (Feedel/retailer data services) |

There are **4 flyer categories**: FL (Flyer), HC (Health Centre), No Promo, and RX HealthMed. FL/HC/No Promo live under the PharmaChoice merchant page; RX HealthMed has its own merchant page. HC and RX HealthMed do **not** follow the same cadence as Pharmachoice — the codesheet shows if they're included that week.

## Files & schedule

- **Files received:** Monday. All assets sent together — you must **clear the RX HealthMed FTP of Pharmachoice files** once uploaded.
- **Publication cadence:** Available From Thu, Valid From Thu; Available To Wed, Valid To Wed.
- **No Promo files** drop at the top of the month and run every week; the codesheet pulls the relevant files for that specific week (not all pages used every week).
- **Linking document:** required, split by FL / HC / RX. No-Promo runs use that month's No-Promo linking doc. HHC does **not** get a linking doc — note "no linking document" in the vendor-task comments.
- **Workflow owners:** Upload/Setup = Vendor/Flex; Image QC = Flex; FQC = DOC/Vendor.

## Upload & setup

1. Download the codesheet from the FTP.
2. **RISK 1:** ensure each page name starts with `_p` — add it if missing (Ctrl+F).
3. **RISK 2:** No Promo pages end with `_0001` (or a variant) — replace with the naming convention seen in the FTP.
4. In Excel, append `.pdf` to every page in the FL/HC/RX zone (the OneGuide provides a short VBA macro for this).
5. **Split into FL, HC, No Promo, and RX** — each runs into its own flyer shell. Copy/paste into separate sheets (include the header). FL and HC can share a tab but must be separated. Download each as its own CSV.
6. **Upload the codesheet:**
   - **Config name: `generic`**
   - PDF Base Directory: take directly from the FTP path.
   - **Toggles: 2nd and last unchecked.**
   - Save.
7. Process the codesheet. Let sessions run.
8. Upload the (split) linking documents to the vendor tasks.

### Config / base-directory notes
- **FL, HC, HHC, RX share the same PDF base directory; No Promo has a different basepath.** For No Promo, search "No Promo" in the FTP and copy the base path from the latest month — verify against the page/zone name in the codesheet (e.g. an "April No Promo" page uses the April basepath).
- Match the week number: flyer shell week number must match the FTP files (e.g. PC17 pages ↔ PC17 shell).
- Confirm the RxHealthMed pages aren't labelled `Month_RxHM_No Promo` before applying standard settings — those follow the No-Promo settings instead.

### Setup QC / Edit Details
- **FL, HC, HHC, RxHM runs:** Available Wed→Thu, Valid Wed→Wed; Internal Run Name `PC XX - <flyer type>`; no external run name; no preview start date; **Distribution: available everywhere** (no theme).
- **No Promo runs:** same dates; Internal Run Name `PC XX - No Promo`; **Distribution: Hosted only.**
- Thumbnails: **Standard 4** (leg heights preset 45/30).

### ⚠️ Common errors / risk items (retailer-specific)
- **Codesheet base directory:** FL/HC/RX same base directory; No Promo different — mixing these up is the top risk.
- **Toggles:** No Promo flyers are **Hosted only** — do not leave them available everywhere.
- Page names must start with `_p`; No Promo suffixes (`_0001`) must be renamed to the FTP convention.
- No Promo codesheets may run **yellow** with a "files uploaded" warning — this is safe to ignore; you can "force process."
- **Store errors on process:** stores may need to be added (Fadmin names the exact store codes). Cross-reference the Reebee booking list for the store code; escalate to the Reebee equivalent if not found.
- **Linking doc too large to attach:** email it to the OS vendor instead (recipients in the OneGuide) with the run ID and run link.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block that has a price or sales story individually; if one price applies to multiple items in a block, box them together as one.
- Box banners with call-to-actions (look for the **red rectangle** to identify the CTA).
- Box the flyer location page and the `pharmachoice.com` banner.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.
- Tag name/brand/description/pre-postfix/valid dates/sale story as seen in flyer; price/original price if available.
- **URLs:** apply strictly per the linking document.
- **Disclaimer:** only enter if it's **within the drawn box** — do not use a page-bottom disclaimer.
- Categories: pick the closest category (chart in the OneGuide).

### Image QC
- Prioritize the PDF image; filter for cutouts and no-images. **No Promo flyers do NOT get Image QC.**

## Final QC (owned by DOC/Vendor)
1. Spotcheck; mark Auto-Stack Spotcheck complete.
2. Image QC (No Promo excluded).
3. QC categories — check all pages; a better category often applies (No Promo excluded).
4. Verify every URL against the linking document.
5. Rerun sessions as needed; verify links; mark items store-only.
6. FQC checklist.
- Flyer Review type: **Lite.**

## Out-of-processing
- See the retailer's 2025 Black Friday operations guidelines (linked in the OneGuide) for publication & ad-hoc request handling.
- Email communications for this account are owned internally (not stored here).

*Note: FTP file-transfer credentials appear in the OneGuide — not stored here (credentials in the OneGuide — not stored here).*

---
*Source: Pharmachoice & RxHealthMed OneGuide (Google Doc `1QsQpcHFXqJDGClOjRRRsMiGNC4ASXY5yQTb50l-8-n8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pharmasave — Processing Guide

> **Source:** Pharmasave OneGuide (Google Doc `1UsAEhoYT8Jx98NuNKrc50EdQKlgNunfJVmn2fwjSBBo`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#pharmasave`, `#pharmasave-scp` |
| Hosted URL | pharmasave.com/flyer/ |
| Flyer types | **Weekly Flyer** (3547 — zones F0, CM, GG, SS, CI) · **Bi-Weekly Medium/Dispensary** (FM, FD) · **West Weekly Flyer** clone (7633) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; Strategic Ops = No (Weekly) / Yes-Feedel (FM/FD) |

Two processing tracks: the **Weekly** flyer (cloned to West after FQC) and the **Bi-Weekly** FM/FD flyers (never cloned).

## Files & schedule

- **Weekly:** files received Thursday. Available From Thu, Valid From Fri; Available/Valid To following Thu (1-week run).
- **Bi-Weekly (FM/FD):** files received Friday. Available From Thu, Valid From Fri; Available/Valid To 2-weeks-Thursday (2-week run) — but only shows **1 week on Flipp**, full 2 weeks on Hosted (trigger required, see below).
- **Linking document:** none — but a **Schematic** (from FTP) carries insert links and must be attached to vendor tasks (new Jan 2025).
- **Workflow owners:** Weekly Upload/Setup = Vendor; Bi-Weekly Upload = Flex; Image QC = Flex; FQC = DOC.

## Upload & setup

### Weekly (config `generic`)
- Only upload under **Flyer Type 3547 - Weekly Flyer** — **do NOT** upload under the WEST run 7633. West is **cloned** from 3547 after all FQC steps (avoids double processing).
- FTP → search "Schematic" → download the Weekly codesheet (e.g. `Digital Schematic 24F006.xlsx`). Confirm run dates match the schematic.
- **Find & Replace:** `Regional_eFlyerSignupCreative_V3.pdf` → `Regional_eFlyerSignupCreative_V3.pdf.pdf`.
- Delete the extra info (links & dates) at the bottom of the codesheet. Save as CSV.
- Upload: Config **`generic`**, PDF Base Directory from FTP, **toggles checked: Store Assignment, Page Upload, PZ Creation, Page Pool, Combine Zones.** Save & Process. Mark Schematic uploaded in FTP.
- Confirm PZ count matches codesheet; mark "Flyer Creation" complete.
- **Setup QC:** Internal Run Name `YEARF0WEEK#` (e.g. 23F028); External Run Name "Weekly Flyer"; no theme, no preview date; all platforms; Standard 4 thumbnails. Attach Schematic sheet to vendor tasks. Geography tab shows added stores — OK to ignore.

### Bi-Weekly FM/FD (config `Generic`)
- FTP → search "Schematic" → download FM/FD codesheet (e.g. `Digital Schematic 24FM07.xlsx`). Same Find & Replace and bottom-info deletion; save CSV.
- Upload: Config **`Generic`**, base directory from FTP, **same 5 toggles** (Store Assignment, Page Upload, PZ Creation, Page Pool, Combine Zones). Save & Process.
- Common warning "Pages already uploaded" — **OK to ignore** (inserts are shared across Weekly/FM/FD).
- **Setup QC:** Internal Run Name `YEARFM/FDWEEK#`; no external run name; 2-week dates; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)
- **Store Selector / Store Closures:** Pharmasave store updates run only **once a day at 3am.** For a closure you **must backdate the Valid To date in Fadmin**, or the store selector delays the closure and **the retailer will always flag it** (e.g. request received Aug 29 → Fadmin date Aug 28).
- **Merged Pages:** insert pages are often larger than regular pages, so Fadmin **merges pages together.** At FQC / Storefront Spotcheck you must **unmerge** (select "Don't Merge" on every merged page). Do this per pricing zone.
- **Sign Up / "Sign Up & Save" insert:** tag as **"Show URL in iFrame"** (NOT Link) — Name "Sign Up", iFrame width 360, height 568.
- **Coupons:** must be tagged with item type **Coupon**, not as items; do not use PDF image; confirm valid dates.
- **Bi-Weekly hide-on-Flipp trigger:** FM/FD must be hidden on Flipp after week 1. Set trigger(s) — Trigger On: Flyer Run, Action: Update Attribute, Attribute: **Hide on Flipp** (and Hide in Distribution at setup), runs Thursday 12:00 AM. Create an OPTICS ticket to confirm the trigger ran; after it runs, confirm on Flipp via a Geography postal code that the flyer is hidden.

## QC specifics

### Box Draw (Weekly = Medium, FM/FD = Low — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo (Box QC-specific), sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Box all items separately; each item with a price boxed on its own; text boxes only if necessary.
- Special weblinks per the attachment (PDF names are far right in the schematic sheet).

### Tag / Tag QC (Low — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name (include brand in name), brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, URLs. **Exclude:** SKU, original price.
- Tag everything as seen on the PDF. Sale story as-is (e.g. "20% off").
- **URLs:** use the attachment — match the PDF name to its URL. AirMiles offers link to the AirMiles Pharmasave partner page; Sign Up page uses "Show URL in Frame" (see risk items).

### Image QC (owned by Flex/DOC)
- Prefer a PDF-extracted or composite image. **Unselect** Composites, PDFs, and Data Piped in the QC filter; grouping of items → leave as cutout; single item + clean PDF → use PDF image. (FM/FD leg heights 40/30.)

## Final QC & cloning
- Confirm dates & external run name; mark Auto-Stack Spotcheck complete.
- **Unmerge merged pages** (Storefront Spotcheck); verify coupons; verify URLs.
- **Weekly cloning to West** (also applies to Holiday Gift Guides, Super Savings Events, Cosmetics — NOT FM/FD):
  1. Complete Weekly FQC and mark **Auto Judge Go Live** complete **before** cloning.
  2. Overview → Clone → to "PharmaSave - West Weekly Flyer & Coupons" → select run (week code + WEST).
  3. On the clone (7633): set dates, Internal Run Name `YEARF0WEEK# WEST`, unmerge pages, verify URLs, **delete EAST pricing zones**, check Geo, complete FQC.
  4. Back on the Weekly run: remove stores from WEST pricing zones (Pricing Zones → West → Stores → Remove All). If a West PZ was deleted in the clone, re-run the codesheet to fix.
- **FM/FD:** do NOT clone. Set the hide-on-Flipp trigger + OPTICS ticket, then do the post-live trigger check.
- Flyer Review type: **Lite.**

---
*Source: Pharmasave OneGuide (Google Doc `1UsAEhoYT8Jx98NuNKrc50EdQKlgNunfJVmn2fwjSBBo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Piggly Wiggly Carolina — Processing Guide

> **Source:** Piggly Wiggly Carolina OneGuide (Google Doc `1uGGMKqF9BYcbA9UnmGQVWv1hJGq6phD8MwbWZBZAGRM`). Contacts/credentials omitted.

A Vendor Solutions grocery account with a codesheet built from an `.ods` versions file.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | (not specified) |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Publication cadence:** Available From Mon, Available To Mon; Valid From Tue, Valid To Tue.
- **Linking document:** N/A.
- **Workflow owners:** Upload/Setup = Vendor; Image QC = Flex; FQC = DOC.

## Upload & setup (config `generic`)

1. In the Piggly Wiggly Carolina FTP, find the `.ods` file whose name matches the run live date (e.g. `VERSIONS.6.11.25.ods` for the June 11 publication).
2. Import the `.ods` into a new spreadsheet. Delete any rows/columns with no pages.
3. **Codesheet manipulation:**
   - Ensure every page ends with `.pdf` so the codesheet uploads properly.
   - **Delete duplicate rows** — e.g. if there are 5 rows of Kinston stores, note the deleted stores and delete 4 of them **for now.**
4. Save as CSV and upload: Name = anything, **Config = `generic`**, PDF base directory = basepath from the `.ods`, **2nd and last box unchecked.**
5. Once processed, mark off flyer creation and **add back the deleted rows** from step 3.
6. Set the flyer run as **hidden in hosted.** Complete Setup QC.

### ⚠️ Common errors / risk items (retailer-specific)
- **"Reused PDFs in multiple zones" backtrace error:** caused by NOT deleting the duplicated pricing-zone rows during step 3. Delete duplicates before processing, then add them back after.
- **Look for multiple products** in a block.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box OFF, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block individually. If a block has multiple prices for an item, box individually and use text boxes as required.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** pre/postfix, valid dates, price, categories, disclaimer, original price. **Exclude:** brand, name, description, SKU, sale story, URLs.
- **Description:** enter as it appears in the flyer (unless it would violate the "Name" rules). When there are multiple brands, do **NOT** enter in the Brand field — put into the Name field.

### Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted.

## Final QC (owned by DOC)
- Confirm dates (per PDF) and availability toggles; thumbnails include retailer logo.
- All items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions complete.
- **Geography changes week over week — this can be ignored.**
- Flyer Review type: **Lite.**

---
*Source: Piggly Wiggly Carolina OneGuide (Google Doc `1uGGMKqF9BYcbA9UnmGQVWv1hJGq6phD8MwbWZBZAGRM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Piggly Wiggly Midwest — Processing Guide

> **Source:** Piggly Wiggly Midwest OneGuide (Google Doc `134ydWUc92LP3e3QZlVF_TNv32kDSgtttYS10aZJ_SQ8`), updated Mar 5, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | shopthepig.com |
| Flyer types | Weekly Ad — **2 ads a week** (Monday ad + Wednesday ad) |
| Processing | Auto-stack; Flex (3FL); no coupons, no Feedel |

Files received **Tuesday**. Works with Mercatus (third party).

## Files & schedule
- **Monday ad:** Available Mon → Mon; Valid Tue → Mon.
- **Wednesday ad:** Available Mon → Tue; Valid Wed → Tue.
- No preview, no linking document. **Pages are shared between the two ads.**

## Upload & setup (Flex) — generic codesheet
- Merchant Details → View Files → download the codesheet XLSX (labeled with the date, e.g. "Ad version 05-27-24.xlsx").
- Open the version doc in Google Sheets and open a **second** sheet. In the second sheet create a **"Wednesday"** tab with headers (in order): **Version, Stores, Page 1 … Page X** (as many Page headers as the version doc lists).
  - Copy version numbers into Version, "Store Region" info into Stores, pages into the Pages columns; number the versions 1–#. Repeat for the second table on the version doc.
- Save & Confirm — **do NOT Process Internally.** Save each tab as its own CSV.
- **Codesheet upload:** Name "Wednesday"; config **`generic`**; PDF base directory = the full file path in the SFTP (e.g. `/Reebee+07-15-2024`), double-check no extra spaces. **Uncheck toggles 2 (region assignment) and 7 (combine zones).**
- **⚠️ When uploading the Tuesday ad you'll get a "pages previously uploaded" warning — this is OK (pages are shared). Force Processing for Tuesday.** Once both codesheets complete, mark Flyer Creation complete.

### Setup QC (DOC)
- Confirm no pages left in the FTP. **Mark all vendor tasks as URGENT** (Vendors tab → select all → Urgency "Yes" → Reassign). Confirm flyer dates on the first page — **⚠️ the Monday-live (Tuesday-valid) ad's first page will NOT include a date range, and that's OK.** Tuesday ad's "pages previously uploaded" warning → OK to toggle "Code Sheets ran correctly".

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **ON**): one item per box; sub-item pricing boxed. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks (and CTAs/sale call-outs).
- **Tag / Tag QC** (Low; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / Flyer Review (DOC)
- Confirm dates vs PDF; availability everywhere; thumbnails include logo (Standard 4); **legibility heights 60/40**; Pages tab has no box-draw errors; no theme.
- **Geography:** ⚠️ there are **2 flyer runs** — compare against the correct run from the previous week.
- **Flyer Review type: Lite.**

---
*Source: Piggly Wiggly Midwest OneGuide (Google Doc `134ydWUc92LP3e3QZlVF_TNv32kDSgtttYS10aZJ_SQ8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pisces Pet Emporium — Processing Guide

> **Source:** Pisces Pet Emporium OneGuide (Google Doc `1oN_uAOjPV3K8h1iJPppOzv2lUxTgH68hLZPPrHgY-j4`). Contacts/credentials omitted.

A Vendor Solutions / simple-retailer account. This OneGuide is mostly the standard simple-retailer template; the real account facts are captured below.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Flipp Basic |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer type(s) | Flyer Type 1: Flyer (12281) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Monday (pages may need to be added to the SFTP by the processor if the client sends files over email).
- **Publication cadence:** Available From Fri, Valid From Fri; Available To Thu, Valid To Thu.
- **Linking document:** Yes — labelled `URL Document Template Flyer Week [week].xlsx` on the SFTP; attach to the pipeline.
- **Workflow owners:** Upload/Setup and FQC = DOC.

## Upload & setup (owned by Flex)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Once listed, Auto-Group (or enter page numbers manually) and confirm the correct language. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all applicable stores.
- **Attach linking document** (from SFTP) to the pipeline; mass-attach the URL document to all processing steps (Box, Tag, Tag QC).

### ⚠️ Common errors / risk items (retailer-specific)
- **RISK — SFTP upload:** confirm there are no pages left in the SFTP that weren't uploaded (Pricing Zone Tab → Items View).
- Confirm flyer dates (usually on the first or last page of the flyer).
- Ensure all preview dates are set; thumbnails Standard 4.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- Linking document used for both Box and Tag.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block with a price.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.

### Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted. Item Image QC (post-processing) is **not required**.

## Final QC (owned by Flex)
- Confirm dates (per PDF) and availability toggles; thumbnails correct and include retailer logo.
- All items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- Flyer Review type: **Lite.**

---
*Source: Pisces Pet Emporium OneGuide (Google Doc `1oN_uAOjPV3K8h1iJPppOzv2lUxTgH68hLZPPrHgY-j4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Plomberie Mascouche — Processing Guide

> **Source:** Plomberie Mascouche OneGuide (Google Doc `1S4qbOpHblK2ngv2TTMo6yMn0_ljR1YTiE4qrP-KgsZw`). Contacts/credentials omitted.

A small Vendor Solutions account processed largely from emailed assets. French-only pages.

## Account at a glance

| | |
|---|---|
| Account segment / tier | N/A (Vendor Solutions) |
| Availability | All platforms |
| Slack channel(s) | N/A |
| Hosted URL | plomberiemascouche.ca/en |
| Flyer type(s) | Flyer Type 1: Seasonal |
| Processing | Auto-stack; no Flex; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Ad hoc — PDFs provided by the retailer contact via email (may include run dates if no shell exists in Fadmin yet).
- **Publication cadence:** Available From / Valid From Thursday.
- **Preview:** N/A.
- **Linking document:** Yes.
- **Workflow owners:** Upload/Setup and FQC = DOC.

## Upload & setup (owned by DOC)

- Download the emailed PDF assets, then log into the **Plomberie Mascouche SFTP** (username `plomberiemascouche`). Create a new folder or transfer the combined PDF into the FTP.
- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu → Autogroup pages (**French pages only**). Save & Confirm — **do NOT process internally.**
- **Pricing zone:** one version, called **Base**; Save & Confirm; add all applicable stores (**2 stores**).
- **Setup QC:** confirm all pages uploaded (Pricing Zone Tab → Items View); confirm dates (on first page of flyer); Standard 4 thumbnails; **no theme, no external run name.**

### ⚠️ Common errors / risk items (retailer-specific)
- **SFTP upload:** confirm no pages remain in the SFTP that weren't uploaded.
- Autogroup **French pages only.**
- Legibility heights 60/40.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- Linking document required (Box Draw/Box QC specific).
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box all single items. Some pages need non-items boxed for CTA links — **defer to the link document** for these callouts.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **SKU:** include if available.
- Ensure every boxed item has its correct URL; CTA non-item boxes get URLs from the link document.

### Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted.

## Final QC (owned by DOC)
- Confirm dates (per PDF) and availability toggles; thumbnails include retailer logo; legibility heights 60/40.
- All items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions complete; geography correct (no extra boxes from the autobox process).
- Flyer Review type: **Lite.**

---
*Source: Plomberie Mascouche OneGuide (Google Doc `1S4qbOpHblK2ngv2TTMo6yMn0_ljR1YTiE4qrP-KgsZw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Potvin & Bouchard — Processing Guide

> **Source:** Potvin & Bouchard OneGuide (Google Doc `1_ZeefJXPI1iDBqqFBEyhlIDE1c0_jg2okWAxHnuyFJs`). Contacts/credentials omitted.

A BMR-family Vendor Solutions account (page names prefixed **PB**). French-primary with cross-languaged English.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Vendor Solutions (see BMR Account Guide, Confluence OP) |
| Availability | All platforms |
| Slack channel(s) | `#bmr` |
| Hosted URL | potvinbouchard.ca |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex N/A; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Wed, Valid From Thu; Available To Wed, Valid To Wed. Set "Available From" one day before "Valid From" (Wednesday).
- **Preview:** Wednesday for the Weekly Ad.
- **Linking document:** an "EXTRA URLS" document (from FTP, labelled **PB**).
- **Workflow owners:** Upload/Setup = Vendor; Image QC = Flex; FQC = DOC/Vendor.

## Upload & setup

1. Identify the correct week's folder for the run.
2. **Select all lowercase files** (uppercase files are the whole flyer, not individual pages). **Page names must start with `PB` — NOT `BMR`.**
3. Auto-group pages; set language to match the files — **PB only has FR files, so assign all pages to French.**
4. Create **2 pricing zones: FR and EN.** EN is cross-languaged: select French, check "Cross language?", then select English to set the English PZ.
5. Add all stores to both zones (PB typically has **4 stores** week over week — confirm against the Runlist in the FTP).
6. If there is an "Extra URL" file on the FTP (labelled **PB**), download and **mass-attach to all vendor tasks.**
7. Standard 4 thumbnails.
8. Overview: theme **Proudly Canadian** (if unavailable, No Theme); available everywhere.

### ⚠️ Common errors / risk items (retailer-specific)
- **Use the `PB` prefix, not `BMR`** — the account shares the BMR family but page names differ.
- Select **lowercase** files only (uppercase = full flyer, not pages).
- Only FR files exist — assign all pages French, then cross-language to build the EN zone.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- Linking document (Tag/QC specific) used.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Items with multiple products/prices: draw separate boxes with respective text boxes (A/B).

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Tag in FRENCH.** For multi-product/price items, tag using the matching text info. Tag links using the attached URL sheet.

### Image QC
- Owned by Vendor; choose the cleanest/most relevant image.

## Final QC (owned by Vendor)
- Flyer sorting; **External Run Names — French: Circulaire; English: Weekly Flyer.**
- Mark auto-stack spotcheck complete; add URLs from the URL document (usually on FTP); check dates and theme; thumbnails.
- Geography — flag if any stores added/removed; vertical & horizontal scroll interactive; ensure **flyer tracking code** is applied (saved from codesheet).
- Flyer Review owned by DOL.

## Out-of-processing
- **Flyer sorting order:** 1) BMR regular flyer, 2) BMR PRO flyer, 3) Agrizone regular flyer, 4) Agrizone guides.
- **Page swaps** follow the standard "baseline" process.

---
*Source: Potvin & Bouchard OneGuide (Google Doc `1_ZeefJXPI1iDBqqFBEyhlIDE1c0_jg2okWAxHnuyFJs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Powell's Supermarket — Processing Guide

> **Source:** Powell's Supermarket OneGuide (Google Doc `1WEyEG-bSgd32tkUPLyz9oZshpveyxFNSi2by_EgjI2c`). Contacts/credentials omitted.

A Vendor Solutions grocery account (part of the AGD Newfoundland family).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#powells-supermarket` |
| Hosted URL | (not specified) |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Publication cadence:** Available From Wed, Valid From Thu; Available To Wed, Valid To Wed.
- **Linking document:** none.
- **Workflow owners:** Upload/Setup = Vendor; Setup QC / Image QC / FQC = Flex.

## Upload & setup

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP menu (or upload manually from email) → Confirm & Upload. Auto-Group or enter grouping numbers; ensure **language = English.** Save & Confirm.
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all stores.
- **Setup QC:** confirm all pages uploaded (Pricing Zone Tab → Items View); confirm dates (first/last page); Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)
- **Look for multiple products** in a block (drives box-draw handling).
- **SFTP upload:** confirm no pages remain in the SFTP that weren't uploaded.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Single-item blocks:** box the whole square — image, the "50% off"/"Buy 2 Get 1 FREE" text, and the product description.
- **Do NOT box** the Powell's Supermarket logo, Facebook icons, or website URLs at the top of the flyer.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, description, price, sale story, categories, disclaimer, original price. **Exclude:** valid dates, SKU, URLs.
- **Name/Brand:** name = the bolded text; brand as seen in flyer. Description = the un-bolded text after the name. Prices as seen in flyer.
- **Every item needs a category** (analytical + Google). Category chart (Flipp categories): Toys, Seasonal, Pharmacy, Pets, Outdoor Living, Home Essentials, Health & Beauty, Grocery, Grills, Gifts, Coupon, Beverages, Beer/Wine & Liquor.
- Select a clean, relevant PDF image for every item.

### Image QC
- Choose a clean white PDF where possible; otherwise a cutout.

## Final QC (owned by Flex)
1. Mark auto-stack off.
2. **Edit Details:** Available From 12am Wed / to 11:59pm Wed; Valid From 12am Thu / to 11:59pm Wed; **no external run name; no theme.**
3. Page order (noted in comments).
4. Image QC — clean PDFs where possible.
5. Category QC — Overview → Item Search; Search 1: Categories blank → fill; Search 2: Google Category blank → fill.
6. Check items for special sale dates (Storefront spotcheck).
7. Thumbnails (4 standard); check previews.
8. Geography tab — ensure no stores added/removed.
- Flyer Review type: **Lite.**

## Out-of-processing
- See the shared Value Grocer & Powell's 2025 Black Friday operations guidelines (linked in the OneGuide) for publication & ad-hoc requests.

---
*Source: Powell's Supermarket OneGuide (Google Doc `1WEyEG-bSgd32tkUPLyz9oZshpveyxFNSi2by_EgjI2c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Première-Moisson — Processing Guide

> **Source:** Première-Moisson OneGuide (Google Doc `1RosBwyKZpIYJDYdrZA_V810n_xkK4Ohq9xVFelW393Q`). Contacts/credentials omitted.

A bilingual (FR/EN) Vendor Solutions account, processed ad hoc.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 |
| Availability | All platforms |
| Slack channel(s) | `#première-moisson` |
| Hosted URL | premieremoisson.com/en |
| Flyer type(s) | Flyer (9478) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Ad hoc; all dates (available/valid from/to) are ad hoc.
- **Preview:** N/A.
- **Linking document:** Yes — attached to all tasks.
- **Workflow owners:** Upload/Setup = Flex; FQC = DOC.

## Upload & setup (owned by Flex)

- **Manual upload:** Pages interface → Edit tab → Upload Local Files → Upload Files → select the Première Moisson files. **Upload the pages twice — once for English, once for French.**
- Select the correct language for each version (ensure there is both a FR and an EN version). Input pagination order manually (1,1,2,2,3,3,4,4 …). Save and Complete.
- Once Flyer Creation is available, create **two pricing zones manually: Base EN (English) and Base FR (French).** Add all stores.

### ⚠️ Common errors / risk items (retailer-specific)
- **Bilingual pages:** items appear with FR on top and EN on the bottom — tag the correct language per the flyer/zone language.
- Pages must be uploaded twice (EN + FR) with manual pagination — a common setup slip.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand: No.
- Tag the correct language per the flyer (FR top / EN bottom).

## Final QC (owned by DOC)
- Double-check run dates; complete Standard 4 thumbnails; confirm pagination and distribution.
- Check the vertical preview — everything clickable, creative rendering as expected.
- **Items without URL:** consult the linking document to fill in outstanding links.
- Flyer Review type: **Lite.**

## Out-of-processing
- Page swaps follow the standard "baseline" process.

---
*Source: Première-Moisson OneGuide (Google Doc `1RosBwyKZpIYJDYdrZA_V810n_xkK4Ohq9xVFelW393Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# President's Choice — Processing Guide

> **Source:** President's Choice OneGuide (Google Doc `1AAAhPMsevVgLtz2MPQjP97N0UN9lNjaSeCcGo0GuaGg`). Contacts/credentials omitted.

The **PC Insiders Book** (Summer / Holiday), a bi-annual bilingual book that is processed on the President's Choice merchant and then **cloned across all Loblaws banners.** This is a high-effort account driven by a Workback Schedule (WBS).

## Account at a glance

| | |
|---|---|
| Account tier | Core+ |
| Availability | PC Insiders version = all platforms; **banner clones = Hosted only** |
| Slack channel(s) | `#lcl-pcinsiders` (cloning coordination in `#loblops`) |
| Hosted URL | pcoptimum.ca (clones posted to all Loblaws banner sites) |
| Flyer type(s) | Bi-annual: **Summer Insiders Book**, **Holiday Insiders Book** |
| Processing | Auto-stack; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** per the WBS on agreed file-drop dates. All publication dates ad hoc / per WBS.
- **Preview:** per the WBS on agreed preview-link delivery dates.
- **Workflow owners:** Upload/Setup and FQC = DOC.
- Client is being trained on the SFTP upload process (may need COC support; WeTransfer as a last resort).
- See the Flipp x SIR Workback Schedule (linked in the OneGuide) for dates.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP → Confirm & Upload → Auto-Group / enter grouping numbers → set correct language (toggle FR QC pages to French) → Save & Confirm.
- **Create 3 pricing zones** by filename:
  - **EN QC** — files with "EN QC" in the name, uploaded English → region set **Quebec - All**
  - **EN ROC** — files with "EN ROC", uploaded English → region set **Rest Of Canada**
  - **FR QC** — files with "FR QC", uploaded French → region set **Quebec - All**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (retailer/BD/WBS); Standard 4 thumbnails; set preview dates for OS processing and client link delivery.

### ⚠️ Common errors / risk items (retailer-specific)
- **Three parallel versions** (EN QC, EN ROC, FR QC) with the same items — box/tag must match across all three; discrepancies are the recurring risk.
- **Item images do not extract cleanly** — many items must be pulled from loblaws.ca post-processing (highly manual; file an ARB ticket). Not every item is available online pre-live — grab images again post-live.
- **Items on one page with details on another** (and back-page/cover items without details) are easy for OS to miss since they only see one page at a time — box/tag these yourself.
- **Cover page** sometimes has multiple versions to swap weekly via triggers + OPTICS tickets — confirm dates with the retailer.
- **Clones must be Hosted only** — double-check availability toggles on every clone.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box all Table-of-Contents pages (text AND numbered images — they link to page numbers).
- Box items whether or not they have article numbers/prices; the client wants items clickable even without a price. **When in doubt, make a box** and the full-time team reviews.
- Box items with at least a Name (and sometimes a Price) even without a SKU/article number.
- Use text boxes to associate item images with their text even when not adjacent; match flavour/type when unsure.
- If two items share a single image, box them together. Box PC Express code call-outs and full category-intro pages.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, brand, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, and **Article Number 1–4** (put the SKU into BOTH the SKU field and the Article Number fields, one per field).
- Table-of-Contents boxes → **Page Link** type, directed to the listed page (images with a number but no text also = Page Link).
- Use **bold text** in a text block as the item Name (even if not captured by the box draw). Put item size in Description; post-sale pricing (e.g. "+ tx") in Postfix.
- If two items were boxed together, include both SKUs in the Description and both Article Numbers in separate fields.
- Full-page boxes → Link type with `https://www.pcoptimum.ca/` (or the linking doc / a printed link if provided). Links are largely added post-processing.

### Image QC
- Select clean PDFs where available; otherwise leave as Cutout (grabbed from the website post-processing).

## Post-processing / Final QC (owned by DOC)

- **Item Image Override:** open all three versions of a page; search the SKU on loblaws.ca (any Loblaws banner works); Copy Image Address → paste into **Override Image URL** → Save; apply to all three versions. Recommend pre-live + post-live ARB tickets. For efficiency, export items (keep only `item_id`, `sku`, `override_image_url`, clear `item_id`) and import into every cloned run to auto-match SKUs.
- **Edit Details:** confirm dates (WBS) and toggles (PC merchant = available everywhere).
- **URLs:** Item Search → filter Item type → Multi Edit → apply the client's flyer landing page (e.g. `pcoptimum.ca/[flyer_name]`, else `pcoptimum.ca/flyers`); fill blank Article Numbers and SKUs (request missing ones from client at preview).
- Verify the 3 versions match (item counts, boxing/tagging) via Pricing Zone Item View; handle back-page items and cross-page items.
- Set Cover-page swap triggers + JIRA OPTICS tickets as needed.
- Flyer Review type: **Lite** (owned by DOL).

## Preview & cloning
- **Preview delivery:** send the preview link to the retailer contact + stakeholders + BD; ask for missing article numbers and non-item direct links; flag missing item PDFs (plan to grab on go-live day).
- **Post-FQC cloning to other Loblaws merchants:** only clone after all base-version updates are made (post-clone changes must be applied to all versions). Clones are **hidden on Flipp / available on Hosted** (also lets the PC Optimum app find them via API). Clone to the **General Merchandise** flyer type (or a prior Insiders Book type).
  - The **back cover (EN ROC version)** is the source of truth for which banners get which zones. Banners listed on the EN ROC back cover (No Frills, Real Canadian Superstore, Real Atlantic Superstore, Loblaws, Fortinos, Independent City Market, Valu-Mart, Zehrs, Loblaws City Market, Shoppers Drug Mart, Maxi) get the EN ROC version in English; bilingual banners also get an **EN ROC FR** cross-language zone. EN QC / FR QC go live to Maxi, Provigo, Pharmaprix (English + French).
  - **Store assignment:** pull the store list from the most recent Weekly run (PC won't provide); build a CSV of store code + pricing zone (EN ROC / EN QC, duplicated with FR names EN ROC FR / FR QC); upload with config **`generic_stores`** and only the first toggle selected.
  - **Links per banner:** update each version so links point to that banner's site (loblaws.ca, zehrs.ca, etc.) instead of the base PC link — use Fetch, or an item import with a `=base URL + SKU` formula (e.g. `loblaws.ca/p/[SKU]`), keeping only `item_id`, `sku`, `url`. Clone the URL-updated version onward (Find & Replace the domain per banner).
  - **Re-complete each clone's FQC checklist and double-check availability toggles — clones must be Hosted only.**

---
*Source: President's Choice OneGuide (Google Doc `1AAAhPMsevVgLtz2MPQjP97N0UN9lNjaSeCcGo0GuaGg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Preston Hardware New — Processing Guide

> **Source:** Preston Hardware New OneGuide (Google Doc `1-WYFBxlzY46Ju0n227LRSk2JEgPWJPUbG60Nr8rXrW0`). Contacts/credentials omitted.

A longtail Vendor Solutions account with a single monthly flyer.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channel(s) | `#1p-preston-hardware` |
| Hosted URL | prestonhardware.com/flyer/ |
| Flyer type(s) | Flyer Type 1: Monthly Flyer |
| Processing | Auto-stack; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** ad hoc.
- **Publication cadence:** Available/Valid From the 1st of the month; Available/Valid To the last day of the month.
- **Preview:** N/A.
- **Linking document:** Yes.
- **Workflow owners:** Upload/Setup and FQC = DOC.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → find the pages matching the internal run name (e.g. "May") → select all from the SFTP menu → Confirm & Upload → Auto-Group / enter grouping numbers → language **English only** → Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all applicable stores.
- **Linking document:** search the FTP for the month's XLS link document. **If there is no link document, reach out to the retailer.**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (first/last page); Standard 4 thumbnails; set preview dates.

### ⚠️ Common errors / risk items (retailer-specific)
- **Look for multiple products** in a block.
- **SFTP upload:** confirm no pages remain in the SFTP that weren't uploaded.
- Missing month's link document → contact the retailer before proceeding.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- Linking document used for both Box and Tag.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks (logo/social correctly left un-boxed/un-tagged).

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.

### Image QC
- Standard: PDF preferred if clean, otherwise cutouts accepted.

## Final QC (owned by DOC)
- Confirm dates (first and last of the month) and availability toggles; thumbnails include retailer logo.
- All items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions complete; geography correct.
- **Items without a URL:** cross-reference the link document to ensure no link was missed during tagging.
- Flyer Review type: **Lite.**

---
*Source: Preston Hardware New OneGuide (Google Doc `1-WYFBxlzY46Ju0n227LRSk2JEgPWJPUbG60Nr8rXrW0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Price Chopper KC — Processing Guide

> **Source:** Price Chopper KC OneGuide (Google Doc `1AK2yfM6Vba_zjNRBImCJ_Kf7da4pUY6DgQIC8lGy9m4`). Contacts/credentials omitted.

A US grocery account with a distinct **St. Joseph (StJ)** pricing zone alongside the main (MO) zone.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Standard |
| Availability | All platforms |
| Slack channel(s) | `#pricechopper-kc`, `#flex-processingsupport` |
| Hosted URL | (not specified) |
| Flyer type(s) | Flyer Type 1: Weekly |
| Processing | Auto-stack; Flex (Processing Support); OS involved in Setup; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Wed, Valid From Wed; Available To Tue, Valid To Tue.
- **Linking document:** N/A per account info, but Box/Tag QC reference a Box-specific and Tag-specific linking doc.
- **Workflow owners:** Upload/Setup = Vendor; FQC = DOC/Flex.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages Tab → Edit → the folder is labelled with the publication start date (all MO pages + the StJ PZ). **You cannot auto-group — manually number the pages** to match the page name/number. Save + Complete.
- Download the **Publication Schedule** from the FTP to help build pricing zones.
- **Create 2 pricing zones:**
  - **Base** → all MO pages.
  - **StJ** → some MO pages + all StJ pages (e.g. pages 1, 2, 4, 8 = StJ, the rest = MO).
- **Stores:** Base PZ = all base stores; StJ PZ = all St. Joseph stores. Check Geo → "No Stores or FSAs/zips were added or removed!"
- **Setup QC:** confirm all pages uploaded from SFTP; **no external run name, hidden on Flipp Hosted only, no theme**; check dates against the bottom of the flyer; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)
- **St. Joseph unique pages:** the retailer sends unique pages for the St. Joseph price zone — ensure the unique page is added **only** to the StJ pricing zone, **not** in the other (Base) zone.
- Pages cannot be auto-grouped — number them manually to match the page name/number.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- Linking document required (Box Draw/Box QC specific).
- **Include:** packaged deals, retailer logo, special weblinks. **Exclude:** coupons, sign-up page, social media.
- Draw clean boxes around every item with prices; do not box sign-up promos.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude:** SKU, disclaimer, URLs.

### Image QC
- Standard (PDF preferred where reflective of the page).

## Final QC (owned by Flex)
1. Spotchecks; mark Autostack Spotcheck complete.
2. Standard 4 thumbnails.
3. **Edit Details:** no theme, no external run name, **hidden in Hosted**, dates correct, no preview.
4. Item Image QC (checking for PDFs); page categories.
5. **Double-check StJ pages** — order and correct page numbers.
6. **Geography:** if the Geo tab is green with "No Stores or FSAs/zips were added or removed!" the warning is safe to ignore; if that message is absent, email the full-time team.
7. Verify links (if any); no errors on front page.
- Flyer Review type: **Lite.**

## Out-of-processing
- See the Price Chopper KC 2025 Black Friday operations guidelines (linked in the OneGuide) for publication & ad-hoc requests.

---
*Source: Price Chopper KC OneGuide (Google Doc `1AK2yfM6Vba_zjNRBImCJ_Kf7da4pUY6DgQIC8lGy9m4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Price Chopper USA — Processing Guide

> **Source:** Price Chopper USA OneGuide (Google Doc `1UYE6CW4B8lzGFxB0SuOYWj7pvfcxPb_xHJ2bLt3AmZA`). Contacts/credentials omitted.

A US grocery account (Tier 1). Weekly flyer processed via a **generic codesheet**; a secondary "PICS/other" flyer type is manual.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 |
| Availability | All platforms |
| Slack channel(s) | `#pricechopperusa`, `#pricechopperusa-scp` |
| Hosted URL | pricechopper.com/digital-flyer/ |
| Flyer type(s) | Flyer Type 1: Weekly · Flyer Type 2: PICS/other |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Sat, Valid From Sun; Available To Sat, Valid To Sat.
- **Preview:** Saturday.
- **Linking document:** none.
- **Workflow owners:** Upload/Setup = DOC; Image QC = Flex; FQC = Vendor (Flex usually completes but must be bumped).

## Upload & setup (owned by DOC)

### Weekly (config `generic`)
- Open the "Generic Codesheet Price Chopper USA.xlsx" that matches the week's page count.
- **Find & Replace the date** (e.g. filename `092723` → use that date).
- **Copy pages from zone 11 to zone 11c.** Save locally as CSV.
- Upload: **Config `generic`**, PDF Base Directory copied from Stale, **toggles: check 1, 3, 4, 6 (leave 2, 5, 7 unchecked).**
- Flex upload team: check the Geography tab — flag any discrepancy vs. the previous week's distribution to the account DOL.

### PICS / other
- Retailer sends the file or uploads to FTP → manual upload; attach any linking doc to the vendor task, else complete setup QC.

### Setup QC
- **Weekly:** Geography — no stores added; Vendor tab — Box Draw ready, no linking doc; sessions run; pricing zone pages normally ~16–20 (all zones same page count); **Edit Details — available Saturday (one day before valid Sunday), no retailer preview, available everywhere, grocery generally no theme.**
- **PICS:** one pricing zone with all stores; dates from email (else confirm with merchant); **available on Hosted only.**

### ⚠️ Common errors / risk items (retailer-specific)
- **Weekly codesheet:** must copy pages from **zone 11 → zone 11c** and set the correct date via Find & Replace before saving.
- **Toggles 1/3/4/6 only** — checking 2, 5, or 7 is a setup error.
- **Geography discrepancy vs. prior week** → flag to the DOL.
- **Box-draw risk (FQC):** OS sometimes doesn't box smaller sub-items separately — fix manually in Pages.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product with a price individually; in a block with multiple differently-priced items, box individually.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select OFF)
- **Include:** name, brand, pre/postfix, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs. **Valid dates:** include only if different from the publication date.
- Tag all fields as seen on the page; pick the best category.

### Image QC
- Select white-background images where possible, otherwise cutouts.

## Final QC (owned by Vendor)
- Geography — no stores added; Codesheet tab all green; sessions run.
- **Pricing zone:** sort zones most→least items; click "items" and scroll to confirm items are drawn correctly (watch for un-boxed smaller sub-items). Fix incorrect tags manually in Pages.
- Flyer Review type: **Lite.**

## Out-of-processing
- **Flyer sorting:** weekly flyer first unless PICS/other ads exist and the retailer specifies a different order.
- **Checkered email (every Wednesday by EOD):** confirm all files received / no missing pages, stating the number of zones and pages and the Saturday-preview / Sunday-valid setup (recipient list in the OneGuide — not stored here).

---
*Source: Price Chopper USA OneGuide (Google Doc `1UYE6CW4B8lzGFxB0SuOYWj7pvfcxPb_xHJ2bLt3AmZA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Price Less IGA — Processing Guide

> **Source:** Price Less IGA OneGuide (Google Doc `1nzDnoGoU5JyvGErhCGy2wC-3crvgJo9wXRPL0Pf-yQk`), updated Apr 27, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flexflyerreview` |
| Hosted URL | myiga.com |
| Flyer types | Flyer — promoted (11877) · Flyer — organic (11912) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons, no Feedel |

## Files & schedule
- **Files received:** Tuesday.
- **Cadence:** Available Wed → Tue; Valid Tue → Wed. No preview, no linking document.

## Upload & setup (Flex)
- **Codesheet build** from the Price Less IGA codesheets sheet: File → Import → Upload → new sheet. Copy the "promoted" column from last week; add a filter.
- Compare column B (store #) week-over-week for changes. Filter column A for "Y" (promoted stores) → paste store numbers (col B) into the "Promoted" tab (cols A & B); replace page names from column K, split text to columns. Repeat filtering "N" for the "Organic" tab.
- Download each (promoted, organic) as CSV and upload to the matching flyer run.
  - Config name **`generic`**; use the corresponding week's FTP file path.
  - **All codesheet toggles checked except the 2nd and last.**
  - Common error: differently named files — adjust the codesheet to match what's in the FTP.
- Mark flyer creation complete, wait for sessions, then Setup QC.

### Setup QC
- Confirm all pages uploaded — **check no pages remain in the SFTP** (Pricing Zone → Items View).
- Confirm flyer dates (usually top of first page). Thumbnails Standard 4. Add "**Weekly Flyer**" to the external run name (English).

## ⚠️ Common errors / risk items
- **Codesheet organization** — organize correctly, especially regarding promoted stores.
- **Store #40:** Always remove store **#40** (its entire row) from the codesheet — this store is manually uploaded into the biweekly flyer runs named "FL".
- FQC geography: compare **FL flyers against other FL flyers**.

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**): box each product block with a price and/or sales story. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**

## FQC / Flyer Review
- Confirm dates vs PDF; all availability toggles unchecked; thumbnails include retailer logo. All items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography matches last week.
- **Flyer Review type: Simple.**

---
*Source: Price Less IGA OneGuide (Google Doc `1nzDnoGoU5JyvGErhCGy2wC-3crvgJo9wXRPL0Pf-yQk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Price Rite Marketplace — Processing Guide

> **Source:** Price Rite Marketplace OneGuide (Google Doc `1v1KPVoPdsXjfP62FxT4lJteAX0SO47NZLCQbsbxrMWQ`), updated Jul 23, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#wakefern` |
| Flyer types | Weekly Ad (9342) |
| Processing | Auto-stack; DOC upload, Flex Flyer Review; no coupons/Feedel (coupons still appear in-flyer) |
| Custom action | **Mi9 Sub Item Generator** — creates sub-items per the blowline doc (runs pre-FQC) |

## Files & schedule
- **Files received:** Monday; goes live external Thursday with a 1-day preview.
- **Cadence:** Available Thu → Thu; Valid Fri → Thu.
- **Linking document:** Yes — the **blowline** file (uploaded ~5 days ahead, before all other assets; scroll to the bottom of the SFTP to find it, under the week's .zip).

## Upload & setup (Vendor)
Codesheet is a **.txt** file (separate from an additional .txt file in the PriceRite/circular folder).
- Download it; copy/paste the whole codesheet text into a **new Google Doc** (reduces formatting errors).
- Remove the lines "Online Start Date" and "Circular Type".
- StartDate/EndDate format = **MM/DD/YYYY**. Keep exactly **one blank line** between each section (EndDate↔Name, Name↔Region/pricing zones, Region↔RegionFiles/pages, and between each RegionFiles line). No empty space under the pages.
- Upload the codesheet as **.txt**, config name **`brookshires`**. Verify pricing zones match the codesheet, then mark flyer creation complete.

### Setup QC (Flex) — building the linksheet
- Open the blowline file in Excel/Sheets. Select column A → Text to Columns → fixed width; verify line breaks don't cut off **PROMO_NUM, UPC_13_NUM, BLOW_LINE**. Remove all other columns.
- New tab **"For OS"** = PROMO_NUM + BLOW_LINE (remove UPC_13_NUM); new tab **"mi9"** = PROMO_NUM + UPC_13_NUM (remove BLOW_LINE).
- In "For OS" only, remove duplicates. Save as **.xlsx** and attach to all tracks.

## ⚠️ Common errors / risk items
- **Look for multiple products in a block** — box separately if two prices are listed; keep as one box if only one price for two items.
- **Mi9 sub-item custom action:** clean the mi9 tab first — delete blank rows, delete rows where a promo code exists but UPC_13_NUM is blank, and fix any UPC_13_NUM cell formatted as a formula (search for `E` or `+`). Download as CSV, upload in Fadmin, copy the file ID. System → Custom Actions → **mi9 sub item generator** (NOT subitem report); paste file ID and flyer run ID; run. On error, read the error log, fix the sheet, re-upload for a new file ID, re-run. Confirm some items now have sub-items (not every item will).

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**): **include coupons.** Exclude packaged deals, retailer logo, sign-up page, social media, special weblinks. Blocks with multiple items → box separately if two prices; one box if one price for two items.
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude pre/postfix, valid dates, URLs.**
  - **SKU custom field:** find the item's name in the blowline's `BLOW_LINE` column (col B); the SKU is in `PROMO_NUM` (col A). Paste into the SKU field. Multiple SKUs → use the first. Not found → leave blank. Never enter more than one PROMO_NUM.
  - **Coupons:** display type Coupon; tag brand/name/description/sales story/disclaimer as written.
- **Image QC:** use PDF images whenever possible **except coupons** — coupons always use cutouts.

## FQC / Flyer Review
- Ensure all coupons tagged correctly. Item Image QC tab: if "Generate data piping groups" is shown, click it (otherwise mi9 generator won't run). Thumbnails Standard 4. **Staggered dates:** the codesheet may drop the preview date — if so, select all → apply selected dates → enter the Thursday date in Date Available and save.
- **Flyer Review type: Lite.**

---
*Source: Price Rite Marketplace OneGuide (Google Doc `1v1KPVoPdsXjfP62FxT4lJteAX0SO47NZLCQbsbxrMWQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# PriceSmart Foods — Processing Guide

> **Source:** PriceSmart Foods OneGuide (Google Doc `17yR6XN7LIJZsueNV1Anurx68loDTaoe3KNPdFiU5zYI`), updated Mar 11, 2026. Contacts/credentials omitted.

> Much of this OneGuide is the unfilled template; the notes below capture the real PriceSmart-specific content (the **Additional Deals / MingPao** flyer type).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (retailer channel not specified) |
| Flyer types | Weekly; Monthly. Additional Deals flyer type = MingPao flyers |
| Processing | Auto-stack; Vendor upload, Flex Image QC, DOC FQC; Feedel (retailer data services) yes; no coupons |

## Files & schedule
- **Files received:** Monday (arrive Tuesday afternoon per upload step).
- **Cadence:** Available Mon → Mon; Valid Tue → Tue. FQC dates below use Thu→Wed.
- If files are delayed, push go-live 1–2 days.

## Upload & setup (Vendor)
- **Tuesday upload:** files arrive Tuesday afternoon. Manually upload pages from FTP — **1 Base pricing zone, all stores.** Thumbnails Standard 4. Setup QC.
- (Reference: UF and PSF cheatsheet.)

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **ON**): box all items with a price, without a price, "Happy Hour" items, sales-story items, and "Shop" items. Box **"SHOP NOW"** separately from a priced/sales-story item. Box the entire page for CIBC "Earn points faster" promos. "Load My Offers" with no original price → single box around item + Load My Offers; with an original price → box the item separately from the "Load My Offers" price. Box Mega Deal/More Rewards and Win-Win callouts.
  - **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
  - **⚠️ Do NOT box** promotional banners, footers, or vacation packages.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include name, pre/postfix, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude valid dates, SKU.
  - **All items get the URL:** `https://www.pricesmartfoods.com/weekly-specials?utm_source=flipp&utm_medium=referral&utm_campaign=psf-mingpao-2021`

## FQC (DOC)
- Dates (Edit Details): Available/Valid from **Thu 12am**, to **Wed 11:59pm**; available everywhere; no theme; Key Message: **Additional Deals**.
- Geography: stores never change.
- Item Image QC → Generate Data Piping Groups; select best image, **do not use plated-food images**. QC thumbnails with no white space.
- **URL fix:** Item Search → URL IS blank → Multi-Edit Items → add the pricesmartfoods weekly-specials URL to all items. Run Page Stitching + Tile Generation repeatedly until green, then re-verify URLs.
- **Flyer Review type: Lite.**

---
*Source: PriceSmart Foods OneGuide (Google Doc `17yR6XN7LIJZsueNV1Anurx68loDTaoe3KNPdFiU5zYI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Princess Auto — Processing Guide

> **Source:** Princess Auto OneGuide (Google Doc `10tPU0PKvnQjJ-ZCgz_kSqmC4kjPQQpw_rq2VWV9cJiQ`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#princessauto` |
| Hosted URL | princessauto.com |
| Flyer types | **Biweekly** (11) · **Monthly / Price Wrecker** (10178) · **Yearly Catalogues** (65) |
| Processing | **Trim Stick**; Vendor setup, Flex + DOC QC, FAB tickets; Feedel (retailer data services) yes; no coupons |

Bilingual (EN + FR). Files received Monday. General cadence: Available Wed, Valid Sun.

## ⚠️ Common errors / risk items
- **Slicing:** after setup, check the pipeline throughout the week to confirm slicing kicks off — it sometimes reads "inactive," which **blocks OS.**
- **SKU boxing:** every item with a unique SKU must have its own box.
- **National Events:** additional links arrive by email and must be boxed/tagged **after go-live** — watch for full flyer revision pages.
- **Yearly catalogue slicing:** drag the slice box down to capture the page number at the bottom.

## Biweekly (11)
### Setup (Flex) — manual upload
- Pages → Edit → select files. Language: French pages have **FR** in the name, English have **EN**. Save only → Autogroup → Save & Continue.
- Pricing zones: **FR** (French) and **EN** (English). Additional PZs may exist (e.g. Saint-Hubert-FR is its own PZ with unique FR pages, pulled out of the FR zone).
- Overview → Edit details: no theme; Wednesday consumer preview (per the schedule); toggles **Hide in Distribution / Flipp / Hosted** (flyer goes live hosted-only first). Thumbnails Standard 4.
- **Create a trigger** to make the flyer available on all platforms one day before go-live, and create an Optics ticket for the live availability check.

### QC
- **Box Draw** (Low; Auto-Box ON, Box QC bot **OFF**): box each item individually with a price; multi-item blocks with different prices → box separately. Box the Email Sign Up and Order Online/Pickup In-Store inserts. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons.
- **Tag / Tag QC** (Low; Auto-tag OFF; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Brand in the brand field (not the Name); copy description exactly. Do **not** include original price when there is a range. SKUs only in the SKU field; only tag the **bold** SKU when multiple exist. Different date from the flyer → set per item.
  - **URLs:** if a SKU is provided → generate/fetch URL. No SKU / SKU doesn't resolve → search by name on princessauto.com and use the **product page** URL (not the search page). No broken URLs.
- **Item Image QC:** check Data Piping early — if data-piped image <90%, filter "Data Pipe Image" + "Supplemental Info" → Data Pipe All to re-run. Use PDF images where data-piped ones aren't available.

### FQC (DOC)
- Fetch URLs for items with SKUs (skip items with no SKU on the PDF). Re-run data piping if low. Mark items **In-Store Only**.
- **Box/tag the weekly inserts:**
  - Email Newsletter (page position 3) — EN `princessauto.com/en/sign-in-newsletter`, FR `.../fr_CA/sign-in-newsletter`.
  - Online Store Pickup (page position 4) — EN `.../en/store-pickup`, FR `.../fr_CA/store-pickup`.
  - Blue Truck BBQ — **Alberta only** (position 5) `bluetruckbarbecue.com/menu`.
- **Flyer sorting order:** Bi-Weekly Event → Monthly Price Wrecker → Special/Standalone → Catalogues. Check QR-code mini-sections have links. Complete the Optics ticket toggle check on the designated day.

## Monthly / Price Wrecker (10178)
- Setup: upload files twice — mark French, then re-upload and mark English. Autogroup. **2 pricing zones (EN, FR)**, all stores in both. No inserts (straight manual upload). No theme; 1-day preview; **available everywhere**. Leg heights **50/35**. Thumbnails Standard 4. Auto-Box ON, Box QC bot **ON**.
- FQC: rerun page stitching; page categories → all surplus; re-run data piping if low; mark In-Store Only; confirm all pages sliced; keep **Bi-Weekly Event as the top sort option**.

## Yearly Catalogues (65)
- EN and FR files split into separate shells; match file names to the correct-language shell. Pricing zones EN/FR, follow page #s (no inserts), all stores in both. External run name = Year + Catalogue Name (e.g. "2023 Air & Power"). Wednesday preview. Toggles: **hosted only for the full year** (Hide in Distribution/Flipp/Hosted). Leg heights **50/35**. Auto-Box ON, Box QC bot ON.
- **Flyer Review type: Simple.**
- **Deep-linking (FQC):** to link Flyer 1 to a specific item/page on Flyer 2, export Flyer 2 items, take the target item_id, and build:
  `https://www.princessauto.com/REF1/flyersView?locale=REF1&flyer_type_name=flyer&flyer_run_id=REF2&flyer_item_id=REF3`
  where REF1 = `en` or `fr_CA`, REF2 = target flyer run, REF3 = first item on the target page. Box & tag as Display Type **LINK**.

## Out-of-processing — video-link embeds
- From a provided link list (SKU, item name, EN/FR URLs): Item Search by SKU → open item → Box QC → resize the existing box to the text only and draw a new box around the image → Save & Complete. On the Tag view set Display Type **Video**, enter the item name exactly, paste the correct-language Video URL, Save.

*(Biweekly/Monthly Flyer Review type: Lite; Yearly: Simple.)*

---
*Source: Princess Auto OneGuide (Google Doc `10tPU0PKvnQjJ-ZCgz_kSqmC4kjPQQpw_rq2VWV9cJiQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pringle Creek Market — Processing Guide

> **Source:** Pringle Creek Market OneGuide (Google Doc `1rB23dqNeFFaK8Jx0N645CRvsL2MZ4Vu1HG3HeNGxzN4`), updated Jul 22, 2024. Contacts/credentials omitted.

> Simple/direct account — the OneGuide is a short generic-retailer guide with no retailer-specific risk items.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Flyer types | Direct — weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons, no Feedel |

## Files & schedule
- **Files received:** weekly. **Cadence:** weekly. No preview, no linking document.

## Upload & setup (Flex)
- Files are uploaded to SFTP.
- **1 zone, English**, containing all pages, assigned to all stores.
- Setup QC: confirm all items in the Setup QC checklist are correct.

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**): box each product block with a price. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC** (Low; Auto-tag **OFF**): include everything — brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Standard pricing spotchecks in pipeline.

## FQC / Flyer Review
- Standard FQC checklist (owned by DOC).
- **Flyer Review type: Lite** — no special risk items; use generic flyer-review standards.

---
*Source: Pringle Creek Market OneGuide (Google Doc `1rB23dqNeFFaK8Jx0N645CRvsL2MZ4Vu1HG3HeNGxzN4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Pro Hockey Life — Processing Guide

> **Source:** Pro Hockey Life OneGuide (Google Doc `1BhyDdjdtV0WlVrIpW-Wtw2lSyfnhpVacW_4GETUgoDs`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fglsports-banners`, `#flex-processingsupport` |
| Hosted URL | prohockeylife.com/pages/flyers |
| Flyer types | Ad-hoc / seasonal |
| Processing | Auto-stack; Vendor setup, OS setup, Flex + DOC QC; no coupons, no Feedel |

## Files & schedule
- **Files received / cadence:** Ad-hoc (all dates ad-hoc). Preview available 1 day before Valid From.
- **Linking document:** Yes — URLs. Found in the fadmin SFTP.

## Upload & setup (Vendor)
- **Manual upload:** select files from FTP (in the folder for the corresponding date; naming convention gives page order/index; usually 3–8 pages). Select all → Auto Group → confirm indexing → Save & Complete.
- **Setup:** start the flyer-creation vendor task → pricing zone: Description **Base**, Language **English**, all pages in correct order → Save & Done. Under FSAs, select **National (Excluding Quebec)**.
- **Linking document:** download from the SFTP and **mass-attach to all vendor tasks** (no manipulation).

### Setup QC
- Dates match the PDFs and Available = 1 day before Valid. No theme. Availability everywhere (not hidden). Complete Setup QC checklist, Save & Confirm.

## ⚠️ Common errors / risk items — tagging accuracy vs the linking document
- **Tag brand exactly as shown in the linking document** (e.g. CCM; "Bauer" vs "BAUER").
- **Tag name exactly as in the linking document**, matching capitalization and punctuation. If the flyer name and spreadsheet name differ, **use the spreadsheet name** (e.g. "CCM Jetspeed FT1 Junior Hockey Skates", not "CCM JETSPEED FT1").
- **Sale story:** use "save" + the exact dollar amount from the "Save Story" column (e.g. "Save $400"). If the flyer says "Save Up To $$$", **do not** use that — always use the exact amount from the linking doc.

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**; linking doc required): draw a box over each item — **every item in the linking document must have a box.** Multiple sizes (e.g. a hockey stick) → box the top one with the image and the other sizes separately. Box PHL logos on the first and last page. Box Triangle Rewards banners. **Include** retailer logo, special weblinks; exclude coupons, packaged deals, sign-up page, social media.
- **Tag / Tag QC** (**Medium**; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. SKU N/A. Brand/name exactly per the linking doc (see risk items).
  - PHL logos tagged as **Link** → `https://www.prohockeylife.com/`.
- **Item Image QC (Flex):** if an item has no clean PDF, open its URL (via "visit"), verify the item, right-click the website image → copy image address, paste into "override image url" in fadmin, save; refresh Item Image QC and select the data-piped image. If no matching website image (verify the URL against the linksheet first) or it doesn't match the flyer, use a cutout. Grouped items (all tape, all of a brand) → website image if available, else cutout.
- **URL/Links QC (Flex):** confirm every item has a URL; cross-reference the linksheet. Confirm all PHL logos on first/last page are boxed and tagged with `https://www.prohockeylife.com/`.

## FQC / Flyer Review
- Complete FQC checklist (Flex).
- **Flyer Review type: Lite.**

---
*Source: Pro Hockey Life OneGuide (Google Doc `1BhyDdjdtV0WlVrIpW-Wtw2lSyfnhpVacW_4GETUgoDs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Product of the Year — Processing Guide

> **Source:** Product of the Year OneGuide (Google Doc `19Q1KL288TCXRNp1tFFu0DXu9R2I8rAj9F-br9v-Uiho`). Contacts/credentials omitted.

> Ad-hoc campaign account processed off the generic simple-retailer template; no retailer-specific risk items were filled in.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Plus |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | Campaign — **Ad Hoc** |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons, no Feedel |

## Files & schedule
- **Files received / cadence:** Ad hoc (available-from/to and valid-from/to all ad hoc). Dates provided via email.
- **Linking document:** Yes (URL document).

## Upload & setup (Flex)
- Pages may need to be added to the SFTP by the processor if the client sends files over email.
- **Manual upload:** Pages → Edit → manually upload the pages provided by BD → Confirm & Upload. Once listed, Auto-Group or enter grouping numbers manually; select the correct language. Save & Confirm — **do NOT Process Internally.**
- **Pricing zone:** create a **Base** zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC
- Confirm all pages uploaded (Pricing Zone → Items View); if uploading from SFTP, confirm nothing is left in the SFTP. Confirm flyer dates (from email). Thumbnails Standard 4. Set all preview dates. **Mass-attach the URL document to all processing steps (Box, Tag, Tag QC).**

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**; linking doc used for both Box/Tag): box and tag each item individually. **Shop Now / Find on Flipp** callouts (most items have them) are boxed and tagged separately. Banners with a play button = video → box and tag. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC** (Low; Auto-tag **ON**; PDF image auto-selection ON): include everything — brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / Flyer Review (Flex)
- Confirm dates vs PDF; availability toggles; thumbnails include the retailer logo. All items boxed/tagged; spotchecks (20% of pricing zones); previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite.**

---
*Source: Product of the Year OneGuide (Google Doc `19Q1KL288TCXRNp1tFFu0DXu9R2I8rAj9F-br9v-Uiho`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# ProNature — Processing Guide

> **Source:** ProNature OneGuide (Google Doc `16LV2O10Ueq3FUL5KqOj4q_7JaSN4H17_7dY-GLY-NzI`), updated Sep 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#heinens` |
| Hosted URL | EN: groupepronature.ca/en/flyer · FR: groupepronature.ca/fr/circulaires |
| Flyer types | Weekly (6484) — runs **bi-weekly (2-week run)** |
| Processing | Auto-stack; Vendor + DOC setup, Flex FQC; no coupons, no Feedel |

Bilingual (EN + FR). Files received Monday; preview Thursday; live Monday. Works mostly with a third party (Turbulence). No retailer-specific risk items called out.

## Files & schedule
- **Cadence:** Available Mon 12am → Sun 11:59pm; Valid Mon → Sun; **2-week run.** Preview Thursday before go-live (external preview Friday, so corrections may land on the live Monday).
- **Linking document:** Yes (URL spreadsheet).

## Upload & setup (Vendor / DOC)
- Retailer emails when files are dropped; confirm receipt, update the Vendor Setup Tracker with FlyerID, mark ready. Files on S3 can be hard to open — use coreFTP to download and save locally.
- **Manual upload:** Pages → Edit → select files. Equal numbers of English ("**An**") and French ("**Fr**") pages. **Do not Auto-Group** — manually set page numbers per the file name (two page 1s, two page 2s, etc.). Manually set language for each French page and **Save only**; re-check that French pages didn't revert before **Save & Complete**.
- **Pricing zones:** create **EN** (all "An" pages) and **FR** (all "Fr" pages), correct page order. Add **all stores to both zones.**

### Setup QC
- Dates: Available/Valid Mon 12am → Sun 11:59pm, 2-week run. Available on all platforms. Preview Thursday. Internal run name = **FLYER/THEME IN ALL CAPS - Live Date**; no external run name; no theme. **Leg heights 40/20.** Thumbnails Standard 4 (1065x600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, organic – 1pg). Confirm sessions ran and FSAs generated.

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**; linking doc used for both Box/Tag): box the retailer logo; box all items separately, but keep **differently-sized variations of one item in a single box**; items with multiple prices in the description → box as separate items. **Do NOT box QR codes.** Exclude coupons, packaged deals, sign-up page, social media.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude disclaimer** (except: include the disclaimer only when it's inside the box, e.g. "(Accessories sold separately)", "Limit of 4 per client", and all warranty messaging like "1-YEAR IN-STORE WARRANTY").
  - Name exactly as in flyer (bold text); don't include quantities in Name unless multiple items with different quantities. One brand → enter exactly; multiple brands → leave Brand blank. Common prefix "STARTING AT"; if no current price, put the sales-story text in prefix and the amount in Current Price. Common postfixes "EACH", "PER PAIR".
  - **Do NOT tag** suggested retail price as original price (leave original price blank, but fill $/% off if applicable); don't tag words like "UNBEATABLE".
  - **Store locator** on the last page → tag with EN `groupepronature.ca/en/store-locator-hunting-outdoor-fishing/`, FR `groupepronature.ca/magasins-plein-air-chasse-peche/`.
  - **Style guide:** no original pricing is to be displayed.

## FQC / Flyer Review (Flex)
- **Page categories:** per the category chart — choose by the theme of items on each page; front page always titled "Front Page".
- URL/Links QC: no links need inserting for this merchant. Spotchecks; mark Auto-Stack complete; confirm vendor tasks done. Dates/leg heights/thumbnails as above; page categories per chart; vertical preview; sessions run and re-verify URLs; geography doesn't change week to week. Clean images where possible; mark items **In-Store Only**; store finder links out. OK to ignore "Other Warnings"/unassigned stores.
- **Flyer Review type: Lite.**

## Out-of-processing
- Post-live page swaps per the baseline page-swap process.

---
*Source: ProNature OneGuide (Google Doc `16LV2O10Ueq3FUL5KqOj4q_7JaSN4H17_7dY-GLY-NzI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Provigo — Processing Guide

> **Source:** Provigo OneGuide (Google Doc `1khEVVNokD5U6hfym-SjS8TahCK5h4v6E_EFtGuLCte0`), updated Dec 18, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Relationship: Excellent) |
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer types | Weekly (5592 / flyer type 6006) |
| Processing | Auto-stack; Vendor setup, OS setup, Flex + DOC QC; Feedel (retailer data services) yes; no coupons |

Loblaw banner, bilingual (FR + EN). Files received Monday.

## Files & schedule
- **Cadence:** Available Tue → Mon; Valid Thu → Tue. **Preview: Sunday.**

## Upload & setup (Flex)
- **⚠️ NEW 2026 — set pixel height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → show/hide rarely-used fields → Height dropdown → select **4096.0 pixels** → OK. If pages were already added before this step, flag the Full-Time Ops stakeholder and continue.
- Weekly flyer = codesheet upload with manual-stores troubleshooting.
- **Set the Sunday preview:** flyer run → Overview → Edit details → Preview start date = the Sunday before the available date → OK.

## ⚠️ Common errors / risk items
- **Tag all "PC Optimum" buttons** with the `pcoptimum.ca` link.
- **Joe Fresh pages:** tag all Joe Fresh items as **ONE box** and as a **direct link** (Joe Fresh diff-groups URL in the OneGuide).

## QC specifics
- **Box Draw** (**Medium**; Auto-Box **ON**, Box QC bot **ON**): draw a box wherever there's a unique price. Box special weblinks. **Include** coupons, packaged deals, special weblinks; **exclude** retailer logo, sign-up page, social media.
- **Tag / Tag QC** (Low; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name:** `[FRENCH NAME], [SIZE] | [ENGLISH NAME]` — bold text, tagged in **both FR and EN** if both are on the PDF, separated by `|`, in **all caps**. Do NOT include in the name: alternative unit pricing (e.g. "6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties".
  - **Description:** non-bold text; first letter capitalized; put alternate unit prices and the "Product of…/No 1 Grade/Frozen/Selected varieties" items here. **Do not put the SKU in the description.**
  - **Article Number fields** (special tagging fields at the bottom): paste the Product SKU into the Article Number field — one SKU per field. Article Number 1 = the same number as SKU and Fetch URL. Include the unit of measure (`_KG`, `_EA`, `_LB`, `_C12`, `_C24`, etc.). Multiple SKUs → first→Article Number 1, second→2, third→3, fourth→4.

## FQC (DOC)
- Merge any remaining flaps. Check dates, no theme, toggles (available everywhere). External run name = **"Weekly Flyer - Valid Thursday, (Month + day) - Wednesday, (Month + day)"**. Thumbnails, geography, FQC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page swap:** standard page swap.

---
*Source: Provigo OneGuide (Google Doc `1khEVVNokD5U6hfym-SjS8TahCK5h4v6E_EFtGuLCte0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Proxim — Processing Guide

> **Source:** Proxim OneGuide (Google Doc `1ZWrGeKnNbRRUgjBLxrQaHbV-46JQDmSSmsh59UTOk_o`), updated Jul 6, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | Yes (channel not specified in guide) |
| Hosted URL | groupeproxim.ca/en/flyer |
| Flyer types | Ad-hoc · **Weekly (5832)** · **Monthly (5869)** · **C – Bi-weekly** (cloned from Weekly) · **Carnet Beauté** (Catalogue, cloned from Weekly) |
| Processing | Auto-stack; Vendor upload, OS setup, Flex + DOC QC; Feedel (retailer data services) yes; no coupons |

Bilingual (EN + FR — French zones are set to English during upload and switched to French at FQC). Files received Monday.

## Files & schedule
- **Weekly cadence:** Available Tue → Mon; Valid Thu → Wed (2-day preview). Files uploaded Thursday (or earlier if assets are in).
- **Monthly:** doesn't necessarily start on the 1st or run exactly a month — trust the prebuilt flyer-run dates.

## Upload & setup (Vendor)
### Weekly (5832) — codesheet upload
- Upload the pagination document (`A# digital.xlsx`) from the SFTP to the shared Proxim folder; update the Vendor Tracker.
- Copy the **pages only** (no header) from the pagination doc → paste into the template's **Pages** tab at A2 → download the **Codesheet** tab as CSV.
- Codesheet notes: Page 3 has **A1/A2** variants; Pages 1–2 have **"regular"/"Holiday"** variants. Keep all pricing zones as **English** for now (including FR zones).
- **⚠️ An invalid store will be assigned so the codesheet can run — no distribution impact, safe to ignore the warning.**
- On error, it's usually a client typo in the codesheet: read the error for the problem file name and fix it in the template (e.g. add the missing `.p1`), re-download the Codesheet CSV, re-upload.

### Monthly (E) — manual upload
- Manual upload from SFTP as **English** pages (FTP → search "Monthly" → latest ~2 pages, standard pagination by page number). Add a Vendor Tracker line below the Weekly run.
- Pricing zones **E** and **E FR**; assign pages 1–2; keep both English for now. Add the **"Proximed Monthly Stores"** store set to both.

### Setup QC (Flex)
- Check sessions, Item View, vendor tasks. **Ignore store-related flags until FQC.** Standard setup QC: Weekly available Tue–Wed (2-day preview), valid Thu–Wed; available everywhere; internal run name set; no external run name; no theme (unless specified).

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **ON**): **box every individual item** with its flyer info — Proxim doesn't use data piping and item-pop images are mostly cutouts, so draw clean boxes. When item and info are separated, box the image and text-box the info. Box the merchant website wherever seen. Atoma-vs-Name-Brand pages: box **both** Atoma and Name Brand. **Anything with a price gets boxed.** Include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.**
  - **Name:** include item name **and** brand name in the Name box.
  - **Description:** separate French and English by spaces; anything not bold/capitalized goes here; capitalized text goes in **both** name and description; put sizes on a separate line between the FR and EN.
  - **⚠️ French pricing convention:** comma in place of the period, dollar sign at the end (e.g. `XX,XX$`). For a **price range** (not a sale/regular price, e.g. $10.99–$13.99), **tag the higher price in the postfix**. Percentage-off with no current price → tag the % off as the **prefix**.

## FQC (Vendor)
- Review/approve pending Ops tasks. Confirm dates & banner name match the PDF page 1; **Available From must be 2 days before Valid From.**
- **Pricing zones (Weekly):** if you see **four** PZs, **delete the two with fewer pages**; if only 2, proceed. Rename **A2 FR → A FR** and **A2 → A**. Remove all stores from both zones and add the **"Proxim Weekly Stores"** set to both (A and A FR).
- **Monthly:** two PZs ("E", "E FR") — don't delete/rename. Add the "Proximed Monthly Stores" set to both.
- **Insert:** upload the insert (Pages → Edit → Upload) to the last position of all pricing zones. Start Vendor Box QC and ensure **one box** covers the entire insert; add a URL only if a URL sheet is in the shared drive (Display Type **Link**). ⚠️ Number of inserts varies and not all need linking.
- **Distribution:** Weekly ('A') available everywhere; Monthly ('E') **Hidden in Distribution + Hidden in Flipp**.
- Draw 4 standard thumbnails (no white borders, logo present). Item Image QC → Generate Data Piping Groups; prefer clean PDF images (white background) over cutouts where appropriate.
- **⚠️ Pricing zone language:** set **A FR** (Weekly) and **E FR** (Monthly) to **French**. **Remove all "WEB" pages** from both zones — they clone into a separate run. Check Vertical Preview interactivity.

### Cloning
- **Weekly → Carnet Beauté** (Flyer Type: Catalogue): flyer shells exist; select the correct run. Same details as Weekly except **assign ONLY the WEB pages** to both zones. Standard-4 thumbnails (logo not cut off), no insert, add "Proxim Weekly Stores" to A and A FR. Re-complete FQC checklist.
- **Monthly (E) clone:** add "Proximed Monthly Stores" to E and E FR before completing the FQC checklist (per FQC video). For cloned runs, mark red tasks "N/A"; then Save → refresh → Save and Confirm.
- **C – Bi-weekly** (cloned from Weekly, runs weekly): 2 zones C/C FR, pages 1–4 (same pagination as the 4-page Weekly).

## Flyer Review
- **Flyer Review type: Lite.**

## Out-of-processing — adding stores
- The vendor uploads the runlist (`XXX digital.xlsx`) to the SFTP by Tue/Wed. Download, copy columns A/B/C, paste into a Google Sheet without formatting, save as CSV. Upload as a codesheet on all runs — Name "store upload", **Config name `proxim_stores`**, PDF base directory `/`, **only the first toggle checked**. Cross-language to French.

---
*Source: Proxim OneGuide (Google Doc `1ZWrGeKnNbRRUgjBLxrQaHbV-46JQDmSSmsh59UTOk_o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Publix Liquors — Processing Guide

> **Source:** Publix Liquors OneGuide (Google Doc `1uG78_9frnEnBsj7Wah4U78sZcj3eskSHwmZUlWehpf0`), updated Apr 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | **Flipp only** |
| Slack channels | `#publix` |
| Hosted URL | None |
| Flyer types | Liquor Ad — Weekly |
| Processing | Auto-stack; Flex vendor setup, Vendor upload, Flex FQC, DOC ad-hoc/store additions; no coupons, no Feedel |
| Resources | 2024 recipe-links spreadsheet; Publix Liquors drive |

Files received **Tuesday (late)**; vendor setup Wednesday.

## Files & schedule
- **Cadence:** Available/Valid Wednesday → Wednesday, 1-week run. No preview. **Hidden on Hosted.**

## ⚠️ Common errors / risk items
- **Staggered dates:** pricing zones should have staggered dates — **PZ 1 Wed → Tue**, **PZ 2 Thu → Wed**. Confirm dates match the PDF. (OK to ignore staggered-dates/unassigned-store warnings.)

## Upload & setup
### Vendor setup (Flex)
- Confirm files are in the FTP (search "liq" for the liquor PDFs). Copy the lowercase file path (e.g. `/050924/liquor_pdfs_050924`). Fill out the Vendor Setup & Setup QC Tracker (FlyerID, start date, file path, mark ready for upload).

### Upload (Vendor)
- Manual upload — **LIQUOR_PDFS (lowercase)**, select all 4 pages, Auto Group. Upload the Loyalty insert to the back position of all pricing zones. Make **1 zone (Base)** and add all stores.

### Setup QC (Vendor)
- Dates Wed → Wed, 1-week run, **hidden on Hosted**, no preview, internal run name `Liquor_[Start Date]`, no external name, no theme. Thumbnails Standard 4. Confirm sessions ran and FSAs generated.

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**): **include coupons**, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. **Recipe + QR code** = one box (picture + QR + recipe link). Box secondary items (smaller print, own price).
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **No item URLs** (page callouts only).
  - Brand in Brand **and** Name fields. Description = small-print size info (ml, L). Prefix N/A — include as sales story. Sale story: multi-pricing, BOGO, Save Up To, "Buy # Get $$ Off". Category usually Grocery (Google category beer/spirits/alcohol).
  - **URLs:** social-media publix links; any URL → Display "Link" as written; recipe link.
- **Image QC / Spotchecks:** N/A.

## FQC (Vendor) — pre-FQC insert & link steps
- Ops spotchecks (mainly "Prefix Unavailable" flags → confirm sale pricing is in the Sale Story). Mark Auto-Stack complete.
- **Add loyalty insert page:** download the Weekly.Spanish.Liquor Loyalty insert from the drive → Pages → Edit → Manual Upload → Save & Confirm → Mark Flyer Creation Complete → mark Box QC/Tag/Tag QC complete → wait for sessions → mark Auto-Stack complete. Pages → Box QC → box the entire page. Tag → Display **Link**, Name "Sign Up", URL = the Publix myaccount register link (in the OneGuide). Then Pages → Layout → Loyalty page → Put In → position **99**, all flyers → Process (sessions re-run).
- **Add recipe link:** Pages → open Page 2 → select this week's link from the 2024 Links spreadsheet (filter by date, may be off 1–2). Ensure the recipe is boxed (product image + QR code + URL); Display Type **Link**; add the URL.
- Confirm vendor tasks done; dates match PDF; thumbnails Standard 4; Item Image QC N/A; Tag/Tag QC both green; sessions run + re-verify URLs; vertical preview; geography (DOC note if stores added). Complete FQC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing
- Post-live page swaps per the baseline page-swap process.

---
*Source: Publix Liquors OneGuide (Google Doc `1uG78_9frnEnBsj7Wah4U78sZcj3eskSHwmZUlWehpf0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Publix (Weekly, Spanish, Extra Savings) — Processing Guide

> **Source:** Publix OneGuide (Google Doc `1qsSR01gkX7XTaK_zf-ivCXAggW77lJjk5-kMKRSIOJs`), updated Apr 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Relationship: Excellent) |
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#publix`, `#publix_offapp` |
| Hosted URL | None (ongoing hosted tests) |
| Flyer types | **Weekly [5944]** · **Bilingual/Spanish [5944]** · **Extra Savings [9562]** (bi-weekly) |
| Processing | Auto-stack; no coupons, no Feedel |
| Ownership | **Weekly & Spanish:** DOC uploads, **OS completes FQC** (Flex not involved). **Extra Savings:** Flex uploads & FQC. DOC handles comms/ad-hocs/page swaps. |

Files received **Tuesday (late)**. High item count.

## Files & schedule
- **Weekly & Spanish:** Available/Valid Wednesday → Wednesday, 1-week run. **Set preview date Friday** (this flyer often fails auto-tagging — the Friday preview unblocks boxing before the weekend). Staggered dates (Wednesday vs Thursday versions).
- **Extra Savings:** bi-weekly; Available/Valid Saturday → Friday, 2-week run; **hidden on Hosted**; no preview.

## Upload & setup — Weekly & Spanish (DOC), codesheet
- Files arrive in FTP; reply to the email confirmation once files sync. *(Note: some contacts on the email chain are Fusion92 — no need to respond to them.)* Distribution list arrives separately; confirm and request any missing store info.
- Download the .xlsx codesheet. Email notes any store openings/closures and flex pages: set closing dates / add new stores in Fadmin (confirm if new stores also belong to the Publix Liquors merchant/store set).
- **Codesheet manipulations (staggered dates)** — mark whether stores get a Wednesday or Thursday version, per tab:
  - **Atlanta (Wed) & Charlotte (Wed):** insert a column B, formula `=A3&"W"`, copy down so each store # has a **W**; paste column B over A as **values only**; delete column B. Delete the black legend table. *(Charlotte also: add Version "V" in the legend and copy "Base - English - XXpages" from another version.)*
  - **Jacksonville (mixed Wed/Thurs):** delete the Liquor row/column; delete the GreenWise Market row **first**; use the Jacksonville Stores spreadsheet — copy row B and paste as values over the stores in column A; delete the black legend area. ⚠️ If a new store is added to Jacksonville, update the spreadsheet (add "W" if it starts Wednesday).
  - **Lakeland (Thurs) & Miami (Thurs):** delete Liquor row/column; delete GreenWise Market rows; align the legend table to match other tabs; delete the black area. *(Miami: MA = English, MB = Bilingual.)*
  - **Wrap/flex pages** (if present): reverse the letters (ZK → **KZ**, K = base); naming e.g. "GO WRAP 1633 - English - 20 pg."
- Save as **.xls** with **"MAIN"** in the name. **Delete the Charlotte tab**, save again with **"SPANISH"** in the name.
- **Upload to FADMIN:**
  - **Weekly:** codesheet name `main`, MAIN file, config **`publix`**, PDF base directory (e.g. `/070821`), **select all toggles except combine zones**.
  - **Spanish:** name `spanish`, SPANISH file, config **`publix_spanish`**, same PDF base directory, **all toggles except combine zones**.
- When running sessions, make sure the **first 4 page-level-task sessions fully complete**.
- **Loyalty insert:** add the Club Publix loyalty insert PDF to the back (Pages → Upload from local → Save & Complete → Layout → Put In → position **99** → **ALL pricing zones**).
- **Flex/Wrap pages:** if not auto-added, manually add to the beginning of the pricing zone. Wrap pages are labeled with the PZ name or noted in the distribution email; insert into positions 1–4 of the matching PZ (usually 4 pages). **Wine pages** (uncommon) insert into the **middle** of the flyer.

## Upload & setup — Extra Savings (Flex), manual
- Manual upload: Pages → Edit → open the week folder → choose the **lowercase** Extra Savings files → Auto Group → Save & Complete. Flyer Creation → 1 Pricing Zone (**Base**), add all stores.

### Setup QC
- **Weekly/Spanish dates:** Available/Valid Wednesday → Wednesday, 1-week run, available everywhere, **preview Friday**, internal run name `Weekly_[Start Date]`, no external name, no theme. **Staggered check:** PZs with "Wednesday" in the name = Wed→Tue; otherwise Thu→Wed. Thumbnails Standard 4.
- **Recipe links (vendor tasks):** from the Publix Aprons Recipes SharePoint list, filter by flyer date (may be off 1–2 days), copy recipe links, add a note to the Tag/Tag QC vendor tasks (>2 links → attach a spreadsheet). Add ready runs to VAST.
- **Extra Savings:** Available/Valid Saturday → Friday, 2-week run, hidden on Hosted, no preview, internal name `ExtraSavings_[Start Date]`.

## ⚠️ Common errors / risk items
- **Coupons** require Display Type **Coupon** and the **"LU# 12345"** (bottom-right corner) in the Description field.
- **BOGO tagging** (see below) — brand + "BOGO*" must be in the **Name** field, and the Save Up To sale story needs a **"$"** added manually (not printed on the page).

## QC specifics (all flyer types)
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**): **include coupons**, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. Box secondary items (smaller print, own price) separately. Don't let boxes cut off sale stories. Two side-by-side products → box/tag individually. Multiple products with text → main box (image) + text box (corresponding text).
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **No item URLs** (page callouts only) + specific recipe links.
  - **Spanish:** Spanish name from the text extraction in the Name field; include the **English name** in the description.
  - Description = non-bold text (sizing/variations); do NOT include items in brackets or with different price points (box/tag separately). Item category usually Grocery; coupons also get "Coupon" in the category.
  - **URLs:** no item URLs. Social media (Facebook/Twitter/Instagram/Pinterest/YouTube publix links); any URL → Display "Link" as written; recipe URLs per task notes.
- **Image QC / Spotchecks:** N/A (owned by Vendor, marked N/A).

### BOGO item tagging
- BOGO shown as bold "BOGO" or a green circle. **Name field must include the Brand name AND "BOGO*"** (all caps + asterisk, at the end). Prefix text = "Buy 1 Get ### FREE*", prefix amount 1.0. **Sale story: add "$"** to the Save Up To amount. Items in brackets don't need special BOGO tagging.

### Coupon tagging
- Display Type **Coupon**; Description includes **"LU# ____"** (bottom-right of coupon); include the full disclaimer/fine print; enter valid dates if different from flyer; add "Coupon" to the category.

## FQC
- **BOGO tagging review** (Vendor, right after Tag QC): Item Search → Prefix Text contains "Buy 1" (~300–600 results); confirm every BOGO item has brand + BOGO* in the name and a "$" in the sale story.
- Ops spotchecks (pricing discrepancy + valid dates). Mark Auto-Stack complete. Re-run the staggered-dates check. Thumbnails Standard 4; Item Image QC N/A; Tag/Tag QC both green; vertical preview; sessions run + re-verify URLs; geography (look for DOC store notes). **OK to ignore "Other Warnings"/unassigned stores.**
- **Flyer Review type: Lite** (Flex). Weekly EN: spot-check ~10 zones that PDF dates match PZ-level valid dates; Spanish: ~3 zones; **Extra Savings should NOT have staggered dates**; confirm vertical preview; confirm BOGO offers have BOGO at the start of the name for NativeX promotions; confirm geography/codesheet ran green.

## Out-of-processing
- **Remove FSAs** custom action is **no longer required as of 08/08/2024** (kept for historical context). Page swaps handled by DOC.

---
*Source: Publix OneGuide (Google Doc `1qsSR01gkX7XTaK_zf-ivCXAggW77lJjk5-kMKRSIOJs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
