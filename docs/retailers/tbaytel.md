# Tbaytel — Processing Guide

> **Source:** Tbaytel OneGuide (Google Doc `171McxQPaC0tnEUuNWkR9pAH5y6URhtmuFLVzI4OOCkw`), updated Jun 22, 2026. Contacts/credentials omitted.

Retailer has been inactive since before the current owners took on the account; some details are sparse accordingly.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only (not on our Hosted) |
| Slack channels | `#tbaytel`, `#flex-processingsupport`, `#flexflyerreview` |
| Flyer type(s) & cadence | Flyer Type 1 — Ad-hoc |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup & FQC; Flex Processing Support + Flyer Review; no coupons; no Feedel |

## Files & schedule

- **Files received:** Ad hoc.
- **Publication cadence:** Ad hoc (available/valid all ad hoc).
- **Preview date:** N/A.
- **Linking document:** Yes, for URLs.

## Upload & setup (owned by DOC)

- **Pages may need to be added to the SFTP by the processor if the client sends files over email.**
- **Manual upload:** Pages → Edit → select all pages from the SFTP menu → Confirm & Upload. Auto-group or manually add page numbers; ensure correct language. Save & Confirm — **do NOT Process Internally.**
- **Pricing zone creation:** usually only 1 PZ. Tbaytel is **FSA-based.** Refer to the email for which region set to use (usually referenced by exact name); if not stated, follow up with the retailer to confirm distribution.
- **Linking document:** URLs for each run live in the FAdmin SFTP (Tbaytel merchant page → Details → FTP path → View Files). Download it; upload by selecting a vendor track, ensuring "Mass Attachment" is checked, and adding the file.

### Setup QC
- Confirm all pages uploaded (Pricing Zone tab → Items View). **RISK:** if uploading from SFTP, confirm no pages in the SFTP remain un-uploaded.
- Confirm flyer dates (usually first or last page). Thumbnails Standard 4. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both Box/Tag — use the Excel as reference for what to box)**
- Include: special weblinks. Exclude: coupons, packaged deals, retailer logo, sign-up page, social media.
- Use an item box for the product and a **text box** for text when the product and text aren't easily boxed together (e.g. iPhone images across from their texts).
- Box all callouts/links/banners and reference the spreadsheet for URLs. Follow the Excel for what should/shouldn't be boxed.

**Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both Box/Tag)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** No brand.
- **Name:** full product name from text extraction (e.g. "iPhone 12 Pro Max – 128GB").
- **Current Price:** the cost per month.
- **Postfix:** the "/month for 24 months, taxes extra, $0 down, 0% APR" callout or "On a 2-year term with any Basic Plan" (no prefix).
- **Original Price:** the "Regular: $____" price.
- **Description:** include GB amount, "$0 down, 0% APR", monthly payment info, device full-price info.
- **Categories:** Google category = Mobile Phones or Mobile Phone Accessories.
- **Sale Story:** the savings callout with SimplePay (e.g. "Save $519.00 with SimplePay").
- **URLs:** provided by retailer as an Excel, laid out by page. If there are no products, tag as a **LINK** instead of ITEM.

**Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## Final QC / go-live notes (owned by Vendor)

- **Pre-FQC:** dates vs PDF; availability toggles; thumbnails include retailer logo. Standard checks: all items boxed/tagged; spotchecks (20% of PZs); previews published/clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** — flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles correct.

---
*Source: Tbaytel OneGuide (Google Doc `171McxQPaC0tnEUuNWkR9pAH5y6URhtmuFLVzI4OOCkw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
