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

## Cause 4 — Pages missing a track ID at upload / processing blocked

**Symptom:** Specific pages don't appear; processing is blocked because a page is
**missing a track ID**, so it's excluded from tile-generation sessions.
*(OTS-1954: re-running tile gen didn't help because untracked pages are excluded.)*

**Scope — this is an *upload-step* problem, not a page-revision one.** Track IDs
are **assigned automatically at upload**. OTS-1954 was a case of the **upload step
going awry**; it does **not** involve page revisions/swaps.

**Fix:** Go back to the **Upload page and hit "Save and Complete"** to
(re)assign the track ID, then let tile gen include the page; escalate if that
doesn't resolve it.

> **Not for a page swap.** If a *swapped/revised* page isn't appearing, a missing
> track ID is **very unlikely** the cause — the page couldn't have been added to
> pricing zones for the revision without one — so **don't lead with this cause**
> and don't cite OTS-1954 for it. See the page-swap guidance in
> `publishing-and-go-live.md`.

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
1985/1986/1997; team SME review (answer-feedback-log FB-009). See
`sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-22.*
