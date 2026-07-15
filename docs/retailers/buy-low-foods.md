# Buy-Low Foods — Processing Guide

> **Source:** Buy-Low Foods OneGuide (Google Doc `1Guz-uUxRF7o0vEHBV4DJ7swShL3JCTjhicRNAj4f0V8`), updated Apr 21, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | All platforms |
| Slack channels | `#buylowfoods` |
| Hosted URL | buy-lowfoods.com |
| Flyer types | 9323 Weekly · Monthly (Budget Savers — currently discontinued) |
| Processing | Auto-stack; Flex Flyer Review (paused for CuSat); no coupons; **Feedel/Strategic Ops: yes** |

## Files & schedule

- **Files received:** Thursday.
- **Buy-Low Weekly cadence:** Available From Wed 3am · Valid From Thu 2:59am · Available To Thu 3am · Valid To Wed 11:59pm.
- **Westrose Weekly cadence (discontinued):** Available From Sat 3am · Valid From Sun 2:59am · Available To Sun 3am · Valid To Sat 11:59pm.
- **External run name:** "Weekly Ad". No theme. No preview date (preview added Tuesday before go-live).

## Upload & setup (owned by Vendor)

**Buy-Low Foods weekly:**
1. Download/open the BL `.xlsx` codesheet for the working week from the fadmin FTP.
2. **Manipulate codesheet** (in Google Sheets, Store Versioning tab): delete first 4 rows, delete column A, delete empty extra rows/columns (everything from column D on). If "Version" file names contain ".pdf", strip it (e.g. `BLBC p1.pdf` → `BLBC p1`). Download as CSV.
3. **Upload:** Name = `upload`; upload the CSV; **Config = `overwaitea`**; PDF base directory taken directly from the SFTP.
4. Check the SFTP (`/BL`) that all pages uploaded; mark flyer creation complete.
5. Stores are added to each pricing zone automatically by the codesheet.
6. **Verify page-to-zone mapping:** store 4819 → BL1, 4820 → BL1, 4811 → BL1, 4818 → BL2, 4802 → BL6, 4817 → BL4; multi-store pricing zone → BLBC pages.

### Setup QC
- Edit details: Avail 3am Wed; Avail To 2:59am Thu; Valid From 3am Thu; Valid To 11:59pm Wed; external run name "Weekly Ad"; no theme.
- Fab 4 thumbnails (BLBC pages first, apply changes; then flyer type "4819", draw thumbnails and apply to zones 4819/4820/4811/4818/4802/4817).
- **Geography will show 4 stores added — ignore during Setup QC** (FQC ensures week-over-week consistency).

## ⚠️ Common errors / risk items
- **Pricing-zone page order (top risk):** two versions exist — **Version A** and **Version B**, distinguished by an A or B in the page name. A Version A page must **never** be in a Version B zone or vice versa.
- **Alternate pricing per KG goes in the description**, not the postfix. Example — Name: New York Strip Loin Roast; Description: "Canadian AA or Better Grades of Beef / 19.80/kg"; Current Price $8.98; Postfix "lb".
- Box the **text rather than the image** on pages with multiple overlapping products.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Exclude:** coupons, packaged deals, retailer logo, social media.
- **Include:** sign-up page, special weblinks.
- Box all items with prices, using text boxes when needed. Box "More REWARDS" pages → name "More REWARDS", link `buy-low.com/morerewards`.
- **Risk:** watch for **date-specific items** (special valid-date callouts).

### Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON)
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. Brand used for box/tag. **Exclude URLs.**
- Bolded first text = name/brand; non-bolded text below = description. Postfix carries "ea"/"kg"; prefix carries "_ for" (with prefix amount).
- Watch date-specific items — add the specific dates to items with a callout.

### Image QC
- Use a clean PDF image when available (almost all items have one); do not use if the product is cut off. Otherwise use the cutout.

## Post-processing / FQC (owned by Flex)
- Page category QC: 1–3 categories per item except page 1.
- FQC: turn auto-stack off; Ops spot checks; confirm edit details/dates as above; page categories on all but page 1; check special sale dates; thumbnails (4 standard, per pricing zone).
- **IMPORTANT: verify correct pages are in correct zones** per the Flipp Store Versioning for the week (FTP).
- Merge skinny pages; flyer sorting order: Current Weekly, Preview of Next Week, Monthly.
- **Flyer Review type: Lite.**

## Out-of-processing
- Generic codesheet path (discontinued Westrose/monthly flows retained in the OneGuide): download Store Versioning `.xlsx` from SFTP, remove WESTEROSE files row, paste page names into the codesheet generator (Backend tab → Export → paste values-only into Copy of Export), verify stores and page names match the SFTP, download CSV. **Config = `generic`; check all toggles except the second and last.**
- **Cloning process (BLFD, Pinetree) and FSA Dedupe custom action are currently discontinued** — do not perform unless reinstated.

---
*Source: Buy-Low Foods OneGuide (Google Doc `1Guz-uUxRF7o0vEHBV4DJ7swShL3JCTjhicRNAj4f0V8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
