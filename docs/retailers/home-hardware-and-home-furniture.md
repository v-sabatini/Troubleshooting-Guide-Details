# Home Hardware & Home Furniture — Processing Guide

> **Source:** Home Hardware / Home Furniture OneGuide (Google Doc `1X9HDiPthDAM6K59fwtSOqXPCfbQUNiMF4w3SxjaM8L0`), updated Mar 12, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ / Tier 1 |
| Availability | All platforms |
| Slack channel(s) | `#homehardware`, `#homehardware_sep`, `#homehardware_mergil` |
| Hosted URL | homehardware.ca |
| Flyer types & cadence | **Flyer (504)** bi-weekly (2 flyers) · **LBM (3520)** bi-weekly · **Pro Flyer (9711)** bi-weekly · **Specials (8741)** ad-hoc (incl. Catalogs/Guides) · Mount Forest custom flyers |
| Processing | Auto-stack; Flex 3FL / Flyer Review; DOC-owned setup & QC; Feedel/data services on Flyer (504) & LBM only; no coupons |

Key resource: the **HH Linking Document** (attached to all vendor tasks) — banner names, links, and item names all come from it. No retailer preview; consumer "preview" available each Wednesday.

## Files & schedule

- **Files arrive:** ad-hoc, typically ~2 weeks in advance.
- **Flyer (504) / LBM (3520):** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. Bi-weekly.
- **Pro Flyer (9711):** Available From Monday, Valid From Tuesday; every two weeks.
- **Specials (8741):** ad-hoc; some are Catalogs/Guides (follow dates on the PDF / confirm with external team via shell dates).

## Asset delivery (owned by DOC)

- Download the file packages from the emailed "Link to Download" (use the fallback link if the first fails). HH weekly + HHBC weekly are usually sent together; PRO and special campaigns come in their own folders.
- Unzip so a regular folder is on the desktop, connect to Home Hardware in Filezilla, and **drag the entire folder over** — do **not** transfer the zip, individual pages, or create your own SFTP folder (dropping the whole folder sets the base path correctly for the codesheet). Sync takes up to ~2 hours.

## Upload & setup (owned by DOC)

- Download the codesheet from the emailed distribution list (subject like "Events Starting …"). Codesheet indicator maps to flyer type: **HH → Flyer (504)**, **HHBC → LBM (3520)**.
- Save as CSV and run in the codesheet interface:
  - **Toggles:** select everything **except Region Assignment and Combine Zones**.
  - **Config name: `home_hardware_lbm`** (used for HHBC + HBC + HH).
  - **Base Path:** match the number to the FTP files; use everything up to language/region (English / bilingual / Quebec).
- Thumbnails: Standard 4. External run names (EN + FR):
  - Flyer (504): **Home Hardware** (EN & FR).
  - LBM (3520): **Home Hardware Building Centre** (EN) / **Centre de rénovation Home Hardware** (FR).
- After all PZs are created, mark Flyer Creation complete and QC pagination (PZ correctness, page counts). While QCing, note major CTAs/direct links (usually on the first and last 3 pages), pull their URLs from the HH Linking Document, format the linking doc, and attach it to all vendor tasks.
- **Specials (8741) setup:** manually upload page(s), one pricing zone labelled **Base**, add stores manually (may need to assign FSAs since paid flyers use a different radius — get FSA lists from the account channel or the Store-Level Campaigns sheet; if organic, keep default FSAs). Set external run name from the original email. No linking doc unless links are provided in the email body.
- **Note:** occasionally a zone has no FSAs and must be added manually; 3 stores share an FSA so those warnings can be ignored (rare).

## ⚠️ Common errors / risk items (retailer-specific)

- **Language tagging — tag in ONE language only.** For French pages, tag in **French only** (never both languages). French PDFs must be copied exactly, including all accents (é à è ù â ê î ô û ë ï ü ç / É À Ç).
- **All items with a SKU MUST have a URL.** If an item has no SKU, do **not** enter a URL. Use the **Fetch** button for single-SKU URLs; for multiple SKUs, tag all SKUs then use a homehardware.ca `/en` or `/fr` search-link. SKU format: keep the hyphen (e.g. `3698-218`, not `3698218`). Paired items with no pair SKU → leave SKU blank.
- **Google category** must be tagged on every item.
- **Washer/dryer pairs boxed & tagged separately** (each side linked to its own SKU; pair price goes in the Sale Story field).
- **"Buy X get Y free":** the FREE item is boxed/tagged as its own item box, with the offer in the Sale Story.
- **Multi-item blocks:** every item linked to its price and text (text boxes may stack); box the HERO (largest) image last. Each **size** gets its own box with its own SKU/URL.
- **"Your Choice"** prefix only when items are boxed together — not when boxed separately. Prefix: "Great Price" (EN) / "PRIX SUPERBE" (FR). Postfixes lowercase; skip postfix if "pack of"/count already in the title. "Priced In-Store" → put in prefix with no current price; if both, use "Only Priced In-Store".
- **Lumber pricing:** in a multi-price table, different sizes must NOT share the one-size price.
- **Do NOT** add sale story/prefix/postfix to items not linked with the original item.
- **Valid dates:** enter as on flyer; **do NOT enter the Aeroplan date**.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON (OFF for LBM), Box QC bot OFF** (ON for Specials 8741). Linking document required for Flyer/LBM/Pro. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks, CTAs. **Exclude** coupons. **All SKUs must be item boxes, not text boxes.**
- **Tag / Tag QC — Medium complexity. Auto-tag OFF.** Include brand, name, pre/postfix, description (SKU in description in flyer format), SKU, price, sale story, categories, disclaimer, original price, URLs, valid dates, Google categories. Keep brand in the Brand field only — never in the Name field.
- **Image QC (FLEX-owned post-processing):** select **Cutouts** and **No Images**; choose clean PDFs (clear item, white background, no shadows/lines). Do **not** select an image for items with no applicable flyer image.
- **URL/Links QC (FLEX-owned):** cross-reference the Linking Document against each page's banners; paste the URL and set **Display Type: "Link"**. Item name must match the linking doc exactly. Use Item Search (URL IS blank, type Item) to catch CTAs mistagged as items → change Display Type to Link; and (type Link) to confirm only non-shoppable direct links appear.
- **Spotchecks:** confirm Brand field upper/lower case; defer pre/postfix to the PDF.

## Flyer review

- **Flyer Review type: Lite.** (Flex 3FL / Flyer Review on Flyer, LBM, Pro; FLEX Image + Links QC on most types; Specials 8741 has no Flex flyer review.)

---
*Source: Home Hardware & Home Furniture OneGuide (Google Doc `1X9HDiPthDAM6K59fwtSOqXPCfbQUNiMF4w3SxjaM8L0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
