# Millbank Hardware — Processing Guide

> **Source:** Millbank Hardware (6751) OneGuide (Google Doc `1LLm4b1qrb4y7EStNNxbq2Qlqw31eYfFronXYkt-jrr4`), last updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Hosted URL | N/A |
| Flyer types & cadence | Flyer Type 1 — Flyer (11968), **ad hoc** |
| Processing | Auto-stack |
| Who's involved | Flex (Upload/Setup + FQC); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files received / cadence: ad hoc.** The client typically emails files very late and asks for ASAP processing. They know our timelines — no daytime processing needed. **Happy if live within 4 days; understand if it takes 5.**

## Upload & setup (owned by DOC)

- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- **Manual upload:** Pages tab → Edit → select all pages from SFTP (or upload manually from email) → Confirm & Upload → Auto-Group **or** manually enter page numbers in the Grouping Number field; ensure language = English → Save & Confirm.
- **Pricing zone creation:** create **Base** pricing zone, select all applicable pages, Save & Confirm, **add all stores.**

**Setup QC:** confirm all pages uploaded (Pricing Zone tab → Items View; confirm no un-uploaded SFTP pages remain); confirm flyer dates (usually first or last page); complete 4 Standard thumbnails; complete Setup QC checklist.

## ⚠️ Common errors / risk items

- **Original Price** — ALWAYS tag the original price if it's listed on the flyer.
- **Multiple items under one name** — they often list many items under the same name with different sizes/prices. **Box every item that has a price**, including unique details (size, code/SKU). Text boxes can be used for the names at the top of the lists.

## QC specifics

### Box Draw / Box QC — **Medium complexity**
- **Auto-Box Draw: OFF. Box QC bot: OFF.** No linking document.
- **Include:** packaged deals. **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC — Low complexity
- **Auto-tag: ON. PDF image auto-selection: ON.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, image QC. **Exclude: URLs.**
- **Standard processing:** Brand from logo (if applicable); Name = large title text; Current Price usually red; Original Price as shown; SKU = associated code; other text in description. Tag exactly as shown.
- **List-item processing:** draw a **text box around the title above the list.** Brand from logo or the BRAND column; Name = large title text at top; Original Price from the REG column; SKU = associated code; size/etc. in description.
- **Linking document (when used):** colours group a table where **one URL applies to the whole coloured block** (e.g. the link in row 16 applies down to row 22 for the green rows).

### Image QC
- PDF preferred if clean; otherwise cutouts accepted.

## Post-processing (owned by DOC)

**⚠️ FSA custom action.** FSAs must be overwritten from what Fadmin generates — Millbank is in South/West Ontario and wants only a few select FSAs; a radius large enough to capture them would also capture most of the GTA (not wanted).
- Open the FSA sheet ("FSA Import" tab); copy the flyer's Pricing Zone ID into Column A for ALL FSAs.
- Download as CSV; on the Custom Actions page run **"Assign FSAs from CSV"** with the flyer run ID.
- Confirm all FSAs added via the Geography tab.
- **RISK:** if there is a page swap, FSA Generation re-triggers and this custom action **must be re-run.**

Then confirm dates (per PDF), availability toggles, thumbnails (include retailer logo), and standard flyer review checks (items boxed/tagged, spotchecks at 20% of PZs, previews clickable, sessions accurate, geography correct).

## Flyer review

- **Flyer Review type: Lite** (owned by DOL). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Millbank Hardware OneGuide (Google Doc `1LLm4b1qrb4y7EStNNxbq2Qlqw31eYfFronXYkt-jrr4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
