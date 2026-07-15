# Kosher (Sobeys) — Processing Guide

> **Source:** Sobeys Kosher OneGuide (Google Doc `1DCXIowBsbdI9QOaf8zO468HCd_v-L8UpscrVDb5igOo`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · S1C1 |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeys-ops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URL | sobeys.com |
| Flyer type(s) | Weekly Flyer — Kosher |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **Vendor** owns upload & Image QC; **FLEX/3FL** owns FQC & Flyer Review; **OS** setup |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available Wednesday–Wednesday, Valid Thursday–Wednesday.
- **Linking document:** No.

## Upload & setup (owned by FLEX)

1. Pages → Edit → Week → select **ONTARIO → Kosher →** dated folder → drill to individual pages. Select all → Select files → Auto-group → save & complete → submit.
2. Pricing zone: Desc `base`, Language English (confirm pagination/index) → save & done.
3. Add stores for the Sobeys Kosher pricing zone; refresh.
4. Sessions: confirm running (page level then flyer level). **RISK:** an "update distributions" warning can be ignored as long as stores/FSAs are assigned to the zones.
5. Merchant page → details → FTP path → "hide uploaded" → search → check off the Kosher codesheet (keeps FTP clear).
6. Edit Details: **External Run Name = `MM/DD - MM/DD` valid range** (e.g. `Weekly eFlyer 03/24 - 03/30`); no theme; Key Messages Long "Weekly Ad. Weekly Savings." Short "Weekly Ad."
7. Confirm next steps assigned to OS, priority **High** (short turnaround).
8. Thumbnails: 1065x600 (pg 1&2), Stock Premium (pg 1), Storefront Carousel Premium (pg 1&2), Storefront Carousel Organic (pg 1), thumbnail (pg 1&2), fpt_400w (pg 1).
9. Mark Autostack spotcheck complete (completes the vertical-preview auto-publish task in FQC).

## ⚠️ Common errors / risk items — Scene+

- **Scene+ callouts:** every offer with an accompanying Scene+ offer must have **"Scene+" in the Sales Story** — even if the flyer only shows points, tag Scene+ in the Sales Story (NOT the disclaimer).
- **Scene+ PTS sale story** must read exactly **"### Scene+ PTS"** (e.g. `500 Scene+ PTS`) — not "500 PTS", "500 Scene", or "500+ PTS".
- **Scene+ Member Pricing items:** Prefix "Scene+ Member Pricing" (keep the **+**); Disclaimer "$xx without Scene+ Card"; Categories add `[Scene+]`.
- **Pepsi/Coca-Cola soft drinks** flagged as a risk item (grocery).
- **Inserts (updated Mondays):** find them in the Sobeys FTP under folder path **"kosher" OR "Ontario"** (use whichever is present); box one box per page, tag as display type **Link** with file name + URL from the insert tracker; add into pricing zones per the tracker; then create an Optics ticket for the lead.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** retailer logo and special weblinks; exclude coupons, packaged deals, sign-up page, social media. Exclude Kosher Market banners.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** brand/name in the branding field only (don't duplicate in name). Include pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU**; URLs excluded unless it's an insert.
  - **KG/LB:** lb price is the main price with `lb` as postfix; **kg price goes in the description** for all produce/meat/seafood.
- **Item Category QC** uses a fixed category chart (Bakery, Pharmacy, Grocery, Pet Care, Home, Baby, Meat, Floral, Produce, **Scene+** [second category on Scene+ items], Dairy, Deli, Health & Beauty, Seafood). Page categories: **all pages get Scene+ and Grocery**, plus all remaining relevant categories.

## FQC / flyer review

- **Leg height 40/35.** Item Image QC (clean PDFs, white background, no shadows — else cutout). Re-run page stitching. QC categories + page categories. Scene+ check via Item Search: Sale Story contains "PTS". Confirm inserts added (note in comments). Other red errors/warnings can be ignored.
- **Flyer Review type: Lite.**

---
*Source: Sobeys Kosher OneGuide (Google Doc `1DCXIowBsbdI9QOaf8zO468HCd_v-L8UpscrVDb5igOo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
