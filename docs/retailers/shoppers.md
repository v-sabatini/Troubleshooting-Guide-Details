# Shoppers (SuperValu) — Processing Guide

> **Source:** Shoppers (SuperValu) OneGuide (Google Doc `1va8K8acYuieM_ay1401jB6E4AES06ivBwwGnGlkn_b4`), updated Apr 28, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Hosted URL | shoppersfood.com |
| Flyer type(s) | Weekly |
| Processing | Auto-stack; Flex Flyer Review; OS Setup; Feedel/Strategic Ops **yes**; no coupons |

## Files & schedule

- **Files received:** Thursday (assets normally arrive ~2 weeks in advance).
- **Cadence:** Available From Wednesday → Available To Wednesday; Valid From Thursday → Valid To Wednesday (available 1 day before valid).
- **Preview:** 1-day preview; go live Wednesday.
- **Linking document:** no.
- **Workflow:** Upload & Setup (Vendor) → Image QC (Flex) → FQC (DOC).
- Keep the **Shoppers URL tracker** updated with correct dates and the flyer run link/ID.

## Upload & setup

- **Codesheet upload:** download the DIG version list `.xlsx` for the week; import into Google Sheets and download the first page as a `.csv`. Upload with **Config `farm_fresh_supermarkets`**, PDF base directory = week's FTP path, **all toggles checked except the 2nd toggle.**
- Mark Flyer Creation complete — stores are added automatically from the `.csv`. Run Setup QC to activate Box Draw.
- Overview → Edit Details: **no theme; Hide in Distribution, Flipp, and Hosted** (toggles); internal run name = `WK #`; **external run name = "Weekly Savings"**; leg heights preset 55/45; thumbnails Standard 4.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot OFF.** Linking doc required (Box Draw specific). Exclude coupons, packaged deals. **Include retailer logo, sign-up, social, special weblinks.** Box all items separately (anything with a price gets a box); use text boxes when needed. Box coupons cleanly including the perforated edges.
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-select ON.** Include name, description, price, sale story, categories, disclaimer, original price. **Include SKU and URLs per overview, but this merchant has no SKU or URL** (N/A). **Exclude pre/postfix and valid dates** (enter valid override dates only if applicable). **Always include Category.** Tag brand, names, sale story, prefix/current price/postfix/original price, and discount **as-is in the flyer.**
- **Image QC:** always choose the most relevant & cleanest image.

## Final QC / go-live (owned by DOC)

- Spot checks: relatively low — use judgment (name, offers, valid dates).
- Leg heights 55/45; thumbnails standard 4.
- Item image QC: PDF > cutout, but select cutout if meat/seafood is not packaged.
- Categories: **no categories on page 1; all other pages should have at least "grocery".**
- Key message "Grocery Savings"; external run name "Weekly Savings"; available 1 day before valid.
- **Flyer Review type: Lite.**

## Out-of-processing — Digital Inserts

- You may get an email indicating a **digital insert** with the file and position. Inserts usually arrive as JPG → convert to PDF before uploading (page size "Fit").
- Upload the digital ad — **no linking, boxing, or tasks required.** Almost always **position 2** of the ad (confirm in the email).
- **Create a trigger to remove the digital insert** for the requested timeframe: Pages → Layout → take out (digital insert) → All Flyers → Run as a trigger → OK.

---
*Source: Shoppers (SuperValu) OneGuide (Google Doc `1va8K8acYuieM_ay1401jB6E4AES06ivBwwGnGlkn_b4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
