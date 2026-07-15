# Indexing CI Baseline Tasks — Shift Procedure

> **What this covers:** The daily CI (Content Improvement) Baseline Task shift for
> indexed flyers — Date Review, FD Board Ops Check, managing duplicate flyers, the
> Top 50 / Premium merchant check, and filing FD tickets. Step-by-step so a
> processor can run the shift end to end. Source Confluence page id: 12181569663
> (space XPTCXE).
>
> **Audience:** CI Baseline Task processors working indexed content.

---

## Tools you'll use

| Tool | Use |
|---|---|
| **Tesseract** (`tesseract.flippback.com`) | Date Review, Content Health, Duplicate Flyer Merchants, Indexed Merchants |
| **FD Board** (Jira project `FD`, board 312 — "Flipp Content Daily Priorities") | Ops Check lane; filing Broken Indexer tickets |
| **FADMIN** (`fadmin.flippback.com`) | Flyer runs, flyer sorting, toggles, geography/FSA |
| **Duplicate Indexed Flyer Tracking** sheet | Log duplicates removed |
| **Flyer Indexing Daily Health Checks** sheet | Top 50 / Premium daily log |

> Order of work is up to the shift, but complete Date Review and the FD Board Ops
> Check first; use leftover time for the full duplicate sweep.

---

## Task 1 — Date Review

Verify indexed flyers show the correct valid dates.

1. In Tesseract, open **Date Review** (`/date_reviews`). Three tabs:
   - **Pending** — flyers with dates inconsistent week over week.
   - **Flagged** — possible date errors, flagged for review.
   - **Approved** — done, no action.
2. For a run, open both **sources**:
   - **Preview** — internal preview; check for printed dates on the flyer and
     whether they match our system.
   - **Website** — the merchant's site (retailers sometimes list flyer dates there).
3. **The dates next to the CATEGORIES header are our system dates, NOT the true
   flyer dates.** Use the dates printed on the flyer itself as the source of truth
   (usually top or bottom of page 1; skim if not there).
4. Cross-reference that the preview matches the flyer live on the merchant website.
5. **If the printed dates match** the "Valid Dates" column → click **Approve**,
   then in FADMIN find the merchant → **Flyer Runs** tab → locate the run → ensure
   **"Hide in Flipp"** and **"Hide in Distribution"** are **un-toggled** (unchecked)
   so the ad pushes to the front end.
6. **If the printed dates do NOT match** → click **Edit**, input the correct dates,
   then repeat the FADMIN step above.

> **Risk item:** Always find dates from the flyer PDFs themselves or the merchant
> website. If unsure, flag in **#flex-ci**.

---

## Task 2 — FD Board Ops Check

Confirm fixed indexers are actually live.

1. Open the **FD board** and the **"Ops Check"** lane. Open the first ticket.
2. Look for a comment reading **"Verified as per this indexing session:"** with a
   Tesseract link — this means the indexer has been fixed and is ready to check.
   If instead there are ongoing questions/discussion, leave it and move to the next.
3. On Tesseract **Content Health**, search the merchant — confirm the indexer is
   **green** with no issues. (A **red** indexer language means it's broken / not
   scraping.)
4. In FADMIN, confirm the flyer has been scraped.
5. In the flyer run's **Geography** tab, grab an **FSA** to live-check.
   - **Live check** = open the Flipp app, enter the FSA/postal code, and confirm the
     flyer is live.
   - **Canadian** FSA is 3 characters — append **`1A1`** to make a valid postal
     code (e.g. FSA `N6H` → `N6H1A1`).
   - **US** zip codes paste into Flipp as-is.
6. If the flyer is live → move the ticket to **Done**.
7. **If the flyer is not live:**
   - On Tesseract Content Health, check whether the indexer is red (broken).
   - Confirm the flyer isn't just hidden on Flipp (check the flyer-run toggles); if
     hidden, complete Date Review flags in Tesseract.
   - If you can't resolve it, escalate to the Content Operations specialist in
     **#flex-ci**.

**Leave for the specialist** (do not action; leave in the Ops Check lane):
- Creation of a flyer type (wrong cadence: weekly / bi-weekly / monthly).
- Missing stores in FADMIN.
- A comment asking for further direction.

> If you're unsure of next steps to gather content, **bump the ticket in #flex-ci
> before signing off** for your shift.

---

## Task 3 — Managing duplicate flyers

Use leftover shift time to clear duplicates (including non–Top 50 / non-Premium).

> **Risk item:** When removing a duplicate, remove the **OLDER** flyer. Keep the
> **newest** flyer by **indexing date** live.

1. Open Tesseract **Duplicate Flyer Merchants** (`/duplicate_flyers_merchants`) and
   the **Duplicate Indexed Flyer Tracking** spreadsheet.
2. Go through each set of duplicates. Right-click IDs under the "indexed flyers"
   column → open in new tab to see details that reveal false duplicates:
   - **Ad Name** (e.g. "Weekly Ad" vs "Easter Specials" suggests a *false* duplicate).
   - **Distribution Area** (do both cover the same areas and match FADMIN?).
   - **Indexed dates** (when scraped — keep the most recent).
3. **Before removing:** in the tracking spreadsheet, find the retailer and correct
   week and add the number of duplicates seen in Tesseract. **Track false
   duplicates too.** If a retailer already has duplicates logged earlier in the
   same week, add the latest count to the tally.
4. **To remove a duplicate — backdate or delete the run in FADMIN:**
   - Search the retailer; open **Flyer Sorting** to see live flyers.
   - Open the retailer's website in another tab.
   - Open each live run (Flyer Sorting → "Details") and compare.
   - If both are the same and correct → **delete or backdate the older one** (by
     indexing date).
   - If runs show different flyers → keep the one matching the retailer's website.
5. Refresh Duplicate Flyer Merchants — the merchant should disappear once only one
   run remains. Repeat for the full list.

---

## Task 4 — Top 50 & Premium merchant check

> **Risk item (before filing any FD ticket):** Check the retailer's website to
> confirm there **is** a live, current flyer to scrape. If there is no flyer, or
> it's expired, **do not file an FD ticket** — the indexer is not broken. Also
> confirm a ticket isn't already filed (use the board's "search board" bar or
> Ctrl+F for the merchant name).

1. Open the Tesseract **"Top 50"** and **"Premium Merchant"** tabs and the log sheet
   in the **Flyer Indexing Daily Health Checks** workbook.
2. Set up a new section below the most recent day and add today's date.
3. For each retailer with a **TRUE** entry, act based on which column is TRUE:

**"Has Duplicates" = TRUE** (indexer created live duplicates):
- Open the retailer's Tesseract page (ID column).
- Click **Sample Zip** (2nd column) to open Backflipp (live flyers for that zip/
  postal code).
- Ctrl+F to the retailer.
- Determine whether they're true duplicates or multiple content pieces.
- If duplicates → **delete the one with the lower flyer run ID** (lower ID = older
  run).
- If different content → false positive, no action.

**"Missing Live Flyer" = TRUE** (Tesseract flags no live flyer):
- Open the Tesseract page → click **Goto**. If no current flyer on the site →
  **false positive**, no action.
- If there is a current flyer and **Gathering State** shows **"No New Flyer"** →
  click **Run All Pricing Zones** (top right).
- If Gathering State or Processing State are **red** → follow the Broken Indexer
  steps below.

**"Failed PZG" = TRUE:** disregard — a Tesseract function under construction; no
action.

**"Broken Indexer" = TRUE:** file an FD ticket (see Task 5). Title
**"Broken Indexer - [RETAILER NAME]"**, add the Tesseract page to the Tesseract
Pricing Zone field, the Goto link to the Merchant Site URL field, request type
**Broken Indexer**, and Severity **TOP50** (if in the Top 50 report) or **other**
(Premium — note this in the ticket body). **Set priority to "2 - Must Do"** for all
Top 50/Premium merchants. Submit and move to the **"Do Next"** swimlane.

4. Log every TRUE retailer in the tracker: **Column A** Retailer Name, **Column B**
   Issue Type (the TRUE column, or "False Positive"), **Column C** actions taken,
   **Column D** helpful notes.

---

## Task 5 — Filing FD tickets

> **Same risk item as Task 4:** confirm there is a live, current flyer on the
> retailer's site before filing, and that no ticket already exists for the merchant.

1. Go to Jira → **FD board** (project FD, board 312, "Flipp Content Daily
   Priorities").
2. Search the merchant name in the board to confirm no existing ticket.
3. Click **Create**. Required fields:
   - **Summary** — the issue (e.g. "Broken Indexer"); note if the merchant is
     Premium or Top 50 to flag urgency.
   - **Tesseract Pricing Zone** — search the merchant on Tesseract and copy the URL
     you land on (`.../pricing_zones?merchant_id=<id>`).
   - **Merchant** — the merchant name.
   - **Merchant Site URL** — from the Tesseract Pricing Zone page, hit **"Go To"**
     under "Starting URL" and paste that link.
4. **To classify Premium/Top 50:** on Tesseract → **Indexed Merchants** → search the
   retailer. If **Top 50** or **Premium** is TRUE, pick it in the ticket dropdown;
   otherwise **N/A**.
5. Click **Create** and move the ticket to the **"Do Next"** swimlane for the
   Trianglz team's review.

---

*See also: `missing-flyers-and-indexing.md`, `flyer-dates.md`,
`retailer-onboarding-process.md`, `escalation-and-tickets.md`,
`post-escalation-what-happens-next.md`.*

*Source: Confluence "Indexing Tasks - CI Baseline Tasks" (XPTCXE, 12181569663).
Contacts/credentials omitted. Last reviewed: 2026-07-15.*
