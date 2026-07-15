# Retailer Processing Guides

Retailer-specific processing instructions, converted from the **OneGuide** Google
Docs (one per retailer/banner). These let the bot answer "how do I process
[retailer] / what's special about it?"

- **Master directory of all retailers:** [`sources/oneguide-retailer-index.md`](../../sources/oneguide-retailer-index.md)
- **Article template:** [`_TEMPLATE.md`](_TEMPLATE.md)

## Status: ✅ Complete

**489 retailer guides converted** from the OneGuide directory (~491 unique
retailers). Built in phased batches via parallel subagents; every batch was
leak-scanned before commit.

### Not converted (source Google Doc unavailable)

These OneGuide entries link to Google Docs that returned "Requested entity was not
found" (deleted, moved, or access-revoked at time of conversion). Re-add if the
docs are restored:

- **Sportsman's Warehouse** — Doc `17kIdvfi60quOc_qHJZOyow0hg7b76bVAh_Q4ZR3gho4`
- **Wellwise SDM** — Doc `1GACOVeDkq_XUw1D64G5VkCnHSreySPgSw-jIKHeN7rw`

## Conventions

- **Contacts and credentials are omitted** (project decision). Passwords, staff
  names, and emails from the source docs are never copied here; the bot points
  people to the OneGuide for who to contact.
- Each article records the source Google Doc ID + (where present) the OneGuide
  "Last Updated" date, and ends with a `Contacts/credentials omitted` source line.
- Source docs are **living documents** — plan a periodic refresh.

## How to refresh / re-run

1. `sources/oneguide-retailer-index.md` has the ordered retailer → Google Doc list.
2. To rebuild one retailer: read its Doc via the Google Drive connector, then
   rewrite `docs/retailers/<slug>.md` from `_TEMPLATE.md` (strip contacts/credentials).
3. To refresh everything, re-run the phased batch process (see session-06 log).
   Slugs are Unicode-normalized: lowercase, accents stripped, `&`→"and",
   apostrophes removed, non-alphanumerics → hyphens.
