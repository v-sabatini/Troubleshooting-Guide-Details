# Publix (Weekly, Spanish, Extra Savings) — Processing Guide

> **Source:** Publix OneGuide (Google Doc `1qsSR01gkX7XTaK_zf-ivCXAggW77lJjk5-kMKRSIOJs`), updated Apr 20, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Relationship: Excellent) |
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#publix`, `#publix_offapp` |
| Hosted URL | None (ongoing hosted tests) |
| Flyer types | **Weekly [5944]** · **Bilingual/Spanish [5944]** · **Extra Savings [9562]** (bi-weekly) |
| Processing | Auto-stack; no coupons, no Feedel |
| Ownership | **Weekly & Spanish:** DOC uploads, **OS completes FQC** (Flex not involved). **Extra Savings:** Flex uploads & FQC. DOC handles comms/ad-hocs/page swaps. |

Files received **Tuesday (late)**. High item count.

## Files & schedule
- **Weekly & Spanish:** Available/Valid Wednesday → Wednesday, 1-week run. **Set preview date Friday** (this flyer often fails auto-tagging — the Friday preview unblocks boxing before the weekend). Staggered dates (Wednesday vs Thursday versions).
- **Extra Savings:** bi-weekly; Available/Valid Saturday → Friday, 2-week run; **hidden on Hosted**; no preview.

## Upload & setup — Weekly & Spanish (DOC), codesheet
- Files arrive in FTP; reply to the email confirmation once files sync. *(Note: some contacts on the email chain are Fusion92 — no need to respond to them.)* Distribution list arrives separately; confirm and request any missing store info.
- Download the .xlsx codesheet. Email notes any store openings/closures and flex pages: set closing dates / add new stores in Fadmin (confirm if new stores also belong to the Publix Liquors merchant/store set).
- **Codesheet manipulations (staggered dates)** — mark whether stores get a Wednesday or Thursday version, per tab:
  - **Atlanta (Wed) & Charlotte (Wed):** insert a column B, formula `=A3&"W"`, copy down so each store # has a **W**; paste column B over A as **values only**; delete column B. Delete the black legend table. *(Charlotte also: add Version "V" in the legend and copy "Base - English - XXpages" from another version.)*
  - **Jacksonville (mixed Wed/Thurs):** delete the Liquor row/column; delete the GreenWise Market row **first**; use the Jacksonville Stores spreadsheet — copy row B and paste as values over the stores in column A; delete the black legend area. ⚠️ If a new store is added to Jacksonville, update the spreadsheet (add "W" if it starts Wednesday).
  - **Lakeland (Thurs) & Miami (Thurs):** delete Liquor row/column; delete GreenWise Market rows; align the legend table to match other tabs; delete the black area. *(Miami: MA = English, MB = Bilingual.)*
  - **Wrap/flex pages** (if present): reverse the letters (ZK → **KZ**, K = base); naming e.g. "GO WRAP 1633 - English - 20 pg."
- Save as **.xls** with **"MAIN"** in the name. **Delete the Charlotte tab**, save again with **"SPANISH"** in the name.
- **Upload to FADMIN:**
  - **Weekly:** codesheet name `main`, MAIN file, config **`publix`**, PDF base directory (e.g. `/070821`), **select all toggles except combine zones**.
  - **Spanish:** name `spanish`, SPANISH file, config **`publix_spanish`**, same PDF base directory, **all toggles except combine zones**.
- When running sessions, make sure the **first 4 page-level-task sessions fully complete**.
- **Loyalty insert:** add the Club Publix loyalty insert PDF to the back (Pages → Upload from local → Save & Complete → Layout → Put In → position **99** → **ALL pricing zones**).
- **Flex/Wrap pages:** if not auto-added, manually add to the beginning of the pricing zone. Wrap pages are labeled with the PZ name or noted in the distribution email; insert into positions 1–4 of the matching PZ (usually 4 pages). **Wine pages** (uncommon) insert into the **middle** of the flyer.

## Upload & setup — Extra Savings (Flex), manual
- Manual upload: Pages → Edit → open the week folder → choose the **lowercase** Extra Savings files → Auto Group → Save & Complete. Flyer Creation → 1 Pricing Zone (**Base**), add all stores.

### Setup QC
- **Weekly/Spanish dates:** Available/Valid Wednesday → Wednesday, 1-week run, available everywhere, **preview Friday**, internal run name `Weekly_[Start Date]`, no external name, no theme. **Staggered check:** PZs with "Wednesday" in the name = Wed→Tue; otherwise Thu→Wed. Thumbnails Standard 4.
- **Recipe links (vendor tasks):** from the Publix Aprons Recipes SharePoint list, filter by flyer date (may be off 1–2 days), copy recipe links, add a note to the Tag/Tag QC vendor tasks (>2 links → attach a spreadsheet). Add ready runs to VAST.
- **Extra Savings:** Available/Valid Saturday → Friday, 2-week run, hidden on Hosted, no preview, internal name `ExtraSavings_[Start Date]`.

## ⚠️ Common errors / risk items
- **Coupons** require Display Type **Coupon** and the **"LU# 12345"** (bottom-right corner) in the Description field.
- **BOGO tagging** (see below) — brand + "BOGO*" must be in the **Name** field, and the Save Up To sale story needs a **"$"** added manually (not printed on the page).

## QC specifics (all flyer types)
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **OFF**): **include coupons**, retailer logo, sign-up page, social media, special weblinks; exclude packaged deals. Box secondary items (smaller print, own price) separately. Don't let boxes cut off sale stories. Two side-by-side products → box/tag individually. Multiple products with text → main box (image) + text box (corresponding text).
- **Tag / Tag QC** (Low; Auto-tag **ON**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **No item URLs** (page callouts only) + specific recipe links.
  - **Spanish:** Spanish name from the text extraction in the Name field; include the **English name** in the description.
  - Description = non-bold text (sizing/variations); do NOT include items in brackets or with different price points (box/tag separately). Item category usually Grocery; coupons also get "Coupon" in the category.
  - **URLs:** no item URLs. Social media (Facebook/Twitter/Instagram/Pinterest/YouTube publix links); any URL → Display "Link" as written; recipe URLs per task notes.
- **Image QC / Spotchecks:** N/A (owned by Vendor, marked N/A).

### BOGO item tagging
- BOGO shown as bold "BOGO" or a green circle. **Name field must include the Brand name AND "BOGO*"** (all caps + asterisk, at the end). Prefix text = "Buy 1 Get ### FREE*", prefix amount 1.0. **Sale story: add "$"** to the Save Up To amount. Items in brackets don't need special BOGO tagging.

### Coupon tagging
- Display Type **Coupon**; Description includes **"LU# ____"** (bottom-right of coupon); include the full disclaimer/fine print; enter valid dates if different from flyer; add "Coupon" to the category.

## FQC
- **BOGO tagging review** (Vendor, right after Tag QC): Item Search → Prefix Text contains "Buy 1" (~300–600 results); confirm every BOGO item has brand + BOGO* in the name and a "$" in the sale story.
- Ops spotchecks (pricing discrepancy + valid dates). Mark Auto-Stack complete. Re-run the staggered-dates check. Thumbnails Standard 4; Item Image QC N/A; Tag/Tag QC both green; vertical preview; sessions run + re-verify URLs; geography (look for DOC store notes). **OK to ignore "Other Warnings"/unassigned stores.**
- **Flyer Review type: Lite** (Flex). Weekly EN: spot-check ~10 zones that PDF dates match PZ-level valid dates; Spanish: ~3 zones; **Extra Savings should NOT have staggered dates**; confirm vertical preview; confirm BOGO offers have BOGO at the start of the name for NativeX promotions; confirm geography/codesheet ran green.

## Out-of-processing
- **Remove FSAs** custom action is **no longer required as of 08/08/2024** (kept for historical context). Page swaps handled by DOC.

---
*Source: Publix OneGuide (Google Doc `1qsSR01gkX7XTaK_zf-ivCXAggW77lJjk5-kMKRSIOJs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
