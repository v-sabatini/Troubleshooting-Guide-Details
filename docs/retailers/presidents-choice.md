# President's Choice — Processing Guide

> **Source:** President's Choice OneGuide (Google Doc `1AAAhPMsevVgLtz2MPQjP97N0UN9lNjaSeCcGo0GuaGg`). Contacts/credentials omitted.

The **PC Insiders Book** (Summer / Holiday), a bi-annual bilingual book that is processed on the President's Choice merchant and then **cloned across all Loblaws banners.** This is a high-effort account driven by a Workback Schedule (WBS).

## Account at a glance

| | |
|---|---|
| Account tier | Core+ |
| Availability | PC Insiders version = all platforms; **banner clones = Hosted only** |
| Slack channel(s) | `#lcl-pcinsiders` (cloning coordination in `#loblops`) |
| Hosted URL | pcoptimum.ca (clones posted to all Loblaws banner sites) |
| Flyer type(s) | Bi-annual: **Summer Insiders Book**, **Holiday Insiders Book** |
| Processing | Auto-stack; no coupons; no Strategic Ops / no Feedel |

## Files & schedule

- **Files received:** per the WBS on agreed file-drop dates. All publication dates ad hoc / per WBS.
- **Preview:** per the WBS on agreed preview-link delivery dates.
- **Workflow owners:** Upload/Setup and FQC = DOC.
- Client is being trained on the SFTP upload process (may need COC support; WeTransfer as a last resort).
- See the Flipp x SIR Workback Schedule (linked in the OneGuide) for dates.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages Tab → Edit → select all pages from the SFTP → Confirm & Upload → Auto-Group / enter grouping numbers → set correct language (toggle FR QC pages to French) → Save & Confirm.
- **Create 3 pricing zones** by filename:
  - **EN QC** — files with "EN QC" in the name, uploaded English → region set **Quebec - All**
  - **EN ROC** — files with "EN ROC", uploaded English → region set **Rest Of Canada**
  - **FR QC** — files with "FR QC", uploaded French → region set **Quebec - All**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (retailer/BD/WBS); Standard 4 thumbnails; set preview dates for OS processing and client link delivery.

### ⚠️ Common errors / risk items (retailer-specific)
- **Three parallel versions** (EN QC, EN ROC, FR QC) with the same items — box/tag must match across all three; discrepancies are the recurring risk.
- **Item images do not extract cleanly** — many items must be pulled from loblaws.ca post-processing (highly manual; file an ARB ticket). Not every item is available online pre-live — grab images again post-live.
- **Items on one page with details on another** (and back-page/cover items without details) are easy for OS to miss since they only see one page at a time — box/tag these yourself.
- **Cover page** sometimes has multiple versions to swap weekly via triggers + OPTICS tickets — confirm dates with the retailer.
- **Clones must be Hosted only** — double-check availability toggles on every clone.

## QC specifics

### Box Draw (Low complexity — Auto-Box OFF, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box all Table-of-Contents pages (text AND numbered images — they link to page numbers).
- Box items whether or not they have article numbers/prices; the client wants items clickable even without a price. **When in doubt, make a box** and the full-time team reviews.
- Box items with at least a Name (and sometimes a Price) even without a SKU/article number.
- Use text boxes to associate item images with their text even when not adjacent; match flavour/type when unsure.
- If two items share a single image, box them together. Box PC Express code call-outs and full category-intro pages.

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** name, brand, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, and **Article Number 1–4** (put the SKU into BOTH the SKU field and the Article Number fields, one per field).
- Table-of-Contents boxes → **Page Link** type, directed to the listed page (images with a number but no text also = Page Link).
- Use **bold text** in a text block as the item Name (even if not captured by the box draw). Put item size in Description; post-sale pricing (e.g. "+ tx") in Postfix.
- If two items were boxed together, include both SKUs in the Description and both Article Numbers in separate fields.
- Full-page boxes → Link type with `https://www.pcoptimum.ca/` (or the linking doc / a printed link if provided). Links are largely added post-processing.

### Image QC
- Select clean PDFs where available; otherwise leave as Cutout (grabbed from the website post-processing).

## Post-processing / Final QC (owned by DOC)

- **Item Image Override:** open all three versions of a page; search the SKU on loblaws.ca (any Loblaws banner works); Copy Image Address → paste into **Override Image URL** → Save; apply to all three versions. Recommend pre-live + post-live ARB tickets. For efficiency, export items (keep only `item_id`, `sku`, `override_image_url`, clear `item_id`) and import into every cloned run to auto-match SKUs.
- **Edit Details:** confirm dates (WBS) and toggles (PC merchant = available everywhere).
- **URLs:** Item Search → filter Item type → Multi Edit → apply the client's flyer landing page (e.g. `pcoptimum.ca/[flyer_name]`, else `pcoptimum.ca/flyers`); fill blank Article Numbers and SKUs (request missing ones from client at preview).
- Verify the 3 versions match (item counts, boxing/tagging) via Pricing Zone Item View; handle back-page items and cross-page items.
- Set Cover-page swap triggers + JIRA OPTICS tickets as needed.
- Flyer Review type: **Lite** (owned by DOL).

## Preview & cloning
- **Preview delivery:** send the preview link to the retailer contact + stakeholders + BD; ask for missing article numbers and non-item direct links; flag missing item PDFs (plan to grab on go-live day).
- **Post-FQC cloning to other Loblaws merchants:** only clone after all base-version updates are made (post-clone changes must be applied to all versions). Clones are **hidden on Flipp / available on Hosted** (also lets the PC Optimum app find them via API). Clone to the **General Merchandise** flyer type (or a prior Insiders Book type).
  - The **back cover (EN ROC version)** is the source of truth for which banners get which zones. Banners listed on the EN ROC back cover (No Frills, Real Canadian Superstore, Real Atlantic Superstore, Loblaws, Fortinos, Independent City Market, Valu-Mart, Zehrs, Loblaws City Market, Shoppers Drug Mart, Maxi) get the EN ROC version in English; bilingual banners also get an **EN ROC FR** cross-language zone. EN QC / FR QC go live to Maxi, Provigo, Pharmaprix (English + French).
  - **Store assignment:** pull the store list from the most recent Weekly run (PC won't provide); build a CSV of store code + pricing zone (EN ROC / EN QC, duplicated with FR names EN ROC FR / FR QC); upload with config **`generic_stores`** and only the first toggle selected.
  - **Links per banner:** update each version so links point to that banner's site (loblaws.ca, zehrs.ca, etc.) instead of the base PC link — use Fetch, or an item import with a `=base URL + SKU` formula (e.g. `loblaws.ca/p/[SKU]`), keeping only `item_id`, `sku`, `url`. Clone the URL-updated version onward (Find & Replace the domain per banner).
  - **Re-complete each clone's FQC checklist and double-check availability toggles — clones must be Hosted only.**

---
*Source: President's Choice OneGuide (Google Doc `1AAAhPMsevVgLtz2MPQjP97N0UN9lNjaSeCcGo0GuaGg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
