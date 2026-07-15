# Les Marches Tradition — Processing Guide

> **Source:** Les Marches Tradition OneGuide (Google Doc `1uCc9R4cbp8CTfQ_PnGlOicnVFtRwrE2oxuavZ91Ty9s`), updated Apr 10, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Publications | 6266: Quebec (QC/TRD) · 6425: New Brunswick (NB/ATL) |
| Availability | All platforms |
| Slack channel | `#iga_quebec` |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); Feedel/retailer data services |
| Coupons | None |

Bilingual account (French + English pricing zones). NB files always contain "ATL" in the name; Quebec files always contain "TRD".

## Files & schedule

- **Files received:** Monday (via FTP). If not received by **Wednesday 3PM**, email the retailer ops contact (in the OneGuide).
- **Cadence:** Available From Tuesday, Valid From Thursday; Available/Valid To Wednesday.
- **Processing type:** Auto-stack.

## Upload & setup (owned by Vendor)

Same steps for QC and NB runs:
1. Pages tab → Edit → Les Marches Tradition folder. QC run uploads from the QC/TRD folder; NB run uploads from the NB/ATL folder.
2. Find the dated folder — **they mark files by the last date of the publication**.
3. Upload files, set all pages to **French**, Save (do not group yet). **Re-upload the same files** from the same folder, then click **Auto-Group** (groups both languages).
4. **⚠️ Page ordering:** you may see duplicate/conflicting page numbers — follow the ordering boxed in green, not red.
5. Two pricing zones — **French and English**; add all stores to BOTH.
6. Edit Details: toggles only available in Hosted; **No Theme**.
7. QC Thumbnails: Standard 4. **⚠️ Ensure the Les Marches Tradition logo is captured** in the stock_premium thumbnail (move it to the end of the page if needed).

## ⚠️ Common errors / risk items

- **Scene+ callout:** every offer with an accompanying Scene+ offer must have **Scene+ tagged in the Sales Story**. Some offers don't say "Scene+" — they only show points earned; Scene+ **still** must be tagged. Correct: `50 Scene+ PTS`. Incorrect: `50 PTS` / `50 Scene`.
- **Clone flyer runs — remove the wrong store set:** on the cloned QC run remove the cloned NB store set; on the cloned NB run remove the cloned QC store set.
- File-arrival delay (see Files & schedule).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** exclude coupons and packaged deals; include retailer logo, sign-up page, social media, special weblinks. Box each product block with a price or sales story.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON):** linking doc required (Tag/QC specific). Include brand, name (bold; French versioning above brand, English below), description (only French on French flyers, only English on English), SKU, price, sale story, categories, disclaimer, original price, URLs, postfix (include /lb AND /kg).
  - **Prefix (updated):** for products with a corresponding callout, apply exactly — EN: `Scene+ Member Pricing`, FR: `Prix Membre Scène+` (accents must match exactly).
  - Scene+ links: EN `https://www.marchestradition.com/en/sceneplus/`, FR `https://www.marchestradition.com/fr/sceneplus/`.
- **Image QC:** prefer clean white-background PDF images.

## Post-processing / FQC (owned by DOC)

- **Page categories:** the retailer emails a category spreadsheet Thursday (also in the Les Marches Tradition Google Drive). Follow it exactly; pages not listed get **no** categories. Match category page to the last page name.
- Re-verify Scene+ callouts (Item Search: Sale Story contains "PTS") and Scene+ prefixes (EN/FR as above).
- Check pages/pricing-zone/sessions/vendors/geography tabs; check Vertical Scroll for squished/cut-off pages.
- **Cloning:** two flyer runs per language — one **Hosted**, one **[Cloned]** for Distribution & Flipp (shells already built — copy to existing flyer run, match dates). Hosted runs: hidden in Flipp & distribution, all stores in both PZs. Clones: hidden in hosted, only that run's stores (NB stores for NB, QC for QC).
- FQC checklist all four runs (Hosted QC, Clone QC, Hosted NB, Clone NB). Other errors/warnings can be ignored.
- **Flyer sorting:** oldest Quebec, oldest NB, newest Quebec, newest NB.

## FQC / flyer review

- **Flyer Review type: Lite** (owned by Flex), separate reviews for QC and NB.
- **Out-of-processing:** baseline page-swap process.

---
*Source: Les Marches Tradition OneGuide (Google Doc `1uCc9R4cbp8CTfQ_PnGlOicnVFtRwrE2oxuavZ91Ty9s`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
