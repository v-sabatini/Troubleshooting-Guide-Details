# Kj's Market — Processing Guide

> **Source:** Kj's Market OneGuide (Google Doc `1Bp0igzugTTpK5lJlt1_nzt1AQOedxDmofHYkT0puNuE`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (Longtail) |
| Availability | All platforms |
| Slack channels | `#kjsmarket` |
| Flyer type(s) | Weekly Flyer |
| Processing | Auto-stack; no coupons; no Feedel/retailer data services |
| Involvement | **Vendor** owns upload; **DOC** owns FQC; **FLEX** owns Setup QC & Flyer Review |

## Files & schedule

- **Files received:** Wednesday.
- **Publication cadence:** Available Wednesday–Tuesday, Valid Thursday–Wednesday.
- **Linking document:** N/A.

> **Shared banner:** Kj's and **IGA Southeast** share files. The version document includes **both** IGA and Kj's info — for this upload use **only the Kj's information**.

## Upload & setup (owned by Vendor)

- **Build the Generic Codesheet:** download the retailer version document from the FTP (search XLS, e.g. `031126_WLF_VERSIONS_FLIPP`). In a blank sheet add headers: Version, Stores, Page 1, Page 2, … (one per page listed). Copy/paste the Kj's data across. Save as `Kjs _date_` (e.g. `Kjs 3.04`).
- **Upload the generic codesheet:** in the flyer-run shell open the Codesheet interface. Name: `codesheet`. **Config name = basepath from the FTP where files were dropped** (e.g. `/3.11`). Toggles to **include:** Store or Set Assignment, Page Upload, Allow Pricing Zone Creation, Tile Generate afterwards. Process; complete flyer setup once the run is GREEN.

## ⚠️ Common errors / risk items

- **Shared FTP with IGA:** when uploading from SFTP, confirm no pages are left unuploaded. Pages remain in the FTP because it's shared with IGA — **ensure ALL Kj-labelled files are uploaded** (don't upload IGA files).
- Confirm all pages uploaded (Pricing Zone tab → Items View) and flyer dates (usually first/last page).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** exclude coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- **Tag / Tag QC (Low; Auto-tag ON):** include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Brand handled in Tag/QC.
- **Image QC:** standard — PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing (20% of pricing zones).

## FQC / flyer review

- Confirm dates (vs PDF) and availability toggles; thumbnails (Standard 4) include retailer logo; all items boxed/tagged; previews clickable; sessions complete; geography correct.
- **Flyer Review type: Lite** (shared review guide with IGA Southeast).

---
*Source: Kj's Market OneGuide (Google Doc `1Bp0igzugTTpK5lJlt1_nzt1AQOedxDmofHYkT0puNuE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
