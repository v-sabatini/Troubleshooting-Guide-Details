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
