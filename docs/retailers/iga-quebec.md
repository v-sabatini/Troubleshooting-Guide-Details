# IGA Quebec — Processing Guide

> **Source:** IGA Quebec OneGuide (Google Doc `17uX9ZAsJPk9vudaBDIWAct1mxuINtUmATVt4c8XItpE`), updated Apr 24, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#iga-quebec`, `#3fl-sobeys`, `#sobeysops` |
| Hosted URL | iga.net |
| Flyer type(s) & cadence | **Weekly Quebec (5710)** · **Weekly New Brunswick (5711)** · **Weekly Iles-de-la-Madeleine (5697)** — all weekly, EN + FR |
| Processing | Auto-stack |
| Who's involved | Flex (Flyer Review); OS (Setup); Strategic Ops (retailer data services / Feedel); no coupons |

## Files & schedule
- **Files received:** Monday.
- **Publication cadence:** Available Tuesday → Monday; Valid Tuesday → Tuesday.
- **Custom action:** "Set cutout images" (used in the IDM FQC process).

## ⚠️ Risk items (most valuable)
- **Box every unique item separately** (e.g. yellow zucchini vs. green zucchini).
- **Choose the PDF image for every item** (some exclusions — see Image QC).
- **Contest dates** apply to the CONTEST only — do **not** override flyer valid dates with them.
- **Pages cropped:** review uploaded pages so none are cut off on any side.
- **`+tx` postfix:** tag ALL items showing `+tx` on the PDF in the Postfix field — **watch liquor items especially**. Enter the price in Postfix Amount.
- **Product URLs:** each boxed item gets the correct SKU from the linking (extract) document. If the fetched URL is invalid/missing: search iga.net by product name → copy the SKU from the URL → input into the URL field.

## Upload & setup (owned by Vendor)

### Quebec (5710)
1. Download **B extract** xls & **Order IGA - Quebec** xls from the FTP.
2. Manual upload — **upload pages twice** (once French, once English); pages from the IGA folder. **Do NOT upload Booklet-folder files.** EN and FR page counts must match (pages look like a zipper). Save & Complete.
3. **Do NOT create pricing zones** — check off Flyer Creation. PZs are created in FQC. A FSA generation error will appear because no stores are added — **ignore it**.

### New Brunswick (5711)
1. Download **BA extract** xls & **Order IGA - NB** xls. Pages come from the **IGA ATL folder** only.
2. Manual upload twice (FR + EN, zipper); Save & Complete.
3. Do not create pricing zones — PZs created in FQC.

### Iles-de-la-Madeleine (5697)
1. Upload pages twice (FR + EN), auto-group (zipper), Save & Complete.
2. Flyer Creation — **2 PZs: English and French** (mark the French PZ as French).
3. Pages in order (P01, P02, …). This is a **simplified pop** — only the image cutout shows on the front end (no item details/pricing).

### Setup QC
- Attach the extract & order documents to vendor tabs (mass attachment); mark vendors High.
- **External Display Names:** QC → FR "Québec – Circulaire Hebdomadaire" / EN "Québec – Weekly eFlyer"; NB → EN "New Brunswick – Weekly eFlyer" / FR "Nouveau-Brunswick – Circulaire Hebdomadaire"; IDM → EN "Iles-de-la-Madeleine - Weekly eFlyer" / FR "Iles-de-la-Madeleine - Circulaire Hebdomadaire".
- **Available Everywhere**, no theme. IDM: add the **3 designated stores only**. Ignore the FSA error for QC.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons.
- Special weblinks: FR `https://iga.app.link/JcS9FMP2JPb`, EN `https://iga.app.link/zmqBgDX2JPb`.
- **Direct-link boxing:** use the Order xls to see what to box/tag; display type = Link.
- Items with more than one image → box each as an individual item. Non-grocery pictured items (no SKU, can't add to cart) are **not** boxed/tagged.

### Tag / Tag QC (Low; Auto-tag OFF)
- **Include** brand, name, pre/postfix, valid dates, description, SKU (from the extract doc), price, sale story, categories, original price, URLs (fetch from SKU), image selection (PDF preferred). **Exclude** disclaimer.
- **All tagging info comes from the PDF except the SKU**, which comes from the linking (extract) document. Match the page via the first number after "IGA" in the page name.
- **Banner callout (bottom of pages):** tag as a link — EN name "Activate Offers"; use FR/EN app.link URLs above.
- **Scene+ items:** tag "Scene+ PTS" in Sale Story; or prefix "Prix Membre Scene+" / "With Scene+ card", disclaimer "Without Scene+ card $X" / "Sans carte Scène+ $X", categories = Scene+ plus the product category.
- **`+tx` (new Jan 2026):** Postfix Text `+tx` after the price.
- **REG price (new Jan 2026):** single reg price → Original Price; **price range** → put "Reg. $X to $Y" in the description and **leave Original Price blank**.

### Image QC
- Rule of thumb: pick the cleanest image. **Do not use PDF images** when there are lifestyle shots or too many shadows/black outlines — leave no image or use cutout. If multiple images, choose the one best matching the product name.

## Post-processing / FQC (Multiple parties)
- **Quebec runs:** complete **Pre-FQC steps only** during FQC (FQC owned by DOC, Pre-FQC by FTE).
- **New Brunswick & IDM:** complete **both** Pre-FQC and FQC (owned by FTE).
- **Pre-FQC checklist:** Scene+ Points, Page Categories, Items without URLs.
- **QC/NB FQC:** create generic codesheet (QC/NB Hosted templates) → PZs with correct page order (NB = 2 PZs, EN + FR); upload with **Config `generic_language`**, PDF base directory from FTP, **toggles 1, 3, 4, 5, 6**; "Already Uploaded" yellow warning is fine → **Force Processing** (any other error → troubleshoot, do not force). Rerun Flyer Creation; add stores via generic codesheet + store sets; Image QC (uncheck PDF, watch unclean fruit PDFs); StoreFront SpotCheck; mark AutoStack complete; add direct links from Order sheet and **always rerun Page Tile Generation after adding links**; add the **extra page provided on Fridays** to all PZs after page W1; check items without URL (compare FR/EN, copy missing SKUs, verify links work); draw thumbnails (Standard 4 + thumbnail + w400); **QC Hosted only:** remove WR (Rachelle Bery) pages from EN/FR/EN Voila/FR Voila PZs. Key Messages EN "Eat Well" / FR "Mieux Manger"; 3-day preview; Available Everywhere.
- **IDM FQC (FTE):** mark item QC & Image QC complete; run custom action **"set cutout images"**; each PZ has **4 stores only** (8372, 8792, 8793, 8794); thumbnails Standard 4 + thumbnail (get IGA title even if not on first page); pages in order; Final QC (save & confirm twice), Available Everywhere; add "simplified pop" and force mark complete for spotcheck/tagged-item QC.
- **CLONING IS NO LONGER NEEDED. DO NOT CLONE.**
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swaps (baseline video). IGA West-style inserts do not apply here.

---
*Source: IGA Quebec OneGuide (Google Doc `17uX9ZAsJPk9vudaBDIWAct1mxuINtUmATVt4c8XItpE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
