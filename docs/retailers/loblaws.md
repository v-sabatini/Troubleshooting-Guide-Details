# Loblaws — Processing Guide

> **Source:** Loblaws OneGuide (Google Doc `1xCQmd7NhAvZ8ZYrmkbM9ojVQ1VgFiME8NwDZOjodNs0`), updated Aug 13, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core / 1 Premium |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lclA` |
| Hosted URL | loblaws.ca |
| Publications | 1 Weekly (Loblaws regular/LSL, flyer type 3400) + Loblaws City Market (pulled from YIGW, flyer type 5048) · ad-hoc General Merchandise |
| Processing | Auto-stack; Flex 3FL; no coupons; Feedel/retailer data services |

The banner has **2 flyers each week**: Loblaws (weekly/LSL) and Loblaws City Market (YIGW).

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday.
- **Preview date:** Sundays (internal preview). Prior to Flex's upload shift, DOC drops the Final Codes in the shared LCL Codesheet drive.

## Upload & setup (owned by Flex)

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE uploading any pages** (Edit Details → show/hide rarely-used fields → Height → 4096.0). If pages are already added, flag to the FT stakeholder and continue. Applies to both Weekly and City Market runs.

### Loblaws Weekly (flyer type 3400)
- Find code sheets in the LCL Codesheets folder. **NEW 2026:** locate two files, **LSL SUB and LSL URB**, and combine their tabs into a single master Google Sheet (use the most up-to-date "REV" versions).
- Codesheet manipulations: delete print tab, Online Hybrid tab, hidden Date tab. For every tab: delete effective date/ERROR (B1), delete the row with the final date, add "Printer Notes:". **Change "STORE NAME" to "STORE ADDRESS" on all tabs** (missing any = missing pricing zones). Delete store totals. Download as XLSX.
- Codesheet upload: **Config `loblaws`**; base path = the weekly (LSL) files path from FTP (not hybrid); **toggles: select all but the second and last**.
- After upload: open the cross-language French version of each PZ, toggle language French, save.
- **Hybrid pages** (uploaded manually): Pages → Edit → HYBRID folder → English pages. Create PZ "HYBRID" (all hybrid pages) and "HYBRID FR" (same pages, cross-language French). Add HYBRID store 1424 to both. (The HYBRID codesheet is reference-only, not for upload.)
- Add the weekly codesheet to the LCL Google Drive for Flex to complete post-processing.
- **Leave a note in every vendor task: "No need to use DVM tagging rules".**

### Loblaws City Market (flyer type 5048)
- Manual upload: Pages → Edit → YIG folder → YIG WEST subfolder → select all files **except** those with a "w" in the name (wb, ww, wy).
- Use codesheet "YIGW" from the City Market folder — reference only the **"CITY" tabs**. Number pages per codesheet; create PZs matching the number of "city" tabs; name PZs to match tab names; add stores by store number (store count per PZ must match the codesheet).
- Double-check dates vs the printed flyer; preview Monday; setup QC; geography shouldn't change; add any URLs from codesheet notes to the run comments.
- **Leave a note in every vendor task: "No need to use DVM tagging rules".**

## ⚠️ Common errors / risk items

- **Pixel Height 4096 must be set before any pages are uploaded** (NEW 2026).
- **STORE NAME → STORE ADDRESS** on all codesheet tabs, or pricing zones won't be created.
- **Codesheet errors:** "multiple pages match in FTP" (only error → force processing); "Found a reused PDF file within the same pricing zone layout" → check for duplicate pages, else delete the rows at the positions named in the error and update page-position numbers (manually add any removed pages). Watch for added characters in Pricing Zone names (breaks processors) and hidden tabs.
- Check FTP after upload for pages that didn't pull in; manually upload leftovers to the correct PZs.
- **URL mismatches:** a fetched URL leading to a different item/size → remove and search by product name; home page → leave; correct item different flavour → leave.

## QC specifics

- **Box Draw (High; Auto-Box ON, Box QC bot OFF):** include coupons, packaged deals, sign-up page, social media, special weblinks; exclude retailer logo. Box each unique price; box "click here" interactive buttons. **CON FLAP page:** one box on the full page linking to the PC Optimum digital-coupon load URL.
- **Tag / Tag QC (Medium; Auto-tag ON):** **As of July 2025 — do NOT use DVM tagging rules** (proceed without the DVM OS Updates sheet; tag as normal). Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Custom fields: Article Number 1–4.
  - **Name:** ALL CAPS; order "Brand Product Name, Quantity" (comma before quantity; no space between number and unit, e.g. 60G; "6 x 10 mL" → "6x10mL"). English only (French → description). Exclude "Product of…", "No 1 Grade", "Frozen", "Selected varieties", per-kg metrics (→ description).
  - **NEW:** "Less Than #, $$$ ea." prices go in the **Description**, not the Sale Story; do not fill postfix for Less Than items.
  - **SKU:** starts with "2"; drop leading zeros; keep unit-of-measure suffix (e.g. `_KG`) in both SKU and Article Number. Ignore SKUs not starting with "2".
  - **URLs:** enter SKU then Fetch. If link → different item/size, remove and find the correct item by name (search loblaws.ca / atlanticsuperstore.ca / nofrills.ca). Home page → leave. All items with a SKU get a URL.
  - **Article Number** (special fields): copy the product SKU into Article Number 1 (2 = second SKU, etc.); include unit-of-measure suffix. Never remove/edit an existing article number unless identical to the SKU.
  - **Joe Fresh banners:** box and tag any "Joe Fresh" callout as a LINK → `joefresh.com/ca/`.
  - PC Optimum Members Pricing = Current Price with a "PC Optimum Members Pricing" prefix. Every item needs a category.
- **Image QC:** use clean PDF where possible; cutout if PDF isn't clean.

## Post-processing & FQC (owned by DOC)

- **URL/Links QC:** reference the Final Codes; links are in the Notes section.
- **Pre-FQC (Flex now completes):** spotchecks; check codesheet URLs (usually PC Express or Joe Fresh); merge flap pages to the right page; leg heights (45/25); mark Image QC complete; QC thumbnails Standard 4 (redraw for Urban PZs EN/FR and Hybrid, starting page 1); No Theme; External Run Name "Weekly Flyer - Valid [dates]".
- **Article number check** (Item Search): Article Number 1 IS NOT blank & URL IS blank → open & Fetch; Article Number 1 IS blank & URL IS NOT blank → add article number.
- Remaining FQC: pagination/PZs match codesheets; sessions; vertical & horizontal scroll; boxes (PZ with most stores). **City Market (YIGW):** valid from 3am, move to Weekly flyer type.
- **Flyer sorting:** most recent flyer at top, secondary publications last.
- Update the LCL Tracker by 2:30 Monday (weeklys only, not secondaries or City Market).
- **Flyer Review type: Lite** (owned by DOL).
- **Live-dates flags:** URL leads to a different item → FLAG; item quantities in the description → FLAG.

## Out-of-processing

- Put flyer run ID in the LCL tracker; flyer sorting (weekly always first: current, upcoming, then secondary pubs newest→oldest).
- **Page swaps** often cause page-stitching issues (visible page doesn't match overlaid items), especially post-live. **Always rerun Page Tile Generation after page-swap sessions**; if issues persist, rerun and mark complete Vendor Box Tag onward; confirm the swap in item view for all PZs.

---
*Source: Loblaws OneGuide (Google Doc `1xCQmd7NhAvZ8ZYrmkbM9ojVQ1VgFiME8NwDZOjodNs0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
