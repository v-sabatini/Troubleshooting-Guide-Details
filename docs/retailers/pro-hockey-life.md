# Pro Hockey Life — Processing Guide

> **Source:** Pro Hockey Life OneGuide (Google Doc `1BhyDdjdtV0WlVrIpW-Wtw2lSyfnhpVacW_4GETUgoDs`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fglsports-banners`, `#flex-processingsupport` |
| Hosted URL | prohockeylife.com/pages/flyers |
| Flyer types | Ad-hoc / seasonal |
| Processing | Auto-stack; Vendor setup, OS setup, Flex + DOC QC; no coupons, no Feedel |

## Files & schedule
- **Files received / cadence:** Ad-hoc (all dates ad-hoc). Preview available 1 day before Valid From.
- **Linking document:** Yes — URLs. Found in the fadmin SFTP.

## Upload & setup (Vendor)
- **Manual upload:** select files from FTP (in the folder for the corresponding date; naming convention gives page order/index; usually 3–8 pages). Select all → Auto Group → confirm indexing → Save & Complete.
- **Setup:** start the flyer-creation vendor task → pricing zone: Description **Base**, Language **English**, all pages in correct order → Save & Done. Under FSAs, select **National (Excluding Quebec)**.
- **Linking document:** download from the SFTP and **mass-attach to all vendor tasks** (no manipulation).

### Setup QC
- Dates match the PDFs and Available = 1 day before Valid. No theme. Availability everywhere (not hidden). Complete Setup QC checklist, Save & Confirm.

## ⚠️ Common errors / risk items — tagging accuracy vs the linking document
- **Tag brand exactly as shown in the linking document** (e.g. CCM; "Bauer" vs "BAUER").
- **Tag name exactly as in the linking document**, matching capitalization and punctuation. If the flyer name and spreadsheet name differ, **use the spreadsheet name** (e.g. "CCM Jetspeed FT1 Junior Hockey Skates", not "CCM JETSPEED FT1").
- **Sale story:** use "save" + the exact dollar amount from the "Save Story" column (e.g. "Save $400"). If the flyer says "Save Up To $$$", **do not** use that — always use the exact amount from the linking doc.

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**; linking doc required): draw a box over each item — **every item in the linking document must have a box.** Multiple sizes (e.g. a hockey stick) → box the top one with the image and the other sizes separately. Box PHL logos on the first and last page. Box Triangle Rewards banners. **Include** retailer logo, special weblinks; exclude coupons, packaged deals, sign-up page, social media.
- **Tag / Tag QC** (**Medium**; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. SKU N/A. Brand/name exactly per the linking doc (see risk items).
  - PHL logos tagged as **Link** → `https://www.prohockeylife.com/`.
- **Item Image QC (Flex):** if an item has no clean PDF, open its URL (via "visit"), verify the item, right-click the website image → copy image address, paste into "override image url" in fadmin, save; refresh Item Image QC and select the data-piped image. If no matching website image (verify the URL against the linksheet first) or it doesn't match the flyer, use a cutout. Grouped items (all tape, all of a brand) → website image if available, else cutout.
- **URL/Links QC (Flex):** confirm every item has a URL; cross-reference the linksheet. Confirm all PHL logos on first/last page are boxed and tagged with `https://www.prohockeylife.com/`.

## FQC / Flyer Review
- Complete FQC checklist (Flex).
- **Flyer Review type: Lite.**

---
*Source: Pro Hockey Life OneGuide (Google Doc `1BhyDdjdtV0WlVrIpW-Wtw2lSyfnhpVacW_4GETUgoDs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
