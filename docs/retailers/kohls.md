# Kohl's — Processing Guide

> **Source:** Kohl's OneGuide (Google Doc `1WOS9edh6DgggwtwGBQosiIvoKp04FDThhHmfv4vk56c`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | **Tier 1 Premium** (account 2470) |
| Availability | All platforms |
| Slack channels | `#kohls`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | kohls.com/feature/flipp.jsp |
| Flyer type(s) | Weekly Flyer (2525) |
| Processing | Auto-stack; **coupons processed by OS**; no Feedel |
| Involvement | **DOC** owns setup & FQC; **FLEX** owns Image QC, Processing Support & Flyer Review |

## Files & schedule

- **Files received:** Monday (via **email** from Prepress — download and upload to CORE FTP).
- **Publication cadence:** Available Tuesday–Friday, Valid Friday–Tuesday.
- **Preview date:** Tuesday the week before available.
- **Linking document:** for **Little Co Books** only.

## Upload & setup (owned by FLEX)

- Pages may need to be added to SFTP by the processor if files come via email. **Manual upload.**
- **Reading page names / versioning:** upload all pages **unless a numerical value follows the letter** (revised pages) — e.g. `01A2B2C2D2` is used instead of `01ABCD`; ignore the superseded version. Letter combos can be any of A/B/C/D (AB, CD, ABCD, BCD…). `R` before the number (e.g. `r01`) = goes to all regions. Format is Date/PageNumber/Stores. Tip: look at the last page to see which versions to build.
- **4 store sets:** AA, BB, CC, DD (on FADMIN) — match to page file names. Pages shared across zones can be combined into one pricing zone; a zone with its own page gets its own zone.
- **Config name: `kohls`.** (Codesheet upload used only if they resume sending Version Memos; currently manual.)

## ⚠️ Common errors / risk items

- **Page-level valid dates:** check the top of each page for separate valid dates (e.g. "3-Day Door Busters"). Dates may be **cut off and split across two pages**.
- **Original price:** always choose the **highest price in a range**.
- **Sale Story:** apply a banner's sale to the Sale Story of **all items listed under it**.
- **Box QC:** confirm coupons are boxed; **two prices sometimes get boxed together — separate them**. Auto-stack spotcheck: merge spread pages in the spotcheck tool.
- **Versioning:** confirm page file names align with assigned store sets (AB pages → AB store sets, etc.).
- **Little Co Books:** lookbook content with no items/prices — always has a linking document defining box placement and tagging.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Stock Premium: use Flipp-created or generic sale story (usually from page 1); include the Kohl's logo in Stock Premium and both Storefront Carousels.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU.** Only enter a disclaimer if it's inside the drawn box (not page-bottom disclaimers).
- **URLs — always enter:** search kohls.com for the item, copy the item-page link into the URL field. If no direct URL, use the search-page URL; for assortments use any item's direct link. If none found, use `http://www.kohls.com`. Coupons must be **link type** pointing to Kohl's sales/deals page.
- **Image QC:** PDF preferred if clean; cutouts otherwise; cleanest image possible.

## FQC / flyer review

- FQC checklist: pricing zones have correct pages per naming convention; box-draw items with price/coupons/social icons; **leg heights 45/35**; view warnings; add missing URLs; store tiles/sale story; check valid dates by page; coupons all link-type with URL; dates on PDFs match run dates; all stores assigned; items clickable; Item Image QA 100% complete.
- **Flyer Review type: Simple.**

---
*Source: Kohl's OneGuide (Google Doc `1WOS9edh6DgggwtwGBQosiIvoKp04FDThhHmfv4vk56c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
