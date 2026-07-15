# ALDI — Processing Guide

> **Source:** ALDI OneGuide (Confluence VEN → Google Doc `1YUO2oxv…bFTtk`).
> **OneGuide last updated:** Oct 6, 2025.
> **What this covers:** Retailer-specific processing instructions for ALDI so the
> bot can help with "how do I process ALDI / what's special about it?"
>
> 🔒 The source doc includes a file-transfer password, staff contacts, and staff
> emails — **all contacts and credentials are omitted here**. For who to contact
> and any passwords, open the ALDI OneGuide directly (FTP creds via the
> `#sftp-automation` Slack channel).

## Account at a glance

| | |
|---|---|
| Account segment | Core+ |
| Availability | All platforms |
| Slack channels | `#aldi`, `#aldi-ops` |
| Hosted URL | aldi.us/weekly-specials/weekly-ads |
| Flyer types | **1) Weekly Ad** (Insert, weekly) · **2) In Store Ad** (Handbill, weekly) |

## Files & schedule (Weekly Ad / Insert)

- **When files arrive:** Monday.
- **Publication cadence:** Available from Wednesday; Valid from Tuesday (→ valid to following Tuesday).
- **Preview date:** Monday.
- **Processing type:** Auto-stack.
- **Involvement:** Flex — FAB tickets sometimes (Image QC support); no coupons; Strategic Ops does retailer data services (Feedel).
- **Handbill / In Store Ad:** always goes **live 1 week *before* its valid dates** (e.g. handbill valid Oct 8 launches Oct 1). Only **one** In Store Ad should be live at a time (the Sneak Peek version).

## Files delivered

- The retailer's file contact sends files via a **secure file-transfer link**
  (password in the OneGuide — not stored here).
- A separate retailer contact sends the **Store Matrix** doc (used to build the
  generic codesheet) plus digital-page instructions.
- Download locally and re-upload to the ALDI SFTP (Flipp FTP creds via
  `#sftp-automation`). You should end up with 4 folders: Insert PDFs, Insert Images
  (Page 1/2/3 subfolders), Handbill PDFs (next week), Handbill Images (Page 1/2).

## Upload & setup (codesheet build)

> ⚠️ **Codesheet manipulation instructions were updated effective Jan 2026** — see
> the "[12.10.25] ALDI Codesheet Update Instructions" doc linked in the OneGuide.

**Insert — Pages codesheet:** headers `zones, page 1, page 2`. From the Store
Matrix Insert tab: `Ad Version → zones` and `→ page 1`; `Back Ad Code → page 2`
(add `page 3` from *Additional Digital Ad Code* if present). Concatenate
`_Front.pdf` onto page-1 names and `_Back.pdf` onto page-2 names (`.pdf` for page
3). Remove duplicates; find/replace `"_ "` → `"_"` to kill stray spaces. Download
CSV → upload to the code sheet tab in FADMIN.

**Insert — Stores codesheet:** headers `stores, pricing zones`. `Flipp Store
Identifier → stores`; `Ad Version → pricing zones`. Download CSV → upload.

**Handbill:** manual page upload (front = position 1, back = position 2); create
Pricing Zones from the back-page names (usually 2 PZs, ~2 pages each; page 1
applies to both). Stores codesheet same as Insert but uses Handbill-tab Back Ad
Codes.

### ⚠️ Common errors (ALDI-specific)

- **Wrong date in page name** — the date prefix is sometimes a previous week;
  ensure the correct date (e.g. `092122i`).
- **Front/back swapped** — a front page listed as back (or vice versa); page 1 =
  Front, page 2 = Back.
- **Case sensitivity** — FADMIN is case-sensitive; if the FTP filename capitalizes
  `Front`/`Back`, match it in the skins list.
- **Wrong versions paired** — keep matching versions together (e.g. `ODGRN_Front`
  with `ODGRN_Back`).
- **Underscore typos** — missing/extra underscore (e.g. `Lox48` vs `Lox_48`); if
  pages don't upload or FADMIN says a page is missing, check underscores.
- **Missing stores (yellow error on Stores codesheet)** — ALDI frequently adds
  stores. Use the FADMIN error to find the missing store code in the Store Matrix,
  then create the store (ALDI merchant tab → stores → create new store) with store
  code, address, city, name ("ALDI, <city>"), zip, and lat/long (from Google Maps
  → right-click pin). Leave a note in the comments tab so the lead has visibility.
- **Duplicate pages** — remove duplicates from the skins list.

## Image import (⚠️ risk item — critical to account success)

- Page 1 images come in the secure-transfer "LINKS" folder; Page 2 (and Digital
  Page 3) come from the SFTP (download via FileZilla).
- Re-upload to SFTP with subfolders (`…/Page 1`, `…/Page 2`, `…/Page 3`).
- Run **Sessions → Image Import**; FTP url = base path up to the `/`; toggle
  **"From Scratch" off** and submit.
- ⏳ Takes ~30–40 min — **do not** complete setup/leave the run until the import
  finishes with no error.

## QC specifics

- **Box Draw:** complexity Low; Auto-Box **enabled**; Box QC bot **enabled**.
  **Exclude:** coupons, packaged deals (e.g. washers/dryers), retailer logo,
  sign-up page, social media, special weblinks. Box each product block (with
  price/sale story) individually; if one price covers multiple items in a block,
  box them together.
- **Tag / Tag QC:** complexity Low; Auto-tag **disabled**. **Include:** name,
  description, price, sale story, categories, disclaimer. **Exclude:** pre/postfix,
  valid dates, SKU, original price, URLs. PDF image auto-selection **on** (select
  clean PDFs for all items).
- **⚠️ Category tagging is a risk item** — use the retailer's category chart in the
  OneGuide (Meat & Seafood, Fresh Produce, Cheese, Bread/Bakery, Deli, Grocery,
  Dairy, Beverage, Frozen, Household) to tag/QC item categories correctly.
- **Image QC:** prioritize PDFs; **prioritize clean product images over flat-lays
  for produce**. Item Image QC is a **risk item — aim for 100% PDF image selection**;
  ensure the same image across all versions of a produce item.

## Post-processing & FQC

- **Pre-price text QC:** via item export — check `PRICE DROP`/`PRICE DROPS`
  pre-price callouts are applied to all relevant items.
- **Category QC:** via item export — verify each category's items belong (use the
  category chart).
- **FQC:** on "Edit Date/Details," compare valid dates to the flyer (check Grand
  Opening "GO" zones for unique dates); QC all Handbill zones' dates. For the
  "Not all pages have slicing validated?" error, type `n/a` and submit.

## Flyer review risk items

- **Flyer sorting:** Weekly Ad (Insert) in **Position 1**, followed by Handbill
  (In Store Ad).
- Only **one** Handbill live at a time (the Sneak Peek version).
- All flyers available on all platforms.
- Insert: ~50 pricing zones/week (~2–5 pages each); watch for digital pages
  (labelled "digital") with possibly different dates. Handbill: 1–2 PZs/week.

## Known recurring issues (from the issue log)

- Weekly Ad not in position 1 (flyer sorting); multiple In Store Ads live at once;
  page-ordering / publishing errors; Weekly Ad hidden in hosted; digital insert
  distributed regionally instead of nationally (manual error).
- Product images sometimes not clean/isolated (cutouts) due to PDF formatting not
  being compatible with PDF Image Extraction.

---
*Source: ALDI OneGuide (Confluence VEN, Google Doc `1YUO2oxv0MbeQe7BAEAFwe_7TlA0bdR_DPDhgqzbFTtk`),
last updated Oct 6, 2025. Credentials/personal emails omitted. Last reviewed: 2026-07-15.*
