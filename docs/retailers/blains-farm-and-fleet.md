# Blain's Farm & Fleet — Processing Guide

> **Source:** Blain's Farm & Fleet OneGuide (Google Doc `1DZtGrW4f6uDhf749DLyi05L0FRW2q_ONK2pvw1Ukb7o`), updated May 15, 2024.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#blainfarmfleet` |
| Hosted URL | https://www.farmandfleet.com/ |
| Flyer type(s) & cadence | Ad Hoc / Monthly (store 2662) |
| Processing | Auto-stack; Flex (Flyer Review); no OS; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Ad-Hoc. **M1000 retailer** — when files are dropped, Fadmin automatically creates the flyer run and kick-starts the upload (pulls in pages, creates pricing zones from the FTP codesheet). Fadmin emails Ops when files drop and again once the run is built.
- **Publication cadence:** all Ad-Hoc.
- **Linking Document:** Yes.

## Upload & setup (owned by FLEX)

- **Codesheets tab:** ensure the codesheet ran successfully (green).
- **FTP:** ensure all pages pulled in and marked uploaded.
- Download the codesheet from FTP (naming: `BlainCodeSheet#####.csv`); cross-check the Pricing Zones tab against it to confirm page order.
- Download the URL/linking document (naming: `BlainLinks#####.csv`); confirm it contains links, save as .xlsx.
- Mark "Flyer Creation" complete once page order is verified.
- Attach the linking document to all vendor tasks. **Paste this note into ALL vendor tasks:** "Please add page link to all items on page… DO NOT TAG BRAND IN THE BRAND FIELD."
- **Overview → Edit Details:** copy INTERNAL name into EXTERNAL RUN NAME without the numbers (e.g. "11035 Spring Denim" → "Spring Denim"); confirm Available/Valid dates match the PDF; No theme; Available Everywhere.
- Standard 4 thumbnails. Complete Setup QC once sessions run.

## ⚠️ Common errors / risk items (retailer-specific)

- **File-number match (RISK):** the numbers in the codesheet and linking-document filenames must match the flyer run number (e.g. run `11035 Spring Denim` → `BlainCodeSheet11035.csv` and `BlainLinks11035.csv`).
- **Do NOT tag brand in the Brand field.**
- **URLs come only from the linking spreadsheet — do NOT use the Blain's website to find URLs.** One URL per page applies to ALL items on that page.
- **Original price rule:** with two prices, use the LOWEST regular price; if original ≤ sale price, use the HIGHER regular price. For "2 for $9" keep original price blank.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- Linking Document required (used for both Box/Tag).
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.
- Box all items separately (with text boxes where needed); red "Other" callouts boxed separately; box ALL clothes together.

### Tag / Tag QC (Low; Auto-tag OFF)
- Linking Document required (Tag/QC-specific).
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, Brand.
- Multiple sizes of the same product → put all info in the description, no second box. Multiple SKUs → include in both Description and SKU field.
- **Prices:** price range → LOWEST sale price = Current Price, HIGHER = Postfix. No sale price → Reg. price in Current Price. Rebate promo → use the **after mail-in rebate** price as Current Price with an asterisk in the Postfix and rebate info in the disclaimer.
- **Member/Non-Member:** tag Current Price with the Non-Member amount, put the Member amount in the Description.
- **Disclaimer:** only if in the box (or if it applies to all items in a group listing / rebate promos); not if at the bottom of the page.
- **URL tagging:** the linking spreadsheet gives ONE URL for ALL items on a page; only tag the specific pages with the provided URL; all items should have a link.

### Image QC
- **Cutouts are always chosen — no PDFs available.** No Item Image QC for this reason.

## FQC (Flyer Review type: Lite; owned by FLEX)
- Complete outstanding spotchecks (original price is always the lower of 2 prices unless equal to current — then use the higher).
- **Links QC:** download the linking document, QC each page so all items on a page share the same page link; then Overview → Items without a URL = 0.
- Do NOT mark In-Store Only; NO page-level categories.
- Edit Details: copy internal → external run name without numbers; no theme; Available Everywhere.
- Leg heights 50/35; Standard 4 thumbnails; sessions run; double-check dates on PDF.
- **Flyer sorting: newest book always first.**

---
*Source: Blain's Farm & Fleet OneGuide (Google Doc `1DZtGrW4f6uDhf749DLyi05L0FRW2q_ONK2pvw1Ukb7o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
