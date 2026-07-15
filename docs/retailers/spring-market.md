# Spring Market — Processing Guide

> **Source:** Spring Market OneGuide (Google Doc `18dVairXtTmpIUdWnZ8MrSa6aqj6XZAkpdkuNgAsFKnU`), updated Dec 8, 2025. Contacts/credentials omitted.

> Spring Market is a **Brookshire's** banner (config `brookshires`, Slack `#brookshires`).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#brookshires` |
| Hosted URL | spring-market.com |
| Flyer type(s) & cadence | **Weekly** (type 7939) + **Monthly** (type 10561). Files Monday; Available From Tuesday, Valid From Wednesday; Available To Monday, Valid To Tuesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

> **Timezone:** FAdmin runs on EST; Brookshire's is Texas-based (CST). Set valid-from = **1 AM** so it goes live at the right time.

## Files & schedule

- **When files arrive:** Monday.
- One-day consumer preview for both weekly and monthly publications.

## Upload & setup (owned by Flex)

1. **Codesheet:** search the FTP for the `.txt` manifest file matching the flyer's naming convention and save it locally.
2. **Codesheet tab → upload the manifest:** Name = flyer naming convention; Config name **`brookshires`**; **PDF Base Directory = `/flyer_zone_pages_pdfs`** (always this base path). Save → Process codesheet.
3. **Deals file:** from the FTP, save the correct deals `.txt` file. Copy its text into Excel and manipulate: Data → Text to Columns → Delimited → uncheck all → check "Other" = `|` → Finish; filter the first row; change columns A & G from general to whole numbers; highlight cells A1, C1, G1 for OS. (6a–6d can be done via macro.) Save as `.xlsx` using the FTP file name.
4. **Vendor tab → Upload Mass Attachment:** attach the Deals Excel file **and** the Blowline file to all vendor tasks.
5. **Edit Details:** no theme; available everywhere; **valid-from = 1 AM**. PZs have staggered dates → adjust all zones to a 1-day preview.
6. Leg heights 40/30; Standard 4 thumbnails; complete Setup QC checklist.

### ⚠️ Common errors / risk items (retailer-specific)

- **"Missing page" codesheet error:** make sure the naming convention in the manifest matches the FTP; correct it in the manifest → save → reupload.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** include coupons, retailer logo, sign-up page, social media; exclude packaged deals and special weblinks. Draw a box wherever there's a unique price.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required; PDF image auto-selection ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Name:** enter as "Brand Product Name" (appears in larger, bold text). **Description:** smaller text below the name; first letter of the first word MUST be capitalized (e.g. "100% natural", weight, "Selected Varieties").
  - **Pre/Postfix:** do NOT use a postfix for "When you Buy ### In a Single Transaction" — put that in the disclaimer. eCoupon offers → postfix "FINAL PRICE WITH COUPON".
  - **Valid dates:** apply date overrides only if a related sales story indicates the item is part of a promotion.
  - **URLs:** Spring Market banner links to the merchant landing page; social icons link to their platforms.
  - **Categories:** label page categories by products/headers; if multiple categories on a page, label those with 3+ products.
  - **Sale Story:** e.g. "BUY ONE GET ONE FOR $0.01" goes in the sale story.
  - **Image QC:** apply clean PDF images where possible (no shadows); use cutouts if no clean PDF.

## Final QC (owned by DOC)

1. Mark Autostack complete.
2. Item Search: **UPC → Is → (blank)** — fill missing UPCs from the linking doc (vendor tab), leave note "UPC checked".
3. Page Categories (page 1 can have categories).
4. Pricing Zones — regions should have the same/similar items per flyer. Check Geography.
5. Re-run outstanding sessions; check outstanding vendor tasks.
6. **Flyer Sorting:** older flyer first, preview second, monthly last.
7. Complete FQC Checklist.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Spring Market OneGuide (Google Doc `18dVairXtTmpIUdWnZ8MrSa6aqj6XZAkpdkuNgAsFKnU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
