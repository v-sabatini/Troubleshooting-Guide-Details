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
