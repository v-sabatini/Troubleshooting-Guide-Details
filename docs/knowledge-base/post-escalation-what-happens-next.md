# After You Escalate: FD, CLSD & MSC — What Happens Next

> **What this covers:** Where an OTS ticket goes once the front-line team
> escalates it, what each downstream team/board handles, and **how long it
> typically takes** — so you can set the right expectation with a retailer or
> account owner. Grounded in the FD, CLSD, and MSC Jira projects (samples from
> Jan 2024–Jul 2026).
>
> **Audience:** Flyer-ops / CX staff who've filed (or are about to file) an
> escalation and want to know "what now?"
>
> ⚠️ **Turnaround numbers below are from samples**, not full-project pulls, and
> vary widely by issue and priority. Use them as rough expectations, not SLAs.

---

## The escalation map (corrected)

| Root cause | Goes to | Project = |
|---|---|---|
| Broken indexer / flyer not gathering | **FD** | Flipp Content Daily Priorities |
| Content-platform / pipeline / categorization / cloning / harmonization *fix* | **CLSD** | Content Layer Service Desk |
| Foursquare measurement / store-trip reporting / ad feasibility | **MSC** | Marketing Science (the "PIA" analytics function) |

> **Note on "PIA":** Links that look like `PIA-1234` now resolve to **`MSC-1234`**
> (Marketing Science). MSC mostly handles **Foursquare advertising/measurement**
> (feasibility checks, trip reporting, data submissions). The **actual
> store-harmonization fixes** are worked in **CLSD** (and historically the **HTS**
> queue), not MSC. Earlier drafts of this CXE Help Center routed harmonization to "PIA" — the
> accurate path is **CLSD** for the fix, MSC for measurement/trip data.

---

## FD — Broken Indexer (missing-flyer escalations)

**What it is:** The **FD** project ("Flipp Content Daily Priorities") is where
**Broken Indexer** tickets live — "any enabled merchant on **Tesseract** that
didn't gather the latest flyer correctly." This is the destination for most
"flyer missing" OTS tickets.

**Volume:** High and routine — the sample showed **~100 broken-indexer tickets in
just the first 24 days of Jan 2024** (roughly 4–5/day). Indexers breaking is
normal background noise, usually triggered by a retailer changing their website.

**Typical turnaround (sample of 100):** very spread out —
- ~13% same day, ~31% within 3 days, ~49% within a week,
- but a real tail: ~27% took 8–30 days and ~23% took **>30 days**.

**What to tell the requester:** "It's been sent to the indexing team (FD); simple
re-gathers can be same-day, but some take a week or more depending on why the
retailer's site broke the scrape." Once FD fixes it, **the flyer goes live
automatically**.

**Examples:** FD-13504 (Apple Valley Natural Foods), FD-16401 (Olive Branch).

---

## CLSD — Content Layer Service Desk (the engineering catch-all)

**What it is:** The deep **content-platform engineering** service desk. This is
where OTS sends anything needing backend investigation or a data/code fix.

**What goes here (recent sample by issue type):**
- **Investigation (~54%)** — the bulk. Examples: missing categorization
  (`CLSD-5757` "Missing categorization for 'limes' – Food Basics"), duplicate
  `publication_id`s mapping to one flyer, empty Kafka maps, **cloning/WES errors**
  (`CLSD-5766` clone into existing shell failed with "WES Error"), **store
  harmonization** (`CLSD-5759` "Harmonize stores manually — Foursquare blocking
  new venue ID"; `CLSD-5760` "RONA Store updater failing … Missing venueId"),
  tagging bugs (`CLSD-5751` "'flag item' bug in fadmin").
- **Ask (~18%)** — feature/enablement requests (e.g. bulk vendor reassignment in
  FAdmin, enabling Nexus product creation).
- **Task (~14%)**, **Data Request (~4%)**, occasional **Data Piping Error**.

**Volume:** Active — ~50/month in the recent sample.

**Typical turnaround (recent sample, ~80% resolved):**
- ~27% same day, ~44% within 3 days, ~62% within a week,
- ~17% 8–30 days, ~5% >30 days. ~20% were still open (it's a live queue).

**What to tell the requester:** "It's with the content-platform team (CLSD).
Quick investigations often close within a day or two; anything needing a code fix
or data migration can take a week-plus." **Mark urgent** if a go-live is blocked.

---

## MSC — Marketing Science / Foursquare measurement ("PIA")

**What it is:** The **MSC** project houses the analytics/measurement function
(historically keyed "PIA"). Most MSC "harmonization/Foursquare" tickets are
**advertising measurement**: Foursquare AAAS feasibility checks, store-trip
reporting, and periodic data submissions (PARF/exposure files to Foursquare).

**When OTS touches it:** For **store-trip / harmonization *reporting*** questions
(e.g. `MSC-8423` "Harmonized retailer not seeing store trips"; `MSC-8738` "Stores
weren't harmonized — can we still get trip data?"). Genuine harmonization
*failures* (like the Pet Valu false-duplicate case, `MSC-8847`, formerly
`PIA-8847`) get logged here for measurement impact but are **fixed via CLSD/HTS**.

**Typical turnaround (sample of 50):** slower/measurement-paced — mostly
**1–4 weeks** (few same-day; ~28% in a week, ~42% in 8–30 days, ~16% >30 days),
because much of it is tied to reporting periods, not incident fixes.

**What to tell the requester:** "Store-trip and Foursquare reporting is handled by
Marketing Science on a reporting cadence — expect days-to-weeks, not same-day."

---

## How to write a good escalation (so it moves faster)

Regardless of destination, include:
- **Flyer run link** (`fadmin.flippback.com/flyer_runs/<id>`) and merchant/store IDs.
- **Exact error text** and a **full-backtrace screenshot** (CLSD investigators ask
  for this every time).
- **What you already tried** (re-ran sessions/AutoBox, cloned, checked FTP, etc.).
- **Time sensitivity / go-live date** — and flag **urgent** only when a go-live is
  genuinely blocked within ~1–2 days.
- For **harmonization**: the merchant/store IDs, lat/longs, the Foursquare error
  log, and the stores flagged as duplicates.

---

*Sources: FD (Broken Indexer), CLSD (Content Layer Service Desk), and MSC
(Marketing Science / "PIA") Jira projects, samples Jan 2024–Jul 2026, incl.
FD-13504/16401, CLSD-5751/5757/5759/5760/5766, MSC-8423/8738/8847. Turnaround
figures are sample-based estimates. See `sources/source-map.md`. Last reviewed:
2026-07-14.*
