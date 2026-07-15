# Royal Ahold (Giant Food, Food Lion, Giant Carlisle, Martin's Foods, Stop & Shop) — Processing Guide

> **Source:** Royal Ahold OneGuide (Google Doc `1_QakDsRnIaJxYVckQgnHHolXDvpAr4ICQYfk0s4bU3w`), Giant Carlisle/Martin's Foods section updated Feb 10, 2026. Contacts/credentials omitted.

> **Scope:** One OneGuide covering the Royal Ahold / Ahold Delhaize banners: **Giant Carlisle, Martin's Foods, Stop & Shop, Giant Landover, Hannaford, and Food Lion.** Processing rules are largely shared across banners with per-banner differences noted below.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#3fl-royal-ahold`, `ahold-delhaize`, `ahold-ops` |
| Hosted URLs | giantfoodstores.com · stopandshop.com · giantfood.com · martinsfoods.com · foodlion.com · hannaford.com |
| Flyer types | Giant Carlisle: Weekly Circular (6405) · Martin's Foods: Weekly Circular (5541) · Stop & Shop, Giant Landover, Food Lion, Hannaford weekly circulars |
| Processing | Trim Stack / Slice / Auto Stack (varies by banner); Flex (Flyer Review / 3FL); Strategic Ops involved (Feedel); coupons processed by OS for Stop & Shop group |
| Resource | Royal Aholds Flex Processing Tracker (shared with Flex weekly) |

## Files & schedule (per banner)

- **Giant Carlisle / Martin's Foods:** files Tuesday; Available From Wed, Valid From Thu, Available To Mon, Valid To Tue; preview Monday; **Slice**; coupons processed by OS.
- **Hannaford:** files Monday; Available From Mon, Valid From Tue, Available/Valid To Mon/Tue; preview Monday; **Trim Stack**; OS Setup; no coupons.
- **Food Lion:** files Monday; Available From Tue, Valid From Wed, Available/Valid To Tue; preview Monday; **Auto Stack**; OS Setup; no coupons.
- **Workflow (all):** Upload & Setup → Image QC (FLEX, 2 days out) → FQC (DOC, 1 day out).

## Upload & setup

### Giant Carlisle (GC) & Martin's Foods (MF) — owned by DOC
- **Transfer files (Tuesday):** in AEM → The Giant Company (GC) → Marketing → Weekly Ad → Weekly Circular → current week → Final Files → download the **Final PDFs** folder (unzip).
  - Verify **Flipp Digital Pages** folder has the C07 pages with **no barcodes**.
  - **⚠️ RISK:** delete the **Page 07** folder entirely — it has the same pages but **with barcodes** on items. Only the Flipp Digital Pages (barcode-free) should be uploaded.
  - Upload to the FTP (pages are very high-res and slow to transfer).
- **⚠️ BIGGEST RISK — pixel height:** in Edit details, **change the height to 4096 pixels BEFORE any pages enter the page pool.** This ENG fix renders Royal Ahold's high-quality pages legibly; if pages are uploaded first, they won't render at 4096. Pre-set this if going on vacation.
- **Codesheets** built from two files: the **Ad Version Sheet** (store distro + PZ codesheet) and the **Recapper** (pages codesheet — **use the "For Flipp" recapper**, not the other one).
  - Ad Version Sheet: trim headers to Store #, Ad Version, Giant, Martin's; rename Store # → "Store Numbers", Ad Version → "Zone" (column A), add a "TBD" column; delete blue-highlighted rows (Flipp doesn't show those); duplicate the tab into GC and MF; filter each banner's "X" column to isolate its stores; download each as CSV.
  - Recapper: Version row starts on row 5; set row 1 "Account:", row 2 "Created:", row 3 "Sales Date:"; copy PZs into the reference column; match PZs to stores from the Ad Version sheet; remove duplicates; delete blank rows; save GC and MF CSVs.
- **Edit details:** Preview Date Monday before go-live; External Run Name "Weekly Ad"; No theme; **4096 pixel height**.
- **Codesheet uploads:**
  - Stores: attach the GC/MF Ad Version sheet, **Config `giant_landover_stores`**, PDF Base Directory `/`, **Toggles 1 & 4**.
  - Pages: attach the GC/MF Recapper, **Config `giant_landover_pages`**, PDF Base Directory from FTP (before the pages folder), **Toggles 3, 5, 6**. Should run green for Carlisle. **⚠️ RISK:** if Carlisle is uploaded first, the Martin's recapper runs yellow ("pages re-uploaded" — usually "HB"/"AD" repeat pages, safe to ignore) → **Force processing** for Martin's.
- Flyer creation → wait ~30 min for sessions (high-res pages). QC thumbnails (Standard 4, stretch across page 1 only). Check valid dates and that GC pages are in the GC run / MF pages in the MF run. Add both runs to the Flex Processing Tracker.

### Food Lion — owned by FLEX
- Download from AEM: Manifest (Flipp folder), Items, Store List, PDFs → upload all to SFTP; save Manifest and Store List as CSV.
- Upload Manifest: Name "Codesheet", **Config `food_lion`**.
- Upload Stores (**only after all pages uploaded**): Name "stores", **Config `food_lion_stores`**, PDF Base Directory `/`, **only the first (store-set assignment) toggle**.

### Hannaford / Stop & Shop / Giant Landover
- Owned by FLEX/DOC; setup steps not fully detailed in the OneGuide.

## ⚠️ Common errors / risk items (retailer-specific)

- **GC/MF end-of-flyer page:** 4–5 products with image + name but **no price/ABID** — **do NOT box these.**
- **Recipe / Savory pages:** box and tag as a **link** using the URL at the bottom of the page (recipecenter.[banner].com).
- **Liquor mail-in rebate:** price in the red box → Current Price with postfix "Final Cost"; price in the yellow box → Original Price; the rebate → Sale Story; fine print → Disclaimer.
- **Coupon type:** OS often mistakenly tags items as coupons. On the C07 coupon page, ensure everything is tagged as **Item, not Coupon**, and all C07 products have item-level valid dates.
- **Red arrows / Sales Tag (NEW):** items with a Sale Tag or Bonus Buy Savings red arrow → put "Y" in the **Sales Tag** field.
- **Disclaimer (NEW, all banners):** items with specific valid dates → tag the "Rest of week $$$/lb." text in the **Disclaimer** field (not description). Add the banner-specific customer-service disclaimer AFTER any existing disclaimer (Giant Landover 1-888-469-4426; Stop & Shop 1-800-767-7772; GC & Martin's 1-888-814-4268 — auto-applied via Style Guide for GC/MF).
- **Valid dates:** watch for 1-day and 3-day sales — tag valid dates even if they match the flyer-level dates.
- **Line Items:** an item with no image / grey-dark background / text-only = a Line Item. Tag normally, select a cutout, and put "Y" in the **Line Item** field with "Do not use PDF images" selected (keeps it off the hosted grid/carousel).
- **Inserts (GC/MF):** ⚠️ ensure each insert PDF is a single page (multi-page PDFs break Fadmin); watch for rare pricing-zone-specific inserts.
- **Hannaford live-date availability:** flyers with "FLIPP" in the name (e.g. "Week 19 FLIPP") are **hidden on Hosted** — do NOT flag as missing from Hosted. Flyers without "FLIPP" are on Hosted — DO flag if missing.

## QC specifics

### Box Draw
- **GC/MF/Stop & Shop/Giant Landover:** Low complexity. Auto-Box ON for Martin's & Giant Carlisle, OFF for Stop & Shop & Giant Landover; Box QC bot OFF. **Exclude** coupons, packaged deals, retailer logo, social media; **Include** sign-up page, special weblinks.
- **Hannaford / Food Lion:** Low complexity, Auto-Box ON, Box QC bot ON; **Include** retailer logo, sign-up page, social media, special weblinks; **Exclude** coupons, packaged deals.
- Draw a box around each individual priced item (text boxes when needed). Multi-items in one ad block with no item-specific details → box as one. Each banner's sign-up page → one box.
- **Multiple-item rules:** for GC/Martin's/Giant Landover, "Buy X Get Y Free" call-outs → box/tag each item individually. For **Stop & Shop** specifically, "Buy Two Packages and Get [items] FREE" → box/tag the main offer AND each attached free item.
- **Food Lion:** "Buy One & Get These" → box separately; 2+ items at one price with separate descriptions → box separately (one description → may stay as one box); double-price boxes (e.g. 2/$7 + 2/$6) → box both with the product; banners → do NOT box.

### Tag / Tag QC (Low complexity)
- Auto-tag: ON for Martin's & Stop & Shop and Food Lion; OFF for Giant Carlisle & Giant Landover. Linking doc: not required for Stop & Shop group; required for Hannaford and Food Lion.
- Name/Brand as in flyer; description as in flyer (**do not** tag the number under the description, or the "Rest of week $$$/lb." text — that goes in Disclaimer). **No SKU** for the Stop & Shop group (SKU included for Hannaford/Food Lion).
- **Sale Story:** as in flyer; do NOT tag "Bonus Buy Savings", Gas Rewards, or cents-off (dollars-off is OK).
- **Item Categories (Stop & Shop group)** — use ONLY: Baby, Bread & Bakery, Beverages, Adult Beverages, Dairy, Deli & Prepared Food, Floral & Garden, Frozen, Grocery, Laundry/Paper & Cleaning, Meat, Health & Beauty, Pet Store, Produce, Seafood.
- **Ad Block ID:** tag the seven-digit code under each item description where present (leave blank if none). **Food Lion** uses the item linking document's "Ad Module Code" (Column H, per AdRun/pricing zone in Column E) → enter under Ad Block ID.
- **Coupons (Stop & Shop group):**
  - **Digital Coupons (yellow flag, call-to-action):** Display Type Item; prefix/postfix/sale story as in flyer (include "$$ off ## WITH DIGITAL COUPON"); **Coupon Matchup = Y** whenever there is a yellow coupon badge. Enter "Digital Coupon" as part of the postfix.
  - **In-flyer Coupons (dotted-line border):** Display Type Item; tag fields as in flyer; **Coupon Matchup left blank**.
- **URLs (Stop & Shop group):** most items do NOT need a URL. Sign-up pages, Savory/Recipe call-outs (recipecenter.[banner].com), and Peapod banners get banner-specific URLs.

### Image QC (all banners)
- One image in the box → select it **only if a clean PDF** (white background, not cut off); else "Do not Use PDF Images" + "Y" in Line Item.
- Multiple images → select the first item listed in the tag; if not clean, next item; single tag with multiple images → first image left-to-right.
- **⚠️ RISK:** avoid grey-background images — select the cutout instead. Always prefer the packaged item over a plated/lifestyle shot.

## Post-processing / FQC

- **URL updates (all banners, FLEX-owned):** Item Search → URL IS blank → apply filter → multi-edit items → apply the correct banner grid-view link:
  - Stop & Shop: stopandshop.com/savings/weekly-ad/grid-view
  - Hannaford: hannaford.com/locations (with flipp UTM)
  - Giant Landover: giantfood.com/savings/weekly-ad/grid-view
  - Martin's Foods: martinsfoods.com/savings/weekly-ad/grid-view
  - Giant Carlisle: giantfoodstores.com/savings/weekly-ad/grid-view/
  - Food Lion: foodlion.com
  - (Refresh and re-run if the bulk edit errors on 300–500+ items.)
- **GC/MF FQC:** verify C07 all Items not Coupons + item-level valid dates; item search Coupon type (nothing should be a coupon); Line Item "Y" check (no clean PDF exists); Sales Tag "Y" check; Ad Block ID check; URL check; disclaimer auto-applied. Complete FQC checklist, then add inserts (from AEM Digital Insert folder + xlsx pagination): set "Page Position", shorten each insert name to a single identifiable word (BD reporting), add to the position for both GC and MF, create an OPTICS ticket with the insert spreadsheet attached, then check vertical scroll for 3 PZs.
- **Food Lion FQC:** add inserts; staggered dates — change "available" and "valid from" from 12am to 1am for PZs ZKBG, ZKNA, ZKNV, ZTNA, ZTNV; NativeX uses ZNRH PZ; standard thumbnails; geo.

## Flyer review
- **Flyer Review type: Lite** (owned by FLEX) across banners.

---
*Source: Royal Ahold OneGuide (Google Doc `1_QakDsRnIaJxYVckQgnHHolXDvpAr4ICQYfk0s4bU3w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
