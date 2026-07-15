# Community Natural Foods — Processing Guide

> **Source:** Community Natural Foods OneGuide (Google Doc `1-VBH3vPRpT_upHzMuqhu_3K_HNLyZMg7MMIyRVpMlWA`), updated Jun 22, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channel | `#community-natural-foods` |
| Hosted URL | communitynaturalfoods.com |
| Publication | Monthly (**9708**), with weekly page swaps |
| Cadence | Files ad hoc. Available Thu, Valid Tue → Tue a month later |
| Processing | Auto-stack; Flex (3FL + Flyer Review); no OS, no coupons, no Feedel |

## Files & schedule
- **One base file set** arrives at the **start of each month** and runs for the month (first flyer's pages are labelled by number only).
- **Each week after**, updated pages (generally new **Page 1 "front"** and **Page 9 "produce"**) are submitted, uploaded to the monthly run and **swapped in via a trigger** on the client-requested date.
- Stores split by **Calgary** and **Edmonton** zones when two zones are used.

## Upload & setup

### New monthly publication (owned by Flex)
- Create a new flyer run (dates from client email); Pages → Edit → upload from that month's FTP path → Autogroup → Save & Complete.
- Flyer Creation: usually one Base PZ, all pages. Stores — one zone: add all + wait for FSAs; two zones: Calgary stores → Calgary zone, Edmonton stores → Edmonton zone.
- Setup QC: thumbnails Standard 4 (always get logo + retailer name). **Attach the MONTHLY URL document from FTP to *all* vendor tasks** (check "Mass Attachment?") — ensure the **monthly** links (not the updated weekly links) are used. Setup QC checklist + Autostack Spotcheck.

### Weekly page swaps (owned by Vendor)
- Pages → Edit → upload the week's new pages from FTP → Save & Complete.
- **Attach the newest URL document** to all new vendor tasks (sometimes one doc, sometimes two — one Edmonton, one Calgary). Autostack Spotcheck.
- **Set a trigger to swap in the new pages for the upcoming Thursday:** Pages → Layout → swap out current Page 1 + Produce Page for the new ones → **"Run as Trigger"** → select the next Thursday at 12:00 am.
- **Make a Jira ticket to verify the trigger ran** the morning after; notify the DOC + DOL.

## ⚠️ Common errors / risk items
- **Page swaps:** Flex uploads the monthly file; **weekly Page 1 + Page 9 updates must be uploaded by DOC, processed by OS, and trigger-swapped** on go-live week. Verify the trigger ran.
- **URLs:** use the attached spreadsheet to add URLs; check the URL section carefully.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; Box Draw/Box QC linking doc)
- **Include:** special weblinks. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- **Box each item individually.**

### Tag / Tag QC (Low; Auto-tag ON; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand (in both Brand + Name), name, pre/postfix, valid dates, description (incl. sizes/weights), price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** SKU.
- Price: include `/lb` and `/kg` price in the postfix.
- **URLs from the spreadsheet** (page #, product name, URL). **Items highlighted yellow = Direct Links** — box and tag as Link type.

### Image QC
- Use PDFs whenever possible; use cutout when the PDF image isn't clean (watch for grainy backgrounds).

## FQC (owned by DOC)
### New monthly publication
- Autostack Spot Check; OS Spot Checks (usually none; occasionally approve a Name or check a Price).
- Overview: legibility heights (preset Scan 40, Read 25); Image QC; thumbnails Standard 4; Edit Details (Available = Valid, Thu → Wed a month later; dates match PDF; available everywhere; no external run name; no theme).
- Pages QC'd; categories accurate per page.
- **URL/Links QC:** open "Items Without URL"; cross-check the attached URL doc (names aren't exact matches — search by brand, e.g. Ctrl+F "CanPrev"). Yellow-highlighted items are direct links — box/tag with correct URL and item type Link.
- PZ item view boxed/tagged; vertical + full-screen preview; sessions green (PDF Image Auto Selection may be yellow); vendors done; geography — no week-over-week changes.
- Complete FQC (ignore the categories/thumbnails warning).
- **Flyer Review type: Lite.**

## Out-of-processing
- Weekly page swaps as above (trigger-based).

---
*Source: Community Natural Foods OneGuide (Google Doc `1-VBH3vPRpT_upHzMuqhu_3K_HNLyZMg7MMIyRVpMlWA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
