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
