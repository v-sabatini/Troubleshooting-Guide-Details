# Content V2 & V2 Publishing — What It Is & How It Affects Processing

> **What this covers:** A plain-language orientation to **"V2"** (Content V2 / V2
> Publishing) — Flipp's shift from the **Flyer-Centric (V1)** content model to the
> **Global-Centric (V2)** model — and what it means for flyer processing and
> troubleshooting.
>
> ⚠️ **Scope note:** V2 is an **in-progress platform migration** described mostly
> in engineering/data strategy docs (as of Oct 2025 – Jul 2026). This article
> explains the concepts and the impact on processing. It is **not** a step-by-step
> "how to run/re-run V2 publishing" runbook — those operational mechanics aren't
> documented yet (see Gap Log **GAP-001 / GAP-002**).

## The one-paragraph version

Flipp is moving from a **"Flyer-Centric"** content model (**V1**) to a
**"Global-Centric"** one (**V2**). In V1, everything hangs off a flyer
(`flyer_id`, `flyer_item_id`). In V2, content is modeled as independent,
globally-identified entities — **Offers, Products, Promotions, Publications** —
that can be distributed to any channel and place. Flyers become **Publications**,
flyer pages become **Sections**, and flyer items become **Offers/Atoms**. The goal
is a single content source (**Curator**) fed through a single ingestion entry
point (**Nexus API**), with legacy systems kept alive by **converters** during the
transition.

## Vocabulary shift (V1 → V2)

| V1 (Flyer-Centric) | V2 (Global-Centric) | Notes |
|---|---|---|
| Flyer / `flyer_id` | **Publication** / `publication_id` | A curated, dynamic collection of displayable items |
| Flyer page | **Section / Section Plan** | Subset of a publication; can have its **own distribution** & rendering |
| Flyer item / merchandise | **Offer** (a kind of **Atom**) | Atom = parent of Offer + Promotion; replaces merchandise/items |
| — (new) | **Promotion** | A displayable ad (image + click action) with no product/offer |
| item / product | **Product** | A purchasable thing at one retailer |
| `flyer_item_id` | `offer_id` / **`global_id`** | **One V2 Offer can map to *many* V1 flyer items** |
| FSA-based availability | **Distribution + Place** | see "distribution" below |

**Key mapping fact:** except for flyer items (1 Offer → many V1 items), V1↔V2 is
roughly **1:1** — everything in V1 has a V2 equivalent. The reverse isn't true:
newer content (DVM, NativeX EU/South America) has **only V2 ids**, no V1 id.

## The big processing-relevant change: distribution

- **V1** distributed flyers by **FSA** (flyer-availability-service) + store finder.
- **V2 distributes to *stores*, not FSAs.** "Distribution" is anything targetable
  — a **Place** (postal code, store, FSA, or polygon), a **channel**
  (app/feature), or (future) a user segment.
- **Publications *and* their Sections can each be distributed** — and a section can
  be distributed to a **subset** of the publication's distributions.
- **Why this matters for troubleshooting:** channel- and zone/section-level
  distribution (e.g. *"hidden everywhere except hosted,"* or one pricing
  zone/section behaving differently from the rest) is a **first-class V2 concept**.
  Publish/distribution behaviour is now **per-publication and per-section/zone, per
  channel** — which is exactly the backdrop to **GAP-001** (publish errors under
  hosted-only distribution) and **GAP-002** (V2 publishing failing for one zone).

## How V2 publishing flows (where "V2 Publishing" fits)

- **Fadmin** is still the PDF-processing CMS, but is shifting from fanning out V1
  data to **producing V2 print content into the Nexus API**.
- **Nexus API** = the single **entry point / source of truth** for incoming flyer
  content. It feeds **Item Platform** (→ V2 Products & Offers → Content API),
  **Publication API** (publication structure), and **Distribution API**
  (distribution IDs).
- **Curator** = the single **V2 serving source**; pulls items/publications/
  distributions from those APIs. **DVM** is the active V2 distribution path today
  (NativeX, retailer apps).
- **Flyers-NG** = the **V1 compatibility layer** during the transition; a converter
  translates **V2 → V1 on read** so legacy **App / Web / Hosted** keep working. It's
  removed once channels are fully V2.
- A **Publication Plan** (content queries + rendering details) is resolved and
  **"hydrated"** into a **Publication Payload** — the actual content the user sees.
  *(This means the full content a user saw is only known at render time.)*
- Being **decommissioned:** Search Platform API, FlyerKit, Backflipp, and the old
  Fadmin → V1 fan-out.

## What this means for the processing team (practical)

- **Terminology in tools/tickets is shifting.** Expect "publication," "offer,"
  "section," "distribution," "global id," **Nexus**, **Curator**, **Flyers-NG**,
  **DVM** alongside the old flyer/item/FSA words — use the mapping table above.
- **Distribution is per channel + per store/section**, so "hidden except hosted"
  and per-zone publish behaviour are expected V2 levers (and new failure surfaces).
- **Reporting/metrics differ:** V2 counts **Offers, not flyer spots** ("Item View"
  ≠ "Offer View"); some V2 content (international, DVM) has **no V1 id** at all, and
  billing/legacy reports still depend on V1 ids (kept alive by converters).
- **Legacy display depends on conversion** (Flyers-NG V2→V1). If something renders
  oddly on a legacy channel *during the transition*, the converter is a suspect.

## Troubleshooting note / current gaps

These sources are **architecture/strategy**, not an ops runbook. They explain
*why* V2 publishing and per-zone/channel distribution exist — but **not** the
step-by-step "re-run V2 publishing for one zone" or "why did the publish task
error with no logs." Those remain **open in the Gap Log (GAP-001, GAP-002)**.
For live cases, escalate to **CLSD** (Content Layer) and loop **Hosted (HS)**;
we'll add an ops runbook here once one exists.

---

*Sources: Confluence — "Transitioning to Global-Centric Model: Content V2 & Event
V2 Adoption Framework" (DATAV, 13022527510); "Content V2 Dimensions" (DATAV,
13245906978); "V1 => V2 Data Pipeline Transition" (EN, 12597657799); "DET Content
V2 Discovery" (DATAV, 12291965139, "flyers are distributed to stores, not FSAs");
"Transitioning from V1 → V2 for Content Retrieval" (CTLR, 11268554758). Migration
in progress as of Oct 2025 – Jul 2026. Last reviewed: 2026-07-15.*
