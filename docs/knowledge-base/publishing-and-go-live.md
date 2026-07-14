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
- If new items/links genuinely won't reflect, escalate to the **Hosted team (HS)**
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
2006/2027/2030/2047/2048/2060/2064. See `sources/ots-ticket-inventory.md`. Last
reviewed: 2026-07-14.*
