# RONA & RONA+ — Processing Guide

> **Source:** RONA & RONA+ OneGuide (Google Doc `1McuMALzI19IKJ1GhUd0FVI0j6AABQnQN2a-NXXAthTw`), updated Jul 14, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (Catalog: Hosted only) |
| Slack channels | `#lowes_rona`, `#lowes-rona-ops` |
| Hosted URL | http://www.rona.ca/en/flyer |
| Flyer types | #83 Weekly Flyer · #2507 Catalog · #9669 Pro Flyer (paused) · #5061 Local Flyer (paused) |
| Processing | **Trim Stick**; Flex via FAB tickets; no coupons; no Feedel/retailer data services; OS N/A |

## Files & schedule

- **Weekly files received:** Wednesday (typically 2 weeks' lead time). Catalog: ad hoc.
- **Available From:** Wednesday · **Valid From:** Thursday · **Available To:** Wednesday · **Valid To:** Wednesday.
- **Linking document:** Yes (Web Links document; provides EN/FR product URLs).
- **Custom action — Set Cutout Images:** deselects cutouts/PDFs when a data-piped image exists, else prioritizes PDFs over cutouts. Run pre-FQC after data piping reaches >90%.
- **Workflow (ideal):** Upload & Setup (DOC, 14 days) → Pre-FQC (DOC, 10 days) → Category QC (FLEX if high volume) → FQC (DOC, 1–2 days) → Corrections (DOC, post-live). Can compress to ~5 days.

## Upload & setup (owned by DOC)

- Retrieve Store List from email; open previous week's codesheet Google Sheet and make a copy; delete all content except row 1.
- From the downloaded codesheet: delete 'price zone' column if present; filter header row and de-select non-RONA stores; paste values only into the sheet; copy zoning info from the tab name into 'base'; repeat for all zones.
- Upload codesheet: **Config name `rona`**, base path from FTP, **all toggles on except the 2nd and last**, save and process.
- **Store-not-found errors are normally leading zeros** — confirm the stores exist and remove the 0s from the codesheet.
- On the PZ tab an FR counterpart is created for each EN zone — **cross-language all to FR**.
- **M2 zone:** they drop true EN and FR files not captured by the codesheet — go to pages → edit pages → search `fr_m2` and upload all in French, then manually swap FR M2 pages into the FR M2 zone.
- Linking doc from email: **double-click any image and compress all** before uploading; mass-attach to all tasks via the 'flyer creation' task.
- Leg heights preset 50/40; standard 4 thumbnails + 'thumbnail' (reflects on hosted); no theme unless specified.
- **RONA+ integration weeks** (naming prevents a standard codesheet): do the standard upload, then pages → edit → locate the comb folder and upload all RONA+ pages; manually create RONA+ zones (with cross-languaged FR counterparts); assign stores manually or via a generic stores codesheet.

### Setup QC
- No overlapping stores/FSAs warnings; leg heights & thumbnails complete; linking doc uploaded to all tasks; dates correct; no cut-off/overlapping pages; geography good; sessions run. The 'unused PDFs' callout = the complete unsplit PDFs — mark off in FTP. Confirm vendor tasks marked 'available'.

## ⚠️ Common errors / risk items (retailer-specific)

- **Multiple products per ad cell:** if multiple items (and SKUs) share an ad cell, **box and tag each product separately** (e.g. labelled "A"/"B") unless the Web Links doc says otherwise.
- **Product linking — never tag a search URL.** Click into the product on rona.ca and extract the direct product-page link. If rona.ca is down for maintenance, wait and process when it's back up.
- **"X% savings on all other products":** box the "ALL other" sale as a separate item.
- **Packaged deals** (appliance pages): separate box per item in the package (washers/dryers each get their own price — not boxed as one unit).
- **Reversed-number risk (FQC):** search Sale Story / Pre Price Text containing 'for' and 'pour' — historically a 2020 CuSat issue where numbers were reversed (3 for $20 vs 20 for $3) and stores had to honour incorrect pricing.

## QC specifics

### Box Draw (HIGH complexity; Auto-Box OFF, Box QC bot OFF)
- Requires Box Draw/Box QC-specific linking document.
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box any banner associated with a website; check the Web Links doc for which items/banners get special links.

### Tag / Tag QC (HIGH complexity; Auto-tag OFF)
- Requires Tag/QC-specific linking document.
- Add **BRAND** in both the brand field and the name field.
- Add **SKU** in both the SKU field and the description; only tag the **first part** of the SKU in the SKU field.
- **Sale story** callouts: e.g. "1/2 PRICE", "2 FOR 1", "SAVE $50, SPECIAL PRICE", "EVERYDAY LOW PRICE", "SAVE $100, NEW LOWER PRICE!".

### Image QC
- **No traditional Item Image QC** — RONA is data-piped and uses the 'Set Cutout Images' custom action.
- Priority: data-piped image → cleanest PDF → cleanest cutout.

### Category QC
- May be offloaded to FLEX (FAB ticket) if high volume. Item search checks: Categories contains **plumbing** (should be none — recategorize to kitchen/bathroom/etc.); **hardware** (should be none); **smart home** (some OK — verify); **farm supplies** (should be none — recategorize soil/paint/storage).

## FQC / go-live notes (owned by DOC)
- All vendor tasks done; all pages sliced (slice validation grayed out); outstanding spotchecks complete.
- Category / link-item search: set 'direct links' category for link-type items; ensure all categories consistent.
- Page categories: none on page 1s or disclaimer page; consistent across groupings.
- Pricing Zones: all PZs same # of pages (check for duplicates if not).
- Data piping: generate groups, data pipe all to 90%+, then run Set Cutout Images.
- Geography via codesheet; flyer sorting reverse chronological, priority Weekly > PRO > Local > Catalog.
- **Tracking/UTM codes:** check the BD Promotion Calendar (column N, #days in promotion — "not promoted" = no codes); copy last week's codes and change the week number (e.g. `3725` = Week 37, 2025).

### Catalog (ad hoc)
- Manual upload; create EN and FR zones, assign all stores unless specified; hide in Flipp & distro (hosted only); mark off 'Secondary Publication?'. Processing then same as weekly. Flyer Review type: **Complex**.

## Flyer Review / out-of-processing
- **Weekly Flyer Review type: Simple** (owned by DOL). Catalog: Complex.
- **Weekly post-live corrections:** shared spreadsheet for both banners. Use column C (store) to find the Pricing Zone via Manage Stores; use Item Search (SKU contains, column E) or Pages interface (RONA page naming: Front = Page 1, Back = Page 2, Page 2 = Page 3; column D). Apply EN and FR URL revisions to the respective pages. Then reapply tracking codes and 'republish' under Special Actions.

---
*Source: RONA & RONA+ OneGuide (Google Doc `1McuMALzI19IKJ1GhUd0FVI0j6AABQnQN2a-NXXAthTw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
