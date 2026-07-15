# Dormez-Vous — Processing Guide

> **Source:** Sleep Country Canada / Dormez-Vous OneGuide (Google Doc `1YQGjJAeOq4oALWbC67SNSDwDhODSGarBU7KI6cfJRPY`), updated Dec 23, 2025. Contacts/credentials omitted.
>
> This shared OneGuide covers **Sleep Country Canada (eFlyer, 3308)** and **Dormez-Vous (Offre spéciale, 3309)**. Notes below focus on the Dormez-Vous type, with Sleep Country details where they differ.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Flipp only** (Flipp & Distribution; hidden on Hosted) |
| Slack channel(s) | `#sleepcountry` |
| Hosted URL | sleepcountry.ca · fr.dormezvous.com |
| Flyer type(s) & cadence | eFlyer (3308) · **Offre spéciale Dormez-Vous (3309)** — both **ad hoc** |
| Processing | Auto-stack; Flex (FAB tickets / Flyer Review); no coupons; **Feedel / retailer data services: Yes** |

## Files & schedule

- **When files arrive / cadence:** ad hoc (refer to the Retailer Schedule).
- **Available:** 1 day before. **If the flyer is live Sunday or Monday, set Preview Date to Friday.**
- **Availability:** Flipp & Distribution only. External Run Name: None. No theme.

## Upload & setup

**Pre-setup (DOC):** submit a PSS Ad-Hoc ticket once files are received; add new CTA linking docs to the Sleep Country Canada Drive folder.

**Dormez-Vous setup (owned by FLEX):**
- Pages → Edit → **select French files first**, toggle Language to French and Save; refresh and select English files.
- Autogroup → Save and complete. Flyer Creation → Start Task.
- Pricing Zones: **English PZ = English pages; French PZ = French pages.** Add "All Stores" to both.
- **⚠️ NEW — Remove store `300` from regular weekly flyers** (store 300 is Warehouse-Sale-only, ad-hoc). **Exception:** Warehouse Sale store `327` still needs to be added week over week.
- Thumbnails: Standard 4. Legibility heights = **40, 30**. Confirm all sessions run; complete Setup QC checklist.

**Sleep Country (eFlyer) setup differences:** single National PZ (Add all files/stores); occasionally a separate AB cover → create a 2nd PZ swapping page 1 for the AB page (National PZ = all stores minus AB set; AB PZ = all stores minus non-AB sets). **NEW — remove Warehouse Sale stores from regular weekly flyers.**

**Setup QC (NEW Sep 2024):** download the CTA URL doc (both FR & ENG page 4 for Dormez-Vous) and mass-attach to Vendor Tasks. Add note: *use the CTA URL Links doc to box/tag/add links to corresponding headings; use the attached PDF page to enter disclaimers (from the bottom of the page) into the disclaimer field.*

### ⚠️ Common errors / risk items (retailer-specific)

- **Disclaimers:** found at the bottom of each page. Tag the disclaimer matching the symbol beside the price or item name. **Every item with a symbol (`*`, `**`, `†`, `††`) must have a disclaimer.** If an item has two corresponding disclaimers, include **both**. Also add any item-specific info to the disclaimer field alongside the page disclaimer.
- **Valid dates:** every item MUST have a valid date. Verify against the disclaimers at the bottom of the page; tag the disclaimer date if present. **If no valid date is given, use the flyer run's last live date as Valid To.** A single image with multiple products (mattress + frame + headboard) can carry different asterisks → different valid dates.
- **Multiple products in one image:** box/tag each as its **own item**, never as one item with the others in its description.
- **Items without a price:** still tag; add a Sale Story (e.g. "Surround yourself in a luxurious duvet").
- **Links:** keep languages/banners separate — **Sleep Country = English sleepcountry.ca links; Dormez-Vous = dormezvous.com (FR at fr.dormezvous.com).** No cross-banner links. The site has no search — find items via categories/brand.

## QC specifics

- **Box Draw (Medium).** Dormez-Vous: Auto-Box ON, Box QC bot ON, no linking doc. Sleep Country: Auto-Box ON, Box QC bot OFF, linking doc required. **Include** coupons and (Sleep Country) special CTA links/banners/price callouts. **Exclude** packaged deals, retailer logo, sign-up page, social media, special weblinks. Item boxes = image + price + description.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU** (N/A). PDF Image Auto Selection = Yes (Sleep Country).
  - **Name/Brand:** brand above the item name; **append the item type** (Mattress, Headboard, Pillow, or Duvet).
  - **Price:** current price is bold black/red text and/or a red bubble; original price has a strikethrough.
  - **Pre/Postfix:** prefix = callouts like "starting at"/"only"; postfix = info directly under/beside the price; asterisks go in the postfix, **after** the text.
  - **Categories:** tag Category and Google Category, as specific as possible.
- **Image QC / datapiping:** Filter → Data Pipe All (should reach 100%; **RISK** — if it stalls, check the URLs that won't clear and the landing page). Then Custom Action "Set Cutout Images" with the Flyer ID. Use a PDF image only when no product URL was found.

## Final QC / go-live

- Mark Autostack Spot Check complete; page 1 may have categories.
- **Disclaimer QC (FLEX):** check every item's disclaimer against the PDF — postfix has the correct symbol, correct disclaimer text applied (**DV FR is hit-or-miss and often needs correction**); every item has valid from/to dates.
- **Item Search (FLEX):** Disclaimer Text IS ___; URL Contains the *other* banner (ensure no cross-banner links); URL IS ___ (fill missing links from the site, toggling site language); Valid To IS ___ (add dates); URL IS NOT ___ → export and fix wrong-product/wrong-language URLs.
- **Sleep Country tracking URLs:** in Manage URLs, add the **Open Flipp App** and **Impression** DoubleClick tracking URLs (per-banner values in the OneGuide — not stored here).
- Image QC; confirm CTA links added as "Links"; complete outstanding tasks/sessions; **Mark Items Store Only**; FQC checklist.
- **Flyer Review type: Lite** (owned by FLEX).
- **Out-of-processing:** standard page swap.

---
*Source: Dormez-Vous OneGuide (Google Doc `1YQGjJAeOq4oALWbC67SNSDwDhODSGarBU7KI6cfJRPY`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
