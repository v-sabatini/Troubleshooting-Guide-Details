# Food Giant and banners — Processing Guide

> **Source:** Food Giant OneGuide (Google Doc `19sS7g3I4gWUKCYmbUheDz978PhZxk4fo_REsTYrCSfY`), updated Mar 13, 2026. Contacts/credentials omitted.

Food Giant is a regional US grocer with **9 banners** under it → 10 Fadmin merchants total, all sharing the same retailer contact:
**Food Giant, Piggly Wiggly - FG, Cashsaver, Mad Butcher, Big Star, Sav-Mor, Save Mart Supermarkets, Pic N Sav, Ripley's Market, Market Place - FG.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flexflyerreview` |
| Hosted URL | foodgiant.com/weekly-ad/ |
| Flyer types | Weekly (per banner) |
| Processing | Auto-stack; DOC (Upload + FQC); Flyer Review by Flex; no coupons; no Feedel |

## Merchant / flyer-type IDs
- **Food Giant:** merchant 3140 — Weekly Ad 11938; **Weekly 12011** (destination for clones)
- **Big Star\*:** 6757 — Weekly Ad 11982
- **Mad Butcher\*:** 6719 — Weekly Ad 11981
- **Piggly Wiggly - FG\*:** 4584 — Weekly Ad 11954
- **Ripley's Market\*:** 6758 — Weekly Ad 11983 (check FTP for files first; only create shell + upload if files present)
- **Sav-Mor\*:** 6762 — Weekly Ad 11990
- **Save Mart Supermarkets\*:** 6763 — Weekly Ad 11991
- **Cashsaver\*:** 6720 — Weekly Ad 11980
- **Pic N Sav:** Weekly Ad 12128
- **Market Place - FG\*:** Weekly Ad 12133

\* = the 8 banners that must be **cloned** into the Food Giant merchant.

## Files & schedule
- **Files arrive:** Tuesday. Retailer emails to say PDFs are uploaded and attaches the codesheet (their "breakdown file").
- **Cadence:** Available From Tuesday; Valid From Tuesday → Valid To Wednesday. (For all banners, **Available From = one day before Valid From**.)
- **All banners now have a 1-day preview.** No External Run Name.
- Sometimes files arrive late; hold firm on 5 business days lead time externally.

## Upload & setup (owned by DOC)

**Codesheet upload** (most banners — light editing of the retailer's Excel):
- Open the retailer's "breakdown file" (contains Food Giant + all banners); copy store info from the "new store" column into the [Food Giant banners codesheet]; paste pagination into the matching tabs; download each as CSV.
- Upload to the matching flyer run: **all codesheet toggles checked except the 2nd and last**; **config name `generic`**; use that week's FTP file path; Process.
- **Codesheet shows yellow** → usually mismatched file names; confirm codesheet names exactly match the FTP; fix names in the codesheet and re-upload.
- File genuinely missing in FTP → flag to coordinator/lead to source from retailer; re-run once present.
- Mark flyer creation complete; wait for sessions; do setup QC.

**Manual upload** (single-store banners): **Big Star, Sav-Mor, Save Mart Supermarkets, Market Place - FG, Ripley's Market.**
- Pages > Edit > open correct folder > select all > Auto-Group (ensure pages in sequence per file-name page number) > Save & Complete > Flyer Creation > create base PZ > add stores > check geography > Setup QC.

### Setup QC (owned by DOC)
- Confirm all pages uploaded (PZ tab → Items View; **RISK:** confirm no un-uploaded SFTP pages).
- Confirm flyer dates (usually top of first page).
- Thumbnails: 4 Standard.
- **Edit Details: set Weekly Ad flyer type to Hidden in Hosted only** — only for Piggly Wiggly - FG, Cashsaver, Mad Butcher, Big Star, Sav-Mor, Save Mart Supermarkets, Market Place - FG, Ripley's Market.
- Complete Setup QC.

## ⚠️ Common errors / risk items
- **Codesheet organization:** ensure codesheets are organized correctly by banner.
- **PDF not found on codesheet upload:** most likely a misnamed file — check the FTP and rename in the codesheet, or contact the retailer if unsure.
- **Cloning (biggest risk):** when cloning, select the **"Weekly"** flyer type — **DO NOT select "Weekly Ad".**

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** box each item. **Exclude** coupons, packaged deals, retailer logo, banners, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON):** Brand tag/QC specific. Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price; **exclude SKU and URLs.**
- **Image QC:** select cutout image — **do not use PDF images.**
- **Spotchecks:** standard pricing spotchecks.

## FQC / cloning (owned by Flex)
- FQC all banners on standard steps; check dates and banner name on PDF page 1 vs Fadmin.
- Confirm all pages assigned to the correct Merchant; Available From = one day before Valid From.
- 4 standard thumbnails; mark Autostack Spotcheck complete; confirm geography matches last week; check vertical preview interactivity; check all Page 1s for item valid dates (assign if OS missed any).
- **Set Weekly Ad flyer type to Hidden in Hosted only** for the 8 asterisked banners.
- **Cloning:** clone the 8 banners (Big Star, Cashsaver, Mad Butcher, Piggly Wiggly - FG, Ripley's Market, Sav-Mor, Save Mart Supermarkets, Market Place - FG) into the **Weekly** flyer type (12011) of the Food Giant merchant (3140). **Do NOT clone Food Giant or Pic N Sav.**
  - Ad Hoc Processing > Clone > uncheck default destination > check "Clone to Food Giant" and select **Weekly** flyer type. New Flyer Run Name = "Banner name - Valid start date" (e.g. `Big Star - Jan 15`).
  - Set clone **Hidden in Flipp** (Hide in… "All Flipfully Apps"). Once clone sessions finish, FQC the clone; for the two page-level tasks write "N/A".
  - Add stores to clones manually or via the generic stores codesheet tab.
- Complete FQC checklist (Save → refresh → Save and Confirm).
- **Availability:** Weekly Ad flyer type = Hidden in Hosted only; Weekly flyer type (clones) = Hidden in Distribution and Flipp only.

## Flyer review
- **Type: Medium.** Owned by Flex. Especially check geography for clones and availability toggles.

---
*Source: Food Giant and banners OneGuide (Google Doc `19sS7g3I4gWUKCYmbUheDz978PhZxk4fo_REsTYrCSfY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
