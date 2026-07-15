# JYSK — Processing Guide

> **Source:** JYSK OneGuide (Google Doc `1uw47tJzpdnJWYUPBNPOpSug3xv06RaTpoMg7a06r2bs`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | **Flipp only** (Flipp does not power JYSK's Hosted) |
| Slack channel | `#jysk` |
| Flyer type(s) & cadence | Flyer Type 1: **Flyer** · Flyer Type 2: **Grand Opening**. Bilingual EN/FR. |
| Processing | Auto-stack |
| Who's involved | Vendor (Upload/Box/Tag); DOC (Links QC, FQC); Flex (FAB tickets / Flyer Review); no coupons; no Strategic Ops/Feedel |

## Files & schedule
- **Files received:** Thursday.
- **Publication cadence:** Available Thursday → Wednesday; Valid Thursday → Wednesday. No preview dates (Available = Valid).
- **Linking document:** yes.

## ⚠️ Risk items
- **Linking errors:** many items share the same name — ensure links are added properly. **Check links during FQC.**
- **"Flyer not available on Hosted" is always a FALSE error** — Flipp doesn't power JYSK's Hosted; do not check their Hosted webpage.

## Upload & setup (owned by Vendor)

### Before upload — URL document manipulation
- Download the links file from SFTP (usually .csv); open in Google Sheets; rename the sheet to "[FLYER NAME] URLs" (e.g. "1089 JYSK URLs").
- In column D, add **EN** after "Flipp" to indicate English URLs.
- For French links, add **`&___store=fr`** to all FR links: paste `&___store=fr` into column E beside FR URLs; in column G use `=CONCAT(D2, E2)` to combine; autofill down; copy the new FR URLs and paste **Values Only** into column F; delete columns F and G.
- Save as **.xlsx** and attach to all vendor tasks during upload.

### Upload
- Manual upload; change language for French files (indicated by "F" in the name); Save (not Save and Complete). Then Auto-Group → Save and Complete (should look like a zipper).
- **2 PZs — English and French**; add all stores for both. Check sessions. Upload the links xlsx as a mass attachment to all vendors.

### Setup QC
- Ensure hidden in hosted; PDF dates match FAdmin; no preview dates (Available = Valid); Legibility Heights **40/30**; mark Setup QC complete.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc for box)
- **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Box/tag separately** items advertised together but with separate names (e.g. a chair and a table in a set) — check the linking doc has 2 links.
- Items that share a name but have **different prices** must be boxed/tagged separately (e.g. FYN 3 tiroirs / 5 tiroirs / 4 tiroirs; COLTON at 3 prices). Some items don't have a corresponding image on the flyer — **still box and tag them**.

### Tag / Tag QC (Medium; Auto-tag OFF; PDF image auto-selection ON; linking doc required)
- **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **⚠️ NEW 6/20/25 — Name rules (drive automations):**
  - Always tag the **bold word first** in the Name (EN and FR) — may mean adjusting the text-extraction box. E.g. "SUNI Outdoor placemat" / "SUNI Napperon extérieur".
  - When there's a slash in the name, **include the space** around it: "HEDEENGE / KELDMOSE Coussin de chaise".
  - Always include the **Brand name first** in the Name even if not visible in the box: "DUNBAR NIGHTSTAND" (not "2 Price NIGHTSTAND").
  - Use the brand printed **alongside** the item name, not text from another brand logo image.
  - Lists of names: **space after the comma** ("Hallgerd, Inhome").
- **URLs:** watch items with the same name but different numbers — the link may carry the matching number.

## Post-processing / FQC
- **URL/Links QC (DOC):** check for FR links on EN flyers (item search URL contains `&___store=fr` + Language English → swap to EN links). Check for name repetition in the link sheet using conditional formatting `=countif(B:B,B1)>1`; verify links for repeated names against page numbers in the URL.
- **Ad-hoc QC (DOC):** check all items are boxed.
- **FQC (DOC):** Standard 4 thumbnails; check items without URL; **mark items in-store only**; complete standard FQC checklist.
- **Flyer Review type: Lite** (owned by Flex).

## Out-of-processing
- **Day of go-live:** the external ops contact sends any link changes — make the adjustments and confirm. See the JYSK Clipping Instructions doc.

---
*Source: JYSK OneGuide (Google Doc `1uw47tJzpdnJWYUPBNPOpSug3xv06RaTpoMg7a06r2bs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
