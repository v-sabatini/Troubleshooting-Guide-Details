# Academy Sports + Outdoors — Processing Guide

> **Source:** Academy Sports + Outdoors OneGuide (Google Doc `1azkr8dL…nymsA`).
> 🔒 Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Availability | All platforms |
| Slack channel | `#academysports` |
| Cadence | **Ad-hoc** — a schedule is provided but **very often changed at the last minute** |
| Processing | Auto-Stack; **Flex not involved**; OS does standard tasks |

> **Note:** shells are made ahead of time, but **follow the PDF dates over the shell dates.**

## Upload
1. Files arrive by email; a linking doc (URL/SKU list) is requested from the retailer.
2. Codesheet dropped in **PDF, XLSX, and CSV** in the SFTP — mark off PDF/XLSX, **download the CSV**.
   - Open and check for issues/disclaimers; **delete any disclaimers in the top 3 rows**.
   - If a **Store Tile column** is in Column B, delete it.
   - Pages sometimes out of order (e.g. "PAGE 2" is `page_10`) — **reorder**.
3. Upload codesheet — **Config: `academy_sports`**; **every toggle checked *except* Region Assignment and Combine Zones.**

## Setup QC
- Confirm all pages picked up (FTP open). Attach the linking document to box, box QC, tag, tag QC, and PQC. Set preview date; external run name from the folder (e.g. "Hunting Ad," "Active Ad").

## Box Draw / Tag (Low complexity)
- **Box Draw:** include social media, sign-up page, special weblinks, retailer logo, packaged deals; **exclude coupons**. **All "SHOP NOW"/"SHOP ALL"/"SHOP ___" call-outs boxed separately** (and tagged as **links** with the same URL as the connected product). Bottom banners boxed & tagged. Boots often have **2 prices on one image = 2 items**; a grouping of shoes with **1 price = 1 item**.
- **Tag:** include all fields (brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs). SKU & URL provided in an attached spreadsheet; if not found, search academy.com.
- **Image selection:** single item in image → clean **PDF**; multiple items in image → **leave as Item Cutout** (do not select PDF).

## Pre-final / out-of-process
- Download **custom tiles** from FTP. Thumbnails: **Standard 4 + custom tile** (override 2nd & 3rd) **and** draw the tile labeled "thumbnail" (shows on their website).
- Action any page swaps / custom-tile swaps from email. Check "Shop Now" boxed separately as direct links; **re-run tile gen on a different script if strange text artifacts appear.**
- Image QC (uncheck data piped); Wayfinding QC; Spotcheck QC; page categories; mark items **In-Store Only**.
- **Tracking codes** (Hosted + Distribution): reference a previous flyer — UTM campaign changes by date, `utm_term` is always `__SKU__`; add **OGMAP** codes; click **Apply All Tracking Codes**.
- FQC, then send a **preview email** (ad dates, custom tile, items without URL, flyer sorting — Active then Hunt, newest at top; separate email per flyer).
- **Flyer Review type: Lite.**

---
*Source: Academy Sports + Outdoors OneGuide (Google Doc `1azkr8dL_5TnYMhHKYbLZyBNlwVk1jGbhpQfUCRnymsA`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
