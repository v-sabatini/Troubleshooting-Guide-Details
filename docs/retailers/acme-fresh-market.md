# Acme Fresh Market — Processing Guide

> **Source:** Acme Fresh Market OneGuide (Google Doc `1QL4dQjicbnqam0zqfX0Ez0nc4iAWKeqH1D4x5FChnKs`), updated Nov 27, 2025.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#onboardings`, `#flex-processingsupport`, `#1plat-acmefreshmarkets` |
| Hosted URL | acmestores.com/weeklyspecials |
| Flyer types | Weekly · Secondary Content (one-pagers / promotional) · Specialty Publications · GMI/SAV |
| Processing | Auto-stack; **Flex = Processing Support**; no OS-outside-standard, no coupons, no Feedel/data services |

## Files & schedule

- **Files received:** Thursday and Monday.
- **Cadence:** Available From Tuesday **7 AM**, Valid From Wednesday; Available To Thursday 12 AM, Valid To Wednesday.
- **Preview date:** None.
- **Linking document:** Provided by the retailer — attach to OS tasks.

## Upload & setup (owned by Vendor)

- **Change the "Available From" time from 12:00 AM to 7:00 AM.**
- **Manual upload:** upload all pages in the SFTP whose name/folder carries the "Valid From" date.
- Typically **2 regional versions — "Buffy" and "Buck"**. The retailer sometimes adds a **"Medina"** zone (labelled accordingly).
- **Manually create one pricing zone per regional version** and assign each its store set. **If a "Medina" zone is required, add store `22` to it and remove store `22` from the Buffy and Buck zones** so there's no overlap.
- Attach the linking document to vendor tasks if found in the SFTP; if not, flag to the Ops account team.

### ⚠️ Common errors / risk items (retailer-specific)

- Forgetting to change Available From to **7 AM** (default is 12 AM).
- **Store 22 overlap** — if Medina is used, store 22 must be in Medina only (removed from Buffy/Buck).
- **Geography discrepancy:** [Flex Upload team] check the Geography tab against the previous week's distribution; flag any discrepancy to Ops.
- **External name must match exactly** (public-facing): Specialty Publications = "Bonus Online Savings"; GMI/SAV = "Health, Home & Beauty".

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** linking doc required (used for both box & tag). Exclude coupons, packaged deals, retailer logo, sign-up page, social media. **Include special weblinks.** Box items individually; box banners where a link is provided in the linksheet.
- **Tag / Tag QC (Low; Auto-tag OFF):** linking doc required. Exclude brand. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. Apply URLs per the linksheet.

## FQC / go-live (owned by DOC)

- Thumbnails, legibility heights, check geography vs. previous week, standard FQC checks.
- **Weekly Ad only — add UTM code at the Flyer Run level:** Manage Tracking Codes → Add Code (Flyer Run section) → Type: **Dynamic Variable**, Code Source: **All**, Variable Name: **`utm_campaign`**, Variable Value: **`mmddyyWeeklyAd`** (updated to the flyer live date each week) → confirm → **Apply All Tracking Codes**.
- **Flyer sorting:** weekly ad displayed first.
- **Flyer Review type: Lite** (owned by DOL).

## One-pagers / promotional flyers (e.g. 3-Day Meat Sale)

- Create a new flyer run in the **Secondary Content** flyer type with the correct date. Most are **Hosted Only** (confirm with Lead if unsure).
- Upload pages into pricing zones (Meat sales: multiple page-1 versions assigned to single stores per version's file name as their own zones; other promos follow the contact's distribution instructions).
- Complete Setup QC → select **"Mark As Vanilla"** (bottom-right of Overview) → notify Lead to review.

---
*Source: Acme Fresh Market OneGuide (Google Doc `1QL4dQjicbnqam0zqfX0Ez0nc4iAWKeqH1D4x5FChnKs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
