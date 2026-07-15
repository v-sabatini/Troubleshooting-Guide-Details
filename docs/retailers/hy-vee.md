# Hy-Vee — Processing Guide

> **Source:** Hy-Vee OneGuide (Google Doc `1pJzlGKZDUemnw5OTt66L23SDIYa9-1DRDdKe0yF0M8A`), updated Apr 30, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channel(s) | `#hyvee`, `#flex-processingsupport` |
| Hosted URL | hyvee.com |
| Flyer types | **DigDotCom** (Weekly Ad) · **Dollar Fresh** (Weekly) · **Special Sales** (all ad-hocs, e.g. 3 Day) |
| Processing | Auto-stack; Flex (Processing Support), flyer review owned by DOL; no OS beyond standard, no coupons processing, no Feedel/data services |

## Files & schedule

- **When files arrive:** DigDotCom & Dollar Fresh — Friday; Special Sales — Monday.
- **DigDotCom cadence:** 1 ad break, either Mon–Sun or Wed–Tue. **Available and Valid are always the same (no consumer preview);** dates may be staggered (some versions live Monday, some Wednesday). Preview date set to upcoming Wednesday so OS processes promptly.
- **Dollar Fresh cadence:** Available/Valid From Wednesday → To Tuesday.
- **Special Sales:** each ad-hoc goes live on different dates (3 Day Ads usually Fri–Sun).
- **Universal timing rule:** set **Available From and Valid From to 1 AM**; **Theme: No Theme**.

## Upload & setup

Codesheet upload for all three flyer types. **Config name: `hy_vee_pages`; check all toggles except Region Assignment.**

- From the FTP, search "xls" and hide uploaded; ignore any `RUNLIST` files. DigDotCom → the "Digital DotCom" xls; Dollar Fresh → the "Dollar Fresh" xls; Special Sales → any xls that is NOT a "Weekly Ad" (e.g. "special ad", "3 day", "1 day").
- **⚠️ Hy-Vee file names are case sensitive** — if the codesheet fails, it's usually a missing page, a typo, extra rows/columns, **or spaces when pasting names** (Fadmin errors on spaces). Flag issues to the DOC.
- **DigDotCom external run name: `Weekly Ad`.** Must attach the **Weblinks document** (from the same FTP folder) to all vendor tasks — **do NOT mark Setup QC if the Weblinks is not attached.**
- **Dollar Fresh:** pages usually 5–6 (first PZ may have one fewer page); external run name `Weekly Ad`; no linking doc.
- **Special Sales:** create the flyer run manually per xls/email; dates from the path name (Available/Valid From = start at 1 AM); internal run name e.g. `HV 3 DAY`; external run name = the front-page callout (e.g. "Bourbon & Beer Sale", "3 Day Sale"). Stores always differ — no need to flag.

## ⚠️ Common errors / risk items (retailer-specific)

- **Banners/callouts at the top of pages must be boxed & tagged** — accessibility requirement Hy-Vee flagged. Even if there's no price/promotion, box headers first, with all info.
- **"Try It" badge:** the red dates are part of the **Sale Story**, NOT the item's valid dates.
- **"Fuel Saver" badge:** the red text under the description is the **Sale Story**, NOT the postfix. (Fuel pages: tag as Item type, Name "Fuel Saver", spend/earn tiers in the description.)
- **"PERKS PRICING"** must be added to the postfix for all applicable items, followed by the non-member pricing.
- **Item-level valid dates** are easily missed — look for dates that apply only to a single item.
- **Cut-off pages:** pages with images only (no text) can be ignored/left un-boxed; the corresponding text page is tagged instead (system can't place the pages side-by-side for Vertical Scroll).
- **Weblinks/URLs (DigDotCom Weekly only):** tag only banners listed in the attached spreadsheet; tag as "Link" item type with the exact URL. Coupons with a link are tagged as an **Item** with the URL attached (not as a Link).

## QC specifics

- **Box Draw — Medium complexity. Auto-Box ON, Box QC bot OFF.** Box all items separately (text boxes when needed), **box all headers first**. **Include** coupons, packaged deals, sign-up page, special weblinks; **exclude** retailer logo, social media. Do NOT box CTAs that lead to other apps. Non-grocery items/banners boxed per the Weblinks spreadsheet (Weekly only).
- **Tag / Tag QC — Low complexity. Auto-tag OFF, PDF Image Auto-Selection ON.** Include brand, name, pre/postfix, valid dates (if different from flyer dates), description (include "Use in…" text in quotes), price, sale story, categories, disclaimer (page-level disclaimers applied to items), original price. **Exclude SKU;** URLs only per the attached weblinks. Tag coupons exactly as shown (cutout border, barcode in box).
- **Image QC:** select a clean PDF where possible; use cutouts for any bad PDF (artificial shadow, jagged lines, discoloration, black shadow, odd shapes, grey edges).

### Final QC (FQC) highlights

- **DigDotCom:** verify every weblink page/item is tagged Link (coupons-with-link tagged as Item); ensure all "click here" CTAs are boxed/tagged (else tag `https://www.hyvee.com/`); dates + 1 AM; sessions run; thumbnails; external run name "Weekly Ad". **Add tracking codes in order:** Source=flipp, Medium=cpc, Campaign=circular, Content=mmddyyyy (go-live date).
- **Dollar Fresh / Special Sales:** spotchecks clear; cover dates match run; 1 AM; Standard 4 thumbnails; sessions run. Special Sales: flag to DOC/DOL if fewer than 6 items (content policy); flyer sorting Weekly Ad → Event Sale → Monthlong → Specialty.

## Revisions / page swaps

- Hy-Vee sends an updated codesheet (file with `rev` in the name) highlighting revisions. Just run the new codesheet on the flyer run — it re-paginates automatically (no manual page swapping). Copy items to/from new pages for live flyers, or have OS process net-new pages pre-live. Notify DOC and DOL when done.

## Flyer review (owned by DOL)

- **Flyer Review type: Lite.**

---
*Source: Hy-Vee OneGuide (Google Doc `1pJzlGKZDUemnw5OTt66L23SDIYa9-1DRDdKe0yF0M8A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
