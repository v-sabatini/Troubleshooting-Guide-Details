# Dollar Tree — Processing Guide

> **Source:** Dollar Tree OneGuide (Google Doc `111JHQBHHcGOPXZhPlPL6_BHOxQbBCtv-Dl0C9DGU4Hw`), updated May 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Core+ · S2C1 (Tier 1) |
| Availability | All platforms |
| Slack channel(s) | `#dollartree` |
| Hosted URL | dollartree.com |
| Flyer type(s) & cadence | **Flyer** (weekly-style schedule) · **Lookbook** |
| Processing | Auto-stack; no Flex; no coupons; no Feedel/retailer data services |

## Files & schedule

- **When files arrive:** per schedule.
- **Preview date:** 2 weeks out — **preview links MUST be sent 2 weeks before go-live.** Set Preview Date to 2 weeks before live in Edit Details.
- **Linking document:** Ad Book Links (xlsx) provided in the SFTP — used for both links and descriptions.

## Upload & setup (owned by Vendor)

- **[Overview] → [Edit Details]:** Available everywhere; **no theme** (unless holidays); External Run Name = a callout from the first page or based on the flyer name; Preview Date = 2 weeks before live.
- **[Pages] → [Edit]:** manually upload the pages.
- Create pricing zone: **base**. Stores: **[Add All]**.
- **[Task Pipeline]:** attach Ad Book links — download from SFTP → open a Vendor Task → **Mass Attachment → (+)** → attach the xlsx.
- Thumbnails: **Standard 4**. Ledge height: **50/40**. Pipeline: **Setup QC**. Autostack Spotcheck → Complete.

### ⚠️ Common errors / risk items (retailer-specific)

- **FSA Generation warning:** go to the Dollar Tree merchant page → Stores/Sets → Stores → search store number 10055 → **[Edit]** → update the zip code to 75703 → **[Update Store]**.
- **Links QC:** ensure every item has the correct link tagged (use the Links doc from SFTP).
- **Description QC (NEW):** add the non-bolded text from the "Copy for Pop-Ups / Sidebar" column of the linking doc into the Description field. **Delete any quotation marks** — no surrounding `"` on the blurb, no double `""`, and remove the extra `"` on inch measurements (e.g. `18""` → `18"`). Search: Description contains `"`.
- **Tracking codes (NEW Jan 2025):** [Overview] → [Manage Tracking Codes] → under Flyer Run add two Dynamic Variable codes, source All: `utm_source = flipp` and `utm_medium = eflyer` → **[Apply All Tracking Codes]** → comment "tracking codes applied".
- **Ghostscript (NEW Apr 2025):** set all pages to **ghostscript** conversion library (fixes "funky" text/dark fonts), **[Save and Complete] → [Submit]**, then **re-run Page Tile Generation**.
- **Basket Offers:** special email callouts where each material is $1.25 **each**, not $1.25 total. Description = "Final Products Shown"; Prefix = "Individual Materials"; Disclaimer = "Final Products created with Multiple $1.25 Materials".

## QC specifics

- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF).** Linking doc required (shared Box/Tag). **Include:** sign-up page, special weblinks (e.g. email signup, store locator). **Exclude:** coupons, packaged deals, retailer logo, social media, and "Click to Shop!" buttons.
- **Tag / Tag QC (Low; Auto-tag OFF).** Include name, pre/postfix, valid dates, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Brand = No. Tag price as-is on the PDF; match names to the links doc using the PDF text; add URLs from the links doc.
  - **Description:** Flyer type = **Include** description; Lookbook type = **Exclude** description in the tag overview, but the July 2024 note still copies "Copy for Pop-Ups / Sidebar" (non-bolded only) into Description. In all cases, strip quotation marks.
- **Image QC:** clean images only — no black backgrounds; use a cutout if the PDF is a lifestyle image.

## Final QC / go-live

- Check for fonts/images darker than the source PDF → fix via ghostscript 9.06 gamma conversion.
- **[Overview] → [Items without URLs]:** confirm all items have URLs; look up missing ones in the URL file.
- Links QC and Description QC per above; Page Categories by best judgment (one per page guidance).
- Apply tracking codes, run ghostscript on all pages, re-run Page Tile Generation, then Pipeline → Final QC Checklist.
- **Flyer Review type: Simple.**
- **Send Preview URLs (owned by DOC):** build the sneak-peek link by inserting the preview code after `weeklyad?` on the dollartree.com URL; send 2 weeks before go-live.

---
*Source: Dollar Tree OneGuide (Google Doc `111JHQBHHcGOPXZhPlPL6_BHOxQbBCtv-Dl0C9DGU4Hw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
