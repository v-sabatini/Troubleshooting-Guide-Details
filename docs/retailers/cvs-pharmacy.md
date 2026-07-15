# CVS Pharmacy (incl. Longs Drugs & Y Mas) — Processing Guide

> **Source:** CVS OneGuide 2.0 (Google Doc `1IHjYNkHXNY6nLtOa_oKs2ZSrKa41BWveiKrzBAU2B9w`), updated Jun 23, 2026. Contacts/credentials omitted.

CVS has **four flyer types — CVS Weekly, Y Mas, Longs Drugs, and Navarro** — processed differently. The Weekly flyer is the complex one (Ad Block IDs, tagging & pagination documents attached to tasks); Navarro and Y Mas are simpler and get no attachments.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard |
| Availability | Weekly / Y Mas — all platforms · **Longs Drugs — Hosted only** · Navarro — all platforms (one Flipp version in the Navarro merchant + one Hosted-only version in the CVS merchant) |
| Slack channels | `#cvs` |
| Hosted URLs | cvs.com/weeklyad/pageview · longs.com/weekly-ad.html · navarro.com/weekly-ad |
| FAdmin merchants | CVS Pharmacy 2264 (Weekly, Y Mas, Longs, Navarro Hosted-only) · Navarro Discount Pharmacy 3026 (Navarro Flipp version) |
| Processing | Auto-stack; **no Flex**; OS completes coupon processing; no Feedel |

## Files & schedule (publication)

| Flyer | Available/Valid | Files & processing |
|---|---|---|
| **CVS Weekly** | Avail From Thu · Valid From Sun · Avail/Valid To Sun @ 2:59 AM | PDFs received well in advance (v23.47 may arrive separately). Tagging doc 5–8 days prior (can upload but not process). Ad Block URLs Mon–Wed before Thu go-live. Coupon doc Wednesdays; coupon corrections Mondays. |
| **Longs** | Avail/Valid From Sun @ 6 AM · To Sun @ 5:59 AM | Files Wednesday evenings; upload & FQC Thu/Fri. |
| **Y Mas** | Avail/Valid From Wed · To Tue (2-week run) | Files 5+ business days ahead; processing day set by processor. |
| **Navarro** | Avail/Valid From Wed · To Tue | Files 2–5 business days ahead; latest upload Mon, latest FQC Tue. |

**Weekly workflow:** Mon = upload Week 2 + coupon corrections · Wed = upload Week 1 + full FQC + flyer review · Thu = Longs upload/FQC · Fri = Ad Block URLs imported + Longs/Y Mas flyer review.

## Upload & setup — Weekly (owned by Vendor; Flyer Type 498)
PDFs arrive via a OneDrive link (email login code to the processor or the CVS alias). Download all files/folders, then log into the CVS SFTP (**username is "CVS" — all caps; lowercase fails**). Non-Weekly banners load into the SFTP as-is; **Weekly requires file prep first.**

**Weekly file prep:**
- Unzip and rename the folder `MM-DD Ad Event`. If v23.47 arrived separately, copy that folder into the main folder (skip the PVT_Zone_Memo).
- In folders **v65, v57, v91, v23-47**, confirm the naming convention `MM-Dp0#v[PZrange]` — page numbers under 10 must have a leading zero (`p01`, not `p1`); `v` always sits between page number and version. v65/v57 have no range.
- In **Core-Zoned**: files like `p02v3-99` are fine as-is. **"All except" files must be renamed.** "All except" = a base page delivered to all zones except those covered by alternate pages (zone sequence runs 1–134). E.g. `p01AllExceptv3-99` → base goes to zones 1 and 134 → rename `p01v1-134`. If 1 or 134 are listed, use the codesheet to find the base sequence's first/last (commonly v3-75). Transfer the folder into "CVS Weekly" in the SFTP.

**Codesheet (Zone Memo) manipulation:** import ZoneMemo `.xlsx` to Google Sheets. Zone groups split into tabs by shared pages (Base v3-75, v23.47, v54, v65 Manhattan, v91, etc.). FAdmin reads the page number (left column) for pagination and the version sequence (second column) for zone placement — it uses the **first and last** number in the sequence as the page-name identifier.
- **Core Ad tab:** scroll to the red "For Flipp Processing" section, delete data between the `page, version, base pricing` headers and the first line under "for flipp processing" (**keep the headers**).
- Duplicate the tab for v23.47, v57, v65, v91, and any other unique folder; put the version under VERSION; delete duplicate page rows created by the duplication.
- Save `.xlsx`, upload to the flyer run.
- **RISK:** a PZ left out of the middle of a version sequence means the page won't be added to that zone. Errors are usually a typo or a wrong page name in the SFTP.
- **After upload — DO NOT change Available/Valid To dates** (early changes cause excessive item-validity spotchecks); adjust in Pre-FQC.
- Sort PZ pages low→high to verify page counts (v65/54/23/47), then high→low to catch double pages.

**Common codesheet errors:** "No page with version x and page number # was found" — check the PDF name vs the codesheet (a page may be mislabeled, e.g. codesheet says p03 but file is p02v43-78), or the leading "0" after "p" is missing. A duplicated row (or a PZ listed in the middle of two rows) also errors — check the page-PDF bottom edges for the source of truth and delete the extra row.

**Setup QC — attach Vendor attachments:** Tagging Document (no manipulation); Table of Contents Category Pagination (update each tab with each category's page #, download `.xlsx`); Ad Block IDs (merge the Core Zone PDFs into one document and attach).

## ⚠️ Common errors / risk items (retailer-specific)
- **Featured product headers** (groups at the top of category pages): use a **cutout** of the whole selection; unless a specific product name is listed, use the category name (e.g. "Shave & Deodorant") and capture "See below for additional details" in the Sale Story.
- **Large item spreads under one product name:** box together when possible (all items share the same name and tagging); when layout prevents it, box separately but keep the **same name and identical tagging.**
- **Two items with different prices must NOT be boxed as one.**
- **Auto-Tag gets many CVS rules wrong** — you must review and adjust EVERY item. Pay extra attention to Descriptions and Name typos.

## Box Draw (Medium — Auto-Box OFF, Box QC bot ON; linking-doc required)
- **Include:** disclaimers, coupons, packaged deals; special weblinks (Weekly only). **Exclude:** sign-up page, social media.
- Box the "Find it Quick" header and its categories separately; **box the capitalized section headers** (HEALTH, BEAUTY, PERSONAL CARE, FOOD & HOUSEHOLD, OTHER OFFERS). Box "Back to Find it Quick" icons and category headers.
- **Box ALL text on the page even if not for sale** (for text-to-speech) — for Weekly, refer to the Tagging Document `.xlsx` for the list. **Avoid text boxes** — prefer two separate default boxes.
- Box the small black "Go to… for…" URL banners.

## Tag / Tag QC (Medium; Auto-tag ON; PDF image auto-selection ON)
- **Include** all fields (name, brand, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs).
- **Name** contains ALL identifying text **including sizes** and any "ANY"/"ALL"; put exclusions with the name text (not the disclaimer). **All sale info other than Current Price goes in the Sale Story** (include the full discount text and any `*`/`††` symbols).
- **SKU = Ad Block Numbers** from the attached "MM-DD Ad Block IDs" PDF (the number in the black box). Almost all items have one; a few (v57/v65/v23-47 unique SKUs) won't appear in the merged PDF — add missing SKUs via Google Sheets during/after Pre-FQC.
- **Description:** sizes and **all badge/banner text** (Same day pickup, New at CVS, Mix & Match, Send to Card, red-box/circle text).
- **Custom fields:** `Extrabucks` (write "Extrabucks" when the word appears — powers a Hosted front-end integration); `Print MFR Coupon` (amount when a Digital mfr coupon is referenced; fill both if it also references Extrabucks).
- **Table of Contents:** "Find it quick!" header tagged as an Item; TOC directions and headers tagged as **Page Links** per the Pagination `.xlsx`. Category page headers tagged as Items.

## Image QC
- Select a **clean PDF image** (lifestyle/plated preferred over cutouts). **Multi-item:** use a clean PDF of the FIRST listed item (move down the list if needed).
- **Cutout only** for text-only items and for **category page header groups** (items directly under a category header like Household); all other items on that page get a PDF.

## Post-processing (owned by DOC)
- **Item Category QC:** select a category for every item; for multi-item names use the first item's category.
- **FQC codesheets:** run the **Staggered Dates codesheet** (unchanged week over week) and the **Eventmaster store codesheet** (paste the header row from an old eventmaster; delete all "Puerto Rico" rows in column I; save `.xlsx`/`.csv` and upload).
- **Pre-FQC:** mark spotcheck complete; standard thumbnails; leg heights 55/35. Edit Details → update Available/Valid To to Sun @ 2:59 AM; External Preview Name "Sneak Peek"; no theme.
- **Item Search QC automation (as of July 2026):** Export Items → drag the `.csv` into the **CVS Automation** Google Colab notebook → run → Import the cleaned `.csv` (~10 min). The automation: (1) flips PAGE_LINK→ITEM for page > 7 non-nav rows; (2) clears stray categories where sale_story + current price are blank; (3) moves ct./pk./oz. sizing from description into name; (4) moves parenthetical "(excludes …)" exclusions into the name; (5) sets the Extrabucks flag from sale_story and renames the column `id_1`. Then manually check for PAGE_LINK-vs-ITEM outliers ("Back to Find it quick" boxes should be Page Links to the TOC page; black-background category names are Page Links).
- **Ad Block URLs** imported Friday (post-processing).

## Flyer Review
- **Weekly:** Wednesday. **Longs/Y Mas:** Friday. Coupon QC checks Thursdays & Sundays; coupon revisions Mondays.

---
*Source: CVS OneGuide 2.0 (Google Doc `1IHjYNkHXNY6nLtOa_oKs2ZSrKa41BWveiKrzBAU2B9w`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
