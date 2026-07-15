# Brookshires — Processing Guide

> **Source:** Brookshires OneGuide (Google Doc `1GsYFxaSBPn_wNvfhGfnfkDzxW51eUBFUGSifxe00C2Y`), updated May 29, 2026. Contacts/credentials omitted.

Covers the Brookshires family of banners: **Super 1 Foods & Discount Pharmacy**, **FRESH by Brookshire's**, **FRESH by Reasor's**, **Brookshires**, **Spring Market**, **Reasor's**.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#brookshires` |
| Hosted URLs | super1foods.com, brookshires.com, spring-market.com, reasors.com |
| Flyer types | Super 1 (#7855 Weekly, #7857 Monthly/Liquor); FRESH by Brookshire's #8005; Brookshires #7940 Weekly, #7941 Websaver, #7942 Liquor Beer Wine (monthly), #8030 Celebrate Cooking (monthly, **hosted only**); Spring Market #7939 Weekly, #10561 Monthly; Reasor's #2357 Weekly, #9642 Monthly |
| Processing | Auto-stack; Flex (3FL / FAB tickets, owns Setup & FQC); no coupons; **Strategic Ops — yes (Feedel processing)** |

## Files & schedule

- **Files received:** Wednesday (Super 1); Monday (FRESH banners).
- **Publication:** typically Available Tue, Valid Wed → Wed (Super 1); FRESH available Tue, valid Wed → Wed. One-day consumer preview for weekly and monthly pubs.
- **Time zone:** set **`Valid From` to 1 AM** — Fadmin runs EST, Brookshires is Texas/CST, so 1 AM ensures it goes live at the right time.

## Upload & setup (owned by Flex)

- **Manifest upload:** find the `.txt` manifest in the FTP matching the flyer's naming convention; upload it in the **Codesheet tab** — **Config `brookshires`**, **PDF Base Directory `/flyer_zone_pages_pdfs`** (always this path). Save → Process codesheet.
- **FRESH by Brookshire's & FRESH by Reasor's share one manifest** (code `31##`) but must be split before upload: Brookshire's = **Region 1 & 2 (stores 802, 803)** — delete Region 3/4; Reasor's = **Region 3 & 4 (stores 804, 805)** — delete Region 1/2.
- **New process (Jul 8, 2026): one vendor attachment — Deals & OfferID.** Download `deals.offerid.txt` from FTP, open with `|` as custom separator, keep only Title, Description, Main_UPC, flippPromotionCode; rename `flippPromotionCode`→`SKU`; remove duplicates; save under the original file name as XLSX.
- **Edit Details:** No theme; available everywhere; one-day consumer preview. **Fixed staggered dates:** running the manifest auto-creates staggered PZ dates — adjust all pricing zones to match the flyer run dates (edit the Available From date). Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- **One SKU per item (critical):** more than one SKU/promotion code per item **breaks the sub-item experience on the front end.** No commas or multiple SKUs in a single item's SKU field.
- **Beer / soft-drink promo codes:** verify all beer has the correct promo code — match the description (e.g. "24 pk/12 oz Cans") to the blowline file (Ctrl+F "beer" in Item Search). Repeat for Coca-Cola, Pepsi, 7UP.
- **Similar products, different SKUs:** e.g. Coca-Cola 6-pack (406576) vs 10-pack (406631) look alike — tag the correct SKU per version.
- **Alcohol page categories:** alcohol page 4 must include the category "alcohol" — but **one page 4 has no alcohol**, so remove the category there.
- **Manifest troubleshooting:** store missing → add in Fadmin (reach out to retailer contact); "missing page" → manifest naming must match FTP, correct and re-upload; flyer-run dates must be adjusted to match the manifest's date range.
- **Blowline / Mi9 errors:** "Illegal quoting in line X" → open the blowline file, remove unique characters (e.g. `"`), save; also remove the character from the item name (Item Search → Name contains, e.g. "Quiche"), re-run, then restore. If the Mi9 API product count is < 20, ensure all items have proper promotion codes and re-run.

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF. PDF auto-selection ON. Linking doc required (Box-specific).** Exclude coupons, packaged deals; include retailer logo, sign-up page, social media, special weblinks. Draw a box for each unique price.
- **Tag / Tag QC — Low. Auto-tag OFF. PDF auto-selection ON. Linking doc required. Pre/Postfix excluded; valid dates only if a promo sale story requires an override.** Include brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name/Brand:** brand as on flyer; name = "Brand Product Name" (larger bold text). **Description** = smaller non-bold text below name, first letter capitalized (100% natural, weight, selected varieties).
  - **SKU** from the `deals.offerid.xlsx` SKU column; **UPC** from the `Main_UPC` column.
  - **Postfix:** do NOT enter for "When you Buy ### In a Single Transaction" (that goes in the disclaimer); eCoupon offers → "FINAL PRICE WITH COUPON".
  - **Sale story:** "BUY ONE GET ONE FOR $0.01" goes in the sale story.
  - **URLs:** Brookshires banner links to the merchant landing page; social icons link to their platforms.
  - **Categories:** page-level; label categories with 3+ products on the same page; **no more than 4 categories per page**; page 1 → copy to same index.
- **Image QC:** clean PDF images preferred; **retailer dislikes ANY shadow (even natural)** → swap to cutout; use cutouts where clean PDFs aren't available.

## FQC / go-live (owned by Flex / DOC)

- Mark auto-stack complete.
- **UPC QC:** Item Search UPC IS blank → fill from linking doc (match name/price); note "UPC checked."
- **SKU QC:** Item Search SKU IS blank → fill promotion codes from the blowline file (try name variations); SKU IS NOT blank → run the 3 risk checks (one SKU per item; beer promo codes; Coca-Cola/Pepsi/7UP). A FLEX ticket on the OT board has OS re-check tagged SKUs (usually Friday, verified Monday before go-live; skipped on short weeks).
- Page categories (page 1 copy to same index; ≤4 per page; alcohol page 4 rule); pricing zones have similar items per region; geography; re-run outstanding sessions/vendor tasks.
- **Flyer sorting:** older flyer first, preview second, monthly last.
- **Blowline custom action not required as of March 2026** — just ensure SKUs/UPCs filled from the Blowline and Deals files.
- **FSA reassign troubleshooting** (PZ without FSA): use the FSA Swap Custom Action with Flyer Run ID, Pricing Zone ID FROM/TO, and the store's zip from the Fadmin store list.
- **Flyer Review:** owned by Vendor (Super 1 Foods review guide).

## Out-of-processing

- **Mi9 sub-items:** if a revised file is sent, press "generate data piping groups" on the data piping page, then "Data Pipe All." If a revised blowline file only has selected items, **merge the revised items into the original blowline file first** — running the revised file alone erases sub-items generated from the original run.

---
*Source: Brookshires OneGuide (Google Doc `1GsYFxaSBPn_wNvfhGfnfkDzxW51eUBFUGSifxe00C2Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
