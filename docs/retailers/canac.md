# Canac — Processing Guide

> **Source:** Canac OneGuide (Google Doc `1aBXgXrDOfOUZbdZU1Y0Vic4FBCP414BE0l0b0LYr5NA`), updated May 12, 2026. Contacts/credentials omitted.

> **Bilingual (EN/FR) Québec retailer.** Two flyer versions: **C** and **CP**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#canac` |
| Flyer types | Weekly (versions C and CP) |
| Processing | Auto-stack; Flex (Unique Shift Type 3FL + Flyer Review); no coupons; no Feedel |

## Files & schedule

- **Files received:** Monday. **Preview date:** Sunday (live date one day before valid date).
- **Cadence:** Available From Wednesday · Valid From Thursday · Available To Wednesday · Valid To Wednesday.
- **Linking/tagging document:** yes — found in the SFTP; search "xls" and download the XLS matching the flyer run name (e.g. flyer run c17 → `c17.xls`; c17p → `c17p.xls`). Attach to all vendor tasks via **mass attachment** ("+").

## Upload & setup (owned by Vendor)

**Version C:** select ONLY the version-C file name (check the upper-case file folder for additional pages). Manual upload into the correct run; ensure correct language (EN + FR); live date one day before valid; attach tagging doc to all vendor tasks.

**Version CP:** select ONLY the CP file name. Manual upload; select language French. Pricing zones — **French: include all pages; English: toggle "cross language" → select English → upload all pages.** Live date one day before valid; attach the CP tagging doc.

## ⚠️ Common errors / risk items
- **Unique Page 1 for additional locations (top risk):** when setting up zones for both versions, check for a unique Page 1 for other locations. **Do NOT bundle additional zones into the base pricing zones** — create two dedicated zones per additional location (e.g. `Salaberry EN`, `Salaberry FR`). Store assignments for additional zones are in the ClickUp task; each cover page names its store (except the base cover).
- **During FQC, verify (against the ClickUp task) the correct number of pricing zones were created and each zone has the correct version of Page 1 with NO DUPLICATES** — zones have been missed and multiple Page-1 versions assigned to the same zone. Flag to processor if wrong.
- **Look for multiple products** — box each SKU separately when a product block has multiple SKUs.

## QC specifics

### Box Draw (Low; Auto-Box OFF, Box QC bot OFF)
- Linking document required (box-specific). **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each individual SKU separately within a multi-SKU product block.

### Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select OFF)
- Linking document required (tag-specific). **Include:** name, pre/postfix, description, SKU, price, sale story, categories, original price, URLs. **Exclude:** valid dates, disclaimer. Brand is box/tag-specific.
- **Include the SKU in BOTH the description and the SKU box.**

### Image QC (data-piped check)
- Overview > Item Image QC → **untoggle "data piped"** → filter. Items that appear need a data-piped URL — fix them; if an item is not on the merchant website or there is any concern, reach out to the DOC.

## Post-processing / FQC (owned by Flex; complete by EOD Monday)

- **Item Category QC (DOC):** ensure items have Google Categories.
- **Item Image QC:** Monday morning, send the flyer link to the Flex-Canac channel for image QC. To verify: Image QC → unselect data piped → search → per item, copy SKU → search canac.ca. If the item exists, copy the white-background image URL into **Override Image URL**; if not, select the white PDF, else a cutout (retailer may flag missing images — if not on the website, tell them so). Ensure data-piped images are selected.
  - **Workaround if image QC won't push to front end:** confirm an override image URL exists, refresh "generate sibling groups" (retriggers data pipping), and wait ~1 hour after the task finishes.
- **URL/Links QC (DOC):** Overview > Items Without URL → check appearing items against the retailer's linking document.
- **External run name:** Overview > Edit Details. C## flyers → EN "Help for Real" / FR "Aide Pour Vrai"; CP## → use the publication name on page 1.
- Standard 4 thumbnails; confirm valid date matches publication and there's a 1-day preview.
- **Preview links** sent before 1PM Tuesdays.

## Ad-hoc — Canac New Brunswick (CNB) cloning
1. Clone the regular weekly run into the CNB run.
2. Remove all stores from each pricing zone.
3. Via Custom Action, assign FSAs **E3V, E4P, E7A, E7B, E7C, E8E** to the Rivière-du-Loup pricing zone.
4. Proceed with standard QC. **(NB processing ends May 20, 2026.)**

- **Flyer Review type: Lite.**

---
*Source: Canac OneGuide (Google Doc `1aBXgXrDOfOUZbdZU1Y0Vic4FBCP414BE0l0b0LYr5NA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
