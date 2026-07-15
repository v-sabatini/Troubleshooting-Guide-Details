# HockeyStickMan — Processing Guide

> **Source:** HockeyStickMan OneGuide (Google Doc `1GzQig7rPMO79KLLFNPQTWFh6Rkhse0iZ7t2jThcUGuc`), updated Jun 5, 2026. Contacts/credentials omitted.

Longtail hockey-equipment retailer with a **linking document** driving both boxing and tagging.

## Account at a glance

| | |
|---|---|
| Account tier | Longtail |
| Availability | All platforms (**we do not power hosted**) |
| Slack channel(s) | `#1plat-hockeystickman` |
| Hosted URL | n/a |
| Flyer type(s) & cadence | Flyer Type 1, weekly |
| Processing | Auto-stack; DOC-owned pipeline; no coupons; no Feedel |

## Files & schedule

- **Files arrive:** Monday. Available From Tuesday → Available To Monday.
- **Linking document: Yes** — dropped in the FTP with the files.

## Upload & setup (owned by DOC)

- **Manual upload:** Pages > Edit > select all pages from the SFTP (flyer date matches the PDF names) > Confirm & Upload. Auto-Group or manually enter grouping numbers; ensure correct language. Save & Confirm — **do NOT process internally.**
- **Pricing zone:** create Base PZ, select applicable pages, add all stores.
- **Attach linking doc:** in the FTP search "XLS", find the file matching the flyer date, attach to all pipeline tasks.
- **Setup QC:** confirm all pages uploaded (PZ tab → Items View; no un-uploaded SFTP pages); confirm flyer dates (first/last page); 4 standard thumbnails; preview dates set.

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF; linking doc used for both box/tag):** **include special weblinks**; exclude coupons, packaged deals, retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc used for both):** include brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude SKU.
  - **⚠️ Linking-document CTA callout:** a CTA with **no item information, only a URL, MUST be tagged as LINK TYPE** (common error is not tagging it as Link).

## Post-processing / FQC (owned by DOC)

- **Pre-Final QC:** dates vs PDF; availability toggles; thumbnails include retailer logo; all boxed/tagged; spotchecks (20% of PZs); previews clickable; sessions completed; geography correct.
- **Links QC:** use "Items without URL" on the Overview page to address any items/CTAs missing a link.
- FQC checklist.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: HockeyStickMan OneGuide (Google Doc `1GzQig7rPMO79KLLFNPQTWFh6Rkhse0iZ7t2jThcUGuc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
