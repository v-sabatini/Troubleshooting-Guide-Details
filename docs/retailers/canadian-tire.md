# Canadian Tire — Processing Guide

> **Source:** Canadian Tire OneGuide (Google Doc `1iuZdREyNZy9MnGw4vsDTnSFpNFtlpysLlpMW2oedD_4`), updated Apr 29, 2026. Contacts/credentials omitted.

> **Complex bilingual (EN/FR) account** with heavy codesheet manipulation, a two-drop weekly cadence (main pages, then Digital Ad inserts), and per-zone FSA/UTM custom actions.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium |
| Availability | **Flipp only** |
| Slack channels | `#canadian-tire`, `#cantire-ssd-testing`, `#ct-nativex` |
| Flyer types | Weekly Flyer (1488) · Catalogue (3436) · Grand Opening/GO (3845) |
| Processing | Auto-stack; Flex via FAB tickets; no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Tuesday (Weekly). **Weekly is a two-drop cadence:** main flyer pages ~2 weeks out; **Digital Ad inserts a week later** (Tue/Wed, ~1 week from live). Catalogue is similar. GO files arrive just within the 5-business-day window.
- **Cadence:** Available From Tuesday · Valid From Thursday · Available To Thursday · Valid To Thursday. Some weeklies run to Sunday.
- **Preview date:** set to the upcoming Tuesday (1 week before live) so OS isn't slammed doing both uploads at once.
- **Linking documents:** Header link sheet + Basebar link sheet (in the VTB Drive folder); the weekly **Digital Ad "Digital Direction" link sheet** is emailed only (not in SFTP).
- **Historical note:** data piping is **defunct** (confirmed Mar 7, 2025 — consistently errors out).

## Upload & setup (owned by DOC)

### Weekly / Catalogue — main pages (codesheet)
Two codesheets: **BIL** (bilingual) and **ENG**. **Do the BIL codesheet first.** Files are read-only — switch to edit mode.
- **Update Date:** set cell B2 to the Available From date. Temporarily set the run's Available From & Valid From to Tuesday and Available To & Valid To to Friday (so the staggered Sale Dates all validate), then revert after.
- **RL Codes:** delete "-BIL" from all zone names (Find & Replace) so they match FAdmin store sets. Move any Sub-Zone text into the RL Codes column.
- **Delete "é" from "Québec"** everywhere (usually B72, B76) — otherwise an **"Invalid byte sequence"** error.
- **Delete pages listed but not in SFTP** (typically 200-series 201–204 and 80-series 81–82 — these come in the second drop).
- **Delete extra text in 70-series page names** (remove "pop "); cells should read only "pg. " + number.
- **Delete pages with a different SFTP base path** (multiple events in one codesheet); upload those manually and place via Pages > Layout.
- **Check for `_REV` pages:** search SFTP "rev"; add "_Rev" to those page names in the codesheet.
- **Upload:** save as CSV → Codesheet tab. Name = `BIL`; **Config = `canadian_tire`**; PDF base directory from SFTP (BIL and ENG base paths differ!); **toggles: all except 2nd (Region Assignment) and last (Combine Zones).** Save & run.
  - **Do NOT process the ENG codesheet until all BIL sessions finish** — back-to-back uploads cause race conditions and errors.
- BIL codesheet makes one English + one French version of each zone; ENG makes one version each.
- After both: manually upload any deleted 100-series pages (upload ENG + BIL, then BIL again set to FR); mark Flyer Creation Complete; insert 100-series pages into zones via Pages > Layout per file names.

### Weekly / Catalogue — Digital Ad inserts (second drop)
- Manually upload all DB + DE pages from the Digital Ads folder, then upload DB pages again set to **French**. Mark Flyer Creation complete.
- **Digital Direction link sheet:** hide rows where Asset Type is "Print"/"FC"/"Print P#" (already-uploaded pages), save, mass-attach to all new vendor tasks. Update Preview Date to the following Monday.

### Grand Opening (GO)
- Manual upload, **no codesheet** — use the schedule from the GO contact. One flyer run per date range; each TC Code = its own folder = its own pricing zone. **Upload GB25 files twice (EN + FR).** Assign page groupings from file names (P01…). Create zones per Schedule; add stores from the GO Store # / Part Store # columns.

### Setup QC (all types)
- **Remove Stores in Multiple PZs:** WAWA, CASSELMAN, SHEDIAC get both English-only and English-bilingual assignments — remove them from the English-Bilingual zones (Overview > Manage Stores).
- Confirm dates on page 1 (watch wrong-Sunday end dates → fix in Staggered Dates); revert Available/Valid dates to originals; set Preview Date to upcoming Tuesday.
- Mass-attach Header + Basebar link sheets to all vendor tasks (attach to Flyer Creation task to cover all tracks). Thumbnails Standard 4.

## ⚠️ Common errors / troubleshooting
- **"Invalid byte sequence"** → an "é" (almost always "Québec", cells B72 & B76). The error flags only the first instance — fix both.
- **"Valid dates" error** → extend the run's valid dates, rerun the codesheet, then revert.
- **"File not found"** → the codesheet processor may dislike multiple Event Names in B2 (and in Format B4 / Page Position B12); delete "/D###" from B2 and clear B4/B12, rerun. File names draw from Plant Code + row-15 page numbers + version text — check those for typos. Last resort: remove the offending page column, run, upload those pages manually, place via Page Layout.
- **BIL vs ENG base paths differ** — grab the correct one.
- **Never upload ENG codesheet before BIL sessions complete** (race conditions).

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- Linking document required (box-specific). **Include:** special weblinks. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Box Headers/Footers listed in the linking docs; box anything saying **"Triangle"** or with a **"Learn More"** callout. Box all items with prices (text boxes when needed); don't overlap adjacent boxes; box black-bolded sub-items separately.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking document required (tag-specific). **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Use text extraction** to minimize spelling errors (careful with numbers); **French flyers must use correct accents (é, è, ê…).**
- **Name:** no ©/™ symbols; capitalize the first letter of the brand (e.g. "simoniz" → "Simoniz"); if the name isn't on the PDF, search the SKU on the CT website.
- **SKU:** enter in BOTH the Description and the SKU field, exactly as printed. **Original Price:** if a range, enter the LOWER number only.
- **URLs:** search the SKU on canadiantire.ca (EN `/en/`, FR `/fr/`) and tag the product URL. **If a SKU ends in X, search WITHOUT the X.** If two SKUs have Xs, only do the first. **All Tires items (no SKU)** get the fixed tires-category URL (EN/FR). Otherwise use the linking document.

### Image QC
- Choose a clean PDF where possible; cutout if none.

## Post-processing / Pre-FQC (owned by DOC; Links/SKU QC can go to Flex via FAB ticket)

- **Insert Digital Ads into zones first** (long sessions run in background). Use the **Insert Breakdown** sheet (duplicate Template tab, match page count, map from the Digital Direction column B). Add **DB inserts to French zones first**, submit, let sessions finish; then **DB inserts to English-Bilingual zones** (carefully add the `DB03##` inserts to DB/English-bilingual zones — both DB and DE appear under the English toggle); then **DE inserts to English-only zones** (0- vs 1- zones; `0(Ex…)` = all 0-zones except those named, where "Mar" = Maritime provinces NS/NB/PEI/Nfld; `0_x_x…` = only 0-zones sharing that name element; never select `1_NWTRky`). Confirm all zones have equal page counts.
- **Direct Links QC:** review each page in the Digital Direction sheet has the correct link (links are often sibling-grouped; grab from URL ENG vs URL FRE column).
- **SKU QC:** Item Search → SKU IS blank, Item Type Item → fill SKU from PDF (skip Tires).
- **Links QC:** Item Search → URL IS blank. Multi-Edit all Tires with the fixed tires URL (EN then FR), then search remaining SKUs on canadiantire.ca (drop trailing X; skip flowers/plants — not posted online).
- **Categories:** none on page 1 (no longer required as of 07/25). **Mark items in store only** (only after Links QC — it blocks saving new links). Thumbnails Standard 4 (add NativeX thumbnail if a NativeX campaign runs).
- **Manage Tracking Codes (Weekly only):** add Flyer Run Tracking Code — Dynamic Variable, Source All, `utm_campaign`, value `2026_03XX-Weekly-Flyer` (change 3XX by week) → Apply All.
- Expect and review **PZs have Staggered Dates** error (verify dates vs page 1). Add revised pages as they arrive.
- **Assign FSAs from .csv custom action:** copy the `1_NwtRky` pricing-zone ID into the CT FSAs sheet, download CSV, FAdmin > System > Custom Actions > "Assign FSAs from .csv", enter the **flyer run ID** (not the PZ ID), upload, run.

### GO Pre-FQC specifics
- Follow the GO contact's email on ecomm links: if links should NOT be added, export items, remove all URLs, re-import; if approved, QC per above. Complete SKU QC; no categories on page 1; mark in-store only (after Links QC); thumbnails Standard 4; add revised pages; verify dates/stores vs Print Schedule.

## FQC / go-live
- Complete Final QC Checklist. Expected ignorable errors: items not QC'd (spot-checked items → "Ignore"); pricing zones without stores (redundant English-Bilingual zones → "Ignore"); Categories without an Image.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page revisions are standard**, but **re-run the "Assign FSAs via .csv" custom action after every revision** (FSAs reset). Use OPTICS tickets as needed.

---
*Source: Canadian Tire OneGuide (Google Doc `1iuZdREyNZy9MnGw4vsDTnSFpNFtlpysLlpMW2oedD_4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
