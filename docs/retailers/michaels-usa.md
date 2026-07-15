# Michaels USA — Processing Guide

> **Source:** Michaels USA OneGuide (Google Doc `1jhv9wccPLjEWSIWHQ2iXAoxMcokADt-iWuW6JBMS82g`), last updated Jun 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | **Flipp & Distribution only** |
| Slack channels | `#michaels`, `#flex-processing-support` |
| Hosted URL | We do not power their hosted |
| Flyer types & cadence | Flyer Type 1 — Weekly |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Related resource | Confluence: "Michaels USA + Canada Account Guide" |

## Files & schedule

- **Files received:** Friday.
- **Publication cadence:** Available From / Valid From = Sunday; Available To / Valid To = Saturday (USA). **Canada dates always begin and end 2 days earlier than the US.**
- **Go-live:** Canada goes live **Friday**; USA goes live **Sunday.**

## Upload & setup

### File transfer to FTP (owned by DOC)
1. **Store list** — Thursdays the retailer emails a store list; upload it to the Michaels FTP via CoreFTP/FileZilla (no manipulation, drop directly, no folder needed).
2. **Flyer PDFs** — Fridays the retailer emails flyer files via a third-party file drop (`ecom.michaelsconnect.com`); the subject contains the run name, the body contains login credentials (**credentials in the OneGuide — not stored here**). Select the folder named for the run and download all files (file names identify USA vs Canada).
3. **Merchant FTP credentials** — generate via the `#sftp-automation` Slack channel (AWS lambda command with your ops email). Host `sftp.flipp.com`, username `michaels`, password from the generation email (**credentials in the OneGuide — not stored here**).
4. **Upload** — create a directory named after the run, with sub-directories `usa` and `can`. Drop "US" files in `usa`, "CAN"/"QUE" files in `can`. Files appear in Fadmin within ~1 hour.

### Setup instructions (owned by Vendor)
1. Download the **"Media Store List"** Excel (pricing-zone names + page allocations).
2. **Upload pages** from the weekly folder — CAN (Canada, English), QUE (Quebec, French — set language to French), US (USA pages).
3. **Create pricing zones and assign pages** using the Page Codes document.
4. **Add stores to PZs:**
   - `CAN` / `CA_AD_B` → Canada store set
   - `QUE` / `CA_AD_A` → Quebec store set
   - `US_AD_C` → All Stores (minus stores in `US_AD_E`)
   - `US_AD_E` → usually Kansas City + Pittsburgh store sets (verify in Media Store List)
5. After sessions finish green, complete the standard Setup QC checklist.

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Include:** coupons. **Exclude:** packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Single/multi items:** even if an image shows multiple products (e.g. a pile of sketchbooks), box them as one "item block" if they share a single price/offer.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude: SKU and URLs.**

### Image QC
- Specific items flagged: all photo boxes by Simply Tidy, and all Yarn. Choose clean PDFs wherever possible.

## Post-processing / Final QC (owned by Vendor)

**⚠️ Risk item:** if an **"Update Distributions Error"** appears in the pipeline, **ignore it** — it does not block Final QC or affect go-live.

- Complete any outstanding spotchecks; mark Auto Stack Spot Check complete.
- **Thumbnails — Standard 4:** Thumbnail_1065_x_600 (across first two pages, no whitespace), Stock_Premium (first page), Storefront_Carousel_Premium (first two pages), Storefront_Carousel_Organic (first page).
- Overview > Edit Details: **available on Flipp only, no theme, no external run name**, dates correct.
- **Ensure no item links** — URLs should not be applied to any items.
- Check coupons boxed/tagged (if applicable); check sessions ran.
- For both Michaels Canada and Michaels USA: ignore the listed Final QC warnings and press "Save and Confirm."

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Michaels USA OneGuide (Google Doc `1jhv9wccPLjEWSIWHQ2iXAoxMcokADt-iWuW6JBMS82g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
