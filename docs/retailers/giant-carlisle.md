# Giant Carlisle & Martin's Foods — Processing Guide

> **Source:** Giant Carlisle & Martin's Foods OneGuide (Google Doc `1w3auLK-JsRcPzRJgoAwPbIPdJ2-bFu6wGt3h5X3Yflw`), updated May 6, 2026. Contacts/credentials omitted.

Royal Ahold banners processed together (same process). **High-touch account** with a codesheet-heavy setup, high-res page requirements, and many retailer-specific rules.

## Account at a glance

| | |
|---|---|
| Account tier | Core (CXE Core pod) |
| Availability | All platforms |
| Slack channels | `#3fl-royal-ahold`, `ahold-delhaize`, `ahold-ops` |
| Hosted URLs | giantfoodstores.com · martinsfoods.com/savings/weekly-ad/print-view |
| Flyer types | Giant Carlisle Weekly Circular (6405) · Martin's Foods Weekly Circular (5541) |
| Processing | Auto-stack; 3FL Flex (Processing Support); no coupons; **Feedel processing (yes)** |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available Thursday, Valid Friday → Thursday. **Preview: Monday** before go-live.
- **Workflow:** Upload & Setup (Flex), Image QC (Flex), FQC (Flex); files transferred by DOC. Add both runs to the Royal Aholds Flex Processing Tracker.

## Upload & setup

### Transfer files (DOC)
- AEM portal → The Giant Company (GC) → Marketing → Weekly Ad → Weekly Circular → working week → Final Files → download **Final PDFs**.
- Use the **Flipp Digital Pages** folder (verify a C07 page has **no barcodes**).
- **⚠️ Delete the "Page 07" folder entirely** — it has the same pages as Flipp Digital Pages but **with barcodes** (we don't want barcodes).
- **NEW May 2026:** there may be a file named **"MY"** in Flipp Digital Pages (often page 3, not 7). Note its page number, find the corresponding "MY" page **with barcodes** in that page-number folder, and delete it.
- Upload pages to the file-drop software (GC → 2026 Files → new folder). Royal Ahold pages are **very high quality / bulky** and slow to transfer.

### ⚠️ #1 Risk — page height must be set to 4096 pixels BEFORE any upload
- In **[Edit details]**, set page **height to 4096 pixels before ANY upload steps / before running any codesheets.**
- If done after codesheets run (or missed), **the run must be re-uploaded and reprocessed entirely** — a huge go-live/CUSAT risk. **Notify the coordinator immediately if missed.** Royal Ahold sends such high-quality pages they won't render at lower pixel heights.

### Codesheet manipulations & upload
- From SFTP → working week → Recapper → download **both** the **Ad Version Sheet** and **Recapper**.
- **Ad Version Sheet = store distro / pricing-zone codesheet.** Trim to headers (Store #, Ad Version, Giant, Martin's); rename Store # → Store Numbers, Ad Version → Zone (column A), add a "TBD" column; filter; delete blue-highlighted rows down. Duplicate into **GC** and **MF** tabs, then in each keep only that banner's stores (filter the other banner's "X" rows and delete). Download each as CSV.
- **Recapper = pages portion.** Version row starts on row 5; set Row1 "Account:", Row2 "Created:", Row3 "Sales Date:"; add a helper column; copy PZs to column C; duplicate into GC and MF tabs; paste each banner's zones from the Ad Version sheet into column A, remove duplicates, match PZs, delete blank rows and helper column; save as CSV.
- **[Edit details]:** Preview = Monday before go-live; External Run Name = "Weekly Ad"; No theme; **set height to 4096 pixels** (Show/hide rarely-used fields).
- **[Codesheet] Stores:** attach GC or MF Ad Version CSV — **Config: `giant_landover_stores`**, PDF Base Directory `/`, **Toggles 1 & 4** → Save (runs green).
- **[Codesheet] Upload (pages):** attach GC or MF Recapper CSV — **Config: `giant_landover_pages`**, PDF Base Directory from FTP (just before the pages folder), **Toggles 3, 5, 6** → Save. Carlisle runs green; if uploaded first, Martin's Recapper may run yellow ("pages re-uploaded" — mostly "HB/AD" repeat pages, safe to ignore) → **Force processing** for Martin's.
- Flyer Creation → sessions run (~30+ min due to high-res pages). Thumbnails Standard 4 (stretch across page 1 only). Confirm valid dates and that GC pages are in the GC run, MF pages in the MF run.

### ⚠️ Other risk items
- **Items with no price/ABID:** near the end of each flyer there may be a page with 4–5 products (image + name) but no prices/ABIDs — **do not box these.**
- **Recipe pages:** box and tag as a **link** using the URL at the bottom of the page.
- **Liquor mail-in rebate prices:** rebate price (red box) → Current Price with postfix **"Final Cost"**; original price (yellow box) → Original Price; rebate → Sale Story; fine print → Disclaimer.
- **Red arrows:** items with a Sale Tag or Bonus Buy Savings red arrow → put **"Y"** in the **Sales Tag** field.
- **Disclaimer (NEW):** for items with specific valid dates, tag the "Rest of week $$$/lb." text in the **Disclaimer** field. A standard price-update disclaimer applies to **all** items via Style Guide rules (should auto-apply; add manually if missing).
- **Valid dates:** watch for 1-day and 3-day sales — tag item valid dates even if identical to flyer-level dates.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include sign-up page and special weblinks**; exclude coupons, packaged deals, retailer logo, social media.
  - **Sign-up pages:** one box each; Display Type = Link, Name = "Email Sign-up" → Martin's `martinsfoods.com/sign-up`, Giant Carlisle `giantfoodstores.com/sign-up`.
  - **Savory/Recipe items:** Display Type = Link, Name as on page → Martin's `recipecenter.martinsfoods.com`, Giant Carlisle `recipecenter.giantfoodstores.com`.
  - **Peapod banners:** Display Type = Link, Name = "Peapod" → the Peapod OpCo URLs per banner.
  - Regular items: box each individual item with a price (text boxes when needed). Multi-items with no item-specific detail: box as one.
- **Tag / Tag QC (Low; Auto-tag ON for Martin's, OFF for Giant Carlisle; PDF Image Auto Selection OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** Brand box-specific. URLs — see below.
  - **Line Items:** items with no image, or clean-but-dark/grey background, or text-only → tag normally, select a cutout, put **"Y"** in the **Line Item** field.
  - **Ad Block ID:** tag the seven-digit code under each item description in the **Ad Block ID** field where present; leave blank if none.
  - **Description:** do NOT tag the number under the description; do NOT tag "Rest of the Week $$$/lb." in description (goes in Disclaimer).
  - **Sale Story:** do NOT tag "Bonus Buy Savings"; do NOT tag Gas Rewards or cents-off sale stories (dollars-off can be included).
  - **⚠️ Categories:** use ONLY the 15-item list (Baby, Bread & Bakery, Beverages, Adult Beverages, Dairy, Deli & Prepared Food, Floral & Garden, Frozen, Grocery, Laundry/Paper/Cleaning, Meat, Health & Beauty, Pet Store, Produce, Seafood). **ALL alcoholic beverages → "Adult Beverages"** (risk item).
- **Image QC:** single-image box → select only if clean PDF (white bg, not cut off), else "Do not Use PDF Images" + Line Item "Y". Multi-image box → image of first item listed in the tag (fall back to next, or first left-to-right). **⚠️ Avoid grey-background images — use the cutout instead.**

## URL updates (Flex)

- Item Search → URL Is blank → multi-edit and apply the banner grid-view links:
  - **Martin's Foods:** `martinsfoods.com/savings/weekly-ad/grid-view`
  - **Giant Carlisle:** `giantfoodstores.com/savings/weekly-ad/grid-view/`
- Applying to 300–500+ items may time out — refresh and repeat until no results remain.

## Final QC / go-live notes (Flex)

- Ensure all Flex tracker tasks for GC and MF are complete before Thursday go-live.
- **Coupon page (C07):** all items tagged as **items, not coupons**; ensure item-level valid dates. Item Search → Item Type = Coupon → confirm none are mistagged.
- Search flyer for valid dates and apply where needed. Confirm all items have a URL (apply grid-view links if missing). Verify Ad Block IDs (missing ones truly have none).
- **Disclaimer:** Item Search → Disclaimer text is blank → should return **no results.**
- **Adult Beverages check:** find alcohol pages via Storefront spotcheck → note page grouping index → Item Search "Categories IS NOT Adult Beverages" on that page index → fix any alcohol items.

## Insert process (DOC, Wednesday)

- Inserts drop in AEM with an insert placement spreadsheet; retailer emails when dropped.
- **⚠️ RISK 1:** watch for pricing-zone-specific inserts (rare — seen Feb 2025).
- **⚠️ RISK 2:** confirm each insert PDF is a **single page** (multi-page PDFs break FAdmin).
- GC and MF share a pagination xlsx; inserts go in the same page position for both banners. In the "Insert" column, rename each to a **single word with no spaces** (used by BD reporting — crucial).
- Create an Optics ticket, attach the insert spreadsheet. **⚠️** Any post-go-live insert/URL changes: note in the ticket comments and attach the updated spreadsheet.
- After adding inserts, check vertical scroll for 3 PZs each (clickability + page positioning).

- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Giant Carlisle & Martin's Foods OneGuide (Google Doc `1w3auLK-JsRcPzRJgoAwPbIPdJ2-bFu6wGt3h5X3Yflw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
