# Target USA — Processing Guide

> **Source:** Target USA OneGuide (Google Doc `1m3ksvWvVVnqCPrezgSm9kb3IEjxwyU1cZer03jXy5A4`), updated Jun 29, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms (hidden in Hosted) |
| Slack channels | `#target` |
| Flyer type(s) & cadence | Weekly Circular — Flyer Type #381 |
| Processing | Auto-stack |
| Who's involved | Vendor setup; OS setup; DOC FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Publication cadence:** Available/Valid Sunday → Saturday.

### ⚠️ Common errors / risk items
- **Valid dates of Books, Movies, and Music:** the available date often differs from the flyer; item valid dates are indicated at the top of the page (e.g. "All movies available March 1st, Books available March 4th").
- **Description:** enter exactly as it appears on the page — a recurring true error.
- Look for multiple products (box separately).

## Upload & setup (owned by Flex)

- **File uploads:** download files from Target USA cloud Windows servers (access provided by the client). If revisions arrive 3–4 days before FQC, sub them into the original content file so OS can process at once. Use an FTP program (Core FTP, FileZilla, etc.).
- **Upload NEW store sets:** clear out all existing store sets in the Store Sets section of Merchant first.
- **Codesheet manipulations (Weekly):** copy only the PDF column to the last Pricing Zone (AK) and page row into a new Excel; save as CSV. Do **not** include the Lettered Ecomm Insert pages (those are uploaded manually if present).
- **Codesheet upload:** Config name = **`target_usa`**; PDF Base Directory from SFTP; toggle **Everything except 2nd & last**; **no Region Assignment or Combine Zones**.
- **Manually upload the Lettered Insert pages** — not in the codesheet; add them during FQC.

### Setup QC (owned by Flex)
- Geography; vendors assigned; sessions running.
- Edit Details: Key Messages Main = "Target Deals"; dates correct; Available = **Hidden in Hosted**; no theme.
- Leg heights preset 60/40. Thumbnails Standard 4. Complete Setup QC checklist.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON)**
- Include: packaged deals, sign-up page, special weblinks. Exclude: coupons, retailer logo, social media.
- Box every item with a price/discount. For items inside a larger image, box the individual product then draw a **text box** around its price/description.
- **Multiple products, one price:** box each product separately (e.g. two different water brands boxed separately = correct; Starbucks + Snapple boxed together = incorrect). Text boxes around each product's name/description.
- **Inserts:** box any call-to-action links; box the entire insert page if a link is present and there are no individual priced items.

**Tag / Tag QC (Low; Auto-tag OFF)**
- Include: name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude SKU and URLs.** Brand is Box-specific.

**Image QC:** clean PDFs if available, cutouts fine otherwise.

## Final QC / go-live notes (owned by DOC)

- Spotchecks. **Add REV pages:** download from the folder provided by the client contact and upload; prefix with REV 1, REV 2, REV 3, etc. depending on version.
- **Add Lettered pages** per the original email: some go to all PZs (e.g. `pceomal` — "al" = all PZs), some are PZ-specific (e.g. `pgcomhi` — "hi" = that PZ). See instructions video (from 5:20).
- Create a Jira ticket for inserts (example OPSMR ticket in the OneGuide). Check geography; all vendor tasks complete; sessions rerun if needed. Pricing Zone tab horizontal/vertical view. No-page category check. Verify REV pages reflect the client's email.
- Edit Details: dates Sunday → Saturday; Available = Hidden in Hosted; no theme; Key Messages Main = Target Deals. Leg heights preset 60/40; thumbnails Standard 4; Image QC = clean PDFs if available, otherwise cutouts.
- **Flyer Review type: Lite.**
- **Out-of-processing:** pre-live page swap (gather files, then swap) — see videos.

---
*Source: Target USA OneGuide (Google Doc `1m3ksvWvVVnqCPrezgSm9kb3IEjxwyU1cZer03jXy5A4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
