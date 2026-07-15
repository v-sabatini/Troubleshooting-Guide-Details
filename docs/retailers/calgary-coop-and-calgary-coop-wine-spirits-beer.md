# Calgary Co-op & Calgary Co-op Wine Spirits Beer — Processing Guide

> **Source:** Calgary Co-op & Calgary Co-op Wine Spirits Beer Liquor OneGuide (Google Doc `1aeV6bYo274O3vstEtpwkQ6XfUvQAq9OhNpL5ZEDF8xA`), updated Mar 11, 2026. Contacts/credentials omitted.

> **Two banners, one shared linking doc** that must be split: Calgary Co-op (food, flyer type **480**) and Calgary Co-op Wine Spirits Beer / WSB (flyer type **3441**).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#calgarycoop` |
| Hosted URLs | calgarycoop.com · coopwinespiritsbeer.com |
| Flyer types | 480 Weekly (Co-op food) · 3441 Weekly (WSB) |
| Processing | Auto-stack; Flex (Setup, FQC, Flyer Review); OS (Setup); no coupons; no Feedel |

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From Wednesday · Valid From Thursday · Available To Wednesday · Valid To Wednesday.
- **Linking document:** yes (shared between the two banners — see below).

## Upload & setup (owned by Flex)

**Shared linking-doc manipulation (do once):** They send **2 linking docs in the FTP — use the `coded.xlsx` file.** Select all → **paste as plain text** (Ctrl/Cmd+Shift+V) to strip formulas. Delete columns Name, Page, Shortened URL. The doc mixes **Co-op Weekly AND WSB** content, so split it: new sheet with headers Flyer, Dates to display, Name Code, URL; move the WSB rows into the new sheet. Save two docs — `Wk___ (Weekly)` and `Wk___ (WSB)`.

**Calgary Co-op Food (480):**
1. Manually upload all pages → 1 pricing zone → all stores.
2. Attach the **Weekly** linking doc to all vendor tasks.
3. Overview > Edit Details: no theme; available everywhere. Thumbnails 4 standard. Setup QC.

**Calgary Co-op WSB (3441):**
1. Pages > Edit > select files. **Page order follows natural pagination (e.g. 1, 1A, 2, 2A).**
2. Pricing zone: Base; assign all stores. Wait for sessions.
3. Attach the **WSB** linking doc to all vendor tasks.
4. Overview > Edit Details: no theme; available everywhere. Thumbnails 4 standard. Setup QC.

## ⚠️ Common errors / risk items
- **Valid dates only on 'Price Drop' items** — do not add valid dates elsewhere.
- **Product links** must be boxed and tagged correctly.
- **Meat and deli categories usually have errors** — verify they are categorized correctly.
- **Unique valid dates in the linking doc are a recurring risk.** During FQC, check the linking doc for unique valid dates; if present, create an **Optics ticket (OPSMR)** and trigger accordingly (add DOC + DOL, assign to 1DOC). WSB **always has one (a 4-day sale)** and can also have unique dates on specific pages.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- Linking document required (box-specific).
- **Include:** coupons, packaged deals, sign-up page, social media, special weblinks. **Exclude:** retailer logo, percent-off sales.
- Single items: box the whole item block. **Multi-items: box separately even if pictured together** (different pricing → cannot be combined).

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON)
- Linking document required (tag-specific). **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- Tag branding only in the branding field (don't double in name). Enter fields as seen in flyer. URLs from the linking doc — usually only top/bottom banners, not food/wine items.
- **Categories: tag both "Categories" AND "Category Highlights" fields; be mindful of meat and deli.**

### Image QC
- Use PDF whenever possible; cutout if no clean PDF. **Co-op food PDFs often have black around the edges.** WSB is essentially all cutouts.

## FQC (owned by Flex)

**Co-op Food:** mark autostack + spotchecks complete; Category QC (meat/deli); Linking Doc QC (insert names + URLs match attached doc) — **check for unique valid dates → Optics ticket**; all vendor tasks/sessions complete; FQC checklist.
- **Ad-hoc:** if a PDF page has a weird shadow, run **"ghostscript 9.06 gamma"** in sessions at the page level.

**WSB:** mark autostack complete; Linking Doc QC — **there is always 1 unique valid date (4-day sale) → Optics ticket**; also check unique valid dates on specific pages; sessions/tasks complete; FQC checklist.

- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps are standard (baseline process).

---
*Source: Calgary Co-op & Calgary Co-op Wine Spirits Beer OneGuide (Google Doc `1aeV6bYo274O3vstEtpwkQ6XfUvQAq9OhNpL5ZEDF8xA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
