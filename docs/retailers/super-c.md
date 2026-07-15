# Super C — Processing Guide

> **Source:** Super C OneGuide (Google Doc `1_gzIS8CZR04JYcgBjeBtMIXnJyyw64-e_385NSvVd8o`), updated Feb 10, 2026. Contacts/credentials omitted.

> Super C is a **Metro banner** (French, Quebec). We do not power their hosted site.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#metro`, `#metro-ops` |
| Hosted URL | N/A (we do not power their hosted) |
| Flyer type | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Thursday. **Cadence:** Available Tue→Thu, Valid Wed→Wed.
- **No linking document.** Store codesheet arrives via email; pages and tracking sheet come via SFTP.

## Upload & setup (owned by DOC)

**Store codesheet upload (creates pricing zones only — no page info):**
- Open the store-assignment spreadsheet; recolor the currently-visible version headings, then unhide and delete all hidden columns (delete every orange-heading column).
- Rename heading "site number" → **"No site"**; delete blank column A. Save as .csv.
- Upload: **only toggles 1 & 4 checked** (Store or Store Set Assignment and Allow Pricing Zone Creation), **config `super_c`**, PDF base directory `/` (the pop-up warning is OK).
- Verify pricing zones — there will be two of each: one **base French** and one **cross-language**.

**Page upload:**
- Upload all pages from the **PDF_FINAUX** folder for the week (labeled by date code). **Do NOT use the BlockID folder.**
- Mark all as **French pages**; auto-group page numbers; Save and confirm.

**Page order:** find the "tracking" sheet in the SFTP for the week and use it as reference in Flyer Creation. Confirm the zone at the top of each tracking-sheet section matches the Fadmin zone; repeat for all base zones. For **CL (cross-language)** zones: unselect the cross-language toggle, switch language English→French, copy the base zone layout (e.g. NAT → NAT CL), then re-check cross-language and switch French→English. Repeat for all CL zones.

**CAHIER (booklets):** occasional extra 4–7 page publications (pages labeled CAHIER in the SFTP); page order is in the tracking sheet under the weekly flyer. No codesheet — create a new flyer run under the weekly flyer type, upload all pages as French, create two zones (base French + "base cl" cross-language), assign all stores.

## ⚠️ Common errors / risk items (retailer-specific)

- **Names are tagged FRENCH first, ENGLISH second.** The English name is found in the description on the last line in **bold**. **Do not tag the Brand field.** Multiple items: first name in Name field, additional names in Description separated by line breaks.
- **"Voir prix en magasin" is a Sale Story, NOT a description.** "Voir variétés en magasin" IS a description — keep it in line with the last item, **do not separate with a line break**.
- **ECONO PACK** ("Format écono") goes in the Description field, not the name.
- **Block ID goes in the SKU field** (from the text-extraction field), upper case, multiples separated by commas. If cut off or "NOBLOCKID", leave SKU **blank**. **If no Block IDs appear in the text extraction at all, notify the Flipp team immediately.**
- "Buy One Get One" deals: include "À l'achat d'un…" + the required product in the Name field, and "Obtenez pour…" + the get-item info in the Description field.
- Keep capitalization exactly as on the page.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box single items with a price; box multi-items sharing a price in one box; BOGO in one box.
- **Tag / Tag QC (Low; Auto-tag OFF; no linking doc):** Include name, description, **SKU (Block ID)**, price, sale story, categories, disclaimer, original price. **Exclude brand, pre/postfix, valid dates, URLs.** Retailer does not include original pricing.
- **Image QC:** clean PDFs when available; cutouts if none.

## Post-processing (owned by DOC)

- **Box & add links from the Tracking Sheet** in the SFTP as Display: Link (page names are in the tracking sheet's second column).
- Check pages for points callouts (tag in sale story); Item Search SKU blank → add SKUs from text extraction.
- Run the **Metro Links custom action** ("Set Metro Banners Items URLs"): find the file in the FTP under `/ZPO400 + Google Feeds`, copy the file name **without** ".csv", then add the tracking code from the Metro Banners Tracking codes sheet.
- **Final QC:** thumbnails Standard 4; SKU QC (add SKUs from text extraction, "NOBLOCKID" left blank); run the Metro custom action after SKU QC; add supplementary links from the tracking sheet; add the Super C tracking code last.

## Corrections & flyer review (owned by DOC / FLEX)

- **Corrections:** Super C uses Madmin for preview links; **FQC should be completed Monday morning** (they access previews by noon). Corrections come by email + SFTP by EOD Monday / early Tuesday and should be actioned within 24 hours (usually name/description updates via item search). ARB can be filed for this task.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Super C OneGuide (Google Doc `1_gzIS8CZR04JYcgBjeBtMIXnJyyw64-e_385NSvVd8o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
