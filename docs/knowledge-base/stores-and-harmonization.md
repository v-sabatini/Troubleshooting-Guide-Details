# Stores & Harmonization — Troubleshooting Guide

> **What this covers:** Store harmonization failures/audits, duplicate or missing
> stores, "store not appearing," and add-store errors. ~29 real OTS tickets.
>
> **Audience:** Flyer-ops / CX staff. Store *location data* issues escalate to
> the **PIA** team; most audits are resolvable by fixing lat/long or confirming
> with the retailer.

---

## Background

**Harmonization** matches a merchant's stores to the canonical store/location
dataset (4Square) so flyers target the right physical locations. When a store
fails to harmonize, or two stores look like duplicates, targeting breaks.

---

## Issue: Store failing harmonization / false duplicate

**Symptom:** Stores won't harmonize, often flagged as a **false duplicate**, or
"stores already harmonized" errors. Titles like "36 Stores Failing Harmonization
with False Duplicate Store".

**Fix (try in order):**
1. **Update the lat/long** for stores whose coordinates are too similar, then
   **re-harmonize**. *(OTS-2025: "updated the lat/longs that were similar and
   harmonized the stores.")*
2. If stores look like duplicates, **confirm with the retailer** whether they're
   genuinely distinct — the retailer may confirm duplicates are correct and
   provide closures/address updates to apply in FADMIN. *(OTS-2024, Wellwise SDM.)*
3. If it's a genuine store-data problem you can't fix, **escalate to PIA** (the
   store/place-data team). *(OTS-2002 → PIA-8847; OTS-2035 → PIA-9159.)*

---

## Issue: Harmonization Audit tickets

**Symptom:** Tickets titled "Harmonization Audit: <retailer>" — a periodic check
of a retailer's store data.

**Fix / process:**
- Work through the flagged stores: fix lat/longs, apply retailer-confirmed
  closures/address changes in FADMIN, and note the resolution on the ticket.
- Escalate anything requiring canonical dataset changes to **PIA**.

---

## Issue: Store not appearing / can't add a store

**Symptoms & fixes:**
- **Grand-opening / new store not appearing on hosted** *(OTS-2056, Lidl US)* —
  verify the store is added, harmonized, and assigned to the live flyer run.
- **"Merchant store code already taken" when adding a store** even though a search
  shows it unused *(OTS-2053)* — a data conflict; escalate to PIA with the store
  code and merchant.
- **Store not appearing on a third-party app** (e.g. Loblaws on PC Optimum)
  *(OTS-1967)* — if it's a third-party app and **not Flipp-hosted**, it's out of
  our scope; route to the **account team** (escalated via DOC).

---

## Issue: Items showing as "In-Store Only"

**Symptom:** All items in a flyer show as "In-Store Only" incorrectly
*(OTS-1991, Sportsman's Warehouse)*.

**Fix:** This was resolved by a **Hosted-team fix** — escalate to the Hosted team
if item availability/flags are wrong system-wide rather than per-item.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Store location / harmonization data can't be fixed locally | **PIA** (store/place data) |
| Store code conflicts / canonical data | **PIA** |
| Item availability flags wrong (In-Store Only, etc.) | **Hosted team (HS)** |
| Third-party app display (not Flipp-hosted) | Account team (via DOC) |

Include the merchant, store code(s), lat/long, and flyer run link.

---

*Sources: OTS Jira board 315, incl. OTS-1967/1982/1991/2002/2009/2024/2025/2035/
2053/2056. See `sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-14.*
