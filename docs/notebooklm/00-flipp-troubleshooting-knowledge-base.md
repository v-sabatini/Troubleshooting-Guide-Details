# Flipp Flyer-Processing Troubleshooting — CXE Help Center

> Combined bundle of the CXE Help Center's general troubleshooting guidance (codesheet errors, missing flyers/indexing, clipping/AutoBox, stores/harmonization, dates, hosted/previews, publishing/go-live, storefront, escalation routing, glossary). For retailer-specific processing, see the "Retailers - <letter>" bundles.

---

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


---

# Codesheet Errors — Troubleshooting Guide

> **What this covers:** The most common errors seen when uploading/processing a
> codesheet in FADMIN, what causes them, and how to fix them yourself before
> escalating. Grounded in real resolved tickets from the TOSS Jira project and
> the Codesheet Troubleshooting Guide (Confluence, space XPTCXE).
>
> **Audience:** Flyer processors and Processing Support staff.
> **Escalation path:** If self-serve steps fail, file an Ops Troubleshooting /
> CLSD ticket (see `escalation-and-tickets.md`).

---

## First, know your codesheet

Before troubleshooting, you should be able to answer these about the retailer's
codesheet. If you can't, that gap is often the root cause.

A codesheet typically does some or all of the following:
- Uploads pages to the flyer run
- Uploads pricing zones to the flyer run
- Adds pages to pricing zones **in a defined order**
- Assigns stores or regions to pricing zones
- Assigns pricing-zone dates (valid-from / valid-to)
- Assigns page / pricing-zone language

Also confirm:
- **Config name(s):** Most retailers have one, some have several (each with a
  purpose). Know them all.
- **PDF base directory & FTP structure:** How the retailer's FTP folders cascade
  (e.g. `/ → 2016 → August → Wk4 Back to School`) and their **file-naming
  convention** (is the date / name / page number in the filename?).
- **How directory separators (`/`) behave** at the start, middle, and end of the
  PDF Base Directory field.

---

## The universal self-serve checklist

Run through this before filing a ticket. It resolves the majority of cases.

1. **Compare to a known-good codesheet.** Pull last week's codesheet that ran
   cleanly for the same retailer and diff it against this week's. Most failures
   are a small change week-over-week.
2. **Check every pricing zone has the required fields:** pages assigned, a
   **valid-from and valid-to date**, and the correct language. A single row
   missing dates or pages is the #1 cause of `NilClass` errors.
3. **Check filenames match the FTP *exactly*.** Watch for:
   - trailing spaces in FTP filenames,
   - underscore vs. hyphen (`RACC701-0201_A` vs `RACC701-0201-A`),
   - trailing page-number suffixes (`..._A` vs `..._A_1`, `_A_2`).
4. **Verify the PDF Base Directory** is correct (a wrong or extra `/` breaks
   file lookup).
5. **Re-save the CSV cleanly** (a corrupted export can cause parse errors).
6. **Fallback:** If you still can't find it, use the **Generic Codesheet** to
   create zones, assign stores, and upload pages manually so the run isn't
   blocked, then file a ticket for the root cause.

---

## Error catalog

Each entry lists the **symptom** (what you see), the **likely cause(s)**, the
**fix**, and the **source ticket** for reference.

### 1. `NilClass` errors

**Symptom — exact error text varies, e.g.:**
- `undefined method 'split' for nil:NilClass`
- `undefined method 'gsub' for nil:NilClass`
- `undefined method 'size' for nil:NilClass`
- `undefined method 'extract_name' for nil:NilClass`
- `no implicit conversion of nil into String`

**What it means:** The processor tried to use a value that turned out to be
empty (`nil`) — almost always because a field the codesheet expected is blank,
or a file it expected to find wasn't there.

**Likely causes & fixes (check in this order):**

| Cause | How to confirm | Fix |
|---|---|---|
| A pricing-zone row is **missing start/end dates** | Scan the codesheet row-by-row for blank valid-from/valid-to cells | Fill in the missing dates and re-run *(TOSS-7033: the culprit was line 131 with no start or end dates)* |
| **PDF base path mistake** + a pricing zone has **no pages** in the CSV | Verify the PDF Base Directory; confirm every PZ has at least one page | Correct the base path and add the missing pages *(TOSS-7012)* |
| A referenced **file was renamed on the FTP** (so lookup returns nil) | Compare filenames in the codesheet to what's actually on the FTP | Ask Ops to rename/resync the file to match, **or** update the codesheet to the new name *(TOSS-7020: a file changed from `FLAP` to `FD`)* |

**Best practice when filing:** attach the failing codesheet **and** a
previously-working one, plus a screenshot of the **full error backtrace** (not
just the top line) and both the FADMIN and pipeline backups. Support asks for
these every time.

---

### 2. File is on the FTP but "not being picked up" / "file not found"

**Symptom:** The codesheet errors saying a file can't be found, or it runs
"successfully" but silently skips pages that are present on the FTP.

**Likely causes & fixes:**

| Cause | Example | Fix |
|---|---|---|
| **Trailing space** in the FTP filename | A `%` appears appended to the directory; file `..._01_00X11.p1.pdf ` has a hidden trailing space | Remove the trailing space from the FTP file(s); often many files in the folder share the problem *(TOSS-494)* |
| **Delimiter mismatch** (underscore vs hyphen) | Codesheet has `RACC701-0201_A`, FTP has `RACC701-0201-A` | Make them identical — replace all instances in the codesheet (or FTP) *(TOSS-7042 / TOSS-7043)* |
| **Trailing page numbers** not accounted for | Codesheet references `RACC701_0201_A_`; FTP has `..._A_1`, `_A_2`, `_A_3` | Update the codesheet so it matches how pages are actually numbered *(TOSS-7042)* |
| **Week number in the path collides with page-number matching** | `Wk03` / `WK01` in the file path gets read as page "3" or "1" | Known processor bug — fix is to match the page number from the **start of the filename**. File a ticket referencing TOSS-7029 / TOSS-7030 |
| **New-year rollover** | `WK55` becomes `WK01`, `WK02`… which then match against page numbers | Same class of issue as above *(TOSS-7030)* |
| **Version-name substring collision** | Looking for `_N` returns both `_NFA_N` and `_NFA_M` | Known processor bug; the fix narrows the match. Reference TOSS-7029 |

> **Tip:** If the run "completes with no error" but pages are missing, it's
> almost always one of the filename-matching causes above. Spot-check that every
> page in the codesheet actually landed in the flyer run.

---

### 3. New versions / pricing zones "throwing the config"

**Symptom:** A previously-stable retailer suddenly errors because new ad
**versions or pricing zones** appeared that the config doesn't recognize (common
with QC ECF / regional versions).

**Fix:**
- **Add the new pricing zones to the config.** This is usually a code change to
  the config processor (handled via the `wishabi/fadmin` repo by the CI/dev
  team), so file a ticket listing the exact new pricing-zone names to add
  *(TOSS-7059, TOSS-6360)*.
- **Immediate workaround:** Remove the erroring pricing zones from FADMIN and
  re-run the codesheet so the rest of the run can proceed *(TOSS-7027, SDM)*.
- Watch for **inconsistent zone names** across tabs — if the food-tab zone names
  don't match the rest, normalize them.

---

### 4. Word bank / exception errors

**Symptom:** Error referencing a pricing zone / value that needs an exception
(e.g. `ONT + OPT` not matching the expected zone name).

**Fix:**
- The value likely needs to be **added to the word bank / exception list** in
  the processor (code change — file a ticket).
- **Workaround:** Remove the erroring pricing zone(s) from FADMIN and re-run
  *(TOSS-7027)*.

---

## When to escalate

File an **Ops Troubleshooting / CLSD ticket** when:
- You've compared to a working codesheet and checked all fields, filenames, and
  the PDF base directory, and still can't find the cause.
- The fix requires a **processor/config code change** (new pricing zones, word
  bank exceptions, filename-matching bugs).

Include: the failing codesheet, a previously-working codesheet, a full
error-backtrace screenshot, the flyer-run link, and FADMIN + pipeline backups.
See `escalation-and-tickets.md` for the full ticketing guide.

---

*Sources: Confluence "Code sheet Troubleshooting Guide" (XPTCXE, 3129146347);
TOSS Jira tickets 494, 6360, 7012, 7020, 7027, 7029, 7030, 7033, 7042, 7043,
7059. See `sources/source-map.md`. Last reviewed: 2026-07-14.*


---

# Missing Flyers, Indexing & Coverage — Troubleshooting Guide

> **What this covers:** The single most common category on the Ops
> Troubleshooting (OTS) board — a flyer, page, or region's coverage is missing
> or not appearing where expected. Grounded in ~120 real OTS Help Desk tickets
> (Jan 2024–Jul 2026).
>
> **Audience:** Flyer-ops / CX staff triaging "flyer missing" reports.
> **Golden rule:** First decide **delay vs. defect**. Much of the time the flyer
> is simply still processing or the retailer hasn't released it yet.

---

## Quick triage

1. **Is it a timing issue?** A new flyer can still be **processing**, or the old
   one just **expired** and the new one isn't live yet. Indexed flyers can take
   **24–48 hours**. If the PDF's own dates start in the future, that's expected —
   wait. *(e.g. OTS-1985: zip in the distro, new flyer still processing → resolved
   as expected; OTS-1929: retailer had no newer flyer → closed.)*
2. **Does the retailer actually have the content?** Sometimes the missing pages
   simply **aren't in the retailer's PDF/source**, so they can't be added
   *(OTS-1944)*. Confirm against the source before escalating.
3. **If it's genuinely not indexing → it's usually a broken indexer** (see below).

---

## Cause 1 — Broken indexer (the most common root cause)

**Symptom:** An indexed retailer's flyer isn't appearing at all, past the normal
processing window. Titles like "Flyer Missing", "broken indexer", "not indexed".

**What's happening:** The automated **indexer** that scrapes the retailer's flyer
has broken — often because the retailer changed their site, the **starting URL is
wrong**, or the **wrong dates are being scraped** (which can cause the indexer to
be disabled).

**Fix / escalation:**
- File a **broken-indexer ticket in the FD project** (the indexing/feed team;
  Jira board 312). This is the standard, repeated resolution.
  *(OTS-1928 → FD-13520; OTS-1930 → FD-13586; OTS-1931; OTS-1960; OTS-1975 →
  FD-13813 to fix the starting URL; OTS-1963 indexer re-enabled after wrong-date
  disable.)*
- Once FD fixes the indexer, **the flyer goes live automatically** — verify and
  close. *(OTS-1939, OTS-1960: "The indexer has been fixed and the flyer is now
  live.")*

> **Tip:** Before filing, search the FD board for the retailer — an FD ticket may
> already exist *(OTS-1939 found an existing FD-13537)*.

---

## Cause 2 — Missing FSA / postal coverage

**Symptom:** The flyer exists, but a specific **FSA** (Forward Sortation
Area — the first 3 characters of a Canadian postal code) or ZIP shows no flyer.
Titles like "FSA Missing".

**Fix:**
- Confirm the postal/ZIP is in the flyer's **distribution (distro)**. If the new
  flyer is still processing, the coverage will appear once it finishes
  *(OTS-1985)*.
- If the FSA/ZIP genuinely isn't covered, it's a **store/distro coverage gap** —
  check store assignments and pricing-zone/region coverage; escalate if the
  mapping needs a data fix.

---

## Cause 3 — Wrong-region targeting (geo-targeting)

**Symptom:** Postal codes see **the wrong location's flyer** — e.g. Calgary
postal codes see the Edmonton flyer, BC codes see the Alberta flyer, Barrie codes
see the Aurora flyer.
*(OTS-1959, OTS-1969, OTS-1997, OTS-1986: Virginia ZIPs seeing the wrong flyer.)*

**What's happening:** Store-to-flyer / postal-to-zone mapping is assigning the
wrong flyer run to those postal codes.

**Fix:**
- Check which **pricing zone / store group** those postal codes are mapped to and
  correct the assignment so the right flyer serves the right region.
- If store location data is at fault, this overlaps with harmonization — see
  `stores-and-harmonization.md` (escalate store-data issues to **CLSD**).

---

## Cause 4 — Pages missing a track ID / processing blocked

**Symptom:** Specific pages don't appear; processing is blocked because a page is
**missing a track ID**, so it's excluded from tile-generation sessions.
*(OTS-1954: re-running tile gen didn't help because untracked pages are excluded.)*

**Fix:** This needs the pages correctly tracked before tile gen will include them;
escalate if you can't assign the track ID yourself.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Broken indexer / wrong scraping URL or dates | **FD** project (indexing/feed team, board 312) |
| Store/postal coverage or location data wrong | **CLSD** (harmonization fix) — see stores article |
| General content escalation / can't self-resolve | **CLSD** |
| Third-party app (e.g. PC Optimum), not Flipp-hosted | Account team (via DOC) |

Always include the flyer run link, the affected postal code(s)/region, and
whether a new flyer is still processing.

---

*Sources: OTS (Ops Troubleshooting) Jira board 315, ~120 tickets Jan 2024–Jul
2026, incl. OTS-1927/1928/1929/1930/1931/1939/1944/1954/1959/1960/1963/1969/1975/
1985/1986/1997. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*


---

# Clipping, AutoBox & Cutouts — Troubleshooting Guide

> **What this covers:** Items that can't be clipped, boxes drawn in the wrong
> place, and cutout-generation failures. ~30 real OTS tickets.
>
> **Audience:** Flyer-ops / CX staff. Most of these are self-resolvable by
> re-running the box/tag steps.

---

## Background

For a flyer to be "clippable," each item needs a **box** drawn around it (so users
can clip it) and a **tag** (item data). **AutoBox** (the "auto box draw" task)
automatically draws these boxes, and completing it kicks off **auto tag**. When
AutoBox misjudges a flyer's layout, items end up unclippable or boxes land
off-center.

---

## Issue: Flyer / items not clippable

**Symptom:** A live flyer can't be clipped, or only some items are clippable.
Titles like "Not Clippable", "some items not clippable".

**Likely cause:** The **AutoBox draw ran poorly** (struggled with the flyer's
formatting), or the flyer was **still processing**.

**Fix (try in order):**
1. **Re-run AutoBox** ("auto box"). This re-draws boxes and **kicks off auto
   tag**; it typically reflects online **within about an hour**.
   *(OTS-1934: "Re-ran auto box which kicked off auto tag!")*
2. **Manually box** the items AutoBox missed — those become clippable immediately.
   *(OTS-2020: "AutoBox ran poorly, I've boxed what was missed so those are now
   clippable.")*
3. If it's a **top-50 indexed retailer** (full tagging) and recently uploaded, it
   may simply still be processing — re-check later. *(OTS-2037.)*

**If it keeps happening for a retailer:** flag it — AutoBox may be consistently
struggling with that flyer's format and needs a closer look / next steps
*(OTS-1984, OTS-1979).*

---

## Issue: Box draw off-center

**Symptom:** Boxes are drawn but **off-center** / misaligned, sometimes only on a
specific page. Titles like "Box Draw Off-Center on Second Page".
*(OTS-1941, OTS-1943.)*

**Fix:** Re-run AutoBox; if it persists, manually adjust the boxes. Repeated
off-center draws on the same retailer indicate an AutoBox tuning issue worth
escalating.

---

## Issue: Item cutout generation failing / blocked

**Symptom:** Item **cutout images** fail to generate or are blocked. Titles like
"Item Cutout Gen Failing", "Item Cutout Generation Blocked".
*(OTS-1936, OTS-1981, and Hy-Vee cutout blocked.)*

**Fix:** Re-run the cutout/image generation step. If it stays blocked, escalate
(often a processing/pipeline issue) via **CLSD** — include the flyer run and the
specific items.

---

## When to escalate

- You've re-run AutoBox and manually boxed, and items still won't clip or tag.
- Cutout generation stays blocked after a re-run.
- The same retailer repeatedly breaks AutoBox (needs a tuning fix).

Escalate via **CLSD** with the flyer run link and example item(s).

---

*Sources: OTS Jira board 315, incl. OTS-1934/1935/1936/1941/1943/1979/1981/1984/
2005/2020/2037. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*


---

# Stores & Harmonization — Troubleshooting Guide

> **What this covers:** Store harmonization failures/audits, duplicate or missing
> stores, "store not appearing," and add-store errors. ~29 real OTS tickets.
>
> **Audience:** Flyer-ops / CX staff. Store *location data* issues escalate to
> **CLSD** (with measurement tracked in **MSC**/"PIA"); most audits are resolvable by fixing lat/long or confirming
> with the retailer.

---

## Background

**Harmonization** matches a merchant's stores to the canonical store/location
dataset (4Square) so flyers target the right physical locations. When a store
fails to harmonize, or two stores look like duplicates, targeting breaks.

---

## Issue: Store failing harmonization / false duplicate

**Symptom:** Stores won't harmonize, often flagged as a **false duplicate**, or
"stores already harmonized" errors. Titles like "36 Stores Failing Harmonization
with False Duplicate Store".

**Fix (try in order):**
1. **Update the lat/long** for stores whose coordinates are too similar, then
   **re-harmonize**. *(OTS-2025: "updated the lat/longs that were similar and
   harmonized the stores.")*
2. If stores look like duplicates, **confirm with the retailer** whether they're
   genuinely distinct — the retailer may confirm duplicates are correct and
   provide closures/address updates to apply in FADMIN. *(OTS-2024, Wellwise SDM.)*
3. If it's a genuine store-data problem you can't fix, **escalate to CLSD**
   (where harmonization fixes are actually worked — e.g. "Foursquare blocking new
   venue ID," store-updater `venueId` errors). The measurement/store-trip side is
   tracked in **MSC** (Marketing Science, the analytics "PIA" function).
   *(OTS-2002 → MSC-8847 [link shows as `PIA-8847`], which referenced HTS-25 and
   CLSD-3483 for the fix.)* See `post-escalation-what-happens-next.md`.

---

## Issue: Harmonization Audit tickets

**Symptom:** Tickets titled "Harmonization Audit: <retailer>" — a periodic check
of a retailer's store data.

**Fix / process:**
- Work through the flagged stores: fix lat/longs, apply retailer-confirmed
  closures/address changes in FADMIN, and note the resolution on the ticket.
- Escalate anything requiring canonical dataset changes to **CLSD**.

---

## Issue: Store not appearing / can't add a store

**Symptoms & fixes:**
- **Grand-opening / new store not appearing on hosted** *(OTS-2056, Lidl US)* —
  verify the store is added, harmonized, and assigned to the live flyer run.
- **"Merchant store code already taken" when adding a store** even though a search
  shows it unused *(OTS-2053)* — a data conflict; escalate to CLSD with the store
  code and merchant.
- **Store not appearing on a third-party app** (e.g. Loblaws on PC Optimum)
  *(OTS-1967)* — if it's a third-party app and **not Flipp-hosted**, it's out of
  our scope; route to the **account team** (escalated via DOC).

---

## Issue: Items showing as "In-Store Only"

**Symptom:** All items in a flyer show as "In-Store Only" incorrectly
*(OTS-1991, Sportsman's Warehouse)*.

**Fix:** This was resolved by a **Hosted-team fix** — escalate to the Hosted team
if item availability/flags are wrong system-wide rather than per-item.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Store harmonization failure / can't be fixed locally | **CLSD** (fix); measurement tracked in **MSC**/"PIA" |
| Store code conflicts / canonical data | **CLSD** |
| Item availability flags wrong (In-Store Only, etc.) | **Hosted team (HS)** |
| Third-party app display (not Flipp-hosted) | Account team (via DOC) |

> **Routing note:** Older tickets show harmonization escalated to "PIA" links —
> these resolve to **MSC** (Marketing Science / measurement). The actual **fix**
> happens in **CLSD**. See `post-escalation-what-happens-next.md`.

Include the merchant, store code(s), lat/long, and flyer run link.

---

*Sources: OTS Jira board 315, incl. OTS-1967/1982/1991/2002/2009/2024/2025/2035/
2053/2056. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*


---

# Flyer Dates — Wrong, Expired & Invalid Valid Dates

> **What this covers:** Flyers showing the wrong valid dates, expired flyers still
> visible (or live flyers showing as expired), and item-level date issues. ~23
> real OTS tickets. **Most of these are self-resolvable in FADMIN.**
>
> **Audience:** Flyer-ops / CX staff.

---

## Background

Every flyer run and pricing zone has **valid-from / valid-to** dates that control
when it's live and when it expires. Most date complaints are fixed by correcting
these dates on the flyer run in FADMIN — no escalation needed.

---

## Issue: Wrong valid dates

**Symptom:** The flyer's valid dates are wrong — e.g. ends on the wrong day of the
week (Thurs–Thurs instead of Thurs–Wed). *(OTS-1932, OTS-1993, OTS-2068.)*

**Fix:** Edit the **valid-to (end) date** (and/or valid-from) on the flyer run in
FADMIN to the correct date and save. *(OTS-1932: "updated dates to end on Jan 17";
OTS-1993: "fixed the valid dates and the flyer is now live"; OTS-2068: "Dates
updated in fadmin to end 09/11".)*

---

## Issue: Expired flyer still visible

**Symptom:** An expired flyer is still showing on the front-end. *(OTS-1972,
OTS-2074.)*

**Fix:** **Backdate** the expired flyer's dates so it drops off. *(OTS-1972: "I've
backdated the expired flyers.")*

---

## Issue: Live flyer showing as expired / not available yet

**Symptom:** A flyer that should be live reads as expired, or isn't available
because its start date is off. *(OTS-2029, Farm and Spice.)*

**Fix:** Update the flyer run's **valid-from** date to the correct availability
date and save. *(OTS-2029: "updated dates on flyer run to reflect avail from Aug 5".)*

---

## Issue: Item-level valid dates not showing correctly

**Symptom:** Item valid dates display incorrectly even when the flyer run looks
right. *(OTS-2069, Calgary Co-op.)*

**Fix:** Check item/pricing-zone-level date overrides in addition to the run-level
dates; correct the level where the wrong date is set.

---

## Escalation

Date issues rarely need escalation — they're a FADMIN edit. Escalate via **CLSD**
only if the dates look correct in FADMIN but the front-end still shows wrong
dates after processing (possible caching/pipeline issue).

---

*Sources: OTS Jira board 315, incl. OTS-1932/1972/1993/2029/2068/2069/2074. See
`sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*


---

# Hosted Sites & Preview Links — Troubleshooting Guide

> **What this covers:** Preview links that don't work, Hosted (retailer-embedded)
> flyers not loading, iframe issues, and pages rendering cropped/incorrectly.
> ~15+ real OTS tickets. These frequently escalate to the **Hosted team (HS)**.
>
> **Audience:** Flyer-ops / CX staff triaging retailer/preview-link complaints.

---

## Background

**Hosted** is the retailer-embedded flyer experience (e.g. a flyer shown in an
iframe on the retailer's own website). **Preview links** let internal/external
folks view a flyer before or around go-live. Both depend on the flyer being fully
processed and correctly published.

---

## Issue: Preview links not working

**Symptom:** Preview links don't open, show the wrong flyer, "This site can't be
reached," or a full-screen preview isn't interactive. *(OTS-1961, OTS-1973,
OTS-1980, OTS-1995, OTS-2012.)*

**Try first:**
- Confirm the flyer is **actually live / fully processed** — previews for a flyer
  that isn't live yet (or is stuck pre-live) won't work. See
  `publishing-and-go-live.md`.
- Regenerate/copy the preview link fresh and confirm you're using the correct
  flyer run.

**If still broken:** escalate to the **Hosted team (HS)** with the flyer run and
the exact preview URL.

> **Note:** Providing a direct link to a **not-yet-live** flyer as a workaround is
> generally **not** advised — previews aren't meant for that use and it carries
> risk. *(OTS-1988: workaround declined for this reason.)*

---

## Issue: Hosted flyer not appearing / not loading

**Symptom:** A live flyer isn't appearing on the retailer's Hosted site, the
iframe won't load, or vertical previews can't be seen. *(OTS-1992 [urgent],
OTS-1971, "Cannot See Vertical Previews".)*

**Try first:** Confirm the flyer is live and Ops-complete (not stuck in
"preview ready" — see `publishing-and-go-live.md`).

**If still broken:** escalate to the **Hosted team (HS)** (e.g. OTS-1971 →
HS-3281). Mark **urgent** if it's a live flyer not appearing on the retailer site.

---

## Issue: Pages cropped / cut off / not rendering

**Symptom:** Flyer pages load but appear **cropped, cut off, or half-rendered**,
or certain pages don't display. *(OTS-1968 RCSS; OTS-1966 Tepperman's.)*

**Fix:** Re-run **page stitching** and **republish**. *(OTS-1966: "re-ran page
stitching and republished.")* If it persists, escalate to the Hosted team.

---

## Issue: Links/redirects wrong on Hosted only

**Symptom:** A page link doesn't redirect correctly, or item links don't reflect
— **on Hosted only** (fine on Flipp). *(OTS-1962, OTS-2012.)*

**Fix:** Since it's Hosted-specific, escalate to the **Hosted team (HS)** with the
specific links and where they should point.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Preview/iframe/Hosted rendering after confirming flyer is live | **Hosted team (HS)** |
| Page stitching didn't fix cropped pages | **Hosted team (HS)** |
| Flyer isn't live yet (root cause is publishing) | See `publishing-and-go-live.md` |

Always confirm live/processed status **before** escalating — many preview issues
are really "the flyer isn't live yet."

---

*Sources: OTS Jira board 315, incl. OTS-1961/1962/1966/1968/1971/1973/1980/1988/
1992/1995/2012. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*


---

# Publishing, Go-Live & Front-End Display — Troubleshooting Guide

> **What this covers:** Flyers stuck before go-live, pipelines/cloning stuck,
> FQC/pipeline not generating, and front-end display problems (prices/text/items
> not showing). ~40 real OTS tickets across "publishing/go-live" and "front-end
> display."
>
> **Audience:** Flyer-ops / CX staff. Stuck-pipeline and go-live blockers often
> escalate to **CLSD**; several have known self-serve fixes (clone / re-save /
> toggle).

---

## Part A — Flyer stuck before go-live

### Issue: Flyer not live / sessions won't run / stuck in "preview ready"

**Symptom:** A flyer won't go live; sessions won't run to allow a FADMIN publish;
the run is stuck in **"preview ready"** instead of **"Ops complete."** *(OTS-1982,
OTS-1992, OTS-2048 "flyer stuck", OTS-2060 "flyer blocked".)*

**Fix (try in order):**
1. **Clone the run / re-process under a different flyer run.** This is the
   repeated fix for a run stuck between states. *(OTS-1992: "Cloning run resolved
   the issue — original run was stuck in 'preview ready' rather than 'Ops
   complete.' CLSD filed to find source." OTS-1982: "Resolved by re-processing the
   flyer under a different flyer run.")*
2. If cloning resolves it but you don't know **why** it got stuck, **file a CLSD**
   so the source can be investigated.

### Issue: Cloning pipeline stuck / clone erroring out

**Symptom:** A clone's pipeline is stuck, a clone errors out consistently, or a
clone doesn't show Vendor/System/Ops tasks. *(OTS-1938, OTS-2006, OTS-2030.)*

**Fix:** Retry the clone; if it consistently errors, **escalate to CLSD** with the
flyer run link and the error. Note the due date if time-sensitive.

### Issue: Pipeline stuck / missing slices / FQC page not accessible

**Symptom:** Flyer pipelines are stuck, slices are missing, or the FQC page/
pipeline won't generate so FQC can't be marked off. *(OTS-2047, OTS-2027,
OTS-2064: "not generating pipeline to mark off FQC".)*

**Fix:** These block go-live and usually need backend help — **escalate to CLSD**
(mark **urgent** if going live imminently). *(OTS-2064 → CLSD-4634.)*

---

## Part B — Front-end display problems

### Issue: Price / pre-price / sale text not showing on Flipp

**Symptom:** Item pre-price, price, or sale-story text isn't displaying (often
**Flipp-only**). *(OTS-1978, Safeway NOW & Health & Beauty.)*

**Fix:** Check the **flyer type / "simp pop" (simple pop) toggle** — if the flyer
type is set to simp pop, item details are suppressed. **Turn the simp pop toggle
off** and details reappear. *(OTS-1978: "Flyer types were set to simp pop. After
turning this toggle off, item details were showing on Flipp.")*

### Issue: New boxes / items / links not reflecting on front-end

**Symptom:** Newly created boxes, items, or links don't show on the front-end or
in vertical preview. *(OTS-1971, OTS-1974.)*

**Fix:**
- First rule out a **false alarm** (still processing / caching) — some of these
  self-resolve *(OTS-1974 turned out to be a false issue)*.
- If new items/links genuinely won't reflect, escalate to the **Hosted team (HS)**
  *(OTS-1971 → HS-3281)*.

### Issue: Future flyers not showing in workflow

**Symptom:** Workflow execution isn't showing future flyers. *(OTS-1964,
Metropolitan Market.)*

**Fix:** **Re-save the flyer run** — open **edit details and save without making
changes**. This nudged the run to appear. *(OTS-1964.)*

### Issue: Item title appears as "Null"

**Symptom:** A flyer item title shows literally as **"Null"**. *(OTS-1998, Ingles
Market.)*

**Fix:** Correct the item's title/data in FADMIN; if it's generated data coming
through empty, escalate with the item reference.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Stuck pipeline / clone errors / FQC won't generate | **CLSD** (urgent if going live soon) |
| New items/links won't reflect on front-end (after ruling out processing) | **Hosted team (HS)** |
| Root cause is the flyer isn't live | Fix go-live first (Part A) |

Always include: flyer run link, current status/state, due date, and what you tried
(clone, re-save, toggle).

---

*Sources: OTS Jira board 315, incl. OTS-1938/1964/1971/1974/1978/1982/1992/1998/
2006/2027/2030/2047/2048/2060/2064. See `sources/ots-ticket-inventory.md`. Last
reviewed: 2026-07-14.*


---

# Common Live-Flyer & Processing Issues — Quick Reference

> **What this covers:** The recurring issues flyer processors actually raise in
> `#helpme-ops` (to the Enablement pod / `@enable-cxe`), the standard things to
> try first, and when to file a CLSD ticket. This is grounded in real Slack
> help-desk threads and is meant to capture the "what do I try first?" instinct
> that experienced processors have.
>
> **The universal remediation loop:** for most live-flyer issues the first
> attempts are: **re-run the relevant session(s) → republish → wait a short
> time for processing → if still broken, file a CLSD ticket to unblock.**

---

## How to read this page

Each issue below follows the same shape:
- **Symptom** — what the processor sees
- **Try first** — self-serve steps
- **If still broken** — escalation

Always include the **flyer run ID and link** (e.g.
`fadmin.flippback.com/flyer_runs/<id>`) when asking for help or filing a ticket.

---

## Flyer tile generation error

- **Symptom:** A flyer run consistently gets a *flyer tile generation error*;
  it blocks completing the Final QC checklist.
- **Try first:** Re-run the tile/thumbnail generation session; wait to give
  processing time to work through the queue; confirm required upstream steps
  completed.
- **If still broken:** File an **urgent CLSD** to unblock (especially if it's
  stopping Final QC before go-live).

## Image import problems (inverted / missing images)

- **Symptom:** Imported images are **inverted and unusable**, or images aren't
  generated for all pages/items despite clean PNGs in the staging area.
- **Try first:** Check the **folder structure of the source files** — a
  **sub-folder within a folder** can break the import logic. Flatten/correct the
  structure and re-import. Confirm the PNGs are truly clean and in the expected
  location.
- **If still broken:** Escalate with examples of the affected pages/items and
  the folder layout.

## Stale pricing / prefix still showing on the front-end

- **Symptom:** An old price prefix or price still shows on the front-end after
  being changed in FADMIN before go-live.
- **Try first:** Save a random pre-fix → remove it → save again (to force a
  change); **re-run all sessions**; **republish**.
- **If still broken:** File a CLSD ticket with the flyer link and screenshots
  showing the live experience vs. the corrected tagging in FADMIN.

## Item pop / prefix won't remove

- **Symptom:** A prefix appears in the item-search preview but disappears once
  the item is selected, so it **can't be removed** even though the retailer
  requested removal. Often isolated to specific items.
- **Try first:** Identify exactly which items are affected; re-run sessions.
- **If still broken:** Escalate with the flyer run ID(s) and the specific item
  IDs.

## Auto-categorization gaps (missing Google categories)

- **Symptom:** Some **Google Categories are missing** after auto-categorization;
  tag QC gets stuck.
- **Try first:** Re-run sessions to see if categories populate. Share a list of
  affected items.
- **If still broken:** File a **CLSD** ticket for auto-categorization failure
  (this is a known escalation path); note if pages are going live soon so it can
  be prioritized/bumped.

## Store harmonization failure (4Square)

- **Symptom:** A store won't **harmonize with 4Square**.
- **Try first:**
  1. Update the store's lat/long, then re-harmonize.
  2. Delete and re-add the store, then re-harmonize.
- **If still broken:** Forward any harmonization-failure error messages and file
  a CLSD ticket (there's a dedicated place to file harmonization error tickets).

## Masthead not showing on the front-end

- **Symptom:** A masthead isn't appearing on the front-end (often time-sensitive
  when promo $$ is attached).
- **Try first:** Re-run the session; confirm the masthead was added to
  **Storefront Premium** and **Storefront Carousel Premium**; confirm the flyer
  ID that budget was assigned to is correct.
- **If still broken:** File a ticket with the flyer run and flyer ID.

---

## Who to contact

- Post in **`#helpme-ops`** and tag **`@enable-cxe`** (the Enablement pod, which
  absorbed the former Skeleton Team's support function).
- For **Processing Support** retailer/run questions, use
  **`#flex-processingsupport`** and tag **`@psflex`**.
- Don't troubleshoot flyer-run issues in DMs — keep it in the help channels so
  others have visibility and can jump in.

---

*Sources: `#helpme-ops` Slack help-desk threads (2025–2026); cross-referenced
with the Processing Support KB and Storefront runbook. See
`sources/source-map.md`. Last reviewed: 2026-07-14. Some remediation steps are
distilled from how issues were actually resolved in-thread — verify against
current SOPs.*


---

# Storefront & Publishing Errors — Troubleshooting Guide

> **What this covers:** How to triage Storefront load failures and
> publishing/republish issues. Grounded in the "How to troubleshoot Storefront
> errors" runbook (Confluence, space QKB) and the Live Flyer Check alert runbook
> (space CTLR).
>
> **Note on audience:** This area is more engineering / on-call oriented than
> codesheet or day-to-day processing. Some steps require VPN, SSO, and access to
> Datadog, Databricks, and Lenses. If you don't have that access, your job is to
> **identify and clearly report** the affected merchant / flyer run, then hand
> off. See `escalation-and-tickets.md`.

---

## Problem: "Storefront errors exceed healthy threshold"

**Symptom / how it shows up:**
- A **Datadog alert**: *Storefront errors exceed healthy threshold* — meaning
  storefronts are failing to load for one or more merchants.
- Teams reporting in Slack that a storefront won't load.

**Goal of troubleshooting:** find the **affected merchant** and **flyer run ID**,
then decide whether a **republish** is needed.

### Step-by-step

1. **Check `#sf-auditor-alerts` in Slack.** This channel reports publications
   that were expected but haven't published yet.
   - If there's an issue, it reports the `flyer_id` and `flyer_run_id`, in a path
     like `storefronts/v2/<flyer_run_id>/<flyer_id>/...`.
   - If all is well, you'll see: `Audit completed. 0 inaccessible publications found.`

2. **Find the Merchant ID:**
   - Fastest: use the Datadog **App Storefront Errors** monitor/dashboard to see
     which merchant has the most errors (narrow the time window as needed).
   - Alternative: the **Databricks** dashboard (second table) — you may need to
     set the interval to the last 12 hours (Databricks has ingestion lag) and
     ensure the data is refreshed.
   - Whichever merchant shows the highest error count is your prime suspect.

3. **Query beacons in Lenses (Production):** (requires VPN + SSO)
   - Go to <https://lenses.flipp.com/> → Explore.
   - Query beacon `Beacon.FlippApp.StorefrontZeroCaseError`, filtered by the
     `merchantId` from step 2. Example:
     ```sql
     USE `kafka`;
     SELECT *
     FROM Beacon.FlippApp.StorefrontZeroCaseError
     WHERE merchant.merchantId = "2178"
       AND _meta.timestamp > now() - (1hour)
     LIMIT 100;
     ```
   - Switch to Table view. In the error-details column you may see
     `Unable to retrieve SFML error 1`.

4. **Narrow to a flyer run / flyer:** find the specific flyer run or flyer with
   the most errors. Reproduce it on your device using the associated **postal
   code** (available as a column in the query results).

5. **Decide on a republish:** once the `flyer_run_id` is isolated, coordinate
   with the team on whether a **republish on FADMIN** is required.

**Need historical data?** Use the Databricks **Storefront 0 Case Notebook** —
enter the `merchant_id` in the Retailer field, run it, and see "Output 3:
Selected merchants" for the total error count and flyer IDs.

---

## Live Flyer Check (alert runbook)

**Symptom:** an alert that a live flyer isn't behaving — not opening, missing
thumbnails, or not fully processed.

**Common root causes seen in the runbook:**
- **Flyer wasn't finished processing** → message `#content-public` to complete /
  republish.
- **Flyer thumbnails don't exist** in the `Flyers.Thumbnails` topic → message
  `#content-public` to republish the flyer.

**Actions:**
- Check the flyer IDs in the pricing zones for errors on the merchants flyer-runs
  admin.
- Trigger a **republish flyer run** when processing didn't complete or thumbnails
  are missing.

---

## When to escalate

- If you don't have Datadog / Databricks / Lenses access, report the **merchant
  ID and flyer run ID** (and, if you have it, the beacon error detail) to the
  content/on-call team via the appropriate channel and file a **CLSD ticket** if
  it's blocking go-live.
- Storefront-wide failures affecting many merchants are a production incident —
  escalate immediately rather than working ticket-by-ticket.

---

*Sources: Confluence "How to troubleshoot Storefront errors" (QKB, 11540496444);
"Alert Runbook: Live Flyer Check" (CTLR, 11691786294). See
`sources/source-map.md`. Last reviewed: 2026-07-14.*


---

# Escalation & Ticketing — When Self-Serve Isn't Enough

> **What this covers:** When and how to escalate a flyer-processing problem, what
> to include so it gets resolved fast, and who owns what. Grounded in the
> codesheet & data-piping troubleshooting guides, the Processing Support KB, and
> `#helpme-ops` practice.

---

## Decision guide: fix it, wait, or file a ticket?

1. **Is it a delay or an error?**
   - Indexed flyers can take **24–48 hours** to process; retailers sometimes
     release late. If it's a delay, **wait / re-run** before escalating.
2. **Have you run the self-serve checklist for that error type?**
   - Codesheet → `codesheet-errors.md`
   - Live-flyer issue → `common-live-flyer-issues.md`
   - Storefront → `storefront-publishing-errors.md`
3. **Does the fix require a code/config change or access you don't have?**
   (new pricing zones, word-bank exceptions, filename-matching bugs, backend
   beacon queries) → **file a ticket.**
4. **Is it blocking a go-live within 1–2 days?** → mark it **urgent** and say so.

---

## Where to ask first (Slack)

- **`#helpme-ops`** — general flyer-ops troubleshooting. Tag **`@enable-cxe`**
  (the **Enablement pod** — the team that absorbed the former Skeleton Team's
  support function; includes Vanessa, Kayla, Han…).
- **`#flex-processingsupport`** — Processing Support retailer/run questions; tag
  **`@psflex`** (the on-shift Scrum Master).
- **`#helpme-flex`** — higher-level PS process / onboarding / retailer-change
  questions; tag **`@flex`**.
- **`#sf-auditor-alerts`** — storefront publishing audit alerts.
- **`#content-public`** — republish / thumbnail / processing-completion asks
  (per the Live Flyer Check runbook).

> Keep troubleshooting **in channels, not DMs**, so others have visibility and
> can help.

---

## The Ops Troubleshooting (OTS) board — the front line

Most day-to-day flyer issues are raised as **Help Desk – Question** tickets on the
**Ops Troubleshooting (OTS)** Jira board (project `OTS`, board 315). OTS is the
**triage layer**: the ops/CX team resolves what they can directly and **escalates
the rest to the specialist team's project**. Knowing where each issue type goes is
half the battle:

| If the root cause is… | Escalate to project | Notes |
|---|---|---|
| **Broken indexer** / wrong scraping URL or dates (flyer not indexing) | **FD** (indexing/feed team, board 312) | By far the most common escalation for "flyer missing" |
| **Store location / harmonization data** (duplicates, lat/long, coverage) | **CLSD** (fix); **MSC** for trip/measurement | "PIA" links resolve to MSC; the fix is worked in CLSD |
| **Hosted site / iframe / preview / front-end rendering** | **HS** (Hosted team, board 67) | After confirming the flyer is actually live |
| **General content / stuck pipeline / cloning / FQC won't generate** | **CLSD** | The catch-all content escalation |
| **Third-party app** display (not Flipp-hosted) | Account team (via **DOC**) | Out of Flipp's direct scope |

Before escalating, always attempt the **self-serve fix** for the issue type
(re-run AutoBox, fix dates in FADMIN, clone a stuck run, re-save, toggle simp pop,
update lat/long) — see the topic articles in `docs/knowledge-base/`.

---

## Filing a CLSD / Ops Troubleshooting ticket

**CLSD** is the escalation ticket type for issues that block or affect a flyer
and need the Content Collection / CI / dev team to investigate.

**Always include:**
- The **flyer run link** (`fadmin.flippback.com/flyer_runs/<id>`) and flyer ID.
- A clear **description of the error** and the **exact error text**.
- A **screenshot of the full error backtrace** (not just the first line).
- **What you already tried** (re-ran sessions, republished, compared to a
  working codesheet, etc.).
- For codesheet issues: the **failing codesheet** *and* a **previously-working
  codesheet**, plus **FADMIN and pipeline backups**.
- **Time sensitivity:** when it goes live, and whether it's urgent.

**Urgency guidance:**
- Mark **urgent** only when it blocks a go-live within ~1–2 days or blocks Final
  QC before go-live.
- Note: some ticket classes (e.g. data-piping) are generally **not** urgent
  because they don't block a flyer from going live — check the norm for the
  issue type before flagging urgent.

---

## Ownership map (who fixes what)

| Problem area | First responder | Likely fixer if code/config change needed |
|---|---|---|
| Codesheet won't process | `#helpme-ops` / `@enable-cxe` | CI/dev team via `wishabi/fadmin` (config, word bank, filename matching) |
| Flyer missing / broken indexer | OTS help desk | **FD** (indexing/feed team) |
| Store / harmonization data | OTS help desk | **CLSD** (fix) / **MSC** (measurement) |
| Hosted / preview / front-end rendering | OTS help desk | **HS** (Hosted team) |
| Live-flyer issue (tiles, images, pricing, categorization) | `#helpme-ops` / `@enable-cxe` | CLSD → Content Collection / CI team |
| Stuck pipeline / cloning / FQC won't generate | OTS help desk | **CLSD** |
| Storefront load errors | `#sf-auditor-alerts` / on-call | Content / platform on-call (republish on FADMIN) |
| Processing Support run/task | `#flex-processingsupport` / `@psflex` | PS Scrum Master |
| PS onboarding / retailer changes | `#helpme-flex` / `@flex` | Vendor Solutions / Flex MGMT |

---

*Sources: Confluence "Code sheet Troubleshooting Guide" (XPTCXE); "Data Piping
Troubleshooting Guide" (XPTCXE); "Processing Support - Knowledge Base" (FLX);
"How to troubleshoot Storefront errors" (QKB); `#helpme-ops` Slack practice. See
`sources/source-map.md`. Last reviewed: 2026-07-14.*


---

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


---

# Glossary — Flyer Processing Terms & Acronyms

> **What this covers:** Plain-language definitions of the terms, tools, and
> acronyms used across this CXE Help Center. The chatbot should use this to
> decode jargon in a user's question (e.g. someone pastes a "PZ" or "CLSD" and
> expects the bot to understand).

| Term | Meaning |
|---|---|
| **Codesheet** | The spreadsheet that tells FADMIN how to build a flyer run: uploads pages & pricing zones, orders pages, assigns stores/regions, sets dates and language. |
| **Config name** | Identifies which processor logic runs for a retailer's codesheet. Some retailers have multiple configs for different purposes. |
| **Pricing zone (PZ)** | A grouping tying a set of pages + valid dates + language + stores/regions together within a flyer run. |
| **FADMIN** | Internal admin tool for building, processing, and republishing flyer runs (`fadmin.flippback.com`; legacy `flyers.merchants.wishabi.ca`). |
| **FTP / SFTP** | File servers where retailers deliver source PDFs/images. Filename and folder conventions matter for codesheet processing. |
| **PDF Base Directory** | The FADMIN field pointing the codesheet at the correct FTP folder. A wrong/extra `/` breaks file lookup. |
| **Session** | An automated processing step on a run (image/tile generation, categorization, tagging, etc.). "Re-run sessions" is a common first fix. |
| **FQC** | **F**inal **Q**uality **C**heck — verification that a run is correct before go-live. |
| **QC** | Quality Check / Quality Control (e.g. tag QC, thumbnail QC). |
| **CLSD** | The escalation ticket type filed for issues needing Content Collection / CI / dev investigation. |
| **TOSS** | The Jira project historically used for Ops Troubleshooting tickets (source of many codesheet error examples in this CXE Help Center). |
| **PS** | **P**rocessing **S**upport — the Flex team that executes uploads, vendor setups, FQCs, page swaps, and revisions for many retailers. |
| **FLEX** | Flexible/vendor staffing org that provides PS Scrum Masters and processors. |
| **FTE** | Full-Time Employee (as opposed to FLEX / DSP hourly staff). |
| **DSP hourly** | Overnight hourly processors (uploads and FQCs only; no Slack access). |
| **COC** | "Completed by Ops Content" / center-of-competence style ownership tag used in PS task-combination charts. |
| **VAST** | A retailer program/segment recently migrated into Processing Support. |
| **Enablement pod (CXE)** | The **Client Experience & Enablement** team that absorbed the former **Skeleton Team**'s troubleshooting/support function. Reachable at `@enable-cxe` in `#helpme-ops`. |
| **Skeleton Team** | Former ops support team (now disbanded); its function moved to the Enablement pod. |
| **Data piping** | The pipeline that feeds retailer data into the system; errors are usually caused by retailer-side changes. Filed via CLSD; generally not urgent since it doesn't block go-live. |
| **Harmonization / 4Square** | Matching a store to the canonical store/location dataset (4Square). Failures block store-level targeting. |
| **Masthead** | The branded header/banner on a storefront; can be tied to promo budget and Storefront Premium placements. |
| **Storefront** | The consumer-facing publication surface; "storefront errors" mean it's failing to load for some merchants. |
| **Republish** | Re-pushing a processed flyer run to storefronts (done in FADMIN); a common fix for missing thumbnails / incomplete processing. |
| **SFML** | Storefront markup/format referenced in storefront beacon errors (e.g. `Unable to retrieve SFML error 1`). |
| **Beacon** | A telemetry event (queried in Lenses), e.g. `Beacon.FlippApp.StorefrontZeroCaseError`. |
| **Generic codesheet** | A fallback codesheet used to create zones, assign stores, and upload pages manually when a retailer's normal codesheet won't process. |
| **OneGuide** | Per-retailer processing instructions referenced by PS. |
| **OTS** | **Ops Troubleshooting** — the front-line Jira help-desk board (project `OTS`, board 315) where day-to-day flyer issues are raised and triaged. |
| **Indexer** | The automated scraper that pulls an indexed retailer's flyer from their website. A "broken indexer" (wrong URL/dates) is the top cause of missing flyers. |
| **FD** | Jira project **"Flipp Content Daily Priorities"** (board 312), home of **Broken Indexer** tickets — the escalation target for missing/not-gathered flyers. |
| **CLSD** | Jira project **"Content Layer Service Desk"** — the content-platform engineering service desk. Handles investigations, pipeline/cloning errors, categorization, tagging, and store-harmonization *fixes*. The main escalation from OTS. |
| **MSC** | Jira project **"Marketing Science"** — the analytics/measurement function (historically keyed **"PIA"**). Handles Foursquare AAAS feasibility, store-trip reporting, and data submissions. |
| **PIA** | Legacy Jira key prefix that now **resolves to `MSC-` (Marketing Science)**. Not a separate project. Store-harmonization *measurement* is tracked here; the *fix* is done in CLSD. |
| **HTS** | A store/harmonization ticket queue referenced by older harmonization escalations (e.g. HTS-25, HTS-35). |
| **HS / Hosted team** | Jira project (board 67) for the Hosted team — retailer-embedded flyer experience (iframe/preview/front-end rendering). |
| **WES** | The newer flyer-processing engine/flyer-type (vs. "legacy"); "WES Error" appears in cloning/pipeline failures escalated to CLSD. |
| **Nexus** | Internal content API/service (e.g. `UpsertOffers`, `upsert_section`) referenced in CLSD platform tickets. |
| **Foursquare AAAS / 4SQ** | Foursquare "Attribution-as-a-Service" — store-visit measurement for ad campaigns, run through MSC. |
| **PARF / exposure files** | Data files sent to Foursquare for measurement/reporting (MSC). |
| **DOC** | A routing/escalation path to the retailer's account team (e.g. third-party app issues not hosted by Flipp). |
| **CLSD** | (see above) general content escalation ticket type; OTS escalates stuck pipelines/cloning/FQC issues here. |
| **FSA** | **Forward Sortation Area** — the first three characters of a Canadian postal code; used for flyer distribution/coverage. "FSA Missing" = a postal area has no flyer. |
| **Distro** | Distribution — the set of postal codes/ZIPs/stores a flyer run is served to. |
| **Geo-targeting** | Mapping postal codes to the correct regional flyer. Errors show as one region seeing another region's flyer. |
| **AutoBox / auto box draw** | The task that automatically draws clip boxes around flyer items. Completing it kicks off **auto tag**. Poor draws cause unclippable/off-center items; the fix is re-running it or boxing manually. |
| **Auto tag** | The task that tags item data; triggered after AutoBox. |
| **Cutout generation** | Generating item cutout images; can fail/block and need a re-run. |
| **Page stitching** | Assembling flyer pages for display; re-running it + republishing fixes cropped/mis-rendered pages. |
| **Tile / thumbnail generation** | Automated step producing flyer tiles/thumbnails; failures block clipping or display. |
| **Preview link** | A link to view a flyer (often pre/around go-live). Not intended for sharing not-yet-live flyers. |
| **Hosted** | The retailer-embedded flyer experience (e.g. shown in an iframe on the retailer's own site). |
| **Simp pop (simple pop)** | A flyer-type toggle; when on, item detail text (pre-price/price/sale story) is suppressed. Turning it off restores item details. |
| **Preview ready / Ops complete** | Flyer-run states. A run stuck in "preview ready" instead of "Ops complete" won't go live; cloning/re-processing is the common fix. |
| **Clone / cloning** | Copying a flyer run; used to resolve a run stuck between states, and a distinct source of "clone erroring" issues. |
| **Tesseract** | Internal tool for indexing sessions (`tesseract.flippback.com`), used to verify indexing/added flyers. |
| **Track ID** | Identifier a page needs to be included in tile-generation sessions; pages missing it get excluded. |

*Last reviewed: 2026-07-14. Add terms as new articles are written.*

