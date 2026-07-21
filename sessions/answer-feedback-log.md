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
