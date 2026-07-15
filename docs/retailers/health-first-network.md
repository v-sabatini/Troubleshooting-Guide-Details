# Health First Network (buying group) — Processing Guide

> **Source:** Health First Network OneGuide (Google Doc `1dSCloBFD9dTObOhlccfwIKILDkTtMbDbyEq7G7mazpc`), updated Sep 17. Contacts/credentials omitted.

Buying group: one base flyer is processed then **cloned** out to many participant merchants.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only, **except** Gagne en Sante / Win in Health and The Peanut Mill (all platforms) |
| Slack channel(s) | `#healthfirstnetwork`, `#flex-buying-group-processing`, `#healthfirstnetwork-process` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Monthly |
| Processing | Auto-stack; Flex (unique shift type); no coupons; no Feedel |

- **Account note (2025):** system supports a max of 3 banners for linking; expansion needs more lead time and investment.
- **Custom action "Remove Stores"** — removes store 100 from all pricing zones, run as part of Setup QC.

## Files & schedule

- **Files arrive:** Monday (confirm with external ops ~17 days out). Assets land on **SFTP** (PDFs + XLSX codesheet, usually `FLIPP_MMYYYY.xlsx`); email sent on upload.
- **Cadence:** Available Wednesday / Valid Thursday. Timeline runs ~17 days out through post-processing.
- **Linking:** URLs processed only for **Win in Health / Gagne en Sante, Natural Focus, Naterro** (come post-processing).

## Upload & setup (owned by Processor)

- Import the XLSX into the **HFN Workbook**; run the numbered macros (1–5): clear formatting, format dates MM/DD/YYYY, rearrange columns, update headers, set "Store Set" = 100 for all rows, sort by launch date. Download tab as CSV.
- Confirm flyer dates from XLSX: earliest Start (MIN), latest End (MAX).
- Upload to flyer run — **config `health_first_network`**, PDF base dir = XLSX path.
  - **Toggles:** ✅ Store/Store Set Assignment, ❌ Region Assignment, ✅ Page Upload, ✅ Allow PZ creation, ✅ Use Page Pool, ✅ Tile Generate, ❌ Combine Zones.
- Run the codesheet.

### ⚠️ Common errors / risk items

- **"Files not named XX"** → PDFs misnamed vs codesheet; fix in the codesheet and re-run. Flag to retailer if high volume.
- Files present but not in the spreadsheet (or vice-versa) → always reach out to clarify.
- **Setup QC:** check created PZ count vs codesheet; run **Remove Stores** custom action (PZ ID = "all", stores = 100) and confirm 0 stores assigned; check SFTP for `000#.pdf` naming; confirm staggered dates set; spot-check pages aren't cut off.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Multiple images + multiple prices = box each; multiple images + one price = single box.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include Name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.** For uniquely-priced multi-items, include product volume/unit in the name.

## Post-processing

**Processor** completes FQC on the **"processing only"** base flyer (thumbnails, no stores assigned, PZs staggered, hidden everywhere, no theme, Tagged/Vendor QC counts match).

**FLEX** then **clones** the base flyer to active participants:
- Deselect "Clone To Health First Network" for each participant; clone up to 10 at a time (may time out); Copy Tracking Codes/URLs = No; clones take 15–30 min.
- Participant FQC: add stores to each merchant's PZ (Win in Health / Gagne en Sante = same stores); check staggered dates match PDFs (Available From = 1 day before Valid From, **except Ki Nature = 2 days**); QC 3 thumbnails; remove "processing only" from internal run name; availability Flipp + Distribution only (except the 3 all-platform banners).
- **NEW / RISK: Do NOT rerun sessions to clear red FQC warnings** — type **"CLONE"** into the field for each warning to turn it green and proceed.

Also documented: ClickUp workspace setup for Flex tasks, Product URL tagging (send/import to 3 clients), and Flipp Web Direct Links.

- **Flyer Review type: Lite.**

---
*Source: Health First Network OneGuide (Google Doc `1dSCloBFD9dTObOhlccfwIKILDkTtMbDbyEq7G7mazpc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
