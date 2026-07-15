# Co-op Home — Processing Guide

> **Source:** Co-op Home OneGuide (Google Doc `1VYnI7mG6lHx7maS-OK2-gp2I5jwz9cn2fdqrsZJ3hSE`), updated Jul 14, 2026. Contacts/credentials omitted.

Federated Co-op (FCL) banner. Three flyer types documented: **Home Centre (3361, Weekly)** — the active/detailed one — plus **ProGrade (11604, Bi-Weekly) — NO LONGER RUNNING** and **Guide (7798, Ad-Hoc, mini-magazines)**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#fclcalco`, `#flex-processingsupport` |
| Hosted URL | co-op.crs/flyers |
| Publications | Home Centre Weekly (**3361**); Guide ad-hoc (**7798**); ProGrade (**11604** — retired) |
| Cadence (Weekly) | Files Monday. Available Wed, Valid Thu–Wed |
| Processing | Auto-stack; Flex (Flyer Review); OS – Setup; **Strategic Ops (Feedel) yes**; no coupons |

## Files & schedule
- Home Centre (Weekly) files received **Monday**. Guide is ad-hoc; mini-magazines currently fall under the Home Centre flyer type.

## Upload & setup — Home Centre Weekly (owned by Vendor)
1. Download the Flipp codesheet (search xls; find the **HC_TC** page, e.g. `Week 09 HC_TC.xls`).
2. Upload: Name = `upload`; **Config name = `coop_home`**; PDF base from FTP (e.g. `/Weekly/2025/Week 08 HC`); **select all toggles except 2 and 7**; Save & run.
3. Open the URL linking document (FTP) → **Digital Inserts tab** → see the week's inserts → go to the flyer run and **manually add the inserts** → mark Flyer Creation complete.

### Codesheet error handling
- **"Error Backtrace = Found a reused PDF file within the same pricing zone layout":** copy the called-out page directly from the sFTP into the codesheet; if it persists, remove the reused page and add it manually.
- **"Error Backtrace = Page cannot be found in sFTP":** make the codesheet page name match the sFTP page name.

### Setup QC
- Edit Details: no theme; dates match PDF; **key message = the title on page 1** (e.g. "Canada Day"); available everywhere.
- 4 standard thumbnails; attach the links doc if in FTP (e.g. `Wk 37 HABS Flyer urls.xlsx`); Setup QC; Autostack spotcheck.

### ProGrade (retired) & Guide (ad-hoc) — brief
- **ProGrade** (11604, no longer running): manual upload → auto-group → 1 PZ, all stores; key message "Pro-Grade Savings"; **hide on Flipp + distribution only if it fails content policy**.
- **Guide** (7798): create run in Guide type; manual upload all pages; 1 PZ, all stores (match the corresponding week's HABS weekly stores); key message = page-1 title; attach links + items list; **highlight items with a tag symbol for the vendor team**.

## ⚠️ Common errors / risk items
- **Reused-PDF and page-not-found codesheet errors** (see error handling above).
- **Digital inserts** must be manually added and placed in the correct position (usually at upload; if not, add at FQC). Check "Pages not in PZ" and the sFTP for un-uploaded inserts (Details → View Files → "hide uploaded").
- **URLs:** anything with `www.home.crs` gets the `https://www.home.crs/` link only; bottom links tagged `https://www.build.crs/`.
- **Do not box/tag** an item with no sale callout or price — **unless it has a specific link**.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot ON)
- **Include:** sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals, retailer logo (Weekly). No linking doc (Weekly).
- Box all items separately; **box priced sizing variants separately**; box all URLs; box all items with **tag symbols**.

### Tag / Tag QC (Low; Auto-tag OFF; Tag/QC linking doc; PDF Image Auto Selection ON)
- **Include:** brand, name, description, price, sale story, categories, disclaimer, original price, **URLs**. **Exclude:** pre/postfix, valid dates, SKU (Weekly).
- Clean PDF example: Name "BE BOOSTER CABLES, 20-FT.", Description "Two gauge. Copper-coated aluminum cable. (5041 298)". No clean PDF → cutout (avoid black/gray backgrounds).

### Image / Category QC
- Single items → clean PDF if available; multi-item → cutout so all options show. **All pages get categories (1–4); none on Page 1.**

## FQC (owned by DOC)
1. Autostack spotcheck; spotchecks if applicable.
2. **Confirm insert pages were added** in the correct position; check "**Pages not in PZ**" is empty (add missing inserts from the URL doc, box/tag them); check sFTP for un-uploaded inserts.
3. Review details (no theme, no external name, key message = page-1 callout); page categories (1–4, none on page 1).
4. **Item Search → URL IS NOT `_`** and compare to the linking docs for missing/incorrect URLs; `home.crs` → `https://www.home.crs/`.
5. Review boxes (don't box priceless/callout-less items unless they have a link); geography; thumbnails Standard 4 (2,1,2,1) — check zones with an insert in first position; thumbnail on the page with the date/callout banner.
6. Sessions; dates on page 1; Storefront Spotchecks (pages not merged); complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Co-op Home OneGuide (Google Doc `1VYnI7mG6lHx7maS-OK2-gp2I5jwz9cn2fdqrsZJ3hSE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
