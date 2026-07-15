# Atmosphere Quebec & Sports Experts — Processing Guide

> **Source:** Atmosphere Quebec & Sports Experts OneGuide (Google Doc `182c2hoW1eaRrOBKWfKJS5zzGkzqJ80xlSzkQ4Xrgjjw`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fglsports-banners` |
| Hosted URL | sportsexperts.ca/en-CA/flyers-promotions/flyers-deals/flyer-sportsexperts |
| Flyer type(s) & cadence | Bi-weekly / ad hoc — 7973 Sports Experts · 9196 Atmosphere Quebec · 10403 Sports Experts Local |
| Processing | Auto-stack; Flex (Flyer Review); **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** Monday; dates called out in the file-delivery email. **Cadence:** Available/Valid Wednesday → Tuesday. **Preview:** usually the Monday before (email specifies).
- **Linking document:** Yes (bilingual EN/FR). **Workflow:** owned by DOC (Upload/FQC/Preview Links/Revisions).

## Upload & setup (owned by DOC)
- **Standard flyers (7973 / 9196):** manual upload from the corresponding FTP folder → Autogroup, don't process internally. If bilingual, upload twice and set the second set to French (they sometimes send EN and FR versions). Pricing zones **EN & FR**.
- **Linking doc manipulation:** combine Name/Brand, Modele, Description; remove unnecessary columns. Once done for EN & FR, upload as a mass attachment to all vendor tasks.
- **Local flyers (10403):** upload, Autogroup, don't process internally; pricing zones **Laval and/or Repentigny** (per email); **absolutely no linking document** — add vendor note "no URLs, please do not add any".
- **Setup QC (standard):** Available everywhere; Available Wed→Tue; Valid = Available unless stated; **internal preview date 1 week before live**; external run name per email; theme N/A unless stated; **legibility heights 55/40**; thumbnails Standard 4.
- **Setup QC (Local):** **RISK** — local flyers often fail content policy due to too few items; confirm enough items before Setup QC. Toggles **Hidden on Hosted**; **deep link** required for the retailer's Facebook ads (only works once live and if the customer's postal code matches; add the flyer run ID to the Links document to generate it).

## ⚠️ Common errors / risk items (retailer-specific)
- **Brand field must be EMPTY.** Brands appear as logos on the PDF (not caught by text extraction), so tag the brand as part of the **Name**, at the **front** (e.g. "THE NORTH FACE VENTURE 2 …"). Never append the brand at the end.
- **Name** must match the link sheet **verbatim** (copy/paste, same casing) — do not use the PDF name.
- **Original Price is never tagged** in the Original Price field — put it in the **Description** ("Regular Price $x.xx" / "Prix régulier: 0,00$").
- **Description** must contain the **SKU** and the regular/original price.
- **Price postfix must always be blank** (no "each"/"per pair"/"chaque"/"la paire") — new ask as of Dec 13 2024.
- **Sale Story** always ALL CAPS, as in the flyer; don't use "Dollars Off"/"Percent Off" fields.
- **Images:** PDF or Data-Piped images only — **cutouts must never be used.** Colour variant images must match the tagged colour.
- **URLs:** use the link sheet; English pages get English URLs (`sportsexperts.ca/en-CA/`), French pages get French URLs (`sportsexperts.ca/fr-CA/`).

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Box single-item offers individually; box multiple items of the same style/colour together in ONE box. On bilingual pages, only box English text on English pages and French text on French pages. Box coupons/general sales callouts (usually red) and Triangle Rewards call-outs. Linking doc used for both Box/Tag (local 10403 has no links).
- **Tag / Tag QC (Low; Auto-tag OFF):** Include name (from link sheet verbatim), valid dates, description, SKU, price, sale story, categories, disclaimer, URLs. **Exclude pre/postfix and original price** (see risk items). Brand is Tag/QC specific — kept out of the Brand field.
- **Image QC:** PDF & data-piped images only; if the image doesn't match the colour variant, override via the merchant page (copy image address → paste into "Override Image URL" → save → reselect in Image QC).

## FQC / post-processing (owned by DOC)
- **Standard flyer:** General Tagging QC (missing URL / missing reg price / missing brand in title / postfix text via `Price Text IS NOT blank` / missing sale story). Item Image QC (clean PDF or data-piped; colour variants match; never cutouts). **Preview links:** format an item-details sheet (keep flyer_name, page, display_type, name, description, sale_story, raw_current_price, url; rename name→Name & description→SKU & Reg Price; EN/FR tabs), then generate preview links from the preview-code sheet and email them (attach the item-details sheet).
- **Local flyer:** standard FQC, no links, no image QC; apply the retailer's campaign **disclaimer to all items** via multi-edit; deep link as above.
- **Final QC checklist:** check flyer boxing (grouped items in one box), mass-update EN/FR URLs from retailer email, apply direct links, verify brand at front of name, one SKU per product, run custom action to set all products to cut-outs, tag missing sale stories; via flyer export, import-blank the pre-price text / descriptions / original prices / price_text fields; generate Amazon preview links for EN + FR and send to the retailer.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swap (per training video).

---
*Source: Atmosphere Quebec & Sports Experts OneGuide (Google Doc `182c2hoW1eaRrOBKWfKJS5zzGkzqJ80xlSzkQ4Xrgjjw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
