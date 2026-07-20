# Welcome — help us vet the CXE Help Center 🧪

Thanks for helping test the **CXE Help Center** — a prototype assistant that helps
the flyer-processing team troubleshoot issues and errors. It's built from our own
Confluence guides, real Ops Troubleshooting (OTS) tickets, and 489 retailer
processing guides. It's **not finished** — your job is to poke at it and tell us
where it's wrong so we can fix it at the source.

## What this is (30 seconds)

- A knowledge base of Markdown articles in this repo (`docs/`) that will eventually
  power a NotebookLM chatbot.
- For now we test it **right here in Claude**: Claude reads the repo and answers as
  the assistant, citing which article it used.

## How to test it (do this)

1. Open **`sessions/prompts.md`** and copy the **"🧪 Reviewer / Vetting prompt" (#7)**.
2. Paste it to Claude. Claude will act as the assistant, answering only from the
   repo and citing its source.
3. **Ask real troubleshooting questions** you'd get from the team — codesheet
   errors, missing flyers, stores/harmonization, publishing/go-live, a specific
   retailer, etc.
4. After each answer, Claude will ask **"was that right?"** Tell it what's wrong or
   missing. It will **log your feedback** to `sessions/answer-feedback-log.md` and
   push it — so nothing gets lost. (You don't edit the articles yourself; the
   owner applies fixes.)

## Where to look

- **`docs/00-index.md`** — the master list of what the assistant knows.
- **`docs/knowledge-base/`** — general troubleshooting / process / QC articles.
- **`docs/retailers/`** — 489 retailer-specific guides.
- **`sessions/answer-feedback-log.md`** — the running feedback list (your notes land here).
- **`docs/GAP-LOG.md`** — known gaps we haven't solved yet.

## Ground rules (important)

- **Everything here is a read-derived copy.** We only ever **read** Confluence /
  Jira / Drive — never change them. Don't paste anything that would modify those.
- **No secrets.** Contacts, emails, and passwords are intentionally left out.
  Please don't add any — if an answer needs a contact/credential, it should point
  to the OneGuide instead.
- **Log feedback, don't rewrite articles** (unless the owner asks). This keeps
  quality controlled and avoids conflicts.
- Work happens on branch **`claude/flyer-chatbot-knowledge-base-yhsxxb`**.

## Good first questions to try

- "My codesheet failed with `undefined method 'split' for nil:NilClass` — what do I check?"
- "A retailer's flyer is missing — what's the usual cause and who fixes it?"
- "How do I process ALDI? Any common codesheet gotchas?"
- "A store won't harmonize — what do I try, and where does it escalate?"
- "I escalated a CLSD ticket — how long until it's resolved?"

Questions? Ping Vanessa (CXE Enablement). Thanks for helping make this accurate! 🙌
