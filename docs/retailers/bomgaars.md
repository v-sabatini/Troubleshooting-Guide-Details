# Bomgaars — Processing Guide

> **Source:** Bomgaars OneGuide (Google Doc `1KPxw8PKHfQ8luGnxoSFW3oj0AWglWh5FUcbOaNf5fmE`), updated Jul 7, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (retailer 6522) |
| Availability | All platforms |
| Slack channels | `#bomgaars` |
| Hosted URL | bomgaars.com |
| Flyer types & cadence | Weekly + Monthly. **Flyer** (type 11191) · **Bonus Buys** (type 11747) |
| Processing | Auto-stack; Flyer Review owned by Flex; no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication:** Available From Tuesday; Valid Monday → Wednesday; Available To Monday.
- **Linking document:** N/A.
- **Processing pipeline:** Upload & Setup (Vendor), Image QC (Flex), FQC (DOC).

## Upload & setup (owned by Flex)

**Always check the ClickUp ticket for special instructions first.**

**Flyer (type 11191):**
- The **Stores/Version document is provided via the ClickUp ticket, not SFTP** — or a comment may say "Add all stores" (then no Version doc needed). If missing, reach out to Coordinator/Lead.
- Manual upload from the dated folder. **Cannot auto-group** — pages don't follow 1,2,3 naming; open the Version Grid (e.g. "021125 Wk 43 Version Grid") for page order. Example: 2 versions (Base, South); Base pages `1TB, 2TB…`, South pages `1TS, 3TS…`. **Version grids vary week over week** and may have multiple zones.
- Group pages per the Version Grid; Save + Complete. Create pricing zones matching the **Version Name** on the grid; add pages.
- **To add stores:** copy Store + Version columns from the Version Grid into a new sheet; rename to `stores` / `pricing zone`; paste-values. **Stores need leading zeroes** to match FAdmin — set Column A to Plain Text, use `=TEXT(A2,"000")` (must retype the formula, not paste it), autofill. Copy the padded codes back into Column A. Pricing-zone names must match the system labels **exactly**. Save CSV, upload in the Codesheet tab, Save and run; when green, verify Pricing Zone tab populated.

**Bonus Buys (type 11747):** manual upload from the 'bonus buys' folder, upload and auto-group, create a `Base` pricing zone, add all stores, Setup QC.

**Setup QC (Flyer):** no external run name; no theme; legibility height 50, 40; standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- Watch for **multiple products** in one box.
- **Codesheet:** store codes must carry leading zeroes (`=TEXT(A2,"000")`) — you cannot copy/paste the formula, retype it; if you hit ERROR/REF# reach out to Coordinator/Lead.
- Pricing-zone names in the codesheet must match the system labels exactly or stores won't match.
- **Flyer sorting (important):** Main flyer (run named `MMM-DD`, e.g. "Apr 13") must be first, followed by Wraps, Flipbooks, Guides, Bonus Buys in that order.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF. No linking doc.** Include coupons and packaged deals; exclude retailer logo, sign-up page, social media, stand-alone URLs/banners. Box all items with prices, using text boxes when necessary.
- **Tag / Tag QC — Low. Auto-tag OFF. PDF image auto-selection ON.** Tag Name/Brand/Description/Price/Pre-Postfix/Sale Story/Disclaimer **EXACTLY as in the flyer, case-sensitive.** **DO NOT tag SKUs unless the Vendor Notes say to.** Sale Story and Disclaimer can be item-level or page-level. Do not change Valid From/To unless clearly on the flyer. Every item needs a category. URLs found via bomgaars.com search.
- **Image QC:** PDF preferred if clean; cutouts accepted if PDF is cutoff/stretched, shadowed, or a multi-item pack-shot.

## FQC / go-live (owned by Vendor)

- Spotchecks (standard pricing); mark auto-stack complete; confirm dates match PDF (available 1 day before valid); re-verify URLs; ensure all pages tagged.
- **Flyer sorting** as above — Main flyer first.
- **Flyer Review type: Lite.**

---
*Source: Bomgaars OneGuide (Google Doc `1KPxw8PKHfQ8luGnxoSFW3oj0AWglWh5FUcbOaNf5fmE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
