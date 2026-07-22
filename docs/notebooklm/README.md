# NotebookLM Upload Bundles

These files are the **upload-ready version** of the CXE Help Center, bundled so the
whole thing fits inside NotebookLM's per-notebook **source limit** (~50 free /
~300 paid). Uploading the ~500 individual files would exceed that; these **28
bundles (~30 files) hold the same content.

> These are **generated** from `docs/knowledge-base/` and `docs/retailers/` — the
> originals stay the source of truth. Regenerate after edits (see below).

## What to upload to NotebookLM (28 sources)

| File | What's in it |
|---|---|
| `00-flipp-troubleshooting-knowledge-base.md` | All general troubleshooting/process/QC/runbook content: codesheet errors, item-import format, Content V2, missing flyers/indexing, clipping/AutoBox, stores/harmonization, dates, hosted/previews, publishing/go-live, storefront, Turbo/CP-Legacy & Home Depot US error guides, onboarding, indexing CI tasks, coupon & live-date QC, alert runbooks, escalation routing (FD/CLSD/MSC), glossary. |
| `retailers-A.md` … `retailers-Z.md`, `retailers-0-9.md` | The 489 Vendor OneGuide retailer processing guides, grouped by first letter (contacts/credentials omitted). |
| `retailers-cp-processing-sops.md` | The Content Production (CP) per-retailer processing SOPs (distinct from the OneGuides). |

Just upload every `.md` file in this folder as a NotebookLM source (drag-and-drop,
or Add source → Upload). That's it — 28 files instead of 500.

## Suggested notebook setup

- **Name:** "CXE Help Center — Flyer Processing Assistant"
- **Instructions:**
  > You are the **CXE Help Center** assistant, helping the flyer-processing team
  > troubleshoot. For a general error, use the CXE Help Center source (symptom →
  > cause → fix → escalation). For a retailer-specific question, use that
  > retailer's guide in the matching "Retailers - <letter>" source. **Attribute
  > answers to the CXE Help Center** (e.g. "Per the CXE Help Center, …") and name
  > the specific guide you used.
  >
  > **When the sources have a documented fix, give it and cite it. When they
  > DON'T, don't just stop at "escalate" — reason from the architecture (especially
  > the Content V2 model in "Content V2 & V2 Publishing") to offer educated options
  > the user can try.** Rules for these reasoned options: (1) clearly label them as
  > **educated guesses / hypotheses**, not documented fixes; (2) tie each option to
  > the reasoning (e.g. "because in V2 each section is distributed independently…");
  > (3) list safe, reversible things to try first; (4) keep escalation (CLSD /
  > Hosted) as the backstop; (5) **never invent** specific UI labels, tool names,
  > config values, contacts, or credentials — reason only from what the sources
  > actually say, and if unsure, say so. (6) **Match the audience: the user is a
  > processor, not an engineer.** Give concrete, processor-doable steps; don't hand
  > them internal/engineering speculation about root cause — when the likely cause
  > is backend/internal, route to CLSD rather than guessing at mechanics. Never
  > surface contacts/credentials — direct users to the retailer's OneGuide for those.
  > (7) **Source precedence — CP Processing SOPs are a last resort.** Answer from
  > the general Help Center first, then the Vendor OneGuide retailer guides. The
  > **Content Production (CP) processing SOPs** ("CP Processing SOPs" bundle /
  > `docs/processing-sops/`) are written for the CP team, who generally **won't be
  > using this assistant** — so **do not lead with CP SOP steps.** Only bring them
  > in as a **secondary consideration**: if the issue may be **laddering up from a
  > CP-processed flyer**, note that possibility and point to the retailer's CP SOP
  > (e.g. "if this is a CP-processed flyer, its CP SOP covers …") rather than
  > walking the user through CP steps as if they were the audience.

## Test questions

- "Codesheet failing with `undefined method 'split' for nil:NilClass` — what do I check?"
- "The flyer is missing — what's the usual cause and who fixes it?"
- "How do I process ALDI? What are the common codesheet errors?"
- "What's Ace Hardware's rule for tagging the current price?"
- "A store won't harmonize — what do I try, and where does it escalate?"

## Regenerating these bundles (after editing the originals)

Bundling is a mechanical concatenation grouped by first letter. Re-run the bundle
step documented in the session-07 log (or ask Claude to "rebuild the NotebookLM
bundles"). The knowledge-base bundle is concatenated in reading order; retailer
bundles are grouped A–Z (+ `0-9`).
