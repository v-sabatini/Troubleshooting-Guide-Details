# Avril Supermarché Santé — Processing Guide

> **Source:** Avril Supermarché Santé OneGuide (Google Doc `1ksg2EiOJfqD0S7NoGQJbqrZGHgxqsFy2VivXFXJMeXE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#avril-supermarche-sante`, `#flex-processingsupport` |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly (Circulaire, 10471) · Flyer Type 2 — Monthly |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received:** Monday. **Cadence:** Available From Wednesday / Valid From Thursday / Valid To Wednesday. **Preview:** Wednesday.
- **Linking document:** Yes. **Workflow:** Setup by DOC; additional FL upload by DOC; Link QC & FQC by Flex.

## Upload & setup (owned by Flex) — Circulaire (10471)
- Files uploaded to SFTP; pages manually uploaded to the flyer run.
- **2 pricing zones: FR and EN.** Upload files twice (mark one set English, one French). Prefix English pages with `EN_` so OS knows which link sheet to use.
- Add all stores. Attach linking docs to vendor tasks with note: "Please tag Links as outlined for their specific languages (EN for EN pages and FR for FR pages)."
- Setup QC: valid dates must match page 1; no sub-pages need to be drawn.

## ⚠️ Common errors / risk items (retailer-specific)
- **Link QC (EN/FR):** ensure the correct URLs by page language. Check EN pricing zone for links containing `fr/` and the FR zone for `en/`; the entire link must be updated per the linking doc.
- **"2 pour 1" items:** tag in the **Sale Story**, not in current pricing.
- **"Taxes en sus":** put in the **Description**, never in the post-fix.
- **Regular price range:** tag a range in the Description as "Reg. 9.59-9.99"; a single regular price goes in Original Price (e.g. "Original Price: 7.29").
- **Validity dates** (usually pg 1): Jeudi+Vendredi = Thu & Fri; Samedi+Dimanche = Sat & Sun; Lundi = Mon; Mardi+Mercredi = Tue & Wed.
- **Brand field "Avril":** any item whose brand just says "Avril" must be updated to Avril Cuisiné, AVRIL SÉLECTIONNÉ, or avril gourmet.
- **Fruit & Vegetable (FL) pages:** placeholder pages must be swapped IN; on Monday the FL page is added to both PZ (an `EN_` version plus the base French), in position 2 of the flyer.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** Exclude coupons, packaged deals. **Include** retailer logo, sign-up page, social media, special weblinks, and the banners at the bottom of most pages (**box the ENTIRE banner**). Use items + text boxes so the whole area is clickable — don't box just the text or just the item. Linking doc is Tag/QC specific.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF Image Auto Selection ON):** Include name, pre/postfix, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude valid dates** (tag validity dates as noted in risk items). Brand is Tag/QC specific.
- **Image QC:** clean images if available.

## FQC / links QC (owned by Flex / multiple parties)
- **Complete Links QC before Final QC:** Overview → items without URL (cross-reference linking sheet; a page of 5 fruits/vegetables is tagged with the last line under page 1 labelled FL); Item Search `URL CONTAINS /en/` in FR zone (deselect Show One Per Item Group) → input correct FR link; repeat for `/fr/` in EN zone.
- FQC: Item Search `Price Text CONTAINS Taxes` → move "Taxes en sus" to Description; Item Search `Brand CONTAINS Avril` → fix bare "Avril" brands. Check box accuracy (banners at end of all pages except page 1; all items incl. photos clickable). Ensure Fruit & Veg pages swapped in.
- Thumbnails (1065x600 x2, storefront carousel premium x2, organic x1); image QC marked off; available everywhere; EN + FR zones all stores; geography no change; no items without URL before FQC.
- **Flyer Review type: Lite.**
- **Post-live:** apply corrections from the retailer's emailed corrections document.

---
*Source: Avril Supermarché Santé OneGuide (Google Doc `1ksg2EiOJfqD0S7NoGQJbqrZGHgxqsFy2VivXFXJMeXE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
