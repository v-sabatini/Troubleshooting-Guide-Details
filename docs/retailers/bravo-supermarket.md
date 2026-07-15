# Bravo Supermarket — Processing Guide

> **Source:** Bravo Supermarket OneGuide (Google Doc `16v3us9CIc43SQ1UijlKAW0MUDXRWozRRjyCkUENOV9M`), updated Jul 30, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#alpha1` |
| Hosted URL | bravosupermarkets.com |
| Flyer types & cadence | Weekly (Available Thu, Valid Fri → Thu) |
| Processing | Auto-stack; Flex (Flyer Review); OS (Setup); no coupons; **Strategic Ops — yes (Feedel processing)** |

## Files & schedule

- **Files received:** Monday.
- **Publication:** Available From Thursday; Valid Friday → Thursday.
- **Linking document:** No.
- **Recommendation:** wait until **Friday afternoon** to begin upload, since not all pages sync at once and later pages may need manual pricing zones.

## Upload & setup (owned by Flex/Vendor — manual upload account)

Flex confirms files received with the retailer; if the email isn't answered, flag `#flex-processingsupport`.

**Bravo Supermarkets / Bravo NE (same as C-Town upload):**
- Files in FTP. Upload ALL **U43 and PU43** pages (**except any containing "AKO"**).
- Create **Base u43** zone and **Base pu43** zone using the 'B' pages from each.
- Create **individual zones** using the custom front pages: e.g. store "321" gets its own PZ using page `U43_321_W21` as page 1, then b2, b3, b4 for the rest.
- Add individual stores to their new zones; add all remaining stores to Base zones. **If a zone has 5 pages, remove the Base page 4 to make room for the store-specific page 4.**
- After the processor runs, check the FTP for skipped pages. **Stores "062" and "032" are intentionally skipped;** `.ako` files are excluded. Upload any missed revised pages manually to the correct PZ.

**Bravo Florida:**
- Manual upload account. Upload ALL **U45** pages; manually number pages 1–4 (P1=Page 1, P4=Page 4).
- Create Base zone from 'B' pages; create individual weekly zones named by store code (look in P1 box for P1s with a store code instead of B; check P4 box for a unique page 4). Add individual stores to their zones; remaining stores to Base (Bravo FL storeset minus individual-zone stores). If a zone has 5 pages, remove Base page 4.

### ⚠️ Common errors / risk items (retailer-specific)

- **New store flagged** ("no store exists for that page"): if the page obviously belongs to a new store (e.g. "Grand Opening"), add the store to FAdmin; if unsure, create it so the processor can run, then flag the merchant.
- **Updated stores:** if the store code exists in FAdmin but the U43/PU43 prefix doesn't match the FTP file, it has flipped U↔PU — edit the store (Merchant page → stores, search numeric code e.g. 315) and switch to the opposite prefix.
- **JPGs uploaded with PDF pages:** pre-processor can't distinguish JPG from PDF and errors ("no store associated"). Create a throwaway store (merchant code from the error, name DELETE, city New York, state NY, address 1, zip 10153), retry codesheet, force processing on the "already uploaded" error, generate sessions, then delete that PZ/store/JPG.
- **COVID "Open for Business" process:** create an `Open for Business` PZ, manually upload the local PDF, do NOT check "process internally," let sessions run, add the one page; reconcile stores against base zones and copy OFB stores from the prior live week; remove any store that has its own PZ this week.
- **Box draw:** multiple related items (e.g. cuts of turkey) → ONE box around the main picture only; box each different item separately even if the price is cut off (no separate text box for the lb price).

## QC specifics

- **Box Draw — Low complexity. Auto-Box ON, Box QC bot OFF. No linking doc.** Exclude coupons, packaged deals; include retailer logo, sign-up page, social media, special weblinks. Box anything with a price; use text boxes when necessary; draw neatly. One box per item.
- **Tag / Tag QC — Low. Auto-tag OFF. PDF image auto-selection ON. No linking doc. No SKU. No URL (N/A this merchant).** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Always include category.**
  - **Name:** as in flyer, ALWAYS CAPITALIZED; no measurements (those go in Description); never include non-bolded words.
  - **Description:** as in flyer; include non-bolded words and measurements; do NOT include 'With Card'/'Without Card' (that goes in Postfix).
  - **Postfix:** enter 'With Card. Without Card $xx.xx' if applicable.
  - **Prices not inside the drawn box (e.g. "2.99 lb", "6.99 LB") STILL must be tagged.**
  - **Valid dates:** use the dates on the first page of the publication. A theme banner (e.g. 4th of July) does NOT change valid dates — stick to the front-page dates.
  - Long non-bolded lists: use "Or" before adding alternatives (items with different measurements) to Description; omit "Or" for plain varieties.

## FQC / go-live (owned by Vendor)

- Mark auto-stack spotcheck complete; confirm dates match first page.
- Thumbnails: standard 4 + `first_page_thumbnail_400w` (note "complete" in comments).
- **Flyer Review type: Lite.**

---
*Source: Bravo Supermarket OneGuide (Google Doc `16v3us9CIc43SQ1UijlKAW0MUDXRWozRRjyCkUENOV9M`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
