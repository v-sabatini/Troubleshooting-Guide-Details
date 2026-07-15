# Linen Chest — Processing Guide

> **Source:** Linen Chest OneGuide (Google Doc `16cZeC5SyuuljARzONXYAxvgmTF59MadnY9iQ1gqyYZI`), updated Oct 23, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channel | `#linen-chest` |
| Hosted URL | linenchest.com/en_ca/flyers |
| Flyer type | Flyer (ad-hoc) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |

Bilingual (French + English). Linking document (URL sheet) + colour map sent via FTP.

## Files & schedule

- **Files received:** Ad hoc; all cadence dates are ad hoc (from the file-drop email).
- File-drop email contains dates, store info, page layout, and tracking code — use it for upload and FQC.

## Upload & setup (owned by Flex)

1. Download the **URL sheet (xls)** and the **FULL Colour Map PDF** from FTP (the capitalized document, not the individual page PDFs).
2. Manually upload pages — **use the lowercase "reebeeflipp Pages" folder** (all-lowercase filenames), NOT the colourmap pages. Autogroup to sort in order.
3. **Mass-attach the XLS URL doc and the Colour Map PDF to all vendor tasks.**
4. **Three pricing zones every week:**
   - **French** — all stores minus Chicoutimi (38 stores).
   - **English** — all stores minus Chicoutimi (38 stores).
   - **Chicoutimi** — only the Chicoutimi store (1). Confirm from the file-drop email whether Chicoutimi receives all pages.

## ⚠️ Common errors / risk items

- **Box count must match the spreadsheet** — sometimes one box covers multiple unique items. Always refer to the **Colour Map PDF** attached to the pipeline.
- **Descriptions:** include all item info (current AND original prices), formatted exactly as the example, with a paragraph line between each product's descriptions.
- Certain full pages must all be **DIRECT LINKS**.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc (Box Draw specific) required — the **Colour Map PDF** tells you which items to box. Exclude coupons, packaged deals; include retailer logo, sign-up page, social media, special weblinks. Multiple items can be one box (per the PDF).
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON):** linking doc (Tag/QC specific). Include brand (exactly as on flyer), name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU** (Linen Chest usually has none; include if present).
  - Tag using the text-extraction text, but **fix formatting** (missing `$`, spacing, line breaks) — do not blindly copy/paste. Include "Was"/"Now" (EN) or "était"/"maintenant" (FR) before prices.
  - **Multiple items/sizes:** Prefix "Starting at" (EN) / "À partir de" (FR); Current Price = lowest sale price. For range prices + multiple variations, tag only the lowest current and original price. For a single range price + no variation, current price + postfix + lowest original price.
  - **URLs:** add EN & FR URLs from the spreadsheet; naming per the merchant's linking doc.
  - **Display Type:** direct links for certain pages; "Item" if listed as "product page" in the spreadsheet; "Link" for "Page SLI"/"Category Page"/"Search Result".
  - **Categories** (EN/FR chart): Bath, Beds and Mattresses, Bedding, Décor, Electrics, Kitchen, Gifts, Glass & Barware, Tabletop. When unsure, confirm on linenchest.com.
- **Image QC:** use clean PDFs whenever possible; cutouts when clean PDFs aren't available.

## Post-processing & FQC (owned by Vendor)

- Item Category QC: Google + Analytical category for all shoppable items.
- Item Image QC: clean white-background image where possible, else cutout.
- URL/Links QC: add missing URLs from the file-drop email.
- **FQC:** Standard 4 thumbnails; check dates against email/publication; add missing URLs.
  - **Add flyer-run-level tracking codes:** Overview → Ad Hoc Processing → Manage Tracking Codes → Flyer Run Tracking Codes → Add: Code type **Dynamic Variable**, Source **All**, Variable **utm_campaign**, Value from the file-drop email.
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Linen Chest OneGuide (Google Doc `16cZeC5SyuuljARzONXYAxvgmTF59MadnY9iQ1gqyYZI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
