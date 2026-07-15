# Atlantic Superstore (RASS) — Processing Guide

> **Source:** Atlantic Superstore OneGuide (Google Doc `1VIwdBqsAqZbewJcGryrTA0vT5Rm7fZDxXc3OfJP_Flc`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (relationship quality: Excellent) |
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer type(s) & cadence | 5892: Weekly · 10549: General Merchandise (owned by Docs) |
| Processing | Auto-stack; Flex (Flyer Review); OS Setup; **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Tuesday / Valid From Thursday / Valid To Wednesday. **Preview:** Sunday.
- **Workflow:** Upload/Setup by Vendor; Article Numbers by Flex; FQC by DOC. Part of the Loblaw/LCL codesheet program (RASS = Real Atlantic SuperStore; DOM = Dominion).

## Upload & setup (owned by Flex) — Config `atlantic_superstore`
- **NEW 2026 — Set Pixel Height to 4096 BEFORE any pages are uploaded.** Edit Details → show rarely-used fields → Height dropdown → 4096.0 px → OK. If pages were added first, flag the Full-Time Ops stakeholder and continue.
- **Codesheet manipulation:** open the RASS DOM Final Codesheet; delete the hidden Date, Store Ledger and Print tabs (leave only pricing-zone tabs). For each tab: copy the PZ name into A1 (replacing "Effective Date:"), delete the `#ERROR!`/formula in B1, convert the `=TODAY()` date to plain text. Add **"& BASE ENGLISH"** to zone names. Unmerge any merged pagination cells and delete blank rows (prevents pages not pulling in). Download as .xlsx.
- Split into RASS (delete Dominion PZs, subtotals/totals) and DOM (delete RA PZs; drop a tab if it only has RA PZs) code sheets.
- Codesheet upload: **Config `atlantic_superstore`**, correct base path, **checks = all but the second and last**. Common error: "file codes match multiple files" → force process, then manually upload anything missing.

## ⚠️ Common errors / risk items (retailer-specific)
- **Shared pages between banners:** because RASS and DOM share certain pages (e.g. FLAP CON or GM pages), pulling a page for one banner marks it uploaded in the FTP. **Remember to manually upload those shared pages for BOTH RASS and DOM.**
- **Store assignments pulled incorrectly (RISK):** stores may appear assigned but the count won't match the codesheet, with overlaps. Fix: delete all stores from all zones, build a generic-stores codesheet and upload it.
- **French cross-lang zones:** naming often has a space between the dash and "FR", which errors when running codesheets. EN stores will run; copy the FR zone name from the individual PZ interface and paste it into the codesheet.
- **Tag all "PC Optimum" buttons** with the pcoptimum.ca link. **Tag all Joe Fresh pages** as ONE box / direct link with the joefresh.ca link.
- Check the correct pages pulled in (RASS: RA or RA/DA only; DOM: DA or RA/DA only). Geography shouldn't change week over week.
- External Run Name: "Weekly Flyer - Valid [dates]". Set a **Sunday preview** start date.

## QC specifics
- **Box Draw (Medium; Auto-Box ON, Box QC bot ON):** **Include** coupons, packaged deals, special weblinks (draw a box over any PC offers with a URL). Exclude retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields; linking doc is Tag/QC specific. Name in ALL CAPS as "Brand Product Name, Quantity" (comma before quantity), English only; French verbiage → description. Do not put unit-price metrics ("6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — those go in description. **Article Number fields:** copy the product SKU (with unit of measure suffix e.g. `_KG`, `_EA`, `_LB`) into Article Number 1 (= SKU/Fetch URL); multiple SKUs map to Article Number 1/2/3/4 in order.
- **URL/Links QC (DOC):** reference Final Codes, links live in the Notes/URL column (col E). Box the linked area (usually the page header or a Shop Now/Click Here button) and tag as **Direct Link, not Item.**
- **Image QC:** PDF preferred unless unclear; meat/fish must be in a package or use the cutout; white background only, no lifestyle backgrounds.

## FQC / go-live (owned by DOC)
- Spotchecks; add codesheet URLs (PC Express / Joe Fresh); merge flap pages via storefront spotcheck; mark AutoStack Spotcheck complete; no overlapping FSAs (re-generate if needed); leg heights 45/20; thumbnails Standard 4 (start on 2nd/3rd page if flaps lead); spotlight "This Week's Savings".
- **Article-number check:** Item Search `SKU IS NOT blank` + `URL IS blank` → open item, Fetch to populate URL; then `Article Number 1 IS blank` + `URL IS NOT blank` → add article number. Spot-check 2nd Article Number fields.
- Page categories: page 1 gets none, each page 1–3 categories. Open the LCL Tracker (done by 2:30 Monday), enter flyer IDs for RASS and DOM. Check sessions, vertical scroll, vendor assignments, boxing, red warnings, flyer sorting (most recent on top, secondary pubs last).
- **Flyer Review type: Lite.**
- **Additional publications:** create a run in the GM/Specialty Grocery flyer type, manual-upload English pages (Provigo = French), 1 EN zone + 1 cross-lang FR zone (Provigo needs all pages French for vendor tasks + cross-lang to EN), assign stores per codesheet.

## Out-of-processing
- Standard page swap (per training video).

---
*Source: Atlantic Superstore OneGuide (Google Doc `1VIwdBqsAqZbewJcGryrTA0vT5Rm7fZDxXc3OfJP_Flc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
