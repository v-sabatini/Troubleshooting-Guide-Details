# Content Production Live Date Checks — SOP (FLEX & TideRise)

> **What this covers:** The morning (and, on weekdays, afternoon) live-date
> checks on Customer Success Delivery (CSD) Content Production flyers — pulling
> the "flyers going live" export, filtering to CP runs, loading them into the
> Live Dates spreadsheet, running each live check, and reporting results.
> Combines two SOPs: the **weekend FLEX** SOP (Confluence 12554666222,
> Sat/Sun) and the **weekday TideRise** SOP (Confluence 12468649985, Mon–Fri),
> which share the same core process and differ mainly in cadence, timing, and
> reporting channel.
>
> **Audience:** FLEX / TideRise live-check vendors and CSD specialists.

---

## Cadence and timing at a glance

| | FLEX (weekend) | TideRise (weekday) |
|---|---|---|
| Days | Saturday & Sunday | Monday–Friday |
| Est. time | ~30 min | 1–1.5 hours |
| Morning download | run by **10:00 AM ET** | **no earlier than 9:30 AM ET** |
| Afternoon check | none | yes (same-day go-live content) |
| Report channel (Slack) | **#cs-delivery** (tag `@csdelivery`) | **#csd-tiderise-pdfsf** |

**Assets required (both):** Live Dates spreadsheet; Flipp app and Reebee app
installed on your phone. Access via the FADMIN vendor login (credentials in the
source doc — not stored here).

---

## Step 1 — Pull and archive the export

1. In FADMIN, go to **Third Parties → Vendors**, then press the **"Flyers going
   live"** button at the bottom. This downloads **`flyers_runs_going_live.csv`**.
2. Upload the **unedited** export to the Flyer Pipeline Archive Google Drive
   folder (folders by year/month; create the folder if it's the first of the
   month/year). Rename it with today's date in **"Month Day"** format
   (e.g. `August 23 - flyer_runs_going_live`). This keeps a daily record.

## Step 2 — Filter to Content Production (CP) runs

1. Open the .csv in Google Sheets and turn on filters (all header row columns).
2. On **Column F – "Flyer Run Content Identifier"**, choose **Clear**, type
   **`CP`** in the search box, **Select all → OK**. This surfaces the Content
   Production runs.
3. Copy the result rows into a new tab called **"CP Runs"**.
4. Back on the export tab, also search the terms **`CP_Processed`** and
   **`Genesis`** (same steps) and add any runs not caught by `CP` to "CP Runs".
5. **All** CP runs receive live-date checks.

**Exclusions / flags:**
- Check the **Available Start / End** dates. If a flyer is live for **only 1
  minute** and has **"Proof"** or **"Preview"** in the Content Identifier,
  **exclude** it.
- If a "Proof"/"Preview" flyer instead shows **"Y"** for Distribution or Flipp,
  **and/or** its live window is longer than 1 minute, **flag it** with a note in
  **column T** of the Live Dates spreadsheet.
- **Home Depot US "Dynamic ads"** have their own rules — see Merchant-specific
  notes below.

## Step 3 — Load data into the Live Dates spreadsheet (Feedback tab)

Do **not** delete previous days' data — keep appending through the week.
(TideRise afternoon check is the exception; see below.)

- **Column B** — the date (column A is hidden and auto-fills the month).
- Export **Column A (Merchant Name)** → **Column C (Merchant Name)**. Columns
  **G–K auto-populate**; if not, the merchant name is misspelled.
- Export **Column F (Flyer Run Content Identifier)** → **Column D (Flyer Run
  Name)**.
- Export **Column G (Hosted URL)** → **Column E (Hosted URL)**.
- Export **Column D (Flyer Run ID)** → **Column F (Flyer Run ID)**.

---

## Live Check Process

1. **Determine which checks apply** from the category assigned to the retailer
   in **column J** (checklist is on the Category tab of the spreadsheet).
   - Example — a **"Dark"** category requires only: "Did it go live on Flipp?"
     and "Have all pages generated every image?"; mark the rest **N/A**.
   - *(On weekends, Dark / Brand / CTE-CEC flyers rarely go live.)*
2. **Confirm you're on the right flyer** when an account has multiple live
   flyers: if the account has more than one publication, a **FADMIN link
   auto-populates**. Open it, and **(TideRise) check there is no red banner
   saying the flyer is blocked from going live** — if present, flag the
   specialist ASAP. Go to the action column, press **vertical preview** for a
   pricing zone, and note the flyer name and what page 1 looks like. Compare
   against the live hosted flyers to pick the correct one.

Then run each applicable check and record Yes/No:

- **Available on Flipp? (Column L)** — set the ZIP/postal from **column K** in
  the Flipp app, search the retailer (column C). Not found → **No**; visible →
  **Yes**.
- **Available on Hosted? (Column N)** — open the Hosted URL (column E); confirm
  the ad (name from column D) is in the carousel of selectable ads. Yes/No.
- **Generated Images? (Column P)** — in the Flipp app confirm every item across
  the flyer has a generated image. Any missing image → **No**.
- **Clickable Items? (Column R)** — click 2 items per page (they should circle),
  press-and-hold to bring up the item pop, then click **"See it"** and confirm
  the flyer price matches the retailer website price. Any function failing →
  **No** (note which items in column T). **Premium retailers:** repeat on two
  items across **all** pages.
- **Notes (Column T)** — anything unsure or in question.

---

## Merchant-specific rules

- **Home Depot US** — has several ad types. Check daily the **PRO Dynamic Ad**
  (Shop Pro Ad, black banner) and **CON Dynamic Ad** (Weekly Ad, white banner),
  both using **ZIP 30339**. These aren't always in the export, hence the extra
  check. **Tax Event, Kids Workshops, Grand Opening** are one-page **Hosted
  only** (not on Flipp/Reebee/Distribution) and use the ZIP from the export;
  they can be done with the regular morning check. **Local Ad** (compressed ad
  blocks) is **not a CP flyer — do not check or include** (it's in the direct
  Live Date Check). **Do not** live-check Home Depot US flyers with "Preview" or
  "Failsafes" in the Content Identifier.
- **Grocery Outlet** — check the Flyer Run Name: **"GENESIS CP"** is on Flipp,
  Reebee and Hosted (check all). A **"HOSTED CP"** flyer is hidden on purpose and
  not on Flipp — mark **N/A** for "Available on Flipp?" (and Reebee).
- **Staples (Canada)** — two flyers go live: the **Weekly** flyer (run name
  `CP_WK# Go-Live`) is available across all channels; the **"QC Hosted Only"**
  flyer is hosted-site only — mark **N/A** for "Available on Flipp?" (Column L).
  The QC Hosted Only run corresponds to the *Circulaire* shown on the Bureau en
  Gros site (`bureauengros.com/a/contenu/flyers`); the Weekly run corresponds to
  the flyer on `staples.ca/a/content/flyers` for a non-Quebec postal code.
- **Bureau en Gros** — one flyer weekly (Fridays); **not on Hosted**, so skip the
  Hosted check and mark **column N = N/A**. In the Flipp app BEG is a separate
  merchant.
- **Geo-Targeting (Staples CA / Bureau en Gros)** — indicated by a third Staples
  run with "Geo-target" or a store number in the run name; the specialist should
  send a specific postal code to check it. If you see a geo-targeted run and have
  no postal code, message the assigned specialist in **#csd-tiderise-pdfsf**.
- **Walmart US** — not on Hosted; mark **column N = N/A**. Still a **premium**
  retailer, so complete all other checks.
- **Costco CA / Costco Grocery (and Costco US / US Grocery)** — confirm the
  correct flyer; up to three flyer types can exist. For Costco Grocery, find the
  **Grocery & Household Deals** flyer.

---

## TideRise afternoon check (weekdays only)

- **Same-day go-live Dark content:** include all flyers scheduled for processing
  that same day, unless other dates are given in the **"Processing Notes"**
  column.
- **Same-day go-live Direct content:** re-download the export, filter to CP runs
  as above, and compare the Flyer Run IDs against the morning check so you only
  add **net-new** flyers. Before starting, **hide** existing rows/data for a
  clean page (**do not delete rows**), add today's date in column B, and copy the
  retailer name from the "Retailer Data" tab into column C (G–K auto-fill; if
  not, flag the specialist in #csd-tiderise-pdfsf).

---

## Reporting and escalation

- When done, post in the Slack channel (FLEX: **#cs-delivery**, tag
  `@csdelivery` not @production; TideRise: **#csd-tiderise-pdfsf**) with a
  screenshot of the live dates and the **link to the Live Dates sheet**. Include
  the completion date as **MM.DD.YY**.
  - 0 errors → add **"All good ✅"**.
  - Any errors → add **"Errors found ❌"** and follow the escalation path.
- **(FLEX weekends)** If any **Direct or Premium** retailer has a column marked
  **No**, escalate to the CSD specialist / on-call lead via Slack DM, then the
  backup contact if there's no response within ~1 hour or the lead is OOO
  (contacts in the source doc — not stored here).

---

## Specialist maintenance (TideRise SOP)

- **Quarterly:** audit the Retailer Data tab so it reflects current accounts;
  ensure each merchant name matches the FADMIN merchant page exactly; set the
  "secondary publication" column correctly (Yes if other ops/CP flyers may be
  live at the same time on the front end).
- **Yearly:** archive the prior year's Feedback data so the sheet doesn't slow
  down. In the Analytics tab, copy the year's accuracy percents and **paste as
  values** (hard-coding them before deletion). Duplicate the Feedback tab as
  **"Feedback YEAR [ARCHIVE]"** and hide it, then clear all Feedback data except
  the autofill columns (row-3 autofill formulas and analytics formulas are
  preserved in the source SOP for reference). Real errors = errors flagged by TR
  and marked **TRUE** by the specialist; FALSE-marked flags are not counted.

---

## See also
- `publishing-and-go-live.md` and `content-v2-and-publishing.md` — how flyers get
  published / go live.
- `common-live-flyer-issues.md` — troubleshooting missing images, tiles, pricing
  once a live issue is found.
- `hosted-and-previews.md` — hosted-site and vertical-preview behavior.
- `escalation-and-tickets.md` — raising blocked/erroring runs beyond the SOP.

---

*Source: Confluence "Content Production Live Date Check [FLEX team SOP]" (VEN,
12554666222) and "CS Delivery Live Dates Check [TideRise SOP]" (VEN,
12468649985). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
