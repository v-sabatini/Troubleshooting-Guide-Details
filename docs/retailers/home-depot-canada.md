# Home Depot Canada — Processing Guide

> **Source:** Home Depot Canada OneGuide (Google Doc `1vHh5IpsUGvj5xB-LXz0Pzqgkb0U4CuO5VIo_XVA3hv8`), updated Jul 14, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Tier 3 Standard) |
| Availability | All platforms |
| Slack channel(s) | `#homedepotca` |
| Flyer type(s) & cadence | Weekly (315) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); DOC (post-processing QC); Strategic Ops — **yes, Feedel/data services**; no coupons |

## Files & schedule

- **When files arrive:** Monday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available To / Valid To Monday.
- **Preview date:** set to the upcoming Monday.
- Bilingual account (English + French pricing zones).

## Upload & setup (owned by FLEX / OS)

Two codesheets: a **Pages codesheet** (same file every week) and a **Store assignment codesheet**.

- **Pages codesheet:** run it — a discrepancy in page count between zones is normal. Then Pages → Edit → search "AS" in page name (7087) → mark all as French; switch AS 7087 pricing zone to French and double-check page assignment; rename the pricing zone to **"AS fr"** (there should be **4 French pricing zones**).
- **Store assignment codesheet:** there are two versions — one for when pricing zone **AR-7102** exists and one for when it doesn't.
- **URL list manipulation:** import URL list to Excel; highlight duplicates in column C and number them to differentiate; compress all images; save as `.xls`.

### Setup QC checklist

- Preview date = upcoming Monday; available everywhere.
- Check vendor assignments (Preview QC is English only); set all vendor task priorities **except** Preview QC and Wayfinding QC to **"high"**; attach the URL list to all vendor tasks.
- Leg heights **45/25**; thumbnails: one page for squares, two pages for rectangles.

## ⚠️ Common errors / risk items (retailer-specific)

- **Look for multiple products per box** — a box must be drawn for **each item with a SKU even if its image isn't on the flyer** (e.g. a 6' and a 5' patio door in one visual = two boxes).
- **Banners are box-drawn/tagged from a weekly spreadsheet** attached to the flyer (used across drawing, box QC, tagging, and QC). It indicates which areas to box, the name to tag, and the link. **Do NOT include "HOME DEPOT" in the link or the description; leave description blank.**
- **FREE items bundled with power tools:** do **not** box the free item separately even if it has its own SKU — keep it in the associated item's box.
- **Appliances always boxed separately** (washer/dryer separate).
- **Colour swatches:** box separately only if **each swatch has its own SKU**; if no unique SKUs, one box for item + swatches.
- **Bilingual pages:** one box around the whole item if a single SKU covers both languages — no separate main + text box per language.
- Only box the item area (e.g. exclude "Why Hardwood?" copy); avoid unnecessary text boxes.

### Pre-Final QC tasks (notable)

1. Ensure all pages have at least 1 slice.
2. Search URL CONTAINS "search" and QC links against the URL list.
3. On appliance pages, search index for VALID TO IS NOT Blank (Item display type) — verify whether the item should have a valid date or if it's from a special-offer banner callout.
4. Search CATEGORY CONTAINS "XX" (PRO) and change to the equivalent "D" (DIY) category.
5. Run "Mass Fetch URLs" custom action; verify all URLs in sessions.
6. Regenerate data-piping groups; rerun data piping on items missing images 2–3× until >70% have images.
7. Confirm no linking-doc names are left as "Item" display type.
8. Spot-check regional banner URLs (banners with 2+ regional versions tagged true to region).
9. Add/QC tracking codes and apply (week numbers **and** dates correct).
10. Upload custom tiles if available (EN tiles → EN zones, FR → FR zones); if none by Monday afternoon, reach out to the retailer.
11. Check largest region in vertical preview; set PQC priority "high" in vendor tab.
12. Flyer sorting: **DIY Weekly > Pro Weekly > Other** (current DIY flyer defaults to bottom of stack).
13. Update the Deep Link Tracker.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot ON.** Linking document required (Box Draw/Box QC specific). **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons.
- **Tag / Tag QC — Low complexity. Auto-tag OFF.** Linking document required. Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.**
- **Image QC:** select the cutout if the PDF includes both washer/dryer, if the PDF is reversed, or if there are black shadows on the PDF; otherwise prefer the PDF image.
- **Post-processing (DOC-owned):** Item Category QC, Item Image QC, URL/Links QC, SKU QC, ad-hoc QC, Final QC.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite.**

---
*Source: Home Depot Canada OneGuide (Google Doc `1vHh5IpsUGvj5xB-LXz0Pzqgkb0U4CuO5VIo_XVA3hv8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
