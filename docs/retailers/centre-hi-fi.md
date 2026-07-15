# Centre Hi-Fi — Processing Guide

> **Source:** Centre Hi-Fi OneGuide (Google Doc `1TbItc_0yRM6EpHA1KwV9QPTF9tS_vMzTc3ZCOoYu_DA`), updated Jun 1, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Premium |
| Availability | All platforms |
| Slack channels | `#centrehifi` |
| Hosted URL | centrehifi.com/en/flyer |
| Flyer type(s) & cadence | Weekly Flyer (files Tuesday; Available Friday, Valid Thursday) |
| Processing | Auto-stack; DOC-owned processing; no coupons; no Feedel |
| Resources | Centre Hi-Fi Codesheet Generator |

## Files & schedule

- **When files arrive:** Tuesday. Available From Friday / Valid From Thursday.
- **Workflow:** Upload & Setup (DOC, 3 days out) → FQC (DOC, 1 day out).

## Upload & setup — codesheet build (via Codesheet Generator)

- Files received via email → download → upload to SFTP. Split-Out Upload can begin once files are in the SFTP.
- In the **Codesheet Generator**: from the Stale, copy the **ENG** ("ANG") file name from the beginning to the second underscore; paste into cell **B3** of the Start Here tab. Copy the corresponding **French** file-name portion into **B4**. **Verify the files' run dates match the flyer run.**
- Determine total pages (highest broken-out page number, or open the main SFTP doc). In the "Codesheet" tab, copy Column A down to the required page count. Create a new tab named the Valid-From date and paste **values only** (Cmd+Shift+V). Download as **.CSV**.
- **Upload codesheet:** Name `Codesheet`; Config Name **`generic_language`**; PDF Base Directory = stale path of the pages broken out.
- **Toggles: all EXCEPT 2 (Region Assignment) and 7 (Combine Zones).**
- Save → Run/Process Codesheet. Confirm **two separate pricing zones** with identical page and store counts, then mark "Flyer Creation" complete.

### Linking document manipulation
- Download the linking doc from the SFTP (e.g. `EXPORT_PROMO_SAVE_CA...xlsx`). Hide the `PROMO_TEXT_FR` and `LINK_FR` columns, save with **ENG** in front of the name. Undo, then hide the ENG columns and save with **FR** in front. Attach both documents to all vendor tasks.

### Setup QC (Vendor)
- Leg heights **40/30**; thumbnails Standard 4.

## ⚠️ Common errors / risk items
- **TV Stands must be boxed and tagged separately** — often pictured with/over a TV but are separate items with separate pricing.
- **EN vs FR boxing differs:** the EN flyer boxes+tags **every Centre Hi-Fi logo** on top of each page and links them; the FR does not (no website linking on top). Expect EN to have many more boxed items — this is normal.
- **Both versions:** first page → tag top website; last page → website, store locator, social media links.
- **TVs with multiple items but no pics:** tag the TV as an item and the main text as a Text Box; the remaining items are items.
- Categories: FR pages usually have categories but EN often won't (stereos = home audio; main categories: portable audio, home audio, TV). Leave last page and financing page blank.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** **Include** packaged deals, sign-up page (box Store Locator, usually last pages), special weblinks (box "Locate your nearest store" and the "Register to Receive Our Bargains…" text). Box all items with a price; use text boxes when necessary. **Exclude** coupons, retailer logo, social media.
- **Tag / Tag QC (Low; Auto-tag OFF, PDF image auto-selection ON):** Include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Tag MSRP pricing in the Description field.** URLs: match item to the Excel by PAGES and SPECIAL_PRICE; enter `LINK_FR` for French pages, `LINK_EN` for English. Sign-up page uses `centrehifi.com/en/pg-courriels` (EN) / `centrehifi.com/fr/pg-courriels` (FR). Store Locator: EN `centrehifi.com/en/store-locator/`, FR `centrehifi.com/magasin-electronique/`.
- **Image QC:** no PDFs — **item cutouts** only.
- **Item Category QC (Vendor):** every item needs a category; most items here = "Electronics".

## FQC (DOC) / go-live
- Overview details: no external run name; no theme generally; hidden-in-hosted no longer applies (unhidden July 2023); call-outs = front page.
- Leg heights 40/30; thumbnails Standard 4; item images all cutouts.
- **Flyer Review type: Lite** (Flex).

## Out-of-processing
- Ad-hoc page swaps (DOC) — standard "baseline" process.

---
*Source: Centre Hi-Fi OneGuide (Google Doc `1TbItc_0yRM6EpHA1KwV9QPTF9tS_vMzTc3ZCOoYu_DA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
