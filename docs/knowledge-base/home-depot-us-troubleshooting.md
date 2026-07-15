# Home Depot US (HDUS) — Troubleshooting Guide

> **What this covers:** Retailer-specific errors and fixes for the **Home Depot
> US (HDUS)** flyer pipeline — CP Legacy, Call Sheet (specialist), Flyer PDF, and
> Fadmin-related issues — plus the API used as source of truth. Source Confluence
> page id: 11997315103 (space CP, "Home Depot US Troubleshooting Guide [2025]").
>
> **Audience:** Content Production processors / HDUS specialists.
> **Escalation path:** Flag to Partner Technology (PT) or escalate per
> `escalation-and-tickets.md`.

---

## Snicket errors (ARCHIVED — reference only)

The **Snicket Issues** section of the source page is marked **Archived**. It is
kept here only for reference; confirm the current process before acting on it.
Errors documented there: *missing columns / validation not possible*,
`API error - FETCH_IMAGE_URL. processBatch. ItemId: not found`, *insufficient
items to fill page*, `API Error - 403: Forbidden - backfill - get nvalues error`,
and *missing marketing asset on s3*. If you hit one of these on a live Snicket
run, check whether the workflow has moved to CP Legacy first, then flag to PT.

---

## CP Legacy errors

### Image Data not found

- **Symptom:** `Image Data not found` — an image in the data sheet could not be
  found or retrieved.
- **Fix:**
  1. Copy the **OMSID** for the affected product(s).
  2. Find those OMSIDs in the **product data sheet** and **remove the entire
     row**.
  3. Update the **placement order** column to adjust for the removed rows.
  4. Redownload the product data sheet and **rerun the Custom Action**.

---

## Call Sheet errors (SPECIALIST ONLY)

### Image Exists — Not Found

- **Symptom:** An item shows `Not Found` under the **Image Exists** column of the
  Call Sheet.
- **Fix:**
  1. Filter for the item with the image not found and copy its **N-Value**.
  2. Open the **backfill file** and Ctrl-F the N-Value.
  3. Copy the **OMSID** for a backfill item with that N-Value.
  4. Replace the OMSID of the not-found item with the new backfill OMSID.
  5. Copy the **Image Shape** from the backfill into the Call Sheet's Image Shape.
  6. Change the item's **Image Exists** value from `Not Found` to `Found`.
  7. Save the Call Sheet.

---

## Flyer PDF errors

### Pricing doesn't match website

- **Symptom:** HDUS flags that flyer pricing does not match the website.
- **Key fact:** The **HDUS API updates daily at 3 AM**; all jobs run after
  **3:30 AM**.
- **Fix / response:**
  1. Check the API to confirm whether the website price matches the API.
  2. The Home Depot **GraphQL API**
     (`https://apionline.homedepot.com/federation-gateway/graphql`) pulls the
     product info and reflects what is in the consumer ad — this is the **source
     of truth**.
  3. If the API matches the ad, explain that the discrepancy is likely due to
     **caching**, since data is pulled after the API refresh.

### Incorrect banner assigning

- **Symptom:** An old or incorrect banner is assigned on the PDF.
- **Fix:**
  1. Confirm the new banner uploaded into **Lago** properly and was not rejected;
     if rejected, reconvert and re-upload. Confirm the banner filename matches the
     **Market Asset Sheet**, and that the file is **72 DPI JPG**.
  2. If the banner is in **Lago Explorer**, check banner assignment there:
     project list → Home Depot US → expand all projects → find the **CP Legacy
     ID** for the run → open the affected page → expand **articles → all** →
     select the marketing block → **Asset Assignment** tab.
  3. If **two banners** are assigned (usually because they share the same name),
     delete the one you don't need. You must **hard delete** that image in the
     remote desktop.
  4. In the **master image list**, for each banner add a letter or two before the
     first `x` in the marketing-block text to create a new unique ID (e.g. add
     `LL`). Apply the same letters to the marketing-block text in the **call
     sheet**.
  5. Re-drop the master image list and **re-run the flyer** with the new call
     sheet.

### Blank banner

- **Symptom:** No banner assigns to the PDF; the space is blank.
- **Fix:**
  1. Same banner checks as above (uploaded/not rejected, filename matches Market
     Asset Sheet, **72 DPI JPG**). The **master image list** assigns banners, so
     if it isn't uploaded, banners won't assign.
  2. On **Lago web** (`https://comosoft-app-lago5.flipp.com:8500/LAGO/`) go to
     the Home Depot US project type → **Monitor → transfer jobs → pending jobs**;
     confirm no tasks are pending.
  3. If none pending, check **done jobs** for `New Snicket Master Image List
     PRO/CON` and confirm no errors. If there is an error, download the error log
     and troubleshoot per the message.
  4. If the banner is in **Lago Explorer**, check assignment (same navigation as
     above). If the Asset Assignment window has no banner, **manually assign**
     one: in the **Asset Light Table**, drag-and-drop the desired banner into the
     Asset Assignment window.
  5. Apply the **unique-ID / re-drop / re-run** steps as in *Incorrect banner
     assigning*.

---

## Fadmin-related errors

### Pricing zones exceed 1000

- **Symptom:** A run exceeds Fadmin's **1000 pricing-zone limit**, causing
  sessions to fail to generate and clogging the Fadmin queue. Zone count is
  visible in the **session tab** under **flyer level tile gen** (example run
  showed 1011 zones).
- **Likely cause:** Increased versioning — usually HDUS providing **non-national
  SKUs**, which raises backfill items and unique pricing and creates more zones.
- **Fix:**
  1. Get the **CP Legacy ID** for the run and search email for the run's CSV
     (datasheet).
  2. In the CSV, add filters to the top row and scroll to column **AX
     (`id_3`)**. Pages aren't in order in the CSV, so use this category column to
     find where most items come from.
  3. Filter each category, note row counts, and find the **page** tied to the
     category with the most rows — that page is driving the versioning.
  4. Contact Home Depot: inform them of the increased job size and the suspected
     page. Ask them to either **resend with national SKUs** or **remove a page or
     two** to reduce versions. Recommend using **insert pages** (not templates)
     for categories without national SKUs going forward.

### Data piping stuck (yellow) or errored (red)

- **Symptom:** A data-piping task in the pipeline is **stuck (yellow)** or
  **errored (red)**.
- **Fix:**
  1. **Rerun the task** `Generate Sibling Groups`.
  2. If that fails, click the **Unblock Flyer Run** button (three dots next to
     the comment box).

### Page 1 removed

- **Symptom:** Business logic removes pages when too many versions push pricing
  zones over 1000. If **Page 1** is removed it can cause **CUSAT** issues; FLEX &
  co-ops check for Page 1 during morning QC and flag missing Page 1 in the
  `hdus-cp` channel.
- **Fix / response:**
  1. Set **yesterday's / failsafe run live** and **hide today's run**.
  2. Find the `Content Production FlyerRun: Datasheet generated` email for
     today's run and check which **OMSIDs** are causing the variation (products
     with **5+ variations** are usually the issue).
  3. Email the HDUS contact: state Page 1 was removed due to increased variation
     exceeding the version limit, that a backup ad is live, list the problem
     OMSIDs, and request **additional national backup OMSIDs**. **Timeline: 2
     business days.** (Note: if new OMSIDs are not national, the page-removal
     logic may still remove Page 1.)
  4. If the issue occurs at the **end of the flyer**, check with HDUS whether any
     backfill OMSIDs are national and can be used; if so, **swap the national
     backfill items into the call sheet**.
  5. If HDUS provides **net-new OMSIDs**, rerun the process in **Snicket from
     scratch** to produce a new call sheet. Then create a new flyer run in the
     HDUS flyer type, run a **5-store test** (any 5 stores), **cancel triggers**,
     and create new triggers for the rest of the week with the new call sheet.

---

## Source of truth: the HDUS API

The Home Depot **GraphQL API**
(`https://apionline.homedepot.com/federation-gateway/graphql`) is used to pull
product info and reflects what appears in the consumer ad. It **refreshes daily
at 3 AM**; jobs run after **3:30 AM**. Use it to confirm pricing when HDUS flags
a discrepancy. (Access credentials/details are in the source doc — not stored
here.)

---

## See also

- `turbo-cp-legacy-error-guide.md` — general Turbo & CP Legacy error strings.
- `home-depot-canada-dvm-module-runbook.md` — HDCA DVM feed/rendering runbook.
- `escalation-and-tickets.md` — escalation and ticketing.

---

*Source: Confluence "Home Depot US Troubleshooting Guide [2025]" (CP, 11997315103). Contacts/credentials omitted. Snicket section is archived in source. Last reviewed: 2026-07-15.*
