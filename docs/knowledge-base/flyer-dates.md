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
