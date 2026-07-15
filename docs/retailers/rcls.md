# RCLS (Real Canadian Liquor Store) — Processing Guide

> **Source:** RCLS OneGuide (Google Doc `17DL8dBcFbFzIYGBbuiBpHYW2wbNzUH1KOFIZAx954Ss`), updated May 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | realcanadianliquorstore.ca/flyer |
| Flyer types | Weekly (6561); Bi-Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); **Yes — Feedel/retailer data services**; no coupons |

## Files & schedule
- **Files received:** Monday (by noon, right after completion). **Weekly:** Upload Mon, FQC Tue, go live Wed. **Bi-weekly:** Upload Wed, FQC Fri, go live Mon.

## ⚠️ Account flags — short lead times
- Flyer arrives on very short lead times (~noon Monday). **Set priority to Urgent** so FQC can be done Tuesday for a Wednesday go-live.
- If dropped Tuesday, it's always valid starting Wednesday, but due to processing time it's agreed with the merchant to go live Thursday.
- **Be cautious of the short processing time.**

## Upload & setup (owned by DOC)
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded** (Open flyer run > Edit Details > Show/hide rarely-used fields > Height dropdown > 4096.0 pixels > OK). If pages already added, flag to FT Ops and continue.
- **Manual upload:** download pages from the email; upload PDFs as Local Files; number pages (auto-group + cross-reference filenames).
- Pricing Zone: **Base — only 1 zone**; add all stores.
- **Put all tasks on high priority.** Check vendors assigned, sessions, item view (dates on last page). Setup QC: check Geography tab (shouldn't change WOW).
- **Bi-weekly:** Available dates = Monday & Tuesday of the week of the clone; Available Mon–Tue, Valid Mon–**Wed**; Preview Friday; External Run Name = "Flyer Valid Monday, MONTH DATE – Wednesday, MONTH DATE".
- **Weekly:** Available Wed–Wed (no preview); Valid Thu–Wed; Preview the Friday before (OS priority only); External Run Name = "Flyer Valid Thursday, [date] – Wednesday, [date]"; No Theme. Mark off Auto Spotcheck.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include packaged deals**; exclude coupons, logo, sign-up, social, special weblinks.
  - For each item with a unique price, draw a box around the item only.
  - **Sale Story / Disclaimer:** when a page has a Sales Story and/or Disclaimer, it applies to **ALL items** on that page — box + text box for every item (text boxes will overlap). The disclaimer at the **bottom of the flyer** should NOT be boxed or added to items.
  - **PC Optimum sale:** all items get a text box for the Optimum callout (usually on last page).
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required — Tag/QC specific):** include Name, Pre/Postfix, Valid Dates, Description, SKU, Price, Sale Story, Categories, Disclaimer, Original Price; Brand is Box Draw/Box QC specific; **exclude URLs.**
  - Name/Brand in bold; Description below in non-bold (don't double-tag if same text in box and below).
  - **PC Member Exclusive:** Member price = Current Price; non-member price goes in Disclaimer.
  - **Sale Story:** bonus/amount-in-bottle callouts (usually red box) tagged; size in a box goes in Description, NOT sale story. Include PC Optimum Point callouts in the sale story for applicable items. Note the decimal: **$1.08** (small numbers = cents).
  - **Valid Dates:** only tag if an item's dates differ from the flyer; for PC Optimum callouts, only tag if dates differ.
- **Image QC:** clean PDF where possible; cutout if PDF not clean.

## Post-processing (owned by DOC)
- **Pre-FQC (bi-weekly & weekly):** mark off Auto Stack Spotcheck; Standard 4 thumbnails; check valid dates match flyer run (no consumer preview); pagination chronological; geo same WOW; boxes consistent; external run name added. Check vendor tasks complete; page categories (first page never has any); check vertical & horizontal scroll (interactive). Flyer sorting: live above Ops complete.
- **FQC checklist (DOC).** **Bi-weekly only:** clone the flyer run the first week after FQC.

## Flyer review
- **Type: Lite.**

## Live-dates flags
- URL leads to a different item → **Flag.** Item quantities put into the description → **Flag.**

## Out-of-processing
- Long weekend notice: bolded dates need modification (comms template in the OneGuide — contacts omitted here).

---
*Source: RCLS OneGuide (Google Doc `17DL8dBcFbFzIYGBbuiBpHYW2wbNzUH1KOFIZAx954Ss`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
