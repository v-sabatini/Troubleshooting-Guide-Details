# Cabela's Canada — Processing Guide

> **Source:** Cabela's Canada OneGuide (Google Doc `1tuSU7voGl0teP9Ef_b9m7Xafiomk8URUw_eq5sid19g`), updated Sep 5, 2025. Contacts/credentials omitted.

> **Note:** Bass Pro Shops Canada and Cabela's Canada versions are **both processed in the Cabela's Canada merchant** (single codesheet).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | Two versions — one **Flipp-only**, one **Hosted-only** |
| Slack channels | `#cabelascanada`, `#flex-processingsupport` |
| Hosted URL | basspro.ca/pages/flyer |
| Flyer types | Weekly + ad-hoc (per the Publication Schedule) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday (ad-hoc varies).
- **Cadence:** Available From Wednesday · Valid From Wednesday · Available To Thursday · Valid To Wednesday (ad-hoc varies).
- **Preview date:** yes — **set it per the Publication Schedule** and send the preview link to the retailer for review.
- **Linking document:** yes — used for both Box and Tag; attach to all vendor tasks.

## Upload & setup (owned by DOC)

- **Codesheet:** download the `(Run Name)_Pagination_Flipp.xls` from the FTP. It contains both Bass Pro CAN and Cabela's CAN versions. There is a **"Stores" tab (Hosted)** and a **"Flipp.com" tab (Flipp-only)** — the difference is inserts (inserts display poorly on Flipp Web).
- **Workflow:** upload the Hosted version (with inserts), then clone to a Flipp-only run and remove inserts from all zones.
- **Upload config:** save Stores tab as CSV → upload to the **Hosted** flyer run. **Config = `cabelas_canada`**; PDF base directory copied from FTP; **check everything except Region Assignment and Combine Zones.** Save & Process.
- **Budget is assigned to the Flipp-only run ID** — always confirm the Hosted and Flipp-only run IDs match the Publication Schedule; do NOT swap which version is which.
- **Language handling:** codesheet uploads "Ottawa English" as English, "Ottawa Bilingual" as French, "Moncton" as English only. Manually add NB pages unique to Moncton and upload **French versions**. Create a new **Moncton FR** pricing zone (marked French) and add **store 84** to it.
- Attach the run's Linking Document (`…Flipp+Links.xlsx`) to all vendor tasks.

### Setup QC
- Add preview date per the Publication Schedule; confirm all pages uploaded (check SFTP for stragglers); confirm dates on the flyer vs schedule; thumbnails 4 Standard; add external run names from the schedule / page 1; confirm link sheet attached.

## ⚠️ Common errors / risk items
- **Codesheet inserts are the #1 upload failure.** If the codesheet errors (even with inserts in the SFTP), remove insert rows (usually highlighted orange), rerun, then upload inserts manually and place them via Pages > Layout. The shopbycategory page usually uploads fine. Reference CLSD-4543 for help.
- Upload **English AND French** versions of inserts going into **Ottawa Bilingual** and/or **Moncton** zones; others can be English-only.
- **Moncton uploading English-only is a known AOO** — file a CLSD ticket to have the codesheet processor treat Moncton like Ottawa (EN + FR).
- **Tag in the correct language.**
- **Links are the biggest tagging risk — almost every item should have a link.** The retailer expects very high link accuracy and has flagged even small error counts.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- Linking document required (box + tag).
- **Include (if in Linking Document):** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- All items get one box. **Top-of-page and bottom-of-page links are often missed by Auto-Box — add them in Box QC per the link sheet.** Box the front-page Cabela's logo. Banners → boxed and tagged as a direct link (if no link, tag as an item with a relevant name).

### Tag / Tag QC (Medium; Auto-tag ON)
- Linking document required (box + tag). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Set banners to **Link** display type; find links in the Linking Document. Flag any box with no link. **Most items have a link** — use Cmd+F on the item's full name (some names are similar, so match the full name). Add SKUs comma-separated.

### Image QC
- PDF preferred if clean; otherwise cutouts. No extra retailer Image QC.

### Link QC (post-processing, can be filed to Flex via FAB ticket)
- **New process:** Overview > Items Missing URLs (fill from Linking Document); then Export Items → Google Sheets, keep only Item ID/Name/SKU/URL, sort by SKU, and investigate outliers (multiple versions of an item usually share a link — a differing link flags an error). Correct via Overview > Item Search → open item → fix in Tagging Interface.

## FQC / go-live
- Work in the **Hosted-only run** (has inserts; hidden on Flipp + Distribution). Confirm dates vs PDF + schedule; availability toggles; thumbnails Standard 4 with logo.
- Check **Items Without URLs** and apply from the link sheet. **C runs often have Category pages linked out that Auto-Box missed and OS didn't add** — box them yourself, apply links from the Linking Document, add to all versions of the page.
- Ensure no pages merged; spotcheck largest English + French previews (clickable); geography same WoW; confirm **store 84 in Moncton FR** zone.
- **Flipp-only clone:** copy Hosted run to the matching Flipp run name; when sessions run, Pages > Layout remove all inserts except the Category page; set toggles (hidden on Hosted only, available on Flipp + Distribution); run FQC.
- **Ad corrections:** apply the correct correction to each pricing zone (match file name to stores per Pagination doc; watch EN/FR versions).
- **Flyer Review type: Lite.**
- **Page copying from Bass Pro is no longer done** (historical only).

---
*Source: Cabela's Canada OneGuide (Google Doc `1tuSU7voGl0teP9Ef_b9m7Xafiomk8URUw_eq5sid19g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
