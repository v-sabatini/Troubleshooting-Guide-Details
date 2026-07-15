# Factory Direct ST — Processing Guide

> **Source:** Factory Direct ST OneGuide (Google Doc `1u0ZLAwwWlDFcAiCIK0OxUP_ZnG5EGGCSe8zFrjc9vBA`), updated May 12, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Weekly: all platforms · Seasonal: Hosted only |
| Slack channels | `#factorydirect` |
| Hosted URL | flyertown.ca/flyers/factorydirectst |
| Flyer types | **Weekly (2833)** · **Seasonal** (weekly when running) · **Dollar Deals / $10 Deals** (run times vary) |
| Processing | Auto-stack |
| Who's involved | Flex (Setup + Flyer Review); OS (Setup); DOC (FQC); no coupons; Strategic Ops — yes, Feedel/retailer data services |

> Note: Factory Direct also sends Big Daddy Closeouts pages, but those have a separate merchant page.

## Files & schedule

- **Files received:** Monday, via SFTP, with an email confirming run times and the Weekly's External Name. Uploads can be done by vendors, but take it back if files arrive late.
- **Cadence:** Available From Wednesday, Valid From Wednesday; Available To Monday, Valid To Tuesday.

## Upload & setup (owned by Flex)

- Up to three publications: **Weekly** (always), **Seasonal**, **Dollar Deals**. FTP has a folder per version; page revisions often arrive later and aren't filed in the right folders.
- Upload all pages with the upcoming Valid Date to the **Weekly** run as English pages; **Auto-Group** (verify numbers against file names). Add all pages to one PZ named **Base**, Save & Done. Assign all stores from the store set.
- Weekly pages get separated to the other versions via the **cloning tool after OS processes** (see out-of-processing). If uploading yourself, you can instead build separate Seasonal/Dollar Deals runs with only their relevant pages.

### Setup QC (Flex)
- Edit Details: Valid Wednesday–Tuesday, same Available dates. **Weekly = available everywhere (no toggles); Seasonal = Hide in distribution & Flipp.** External run name from the email for Weekly; use the first-page title for Seasonal and $10 Dollar Deals. No theme.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **⚠️ An item with different prices and SKU numbers must be boxed with a text box.**

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific.
- **Brand:** enter into Brand tab; items with no brand → tag **"Debranded"**.
- **SKU:** all SKUs; items with multiple SKUs — enter all.
- **URLs:** search their website by SKU or item name.

### Image QC
- Generally receives cutout images only — no need to QC.

## Post-processing (owned by DOC)
- **URL/Links QC:** every item should have a link; use the SKU to Fetch/Update any missing. If a populated link is wrong, find the item on their site by SKU.

## Out-of-processing

- **Page swaps:** very common (a few per week). Requests arrive by email with new files via SFTP; Flex can action.
- **Pre-FQC:** mark In-Store Only; mark Auto Stack complete; confirm dates in Item View; legibility heights **Scan 30 / Read 20**; page categories; verify store assignment.
- **Cloning (after Data Piping + Vertical Preview populate):**
  - Overview → Ad Hoc Processing → Clone. Create **Seasonal** clone and **$10 Deals** clone; copy tracking-code URLs = **Yes**. Check stores copied over in Pricing Zones.
  - Remove all but Seasonal pages from the Seasonal clone PZ; all but Dollar Deals pages from the $10 clone PZ. **Hide both in Distribution and Flipp.**
  - Remove all but Weekly pages from the Weekly run.
  - Sort: **Weekly (first), then Seasonal, then Dollar Deals.** Proceed to FQC.

## Flyer Review
- **Type: Lite.**

---
*Source: Factory Direct ST OneGuide (Google Doc `1u0ZLAwwWlDFcAiCIK0OxUP_ZnG5EGGCSe8zFrjc9vBA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
