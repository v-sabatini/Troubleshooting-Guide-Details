# La Moisson — Processing Guide

> **Source:** La Moisson OneGuide (Google Doc `1GeRYg9_B-_fZPWnsrDQeytSE319e9yvB5peOe6wBgYw`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Platforms / availability | **Two flyers per period** — Standard (all platforms) + Off App (Hosted only) |
| Slack channel(s) | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | lamoisson.com/pages/circulaire-flyer |
| Flyer type(s) & cadence | Flyer (11783), ad-hoc |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); no OS beyond standard; no coupons; no Feedel |
| Linking document | **Yes — REQUIRED, must be split into two docs** |

French-language account.

## Files & schedule

- **Files arrive:** ad-hoc.
- **Cadence:** Available/Valid From 1st or 16th → To 15th or 30th/31st of the month.

## ⚠️ Common errors / risk items — TWO FLYERS

- **There are always two flyers per period, going live at the same time:**
  - **On App / Standard** → available everywhere.
  - **Off App** → **Hosted only** (files/folder named "off app" or "hidden from apps"; have their own section in the linking doc). If no second flyer shell exists for the period, create one for the same dates.
- Pages may need to be added to the SFTP by processor if client emails files.

## Upload & setup (owned by Vendor)

- **Linking document:** one doc is sent via SFTP containing links for both flyers — **create two copies**:
  - "La Moisson Linking Doc - On App" → delete all rows below/including "Pages off apps".
  - "La Moisson Linking Doc - Off App" → delete rows 2 through "Pages off App", leaving only Off App links.
- **Original flyer run:** manual upload (exclude any pages with "OFF APP" in the name); add page index numbers to the Grouping Number field; language **French**; Save & Confirm (**do NOT process internally**).
  - PZ 1 = Base (French, all applicable pages); PZ 2 = "Base CL" (French, check **cross language**). Add all stores to both (ignore FSA/store overlap warning for now).
- **Off-App flyer run (Hosted only):** same steps but upload only the pages with "OFF APP" in the name. Attach the correct linking doc to all vendor tasks.

### Setup QC
- Confirm availability: **Off App = HOSTED only; Standard = EVERYWHERE**. Confirm all SFTP pages uploaded; flyer dates; thumbnails Standard 4; preview dates set.

## QC specifics

- **Box Draw (HIGH; Auto-Box ON, Box QC bot OFF):** linking doc used for both Box/Tag. **RISK:** Auto-Box can't draw text boxes and with this layout usually only boxes the actual products — **during Box QC, draw text boxes** so Text-Extraction & Auto-Tag run properly. Include (if in linking doc) coupons, packaged deals, retailer logo, sign-up page, special weblinks; social media **excluded unless in linking doc**. Recipe pages: box title + recipe boxes per URLs in the doc (tag as Link item type).
- **Tag / Tag QC (Medium; Auto-tag ON):** Brand small font ALL CAPS; Name medium font (shown French then English — **tag French only**); pre/postfix small grey text near price ("&+"); include valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude SKU.** Percentage discounts (e.g. -10%) go with Sale Story.
- **Image QC:** PDF preferred if clean, otherwise cutouts accepted.

## Final QC / go-live notes (owned by Flex)

- Confirm dates, availability toggles, thumbnails include retailer logo.
- **Links QC:** Overview → Item Search → URL → Is → compare items without a URL to the linking doc.
- Confirm no pages in the PZ have "Off App" in the name (remove if so).
- In the "Base CL" (cross-language) PZ, change the language toggle to **English** (without deselecting cross-language) — you should then have a French and an English PZ, and the FSA/Store overlap errors should disappear.
- Standard checks: all boxed/tagged, spotchecks 20%, previews clickable, sessions complete, geography correct.
- **Flyer Review type: Lite.**

---
*Source: La Moisson OneGuide (Google Doc `1GeRYg9_B-_fZPWnsrDQeytSE319e9yvB5peOe6wBgYw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
