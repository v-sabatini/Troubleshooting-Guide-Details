# Lowes Food — Processing Guide

> **Source:** Lowes Food OneGuide (Google Doc `1K33m8W9GJZVYyLEDGhSZbUgbK4uvgCpfwiJJEqj_SMQ`), updated May 5, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#Lowesfood` |
| Publication | Weekly (Flyer Type 1) |
| Processing | Auto Stack; Flex (Flyer Review); **OS completes coupon processing**; no Feedel |

## Files & schedule

- **Files received:** Monday. Inserts sent Monday/Tuesday; a SKU/coupon document may be provided for coupon tagging.
- **Cadence:** Available/Valid From Wednesday, Available/Valid To Wednesday.
- **Processing type:** Auto Stack.

## Upload & setup (owned by Flex)

- Manual upload: Flyer Run → Pages → Edit; download the pages for the corresponding week (e.g. Week `121725`).
- **Pricing zone setup:** use the **`LowesFoods_GRID-StoreCopies_(date).xlsx`** file as source of truth — PZ names are in the **"Version"** column; the GRID file also defines page order and store allocation.
- Check dates; no theme; **external run name "Weekly Ad"**; Standard 4 thumbnails.

### ⚠️ Common errors / risk items
- **Coupon ID spreadsheet:** check the SFTP. If present, attach it to Vendor Tasks; if not, leave a comment "no coupon file available".
- **Secondary publications:** before marking files complete, check whether there's **more than one GRID XLS** in the SFTP (indicates a secondary publication).
- Watch for multiple products in one callout.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include coupons**; exclude packaged deals, retailer logo, sign-up page, social media, special weblinks. Every item with a pricing callout is boxed individually (not every item has its own image, but all must be boxed); avoid text boxes unless necessary. Box the coupon graphic.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON):** linking doc (Tag/QC specific). Include name, SKU, price, sale story, categories, disclaimer, original price. **Exclude pre/postfix, valid dates, description, URLs.**
  - **Coupons:** if a Coupon ID spreadsheet is available, ensure the **Coupon ID is entered in both the SKU and Coupon ID fields**. If no spreadsheet, proceed without IDs.
- Spotchecks: standard.

## Post-processing & FQC

- **Item Category QC (DOC):** add both Analytical and Google categories (except inserts).
- **Item Image QC (DOC):** clean white-background PDF if available, else cutout.
- **Digital inserts:** ~1pm every Tuesday, Lowes Food drops inserts to the SFTP and links to the processor's email. Check the link for the number of inserts, position, and impacted PZs — **do NOT complete FQC before inserts are added.** Read the "Position on Flyer" column: e.g. `After Page 2A_, 2_287, 2_289, 2_285` → insert into base, 287, 289, 285 (A = BASE zone). Manual upload; when tagged, inserts are a Link (add the emailed link).
- **Coupon ID tagging:** a `Coupon_Tagging_Template_Flipp` file may arrive after processing. For each item, search the name in Item Search (FAdmin) and enter the **Coupon ID into both the Coupon ID and SKU fields**, matching the file exactly. May be done manually by DOC or via an ARB ticket for Flex.
- **FQC (Flex):** Standard 4 thumbnails; dates vs PDF; external run name "Weekly Ad"; complete FQC checklist.
- **Flyer Review type: Lite** (owned by Flex).
- **Out-of-processing:** check flyer sorting so all weekly publications appear first.

---
*Source: Lowes Food OneGuide (Google Doc `1K33m8W9GJZVYyLEDGhSZbUgbK4uvgCpfwiJJEqj_SMQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
