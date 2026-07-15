# Rural King — Processing Guide

> **Source:** Rural King OneGuide (Google Doc `1v-FTMlGRmcgXdQt72QWsW219J_19lDoBhoDC5B1x8hE`), updated Apr 30, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Flyer types | Flyer Type 1 — Weekly (11840) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel; OS N/A |

## Files & schedule

- **Files received:** Wednesday
- **Available From:** Thursday · **Valid From:** Thursday · **Available To:** Wednesday · **Valid To:** Wednesday
- **Preview:** Wednesday, 2-week preview (with enough lead time)
- **Linking document:** N/A (links searched on website)
- **Workflow:** Upload & Setup (DOC, 15 days out) → Image QC (FLEX, 12 days) → FQC + Send Preview (DOC, 11 days) → Receive Corrections (5 days).

## Upload & setup (owned by FLEX)

- **⚠️ Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages Tab → Edit → select all pages from SFTP → Confirm & Upload. Manually add page numbers into the Grouping Number field; ensure correct language. Save & Confirm; **do NOT Process Internally.**
- **Pricing zone creation (manual, from the "Version Sheet"):** pricing zone names are in BLUE; paginate pages left to right (e.g. Zone "A": 1A,2A,3A,4A,5A,6H,7A,8A). Complete for all zones in blue.
- **Store assignment — generic store codesheet from the Version Sheet:** paste Version Sheet column C into column A of a blank sheet and column B into column B (paste values, Ctrl+Shift+V); delete the blank row 1; headers "stores" (A1) and "pricing zone" (B1); save as CSV. Upload via codesheet tab with **config `generic_stores`**, **Store Assignment toggle only**, process.

## ⚠️ Common errors / risk items (retailer-specific)

- **ALL products must have a SKU if listed on the PDF**, and **each item must have exactly ONE SKU.** SKUs pull the correct item on Add-to-Cart — a wrong SKU or multiple SKUs in the field breaks that functionality.
- **Multiple/shortened SKUs:** when an item lists multiple SKUs shortened after the first, reconstruct the full SKU by taking the first SKU and changing the ending digits to match each shortened one (e.g. 2024049029, ...030, ...031, ...032). Still only one SKU per item.
- **All items must have a link.** Search each SKU on https://www.ruralking.com to match the item and get the product-page URL. **For guns, search on rkguns.com.**

## QC specifics

### Box Draw (HIGH complexity; Auto-Box ON, Box QC bot OFF)
- No linking document required.
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Items with several different product images and different SKUs but the **SAME PRICE** → box together.
- Variations with different prices listed below the main item → box separately.

### Tag / Tag QC (HIGH complexity; Auto-tag ON)
- No linking document (links searched on website).
- Include brand, name, pre/postfix, valid dates, description, **SKU (very important)**, price, sale story, categories, disclaimer, original price, URLs.
- All items should have a link (URL from ruralking.com; guns from rkguns.com).

### Image QC
- Standard — PDF preferred if clean; otherwise cutouts accepted.

## Pre-Final QC / FQC (owned by DOC)
- Confirm dates against PDF; availability toggles; thumbnails incl. retailer logo; PDF images where possible.
- **Link QC:** Item Search URL IS BLANK → fill in blank URLs by searching the SKU or item name on ruralking.com; correct any incorrect SKUs.
- **Send preview link at least 3 days before live** to Rural King (they respond with an updated link sheet — update any links listed; they sometimes send a link sheet before the preview).
- Standard flyer review checks: all items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions completed; geography correct.

## Flyer review
- **Flyer Review type: Simple** (owned by DOL). Checks include ensuring SKUs are tagged.

---
*Source: Rural King OneGuide (Google Doc `1v-FTMlGRmcgXdQt72QWsW219J_19lDoBhoDC5B1x8hE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
