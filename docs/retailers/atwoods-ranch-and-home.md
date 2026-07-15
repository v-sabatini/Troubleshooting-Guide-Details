# Atwoods Ranch & Home — Processing Guide

> **Source:** Atwoods Ranch & Home OneGuide (Google Doc `1wLtiirDZu3icD7Gxsfb5VtMSiIFkzie2oStE--ClFTE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 |
| Availability | All platforms |
| Slack channels | `#atwoods` |
| Hosted URL | www.atwoods.com |
| Flyer type(s) & cadence | Scheduled + ad-hoc (regular flyer; plus Bargain Barn monthly) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule
- **Files received / cadence:** ad-hoc. **Linking document:** Yes.
- **Workflow:** Upload/Setup by Vendor; FQC by DOC. Track the run in the VAST spreadsheet (fill flyer run ID + available date, set SETUP READY).

## Upload & setup (owned by Vendor) — Codesheet, Config `m1000`
- Download files from the emailed transfer link (pages, codesheet, linking doc). Upload **only the PDF pages** to the FTP (not the codesheet/linking doc). **(FTP credentials in the OneGuide — not stored here.)**
- **Code Sheets** upload: Name = Weekly, choose file, **Config Name `m1000`**, PDF Base Directory from FTP, **Toggles 1, 3, 4, 5, 6** → Save Code Sheet → Process Code Sheet.
- Overview → Edit Details: available everywhere, theme (e.g. Black Friday) or none, key messages (page-1 callout or generic e.g. Weekly Savings), **external run name from the codesheet/emails**.
- Thumbnails Standard 4; Pricing Zones → Spotlights to QC key messages; attach the linking doc via Vendors → Upload Mass Attachment (all tasks). Pipeline: Setup QC.

## ⚠️ Common errors / risk items (retailer-specific)
- **Ad-hoc publications** (Bargain Barn, Salina, Siloam) arrive randomly — create an empty flyer-run shell, confirm dates with the retailer, and bump the new flyer in `#atwoods` to BD. (Reference existing runs in the "Flyer" flyer type for setup.)
- **Bargain Barn** is a 2-page clearance flyer with **NO retailer logo** → cannot go on Flipp (content policy: needs the Atwoods name/logo on the front). Set it **available only on Hosted**, external run name & key messages "Bargain Barn".
- **Atwoods logo** on page 1 links to atwoods.com. **Facebook** is the only social to tag. **Email Signup** (last page) must be tagged — box only the top half (exclude the "JOIN" text).
- **Credit-card / Slice / Summary-of-credit-terms** links must be tagged (URLs listed in the OneGuide). **Summary of Credit Terms has an UPDATED URL** — do not miss tagging it.
- **Image QC:** most regular-flyer images are cutouts (PDFs aren't clean); watch for OS selecting items with a **black background**.

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** **Include** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box the Credit Card & Slice pages/boxes and the summary-of-credit-terms (usually bottom of page 9). Linking doc is Box-specific.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF Image Auto Selection ON):** Include all fields. Linking doc is Tag/QC specific; brand is Box-specific.
- **Item Category QC (DOC):** food → Home & Outdoor Living; guns → Outdoor Recreation.

## FQC / go-live (owned by DOC)
- Legibility heights 50/40 (pre-set). Item Image QC (mostly cutouts; avoid black backgrounds). Category QC via "Items Without Analytics Categories". Page categories: page 1 none; guns = Outdoor Recreation.
- Tag the risk-item links (logo, Facebook, email signup, summary of credit terms). Links QC for items without a URL: pull the CSV from Vendors, reformat to item import (delete "item name"/"Error", rename `links` → `english_url`, drop rows with no URL), Import Items. Check horizontal & vertical previews.
- Pipeline: Final QC. **Update Flyer Sorting** so the newest weekly flyer shows first (confirm via emails/retailer if unsure).
- **Flyer Review type: Lite.**

---
*Source: Atwoods Ranch & Home OneGuide (Google Doc `1wLtiirDZu3icD7Gxsfb5VtMSiIFkzie2oStE--ClFTE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
