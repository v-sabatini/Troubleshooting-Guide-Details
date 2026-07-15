# Safeway Canada, Sobeys West, Sobeys Ontario & Sobeys Atlantic — Processing Guide

> **Source:** Safeway Canada / Sobeys OneGuide (Google Doc `1FaE9uwvdrTb4ehSxRXGC0ZmfAMOHf-MpMro_hMJNVis`), updated Oct 20, 2025. Contacts/credentials omitted.

> **Scope:** One OneGuide covering four banners — **Safeway Canada, Sobeys West, Sobeys Ontario, Sobeys Atlantic.** Upload/setup differs per banner (below); OS pipeline processing and post-processing QC are shared across all banners.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium (S1C1) |
| Availability | All platforms |
| Slack channels | `#sobeys`, `#sobeysops`, `#3fl-sobeys`, `#sobeys-dataservices` |
| Hosted URLs | Safeway Canada: safeway.ca/flyer · Sobeys: sobeys.com/en/flyer |
| Publications | Safeway Canada Weekly Flyer; Sobeys Weekly Flyer — West / Ontario / Atlantic |
| Processing | Auto-stack; Flex (3FL — Pre-FQC image/category QC, Mondays); no coupons; Strategic Ops involved (Feedel / retailer data services) |
| Key trackers | Sobeys Insert Tracker · Sobeys 3fl Weekly Tracker · Rachelle Bery (RB) Store List |

## Files & schedule (all banners: files Wed, preview Mon, live Wed)

- **Safeway Canada:** Available From Wed 3:00AM, Valid From Wed, Available To Thu 3:00AM, Valid To Tue.
- **Sobeys West:** Available From Wed 3:00AM, Valid From Wed, Available To Thu 3:00AM, Valid To Tue.
- **Sobeys Ontario:** Available From Wed, Valid From Wed, Available To Thu, Valid To Tue.
- **Sobeys Atlantic:** Available From Wed 6:00AM, Valid From Wed, Available To Thu, Valid To Tue 10:59PM.
- **Workflow:** Upload & Setup (DOC, Wed) → 3FL Pre-FQC (FLEX, Mon: Image QC & Category QC) → Inserts / Image QC / Category QC / Scene+ / Page Categories / Compliments / SJC Links / Deep Links / Custom Tiles / FQC (DOC, Tue) → Live (Wed).

## Upload & setup (owned by DOC) — per banner

**Common to all banners:** files arrive in an SFTP subfolder; download the PDF codesheet and the store distribution file. Manipulate the codesheet, save as CSV, upload. Then build a generic store codesheet from the distribution file's Digital tab, save as CSV, upload. Edit Details: Preview Date Monday before go-live, available everywhere, external run name "Weekly eFlyer mm/dd - mm/dd", no theme. Thumbnails Standard 4 + Thumbnail 400W. Merge skinny "flap" pages (FL01 → merge into FL02 so pages are side-by-side). Attach the week's Embedded Links doc (`SobeysWkxx_Embedded Flyer Links.xlsx` — shared by all banners) to all vendor tasks via Mass Attachment on "Vendor Box QC". Set all vendor tasks to Urgent. Check `#sobeys` Slack for special campaigns (may need Urgent Processing Tickets to hit data-service deadlines).

- **Safeway Canada:** files in `/SOBEYS WEST/`. Codesheet: **DELETE "Sobeys" zones, KEEP ON and BC zones** (those are Safeway-only); rename Safeway zones to letter+number (AB1, SK1, ON1, BC1, etc.); change DIGITAL/FLAP01/FLAP02 → FLYER; move P01 above FL01; delete hidden columns; clear rows 2–5. Stores from the `[GROCERY Digital]` tab (paste top-down in the same order as the codesheet left-to-right).
- **Sobeys West:** files in `/WEST/`. Codesheet: **DELETE ON and BC zones (Safeway-only), DELETE "Safeway" zones**; keep/rename Sobeys zones (AB1, SK1, MB1, etc.). Same DIGITAL/FLYER, P01, hidden-column steps. Stores from `[GROCERY Digital]` tab.
- **Sobeys Ontario:** files in `/ONTARIO/`. Codesheet: rename zones to Zone# (Zone 1, Zone 1B, Zone 2); cut/paste the Bilingual zone so all zones are in one row and delete extra bilingual cells. Stores from `[Digital]` tab (**Zone 1A = Zone 1**).
- **Sobeys Atlantic:** files in `/ATLANTIC/`. Codesheet: rename zones to Zone#; cut/paste Bilingual zone into one row. Stores from `[Digital]` tab, zones renamed to match Fadmin.
- **Highlighted rows** in a codesheet → the Store Code needs updating in Fadmin (Stores/Sets → change old code to new, e.g. St. Anne's 5302 → 4048).

## ⚠️ Common errors / risk items (retailer-specific)

- **Rachelle Bery (RB) pages** are store-specific: let the codesheet pull them in (OS still boxes/tags), but **remove them from all pricing zones during Setup QC** and note the position — they get re-added to their own store-specific pricing zones during the Inserts process.
- **Scene+ items:** Sale Story must read "*xxx* **Scene+** PTS when you buy x" (**no space** between "Scene" and "+"); add the **[Scene+]** category (the only case where an item has 2 categories).
- **Scene+ Member Pricing items:** Prefix "Scene+ Member Pricing" (don't forget the "+"); Disclaimer "$xx without Scene+ Card"; category [Scene+].
- **Verified items:** must have "Verified" in the prefix (e.g. "Verified" or "Verified Scene+ Member Pricing").
- **HOT PRICE items:** Prefix "HOT PRICE" and delete "HOT PRICE" from the Sale Story.
- **Compliments items:** "Compliments" in the Brand field AND "COMPLIMENTS" (caps) at the start of the Name field; French name goes in Description, not Name.
- **Item SKUs (NEW Dec 1 2025):** if there are NO SKUs on the PDF, tag the items as one item block (as usual) — **do NOT flag to OS.** One SKU per item; delete extra SKUs Fadmin pulled in; if multiple, search sobeys.com / safeway.com to match SKU to item.
- **SJC Links / Deep Links / Embedded Links / Custom Tiles:** check the week's entries in the Sobeys Insert Tracker / Slack and box/tag; ensure the Embedded Links doc is attached to vendor tasks.

## QC specifics

### Box Draw (Low complexity; Auto-Box ON, Box QC bot OFF)
- No linking document required. **Exclude** coupons and retailer logo; **Include** social media.
- Item block with 1 item → one item box over image and text. Item block with 2+ items → **stack the Text Boxes on top of one another**.
- Box social media links (Digital Exclusive, App Store, Google Play) and Embedded Links CTAs (Learn More, Order Online, Recipe).

### Tag / Tag QC (Low complexity; Auto-tag ON — Tag Lite)
- No linking document. Include brand, name, pre/postfix, valid dates, description, SKU (new Dec 2025), price, sale story, categories, disclaimer, original price, URLs, image selection (PDF preferred, new Apr 2025).
- **Brand:** always include; for Compliments items include "COMPLIMENTS" in both brand and name. **Name:** as-is, brand NOT in name (exception: Compliments). French name → Description.
- **Pre/Postfix:** use the drop-down, match the PDF. Price-per-weight → `/lb` in postfix, `$$$/kg` in Description. Scene+ / Verified / HOT PRICE prefixes as above.
- **Valid dates:** only include if they differ from the flyer run dates.
- **Categories:** based on page headings; one per item, plus [Scene+] where applicable (Category and Category Highlights should match). Detailed category guide: Meat (raw/ground, no boxed/plant-based meats), Produce, Seafood (fresh/frozen, no canned/boxed), Deli, Bakery, Grocery, Dairy, Floral, Home, Baby & Pet Care, Pharmacy, Baby, Health & Beauty, Beverages (no instant coffee), Scene+.
- **URLs:** Digital Exclusive (Safeway: safeway.ca/mobile-app; Sobeys: sobeys.com/en/promotions/mobile), App Store, Google Play (Foodland app), plus Embedded Links CTAs (use Sobeys vs Safeway URLs correctly).

### Image QC (completed during Tag/Tag QC; also FLEX/3FL on Mondays)
- **Rule of thumb: pick the cleanest image.** If no clean PDF image, choose the cutout / "Do not use PDF images". Multiple options → the image best matching the product name.
- **Do NOT use PDF images** for lifestyle shots (products on a cutting board/plate) or images with too many shadows / black outlines.

## Post-processing QC (all banners)

- **Inserts (DOC):** find inserts in the Sobeys Insert Tracker (correct banner tab); RB pages via the RB Store List. Conditional-formatting formula to highlight store-specific inserts: `=COUNTIF($B$1:$C$1000, B1)>1`. (Process is video-documented — too complex to write out.)
- **Item Image QC / Category QC / Page Category QC (FLEX — 3FL, Mondays):** verify via the Sobeys 3fl Weekly Tracker. Categories one per item + Scene+ where applicable. Page categories: none on page 1, use as many as visible, include [Scene+] on predominantly-Scene+ pages.
- **Scene+ Points QC (DOC):** Item Search Sale Story contains "PTS" (must read "xxx Scene+ PTS when you buy x"); add [Scene+] category to any items with Scene+ callouts missing it (export/import if many); Scene+ Member Pricing items → Prefix "Scene+ Member Price", Disclaimer "xx without Scene+ Card", category [Scene+].
- **Compliments QC (DOC):** Item Search Brand contains "compliments" → ensure "compliments" in Name; Brand is-not "compliments" + Name contains "compliments" → add "Compliments" to Brand (export/import if many).
- **Verified QC (DOC):** Page Grouping Index 1 + Prefix is-not "Verified" → ensure Verified items have Prefix "Verified".
- **HOT PRICE QC (DOC):** Sale Story contains "hot price" → set Prefix "Hot Price" and delete "HOT PRICE" from the Sale Story.
- **Embedded / SJC / Deep Links (DOC):** tag CTAs from the Embedded Links doc (correct Sobeys vs Safeway URLs); box/tag SJC Links and Deep Links per the week's Sobeys Insert Tracker tabs (Deep Links: red weeks = none).
- **Custom Tiles (DOC):** check `#Sobeys` Slack; apply via QC Thumbnails → Storefront Premium & Storefront Carousel Premium → Override Thumbnail on the right zones. Store-specific → duplicate pricing zones ("AB1 - Custom Tile") and move the store; FSA-specific → duplicate zones + Assign/Remove FSAs custom actions. Date-specific tiles → Create Trigger (remove manually — no removal trigger) and file an OPTICS ticket.

## FQC / go-live (owned by DOC)
- **⚠️ NEW (Apr 28 2026) Safeway Canada ONLY:** after post-FQC steps, **clone the Safeway Canada AB/MB/SK ad into the Safeway Canada ON/BC ad.** From the AB/MB/SK version remove stores and delete PZs containing BC/ON (incl. BC1/BC2/ON1/ON2); from the ON/BC version remove stores and delete PZs containing AB/MB/SK. Re-run tile generation and page stitching, and complete FQC for the cloned ad.
- Basic checks: geography, vertical preview, then the pipeline FQC checklist.

## Flyer review
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Safeway Canada / Sobeys OneGuide (Google Doc `1FaE9uwvdrTb4ehSxRXGC0ZmfAMOHf-MpMro_hMJNVis`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
