# T&T Supermarket — Processing Guide

> **Source:** T&T Supermarkets OneGuide (Google Doc `1EUrSSpTCTBQ9B59qpQsiC36zpfzgL9MLd7eLFcXFJJg`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | (not specified) |
| Availability | All platforms |
| Slack channels | `#hosted-tnt` |
| Hosted URL | tntsupermarket.com |
| Flyer type(s) & cadence | Flyer Type 1 — Weekly |
| Processing | **Trim Stack** |
| Who's involved | Vendor upload/setup; DOC FQC; no Flex; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Wednesday, usually near EOD.
- **Publication cadence:** Available/Valid Friday → Thursday.
- **Preview date:** Friday.
- **Linking documents:** 3 uploaded to FTP — **AB, BC** and **ER**.

### ⚠️ Common errors / risk items
- **Rewards pages:** one box for the whole page, tagged with the correct link from the matching link sheet.
- **Flyer not ready by Friday:** set up a **FLYER COMING SOON** placeholder. Notify DOC & DOL. Reuse the coming-soon run (flyer run 979420); adjust its available/valid dates. Set its available/valid-to time to when the real run is expected live, and adjust the real run's dates/times too.

## Upload & setup (owned by Flex)

- **NEW 2026 — Set Pixel Height to 4096 BEFORE uploading any pages.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → 4096.0 pixels → OK. If pages were already added, flag the Full-Time Ops stakeholder and continue.
- **Manual upload:** pages are submitted Wed afternoon–EOD, referencing **WR** and **ER** pages (sometimes sent separately).
  - **WR** pages → Alberta (**AB**) and British Columbia (**BC**) zones.
  - **ER** pages → Saint Laurent/Quebec (**SL**), GTA, Promenade Mall (**PR**), Ottawa (**OW**), Waterloo (**WL**) zones.
  - Best to wait for all zones' pages before uploading.
- Pages → Edit → select all pages from the most recent folder (open each folder icon so FAdmin grabs all pages). Rename each page so its target Pricing Zone prefixes the name.
- Some **Poster**/**Reward** pages only say "ER"/"WR"/"GTA": you need one per WR region (AB, BC) and per ER region (GTA, OW, WL). SL is the only French region and always gets its own version. If only one ER/WR page is included, upload multiple copies and assign each to a region, renaming accordingly.
- **IMPORTANT:** toggle **all SL pages to French**, Save, then confirm toggles saved or you must reupload in a new track.
- Grouping optional (page 1s = 1, page 2s = 2, etc.; SEA pages = 4, Rewards = 5, PR = 6). Save and Complete.
- **Flyer creation — 6 pricing zones:** AB (Eng), BC (Eng), GTA (Eng), OW (Eng), WL (Eng), SL (French). Page order: positions 1/2/3 = pages 1/2/3; position 4 = SEA/FnV insert; position 5 = Rewards (position 6 for PR zone).
- **Assign stores** via generic codesheet upload (save the codesheet CSV from the previous run). After FSA Generation session, Geography tab should read **No Stores or FSAs/zips were added or removed!**

### Setup QC (owned by DOC)
- Edit Details: no consumer preview; Available/Valid Friday → Thursday; Hide on Distribution and Hosted; no theme.
- Thumbnails Standard 4 (1065 x 600, stock premium, storefront carousel, storefront organic).
- **Vendor tasks — IMPORTANT:** mass-attach ALL URL documents to EVERY vendor task (English and French). Add the note: all items get the same link; reward pages get one link per page; no SKUs; AB doc → AB pages, BC doc → BC pages; ER doc → WL tab for WL, GTA tab for GTA, OW tab for OW, SL tab for SL. Refresh to confirm the note saved to every task.
- File an Urgent Processing Ticket.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc Tag/QC-specific — continue if not attached)**
- Include: coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Draw a box where there's a unique price or a sale story (e.g. 10% OFF). **If an item has a "?" question mark as the image, do NOT box.**
- Posters (e.g. Rewards pages) embedded in the flyer must be tagged as a direct-link display type — URL from "Other Posters" in the item list.

**Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON)**
- Include: name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. No brand.
- **Name:** ALL CAPS, format "Brand Product Name, Quantity" (always a comma before quantity, e.g. 60g, 1lb, bunch, pkg of 24). Do NOT include "Product of…", "No 1 Grade", "Frozen", "Selected varieties" in the name — put those in the description.
- **Valid dates:** only apply date overrides when a related promo sale story is present on the item.
- **SKU:** use the "Item Number" column in the linking document.
- **Description:** first letter of first word capitalized; include "Product of…" here. **Categories:** every item needs Google + analytics categories. **Disclaimer:** noted under "remarks" in the link doc.

**Image QC:** select the cleanest PDF; if none, use the relevant cutout.

## Final QC / go-live notes (owned by DOC)

- **Upload category pages:** download the 2 category pages (ENG & FR) from the previous run or from the VTB Drive folder; upload to the current run (correct language each). After upload, delete the auto-boxed boxes (wait until Box QC is enabled to avoid a FAdmin pipeline error). Copy items from the previous run's category pages (Pages → Copy Items; match languages). Layout: add category page as last page (position 99) to all English and French zones.
- Mark Autostack Spotcheck complete. Edit Details: Available/Valid Friday → Thursday; hidden on Distribution and Hosted; no external run name; no theme.
- Complete Item Image QC (PDF where possible, cutouts otherwise). Leg heights 40/30; Standard 4 thumbnails.
- Pages: check outstanding QC; confirm Poster/Reward pages boxed & tagged (add missing links from URL docs if a page shows 0 items); no Page 1 has a category.
- Confirm stores assigned; sessions run correctly and links verified; Geography: **No Stores or FSAs/zips added or removed!**
- **Live-date risk items:** valid dates of Books/Movies/Music (available date often differs from flyer; dates at top of page); description must match page exactly.
- **Flyer Review type: Lite.**

---
*Source: T&T Supermarket OneGuide (Google Doc `1EUrSSpTCTBQ9B59qpQsiC36zpfzgL9MLd7eLFcXFJJg`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
