# Princess Auto — Processing Guide

> **Source:** Princess Auto OneGuide (Google Doc `10tPU0PKvnQjJ-ZCgz_kSqmC4kjPQQpw_rq2VWV9cJiQ`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#princessauto` |
| Hosted URL | princessauto.com |
| Flyer types | **Biweekly** (11) · **Monthly / Price Wrecker** (10178) · **Yearly Catalogues** (65) |
| Processing | **Trim Stick**; Vendor setup, Flex + DOC QC, FAB tickets; Feedel (retailer data services) yes; no coupons |

Bilingual (EN + FR). Files received Monday. General cadence: Available Wed, Valid Sun.

## ⚠️ Common errors / risk items
- **Slicing:** after setup, check the pipeline throughout the week to confirm slicing kicks off — it sometimes reads "inactive," which **blocks OS.**
- **SKU boxing:** every item with a unique SKU must have its own box.
- **National Events:** additional links arrive by email and must be boxed/tagged **after go-live** — watch for full flyer revision pages.
- **Yearly catalogue slicing:** drag the slice box down to capture the page number at the bottom.

## Biweekly (11)
### Setup (Flex) — manual upload
- Pages → Edit → select files. Language: French pages have **FR** in the name, English have **EN**. Save only → Autogroup → Save & Continue.
- Pricing zones: **FR** (French) and **EN** (English). Additional PZs may exist (e.g. Saint-Hubert-FR is its own PZ with unique FR pages, pulled out of the FR zone).
- Overview → Edit details: no theme; Wednesday consumer preview (per the schedule); toggles **Hide in Distribution / Flipp / Hosted** (flyer goes live hosted-only first). Thumbnails Standard 4.
- **Create a trigger** to make the flyer available on all platforms one day before go-live, and create an Optics ticket for the live availability check.

### QC
- **Box Draw** (Low; Auto-Box ON, Box QC bot **OFF**): box each item individually with a price; multi-item blocks with different prices → box separately. Box the Email Sign Up and Order Online/Pickup In-Store inserts. **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons.
- **Tag / Tag QC** (Low; Auto-tag OFF; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - Brand in the brand field (not the Name); copy description exactly. Do **not** include original price when there is a range. SKUs only in the SKU field; only tag the **bold** SKU when multiple exist. Different date from the flyer → set per item.
  - **URLs:** if a SKU is provided → generate/fetch URL. No SKU / SKU doesn't resolve → search by name on princessauto.com and use the **product page** URL (not the search page). No broken URLs.
- **Item Image QC:** check Data Piping early — if data-piped image <90%, filter "Data Pipe Image" + "Supplemental Info" → Data Pipe All to re-run. Use PDF images where data-piped ones aren't available.

### FQC (DOC)
- Fetch URLs for items with SKUs (skip items with no SKU on the PDF). Re-run data piping if low. Mark items **In-Store Only**.
- **Box/tag the weekly inserts:**
  - Email Newsletter (page position 3) — EN `princessauto.com/en/sign-in-newsletter`, FR `.../fr_CA/sign-in-newsletter`.
  - Online Store Pickup (page position 4) — EN `.../en/store-pickup`, FR `.../fr_CA/store-pickup`.
  - Blue Truck BBQ — **Alberta only** (position 5) `bluetruckbarbecue.com/menu`.
- **Flyer sorting order:** Bi-Weekly Event → Monthly Price Wrecker → Special/Standalone → Catalogues. Check QR-code mini-sections have links. Complete the Optics ticket toggle check on the designated day.

## Monthly / Price Wrecker (10178)
- Setup: upload files twice — mark French, then re-upload and mark English. Autogroup. **2 pricing zones (EN, FR)**, all stores in both. No inserts (straight manual upload). No theme; 1-day preview; **available everywhere**. Leg heights **50/35**. Thumbnails Standard 4. Auto-Box ON, Box QC bot **ON**.
- FQC: rerun page stitching; page categories → all surplus; re-run data piping if low; mark In-Store Only; confirm all pages sliced; keep **Bi-Weekly Event as the top sort option**.

## Yearly Catalogues (65)
- EN and FR files split into separate shells; match file names to the correct-language shell. Pricing zones EN/FR, follow page #s (no inserts), all stores in both. External run name = Year + Catalogue Name (e.g. "2023 Air & Power"). Wednesday preview. Toggles: **hosted only for the full year** (Hide in Distribution/Flipp/Hosted). Leg heights **50/35**. Auto-Box ON, Box QC bot ON.
- **Flyer Review type: Simple.**
- **Deep-linking (FQC):** to link Flyer 1 to a specific item/page on Flyer 2, export Flyer 2 items, take the target item_id, and build:
  `https://www.princessauto.com/REF1/flyersView?locale=REF1&flyer_type_name=flyer&flyer_run_id=REF2&flyer_item_id=REF3`
  where REF1 = `en` or `fr_CA`, REF2 = target flyer run, REF3 = first item on the target page. Box & tag as Display Type **LINK**.

## Out-of-processing — video-link embeds
- From a provided link list (SKU, item name, EN/FR URLs): Item Search by SKU → open item → Box QC → resize the existing box to the text only and draw a new box around the image → Save & Complete. On the Tag view set Display Type **Video**, enter the item name exactly, paste the correct-language Video URL, Save.

*(Biweekly/Monthly Flyer Review type: Lite; Yearly: Simple.)*

---
*Source: Princess Auto OneGuide (Google Doc `10tPU0PKvnQjJ-ZCgz_kSqmC4kjPQQpw_rq2VWV9cJiQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
