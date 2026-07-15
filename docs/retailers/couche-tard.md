# Couche-Tard — Processing Guide

> **Source:** Couche-Tard OneGuide (Google Doc `1cGPKJI87lLNpZ6OF20V7ph4f6Dc0XZ9c9HFS2amGC18`). Contacts/credentials omitted.
> Note: the source doc is labelled a mock-up; real account facts are captured below.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Flipp only |
| Slack channels | `#circlek` |
| Flyer type(s) | Flyer (pub 7958) — ad-hoc, good lead time (~2 weeks in advance) |
| Processing | Auto-stack; **Flex not involved**; OS completes flyer processing only; no coupons; no Feedel |
| Language | **French only** |

## Files & schedule

- **When files arrive:** ad-hoc, ~2 weeks lead time.
- **Publication cadence:** varies; available 1 day before Live date; sometimes short run (e.g. Friday–Sunday).
- **Preview date:** set for **5 processing/business days after files are received** (files come with lots of lead time but the retailer requests the preview well in advance).
- **Owners:** Upload & Setup = Vendor; Image QC = Flex; FQC = DOC (plus send retailer preview).

## Upload & setup (owned by Flex)

- Retailer is not currently set up on the FTP — will need to be added. If the client sends files over email, pages may need to be added to the SFTP (flag to processor).
- Download pages from email (typically 3 pages).
- **Manual Upload:** Pages → Edit → select the PDFs → Upload → **toggle language to FRENCH** → Save → Auto-Group → Save & Complete.
- **Flyer Creation:** Start Task → 1 pricing zone (**Base**) → **language FRENCH** → Save & Done → Pricing Zones → add all stores.
- **⚠️ RISK: pages must be uploaded in French.**
- **Setup QC:** Available From = 1-day preview; Valid From / Available To / Valid To confirmed by retailer email (ad-hoc times). **Hidden on hosted, available on Flipp & Distribution.** Preview date = 5 days after files received. Internal Run Name = month; no external run name; no theme. Thumbnails Standard 4 (1065×600 ×2pg, Stock Premium ×1, Storefront Carousel Premium ×2, Storefront Carousel Organic ×1). Confirm sessions ran; no geography changes.

## ⚠️ Common errors / risk items

- **Pages must be uploaded in French** and the pricing zone language set to French.
- Retailer not on FTP — needs to be added.
- **Preview URL is in English but the flyer is French** — before sending, copy the URL, change `=en` to `=fr`, use a Montreal/Quebec postal code, review, then send the full URL to the retailer for review.

## QC specifics

- **Box Draw — Low complexity; Auto-Box OFF, Box QC bot OFF.** No linking document. Use text boxes when appropriate. **Milk page: box the entire page** (Sale Story = "Au prix minimum permis par la loi."). **Include** coupons and packaged deals. **Exclude** retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
  - Tag brand from extracted text / PDF / product images; **most items are Multi-Item** — select this and enter all brands. Name as on PDF; put quantity/amount in Description. Prefix = Multi-Buy; **watch for asterisks (\*) tied to disclaimers** (include as a postfix). Categories = Groceries — Food, Beverages (most appropriate sub-category). Choose a clean PDF image if available.
- **Image QC:** avoid PDFs with black shadows; select clear PDFs if available.

## FQC (owned by DOC)

- Edit Details: available/valid dates per retailer email; preview 5 days after setup; **hidden on Flipp**; no external run name; no theme.
- Thumbnails Standard 4; **legibility heights = 40/30.**
- Item Image QC: select clear PDFs, de-select images with black shadows.
- Pages tab: confirm tag & tag QC match; no page categories. Pricing Zone → Item View: all items boxed & tagged; full-screen preview. Geo tab: no changes.
- **Send preview link:** Overview → Ad-Hoc Processing → Preview URL — change `=en` to `=fr`, use a Montreal/Quebec postal code, send the full URL, wait for retailer approval, fix any corrections.
- **Flyer Review type: Lite (owned by DOL).**

## Out-of-processing

- Post-live page swaps, post-live checks, late links as needed.

---
*Source: Couche-Tard OneGuide (Google Doc `1cGPKJI87lLNpZ6OF20V7ph4f6Dc0XZ9c9HFS2amGC18`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
