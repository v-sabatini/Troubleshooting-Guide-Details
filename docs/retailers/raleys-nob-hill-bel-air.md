# Raley's / Nob Hill / Bel Air — Processing Guide

> **Source:** Raley's/Nob Hill/Bel Air OneGuide (Google Doc `1KXMWbNZC6pvwPvkGay4DbIGcZbxGdHr3iCciVW2E5_Q`), updated Oct 29, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | Flipp only (hidden on Hosted) |
| Slack channels | `#raleys` |
| Hosted URL | n/a |
| Flyer types | Weekly Flyer (Raley's, Bel Air, Nob Hill Foods) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup + FQC); no coupons; no Feedel |
| Stores | 80 total |

## Files & schedule
- **Files received:** Monday (retailer drops into FTP; Flex confirms receipt). Available/Valid Wednesday–Tuesday, no preview.

## Upload & setup (owned by Flex)
- **Manual upload:** Pages > Edit > check all files in the LOWERCASE folder (whole PDF is auto-split into pages by fadmin) > Select Files > Auto Group > Save and Complete.
- **Flyer Creation:** create 1 pricing zone, description "Base"; ensure all pages added; add all 80 stores.

### Setup QC
- Pricing Zone tab: language English, pages sequential; open item view, check dates at bottom of page 1, confirm pages load/readable.
- Overview > Edit Details: Available Wed–Tue (no preview); Valid Wed–Tue; Internal run name = flyer start date; Preview one day before start; **Hidden on Hosted**; no external run name; no theme.
- Thumbnails: Standard 4.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF, PDF image auto-selection ON):** exclude coupons, packaged deals, logo, sign-up, social, special weblinks. Box every item with a price; box similar versions/sizes with different prices separately. Many items can be drawn with grids — don't forget single items that blend in, e.g. the "Deal of the Week".
- **Tag / Tag QC (Low; Auto-tag ON):** include Name, Pre/Postfix, Valid Dates, Price, Categories, Disclaimer, Original Price. Exclude Brand, Description, SKU, Sale Story, URLs.
- **Image QC:** select clean PDFs wherever possible.

## Pre-FQC / FQC (owned by Vendor)
- Complete outstanding Ops spotchecks. Confirm Available/Valid Wed–Tue (check bottom banner on page 1), internal run name, hidden on Hosted, no external run name, no theme.
- Ad Hoc Processing > Mark Items Store Only. Legibility heights: Scan 35 / Read 25.
- **Image QC = cutouts only**; complete via custom action "Set Cutout Images" (enter Flyer Run ID) — requires being added as Project Coordinator.
- Thumbnails Standard 4; if skinny pages sit in 2nd/3rd position, ensure the 2-page thumbnails cover both (they merge).
- Pricing Zone: item view all boxed; note pages with different valid dates; check full-screen (horizontal) preview clickable (vertical won't load since hidden on Hosted); confirm all 80 stores assigned. **Storefront spotcheck: merge any skinny pages** (Merge + refresh).
- Sessions: all green (PDF Image Auto Selection may be yellow — OK). Geography: "no stores/FSAs added/removed" (one or two changes is normal backend behaviour).
- **FQC:** ignore the "Not all categories used in pricing zones have thumbnails" warning.

### Post-FQC — clone into Bel Air & Nob Hill Foods
- Add self as Project Coordinator on Bel Air and Nob Hill Foods merchant pages.
- Overview > Ad hoc Processing > Clone. Check ONLY the target banner; select **"Weekly Flyer"** in dropdown (NOT "Weekly"); pick the correct existing run matching the date; Copy Tracking Codes/URLs = No; Clone. Repeat for the other banner.
- In the new run: Storefront Spotcheck (confirm merged pages still correct); add all stores to pricing zone; check horizontal preview clickable.
- **If items aren't clickable after cloning:** rerun Page Tile Generation; once Complete, rerun all Vendor Tasks starting with Vendor Box Draw; recheck preview in ~1 hour. Can take up to an hour; if still broken, email full-time team to investigate.

## Flyer review
- **Type: Lite.**

---
*Source: Raley's/Nob Hill/Bel Air OneGuide (Google Doc `1KXMWbNZC6pvwPvkGay4DbIGcZbxGdHr3iCciVW2E5_Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
