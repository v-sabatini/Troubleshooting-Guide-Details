# Fleet Farm — Processing Guide

> **Source:** Fleet Farm OneGuide (Google Doc `1yxW7OEtcnh1lqZjThV600C95bGTe7eDmvhqCb8g4_V4`), updated Jul 7, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channels | `#fleetfarm` |
| Hosted URL | fleetfarm.com/sitewide/weeklyAd |
| Merchant | 3427 (also 3817) |
| Flyer types | **Weekly Ad** · **Catalog** · Weekly Ad — **Weekend Disruptor** |
| Processing | Auto-stack; no coupons, no Feedel |
| Linking document | **Yes — required (used for both Box and Tag)** |

## Weekly Ad — files & schedule

- **When files arrive:** ad hoc.
- **Publication cadence:** Available From Monday, Available To Sunday; Valid From Sunday, Valid To Monday (Weds–Tues cadence when confirming).
- **Preview date:** ad hoc. **Processing type:** Auto-stack.

### Upload & setup (owned by DOC) — manual upload
- Pages Tab → Edit. Select all pages from the SFTP menu on the right.
  - Files are in folders labelled with a **C# matching the flyer run name**.
- Once pages are listed at the bottom, **Auto-Group**.
- **Find & attach the corresponding link document (from the SFTP) to all tasks.**
- **Save & Confirm — do NOT Process Internally.**
- **Pricing zones:** one zone, Base, add all stores.
  - If the flyer name indicates a specific state or city, only those stores are manually added. Comments may also indicate store info if not applied to all stores.
- **⚠️ RISK: processing cannot start without the link document.** If no link document is in the SFTP, complete all previous steps **but do not complete Setup QC.**

### Setup QC checklist (owned by DOC)
- Confirm all pages uploaded correctly (Pricing Zone tab → Items View). **RISK: confirm no pages remain un-uploaded in the SFTP.**
- Confirm flyer dates — **dates are NOT on the PDF; they always follow Weds–Tues cadence.** Specific date ranges may be listed for front/back page items.
- Complete thumbnails (4 Standard); ensure all preview dates set; complete Setup QC checklist.

## Weekend Disruptor (single-page Weekly Ad variant)

- **When files arrive:** ad hoc. **Cadence:** Available From Thursday, Available To Sunday; Valid From Sunday, Valid To Thursday.

### ⚠️ Common errors / risk items (Weekend Disruptor)
- **Available-time adjustment:** because the file is sent the Wednesday before the Thursday launch, the AVAILABLE time must be set to **24 hrs from confirmation of file receipt (inclusive of links)**. E.g. if all assets received and uploaded at 3pm, it's available Thursday @ 3pm EST.
- **Cannot go live without links.** Links **must** be sent before this ad can launch — the retailer has instructed it can never go live without links.

### Upload & setup (owned by DOC)
- Manual upload: Pages Tab → Edit, select the single page from the FTP. No need to autogroup.
- Attach the link document to all tasks.
- Save & Confirm — confirm OK to autogroup all as PAGE 1 (only 1 page).
- Pricing zones: one zone, Base, add all stores.
- **RISK: processing cannot start without the link document** — same rule as above.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF; linking doc required)
- **Include:** special weblinks.
- **Exclude:** coupons, packaged deals, retailer logo (**do NOT box and link the logo**), sign-up page, social media.
- **Ensure sub-items are boxed separately from the main item.**
- **Banners & CTAs:** called out on the link document with "BANNER" in the Product Name (Column B) and "NO SKU" in the SKU (Column C). Box these — apply the boxes moving forward.

### Tag / Tag QC (Medium complexity — Auto-tag OFF; linking doc required for both Box/Tag)
- Brand used for both Box and Tag.
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **URLs: only use links found directly on the spreadsheet. If a link is not available on the sheet, leave it BLANK** — do NOT input a "search" URL or any link not on the spreadsheet.
- Tag sub-items and Banners/CTAs (per the link document) as well.

### Image QC
- Standard: PDF preferred if clean; otherwise cutouts accepted.

### Spotchecks
- Standard pricing spotchecks included in the pipeline.

## Post-processing / FQC (owned by DOC)
- Retailer preview email sent (Generate Direct URL in Fadmin: select Weekly Ad toggle, input flyer name or C# to find the run, Generate HTML, copy the direct link from the URL column).
- Pre-final: confirm dates against PDF; availability toggles correct; thumbnails correct with retailer logo; **confirm External Run Name added; confirm flyer sorting is accurate.**
- Complete FQC checklist.

## Flyer Review (owned by DOL)
- **Flyer Review type: Lite.**

---
*Source: Fleet Farm OneGuide (Google Doc `1yxW7OEtcnh1lqZjThV600C95bGTe7eDmvhqCb8g4_V4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
