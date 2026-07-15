# Runnings — Processing Guide

> **Source:** Runnings OneGuide (Google Doc `1tEJ3PBpl7bljuXLW4tWiGTbXUZIJcYCD34qbIGFvxlY`), updated Jun 1, 2026. Contacts/credentials omitted.

> **Key upload fact:** Runnings sends **one version of the codesheet** (e.g. "3B", "4A", "5D") with a row for each unique flyer run. Open the .xlsx and use the correct row per the flyer run you are uploading.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#runnings` |
| Hosted URL | https://www.runnings.com/ |
| Flyer types | Flyer Type 1 — Weekly (+ Lena's Liquor, monthly pull-out) |
| Processing | Auto-stack; Flex (Flyer Review); OS Setup; Strategic Ops involved (retailer data services / Feedel); no coupons |

## Files & schedule

- **Files received:** Monday (often ~a month's lead time; **Lena's Liquor is a much shorter lead**).
- **Available From:** Thursday · **Valid From:** Sunday · **Available To:** Saturday · **Valid To:** Saturday
- **Linking document:** Yes (URL document per publication).
- **Workflow:** Upload & Setup (Vendor, 5+ days out) → FQC (Vendor, 1 day out).
- **[DOC]** The retailer emails to confirm files are on the SFTP; use the email to create runs (there can be multiple runs per email — each with its own dedicated SFTP folder). Add flyer run IDs to the VAST tracker.

## Upload & setup (owned by Vendor)

**⚠️ ALWAYS use the correct row from the codesheet** — multiple runs are in the one BASE.xlsx, each row named by the flyer run name.

1. Download the codesheet .xlsx and URL document(s) from the SFTP. URL attachments have "URL" in the name. Multiple URL docs are common — match the URL name to the run.
2. The single codesheet .xlsx includes **all** publications for the week (e.g. `Runnings_10B_Base.xlsx` contains both 10B Base and 10B Insert).
3. Open the generic Runnings codesheet template; **duplicate the Template tab and rename it per flyer — one new tab per flyer** (10B Base and 10B Insert each get their own tab).
4. In the new tab, change the date (MM/DD/YYYY) in the **START** and **END** columns to the dates from the downloaded excel. **Do NOT remove the leading `'`. Edit the date only — do NOT change the times, and do NOT copy directly from the FTP excel.** (Changing the time format triggers a warning and the codesheet won't run.)
5. Copy **Version, Stores, and Pages** from the downloaded excel into the flyer tab.
6. Find & Replace the page-name ending: add **.pdf** → This Sheet → Match Case → Replace All.
7. Save the tab as a **.csv**.
8. Codesheet upload: Name **codesheet**, choose the .csv, **Config name `runnings`**, PDF Base Directory = base path to the flyer PDFs (e.g. `/Runnings2025/2025 10B/10B Base` for 10B Base, `/…/10B Insert` for 10B Insert). **Toggle everything except the 2nd and last.** Save & Process.
9. Download the URL .xlsx and attach to all vendor tasks (**select Mass Attachment**). Base URL attachments usually don't have "BASE" in the name; Insert URL attachments have "INSERT". **OS won't start tagging until linking docs are attached.**
10. Mark Flyer Creation task Complete.
11. After the codesheet runs successfully, **hide the tab(s) you created** — only the Template tab should remain visible.

### Setup QC
- Draw Standard 4 Thumbnails.
- Add External Run name = the main callout on the cover page (e.g. "Brands You Love!").
- **Staggered Dates error** is generally a false flag (the "runnings" codesheet processor interacting with pricing-zone-level dates). To clear: Staggered Dates tab → select all Pricing Zones → Apply Dates to Selected Flyers → click into any bolded Available From/Valid From values → OK. Dates should not change but should no longer be bolded.

### Lena's Liquor (monthly pull-out)
- 1-page flyer with <7 items; runs monthly (usually 1st to end of month; if late, publish ASAP or within requested dates).
- Manual upload; Flyer Creation → Start Task; make one "Base" pricing zone; assign **store code 27**.
- Edit Details: dates per email, available everywhere, no theme; Standard 4 thumbnails.

## ⚠️ Common errors / risk items (retailer-specific)

- **PDF Image Extraction errors are the largest contributor to live-date errors.** Use relevant, clean images; if none, use the cutout. Verify the selected image is the one most similar to the item; if no similar image, use no PDF.
- **Using the wrong codesheet row** for a run — always match the row to the flyer run name.
- Changing the date **time** in the template (breaks the codesheet) — edit date only, keep the leading `'`.
- Staggered Dates warning — resolve via the Staggered Dates steps (false flag).

## QC specifics

### Box Draw (Low complexity; Auto-Box ON, Box QC bot ON)
- Requires Box Draw/Box QC-specific linking document.
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons and packaged deals.
- Box all items separately (text boxes when necessary); box all Runnings logos (first and last page); box all social icons (Facebook, Twitter, Instagram); anything with a price gets a box.

### Tag / Tag QC (Low complexity; Auto-tag OFF; PDF Image Auto Selection ON)
- Requires Tag/QC-specific linking document.
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude** pre/postfix and valid dates.

### Image QC (owned by Vendor)
- PDF preferred if clean; otherwise cutouts accepted.

## Post-processing / FQC (owned by Vendor)
- **Links QC:** social links — Facebook https://www.facebook.com/myrunnings, Twitter https://twitter.com/MyRunnings, Instagram https://instagram.com/myrunnings/, Pinterest https://www.pinterest.ca/runnings/.
- Mark off Autostack Spotcheck; leg heights auto-set (should be 65/40); Standard 4 Thumbnails; External Run Name set; re-check Staggered Dates error.
- Ad hoc processing → Mark Items In Store Only.
- Pages: all items QC'd. Pricing Zone: vertical/horizontal previews interactive, item view all tagged, storefront spotcheck slicing good.
- Geography: compare to a similarly-named run (Base/Insert/Lena's Liquor); usually no changes; if mismatch, confirm the codesheet ran green (else flag account owner).

## Flyer review
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Runnings OneGuide (Google Doc `1tEJ3PBpl7bljuXLW4tWiGTbXUZIJcYCD34qbIGFvxlY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
