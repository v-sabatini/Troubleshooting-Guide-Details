# Flipp Flyer-Processing Troubleshooting — CXE Help Center

> Combined bundle of the CXE Help Center's general troubleshooting, process, QC, and runbook guidance. For retailer-specific processing, see the "Retailers - <letter>" bundles and the "CP Processing SOPs" bundle.

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

# Content V2 & V2 Publishing — What It Is & How It Affects Processing

> **What this covers:** A plain-language orientation to **"V2"** (Content V2 / V2
> Publishing) — Flipp's shift from the **Flyer-Centric (V1)** content model to the
> **Global-Centric (V2)** model — and what it means for flyer processing and
> troubleshooting.
>
> ⚠️ **Scope note:** V2 is an **in-progress platform migration** described mostly
> in engineering/data strategy docs (as of Oct 2025 – Jul 2026). This article
> explains the concepts and the impact on processing. It is **not** a step-by-step
> "how to run/re-run V2 publishing" runbook — those operational mechanics aren't
> documented yet (see Gap Log **GAP-001 / GAP-002**).

## The one-paragraph version

Flipp is moving from a **"Flyer-Centric"** content model (**V1**) to a
**"Global-Centric"** one (**V2**). In V1, everything hangs off a flyer
(`flyer_id`, `flyer_item_id`). In V2, content is modeled as independent,
globally-identified entities — **Offers, Products, Promotions, Publications** —
that can be distributed to any channel and place. Flyers become **Publications**,
flyer pages become **Sections**, and flyer items become **Offers/Atoms**. The goal
is a single content source (**Curator**) fed through a single ingestion entry
point (**Nexus API**), with legacy systems kept alive by **converters** during the
transition.

## Vocabulary shift (V1 → V2)

| V1 (Flyer-Centric) | V2 (Global-Centric) | Notes |
|---|---|---|
| Flyer / `flyer_id` | **Publication** / `publication_id` | A curated, dynamic collection of displayable items |
| Flyer page | **Section / Section Plan** | Subset of a publication; can have its **own distribution** & rendering |
| Flyer item / merchandise | **Offer** (a kind of **Atom**) | Atom = parent of Offer + Promotion; replaces merchandise/items |
| — (new) | **Promotion** | A displayable ad (image + click action) with no product/offer |
| item / product | **Product** | A purchasable thing at one retailer |
| `flyer_item_id` | `offer_id` / **`global_id`** | **One V2 Offer can map to *many* V1 flyer items** |
| FSA-based availability | **Distribution + Place** | see "distribution" below |

**Key mapping fact:** except for flyer items (1 Offer → many V1 items), V1↔V2 is
roughly **1:1** — everything in V1 has a V2 equivalent. The reverse isn't true:
newer content (DVM, NativeX EU/South America) has **only V2 ids**, no V1 id.

## The big processing-relevant change: distribution

- **V1** distributed flyers by **FSA** (flyer-availability-service) + store finder.
- **V2 distributes to *stores*, not FSAs.** "Distribution" is anything targetable
  — a **Place** (postal code, store, FSA, or polygon), a **channel**
  (app/feature), or (future) a user segment.
- **Publications *and* their Sections can each be distributed** — and a section can
  be distributed to a **subset** of the publication's distributions.
- **Why this matters for troubleshooting:** channel- and zone/section-level
  distribution (e.g. *"hidden everywhere except hosted,"* or one pricing
  zone/section behaving differently from the rest) is a **first-class V2 concept**.
  Publish/distribution behaviour is now **per-publication and per-section/zone, per
  channel** — which is exactly the backdrop to **GAP-001** (publish errors under
  hosted-only distribution) and **GAP-002** (V2 publishing failing for one zone).

## How V2 publishing flows (where "V2 Publishing" fits)

- **Fadmin** is still the PDF-processing CMS, but is shifting from fanning out V1
  data to **producing V2 print content into the Nexus API**.
- **Nexus API** = the single **entry point / source of truth** for incoming flyer
  content. It feeds **Item Platform** (→ V2 Products & Offers → Content API),
  **Publication API** (publication structure), and **Distribution API**
  (distribution IDs).
- **Curator** = the single **V2 serving source**; pulls items/publications/
  distributions from those APIs. **DVM** is the active V2 distribution path today
  (NativeX, retailer apps).
- **Flyers-NG** = the **V1 compatibility layer** during the transition; a converter
  translates **V2 → V1 on read** so legacy **App / Web / Hosted** keep working. It's
  removed once channels are fully V2.
- A **Publication Plan** (content queries + rendering details) is resolved and
  **"hydrated"** into a **Publication Payload** — the actual content the user sees.
  *(This means the full content a user saw is only known at render time.)*
- Being **decommissioned:** Search Platform API, FlyerKit, Backflipp, and the old
  Fadmin → V1 fan-out.

## What this means for the processing team (practical)

- **Terminology in tools/tickets is shifting.** Expect "publication," "offer,"
  "section," "distribution," "global id," **Nexus**, **Curator**, **Flyers-NG**,
  **DVM** alongside the old flyer/item/FSA words — use the mapping table above.
- **Distribution is per channel + per store/section**, so "hidden except hosted"
  and per-zone publish behaviour are expected V2 levers (and new failure surfaces).
- **Reporting/metrics differ:** V2 counts **Offers, not flyer spots** ("Item View"
  ≠ "Offer View"); some V2 content (international, DVM) has **no V1 id** at all, and
  billing/legacy reports still depend on V1 ids (kept alive by converters).
- **Legacy display depends on conversion** (Flyers-NG V2→V1). If something renders
  oddly on a legacy channel *during the transition*, the converter is a suspect.
- **V1 and V2 can succeed/fail independently.** Because both paths run during the
  transition, a **V2 publish failure doesn't necessarily take the flyer dark** — a
  zone whose **V2** publish failed can still be **live on V1-powered experiences**,
  just missing from **V2-powered experiences**. *(Confirmed via processing-team
  feedback, 2026-07-15.)*
- **A failed V2 publish task can block other sessions.** The bigger operational
  impact is often not the missing V2 content but that the **errored task blocks
  other flyer sessions from kicking off** — which is why these escalate quickly.
  See `publishing-and-go-live.md` → "V2 Publishing fails for one pricing zone."

## Troubleshooting note / current gaps

These sources are **architecture/strategy**, not an ops runbook. They explain
*why* V2 publishing and per-zone/channel distribution exist — but **not** the
step-by-step "re-run V2 publishing for one zone" or "why did the publish task
error with no logs." Those remain **open in the Gap Log (GAP-001, GAP-002)**.
For live cases, escalate to **CLSD** (Content Layer) and loop **Hosted (HS)**;
we'll add an ops runbook here once one exists.

---

*Sources: Confluence — "Transitioning to Global-Centric Model: Content V2 & Event
V2 Adoption Framework" (DATAV, 13022527510); "Content V2 Dimensions" (DATAV,
13245906978); "V1 => V2 Data Pipeline Transition" (EN, 12597657799); "DET Content
V2 Discovery" (DATAV, 12291965139, "flyers are distributed to stores, not FSAs");
"Transitioning from V1 → V2 for Content Retrieval" (CTLR, 11268554758). Migration
in progress as of Oct 2025 – Jul 2026. Last reviewed: 2026-07-15.*


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
>
> **Related:** Doing an **item import or SKU update**? The file-format rules
> (column order, accepted headers, blanks, dates) are in
> [`item-import-format.md`](item-import-format.md).

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
2. **Check every pricing zone has the required fields:** pages assigned, the
   correct language, and — **for codesheets that require dates** — a valid-from
   and valid-to date. (Many processors set pricing-zone dates **automatically to
   match the run**, so missing dates only cause errors on configs that actually
   require them — don't assume it's the cause.)
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
empty (`nil`) — almost always because a file it expected to find wasn't there,
or a field the codesheet expected is blank.

**First, confirm which codesheet processor / config is in use.** The likely
causes differ by processor — for example, some configs set pricing-zone dates
**automatically to match the run**, while others (e.g. a generic codesheet with
no dates) **require** them. Knowing the processor tells you which of the causes
below are even possible, so establish this before diagnosing.

**Likely causes & fixes (check in this order):**

| Cause | How to confirm | Fix |
|---|---|---|
| A **page/file name in the codesheet doesn't match the SFTP** (so lookup returns nil) — **the most common cause** | Compare page/file names in the codesheet to what's actually on the SFTP; watch for renames, delimiter (`_` vs `-`), trailing spaces, and page-number-suffix differences | Make them identical — rename/resync on the SFTP **or** update the codesheet to match *(TOSS-7020: a file changed from `FLAP` to `FD`)*. See error #2 below for the full filename-matching detail. |
| **PDF base path mistake** + a pricing zone has **no pages** in the CSV | Verify the PDF Base Directory; confirm every PZ has at least one page | Correct the base path and add the missing pages *(TOSS-7012)* |
| A pricing-zone row is **missing start/end dates** — **only on codesheets that require dates** | Scan the codesheet row-by-row for blank valid-from/valid-to cells | Fill in the missing dates and re-run *(TOSS-7033: the culprit was line 131 with no start or end dates)* |

> **Don't rank "missing dates" first.** Because most processors set dates
> automatically to match the run, a missing-dates row is usually the *least*
> likely cause — unless the specific processor requires dates. Lead with the
> filename/SFTP match.

**Best practice when filing:** attach the failing codesheet **and** a
previously-working one, plus a screenshot of the **full error backtrace** (not
just the top line) and both the FADMIN and pipeline backups. Support asks for
these every time.

#### `NilClass` on a `generic_stores` (store-assignment) codesheet

A **`generic_stores`** codesheet only **assigns stores to pricing zones**, so a
`NilClass` here narrows to the store / pricing-zone fields.

- **Most common cause: a pricing-zone name that doesn't match Fadmin — usually a
  typo or a trailing/leading space.** The mismatch can be in **either** the
  codesheet **or** the Fadmin pricing-zone name, so pull **both** lists and
  cross-reference them.
- **A missing/unfindable store code is NOT a `NilClass` error.** When the system
  can't find a store code it **names that specific store code in the error
  message** — so if the error is a `NilClass`, a missing store code is probably
  *not* the cause; don't chase it here. *(To add a genuinely missing store, add
  it at merchant level with the SAP# as the merchant code and re-run — but that's
  a different error.)*
- **Watch for hidden spaces.** Fadmin's **Pricing Zone tab doesn't always display
  a trailing/leading space**, so two names can *look* identical. To confirm,
  either **click into the zone**, or run the **`Pricing Zone Page` custom action**
  and **export the resulting `.csv`** to cross-reference against the codesheet.
- **Locating the bad zone:**
  - If the codesheet added stores to zones **in the same order** as the Pricing
    Zone Page ordering, look at the **first zone showing `0/0`** — the typo is
    there.
  - If the codesheet is **out of order**, pull the store list from
    **Overview → Manage Stores** and use it to find **where the codesheet stopped
    adding zones**, then check that zone for the typo/space.

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
7059; team SME review (answer-feedback-log FB-002, FB-003). See
`sources/source-map.md`. Last reviewed: 2026-07-22.*


---

# Item Import — File Format & Common Failures

> **What this covers:** The accepted file format for an **item import** (and
> **SKU update**) in FADMIN — required column order, the full set of accepted
> column headers, language prefixes, date formatting, and how to leave a value
> blank — plus the most common reasons an item import fails to run. Grounded in
> team SME review.
>
> **Audience:** Flyer processors doing item imports / SKU updates.
> **Escalation path:** If the file follows every rule below and still won't
> import, file a CLSD ticket with the `.csv` attached (see
> `escalation-and-tickets.md`).

---

## The rules that make an import run

An item import is a `.csv` of item data. Most "it won't run" failures come from
the file's **shape**, not its values. Check these first:

1. **Column order matters for the first two columns.**
   - **`item_id` must be column 1.**
   - **`sku` must be column 2.**
   - Everything after that can be in any order. A file whose columns are, say,
     `item_id, name, sku, …` **will fail** because `sku` is in position 3, not 2.
2. **A minimum of 3 columns is required.** `item_id` + `sku` alone will **not
   run** — even for a SKU-only update. Add at least one more valid header
   column; **it may be completely empty** (e.g. add a `url` column with just the
   header and no values, and the import will run).
3. **Dates must be `YYYY-MM-DD`.** Any date column (e.g. `valid_from`,
   `valid_to`) has to be in that format.
4. **To store a blank value, put `*blank*` in the cell.** `*blank*` explicitly
   saves the field as an empty string — use it to **clear** a field.
5. **Watch SKU formatting.** Spreadsheets can mangle long SKUs into scientific
   notation or insert commas. Confirm the SKU column is stored as text and the
   values are intact.

---

## Accepted column headers

The retailer OneGuides do **not** list the full set of accepted headers. These
are the accepted column headers for an item import:

```
analytics_categories, auto_play_video, bonus_offer_description, brand, brand_id,
data_piping_url, deferred, description, disclaimer_text, display_type,
display_url, external_override_image_source_url, feature_html,
google_category_id, id_1, id_2, id_3, id_4, id_5, id_6, iframe_display_height,
iframe_display_width, in_store_only, item_corrections, item_side_list_url_text,
keywords, name, overlay_url, page_destination, play_video_inline, pre_price_text,
price_text, qualifying_quantity, raw_current_price, raw_dollars_off,
raw_original_price, raw_percent_off, reward_quantity, sale_story, sku, url,
valid_from, valid_to, video_sound_on, youtube_embedded_url
```

…plus **`item_id`**. Remember the ordering rule: **`item_id` = column 1, `sku` =
column 2**; the rest may be in any order.

### `google_category_id`

`google_category_id` **is a valid header** — don't drop it just because its
value is a number. In FADMIN the Google Category is **displayed in words**, but
the **backend value is numeric**, so a value like `319` is legitimate.

### Language prefixes (`english_` / `french_`)

You can prepend **`english_`** or **`french_`** to any field so it applies only
to English or French items. Example header row:

```
"item_id","sku","english_url","french_url","keywords"
```

---

## Common item-import failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Import fails to run | **Wrong column order** — `item_id` not in column 1, or `sku` not in column 2 | Reorder so `item_id` is column 1 and `sku` is column 2 |
| SKU-update file won't run | **Fewer than 3 columns** (just `item_id` + `sku`) | Add any third valid header column — it may be empty (e.g. a blank `url` column) |
| Dates rejected / rows import wrong | Dates not in `YYYY-MM-DD` | Reformat all date columns to `YYYY-MM-DD` |
| A field won't clear / saves oddly | Empty cell where an explicit blank was intended | Put `*blank*` in the cell to save an empty string |
| Long SKUs corrupted | Spreadsheet converted them to scientific notation / added commas | Store the column as text; re-enter clean values |

---

## When to escalate

If the file follows all the rules above and still won't import, file a **CLSD**
ticket with the `.csv` attached and the exact error text. See
`escalation-and-tickets.md`.

---

*Sources: team SME review (answer-feedback-log FB-006, FB-007). Cross-reference:
`codesheet-errors.md`, `common-live-flyer-issues.md`. See
`sources/source-map.md`. Last reviewed: 2026-07-22.*


---

# Turbo & CP-Legacy — Error Guide

> **What this covers:** The processor-facing errors seen in **Turbo** and
> **CP Legacy** import/custom-action jobs, with the exact error strings, the
> usual cause, and the self-serve fix. Source Confluence page id: 13617366001
> (space CP, "Error Guide: Turbo & CP-Legacy [2026]").
>
> **Audience:** Content Production processors.
> **Escalation path:** If self-serve steps fail, escalate per
> `escalation-and-tickets.md`.

---

## Turbo errors

### `Invalid Flyer Type for Merchant`

- **Symptom:** The error log reads `Invalid Flyer Type for Merchant`.
- **Likely cause:** The wrong **Flyer Type ID** was entered for that specific
  retailer.
- **Fix:** Double-check the Flyer Type ID, correct it as required, and submit the
  **Import Job** again.

---

## CP Legacy errors

### `Error processing image: Request was blocked by retailer. Please try with proxy option. HTTP 403 - Forbidden`

- **Symptom:** A CP Legacy job errors with, verbatim:
  `"Error processing image: Request was blocked by retailer. Please try with proxy option. HTTP 403 - Forbidden"`
- **Likely cause:** More often than not, the URL for the problematic SKU is
  incorrect or invalid.
- **Fix:**
  1. Copy the problematic **SKU / Ecom ID** and look it up in the **product data
     sheet**.
  2. Click the product **image URL** link to confirm it works.
  3. If the link is invalid, update it with the correct URL and **rerun the
     custom action**.

### `ERROR: Not enough rows in Product CSV for zone [Insert Store Set here]`

- **Symptom:** A CP Legacy job errors with, verbatim:
  `"ERROR: Not enough rows in Product CSV for zone [Insert Store Set here]"`
- **Likely causes:**
  - An invalid/incorrect SKU image URL (same class as above); **and/or**
  - A **mismatch** between the **"Store Sets"** and **"Sale Story"** values.
- **Fix:**
  1. Check the problematic SKU/Ecom ID against the product data sheet and fix any
     invalid image URL (as above).
  2. In the preview, confirm the **Store Sets** and the **Sale Story** are correct
     and **match the expected values in the Story Curation Sheet**.
  3. Resubmit the **Import Job**.

---

## See also

- `home-depot-us-troubleshooting.md` — retailer-specific CP Legacy / Snicket /
  Fadmin errors.
- `escalation-and-tickets.md` — when and how to escalate.

---

*Source: Confluence "Error Guide: Turbo & CP-Legacy [2026]" (CP, 13617366001). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


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

## ⭐ Start here: is it a *processed* flyer or an *indexed* flyer?

This determines where to look — and they point in **opposite directions**:

- **Processed (non-indexed) flyer** — one your team builds/uploads and processes.
  **If you're a processor asking "my flyer is missing," this is almost always the
  case.** The cause is in **processing/publishing, not the indexer** — jump to
  **"Processed flyer missing"** below.
- **Indexed flyer** — auto-scraped from the retailer's website (often a
  CX-reported "missing flyer" for an indexed retailer). Here the usual cause **is**
  a broken indexer — see **Cause 1** below.

---

## Processed flyer missing (the processor default)

For a flyer you're processing, work these before ever thinking about the indexer:

1. **Still processing / not live yet** — confirm the run actually finished:
   sessions complete, state is **Ops-complete** (not stuck in "preview ready").
   → see `publishing-and-go-live.md`.
2. **Stuck run / didn't go live** — clone / re-process the run; escalate to
   **CLSD** if it won't move. → `publishing-and-go-live.md`.
3. **Wrong dates** — valid-from set in the future, or an expired flyer showing /
   a live one reading as expired → fix dates in FADMIN. → `flyer-dates.md`.
4. **Published but hidden / distribution** — check availability & channel toggles
   (hidden on all channels, or a hosted-only distribution). → `hosted-and-previews.md`,
   `publishing-and-go-live.md`.
5. **A specific area sees nothing** — coverage/FSA or wrong-region geo-targeting
   (see "Coverage" causes below).

Only if none of the above applies — and the retailer is genuinely **indexed** —
move on to the broken-indexer path.

---

## Quick triage (indexed flyers)

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

## Cause 1 — Broken indexer (the top cause for *indexed* retailers)

> Applies to **indexed** retailers only. For a **processed** flyer, use the
> "Processed flyer missing" section above instead — the indexer isn't involved.

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

### Issue: V2 Publishing fails for one pricing zone (V1 still succeeds)

**Symptom:** **V2 Publishing** errors for **one pricing zone but not others**. The
pipeline task shows errored (sometimes **with no logs**), and — importantly — the
**errored task blocks other flyer sessions from kicking off**.

**What it means for go-live:** During the V1→V2 transition, most experiences have
both a V1 and a V2 path. If **V2 fails but V1 succeeds**, that zone **still goes
live on V1-powered experiences — just not on V2-powered experiences.** So the
flyer usually isn't fully dark; the real problem is the **errored task blocking
downstream sessions.** (See `content-v2-and-publishing.md`.)

**What to try / know:**
- **You can't re-publish a single zone — republishing is all-or-nothing.** A
  manual republish often **just repeats the same error**, so don't expect it to
  clear this on its own.
- **Cloning *might* resolve it, but the error can also block the clone** — it's not
  a guaranteed fix.
- **Setup is usually not the culprit** and is typically already verified by the
  time this reaches the help desk — don't spin on re-checking the zone's setup.

**Escalate to CLSD.** This is the confirmed path — the root cause (why V2 publish
fails for the zone) is a content-platform/engineering matter. Include: the flyer
run link, the specific zone, that the **errored task is blocking other sessions**,
and that a **manual republish repeated the error**. Mark urgent if go-live is close.

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
- **For a link/URL specifically, try these before escalating (in order):**
  1. **Re-run the Item Cutout Generation session** — re-running a task
     **downstream of** item cutout generation makes it **re-kick off**.
  2. **Re-run the Vendor tasks** — Vendor tasks **act as sessions**, so re-running
     them **kicks off the item-level sessions**.
  3. **Republish** the flyer.
  4. Run the **`Touch Storefront Objects`** custom action to push the change to
     the storefront.
- If new items/links **still** won't reflect, escalate to the **Hosted team (HS)**
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
2006/2027/2030/2047/2048/2060/2064; team SME review (answer-feedback-log FB-008).
See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-22.*


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

> **Item import / SKU update won't run?** That's a file-format issue — see
> [`item-import-format.md`](item-import-format.md) (column order, accepted
> headers, 3-column minimum, blanks, date format).

---

## Flyer tile generation error

- **Symptom:** A flyer run consistently gets a *flyer tile generation error*;
  it blocks completing the Final QC checklist.
- **Does it block go-live?** **Yes.** If the **Final QC checklist isn't
  completed, the flyer does not publish** — treat this as go-live-blocking.
- **Try first:**
  1. Re-run the tile/thumbnail generation session; wait to give processing time
     to work through the queue; confirm required upstream steps completed.
  2. **Check the error on the Page Tile Generation task** — it may point to a
     **specific page** that's the problem.
  3. **If only ONE track is erroring, consider deleting that whole track** — e.g.
     if it's a **revised page** or **category pages added after the initial
     upload**. Deleting the erroring track can temporarily get the run into a
     state where **FQC can proceed**; you can then **retry the upload of that
     track**.
     - ⚠️ **Only if the WHOLE track can be deleted. Do NOT partially delete a
       track** — partial deletion causes downstream impacts.
     - **Make a backup first.**
- **If still broken:** **Ask in Slack (the Enablement team) before filing a
  ticket** — CLSD is for errors whose **system cause the CXE team can't
  identify**, so the Slack check comes first. If it's still unresolved, file an
  **urgent CLSD** to unblock (especially if it's stopping Final QC before
  go-live).

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

## Link / URL not reflecting on the front-end

- **Symptom:** An item's **link/URL** was updated in FADMIN but isn't reflecting
  on the front-end (often **Hosted**).
- **Try first (in order):** rule out caching / still-processing; **re-run the
  Item Cutout Generation session** (re-run a task downstream of it to re-kick
  it); **re-run the Vendor tasks** (they act as sessions and kick off item-level
  sessions); **republish**; run the **`Touch Storefront Objects`** custom action.
- **If still broken:** escalate to the **Hosted team (HS)**. See
  `publishing-and-go-live.md` ("New boxes / items / links not reflecting") for
  detail.

## Auto-categorization gaps (missing Google categories)

- **Symptom:** Some **Google Categories are missing** after auto-categorization.
- **Know this first:** **Auto-categorization can't be manually re-run**, and a
  **missing category does NOT block tagging** — an item with no assigned category
  can still generally be tagged. So a missing category is usually **not** what's
  blocking Tag QC; see the Vendor/Tag QC entry below for the likelier cause.
- **Try first:** Confirm whether the missing category is actually blocking
  anything downstream. Share a list of affected items.
- **If it needs fixing:** File a **CLSD** ticket for the auto-categorization gap;
  note if pages are going live soon so it can be prioritized/bumped.

## Vendor / Tag QC task errors when moving between items

- **Symptom:** Advancing to the next item in **Vendor Tag QC** errors — and the
  processor gets the **same failure** when starting the task from the flyer-run
  pipeline. (Vendors report the task "isn't working.")
- **Likely cause:** One or more **pages/items were deleted before the Vendor
  tasks were completed**, so Tag QC is looking for items/pages that **no longer
  exist** — which errors when advancing. (This fits the same failure showing up
  for both the vendor and the processor.)
- **Try first / diagnose:** Pull the **task's error log** — it can reveal the
  deleted item/page. Don't send the processor hunting for the culprit item by
  hand; if the log doesn't name it, that identification is fine to **leave to
  CLSD**.
- **If still broken:** File a **CLSD** ticket with the task error log; CLSD
  typically identifies the specific culprit item and unblocks it.

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

*Sources: `#helpme-ops` Slack help-desk threads (2025–2026); team SME review
(answer-feedback-log FB-004, FB-005, FB-008); cross-referenced with the Processing
Support KB and Storefront runbook. See `sources/source-map.md`. Last reviewed:
2026-07-22. Some remediation steps are distilled from how issues were actually
resolved in-thread — verify against current SOPs.*


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


---

# Retailer Onboarding & Offboarding — Process Guide

> **What this covers:** How the Ops Onboarding (OBQB) team takes a retailer from
> assignment to go-live — direct (full-processing) onboarding, indexed
> onboarding, rebranding, and offboarding — including the exact FAdmin/MAdmin
> merchant-setup steps and workflow toggles processors must set. Source
> Confluence page id: 3129144452 (space XPTCXE).
>
> **Audience:** Onboarding quarterbacks (OBQBs) and flyer processors setting up
> new or returning merchants.

---

## Who owns onboarding

The **Onboarding Quarterbacks (OBQBs)** are an Operations team that makes retailer
onboarding fast and seamless for Ops, BD, and retail partners. **Hosted owner:**
Technical Enablement Team.

**Loop in an OBQB when:**
- The retailer is a **net-new onboarding**.
- A retailer is returning to Flipp after an extended absence.
- A retailer is **adding a banner** to an existing merchant group.
- There is a one-off, pre-approved campaign for a net-new retailer.
- A CPG/Brand requires new merchant setup.

**The OBQB team is NOT responsible for:** setting up Hosted 2.0, Hosted
troubleshooting, budget/revenue, Salesforce, reporting, or NativeX (outside
campaign setup).

**How to include an OBQB:**
1. File an **Onboarding Ticket** in Jira on the **Operations Onboarding Board
   (project `MM`, board 274)**.
2. Post in the **#onboardings** Slack channel and tag **@qbs**.
3. Include: retailer name, ideal launch date, and the ticket link.
4. An OBQB picks up the ticket within **24–48 hours** and follows up for details.

---

## Direct (full-processing) onboarding — end-to-end

### 1. Assignment & Jira ticket
New onboardings are posted in **#onboardings** by BD with an accompanying ticket
on the Operations Onboarding Board (MM). Tickets are picked up within 24–48 hours.

### 2. Intro to retailer
Once assigned, the QB is introduced to the retailer by email and establishes
timelines, expectations, and relationship details. This can be informal (Slack /
email) — it does not need to be a formal meeting. Use the Internal Kickoff
Discussion Checklist (link in source doc).

### 3. SFTP creation
1. Create SFTP credentials using the **SFTP Automation** (via AWS Chatbot — see the
   EF1 SOP "How to Create or Retrieve SFTP Credentials via AWS Chatbot").
   *(credentials in the source doc — not stored here)*
2. After the merchant is created in FAdmin, add SFTP credentials:
   **Merchant Page > Details > Edit Merchant > FTP Username, Base Path, toggle ON
   FTP Sync Enabled > Save Changes.**
3. After the external intro: send the retailer a **one-time URL** with their SFTP
   credentials, ask them to drop assets to the SFTP, and confirm receipt.

### 4. Create the merchant in FAdmin (new client)
**Salesforce is the single source of truth** for newly created retailers. Country
information is entered via Salesforce; flag discrepancies to BD (they update or
create a net-new merchant).

1. Open the **Merchant Admin (MAdmin)** interface.
2. Search the incoming retailer name; it appears under **Account Name** with
   **(To Be Filled)** in the Name column. *(Sync can take ~1 hour; if not visible
   after 1–2 hours, flag to BD.)*
3. Click the **To Be Filled** hyperlink to open the Merchant page.
4. Fill in:
   - **Internal Name** — pre-filled from Salesforce; editable if needed.
   - **Relationship?** → **Direct**
   - **Distribution Channels?** / Only Show In → **All Channels**
   - **Supported Language?** → English (add French only if there is French content).
   - **Display Name** — input language, Name, and Display Name for all languages.
   - **Name Identifier** — all lowercase, no spaces (e.g. `IGA Southwest` → `igasouthwest`).
5. **Upload logos:** main logo (any shape, rectangular recommended; Vector or
   transparent PNG, HD) and **Storefront Logo** (square `.jpg`, min 60×60,
   max 120×120 px). Input SFTP details and toggle ON Sync Enabled if not done.
6. **Details > Processing Settings:** URL = merchant website; enter Salesforce ID
   (from BD); enter the store locator URL in **Default Store Locator URL**.
7. **Custom tab:** disable **Show Simplified Pop** (if enabled); set default
   **chrome setting to "flatsheet."**
8. **Details tab > Edit Store Settings:** Harmonize stores with Foursquare → Yes;
   select a Foursquare Venue Category; Update.
   *(Note: Harmonize/Venue Category no longer function in this UI — see the "Add
   Stores to Merchant" flow / stores-and-harmonization.md.)*
9. Add categories from the retailer's website.
10. Assign yourself as **DOC and DOL** on the merchant.
11. Post in **#osteam** to determine vendors to auto-assign, providing: Content
    Type (Grocery/Electronics), Language, Processing Type (Simp Pop or Full),
    Budget (Y/N), flyer cadence (weekly/monthly), approx. items per publication,
    and lead time.

### 5. Workflow settings (all retailers)
Set every retailer up with these Merchant Workflow toggles:
- Use PDF image extraction
- Use PDF Image Auto Selection
- Uses auto box draw **(do NOT skip Box QC)**
- Vendor Tag
- Tag QC
- Vendor Spot Check
- Auto Tag Enhanced
- **Auto Tag Fields → All**

> **Always ensure Flyer Type settings match Merchant Workflow settings** — Flyer
> Type overrides the merchant level.

### 6. Build the Flyer Type
1. Create Flyer Type name.
2. Create SEO Name (Flyer Type name, no spaces).
3. Enable store selection.
4. Enable **Geo-Awareness (GA)** if confirmed in IKO (**US retailers only**).
5. Enable **max store distance** (Canadian retailers, or US retailers not using GA).
6. Add Hosted URL.
7. Submit a ticket to add any Flyer Type to stacks.
8. Move the Jira ticket to **Content Processing** when files are received.

### 7. Process & prep assets
- Upload received files and begin processing.
- Create a **OneGuide 2.0** from the template.
- If proceeding with an OKO, prep the OKO deck (separate CA / USA templates).
- Tier 1/2 retailers may get an end-to-end analysis from the Content Strategy
  team — confirm with them before offering externally.

### 8. Codesheet creation (if a codesheet is provided)
- First understand the codesheet and build 1–2 versions of the ad yourself.
- File a **TOSS** ticket to automate the codesheet process, including: how to read
  and version the pages, how to determine stores per version, and any info needed
  to paginate correctly.
- Create a Merchant Code Sheet page (Confluence OP space).
- See `codesheet-errors.md` for troubleshooting once it's live.

### 9. Links check (tracking codes)
- Check received links for tracking codes (**quick check: look for `utm` in the
  URL**). If present, inform the account team — BD communicates that only promoted
  retailers receive tracking codes.
- Tracking codes on **product URLs** are removed automatically when the "Buy Now"
  button turns off.
- **Direct links** keep tracking codes even when budget runs out — but if the
  retailer is launching **organic**, remove direct-link tracking codes before go-live.

### 10. Vendor assignment & store upload
- Confirm vendors via **#osteam** and auto-assign on the merchant page.
- Upload the most recent store list. As long as the **merchant store code matches**,
  data updates in place; if the code does not match, upload then delete duplicates.
- **Systematically build all lat/longs using the Geocode Google Sheets add-on**
  (see the Lat/Long SOP and `stores-and-harmonization.md`). For many mall stores,
  an OS ticket can be filed to audit Geocode lat/longs (front-entrance inaccuracy);
  use internal resources to audit when possible.

### 11. Dry run (optional — account team's discretion)
Process the publication in full and set up a walkthrough with retailer + BD.
Consider a dry run when: the retailer is integrating Hosted, is very unfamiliar
with Flipp, has confusing/specific tagging needs, or is an enterprise retailer.

### 12. Go-live walkthrough
- Present OKO deck and risk items (e.g. clean images cannot be extracted from the
  files provided).
- Update Vendor Guide and merchant-specific FQC per feedback.
- Follow up with preview link and OKO deck, then next steps.
- Get sign-off on the preview and confirm go-live.
- Update the Audit Cycle Spreadsheet.

### 13. Go-live checklist
- [ ] Stacks assigned
- [ ] Stores have lat/longs and **≥90% harmonized**
- [ ] Turn off Indexer (if required)
- [ ] **Always un-check "Indexed?" when transitioning a retailer from Indexed to Direct**
- [ ] Upload Merchant Schedule to FAdmin
- [ ] Links set up correctly
- [ ] Confirm distribution with retailer + BD
- [ ] Add retailer to Capacity Allocation
- [ ] Close Jira ticket

---

## Onboarding a client that already exists in FAdmin

Open **Merchant Page > Details > Edit Merchant Information** and update as needed:
- Name — ensure Name Identifier has **no spaces**.
- Upload Logo and Storefront Logo (square `.jpg`, 60×60 to 120×120 px).
- Merchant website URL; Salesforce ID (from BD); SFTP credentials; store locator URL.
- If currently indexed, disable **"Flipp-Only?"**
- **Whitelist** the retailer so it appears in Flipp web search.
- **Mobile tab:** ensure "Use new mobile experience" is enabled.
- **Custom tab:** disable Show Simplified Pop (if enabled); set default chrome to
  **"flatsheet."**
- Add categories from the retailer's website.
- Assign yourself as **Lead**; confirm vendors via #osteam.

> **DO NOT un-check "Indexed?" at this stage of the process.**

Then apply the same **Workflow Settings** and **Flyer Type** steps as a new client.

---

## Indexed content — onboarding & disabling

Before indexing, confirm content is scrapable and does **not** fall into the
do-not-index categories:
- Content is from a competitor's hosted iframe.
- Content is not on the retailer's own domain but on a third party (Facebook,
  Adobe, blog domain).
- Content fails content policy: no shoppable items, advertises a service only,
  consistently too few items, or contains prohibited content.

If you doubt scrapability, file an **"Ops Request" FD ticket** (OS Eng confirms).
Otherwise proceed and get final confirmation after filing a **"New Indexer" FD
ticket**.

**Indexed merchant setup mirrors the direct flow, with one key difference:**
- **Relationship? → Indirect.** *(If this is not "Indirect," the retailer will
  not appear in Tesseract.)*
- Complete the remaining steps: determine task workflow, build Flyer Type, assign
  stacks, add stores, **file New Indexer ticket**, and **confirm the indexer is up
  and running**.

**What makes content ideal to index:** downloadable PDF/JPEG pages; valid dates on
the same page the flyer lives; same URL week over week; consistently meets content
policy. **Less ideal:** dates only on the flyer page(s) (needs extra QA — indexers
can't pull dates from pages); URL changes week to week; interactive/link-out pages
(case-by-case, e.g. Costco, Whole Foods).

**Requests to index new content come from** (most→least common) Business
Development (Flipp Lite / Tier 5), Customer Experience (user CX tickets), and
internal requests. Explore any option unless previously asked to stop indexing
that retailer.

**Flipp Lite (Tier 5):** low-cost indexed package, **minimum $500/month**. Ads get
daily live/valid-date/function checks by part-time staff. The participating-merchant
list ("Indexed Flipp Lite + Top 50" sheet) is maintained by the Skeleton Team via
**#flipplite** (no direct edit access).

**Support channels for indexing:**

| Channel | Purpose |
|---|---|
| #onboardings | OBQB team; onboarding questions (tag @QB) |
| #helpme-ops | Skeleton Team; confirm correct escalation for indexing issues (tag @SkeletonTeam) |
| #ops-stack-support | Support adjusting flyer-type stacks |

> The escalation path for indexing was noted as changing soon (indexing revamp in
> progress) — confirm the current process in the channels above.

See also `missing-flyers-and-indexing.md` and `indexing-ci-baseline-tasks.md`.

---

## Rebranding a retailer (manual changes)

**Prerequisites:**
- Confirm the go-live date of the rebrand before changing merchant name & logo.
- Request the updated merchant name and updated logos for both **Logo** and
  **Storefront Logo** fields (Details page).
- If the Hosted experience is moving to a different website, involve the account PT
  (or file a Technical Enablement (TE) Support Ticket) to determine whether new
  credentials are needed or the retailer reuses the same integration code — this
  depends on whether a **new name identifier** is generated. A new name identifier
  implies new SFTP credentials and a new codesheet config name.
- Confirm the new Hosted URL; if changing, update it in FAdmin and in the Account &
  Vendor Guides, and inform OS for live-check purposes.
- **File a Harmonization Troubleshooting (HTS) ticket** to determine whether to
  re-harmonize existing stores or ask Foursquare to rename stores.
  **DO NOT re-harmonize existing stores before confirmation — you will lose
  existing store trip reporting.**
- Connect with BD to confirm past-flyer reporting is unaffected (they check with
  the PIA team).
- Connect with Marketing to update the merchant name in push notifications.
- If the retailer has a US/Canadian counterpart with an account team, give that
  Ops team visibility.

**Day of the rebrand:**
- Update & live-check logos and name on **both Hosted and Flipp App/Web**.
- To reflect changes on the Storefront scrolling interface, **unmark Autostack
  Spotcheck / Spotcheck QC complete, then re-mark complete.**
- Live-check that the flyer is live on the correct Hosted URL and verify any other
  changes.

---

## Offboarding

**Offboard a retailer when:**
1. Ops has not received content in **6 months** (and the retailer is not seasonal).
2. The account team has had no communication / indication of assets in 6 months.
3. The retailer advises they will no longer send assets.

**If the account stops sending files:**
1. Notify the account team.
2. Advise the **Content Improvement team** to start assessing whether content can
   be indexed. Provide: Merchant Name, FAdmin Merchant ID, Merchant Website URL,
   and the **content cutoff date** (last day Flipp will have content).

**BD cutting a retailer for budget reasons:** processing stops if the retailer
won't meet the BD-proposed **Minimum Spend** (typically $2–5k monthly to stay
live). Stay looped in, ensure the Minimum Spend Operations Progress Tracker fields
are filled, and the Ops Lead should confirm via Slack that BD has notified Content
Improvement to assess indexing.

**Content becoming indexed** (cost-analysis initiative): BD reaches out to the Ops
Lead. Action items: confirm the indexer turn-on date with BD, confirm BD is filing
the indexer ticket (BD tells the retailer), and email the retailer confirming their
last processed publication and that you'll no longer be on the account (a template
is in the source doc — contacts/addresses omitted here).

---

*See also: `codesheet-errors.md`, `stores-and-harmonization.md`,
`missing-flyers-and-indexing.md`, `indexing-ci-baseline-tasks.md`,
`hosted-and-previews.md`, `publishing-and-go-live.md`, `escalation-and-tickets.md`.*

*Source: Confluence "Retailer Onboardings" (XPTCXE, 3129144452). Contacts/credentials
omitted. Last reviewed: 2026-07-15.*


---

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


---

# Account Flyer Review Directory — Reference

> **What this covers:** What the Account Flyer Review directory is and how
> processors use it. Source Confluence page id: 10670702896 (space XPTCXE).

The **Account Flyer Review** page is an **alphabetical directory of per-retailer
flyer-review documents**. Each entry links to that retailer's own Google Doc
(hosted in Google Drive), which holds the retailer-specific flyer-review /
processing notes for that account.

**How to use it:**
- Find the retailer alphabetically (A–Z) and open its linked doc for
  retailer-specific review guidance before processing or QC'ing that account's
  flyer.
- Some entries **share one doc** because the banners are grouped under a single
  merchant/account (e.g. *Albertsons Market / United Supermarkets / Market Street /
  Amigos United*; *Pet Valu / Total Pet / Tisol / Paulmac's Pets / Bosley's*; the
  SpartanNash family such as *Family Fare / D&W Fresh Markets / Martin's / VG's
  Grocery*). Follow the link rather than assuming one doc per banner name.
- A few retailers list multiple docs by content type (e.g. *Food 4 Less* has
  separate Adult Bev and Weekly Ad docs; *Lidl US* splits Weekly Ad and Magazine).

**Notes:**
- The directory itself contains **no processing procedure** — it is a navigation
  index. The actionable detail lives in each retailer's linked doc.
- Contents of the linked Google Docs are not stored in this knowledge base; open
  the source directory page for the current links.

---

*See also: `retailer-onboarding-process.md`, `codesheet-errors.md`,
`common-live-flyer-issues.md`.*

*Source: Confluence "Account Flyer Review" (XPTCXE, 10670702896). Contacts/credentials
omitted. Last reviewed: 2026-07-15.*


---

# Coupon Ops Daily Queues — Verification, Item Matching & OS Match QC — Guide

> **What this covers:** The three linked Coupon Ops baseline tasks that form the
> coupon pipeline — **Coupon Verification**, **Item Matching**, and **OS Match
> QC** — including what each queue is, its daily target, and the risk items to
> watch. Sourced from Confluence pages 13536002653 (Coupon Verification),
> 13536002854 (Vendor Guide: Item Matching), and 13536003039 (OS Match QC).
>
> **Audience:** Coupon Ops team and OS vendors.

---

## Pipeline order

These three tasks run in sequence. **OS Match QC** explicitly lists **Coupon
Verification** and **Item Matching** as its prerequisites:

1. **Coupon Verification** — verify incoming coupons (assign brands) so they are
   eligible to be matched.
2. **Item Matching** — match flyer items to the verified coupons.
3. **OS Match QC** — QC the matches for discrepancies flagged by OS.

All three queues **should be cleared by EOD every day.**

---

## 1. Coupon Verification

**What it is:** The most important baseline task. Coupons arrive in FADMIN via
multiple feeds and **must be verified before they can be matched** to flyer
items. Queue: `admin.flipp.com/coupons/next_to_verify`.

**Target:** Clear the queue by EOD every day.

**Risk items and how to mitigate:**

| Risk | Detail / fix |
|---|---|
| **Incorrect brand and/or not all brands assigned** | The correct brand(s) must be assigned so all possible item matches are gathered for matching and L2ID badging. For a **multi-brand coupon, assign all brands.** |
| **Brand not in system** | Brands must be added to coupons and each brand must be tied to a manufacturer. In some cases you must **create a new manufacturer and a new brand** before you can assign it. |

**Exceptions — Meijer coupons** follow the same general process, with two
differences:
- **Storewide is allowed** (e.g. "10% off general merchandise"). *Note: Family
  Dollar can also have storewide coupons.*
- **Final Price = Disallowed**, and **High Risk = No**.

---

## 2. Item Matching

**What it is:** The process where items from flyers are matched to applicable
coupons. Executed by **OS** and monitored by the Coupon Ops team so thresholds
are not exceeded.

**Target:** Match items as soon as they are added to the Item Matching queue;
ideally the queue is cleared by EOD every day.

**Matching rules** consider **brand, type of item, sizing, and exclusions.**
(An OS Decision Chart for Matching accompanies the source page.)

**Watch for common name variations** — the same product category appears under
many labels. Match across all of these:

- **Toilet Paper** = Bathroom Tissue / Bath Tissue / Toilet Tissue
- **Dish Detergent** = Dishwashing Liquid / Liquid Dish Detergent / Dish Soap /
  Dish Liquid. *Note: Dawn Dish Detergent may be labelled "Dawn Ultra"; Gain
  also has a "Gain Ultra" dish detergent.*
- **Fabric Softener** = Fabric Conditioner / Fabric Enhancer / Liquid Fabric
  Softener / Liquid Fabric Conditioner / Liquid Fabric Enhancer
- **Dryer Sheets** = Fabric Softener Sheets / Fabric Softener Dryer Sheets /
  Fabric Sheets
- **In-Wash Scent Booster** = In-Wash Fragrance Booster / In-Wash Scent Booster
  Beads / Laundry Scented Beads / Laundry Scented Booster / Fragrance Booster /
  Scent Booster Beads / Scent Booster
- **Invisible Spray** = Dry Spray / Body Spray / Antiperspirant / Deodorant
- **Clear Gel** = Antiperspirant / Deodorant

---

## 3. OS Match QC

**What it is:** A queue populated by coupons that have an **item-match
discrepancy flagged by OS.** Owned by the Coupon Ops team.

**Target:** Both the Coupon Item Match and OS Match QC queues should be cleared
by EOD every day.

**Risk items and mitigation:**

| Risk | Mitigation |
|---|---|
| **Incorrect items matched to a coupon** | Thoroughly read all inclusions and exclusions (size, type, count); Google items when unsure what they are or what size (e.g. loads vs. oz for laundry items); run the OS Accuracy Check. |
| **Not all applicable items matched to a coupon** | Run the OS Accuracy Check. |

**Prerequisites before starting:** Coupon Verification and Item Matching.

---

## See also
- `coupon-accuracy-checks.md` — the downstream False Positive / False Negative
  audit of live coupon matchups on Flipp Web and hosted sites.
- `escalation-and-tickets.md` — where to raise issues that need dev/config help.

---

*Source: Confluence "Copy of Coupon Verification" (VEN, 13536002653), "Copy of
Vendor Guide: Item Matching" (VEN, 13536002854), and "Copy of OS Match QC" (VEN,
13536003039). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Coupons Accuracy Checks — QC SOP

> **What this covers:** How to audit the quality of live coupon matchups on
> Flipp Web and hosted retailer sites — checking for both **False Positives**
> (wrong matchups) and **False Negatives** (items with a call-to-action that are
> missing a coupon badge). Sourced from Confluence page 8733982776.
>
> **Audience:** OS vendors / Coupon Ops. **Cadence:** every **Thursday and
> Sunday**. Start **no earlier than 5 AM ET**; notify Coupon Ops by email that
> the check is complete by **9 AM ET** (addresses in the source doc).

---

## Setup

- The Coupon Ops team pastes weekly templates into the **OS Coupon Accuracy
  Checks** spreadsheet. Each flyer listed must be checked for **both** False
  Positives and False Negatives; record both results in the same template.
- **Recommended method:** complete the False Positive and False Negative checks
  for one flyer before moving to the next.
- Open a browser to Flipp.com and enter the **ZIP code** of the flyer being
  checked. Search the merchant; if more than one flyer is available, open them
  all and match the **Flyer Type** in the URL to the template.
  - The Flyer Type is the segment **after** the retailer name. Example —
    CORRECT: `flipp.com/en-us/agawam-ma/weekly_ad/7864488-walgreens-weekly-ad?`
    (the `weekly-ad` after the name). Do not read the `weekly_ad` path segment
    before the ID.
  - **If the Flyer Type is listed as `(HOSTED SITE)`**, do the check on the
    retailer's own website instead: open the site, enter the listed ZIP, select
    the first store location, and open the **newest** weekly flyer. (Hosted
    retailers include Food Lion, Stop & Shop, Giant Carlisle, Martin's Foods,
    Giant Landover, Family Dollar.)

---

## False Positive check (are the existing matchups correct?)

1. **Count the matchups.** Open the flyer for the correct Flyer Type. Find items
   with coupon badges; for each, open the item, scroll down, and count all
   coupons matched to it. Record the total in the template under **"# of
   Matchups"**.
2. **Verify each matchup.** Open each badged item and apply the item-matching
   rules — **brand, type of item, sizing, and exclusions** — to decide whether
   each coupon is correctly matched. A matchup is a **False Positive** when the
   item's size/count falls outside the coupon's stated sizing. Examples:
   - Item size 90 oz. not within coupon sizing (25 oz, 40–60 ct, 9.7 oz) → FP
   - Item size 20 lbs. not within coupon sizing (12 lb – 13.5 lb) → FP
   - Item count 4 pk. not within coupon sizing (6 to 12 pk.) → FP
3. Repeat until all matchups on the flyer are evaluated; record each error.

**How to record a False Positive** — fill in: **Merchant, Issue, Flyer ID,
Flyer Item ID, Coupon ID.**
- **Flyer ID** — in the flyer URL with no item open.
- **Flyer Item ID** — in the URL once an item is opened.
- **Coupon ID** — click "Clipping/Redemption Help", then read it from the URL.
- **For hosted-site retailers:** record the **Item Name** under Flyer Item ID
  and the **coupon text** under Coupon ID.

---

## False Negative check (are any CTA items missing a badge?)

1. **Count and document the number of CTAs (calls-to-action)** in the flyer.
   Refer to each merchant's CTA definitions in their account-specific L2ID
   Vendor Guide. Record the total under **"Total # of CTAs in Flyers"**.
2. **Record any flyer item that has a CTA but no coupon badge** on it.

**How to record a False Negative** — fill in: **Merchant, Issue, Flyer ID, Flyer
Item ID.**
- **Flyer ID** — flyer URL with no item open.
- **Flyer Item ID** — URL with the item open.
- **For hosted retailers:** you do **not** need the Flyer ID. Record the **page
  number** where the item was found, plus the **Item Name** (click "Details" to
  open the item pop, copy the name) under Flyer Item ID.

---

## See also
- `coupon-ops-verification-matching-qc.md` — the upstream verification and
  item-matching tasks (and the full item-matching rules) that these checks audit.
- `escalation-and-tickets.md` — for issues needing dev/config follow-up.

---

*Source: Confluence "[NEW] Coupons Accuracy Checks" (VEN, 8733982776).
Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

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


---

# Alert Runbooks — On-Call Reference

> **What this covers:** On-call/alert runbooks for three content-pipeline
> alerts: **Content Sieve — flyer items unpublished > 1 day**, the **Home Depot
> Canada (HDCA) DVM module**, and the **Live Flyer Check**. For each: what the
> alert means, how to investigate, and how to resolve. Grounded in Confluence
> pages 12697240306 and 11691786294 (space CTLR) and 13564379282 (space RT).
>
> **Audience:** On-call engineers and content-platform staff. This is more
> engineering/on-call oriented than the processor-facing articles.
>
> **See also:** `storefront-publishing-errors.md` (holds a shorter Live Flyer
> Check summary), `content-v2-and-publishing.md`, `publishing-and-go-live.md`,
> `missing-flyers-and-indexing.md`, `escalation-and-tickets.md`.

---

## 1. Content Sieve — Flyer Items unpublished for more than a day

**Alert name:** `Content Sieve - Flyer Items are unpublished for more than a day`
**Priority:** P2 — lost revenue from missing searchable flyer items.

**What it means:** Content Sieve continuously polls for eligible flyer items to
publish to the `Eventification.FlyerItems` topic, joining `Merchants`,
`Flyer Runs`, `Flyers`, `Page Items` and `CrowdCuration Flyer Items` from their
Kafka topics. When items sit at `READY_FOR_PUBLISHING` for more than a day, the
Datadog monitor fires (there is also a **Content Sieve Lag** monitor).

**Potential impact:** Flyer items would not be available in Search and IMS.

**Key references:** service repo `wishabi/content-sieve`; event emitter
`app/lib/jobs/flyer_run_check.rb`; Prime Radiant service
`content-sieve-consumer`; consumer group in Lenses
(`content-sieve-consumer`). (Dashboard/monitor/log links in the source doc.)

### Investigation

1. **Verify the alert** by running the `FlyerRunCheck` query. Note the
   `flyers.available_to >= NOW()` filter — only currently-active flyers are
   returned; items with expired flyers can never be published and should not be
   investigated here.

   ```sql
   SELECT DISTINCT `flyer_items`.`flyer_run_id`
   FROM `flyer_items`
       INNER JOIN `page_items` ON `page_items`.`id` = `flyer_items`.`page_item_id`
       INNER JOIN `flyer_runs` ON `flyer_runs`.`id` = `flyer_items`.`flyer_run_id`
       LEFT OUTER JOIN `flyers` ON `flyers`.`id` = `flyer_items`.`flyer_id`
   WHERE `flyer_runs`.`state` = 'ops_complete'
     AND `flyer_runs`.`available_to` >= CURDATE()
     AND `flyer_items`.`publish_status` = 'READY_FOR_PUBLISHING'
     AND `flyer_items`.`updated_at` < DATE_SUB(NOW(), INTERVAL 1 DAY)
     AND `flyers`.`id` IS NOT NULL
     AND `flyers`.`available_to` >= NOW();
   ```

2. **Check publishing lag** — this query should return **no** row with
   `flyer_items.updated_at >= 1 day ago`:

   ```sql
   SELECT count(*) FROM flyer_items FORCE INDEX(index_flyer_items_on_publish_status)
   INNER JOIN `flyers` ON `flyers`.`id` = `flyer_items`.`flyer_id`
   INNER JOIN `flyer_runs` ON `flyer_runs`.`id` = `flyer_items`.`flyer_run_id`
   INNER JOIN `page_items` ON `page_items`.`id` = `flyer_items`.`page_item_id`
   INNER JOIN `merchants` ON `merchants`.`id` = `flyer_items`.`merchant_id`
   WHERE `flyer_items`.`publish_status` = 'READY_FOR_PUBLISHING'
     AND `flyer_runs`.`state` = 'ops_complete'
     AND `flyers`.`available_to` >= NOW() LIMIT 2000;
   ```

   (A fuller row-level variant selecting the joined item/page/flyer/merchant
   columns is in the source doc.)

3. **Confirm recent output** — messages published to `Eventification.FlyerItems`
   in the last few hours:

   ```sql
   USE `kafka`;
   SELECT * FROM Eventification.FlyerItems where _meta.timestamp > NOW() - '4h' LIMIT 100;
   ```

4. **Confirm the consumer has active connections** to the cluster (Lenses
   consumer group `content-sieve-consumer`).

5. **Identify missing joins** — each of these should ideally return **no**
   results. Missing rows mean upstream content never landed:
   - **Merchants:** `LEFT JOIN merchants ... WHERE merchants.id IS NULL`
   - **Flyer Runs:** `LEFT JOIN flyer_runs ... WHERE flyer_items.flyer_run_id IS NULL`
   - **Flyers:** `LEFT JOIN flyers ... WHERE flyer_items.flyer_id IS NULL`
   - **Page Items:** `LEFT JOIN page_items ... WHERE flyer_items.page_item_id IS NULL`

   (Full SQL for each in the source doc; all filter on
   `publish_status = 'READY_FOR_PUBLISHING'` and active flyers.)

### Resolution

1. Use the join queries above to determine if upstream content is missing.
2. Republish the missing upstream content (see the Rails-console section below).
3. If a topic/partition has stalled, follow **Stuck partition / consumer
   offset** below.
4. **Missing merchant record** (Step 5 Merchants returns IDs with no
   `merchants` row): the `Merchants.Merchant` Kafka message was never published
   or failed to upsert.
   - Check whether the merchant exists in fadmin.
   - Verify it is a Canadian or American merchant (merchant-admin edit page).
   - If it exists, trigger a **republish of the merchant** to the
     `Merchants.Merchant` topic **from merchant-admin** (not fadmin — fadmin has
     no `Merchants.Merchant` producer). content-sieve-consumer will ingest it,
     and the poller publishes the affected flyer items on the next cycle.
   - If the merchant does **not** exist in fadmin, the content cannot be
     recovered. Silence the alert by moving the items to a terminal status:

     ```sql
     UPDATE flyer_items
     SET publish_status = 'UNPUBLISHABLE'
     WHERE merchant_id IN (<affected_ids>)
       AND publish_status = 'READY_FOR_PUBLISHING';
     ```

5. Republish the affected flyer items.

### Republishing from the fadmin production Rails console

Several resolution steps ("republish page items / flyer items") run from the
**fadmin production Rails console**. It re-emits upstream content to the topics
content-sieve consumes (`Flyers.PageItem`, `Flyers.FlyerItem`).

The console runs on the `fadmin` web pods in the `services-eks-prod` EKS cluster
(us-east-1, namespace `fadmin`). Exec into a `fadmin-*` pod (container `fadmin`)
via k9s or kubectl and start the console. `RAILS_ENV` is **not** set in the
container, so pass it explicitly or Rails won't boot as production:

```shell
POD=$(kubectl --context fadmin-prod get pods -l app=fadmin -o jsonpath='{.items[0].metadata.name}')
kubectl --context fadmin-prod exec -it "$POD" -c fadmin -- env RAILS_ENV=production bundle exec rails console
# or, once shelled into the pod:
RAILS_ENV=production bundle exec rails console
```

This is **production** (`fadmin_production`): reads are safe; any producer call
or write hits live data. Use the `fadmin-*` web pods, **not** `delayed-jobs-*`
pods. For read-only poking, `rails console --sandbox` rolls back on exit. (The
staging console uses a different pod label and `RAILS_ENV` — see the source
doc's staging-access page.)

**Republish page items** (content-sieve joins on page items, so this is the
usual recovery lever). Producer `Kafka::Producers::PageItemProducer` → topic
`Flyers.PageItem`. `send_events` always emits for the records passed (no
dirty-check), so it is safe for manual recovery:

```ruby
# one or more page items by id
Kafka::Producers::PageItemProducer.send_events(PageItem.where(id: PAGE_ITEM_IDS))

# every page item in a flyer run, batched
PageItem.where(page_id: FlyerRun.find(FLYER_RUN_ID).page_ids).ids.in_groups_of(100) do |group|
  Kafka::Producers::PageItemProducer.send_events(PageItem.where(id: group.compact))
end
```

**Republish flyer items.** Producer `Kafka::Producers::FlyerItemsProducer` →
topic `Flyers.FlyerItem`:

```ruby
# one or more flyer items by id
Kafka::Producers::FlyerItemsProducer.send_events(FlyerItem.where(id: FLYER_ITEM_IDS))

# all flyer items on a flyer, batched
Flyer.find(FLYER_ID).flyer_items.in_groups_of(100) do |group|
  Kafka::Producers::FlyerItemsProducer.send_events(group.compact)
end
```

### Stuck partition / consumer offset

A partition can get pinned on a single offset that never advances — the
**Content Sieve Lag** monitor fires, and Lenses shows the consumer group's
committed offset on one partition not moving.

**How to recognize it:**
- In Lenses, one partition's committed offset is frozen while lag climbs.
- In CloudWatch, the **same entity** (same `id` / `message_id`) is reprocessed
  every few minutes, each time on a **different** `container_id`, often
  interleaved with a rebalance storm (`Timed out while waiting for response` on
  `join_group`/`sync_group`, `Kafka::RebalanceInProgress`).

**Root-cause pattern:** The consumer only republishes flyer items when a
**monitored attribute** of the incoming message differs from the stored row
(`app/lib/utils/flyer_item_updater.rb#monitored_attributes`):

| Model | Monitored attributes |
| --- | --- |
| `Merchant` | `large_image_path`, `storefront_logo_url`, `translations` |
| `Fadmin::Flyer` | `language`, `available_to`, `available_from`, `valid_to`, `valid_from` |
| `Fadmin::FlyerRun` | `state` |

The whole batch is consumed in **one transaction**. If a monitored attribute
differs, the consumer fires `republish_flyer_items`. If that republish can't
commit (lock contention / deadlock / the member is kicked mid-batch and
rebalances), the **entire batch rolls back** — so the differing attribute is
never persisted, the diff never resolves, and the offset never advances. The
redelivered message hits the same diff and loops indefinitely.

**Resolution:**
1. From Lenses, get the message at the stuck offset; pull the corresponding row
   from the Content Sieve DB.
2. Diff the **monitored attributes** for that model (table above) — find the
   field that differs between the Kafka message and the DB row.
3. Align the DB row to the message so the diff disappears, e.g. (merchant
   translations diff):

   ```sql
   UPDATE merchants
   SET translations = '<exact JSON from the Kafka message>'
   WHERE id = <merchant_id>;
   ```

   On the next consume the dirty-check comes back empty → no republish → the
   batch commits cheaply → the offset advances.

4. **If you get** `Lock wait timeout exceeded`, a long-running consumer
   transaction (the stuck batch itself) is holding the row lock. Find and kill
   it, then immediately re-run the `UPDATE`:

   ```sql
   SELECT trx_id, trx_state, trx_started,
          TIMESTAMPDIFF(SECOND, trx_started, NOW()) AS age_s,
          trx_mysql_thread_id AS thread_id,
          trx_rows_locked, trx_rows_modified, LEFT(trx_query, 200) AS query
   FROM information_schema.innodb_trx
   ORDER BY trx_started ASC;          -- oldest / highest rows_locked is the culprit
   KILL <thread_id>;
   ```

   Killing it just rolls back the batch that was failing anyway. After the kill,
   Kafka must rebalance before another consumer re-reads the offset — that's
   your window.

A heavy `republish_flyer_items` (large merchant/flyer/run) is what makes this
loop likely. PR #68 switched `republish_flyer_items` from per-row `update!` to
bulk `update_all` to shrink the deadlock window.

**Verify:** publishing lag reduced; consumer lag on ingested topics reduced;
messages appear on `Eventification.FlyerItems`; the Lenses offset advances past
the stuck offset; the `Changed attributes <Model> <id>` / `Updating flyer items`
CloudWatch lines for that entity stop recurring.

**Notable past occurrences:**
- *2026-05-11* — flyer_runs 1207647/1207648: missing merchant 7321 (absent from
  fadmin and Kafka). flyer_runs 1062812/1139066: flyer expired Sept 2025.
  Fixed the verification query and Step 5a SQL bug, and tightened the
  `FlyerRunCheck` window from `6.months.ago` to `Time.zone.now`.
- *2026-06-09* — `Merchants.Merchant` partition 3 stuck at offset 1695430 on
  merchant 1976 (Familiprix): DB `translations` carried a stale `es` locale
  absent from the message → merchant flagged "changed" on every redelivery →
  per-row `update!` republish deadlocked against the poller and never committed
  → offset looped + rebalance storm. Aligned `merchants.translations` to the
  message (after `KILL`-ing the transaction holding the row lock). Root-cause
  fix: PR #68.

---

## 2. Home Depot Canada (HDCA) DVM module — On-Call Runbook

**Module type:** Top Offers + Weather Signals (Phase 2). Slack channel
`#thdca-dvm`.

**Overview:** The HDCA DVM module delivers dynamically rendered promotional
content on Flipp's Hosted and App channels. Phases:
- **Phase 1 – Top Offers:** live since 2026-03-26 (Hosted).
- **Phase 2 – Weather Signals:** live since 2026-04-16 (Hosted & App).

Data flows daily: retailer-supplied local feed → **AMP Production ingestion** →
**DVM rendering**. Hourly audits post results to `#dvm-rendering-incidents`;
feed-ingestion failures surface in `#content-feeds-support` via Datadog alerts.

**Module schedule (EST):**

| Ingestion job | Scheduled time | Notes |
| --- | --- | --- |
| PRODUCT ingestion | ~10:10 AM | Must complete before OFFERS |
| OFFERS ingestion | ~10:30 AM | Depends on the PRODUCT run |
| Feed file expected by | ~10:00–10:15 AM | Late delivery is the #1 cause of incidents |
| Audit checks | Hourly | Results post to `#dvm-rendering-incidents` |

**Monitoring:**
- Datadog alert in `#content-feeds-support` → feed ingestion failed or feed file
  not received.
- Audit check fails in `#dvm-rendering-incidents` → module has missing or 0
  offers; may indicate ingestion didn't run.

### Troubleshooting playbook

1. **Identify the alert.** Check `#dvm-rendering-incidents` for hourly audit
   failures and `#content-feeds-support` for Datadog feed-ingestion alerts
   tagged to Home Depot Canada.
2. **Check if the feed file was delivered.** The most common root cause is HDCA
   delivering the feed file *after* the ingestion scheduler ran (expected by
   ~10:00–10:15 AM EST).
   - Check whether the feed file exists in the expected S3 location (ask AMP eng
     / feeds support if you lack AWS access).
   - **Not yet present:** wait and monitor; escalate to the Partner Technology
     Manager or the HDCA contact if the file is more than 2 hours late.
   - **Present but not picked up:** proceed to step 3.
   - **Known pattern:** HDCA often uploads after the scheduled ingest time
     (10:47 AM observed on 2026-05-28); the job has already run and missed the
     file, so a manual re-run is required.
3. **Manually restart ingestion.** Tag `@amp-prod-eng` (or the AMP feed-ingestion
   engineers) in `#content-feeds-support`:
   - Restart **PRODUCT ingestion** first.
   - Once PRODUCT completes, restart **OFFERS ingestion**.
   - Confirm the feed configs are re-run (reply to the Datadog alert thread).
4. **Verify the module is live.** Check the next hourly audit in
   `#dvm-rendering-incidents` to confirm the module is populating with offers;
   you can also verify via the module URL / test environment.
5. **Check the module schedule.** If the module is expected live but isn't,
   verify the current flyer-run dates/schedule on the *DVM Partner: Home Depot
   CA Modules* page (Confluence RT 13052313621). The module is only live during
   active flyer periods — expired offers won't show even if ingestion is
   healthy. If the module isn't scheduled to be live (between flyer runs),
   missing offers have **no user impact** — confirm before escalating
   externally.
6. **Escalate if unresolved.** If the issue persists after re-running ingestion:
   tag the Partner Technology Manager in `#thdca-dvm` with what was tried; loop
   in the Engineering Manager if eng investigation is needed; if HDCA data is
   the issue and the module is live, have Customer Success reach out to the HDCA
   contact.

**Recurring pattern:** HDCA feed delivery is inconsistent — files expected
before ~10:15 AM EST have arrived as late as 10:47 AM or not at all. Across
recent incidents (Mar–Jun 2026) the predominant root cause is **late feed-file
delivery by HDCA**. The AMP team is investigating a longer-term event-driven
ingestion trigger (vs. a fixed schedule).

**Reference tickets/links:** PPP-1119 (feed ingestion, AMP/CCOL); DR-358 / DR-280
(DVM Rendering epics); channels `#content-feeds-support`,
`#dvm-rendering-incidents`, `#thdca-dvm`. (Contacts in the source doc — not
stored here.)

---

## 3. Live Flyer Check

**Alert name:** `Live Flyer Check failed`. **Priority:** P2.

> A shorter version of this runbook already lives in
> `storefront-publishing-errors.md`. This section is the fuller reference.

**What it means:** Live flyers are not available in **FMS** (Flyer Metadata
Service). The alert fires when the live-flyer-check script detects a flyer is
not available in FMS.

**Potential impact:** Missing/unavailable flyers, potentially leading to lost
revenue.

**Reference:** GitHub Actions workflow `missing_flyers.yml` in
`wishabi/flyer-metadata-service-api`.

### Investigation

1. **Rerun** the *Missing Flyer Check* GitHub Actions workflow.
2. Check whether the alerted flyer IDs are **already known / intentionally
   ignored** — see *Suppressing known flyers* below before investigating
   further.
3. **Verify the flyer IDs are not in** the `production_fms_flyer_metadata`
   DynamoDB table. To show in the FMS dynamo table, a flyer must exist in both
   Kafka topics below:

   ```sql
   SELECT * FROM Eventification.Flyers
     WHERE _meta.timestamp > NOW() - "7d"
       AND _value.flyer.id IN ( 7972679, 7972680, 7972687, 7972688 );
   ```

   ```sql
   SELECT * FROM Flyers.Thumbnail
     WHERE _meta.timestamp > NOW() - "7d"
       AND _value.flyer_id IN ( 7972679, 7972680, 7972687, 7972688 );
   ```

   (The IDs above are examples — substitute the alerted flyer IDs.) A flyer
   missing here may need the Ops team pinged (`@enable-cxe`).
4. Investigate the flyer **eventification pipeline**.

### Resolution

1. **If the flyer is not in the database**, reduce the flyer run's `valid_to`
   and `available_to` in fadmin, then republish. Find the flyer run id:

   ```sql
   select id, flyer_run_id, available_to from flyers where id in () group by flyer_run_id;
   ```

   Then edit and **republish** the run at
   `fadmin.flippback.com/flyer_runs/{FLYER_RUN_ID}`.
2. **Check the flyer IDs in the pricing zones for errors** at
   `flyers.merchants.wishabi.ca/flyer_runs/{FLYER_RUN_ID}/pricing_zones`. If
   errors are found, notify the `content-public` channel.
3. Re-confirm the flyer now exists in both `Eventification.Flyers` and
   `Flyers.Thumbnail` topics (queries as in Investigation step 3).
4. **If it is in the database**, it's a **code issue** — investigate/escalate to
   engineering.

### Suppressing known flyers

Use when a flyer run is intentionally being ignored (mid-migration, known
processing delay) and the alert is expected noise. The check supports an
`IGNORED_FLYER_IDS` allowlist; any flyer ID in the list is excluded from the
missing-metadata check and will not alert.

**To add IDs:** in `wishabi/flyer-metadata-service-api`, go to **Settings →
Secrets and variables → Actions → Variables**, edit `IGNORED_FLYER_IDS` (a JSON
array of integers, e.g. `[7945656, 7945657]`), and save. The next hourly run
skips those IDs.

**To remove IDs:** edit `IGNORED_FLYER_IDS` and remove them (or set `[]` to
clear). **Always clear the allowlist once the issue is resolved** — suppressed
IDs will never alert even if they go missing for a different reason.

**Verify:** rerun the failing instance of the Live Flyer Check job.

**Notable past occurrences:** most resolutions were "edit dates with no real
change and resubmit/republish," which made the flyer appear in DynamoDB; some
were flyers still processing (message `content-public`); one (2026-05-22) was
intentional suppression via `IGNORED_FLYER_IDS` for flyers `7945656`/`7945657`
(allowlist feature added in PR #62).

---

*Source: Confluence "Alert Runbook: Content Sieve - Flyer Items are unpublished
for more than a day" (CTLR, 12697240306); "Home Depot Canada DVM Module —
On-Call Runbook" (RT, 13564379282); "Alert Runbook: Live Flyer Check" (CTLR,
11691786294). Contacts/credentials omitted. Last reviewed: 2026-07-15.*


---

# Home Depot Canada (HDCA) DVM Module — On-Call Runbook

> **Moved:** To avoid duplication, the full HDCA DVM module on-call runbook now
> lives in **[`alert-runbooks.md`](alert-runbooks.md) → Section 2 "Home Depot
> Canada (HDCA) DVM module"** (feed-ingestion schedule, the late-feed incident
> pattern, PRODUCT→OFFERS manual re-run, and escalation).
>
> This short stub remains so the runbook is still findable by retailer name.
> **See also:** the retailer guide `../retailers/home-depot-canada.md`, and
> `content-v2-and-publishing.md` (DVM is the active V2 distribution path).

*Source: Confluence "Home Depot Canada DVM Module — On-Call Runbook" (RT,
13564379282). Consolidated into `alert-runbooks.md`. Last reviewed: 2026-07-15.*


---

# Publisher QA (DSP / Off-App) — Superseded / Paused

> **What this covers:** Pointer to the Publisher QA SOP for off-app (DSP)
> publisher domains. Sourced from Confluence page 11424890881.

**Status: PAUSED — do not treat as current process.** As of 2026-04-22 the SOP
states the current process "does not drive value" and is **paused until the team
re-aligns**, pending ThoughtSpot automation discovery and an updated KPI set
(the intended direction is a **weekly Thursday** check keyed on Level-1
performance KPIs such as eCPM out of range, 0% item-interaction, served-but-not-
viewable impressions, and negative margin — not the former Monday/Thursday WoW
EV / clicker-rate flags).

Because the SOP is mid-revision, its step-by-step instructions (ThoughtSpot
export, forcing the Native X experience on direct integrations, ad-placement QC,
and the stakeholder email) are **not ingested here.** If you need this process,
confirm the current owner and revised SOP before following the source page.

*Source: Confluence "Publisher QA SOP Instructions - DSP" (VEN, 11424890881).
Contacts/credentials omitted. Last reviewed: 2026-07-15.*


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

> **Ask in Slack before filing a CLSD.** CLSD is for errors whose **system cause
> the CXE / Enablement team can't identify** — a quick Slack check with the
> Enablement team often resolves the issue or confirms that escalation is the
> right call.

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
| **Session** | An automated processing step on a run (image/tile generation, categorization, tagging, etc.). "Re-run sessions" is a common first fix. **Vendor tasks can also act as sessions** — re-running them kicks off item-level sessions. |
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
| **Touch Storefront Objects** | A FADMIN **custom action** that pushes changes to the storefront; worth trying when an item link/URL change isn't reflecting on the front-end. |
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
| **Content V2 / V2** | The newer **Global-Centric** content model (Offers, Products, Promotions, Publications with global IDs), replacing the **Flyer-Centric** V1 model. See `content-v2-and-publishing.md`. |
| **V1 (Flyer-Centric)** | The legacy content model where everything hangs off a flyer (`flyer_id`, `flyer_item_id`). Being migrated to V2. |
| **Publication** | V2 equivalent of a flyer — a curated, dynamic collection of displayable items; can be distributed per channel/place. A **Publication Plan** (queries + rendering) is "hydrated" into a **Publication Payload** (what the user sees). |
| **Section / Section Plan** | V2 equivalent of a flyer page; a subset of a publication that can have its **own distribution** and rendering. |
| **Offer** | V2 equivalent of a flyer item — a price/discount on one or more products for a period, for one retailer/language. **One Offer can map to many V1 flyer items.** |
| **Atom** | Parent type of **Offer** and **Promotion**; replaces the V1 "merchandise/items" concept. |
| **Promotion** | A V2 displayable ad (image + click action) with no specific product/offer (e.g. a store-opening ad). |
| **Product** | A purchasable thing sold at one retailer (V2 dimension). |
| **Global ID** | V2 identifier for content, independent of any flyer (vs V1 `flyer_id`/`flyer_item_id`). |
| **Distribution / Place** | V2 targeting: a **Distribution** targets a **Place** (postal code, **store**, FSA, polygon), a channel, or (future) a user segment. In V2, flyers distribute to **stores, not FSAs**. |
| **Nexus API** | The single V2 **entry point / source of truth** for incoming flyer content; Fadmin produces V2 print content into it. |
| **Curator** | The single V2 **serving source**; pulls items/publications/distributions and feeds all channels. |
| **Flyers-NG** | The V1 **compatibility layer** during the V1→V2 transition; converts V2→V1 on read so legacy App/Web/Hosted keep working. |
| **DVM** | The active V2 distribution path today (NativeX, retailer apps); built on the V2 model. |

*Last reviewed: 2026-07-22. Add terms as new articles are written.*

