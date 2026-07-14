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
  `stores-and-harmonization.md` (escalate store-data issues to **PIA**).

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
| Store/postal coverage or location data wrong | **PIA** (store/place data) — see stores article |
| General content escalation / can't self-resolve | **CLSD** |
| Third-party app (e.g. PC Optimum), not Flipp-hosted | Account team (via DOC) |

Always include the flyer run link, the affected postal code(s)/region, and
whether a new flyer is still processing.

---

*Sources: OTS (Ops Troubleshooting) Jira board 315, ~120 tickets Jan 2024–Jul
2026, incl. OTS-1927/1928/1929/1930/1931/1939/1944/1954/1959/1960/1963/1969/1975/
1985/1986/1997. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*
