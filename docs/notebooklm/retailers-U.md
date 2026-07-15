# Retailer Processing Guides — U

> Bundle of 3 retailer-specific processing guides (U). Contacts and credentials are omitted from every guide.

**Contains:** UHome Mart, Uniprix, United Farmers of Alberta (UFA)


---

# UHome Mart — Processing Guide

> **Source:** UHome Mart OneGuide (Google Doc `1BURnq_27QeYhufkucPlmVN1ogOYcxISFtTl3O5yz5bY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Hosted URL | N/A |
| Flyer type(s) & cadence | Flyer |
| Processing | Auto-stack; Upload/Setup (Vendor) → FQC (Vendor); Flyer Review (Vendor); no coupons; no Feedel/data services |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Friday · Available To Thursday · Valid From Friday · Valid To Thursday.
- **Linking document:** N/A.

## Upload & setup (Vendor, manual)

1. Pages tab → Edit → select all pages from the SFTP menu. The folder is named by the flyer's valid date — **always use the lower-case folder; do not upload the Upper Case folder.** Confirm & Upload.
2. Auto-Group → Save & Complete.
3. **Pricing zone:** create one zone called **Base**, add all stores. Save & Complete.

### Setup QC checklist

- Confirm all pages uploaded: in the SFTP no pages should remain **except the 'multi-page' PDF** (the Upper Case name not ending in `P####`). If pages were missed, flag to the FT team.
- Confirm flyer valid dates match page 1 of the PDF.
- Complete thumbnails (**4 Standard**).
- **Geography tab: ensure 0 changes to stores or FSAs** — flag any change (100% of discrepancies) to the FT team via Slack/email, but continue the checklist.
- Platform toggles: available on **all** platforms.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** no linking document. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include brand, name, pre/postfix, valid dates, description, price, original price, sale story, categories, disclaimer. **Exclude SKU and URLs.** Image: always select a clean PDF if available.

## Pre-FQC / FQC (Vendor)

- Confirm valid dates vs. PDF; platform toggles available everywhere; thumbnails drawn with retailer logo. Standard checks: all items boxed/tagged, previews clickable. **Geography consistent with last week (no stores/FSAs added or removed)** — immediately flag 100% of discrepancies to the FT Ops team (does not block work). Complete FQC checklist.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: UHome Mart OneGuide (Google Doc `1BURnq_27QeYhufkucPlmVN1ogOYcxISFtTl3O5yz5bY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# Uniprix — Processing Guide

> **Source:** Uniprix OneGuide (Google Doc `1xUcqTvwoZUT1Y1yQj1BI1-IdJGp3hVpFpImrWYgg8oY`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#mckesson` |
| Flyer type(s) & cadence | **Weekly Flyer (#3551)** and **Uniprix Sante (#6648)** — both weekly (Thu–Wed) |
| Processing | Auto-stack; Upload/Setup (Flex) → FQC (DOC/Vendor); Flex (Processing Support + Flyer Review); Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence — Weekly:** Available From Tuesday (2-day consumer preview) · Valid From Thursday · Available/Valid To Wednesday. **Sante:** Available From Thursday (**no preview**) · Valid From Thursday · Valid To Wednesday.
- **Bilingual:** all pages uploaded in **French**; two pricing zones per flyer — **FR** (French) and **ENG** (English cross-language).

## Upload & setup (Flex, manual)

- **Weekly (#3551):** upload all pages, group per the pagination spreadsheet in the SFTP (week number is in the comment section). Place "Insert" pages at the end. Create 2 pricing zones (FR = French, ENG = English cross-language). Add the **"Uniprix Stores"** store set to both.
- **Sante (#6648):** upload pages (format DDMM, typically 4 pages) in French. Create 2 pricing zones (FR/ENG). Add the **"Uniprix Sante Stores"** store set to both.
- **Sante store assignment via codesheet:** download the SANTE store doc from the merchant FTP; build a tab with Column A = stores (from the "SAP" column), Column B = pricing zone. All get **ENG**, then paste the SAP again and apply **FR** (match the PZ names in Fadmin). Remove the "# " prefix from store codes (find "# " → replace with blank). Save as CSV, upload — **Config `generic_stores`**, base directory `/`, **only the first toggle**, save & process.

### ⚠️ Common errors / risk items (retailer-specific)

- **Incorrect boxing** is the top risk on both the Weekly and Sante flyers — follow the box-draw instructions exactly.
- **Bilingual tagging required** — include both English and French text in every field.
- **Valid-date overrides** at item or page level are rare and easy to miss — watch for them.
- **Upload all pages in French** (this is easy to get wrong given the ENG cross-language zone).

## QC specifics

- **Box Draw (HIGH complexity; Auto-Box ON, Box QC bot ON):** no linking document. **Include** coupons and packaged deals; **exclude** retailer logo, sign-up page, social media, special weblinks. Generally one box per price; when text applies to more than one product, box products individually; similar products may occasionally be boxed together with the smaller item's info in the description.
- **Tag / Tag QC (Medium; Auto-tag OFF):** linking document required (Tag/QC-specific). Include brand, name, pre/postfix, valid dates, description, SKU, price, original price, sale story, categories, disclaimer. **Exclude URLs.**
  - Brand as it appears; if multiple brands, do **not** use the brand field — put all in Name with item types separated by commas. Name = brand + name + item.
  - Descriptions fully bilingual; for multi-item boxes include the brand in the description to distinguish; add any quantity to the description. Postfix usually "CH./EA."
  - Sale story: an orange/yellow circle → "Bas prix garanti/ Low Price Guarantee". Exclusions go in the disclaimer.
- **Image QC:** select the most applicable PDF image with white background; no black shadows; multi-item → pick the PDF of just one.

## Pre-FQC / FQC

- Leg heights **40/30**; thumbnails Standard 4; geography same WOW (correct store set); **mark items in-store only**; cross-language all ENG zones to English.
- **Weekly:** remove all "E#" pages (E1–E4) from both zones — these become a separate **Carnet Beaute** run (cloned into Catalogue flyer type; assign only the E# pages; Standard 4 thumbnails with brand logo not cut off; **no insert**).
- **Add inserts:** pull upcoming inserts from the shared Drive, match the Promo/week number in the Fadmin comment box, upload and change language to French, box/tag as a **Direct Link** with the URL from the spreadsheet, add to the ENG zone at position 20, then replicate to FR via the Cross Language Adjustments SOP; verify in vertical preview (re-run Page Tile Gen if missing).
- **Top Product tagging (Weekly):** from the FTP Top Product Sheet, for the six listed items set the last tagging field "Important" = YES and ensure the Brand field is filled.
- **Sante:** clone to Uniprix Sante (matching date); the clone won't pull stores — re-add the Uniprix Sante Stores set; complete FQC for both clone and main Sante run.

## Out-of-processing (recurring inserts)

- Five **brand-owned inserts** (Option+, French/Our Trusted Brands, Nosh&Co, Savvy, Kit) are added to the end of the flyer every week (URLs per the OneGuide table), plus any additional inserts per the retailer's Wednesday email. Add to both Weekly and Sante runs; may copy items from the prior run when inserts are unchanged.

## Flyer review

- **Flyer Review type: Lite.**

---
*Source: Uniprix OneGuide (Google Doc `1xUcqTvwoZUT1Y1yQj1BI1-IdJGp3hVpFpImrWYgg8oY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*

---

# United Farmers of Alberta (UFA) — Processing Guide

> **Source:** United Farmers of Alberta (UFA) OneGuide (Google Doc `1t94yaUWOPMzAaLhF5BjVfUbucoguGTwKnykgzNu0y9w`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | retailer channel, `#flex-processingsupport` |
| Flyer type(s) & cadence | Weekly SALES DS and Monthly. Setup split by region: **AB pages (549 Flyer)** and **SASK pages (12003, "230kmflyer")** |
| Processing | **Trim Stack**; Upload/Setup (Flex) → Image QC (Flex) → FQC (Flex/DOC); Flyer Review (DOL); Strategic Ops (Feedel/data services) — yes; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday.
- **Linking document:** sent over email — if not attached in ClickUp, reach out to the processor for it.

## Upload & setup (Flex, manual)

Setup is done per region into separate runs:

- **AB pages (Flyer 549):** Pages → Edit → select all **AB** pages from the SFTP (or upload from email). Auto-Group / grouping numbers; language = **English**. Create **Base - AB** pricing zone with all applicable pages; add all stores. Attach the emailed linking document to all vendor tasks.
- **SASK pages (Flyer 12003 / 230kmflyer):** same steps selecting **SASK/SK** pages; create **Base - SK** pricing zone; add all stores; attach linking document.

### Setup QC checklist (both regions)

- Confirm all pages uploaded (Pricing Zone → Items View); **RISK:** confirm no SFTP pages left un-uploaded. Confirm flyer dates. Complete thumbnails (**4 Standard**). Complete Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **Get the linking document** from the full-time member if not attached — required for both box draw and tagging.
- **URLs:** use the links from the retailer XLS on **all** items — match the SKU from the flyer page to the tagging document to find the URL; if no SKU, match by item name.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** linking document required. **Include** coupons, retailer logo, sign-up page, social media, special weblinks; **exclude** packaged deals. Box **every individual item** with its price/SKU/name (item-pop, clean boxes). Use text boxes when item and text aren't side-by-side. Box sale banners.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF auto-select ON):** include brand, name, description, SKU, price, original price, sale story, categories, disclaimer, URLs. **Exclude pre/postfix and valid dates.** Tag name as it appears in the Product Name, SKU and Links columns; price/sale story/disclaimer from the PDF.
- **Image QC:** choose clean PDFs where possible on the right-hand side of the tagging interface **as you tag**.

## FQC (Flex)

- **Check URLs:** open the linking document attached to vendor tasks, review every link on each page, then add a comment "All links checked".
- Spotchecks if required. QC thumbnails Standard 4 (stock premium, storefront carousel premium/organic).
- Edit Details: run dates match the PDF; available everywhere; external run name — Regular Monthly: `*Month* Flyer *Year* AB (Alberta)` (e.g. "June Flyer 2026 AB (Alberta)"); 230kmflyer/SASK: `*Month* Flyer *Year* SASK (Saskatchewan)`.
- Flag missing pages or geography changes to the full-time team. Complete FQC checklist.

## Flyer review

- **Flyer Review type: Lite** (owned by DOL).

---
*Source: United Farmers of Alberta (UFA) OneGuide (Google Doc `1t94yaUWOPMzAaLhF5BjVfUbucoguGTwKnykgzNu0y9w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
