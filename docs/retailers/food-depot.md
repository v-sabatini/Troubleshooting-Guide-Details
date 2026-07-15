# Food Depot — Processing Guide

> **Source:** Food Depot OneGuide (Google Doc `1Ozjc26SH7-f4iWFeZ5Luge77KhQZsZC-ubPxcmjH9Ds`), updated Jan 21, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | N/A |
| Flyer types | Direct; merchant 2916 |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons, no Feedel |
| Linking document | **Required** (used for both Box and Tag) |

## Files & schedule
- **When files arrive:** Thursday.
- **Publication cadence:** Available From Monday, Valid From Sunday, Available To Monday, Valid To Sunday.
- **Preview date:** Friday before go-live — **set an internal preview date so OS completes processing ahead of the weekend.**
- **Processing type:** Auto-stack.

## Upload & setup (owned by Vendor)
- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages Tab → Edit. Select all pages from the SFTP (or upload from email). Confirm & Upload.
- Once pages listed, **manually enter grouping numbers** — usually only 4 pages total (2× Page 1 & 2× Page 2). **Ensure language is English.** Save & Confirm.
- **Pricing zones:**
  - Create **Base** zone, select all applicable pages. Save & Next.
  - Create **Marketplace** zone, add pages with **"85" in the name**. Save & Confirm.
  - Add all stores **except #85** to Base; add **Store 85** to Zone 85.

### Tagging document prep
- Collect all spreadsheets (usually 3): Grocery (SKUs for most items, 2 tabs — one for regular pages, one for marketplace), Produce - Regular, Produce - Marketplace.
- **Remove all UPC columns** — there should only be **eGrowcery POS**, used for SKU tagging.
- **Highlight the eGrowcery POS column in yellow** wherever it applies, for each section and tab.
- If a product has two SKUs, **ensure there is no space after the comma.**
- Open all spreadsheets and add the Produce and Meat items (paste plain text only) to the corresponding sheets on the Grocery spreadsheet.
- **If only ONE Grocery document is provided,** do all the same manipulations on just that document.
- Save as XLSX and attach to all vendor tasks, with a note to tag all SKUs (eGrowcery POS, highlighted yellow) and use both tabs.

### Setup QC checklist (owned by Vendor)
- Confirm all pages uploaded (Pricing Zone tab → Items View); confirm no un-uploaded pages remain in the SFTP.
- Confirm flyer dates (usually first or last page); **set internal preview date for Friday before go-live.**
- Complete thumbnails (4 Standard); complete Setup QC checklist.
- **File an urgent processing ticket for the flyer.**

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF; linking doc required)
- **Include:** packaged deals.
- **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Risk item: look for multiple products.**

### Tag / Tag QC (Low complexity — Auto-tag ON; linking doc required)
- Brand used for both Box and Tag.
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price.
- **Exclude:** URLs.
- **SKU (from the tagging document):**
  - SKUs are also called **eGrowcery POS**, highlighted in yellow throughout the document.
  - **Use the Marketplace tab for pages with "85" in the file name; use the Food Depot tab for all other pages.** Use both tabs.
  - **Enter up to 12 SKUs per item** — if an item has more, enter the first 12.
  - Cross-reference the item name against the Product Detail & Description columns to find the product.
  - **Tag all SKUs — do not leave any blank unless they cannot be found in the document.**

### Image QC
- PDF preferred if clean; otherwise cutouts accepted.

### Spotchecks
- Standard pricing spotchecks included.

## Post-processing / Final QC (owned by Flex)
- Item Image QC: PDF preferred if clean, else cutouts.
- **⚠️ SKU QC — RISK: all SKUs must be tagged for the Add to Cart function to work.** Overview → Item Search → enter `SKU + IS + [blank]`; use the vendor attachment (CTRL+F the eGrowcery POS code) to fill any blank SKUs. If many are left over, escalate with a feedback ticket to vendors.
- Pre-final: confirm dates against PDF; availability toggles; thumbnails with retailer logo; all boxed/tagged; spotchecks complete (20% of pricing zones); previews published/clickable; sessions completed; geography correct.
- Complete FQC checklist.

## Flyer Review (owned by Flex)
- **Flyer Review type: Lite.**

---
*Source: Food Depot OneGuide (Google Doc `1Ozjc26SH7-f4iWFeZ5Luge77KhQZsZC-ubPxcmjH9Ds`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
