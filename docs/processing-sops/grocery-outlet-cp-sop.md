# Grocery Outlet — CP Processing SOP

> **What this covers:** Content Production processing for Grocery Outlet (GO) —
> the current Monday/Tuesday Genesis workflow (custom action report, image
> ingestion, upload, inserts, grid processing, FSA checks, Fadmin) and the DVM
> asset/custom-action process.
> Source Confluence page id: **8666612155** (CP space).
> **See also:** Grocery Outlet OneGuide in `docs/retailers/grocery-outlet.md`.
> Contacts/credentials intentionally omitted.
>
> Note: the page also retains a "DNU! Monday Processing – Old Process" section
> (superseded); that legacy flow is intentionally not reproduced here.

## Account at a glance

| | |
|---|---|
| Merchant ID | 2906 |
| Flyer Type (Genesis) | 3435 |
| Validity | Wednesday → Tuesday |
| Slack (system) | `#amp-system-support` |
| Slack (DVM) | `#wg-grocery-outlet-dvm-flyer` |

## Monday processing (2025/2026 update)

### Run the custom action

- Start work at 1pm. In CP Legacy, run **'Grocery Outlet Report V3'** (5–10 minutes).
- Project name: `GO (flyer run ID) - (Date)` e.g. `GO 875717 - June 28`.
- Select the **CP GENESIS** flyer run (correct Flyer Type with "CP GENESIS" in the name, correct run dates). Provide the flyer available-from/to dates spelled out (e.g. `June 28, 2023- July 4, 2023`; use short forms for long months, e.g. Dec). Ensure dates are Wed–Tues.
- On completion an email arrives; download both `.csv` files.

### Downloading images (new process, Apr 2026)

- Open both `.csv` files as Google Sheets.
- In CP-Legacy, select **'auto image processing'** custom action; attach the images `.csv` in the 'Product Data CSV' spot.
- Message in `#amp-system-support` (@here + @csdelivery) ~15 minutes before running, stating the time and ingestion point (e.g. "I am dropping GO images in ingestion point 2 in 15 minutes").
- Select **ingestion point 2** (unless told to use point 1 by the team). Click **run action**.

### QC data

- The custom-action email lists flags. Alert the processor if any Item Names are flagged. **Empty brand can be ignored.**
- Any stores showing "removed due to less than 5 items" must be flagged to the processor with final assets.
- Rename the results `.csv` as `GO Datasheet MMM DD` (e.g. `GO Datasheet Dec 17`), download as `.xls`, and send to the processor with the images `.csv` and any removed-store flags.

### Checking stores (while report generates)

- Open the grid `.xls` from the GO FTP (`.../merchants/2906/ftp_files`); use the latest file, check for REV files.
- Filter column B for blanks, delete blank rows, unfilter.
- Filter column M (Genesis) for "no" — those are typically new stores that go live one day later (handled Tuesday). Record store numbers that are not found to flag to the processor.

### DVM assets

Upload the GO Datasheet, folder of PDFs from Cyberduck, and grid XLS to the GO Weekly Files drive in a folder `MMM DD DVM Assets`. Once the processing version of the grid is created (Tuesday), add it in `.csv` format.

### Upload process (Aug 2025)

- Once images are in, run Custom Action **"Content Production Flyer Creation"**: flyer type `3435`, current week's flyer run ID, GO Datasheet xls saved as CSV.
- **Set trigger for 9pm.** Check Lago Explorer (~10 min after) that automats picked up the job. If the run stalls, cancel the job, verify cancelled in LAGO, and restart (stalls occur when too many jobs run at once).

## Tuesday processing

- Flyer run should be ready by 9am. Confirm all sessions ran and pricing-zone images populate.

### Add inserts

- In the Flyer Run → Pages tab → Edit; open the go-live-dated folder, select all pages (expand all arrowed sections), Select Files, capture revised files, Add pages, Save and complete, let sessions run.

### Copy PDF tagging

- In the Processing-Only flyer run (created by Ops) → Pages tab → Copy items → add the CP run's flyer run ID as Destination.
- Back in the original run, confirm everything boxed/tagged correctly. **Ensure tagging is correct on loyalty/cover pages.** Verify PDFs are not jumbled/layered incorrectly; check the live/previous run for additional insert-page tagging.

### Grid processing

- Manipulate the grid `.xls`. Duplicate the first tab → rename **Processing** (or Processing 1 if multiple). Filter column B (stores) for blanks, delete blank rows. Change Page # to **Cover Page** (including the email sign-up page), delete all columns after end date and the URL columns (Genesis column can stay). Download the Processing tab as CSV.
- Run **Custom Action – 'grocery outlet insert pages'** (on the original custom action page, not CP-Legacy) with this CSV + flyer run ID. Let sessions run; spot-check pricing zone layout. Create Processing 2, 3 tabs and triggers for pages that come down/up on other days.
- **Light PDF weeks** (e.g. only loyalty page + coupons/covers/sale inserts for select stores): use the layout tab instead of the custom action — insert the "download the deals" page in last position (position 10) for all stores, and note store/zone-specific extra pages (typically position 1).

### Check FSAs

- Pricing Zone tab → Stores/FSAs; sort smallest-to-largest. If any are 0 (typically 2 stores), find the store zip in the grid, find the other store with the same zip, then run custom action **"Fsa Swap"** (from 443 to 469, using those store IDs and `91006` as the FSA).
- Remove unwanted ZIPs via custom action **'remove FSAs'** (Flyer Run ID, no Pricing Zone ID, paste the EAST ZIP list into 'FSAs to Remove').

### Fadmin processing

- Item Image QC — cutouts only if the image is not clear. If clean images are not loading, re-run datapiping, then PDF image extraction at 0x0, then choose all pages and force selection.
- Mark items in store only; check leg. heights.
- **Draw the 5 tiles** (also press Mark Complete): `Thumbnail 1065x600`, `Stock_premium`, `Storefront_carousel_premium`, `Storefront_carousel_organic`, `xw_thumbnail`. (Rarely there is a custom tile.)
- No toggles hidden and no theme (for hosted-only, hidden in Flipp). Spot-check horizontal and vertical preview.
- Notes: every pricing zone has 1 store only; each has the email sign-up page in last position; minimum 6 items; Grand Opening stores start 1 day later; Flyer Sorting — Weekly Ad in 1st position ahead of any standalone ads. New stores without genesis pages / few cover-inserts go hosted-only (staggered dates if enough items to go live on both).
- Complete the verification list on the GO HQ sheet (PDF layering, FSAs fixed, store count, grand-opening stores, triggers applied).

## DVM process

- Upload datasheet + grid XLS to a `MMM DD DVM Assets` folder; add the processing CSV (all versions/tabs). Update the GO team in `#wg-grocery-outlet-dvm-flyer` with expected page/layout changes.
- Once all main-run processing is complete, set triggers:
  - **'Grocery Outlet Publish DVM'** custom action for 12:01am (main-run flyer run ID + the same GO Datasheet CSV; 2–8 min).
  - **'Grocery Outlet Insert DVM Sections'** custom action for 12:05am (flyer run ID + processing version of the grid CSV).
- **DVM error playbook (monitor):**
  - "Failed due to no genesis pages" (lists store number) — happens when the grid says "yes" under Genesis but the store has no genesis pages (no data uploaded). Fix: on the processing tab, find the store and change Genesis to "No".
  - Fails if a filename on the grid is missing its extension — ensure all files include `.pdf`.
  - Fails if there are duplicate pages within one store (one row = one store).
  - Flag unresolved failures in `#wg-grocery-outlet-dvm-flyer`.

---
*Source: Confluence "Grocery Outlet SOP" (CP, 8666612155). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
