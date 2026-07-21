# Answer Feedback Log

A running record of **team vetting** of the CXE Help Center assistant's answers.
Reviewers test the bot and log corrections here; the owner applies fixes to the
source articles and marks each entry resolved.

**How to add an entry:** use the Reviewer/Vetting prompt (`prompts.md` #7) — Claude
will append entries for you — or add one manually with the template below.

**Status key:** 🔴 Open · 🟢 Applied to article

---

## Template (copy for each new item)

```
### FB-00X — <short title> 🔴 Open
- **Date / reviewer:** YYYY-MM-DD / <name or initials>
- **Question asked:** <the question>
- **What the bot said:** <summary of the answer>
- **What's actually correct / the issue:** <reviewer's correction or note>
- **Article(s) affected:** <e.g. codesheet-errors.md>
- **Owner action:** <what to change; mark 🟢 once applied + note the commit>
```

---

## Entries

<!-- Newest at the top. Example format:

### FB-001 — Missing-flyer answer assumed indexed flyer 🟢 Applied
- **Date / reviewer:** 2026-07-15 / Vanessa
- **Question asked:** "A retailer's flyer is missing — what's the usual cause and who fixes it?"
- **What the bot said:** Defaulted to broken indexer → FD.
- **What's actually correct / the issue:** A processor asking this is usually on a
  *processed* (non-indexed) flyer; lead with processing/publishing causes, not the indexer.
- **Article(s) affected:** missing-flyers-and-indexing.md
- **Owner action:** ✅ Applied — added "processed vs indexed" split + processor-default section.

(The FB-001 example above is a real correction already applied; add new items below.)
-->

### FB-002 — `NilClass` fix over-ranks "missing dates" as the #1 cause 🔴 Open
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "A codesheet upload failed with `undefined method 'split' for nil:NilClass` — what do I check? What information do you need to diagnose?"
- **What the bot said:** Led with "a pricing-zone row missing start/end dates" as the **#1 cause** of `NilClass` errors (citing TOSS-7033), then PDF base path / zones with no pages, then filename/FTP rename mismatch.
- **What's actually correct / the issue:**
  1. **Dates are usually set automatically to match the run**, so a missing-dates row is actually the **least likely** cause — *unless* the specific codesheet processor being used is one that requires dates (e.g. a generic codesheet with no dates). It should not be presented as the #1/most-common cause.
  2. In the reviewer's actual case, the **PDF base directory was `/` (correct)** and **all pricing zones had pages** — so causes #2 in the answer did not apply either.
  3. The real cause was **page/file names in the codesheet not matching what was on the SFTP** (the filename-matching class of issue). This is the more common culprit and should be ranked first.
  4. **Process improvement:** the bot should **ask the user which codesheet processor / config is being used** before diagnosing, since the likely causes differ by processor (e.g. whether dates are required at all).
- **Article(s) affected:** `codesheet-errors.md` (section "1. `NilClass` errors" — the likely-causes ordering and the "#1 cause of NilClass errors" claim in the universal self-serve checklist, item 2).
- **Owner action:** Re-order likely causes so **filename/SFTP mismatch leads** and **missing-dates is demoted** (noting it mainly applies to codesheets that require dates); soften/remove the "#1 cause" wording in the checklist; add guidance to **confirm which codesheet processor is in use** as a first diagnostic step. 🔴 Not yet applied.

### FB-003 — `NilClass` on a `generic_stores` codesheet: PZ-name typo/space is the real #1, + missing troubleshooting technique 🔴 Open
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "I got the same [`NilClass`] error but with a `generic_stores` codesheet. Why?"
- **What the bot said:** Explained a `generic_stores` sheet only assigns stores to pricing zones, so the nil narrows to the store/PZ fields; listed causes: (1) wrong/missing `stores`/`pricing zone` headers, (2) blank cells / stray blank row, (3) PZ name not matching Fadmin, (4) store code the system can't find (add store at merchant level with SAP# as merchant code, re-run), (5) re-save CSV cleanly. Called #1/#3 the most likely.
- **What's actually correct / the issue:**
  1. **Correction — a missing/unfindable store code does NOT produce a `NilClass` error.** When the system can't find a store code it **names that specific store code in the error message**. So if the error is a `NilClass`, it's **probably not** a missing store code. This should be separated out from the `NilClass` causes.
  2. **The most common real cause is a PZ name in the codesheet that doesn't match Fadmin due to a typo** — and the typo can be **in the codesheet OR in the Fadmin pricing-zone name**. Rank this first.
  3. **Trailing / leading spaces** in the PZ name (again, either the codesheet or the Fadmin PZ name) are a very common miss. Getting a list of **both** to cross-reference is useful.
  4. **Important gotcha:** Fadmin's **Pricing Zone tab does not always display the extra space**, so processors need to either **click through into the zone to confirm**, or run the **`Pricing Zone Page` custom action** and export the resulting **.csv** to cross-reference against the codesheet.
  5. **Locating the bad zone (technique not in KB):**
     - If the codesheet added stores to zones **in the same order** as the Pricing Zone Page ordering, focus on the **first zone showing `0/0`** — the typo is there.
     - If the codesheet is **out of order**, pull the store list from **Overview > Manage Stores** and provide it (e.g. to the chat bot) to determine **where the codesheet stopped adding zones**, then check that zone for the typo.
- **Article(s) affected:** `codesheet-errors.md` (NilClass section — needs `generic_stores`/store-assignment guidance: PZ-name typo & leading/trailing space as top cause, the "missing store code names itself, so it's not NilClass" clarification, and the Pricing Zone Page / Manage Stores locating technique). Possibly cross-link from `stores-and-harmonization.md`.
- **Owner action:** Add a store-assignment (`generic_stores`) subsection to the NilClass guidance capturing points 1–5 above. 🔴 Not yet applied.

### FB-004 — Page Tile Generation error: add "delete the whole track" workaround + Slack-first escalation 🔴 Open
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "Page Tile Generation errored on one of my flyer's tracks. It's blocking the Final QC checklist task from generating. Will this keep my flyer from going live? How do I fix it?"
- **What the bot said:** Treat as go-live-blocking (FQC is a required gate); try first = re-run the tile/thumbnail generation session, wait for the queue, confirm upstream steps completed; if still broken file an **urgent CLSD** with the run link, the specific track, and that the errored task is blocking FQC. Inferred the blocker is the stuck task, not the whole flyer being dark.
- **What's actually correct / the issue:** Answer confirmed correct (**if the Final QC checklist is not completed, the flyer does not publish**). Two things to **add to the KB**:
  1. **"Delete the whole track" workaround.** If only **one track** is erroring, it may be worth asking whether that track can be **deleted** — e.g. if it's just a **revised page**, or **category pages added post-initial upload**.
     - ⚠️ **Only if the WHOLE track can be deleted.** **Partially** deleting a track causes downstream impacts — do not partially delete.
     - **Make a backup first.**
     - Deleting the erroring track (within those constraints) can **temporarily get the run into a state where FQC can proceed**; they can then **retry the upload of the erroring track**.
     - They can also **check the error message on the Page Tile Generation task** to see whether the problem is with a **specific page**.
  2. **Slack-first escalation.** Before filing a CLSD, they can **ask in `#helpme-cxe` on Slack** for department advice — specifically from the **Enablement team**. CLSD is for errors whose **system cause the CXE team cannot identify**; the Slack check comes first.
- **Article(s) affected:** `common-live-flyer-issues.md` ("Flyer tile generation error" — add the whole-track delete workaround + backup + check-error-for-specific-page, and the ask-in-Slack-before-CLSD step). Also `publishing-and-go-live.md` and `escalation-and-tickets.md` for the Slack-before-CLSD step.
- **⚠️ Discrepancy to reconcile:** Reviewer names the Slack channel **`#helpme-cxe`** (Enablement team). `common-live-flyer-issues.md` (intro) currently references **`#helpme-ops`** ("to the Enablement pod / `@enable-cxe`"). Confirm the correct channel name and make it consistent across articles.
- **Owner action:** Add the whole-track-delete workaround (with the WHOLE-track-only + backup constraints) and the Slack-first escalation step; reconcile the `#helpme-ops` vs `#helpme-cxe` channel name. 🔴 Not yet applied.
