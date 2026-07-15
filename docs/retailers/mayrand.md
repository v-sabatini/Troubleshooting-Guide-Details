# Mayrand — Processing Guide

> **Source:** Mayrand OneGuide (Google Doc `1qKx7bExVprWGPjE84y9LPOIlg77CttQbpMcQucwNWpg`), updated Oct 21, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#mayrand` |
| Flyer type | Weekly (11319) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons/Feedel |
| Languages | EN + FR |

## Files & schedule
- **Files received:** Thursday.
- **Cadence:** Available From Wednesday → Available To Tuesday; Valid From Tuesday → Valid To Wednesday. **Friday preview.**
- **Linking document:** Yes (English- and French-specific URL/tagging document).

## Upload & setup (owned by Flex)
- **Manual upload:** Pages tab → Edit → select all pages from SFTP → Confirm & Upload. Assign pages with **FR** in the name to French, **EN** to English. Save → Auto-Group (zipper) → Save & Complete (do NOT process internally).
- **Pricing Zones:** create **EN PZ** and **FR PZ**; assign English pages to EN, French to FR; add all stores to both.
- **Setup QC:** confirm all pages uploaded; confirm dates (first/last page); thumbnails Standard 4; **no preview date (Available = Valid)**; no theme.
- **⚠️ IMPORTANT:** before attaching the linking documents to vendor tasks, **delete columns E–AC**, save as `.csv`, then attach.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **include** retailer logo and special weblinks; exclude coupons, packaged deals, sign-up page, social media. Box any product block with a price or sales story; box all social media and weblinks.
  - **Only** box and tag these headers (EN or FR): *Nos Heures D'Ouverture / Our Stores*, *Service Personnalisé / Our Services*, *Site Internet / Website*.
- **Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** PDF preferred if clean; otherwise cutouts (owned by Vendor).

## ⚠️ Common errors / risk items — tagging (most valuable)
- **ALWAYS follow the URL/tagging document (EN- and FR-specific), NOT the PDF**, as the tagging guideline.
- **SKU goes ONLY in the SKU field** — never in the Name or Description.
- All text under the document's **Name** column goes in the FAdmin Name field (except the SKU). If a descriptor (e.g., "540 ml") is included under Name by the retailer, put it in the Name (no duplicate in Description).
- Information **not** in the tagging doc (e.g., "9.90$/kg") should not be in the Name but **should still be tagged**.
- Common incorrect examples: Name not following the URL doc; SKU duplicated in the description; brand name omitted from the brand field.

## Post-processing / FQC
- **Pre-FQC Links QC** — **there should be 0 items without URLs:**
  - Item Search → URL → IS → (blank): assign URLs from the linking docs.
  - URL CONTAINS `/en/` with Language French → confirm no French items get English URLs (and vice versa for `/fr/`).
  - URL CONTAINS `%3B%22` → remove that and everything after it from the URL.
- **FQC (owned by DOC):** dates correct per PDF; available on all platforms; thumbnails drawn and include the retailer logo.
- **Flyer Review type: Lite** (owned by DOL) — see the Mayrand flyer review guide.

---
*Source: Mayrand OneGuide (Google Doc `1qKx7bExVprWGPjE84y9LPOIlg77CttQbpMcQucwNWpg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
