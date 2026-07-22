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
