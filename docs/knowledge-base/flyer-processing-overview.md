# Flyer Processing — How It Works (Orientation)

> **What this covers:** A plain-language orientation to how flyers get processed
> and published at Flipp, and where the common failure points are. This gives
> the chatbot the context it needs to place a specific error in the bigger
> picture. Grounded in the Processing Support KB (Flex Hub), the Flyer
> Troubleshooting Guide (CX), and the Urgent Flyer Processing guide (XPTCXE).

---

## ⚠️ Source-of-truth note

The Confluence **Processing Support KB** (space FLX) is, as of **June 2026**,
**no longer maintained** — it points to the **Processing Support ClickUp space**
for the latest training and process updates. Treat the process details below as
orientation and **verify current process against ClickUp**. (Pulling that
ClickUp space into this CXE Help Center is a recommended next step — see the
session log.)

---

## The big picture

A flyer moves from a retailer's raw assets to a live, shoppable publication on
Flipp. At a high level:

1. **Assets arrive** — the retailer delivers PDFs/images to an **FTP/SFTP**
   directory, plus a **codesheet** describing how to build the flyer.
2. **Upload / build** — a processor runs the **codesheet** in **FADMIN**, which
   uploads pages, creates **pricing zones**, assigns pages to zones in order,
   assigns stores/regions, sets valid dates, and sets language.
   *(This is where most codesheet errors happen — see `codesheet-errors.md`.)*
3. **Processing sessions** — automated steps generate images/tiles/thumbnails,
   run auto-categorization, tagging, harmonization, etc.
   *(Failure points: tile generation, image import, categorization, harmonization
   — see `common-live-flyer-issues.md`.)*
4. **Final Quality Check (FQC)** — a processor verifies the run is correct before
   it goes live.
5. **Publish / go-live** — the flyer is published to storefronts.
   *(Failure points: storefront load errors, missing thumbnails, republish needs
   — see `storefront-publishing-errors.md`.)*
6. **Post-live revisions** — page swaps, price/prefix corrections, etc., which
   may require re-running sessions and republishing.

---

## Where issues get reported: the OTS board

Day-to-day flyer problems are raised on the **Ops Troubleshooting (OTS)** Jira
board (project `OTS`, board 315) as **Help Desk – Question** tickets. OTS is the
**front-line triage layer** — ops/CX resolves what it can and escalates the rest
to specialist teams (indexing → **FD**, store data → **CLSD**, hosted/front-end →
**HS**, general content → **CLSD**). The knowledge-base articles are organized
around the issue categories that show up most on this board:

- Flyer/pages/coverage missing → `missing-flyers-and-indexing.md`
- Items not clippable / boxes off → `clipping-and-autobox.md`
- Store & harmonization → `stores-and-harmonization.md`
- Wrong/expired dates → `flyer-dates.md`
- Hosted sites & preview links → `hosted-and-previews.md`
- Stuck go-live / front-end display → `publishing-and-go-live.md`

See `sources/ots-ticket-inventory.md` for the full breakdown and frequencies.

## Key concepts

- **Codesheet:** the spreadsheet that tells FADMIN how to build the flyer run
  (pages, pricing zones, order, stores/regions, dates, language). Some retailers'
  codesheets do all of this automatically; others require manual work.
- **Pricing zone (PZ):** a grouping that ties a set of pages + dates + language +
  stores/regions together. Many errors trace back to a single misconfigured PZ.
- **Config name:** identifies which processor logic runs for a retailer's
  codesheet. Some retailers have multiple configs for different purposes.
- **FADMIN:** the internal admin tool where runs are built, processed, and
  republished (`fadmin.flippback.com`).
- **FTP / SFTP:** where retailer source files live; filename and folder
  conventions matter a great deal (see codesheet errors).
- **Session:** an automated processing step on a run; "re-run sessions" is a
  common first remediation.

---

## Types of live-flyer complaints (and where they point)

From the customer-facing Flyer Troubleshooting Guide, live-issue reports usually
fall into:

- **Missing flyer** — the retailer has no live content available at that time.
  Often *not a bug*: the retailer's flyer-run cycle, or they intentionally have
  no flyer for certain locations. Indexed flyers can also take **24–48 hours** to
  be gathered and processed, and retailers sometimes release flyers late.
- **Wrong flyer** — not opening, wrong valid dates, discrepancies, blurry pages,
  items unclippable. When it's not just a processing delay, the root cause is
  usually an **error in processing/publishing on our end** and needs correction.

> **Rule of thumb:** distinguish a **processing delay** (wait / re-run) from a
> genuine **processing error** (needs a fix or a ticket).

---

## Urgent processing

Typical lead time for a flyer is **5–10 business days**. An **urgent processing**
request is for flyers that need processing **1–2 days** before going live.
Common valid reasons:
- Assets/pages were uploaded incorrectly and need redoing.
- **Reprocessing required** — the flyer was processed incorrectly and needs
  corrections.
- **Special event** — the flyer must be completed for a time-sensitive event.

See the Urgent Flyer Processing guide for the current request process and SLAs.

---

## Who does what (Processing Support)

**Processing Support ("PS")** executes key Flyer-Ops tasks (uploads, vendor
setups, FQCs, page swaps, revisions) for many retailers — more than a third of
all runs that go live pass through PS. Roles:
- **Scrum Masters (FLEX):** manage the PS board, triage requests, help with
  blockers/troubleshooting.
- **Daytime Processors (FLEX/FTE):** execute run tasks; communicate in
  `#flex-processingsupport`.
- **Overnight Processors (DSP hourly):** uploads and FQCs only; no Slack access —
  they leave notes on the ClickUp task.

Work management lives on the **PS Board** and **Retailer Info Hub** in ClickUp.
Blocked runs surface on the **Blocker Board**.

---

*Sources: Confluence "Processing Support - Knowledge Base" (FLX, 11717181547);
"Flyer Troubleshooting Guide" (CX, 2259652718); "Urgent Flyer Processing"
(XPTCXE, 3129139207). See `sources/source-map.md`. Last reviewed: 2026-07-14.*
