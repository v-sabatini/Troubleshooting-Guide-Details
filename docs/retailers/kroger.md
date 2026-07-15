# Kroger — Processing Guide

> **Source:** Kroger OneGuide (Google Doc `1vMpgwKQXwOGb4w3AOvlxT84QVEBib0zC_oPnftF_xw4`). Contacts/credentials omitted.
> **Large, complex Tier 1 Premium account** with many banners and 8+ flyer types.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · **Tier 1 Premium** |
| Availability | Most flyer types all platforms; some Hosted-only (see per-type notes). **Kroger does NOT use the Flipp hosted iframe.** |
| Slack channels | `#kops` (FT Kroger ops), `#kroger` (full team), `#3fl-kroger` (Flex processing), `#flex-processingsupport` |
| Hosted URL | n/a (no Flipp hosted iframe) |
| Processing | Auto-stack (Ocado = Trim Stack); no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **Unique Shift Type 3FL**; DOC + FLEX split across the multi-day workflow |
| Flyer types | Weekly Ad · Weekly Ad [F4L 704 / Foods Co 704 / Mariano's 531] · Bi-Weekly [Ruler Foods 090] · Weekly Ad [Ocado] · Marketplace · Gen Merch · Ship to Home · Ad Hoc Content · Adult Beverage · (Discontinued: New Releases) |

## Account-wide risk items

- **Flyer sorting:** set Flyer Type **Newest First** for all weekly flyers (Flipp no longer powers Kroger's hosted).
- **Item valid dates — "2 Day Sale":** 2-day-sale items (often boxed on the first page TB01, e.g. "2 DAY SALE" callout) need **unique valid dates** matching the days on the page. **The item directly above the "2 DAY SALE" banner also needs those valid dates.**
- **B#G# / Final Cost deals:** any B#G# deal ("BUY # GET # FREE of Equal or Lesser Value With Card") **must** have a Sale Story; an accompanying limit ("LIMIT # TOTAL WITH CARD") goes in the disclaimer. Any **"FINAL COST" / "FINAL PRICE"** callout must be added to the Sale Story.
- **Boxing/pages appear off after reordering:** if pages are reordered via a second codesheet, some system tasks must be re-run manually or boxes/pages render incorrectly. After forced processing finishes, **re-run Page Tile Generation** (per track) — this cascades Flyer Tile Gen, Low Res PDF Gen, PDF Text Extraction, Flyer Thumbnail Gen. If pages still look off, re-run **Page Stitching**.

## Custom action — FSA Swap (Weekly Ad)

During FQC, if a pricing zone has 0 FSAs and 1 store: identify the store(s), find the zip (Merchant page > stores/store sets), then run the **FSA Swap** custom action with Flyer run ID, Pricing Zone ID FROM (find current zone via Ctrl+F in Geography), Pricing Zone ID TO, and the list of FSAs (store zip).

---

## Flyer type 1 — Weekly Ad

**Merchants:** all Kroger banners **except** Ruler Foods 090, Food 4 Less 704, Foods Co 704, Mariano's 531, Ocado.

- **Files:** sent on different days per banner (see "Asset Drop Date"). Multi-day workflow (files 9→5 days out; Image/Category QC; FQC 1 day out).
- **Cadence:** Available Tuesday, Valid Wednesday–Tuesday; preview Tuesday. Linking document: Yes.

**Upload & setup (DOC):**
- Confirm receipt of the **Jenkins email** (search "Jenkins", reply-all confirming). Identify the codesheet (search "xls" in the banner's STALE).
- **Codesheet manipulations** (3 kinds): (1) Standard — delete heading row, blacked-out rows, and the last two total rows; reorder per the latest posting plan / ENT doc. (2) IA05 & special pages — break out unique per-store pages into their own pricing zones. (3) Separating shared codesheets for divisions that share one file: **615** (Dillons/Bakers/Gerbes — Gerbes = 100s store #s, Bakers = 300s, Dillons = the rest), **024** (Louisville "LV…"/JayC "JC…"), **021** (Central/Pay Less = zone CEAND only), **531** (Metro Market = zone RS3SP only / Pick N Save), **620** (City Market = 400s store #s / King Soopers). A **Kroger Codesheet Manipulation Tool** (Colab) automates all three (single-user — toggle "currently in use").
- **Codesheet upload: config `kroger`**, PDF Base Directory from STALE, **toggles: all but the second.** For split shared codesheets, process simultaneously to avoid shared-file errors. After processing, check STALE and manually upload any missed pages (Boost inserts, credit-card pages, "IABoost", etc.). Mark Flyer Creation complete.
- **Thumbnails (5):** the standard 4 (Thumbnail 1065x800, Stock_premium, Storefront_carusel_premium, Storefront_carusel_organic) **plus first_page_thumbnail_400w**. Exception: if page 2 is a wide/short banner insert, draw the 1065x800 and Storefront_carusel_premium over page 1 only. Typically No Theme.

**QC:**
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **include** Retailer Logo (front cover always boxed) and **"Shop Now" callouts**; also box Retailer Offers. Boxes drawn over each item's text + image (no text boxes). Multiple items sharing a sale story → box each separately (box around name, text box around image). Exclude coupons and packaged deals.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
  - **Retailer Offer** (top-right of BD01/TB01): tag as a **Link** to the banner's own site (each banner has its own domain, e.g. ralphs.com, kingsoopers.com, frysfood.com — see OneGuide list). Change display type Item → **Link**.
  - **Fuel Points on Page 1:** tag with the banner-specific `…/pr/fuel-event?cid=dm.pro.weeklyad_ENTAd` link (list in OneGuide; Ruler/F4L not applicable). Fuel banners **not** on page 1: use the link shown on the PDF.
  - Also tag Bakery/Deli, Boost, Gift Card, Military/Senior discount, Cocinalatina banners with the link shown on the banner.
- **Image QC (Vendor):** clean PDF images; use cutout if the PDF is cut off / has an odd background.

---

## Flyer type — Weekly Ad [Food 4 Less 704, Foods Co 704, Mariano's 531]

- Same account-wide risk items. **Config `kroger`** for all. **Toggles to check:** Store or Store Set Assignment, Page Upload, Allow pricing zone creation, Use Page Pool, Tile Generate afterwards; copy PDF base directory from FTP. **Do not add stores to pricing zones after the codesheet runs.**
- **Food 4 Less 704** has two flyers in separate flyer types: California Weekly Ad (2951, use codesheet version **FL1HL** / prefix `F4LCA`) and Chicago Weekly Ad (9307, codesheet **F4LMW** = Midwest).
- **Foods Co 704** (Weekly Ad 2952) uses the F4LCA codesheet, keeping only the Foods Co versions (FL2… pages). **Mariano's 531** (Weekly Ad 3626) — delete the "Flipp Store #" column.
- F4L Cali and Foods Co share pages → a **yellow "already uploaded" codesheet warning is normal**; click Force Processing (it stays yellow).
- **IA16 / IA15 / IA99 alcohol-only pages:** until the posting plan is received, **assume they stay in the weekly ad**; the posting plan (Wed/Thu) determines whether a page is moved to the Adult Beverage flyer.
- Check Geography = "No Stores or FSAs/zips were added or removed!" (else flag). Set preview date to the Wednesday before go-live.
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — Bi-Weekly Ad [Ruler Foods 090]

- Setup owned by FLEX. **Box Draw:** Auto-Box ON. **Tag:** Auto-tag ON. Image QC / Category QC / FQC owned by FLEX.

## Flyer type — Weekly Ad [Ocado]  (Trim Stack)

- **Merchants:** Kroger Ocado FC03 (Groveland Clone), Kroger Atlanta 011 (Ocado Groveland, Birmingham), Kroger Dallas 035 (Ocado Oklahoma City). Files Tuesday; preview Wednesday.
- **Different live dates:** Groveland & Groveland-Cloned live Monday (must be FQC'd by Friday); Birmingham & Oklahoma City live Tuesday (FQC Mondays). Groveland Clone = **Hosted only**.
- **Risk:** build the Ocado-specific linking doc — add `&cid=dm.pro.weeklyad_ENTAd` to the end of all Deeplinks, share edit access with Flipp, attach to the Kroger Flex Team Tracker (Ocado section, column J). **Adjust FSAs during FQC** via the "Assign Fsas from Csv" custom action (4 Ocado flyers).
- **Box Draw:** Auto-Box **OFF**. **Tag:** Auto-tag **OFF**.

## Flyer type — Marketplace

- **Merchants:** most Kroger banners (Dillons 615, Fry's 660, King Soopers 620, Kroger Atlanta/Central/Cincinnati/Columbus/Dallas/Delta/Houston/Louisville/Michigan/MidAtlantic/Nashville, Smith's 706). Files Monday; Available Tuesday, Valid Tuesday–Tuesday.
- **Setup: config `kroger_mp`**, PDF base directory from FTP, **toggles all but the second**; Save & Run codesheet; mark Flyer Creation complete. **Do not add stores to pricing zones after the codesheet runs.**
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **OFF**.

## Flyer type — Gen Merch Ads

- **Merchants:** Smith's 706, Fred Meyer 701. Files Wednesday; Available Tuesday, Valid Wednesday–Tuesday.
- **Setup (FLEX): config `kroger`**, path from FTP, **check all toggles except the second and last**. Manipulations: delete top row + bottom two rows; save as CSV. Note: Smith's codesheet now comes with Fred Meyer's — for the Smith's upload remove the Fred Meyer pricing zones (Smith's zones start **S**, Fred Meyer start **F**). Manual upload looks for the **SM_GEN** folder (not Smith's_MP).
- **⚠️ Risk — "Save ##%" deals:**
  - **Multi-item deal** (multiple items/categories under one "Save ##%", each with its own price or a price range): **one box**; item Name starts with the % promo text ("SAVE 40% With Card on …"); everything else in the description; no current price; tag Percent Off.
  - **Single item** with a "Save ##%" callout: Name is just the item/brand (NOT "save on…"); the "SAVE ##% With Card" goes in the **Sale Story**.
- **Box Draw:** Auto-Box **OFF**, Box QC bot **OFF**. **Tag:** Auto-tag **OFF**.

## Flyer type — Ship to Home

- **Merchants:** all Kroger banners except Kroger Ocado FC03 and Ruler Foods 090. Files Monday. **Availability: Hosted only.**
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — Ad Hoc Content

- Files Monday; all platforms. **Box Draw:** Auto-Box **ON**, Box QC bot **ON**. **Tag:** Auto-tag **OFF**.

## Flyer type — Adult Beverage Ad

- **Merchants:** Ralphs 703 (files Monday), Food 4 Less 704 (Friday), Foods Co 704 (Friday). All platforms.
- Receives the alcohol-only IA15/IA16/IA99 pages split off from the corresponding weekly ads (per posting plan).
- **Box Draw:** Auto-Box **ON**. **Tag:** Auto-tag **ON**.

## Flyer type — New Releases (marked Discontinued)

- Fred Meyer 701; Hosted only. Auto-Box OFF, Auto-tag OFF. **This flyer type is discontinued in the OneGuide.**

---
*Source: Kroger OneGuide (Google Doc `1vMpgwKQXwOGb4w3AOvlxT84QVEBib0zC_oPnftF_xw4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
