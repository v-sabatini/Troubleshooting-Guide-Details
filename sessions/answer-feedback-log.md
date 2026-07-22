# Answer Feedback Log

A running record of **team vetting** of the CXE Help Center assistant's answers.
Reviewers test the bot and log corrections here; the owner applies fixes to the
source articles and marks each entry resolved.

**How to add an entry:** use the Reviewer/Vetting prompt (`prompts.md` #7) — Claude
will append entries for you — or add one manually with the template below.

**Status key:** 🔴 Open · 🟢 Applied to article · ⚠️ needs Vanessa (a point that can't be reconciled from the sources without her call)

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

### FB-002 — `NilClass` fix over-ranks "missing dates" as the #1 cause 🟢 Applied
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "A codesheet upload failed with `undefined method 'split' for nil:NilClass` — what do I check? What information do you need to diagnose?"
- **What the bot said:** Led with "a pricing-zone row missing start/end dates" as the **#1 cause** of `NilClass` errors (citing TOSS-7033), then PDF base path / zones with no pages, then filename/FTP rename mismatch.
- **What's actually correct / the issue:**
  1. **Dates are usually set automatically to match the run**, so a missing-dates row is actually the **least likely** cause — *unless* the specific codesheet processor being used is one that requires dates (e.g. a generic codesheet with no dates). It should not be presented as the #1/most-common cause.
  2. In the reviewer's actual case, the **PDF base directory was `/` (correct)** and **all pricing zones had pages** — so causes #2 in the answer did not apply either.
  3. The real cause was **page/file names in the codesheet not matching what was on the SFTP** (the filename-matching class of issue). This is the more common culprit and should be ranked first.
  4. **Process improvement:** the bot should **ask the user which codesheet processor / config is being used** before diagnosing, since the likely causes differ by processor (e.g. whether dates are required at all).
- **Article(s) affected:** `codesheet-errors.md` (section "1. `NilClass` errors" — the likely-causes ordering and the "#1 cause of NilClass errors" claim in the universal self-serve checklist, item 2).
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — reordered NilClass causes so filename/SFTP mismatch leads, demoted missing-dates to date-requiring configs, softened the "#1 cause" checklist wording, and added a "confirm which codesheet processor is in use" first step.

### FB-003 — `NilClass` on a `generic_stores` codesheet: PZ-name typo/space is the real #1, + missing troubleshooting technique 🟢 Applied
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
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — added a `generic_stores` store-assignment subsection to the NilClass guidance capturing points 1–5 (PZ-name typo/space as top cause, the "missing store code names itself, so not NilClass" clarification, hidden-space gotcha via Pricing Zone Page export, and the first-`0/0`-zone / Manage Stores locating technique).

### FB-004 — Page Tile Generation error: add "delete the whole track" workaround + Slack-first escalation 🟢 Applied · ⚠️ needs Vanessa (channel name)
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
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — added the whole-track-delete workaround (WHOLE-track-only + make-a-backup constraints, plus "check the Page Tile Generation task error for a specific page") and the Slack-first-before-CLSD step to `common-live-flyer-issues.md`; added a Slack-before-CLSD note to `escalation-and-tickets.md`.
  - ⚠️ **Needs Vanessa — channel name not reconciled.** The reviewer names **`#helpme-cxe`** (Enablement team); the existing articles reference **`#helpme-ops`** / `@enable-cxe`. To avoid introducing an inconsistency, the applied text says "ask the Enablement team in Slack" **without** committing to a channel. **Please confirm which channel is correct** so I can make it consistent across `common-live-flyer-issues.md`, `escalation-and-tickets.md`, and the tile-gen step.

### FB-005 — Vendor Tag QC errors between items: it's deleted pages/items, not auto-categorization (+ auto-cat can't be re-run) 🟢 Applied
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "Vendors flagged the Vendor Tag QC task isn't working — moving to the next item errors, and the processor gets the same effect starting the task from the flyer run pipeline. Why might this be?"
- **What the bot said:** Led with the documented **auto-categorization gap** cause (missing Google Categories → tag QC gets stuck), advised **re-running sessions** to populate categories and listing affected items, then reasoned it's a data problem on a specific item and told the user to **isolate which item** it dies on; CLSD as backstop.
- **What's actually correct / the issue:**
  1. **Correction — auto-categorization is NOT the likely cause here, and the article's remediation is wrong.** **Auto-categorization cannot be manually re-run.** And if it **doesn't assign a category, the item is still generally able to be tagged** — so a missing category does **not** block Tag QC. The existing "re-run sessions to see if categories populate" guidance is not actionable.
  2. **The more likely cause: one or more pages/items were DELETED before the Vendor tasks were completed.** The Tag QC task is then **looking for items/pages that no longer exist**, which is what errors when advancing. This fits the symptom (same failure for vendors and for the processor launching from the pipeline).
  3. **Diagnosis:** ask the user for the **task's error log** — it can reveal the deleted item/page more precisely.
  4. **Correction on my "isolate which item" advice:** the **user is unlikely to be able to identify the culprit item themselves.** If an error message points to it, use that; otherwise it's **fine to leave that identification to the CLSD team.** Don't send the processor hunting for it.
- **Article(s) affected:**
  - `common-live-flyer-issues.md` — **"Auto-categorization gaps (missing Google categories)"** entry: correct the claim that re-running sessions repopulates categories (auto-cat can't be manually re-run) and clarify that a missing category doesn't block tagging. **Add a new entry** for **Vendor/Tag QC task erroring when moving between items → likely a page/item deleted before Vendor tasks completed**, with "provide the task error log" as the diagnostic and CLSD as the unblock.
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — corrected the auto-categorization entry (auto-cat can't be manually re-run; a missing category doesn't block tagging; removed the "re-run sessions to repopulate" step) and added a new "Vendor / Tag QC task errors when moving between items" entry (likely a page/item deleted before Vendor tasks completed → pull the task error log → CLSD identifies the culprit, not the processor).

### FB-006 — Item import failed because of COLUMN ORDER; Help Center has no item-import file-format spec 🟢 Applied
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "I tried to do an item import but it failed. Look at the .csv and tell me why." (File `Test_Flyer_Item_Import__Sheet1.csv`, header row `item_id,name,sku,google_category_id`.)
- **What the bot said:** Called the CSV structurally clean; guessed the problem was the `google_category_id` column (claimed no documented import uses it, and that Google Category must be a name/path not a numeric ID like `319`); suggested dropping that column. Also flagged that the Help Center has no item-import format reference.
- **What's actually correct / the issue (multiple corrections + new spec to document):**
  1. **Wrong diagnosis — the real problem is COLUMN ORDER.** `item_id` **must be column 1 and `sku` must be column 2.** In the file the order was `item_id, name, sku, google_category_id`, so `sku` was in position 3 → import fails. (The bot also misread the column order, which is how it missed this.)
  2. **`google_category_id` IS a valid column header** — the bot was wrong to flag it. In FAdmin the Google Category is **displayed in words**, but the **backend ID is a numerical value**, so `319` is a legitimate value.
  3. **The retailer guides do NOT list all accepted import headers.** The full set of accepted column headers is:
     `analytics_categories, auto_play_video, bonus_offer_description, brand, brand_id, data_piping_url, deferred, description, disclaimer_text, display_type, display_url, external_override_image_source_url, feature_html, google_category_id, id_1, id_2, id_3, id_4, id_5, id_6, iframe_display_height, iframe_display_width, in_store_only, item_corrections, item_side_list_url_text, keywords, name, overlay_url, page_destination, play_video_inline, pre_price_text, price_text, qualifying_quantity, raw_current_price, raw_dollars_off, raw_original_price, raw_percent_off, reward_quantity, sale_story, sku, url, valid_from, valid_to, video_sound_on, youtube_embedded_url`
     (plus `item_id`). **Required order:** `item_id` = column 1, `sku` = column 2.
  4. **Language prefixes:** you can prepend **`english_`** or **`french_`** to any field so it applies only to English or French items. Example: `"item_id","sku","english_url","french_url","keywords"`.
  5. **Date columns** (e.g. `valid_from`, `valid_to`) **must be in `YYYY-MM-DD` format.**
  6. **To save a value as a blank string**, put **`*blank*`** as the cell contents.
- **Article(s) affected:** **New article needed** — there is no item-import file-format reference in the Help Center. Create one (e.g. `docs/knowledge-base/item-import-format.md`) capturing points 1–6: required `item_id`/`sku` column order, the full accepted-header list, `english_`/`french_` prefixes, `YYYY-MM-DD` date format, and the `*blank*` convention. Also add "wrong column order (item_id/sku not in positions 1/2)" as a documented item-import failure cause.
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — created `docs/knowledge-base/item-import-format.md` capturing points 1–6 (required `item_id`/`sku` column order, full accepted-header list, `google_category_id` is valid/numeric, `english_`/`french_` prefixes, `YYYY-MM-DD` dates, `*blank*` convention) plus "wrong column order" as a documented failure cause; cross-linked from `codesheet-errors.md` and `common-live-flyer-issues.md`; added to the index and the NotebookLM KB bundle.

### FB-007 — Item import requires a minimum of 3 columns 🟢 Applied
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "I'm trying to do a SKU update. I have a column with item_ids and a column with SKUs, in the correct order. Why isn't it working?"
- **What the bot said:** Suggested (1) SKU values mangled by the spreadsheet into scientific notation / commas (documented gotcha), (2) header names not exactly `item_id`/`sku`, (3) blank cells needing `*blank*` to clear. Asked whether it errors vs. runs but doesn't change SKUs.
- **What's actually correct / the issue:** SKU formatting (cause 1) was correctly formatted in this case, though it's a valid thing to keep in mind, and causes 2–3 are worth pointing out. **The real cause the knowledge base is missing: an item import requires a MINIMUM of 3 columns.** A two-column file of just `item_id` + `sku` will not run. You need `item_id`, `sku`, **and any third column — even if it is entirely blank.** Example: adding a blank column with just the header `url` (no values) would likely have let it run.
- **Article(s) affected:** The planned item-import format article (see FB-006). Add the **minimum-3-columns** requirement: `item_id` (col 1), `sku` (col 2), plus at least one more valid header column (may be empty). Note this applies to SKU-update imports specifically (two-column item_id + sku files fail).
- **Owner action:** ✅ Applied 2026-07-22 (commit `6e5da2b`) — documented the 3-column minimum in `item-import-format.md` (rule 2: `item_id` + `sku` alone won't run; add at least one more valid header column, which may be empty), with a matching row in the common-failures table.

### FB-008 — Link/URL not reflecting on front-end: name the specific sessions/actions to re-run 🟢 Applied
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "I updated an item's link but it isn't reflecting on the front end (Hosted) — what can I try?" → follow-up: "What are the 'relevant Sessions' to rerun?"
- **What the bot said:** Rule out a false alarm (processing/caching), run the standard loop (re-run relevant sessions → republish), try the re-save nudge, escalate to Hosted (HS) if it won't reflect. On the follow-up, flagged that the Help Center **defines "session" generically but never names which session maps to a link/URL update**, and reasoned that image/tile/categorization sessions wouldn't carry a link so republish was the operative step.
- **What's actually correct / the issue (fills the gap — new content):** For a link/URL not reflecting on the front end, the specific things to re-run/try are:
  1. **Item Cutout Generation session** — tasks **downstream of** the item cutout generation session can be re-run to make it **re-kick off**.
  2. **Vendor tasks act as sessions** — they can be re-run, and doing so **kicks off item-level sessions**. So suggesting a Vendor-task re-run is valid.
  3. **Republish** — a correct option to try (already covered).
  4. **`Touch Storefront Objects` custom action** — a custom action that can be tried to push the change to the storefront. (New — not currently in the KB.)
- **Article(s) affected:** `publishing-and-go-live.md` ("New boxes / items / links not reflecting on front-end" — add these concrete re-run/actions before the HS escalation) and `common-live-flyer-issues.md`. Also worth noting in `glossary.md` that **Vendor tasks can behave as sessions that kick off item-level sessions**, and adding the **`Touch Storefront Objects`** custom action.
- **Owner action:** ✅ Applied 2026-07-22 (commit `09a805a`) — expanded the "New boxes / items / links not reflecting on front-end" fix in `publishing-and-go-live.md` with the ordered steps (re-run Item Cutout Generation via a downstream task, re-run Vendor tasks as sessions, republish, `Touch Storefront Objects` custom action); added a matching "Link / URL not reflecting on the front-end" entry in `common-live-flyer-issues.md`; and added the Vendor-tasks-as-sessions note plus a `Touch Storefront Objects` term to `glossary.md`.

### FB-009 — Page swap not on front end: Track-ID cause mis-cited; wrong escalation routing; add undo/redo workaround 🔴 Open
- **Date / reviewer:** 2026-07-21 / Hannah S-K
- **Question asked:** "I made a page swap but it's not appearing on the front end. What can I try?"
- **What the bot said:** Rule out false alarm; re-run **page stitching** + republish; **check the swapped page has a Track ID** (citing missing-flyers-and-indexing.md Cause 4 / OTS-1954, claiming a page missing a track ID is excluded from tile gen); re-run tile gen after confirming the track ID; escalate to the **Hosted team (HS)** if page stitching doesn't fix it or if it's Hosted-only.
- **What's actually correct / the issue:**
  1. **Track ID correction + mis-citation.** Track IDs are **automatically assigned at upload.** If one is genuinely missing, the fix is to **go back to the Upload page and hit "Save and Complete."** This is **very rare for a page swap**, because the person doing the upload couldn't have added the page into any pricing zones to make the revision without it. **The cited ticket (OTS-1954 / Cause 4) does NOT involve page revisions at all** — it's about the **upload step going awry**, so citing it for a page-swap-not-appearing is a misapplication. Don't lead a page-swap answer with the track-ID cause.
  2. **Escalation routing correction (recurring).** For an issue affecting the front end **everywhere** (not Hosted-specific): escalate to **`#helpme-cxe` first, then CLSD** if it's broken everywhere on the front end. **The Hosted team (HS) is only for Hosted-ONLY issues.** This question said "front end" (not Hosted-only), so HS was the wrong default — it should be `#helpme-cxe` → CLSD. **You can always ask the user to confirm** whether it's Hosted-only or everywhere.
  3. **New workaround to add:** **undo and redo the page swap** — this re-kicks all the relevant sessions, which may not have completed correctly the first time.
- **Article(s) affected:**
  - `missing-flyers-and-indexing.md` — clarify Cause 4 / OTS-1954 is about the **upload step**, not page revisions; note track IDs auto-assign at upload and the "Save and Complete on the Upload page" fix; note it's rare for a page swap.
  - `hosted-and-previews.md` / `publishing-and-go-live.md` escalation tables — correct routing: **front-end-everywhere → `#helpme-cxe` → CLSD; Hosted-only → HS**; and to confirm scope before routing.
  - Page-swap / post-live-revision guidance — add the **undo/redo the page swap** workaround (re-kicks relevant sessions).
- **Owner action:** Fix the mis-cited track-ID guidance, correct the everywhere-vs-Hosted-only escalation routing, and add the undo/redo-page-swap workaround. 🔴 Not yet applied.
