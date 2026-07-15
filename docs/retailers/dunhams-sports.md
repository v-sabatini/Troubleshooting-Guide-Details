# Dunham's Sports — Processing Guide

> **Source:** Dunham's Sports OneGuide (Google Doc `12-ka51gSSdn435BG6_3112Y1ENmfoQ5StydTDi4SK7o`), updated Jun 12, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (Weekly) |
| Slack channel(s) | `#dunhams`, `#flex-processingsupport` |
| Hosted URL | dunhamssports.com |
| Flyer type(s) & cadence | **Weekly** (198) · **Monthly Digital Guide** (9637) · **Weekly Coupon** (9638) |
| Processing | Auto-stack; no coupons processing (coupon flyer type is separate); no Feedel |

## Files & schedule (Weekly)

- **When files arrive:** Wednesday. Available From Friday · Valid From Saturday · Available To Thursday · Valid To Thursday.

## Upload & setup

**Weekly (198):**
1. Get the generic codesheet (added to the Setup QC Files folder), save as CSV.
2. Codesheet upload tab → Details → config **`generic`** → **select tabs 1, 3, 4 and 6** → get Green Status.
   - **If a store error:** click directly on the Stores cells; if store numbers lack commas between them that causes the error — leave one store, delete the rest, then manually add them back.
3. Check the FTP for any remaining files; upload the rest manually if needed. Confirm pricing zones, pages and store count match the codesheet.
4. **⚠️ IMPORTANT: no cover page in the first position of any Pricing Zone** even if listed in the codesheet — cover pages go first only in clone versions. Mark Flyer Creation complete.
- **Setup QC:** External run name = "Weekly Ad"; **no theme**; date = 2 days before valid; run **Trim Boxing** (Overview → Ad Hoc → Update trim boxing) after sessions:
  - **Bottom cut:** Left 0, Bottom **90**, Right [1st Tbox value], Top [2nd Tbox value].
  - **Top cut:** Left 0, Bottom 0, Right [1st Tbox value], Top [2nd Tbox value **− 90**] (e.g. 837 → 747).
- Legibility heights **40–30**. Confirm cover page position vs. the retailer email (reorder if not positions 1–2; codesheet always places them at the start). Thumbnails 21212, **1065x800** — **don't include guns** (exception: a couple of guns not filling the page is OK).

**Monthly Digital Guide (9637):** manually upload the **broken-out pages** (not the full PDF), Auto-Group, confirm page order (P0001, P0002…). Create **base** pricing zone, add all stores unless email specifies (then do a generic store upload). Legibility **40–30**. Download the Linking Sheet (.xlsx) from SFTP and mass-attach to vendor tasks (if none, check the FAdmin comment — no URL doc may be required). Edit Details: hide in Distribution and Flipp; no theme; preview date 1 day before go-live.

**Weekly Coupon (9638) — two ads:**
- **Friday Only:** clone previous week's coupon; available Friday 12:00am–11:59pm; hosted only; external "Coupon"; entire page = one box; thumbnails "thumbnail"; mark in-store only. One run for Friday with all stores (**stores with no ads do NOT get the Friday Only Coupon**).
- **No Ad Store Coupon:** clone; available Saturday 12:00am–Thursday 11:59pm (while the weekly ad is valid for all other stores); hosted only; external "Coupon"; add stores per the No Ad Coupon generic-stores codesheet; thumbnails "thumbnail"; mark in-store only; leg heights **40–35**.

### ⚠️ Common errors / risk items (retailer-specific)

- **Image QC:** watch for **incorrect item pictures** — wrong-item photos sometimes get auto-selected; use the cutout showing the correct item.
- **Firearms / content policy:** if guns appear on page 1 or 2 the Weekly fails content policy → **clone**: original flyer shell = **Hosted only**, clone = **Flipp only** (with cover page in position 1, thumbnails redrawn). Complete FQC for both.
- **No cover page** in the first position of any pricing zone (weekly) except clones.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** Linking doc: **No** for Weekly, **Yes** for Digital Guide. Box all items with prices/sale stories; **product blocks with secondary pricing must be boxed separately.** **Include** sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals, retailer logo.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON).** Linking doc: No (Weekly) / Yes (Guide). Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.** Brand handled via Box Draw/Box QC.
- **Image QC:** single item → PDF image if clean/clear; **multiple items (>1 product) → do NOT use PDF** even if clean; **firearms → always Do Not Use PDF Image.**

## Post-processing / Final QC

- **URL/Links QC (DOC, Guides only):** item search URL IS ___; cross-reference the linking doc for items missing links.
- **SKU QC (DOC, Weekly only):** from the Dunham's Sports Links Sharing Document, add each SKU to the corresponding page's first item; click Save twice. Find the flyer run ID in the document tabs.
- **FQC:** spotcheck + autostack complete; draw 4 standard thumbnails; **Guides only — set every item's Display Type to Link, not Item.** FAdmin Slice (full page; edit slice if wording left top/bottom, but never cut items). Image QC (PDF preferred, watch for wrong images). Page categories (hunting for guns; no category on first/cover pages; max 4/page). Mark Items Store Only; leg heights **40–30**. Check external run name (Weekly = "Weekly Ad"; Guides per email). Geography per codesheet (missing stores may be coupon-only). Horizontal/vertical QC; no theme.
- **Flyer sorting:** Weekly first, then one-pager/guides in order of date (newest guide first) via Flyer Type New First.
- **Guides only:** after FQC, send preview link and direct link.

## Flyer review

- **Flyer Review type: Simple** (owned by FLEX). Weekly ads with firearms-heavy first two pages launch as two flyers (one with a sign-up page cover, one Hosted-only clone without it).

## Out-of-processing

- Trim boxing update via Overview → Ad Hoc → Update trim boxing (same Bottom/Top parameters as setup).

---
*Source: Dunham's Sports OneGuide (Google Doc `12-ka51gSSdn435BG6_3112Y1ENmfoQ5StydTDi4SK7o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
