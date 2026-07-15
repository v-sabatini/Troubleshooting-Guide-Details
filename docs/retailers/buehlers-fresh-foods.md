# Buehler's Fresh Foods — Processing Guide

> **Source:** Buehler's Fresh Foods OneGuide (Google Doc `1GuhP37Z0s_bkCzxhG-3C3kOCRULe3m3EfREvR-JR2Ew`), updated Jun 26, 2026. Contacts/credentials omitted. (SpartanNash independent partnership.)

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#spartannash-independent-partnership`, `#flex-processingsupport` |
| Hosted URL | Metcalfe's |
| Flyer types & cadence | Direct, Weekly |
| Processing | Auto-stack; Flex (Processing Support, owns Setup & FQC); no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** weekly, via SFTP.
- **Publication:** Available From Tuesday (1 day prior to PDF); Valid Wednesday → Tuesday (match PDF); preview / linking doc N/A.

## Upload & setup (owned by Flex)

- Files in SFTP. **DO NOT upload the region key files** — those go only to the Vendor Tasks.
- **1 pricing zone, English, all pages, all stores.**
- **Build the SKU document:** download `flyer_zone_deals.xlsx` from FTP; delete columns zone, image_name, department, card_required, promo_text, deal_start_date, deal_end_date; rename `product_codes`→`SKUs` and `Title`→`Name`; reorder/sort by page number; rename to "Buehler's *Ad Live Date* SKUs" and download as XLSX.
- Attach the **Region Key files** and the manipulated SKU document to vendor tasks, with the note instructing taggers to add the "Product Codes" from the SKU sheet that match the hand-written number in the "Sale Group" column of the Key PDF.
- **Reorder pages** to match the Region Key document.

### ⚠️ Common errors / risk items (retailer-specific)

- **SKU tagging is the key risk.** Tag SKUs **only** by matching the hand-written IDs in the Key PDF against the `sale_group` column of the SKU sheet — **DO NOT search by name.** Remove any trailing comma/period from the SKU field.
- If a Key PDF item block shows **2 codes**, box each item separately.
- **Buy # Get # Free deals:** use the exact case-sensitive format `Buy # get # free` OR `Buy one get one free` (incorrect formatting breaks the retailer's website). Buy#Get# always goes in the Sale Story; current price stays empty; single quantities and regular retail go in Original Price.
- **Do NOT** add "with your Advantage Card" / "With Card" to the Sale Story or Disclaimer.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, Box QC bot OFF. No linking doc.** Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Two codes on one Key-PDF block → box separately.
- **Tag / Tag QC — Low. Auto-tag OFF. Valid dates excluded.** Include brand (used for box+tag), name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. SKU tagging as above (Key PDF hand-written ID → sale_group → SKUs).

## FQC / go-live (owned by Vendor)

- **Add missing SKUs:** Overview → Item Search → SKU IS blank; cross-check the Key PDF product ID against the `sale_group` column of the SKU sheet and add.
- **Remove exclamation marks** from Sale Story/Disclaimer; **remove "With Card"/"With Advantage Card"** from any Sale Story.
- **Upload the insert** (from Drive) to the last page of the base pricing zone — no boxing/tagging.
- Confirm page order matches the Region Files Key document; enforce the Buy#Get# format.
- Standard checks: vendor tasks complete; geography consistent; vertical/horizontal previews; dates (Available From Tuesday 1 day prior, Valid Wed → Tue, match PDF).
- **Flyer Review type: Medium.**

---
*Source: Buehler's Fresh Foods OneGuide (Google Doc `1GuhP37Z0s_bkCzxhG-3C3kOCRULe3m3EfREvR-JR2Ew`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
