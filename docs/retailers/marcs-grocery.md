# Marc's Grocery — Processing Guide

> **Source:** Marc's Grocery OneGuide (Google Doc `1ur8X7iuStH_mKFPWGGoSB-fYzu5rLnSPxwdNFMTNrZA`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | marcs.com |
| Flyer types | Weekly (merchant #3101/3199); Distribution Category: Grocery |
| Processing | Auto-stack; Strategic Ops **yes** (Feedel); OS setup; Flex flyer review |

## Files & schedule

- **Files received:** via FTP ~two weeks before the flyer run; files marked by the **valid date** of the publication (e.g. `06142017 Flipp`). Live 12 AM Tuesdays; preview date Thursday before live.
- **Linking document:** **Yes** — `Inmar.pdf` and `PageLayout:Inmar.pdf` in the FTP, uploaded per week. Attach each as a mass attachment to all vendor tasks (if `PageLayout:Inmar.pdf` is missing, use `Inmar.pdf`).

## Upload & setup (owned by Vendor)

- **Internal name:** Valid Date (Preview Date); external "Weekly Ad"; Distribution Category **Grocery**.
- **Manual upload** from the corresponding dated folder. M5 pages may be in a separate folder; additional pages should all be uploaded. Page pagination comes from `PageLayout_Inmar.pdf`. Additional pages should match the page index/order they're placed in.
- **Pricing zones:** 5 standard — **M1, M2, M3, M4, M5**. (M6 is used for **NEW STORES only** — get store details from the lead.) Create each manually and assign pages by file name; some pages serve multiple zones (e.g. `P3 M1234` = page 3 for M1–M4). Assign stores via the preset store sets.

### ⚠️ Common errors (retailer-specific)

- **Box every individual item separately** — if multiple items share one box, box each one.
- **Brand on every item** — put the brand in both the name field (before the product name) and the brand field. Every item should have a brand (product or logo).
- **Image selection** — select the correct PDF only when clean/transparent; use the cutout when no clean PDF; **no PDF images for text-line items** (use cutout). For grouped items select the PDF of one item; don't use a single image to represent a group.
- **Coca-Cola products** — verify brand, name, and description are tagged correctly.
- **Coupon ID tagging** — see below; a recurring risk item.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** Linking doc required. Include retailer logo, sign-up page (WIC), social media, special weblinks, store locator, payment policy, digital coupon program, party-tray/gift-card creatives; **exclude coupons.** Boxes must **not overlap**; items with their own description boxed individually; multiple line items boxed each separately.
- **Tag / Tag QC (High; Auto-tag OFF; PDF image auto-selection ON).** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs; **exclude SKU.**
  - **Coupon ID (custom field):** tag the **"Manufacturer Offer ID"** from the Inmar PDF into the **Coupon ID** field for the applicable items. Keep **Display Type = "Item"** (NOT Coupon). Use the item name (highlighted blue in the Inmar doc) to verify; the Manufacturer Offer ID is highlighted orange.
  - Name: full name, no special characters (e.g. `•`). Include quantities in the description. Add dollars-off/percent-off where applicable.

## Post-processing / FQC (DOC)

- File a **FAB ticket** to have FLEX complete Image QC, Coupon ID QC, and spotchecks (clone the sample FAB ticket, update due date, flyer run, Inmar doc, assignee, dates, links). If Image + Coupon ID QC will take >30 min, file a FAB ticket for FLEX support.
- **FQC checklist:** Links QC (no links) marked done; check dates (live 12 AM Tue); Distribution Category Grocery; preview date Thursday; shown on all channels; spotlights/key messages; open pricing zones full-screen and click items to confirm pops/links work; confirm all pages in correct zones; Item Image QC (clear PDFs — line items use no PDF images); page-level categories (**no categories on page 1**, check for sub-pages); thumbnails (M1–M6 share thumbnails, **M7 adjusted separately**).
- **Coupon ID QC:** open the `Inmar.pdf` for the run, use Item Search ("Name" "CONTAINS") to find each listed item, and tag the corresponding Manufacturer Offer ID into the Coupon ID field.
- **Flyer Review type: Lite.**

## Out-of-processing

- Page swaps handled per the baseline page-swap process. Black Friday comms exist for 2024/2025.

---
*Source: Marc's Grocery OneGuide (Google Doc `1ur8X7iuStH_mKFPWGGoSB-fYzu5rLnSPxwdNFMTNrZA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
