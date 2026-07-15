# Ambrosia Natural Foods — Processing Guide

> **Source:** Ambrosia Natural Foods OneGuide (Google Doc `1vYLvssbWXcw6mgIv9HQ_iJ8tf-0I34vRlIbaO0nh_z4`), updated Mar 13, 2026.
> Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 2 Premium |
| Availability | **Flipp only** |
| Slack channels | `#ambrosianaturalfoods` |
| Hosted URL | None |
| Flyer types | **Monthly (9701)** · **Bi-Weekly (10165)** — both Ad-Hoc |
| Processing | Auto-stack; **Flex owns processing & comms**; OS completes upload; no coupons, no Feedel/data services |

## Files & schedule

- **Monthly (9701):** Ad-hoc files. Available/Valid From = 1st of the month; Available/Valid To = last day of the month (1-month run). No preview date.
- **Bi-Weekly (10165):** Ad-hoc; dates based on the retailer email (confirmed by DOC). No preview date. Retailer sends files directly to SFTP and emails to confirm; Flex confirms receipt (flag to `#flex-processingsupport` if no email reply; flag to DOC if files not uploaded to FTP), then adds run details to VAST and marks ready for Setup.
- **Linking document:** No.

## Upload & setup (owned by Vendor)

- **Manual upload:** Pages → Edit → Upload from FTP → select pages from the corresponding Month folder → Auto-group → Save & Complete.
- **Pricing zone:** Flyer Creation → one zone **"Base"** → add all stores.

### Setup QC / dates

- **Monthly:** Available/Valid From = 1st, To = last day; **hidden on hosted**; no preview date; Internal Run Name = "Month"; External Run Name = "Month Specials" (e.g. May Specials); No Theme.
- **Bi-Weekly:** dates confirmed by DOC; **available on Flipp & Distribution, hide on hosted**; Internal Run Name = e.g. "July Bi-Weekly"; no external run name; No Theme.
- Thumbnails Standard 4 (1065×600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, storefront carousel organic – 1pg). Confirm sessions run; Geography = no stores added/removed.

### ⚠️ Common errors / risk items (retailer-specific)

- **Flipp-only account** — check the availability toggles carefully (monthly: available everywhere; bi-weekly: Flipp & Distribution only, hide on hosted).
- **Watch multi-buy prefixes** (e.g. `##/$$` = 2/$5).
- **"Save Up To"** goes in the **Sale Story** field only — do NOT enter it in the Dollars Off field.
- Page categories: **none** — remove any that were added.
- Do NOT box/tag product ads that have **no sale price**.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** no linking doc. Exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. Box any item with a price; exclude items without prices.
- **Tag / Tag QC (Low; Auto-tag ON):** no linking doc. Include brand (if easily identifiable), name, pre/postfix, valid dates, description (small/unbolded print), SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs.** Postfix examples: LB., EA., BAG. Item category usually **Grocery** or **Health & Pharmacy**.
- **Image QC: none — cutouts only** (no image extraction). No URL/Link QC (no links).

## FQC / out-of-processing (Vendor-owned FQC)

- Ops spotchecks; mark Auto Stack Spot Check complete; confirm vendor tasks done. Verify dates/run name/theme per above; thumbnails; Tag QC items green; page categories none; vertical preview items clickable; sessions run & FSAs generated; geography unchanged.
- **Flyer Review type: Lite** (owned by Flex).
- **Out of processing:** page swaps are standard (baseline page-swap video).

---
*Source: Ambrosia Natural Foods OneGuide (Google Doc `1vYLvssbWXcw6mgIv9HQ_iJ8tf-0I34vRlIbaO0nh_z4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
