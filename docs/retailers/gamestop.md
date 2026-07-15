# GameStop — Processing Guide

> **Source:** GameStop / EB Games OneGuide (Google Doc `1cU4aPMgOuJkdvrPUK_M5NjjCwg9vhVfBxu__EJ2r6Ps`), updated Feb 3, 2026. Contacts/credentials omitted.

Runs under the EB Games banner in Flipp. Bilingual (EN/FR) with Quebec-specific "ECO" pages.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#ebgames`, `#flex-processingsupport` |
| Hosted URL | N/A |
| Flyer types | Weekly (Type 1) · Monthly (Type 2) |
| Processing | Auto-stack; Flex (Flyer Review), OS (Setup); no coupons; **Feedel processing (yes)** |

## Files & schedule

- **Files received:** Ad-hoc; retailer sends file-drop notifications and instructions by email. Sometimes sends URLs with UTMs.
- **Cadence:** Ad-hoc (Available/Valid Ad-hoc).
- **Setup owned by** DOC; FQC by FLEX.

## Upload & setup

- **Create Flyer run:** Flyer run type = Flyer; Distribution Categories = Electronics; Internal Run Name = Date-Month.
- **Manual Upload:** files in SFTP; change language to **French** for all pages labeled **FR**; Auto Group → Save and Complete.
- **Pricing Zones (English & French versions):** separate zones for English pages, French pages, and **ECO** pages (you won't always receive ECO pages).
- **Store assignment:**
  - All ECO pages (French and English) → **Quebec region.**
  - The rest → **National-excluding-Quebec.**
  - If only ENG and FRE pages are received, distribute both versions **nationally.**
- Setup QC: dates match PDF, hide in hosted, no theme unless specified, Standard 4 thumbnails, mark items In-Store Only, check pages/zones/sessions/vendors. **Attach the linking document to vendor tasks.**

### ⚠️ Common errors / risk items
- Geography can change WoW depending on whether ECO/Quebec pages are present.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot OFF):** include special weblinks; exclude coupons, packaged deals, retailer logo, sign-up page, social media.
  - If a multi-item name has **"or"** and the price says **"ea.,"** box the products separately.
  - If multiple items sit under one banner (e.g. "Available Now," "50% off") and the linking doc has only **one URL**, box and tag the items separately.
- **Tag / Tag QC (Low; linking doc required; Auto-tag OFF; PDF Image Auto Selection ON):** include name, description, **SKU**, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude pre/postfix and valid dates.** Brand is box-specific.
  - Add SKUs in the **description** field. SKU found alongside certain games; if none, omit. Names are sometimes obscure.
- **Image QC:** select clean PDF when possible, cutouts if none available.

## Final QC / go-live notes

- Mark Auto Stack Spotcheck complete; check dates vs. PDF; hidden in hosted; mark items In-Store Only; Standard 4 thumbnails.
- Pricing zones: ECO → Quebec region, all others → National (excl. Quebec); confirm EN/FR language settings.
- **Ignore** the "Not all categories that are used in pricing zones have thumbnails" warning.
- **Flyer Review type: Lite.**

## Out-of-processing

- Instructions for page swaps / post-live checks live in the OneGuide (not filled in here).

---
*Source: GameStop / EB Games OneGuide (Google Doc `1cU4aPMgOuJkdvrPUK_M5NjjCwg9vhVfBxu__EJ2r6Ps`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
