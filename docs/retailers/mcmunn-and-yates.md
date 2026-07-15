# McMunn & Yates — Processing Guide

> **Source:** McMunn & Yates OneGuide (Google Doc `1eFyVghZuOH-e9X8rztLhexNd03sxHtEjwfhqs46ALZo`), updated Jun 24, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium (merchant 2568) |
| Availability | All platforms |
| Slack channels | `#mcmunn_yates`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | mcmunnandyates.com |
| Flyer type | Flyer 2417 (**biweekly**, runs 2 weeks) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons/Feedel |

## Files & schedule
- **Files received:** Monday (linking document dropped to FTP).
- **Cadence:** Available From Wednesday → Available To Wednesday (biweekly, 2 weeks); Valid From Wednesday → Valid To Thursday. **Monday preview.**
- Retailer refers to ads as e.g. "July #1", "July #2" (reflected in the merchant schedule).

## Upload & setup (owned by Vendor)
- Confirm dates in email; visible everywhere; no theme; no external name.
- **Manual upload:** Pages tab → Edit → select pages that match the **flyer run name** (e.g., "July #1"); select all lowercase pages for all zones labelled with that name (North, SouthA, SouthB, SouthC, SouthD, etc.) → Confirm & Upload.
- Auto-Group or manually number; ensure language = **English**; Save & Confirm (do NOT process internally).
- **Pricing Zone creation:** create PZs based on the **Version List `.xlsm`** in FTP and assign stores accordingly. Add pages labelled with the PZ name to the correct zone (SouthA pages → SouthA zone).
- **Attach the linking doc from the SFTP.**
- **Setup QC:** confirm all pages uploaded (Items View); confirm dates (first/last page); thumbnails Standard 4; preview dates set.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **include** retailer logo; exclude coupons, packaged deals, sign-up page, social media, special weblinks. Box all items separately (text boxes when necessary); box items with multiple types/models individually.
- **Tag / Tag QC (Low; Auto-tag ON; PDF Image Auto Selection ON):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU** (tagged in brackets per notes but not the SKU field).
  - **⚠️ Tag-Lite retailer — DO NOT tag Name, Brand, Description, SKU, Sales Story** (auto-tagged). If a Name is missing, tag the name.
  - URLs come from the Links Spreadsheet in the Vendors tab; match SKUs on the linking doc to flyer items and use the URLs **exactly** as provided.
- **Image QC:** **clean images / PDFs must be selected — retailer does not want cutout images (PDF Image mandatory).**

## ⚠️ Common errors / risk items (most valuable)
- **PDF images mandatory** — no cutouts.
- **Linking:** sales banners may have a different link than the products beneath them — tag by matching the SKU. Retailer may email specific links.
- Retailer may note "LINK ENTIRE AD TO WEBSITE" in the linking doc "notes" column for banners — box the banner/lifestyle image accordingly.
- **⚠️ Box QC — combo pages:** if combo pages appear during the Box QC task, **DELETE ALL BOXES & DO NOT DRAW ANY** (pages not cut).

## Post-processing / FQC (owned by Flex)
- **Pre-FQC:** dates per PDF; all items have a URL (fill missing from the linking doc); page names match PZ name (southA → southA pages); toggles (available everywhere); thumbnails include retailer logo (standard 4); all items boxed/tagged; spotchecks 20% of PZs; previews clickable; sessions complete; geography correct (no stores added/missing).
- **Flyer Review type: Lite:** flyer dates, sessions, previews, tagging accuracy, geography, availability toggles.

---
*Source: McMunn & Yates OneGuide (Google Doc `1eFyVghZuOH-e9X8rztLhexNd03sxHtEjwfhqs46ALZo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
