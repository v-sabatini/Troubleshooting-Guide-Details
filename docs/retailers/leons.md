# Leon's — Processing Guide

> **Source:** Leon's OneGuide (Google Doc `1p07Jyq7s5fddo7Gg8ngMQWzmANCRL1QCc8bxTHnRCJw`). Contacts/credentials omitted.

> Multi-flyer-type furniture account, bilingual, zone-based. High box-draw complexity.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | All platforms (varies by flyer type) |
| Slack channel(s) | `#leons` |
| Hosted URL | leons.ca |
| Flyer types | **2571 Corporate Stores** (main), **9216 TV Flyer** (vanilla, hosted only), **2455 Non-Promoted** (OLD — appliance, now appended to Corporate), **12335 DVM Test** (BBFL Electronics only) |
| Processing | Auto-stack (Corporate); Trim Stick (TV/Non-Promoted); Normal Indexed (DVM Test) |
| Who's involved | Flex (FAB tickets + SKU/URL QC); **Feedel/Strategic Ops: yes**; no coupons |

Zones: EN = Z1, Z2, Z3, Z4, Z5, Z5-NB, ME; FR = FQ, FZ5 (etc.). Corporate vs Franchise store sets per zone.

## 2571 Corporate Stores (main flyer)

### Files & schedule
- **Files arrive:** ad-hoc. Available/Valid From Thursday → To Wednesday.
- **Preview date:** Thursday before go-live (so OS can complete it and an urgent ticket can be filed). FQC 2 days before go-live so export links can be sent to the Leon's team.
- **Workflow:** Upload & Setup (DOC) → SKU & URL QC (Flex, 3 days out) → FQC (DOC).

### Upload & setup (owned by Flex)
- Pages → Edit → select all files for the campaign + Email inserts (last position). EN zones: Z1–Z5, Z5-NB, ME. FR zones: FQ, FQ5-NB. Toggle French pages FR (refresh to confirm); rest stay EN.
- If pages have different dates, upload in groups and rename page files to include the date range in ALL CAPS (e.g. `MAY12-JUNE_hte_flyer..._Z4_p0001`). Auto-group; Save and Complete.
- **Assign stores (Flyer Creation):** Z1 = Z1 Corporate + Z1 Franchise; Z2 = Z2 Corp + Z2 Franchise; Z3 = Z3 Franchise only; Z4 = Corporate only; Z5 = Z5 Corp + Z5 Franchise; ME = ME Corp + ME Franchise; FZ5 = FZ5/Z5 Franchise store sets; FQ/FZ = ZF1 Corp + ZF1 Franchise. For province-specific zones (Z5-nb, Z2-ab, FZ5-NB) add only that province's stores and remove them from the main zone.
- Wait for sessions; hard-merge banners/products that stretch across pages. Add Email Insert pages last. **RISK: the Shop Online insert is discontinued until further notice.**
- Edit Details: usually no theme; External Run Name (EN and FR) = first page callout. **⚠️ RISK: if one PZ doesn't share the same EN/FR external name callout, it must be cloned into its own flyer shell after FQC.** Available everywhere.
- Thumbnails (5): Standard 4 + a "Thumbnail" spanning 2 pages for hosted. Attach the flyer product feeds (separate EN and FR docs) to Vendor Tasks.
- **Appliance/Vendor pages (NEW 2026):** the vendor team sometimes sends appliance pages that are appended to the end of the corresponding PZ (EN National = Z1–Z5/Z5NB; EN Quebec = ME; FR Quebec = FQ; disregard FR National). If they arrive late, process within 5 business days and insert into the PZs after processing.

### QC specifics
- **Box Draw (HIGH; Auto-Box OFF, Box QC bot OFF):** linking doc required (box-specific). **Include** packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons. Box every item listed (item box + text box; if not pictured, box the text). **Box each TV size and each mattress/bed size separately.** Box the email signup page and all social icons; tag French logos with French links. "Find Your Store" button boxed for EN and FR.
- **Tag / Tag QC (Medium; Auto-tag OFF, PDF image auto-selection ON):** **Include** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name/Brand:** copy the product name exactly from the Leon's product page URL; if no URL, use the flyer name. **No copyright/trademark symbols** (e.g. no ®).
  - **SKU:** enter as in flyer, in both SKU and description fields. Sub-items (loveseat, chair, ottoman) have different SKUs — search the linking doc by item name.
  - **URLs:** refer to `www.leons.ca` (search by SKU). **French pages use the `https://fr.leons.ca` subdomain.** Do NOT tag search links as product URLs.
  - **Valid dates:** TV valid dates apply to all TV sizes/dimensions of a model.
  - **Categories:** Living Room, Bedroom, Dining, Appliances, Beds & Mattresses, Electronics, Office, Patio & Outdoor.
  - **Sale Story:** item-specific only; don't tag general callouts; callouts like "SAVE $600, + SAVE THE TAX†" go exclusively in Sale Story (not prefix/disclaimer).
  - **Disclaimer:** include all item prices when purchased separately, plus the disclaimer for the entire set.
  - **Price:** leave blank for products without pricing on the page.
  - Banners/social/email-signup use the exact EN/FR links listed in the OneGuide.
- **Image QC:** use **data-piped images** where possible (target **95%+**). Don't use a PDF image if a product URL exists or if there's no clean/complete PDF image.

### ⚠️ Risk items
- **URLs** — every item must be correctly linked (URL drives name, image, details).
- **Box Drawing** — every item should have a box even if not pictured.
- **Item Valid Dates** — ensure valid dates are tagged for TVs and their models/sizes.

### Final QC / go-live (owned by DOC)
- Data-pipe images early (long-running; target ~90%+). Mark page categories/spotchecks.
- **Link QA (Item Search):** URL contains "fr." with language English → catches French links on English pages; URL contains "www." with language French → catches English links on French pages. Switch prefixes (fr. = French, www. = English). Check financing links (URL contains "finan") and set EN/FR financing-flexiti links.
- Image QC after data piping (clean PDFs if available, else cutouts; appliances split up are fine). Check pages/sessions/vendor/geography. Split any flyers with different first-page callouts into their own flyers. Flyer sorting: (1) Printed flyer, (2) Digital flyer.
- If "not all pages have slicing validated" error appears after checking slicing, write "done" in the error field.
- **Export + retailer preview:** export items (keep headers item_id, flyer_name, page, name, description, sku, raw_current_price, url), send preview + export links to the Leon's team. Import returned URLs, then mark items in-store. **Cloning:** after corrections, clone flyers per external run name — financing events (e.g. "Don't Pay A Cent") can't run in Quebec by law, so Quebec runs a different title.
- **Flyer Review type: Medium** (owned by Flex).

## 9216 TV Flyer (vanilla, hosted only)
- Trim Stick; **Hosted only**. Only applicable when Z4 has its own corporate flyer pages — a west-coast store that displays its flyer on TV via a special integration.
- New flyer run, same dates as corporate, **hidden in distribution and Flipp**. Manual upload Z4 files only; one PZ "Z4" with **store code CQ**. Make the flyer **vanilla**; mark all vendor tasks complete. Leg heights 40/30; one thumbnail (+ "thumbnail" 2-page). No inserts. Key Msg: Free Local Delivery (English only). No theme. On FQC, write "vanilla" in the "not all pages have at least one page item" error box.
- **No OS pipeline tasks** (vanilla). **Flyer Review: Lite.**
- **Live-dates note:** TV Flyer ads (named "TV Display-VANILLA") do NOT need to be flagged in live dates for being vanilla / not on hosted — this is a specialty link for the Leon's team, not public.

## 2455 Non-Promoted (OLD — appliance)
- DVM-processed flyers only; appliance pages are now appended to Corporate Store flyers. Trim Stick, hosted only. Vendor team drops EN + FR pages in FTP. Four PZs: EN & FR National (all stores minus ME/ZF1 store sets), EN QC (ME Corp+Franchise), FR QC (ZF1 Corp+Franchise). External Run name "Appliance Sale/Solde D'électroménagers"; check off secondary publication; available hosted only. Box/Tag same as Corporate (HIGH box complexity). **Flyer Review: Lite.**

## 12335 DVM Test (BBFL Electronics only)
- Normal Indexed; all platforms. Box Draw HIGH (Auto-Box ON, Box QC bot ON) — include packaged deals, sign-up page, social media, special weblinks; exclude coupons, retailer logo. Tag Medium: include brand, name, description, SKU, price, categories, URLs; exclude pre/postfix, valid dates, sale story, disclaimer, original price. Find name by searching the SKU on leons.ca; every item tagged with URLs from the attachment (EN/FR links). **Do NOT tag** "Best brands for less" or "30 Day Price Guarantee" CTAs.

---
*Source: Leon's OneGuide (Google Doc `1p07Jyq7s5fddo7Gg8ngMQWzmANCRL1QCc8bxTHnRCJw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
