# Nebraska Furniture Mart — Processing Guide

> **Source:** Nebraska Furniture Mart OneGuide (Google Doc `1EcO1fTUSazQS82hr6DzGft-GyV1k56Nq0HMGzCoPowE`). OneGuide last updated Oct 22, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | Most: all platforms. **Flooring: hosted only** when it doesn't meet content policy |
| Slack channel(s) | `#nebraskafurnituremart` |
| Hosted URL | http://www.flyertown.ca/flyers/nebraskafurnituremart |
| Flyer type(s) & cadence | 2939: Weekly, Bi-weekly & Ad-hoc (4–6 flyers go live most weeks) |
| Processing | Auto-stack |
| Involvement | Flex (Flyer Review); OS — Setup; no coupons; **Strategic Ops — yes (Feedel/retailer data services)** |

## Files & schedule (Flyer Type #1)

- **When files arrive:** Tuesday
- **Publication cadence:** Available From Wednesday, Valid From Thursday; Available To Wednesday, Valid To Thursday. **Varies publication to publication — always check what the flyer says and the shared client link document.**
- **Processing type:** Auto-stack
- **Linking document (Flipp Direction Document):** *sometimes* in the FTP; mass-attach to vendor tasks if present.
- **Workflow:** Upload & Setup (Flex) → FQC (Vendor)

## Upload & setup

### Full-time processor pre-upload step — building flyer shells
- A [Shared deep link doc] tracker is used to build shells in advance. If columns A–D are filled but column E is blank, you need to build shells.
- To build new runs: open the Flyer Schedule Creator → copy flyer names from column A into the creator's Name column → adjust available/valid dates to match the tracker → download as CSV → in Fadmin, go to Merchant Schedules, search "Nebraska Furniture Mart", upload the CSV and click **Upload Schedule**.
- Confirm the number of shells built matches what the merchant requested. File a Project Management Queue (PMQ) ticket for each run. Populate the deep links back into the tracker (Concat tab → paste flyer id into column B → link auto-populates in column C → paste as value into column G of the Current Ad tab).

### Setup instructions (Weekly flyers)
- Usually 4–6 flyers go live weekly (mostly Wed–Thurs runs). Repeating versions: Online, DM Online, Flooring, Bedding, Mrs B's ROP, etc.
- **Manual upload:** select files from the **lowercase** folder for each run based on its Internal Name. NOTE: Mrs B's ROP is usually only 1 page → appears under the **uppercase** folder (also Lift and Lighting sometimes). Best practice: after uploading all flyers, check the SFTP (Merchant Page > Details > View Files) with "Hide Uploaded" to catch any missed pages.
- Auto-group, then Save and Complete.
- **Flyer Creation task — pricing zones by store:** they have **4 stores: OM, KC, DM, TX**. Store codes are part of the file names. Name each PZ after the store(s) (e.g. a file set for OM/KC/TX → one PZ named `OMKCTX`; region-specific pages → separate OM, KC, TX zones). Files with **"NFM.com ONLY"** in the name display on hosted only — hide on Flipp and distribution (Overview > Edit Details). Flag to DOC if a flyer has no stores referenced in its file names. Save and Done.
- Add the correct store(s) per version based on the PZ name.

### Setup QC (owned by Flex)
- Overview > Edit Details: check valid dates against flyer page assets (usually page 1, occasionally last page); no preview (available and valid dates are the same); give an external name based on the titular messaging on page 1 (e.g. "Memorial Day Sale").
- Generally **No Theme** unless around a holiday.
- Standard 4 thumbnails (thumbnail_1065_x_600, stock_premium, storefront_carousel_premium, storefront_carousel_organic).
- Mass-attach the linking document if present. Complete Setup QC checklist.

### ⚠️ Common errors / risk items
- **Content policy:** Flooring ads generally don't meet content policy (fewer than 6 items total, or under ~3 items/page average). Hide such ads on Flipp and distribution and leave a comment ("Hidden on Flipp/Distribution because this does not meet content policy"). 1-page ads must have at least 6 items.
- **Store assignment source of truth is the page file names** (e.g. "1115 Online Omkc P0001" = OM and KC only; DM and TX correctly left out). Geography is not always the same as another run — verify per run.
- **Inverted/upside-down images:** if an image is inverted, select "Do Not Use PDF Images."
- Cadence dates vary each publication — always confirm against the flyer and shared link document.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot ON; linking doc rarely needed for catalogues)**
- **Include:** packaged deals (e.g. washers/dryers).
- **Exclude:** coupons, retailer logo, sign-up page, social media, special weblinks, financing options.
- Single item: box the entire image even if it includes different SKUs of the same item type. Use **text boxes** only when you can't avoid including another product. Multi-item/bundles displayed together can be boxed together. **Bundled items with different original/suggested retail prices → box and tag separately.**

**Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Selection ON) — Tag Lite retailer**
- **Do NOT tag:** Brand, Description, SKU, Sale Story.
- **Include:** name, pre/postfix, valid dates, price, categories, original price.
- **Exclude:** brand, description, SKU, sale story, disclaimer, URLs (unless a URL doc is provided).
- **Valid dates:** zoom out of flyers to check for valid dates — must be entered for every item where the availability differs from the run dates (e.g. Doorcrashers, New Releases). "Good Tomorrow"/"Good Through" → valid for that one day only. "Available Tuesday" → put the date in Item Valid From, leave Item Valid To blank.
- **Categories:** every item needs one; most common are Furniture, Beds & Mattresses, Appliances, Electronics.

**Image QC**
- Use clean PDF whenever possible; select cutouts when clean PDFs aren't available. Watch for inverted/upside-down images → "Do Not Use PDF Images."

## Post-processing (owned by DOC/Flex/Vendor)
- **Item Category QC (DOC):** one category per item; most common are Furniture, Beds & Mattresses, Appliances, Electronics.
- **Item Image QC (DOC):** clean PDF where possible; watch for inverted images.

## Pre-/Final QC (owned by Vendor)
- Mark Autostack Spotcheck complete.
- Overview → Edit Details: check external run names set (if not, use page 1 callouts, e.g. "Veterans Day Sale"); avoid duplicate external names (use "More Ways To Shop" or the flyer name); check thumbnails (Standard 4 — for 1-page ads the NFM logo should show in the thumbnail even if at the bottom of the page); under Ad Hoc Processing, open Manage Tracking Codes → Apply All Tracking Codes, and **Mark items in store only**.
- Pages tab: check run dates (usually bottom-right of page 1); apply one category per page (except page 1s).
- Pricing Zone tab: Item View — everything boxed; full-screen/vertical previews scroll and items are functional; stores assigned to all regions; hide ads failing content policy with a comment.
- Geography: source of truth is page file names; geography may differ from other runs.
- Complete FQC checklist.

## Flyer review
- **Flyer Review Type: Lite** (owned by Flex).

## Out-of-processing
- Page swaps happen occasionally. The retailer emails item-update requests and sends new files through the SFTP. Flex team can action with a FAB ticket.

---
*Source: Nebraska Furniture Mart OneGuide (Google Doc `1EcO1fTUSazQS82hr6DzGft-GyV1k56Nq0HMGzCoPowE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
