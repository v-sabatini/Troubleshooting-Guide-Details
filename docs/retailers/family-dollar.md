# Family Dollar — Processing Guide

> **Source:** Family Dollar OneGuide (Google Doc `1HuK6ihBgNqys7xjB4w9ihberVDvJvClhnDjkcy_OazY`), updated Oct 4, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium (S2C1) |
| Availability | All platforms |
| Slack channels | `#familydollar`, `#familydollar-dollartree-offapp`, `#familydollar-dollartree-ampproduction` |
| Hosted URL | familydollar.com |
| Flyer types | **Current Ad (Weekly)** · **Grand Opening Specials** · **Digital Book** · **AT&T/Tracfone** |
| Processing | Auto-stack |
| Who's involved | DOC processes (Flex N/A); OS (Setup); no coupons; Strategic Ops — yes, Feedel/retailer data services |

## ⚠️ Recurring risk items
- **Image QC:** select PDF images — no cutouts unless there are no clean PDFs.
- **Smart Coupon tagging (*NEW Nov 2024*):** a Smart Coupon attachment provides SKU, URL, and Coupon ID; find the item by page/name/description and tag all three.
- **Flyer sorting:** order must be **Weekly Ad, Digital Book, Grand Openings, Other.**
- **Page categories:** ALL pages must have ONE category (including page 1).
- **FSA generation:** ensure FSAs are generated for each PZ; update store zip codes and re-run FSA generation in Session.

---

## Current Ad (Weekly)

### Files & schedule
- **Files received:** Tuesday. **Coupon ID doc arrives Wed EOD** → process overnight, FQC Thursday.
- **Cadence:** Available/Valid From Saturday; Available To Sunday, Valid To Saturday. Preview date = Wednesday before go-live.

### Upload & setup (owned by DOC)
- The files email includes/points to a codesheet (check FTP if not attached).
- Open codesheet: **delete the "ABD#" row; delete the page 4 (SC coupon) column** and note its position in comments (position for the weekly insert). Save as CSV.
- Codesheet upload: **Config `family_dollar_weekly`**, FTP path from the file, **toggles 3, 4, 5, 6 ON.** Save & process.
- Check stale — version matrix sits in stale; mark as uploaded. Confirm PDF dates vs. run dates. Thumbnails **Standard 4.** Set preview day = Wednesday before go-live. Stores are typically assigned in FQC (if Digital PZ only, assign All Stores).
- **Attach the Smart Coupons doc to all vendor tasks; file an urgent processing ticket** for overnight processing.

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF; no linking doc)
- **Include** coupons, Smart Coupon, social media, special weblinks. **Exclude** packaged deals, retailer logo.
- **All items and banners must be boxed.** Box each item with an individual price.
- **All banner callouts** get boxed/tagged with the URL on the PDF; if none, use `https://www.familydollar.com` (scan QR codes where present).

### Tag / Tag QC (Low; Auto-tag OFF; no linking doc)
- Include name, pre/postfix, valid dates, description, **SKU, URL (*NEW Nov 2024*)**, price, sale story, categories, disclaimer, original price, **Coupon ID (*NEW Nov 2024*)**. Brand is box-draw specific.
- **Brand:** only if a single-brand item; leave blank for multiple brands.
- **Name:** as on the flyer; for multi-product items include ALL info; put a period after amounts (ea. lb. ct. pk. oz. ft.).
- **Description** (each item on a new line):
  - Singular product → add the specs (e.g. `8.6 oz.`). Soda → include `**§`.
  - Smart Coupon "Price x/$x" → add `Reg. Price x/$x`. Smart Coupon "Sale! x/$x" → add `Sale! x/$x`.
  - **Reg. Price ranges go in the Description, NOT the Original Price field** (which can't hold ranges).
  - "also valid on…" → add to description, do NOT add the postfix.
- **SKU / URL / Coupon ID:** from the Smart Coupons attachment, matched by page/name/description.
- **Prefix:** as on flyer; ensure "Sale!" keeps its exclamation mark.
- **Current Price:** as on flyer; blank if none (often a "Get More! Buy x Get x FREE" postfix instead).
- **Postfix — add the biggest sale callout here:**
  - `with $x off Smart Coupon†` — "with" lowercase, add "off" after the price, include the SC amount, must have †; add `*` only if it's an MFR offer.
  - `$x OFF with Smart Coupon†`; `Get More! Buy x Get x`.
- **Original Price:** single value only; if it says "Reg. Price", put it in the Description instead.
- **Sale Story:** only if the Postfix is already occupied.
- **Disclaimer order:** Must Buy x / Limit x → PDF disclaimers → "Pet selection varies by store." → exclusions/availability + `†See Smart Coupons for details and participating products.` → `*MFR Offer.` → `**+CA CRV where applicable.` → `§Prices not valid in Philadelphia, PA.`
  - **⚠️ No space between `†` and `See`.** "participating" always lowercase. `*MFR` needs its asterisk.
- **Item Valid From/To:** only when different from the flyer dates.

### Image QC
- Requires image extraction. **Select clean PDFs; no partial/unclear images.** Ideally no cutouts.

### FQC (owned by DOC)
1. **Add stores:** copy the Store List Vendor sheet; keep Store + State; Find & Replace states to match the PZ names in Fadmin (the Ad PZ is the non-beer standard zone). Rename headings FD Store # → `stores`, Circular Version → `pricing zone`; save CSV. Upload as **gen stores codesheet, Config `generic_stores`, base path `/`, toggle 1.** Run.
2. **Page Categories:** ALL pages need exactly ONE category (incl. page 1).
3. **Item Search cleanup** (extensive): delete `|` brands; ensure periods after ea/oz/lb/ct/pk; move sale callouts (save/off/buy) into the Postfix; move "Reg. Price" into the Description; "Smart Coupon" two words with capital S/C; ensure `†See Smart Coupons…` in disclaimer where price contains `†`; verify `*MFR Offer`, `§`/CA CRV disclaimers, etc.
4. **Links QC:** social-media banners boxed/tagged (Google Play & App Store links); Smart Coupon on all page 1s boxed/tagged as ITEM type from the SC attachment.
5. **SC Digital Insert Page:** four versions (phone, hispanic, caucasian, AA) rotate weekly — check last week, use the next. Insert via Pages → Edit → Forever; place in all PZs at the codesheet position; tag with the Smart Coupons URL.
6. **Banner Links QC:** every banner/URL callout/ad space must have a Link-type URL (PDF URL, QR scan, or default familydollar.com).
7. **Coupon ID QC:** export items with URL not blank; conditional-format duplicate URLs against the Coupon ID attachment to catch untagged items; repeat for Coupon ID and SKU.
8. **Tracking codes:** Manage Tracking Codes → add Dynamic Variables `utm_source=flipp` and `utm_medium=eflyer`; Apply All; comment "tracking codes applied".
9. Complete FQC checklist; send preview URL Thursday; make corrections.

### Combo Stores (owned by DOC)
- Clone the weekly to the combo shell (share the FRID with BD in `#familydollar`); add the same tracking codes. Remove all stores from the combo run, then rebuild store assignment from the combo store sheet (rename leftover PZs to "Ad"). Remove those stores from the weekly run (max 200 at a time). **FSA Dedupe** the two runs with the combo run as first priority. Check Geo for both; FQC the combo run.

---

## Grand Opening Specials
- **Files:** Friday (bi-weekly). Available From Thursday, Valid From Saturday; Available To Thursday, Valid To Saturday. Preview = Wednesday before go-live.
- Create the shell in the **Grand Opening Specials** flyer type; External Run Name `Grand Opening!`.
- Box Draw Low / Auto-Box OFF; Tag Low / Auto-tag OFF.
- **Deep links:** a Grand Opening Store List email arrives a few days after files; use it to build the store list.

## Digital Book
- **Files/cadence:** on schedule. Available on all platforms. Auto-stack.
- Manually upload the digital-book pages.
- Box Draw Low / Auto-Box OFF; Tag Low / Auto-tag OFF.

## AT&T/Tracfone
- **Files:** monthly, on schedule. Available on all platforms. Auto-stack.
- Create the shell in the **AT&T/Tracfone** flyer type.
- Box Draw Low / Auto-Box OFF; Tag Low / Auto-tag OFF.

---

## Flyer sorting check (owned by Flex)
- On the Merchant page, confirm flyer sorting = **"Flyer Type Newest First"**; if not, flag the DOC/DOL via Slack.
- Order: Weekly Digital Insert → LookBooks → GO (grand openings) → Mobile Ads. Sign off in the Family Dollar Weekly Flyer Sorting Checklist.

## Flyer Review
- **Type: Lite** (owned by DOL).

## Out-of-processing
- **Tracking codes** and **Thursday preview URLs** as above (contacts and templates in the OneGuide — not stored here).
- **Pre-live corrections (Fridays):** apply corrections from the retailer's document; refer to Tag/Tag QC for tagging questions.

---
*Source: Family Dollar OneGuide (Google Doc `1HuK6ihBgNqys7xjB4w9ihberVDvJvClhnDjkcy_OazY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
