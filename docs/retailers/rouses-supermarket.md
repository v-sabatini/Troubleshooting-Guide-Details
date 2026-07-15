# Rouses Supermarket — Processing Guide

> **Source:** Rouses Supermarket OneGuide (Google Doc `141srvqNCh83f8xepYh43daRJhpmHp2UVoxkaLWrl70M`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#rouses`, `#flex-processingsupport` |
| Hosted URL | https://www.rouses.com/weekly-ads/ |
| Flyer types | Flyer Type 1 — Weekly · Flyer Type 2 — Monthly (ad hoc) |
| Processing | Auto-stack; Flex via FAB tickets; no coupons; no Feedel; OS N/A |

## Files & schedule

- **Files received:** Wednesday
- **Available From:** Tuesday @ 4pm · **Valid From:** Wednesday · **Available To:** Wednesday · **Valid To:** Wednesday
- **Preview:** Wednesdays at 7pm
- **Linking document:** N/A
- **Workflow:** Upload & Setup (DOC, 5 days out) → FQC (DOC, 1 day out).
- **Monthly flyers are ad hoc** — flyer shells need to be created.

## Upload & setup (owned by Vendor)

- **Generic codesheet:** the codesheet is dropped in the FTP with the files (naming e.g. `8-9-23 Codesheet.xlsx`). Download the "Codesheet" excel and upload as a **generic codesheet**.
  - **Config name: `generic`**.
  - **PDF base directory:** take from FTP up to before the second forward slash.
- Setup QC: standard checklist; confirm valid dates (Available From Tue @ 4pm, Valid From Wed, Available/Valid To Wed).

## ⚠️ Common errors / risk items (retailer-specific)

- **"Multiple pages found in the FTP" yellow warning is normal** — Rouses uploads the same pages multiple times in the FTP. Press **"Force processing"**.
- Watch for **special sale pages** (e.g. "Four Day Sale") — enter the specific valid dates for those days (e.g. 4 Day Sale Fri Oct 18 – Mon Oct 21) and include the disclaimer for those special sales.

## QC specifics

### Box Draw (Low complexity; Auto-Box ON, Box QC bot ON)
- Requires Box Draw/Box QC-specific linking document.
- **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons.
- Box any product block with a price and/or sale story; no prices/promos = no boxes.

### Tag / Tag QC (Low complexity; Auto-tag ON; PDF Image Auto Selection ON)
- **No linking document required.**
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs** (no URLs for this retailer).
- **Pre/Postfix — enter as in the flyer:** common prefixes `#/$` (e.g. 3/$5, 2/$7); common postfixes LB, ea.
- **Valid dates:** special sales like 4-day sales get those specific valid dates.
- **Disclaimer:** include for special sales like the Four Day Sale.

### Image QC (owned by DOC)
- **Choose the PDF image if it is clean with no black background; otherwise choose the cutout.**

## FQC / go-live notes (owned by DOC)
- Check dates against PDF (Available From Tue @ 4pm; Valid From Wed; Available/Valid To Wed).
- **No URLs.** Auto-stack. Cutout images are fine.
- **Flyer Sorting:** most recent flyer first, followed by monthly newest→oldest (e.g. weekly, hispanic or weekly, monthly, hispanic). May need manual reordering even when it looks correct.

## Flyer review / out-of-processing
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Rouses Supermarket OneGuide (Google Doc `141srvqNCh83f8xepYh43daRJhpmHp2UVoxkaLWrl70M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
