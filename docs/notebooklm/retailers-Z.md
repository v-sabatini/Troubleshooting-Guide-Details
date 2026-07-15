# Retailer Processing Guides — Z

> Bundle of 1 retailer-specific processing guides (Z). Contacts and credentials are omitted from every guide.

**Contains:** Zehrs


---

# Zehrs — Processing Guide

> **Source:** Zehrs OneGuide (Google Doc `1d4D9o7NxZu8eRaYYSk4PUceHTOI0AhT_UVzs9bWw3UI`), updated Dec 18, 2025. Contacts/credentials omitted.

> Loblaw (LCL) banner. Cross-language retailer (English + French PZs for every zone).

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core · Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | zehrs.ca |
| Flyer type / cadence | Weekly (+ occasional ad-hoc / seasonal content) |
| Processing | Auto-stack; **3FL** (Flex) upload, DOC FQC; no coupons; **Strategic Ops / Feedel: yes** |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Wednesday, Valid From Thursday; Available To Wednesday, Valid To Wednesday.
- **Preview date:** Sunday (internal preview for processing); 1-day consumer preview.
- Prior to Flex's upload shift, **DOC must drop the Final Codes** in the shared LCL Codesheet Drive.

## Upload & setup (owned by Flex)

### ⚠️ NEW 2026 — Set Pixel Height to 4096
**Must be done before any pages are uploaded.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were added first, flag to the Full-Time Ops stakeholder and continue.

### Weekly upload (config `zehrs`, toggles 1/3/4/5/6)
- Find the codesheet in the LCL Codesheets folder (`ZEHRS`). Use the correct week number (e.g. `WK6 ZEH FINAL CODE SHEET_R1`); if a revised file exists (R1, R2…), use it.
- **Codesheet manipulations:** delete the **Print** tab; delete the **Effective Date** formula; delete **Row 6** (the date row); add a **"LEGEND TO MATCH CODES"** row above the stores table; delete all store totals; repeat for **all tabs**; delete hidden tabs.
- Download as **.xls** and upload.
- **Check Stale FTP for missed pages immediately after upload** and upload any missed.
- **PZs:** not all get built — the codesheet sometimes only pulls certain PZs. Check store totals to see which pulled; otherwise manually build each PZ (with a **cross-language French version for each**). Assign stores via CSV. Match PZ names to codesheet tab names (helps with zone-specific page swaps).
- **Cross-language FR PZ to French (all zones).** Add codesheet URLs to Notes for FQC reference.
- **Manual upload:** upload all pages, then build all PZs individually (EN + FR per zone).

### Setup QC
- Sunday preview (Edit Details → Preview start date → the Sunday before available date). 1-day consumer preview.
- **No theme.** Spotlight = "Weekly Deals" unless a special pub.
- **External Run Name** = `Weekly Flyer - Valid Thursday, Dec 28 - Wednesday, Jan 3` (example format).

### ⚠️ Error troubleshooting
- **Most common:** multiple pages match in the FTP — if that's the only error, **Force process**.
- Otherwise re-check codesheet manipulations and hidden tabs; watch for added characters in Pricing Zones (processors won't run).
- **"Found a reused PDF file within the same pricing zone layout":** check for duplicate pages in the codesheet; if none, do a manual upload, or delete the rows at the page positions named in the error backtrace (per zone) and **update the page-position column numbers**. Removed pages must then be added manually.
- Re-check FTP after upload for pages that didn't pull in; manually upload and add to correct PZs.

## QC specifics

### Box Draw (HIGH complexity; Auto-Box ON, Box QC bot OFF)
- No linking document. **Include:** coupons, packaged deals, sign-up page, special weblinks. **Exclude:** retailer logo, social media.
- Draw a box only where there's a unique price; box only the item, not surrounding areas.
- **Do NOT box** branded banners/backgrounds unless they have pricing, and **do NOT box** banners with contest callouts.
- **Page-level categories** during box draw for all pages **except the front cover**: Deli & Ready Meals, Bakery, Meat & Seafood, Dairy & Eggs, Drinks, Baby Needs, Household Supplies, Beauty & Skincare, Medicine & Health, Frozen, Produce.
- **Interactive buttons** ("click here") → box.
- **CON FLAP page** → draw one box on the full page, link out to the PC Optimum load URL (in the OneGuide).
- **'No name' banners** throughout → box and tag as a **LINK** to `https://www.zehrs.ca/collections/no-name`.
- **Joe Fresh callouts** → box and tag as a **LINK** to the Joe Fresh URL (in the OneGuide).

### Tag / Tag QC (Medium; Auto-tag ON, PDF image auto-selection ON)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Brand:** as seen (tag only the name, not the price).
- **Name:** ALL CAPS; order "Brand Product Name, Quantity" (comma before quantity); English only (French → description); exclude metrics like "6.59/kg", "Product of…", "No 1 Grade", "Frozen", "Selected varieties" (those go in description).
- **SKU:** starts with "2"; drop leading zeros; include unit of measure (e.g. `_KG`) in both SKU and Article Number. If a number doesn't start with "2", ignore it.
- **URLs:** click Fetch after entering SKU; open the link — if it leads to a *different item* or *different size*, remove it and search by product name; if it leads to the Loblaws **home page** or the correct item in a *different flavour*, **leave it**. All items with a SKU will have a URL.
- **Article Number** (special fields at bottom): copy Product SKU in; AN1 = SKU/Fetch value; include unit of measure; multiple SKUs → AN1, AN2, AN3, AN4.
- **Price:** as on flyer; watch multibuy (prefix + postfix); PC Optimum member pricing = Current Price with a **"PC Optimum Members Pricing"** prefix.
- **Sale Story / PC Optimum:** add "PC" in front of "PC OPTIMUM" (text extraction drops it).
- **Valid dates:** only add overrides when a promo sale story on the item indicates it.

### Image selection
- Use clean PDF where possible; cutout if the PDF isn't clean.

### Links QC
- Different item / different size → remove link. Zehrs home page or correct item different flavour → leave link.

## Post-processing
- **URL/Links QC (DOC):** reference the Final Codes; links in the Notes section; Flex should tag them — verify their work.
- **Pre-FQC (Flex):** mark Autostack Spotcheck complete; tackle spotchecks; **leg heights 45/25**; Standard 4 thumbnails (start where logo is); Image QC → mark complete; merge flap page to the right; tag codesheet URLs.
  - **Article Number check #1:** AN1 IS blank AND URL IS NOT blank → fill AN.
  - **Article Number check #2:** AN IS NOT blank AND URL IS blank.
  - Put flyer run ID in the LCL tracker; check sessions, geography, PZ → Items boxing, and warnings on the front.
- **Flyer sorting:** current flyer → upcoming flyer → secondary pubs (newest → oldest).

## Final QC / go-live notes
- **FQC (DOC):** add flyer ID to the LCL Tracker by Tuesday afternoon.
- **Live-date flags:** URL leading to a different item → **FLAG**; item quantities put into the description → **FLAG**.
- **Flyer Review type: Lite.**

## Out-of-processing
- Put flyer run ID in the LCL tracker.
- **Flyer sorting:** current weekly first → upcoming weekly → secondary pubs (newest → oldest).
- **Page swaps** often cause **page-stitching issues** (visible page doesn't match item positions), especially post-live. Best practice: **always rerun Page Tile Generation** after the swap sessions kick off; if issues persist, rerun and mark complete Vendor Box Tag onward; open the item view of *all* PZs to confirm the swap succeeded.
- Standard page swap otherwise.

---
*Source: Zehrs OneGuide (Google Doc `1d4D9o7NxZu8eRaYYSk4PUceHTOI0AhT_UVzs9bWw3UI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
