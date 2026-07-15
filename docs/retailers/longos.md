# Longos — Processing Guide

> **Source:** Longos OneGuide (Google Doc `1ln-lCqplH7smFcwMhBlYcnDizdM5w7Syuw-z4byHXTs`), updated Sep 19, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | All platforms |
| Slack channel | `#longos` |
| Hosted URL | longos.com/flyers |
| Publications | Weekly Flyer · Pharmacy · Baby · Garden Foods (separate merchant) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Feedel/retailer data services |

## Files & schedule

- **Files received:** Wednesday.
- **Cadence:** Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. **Live Thursdays.** Set internal preview date to **Tuesday**.

## Upload & setup (owned by DOC)

All flyers processed the same way (Garden Foods processed under its own merchant, hidden in hosted).

- **Manual upload:** select files from FTP in the dated folder — **⚠️ two folders share the correct date; use the ALL-lowercase one.** Upload all, click Auto Group (usually separates PZs and indexes pages: `…0001.pdf` → page 1, etc.). Confirm indexing before Save & Complete.
- **Pricing zones & stores:** create zones per the store list (usually Zone 1, Zone 2, Zone 3 — check weekly). Zones may include 'Corp', 'Garden Foods', occasionally 'Passover' or a new-store zone. Put pages into zones by file name, matched to the store-list info (Zone 1 = Corp, Zone 2 = Garden Foods, Zone 3 = passover in the example). Pages named "zone 1_p0001.pdf" go to zone 1.
- **Stores:** build a **generic stores codesheet** from the store-list second tab (use the template). Ensure PZ names in the codesheet match Fadmin. **⚠️ If the flyer has Garden Foods pages (usually Zone 2), the Garden Foods store number in Fadmin is 50 even though the store list may say 39** — update Zone 2 accordingly. Upload the generic codesheet in "codesheets".

### Setup QC checklist
- **No linking document/spreadsheet** for any Longo's flyer.
- Valid dates: **⚠️ if dates on the flyer run differ from the flyer pages, flag to full-time Ops** (staggered dates — see risk items).
- Rare/ad-hoc: Baby → one PZ "Base", Add All "*Baby Flyer"; Pharmacy → one PZ "Base", Add All "*Pharmacy Flyer".

### Garden Foods (separate merchant)
- Same upload; **no store list**. Select only pages with "Garden Foods"/"Zone 2" in the name (ignore "already uploaded" warning). Base pricing zone, add all pages. Only **one store** to add (Add All under stores/FSAs). Toggle: hidden in hosted, visible in distribution & Flipp. **No cloning required (as of March 2026).**

## ⚠️ Common errors / risk items

- **Staggered dates:** pricing zones may have different dates for the same flyer — confirm with the Longo's team, then edit dates per zone (Overview → Edit Dates/Details).
- **Page-level valid dates:** last 1–2 pages often have different valid dates than the rest — tag from the bottom of each page. Check **every** page for specific deals.
- **Monthly ads:** last page (and sometimes front page) has its own deals — override the flyer valid dates with item-level valid dates.
- Sales stories that apply only to certain items on a page; postfix sometimes incorrect or missed.
- Image QC: images with shadows/backgrounds.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box all items with prices (text boxes when needed, no overlapping boxes). Don't forget veggie/fruit boxes.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.**
  - Brand in Brand field; remaining bold text in Name.
  - **Valid dates:** for two-week flyers with dinner-day sales (Monday/Tuesday etc.) that don't name a specific date, tag item dates as the flyer valid dates (Fadmin can't choose two different Mondays). Last-page items: use the page-bottom dates.
  - Categories (department chart): Babies & Kids, Electronics, Fashion, Floral, Grocery, Health & Pharmacy, Home & Garden, Office, Pets, Sports. Every item needs both an item category and a Google category.
  - **Sale story:** special banners, discounts/dollars off (red under current price), and Thank You Rewards points earned.
  - Page categories from the top of the page (else the closest drop-down).
- **Image QC:** use clean PDFs (never black backgrounds); **most PDFs are not clean — cutout preferred** when no clean PDF exists.

## Post-processing & FQC

- **Item Image QC (Flex):** spot-check OS image selection.
- **Ad-hoc (Flex) — FMP flap page:** retailer sends "FMP Flap" Fri/Mon before go-live; process and place in **position 2 of every pricing zone**. FMP with "Longos" in the name → Longos flyer; "Garden Foods" → Garden Foods merchant.
- **Final QC (DOC):** preview dates as specified; Mark In Store Only; check horizontal/vertical previews (auto-publish first); Thank You Rewards may appear on Living Well pages. **No cloning required (March 2026).**
- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Longos OneGuide (Google Doc `1ln-lCqplH7smFcwMhBlYcnDizdM5w7Syuw-z4byHXTs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
