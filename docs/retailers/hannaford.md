# Hannaford — Processing Guide

> **Source:** Hannaford OneGuide (Google Doc `1G2LxIcwfE6r-QLu1t54b6Bce_4cEYJCwHXRUZZfvhOE`), updated May 7, 2026. Contacts/credentials omitted.

Ahold Delhaize / Royal Ahold banner. **High-risk account** — pixel settings, Ad Block IDs, and a Hosted/Flipp clone all have hard rules.

## Account at a glance

| | |
|---|---|
| Account tier | Core |
| Availability | **Two flyers:** one Hosted-only (original) + one clone available on Flipp/Distro |
| Slack channel(s) | `#3fl-royal-ahold`, `ahold-delhaize`, `ahold-ops` |
| Hosted URL | hannaford.com/savings/weekly-ad/print-view |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack; Flex (**3FL**); no coupons; **Feedel/Strategic Ops: YES** |
| Resources | AEM Portal (all files except inserts), Royal Ahold Flex Tracker, Insert Tracker, 3FL Task Instructions |

## Files & schedule

- **Files arrive:** Thursday evening in the **AEM Portal** (FS-member access only); DOC drops them into the Hannaford **SFTP**.
- **Cadence:** Available From Friday / Valid From Saturday; goes **live Friday**, valid Saturday. Preview Friday.
- **Inserts** are dropped in the SFTP almost daily ahead of their week; **triggered on Sunday** when the flyer becomes valid.

## Upload & setup (owned by DOC)

**⚠️ #1 RISK — set the flyer height to 4096 pixels BEFORE any pages enter the page pool or any tile-gen/system task runs, on BOTH the Hosted shell and the Clone.** Pixels cannot be applied afterward — doing so risks breaking the flyer and the clone. If forgotten, make new flyer runs and notify BD.

Three files (all `.txt`, import into Google Sheets rather than open):
- **Locations** = stores codesheet · **Manifest** = pagination codesheet · **Items** = vendor tagging attachment.
- **Upload Manifest first:** Name `Manifest`, **config `food_lion`**, base dir = weekly PDF path, all toggles except the first two, save & **process first** (wait for green).
- **Upload Locations second:** Name `Locations`, **config `food_lion_stores`**, base dir = **`/`**, only 1st and 4th toggle, save & process.

**Items linking document setup (critical):** delete headings, keep Page Number, Item Description/Copy Headline, Overline/Copy Body, Primary UPC, Zone, Date Start. Change Date Start to `yyyymmdd`, then in a new **Ad Block ID** column: `=CONCATENATE(F2,"",E2)` → format `20220914FP24`. Highlight Ad Block ID yellow, Overline pink, move Page Number to column A, save as XLS, attach to all vendors with the note "tag ALL items that have an Ad Module Code — no item should be missed."

- **Setup QC:** dates on page 1 bottom-left; linking doc attached to all vendors; **external run names — "Hannaford Week # Flyer" (Hosted) and "Hannaford Week # Flipp" (Flipp App)**; 4 standard thumbnails drawn across **page 1 only**; add flyer run ID to the Royal Ahold Tracker so 3FL tasks can run before go-live.

### ⚠️ Common errors / risk items

- **Flyer name "Week #" must match the Items document number exactly** (e.g. SFTP `HNBItemsWK01_05_10.txt` → shell must be "Week 01", not "Week 1") or the UPC custom action breaks.
- The week's **Items txt must be in the SFTP** or the SKU auto-populate custom action won't work.
- **Ad Block IDs** must follow `YEARMONTHDAYPAGELETTERNUMBER` (e.g. `20240414FP20`), no extra spaces/characters — they power "related items" on Hosted. If the format looks different, **stop processing and flag immediately.**
- **Style Guide rules** can only run AFTER 3FL tasks (UPC auto-tag + SKU QC) and **only ONCE**. If the UPC custom action finishes with 0 SKUs updated, escalate to engineers as CLSD.
- **Clone risk:** don't clone unless pixels are 4096 on both shells and all processing is complete on the original; don't clone until after Style Guide rules. Tracking codes carry over. Toggles must differ (Hosted-only vs hidden-on-Hosted) or the retailer sees two available flyers in their iFrame.

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required):** **include retailer logo, sign-up page, social media, special weblinks**; exclude coupons, packaged deals. Box each unique price; plated items — box the text/price, text-box the photo; "Or" second item = one box; digital coupon tagged as **Postfix**, not as a coupon. Don't box banners/social icons.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON; linking doc required):** include brand, Name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Do NOT enter SKU** (populated by the custom action in FQC).
  - **Brand field = "Hannaford"** for Hannaford own-brand items.
  - **Custom fields:** Ad Block ID (from the yellow column of the Items doc, per page/description/overline/UPC); Line Item = Y when no clean PDF; Sales Tag = Y when a SALE badge is on the PDF.
  - **Categories:** Adult Beverages only for alcohol/spirits, not regular beverages.
- **Image QC:** 1 image in box → select it only if a clean PDF (white bg, not cut off), else "Do not Use PDF Images" + Line Item = Y. Multiple images → first item listed (left-to-right); grey-background items → use the cutout.

## Post-processing / FQC

**3FL tasks (owned by Vendor):** Item Image QC (clean PDFs, left-to-right order); **SKU QC** — run custom action **"Hannaford Upc Auto Tagging"** (input flyer run, Run Action, wait for completion email), then Item Search SKU IS blank and fill from the SFTP Items txt (**use the longer of the two UPCs**); **Ad Block ID QC** — Item Search Ad Block ID IS blank, fill from linking doc; **URL Link QC** — Item Search URL IS blank, multi-edit the TTM print-view URL (`?utm_source=flipp-app…`).

**DOC:** run **Style Guide rules ONCE** (strips leading 0s to 13-digit SKUs for the Hosted API); build **insert triggers** (box/tag inserts as LINK per the Insert Tracker, positioned as a Sunday trigger — repeat for the clone; create an Optics Afterhours ticket); **clone** the run to the Flipp App shell (separate external run names, separate insert triggers, Optics ticket with fadmin name + URL, lead + BD tagged). Tracking codes already applied at flyer level.

- **FQC checklist:** geography; 4 thumbnails on page 1 only; toggles (Hosted-only vs hidden-on-Hosted); external run names; no clean images left; all Ad Block IDs + SKUs tagged; insert triggers in place; vertical scroll works; insert direct links land correctly; tracking codes carried over; Optics ticket created with Afterhours + lead review.
- **Live dates:** if "FLIPP" is in the name it's hidden on Hosted (don't flag); if not, it should show on Hosted (flag if missing). Verify Ad Block ID "related items" function on Hosted.
- **Flyer sorting:** newest preview must not be first on the retailer site (automated).
- **Flyer Review type: Lite.**

---
*Source: Hannaford OneGuide (Google Doc `1G2LxIcwfE6r-QLu1t54b6Bce_4cEYJCwHXRUZZfvhOE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
