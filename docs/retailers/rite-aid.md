# Rite Aid — Processing Guide

> **Source:** Rite Aid OneGuide (Google Doc `1aYOd1wU…6MAKmg`), updated Mar 3, 2025.
> 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#riteaid`, `#riteaid-sepnels` |
| Flyer type / cadence | 9671 Weekly — files received **Monday**; Available from Wednesday; **Valid from Sunday → Tuesday** |
| Processing | Auto-stack; Flex (Flyer Review); OS setup; no coupons processing; Strategic Ops (Feedel) yes |

## ⚠️ Risk items (Rite Aid-specific)
- **Category (navigation) pages:** each category button must be boxed & tagged as a **Page Link**, redirected to the pages listed in the Categories sheet (vendor attachment). Two nav-page types: regular and **alcohol** (`navigation bar_28_alcohol_5`).
- **"Back to the Top" button:** box & tag as a **Page Link to page 1** (never an item).
- **Coupons = barcode only:** tag as a coupon **only if it has a barcode**; no barcode → tag as an item.
- **Disclaimers to watch for:** "Less $$ Manufacturer's Mail-In Rebate", "Regular Retail with Card", "With Card", "Only Available at Save a Lot/Rite Aid Locations", single price "Or $$ Ea.", "equal or lesser value with card", "Less $$ Manufacturer's Coupon…", "Worth at least $$ in savings", "Limit ## offers per card", BonusCash offer disclaimer.
- **Sale story:** BonusCash (items in a shaded area/colored outline); "BUY 1 GET 1 1¢".

## Upload & setup (owned by Vendor)
- **Pages codesheet** arrives via email. Open in Sheets. **Risk:** check the bottom for **"Pages to Come" rows and delete them entirely**. Save as CSV and upload. If it errors, do a Find & Replace on spaces, then re-add spaces to the header names.
- On the PZ tab, ensure all zones have the **same # of pages**; ensure no pages remain in the FTP.
- **Risk:** after sessions run and PZs generate, **delete the `M17` and `NA55` pricing zones** (they have no stores).
- **Store codesheet** (via email, if available — can also do at FQC): open in Sheets, **find & delete the `SP43X` rows** (full rows), download first tab as CSV, upload. Confirm all zones have stores; no net-new page-less zones.
- **Categories sheet + URL doc:** attach the Categories doc to vendor tasks; if no URL doc, comment **"No linking document attached, please box & tag everything as items."**
- **Liquor Ads:** same process, shell in **"Additional Deals"** flyer type. **Flu Page ads:** Weekly flyer type, hidden on Dist/Flipp.

## QC specifics
- **Box Draw:** Low; Auto-Box **on**, Box QC bot **off**. **Include** retailer logo, sign-up page, social media, special weblinks (incl. Back-to-Top as a Page Link); **exclude** coupons, packaged deals.
- **Tag / Tag QC:** Low; Auto-tag **off**. **Include** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude** pre/postfix, valid dates. Watch pre/postfix exceptions: "WITH CARD", "OR $$ EA.", "REGULAR RETAIL WITH CARD", "BUY 1 GET 1 1¢…", ad blocks "You Pay"/"Online Offer"/"Final Cost". BOGO/%-off/$-off → prefix amount/text fields.
- **Image QC:** PDF preferred.

## Pre-Final QC / FQC
- **Trim Box test (new):** if approved by CS, Overview → Ad Hoc → Update Trim Boxes, apply to all pages (a "couldn't push trim to navigation pages" error is fine); sessions re-run.
- Preview name "Preview Next Week's Savings"; No theme; **Valid from → 3 AM**; legibility **45/35** preset; standard thumbnails.
- **Item searches:** "Back to the top" must be a Page Link (not an item); nav-page categories page-linked (search "grocery"/"health & wellness"/"beverages"); coupon types = barcode only.
- Category QC: page-link both alcohol and regular nav pages; check items without analytics categories.
- Photo Insert (usually last/second-to-last page) → direct link to riteaid.com/photo. Mark items **In-Store Only**. FQC checklist: add **N/A** in the Regions/Stores section for the expected error.
- **Flyer Review type: Lite.** Send preview the **Thursday** prior to live date.

---
*Source: Rite Aid OneGuide (Google Doc `1aYOd1wU9aF7mCTtV9bsylzHzpEGbLp4TkBwZc6MAKmg`), updated Mar 3, 2025. Contacts/credentials omitted. Last reviewed: 2026-07-15.*
