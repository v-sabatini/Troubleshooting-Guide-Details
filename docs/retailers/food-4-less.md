# Food 4 Less (PAQ Inc) — Processing Guide

> **Source:** Food 4 Less (PAQ Inc) & Rancho San Miguel Markets OneGuide (Google Doc `1nzCQ_IaiBFcH2W2tyYGbyV4taSMfzUAl9jg_TeTaKro`), updated Jun 23, 2026. Contacts/credentials omitted.
>
> This OneGuide covers two merchants — **Food 4 Less (7355 / flyer type 12392)** and **Rancho San Miguel Markets (7356 / flyer type 12393)**. This article documents Food 4 Less; Rancho San Miguel setup differences are noted at the end.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms |
| Slack channels | `#paq` |
| Hosted URL | N/A |
| Flyer types | Flyer |
| Processing | Auto-stack; no coupons, no Feedel |

## Files & schedule
- **When files arrive:** Wednesday.
- **Publication cadence:** Available/Valid From Wednesday; Available/Valid To Thursday.
- **Linking document:** N/A. **Processing type:** Auto-stack.

## Upload & setup — Food 4 Less (owned by Vendor)
- **Manual upload:** Pages Tab → Edit. Select all pages from the SFTP menu — folder named by the flyer's valid date. **If two folders share the same name, always use the *lower case* folder — do NOT upload the Upper Case folder.** Confirm & Upload.
- Scroll down, click "Auto-Group…", Save & Complete.
- **Pricing zones (2 total — the only difference is two versions of page 1):**
  - **Zone #1 "Base":** add the page 1 that does **NOT** have "Ceres" in the name, plus all remaining pages in numerical order. Add **all stores**, then **REMOVE store #3 "Ceres"**. Save & Next.
  - **Zone #2 "Ceres":** add the page 1 that **HAS** "Ceres" in the name, plus all remaining pages in order. Add **only store #3 "Ceres"**. Save & Complete.

### Setup QC checklist (owned by Vendor)
- Confirm all pages uploaded: open the SFTP, ensure no pages remain except the multi-page PDF (Upper Case name not ending in "P####"). **If pages were missed, flag to the FT team.**
- Confirm flyer valid dates match page 1 of the PDF.
- Complete thumbnails (4 Standard).
- **Geography Tab: ensure 0 changes to Stores or FSAs. Flag 100% of discrepancies to the FT team via Slack/email** (continue the checklist regardless).
- Platform toggles: available on ALL platforms. Complete Setup QC checklist.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Tagging rules are completely standard.**
- **Include:** image (always select a clean PDF if available), brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price.
- **Exclude:** SKU, URLs.

### Spotchecks
- Standard spotchecks included in pipeline.

## Post-processing / FQC (owned by Vendor)
- Pre-final: confirm valid dates against PDF; available everywhere; thumbnails include retailer logo; all boxed/tagged; previews published/clickable; **geography consistent with last week (no stores/FSAs added/removed) — immediately flag 100% of discrepancies to the FT Ops team** (does not block work).
- Complete FQC checklist.

## Flyer Review (owned by Vendor)
- **Flyer Review type: Lite.**

## Rancho San Miguel Markets (same OneGuide — setup differences)
- Same schedule, box/tag rules, and FQC as Food 4 Less.
- **Upload:** same manual upload (use the lower case folder), Auto-Group, Save & Complete.
- **Pricing zones:** create **only one zone "Base"**, add all stores, Save & Complete (no Ceres split).

---
*Source: Food 4 Less (PAQ Inc) OneGuide (Google Doc `1nzCQ_IaiBFcH2W2tyYGbyV4taSMfzUAl9jg_TeTaKro`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
