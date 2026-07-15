# Red Apple Store — Processing Guide

> **Source:** Red Apple Store OneGuide (Google Doc `1W4H7lIAUYjqT2qbtEJHxQF9bbr6j8LWpivWRv4-mDkc`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#redapplestores` |
| Hosted URL | redapplestores.com/products/everyday-savings-flyer.htm |
| Flyer types | Monthly / Bi-Weekly |
| Processing | Auto-stack; Flex (Processing Support); **Yes — Feedel/retailer data services**; no coupons |
| Notes | **Cloned into The Bargain Shop after FQC** (thebargainshop.com). |

## Files & schedule
- **Files received:** Tuesday. Available From Wed; Valid From Thu; Available/Valid To ad hoc — **must match the PDF**. Linking document: Yes (on FTP).

## Custom actions
- **Clone:** after FQC, clone Red Apple Store into The Bargain Shop.
- **Image import:** in the SFTP there are PNG files. Copy the path **up to `/flyer`** (e.g. from `/Red Apple Stores/091925_BBBS_Oct23-31_Flyer_Halloween/Page2`, copy `/Red Apple Stores/091925_BBBS_Oct23-31_Flyer_Halloween`). In the flyer run > Sessions > find **Image Import** > paste the path > toggle **without color profiles** and **from scratch** > submit. (Do this during upload/setup.)

## Upload & setup (owned by Vendor)
1. Manually upload all pages (file name should match the flyer run name) > auto group > Save > Save and complete.
2. Flyer creation: 1 pricing zone **BASE**; add all stores.
3. Check SFTP for un-uploaded pages (confirm with FT team if needed).
4. Attach the linking doc (search "link" in SFTP, download the PDF linking document) to all vendor tasks.
5. Run the **Image Import** custom action (see above).

### Setup QC
- Geography tab: ensure no stores added. Check PDF dates vs. flyer run dates (usually a 1-day preview, but not always — confirm with FT team when unsure). Complete thumbnails and setup QC checklist.

## QC specifics
- **Box Draw (Low; Auto-Box OFF, Box QC bot OFF):** **include retailer logo and special weblinks**; exclude coupons, packaged deals, sign-up, social. Box all items separately; box banners with CTA buttons / direct links; box the logo.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON; linking doc required for Box/Tag):** include Name, Pre/Postfix, Valid Dates, Description, Price, Sale Story, Categories, Disclaimer, Original Price; Brand is Box Draw/Box QC specific; exclude SKU, URLs.
  - **⚠️ Only the items on the ELAVOE page have links.** Elavoe items require links from the PDF linking document.
  - Example tags: percent-off items ("30% OFF", Percent Off 30, disclaimer); priced items (Name, Description, Price); link items (Item type Link, e.g. "Everyday Favourites at Low prices" → everyday-savings.htm; "ELAVOE SHOP NOW" → link from PDF).

## Post-processing
- **Item Image QC:** ensure the Image Import ran correctly. In the Image QC interface, untoggle "pdf image" and "data piped image" and confirm each remaining item has a **clean white PDF image**. **If image colours are inverted or tinted, flag to the processor.**
- **URL/Links QC (Flex):** box and tag the Red Apple logo (link redapplestores.com). Open linking doc and add all listed links. If there's an "everyday low saving, shop now" section, link it to everyday-savings.htm. Check the **Elavoe page** (usually the last) — every product has a link matching the linking doc; the linking-doc file name tells you which page (e.g. "Elavoe June12-15_PAGE7 Links.pdf" → page 7). Ensure Standard 4 thumbnails; confirm dates.

### FQC (owned by Flex) + clone
1. Complete post-processing steps + FADMIN FQC checklist.
2. **After FQC, clone into The Bargain Shop.** In The Bargain Shop: add all stores to the pricing zone; ensure Image QC complete; **move the boxes from the Red Apple logo onto the Bargain Shop logo** and change the tag link to thebargainshop.com; complete the FQC checklist.

## Flyer review
- **Type: Lite** (covers Red Apple Stores & The Bargain Shop).

---
*Source: Red Apple Store OneGuide (Google Doc `1W4H7lIAUYjqT2qbtEJHxQF9bbr6j8LWpivWRv4-mDkc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
