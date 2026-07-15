# Food Fair Markets — Processing Guide

> **Source:** Food Fair Markets OneGuide (Google Doc `1ynSoHzTuPdHdSIAq-noI8_D4aoHzZucI8ZiL2qtCtyY`), updated Feb 25. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | Weekly flyer (Flyer Type ID 10990) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); OS does FQC; no coupons; no Feedel |

## Files & schedule
- **Files arrive:** Wednesday (retailer sends via SFTP and confirms by email; PSS owns email-receipt confirmation).
- If no response within 24 hours, flag in `#flex-processingsupport`.
- **Cadence:** Available/Valid From Sunday → Available/Valid To Saturday.
- Preview: N/A. Linking document: N/A.

## Upload & setup (owned by Flex)
1. **Manual upload** pages: Pages > Edit > Select Files from FTP; pick pages from the folder with the correct dates (naming convention `MMDDYYYY-MMDDYYYY`); **Auto-Group**; all pages **EN only**; Save & Complete.
2. Flyer Creation → **1 PZ**: Description = base = EN; ensure pages are in sequential order; Save.
3. **Set Preview Date to Thursday** so the flyer is processed for FQC on Friday.
4. Complete Setup QC.

### Setup QC checklist
- Available/Valid From = Sunday, Available/Valid To = Saturday (check against PDF page 1).
- Available on Flipp and Distribution, **Hidden on Hosted**.
- Check theme, apply if available.
- All stores added.
- Add Flyer ID to the VAST Tracker for FQC.

## ⚠️ Common errors / risk items
- **Look for multiple products** — a single ad block may contain more than one product; box each separately.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** box each item. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** Brand used for both box/tag. **Include** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** Standard — PDF preferred if clean, otherwise cutouts accepted.
- **Spotchecks:** standard pricing spotchecks included.

## FQC / flyer review (Vendor owns FQC checklist; Flyer Review owned by Flex)
- Confirm dates match PDF (front page); availability toggles = Available on Flipp + Distribution, Hidden on Hosted.
- Thumbnails correct and include retailer logo (4 Standard).
- All items boxed and tagged; spotchecks complete; previews published/clickable; geography same week over week.
- **Flyer Review type: Lite.**

---
*Source: Food Fair Markets OneGuide (Google Doc `1ynSoHzTuPdHdSIAq-noI8_D4aoHzZucI8ZiL2qtCtyY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
