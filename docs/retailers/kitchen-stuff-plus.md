# Kitchen Stuff Plus — Processing Guide

> **Source:** Kitchen Stuff Plus OneGuide (Google Doc `1t-3B1OBO2UOtz-AP2RXHLxezdjH7WeXkfy0Da10RLyk`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport` (+ retailer channel) |
| Hosted URL | kitchenstuffplus.com |
| Flyer type(s) | Weekly Flyer |
| Processing | Auto-stack; no coupons; **Feedel / retailer data services: Yes** |
| Involvement | **DOC** owns setup & post-processing; **Flex** owns Flyer Review |

## Files & schedule

- **Files received:** Thursday (via FTP: publication files + a CSV tagging/linking document).
- **Publication cadence:** Available/Valid Monday–Sunday.
- **Linking document:** Yes (CSV attached to Tag & QC).

## Upload & setup (owned by DOC)

- Receive files via FTP (publication PDFs + CSV tagging doc).
- **Manual upload:** select the split pages, language English, auto-number pages.
- One pricing zone (**Base**) — add all stores.
- Attach the `.csv` to Tag & QC in the Vendors tab.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** **include** coupons, sign-up page, social media, special weblinks; exclude packaged deals and retailer logo. Box all items with price/sale story; text boxes where needed; box callouts.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** **include SKU, name, description, price, sale story, categories, disclaimer, original price, URLs.** Exclude pre/postfix and valid dates. PDF image auto-selection ON.
  - Original Price examples: "Reg. from $99.99 ea." → 99.99; "Compare at $70" → 70.
- **Image QC:** prioritize clean PDF images; for multi-items use a clean individual image if no group image. Avoid images with shadows/black backgrounds.

## ⚠️ Common errors / risk items

- **Missing URLs:** OS sometimes doesn't tag a URL (accident, or none on the CSV). Use Overview > "Items Without a URL" to catch these.
- **Last page** must be boxed and tagged (% off info).
- **[Item Types → Hosted Link clone]** After the "Flipp – Item Types" run completes, **clone it into a separate "Hosted – Link Items" flyer** because hosted properties require direct links only for this retailer — display type must be **Link** (not Item) for all ad cells:
  - Overview > Export Items → open the emailed export.
  - Delete the "Page Items" header row; delete the "Flyer Items" header row and all flyer-item rows below it; delete unnecessary columns; swap "ITEM" → "LINK" under Display Type; move the SKU column to column B; save as `.csv`.
  - Overview > Import → upload the file. Verify via Item Search: Display Type = ITEM should return **0 results**.
  - **RISK:** ensure the "Flipp – Items" run is **hidden in Hosted**, and the "Hosted – Links" run is **hidden in Flipp**.

## FQC / flyer review

- Final QC: spot check; thumbnails drawn; item preview (last page % off boxes); report items without URL (fix via spreadsheet/website); verify category thumbnail generation; check flyer sorting.
- **Flyer Review type: Lite.**

---
*Source: Kitchen Stuff Plus OneGuide (Google Doc `1t-3B1OBO2UOtz-AP2RXHLxezdjH7WeXkfy0Da10RLyk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
