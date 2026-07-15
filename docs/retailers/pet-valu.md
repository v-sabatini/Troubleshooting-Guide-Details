# Pet Valu — Processing Guide

> **Source:** Pet Valu OneGuide (Google Doc `1cnCzKzcNPsvax7nX-nrzxz6WMC3RHflPuPHYiYn6oq4`). Contacts/credentials omitted.
> Covers banners: **Pet Valu, Bosley's, Paulmac's Pets, Total Pet, Tisol.**

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#petvalu` |
| Hosted URL | petvalu.ca/flyer |
| Flyer types | Flyer (types 63, 2459, 6118, 4223, 4635) |
| Processing | Auto-stack; Flex (FAB tickets); no coupons; Strategic Ops (Feedel/retailer data services) |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available From Wed, Valid From Thu; Available To Mon, Valid To Tue.
- **Preview:** 1-day consumer preview, 2-day merchant preview (set preview start 2 days before available date). Preview not required if files arrive at 5-business-day lead time.
- **Linking document:** Evergreen linking doc, attached to all vendor tasks (Setup QC task → toggle Mass attachment → attach). Box Draw/Box QC-specific and Tag/QC-specific linking docs also required.
- **Workflow owners:** Upload/Setup = Vendor; FQC = DOC.

## Upload & setup (owned by Flex)

**READ ME:** After confirming with the retailer/processor that all banners are the same, only send the **Pet Valu** banner to OS for processing. You must still upload the other banners but delete their boxes in the Box QC interface — boxes get copied from Pet Valu to the other banners after FQC/corrections.

- On the run's Pages tab → Edit → select the FTP folder → upload all pages. Page naming by banner:
  - Pet Valu: `pvon`, `pvbc`, `pvabmbsk` (sometimes just one PV version)
  - Tisol: `ti` · Total Pet: `tp` · Bosley's: `bos` · Paulmac's Pets: `pm`
- **Check the shared insert tracker** for additional inserts to upload; missing pages → confirm with their team.
- **Pricing zones:** Pet Valu zones match page names (PVON, PVBC, PVABMBSK); if only one PV version, zone = BASE. Tisol/Total Pet/Bosley's/Paulmac's each get one BASE zone.
- **Store sets:** PVBC zone → PVBC set; PVON zone → PVON set; PVABMBSK zone → PVABMBSK set. If only one PV version → assign all three sets. If no PVABMBSK version → PVON flyer gets both PVON and PVABMBSK sets. Tisol/Total Pet/Bosley's/Paulmac's each get all stores.
- Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)

- **TOTM (Treat of the Month) page** refreshes on the **1st of every month.** If a flyer spans two months you must upload the next month's TOTM page and **set a trigger** (Pages → Layout → swap page → "Run as Trigger", date = 1st of month, time = 12 AM). Create a ticket if needed.
- **Custom tiles** must be added, along with triggers for any replacements.
- **Flyer sorting** (check at FQC): monthly flyers ALWAYS first, followed by any catalogs.
- **Social media / URLs** must be boxed; in tagging set item display type = "Link" and insert links.
- **Page 1 links** must be complete and present on **all banners** (display type "Page Link"; destinations in the linking doc, same across banners).
- Linking doc attached to all vendor tasks; pages added to the appropriate banner.
- If all banners are the same, **hold off** on copying boxes from Pet Valu to the other banners until after previews are sent and corrections made.

## QC specifics

### Box Draw (HIGH complexity — Auto-Box ON, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box the product image and use a **text box** to reference item info when needed.
- Box any **call to action** (Explore More, See More, Learn More, Shop All, Shop Now).
- Box "Shop your locally owned & operated store, part of Canada's leading pet retailer."
- Box the logo; box call-outs (usually pages 1–2).
- Box each **"Get the Xth bag free with Your Rewards"** separately from the product it refers to.
- If an offer has different pricing, box separately and use text boxes to tie price to the correct image.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates (valid dates included only if stated).
- **Brand:** enter into brand field even if it repeats in the name field.
- **Price/Original Price fields are ONLY for regular pricing.** Any red text (dollar/percentage discount or sale price) goes in **Sale Story** — add the sale-story call-out first, then the sale pricing.
- **Price Text:** if a price range, put the second half of the range here.
- **Multiple items:** box ~10 products + supporting info together; box related products with a common description together; include all items in the description. Include all text under the product name except disclaimers.
- **Every item gets a URL.** Easiest method: copy the item name, search on petvalu.ca, use the search-results URL. Brand direct links used where there's a CTA (Shop All/Shop Now).
- **Lookbooks:** if SKUs appear in brackets on the PDF, search the SKU on the website to get the correct product link.
- **Standing direct links** (per banner logo and recurring banners): Pet Valu petvalu.ca, Tisol tisol.ca, Total Pet totalpet.ca, Bosley's bosleys.ca, Paulmac's paulmacs.com; Your Rewards, AutoShip, TOTM titles, Dog Wash, Raw Food, Grooming, Adoption, Find Your Store, and "Lower Price. Locked In." all have fixed collection links (in the OneGuide).
- **Categories:** Dog/Cat/Small Pet × feed/treat/train/protect/play, plus Events/Ads.
- **Disclaimer:** include per the linking doc (e.g. "Must be of equal size and value").

### Image QC
- Prefer PDF image (PDF Image Auto-Selection enabled).

## Post-processing / FQC (owned by DOC)
- Page categories (Pages tab), Page 1 links present/boxed/tagged for **all banners** — verify in hosted preview.
- **Items without URLs:** Overview → Information/Reports → "items without a URL"; fill in from the banner's linking doc.
- **Disclaimers:** item search compared against the linking doc.
- **RISK ITEM:** do a thorough spot-check — incorrect links are likely.
- Flyer Review type: **Lite.**

## Out-of-processing
- TOTM page swap + trigger (see Common errors above); repeat for any inserts needing swap (use the shared insert tracker).
- **Merchant preview:** if all banners are the same, only send Pet Valu's. Send 2 days before available date (only when assets arrive >5 business days from go-live). Preview links: Overview → Ad Hoc Processing → Preview URL → Hosted 2 Preview Link (EN); a preview start date on/before today is required.
- After corrections, copy boxes from Pet Valu to other banners; update logos to each banner's hosted name; confirm item counts match across banners.

---
*Source: Pet Valu OneGuide (Google Doc `1cnCzKzcNPsvax7nX-nrzxz6WMC3RHflPuPHYiYn6oq4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
