# Metro Quebec — Processing Guide

> **Source:** Metro Quebec OneGuide (Google Doc `1ltuZePeprRCWDNW_k17hMqJVea8E_J4HQCooMC16KBw`), last updated Sep 6, 2024. Contacts/credentials omitted.
>
> If you are working on English tasks/pages, use the Metro Ontario OneGuide instead. (This guide contains both Ontario 506 and Quebec 5844 instructions.)

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** (relationship quality: Excellent) |
| Availability | All platforms. **We don't power their hosted, but leave all toggles unchecked.** |
| Slack channels | `#metro`, `#opsmetro`, `#metro-reporting`, `#3fl-metro` |
| Hosted URL | metro.ca/en/flyer (hosted powered by TC) |
| Flyer types | **506: Ontario** (weekly + standard secondary pubs) · **9290: Digital** (vendor/brand ads) · **7988: Metro Health** (ad hoc) · **5844: Quebec** (weeklies & secondary pubs) |
| Processing | Auto-stack |
| Who's involved | Flex (FAB tickets); OS (flyer processing only); no coupons; **Strategic Ops — yes (Feedel / retailer data services)** |

## ⚠️ Common errors / risk items

- **SKUs / Block-IDs** are found in text extractions or on the BLOCKID FTP file — **not on the flyer page.**
- **Incorrect valid dates** on the red banner at the bottom of page 2 come from the print flyer's flap — **NOT an error.** Flag if unsure.
- **Wrong image** — similar products per page look alike but differ in name/quantity. Select the image of the **first product** in a list.

## Quebec (5844) — files & schedule

- **Files received:** Thursday.
- **Publication cadence:** Available From Tuesday; Valid From Thursday; Available To / Valid To Wednesday (EST).
- **Preview date:** From Monday (preview links aren't sent to the client — they access via Madmin).
- **Workflow:** Wednesday — store-list codesheet & page upload (DOC); Monday — SKU QC (Flex), FQC + SKU custom action (DOC); Tuesday — revisions (DOC).

## Quebec (5844) — upload & setup (owned by DOC)

**Pre-processing / codesheet.** Required assets: Store List (by email), Tracking sheet (by SFTP).
- They send two copies of pages: normal, and ones with the SKU/Block-ID layered on top ("visible"). In SFTP search "blockid"/"block-id"; mark folders labelled "Block ID" as uploaded. This search also catches INSERT pages (dropped in a "block ID" folder) — mark all off, then Ctrl-F "layered" to unmark the insert pages you'll upload ("visible" pages show the SKU).

**Upload.**
- Search "BLOCK" pages in FTP, mark uploaded (not needed for processing — legacy).
- Download the Store Assignment sheet; double-check its versions match the Tracking Sheet (pagination doc). Import to Sheets: unhide and delete unneeded version columns (highlight the ones you need first).
- **Store ID overrides (Site Number column):** **Lachine = 5398**, **Prevost = 5427**.
- Save as CSV, then re-open to confirm no extra/duplicated columns (can create extra PZs).
- **Upload as Codesheet: Config `metro_qc_stores`, PDF Base `/`, toggle store assignment + pricing-zone-creation only.** After upload, check the Pricing Zone tab for extra store-less PZs (system sometimes creates combined zones like "NAT ECO" with no stores — delete them).
- Manually add stores **14** and **387** to the Nat & Nat CL zone store assignments.
- Find the "REV" folder (ignore Block ID). Download / match pages per the Tracking Sheet (page labels may differ slightly, e.g. `-` vs `_`, "Web_01" vs "Web1"; "venir" = French "to come" = sent later). Upload INTER pages (separate folder, labelled with valid date). Update grouping manually (FAdmin can't group these). **Change page language to French**, Save, then Save As, and re-verify all pages are French.
- In Pricing Zones, update pagination per Tracking Sheet (per-zone page differences highlighted red; INTER pages go in position 1 for noted zones).

**Setup.** EST dates: Avail Tue, Avail To Wed, Valid Thu–Wed. Toggles available everywhere; no external run name; no theme; vendor tasks HIGH priority.

## Ontario (506) — upload & setup (owned by DOC)

- **Codesheet:** manipulate the Automatic Codesheet from the client's Digital Codes sheet; download CSV; upload with **Config `metro`**, Base path = base folder up to the date only. Creates EN + FR PZs; bilingual zones show French, others get `FR` + cross-language toggle.
- **Digital inserts:** manual upload from the date + "Digital Inserts" folder; skip secondary-pub pages and "visible" pages; re-upload inserts for bilingual PZs; set language toggles; Save & Complete.
- **Setup:** mark Flyer Creation complete; EST dates Avail Thu, Avail To Wed, Valid Thu–Wed; preview Monday; toggles everywhere; no external run name/theme; vendor tasks HIGH; Setup QC.
- **Secondary pubs:** manual upload of "layered" pages (1 version), index, English, Save & Complete. Zones: Base (EN) + Base CL (EN + cross-language, → French at FQC). External Run Name = main callout on page 1 in **both EN & FR**.

## QC specifics

### Box Draw / Box QC — Low complexity (owned by Vendor)
- **Auto-Box Draw: ON. Box QC bot: ON.** Linking document required (Box Draw/Box QC specific).
- **Include:** coupons, packaged deals, retailer logo, sign-up page, special weblinks. **Exclude:** social media.
- Box each product block that includes a price; **if multiple items share the same price, group and box them as a single box.**

### Tag / Tag QC — Low complexity (owned by Vendor)
- **Auto-tag: ON.** Linking document required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Name = bold; Description = non-bold; Price = XL number; Pre/Postfix = small text with price. **SKU = text-extracted** (e.g. `VF-09`, `FL872-03`); **do NOT tag URL** (auto later). Tag coupon offers.
- **Original price:** single price → Original Price field; a **range** → Description field.

### Image QC
- Clean PDF preferred; cutout is fine otherwise.

## Post-processing (owned by DOC)

- **SKU QC** — Item Search for items without a SKU; add manually from Text Extraction or file a Flex/FAB ticket. Then run custom action **"Set Metro Banners Item URLs"** (Flyer Run ID + Merchant ID + ZDMP filename from SFTP `/ZPO400 + Google Feeds`; use the **QC** file for Quebec). QC via Item Search.
- **FSA Override** — after FR/CL zones go French, rerun FSA Generation if overlapping. On Geography, remove all Ontario FSAs starting with **K** via custom action "Remove FSAs" (FSAs + Flyer Run ID). Confirm on Geography tab.
- **Tracking codes** — Overview → Manage Tracking Codes at flyer-run level (Dynamic Variable, Hosted, utm_source) → Apply All Tracking Codes; changes per platform/clone.
- **FQC** — normal FQC checklist.

## Flyer review

- **Flyer Review type: Medium** (owned by DOL).
- **Ontario:** Avail Wed–Wed, Valid Thu–Wed; thumbnails Standard 4; flag items without URL if >30% missing; pages with 0 tagged items OK only if banner/insert; codesheet 1× green; Geography no change WoW; ensure FSAs **L0E, L9P, L4P** assigned.
- **Quebec:** as ON except Avail Tue–Wed; flag items without URL if >50% missing.
- **Digital flyer type:** external run name required (custom, EN & FR); items have no URLs; geography may be inconsistent.

---
*Source: Metro Quebec OneGuide (Google Doc `1ltuZePeprRCWDNW_k17hMqJVea8E_J4HQCooMC16KBw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
