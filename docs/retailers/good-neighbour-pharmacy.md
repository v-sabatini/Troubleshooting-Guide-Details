# Good Neighbour Pharmacy — Processing Guide

> **Source:** Good Neighbour Pharmacy OneGuide (Google Doc `1gHiQJYnSkz2m4zJ-XzZNRCBAhqFzCtW4WdBnMXDw84A`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | Hosted only |
| Slack channels | `#goodneighbourpharmacy` |
| Publication schedule | Monthly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing; OS completes Upload + FQC |

- **Cadence:** Available Tuesday, Valid Tuesday.

## Files & schedule

Each month they submit files for **two uploads**: a **manual upload (Flyer Type 1)** and a **codesheet upload (Flyer Type 2)**.

## Upload & setup

### Flyer Type 1 — Manual upload
1. Document name is `gn minicirc`; there should always be **5 zones with the same number of pages per zone**. If there are fewer zones or missing pages, **email the retailer**.
2. Upload the pages.
3. Build the pricing zone: description name = zone #, add the pages, Save and Next.

### Flyer Type 2 — Codesheet upload
1. Download the codesheet from the FTP and manipulate:
   - Sort `GN_TPR_Zone` lowest → highest.
   - Create 2 new columns for Pg 2 & Pg 3.
   - Add `.pdf` to the `GN_Flipp P2 File Name` and `GN_FLIPP P3 Filename` columns after the pages (Find & Replace `P3` → `P3.pdf`); remove the formulas for pg 2 and 3.
2. Save as CSV and upload into the flyer run:
   - **Config name:** `good_neighbor_pharmacy`
   - **Toggles:** all toggles **except region assignment**
   - **Base path** from directory — do NOT include `/FLIPP P1`, only everything before the `/`.

### Setup QC (both flyer types)
1. Upload the **GNP Categories** document to the vendor task (same one all year).
2. Set details: External run name (e.g. "April Circular"), **no theme**, no preview date, **available everywhere (Hosted, Flipp & Distribution)**.
3. Complete Setup QC checklist.

## ⚠️ Common errors / risk items
- **`gn minicirc` must have 5 zones with equal page counts** — if not, email the retailer before proceeding.
- **FSA Dedupe custom action (out-of-process / pre-FQC):** when both runs are READY but NOT yet FQC'd, run the **FSA Dedupe** custom action. Priority: the **codesheet should have more FSAs** (top priority). Flyer Run 1 ID = codesheet; Flyer Run 2 ID = manual. Only complete the FQC checklist after FSA Dedupe is done.
- Include a google category AND an analytical category on each item.

## QC specifics

### Box Draw (Low complexity)
- **Include:** social media, special weblinks, retailer logo, packaged deals. **Exclude:** coupons, sign-up page.
- Linking document required for tagging and item QC.

### Tag / Tag QC (Low complexity)
- **Include:** brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude:** SKU, URLs.
- Tag all fields "as seen on page."

### Image QC
- Select a PDF with a white background where possible; otherwise select the cutout.

## Pre-Final QC
- Legibility heights: 45 × 35. Standard 4 thumbnails.
- Pages → categories: no more than 3 categories per page.
- Recheck details (external run name, no theme, no preview date, available everywhere).
- QC social media boxes/links; ensure bottom social media boxes are tagged.
- Check all pricing zones have a store.
- Run **FSA Dedupe** (see risk items) before completing the FQC checklist.

---
*Source: Good Neighbour Pharmacy OneGuide (Google Doc `1gHiQJYnSkz2m4zJ-XzZNRCBAhqFzCtW4WdBnMXDw84A`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
