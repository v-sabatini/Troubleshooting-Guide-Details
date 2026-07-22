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

### Issue: V2 Publishing fails for one pricing zone (V1 still succeeds)

**Symptom:** **V2 Publishing** errors for **one pricing zone but not others**. The
pipeline task shows errored (sometimes **with no logs**), and — importantly — the
**errored task blocks other flyer sessions from kicking off**.

**What it means for go-live:** During the V1→V2 transition, most experiences have
both a V1 and a V2 path. If **V2 fails but V1 succeeds**, that zone **still goes
live on V1-powered experiences — just not on V2-powered experiences.** So the
flyer usually isn't fully dark; the real problem is the **errored task blocking
downstream sessions.** (See `content-v2-and-publishing.md`.)

**What to try / know:**
- **You can't re-publish a single zone — republishing is all-or-nothing.** A
  manual republish often **just repeats the same error**, so don't expect it to
  clear this on its own.
- **Cloning *might* resolve it, but the error can also block the clone** — it's not
  a guaranteed fix.
- **Setup is usually not the culprit** and is typically already verified by the
  time this reaches the help desk — don't spin on re-checking the zone's setup.

**Escalate to CLSD.** This is the confirmed path — the root cause (why V2 publish
fails for the zone) is a content-platform/engineering matter. Include: the flyer
run link, the specific zone, that the **errored task is blocking other sessions**,
and that a **manual republish repeated the error**. Mark urgent if go-live is close.

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
- **For a link/URL specifically, try these before escalating (in order):**
  1. **Re-run the Item Cutout Generation session** — re-running a task
     **downstream of** item cutout generation makes it **re-kick off**.
  2. **Re-run the Vendor tasks** — Vendor tasks **act as sessions**, so re-running
     them **kicks off the item-level sessions**.
  3. **Republish** the flyer.
  4. Run the **`Touch Storefront Objects`** custom action to push the change to
     the storefront.
- If new items/links **still** won't reflect, escalate to the **Hosted team (HS)**
  *(OTS-1971 → HS-3281)*.

### Issue: A page swap isn't appearing on the front end

**Symptom:** A page was **swapped/revised** but the change isn't showing on the
front end.

**Fix (try in order):**
1. Rule out a **false alarm** (still processing / caching).
2. **Undo and redo the page swap** — this **re-kicks all the relevant sessions**,
   which may not have completed correctly the first time.
3. Re-run **page stitching** and **republish**.
4. *(Rarely relevant for a swap)* A missing **track ID** is an **upload-step**
   issue, not a page-revision one — don't lead with it for a swap (see
   `missing-flyers-and-indexing.md` Cause 4).

**Escalate by scope:** if it's broken on the front end **everywhere**, ask the
Enablement team in Slack, then **CLSD**. If it's **Hosted-only**, go to the
**Hosted team (HS)**. **Confirm whether it's Hosted-only or everywhere before
routing.**

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
| Item/link/page change won't reflect **everywhere** on the front-end (after ruling out processing) | Ask the **Enablement team in Slack**, then **CLSD** |
| Item/link/page change won't reflect **Hosted-only** | **Hosted team (HS)** |
| Root cause is the flyer isn't live | Fix go-live first (Part A) |

> **Confirm scope before routing.** "Front end" is not the same as "Hosted." The
> **Hosted team (HS) handles Hosted-only issues**; something broken **everywhere**
> on the front end goes to Slack (Enablement) → **CLSD**. If you're unsure, ask
> the user whether it's Hosted-only or everywhere.

Always include: flyer run link, current status/state, due date, and what you tried
(clone, re-save, toggle).

---

*Sources: OTS Jira board 315, incl. OTS-1938/1964/1971/1974/1978/1982/1992/1998/
2006/2027/2030/2047/2048/2060/2064; team SME review (answer-feedback-log FB-008, FB-009).
See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-22.*
