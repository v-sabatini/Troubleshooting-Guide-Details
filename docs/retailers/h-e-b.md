# H-E-B — Processing Guide

> **Source:** H-E-B OneGuide (Google Doc `1DQuZWM8aatVpLrz7_LFAlKz2pX4G3ziySzDR_AYuQ84`), updated Jul 6, 2026. Contacts/credentials omitted.

Two-city account: **Houston (HFD)** and **San Antonio (SAFD)** processed as separate zone sets in one run, plus a weekly Houston digital insert.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | (not specified) |
| Flyer type(s) & cadence | Weekly + Monthly |
| Processing | Auto-stack; Flyer Review (Medium); OS setup; no coupons; **Feedel/Strategic Ops: YES** |

## Files & schedule

- **Files arrive:** Monday. Available From **Monday @ 1:00 AM** / Valid Tuesday. 1-day preview.
- **In FTP** (search "xls"): files with **"Recap"** = page codesheet; **"WeeklyAdInfo"** = linking doc. Ad Zone charts held in a shared Drive folder.

## Upload & setup (owned by Vendor)

**Process Houston stores + pages FIRST** (makes it easier to add the Digital Insert during FQC; keeps PZs distinguishable — Houston PZs are numbered **60–85**, San Antonio outside 60–85).

**Pages codesheet manipulation:**
- **Houston:** delete Column E ("Digital Resize" / "Column 4") entirely, save as CSV (fadmin treats it as already-uploaded; re-added later — this is the HEB app insert, required weekly in Houston).
- **San Antonio:** delete any "N/A" cell text (leave blank, don't shift up), save as CSV.

**Codesheet uploads (base dir `/`):**
- Houston/San Antonio **stores:** config **`heb_stores`**, toggles **1,4,5,6** checked (NOT 2,3,7).
- Houston/San Antonio **pages:** config **`heb_original`**, toggles **1,3,4,5,6** checked (NOT 2,7).

**Setup:** download "WeeklyAdInfo" per city, upload via Vendor tab "Upload mass attachments" (Houston + San Antonio). Rerun sessions. Leave "HEB app - Digital Resize.pdf" stale until FQC (Friday PM). Geography: no stores added/removed. LH 40/30; standard 4 thumbnails; available 1am Eastern day before; 1-day preview.

### ⚠️ Common errors / risk items

- **PZ tab (RISK):** confirm all Houston zones (60–85) sit at the top after upload.
- **New versioning (ad zone) list:** always use the most up-to-date; Houston — delete both sister-banner sections (Mi Tienda + Joe V's); San Antonio — delete Blush Pink/blue/green "Subtitle" cells (keep darker pink Ad Zone), Ctrl+F "EFC" and delete EFC store numbers; save as CSV.
- **Promo IDs are zone-specific** — be careful when tagging.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required):** **include** coupons, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. Box every item with a unique item ID; box all coupons; **red italic text = box separately.**
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - Multi-item brands/names separated with **"OR"**; red text before names NOT tagged; BOGO — the product to purchase goes in Name.
  - **Custom fields — Promo ID & Unique Promo ID:** every item on every page has both. Filter the pipeline spreadsheet by AD ZONE (the number after "z" in the page description, e.g. `H0718p01z50` → zone 50; pages with "x" appear across multiple zones — use the first match), then by page, find the item by description, tag Promo ID (Column B) and Unique Promo ID (Column E).
  - **Override Image URL:** for two-line items sharing an ad block with another product, use the arbitrary-files image link in Override Image URL.
- **Image QC:** **only ad blocks with 1 image get a PDF image.** Multi-image / BOGO deals → "Do Not Use PDF Images" (select the cutout). Meal deals can stay cutouts.

## Post-processing / FQC (owned by DOC)

- **File a FAB ticket** (clone the sample) for FLEX to complete Image QC, Coupon ID QC, and Spotchecks.
- **Promo ID QC:** Item Search → Promo ID IS blank → fill from the linking doc for the correct zone (Houston "H" / San Antonio "SA"); zone-specific.
- **Item Image QC:** filter cutouts/no images; pick clean PDFs but beware sale-story mismatch (e.g. BOGO PDF shows only one product). Text-only promos → Override Image URL.
- **Houston Digital Insert:** upload the held page, group as last page, **Process Internally**; add to Houston zones 60–86 (no box draw, static page); mark box draw complete; place in last page position via Pages > Layout; note "HEB insert added" in comments; no page category on the insert.
- **Categories:** 2 categories per page except page 1.
- **Flyer Review type: Medium.**

---
*Source: H-E-B OneGuide (Google Doc `1DQuZWM8aatVpLrz7_LFAlKz2pX4G3ziySzDR_AYuQ84`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
