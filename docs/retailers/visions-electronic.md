# Visions Electronics — Processing Guide

> **Source:** Visions Electronics OneGuide (Google Doc `1MUUF_49n2-vvt08zsg-4SBFK-TRpqE8CbXrDblVM10w`), updated Dec 1, 2025. Contacts/credentials omitted.
> **High box-draw complexity.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp & Distribution (**not hosted** — Flipp no longer powers Visions Hosted) |
| Slack channels | `#visions`, `#flex-processing support` |
| Hosted URL | http://www.visions.ca/eFlyer/default.aspx |
| Flyer types | **Weekly** (ID 7184), goes live every **Friday** |
| Processing | Auto-stack; Flex; DOC-owned; no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Workflow:** Upload & Setup (5 business days out / Friday before, DOC) → Spotchecks & FQC + send retailer preview (2 days out / Wednesday, DOC) → FQC (1 day out, DOC) → Live (Friday).
- **Dates are NOT on the PDFs** — confirmed by the retailer in file-drop emails.
- **Linking document:** Yes (SKU/URL spreadsheet from FTP) — used for package items and banner (direct-link) tagging. Individual items generate links from the SKU.

## Upload & setup (Flex)

- Manual upload (normally **1 pricing zone — Base**, add all stores). Uploaded to flyer type "Flyer"; select the run with the correct live date (ad goes live every Friday). Pages → Edit → select the folder titled with the live date → select all pages → Select Files.
- **Versioning (less common since 2024):** if the retailer specifies different pricing zones by email, build PZs by page version — e.g. pages ending "AB" = Alberta version; "AOMKTS" = All Other Markets. Email the retailer to confirm discrepancies.
- **Sign-up page** is manually uploaded and placed in the **last position**.
- Download the links spreadsheet from FTP and attach to Tag and Links QC on the pipeline.
- **Setup QC:** confirm all pages uploaded (PZ Tab → Items View); confirm dates; complete 4 standard thumbnails; ensure preview dates set.

## QC specifics

### ⚠️ Box Draw (HIGH complexity; Auto-Box ON, Box QC bot OFF; linking doc required)
Include coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Box every item with a price separately.** If one product has multiple prices, put a **text box** around the lowest price and box the other prices separately as items. If two items share a product name but have different prices, box the prices separately.
- **Banners & links (specific URLs):**
  - Financing banners → link to `http://www.visions.ca/info/finance`.
  - **Sign-Up Page** (last page) → tag as "SHOW URL IN iFrame", URL `https://f.wishabi.net/arbitrary_files/36600/1474489548/36600_Flipp_Visions-Newsletter-Signup.html`, iFrame width 700, height 450.
  - "In-home Setup Solutions" MORE INFO → `http://www.visions.ca/content/homesetup/`.
  - Box promo banners (e.g. "Save up to 50% Off Car Install Labour") **separately** from the item — any promo not tied to the product gets its own box.
  - "Find a Store" button → link `https://www.visions.ca/storelocator/default.aspx`.
  - Rebate "Click Here to Download" banners → link to the rebate-form PDF URL provided.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required)
Include name, pre/postfix, valid dates, **SKU (copy from SKU/URL doc)**, price, categories, disclaimer, original price, **URLs**. Brand = No. **Exclude Description and Sale Story** (description typically blank).
- **Use the URL spreadsheet the DOC attaches** for item URLs and for Banner (Direct Link) names.
- If item dates differ from the run dates, put them in the item pop.
- Current Price = sale price; Original Price = before-sale; discount → designated field. Postfix e.g. "or $XX Monthly".
- **Do NOT include monthly-payment text** in name/description/disclaimer (e.g. "OR $XX.XX MIN. MONTH PMT").
- **Description usually left blank** — only used if no product page (URL) or a TV home-theatre package; never put descriptive subtext before the bold name; never put SKU in description.
- **SKU** = the advertised item's SKU (not the bonus item). TV SKUs: ensure only the TV size is in the SKU. One price with multiple SKUs → tag all SKUs.
- **Cell pages:** Prefix "As low as", Current Price 0, Postfix "Down", Sale Story "and $XX per month", Disclaimer "Full device price $X".
- **Category chart:** TV & Video; Home Audio & Accessories; Camcorders & Digital Cameras; Portable Electronics; Car Audio/Video; Cell Phones & Accessories; Furniture & Accessories (TV stands, media cabinets, massage chairs); Car Electronics & GPS; Smart Home Control & Automation (incl. security cameras); Computers; Laptops & Tablets; Appliances. (Security cameras → Smart Home, not Cameras; Car Audio not under Home Audio.)

### Image QC
Use **cutout images**. Select PDF image only if available and clean, and it must show the actual electronic (e.g. the TV itself, not the program on screen). **Packages/bundles → leave as a cutout** so all products show; never pick a PDF of one item in the package.

## FQC / go-live

- **URL/Links QC (DOC):** "Items without URL" on Overview; compare against the SKU doc; apply any missing URLs.
- **Item Category QC & Item Image QC (DOC).**
- **Final QC (Flex):** Geo, PZs (all stores), all pages tagged, QC thumbnails; Item Image QC; page categories 1–3 per page except page 1; check items without URLs vs linking doc.
- **[Optional] Preview QC (Flex):** spotlights & storefront sale story from front page; Image QC; full category QC; check toggles (all platforms); mark items store-only; **leg height 55/45**; thumbnail QC (custom tile from FTP); geography vs previous week. (Post-PQC clone to a "Buy Online" flyer type is noted as no longer needed.)
- **Post-FQC (DOC):** send preview by Wednesday / Thursday morning at latest; action items from the Visions Corrections Sheet before go-live.
- **Flyer Review type: Lite** (DOL): name from email; dates per PDF; **not available on hosted**; mark store-only; no special tile; one version all stores; email insert as last page; product links & category pages tagged.

### ⚠️ Live-date / PQC common errors
- Search-page results instead of item results.
- Individual item URL instead of the package URL.
- **Flipp no longer powers Visions Hosted — check live dates on flipp.com.**

---
*Source: Visions Electronics OneGuide (Google Doc `1MUUF_49n2-vvt08zsg-4SBFK-TRpqE8CbXrDblVM10w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
