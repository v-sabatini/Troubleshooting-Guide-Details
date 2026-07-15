# Home Depot USA — Processing Guide

> **Source:** Home Depot USA OneGuide (Google Doc `1JzFdQSmwhWkaBJmaYF-lsC2bG9eJkgFxnIaFzijgHLA`), updated Apr 10, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 — S1C2 Premium |
| Availability | All platforms (Catalog & Standalone: **Hosted only**) |
| Slack channel(s) | `#homedepotus`, `#flex-processingsupport` |
| Hosted URL | homedepot.com/c/localad |
| Flyer types | Local Ad (248), Puerto Rico (293), Guam (299), Catalog (6868), Standalone 1 (9976) |
| Processing | Auto-stack; Flex (Processing Support / Flyer Review); DOC-owned setup & QC; Feedel/data services on Local Ads; no coupons |

## Files & schedule

- **Local / PR / Guam:** files received Monday or Friday. Available From Wednesday, Valid From Thursday; Available/Valid To Wednesday. Preview 1 week before go-live. Setup + Image QC + FQC owned by DOC.
- **Catalog:** files Monday. Available From Monday, Valid From Sunday. Preview 1 week ahead. Hosted only. Linking document (Smartsheet) required.
- **Standalone 1:** ad-hoc, hosted only.
- **Publication timing rule:** Available date = 1 business day prior to Valid date, launch at **3:00 AM**. Set a trigger to flip the Valid date from the preview date to the true Valid date ~24 h before launch.

## Upload & setup (owned by DOC)

- A 3rd-party team (Quad) emails when PDF pages + codesheet are on the SFTP.
- **Codesheet indicators:** National/Print Ad = **ST**; PR/USVI = **SCG** or **TCG** (Market 133 PR, 337 USVI St Thomas, 559 USVI Kingshill); Guam = **SG** (Guam can be a manual upload — only 1 store / 1 PZ).
- Download the `.xls` with the correct indicator → save as `.csv` (no manipulation **unless** there are subpages, e.g. page `02_03` — then delete the "page 3" column). Upload to FAdmin. **Config name: `home_depot_usa`.** Codesheet uploads all pages and pricing zones.
- **Catalog upload:** manually upload all pages & auto-group; 1 PZ = "base"; add all stores then remove PR/USVI and Guam store sets; attach the Smartsheet + LoRes file to all vendor tasks.
- **Setup QC:** preview date = 1 week before Available; change Valid to match preview date; trigger to fix Valid ≥24 h before launch; External Run Name = callout on first page.

## ⚠️ Common errors / risk items (retailer-specific)

- **URLs (all items must have a URL except Live Goods/plants).** Search the SKU on homedepot.com, select the **SINGLE item result — never a bundle item option**, visually confirm the Store SKU # matches, then paste the URL. **Do NOT use Fetch URL, "search" page URLs, or bundle URLs.**
- **OMSID field (critical):** any item with a SKU + URL must also have an **OMSID** = the 9-digit "Internet Number" (last 9 digits of the product URL, or the Internet # on the PDP). **Do NOT use the SKU# or Model# as the OMSID.** Ensure OMSID goes in the OMSID field, **not the Badge field**.
- **Badge field:** items with a **SPECIAL BUY** icon → Badge = `SPECIAL BUYS`; **NEW LOWER PRICE** → `NEW LOWER PRICES`. All caps, tagged exactly.
- **Description:** only add a description if there is **no** URL.
- **Washer/dryer pairs and appliances: always boxed and tagged separately.**
- **Multiple SKUs in one ad block with multiple images → box separately;** multiple SKUs that are just different **colours** of the same item → box together.
- **Box/tag ALL direct links, banners, and "green box" areas:** Home Depot logo, front-page publication name, Free/Fast Delivery, Select Appliances, financing offers, "Behr COLOR OF THE YEAR", "Low Prices. Guaranteed.", and every URL CTA (homedepot.com/lawncare, /ryobi, /milwaukee, /paint, /appliances, etc.). CTAs appear all over the flyer — do not miss any.
- **For PR/USVI/Guam URLs:** change store location by zip — Puerto Rico `00961`, USVI `00961`, Guam `96913`.
- **Catalog-specific:** draw one neat box over the item and its black dot — **no overlapping boxes, no text boxes**; box QR codes with adjacent text; keep Brand in the Brand field (never "Unbranded", never put brand in the Name field); use the **SKU as the OMSID** for Catalog only; Description is data-piped so leave blank; landing-page URLs → set Display Type: Link.

## QC specifics

- **Box Draw — Low complexity. Auto-Box OFF, PDF Image Auto-Selection ON, Box QC bot ON.** (Catalog: linking document required.) **Include** retailer logo, sign-up page, social media, special weblinks. **Exclude** coupons and packaged deals.
- **Tag / Tag QC — Low complexity. Auto-tag ON.** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, **OMSID**. Enter brand as shown in flyer, all caps; enter valid dates only if different from the flyer run date (e.g. only the "get 1 free" select tool gets the special valid date).
- **Image QC:** **images are data-piped — select cutouts.** Custom Action → Set Cutout Images (add Flyer Run ID) to force data-piped images; use the clean PDF where no data-piped image exists.
- **Direct-link URL reference:** Delivery, Pick Up, Credit Center, Appliances, Military, "Nobody Beats Our Prices" (price-match), Return Policy, Store Locator (see the OneGuide for the exact URLs).

### Final QC highlights

- Data piping >95% (double-check missing/errored images); thumbnails Standard 4.
- Item Search sweeps: OMSID blank + URL not blank → add OMSID; SKU not blank + OMSID blank → add URL + OMSID; SKU blank → OK only for Live Goods.
- Geography: no change week over week; make URL corrections per the direct-link list.
- **Catalog FQC:** fix boxes/QR codes; export items to confirm brand not in Name field (a `=IFERROR(TRIM(REPLACE(...)))` formula strips brand from name); confirm SKU in OMSID field; CTL+F each Smartsheet URL in Item Search to verify tagging; data-pipe near 100%.
- Send preview ~1 week ahead.

## Flyer review (owned by FLEX)

- **Flyer Review type: Lite** (all flyer types).

---
*Source: Home Depot USA OneGuide (Google Doc `1JzFdQSmwhWkaBJmaYF-lsC2bG9eJkgFxnIaFzijgHLA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
