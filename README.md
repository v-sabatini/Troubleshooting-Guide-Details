# Flyer Processing Troubleshooting — Knowledge Base

A curated knowledge base that powers a **chatbot to help the flyer-processing
team troubleshoot issues and errors**. It's being prototyped here (in Claude +
GitHub) and will eventually be migrated into **NotebookLM**.

Everything is written as clean, self-contained **Markdown** so it reads well for
humans in GitHub *and* uploads cleanly as NotebookLM sources.

## Start here

- 📖 **[docs/00-index.md](docs/00-index.md)** — the master index of all articles.
- 🧭 **New to the project or starting a session?** Open
  **[sessions/prompts.md](sessions/prompts.md)** and paste the **Resume prompt**.

## What's inside

```
README.md                       ← you are here
NOTEBOOKLM.md                    ← how to migrate this KB into NotebookLM
docs/
  00-index.md                    ← master table of contents
  knowledge-base/                ← the actual troubleshooting articles
    flyer-processing-overview.md
    codesheet-errors.md
    common-live-flyer-issues.md
    storefront-publishing-errors.md
    escalation-and-tickets.md
    glossary.md
  templates/
    kb-article-template.md       ← use this to add new articles
sources/
  source-map.md                  ← provenance: every article → its source
sessions/
  prompts.md                     ← copy/paste prompts to resume & wrap up sessions
  logs/                          ← what was done each session + next steps
```

## How the knowledge base is written

Every article follows the same shape so the chatbot gives consistent answers:

**Symptom (exact error text) → Likely cause → Fix → When to escalate → Source.**

Principles:
- **Exact error strings are kept verbatim** — people paste them, and the bot
  matches on them.
- **One self-contained topic per file** — best for NotebookLM retrieval.
- **Every claim is sourced** (Jira ticket, Confluence page, or Slack thread) and
  tracked in [`sources/source-map.md`](sources/source-map.md).
- **Plain language** — written for a new processor, not an engineer.

## How we work session-to-session

So we never lose context between sessions:
1. **Start** a session by pasting the **Resume prompt** (`sessions/prompts.md`).
   It reads the latest session log and gets Claude up to speed.
2. **End** a session by pasting the **Wrap-up prompt**. Claude writes a new
   session log with what changed and the next steps, then commits.

## Current coverage

| Area | Status |
|---|---|
| Codesheet errors | ✅ First version |
| Core flyer processing / ops | ✅ First version |
| Missing flyers / indexing / coverage | ✅ From 381 OTS tickets |
| Clipping / AutoBox | ✅ From OTS tickets |
| Stores / harmonization | ✅ From OTS tickets |
| Flyer dates | ✅ From OTS tickets |
| Hosted / previews | ✅ From OTS tickets |
| Publishing / go-live / front-end | ✅ From OTS tickets |
| Post-escalation (FD / CLSD / MSC) | ✅ Boards + turnaround |
| Storefront / publishing | ✅ First version |
| Common live-flyer issues | ✅ First version |
| Data piping | ⬜ Deferred |
| Processing Support (ClickUp) | ⬜ Not yet ingested — current source of truth |

## Status

🚧 **Prototype, in active development.** Content is synthesized from internal
sources and needs a subject-matter review pass before it's treated as
authoritative. See the latest file in [`sessions/logs/`](sessions/logs/) for
where we are and what's next.
