# Ashley Furniture Homestore — Processing Guide

> **Source:** Ashley Furniture Homestore OneGuide (Google Doc `1gHwRvKATecE2W6jjULExiZy9F5HGS65oM-vOGF32_ac`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#ashleycanada` |
| Hosted URL | flyertown.ca/flyers/ashleyfurniturehomestore-west |
| Flyer type(s) & cadence | 4149: West Flyer (ad-hoc) · Flyer Type 2 (Monthly) |
| Processing | Trim Stick; Flex (FAB Tickets); OS Setup; **Feedel/Strategic Ops = Yes**; no coupons |

## Files & schedule
- **Files received:** ad-hoc. **Cadence:** Available From Monday / Valid From Tuesday.
- **Workflow:** Upload/Setup by Vendor; Image QC by Flex; FQC by DOC.

## Upload & setup (owned by Flex)
1. Pages → Edit → select correct files for the week → Autogroup → Save and complete.
2. Create pricing zone: **Base**. Add all stores.
3. Check sessions — all green **except** PDF Image Auto Selection. Clear remaining FTP files.
4. If no linking doc in FTP, add vendor note "No linking doc, proceed with tasks"; if present (FTP or email), upload as mass attachment to all vendor tasks.
5. Overview → Edit Details → Available everywhere, No theme.
6. Check the Flipp × Ashley Homestore sheet to see whether a **UTM code** should be applied.
- Setup QC: thumbnails Standard 4.

## ⚠️ Common errors / risk items (retailer-specific)
- **URL domain (top risk):** always use the **`.ca`** URL (`ashleyhomestore.ca`). Do **NOT** use `.com` (`ashleyfurniture.com`).
- **Disclaimers:** found at bottom of each page; tag the disclaimer matching the symbol beside the price/name. Every item with a symbol (`*`, `**`, †, ††) must have a disclaimer.
- **Data piping:** some items won't pipe because they aren't live on the website yet — spot-click items to confirm. **Data-piping should not fall below 90%.**
- **SKUs must be prefixed `AFHS-`** (e.g. `AFHS-M71131`, not `M71131`); add the prefix if missing. For multiple SKUs, enter the package-deal SKU first, then individual items.
- Only search SKUs on the Ashley **Canada** website (ashleyhomestore.ca).

## QC specifics
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** Exclude coupons. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. Linking doc is Box-specific.
- **Tag / Tag QC (Low; Auto-tag OFF):** Include all fields. Brand entered EXACTLY as in the name field, name as-is with significant words capitalized. Price/original price as-is; do **not** put sale story in postfix. Valid-date override only for 1–2 day sales differing from flyer dates. Confirm each URL (flag to Ops if wrong). Categories = appropriate Google category.
- **Image QC:** data-piped image > pdf > cutout. If piped + pdf images are bad, delete the URL to enable cutout selection, then re-insert the URL.
- **Post-processing (DOC):** Item Category QC, Item Image QC, URL/Links QC, SKU QC.

## FQC / go-live (owned by DOC)
- Apply all tracking codes. Item Search for missing SKUs (`SKU IS BLANK`, Item Type = Item) and missing URLs (`URL IS BLANK`) — appliance pages often left blank. Saving a URL auto-runs data-piping.
- Data Piping → aim near 100% Data Piped Image. Image QC (piped > pdf > cutout).
- Page categories by Grouping #/Page Name; **pages 1 and 4 get no categories**; categories must match the page; ON/WEST share categories but WEST APPLIANCES uses **Home Appliance**.
- Open Additional Links xlsx and confirm every link is boxed/tagged. Wayfinding QC, Spotcheck QC, mark items In-Store Only, re-verify URLs. Check horizontal (Flipp Web) and vertical (App/Hosted) previews.
- **Flyer Review type: Lite.**

## Out-of-processing
- Standard page swaps / post-live checks as directed.

---
*Source: Ashley Furniture Homestore OneGuide (Google Doc `1gHwRvKATecE2W6jjULExiZy9F5HGS65oM-vOGF32_ac`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
