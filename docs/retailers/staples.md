# Staples (Canada / Professional) — Processing Guide

> **Source:** Staples Canada/Professional OneGuide (Google Doc `1O11mnxwQZGBYewJgG5L35J2-FYkTW3xcowA7sntsqvE`), updated Oct 1, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#staplesca` |
| Processing | Auto-stack; Strategic Ops (Feedel/retailer data services); no Flex, no OS, no coupons |
| Banners / flyer types | **Staples Canada / Core (PREF)** — Business Flyer (2802), file type PCAM, codesheet "Pref" · **Staples Professional** — Cross Category (5782, "Pro"), Cross Category Supreme (11147, "Sup"), Cross Category Denis (11909, "Den") · **Staples Preferred** (2797, "PrefCA") — **inactive/no longer processed as of April 2025** |
| Hosted URLs | Staples Canada EN staples.ca / FR bureauengros.com · Staples Professional eway.ca (EN/FR), Denis eway.ca/denis |

## Files & schedule

- **When files arrive:** schedule / ad-hoc.
- **Cadence:** typically monthly; dates usually on the front page, else on the publication schedule/tracker.
- **Preview date:** week before go-live.
- **Linking document:** n/a.
- Files are dropped by the retailer into the **"Ops Flyers"** folder in the SFTP (SFTP credentials in the OneGuide — not stored here). If files land elsewhere, ask the retailer to correct.

## Upload & setup

- Create flyer shells when the retailer emails about a file drop. Put "Pref", "Pro", "Sup", "Den" in the shell name to identify banners; add the flyer ID to the publication tracker.
- **Use the codesheet (Pref / Pro / Sup) that matches the flyer run name.**
- Manual upload of pages + store sets, OR codesheet upload. Download the codesheet CSV per banner.
- In codesheet **column B (Zones):** if there are duplicate zone names, append "EN"/"FR" so Fadmin can differentiate languages.
- If uploading via codesheet, verify French pages uploaded as French pages — if not, a Language or Zones column error (extra space, or ROC EN vs ROC FR not differentiated).
- Thumbnails: **Standard 4**.
- **Edit Details:** no preview days. **Staples Canada:** hosted only, Secondary publication, no theme. **Staples Professional / Supreme / Denis:** hosted only, no theme.
- For **Staples Canada**, add a reminder note in the **Tag** and **Tag QC** vendor tasks: EN → search SKUs on staples.ca for URLs; FR → search on bureauengros.com.

## ⚠️ Common errors / risk items (retailer-specific)

- **URL sourcing (most important):** For **Staples Canada & Staples Preferred**, URLs must be found by **manually searching each SKU on the website** and copy/pasting from the address bar — **DO NOT FETCH URLS.** EN → staples.ca, FR → bureauengros.com. For **Staples Professional / Supreme / Denis**, URLs **can be fetched**.
- If a Staples Canada URL search returns items via `URL CONTAINS AffixedCode`, those URLs must be fixed manually (or, for 30+ items, submit an OS reprocessing ticket — check with DOC).
- Cross-language check: EN items must not carry `bureauengros` URLs and FR items must not carry `staples.ca` URLs — search and correct.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Include the retailer logo (page 1). **Box all items** — some items have pricing but no image; box the item name/description + price. Exclude coupons.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON):** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Enter fields "as is."
  - **Categories:** every item must have a category; if unsure use **Office Products**.
  - Enter valid dates only when a callout differs from the flyer dates.
- **Image QC:** select a clean PDF image if available (most items have one); use a cutout only if no clean PDF.

## Post-processing (owned by DOC)

- **Item Category QC:** every item must have a category — Item Search → Categories IS blank → multi-edit → add **Office Products**.
- **URL/Links QC:** check email for any additional retailer links. **Box and tag the Staples logo(s) on page 1 as Display: Link** with the banner URL (Staples Canada EN staples.ca / FR bureauengros.com; Professional EN eway.ca/en / FR eway.ca/fr). Ensure a majority of items have links; add missing ones per the manual/fetch rules above.
- **Final QC:** check Geography for added/missing stores (add missing stores via Merchant → Stores/Sets); ledge heights **45/35**; thumbnails Standard 4.

## Flyer review

- **Flyer Review type: Lite.** EWAY = Staples Professional, PCAM = Staples Canada (Business); content usually identical between them except the logo. Check dates/external run names per the publication tracker, hosted-only, normally 2 pricing zones (EN & FR), all items boxed (visible-price CP non-enforceable since hosted only), pages chronological, geography no change.

---
*Source: Staples (Canada, Professional) OneGuide (Google Doc `1O11mnxwQZGBYewJgG5L35J2-FYkTW3xcowA7sntsqvE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
