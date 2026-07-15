# Slumberland — Processing Guide

> **Source:** Slumberland OneGuide (Google Doc `1pP1_CCSb2Paqok-WKk0Bm89UFJuzinCsMaithB1XeR4`), updated May 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#slumberland` |
| Hosted URL | slumberland.com |
| Flyer type(s) & cadence | Flyer (type #791) — ad-hoc; Available/Valid From Sunday, Available/Valid To Saturday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |

## Files & schedule

- **When files arrive:** ad-hoc.
- **Publication cadence:** Available From / Valid From = Sunday; Available To / Valid To = Saturday.
- **Preview date:** set the Friday before go-live (2 days before go-live).

## Upload & setup (owned by Flex)

- **If a codesheet is provided (from FTP):** use the **[Master]** tab — Column A = first letter of the file names (change on the codesheet if it doesn't match before uploading); Column B = store code (assigns those stores to the base pricing zone). Save as CSV.
  - Always **1 pricing zone created**, but store assignments vary week-over-week.
- **If NO codesheet (manual upload):** **[Pages]** → manually upload pages and create a base pricing zone. **[Add All]** stores to the base pricing zone, then use the **[Geography]** tab to check which new stores (shown in green) were added and remove them from the base pricing zone.
- **[Overview] → [Edit Details]:** Available everywhere; Key Message from front page; External run name = same as KM; Preview date = Friday before go-live; **no theme**.
- Thumbnails: Standard 4. Spotlights: QC Key Message.
- **Setup QC:** check date on bottom of last page (only end date shows — start date is always the Sunday before).

### ⚠️ Common errors (retailer-specific)

- Codesheet "store not found" error → likely a new store; add manually to FAdmin.
- "Not all files uploaded" error at Setup QC → **safe to ignore as long as you've checked the FTP.**
- At Final QC, "slicing not checked" error → write "slicing checked" in notes; **[Force Mark Complete]** if it occurs, otherwise you won't be able to access the preview.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **include** packaged deals (e.g. washers/dryers); **exclude** coupons, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs; exclude disclaimer. Include brand + size in the name. URLs provided in separate linking docs (EN & FR). Categories are typically Living Room, Bedroom, Dining Room, Beds and Mattresses.
- **Image QC:** prefer clean PDF image; cutouts otherwise.

## Post-processing / Final QC (owned by DOC)

- Ledge Heights: 40/30.
- Confirm all items boxed — all SKUs, all logos, event callouts (tag as item + disclaimer if applicable).
- **Check links** (search SKUs on website for any missing): Slumberland home, "No interest/financing", Free Shipping, Mattress category, "120 Night", Price Match, Financing Terms disclaimer (bottom of last page), and social links (Facebook, Pinterest, Twitter, Instagram, YouTube).
- **[Pages] → [Categories]:** skip page 1, 1–3 per page. Use **[Beds/mattresses]** for a mattress or bed frame vs. **[Bedroom]** for bedroom sets. Then **[Draw Category Thumbnails]**.
- **[Manage Tracking Codes]:** mmdd = the available-from date. Code #1: source [All], var `utm`, value `WEB_AD_FLIPP_yyyymmdd`. Code #2: source [Mobile], var `utm`, value `WEB_MOB_AD_FLIPP_yyyymmdd`. Then **[Apply All Tracking Codes]**.
- Verify **[Sessions]** URL, horizontal & vertical previews, then run Final QC pipeline (available everywhere).

## Flyer review

- **Flyer Review Type: Lite.**

## Out-of-processing

- **Weekly preview links** (sent Friday before): Hosted preview, Vertical preview, and Direct link (direct link won't work until ads are live) — see the OneGuide for the exact URL construction.
- **Multi-week "Memorial Day"-style events:** new pages are inserted on the Sunday of each week — file an After-Hour Trigger Check ticket. Manually upload the new pages; verify no stores added/removed against the prior week's codesheet; update preview date; after OS boxes/tags, redo page categories (skip page 1), redraw category thumbnails, check missing links, check **[Sessions]**, set the trigger to place new pages in positions 1–4, and create OPTICS trigger-check tickets (Ops + After-Hours).
  - **Note:** a specific store (e.g. Batavia) may be on hold — do not include it in the base pricing zone until cleared.
- **After the trigger runs:** confirm pages inserted into positions 1–4, redraw thumbnails (Standard 4), delete old tracking codes and create new ones (Apply All), re-generate Data-Piping Groups, toggle the Auto-Stack spotcheck Incomplete→Complete, check **[Sessions]**, verify live on slumberland.com and the Flipp app, then close the OPTICS tickets.

---
*Source: Slumberland OneGuide (Google Doc `1pP1_CCSb2Paqok-WKk0Bm89UFJuzinCsMaithB1XeR4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
