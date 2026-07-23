# Clipping, AutoBox & Cutouts — Troubleshooting Guide

> **What this covers:** Items that can't be clipped, boxes drawn in the wrong
> place, and cutout-generation failures. ~30 real OTS tickets.
>
> **Audience:** Flyer-ops / CX staff. Most of these are self-resolvable by
> re-running the box/tag steps.

---

## Background

For a flyer to be "clippable," each item needs a **box** drawn around it (so users
can clip it) and a **tag** (item data). **AutoBox** (the "auto box draw" task)
automatically draws these boxes, and completing it kicks off **auto tag**. When
AutoBox misjudges a flyer's layout, items end up unclippable or boxes land
off-center.

---

## Issue: Flyer / items not clippable

**Symptom:** A live flyer can't be clipped, or only some items are clippable.
Titles like "Not Clippable", "some items not clippable".

**Likely cause:** The **AutoBox draw ran poorly** (struggled with the flyer's
formatting), or the flyer was **still processing**.

**Fix (try in order):**
1. **Re-run AutoBox** ("auto box"). This re-draws boxes and **kicks off auto
   tag**; it typically reflects online **within about an hour**.
   *(OTS-1934: "Re-ran auto box which kicked off auto tag!")*
2. **Manually box** the items AutoBox missed — those become clippable immediately.
   *(OTS-2020: "AutoBox ran poorly, I've boxed what was missed so those are now
   clippable.")*
3. If it's a **top-50 indexed retailer** (full tagging) and recently uploaded, it
   may simply still be processing — re-check later. *(OTS-2037.)*

**If it keeps happening for a retailer:** flag it — AutoBox may be consistently
struggling with that flyer's format and needs a closer look / next steps
*(OTS-1984, OTS-1979).*

> **When AutoBox *can't* box a retailer at all — check the source format.** If a
> retailer has **no PDF flyer** and their "flyer" is really just **text/images
> on their website** (the app image is a screenshot of that site), the layout is
> often **very long, skinny pages** that AutoBox can't get enough detail from to
> box items properly. That's a **source-format limitation, not a processing
> bug** — re-running AutoBox won't fix it; expect to **box manually**, and if
> it's chronic it's a conversation about the retailer's asset format, not a
> ticket. *([OTS-2332](https://flippit.atlassian.net/browse/OTS-2332): Mitsuwa
> Marketplace — website-screenshot pages too long/skinny for AutoBox to box.)*

---

## Issue: Box draw off-center

**Symptom:** Boxes are drawn but **off-center** / misaligned, sometimes only on a
specific page. Titles like "Box Draw Off-Center on Second Page".
*(OTS-1941, OTS-1943.)*

**Fix:** Re-run AutoBox; if it persists, manually adjust the boxes. Repeated
off-center draws on the same retailer indicate an AutoBox tuning issue worth
escalating.

---

## Issue: Item cutout generation failing / blocked

**Symptom:** Item **cutout images** fail to generate or are blocked. Titles like
"Item Cutout Gen Failing", "Item Cutout Generation Blocked".
*(OTS-1936, OTS-1981, and Hy-Vee cutout blocked.)*

**Fix:** Re-run the cutout/image generation step. If it stays blocked, escalate
(often a processing/pipeline issue) via **CLSD** — include the flyer run and the
specific items.

---

## When to escalate

- You've re-run AutoBox and manually boxed, and items still won't clip or tag.
- Cutout generation stays blocked after a re-run.
- The same retailer repeatedly breaks AutoBox (needs a tuning fix).

Escalate via **CLSD** with the flyer run link and example item(s).

---

*Sources: OTS Jira board 315, incl. OTS-1934/1935/1936/1941/1943/1979/1981/1984/
2005/2020/2037; [OTS-2332](https://flippit.atlassian.net/browse/OTS-2332)
(weekly scan 2026-07-22). See
`sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-22.*
