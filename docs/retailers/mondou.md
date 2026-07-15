# Mondou — Processing Guide

> **Source:** Mondou OneGuide (Google Doc `1c1TXrCicnEd8FAJRkfanmcQdd_hwv8qSWxZMtheGBI4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | N/A |
| Availability | All platforms |
| Slack channels | `#mondou`, `#flex-processingsupport` |
| Hosted URL | mondou.com (we power their hosted) |
| Flyer types & cadence | Flyer Type 1 — **Ad-hoc** |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support); OS N/A; no coupons; no Strategic Ops (no Feedel) |
| Language | Bilingual — English & French |

## Files & schedule

- **Files: ad-hoc.** Usually sent **7 business days before live** and **5 business days before merchant preview.**
- **Preview:** URLs sent 2 days in advance of the live date.
- **Linking document:** Yes — dropped to FTP.

## Upload & setup (owned by Vendor)

- **Manual upload:** select pages → Edit → select files from FTP (named by live date; `AN` = English, `FR` = French). Group by page number in the file name. Assign English to `AN` files, French to `FR` files. Save and Complete.
- **Pricing zones:** two zones — EN and FR (descriptions "EN"/"FR"). Create EN (English pages, correct order), Save & Next; create FR (Language: French, French pages, correct order), Save & Done. **Add all stores to each PZ.**
- **Vendor attachments:**
  - The FTP has a **"Layout" PDF** telling Vendors how to box pages. Due to its size, **compress it** (pdfcompressor.com) before attaching. Vendors tab → Upload Mass Attachment → All Vendor Assignments → attach the compressed Layout PDF.
  - Attach the **tagging Excel** (e.g. "Flipp_Mondou_…") to Tag/QC — contains both EN + FR links, so upload once.
- **Custom Tiles — ONLY if the flyer is a masthead/promoted publication** (BD will tell you). If not, skip and do Standard 4 thumbnails. If yes, download both custom tiles (AN + FR) and override Storefront Premium + Storefront Carousel Premium on the EN PZ (AN tile) and FR PZ (FR tile).
- **Edit Details:** valid dates match PDF; available 1 day before valid; **preview date 3 business days before the available date**; available everywhere; no theme. Complete Setup QC.

## ⚠️ Common errors / risk items

- **EN vs FR tagging** — use the correct language from the tagging document for each item. **Pay special attention to URLs: EN URLs on the English version, FR URLs on the French version.** Do NOT translate — if only French text is present, tag in French even on an English page.
- **Free-item-with-purchase sale story** — e.g. Brand: OPEN FARM; Name: OPEN FARM Cat Food; Description: 1.81 kg; Sale Story: "FREE Open Farm Cat food pack 156g With the purchase of Open Farm Cat Food 1.81kg."

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** Linking document required (Box Draw/Box QC specific).
- **Include:** social media. **Exclude:** coupons, packaged deals, retailer logo, sign-up page, special weblinks.
- **Box EXACTLY as laid out in the Layout document** (boxes identified by circles/lines with a number each). **Follow the layout document above all other guidelines.** Box banners with overarching stories together.

### Tag / Tag QC — Low complexity
- **Auto-tag: OFF.** Linking document required (Tag/QC specific).
- **Include:** name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **URL tagging:** ALL items must have a URL. Use only the URL FR and URL EN columns of the spreadsheet; FR URLs → French pages, EN URLs → English pages. **Direct Link = YES** items: change Display Type to Link, then paste URL and save.

### Image QC
- Select clean PDFs whenever possible; otherwise the cutout image.

## Post-processing (owned by Flex)

**All post-processing must be completed two days before the live date so retailer previews can be sent.**

- **Category QC / Image QC:** standard.
- **URL/Links QC:** Overview → Items without a URL → assign missing URLs from the vendor-tasks doc; **0 items without a URL.**
  - **⚠️ RISK:** FR pages/items need FR URLs; EN pages/items need EN URLs. QC via Item Search: (URL contains `fr-CA`, PZ = EN) should return nothing — fix any that appear; then (URL contains `en-CA`, PZ = FR) should return nothing — fix any that appear.

## Final QC (owned by Vendor)

- 0 items without a URL; Standard 4 thumbnails.
- **Flyer Sorting:** lookbooks always second to primary content (Merchant Page → Flyer Sorting).
- Edit Details: available everywhere, no theme, no external run name, dates correct. Listed warnings may be ignored.

## Cloning — "Flipp App" + "Hosted" links for the same publication

When the retailer provides both link sets: ensure the original flyer has all "FINAL URL FLIPP APP" links applied. Clone to the same flyer type, name it "hosted - clone." On the clone, item export → in Sheets keep only `item_id, sku, url` → find/replace the Flipp utm parameters (e.g. `utm_source=flipp&utm_campaign=…`) with the hosted parameter `origin_page=flippflyerpage` → confirm links match the "FINAL URL HOSTED (ON MONDOU)" column → download CSV → import items to the cloned run → verify via last session results.

## Retailer previews (owned by DOC)

- 2 days before live, send EN + FR preview links (Overview → Ad Hoc Processing → Preview URLs → copy Hosted 2 Preview URLs). Send **only after FQC** with all items URL-tagged. The retailer reviews and returns corrections; update the items.

## Custom URLs / Deep Links (owned by DOC)

- "Deep Links" take a user directly to the live flyer on the hosted page (not preview access) — used in retailer email blasts. Available any time once the flyer shell is built (only the flyer ID is needed). If the flyer ID changes, resend updated deep links. Append the flyer ID to the base URLs:
  - **English:** `mondou.com/en-CA/flyer-c44.html?locale=en&flyer_run_id=<ID>`
  - **French:** `mondou.com/fr-CA/circulaire-c44.html?locale=fr&flyer_run_id=<ID>`

## Flyer review

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Mondou OneGuide (Google Doc `1c1TXrCicnEd8FAJRkfanmcQdd_hwv8qSWxZMtheGBI4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
