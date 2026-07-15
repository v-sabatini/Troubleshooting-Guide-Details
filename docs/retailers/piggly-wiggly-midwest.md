# Piggly Wiggly Midwest — Processing Guide

> **Source:** Piggly Wiggly Midwest OneGuide (Google Doc `134ydWUc92LP3e3QZlVF_TNv32kDSgtttYS10aZJ_SQ8`), updated Mar 5, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | shopthepig.com |
| Flyer types | Weekly Ad — **2 ads a week** (Monday ad + Wednesday ad) |
| Processing | Auto-stack; Flex (3FL); no coupons, no Feedel |

Files received **Tuesday**. Works with Mercatus (third party).

## Files & schedule
- **Monday ad:** Available Mon → Mon; Valid Tue → Mon.
- **Wednesday ad:** Available Mon → Tue; Valid Wed → Tue.
- No preview, no linking document. **Pages are shared between the two ads.**

## Upload & setup (Flex) — generic codesheet
- Merchant Details → View Files → download the codesheet XLSX (labeled with the date, e.g. "Ad version 05-27-24.xlsx").
- Open the version doc in Google Sheets and open a **second** sheet. In the second sheet create a **"Wednesday"** tab with headers (in order): **Version, Stores, Page 1 … Page X** (as many Page headers as the version doc lists).
  - Copy version numbers into Version, "Store Region" info into Stores, pages into the Pages columns; number the versions 1–#. Repeat for the second table on the version doc.
- Save & Confirm — **do NOT Process Internally.** Save each tab as its own CSV.
- **Codesheet upload:** Name "Wednesday"; config **`generic`**; PDF base directory = the full file path in the SFTP (e.g. `/Reebee+07-15-2024`), double-check no extra spaces. **Uncheck toggles 2 (region assignment) and 7 (combine zones).**
- **⚠️ When uploading the Tuesday ad you'll get a "pages previously uploaded" warning — this is OK (pages are shared). Force Processing for Tuesday.** Once both codesheets complete, mark Flyer Creation complete.

### Setup QC (DOC)
- Confirm no pages left in the FTP. **Mark all vendor tasks as URGENT** (Vendors tab → select all → Urgency "Yes" → Reassign). Confirm flyer dates on the first page — **⚠️ the Monday-live (Tuesday-valid) ad's first page will NOT include a date range, and that's OK.** Tuesday ad's "pages previously uploaded" warning → OK to toggle "Code Sheets ran correctly".

## QC specifics
- **Box Draw** (Low; Auto-Box **OFF**, Box QC bot **ON**): one item per box; sub-item pricing boxed. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks (and CTAs/sale call-outs).
- **Tag / Tag QC** (Low; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.**
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.

## FQC / Flyer Review (DOC)
- Confirm dates vs PDF; availability everywhere; thumbnails include logo (Standard 4); **legibility heights 60/40**; Pages tab has no box-draw errors; no theme.
- **Geography:** ⚠️ there are **2 flyer runs** — compare against the correct run from the previous week.
- **Flyer Review type: Lite.**

---
*Source: Piggly Wiggly Midwest OneGuide (Google Doc `134ydWUc92LP3e3QZlVF_TNv32kDSgtttYS10aZJ_SQ8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
