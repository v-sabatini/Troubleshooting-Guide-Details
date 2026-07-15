# MarchesTAU — Processing Guide

> **Source:** MarchesTAU OneGuide (Google Doc `1FwwWKHItEnhVx4Tgbp5x6D8NSa5RyQhfACukFQsLECA`), updated Sep 22. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channel | `#marchestau` |
| Hosted URL | N/A (in discussions for Hosted) |
| Flyer types | **Monthly Flyer** (direct, ~1–2/mo) · **Mini Flyer** · **Produce Flyer** (one-pager) |
| Processing | Auto-stack; Flex (Flyer Review); no coupons/Feedel |
| Lead time | **7 business days** required (custom link process) |

## Files & schedule
- **Files received:** Wednesday (Monthly). No email sent when files drop — **check SFTP regularly**.
- **Cadence (Monthly):** Available/Valid From Monday → To Sunday.
- **Produce Flyer:** file usually shared late; **must be uploaded the same day received**. If files arrive Thursday, go live following Monday; if Friday, go live following Tuesday.
- **Linking:** Links are embedded in the PDF (retailer cannot supply a spreadsheet), so a unique mid-process linking procedure is used — see URL/Links QC below.
- Schedule is set at the start of the year and rarely changes; enforce lead time for additions.

## Upload & setup
- **Monthly & Mini:** files in SFTP ≥ 8 business days ahead. Manual upload all pages → Auto group → **FR only**. **2 PZ = base = FR, base cl = EN.** Add all stores.
- **Produce (one-pager):** manual upload page in French; **2 PZ = base FR, base cl EN**; add all stores; mass-attach linking sheet to vendor tasks.
- **Setup QC:** Available/Valid dates match PDF; toggle **Available everywhere**; check theme (else No Theme).
- **External run names:** Monthly = *Monthly Flyer* / *Circulaire*; Mini = *Mini Flyer* / *Mini Circulaire*; Produce = *Fruits and Vegetables Flyer* / *Fruits et Légumes Circulaire*.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each item individually.
- **Tag / Tag QC (Low; Auto-tag ON for Monthly/Mini, OFF for Produce):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
- **Produce one-pager:** linking document required for both box & tag; **all items must be tagged with their correct URLs** from the linking doc attached to the pipeline.
- **Image QC:** standard.
- **Spotchecks:** standard.

## ⚠️ Common errors / risk items
- No drop email — **monitor the SFTP** so files aren't missed.
- Links are embedded in the PDF only; missing the mid-process link collection breaks the custom linking.
- FQC: items without a URL should be **< 10%**; investigate missing Produce URLs against the linking sheet.

## URL/Links QC (owned by DOC) — Monthly linking process
- Links are embedded in the PDF pages; DOC clicks into the **raw PDF** (not the FAdmin-uploaded version) and copies links into the URL field.
- **Flow:** DOC files an ARB ticket → Flex completes the link pulls → DOC applies links.
- Rename file **MarchesTAU MM YY Links** and file the ARB ticket for Flex, including the link document, the SFTP path, and the reference video.
- **Post-processing steps (all flyer types):** QC thumbnails Standard 4; confirm external run name; every priced/callout item is boxed; no overlapping boxes; sessions all green; Geography no changes.

## FQC / flyer review
- **Flyer Review type: Lite** (completed by Flex). Dates same as PDF; Available = Valid; available everywhere; external run name set; check pagination order; item boxes; iframe; vertical geography; no change WOW.

## Out-of-processing
- Page swaps and post-live checks handled ad hoc (see OneGuide video reference).

---
*Source: MarchesTAU OneGuide (Google Doc `1FwwWKHItEnhVx4Tgbp5x6D8NSa5RyQhfACukFQsLECA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
