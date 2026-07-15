# VALU-MART — Processing Guide

> **Source:** VALU-MART OneGuide (Google Doc `1UZsT5i7Hdn5sdtCceYdtf05XVpPnwcy7-m8W-ubzym0`), updated Feb 9, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer types | Weekly; Monthly |
| Processing | **Trim Stack**; Flex (Processing Support); no coupons; **Yes — Feedel / Strategic Ops (retailer data services)** |

This is a Loblaws/LCL banner. Upload is normally completed by FTEs; full-time processors must place the codesheet into the tracker for the FTE to complete.

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday (1-day Sunday preview referenced in setup).
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → FQC (1 day out, DOC).

## Upload & setup

**Processor step (adds codesheet for FTE):** Find the final "wk # Maxi" codesheet in email and download it; add it to the Maxi folder in the Codesheet Drop Box drive; in the Flex LCL tracker toggle off F25 (codesheet dropped) and, once files arrive, E25 (files in SFTP).

**FTE upload:**
1. **NEW 2026 — Set Pixel Height to 4096 *before* any pages are uploaded.** Open flyer run → Edit Details → show rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were already added before this step, flag to the Full-Time Ops stakeholder and continue.
2. Retrieve **both** xls files for the week from the Valu-mart Codesheet Drop Box; the week number must match the flyer number in the tracker.
3. Use only specific tabs: **VM ICM CODE FINAL → "VM online" tab only**; **VM S CODE FINAL → "VM S Online" tab only**. Do **not** use any other tabs.
4. Manual upload: Pages → Edit → under "select files from FTP" expand the correct week folder → check the folder box to select all pages → Select Files. **Set the language toggle to French** for all Valu-mart pages. Save; re-check that toggles did not revert to English (re-apply French and repeat if they did), then Save & Confirm.
5. Flyer Creation → create **4 pricing zones** from the codesheets:
   - VM S (VM S tab, French language)
   - VM S (VM S tab, cross-language English pages)
   - VM (VM tab, French language)
   - VM (VM tab, cross-language English pages)
   - Add pages in the order of the codesheet "file codes" column.
6. Assign stores from store sets: **VM zones → VM store set; VMS zones → VMS store set.**
7. Edit Details: set **Preview start date = the Sunday before the available date**; **External Run Name = "Weekly Flyer Valid Thursday, [date] – Wednesday, [date]"**.
8. Geography shouldn't change — if it does, flag it in the 3FL Loblaws channel. Complete Setup QC (check in item view, ensure dates correct).

### ⚠️ Common errors (retailer-specific)

- **Pixel height must be 4096 before pages are uploaded** — doing it after requires flagging Full-Time Ops.
- **Wrong codesheet tabs:** only VM online / VM S Online tabs may be used.
- **Language reverts to English:** French toggle can revert after saving — re-verify before Save & Confirm.
- **Revised codesheets:** always check email for a revised codesheet after upload; if one exists, use it over the final.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Include retailer logo, sign-up page, social media, special weblinks. Exclude coupons, packaged deals. Draw a box only around the item (with its unique price / multi-item), not surrounding space. **Do not box PC Optimum promos or the retailer logo** (in the exclude examples).

**Tag / Tag QC (Low; Auto-tag OFF):** Include everything — name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand = Box Draw/Box QC specific.
- **Name:** ALL CAPS, format "Brand Product Name, Quantity" (always a comma before the quantity, e.g. "60g", "1 lb", "pkg of 24"); product name is the bold text. Bilingual pages: **only the French name in Name**, English in Description.
- **Description:** flyer info only (never from website); metrics like "6.59/kg", "Product of…", "No 1 Grade", "Frozen", "Selected varieties". No SKU in description.
- **SKU:** from text extraction (not visible on page), starts with "2"; drop leading zeros before the article number; keep unit suffix like `_KG`/`_EA` in both SKU and article-number fields; if multiple SKUs, enter only the first (before the comma).
- **URL:** every item with a SKU must have a URL — click **FETCH** to auto-generate.
- **Article Number:** same values as the SKUs, entered in the order shown; if more than 4 SKUs, enter only the first 4.

**Image QC:** correct = white background, no grey/shadow; incorrect = non-white background.

**Spotchecks:** standard pricing; reference Tag/Tag QC instructions.

## FQC / go-live

- **Pagination & store QC (DOC):** use the revised codesheet if one arrived post-upload; check pagination for each PZ and confirm assigned store #s match the codesheet.
- **URL/SKU/Article # QC (DOC):** item search "SKU IS NOT blank AND URL IS blank" → open item, Fetch. Then "Article Number 1 IS blank AND URL IS NOT blank" → add article number (also in SKU and part of URL).
- **Ad-hoc QC (Flex):** dates Available Wed→Wed (1-day preview), Valid Thu→Wed; External Run Name "Weekly Flyer Valid Thursday, [date] – Wednesday, [date]"; no theme; 4 standard thumbnails; check vertical & horizontal scroll (items clickable in full-screen preview); Link QC (any links in the codesheet must be on the flyer page); check SFTP for revised files and swap in rev pages before go-live.
- **Final QC (DOC):** after the checklist, on the flyer sorting page ensure the newest weekly flyer shows first.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** standard page swap.

---
*Source: VALU-MART OneGuide (Google Doc `1UZsT5i7Hdn5sdtCceYdtf05XVpPnwcy7-m8W-ubzym0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
