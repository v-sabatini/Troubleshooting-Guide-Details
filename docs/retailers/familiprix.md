# Familiprix — Processing Guide

> **Source:** Familiprix OneGuide (Google Doc `1Ajg_9-Q-DyqN-agQ5O_TnqxQC0eaIHrSmBv_-67t5oo`), updated Apr 7, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#familiprix` |
| Hosted URL | familiprix.com/en/flyer |
| Flyer types | Weekly Flyer – Hosted · Weekly Flyer – Extra (4 versions: Regular, Extra, Santé, Clinique — each EN + FR) |
| Processing | Auto-stack |
| Who's involved | Flex (Setup + Flyer Review); OS (Setup); DOC (FQC); no coupons; Strategic Ops — yes, Feedel/retailer data services |

## Files & schedule

- **Files received:** Monday. FTP drop includes 4 versions (Regular, Extra, Santé, Clinique).
- **Cadence:** Available From Tuesday, Valid From Wednesday; Available To Monday, Valid To Tuesday. Preview date = Thursday before live.
- **You upload to the Hosted run only** (usually "Week XX - Hosted"); other runs are created by cloning during FQC.

## Upload & setup (owned by Flex)

- **Blank codesheet upload:** download the blank codesheet, name it e.g. "Familiprix - Week X". Flyer run → Codesheets: Name `CS`, **Config `familiprix`**, PDF base directory from FTP, **3rd, 4th and 6th toggles checked only.** Process.
- The codesheet auto-creates all PZs: **English/French × Regular, Extra, Clinique, Santé** (Clinique and Santé have far fewer pages).
- **⚠️ "Pages Previously Uploaded" warning is normal** — files are uploaded twice per distribution (EN Regular & FR Regular use the same PDFs).
- **⚠️ Do not assign stores until FQC.**
- **Linking sheet:** split into separate EN and FR sheets. **Product linking sheet:** create separate EN and FR files, each with 4 tabs (Regular, Extra, Clinique, Santé); delete rows not matching each tab. FR file gets `_FRENCH` suffix.
- **⚠️ Risk:** attach the English linking + product-linking docs to the **English** vendor tasks and the French to the **French** tasks.
- Edit Details: no theme; **hide in distribution and Flipp;** preview date = Thursday before live.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required)
- **Include** packaged deals, retailer logo, sign-up page (box entire page), social media, special weblinks, banners with a call to action. **Exclude** coupons.
- **Box each product individually** even within the same sale block; use text boxes for product descriptions.
- **⚠️ Do NOT box product blocks that have points callouts.**

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON; linking doc required)
- Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Brand is box-draw specific.
- **Name:** tag as it appears in the **Product Name e-commerce** column in both EN and FR.

### Image QC
- Choose clean PDFs on the right side of the tagging interface **as you tag.**

## FQC (owned by DOC — happens in 2 parts)

### Part 1 — FQC Hosted
- **⚠️ Verify the comment "links QC completed" is present before starting.** If missing, do not proceed — reach out to the account coordinator.
- Complete Ops spotchecks (FR & EN); open the linking doc (not the product linking doc) in the vendors tab.
- Add special valid dates if the flyer needs them.
- QC thumbnails Standard 4 — **different set per PZ** (same 4 for EN & FR Santé, 4 others for EN & FR Clinique, etc.).
- Check vertical preview; **HIDE in distribution and Flipp.**
- **⚠️ No stores added until after cloning.** Then add store sets to the corresponding PZ for the hosted run.

### Part 2 — Cloning & store assignments
- From the FQC'd Hosted run, **Clone to the existing Clinique, Santé, and Regular runs — DO NOT create a new run;** always copy to an existing run. Match week numbers (Week 27 Hosted → Week 27 Regular/Clinique/Santé).
- In each clone, Edit Details → change toggles to **hide in hosted only.** Re-run **Page Tile Generation** and **Page Stitching** from System Tasks.
- **Store assignments — HOSTED:** each version's EN+FR PZ gets its matching store set (Clinique→Clinique stores, Extra→Extra, Regular→Regular, Santé→Santé).
- **Store assignments — CLONES (Clinique, Santé, Regular, Extra):** add all stores only to the EN & FR PZs matching the run name; the remaining zones get no stores.
- **⚠️ Risk:** set the cloned flyers to hidden in hosted, available on Flipp and in distribution.

## Flyer Review
- **Type: Lite** (separate flyer-review guides exist for Regular, Santé, Clinique, Extra).

---
*Source: Familiprix OneGuide (Google Doc `1Ajg_9-Q-DyqN-agQ5O_TnqxQC0eaIHrSmBv_-67t5oo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
