# Dollar General — Processing Guide

> **Source:** Dollar General OneGuide (Google Doc `1jlb9IxDTPQoqr-54KfMrOWQMjdUH9JF9PGFOZ7LxaZE`), updated Jul 8, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#dollargeneral`, `#dollargeneral-sep` |
| Hosted URL | dollargeneral.com/deals/weekly-ads |
| Flyer types | Weekly Ad (224) · Market Ad (245, **no longer receiving**) · Private Brands · Wireless/Ad-Hoc (3303) |
| Processing | Auto-stack; processor-owned; no Flex; no coupons; no Feedel |

## Files & schedule
- **Files received:** ad-hoc, **1+ month lead time on PDFs**; **links received the week before launch.**
- **Publication:** Available/Valid From Sunday → To Saturday.
- **Preview:** 2-day internal preview (Thursday) **if links are received by 1 PM EST the Tuesday before launch.** Thursday evening/Friday = rev pages & corrections.
- **Retailer regularly has 20K+ stores assigned weekly.**
- Linking document: Yes.

## ⚠️ Common errors / risk items (retailer-specific)
- **Revised codesheet after original upload:** given the volume, a re-sent codesheet with updated distribution must be uploaded into a **net-new run** — there's no clean way to update the existing run.
- **File delivery is split:** not all weekly pages arrive together; missing creative usually comes the **Friday before launch** (DG's email marks it "Creative Pending"). Doesn't block upload but requires codesheet manipulation.
- **Flyer sort order** (OS does weekly live checks): **1. Weekly, 2. Market, 3. Private Label, 4. Wireless Deals.**
- **Version-specific pages/inserts → blank spaces on the codesheet** for some stores. FAdmin auto-fills those gaps with other pages (likely Page 1) — **these must be removed during FQC.**
- **Valid dates:** every item on DG Deals pages must have its individual valid dates.
- **Maximum % Merge must ALWAYS be 0%** (Merchant Page → Workflow tab) so Disruptor pages aren't merged on the front end.

## Upload & setup (owned by Processor)

### Weekly (Flyer type 224)
- In the SFTP filter "Hide Uploaded?" or search XLS; download the weekly **Store Version sheet** (the Version Indicator isn't needed).
- **Inserts** (columns G onward, e.g. Delivery, Tax — 1–4, possibly none): add a column between Version Name and the first insert, and build a formula, e.g. `=F2 & IF(H2="X"," Delivery","")` (repeat per insert: `... & IF(I2="X"," Tax","")`). This appends the insert name to the pricing-zone name wherever an "X" is present.
- Copy the new column → **paste values only** over the Version Name column (Column F) → rename Column F **"Media Version"** → delete the helper formula/columns.
- **Blank columns are version-specific pages** — OK for now, but FAdmin will auto-populate them (remove in FQC).
- Delete columns for pages not yet delivered ("Creative Pending"); **if you delete columns, renumber Page # in Row 1 in order.** Save as CSV.
- **Upload:** flyer run → codesheet → Name **Base**, Config **`dollar_general`**, base path from FTP, toggles = everything except 2nd and last → Process. Takes ~10 min (may briefly say FROZEN — wait). **Wait for green before marking Flyer Creation complete.** If red, check pages are in the FTP and names match.
- Attach circular links to all vendors (files may be uploaded before links arrive). Mark Setup QC complete; Preview Start date = Thursday before launch.

### Wireless / Ad-Hoc (Flyer type 3303)
- Create shell → manual upload (**file names vary — often no folder, named for the following month, e.g. `TVB_POP_APRIL`**) → one pricing zone "Base", add all stores (adds in the background). No linking doc. Thumbnails Standard 4. Mark items in-store only; run **'set cutout image'** custom action. External run name "Wireless Deals". **Hosted only; mark Secondary Publication.**

### Private Brands
- Create shell → **change pixel height to 4096 px before upload** (Edit Details → rarely-used fields). Internal run name "DG Private Brands [month]". Manual upload.
- Download **VI_SKUs** xls; keep only the "Skus and Links" tab, save as the linking document. Usually 1–2 pages per zone.
- **Two zones: Base** (all stores **minus** the 'Toy Blue' store set) and **Blue** (**only** the 'Toy Blue' store set). Attach linking doc; external name "Switch to Save with DG Brands"; available everywhere. May need a deeplink post-FQC.

### Market Ad (245 — no longer receiving)
- Codesheet: download DG store list + DGM version; cell A5 "Media Version", delete rows 1–4; filter by green and delete green rows; delete columns J–Z; replace missing Fronts/Backs with the Base page; match date format to FTP file names; save CSV. Upload with Config **`dollar_general_market`**, unmark 2nd and last toggle. 2 pages per zone; no linking doc. Available time 3 AM; external run name "Dollar General Market Ad"; mark items in-store only.

## Box Draw (Medium — Auto-Box ON, Box QC bot OFF; linking-doc required)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box all items attached to the price; include as much of the image as possible; **multiple items with one price → one box.**

## Tag / Tag QC (Medium; Auto-tag ON; linking-doc required)
- **Include:** name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs, valid dates. Brand used for Box/Tag.
- **`Dollars Off` must ALWAYS be BLANK** no matter what.
- **Valid dates — IMPORTANT:** any item with valid dates different from the flyer's must be tagged individually.
- Fresh Produce insert page → box and link to `dollargeneral.com/fresh-produce`.
- **Pricing patterns:**
  - **# FOR # deals:** "Buy #, Get # FREE" → Sale Story; regular price → Current Price; Postfix "Reg." + "ea.".
  - **# FOR $ deals:** Postfix "SALE # for"; Postfix Amount = 2; Current Price = 8; Postfix `*`.
  - **BOGO:** goes in Sale Story (translated to "BUY # GET % OFF"); regular price → Current Price.
  - **$ - $ = $ deals:** Current Price reflects the yellow/black-outlined text; Prefix "X for$"; Sale Story = the savings amount above the yellow text (e.g. "- $1 with dg digital coupon when you buy 2").
  - **[NEW 6/19/2026] $1 EVERYDAY deals:** any "$1 EVERYDAY" callout **must** be tagged with an **"EVERYDAY" prefix.**

## FQC (owned by Processor)
### Weekly
- **Remove Page 1 from extra positions:** Pages → Layout → find the versioned Page 1 (not Base) → Take Out → All Flyer → deselect only the zones that have it in position 1 → OK → submit and let sessions complete.
- **Staggered dates / Mass Edit by region:** EST 12 AM — VA, NC, FL, SC · **CST 1 AM — TN, AL, TX, MS** · **PST 3 AM — CANV**.
- External run name added; Disruptor links added; **remove all Dollars Off** (via item export/import if many: Item Search → Dollars Off Is Not [blank] → export → blank the column → re-import).
- Check 1st/2nd page item valid dates (weekend/x-day sale banners). Thumbnails Standard 4 — **draw only Page 1** (Pg 1 and Pg 2 have mismatched dimensions). Check flyer order.
- Add tracking URLs (DoubleClick impression + open links, provided by PT). Run **'set cutout images'** custom action.
- **[NEW] $1 EVERYDAY prefix:** Item Search `Current Price is $1` + `Pre-fix is [blank]` → update any results to add "Everyday" prefix.
- Ensure preview date set; complete FQC; send preview + final store count **Thursday by 1 PM** (EOD latest).

### Market / Private Brands / Wireless
- Confirm dates + external run name + Standard 4 thumbnails + flyer order for each. Market: available 3 AM / valid 12 AM, items in-store only. Wireless: hide on Flipp network, Secondary publication. Private Brands: available everywhere, Blue zone = 'Toy Blue' store set, Base zone = all minus 'Toy Blue'.

## Troubleshooting
- **Codesheet errors:** ensure "version" is renamed to "Media Version"; check file names for missing leading zeros (`02.02` vs `2.02`). Market: remove extra bottom rows; replace non-listed page-1 versions with the base page.
- **FQC:** 2nd page too wide for thumbnails → keep thumbnail on Page 1 (retailer is fine with this). Disruptor links not saving → uncheck "mark items in-store only", add links, re-mark in-store only.
- **Post-launch revisions:** always file a ticket / notify the processor; validate slicing on new pages. **Page-order changes are high risk** (CuSat with merged-appearing pages during syncing) — perform the change, re-run page stitching, and republish to minimize sync time.

## Flyer Review — **type: Medium** (owned by Reviewer)
- Major risk items: external run name present; item-level valid dates; flyer sort order (Weekly newest first, Market, Private Label); **Maximum % Merge = 0%**; staggered dates/times by region; Geography (Weekly may change WOW — confirm codesheet is green; all other publications match previous weeks).

## Out-of-processing
- Black Friday comms doc provided (2025).

---
*Source: Dollar General OneGuide (Google Doc `1jlb9IxDTPQoqr-54KfMrOWQMjdUH9JF9PGFOZ7LxaZE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
