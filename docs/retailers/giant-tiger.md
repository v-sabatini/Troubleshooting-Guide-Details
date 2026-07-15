# Giant Tiger — Processing Guide

> **Source:** Giant Tiger OneGuide (Google Doc `1_X0Lg4V0mBJfkosLVvbpr51v8GNVNWl2lHSIHvlQAEQ`). Contacts/credentials omitted.

Tier 1 Premium bilingual (EN/FR) retailer. Codesheet + store-set upload, a Shopify URL-pull step, a logo-appending custom action, and Tuesday link revisions.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#gianttiger` |
| Hosted URL | gianttiger.com |
| Flyer types | Weekly (1 type) |
| Processing | Auto-stack; no Flex; no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday. Upload by Tuesday (Wednesday latest).
- **Cadence:** Available Tuesday, Valid Wednesday → Tuesday. **Preview: Friday before** (set preview to Friday even though preview is not until Monday).
- **Setup owned by** FLEX; Image QC by Flex; FQC by DOC/FLEX.
- **Custom Action:** Giant Tiger Logo Appending (appends logo1/logo2 to page-1 items of the grocery and core pages; runs any point in FQC).

## Upload & setup

- Retailer emails when files land on FTP. Search FTP for `xlsx` → download **codesheet, run list, and SKU file**.
- **Store Set Upload:** in the Run List, rename Column A (Store_Dealer → Merchant Store Code) and Column B (Format → Store_Set_Name); save as CSV. On the Store Sets page → **Clear All Store Sets** → upload the Runlist CSV. **⚠️ Click Upload ONCE** — clicking twice uploads the store sets twice.
- **Codesheet manipulations:** unhide/delete column A; delete everything below the codesheet info (from Code Legend down); in the pink **Language** row, change language-location to just language:
  - French-Quebec → French · Bilingual-Quebec → English · Bilingual-Ontario → French · Bilingual-Atlantic → French · English-Ontario/Atlantic/West → English · Bilingual-West → French
  - Unusual zones: use the VIP_Email page (`VIP_Email_EN` → English, `VIP_Email_FR` → French).
  - Delete superfluous tabs. **Delete the VIP_Email row** (upload the EN/FR VIP pages manually after the codesheet runs). Save as CSV.
- **Banner Links file:** from the ORIGINAL codesheet, delete everything above the Digital Insert URLs section, save as `Week_BannerLinks.xlsx`.
- **Weekly URL document:** copy the SKU file's Grocery tab into the SGHG tab; use the **GiantTigerShopify Pull Product URLs** google sheet (clear WEEK MAPPING, paste SKU data, run "Populate URLs"), download WEEK MAPPING as CSV → `Week_URLs.csv`.
- **Upload with codesheet:** Codesheet tab → upload codesheet.csv → paste FTP path into **PDF Base Directory** (**do not include the last slash or anything after it**) → Save → Process.
- **Add VIP pages manually** after the codesheet runs (French toggle for the FR page); add to all pricing zones per language via Pages → Layout → "Put In". Mark Flyer Creation complete.

### ⚠️ Common errors / risk items
- **Price check items over $100** — scan the flyer and verify prices.
- **Flyer sorting:** weekly ad always first, then lookbooks.
- **Codesheet upload errors:**
  - **"cannot find file":** name/format/spacing in the codesheet must exactly match the FTP (watch for stray spaces).
  - **"pages previously uploaded":** check the naming convention reflects the correct week; clarify files with the retailer. (Also expected/ignorable at overview.)
  - **"NIL":** re-check all codesheet revisions and cell placement.
- Pre-setup: clear FTP; mass-attach Banner Links + URL (WEEK MAPPING) docs to all vendor tasks; no external run name; add theme if applicable.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box OFF, Box QC bot ON):** include sign-up page, social media, special weblinks; exclude coupons, packaged deals, retailer logo.
  - Sign-up page: box **top and bottom in two separate boxes** (per Banner Links doc, consistent WoW). Special weblinks: box ad-match and claw-back areas (per Banner Links doc).
  - **⚠️ Do NOT box individual SKUs as standalone items** — they should be a **text box linked to the product's photo, or not boxed at all.**
- **Tag / Tag QC (Low; linking doc required; Auto-tag OFF):** include name, pre/postfix, valid dates, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. Brand box-specific.
  - **Brand** in the new Brand field. **Description:** put all SKUs here if multiple; do NOT enter package info; enter the description next to the item.
  - **SKUs & URLs:** reference the attached URL document — use the correct-language URL.
  - **Price:** as on flyer; **if a range, use the higher price.** Shoes get postfix "pair".
  - **Banner Links doc:** use the English-column URL for English pages and French-column URL for French pages.
- **Image QC:** clean PDF images, cutouts OK if none available.

## Final QC / post-processing

- **Item Category QC (Flex):** QC Categories → search "clothing" → verify women's/men's/kids classification (open the page for context).
- **Banner Links QC (Vendor):** cross-reference each Banner Links page's links against the doc; correct any wrong ones.
- **Links/SKU QC (Vendor):** Item Search — SKU blank (Item type Item), URL blank (search EN then FR), and URL contains `/p/` → mass-edit to the correct base URL:
  - **EN:** `gianttiger.com` · **FR:** `gianttiger.com/fr/`
- **Ad-hoc QC (Vendor):** QC prices over $100; Sessions → "Mark items in-store only"; **⚠️ NEW — remove stores 431, 436, 446** (custom action "Remove Stores", all zones); run the **Logo Appending** custom action; set Tracking Codes (`FW##_W##` — note GT's fiscal year differs from ours).
- **Final QC (Flex):** geography should not change; "pages previously uploaded" always shows (ignore); Standard 4 thumbnails (start at logo); dates match PDF; flyer sorting weekly-ad first, lookbook after.
- **Flyer Review type: Lite.**

## Out-of-processing

- **Tuesday link revisions:** the retailer emails link revisions for the Wednesday-valid flyer. Although technically live, TTMs are hidden during the preview day — complete revisions by EOD Tuesday. Swap boxes in Box QC for items needing link swaps; update any new links per email; note completion in run comments.

---
*Source: Giant Tiger OneGuide (Google Doc `1_X0Lg4V0mBJfkosLVvbpr51v8GNVNWl2lHSIHvlQAEQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
