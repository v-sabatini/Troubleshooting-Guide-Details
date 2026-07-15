# Lidl US — Processing Guide

> **Source:** Lidl US OneGuide (Google Doc `15lWXIeZeOKaSjwUUwlHKfUClCORU2TPa55sXRCTwlCg`), updated Jul 14, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#lidlus` |
| Hosted URL | N/A |
| Publications | 6636: Weekly Ad · (archived) Additional Tab / "MarketingPagesTab" · Magazine |
| Processing | Auto-stack; Flex + OS Processing Support; no coupons; Feedel/retailer data services |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Wednesday, Valid From Friday; Available/Valid To Thursday. (Setup QC lists Available Mon → Tue, Valid Wed → Tue — confirm against the run.)
- **Processing type:** Auto-stack.

## Upload & setup — Weekly (Flyer Type 6636)

Add info to the VAST tracker to start upload. Codesheet-driven upload:
1. Download the **Flipp Version .xlsx** from FTP for the week.
2. Codesheet manipulation:
   - Store openings (grand openings) are in **yellow, marked "GO" in column F** — must be added to FADMIN, then to the pricing zone; add a comment note. Delete the salmon-coloured row and any store openings before upload.
   - Delete column A; in the new column A add **"CW"** in front of the week number (FADMIN matches the run name to the codesheet name).
   - Highlight column E, replace `CW##_` with blank (leave only the zone name).
   - Delete rows highlighted **red** (closed stores); delete the Harlem row if present.
   - Unhide any hidden tabs, then delete them.
3. Save as **CSV** named **`CW## Flipp Version`** (e.g. `CW18 Flipp Version`). A different name causes an upload error.
4. Upload codesheet; confirm all pages uploaded in FTP (manually add missing pages + PZs by Version name).
5. Mark Flyer Creation + Setup QC complete.

### ⚠️ Common errors / risk items
- **Wrong file name** on the CSV causes an upload error.
- **"marketingpagestab … has already been uploaded!"** warning → Force Processing, then remove all marketingpagestab pages (Pages → Layout → takeout, then Pages → Edit → delete pages named "marketingpagestab").
- **Empty Version Name rows** cause an upload error — delete those rows and re-upload.
- **Tagging social media icons** (bottom-right of page): YouTube, Lidl website, Facebook `facebook.com/LIDLUS/`, Twitter `twitter.com/lidlus`, Pinterest `pinterest.com/LidlUS/`, Instagram `instagram.com/lidlus/`.
- **SKU in description:** include the item number (e.g. "No. 992961") as the last part of the description.
- **Item-level valid dates:** sections with Saturday–Sunday date callouts — apply those valid dates to all items in that section; watch for pages with different start/end dates (tag both Valid From and Valid To).

### Setup QC checklist
- Pricing Zones: all PZs have the same page count.
- Internal run name always **"Week xx"** (so the codesheet is recognized); no preview date; **hide on Hosted only**; no theme; Standard 4 thumbnails.

## QC specifics

- **Box Draw (Low/Easy; Auto-Box ON, Box QC bot ON):** exclude coupons, retailer logo, sign-up page, social media, special weblinks; **include packaged deals**. Box each product block individually.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON):** linking doc required. Include brand, name, valid dates, description, SKU, price, sale story, categories, original price. **Exclude pre/postfix, disclaimer, URLs.**
  - Include SKU/item number in the description.
  - Item valid dates: any page with a date callout at the top applies to all items on that page (tag both From and To).
- **Image QC (PDF preferred, done in Tag/Tag QC):** use clean PDF; if not clean/clear use the cutout. For multiple items use the cutout showing all items.

## FQC (owned by Flex)

- Check Geography (usually unchanged); Standard 4 thumbnails; check pricing-zone previews.
- Item Search for "Starting at" (must have "starting at" in prefix), for blank Valid From by page, and for the Dish page ("VIEW MORE" → `lidl.com/the-dish`).
- Compare item count between versions of each page (except GO/store-specific pages).
- Confirm website/social callouts boxed/tagged (page P0002 social links: Facebook, Instagram, etc.).
- Toggles: **Hidden on Hosted only.**
- **⚠️ Flyer sorting:** Weekly Ad appears first, then the Additional Tab. **Adjust flyers every Friday EOD** so the system orders correctly.
- **Flyer Review type: Lite.**

## Out-of-processing / archived

- Store hours: lidl.com; order online: shipt.com/stores/lidl (participating stores).
- **Archived (no longer actioned):** Additional Tab "MarketingPagesTab" upload (hide in distribution/Flipp, secondary publication, external run name "Exclusively At Lidl"); distribution/Flipp display triggers run the Tuesday after go-live; OPTICS ticket for trigger check; Links Tracker updates.

---
*Source: Lidl US OneGuide (Google Doc `15lWXIeZeOKaSjwUUwlHKfUClCORU2TPa55sXRCTwlCg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
