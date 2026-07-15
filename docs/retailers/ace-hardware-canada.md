# Ace Hardware Canada — Processing Guide

> **Source:** Peavey Mart, Mainstreet Hardware & Ace Hardware Canada OneGuide (Google Doc `19y-BkwPR479HcTFVZhE3QFSionUCTTC2gqYQ8OTNrAw`), updated May 11, 2024.
> One guide covers three banners (Peavey Industries). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#peaveyindustries` |
| Hosted URLs | flyertown.ca/flyers/peaveymart-peaveymartm1000 · flyertown.ca/flyers/mainstreethardware-flyer · peaveymart.com/flyer |
| Flyer types | Peavey Mart (type 2685, weekly) · Ace Hardware Canada (type 2685, weekly) · Mainstreet Hardware (type 9970) |
| Processing | Auto-stack; **Flex = FAB Tickets**; no OS, no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Monday.
- **Peavey Mart cadence:** Available From Monday, Valid From Friday; Available To Monday, Valid To Tuesday. Valid dates normally Fri–Wed but rotate — **always check the PDFs**.
- Available dates = **four days before** valid dates.
- **Linking document:** No.
- Set internal preview date to the **following Monday**; OS processing takes 1–2 business days — do not skip setting the preview date.

## Upload & setup (owned by Flex)

- **Peavey Mart — codesheet upload:** open the flyer run; confirm the code in the run name matches the FTP files (e.g. 1A/1B/1C). Find the `.csv` codesheet in the FTP, copy its name and its path (use the path affiliated with the codesheet — there are subfolders). Name = "base". **Config name: `generic`. Toggles: 1, 3, 4, 6.** Process.
  - Internal run name convention: `04D_Peavey Mart_2022`. External run name = main callout on page 1. Seasonal theme: no theme. Standard 4 thumbnails.
  - Once OS tagging is complete, an Item Export is sent to Peavey (see post-processing — owned by DOC, Flex does not do this).
- **Ace Hardware Canada — codesheet upload:** create codesheet (name "flyer"), base path, upload local codesheet, **Config name: `generic_language`**, set PDF base directory from Merchant → Details → FTP Path → View Files. **Toggles: 1, 3, 4, 6.** Save, process, check sessions. Update preview date to **four full days after upload**.
- **Mainstreet Hardware — manual upload:** Pages → Edit → select the **MainStreet** folder (case-insensitive) → select all (usually 4 pages). Autogroup, cross-referencing the file name so indexing is correct. Save & complete. Create **one** pricing zone "Base", language English. Pricing zone → Stores/FSAs → add all. External run name = main callout on page 1; no theme; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- **Valid dates rotate weekly** — verify against the PDFs, don't assume Fri–Wed.
- **Available dates must be exactly 4 days before valid dates.**
- **Logo/banner boxing is Peavey-Mart-only.** Do NOT box logos/banners for Mainstreet Hardware. Only box the large logos (front/last page), not the small corner logos on interior pages.
- **Multi-size/dimension items:** box each size separately and ensure the correct text box is associated with the correct item — mis-association breaks tagging.
- Don't put a weekly flyer under a catalog in flyer sorting — the catalog would show before the preview flyer on the hosted experience.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Box every item with a price; use text boxes when item and price can't be boxed together; box items with SKUs even without a price; keep disclaimers inside the box. Box footers (with or without a link), top/mid banners, the "Proudly Serving Rural Communities" banner (last page, whole area), social-media logos (last page, each separately). Single-page banners = one box around the whole page; Gift Card page = box the Peavey logo separately then the rest.
- **Tag / Tag QC (Low; Auto-tag ON, PDF image auto-select ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. Brand is box-draw specific. **URLs = risk item.** Do Image QC for all three banners during the tag process.
- **Image QC:** use PDF image extraction. Prefer a clean PDF image for single items; do not use images with black background, shadow, curvy borders, or lifestyle background. If multiple images in one box, use the **cutout**. If no clean PDF image, use the cutout.

## Post-processing / FQC

- **Item Export (owned by DOC — Flex skips):** export items, trim to 10 columns (item_id, flyer_name, page, display_type, brand, name, description, sku, sale_story, url), split a tab per region, upload to SFTP (credentials in the OneGuide — not stored here), then notify the retailer. Separate export emails exist for Peavey Mart, Mainstreet Hardware (one tab) and Ace Hardware (seven tabs). Note "export sent" + date in the flyer comments. When the export is returned, keep only item_id, sku (delete all skus), and url.
- **FQC (Flex):** set external run name (from Key Message), theme (usually No Theme), thumbnails — Thumbnail 1065×600: 2 pages (logos); Stock premium: 1; Storefront Carousel Premium: 2; Storefront Carousel Organic: 1 (apply to all). Insert/swap pages if needed. Flyer sorting: weekly above catalogs, preview below live.
- **Flyer Review type: Lite.**
- Preview links (DOC-owned) sent per banner.

---
*Source: Ace Hardware Canada OneGuide (Google Doc `19y-BkwPR479HcTFVZhE3QFSionUCTTC2gqYQ8OTNrAw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
