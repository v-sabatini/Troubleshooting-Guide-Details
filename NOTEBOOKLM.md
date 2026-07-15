# Migrating This CXE Help Center into NotebookLM

This repo is the **authoring home** for the flyer-processing troubleshooting
CXE Help Center. NotebookLM is the **delivery surface** — where your team will
actually chat with it. This guide explains how to move from one to the other.

## Why keep authoring in GitHub?

- **Version control & review** — changes are tracked; you can see who changed
  what and roll back.
- **Provenance** — every article cites its source (`sources/source-map.md`), so
  answers stay trustworthy.
- **Portability** — clean Markdown uploads cleanly to NotebookLM today, and to
  other tools later if needed.

NotebookLM works best when each **source** is a focused, self-contained
document — which is exactly how the articles here are written.

## What to upload as NotebookLM sources

Upload the files in **`docs/knowledge-base/`** — each one becomes a source:

1. `flyer-processing-overview.md`
2. `codesheet-errors.md`
3. `common-live-flyer-issues.md`
4. `storefront-publishing-errors.md`
5. `escalation-and-tickets.md`
6. `glossary.md`

Optionally add `docs/00-index.md` as a source so the model has the "map."

> You generally **don't** need to upload `sources/`, `sessions/`, `templates/`,
> or `README.md` — those are for authoring, not for answering user questions.

## How to upload

NotebookLM accepts Markdown/text, PDF, Google Docs, and copied text. Two options:

- **Simplest:** open each `.md` file in GitHub, copy the raw text, and use
  **Add source → Copied text** in NotebookLM. (Or download the files and use
  **Add source → Upload.**)
- **Google Docs route:** paste each article into its own Google Doc and add them
  as Drive sources — handy if you want to keep editing inside Google.

Keep **one article = one source** so retrieval and citations stay clean.

## Suggested notebook setup

- **Notebook name:** "Flyer Processing Troubleshooting Assistant"
- **Notebook description / instructions (if available):**
  > You are a troubleshooting assistant for the flyer-processing team. When a
  > user describes an error, match it to the exact error text in the sources,
  > then give the symptom → likely cause → fix → when-to-escalate. Always cite
  > which source you used. If the answer isn't in the sources, say so and point
  > to the escalation guide rather than guessing.

## Test it before rolling out

Paste in real questions your team asks and confirm good answers, e.g.:
- "Codesheet failing with `undefined method 'split' for nil:NilClass` — what do
  I check?"
- "The file is on the FTP but the codesheet says it can't find it."
- "New pricing zones appeared and the config is throwing an error."
- "Storefront won't load for one merchant — how do I find the flyer run?"
- "Old price prefix is still showing on the front-end after go-live."
- "When should I file a CLSD ticket vs. just re-running sessions?"

If any answer is weak, improve the **source article** here, then re-upload that
one source. **Keep GitHub as the source of truth** and treat NotebookLM as a
published copy you refresh.

## Keeping it in sync

When you update an article here:
1. Commit the change in GitHub.
2. Re-upload (or re-paste) that single source in NotebookLM.
3. Note the refresh in the session log.

*A future enhancement could automate export, but manual re-upload is fine for a
prototype.*
