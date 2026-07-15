# Ranch Fresh Supermarket — Processing Guide

> **Source:** Ranch Fresh Supermarket OneGuide (Google Doc `19QuHRjMDTDhwPAxLi0EZ9DFnc6L5lKeTKtRAVBRLk9o`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Standard |
| Availability | Flipp only |
| Slack channels | `#ranch-fresh-supermarket`, `#flex-processingsupport` |
| Flyer types | Weekly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule
- **Files received:** Thursday (retailer sends separate emails, one page each — typically 3 pages / 3 emails; files usually arrive 11 AM–3 PM Thursday). No preview, no linking document.
- Available Fri; Valid Thu → Thu.

## Processing model (important context)
This merchant was formerly Simplified Pop (no vendor processing). With Simplified Pop deprecated (2025) and auto-tag not reliably filling the Name field, **Item QC was reinstituted to run overnight after FQC.**
- **Thursday:** flyer uploaded → system tasks run (mark off Box QC) → auto-tag runs → FQC'd (Item Tag manually re-assigned to DSP after FQC) → flyer reviewed → pipeline Tag QC completed overnight.
- **Friday:** validate Tag QC completed and Name field populated.

## Upload & setup (owned by Vendor/Flex)
- Download each page from the emails; **manual upload**. Attach PDFs to the ClickUp task once processed.
- Create one PZ "Base", add all stores. Add all pages in numerical order.
- Edit Details: Available & Valid Fri–Thu; Hidden on Hosted; No theme. Draw Thumbnails (standard).
- **Vendor tasks are NOT required until AFTER FQC** — continue straight to post-processing.

## ⚠️ Risk item — Full Screen Preview not interactive post-FQC
If clicking an item shows no pop-up, the preview isn't interactive. Fix:
1. Flyer Creation task (ops task) > refresh > when available, Start and make a **new pricing zone** ("Base v2") with all pages > Save and complete.
2. Systems tasks: refresh (a) Page Tile Generation and (b) Page Stitching.
3. In pricing zone tab, remove stores from the original PZ and add to the new PZ.
4. After sessions rerun, recheck full screen preview. If still not interactive, flag to the FT Ops owner.

## Post-processing
1. After Setup QC, allow system tasks + Auto Box Draw to run.
2. Mark **Vendor Box QC**, **Vendor Tag**, **Vendor Tag QC** complete.
3. Continue to FQC.

### FQC (owned by Flex)
- Complete FQC checklist; confirm Full Screen Preview interactive (fix per risk item above).
- **NEW:** after FQC checklist, re-assign **Vendor Tag QC** via the Vendor Pipeline Task > "Rerun Task". Confirm on Vendors tab: **Vendor Tag QC (Vendor ID 56)** and **Vendor Spot Check (Vendor ID 43)** reassigned. (Vendors perform Item QC & spotchecks that ensure the Name field is tagged.)

## QC specifics (not required until after FQC)
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, logo, sign-up, social, special weblinks. **Box QC: delete the boxes on the top half of the first page.**
- **Tag / Tag QC (Low; Auto-tag ON, PDF image auto-selection OFF):** include Brand, Name, Pre/Postfix, Valid Dates, Description, Price, Sale Story. Exclude Image, SKU, Categories, Disclaimer, Original Price, URLs. **Do not tag regular price.** Examples: Brand "Haday", Name "Haday Premium Soy Sauce", Desc "1.9L", Price 5.99, Postfix EA; Name "Fresh Mackerel", Price 3.99, Postfix LB.

## Flyer review
- **Type: Lite.**

## Out-of-processing
- Standard page swap.

---
*Source: Ranch Fresh Supermarket OneGuide (Google Doc `19QuHRjMDTDhwPAxLi0EZ9DFnc6L5lKeTKtRAVBRLk9o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
