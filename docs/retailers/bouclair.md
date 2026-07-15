# Bouclair — Processing Guide

> **Source:** Bouclair OneGuide (Google Doc `1ImAilVMh0JrJ8N1tDAXwHvfTlQIErcYf9m0l6cYpbVY`), updated May 1, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard (retailer 1970) — bilingual EN/FR |
| Availability | All platforms |
| Slack channels | `#bouclair` |
| Hosted URL | bouclair.com/en/flyer.html |
| Flyer types & cadence | Weekly (Available Mon, Valid Tue); Mini sale (available Fri, valid Sat–Sun) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; no Feedel/Strategic-Ops |

## Files & schedule

- **Files received:** Monday (retailer emails when files are in the FTP).
- **Publication:** Available From Monday, Valid From Tuesday. Flyer available everywhere, live Wednesday.
- **Preview:** to retailer one day before (often a small preview window the afternoon before go-live).
- **Files include:** page PDFs (EN + FR), EN & FR linking documents, and a box-draw/TAG PDF.

## Upload & setup (owned by DOC)

- Download from FTP: Excel link sheets + TAG PDF. Attach the Excel spreadsheets to Tag and QC; attach the TAG PDF to Box Draw and Box QC. **Both EN and FR linking documents must be attached.**
- Pages → Edit → select EN and FR files from FTP → index → assign correct language. There are EN, FR, and TAG files — **DO NOT upload TAG pages.**
- **Create two pricing zones: EN (all English pages) and FR (all French pages). Assign all stores (~105) to BOTH zones.**
- Attachment formats: `DF#-EN (tags)` → all Box/Box QC tasks; `Flyer # MM-DD_EN/FR` → the language-matching Tag and QC tasks.
- **Setup QC:** legibility heights 60/40; standard 4 thumbnails; available everywhere live Wednesday; preview one day before.

### ⚠️ Common errors / risk items (retailer-specific)

- **Display type from the linking doc decides item type.** Product page = `Item`; category/collection/home/contest page = `Link`. Getting this wrong is the main recurring issue — items that are really category callouts must be set to `Link`.
- **Pricing:** use the price in the **tagging/linking sheet as priority**, even if it differs from the flyer or website. If a price was missed, use the URL to gather it.
- **Overlapping items:** use text boxes so a larger portion stays clickable (e.g. draw the chair as a text box so the rest of the coffee table stays clickable).
- Single item on a page → box the entire page.
- Tag EN pages in English, FR in French; apply the matching-language linking doc/URLs.
- **Images are 100% data-piped** — select the data-piped image; PDF/cutout only as backup, **and flag any cutout to PC.**

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF. Linking doc required (Box-specific — the TAG PDF).** Exclude coupons; include packaged deals, retailer logo, sign-up page, social media, special weblinks. Verify item count on the page matches the linking sheet after boxing.
- **Tag / Tag QC — Low. Auto-tag OFF. Linking doc required (separate EN & FR).** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Reading the linking sheet:** Col A = page/box letter; Col B (UTM Content) = SKU; Col C = product name; Col D (Comments) = display type (product page → item; category/collection → direct link); Col E ignore; Col F (Flyer Link) = URL for tagging; Col G = price (items only, use even if it differs from flyer/website).
- **Image QC:** select data-piped image only; PDF/cutout backup only, flag cutouts. **Page categories: every page except page-1s needs 1–3 categories.**

## FQC / go-live (owned by DOC)

- Page categories match EN ↔ FR; legibility heights 60×40; thumbnail QC; enter Sales Story/Key Messages EN & FR.
- Pricing zones: **add all stores for both languages.** Confirm items that should be direct links have Display Type = Link.
- Data piping as close to 100% as possible — re-run and check reports; PDF extract only if unavailable; item image QC that data-piped images match cutouts.
- After FQC and corrections, **clone the run for Ecomm processing.**
- **Flyer Review type: Lite.** (Mini sale: available 1 day early Fri, valid Sat–Sun.)
- **Live dates:** if prices are incorrect, use the prices indicated on the website.

## Out-of-processing

- Page swap: standard baseline process.
- Black Friday comms guidelines exist (2024, 2025).

---
*Source: Bouclair OneGuide (Google Doc `1ImAilVMh0JrJ8N1tDAXwHvfTlQIErcYf9m0l6cYpbVY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
