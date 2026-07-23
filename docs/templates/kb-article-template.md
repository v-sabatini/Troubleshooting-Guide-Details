# [Article Title] — Troubleshooting Guide

> **What this covers:** One or two sentences on scope.
> **Audience:** Who this is for.
> **Grounded in:** Which source(s) this came from.

---

## Overview / context (optional)

A short orientation so the reader/bot understands where this fits.

---

## Self-serve checklist

Ordered steps a processor should try before escalating.

1. ...
2. ...

---

## Error / issue catalog

Repeat this block per distinct error or issue. Keep the **exact error text**
verbatim — users paste it, and the chatbot matches on it.

### [Issue name / exact error string]

- **Symptom:** What the user sees (include the literal error message).
- **Likely cause(s):** The underlying reason(s).
- **Fix:** Concrete resolution steps.
- **If that doesn't work / escalate:** Next step + what to include.
- **Source:** Ticket / page reference. **Link live Jira tickets** so the reader
  can open them: `[OTS-2332](https://flippit.atlassian.net/browse/OTS-2332)`
  (same for FD/CLSD/HS/MSC/DOC keys). Leave **retired `TOSS-####`** keys as plain
  text — that project is archived and the link won't resolve.

---

## When to escalate

Clear trigger conditions + where to go (channel, ticket type) + what to include.

---

*Sources: [list]. See `sources/source-map.md`. Last reviewed: YYYY-MM-DD.*

<!--
AUTHORING NOTES (delete or keep — not shown to end users if you strip HTML comments):
- Write in plain language; assume a new processor is reading.
- Prefer question-style or symptom-style headings — they match how people ask.
- Always keep exact error strings verbatim.
- One self-contained topic per file works best for NotebookLM retrieval.
- Cite the source ticket/page so answers are trustworthy and verifiable.
- Render live Jira ticket references as markdown links to
  `https://flippit.atlassian.net/browse/<KEY>` (OTS/FD/CLSD/HS/MSC/DOC). Keep
  retired TOSS keys as plain text.
-->
