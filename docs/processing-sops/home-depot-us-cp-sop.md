# Home Depot US — CP Processing SOP [2026]

> **What this covers:** The Content Production processing workflow for Home Depot US
> CON (Consumer) and PRO (Professional) dynamic ads on the Legacy/Snicket workflow —
> asset intake, Snicket runs, the Generate Home Depot USA Callsheet custom action,
> Flyer Creation, previews/failsafes/go-lives with daily refreshes, one-pager
> inserts, store setup, post-processing revisions (page-removal logic), and the
> Flex/Co-op morning QA.
> Source Confluence page id: `11993514005` (CP space; page titled "Home Depot US
> SOP [2026]").
>
> **See also:** Home Depot USA OneGuide at `docs/retailers/home-depot-usa.md`.
> Retailer troubleshooting: HDUS Troubleshooting Guide (Confluence CP 11997315103).

## At a glance

| | |
|---|---|
| Merchant ID | 2135 |
| Flyer Type ID | CON 6120 · PRO 6284 · Standalone 1 (one-pagers) 9976 |
| Store Set ID | CON 251177 (CPNationalCON) · PRO 251178 (CPNationalPRO) |
| Slack channels | `#homedepotus` (account team), `#amp-hdus` (morning QA) |
| Workflow | Legacy — Snicket + Flyer Creation custom action |
| Volume | PRO ~52 flyers/yr (4–5 pages); CON ~30 flyers/yr (6–12 pages, goes dark in some periods) |

## Weekly schedule

| | PRO | CON |
|---|---|---|
| Preview | Wed EOD / Thu morning | Mon EOD |
| Failsafe | Thu 7:00 PM | Tue 7:00 PM |
| Go-Live | Mon 4:00 AM | Thu 3:30 AM |
| Daily refreshes | Daily 4:00 AM | Daily 3:30 AM |

- **Preview dates:** Available window 1 min (e.g. CON Thurs 12:00–12:01 AM); hide on Flipp & Distribution.
- **Go-Live / refresh:** full 24h available (CON 6:00 AM–next 5:59 AM, PRO 7:00 AM–next 6:59 AM); show all; refresh triggers PRO 4:00 AM / CON 3:30 AM.

## Data & workflow
- **Datasource:** the HDUS API pulls product info. Datasheets: the **Market Asset Sheet** (page structure, templates, banners) and the **Product Category Sheet** (product OMSIDs). HDUS should provide **national** OMSIDs.
- **Versioning:** max 1000 pricing zones. Number of versions depends on store-level item availability and page de-duplication. **Page removal logic:** 100 pages/pricing-zone and 1000 pricing-zone limits — when pricing fluctuation pushes past 1000, the page(s) with the most pricing variation are removed and HDUS is asked for new national SKUs.

## Processing

### Folder setup
- In the CP drive: `HomeDepot USA > Assets from THD > Consumer Ad/Professional Ad`. Create a folder with the date + publication type (CON or PRO), with subfolders **Input, Output, RAW, Images**.

### Sheets & raw files
- Monday: the HDUS contact emails "Consumer/PRO Dynamic Ad Upload" — download the Product Category Sheet & Market Asset Sheet, open in Google Sheets.
- Download this week's asset folder from the HDUS OneDrive (verification links in the HDUS Toolbox; request a new link from HDUS if expired). Drop asset folders into RAW.
- In RAW there should be **PODS** and **Headers & Footers** folders — convert all those images to **72 DPI JPG**. Rename images to match the Market Asset Sheet banner names (e.g. capitalize `pro`; add/remove a leading zero on single-digit months like `02.03_Page1_Hero` vs `2.03_Page1_Hero`).
- Open the HDUS PDF mock-up and confirm banner images match; confirm all category banners have text callouts (flag to specialist if missing).

### Market Asset Sheet
- Delete extra columns/rows. Confirm banner names match the banner image files (names include `.jpg`). Confirm the fiscal week column is updated. Compare each page's template to the mock-up.

### Product Category Sheet
- Delete extra columns/rows; delete "Drop" from the "Ad Drop Date" header. Confirm the page count matches the Market Asset Sheet (insert pages have no items and aren't included). Remove duplicate OMSIDs (Column E → Data → Data cleanup → Remove duplicates); if an OMSID is removed, update the Column C ordering.

### Upload sheets
- Download both as CSV to the Input folder, renamed `market_asset_sheet` and `product_category_sheet`.

### Snicket
> Before processing, confirm in `#cp-concierge` that no one else is ingesting images while HDUS processes (Snicket ingests 1000+ images afterward and can delay others).
- Connect to VPN, go to Snicket, **Create Snicket run:** Merchant `Homedepotusa`; Publication name `Date - Preview - CON/PRO Dynamic Ad` (e.g. `2.20 - Preview - CON Dynamic Ad`); Publication Type Flyer; dates = live dates for the week. Create run.
- Upload banner images to **Marketing assets** under Data Ingestor. Drag the market asset sheet, product category sheet and template coordinates into **Run Asset Inputs**. Press **Go**.
- **Download output:** `snicket_backfill.csv`, `snicket_call_sheet.csv`, `Snicket_HDUSA_Master_Image_List_PROCON.txt` → into the Output folder. Rename the call sheet `DATE_PRO/CON_snicket_call_sheet`; remove PRO/CON from the Master Image List name per the publication. In the call sheet, filter "Image Exists" and confirm **no products are Not Found** (if any, see the troubleshooting guide → Call Sheet Errors → Image Exists - Not Found). Upload the Master Image List to the Comosoft Import in Cyberduck.

### Generate Home Depot USA Callsheet custom action
- Run the **Generate Home Depot USA Callsheet** action in CP-legacy: choose the Market Asset Sheet and Product Category Sheet for the run; Marketing assets = all images in the run's Images folder; use **Image Ingestion Point 2** and flag in `#amp-system-support` before dropping images / running.
- On success you get a no-reply email — download all attachments (Master Image List, Callsheet, Backfill, Image List) to Output. Rename call sheet and Master Image List as above; confirm Image Exists has no Not-Found; upload the Master Image List to Comosoft Import in Cyberduck.

### PRO-only call sheet modifications
- In the Call Sheet (banners in Column H) rename (casing exact):
  - `Pro_header.jpg` → `NEW-Pro_header.jpg`
  - `Pro_LDT_Header.jpg` → `NEW-Pro_LDT_Header.jpg`
  - `Pro_delivery.jpg` → `NEW-PRO_delivery.jpg`
  - `Pro_THD_logo.jpg` → `NEW-Pro_THD_logo.jpg`
- In the Master Image List (text editor) make the same replacements **without the `.jpg` extension**. Drop both files into the PRO run Output folder; re-upload the Master Image List to Cyberduck.

### Flyer run shell & processing preview
- Specialists create go-live/preview shells; for a preview, the flyer run ID is shared in advance.
- Create a preview flyer run: Available From = day before go-live 11:58 PM, Available To = day before go-live 11:59 PM; Valid From = now, Valid To = go-live day; Internal Run Name `Go-live Date - Preview - Con/Pro Dynamic Ad`; toggles **Hidden on distribution + Hidden on Flipp**.
- In CP-Legacy → **Flyer Creation:** Flyer Run ID = preview shell; Flyer Type ID CON 6120 / PRO 6284; **Store Codes 121**; attach the callsheet. Run.
- **Fadmin:** QC items/images; set a **hide-in-hosted trigger** at the same time as the available-from date/time (keeps the preview from going live); set preview date; send to specialist for review.
- **Lead review:** assign to lead for final approval; on the HDUS Toolbox "Flyer Review (Preview ONLY)" tab, fill the day of week and assign review. Send the preview email to HDUS once approved (one-store preview — viewers use zipcode **30339**, store **121**).

### Failsafe
- Copy the failsafe shell run ID. In CP-Legacy → Flyer Creation: Flyer Run ID = failsafe shell; Flyer Type ID 6284 (PRO) / 6120 (CON); Store Set ID 251178 (PRO) / 251177 (CON); Run At = 7 PM (Tue CON / Thu PRO); attach callsheet.
- QC the run next morning: search the CP Legacy ID in email for the datasheet email — it flags any pages removed due to page-removal logic or out-of-stock. Rule: a single version of a non-page-1 page removed in a single store usually needn't be flagged; multiple stores/pages, or page 1, must be flagged to HDUS for more national SKUs.
- Confirm **page 1 is present** (PRO: navy "PRO" banner; CON: "How Doers Get More Done" white banner). The failsafe **does** go live. Post in `#hdus-cp` when it looks good (note any removed pages).

### Go-live & daily refreshes
- Copy the go-live shell ID. In CP-Legacy → Flyer Creation per refresh: Flyer Run ID = refresh ID; Flyer Type ID 6284/6120; Store Set ID 251178/251177; Run At = refresh date 4:00 AM (PRO) / 3:30 AM (CON); attach callsheet. Repeat for all refreshes. Tag the specialist on the Toolbox Flyer Runs tab to review triggers.

## One-pager inserts (Grand Openings, Kids Workshops, Tax/Seasonal events)
- These are static or single-link pages sent by the HDUS contact; because they don't meet Flipp content policy they are **hosted only**.
- Download and, if not PDF, convert to PDF. If for a grand opening / new store, add the store to Fadmin first (see Store setup). Good practice: verify the store exists in Fadmin for any one-pager.
- Manually upload to the **Standalone 1** flyer type (9976): create a run (dates per email; internal run name per convention; toggles **Hide in Distribution + Hide in Flipp**; external run name by theme so it doesn't show as "Standalone 1"; No theme). Upload the PDF, Save and Complete. On the Flyer Creation task, start task → name the pricing zone / add the page → save. Add stores in the pricing zone.
- If the page has a store link that isn't available yet, box & tag the full page with the link once the HDUS contact provides it.
- Create a CP Jira ticket for the one-pager review (include the email + flyer run link), assign to the lead, and log it in the Toolbox one-page insert section (flyer run id, name, link, Jira link).

## Post-processing revisions & updates
- **Updated banner:** download (71 DPI JPG, name must match the original), upload to Cyberduck (Marketing block = hero banners; Institutional messaging = footers/headers). In the Master Image List add a unique character to the marketing block name (e.g. add `SL`); update the OMSIDs for banners/headers in the Call Sheet to match. Re-upload the Master Image List; run a 1-store test; delete/re-create the failsafe trigger (pre-live) or all upcoming triggers (post-live) with the new call sheet.
- **Item doesn't match category:** delete the flagged OMSID row in the call sheet, keep item order numerical; a replacement item is already present (extra items in the call sheet), just confirm it matches the category (move a matching item up if needed).
- **Banner link add/update (no new SKUs):** edit the call sheet directly — Column H (Filename) to find the banner, Column I (URL) to set the new link; save; cancel and re-create any triggers built on the old call sheet.

### Page 1 removed (version limit exceeded)
- If page 1 is removed it can cause CUSAT; Flex/co-ops check for page 1 during morning QC and flag in `#hdus-cp`.
- **Early in the week:** the backup/failsafe run should be set live and today's hidden. Find the "Datasheet generated" email to identify OMSIDs causing variation (usually products with 5+ variations). Email HDUS: page 1 removed due to version limit, backup extended, list problem OMSIDs, request additional **national** backup OMSIDs, note 2-business-day timeline. On receiving updated OMSIDs, re-run Snicket from scratch for a new call sheet, run a 5-store test to confirm page 1 exists (e.g. stores 121, 975, 1001, 2412, 4113), then re-make triggers/failsafes.
- **Late in the week** (can't re-process in time): pull ~10 OMSIDs from the backfill file matching page 1's category, email HDUS suggesting backfill OMSIDs for tomorrow's ad; once they confirm, swap them into the top of the call sheet for page 1, run a 5-store test, re-make triggers/failsafes.

## Fadmin flyer set-up (shells)
- **Automated:** in the Toolbox "PASTE CON/PRO Flyer Runs" tab, use Flyer Automation → add schedules; enter the flyer week start date(s) (comma-separated for multiple weeks); the script builds the rows.
- **Manual:** copy/paste a previous week's rows and adjust names/dates (mind the different CON vs PRO end times).
- **Upload to Fadmin:** copy the header `flyer_type_id`…`valid_to` + the new rows into a new sheet, save as CSV, go to the Fadmin merchant schedules page, select Home Depot USA, attach the CSV, upload. Fix any invalid runs (usually date typos) and re-run only the failed rows. For valid runs, download the completed shell CSV, copy the IDs into the PASTE tab, then add rows to the Toolbox Flyer Runs tab with name/ID and drag the URL formula down.

## Store setup
- **Add store (grand opening / new store):** confirm required info from HDUS (Store #, address, zip, city, state). Get lat/long from Google Maps (right-click the pin). Merchant page → Stores/Sets → View Stores → search the store code to confirm it's not present → Create new store. Input info + lat/long into both Latitude/Flipp latitude and Longitude/Flipp longitude (**ensure all digits, and a negative longitude**). Be very careful — incorrect lat/long affects distribution and Foursquare location. **Harmonize** the store after creating.
- Add the store to store sets 251177 (CON) and 251178 (PRO): Stores/Sets → View Store Sets → find the set → Add Stores → Ctrl+F the store code → check → Send (do both sets).
- **Remove store:** View Store Sets → find the CP set → See Stores → Remove.

## Morning QA (Flex & Co-op tasks)
- Both CON and PRO refresh daily; QC each morning starting **9:00 AM EST** (CON go-live 9:00 AM, PRO 9:30 AM). If CON is dark, skip it (no flyer); PRO never goes dark.
- Find today's run in the HDUS Toolbox Flyer Runs (go-live is always the first run of the week; refresh runs list their go-live date after "CP Refresh").
- **Data piping stuck (yellow):** re-run **Generate Sibling Groups** (do this first — it can take a while); then confirm data-piped images = 100%+.
- **Data piping errored (red):** press **Unblock flyer run** (three dots by the comment box).
- **PDF Image Auto Selection errored:** ignore.
- Confirm flyer dates match today and run to next day; confirm **page 1** present for both (PRO navy banner / CON "How doers get more done") — if missing, flag to specialists and follow the "flyer run failed to process" steps.
- Check a pricing zone with a reasonable store count via the **vertical preview** (flyer normal, products clickable, images clean). Set Seasonal Theme = **No Theme**.
- Verify on the HDUS site (Shop All → Savings → Local Ad, or `/c/localad`): CON = "Weekly Ad", PRO = "Shop Pro Ad" — live, clickable, clean images.
- Post in `#amp-hdus` when done (note errors and ping the CP team member on HDUS from the pinned message).
- **If a run failed to process:** set yesterday's run live instead (copy today's available-to and valid-to dates into yesterday's run), hide today's run on all platforms, flag in `#amp-hdus` (ping the CP team; also notify Yao He with the live flyer run id), and annotate the Toolbox. **Co-Ops only:** mark the morning-QA Jira ticket done.

---
*Source: Confluence "Home Depot US SOP [2026]" (CP, 11993514005). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
