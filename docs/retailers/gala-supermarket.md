# Gala Supermarket — Processing Guide

> **Source:** Gala Supermarket OneGuide (Google Doc `1NCel4CP401CLWF2r-lrCIx9e0Er33VOdGQimIQ-yQUI`). Contacts/credentials omitted.

Multi-store grocery banner (Flyer 12257). Files arrive per-store with confusing naming conventions — see the store-code reference below.

## Account at a glance

| | |
|---|---|
| Account tier | Flipp Basic |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | N/A |
| Flyer types | Weekly (12257) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available/Valid Friday → Thursday.
- **Setup & Pre-FQC owned by** FLEX (pre-FQC checklist owned by Vendor); Final QC by FLEX.

## Upload & setup

- **Manual Upload** (Pages Tab → Edit → select from SFTP). Files sit in multiple folders with confusing names. Manually add the store name to Page Name and page numbers into the Grouping Number field; ensure correct language. Save & Confirm.
- **Store-file naming reference** (`##` = launch date):
  - **Patchogue** — `GC00## P01 PC 02##` (folder contains "patchogue")
  - **Worcester** — `GC00## P01 MA 02##` (folder contains "worcester" or "Mass")
  - **Brentwood** — `01 Gala 2 ##`, no code on filename (folder "flippbrentwood"; add "Brentwood" in FAdmin)
  - **Freeport Baldwin** — `GC00## P01 FB 02##` (folder "fqflippgalafreeportbaldwin", also "nassau", nested under "Gala Foods")
  - **Bridgeport** — `GC00## P01 BR 02##` (folder contains "bridgeport")
  - **Centereach** — `Feb ## P1` (folder "flippgalacentereach"; files lack the name — add in FAdmin; only 2 files, Servlet Email Attachment = Page 2)
  - **Boca Raton** — `4370 Gala Fresh ## ## 26` (store code 4370; folder "boca raton" under GalaFresh)
  - **Lakeworth** — `4371 Gala Fresh ## ## 26` (store code 4371; folder "lakeworth" under GalaFresh)
  - **Riverhead Shirley** — `GC00## P01 RV 02##` (folder contains "riverhead")
- **Pricing Zones:** create a zone per store group (only if files exist) and select applicable pages; add all applicable stores via Store Sets.

### ⚠️ Common errors / risk items
- **Retailer does NOT consistently send files for all stores week over week — missing stores is OK.** Geography will *not* be consistent WoW; a discrepancy is acceptable as long as all FTP files were uploaded.
- Confirm no pages remain unuploaded in the SFTP.
- Centereach has no store code — easier to identify/name that file first.

## QC specifics

- **Box Draw (Low; linking doc required; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box each product block.
- **Tag / Tag QC (Low; linking doc required; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Basic tagging guidelines apply.
- **Image QC:** PDF preferred if clean, otherwise cutouts.
- **Spotchecks:** standard pricing spotchecks.

## Final QC / go-live notes

- Confirm dates vs. PDF; available on all platforms; thumbnails include logo; all items boxed/tagged; spotchecks complete (20% of zones); previews clickable; sessions complete.
- **Flyer Review type: Lite** (flyer review guide exists per the OneGuide).

---
*Source: Gala Supermarket OneGuide (Google Doc `1NCel4CP401CLWF2r-lrCIx9e0Er33VOdGQimIQ-yQUI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
