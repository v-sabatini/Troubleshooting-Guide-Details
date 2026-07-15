# Weis Market — Processing Guide

> **Source:** Weis Markets OneGuide (Google Doc `1y184ktYH5iUJFspZrKP_PnglT2dEqvr_5jAgCeZ3KkQ`), updated May 1, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Merchant ID | 2455 |
| Flyer types | **Weekly Circular** (weekly — includes the 1–2 page 3 Day Sale) · **Monthly** (Ad Specials / grocery, HBC / Home, NOS / Natural & Organics) |
| Processing | Auto-stack; DOC upload/setup, Vendor pipeline, DOC FQC; no coupons; **Strategic Ops / Feedel data services: yes** |

## Files & schedule

- **Files received:** Monday.
- **Weekly cadence:** Available From Thursday, Valid From Wednesday; Available To Tuesday, Valid To Wednesday. Weekly flyer runs Thu–Wed; the 3 Day Sale runs Thu–Sun.
- **No preview days.**
- **Linking (tagging) document:** Yes for all flyers **except NOS**.
- All flyers are processed exactly the same.

## Upload & setup

- **Page numbers** are the digits after the underscore in the page name (e.g. `73_7` = page 7).
- **Codesheet** arrives on the SFTP as a `.txt`; open and save locally. There can be **more than one codesheet** — match the `CircularType` name (e.g. "Weekly") to the flyer / external run name.
- **Codesheet config: `weis`**; PDF Base Directory = entire path; **toggle all options except region assignment**.
- **Tagging document** arrives on the SFTP as `.xlsx` ("Weekly/Monthly Sale Items"), split into tabs (Weekly, 3 Day Sale; or HBC, Grocery, 3 Day Sale for monthly). Match tabs to flyers by comparing page numbers in the tab to the pages in the codesheet. If a flyer has more than one tagging tab, note it in the vendor tasks.
  - **Tagging doc manipulations:** delete empty columns G and H; select all and remove duplicates on every tab; save, import to Google Sheets, re-download as `.xlsx`; split tabs into individual `.xlsx` files per flyer; attach to all vendor tasks.
  - **NOS has no tagging document** — leave the note: "No Excel needed for processing, use PDF details."
- **External Run Names** (must be set on Edit Details): Weekly = `Weekly Circular`; 3 Day Sale = `3 DAY SALE`; NOS = `Natural & Organic`; HBC = `Monthly Home`; Grocery monthly = `Ad Specials`.
- No theme. Standard 4 thumbnails.

### ⚠️ Common errors (retailer-specific)

- **DO NOT box or tag the Rewards section** — promos stating "Free with xxx points" or "0.99¢ with xxx points" must not be boxed or tagged. Remove any boxes drawn there.
- **Codesheet typos** are frequent: commas used instead of periods (and vice versa), missing `.pdf` after page names, and page-allocation/order mistakes. If files are named "Region 1", correct to "RegionFiles 1".
- **Liquor pages** and typically **page 7** are not in the tagging document — this is expected. Only escalate if a *regular* page is missing.
- **Small red card** in the corner of a product → postfix must be "With Weis Preferred Shoppers Club."

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** packaged deals, retailer logo, sign-up page, special weblinks. **Exclude:** coupons, social media.
- Box every item with a price. Multiple products sharing one price can go in one box; small product names under larger products with different prices need their own box. Don't overlap items — use text boxes.
- **Never box the Rewards section.**

### Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON)
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **SKU:** listed under UPC in the spreadsheet; enter up to **12 SKUs max** per item (first 12). Monthly NOS flyers usually have no spreadsheet.
- **Postfix:** add "with Weis Preferred SHOPPERS CLUB" when the card logo appears (including sub-items); combine postfixes where needed; do **not** add postfix to items without a price. **Any points offer goes in the Sale Story, not the postfix.**
- **Discount:** do not enter Dollars Off / Percent Off unless explicitly on the flyer.
- **Valid dates:** found at the bottom of the page unless otherwise specified; enter override dates if applicable.
- **Disclaimer:** only if within the drawn box (not the page-bottom disclaimer).
- **Page categories:** page 1 has none; every other page needs at least 1 (use the header on the page, e.g. Deli/Cheese & Baked Goods, Dairy & Frozen, Snacks & Beverages/Aisles of Savings).

### Image QC
- Prefer PDF. Avoid lifestyle/plated or images with backgrounds — choose the cutout unless it's really bad. Select the packaged item, not the plated item; avoid cutouts with a white border.

## Final QC / go-live notes
- Set the **External Run Name** on Edit Details (list above).
- **SKU corruption check:** Overview → Item Search, "SKU" + "Contains" + "+" and "+" + ",0" — any hits are corrupt SKUs; fix/confirm against the tagging spreadsheet (search by product name).
- Confirm **no boxing/tagging in the Rewards section.**
- **Leg heights 50/30.** Standard 4 thumbnails.
- **Flyer sorting:** weekly → 3 day → monthly flyers.
- Spotchecks handled by OS.
- **Flyer Review type: Lite.**

## Out-of-processing
- SFTP credentials are provisioned via the `#sftp-automation` Slack automation (credentials in the OneGuide — not stored here). Weekly files are dropped into a dated folder under the current year.
- **Vendor setup:** use the VAST spreadsheet, find the Weis Markets row(s) for the current week (multiple flyer run IDs may be needed for one file drop), fill in the flyer run ID and available date, and set to SETUP READY.

---
*Source: Weis Market OneGuide (Google Doc `1y184ktYH5iUJFspZrKP_PnglT2dEqvr_5jAgCeZ3KkQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
