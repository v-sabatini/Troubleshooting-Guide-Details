# C Town — Processing Guide

> **Source:** C Town OneGuide (Google Doc `1P5MMd4MANKEAsToKNU5k9_vZPkZAN_UrHlxmAVRwKto`), updated Aug 15, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#alpha1` |
| Hosted URL | ctownsupermarkets.com |
| Flyer type(s) | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons |
| Strategic Ops | Yes — retailer data services (Feedel processing) |

## Files & schedule

- **When files arrive:** Monday. **Upload Friday** (afternoon recommended — see risk items).
- **Publication cadence:** Available From Thursday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **No linking document.**
- **Owners:** Upload & Setup = Vendor; Image QC = Flex; FQC = DOC.

## Upload & setup (owned by Vendor) — same as Bravo Supermarket NE upload

- C Town is a **manual upload** account. Files are in the FTP — upload **ALL U41 and PU41 pages** (except any containing "AKO"). Double-check the FTP to confirm all files uploaded.
- **Create pricing zones (Flyer Creation):**
  - Create **Base u41** zone; add pages labelled **U41 B.** Save & Next.
  - Next zone **003** — change page one to **U41 003**, keep the rest the same. Save & Next.
  - Next zone **022** — change page one to **U41 022**, keep the rest the same… and so on through **ALL** remaining pages. Do the same for **ALL Base pu41** zones.
- Add individual stores to their new zones; add all remaining stores to the Base zones. **If a zone has 5 pages, remove the base page 4 to account for the store-specific page 4.**
- Proceed with Setup QC. Once the processor runs, check the FTP for skipped pages — the processor knows to skip stores **"062" and "032"**, and .ako files are excluded. Upload any missed revised pages manually and assign to the correct pricing zone.

## ⚠️ Common errors / risk items

- **New stores:** the processor may flag a file with no matching store. If clearly a new store (e.g. "Grand Opening" on the page), add it to fadmin.
- **Updated stores:** if a store code exists in fadmin but the U43/PU43 prefix doesn't match the FTP file, it likely switched from U↔PU. On the Merchant page → stores, search the numeric code (e.g. 315) and update the store to the opposite prefix.
- **Late-syncing pages:** not all pages sync at once — some arrive later, requiring manual pricing zones. **This is why upload is recommended for Friday afternoon.**
- **JPGs uploaded with PDF pages:** the pre-processor can't distinguish PDF from JPG and errors that no store is associated. Create a new store (merchant store code from the error, name DELETE, city New York, state NY, address 1, zip 10153), retry on the codesheet, force processing on the "already uploaded" error, generate sessions, then delete the PZ, the store, and the JPG from the page assortment.
- **COVID "Open for Business" PZ** process documented in the OneGuide (manual PDF upload, do not check Process Internally, copy stores from the prior live week).

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. Box all items separately (anything with a price gets a box); use text boxes when needed. **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons, packaged deals.
  - For **multiple related items** (e.g. cuts of turkey) box only the main picture (one box; no text box). Draw ONE box per different item. Only one box per item even if the price gets cut off. **Box QC: no duplicated boxes on an item.**
- **Tag / Tag QC — Low; Auto-tag OFF; PDF image auto-selection ON.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU. Always include category.**
  - **Name:** as in flyer, ALWAYS CAPITALIZED; no measurements (those go in Description); never non-bolded words.
  - **Description:** as in flyer; include all non-bolded words and measurements; do **not** include "With Card"/"Without Card" (that goes in Postfix).
  - **Postfix:** "With Card. Without Card $xx.xx" if applicable.
  - **Prices not inside the drawn box (e.g. 2.99 lb / LB.) must still be tagged.**
  - **Valid date overrides:** use the dates on page 1 of the publication. A theme banner (e.g. "4th of July") does **not** set valid dates — always use the front-page valid dates.

## FQC (owned by DOC)

- Mark autostack spotcheck complete; **legibility heights 60/40**; dates correct per page 1.
- Thumbnails — Standard 4 + `first_page_thumbnail_400w` (write complete in comments).
- Page categories.
- **Flyer Review type: Lite.**

---
*Source: C Town OneGuide (Google Doc `1P5MMd4MANKEAsToKNU5k9_vZPkZAN_UrHlxmAVRwKto`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
