# Retailer Processing Guides — I

> Bundle of 8 retailer-specific processing guides (I). Contacts and credentials are omitted from every guide.

**Contains:** i4 Furniture, IGA Quebec, IGA Southeast, IGA West, IKEA, Independent City Market, Independent Food Town (Sobeys), Indigo


---

# i4 Furniture — Processing Guide

> **Source:** i4 Furniture OneGuide (Google Doc `11g0_fdv0SipMkpXR3ZWQMD7vcImO5fsZSNxnCdnIXa4`), updated Mar 21, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel(s) | `#i4furniture`, `#flex-processingsupport` |
| Flyer types | Flyer / Monthly (11070) |
| Processing | Auto-stack; **Flex owns processing & comms**, OS only completes flyer processing; flyer review owned by DOL; Feedel/data services — **yes**; no coupons |

## Files & schedule

- **When files arrive:** ad-hoc, based on retailer request. **Valid and Live dates are the same** (no preview). All publication dates come from the retailer email. Files may need to be added to the SFTP by the processor if the client sends them over email (flag to processor). SFTP login: `i4furniture`.

## Upload & setup

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group or manually add grouping numbers, ensure correct language, Save & Confirm.
- **Pricing zone creation:** create a **Base** pricing zone, select all applicable pages, Save & Confirm, add all stores.

### Setup QC checklist (FLEX)

- Overview → Edit Details: Available/Valid dates per the retailer email; **no preview date**; available everywhere; **External Run Name: None**; No Theme.
- Thumbnails: Standard 4 (1065×600 → 2 pg, Stock premium → 1 pg, Storefront carousel premium → 2 pg, Storefront carousel organic → 1 pg).
- **Leg heights: 45, 35.** Confirm all sessions have run.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF.** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
  - **Box each size option separately** (Twin, Double, Queen).
  - **Multiple product vignettes:** use text boxes to match each product description + price to its image (e.g. dining-table image → "Lynnfield Dining Table, 2 arm chairs & 4 side chairs"; server image → "Lynnfield Server").
  - **Do not box items without a price or website link.**
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Include name (with identifiers from the PDF image, e.g. "Brooklyn Upholstered Bed Twin" — not just "Twin"), pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude brand and URLs.**
- **Spotchecks (FLEX):** spelling errors & price discrepancies.

## Final QC (FLEX-owned)

- Edit Details as in Setup QC (dates per email, no preview, external run name None, No Theme); Standard 4 thumbnails; leg heights 45, 35.
- Confirm tagged/tag-QC item counts match; all items boxed; vertical preview; all sessions run; Geography — no stores added/removed.

## Flyer review (owned by DOL)

- **Flyer Review type: Lite.**

---
*Source: i4 Furniture OneGuide (Google Doc `11g0_fdv0SipMkpXR3ZWQMD7vcImO5fsZSNxnCdnIXa4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# IGA Quebec — Processing Guide

> **Source:** IGA Quebec OneGuide (Google Doc `17uX9ZAsJPk9vudaBDIWAct1mxuINtUmATVt4c8XItpE`), updated Apr 24, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#iga-quebec`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | iga.net |
| Flyer type(s) & cadence | **Weekly Quebec (5710)** · **Weekly New Brunswick (5711)** · **Weekly Iles-de-la-Madeleine (5697)** — all weekly, EN + FR |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Tuesday → Monday; Valid Tuesday → Tuesday.
- **Custom action:** "Set cutout images" (used in the IDM FQC process).

## ⚠️ Risk items (most valuable)
- **Box every unique item separately** (e.g. yellow zucchini vs. green zucchini).
- **Choose the PDF image for every item** (some exclusions — see Image QC).
- **Contest dates** apply to the CONTEST only — do **not** override flyer valid dates with them.
- **Pages cropped:** review uploaded pages so none are cut off on any side.
- **`+tx` postfix:** tag ALL items showing `+tx` on the PDF in the Postfix field — **watch liquor items especially**. Enter the price in Postfix Amount.
- **Product URLs:** each boxed item gets the correct SKU from the linking (extract) document. If the fetched URL is invalid/missing: search iga.net by product name → copy the SKU from the URL → input into the URL field.

## Upload & setup (owned by Vendor)

### Quebec (5710)
1. Download **B extract** xls & **Order IGA - Quebec** xls from the FTP.
2. Manual upload — **upload pages twice** (once French, once English); pages from the IGA folder. **Do NOT upload Booklet-folder files.** EN and FR page counts must match (pages look like a zipper). Save & Complete.
3. **Do NOT create pricing zones** — check off Flyer Creation. PZs are created in FQC. A FSA generation error will appear because no stores are added — **ignore it**.

### New Brunswick (5711)
1. Download **BA extract** xls & **Order IGA - NB** xls. Pages come from the **IGA ATL folder** only.
2. Manual upload twice (FR + EN, zipper); Save & Complete.
3. Do not create pricing zones — PZs created in FQC.

### Iles-de-la-Madeleine (5697)
1. Upload pages twice (FR + EN), auto-group (zipper), Save & Complete.
2. Flyer Creation — **2 PZs: English and French** (mark the French PZ as French).
3. Pages in order (P01, P02, …). This is a **simplified pop** — only the image cutout shows on the front end (no item details/pricing).

### Setup QC
- Attach the extract & order documents to vendor tabs (mass attachment); mark vendors High.
- **External Display Names:** QC → FR "Québec – Circulaire Hebdomadaire" / EN "Québec – Weekly eFlyer"; NB → EN "New Brunswick – Weekly eFlyer" / FR "Nouveau-Brunswick – Circulaire Hebdomadaire"; IDM → EN "Iles-de-la-Madeleine - Weekly eFlyer" / FR "Iles-de-la-Madeleine - Circulaire Hebdomadaire".
- **Available Everywhere**, no theme. IDM: add the **3 designated stores only**. Ignore the FSA error for QC.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons.
- Special weblinks: FR `https://iga.app.link/JcS9FMP2JPb`, EN `https://iga.app.link/zmqBgDX2JPb`.
- **Direct-link boxing:** use the Order xls to see what to box/tag; display type = Link.
- Items with more than one image → box each as an individual item. Non-grocery pictured items (no SKU, can't add to cart) are **not** boxed/tagged.

### Tag / Tag QC (Low; Auto-tag OFF)
- **Include** brand, name, pre/postfix, valid dates, description, SKU (from the extract doc), price, sale story, categories, original price, URLs (fetch from SKU), image selection (PDF preferred). **Exclude** disclaimer.
- **All tagging info comes from the PDF except the SKU**, which comes from the linking (extract) document. Match the page via the first number after "IGA" in the page name.
- **Banner callout (bottom of pages):** tag as a link — EN name "Activate Offers"; use FR/EN app.link URLs above.
- **Scene+ items:** tag "Scene+ PTS" in Sale Story; or prefix "Prix Membre Scene+" / "With Scene+ card", disclaimer "Without Scene+ card $X" / "Sans carte Scène+ $X", categories = Scene+ plus the product category.
- **`+tx` (new Jan 2026):** Postfix Text `+tx` after the price.
- **REG price (new Jan 2026):** single reg price → Original Price; **price range** → put "Reg. $X to $Y" in the description and **leave Original Price blank**.

### Image QC
- Rule of thumb: pick the cleanest image. **Do not use PDF images** when there are lifestyle shots or too many shadows/black outlines — leave no image or use cutout. If multiple images, choose the one best matching the product name.

## Post-processing / FQC (Multiple parties)
- **Quebec runs:** complete **Pre-FQC steps only** during FQC (FQC owned by DOC, Pre-FQC by FTE).
- **New Brunswick & IDM:** complete **both** Pre-FQC and FQC (owned by FTE).
- **Pre-FQC checklist:** Scene+ Points, Page Categories, Items without URLs.
- **QC/NB FQC:** create generic codesheet (QC/NB Hosted templates) → PZs with correct page order (NB = 2 PZs, EN + FR); upload with **Config `generic_language`**, PDF base directory from FTP, **toggles 1, 3, 4, 5, 6**; "Already Uploaded" yellow warning is fine → **Force Processing** (any other error → troubleshoot, do not force). Rerun Flyer Creation; add stores via generic codesheet + store sets; Image QC (uncheck PDF, watch unclean fruit PDFs); StoreFront SpotCheck; mark AutoStack complete; add direct links from Order sheet and **always rerun Page Tile Generation after adding links**; add the **extra page provided on Fridays** to all PZs after page W1; check items without URL (compare FR/EN, copy missing SKUs, verify links work); draw thumbnails (Standard 4 + thumbnail + w400); **QC Hosted only:** remove WR (Rachelle Bery) pages from EN/FR/EN Voila/FR Voila PZs. Key Messages EN "Eat Well" / FR "Mieux Manger"; 3-day preview; Available Everywhere.
- **IDM FQC (FTE):** mark item QC & Image QC complete; run custom action **"set cutout images"**; each PZ has **4 stores only** (8372, 8792, 8793, 8794); thumbnails Standard 4 + thumbnail (get IGA title even if not on first page); pages in order; Final QC (save & confirm twice), Available Everywhere; add "simplified pop" and force mark complete for spotcheck/tagged-item QC.
- **CLONING IS NO LONGER NEEDED. DO NOT CLONE.**
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swaps (baseline video). IGA West-style inserts do not apply here.

---
*Source: IGA Quebec OneGuide (Google Doc `17uX9ZAsJPk9vudaBDIWAct1mxuINtUmATVt4c8XItpE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# IGA Southeast — Processing Guide

> **Source:** IGA Southeast OneGuide (Google Doc `11v7KR2DSaiX8sEc3MvFniW7NlNe-IUQ8hClpEAJ7Sz0`), updated Jun 22, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard / Longtail |
| Availability | All platforms |
| Slack channel(s) | `#kjsmarket` |
| Flyer types | Flyer |
| Processing | Auto-stack; Vendor setup, DOC FQC, Flex Flyer Review; no OS, no coupons, no Feedel/data services |

> **⚠️ Shared banner account:** Kj's Market and IGA Southeast share a version document — the uploaded file includes **both** IGA and Kj's information. **For this account use ONLY the IGA information.** Pages remain in the FTP because it's shared with Kj's Market; ensure **all IGA-labelled files** are uploaded.

## Files & schedule

- **When files arrive:** Wednesday.
- **Publication cadence:** Available From Wednesday → To Tuesday; Valid From Tuesday → To Wednesday.
- **Workflow:** Upload & Setup owned by Vendor/DOC; FQC owned by DOC.

## Upload & setup (owned by DOC)

Generic codesheet built by hand from the retailer version document.

- From the FTP, download the retailer version XLS (e.g. `031126_WLF_VERSIONS_FLIPP`).
- Open a blank Google sheet; add headers **Version, Stores, Page 1, Page 2, …** (as many pages as listed). Copy/paste the corresponding info from the retailer sheet into your columns. Save as **"IGA _date_"** (e.g. "IGA 3.04").
- **Upload the generic codesheet:** Codesheet interface → Name "codesheet" → upload → **Config name = the base path from the FTP where files were dropped** (e.g. `/3.11`). Toggles to **include:** Store or Set Assignment, Page Upload, Allow Pricing Zone Creation, Tile Generate afterwards. Process; complete Flyer Setup once it runs GREEN.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View). Because the FTP is shared with Kj's Market, confirm **all IGA-labelled files** are uploaded.
- Confirm flyer dates (usually first/last page); Thumbnails Standard 4; ensure preview dates are set.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF.** **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing spotchecks (20% of pricing zones at pre-FQC).

## Final QC / flyer review

- Pre-FQC (DOC): dates vs PDF; availability toggles; thumbnails include retailer logo; all items boxed/tagged; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (owned by FLEX; shared guide with Kj's Market).

---
*Source: IGA Southeast OneGuide (Google Doc `11v7KR2DSaiX8sEc3MvFniW7NlNe-IUQ8hClpEAJ7Sz0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# IGA West — Processing Guide

> **Source:** IGA West OneGuide (Google Doc `19rBM54T1ql-vUWioGWidz435XUYoeiw0zbZ1T-uiV40`), updated Nov 24, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#sobeys-dataservices`, `#3fl-sobeys` |
| Flyer type(s) & cadence | **Weekly Flyer (3609)** |
| Processing | Auto-stack |
| Who's involved | Flex (3FL); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Wednesday 3:00 AM → Monday 11:59 PM; Valid Thursday 3:00 AM → Tuesday 11:59 PM.

## ⚠️ Risk items (Scene+)
- **Scene+ callout:** every offer with an accompanying Scene+ offer must have **Scene+ tagged in the Sales Story** — including offers that only show points (no "Scene+" text).
- **Scene Member Pricing items:** Prefix "Scene+ Member Pricing" (**don't forget the + sign**); Disclaimer "$xx without Scene+ Card"; Categories add [Scene+].
- Do **not** tag Scene+ in the disclaimer field — only in the sale story.

## Upload & setup (owned by Vendor — manual)
1. Pages → Edit → IGA West → folder with the flyer publication date.
2. Select all pages → select files → autogroup → Save & Complete.
3. FTP → download the **zone codesheet** for pagination & number of zones.
4. Rearrange pages in the pricing zone per the zone codesheet.
5. **Create pricing zones** — use the zone name from the codesheet as the PZ description; follow the codesheet pagination. One zone → one PZ; more than one → create all (zone 2 has unique pages).
6. **Add stores** — the **Distribution Recap** doc in the FTP is the store distribution list. Open the generic stores codesheet (IGA West tab): column A = stores from the Base Run List, column B = pricing-zone name. Save as .csv. In FAdmin, toggle to codesheet, attach the .csv, Save & Complete ("using the root path" warning → OK). Process Codesheet (should run green); confirm store count matches the Base Run List.
7. **If flap pages:** order P01, FLAP 1, FLAP 2, P02, … then Pricing Zones → More → Storefront Summary to merge the skinny flap pages.
8. Overview → Edit Details: Available From & Valid From **3 AM**; available everywhere; no theme; **External run name** "Weekly eFlyer valid [from date] - [to date]"; preview date = the following Monday; Key Messages (long & short) "Weekly Savings".
9. Thumbnail QC — get the logo: `Thumbnail_1065_x_600` (2 pages), `Stock_premium` (1 page), `Storefront_carousel_premium` (2 pages), `Storefront_carousel_organic` (1 page), `Thumbnail` (2 pages), `First_page_thumbnail_400w` (1 page).
10. Mark setup QC checklist complete; once sessions run, mark autostack spotcheck complete.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required)
- **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
- Box all items attached to a price; include as much of the image as possible; multiple items with one price → same box. Box the sign-up promo box as a whole; box Scene point offers as individual items.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude** SKU.
- **Brand/Name:** always enter brand in the brand field and at the start of the name field.
- **Prefix/Postfix/Price:** use drop-downs, exactly as PDF. "Buy ### or more" → prefix text; "Buy ### at $$$" → description with price as Original Price. **Prices under $1 need a leading "0."** (e.g. $0.51).
- **Valid dates:** only add overrides if the item date differs from the flyer; watch Blue Friday dates.
- **Description:** as in flyer; **lb price is the main price** (lb postfix), **kg price goes in the description** for all produce/meat/seafood.
- **Coupons:** display type Coupon; always tag sales story, disclaimer, valid dates; tag Blue and Green coupons separately; Scene+ offers → Scene+ in Categories and Category Highlights.
- **URLs:** N/A during tagging (deep links added post-processing).

### Image QC
- Pick the cleanest image; if none clean, choose the cutout. **Do not use PDF images** for lifestyle shots, heavy shadows/black outlines, or partial images.

## Post-processing / FQC
- **Item Category QC (Flex):** categories include Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, Scene+, Dairy, Deli, Health and Beauty, Seafood (see OneGuide chart for what falls where). Scene+ items get Scene+ as a **second** category.
- **Deep Links QC (multiple parties, new 02/25/2025):** check the Sobeys Insert Tracker → Deep Links tab (dates in red get no deep links); tag the banner/item as a link with SKU + link.
- **Final QC (DOC, by Tuesday 3 PM):** check Scene+ per PZ (Sale Story contains "PTS"); description lb/kg rule; Sessions → Page Stitch (Stitch All); QC Categories for unreviewed items; **Legibility Heights 50/40**; horizontal + vertical preview; merge skinny pages in storefront spotcheck (if flaps in position 1-2, move the cover page to position 1, flaps follow — retailer instructed this, no notification needed).
- **Inserts:** find the week's inserts in the Sobeys Insert Tracker (WEST tab); upload insert pages (Pages → Edit → Year → IGA → WEST → Inserts, or local); Save and Continue → Process Internally → Submit; box & tag using the link in the inserts doc (or copy from prior week if unchanged — verify URL); add insert pages to **all** PZs at the position in the tracker. Flyer sorting: newest first, then current flyer.
- **⚠️ IGA West does NOT receive Voila inserts** even if listed in the Sobeys insert tracker.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Inserts:** same as above; file an **OPTICS ticket** (OPSMR board), move to "Lead Review" lane and assign to the lead. Sobeys inserts can be combined into one ticket.
- **Troubleshoot:** if sessions fail after adding insert pages, remove the pages from the PZ and from Pages, then re-upload.

---
*Source: IGA West OneGuide (Google Doc `19rBM54T1ql-vUWioGWidz435XUYoeiw0zbZ1T-uiV40`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# IKEA — Processing Guide

> **Source:** IKEA OneGuide (Google Doc `1p2g6USLb7wopGIMZ8kkp-09dL7gwWf2bELSWF85OJOs`), updated Aug 21, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#ikeacanada`, `#flex-processingsupport` |
| Flyer types | Event (1079) — ad-hoc |
| Processing | Auto-stack; Vendor/DOC setup, DOC FQC, Flex Flyer Review; **FSA-based** (no stores); no coupons, no Feedel/data services |

Bilingual account (English + French pricing zones). Linking document used for both Box and Tag.

## Files & schedule

- **When files arrive:** ad-hoc; all publication dates ad-hoc.
- **Workflow:** Upload & Setup owned by Vendor/DOC; FQC owned by DOC.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-Group or manually add grouping numbers; **ensure correct languages** (English for EN pages, French for FR pages). Save & Confirm. **Do NOT process internally.**
- **Pricing zones:** create a **Base pricing zone for EN and one for FR**, select applicable pages, Save & Confirm.
- **IKEA is FSA-based — do NOT add any stores.** Assign FSAs via the **`Assign FSA from CSV` custom action** using the IKEA template: copy the EN pricing-zone ID into the blue `flyer_id` cells and the FR pricing-zone ID into the yellow cells, download as CSV, run the custom action for both zones.

### Setup QC checklist

- Confirm all pages uploaded (Pricing Zone tab → Items View); no un-uploaded SFTP pages.
- Confirm flyer dates (usually first/last page); Thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)

- **Category tagging (recurring confusion):** when unsure of an item's category, **visit ikea.ca and search the item** — use the site's general category. Reference examples: Bathroom (sink, faucet, towel), Bedroom (duvet, mattress, PAX/closet storage, nightstand, bed frame), Decorations (potted plant, picture, poster, Ribba frame, vase, candle holder), Home Accents (vase, candle holder, candle), Kitchen (countertop, step stool, plates, sinks, faucets, cutlery), Living Room (coffee table, bookcase, shelf unit, basket, sofa), Textile (carpets, rugs, curtains).
- **Page links:** some first-page links in the linking document must be set as **Display Type: Page Link**, linking to the page number specified.
- **URLs:** almost all items should have a URL — if an item lacks one, check the link sheet.
- **Brand should NOT be tagged on any item.**

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON (enabled May 2025), Box QC bot OFF.** Linking document required. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media; **include special weblinks only if listed on the link sheet.**
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Linking document required. Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude brand, pre/postfix, and valid dates.**
- **Image QC:** clean PDFs preferred; use cutouts if no clean PDF.
- **Spotchecks:** reference Tag/Tag QC; confirm brand is not tagged.

## Final QC (DOC-owned) / flyer review

- Pre-FQC: verify URLs (almost all items have one; check link sheet for any missing); confirm first-page page-link items set as Display Type: Page Link; dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite.**

---
*Source: IKEA OneGuide (Google Doc `1p2g6USLb7wopGIMZ8kkp-09dL7gwWf2bELSWF85OJOs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Independent City Market — Processing Guide

> **Source:** Independent City Market OneGuide (Google Doc `1ikZpPksToIoNiY-MGLcmyIxnp9NQkU2Vo22b5TJkOOQ`), updated Dec 18, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core · Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | independentcitymarket.ca |
| Flyer type(s) & cadence | **Weekly Flyer** (ICM/LCM) |
| Processing | Auto-stack |
| Who's involved | Flex (3FL + Flyer Review); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available Thursday → Wednesday; Valid Thursday → Wednesday.
- **Preview:** Sunday internal preview (set "Preview start date" to the Sunday before the available date).
- **Linking document:** No.
- **Custom action — Article Corrections:** run the LCL custom action "LCL Article Number Report" to download the Article Corrections report in FAdmin.

## Upload & setup (owned by Flex; DOC drops Final Codes first)

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → show/hide rarely-used fields → Height → select **4096.0 pixels** → OK. If pages are already added, flag to the Full-Time Ops stakeholder and continue.

- DOC must drop the Final Codes into the shared LCL Codesheet Drive before Flex's upload shift.
- Reference the **VM ICM** Final codesheet in inbox for pagination and store changes. **Ignore the PRINT and VM ONLINE tabs**; only process the ICM and LCM tabs (these are the pricing zones).
  - ICM tab only → 1 PZ (ICM), base = 5 stores (all ICM + LCM).
  - ICM + LCM tabs → 2 PZs (ICM, LCM); store sets already separate the stores — confirm assignment.
  - Kosher tab (usually "ICM K") → 3rd PZ (Kosher); confirm store on codesheet. Kosher PZ usually only gets **store #479** (then remove #479 from Base).
- Upload all files under the correct week **as English pages**; number per codesheet (File Code order usually 1, 4, 2, 3, or 1, 4, 2, 3, K).
- Add stores (5 total between zones). Check dates in item view; **no consumer preview**. Check Merchant FTP to confirm all pages pulled in. **No theme.**
- **External Run Name:** "Weekly Flyer - Valid [insert valid dates]".
- Add the weekly codesheet into the shared Google Drive for Flex to complete post-processing.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot OFF)
- **Include** coupons, packaged deals, sign-up page, special weblinks. **Exclude** retailer logo, social media.
- Draw a box only around each item that has a unique price (not additional places). Box interactive "click here" buttons.
- **CON FLAP page:** draw one box over the full page and link out with the PC Optimum digital-coupon load URL provided in the OneGuide.
- **Page-level categories** on every page **except the front cover** (Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce).

### Tag / Tag QC (Medium; Auto-tag ON)
- Include: brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Name:** ALL CAPS, order "Brand Product Name, Quantity" (comma before quantity); product name bolded; English only (French → description). Do **not** put "/kg" metrics, "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — those go in the description.
- **SKU:** enter as shown; **SKU starts with "2"** — if it doesn't, ignore it. Drop leading zeros. Keep unit-of-measure suffixes (`_KG`, `_EA`, etc.) in both SKU and Article Number fields.
- **URLs:** fetch from SKU. If the link goes to a **different item or size**, remove it and find the correct item by name; if it goes to the **Loblaws home page** or the **correct item in a different flavour**, leave the link. All items with a SKU should have a URL.
- **Article Number fields** (bottom of Tag interface): copy the product SKU into Article Number 1 (matches SKU + fetch URL). Multiple SKUs → apply in order to Article Number 1, 2, 3, 4.
- **Joe Fresh callouts:** box and tag as a LINK to joefresh.com/ca.

### Image QC
- Use clean PDF where possible; use cutout if PDF is not clean. Meat/fish must be in a package (else cutout). White background only — no lifestyle backgrounds.

## Post-processing / FQC
- **URL/Links QC (DOC):** reference Final Codes; links are in the Notes section of the final codes; verify Flex's tagging.
- **Pre-FQC (Flex):** spotchecks; merge flap pages to the right page via storefront spotcheck; box/tag codesheet URLs; Legibility Heights 40/30; Image QC; QC thumbnails Standard 4 (start on 2nd/3rd page if flaps at start); Article number check (SKU not blank + URL blank → fetch; Article Number 1 blank + URL not blank → add); no theme; page categories (no category on page 1, 1-3 per page); check geography, vendors tab, vertical scroll; flyer sorting newest at top, secondary pubs last.
- **FQC (DOC):** add flyer ID to LCL Tracker by Tuesday afternoon.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put flyer run ID in the LCL tracker. Flyer sorting: current weekly (regular) → upcoming weekly → secondary pubs newest→oldest.
- **Page swaps** are standard. Completing page swaps often causes **Page Stitching issues** (visible page doesn't match overlaid items) — especially post-live. Best practice: **always rerun Page Tile Generation** after page-swap sessions kick off; if issues remain, rerun and mark complete Vendor Box Tag onward. Open item view of **all** pricing zones to confirm the swap succeeded.

---
*Source: Independent City Market OneGuide (Google Doc `1ikZpPksToIoNiY-MGLcmyIxnp9NQkU2Vo22b5TJkOOQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Independent Food Town (Sobeys) — Processing Guide

> **Source:** Independent Food Town (Sobeys) OneGuide (Google Doc `1sK8KdsjRJXolP20yJPvwVH05cyt0EAUS35IQ1yn8d10`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Publication schedule | Weekly |
| Availability | All platforms |
| Slack channel | `#sobeys` |
| Flyer type(s) & cadence | **Weekly Flyer** — Flyer Type # 3716 |
| Processing | Auto-Stack |
| Who's involved | Flex owns processing; OS completes Upload + FQC |

## Files & schedule

- **Publication cadence:** Available Wednesday, Valid Tuesday.

## Upload & setup

- **Check the FTP** — pages carry the flyer's end date.
- **Manual upload** (auto-group) pages → Save & Complete.
- Flyer Creation: **1 pricing zone = Base.**

### Setup QC
- Add all stores.
- Under Pricing Zones → Items, make sure nothing is cut off.
- Complete Setup QC; set vendor tasks to High.
- **Add box & tag recipe callouts to vendor comments (if applicable):** box & tag the recipe callout on page 1 → `http://familyfoods.ca/recipes/`.

## QC specifics

### Box Draw (Low complexity)
- **Include** special weblinks. **Exclude** social media, coupons, sign-up page, retailer logo, packaged deals.
- No linking document.

### Tag / Tag QC (Low complexity)
- **Include** brand, name, pre/postfix, valid dates, price, sale story, categories, original price.
- **Exclude** description, SKU, disclaimer, URLs.

### Image QC
- **PDF preferred**; only use cutout if the PDF is unclean or unavailable.
- Items with multiple products at the same price are boxed/tagged together.

### ⚠️ Risk item
- Make sure the **Recipe box on page 1 is boxed and tagged** (if applicable) with `http://familyfoods.ca/recipes/`.

## Pre-Final QC tasks
1. Autostack spotcheck complete.
2. Check Details → **Hidden in hosted**, no theme, external run name = "Weekly eFlyer + valid date", key message = "This Week's Deals".
3. Check sessions.
4. QC Thumbnails → 4 basic + `first_page_thumbnail_400w` (1 page) — note in comments.
5. Check leg heights (**40/35**).
6. Confirm the Recipe of the Week is boxed/tagged → `http://familyfoods.ca/recipes/`.
7. Page categories (including first page).
8. Check vertical and horizontal preview.
9. Final QC.

## FQC / Flyer review
- FQC: Sessions, Vendors, Geography; recipe callouts use `http://familyfoods.ca/recipes/`.
- **Page swaps:** open flyer run → Pages → Edit → select new page from FTP → add "REV" to the new page name → Save and Complete → Copy Items from the old page (only if same page) and adjust items that changed → add new page to PZ once boxed/tagged.

---
*Source: Independent Food Town (Sobeys) OneGuide (Google Doc `1sK8KdsjRJXolP20yJPvwVH05cyt0EAUS35IQ1yn8d10`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Indigo — Processing Guide

> **Source:** Indigo OneGuide (Google Doc `1yIqlHCTAcc7YLEtT7bhl0hCBaTl7XRRuYOPqJzHOI_8`), updated May 15, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (Kids Catalogue is **Hidden in Hosted** on the main run; a hosted-only clone handles hosted) |
| Slack channel(s) | `#indigo` |
| Hosted URL | chapters.indigo.ca |
| Flyer types | **Kids Catalogue (1483)** — yearly publication during the holidays |
| Processing | Auto-stack; Flex (Processing Support / setup), FLEX Image QC, DOC FQC; Feedel/data services — **yes**; no coupons |

Linking document (Product Map + Product List) required for both Box and Tag.

## Files & schedule

- **When files arrive:** yearly (holiday season). Dates must be confirmed with the retailer.

## Upload & setup (owned by FLEX)

- **Shell:** create a flyer run in Kids Catalogue; dates confirmed with retailer; internal name per retailer email; **Availability: Hidden in Hosted** (hosted handled by a clone — see Out-of-processing); external run name = the publication callout; apply seasonal theme per campaign.
- **Manual upload:** upload files from the **lowercase folder** (auto-split by Fadmin); do **not** upload the mapping file. Upload as English (default), Auto-Group. If there's a cover page, hold it until the end (cover-page links/category often come later by email).
- **Pricing zones:** Base, English. Create a store set from Indigo's store list — Merchant Page → Store/Sets → CSV with headers `store_set_name`,`merchant_store_code`, upload, add in PZ. **Do not include US stores; remove store 0001** (added to the hosted clone later).
- **Vendor prep:** download the PDF mapping guides from FTP, upload them to a Google Drive; attach the Excel linking document to vendor tasks; email OS the Excel linking document + Google Drive link (recipients in the OneGuide — contacts not stored here).

### Setup QC checklist

- Thumbnails: Standard 4 (plus custom tiles if provided — confirm with BD). **Leg heights 60/50.**

## ⚠️ Common errors / risk items (retailer-specific)

- **Everything is driven by the Product Map + Product List spreadsheet** attached to vendor tasks — box and tag strictly from them.
- **Product Map (boxing):** each product on a page has a letter (A, B, C…). **Box every product separately unless the document says otherwise.**
- **Product List (tagging):** columns give page # (grey), Product ID/letter (red), **Name** (yellow), **UPC/ISBN = SKU** (blue), and **URL** (green). Match each item's letter on the Product Map and tag Name/SKU/URL from the corresponding row.
- **Brand:** enter only in the Brand field — never in any other field.
- **Valid dates:** only add date overrides when an item's sale story indicates it's part of a promotion.
- **Categories:** every item needs one from — Kids, Accessories, Electronics, Toys, Baby, Holiday Home Decor, Gift Ideas, Holiday Gifts, Books, For The Home, Heather's Gifts.
- **Spotchecks:** use the spreadsheet for flagged words; item name must match the spreadsheet (else use the name on the page).

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF.** Linking document required. **Include** packaged deals, sign-up page, social media, special weblinks. **Exclude** coupons, retailer logo.
- **Tag / Tag QC — Medium complexity. Auto-tag OFF.** Linking document required. Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs (all from the Product List).
- **Image QC:** PDF preferred; cutout sufficient if no clean PDF.

### Final QC (DOC-owned) highlights

- Thumbnails Standard 4 (+ custom tiles if provided); leg heights 60/50; **no page categories**.
- Check items without a URL and add if applicable — **Indigo sends updated URL lists; do NOT search their website.** Use PDF images where possible.
- **Tracking codes:** only **one** tracking code allowed (confirm with the lead if more). Overview → Ad Hoc Processing → Manage Tracking Code — Dynamic Variable, Code Source Hosted, variable name/value per the monthly WBS. Click Apply; **re-apply after any page swap.**

## Out-of-processing / hosted clone

- Prefer a preview; link callouts at page bottoms to the website; create a Jira ticket for page-swap triggers.
- **Clone for Hosted 2.0:** clone into the "Guide" flyer type, prefix name with `[Hosted]`, update tracking code per WBS, then Hide in Distribution, Hide in Flipp, Unhide in Hosted; double-check WBS dates; remove all stores and add store 0001.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite.**

---
*Source: Indigo OneGuide (Google Doc `1yIqlHCTAcc7YLEtT7bhl0hCBaTl7XRRuYOPqJzHOI_8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
