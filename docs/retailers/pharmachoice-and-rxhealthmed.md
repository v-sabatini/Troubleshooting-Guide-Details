# Pharmachoice & RxHealthMed — Processing Guide

> **Source:** Pharmachoice & RxHealthMed OneGuide (Google Doc `1QsQpcHFXqJDGClOjRRRsMiGNC4ASXY5yQTb50l-8-n8`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms — **except** flyers labelled "No Promo" and/or with fewer than 6 items, which are **Hosted only** |
| Slack channel(s) | `#pharmachoice` |
| Hosted URL | Pharmachoice via merchant portal; RxHealthMed rxhealthmed.ca |
| Flyer types | **Pharmachoice:** Flyer (#3167), Health Centre Flyer (#5691) · **RxHealthMed:** Weekly Flyer (#7272) |
| Processing | Auto-stack; Flex (Processing Support / FAB tickets); no coupons; Strategic Ops (Feedel/retailer data services) |

There are **4 flyer categories**: FL (Flyer), HC (Health Centre), No Promo, and RX HealthMed. FL/HC/No Promo live under the PharmaChoice merchant page; RX HealthMed has its own merchant page. HC and RX HealthMed do **not** follow the same cadence as Pharmachoice — the codesheet shows if they're included that week.

## Files & schedule

- **Files received:** Monday. All assets sent together — you must **clear the RX HealthMed FTP of Pharmachoice files** once uploaded.
- **Publication cadence:** Available From Thu, Valid From Thu; Available To Wed, Valid To Wed.
- **No Promo files** drop at the top of the month and run every week; the codesheet pulls the relevant files for that specific week (not all pages used every week).
- **Linking document:** required, split by FL / HC / RX. No-Promo runs use that month's No-Promo linking doc. HHC does **not** get a linking doc — note "no linking document" in the vendor-task comments.
- **Workflow owners:** Upload/Setup = Vendor/Flex; Image QC = Flex; FQC = DOC/Vendor.

## Upload & setup

1. Download the codesheet from the FTP.
2. **RISK 1:** ensure each page name starts with `_p` — add it if missing (Ctrl+F).
3. **RISK 2:** No Promo pages end with `_0001` (or a variant) — replace with the naming convention seen in the FTP.
4. In Excel, append `.pdf` to every page in the FL/HC/RX zone (the OneGuide provides a short VBA macro for this).
5. **Split into FL, HC, No Promo, and RX** — each runs into its own flyer shell. Copy/paste into separate sheets (include the header). FL and HC can share a tab but must be separated. Download each as its own CSV.
6. **Upload the codesheet:**
   - **Config name: `generic`**
   - PDF Base Directory: take directly from the FTP path.
   - **Toggles: 2nd and last unchecked.**
   - Save.
7. Process the codesheet. Let sessions run.
8. Upload the (split) linking documents to the vendor tasks.

### Config / base-directory notes
- **FL, HC, HHC, RX share the same PDF base directory; No Promo has a different basepath.** For No Promo, search "No Promo" in the FTP and copy the base path from the latest month — verify against the page/zone name in the codesheet (e.g. an "April No Promo" page uses the April basepath).
- Match the week number: flyer shell week number must match the FTP files (e.g. PC17 pages ↔ PC17 shell).
- Confirm the RxHealthMed pages aren't labelled `Month_RxHM_No Promo` before applying standard settings — those follow the No-Promo settings instead.

### Setup QC / Edit Details
- **FL, HC, HHC, RxHM runs:** Available Wed→Thu, Valid Wed→Wed; Internal Run Name `PC XX - <flyer type>`; no external run name; no preview start date; **Distribution: available everywhere** (no theme).
- **No Promo runs:** same dates; Internal Run Name `PC XX - No Promo`; **Distribution: Hosted only.**
- Thumbnails: **Standard 4** (leg heights preset 45/30).

### ⚠️ Common errors / risk items (retailer-specific)
- **Codesheet base directory:** FL/HC/RX same base directory; No Promo different — mixing these up is the top risk.
- **Toggles:** No Promo flyers are **Hosted only** — do not leave them available everywhere.
- Page names must start with `_p`; No Promo suffixes (`_0001`) must be renamed to the FTP convention.
- No Promo codesheets may run **yellow** with a "files uploaded" warning — this is safe to ignore; you can "force process."
- **Store errors on process:** stores may need to be added (Fadmin names the exact store codes). Cross-reference the Reebee booking list for the store code; escalate to the Reebee equivalent if not found.
- **Linking doc too large to attach:** email it to the OS vendor instead (recipients in the OneGuide) with the run ID and run link.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks.
- Box each product block that has a price or sales story individually; if one price applies to multiple items in a block, box them together as one.
- Box banners with call-to-actions (look for the **red rectangle** to identify the CTA).
- Box the flyer location page and the `pharmachoice.com` banner.

### Tag / Tag QC (Low complexity — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name, brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** SKU.
- Tag name/brand/description/pre-postfix/valid dates/sale story as seen in flyer; price/original price if available.
- **URLs:** apply strictly per the linking document.
- **Disclaimer:** only enter if it's **within the drawn box** — do not use a page-bottom disclaimer.
- Categories: pick the closest category (chart in the OneGuide).

### Image QC
- Prioritize the PDF image; filter for cutouts and no-images. **No Promo flyers do NOT get Image QC.**

## Final QC (owned by DOC/Vendor)
1. Spotcheck; mark Auto-Stack Spotcheck complete.
2. Image QC (No Promo excluded).
3. QC categories — check all pages; a better category often applies (No Promo excluded).
4. Verify every URL against the linking document.
5. Rerun sessions as needed; verify links; mark items store-only.
6. FQC checklist.
- Flyer Review type: **Lite.**

## Out-of-processing
- See the retailer's 2025 Black Friday operations guidelines (linked in the OneGuide) for publication & ad-hoc request handling.
- Email communications for this account are owned internally (not stored here).

*Note: FTP file-transfer credentials appear in the OneGuide — not stored here (credentials in the OneGuide — not stored here).*

---
*Source: Pharmachoice & RxHealthMed OneGuide (Google Doc `1QsQpcHFXqJDGClOjRRRsMiGNC4ASXY5yQTb50l-8-n8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
