# Cub — Processing Guide

> **Source:** Cub OneGuide (Google Doc `1IGQXiDsT5h_9Ru8PIY1-9OYi5Tr-OjA0i1xDB0icJgw`), updated May 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#supervalu` |
| Hosted URL | cub.com/savings/view-ads.html |
| Flyer types | **Weekly Savings** (pub 2416) · **Special Savings / LTD** (pub 10563) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons |
| Strategic Ops | Yes — retailer data services (Feedel processing) |

## Files & schedule

- **When files arrive:** Monday (upload Wed/Thurs after the codesheet + PDF emails are received).
- **Publication cadence:** Available From Monday, Valid From Tuesday; Available To Monday, Valid To Tuesday. **Staggered dates — always confirm against the PDFs.**
- **Linking document:** Yes — URLs on the insert page (only required for the insert page; proceed without it if not attached, as inserts/links often arrive late).
- **Owners:** Upload & Setup = DOC; Image QC = Flex; FQC = Flex.

## Upload & setup (owned by DOC)

- Download files from the emailed codesheet/PDFs and upload to SFTP with the manipulated **.txt** file.
- Save the codesheet(s) as **.csv**. Usually no manipulation needed, **but** check for pages named **GATE** or **INSERT** — rename so all pages are labelled **PAGE 1, PAGE 2, PAGE 3**, etc.
- **Codesheet upload:** config name **`farm_fresh_supermarkets`**; PDF base directory = entire base path; **uncheck region assignment and combine zones.**
- **Setup QC — staggered dates (always check against the PDFs):**
  - **Available from:** earliest date in the email, **1:00 AM**
  - **Available to:** one day **after** the last date in the email, **12:59 AM**
  - **Valid from:** one day **after** the earliest date in the email, **3:00 AM**
  - **Valid to:** final date in the email, **11:59 PM**
  - Available everywhere; no theme; four standard thumbnails.

## ⚠️ Common errors / risk items

- **Staggered dates** — always confirm against the PDFs (see the AM/PM times above).
- Rename **GATE**/**INSERT** pages to PAGE 1, 2, 3… before codesheet upload.
- **Banners / Cub rewards callouts are excluded during Box Draw** — Cub tells the Ops team when they need to be boxed/tagged, done during FQC with retailer-provided URLs (not every week).
- Linking spreadsheet is only for the insert page — process without it if not attached (inserts/links often late).

## QC specifics

- **Box Draw — Low complexity; Auto-Box ON, Box QC bot OFF.** No linking document. Box all items; **draw sub-items separately** when small items with different prices are embedded in a larger box. **Include** coupons and packaged deals. **Exclude** retailer logo, sign-up page, social media, special weblinks — and **exclude** the Cub / My Cub Rewards logo, brand logos, banners, and Cub reward callouts (handled at FQC when needed).
- **Tag / Tag QC — Low; Auto-tag ON; PDF image auto-selection ON.** Linking document required (insert page only). Include brand, name, pre/postfix, valid dates, description, price, sale story, categories, original price. **Exclude SKU (no longer required), disclaimer, URLs.**
  - Tag the **BOLDED** name. Postfixes include "lb with myCUB rewards", "with my Cub rewards", "when you buy any ### or participating item" (all in the dropdown). Every item requires a category. If multiple items sit under a header, ensure they **all** have Valid From/To dates. Insert page items → tag as **Links** (name + URL only).
- **Image QC:** **PDF image preferred over cutout** (e.g. California Jumbo Cherries, 80% Lean Ground Beef).

## FQC (owned by Flex)

- **Staggered dates** (recheck against PDFs, times as above).
- Thumbnails correct and include retailer logo.
- Standard checks: all items boxed and tagged; spotchecks complete (20% of pricing zones); previews published and clickable; sessions completed; geography correct.
- **Doable Dinners banners:** tag as items with URL `cub.com/sm/pickup/rsid/1612/meals` (if a QR code with no products, tag as a link). **Digital coupons:** tag as items with URL `cub.com/coupon-gallery`.
- **Flyer Review type: Lite.**

## Out-of-processing — Digital Inserts

- Refer to the "digital inserts" email and add inserts into each pricing zone.
- Manually upload the insert pages (split first if multiple pages). Mark Flyer Creation complete — **do not create new PZs.**
- Box and tag the insert page(s) with the URLs from the email — all items tagged as **Links** (name + URL; URLs from the email, names at processor discretion).
- Confirm whether inserts are version-specific (noted in the email); add inserts to all pricing zones **always after** the main flyer pages.
- After sessions re-run: verify URLs and re-run page tile generation.
- Page swaps: follow the baseline page-swap procedure (video in the OneGuide).

---
*Source: Cub OneGuide (Google Doc `1IGQXiDsT5h_9Ru8PIY1-9OYi5Tr-OjA0i1xDB0icJgw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
