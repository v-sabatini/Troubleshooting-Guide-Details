# Proxim — Processing Guide

> **Source:** Proxim OneGuide (Google Doc `1ZWrGeKnNbRRUgjBLxrQaHbV-46JQDmSSmsh59UTOk_o`), updated Jul 6, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | Yes (channel not specified in guide) |
| Hosted URL | groupeproxim.ca/en/flyer |
| Flyer types | Ad-hoc · **Weekly (5832)** · **Monthly (5869)** · **C – Bi-weekly** (cloned from Weekly) · **Carnet Beauté** (Catalogue, cloned from Weekly) |
| Processing | Auto-stack; Vendor upload, OS setup, Flex + DOC QC; Feedel (retailer data services) yes; no coupons |

Bilingual (EN + FR — French zones are set to English during upload and switched to French at FQC). Files received Monday.

## Files & schedule
- **Weekly cadence:** Available Tue → Mon; Valid Thu → Wed (2-day preview). Files uploaded Thursday (or earlier if assets are in).
- **Monthly:** doesn't necessarily start on the 1st or run exactly a month — trust the prebuilt flyer-run dates.

## Upload & setup (Vendor)
### Weekly (5832) — codesheet upload
- Upload the pagination document (`A# digital.xlsx`) from the SFTP to the shared Proxim folder; update the Vendor Tracker.
- Copy the **pages only** (no header) from the pagination doc → paste into the template's **Pages** tab at A2 → download the **Codesheet** tab as CSV.
- Codesheet notes: Page 3 has **A1/A2** variants; Pages 1–2 have **"regular"/"Holiday"** variants. Keep all pricing zones as **English** for now (including FR zones).
- **⚠️ An invalid store will be assigned so the codesheet can run — no distribution impact, safe to ignore the warning.**
- On error, it's usually a client typo in the codesheet: read the error for the problem file name and fix it in the template (e.g. add the missing `.p1`), re-download the Codesheet CSV, re-upload.

### Monthly (E) — manual upload
- Manual upload from SFTP as **English** pages (FTP → search "Monthly" → latest ~2 pages, standard pagination by page number). Add a Vendor Tracker line below the Weekly run.
- Pricing zones **E** and **E FR**; assign pages 1–2; keep both English for now. Add the **"Proximed Monthly Stores"** store set to both.

### Setup QC (Flex)
- Check sessions, Item View, vendor tasks. **Ignore store-related flags until FQC.** Standard setup QC: Weekly available Tue–Wed (2-day preview), valid Thu–Wed; available everywhere; internal run name set; no external run name; no theme (unless specified).

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **ON**): **box every individual item** with its flyer info — Proxim doesn't use data piping and item-pop images are mostly cutouts, so draw clean boxes. When item and info are separated, box the image and text-box the info. Box the merchant website wherever seen. Atoma-vs-Name-Brand pages: box **both** Atoma and Name Brand. **Anything with a price gets boxed.** Include packaged deals, retailer logo, sign-up page, social media, special weblinks; exclude coupons.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price. **Exclude disclaimer and URLs.**
  - **Name:** include item name **and** brand name in the Name box.
  - **Description:** separate French and English by spaces; anything not bold/capitalized goes here; capitalized text goes in **both** name and description; put sizes on a separate line between the FR and EN.
  - **⚠️ French pricing convention:** comma in place of the period, dollar sign at the end (e.g. `XX,XX$`). For a **price range** (not a sale/regular price, e.g. $10.99–$13.99), **tag the higher price in the postfix**. Percentage-off with no current price → tag the % off as the **prefix**.

## FQC (Vendor)
- Review/approve pending Ops tasks. Confirm dates & banner name match the PDF page 1; **Available From must be 2 days before Valid From.**
- **Pricing zones (Weekly):** if you see **four** PZs, **delete the two with fewer pages**; if only 2, proceed. Rename **A2 FR → A FR** and **A2 → A**. Remove all stores from both zones and add the **"Proxim Weekly Stores"** set to both (A and A FR).
- **Monthly:** two PZs ("E", "E FR") — don't delete/rename. Add the "Proximed Monthly Stores" set to both.
- **Insert:** upload the insert (Pages → Edit → Upload) to the last position of all pricing zones. Start Vendor Box QC and ensure **one box** covers the entire insert; add a URL only if a URL sheet is in the shared drive (Display Type **Link**). ⚠️ Number of inserts varies and not all need linking.
- **Distribution:** Weekly ('A') available everywhere; Monthly ('E') **Hidden in Distribution + Hidden in Flipp**.
- Draw 4 standard thumbnails (no white borders, logo present). Item Image QC → Generate Data Piping Groups; prefer clean PDF images (white background) over cutouts where appropriate.
- **⚠️ Pricing zone language:** set **A FR** (Weekly) and **E FR** (Monthly) to **French**. **Remove all "WEB" pages** from both zones — they clone into a separate run. Check Vertical Preview interactivity.

### Cloning
- **Weekly → Carnet Beauté** (Flyer Type: Catalogue): flyer shells exist; select the correct run. Same details as Weekly except **assign ONLY the WEB pages** to both zones. Standard-4 thumbnails (logo not cut off), no insert, add "Proxim Weekly Stores" to A and A FR. Re-complete FQC checklist.
- **Monthly (E) clone:** add "Proximed Monthly Stores" to E and E FR before completing the FQC checklist (per FQC video). For cloned runs, mark red tasks "N/A"; then Save → refresh → Save and Confirm.
- **C – Bi-weekly** (cloned from Weekly, runs weekly): 2 zones C/C FR, pages 1–4 (same pagination as the 4-page Weekly).

## Flyer Review
- **Flyer Review type: Lite.**

## Out-of-processing — adding stores
- The vendor uploads the runlist (`XXX digital.xlsx`) to the SFTP by Tue/Wed. Download, copy columns A/B/C, paste into a Google Sheet without formatting, save as CSV. Upload as a codesheet on all runs — Name "store upload", **Config name `proxim_stores`**, PDF base directory `/`, **only the first toggle checked**. Cross-language to French.

---
*Source: Proxim OneGuide (Google Doc `1ZWrGeKnNbRRUgjBLxrQaHbV-46JQDmSSmsh59UTOk_o`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
