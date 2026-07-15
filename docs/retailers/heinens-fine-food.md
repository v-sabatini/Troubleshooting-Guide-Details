# Heinen's Fine Food — Processing Guide

> **Source:** Heinen's Fine Foods OneGuide (Google Doc `1jzDekSjUedeXwa8KJ_4-QP1vqF47Fe-lDagPKwobcWE`), updated Feb 19, 2026. Contacts/credentials omitted.

Two-market flyer: **Cleveland (HE)** and **Chicago (CH)** run as two pricing zones.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | Flipp only |
| Slack channel(s) | `#heinens` |
| Hosted URL | heinens.com |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday (retailer emails when files are dropped — respond confirming receipt; update Vendor Setup Tracker / VAST with FlyerID).
- **Cadence:** Available From **Tuesday 12:00 PM** / Valid Wednesday → Available/Valid To Tuesday. 1-week run. No preview date. Hidden on Hosted. No linking document.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages > Edit > select page(s) from FTP > **do not auto-group**. Files are labelled **HE (Cleveland)** and **CH (Chicago)** — two of each page number. Manually set grouping by file name; all English; Save & Complete.
- **Pricing zones:** create two — **HE** (add all HE pages, Cleveland) and **CH** (add all CH pages, Chicago). Add "HE" store set to HE PZ, "CHI" store set to CH PZ.
- **Setup QC:** Available From Tuesday 12:00 PM; Valid From Wednesday; internal run name "Week ##"; no external run name; no theme; standard 4 thumbnails (1065×600 ×2pg, Stock premium ×1, Storefront carousel premium ×2, organic ×1); confirm sessions ran and FSAs generated.

### ⚠️ Common errors / risk items

- **Category mis-tag (RISK):** items tagged as Dairy when they're in the Deli section, etc. — categories are location-based on the page.
- **Auto-box draw errors on certain pages** → pages need re-upload. Fix: set the run as **NGL** (hide all availability toggles, reassign all vendor tasks to Flipp), make a new flyer run, and do a manual upload of the affected pages **with CropBox**.
- **Red sessions in Setup QC** → find **Page Tile Generation** in the WES pipeline, Rerun Task, wait a few minutes; escalate if it persists.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include retailer logo**; exclude coupons, packaged deals, sign-up page, social media, special weblinks. Do not box QR codes or the social/website URL.
- **Tag / Tag QC (Low; Auto-tag ON):** include Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and item URLs.** Brand tagged only if a single brand (leave empty if multiple). BOGO with no price → "BOGO" in Prefix, other sale story in Sale Story. **Coupons: Display Type = Coupon, draw barcode for all three barcodes.**
  - **Categories (location-based):** use the page section header. Page 3s = all Grocery except bottom-right = Wellness. Cheese in "Prepared Foods" = "Artisan Cheese"; "Grab 'n Go"/"Dinner Solutions" = "Prepared Foods".
  - **URLs:** no item URLs; add URL to the retailer **logo** only (Display Type: Link → `https://www.heinens.com/`).
- **Image QC:** always select PDF if available (lifestyle image OK); if PDF cut off, use Cutout; multi-items use 1 image.

## Post-processing / FQC (owned by Vendor)

- Item Category QC and Item Image QC (Generate All, usually <100 items).
- **Link FQC:** confirm page 1 logo linked to `https://www.heinens.com/`, verify URL via Sessions, confirm in preview.
- Spotcheck; mark Auto-Stack completed; confirm vendor tasks; dates/thumbnails; geography stable week-over-week; **OK to ignore "Other Warnings" / stores-not-assigned.**
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Heinen's Fine Foods OneGuide (Google Doc `1jzDekSjUedeXwa8KJ_4-QP1vqF47Fe-lDagPKwobcWE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
