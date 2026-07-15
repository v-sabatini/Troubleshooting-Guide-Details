# Your Independent Grocer — Processing Guide

> **Source:** Your Independent Grocer OneGuide (Google Doc `1K5FvZ32ltiUeonhxuUWtmqQuLoBLKZY5MHRZxioYw98`), updated Feb 9, 2026. Contacts/credentials omitted.

> Loblaw (LCL) banner. Covers three sub-banners: **YIGO** (Ontario), **YIGW** (West) and **YIGA** (Atlantic).

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblaw-lcl`, `#loblawops` |
| Merchant IDs | 2337 (weekly); Flyer types: Weekly = 5892, General Merchandise = 10553 |
| Flyer type / cadence | Weekly (+ General Merchandise, owned by Docs) |
| Processing | Auto-stack; OS setup, Flex Flyer Review; no coupons; **Strategic Ops / Feedel: yes** |

## Files & schedule

- **Files received:** Monday.
- **Cadence:** Available From Tuesday, Valid From Tuesday; Available To Monday, Valid To Tuesday.
- **Preview date:** Sunday (1-day consumer preview).
- Prior to Flex's upload shift, **DOC must drop the Final Codes** in the shared LCL Codesheet Drive.

## Upload & setup (owned by Flex)

### ⚠️ NEW 2026 — Set Pixel Height to 4096
**Must be done before any pages are uploaded.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → select **4096.0 pixels** → OK. If pages were already added first, flag to the Full-Time Ops stakeholder and continue.

### YIGO Weekly (config `your_independent_grocer_ontario`, toggles 1/3/4/5/6)
- Open codesheet; delete the **Print** tab and the hidden **Date** tab.
- For all tabs: change "Date"/"Printer Notes" → **"NOTES"**; shift Info Table header cells (usually A1–B7) **one cell to the right**; delete the `#ERROR` formula in B1; delete store-count subtotals/totals at the bottom of the stores section; add the tab name to each Zone; add **"BASE ENGLISH"** above store names.
- **⚠️ Risk item:** there must be a **"Legends to Match Codes"** row above the zone name and base English so all zones are pulled.
- Download as **.xls**, upload each tab.
- If you get a "pages matching" error, ignore and **Force process**; any other error → check manipulations and that all stores are in Fadmin with the right store code.
- **Check Stale for missed pages** and add to the PZs. **Copy layout from ENG and cross-language to FR.**
- **⚠️ Risk item:** check Online Suppressed PZ pagination vs codesheet — it should have **no Online pages**.

### YIGW Weekly (config `your_independent_grocer_west`, toggles 1/3/4/5/6)
- Delete Print tab and "City" tab(s). Per tab: shift Info Table header right; delete the Date cell; delete formulas (e.g. `#ERROR`); delete "Legend to match zones" rows; add **"ZONE ENGLISH"** to zone names; add tab name to zone code (e.g. WB NV); delete store subtotals/totals. The last "CITY" tab isn't in the run — delete it.
- Download each tab separately as **.csv**, upload each.
- **Copy layout from ENG and cross-language to FR zones.** Check FTP for missed pages; "city"-named files can be checked off; Online pages rarely get pulled — pull them in manually via the layout tab.
- **Missing FSAs:** Online WY generates only one FSA, shared with Online WY NV — assign it to the zone with the **most pages** (e.g. if Online WY NV has an extra "NV" page, assign it there), confirm geo works, and leave a note. Zones with zero FSAs are rarely flagged (known/accepted for YIGW).

### YIGA Weekly — Manual upload
- Open codesheet for pagination reference. Go to the weekly flyer → Pages → Edit → drop down the week → select all files and upload.
- **Re-order pages (do NOT autogroup)** to codesheet order. Note **NFLD** and **MAINLAND** zones differ in page name (Mainland = YA, NFLD = YN).
- Save and complete → start Flyer Creation (in WES) → create PZs **ONLINE MAINLAND** and **ONLINE NFLD** → assign YA pages to Mainland, YN pages to NFLD → **copy layout from ENG, cross-language to FR** → save and complete.
- Add stores per the store set for each zone; **Online Mainland gets both Mainland and PCO Mainland store sets.**

### Setup QC (all banners)
- Preview date = Monday; 1-day consumer preview.
- **External Run Name** = `Weekly Flyer - Valid ______` (e.g. "Weekly Flyer - Valid Thursday, Jun 12 - Wednesday, Jun 18").

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- No linking document. **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons.
- Box each product block; box any inserts / sign-up pages.
- **⚠️ PC Optimum button:** box and tag as a **link to https://www.pcoptimum.ca**.

### Tag / Tag QC (Low; Auto-tag OFF; linking document required)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.**
- **Name/Brand:** as on the PDF. **Description:** flyer info only (never from the website); not bold; first letter capitalized; metrics like "6.59/kg"; "Product of…", "No 1 Grade", "Frozen", "Selected varieties"; do not put NG code/SKU here; enter **both English and French** if present.
- **Price:** as on flyer. Member-only pricing → Current Price = member price; put "$X.XX Non-member price" in **Disclaimer text**.
- **SKU:** enter the flyer SKU; if multiple, enter only one; include the unit of measure (e.g. `_KG`) in both the SKU and Article Number fields.
- **Article Number** (special fields at bottom of Tag interface): copy the Product SKU in; Article Number 1 = the SKU/Fetch URL value; include the unit of measure; multiple SKUs → first→AN1, second→AN2, etc.
- **Sale Story / PC Optimum:** add "PC" in front of "PC OPTIMUM" (text extraction drops the "PC").
- **Page categories** tagged during Box Draw, ≥1 of: Fruits & Vegetables, Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Pantry, Natural Foods, Baby Needs, Pet Food & Accessories, Household Supplies, Beauty & Skincare, Personal Care, Medicine & Health, Diet & Nutrition.

### Image QC
- Use clean PDFs.

## Post-processing (owned by DOC)
- **URL/Links QC:** reference the Final Codes; links are in the **Notes/URL's** column E. Box the linked area (often the page header, or a Click Here / Shop Now button) and tag as **Direct Link, not Item**.

## Final QC / go-live notes (owned by DOC)
- Same process for all YIG banners. Mark Autostack Spotcheck complete; complete spotchecks.
- **Leg heights 40/30.** Standard 4 thumbnails (start where the logo is). Image QC = clean PDFs.
- Open the week's codesheet → per tab see which PZs get links; box to add the link if OS didn't (usually the PC Optimum on Flap 1). Joe Fresh links are pre-tagged by OS — update per codesheet if needed.
- Merge flap pages (skinny pages): 2 flaps → merge together; 3+ → merge first two, then next flap to the broad page.
- **Article Number check:** Item Search → Article number 1 IS blank AND URL IS NOT blank → fill AN, SKU, URL.
- Check geography; PZ → Items → double-check boxing.
- **Add the Article number to the LCL tracker.**
- **Flyer sorting:** current flyers (order ONT, WEST, ATL) → upcoming flyer.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page swap:** standard.

---
*Source: Your Independent Grocer OneGuide (Google Doc `1K5FvZ32ltiUeonhxuUWtmqQuLoBLKZY5MHRZxioYw98`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
