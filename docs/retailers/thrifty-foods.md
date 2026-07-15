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
