# Manitobah — Processing Guide

> **Source:** Manitobah OneGuide (Google Doc `1v8jocY-_ROLiaAc33hOIcDpcjixIbStv17O9Xn_Idfk`), updated Nov 26, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1p-manitobah` |
| Flyer types | Ad hoc — **two merchants:** Manitobah (Canada, #12171) and Manitobah US (USA, #12193) |
| Hosted URL | USA: manitobah.com/pages/catalog · Canada: not on hosted |
| Processing | Auto-stack; no coupons; no Strategic Ops / Feedel; Flex (Processing Support) |

**Two merchants, processed identically except URLs:** Canada URLs end in **`.ca`**, USA URLs end in **`.com`**.

## Files & schedule

- **Files received:** ad hoc (PDF pages + URL docs via SFTP). Always double-check PDF dates; confirm with client/BD if needed.
- **Linking document:** **Yes** (URLs) — **two separate URL docs**, one for US (`.com`) and one for Canada (`.ca`).
- **Custom action (USA only):** "Assign FSAs from CSV" — assigns FSAs to the single pricing zone; runs post-FQC and after any page swap.

## Upload & setup (owned by DOC)

- Manually upload pages: Pages → Edit → select pages with the country code for that shell (`can` or `us`). Index pages in order; **language = English only.** Save + Save & Complete.
- Create **Base** pricing zone for all pages; add all stores. **USA has 1 dummy store** that must be added so it goes live on Hosted.
- Once sessions run, **attach the URL document as a mass attachment to all vendor tasks.**

### ⚠️ Common errors (retailer-specific)

- **URL QC (top risk):** ensure **all Canada URLs end in `.ca`** and **all USA URLs end in `.com`**. See the Links QC filters below.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF).** Linking doc (Tag/QC specific). Include special weblinks; **exclude** coupons, packaged deals, retailer logo, sign-up page, social media.
  - Multi-item products boxed **separately** using the text-box feature; box the callout at the bottom; Direct-Link items (gift cards, etc.) are called out in the linking doc.
- **Tag / Tag QC (Low; Auto-tag ON).** Include name, pre/postfix, valid dates, description (use descriptions from the linking/tagging doc), SKU, price, sale story, categories, disclaimer, original price, URLs; **exclude brand.**
  - Callouts/non-product items tagged as **Direct Links** per the linking doc; "Shop Your Way"-type bottom section boxed with links.

## Post-processing (DOC)

- **URL/Links QC** via Item Search:
  - **ALL:** URL "is" blank → 0 items should appear; any that do, check the linking doc.
  - **USA:** URL "contains" `.ca` → 0 results (any → correct to `.com`).
  - **Canada:** URL "contains" `.com` → 0 results (any → correct to `.ca`).
- **Assign FSAs from CSV (USA):** copy the base pricing-zone ID, paste into the `flyer_id` column of the FSA-list template (all rows same number), save as CSV, run the "Assign FSAs from CSV" custom action with the flyer run ID. Repeat for the 2nd flyer run with the correct sheet.

## FQC / flyer review

- **FQC (FLEX):** standard-4 thumbnails; complete FQC checklist in FADMIN.
- **Flyer Review type: Lite.**

---
*Source: Manitobah OneGuide (Google Doc `1v8jocY-_ROLiaAc33hOIcDpcjixIbStv17O9Xn_Idfk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
