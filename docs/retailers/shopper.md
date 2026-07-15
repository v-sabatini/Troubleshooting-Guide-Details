# Shopper+ — Processing Guide

> **Source:** Shopper+ OneGuide (Google Doc `1WJz0nJ_QVtbqbYIMEGEnFDzM_sc4J3MC6MDWY88TbD4`). Contacts/credentials omitted.

Shopper+ is an **online-only** retailer processed alongside two sibling banners, **Primecables** and **123ink**. There are two flyer types (Weekly and Friday), and the Weekly flyer is **cloned** into four additional versions.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Varies by version — see cloning (some Hosted-only, some Flipp/Distribution-only) |
| Slack channels | `#shopperplus`, `#flex-processingsupport` |
| Hosted URLs | shopperplus.ca · primecables.ca · 123ink.ca |
| Flyer types | **Weekly** (Tue–Tue) with 4 clones (Primecables x2 hosted+app, 123ink x2 hosted+app); **Friday** (Fri–Sun) in 3 versions (Shopper+, Primecables, 123ink) |
| Processing | Auto-stack; Flex Processing Support; no coupons; no Feedel |
| Linking document | Yes, always |

> **Historical context:** 3 "fake" store locations are set up in FAdmin with large distribution ranges so shoppers in those FSAs are served the flyer — there are no physical storefronts.

## Weekly flyer

- **Files received:** Tuesday (email when files are in). **Cadence:** Available From Tue 9:30 AM, Available To Tue 9:59 AM; Valid From Tue 10:00 AM, Valid To Tue 9:59 AM. **Preview date:** Thursday before go-live (important — enables the preview email). Tue–Tue, no customer preview.
- **Setup (DOC):** upload all page versions/languages to one main Shopper+ run; set page order per the **Pagination doc in the SFTP** (Shopper+ 1–4, Primecables 5–8, 123ink 9–12, Common 13–15). Create two pricing zones (EN / FR) each in correct page order; add all stores to **both**.
- **Setup QC:** dates as above; internal run name = valid dates; preview date Thursday; available everywhere (toggles blank); no external run name; no theme (unless seasonal carousel requested). Thumbnails: standard 4 (1065x600, stock_premium, storefront_carousel_premium, storefront_carousel_organic). **Attach the linking document to all tasks (Mass Attach)** — file `flyer url raw-Flipp_Shopper+WeeklyFlyer[Dates].xlsx` in the SFTP. **If uploading on a Wednesday, file an Urgent Processing ticket.**
- Occasionally a new page 1 arrives to be swapped in on a specific date — leave it out of the pricing zones and set a trigger.

## Friday flyer

- **Files received:** Tuesday (separate email). **Cadence:** Friday 12:00 AM → Sunday 11:59 PM; no preview. Available on **Hosted only**.
- **Setup (Flex):** three separate uploads — one each to the Shopper+, Primecables, and 123ink flyer types; each run gets **only** its own banner's pages (both languages) per the Pagination doc; common pages added where indicated. Two pricing zones (EN / FR), all stores in both.
- **Setup QC:** Friday–Sunday times; internal run name = "Friday + dates"; **Hide on Flipp and Distribution (check toggles); check off Secondary publication**; no external run name; no theme; standard 4 thumbnails; attach linking doc `flyer url raw-Flipp_Shopper+FridayFlyer[Dates].xlsx`.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Linking doc required (used for both Box/Tag). Exclude coupons, packaged deals, retailer logo, sign-up, social. **Include special weblinks** (per linking doc).
- **Tag / Tag QC — Medium; Auto-tag OFF.** Include brand, name, pre/postfix, valid dates, **description (tag the PLUS price in the description)**, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Image QC:** use PDF images wherever possible; cutouts only if the PDF is unavailable or looks bad.
- **URL/Links QC:** Overview → Items Without a URL — generally all items get a link; find missing links in the linking doc and **apply the correct language link (EN/FR)**.

## Final QC / go-live

- Items missing URL: should be none. Leg height 60/40. No item image QC. 4 standard thumbnails. All items QC'd; check tagging on the last 2 pages (known error spot). Pages in correct order per zone; languages set. Sessions ran; vendor tasks complete; **geography same WOW** ("No Stores or FSAs/zips were added or removed"). "Not all categories have thumbnails" and "stores not assigned" warnings can be ignored.
- **Weekly FQC must be done Thursday** so the preview link goes out on time; Flex messages DOC when done.

## Cloning (Weekly flyer only)

After the Shopper+ Weekly flyer is FQC'd and page swaps are completed (typically Monday), make **4 clones** via Overview → Ad Hoc Processing → Clone. Do **not** copy tracking codes/URLs; clone into the prebuilt shell (same "Month + Day" name). For each:

1. **Primecables (Hosted only):** hide on Flipp & Distribution; delete all Shopper+ & 123ink pages — keep only Primecables + Common (~7 pages/zone); rerun sessions; redo FQC.
2. **123ink (Hosted only):** hide on Flipp & Distribution; delete all Shopper+ & Primecables pages — keep only 123ink + Common; rerun; redo FQC.
3. **Primecables (Flipp/Distribution only):** hide on Hosted; keep only Primecables + Common; add all stores to both zones; rerun; redo FQC.
4. **123ink (Flipp/Distribution only):** hide on Hosted; keep only 123ink + Common; add all stores to both zones; rerun; redo FQC.

Then send the retailer the two Hosted-only preview links (Primecables & 123ink, flyer types 10612 / 10613) — verify they load first.

## Flyer review / out-of-processing

- **Flyer Review type: Lite.**
- Post-live page swaps: reviewed Monday (sometimes Friday); a FAB ticket can route swaps to Flex; complete in time to re-clone and re-send previews.

---
*Source: Shopper+ OneGuide (Google Doc `1WJz0nJ_QVtbqbYIMEGEnFDzM_sc4J3MC6MDWY88TbD4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
