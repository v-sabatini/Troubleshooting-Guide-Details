# Sports Excellence (Canada & USA) — Processing Guide

> **Source:** Sports Excellence Canada & USA OneGuide (Google Doc `1zo7pdJwhcKFnLRaWur26WYUxLMXwXlj-nXyjH5h5hC4`), updated May 25, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#sports-excellence` |
| Flyer type(s) & cadence | **Canada** (merchant 2665 / type 2614) and **USA** (merchant 3409 / type 3445). Files Monday; publication dates ad-hoc, heavily dependent on file delivery. Available From Monday, Valid From Tuesday |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; Strategic Ops = yes (Feedel/retailer data services) |
| Linking document | Yes (used for both Box and Tag) |

## Files & schedule

- **When files arrive:** Monday, but see the lead-time risk below.

### ⚠️ Common errors / risk items (retailer-specific)

- **Lead time:** the client ALWAYS sends files late (often the day before they want it live) and is hard to reach. Push back — they know 5 business days' lead time is required. Their flyers have no dates and they rarely push back after we set dates.
- **Linking document:** usually messy / supplied incompletely (rows meant to be hidden or deleted). Before uploading, confirm it has links and no crossed-out rows. If broken, fix if possible, otherwise request a new document — processing cannot begin without it and the live date may slip.
- **Items with multiple sizes** (Junior/Intermediate/Senior, each with its own link): there's no room to box each cleanly. **For Senior items, box the image and use a text box for the price; for all other sizes in that space, box only the price.**

## Upload & setup (owned by Flex)

### Canada (merchant 2665, type 2614) — manual upload
- **First confirm whether French pages were received** (Merchant → Details).
  - **Bilingual files:** upload the bilingual folder, select all, mark language **French**, click SAVE (not Save & Complete); confirm it stays French; then re-select the bilingual folder AND the English Canada folder and select the files (a re-upload warning is expected). Manually group pages by PDF name.
  - **French only:** Pages → Edit → upload from the corresponding FTP folder; ensure French pages have the language set to French.
  - **No French:** upload as standard (Pages → Edit → upload from FTP folder; Autogroup; do not process internally).
- **Pricing Zones (Canada = 3 PZs):** English (all stores except QC); Bilingual: English (QC only); Bilingual: French (QC only). Varies with files received — English-only files → no QC stores; French pages not bilingual → only 2 zones (EN for rest of Canada, FR for QC only).
- **Linking document:** confirm supplied correctly, then upload to all tasks with a note telling vendors to refer to the columns labelled for the language needed.

### USA (merchant 3409, type 3445) — manual upload
- Pages → Edit → upload from FTP folder; Autogroup; do not process internally.
- **Pricing Zone: Base; Store Selection: Add All Stores.** Same linking-document confirmation and upload steps as Canada.

### Setup QC (owned by Flex)
- Toggles: Hidden in Hosted. Available/Valid dates per client (only if 5 business days' lead time; otherwise push back — confirm via client email/Slack/BD and notify BD of finalized dates). External Run Name = N/A; no theme (unless Black Friday/Holiday, etc.). Legibility Heights 50/30; Standard 4 thumbnails.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box all items with prices (text boxes when needed); box social icons and website callouts on each page; box store locators next to items.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Brand/Name as stated in the linking document or at the top of the page.
  - **Price colours:** Current Price = green, Postfix = red, Original Price = pink.
  - **Price range:** put the **highest** price in Current Price, add the designation (JR/INT/SR) in the Prefix, and the other range prices in the Description. If more than one price per item, the lower goes in the Description.
  - URLs as stated in the linking document; every item requires a category; disclaimer only if within the drawn box (not if at bottom of page).
- **Image QC:** usually cutouts only.

## Pre-Final QC / Final QC (owned by DOC)

- **Spot checks:** verify no postfixes (prefixes only); use the linking doc to confirm banners/links are actually boxed; check language.
- **Leg Heights:** scan 50 / read 30. **Thumbnails:** Standard 4 applied to all zones; custom tiles (from merchant FTP) applied via QC thumbnails to storefront premium + storefront carousel premium, one by one, per pricing zone (both EN and FR; for French update both BIL FR and BIL ENG). If a "thumbnail too big" error occurs, resize in Paint (uncheck maintain aspect ratio; match FAdmin's size, e.g. 1065x600) and save with "updated" in the filename.
- **Image QC:** click data-pipe images so images appear; PDF over cutout; cutout if PDF not clean.
- **Mark items In-Store Only** (Ad Hoc Processing → confirm the completed count matches page count).
- **Categories:** all pages except page 1; tag French in English (auto-translates on front end); last page (usually links) gets "Sports" category.
- **Tagging check:** prefixes correct with no postfixes; descriptions correct; **page 1 — box only the website (do not tag the whole logo; English site should have `en_ca`); only the URL to the website is tagged on page 1 across all zones**; last page prefix correct (JR/SR); URLs correct and tagged as links (not items); use the correct link for English Canada / French / USA English per zone; Instagram and Facebook tagged.
- **Previews:** check horizontal and vertical.
- **Final QC:** check dates; geography unchanged; the "pages uploaded twice" warning can be ignored.

## Flyer review

- **Flyer Review Type: Lite.**

---
*Source: Sports Excellence (Canada & USA) OneGuide (Google Doc `1zo7pdJwhcKFnLRaWur26WYUxLMXwXlj-nXyjH5h5hC4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
