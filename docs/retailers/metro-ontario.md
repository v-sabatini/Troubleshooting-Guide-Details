# Metro Ontario — Processing Guide

> **Source:** Metro Ontario OneGuide (Google Doc `1gwpKzf-Vko1XcRlFZwfsXMshenK1zXZHuGBSWZCGtIo`), last updated Jul 14, 2026. Contacts/credentials omitted.
>
> For French tasks/pages, see the Metro Quebec OneGuide instead.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** (relationship quality: Excellent) |
| Availability | All platforms. **We don't power their hosted, but leave all toggles unchecked.** |
| Slack channels | `#metro`, `#opsmetro`, `#metro-reporting`, `#3fl-metro` |
| Hosted URL | metro.ca/en/flyer (hosted powered by TC) |
| Flyer types | **506: Ontario** (weekly) · **9290: Digital** (vendor ads — P&G, brand-specific — + standard secondary pubs) · Quebec types 5844 / 12207 handled in the QC OneGuide |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (flyer processing only); no coupons; **Strategic Ops — yes (Feedel / retailer data services)** |

> **NOTE:** For any secondary publications, flag the flyer run and dates in `#metro` tagging BD members — they use this to add budget behind the flyers.

## Files & schedule (Ontario 506)

- **Files received:** Friday.
- **Publication cadence:** Available From Wednesday; Valid From Thursday; Available To / Valid To Wednesday (EST).
- **Preview date:** Internal preview only, from Monday.
- **Weekly workflow:** Thursday — codesheet manipulations & upload (DOC); Friday — digital inserts & REV pages (upload 2); Monday — SKU QC (Flex, requires Flex ticket); Tuesday — FQC + SKU custom action (DOC); Wednesday — flyer live; Thursday — Store Manager Specials page upload/processing; Friday (+ Sat & Mon) — Store Manager Specials live check.

## Upload & setup — Standard weekly (owned by DOC)

**Codesheet manipulations.** Required assets: PDFs (standard pages + digital inserts), Digital Codes spreadsheet, the Automatic Codesheet (shows versions, stores per version, page order — inserts not included), and the Store Matrix (store locations × insert distributions).
- Client sends the Digital Codes codesheet; selected data is copy/pasted into the Automatic Codesheet.
- Metro occasionally sends a Store Matrix listing which stores get which inserts. Paste into the Automatic Codesheet ("Flyer Zones_Matrix as of…"). The `1`s under each Insert Code column must be replaced with that column's title (e.g. under `ATT_DEL`, replace each `1` with `DEL`), because those distinctions drive the automated codesheet.

**Upload.**
- **Part 1 — Codesheet:** once manipulated, download as CSV. Upload on the Codesheet tab with **Config: `metro`**, Base path = base folder up to the date only (nothing after the date, so all folders for that date are referenced). The codesheet creates pricing zones by insert and auto-creates English + French versions. Bilingual zones show as French; all others get `FR` in the name and toggle as **cross language**.
- **Part 2 — Digital inserts manual upload:** Pages tab → Edit → folder with matching date + "Digital Inserts." Select all pages **except** secondary-pub pages and pages with **"visible"** in the name (those carry Block-IDs/SKUs layered on top — not wanted). Re-upload inserts needed for bilingual PZs; set correct language toggles; Save & Complete.

**Setup.**
- Search Pages for names with "Block" — only inserts labelled "Block ID - Layered" should appear. If a regular page (e.g. 02_DM/DM2) has "Block ID," it's the wrong page (SKUs visible on top of items) and must be replaced.
- Mark Flyer Creation complete. Confirm EST dates (Avail Wed–Wed, Valid Thu–Wed) match the PDF, especially secondary pubs. Internal preview: Monday before go-live. Toggles: available everywhere. No external run name, no theme. Set vendor tasks to HIGH priority. Complete Setup QC.

## Upload & setup — Secondary publications (owned by DOC)

- Secondary-pub info is at the bottom of the codesheet email, or in the codesheet below all versions (first/second chart).
- Manual upload: select pages for that publication with **"layered"** in the PDF name (only 1 version needed); index by page number; ensure English; Save & Complete.
- Pricing zones: Zone 1 = Base (English); Zone 2 = Base CL (English + cross-language toggle — changed to French during FQC in case of REV pages).
- Setup: Avail/Valid Thu–Wed; preview Monday. External Run Name = main callout on page 1, added to **both EN & FR** fields.

## ⚠️ Common errors / risk items

- **SKUs / Block-IDs** are found in text extractions or on the BLOCKID FTP file — **not on the flyer page.**
- **Incorrect valid dates** on the red banner at the bottom of page 2 are caused by the print flyer's flap — **this is NOT an error.** If unsure, flag it.
- **Wrong image** — many similar products per page look alike but differ in name/quantity. Be careful selecting images; select the image of the **first product** in a list.

## QC specifics

### Box Draw / Box QC — **High complexity** (owned by Vendor)
- **Auto-Box Draw: OFF. Box QC bot: OFF.** No linking document.
- **Include:** coupons, packaged deals.
- **Exclude:** retailer logo, sign-up page, social media, special weblinks.
- **Box each item separately, including inside multi-item boxes**, using text boxes. If a text box would cover an item, that's fine. **Capture the whole product image in the box so text extraction works.**

### Tag / Tag QC — Low complexity (owned by Vendor)
- **Auto-tag: ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Multi-item boxes:** tag using all text in the same box — Name = bold text, Description = non-bold, Price = XL number, Pre/Postfix = small text with price. **SKU = text-extracted** (not always on the same line; e.g. `VF-09`, `FL872-03`, `P-03`, `31-018EL`). **Do NOT tag URL** (tagged automatically later).

### Image QC
- Clean PDF preferred; otherwise a cutout is fine.

## Post-processing (owned by DOC)

- **Insert process** — reference the insert-process videos; complete before marking autostack spotcheck complete.
- **SKU spotcheck / SKU QC** — Item Search for items without a SKU; SKU is an alpha-numeric code with a dash (e.g. `GM07-F01`) found in Text Extraction. If few, add manually; if many, file a Flex/FAB ticket. Then run the custom action **"Set Metro Banners Item URLs"** (Flyer Run ID + Merchant ID + ZDMP filename from SFTP `/ZPO400 + Google Feeds`; use the **CV** file for Ontario). QC via Item Search (SKU is-not-blank; URL is-blank vs is-not-blank).
- **FSA Override** — 3 FSAs are manually added. After FR/CL zones go French, rerun FSA Generation if overlapping (red). On Geography, remove all Quebec FSAs starting with **J** (e.g. J8T, J8V, J9A…) via custom action "Remove FSAs" (FSAs + Flyer Run ID; ignore Pricing Zone ID). Export FSAs, edit in Sheets (delete "Pricing Zone Name"; rename "Pricing Zone ID"→`flyer_id`, "FSA"→`fsa`), find the two flyer IDs containing **L3Y** and add rows for **L0E, L4P, L9P** to each. Download CSV, use "Assign FSAs by CSV." **If new pages are uploaded, re-run this custom action every time.**
- **Page merging** — Storefront Spotcheck one PZ per version; merge skinny pages (positions 1 & 3) to the next page, then rerun Page Tile Gen.
- **Tracking codes** — Overview → Manage Tracking Codes → Apply All Tracking Codes (set at Flyer Type level).

## Flyer review / go-live

- **Flyer Review type: Medium** (owned by DOL).
- **Ontario checks:** thumbnails Standard 4; check notes for errors/warnings; flag items without URL if >10% missing and no note; live 1d prior to valid; available everywhere; pages with 0 tagged items OK only if banner/insert; items-vs-tagged totals equal; interactivity in Item/Horizontal/Vertical preview with no cutoff in vertical scroll; codesheet green; Geography no change WoW; ensure FSAs **L0E, L9P, L4P** assigned.
- **Quebec flyer:** same as ON except live **2d** prior to valid.

---
*Source: Metro Ontario OneGuide (Google Doc `1gwpKzf-Vko1XcRlFZwfsXMshenK1zXZHuGBSWZCGtIo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
