# Dierbergs — Processing Guide

> **Source:** Dierbergs OneGuide (Google Doc `1b6ibSPSGy0-_X3RUIjdv6lqqVvXVRHozGy6XcSwZISc`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#dierbergs`, `#flex-processingsupport` |
| Hosted URL | dierbergs.com |
| Flyer type(s) | Weekly Ad; Monthly; plus Rewards, Bob's Barn, Hosted/Preview, and ad-hoc runs |
| Processing | Auto-stack; Flex = Processing Support; OS = Setup + FQC; no coupons; no Feedel |

## Files & schedule
- **Files received:** Tuesday (PDFs + codesheet in the SFTP).
- **Weekly publication:** Available/Valid From Tuesday → To Monday. **Ad-hoc:** dates per PDF (valid & available same day / no consumer preview).
- **Linking documents:** **two** — a URL linking document (Insert Management Tracker) and a UPC document.

## Upload & setup (owned by Vendor) — pages are uploaded via codesheet
**Codesheet manipulation:**
1. Download the codesheet from the SFTP → open in Google Sheets.
2. If it has more than one file set, **split by duplicating into separate tabs** named per the codesheet labels (e.g. Weekly tab keeps only weekly pages, Rewards tab keeps only rewards pages, etc.). Rename column1 → zones, column2 → stores.
3. Add ".pdf" to the end of each page name (via `=concat` or manually). **No spaces; names must match the SFTP exactly.**
4. Save as `.csv`.

**Codesheet upload:** flyer run → Code Sheets → **Config name: generic** → PDF Base Directory = the SFTP folder the codesheet is in → set toggles → Save → Process Code Sheet. Confirm pages/pricing zones/stores assigned; check FTP that all pages uploaded.

**Attachments:** download the **UPC document** from FTP (dates matching run), navigate to the correct tab, download the relevant tab as `.csv`, attach to all vendor tasks. Get the **Linking Document** from the Insert Management Tracker (current year tab → find date/flyer), copy the links + row 1 into a new sheet, download `.csv`, attach to all vendor tasks.

**Setup QC — Edit Details per run type:**
- **Weekly Ad:** Available/Valid Tue–Mon; available everywhere; external run name "Weekly Ad".
- **Rewards Ad:** dates match PDF; **Hosted only**; external run name "Rewards".
- **Bob's Barn:** dates match PDF; available everywhere; external run name "Bob's Barn".
- **Ad-hoc (Organic Sale, 15-hour BASE, 72-hour Lake, etc.):** dates match PDF; available everywhere (if meets content policy); **Secondary Publication toggle = Yes**.
- Fab-4 thumbnails; Geography "no stores/FSAs added or removed".

**Hosted/Preview flyer (static, no clickable items):** upload and FQC in one sitting. Use the **Dierbergs Hosted Codesheet Generator** — paste all "preview" version file names into the "start here" tab, duplicate the Codesheet tab renamed to the flyer start date, confirm page count per version (lake/east/base) in the FTP, delete extra page columns beyond the last page, download `.csv`, upload to the Hosted run (config generic). Setup QC: Available Fri–Mon (one week prior to valid), Valid Tue–Mon, internal run name "Month-day HOSTED", **Hosted only**, external run name "SNEAK PEEK". FQC: mark vendor tasks + auto spotchecks complete, add comment "static flyer, no clickable items".

## ⚠️ Common errors / risk items (retailer-specific)
- **WOW Wednesday (and similar) valid dates:** items/deals are valid **only on the Wednesday** the flyer goes live — ensure all items on that page carry the correct (single-day) valid dates.
- **CTAs must be boxed AND tagged:** all of **CLIP NOW, SHOP NOW, WATCH NOW, LEARN MORE** must be boxed separately and tagged with the URL from the linking document.
- **Name risk items:** (1) if the flyer name has dots, delete them and separate names with commas; (2) keep the "&" symbol in the name (don't write "and"); (3) fix text-extraction errors against the flyer.
- **Description risk:** if the description has dots beside words, separate onto different lines.

## Box Draw (Low — Auto-Box ON, Box QC bot ON; linking-doc required)
- **Include:** coupons, packaged deals, retailer logo, social media, special weblinks. **Exclude:** sign-up page.
- Box items as they appear (price but no image still gets a box); use text boxes; box multiple amounts/prices separately.
- Banners with callouts tagged per the **Dierbergs URL Management Tracker**: Column E = flyer page, Column F = ad block, Column G = URL. Apply the correct URL to **all versions** of a page (e.g. pg 6 and pg 6 L).

## Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand used for Box/Tag.
- **Custom field "Extra SKUs":** used when SKUs exceed the SKU field character limit.
- **SKUs (UPCs):** from the attached UPC document, tag all UPCs associated with the item. **Items sharing the same AD GROUP name are grouped** (e.g. all Coke items = Ad Group 170) — include all their UPCs, comma-separated. Overflow → Extra SKUs field.
- **Sale Story:** for page-wide promos ("Buy 4 Save $4") use only the main callout.
- **URL/CTA:** CLIP NOW / CLICK HERE / CLIP COUPON NOW / LEARN MORE / SHOP NOW get their own box, tagged as a direct link from the linking document.

## URL/Links QC (owned by Vendor)
- Verify the number of URLs in the URL document matches FAdmin; apply per Columns E/F/G to all page versions.
- **YouTube CTAs:** change item type to Video, open the link, click Share → Embed, copy from `https:` to the first `"`, paste into the Video URL field.

## Image QC
- Use PDF images if available, matched to the flyer product. **Do not use dark/black-background images — leave as cutout.** White-background cutouts acceptable when no clean PDF; never lifestyle or dark backgrounds.

## FQC (owned by Vendor)
- Check staggered dates (all pricing zones vs Page 1); check 1–3 day valid-date sales across pages; links tagged (match tracker count, applied accurately).
- **UPCs applied:** Item Search `SKU Is [blank]` should be **< 10**; `SKU Is Not [blank]` should be **98%+** of items.
- Item image QC green; thumbnails (1065×600 ×2, storefront carousel premium ×2, organic ×1).
- Edit Details per run type (Weekly/Rewards/Bob's Barn as above); page categories (≥1 per page except Page 1 / no-product pages); all items boxed/tagged; sessions rerun as needed; Geography unchanged WOW; **Overview → Ad Hoc Processing → Mark Items Store Only** (count changes to 100%).
- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps standard (baseline page-swap video). Black Friday comms doc provided.

---
*Source: Dierbergs OneGuide (Google Doc `1b6ibSPSGy0-_X3RUIjdv6lqqVvXVRHozGy6XcSwZISc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
