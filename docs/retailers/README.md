# Retailer Processing Guides

Retailer-specific processing instructions, converted from the **OneGuide** Google
Docs (one per retailer/banner). These let the bot answer "how do I process
[retailer] / what's special about it?"

- **Master directory of all 493 retailers:** [`sources/oneguide-retailer-index.md`](../../sources/oneguide-retailer-index.md)
- **Article template:** [`_TEMPLATE.md`](_TEMPLATE.md)

## Conventions

- **Contacts and credentials are omitted** (per project decision). Passwords,
  staff names, and emails from the source docs are never copied here; the bot
  points people to the OneGuide for who to contact.
- Each article records the source Google Doc ID + the OneGuide "Last Updated" date.
- Source docs are **living documents** — plan a periodic refresh.

## Progress — phased rollout (all 493, alphabetical)

**Done (6 / 493):**
- [ALDI](aldi.md)
- [The Beer Store](the-beer-store.md)
- [2001 Audio Video](2001-audio-video.md)
- [Academy Sports + Outdoors](academy-sports-outdoors.md)
- [Accès Pharma](acces-pharma.md)
- [Ace Hardware](ace-hardware.md)

**Next batch (continue alphabetically):** Ace Hardware Canada → Acme Fresh Market
→ AG Foods → Al Arsh Halal Meat → Alaska Commercial → Albertsons United Banners →
Alf Curtis → … (see the master directory for the full ordered list).

## How to continue (for the next session)

1. Open `sources/oneguide-retailer-index.md` for the ordered retailer → Google Doc list.
2. For each retailer: read the Doc via Google Drive, then write
   `docs/retailers/<slug>.md` from `_TEMPLATE.md` — capturing account facts,
   cadence, upload/codesheet steps (config names + toggles), box/tag include-exclude
   rules, **retailer-specific common errors / risk items**, and FQC notes.
   **Strip all contacts and any credentials.**
3. Move the retailer to the "Done" list above and commit.
