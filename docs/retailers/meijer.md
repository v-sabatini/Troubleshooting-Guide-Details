# Meijer — Processing Guide

> **Source:** Meijer OneGuide (Google Doc `1a0dT6vR1xS-lmVgsuA3W4UtsFbIAziCBzc6j9X537Ww`), updated Apr 30, 2026. Contacts/credentials omitted.

> High-complexity, DOC-heavy account with codesheet automation, a Deep Link workflow, and multiple flyer types. See also the Meijer Vendor Guide (Confluence VEN) and "All Things Meijer" working sheet.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium (merchant 2281) |
| Availability | All platforms (**we do NOT power the Meijer hosted**) |
| Slack channels | `#meijer`, `#meijer-scp` |
| Hosted URL | meijer.com/weeklyad.html |
| Flyer types | **Weekly Ad ("One Stop", 542)** · **Pullout (GM)** · **Two-Day Sale (Super Sale)** · **Guides** · **One-Pager (market-specific)** · **Market Format / MeijerDigitalAd** |
| Processing | Auto-stack; Flex N/A; **OS completes coupon processing** (Weekly); no Feedel |
| Tagging document | UPC `.xls` (SKU + Block IDs); Traffic/Placements `.xls` (URLs, Weekly only) |

### Flyer-type quick facts
- **Weekly Ad ("One Stop", `mm/dd`o01):** Avail Fri–Sat, Valid Sun–Sat (2-day preview). **Interstitial inserts** (C1, C2, V1, V2, V3…) are URL link-outs. Page trim 648×864.
- **Pullout (GM):** ad-hoc, ≥1/week, varying duration (dates on PDF), named "X-Pagination" (e.g., Graduation-Pagination). Page trim 648×864.
- **Two-Day Sale:** lives in "Super Sale" flyer type; 2-day sale with 1-day preview.
- **One-Pager (market-specific):** same cadence as Weekly; no page trimming.
- **Market Format / MeijerDigitalAd:** **Flipp only** (we don't power the Meijer hosted); `ALL_SALE_MeijerDigitalAd` is the only publication that does **not** need a linking document.

## Files & schedule (Weekly Ad)
- **Files received:** Tuesday. **Cadence:** Available From Tuesday → Available To Tuesday; Valid From Wednesday → Valid To Tuesday. Preview date Thursday before go-live. Linking document: Yes (Main Weekly only).
- **Pullout:** files Wednesday; Available Fri → Sat, Valid Sun → Sat (varying); preview Thursday.

## Upload & setup (owned by DOC)
- Confirm receipt by email; files in FTP. In the FTP, mark off all `csv` and `UPCGroceryServer` (search "grocery") files as uploaded; search "pagination" to identify unique flyer runs.
  - **⚠️ Repeat-week detection:** if a pagination folder ends in `_Wk2/_Wk3` etc. **and** the file's date does **not** match the highest-level folder date, it is a repeat from a prior week — **do not upload** (search the full basepath and mark all files uploaded). If the pagination file date **matches** the top folder date, it is new (upload).
- Organize files locally (copy template folder, rename to the week; subfolders for Pullouts, Pagination Docs, UPC Docs). **Combine all Weekly UPCs into a Master UPC** for OS tagging.
- **All Things Meijer sheet:** add a new row in the **[Deep Link Working Sheet]** tab for the week (dates, names, Flyer Run ID) — sets up sending Deep Links within ~24h. Create flyer shells and rows for each Pullout.
- **Weekly Google Doc (for the Optics ticket):** use the working template — **[Traffic]** (interstitial URLs → download XLS, attach to all tasks), **[Pagination]** (regular page order), **[Codesheet]** (page list built from pagination docs), **[Revisions]** (page swaps). Attach to the OPTICS ticket for the lead. A Colab automation notebook exists for codesheet creation.
- **Run codesheet:** Config **`meijer`**; **standard toggles (1,3,4,5,6)**; base path one level only (e.g., `/0330_Flipp5/`). Weekly only — after codesheet finishes, **manually upload interstitial pages (track 2)** (C1A, C1B, C2A, V1A, V2A, …).
- **Trim Boxes (after page tile gen, before flyer creation):** apply to **[All Pages] → Assign to All Pages** to kick off Tile Gen/sessions (QA before completing flyer creation so the system doesn't start Auto Box Draw). Dimensions: **Left 0, Bottom 0, Right 648, Top 708** (Weekly, Pullouts, Interstitials). Single stuck pages → nudge boxes 1 pixel.
- **[Traffic]:** from Hailey's "MM.DD Flipp Placements & Links" email — copy PDF name, Placement name, URL into the Traffic tab, download as XLS for OS. (No Pullout info — Pullouts don't get product links.)
- **Inserts:** interstitial pages inserted in **alphanumeric order at the end of all versions** (version "A" before "B").
- **Attachments:** attach the date-URLs XLS + Master UPC to **all tasks, all tracks** (mass-attach from Flyer Creation).
- **Overview:** Standard 4 thumbnails; **preview date = Thursday before go-live**; **external run name = "Weekly ad"** (Pullout = "Callout on page 1", all lowercase); no theme.
- **Setup QC:** standard; **clear stale (no pages remaining)**.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item with a price/sales story; box any product block with a "Shop Now" callout.
- **Tag / Tag QC (Medium; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price.
  - **SKU:** from the UPC XLS **column A** ("UPC") — applied to **track 1** pages (majority).
  - **Block ID:** from the UPC XLS **column M** — applied to track 1 pages (connects the item to the Meijer database — **high priority**).
  - **URLs:** from the Placements/Links XLS — applied **only to track 2** pages (C1, C2, V1, V2…).
  - Linking doc required for Tag/QC (except the `ALL_SALE_MeijerDigitalAd` publication).
  - **Sale Story order matters:** e.g., "BOGO 40% off of equal or lesser value" (not "…of equal or lesser value 40% off"); set Percent Off field.
  - **Images:** single-item block → clean PDF if available; **multi-item block → cutout**; lifestyle images → cutout. Avoid black/gray backgrounds.
- **Spotchecks:** standard pricing spotchecks in pipeline.

## ⚠️ Common errors / risk items
- **Tagging example — AirPods:** do **not** tag price as "3 for $249"; tag Name = Apple AirPods Pro 3, Price = $249.
- **Do not miss a UPC document** when building the Master UPC (would require re-running OS tag).
- **Repeat-week pagination files** (`_Wk2` etc. with a past date) must not be uploaded.
- **Trim boxes** must be applied to **all tracks** before flyer creation, or Auto Box Draw kicks off incorrectly.
- **Page swaps** from the retailer (Kurt) come in through the week — track them but **do not action until after SKU, Block ID, and Offer ID checks**.

## Post-processing / Pre-FQC (owned by DOC)
- **Page reduction** steps for the Weekly (from the Page Reduction email/document; note the affected store set).
- **Add interstitial inserts** (if not done at upload); QA URLs against the Traffic tab (check the URL ending terms).
- **Item searches (using the Master UPC):**
  - **SKU** IS blank / CONTAINS `+` (Item) → copy SKU from Master UPC column A (item-specific deep links, lower priority).
  - **Block ID** IS blank (Item) → copy Block ID from column M (**high priority**).
  - **Offer ID** IS NOT blank (Item) → check if an Offer ID is applicable; remove if not.
- **Offer ID Import (NEW 5/23, Weekly Ad):** pull an item report (after Block IDs fixed), use the OfferID Importer sheet (import Item Report + Master UPC as tabs, run Macros 1–3, remove blank/N/A id_2 rows, download ITEM IMPORT as CSV, run Item Import). GM Pullout uses a manual Offer ID process (filter Offer ID column, add via item search by SKU).
- **Page swaps:** execute the **[Revisions]** tab before go-live.
- **Tracking URLs:** promoted content (currently all ads) uses DoubleClick impression/open URLs (same WOW — no changes needed).
- **Preview links:** send no earlier than **3:30 PM Thursday**; copy the Hosted 2.0 URL into the Deep Link Working Sheet.
- **Flyer sorting:** **Flyer Type Oldest First** (old weekly, new weekly, pullouts, other) — periodically QA it hasn't reset.
- Update the **OPTICS** ticket for the lead (attach the weekly sheet).

## FQC / flyer review
- **FQC checklist** completed by DOC.
- **Flyer Review type: Medium** — Weekly owned by Vendor; Pullout owned by DOL (see the Meijer flyer review guides).

---
*Source: Meijer OneGuide (Google Doc `1a0dT6vR1xS-lmVgsuA3W4UtsFbIAziCBzc6j9X537Ww`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
