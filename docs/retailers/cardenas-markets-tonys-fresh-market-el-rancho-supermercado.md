# Cardenas Markets, Tony's Fresh Market, El Rancho Supermercado — Processing Guide

> **Source:** Cardenas Market / El Rancho Supermercado / Tony's Fresh Market OneGuide (Google Doc `1S5VFYJ1dI7hckrHl1evB8ffNTXhJgxzMsPIhlo_d-Q4`), updated Jun 16, 2026. Contacts/credentials omitted.

> **Three banners under one parent (Heritage Grocers).** Spanish-language grocery. Weekly Ad + Monthly Savings Guide.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#cardenas`, `#flex-processingsupport`, `#flex-flyer-review` |
| Hosted URL | cardenasmarkets.com/shop/weekly-ad/ |
| Flyer types | Weekly (3563) · Monthly Savings Guide (same flyer type as weekly) |
| Processing | Auto-stack; Flex (Processing Support); OS (Setup); no coupons/Feedel |

## Files & schedule

- **Files received:** Tuesday. **Cadence:** Available From Tuesday · Valid From Tuesday · Available To Wednesday · Valid To Tuesday. Available From = 1 day before Valid From (1-day preview).
- **SFTP path prefixes** (files for all 3 banners land in each SFTP — upload to the correct banner, mark the others off): Cardenas `/CMKTS_`, El Rancho `/ers_` (lowercase, **not** `/ERS_`), Tony's `/TFM_`.

## Upload & setup — Weekly (owned by Vendor, codesheet generator)

- Use the correct **Codesheet Generator** per banner (Cardenas / El Rancho / Tony's).
- **Backend tab, cell A1 = flyer date (MMDD)** matching the FTP folder. If MMDD starts with 0, prefix an apostrophe (`'0629`). If they use YYYYMMDD (e.g. 20260627), use that.
- **NEW (Jun 16 2026):** use the retailer's Gemini gem — attach the image saved from the email (nothing else), send, and copy the plain-text table it outputs. Paste as plain text into cell A1 of the **EXPORT** tab to fill zone/store info. (If the gem doesn't return the table, ask it for "the table in a code block plaintext format".)
- Check the FTP for how many pages each version (V##) receives. Copy the EXPORT tab → paste **Values Only** into the CODESHEET tab. Adjust Page # columns to match the FTP: if all zones get 4 pages, keep columns C–F and delete G & H; if any zone gets 5–6 pages, keep the Page 5/6 data only for those zones.
- Download CODESHEET tab as CSV → flyer run > Code Sheets. **Name = `codesheet`; Config = `generic`; toggles = ALL except 2 and 7; PDF Base Directory** from the FTP (e.g. `/cmkts_062426` — grab only the first directory after "/" and before the second "/", no `/v34` etc). Save Code Sheet → Process Codesheet → mark Flyer Creation Done.
- Edit Details: valid dates match PDF; Available From = 1 day before Valid From; No theme; no external run name.

## Upload & setup — Monthly Savings Guide (owned by Flex)
- Manually upload the versions (e.g. Cardenas V1, V2, V5), paginating via the version code + page number in each file name; create pricing zones. Add stores via store sets (Tony's: add all stores for distribution). Edit Details: **External Run Name = "Monthly Savings Guide"; No theme.** Thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **Flyer sorting:** the **weekly ad must always appear before the sales guide** on the website. Correct order: Oldest Weekly, Newest Weekly, Monthly. (A flyer only appears on the sorting page after autostack spot check is marked complete.)
- **Multiple items in one ad block** — box separately; watch small sub-items embedded in larger boxes.
- **1/2/3-day special sales appear most weeks** — every item under those headers needs **both** a Valid From and Valid To date. On page 3, watch for unique valid dates (Tuesday/Thursday Specials) in the top section and coupons in the bottom section.

## QC specifics

### Box Draw (Low; Auto-Box ON, Box QC bot OFF)
- **Include:** coupons, packaged deals. **Exclude:** retailer logo, sign-up page, social media, special weblinks.
- Every item gets its own box; draw embedded sub-items separately.

### Tag / Tag QC (Low; Auto-tag ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates (except special-sale items — see below).
- **Name = the BOLDED name, in Spanish;** the **English name goes in the Description** (tag as it appears). Enter price/prefix/SKU/sale story as in flyer.
- **Valid Dates:** tag Valid From/To when applicable; **all items under 1/2/3-day sale headers get both dates.**
- **URLs:** box links, tag with "Link" display type and the link in the callout.
- **Categories:** every item requires a category selection.
- **Disclaimer:** only if within the drawn box (not page-bottom disclaimers). Coupons may have disclaimers; leave blank if illegible.

### Image QC
- Select clean PDFs whenever available; cutout if no clean PDF.

## FQC (Weekly owned by DOC; Monthly owned by Flex)
- Mark Autostack complete; Edit Details (No theme, no external run name — Monthly: "Monthly Savings Guide"); thumbnails Standard 4; mark items in-store only.
- Categories: **none on the first page of each version**; tag the rest by items on the page.
- Open all pages: verify coupons (display type Coupon, valid dates tagged) and all special-sale-date items are boxed/tagged correctly; Image QC.
- **Geography must read "No Stores or FSAs/zips were added or removed!"** Check all sessions ran. Complete FQC checklist.
- **Check Flyer Sorting** on the merchant page: Weekly (current) before Monthly.
- **Flyer Review type: Lite.**

## Out-of-processing
- Page swaps are standard (baseline process).

---
*Source: Cardenas Markets / Tony's Fresh Market / El Rancho Supermercado OneGuide (Google Doc `1S5VFYJ1dI7hckrHl1evB8ffNTXhJgxzMsPIhlo_d-Q4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
