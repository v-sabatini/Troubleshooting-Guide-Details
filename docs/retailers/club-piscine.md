# Club Piscine — Processing Guide

> **Source:** Club Piscine OneGuide (Google Doc `1LYN1e-YorL7xiokFDooOuNnCPFVy9C3tAinMXzABnqU`), updated May 16, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (**we don't power their hosted**) |
| Slack channel | `#clubpiscine` |
| Hosted URL | clubpiscine.ca |
| Publication | Monthly (**7979**) |
| Cadence | Files Monday. Available Mon, Valid Tue–Mon |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Files received **Monday**; linking document provided. Two flyer runs run at once (split for budget): **Generic** and **Nepean (ON)**.

## Upload & setup (manual; owned by Flex)
1. Pages → Edit → select files. Upload **EN + FR** files to the Generic run; upload **ON** files to the Nepean run.
2. Mark files French → Save → refresh to confirm all FR. Then re-upload same files → mark EN → Save.
3. Autogroup → Save & complete.
4. **Pricing Zones:** Generic run → EN (English) + FR (French); Nepean run → ON (English).
5. Assign stores: Generic EN → add all QC stores; Generic FR → add all QC stores (ignore warning); Nepean Base → add one "ON" store.
6. **Linking document:** split into 1 English, 1 French, 1 ON doc; attach to all vendor tasks.
7. Edit Details: available everywhere, no theme. **Dates are on the back-page disclaimer — client tends to ignore these and follows the dates in their email; if no email, confirm dates.**
8. Leg heights **55/45** (pre-set); thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **Look for multiple products** in a single callout.
- **FR linking doc:** sometimes the column headers (Page, Description) are in French → change subtitles to English if needed.
- **FSA overlap between the two runs** — must be manually deduped at FQC (see below).

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** special weblinks only. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media.
- Draw clean boxes (use the grid). **Do not box any callout without a specific SALE callout.** Linking doc required.

### Tag / Tag QC (Low; Auto-tag OFF)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.
- Name/Description/Categories/URLs come from the attached spreadsheet; price from the item image. Apply unique valid dates and disclaimers where shown.

### Image QC
- Select clean PDF images; most have **black backgrounds**.

## FQC (owned by DOC)
1. Complete outstanding spotchecks.
2. Item Image QC — clean PDFs.
3. Ensure all items boxed/tagged; spotcheck items against the linking doc.
4. Pages → Categories: best judgement.
5. Check pages, vendors, sessions, geography.
6. **Perform FSA Dedupe before completing the checklist** (see below).

### FSA Dedupe (why & how)
- Because the two runs (Generic + Nepean) run simultaneously, some FSAs overlap → a customer in an overlap FSA would see both flyers, so they must be manually deduped.
- Create a **`[DO NOT USE] Club Piscine FSA Dedupe Run`** shell (past date, hidden all channels; upload any 1-page PDF, process internally). Create 2 PZs mirroring the live runs (Nepean → all ON stores; Generic → all QC stores).
- Wait for the "FSA generation" session; this run produces the real FSA distribution. Compare the real run's breakdown-zone FSAs ("unadjusted") against the dedupe run's ("adjusted") in Excel; use `=countif($A$1:$B$999,A1)>1` conditional formatting to flag duplicates. Non-highlighted FSAs are the ones to remove.
- Use FAdmin **Custom Actions → "Remove FSAs"** with the real run's Flyer ID + Pricing Zone ID; paste the non-highlighted FSAs; reload and confirm FSA counts match the test run. Note "custom action to remove FSAs completed." **Repeat for the Generic run.**

- **Flyer Review type: Lite.**

---
*Source: Club Piscine OneGuide (Google Doc `1LYN1e-YorL7xiokFDooOuNnCPFVy9C3tAinMXzABnqU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
