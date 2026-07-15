# PartSource — Processing Guide

> **Source:** PartSource OneGuide (Google Doc `1TI-N_pxk8qLc-Gm78UvQzNUtFpPoHJq6R7IRio4ja3c`), updated Mar 13, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#partsource` |
| Hosted URL | partsource.ca/pages/flyer |
| Flyer types & cadence | 3540: Weekly (Inserts / "Evergreen" and Deals flyers) |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Background / files & schedule

- **When files arrive:** Monday.
- **Cadence:** Available From Thursday, Valid From Friday; Available To Monday, Valid To Tuesday.
- **~90% of content comes from quarterly inserts** provided with a schedule, so many flyers can be uploaded in advance. The insert schedule marks with an "x" which insert belongs to each publication and its pagination.
- **Non-insert (Deals) flyers:** files sent via WeTransfer over email.
- **All insert flyers get a 1-day consumer preview** — send the item export 2 days before going live.
- **Watch content policy:** occasionally PartSource has fewer than 5 shoppable items — keep a lookout.

## Upload & setup

### Inserts / Evergreen (owned by Flex)
1. Check the flyer schedule to find which insert is needed for the week (marked "x").
2. Open the flyer run shell. Pages → Edit → upload files for that insert → Auto-group.
3. Pipeline → start **Flyer Creation**. Pricing Zone: **Base**, add all stores. Wait for sessions.
4. Edit Details: 1-day consumer preview; set preview date for the Monday before go-live; no theme; available everywhere.
5. **Standard 4 thumbnails** — if the PartSource logo sits in the bottom-right corner, shift the thumbnail to cover it. Complete Setup QC checklist.

### Deals flyers (owned by Flex)
- Same base steps (Pages → Edit → select all → Auto-group; Flyer Creation; Base PZ, all stores; sessions).
- Edit Details: 1-day consumer preview; preview date Monday before go-live; no theme; available everywhere.
- **Deals go live on hosted only first, then must go available everywhere on the valid date.** Create **2 triggers** (Overview → Triggers): one to display on Distribution, one to display on Flipp — both set to run on the valid date.
- Create an Optics ticket for a live check that it's available everywhere.
- Standard 4 thumbnails (cover the logo if needed). Complete Setup QC checklist.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc required):**
- **Include:** packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Draw a box whenever there is a unique price for an item. Box banners containing a `.com`/`.ca` address. Box social-media icons (Facebook, Twitter, Instagram).

**Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON; linking doc required):**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. Brand is Box-specific.
- Exclude: disclaimer, URLs.
- **Price range:** enter the first price in Current Price; enter the second by selecting `- $$$` from the postfix dropdown and putting the price in the postfix amount field.
- **Prefix/Postfix:** select from dropdown; if missing, flag to PC to update the list.
- **URLs:** do **not** enter URLs unless it's a social-media banner. Social icons = direct-link display type, named for the platform (e.g. "Facebook"); Email Sign Up links to the partsource.ca email signup page.

**Image QC:** select a PDF image for all items; prioritize clean white backgrounds. **If the PDF image has a black shadow, use the cutout image instead.**

## Post-processing (owned by DOC)

**Item Category QC** (category chart):

| Category | Example items |
|---|---|
| Car Care | Risers, ramps, jacks, inflators, polishing sets, cleaners, Armour All / Turtle Wax, WD-40 |
| Tools | Tire rack, assemblies, shocks/struts, compressors, drills |
| Accessories | Filters, cushions, wipers, gas cans, seat/wheel covers, trouble lights |
| Hard Parts | Chassis components, rotors, brake pads, spark plugs, calipers, headlights, alternators |
| Electronics | Batteries, code readers, chargers, GPS, phones, cameras |
| Fluids & Additives | Transmission fluid, lubricants, antifreeze, coolants, engine oils |

- **Page categories:** include categories on the first page too; coupon pages don't need categories.
- **SKU QC:** Item Search SKU → IS → blank; apply from the PDF all that are blank.
- **⚠️ RISK:** go through each item and confirm the product name and SKU as tagged match the flyer page.

**Item URL export process (DOC):**
- Overview → export items; keep only Item ID, Page, Name, SKU, URL (URLs blank for the retailer to fill). Sort by name, save `.xlsx`.
- Email/schedule the item export for 9 AM the day before the available date, including the preview URL (1st English URL under ad-hoc processing).
- When the retailer returns the URL spreadsheet: keep only `item_id, sku, url`, save `.csv`, Overview → Import Items. Verify via Item Search URL → IS → blank.
- Mark items in store. Generate the email-blast URL from the merchant Generate URLs page (Type: Full Screen; Locale: English; Generate HTML) and add it to the external schedule sheet ASAP.

## Flyer Review / out-of-processing

- **Flyer Review type: Lite** (owned by DOL).
- **Out-of-processing:** baseline page-swap process available (see OneGuide video).

---
*Source: PartSource OneGuide (Google Doc `1TI-N_pxk8qLc-Gm78UvQzNUtFpPoHJq6R7IRio4ja3c`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
