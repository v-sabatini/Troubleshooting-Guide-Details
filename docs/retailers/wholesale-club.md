# Wholesale Club (RCWC C&C) — Processing Guide

> **Source:** Wholesale Club (RCWC C&C) OneGuide (Google Doc `1xBi5CeEDQgmzNNbiXOYdH-R85t5j8vgg8BxFKmrJM4g`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Hosted URL | nofrills.ca |
| Flyer type(s) | Weekly (5994) + Vendor Book/Club Saving (VBT/CSF), Wine Day, Customer Day |
| Processing | Auto-stack; Flex = Flyer Review + Weekly upload; OS = Setup; **Strategic Ops: yes** (Feedel); no coupons |
| Cadence | Files Monday; Available Wed→Wed (1-day preview); Valid Thu→Wed; Sunday preview start |

## Upload & setup

**⚠️ NEW 2026 — set Pixel Height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → Show/hide rarely-used fields → Height dropdown → **4096.0 pixels** → OK. If pages were already added, flag to the full-time Ops stakeholder and continue.

- **There is NO codesheet** for Vendor Book / Wine Day / Extra / Customer Day publications — **the processor completes those uploads, not Flex.** Manual upload: Pages → Edit → find the vendor-book folder (may be CSF / VENDOR BOOK etc.); upload ATL, ONT, WEST, QUE folders (**QUE files = FRENCH**); create pricing zones **ATL, ONT, WEST, QUE, QUE ENG**; add the store set; thumbnail; no theme unless applicable.
- **Weekly Flyer — Flex completes the upload**, but the processor must add the codesheet to the shared Google Drive by **EOD Thursday** before the Friday shift. If Flex doesn't: ensure Pixel 4096, open the codesheet, manual-upload pages, create a pricing zone per codesheet tab, assign stores per the codesheet.
- Setup QC: Available Wed→Wed (1-day preview), Valid Thu→Wed; **Sunday preview start** (Edit Details → Preview start date = Sunday before available); external run name "Weekly Flyer Valid Thursday, Month date - Wednesday, Month date"; no theme; mark off Auto Spotcheck.

## QC specifics

- **Box Draw — Low; Auto-Box ON, Box QC bot ON.** Include coupons, packaged deals, special weblinks; exclude retailer logo, sign-up page, social media. Box around the full item + price.
- **Tag / Tag QC — Low; Auto-tag OFF.** Linking doc required (Tag/QC specific). Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs, **Coupon, Article Number**. No spreadsheet required.
  - **Name in ALL CAPS** (appears bold); product size after name using a comma.
  - **SKU:** enter the flyer SKU in SKU **and Article Number**; only use a SKU that **starts with "2"**; include the unit of measure (`_EA`, `_KG`, `_CS12`); one SKU only if multiple.
  - **Article Number** field (bottom of tagging interface): copy the SKU in with UoM; multiple SKUs → Article Number 1/2/3/4 in order.
  - **URLs:** after SKU entered, click **Fetch**. If the link goes to a different item/size → remove and search wholesaleclub.ca by product name; if it goes to a different flavour (same item) → leave; if it goes to the WSC home page → leave. Items with no SKU → find URL on wholesaleclub.ca.
  - **Sale Story:** "Optimum" offers tagged as **PC Optimum**; all $/%-off tagged in sale story (and in dollars-off/percent-off). Disclaimer: "limit"/"price after limit" callouts.
  - **Coupons:** Display Type = COUPON; draw all three barcodes.
- **Image QC:** clearest PDF; avoid black around the product; cutout only if no clean PDF.
- **Page categories:** every page except page 1s — min 1, max 3.

## FQC / pre-FQC tasks

- **CSF/Vendor Book:** mark off auto-stack + ops spot check; upload revised pages; build **Burnaby (store 6725)** and **Quebec City (store 8243)** into their own pricing zones (Burnaby, Quebec City Fr, Quebec City CL) — these two stores get unique **7-day FLASH OFFER flaps** to be posted only while valid and swapped weekly; set page removal/insert triggers by flap valid date; merge flaps (storefront spot check). Thumbnails Standard 4, start at logo, do NOT include flap pages.
- URL check: item search SKU IS NOT blank + URL IS blank → open + Fetch. Article Number check: Article Number 1 blank + URL not blank → add article number (also in SKU + part of URL).
- **Weekly:** pagination + store QC against the (revised) codesheet; URL/SKU/Article Number QC; check vertical + horizontal scroll; link QC from codesheet; swap in any revised SFTP pages before go-live.
- **Live-date risk items:** URL leading to a different item → **FLAG**; item quantities in the description → **FLAG**; Article Number field usage (see above).
- **Flyer Review type: Lite.**

---
*Source: Wholesale Club (RCWC C&C) OneGuide (Google Doc `1xBi5CeEDQgmzNNbiXOYdH-R85t5j8vgg8BxFKmrJM4g`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
