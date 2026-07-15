# ANBL (New Brunswick Liquor Corporation) — Processing Guide

> **Source:** ANBL OneGuide (Google Doc `1GE_oRs_xrglC9JbFqLotxEAa3PumKEwN81fBBNCwY5Y`), updated May 9, 2024.
> Bilingual (EN/FR) retailer. Contacts/credentials omitted (SFTP login and password are in the OneGuide — not stored here).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#anbl` |
| Hosted URL | anbl.com |
| Flyer types | Weekly |
| Processing | Auto-stack; **Flex = Flyer Review**; **OS = Setup**; no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday. The retailer emails a WeTransfer link **or** a PDF attachment (one big English PDF + one big French PDF) plus a linking document; you upload them to Core FTP/FileZilla yourself (creds in the OneGuide — not stored here). The two big PDFs break out into individual pages.
- **Cadence:** Available From Monday, Valid From Sunday. Dates are pre-set in the flyer shells.
- **Linking document:** Yes.

## Upload & setup (owned by Flex; manual upload)

- Create a new folder in the FTP and upload the EN + FR PDFs.
- Pages → Edit → Select files. **Upload the French files → mark FR language → Save → refresh** to confirm all FR. Then **upload the English files → mark EN language → Save.** Auto-group → Save & Complete.
- **Pricing zones:** EN (English files) and FR (French files). Ignore the "stores in another zone" warning.
- Wait for sessions to run.
- **Attach the linking doc as `.xlsx`.**
- Edit Details: no theme, available everywhere. Legibility heights (pre-set) **45/35**. Thumbnails Standard 4. Geography: no stores added/removed.

### ⚠️ Common errors / risk items (retailer-specific)

- **Split the linking doc into EN and FR** — create 2 separate `.xlsx` files. Attach the English linking doc to English vendor tasks and the French linking doc to French vendor tasks.
- **Beer case size in Item Description is usually inaccurate** — verify against the flyer during FQC.
- **Unique item valid dates** — verify Valid From/To against the flyer.
- Setup QC: confirm the linking document ("Flyer pricing") is attached; double-check dates against the publication schedule.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks. Box each item per the spreadsheet (single or multi-item); use a text box for the text next to each item.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-select ON):** linking doc required. Include name, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific. **Exclude pre/postfix.** Tag items with multiple versions separately; tag the bottom banner on each page as a **Link** type.
- **Image QC:** tends to be all cutouts — double-check.

## FQC / go-live (owned by DOC)

1. **Items without URL** (Overview) should be 0 — if not, cross-reference the linking doc.
2. Pricing Zone tab → Item QC: # of boxes and tags equal/similar.
3. Pages tab: first page(s) no categories; **RISK** — verify unique valid dates against the flyer; **RISK** — recheck beer case size in item descriptions.
4. Image QC: usually cutouts, double-check.
5. Pages tab all 3 numbers green & equal; sessions run; vendor tasks complete.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: ANBL OneGuide (Google Doc `1GE_oRs_xrglC9JbFqLotxEAa3PumKEwN81fBBNCwY5Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
