# Real Canadian Superstore (RCSS & RWSS) — Processing Guide

> **Source:** Real Canadian Superstore OneGuide (Google Doc `1WAobo1UGXs53xa8x6C9DJpkpVeCm5npBQLwUsPVtq1o`), updated Mar 5, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+; Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl`, `#3fl-loblaws` |
| Hosted URL | realcanadiansuperstore.ca |
| Flyer types | 2 weekly flyers — **RCSS** (Ontario) and **RWSS** (West Coast); ad-hoc Catalogue/Seasonal |
| Processing | Auto-stack; Flex (3FL); **Yes — Feedel/retailer data services**; no coupons |

## Files & schedule
- **Files received:** Thursday or Friday. **Internal preview:** Sundays.
- Available From Wed; Valid From Thu; Available/Valid To Wed.
- **RCSS Valid From 12:00 AM; RWSS Valid From 3:00 AM** (West Coast time difference — always set RWSS to 3:00 AM, never change RCSS).
- Linking document optional (links provided in codesheet, can be attached to task).

## Historical context
- **Dec 1, 2025:** stopped submitting Table of Contents pages (low clicks vs. effort).
- **Jan 19, 2026:** publish in English and French with Cross-Language zones (retailer request).

## Upload & setup

### Pre-setup — codesheet generation (owned by DOC)
- COC/COL drop the Final Codes in the shared LCL Codesheet Drive before the upload shift. You receive **separate emails for RCSS and RWSS**; upload each to its folder (RCSS ONT / RCSS WEST). Move old week's codesheet to Old Files. Always use the most recent revision before Friday's upload shift.
- Generate the **Generic Codesheet** via the Loblaws Codesheet Automations Colab notebook: run the **SFTP List Tool** (enter base path matching the codesheet, e.g. `/RWSS/WK23_RWSS_2026`), then **1. Match Files** (produces a Translation Key), verify File Codes/File Names (**check one version of every unique page; watch complicated flap names like "FLAP 1D M" and 10K-zone page matches**), then **2. Generate Generic Codesheet**. Upload to the correct folder and update the 3FL LCL Processing Tracker.

### Setup (owned by Vendor)
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded** (Edit Details > Show/hide rarely-used fields > Height > 4096.0 > OK). If pages already added, flag to FT Ops and continue.
- **Codesheet upload:** use the **generic** config name; base path from SFTP (grab the ON, WEST, or ATL folder matching your upload); **select all toggles but the second and last**.
  - **⚠️ Errors:** if the only warnings are "The following files matched multiple files on the FTP", hit **Force Processing**. If there are **store-missing** errors, flag to the FT processor in `#3fl-loblaws` (likely a new store / store-code change), then rerun.
- Mark Flyer Creation complete. Geography tab: select RCSS or RWSS and confirm "No Stores or FSAs/zips were added or removed!"; flag discrepancies in `#3fl-loblaws`.
- **If the codesheet fails, revert to manual upload** (build each PZ per codesheet tab; assign stores via generic_store config, first toggle only, `/` base path).

### Setup QC
- Edit Details: Preview Start = Sunday before Available From; Available Wed, Valid Thu; **RWSS Valid From 3:00 AM, RCSS 12:00 AM**; Available/Valid To the following Wed; No Theme; External Run Name = "Weekly Flyer - Valid Thursday, MM DD - Wednesday, MM DD" (**matches VALID dates, not available**). Mark Autostack Spotcheck complete.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** **include** coupons, packaged deals, sign-up pages, special weblinks; **exclude** retailer logo, social media. Box each unique price; group offers get their own box; all extra Optimum offers boxed; **HOTM (Hit of the Month) flap — box each item separately**; all Joe Fresh callouts as one box; PC Financial and PC Express Delivery pages boxed. Box any interactive "click here" button; the CON FLAP page = one box on the full page with the PC Optimum load link.
- **Tag / Tag QC (Medium; Auto-tag ON):** include Name, Pre/Postfix, Valid Dates, Description, SKU, Price, Sale Story, Categories, Disclaimer, Original Price, URLs; Brand is Box Draw/Box QC specific. **Article Number** custom fields.
  - **Name MUST be ALL CAPS, bold; product size after name with a comma.** Do NOT include in name: metric prices (e.g. "6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties".
  - **SKU** starts with "2"; ignore SKUs not starting with 2; keep unit-of-measure suffix (e.g. `_KG`). Drop leading zeros.
  - **URL:** after entering SKU, click **Fetch**. If link goes to a wrong item/size, remove and search product name on the site; if it leads to the homepage, leave it; if correct item but different flavour, leave it. **All items with a SKU must have a URL.**
  - **Article Number** fields at the bottom of the tag interface: paste the product SKU (incl. unit of measure); Article Number 1 = SKU/Fetch URL value; multiple SKUs → Article Number 1/2/3/4 in order.
  - **Sale Story:** all dollar-off and Optimum offers tagged; PC-symbol offers tagged "PC Optimum"; "when you purchase" → "Get ### pts when you purchase"; BOGO tagged.
  - **Valid Dates:** include date overrides only when the applicable sale story indicates the promotion; all coupons must have valid dates.
  - **Joe Fresh banners:** box and tag as a LINK with the Joe Fresh campaign URL.
- **Image QC:** clean PDF where possible, else cutout.

## Post-processing (owned by Vendor, then DOC)
- **URL/Links QC:** reference the Final Codes for pages with links (Notes/URL's column E); box the linked area (often the header, or a "Click Here / Shop Now" button).
- **Thumbnail QC:** Standard 4, starting on the first page the logo appears (not always page 1).
- **Merge Flaps:** in Pricing Zones storefront spotcheck, merge all skinny pages (mostly "FLAP" pages).
- **Article Number/SKU check:** Item Search Article Number 1 IS [BLANK] and SKU IS [BLANK] — add any missing ones seen on the PDF (Fetch to populate URL). RWSS especially has many items printed without article numbers/SKUs — the goal isn't zero results, just that shown items weren't tagged wrong.
- **Pre-FQC (DOC):** mark Autostack Spotcheck complete; leg heights auto (45/25); thumbnails Standard 4 (start at logo); Image QC not needed (PDFs auto-selected/reviewed in tagging); check items QC'd + spotcheck URLs; storefront spotcheck flaps merged; geography same WOW (flag missing stores to the Loblaws contact who sent the codesheet).
- **Flyer sorting:** Flyer Type Newest First — Upcoming, Current, then secondary pubs newest→oldest. Watch `#flyer-sorting-alerts`.

## Flyer review
- **Type: Lite.**

## Live-dates flags
- URL leads to a different item → **Flag.** Item quantities in the description → **Flag.**

## Out-of-processing
- **Article # revisions** (see Article Number Report SOPs).
- **Page swap:** standard process; for a Flap page, re-merge the revised page in the storefront spotcheck. Page-stitching issues can occur (visible page doesn't match overlaid items) — **always rerun Page Tile Generation after a swap's sessions kick off**; if issues persist rerun/mark complete Vendor Box Tag onwards; confirm across all pricing zones.

---
*Source: Real Canadian Superstore OneGuide (Google Doc `1WAobo1UGXs53xa8x6C9DJpkpVeCm5npBQLwUsPVtq1o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
