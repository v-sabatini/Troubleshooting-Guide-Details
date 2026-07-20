# How to Review & Test the CXE Help Center

A step-by-step for team members helping vet the assistant's answers. No setup —
it runs in the browser. (See also `ONBOARDING.md`.)

## What you'll need
- Your work **Claude** login.
- Access to the **`v-sabatini/troubleshooting-guide-details`** GitHub repo (ask
  Vanessa if you can't see it).

## Steps

**1. Open Claude Code on the web.**
Go to **[claude.ai/code](https://claude.ai/code)** and sign in with your work account.

**2. Start a session on the repo.**
Point it at the repo **`v-sabatini/troubleshooting-guide-details`**, branch
**`claude/flyer-chatbot-knowledge-base-yhsxxb`**.
- No branch picker? Just start on the repo and make your first message:
  `Please check out the branch claude/flyer-chatbot-knowledge-base-yhsxxb`.

**3. Turn Claude into the assistant.** Paste this as your first real message:

> I'm helping vet the **CXE Help Center** assistant. Act as the assistant,
> answering **only** from this repo (`docs/knowledge-base/`, `docs/retailers/`,
> and — only as a last resort — `docs/processing-sops/`), and **cite the source
> article** for each answer. Follow the bot rules in `docs/notebooklm/README.md`.
> I'll ask real troubleshooting questions. **After each answer, ask me if it was
> correct.** When I say something's wrong or missing, **log my feedback** to
> `sessions/answer-feedback-log.md` (dated: the question, what you said, the
> correct info, and the article it affects), then commit and push. **Don't change
> the knowledge-base articles** — just capture the feedback.

*(This is prompt #7 in `sessions/prompts.md` if you'd rather copy it from there.)*

**4. Ask real questions** — the stuff you actually get from the team. To start:
- "My codesheet failed with `undefined method 'split' for nil:NilClass` — what do I check?"
- "A retailer's flyer is missing — what's the usual cause and who fixes it?"
- "How do I process ALDI? Any common codesheet gotchas?"
- "A store won't harmonize — what do I try, and where does it escalate?"
- "I escalated a CLSD ticket — how long until it's resolved?"

**5. Correct it.** After each answer, tell Claude if it's right. If it's wrong or
incomplete, say what's actually true — Claude logs your feedback to
`sessions/answer-feedback-log.md` so the owner can fix the source. **You don't
edit any files yourself.**

## Ground rules
- It's a **read-only copy** of our docs — don't try to change Confluence/Jira/Drive from here.
- **No secrets** — please don't add contacts, emails, or passwords. If an answer
  needs a contact/credential, it should point to the OneGuide instead.
- **Log feedback, don't rewrite articles** (unless the owner asks) — keeps quality
  controlled and avoids conflicts.

## Where things live
- `docs/00-index.md` — master list of what the assistant knows.
- `docs/knowledge-base/` — general troubleshooting / process / QC articles.
- `docs/retailers/` — 489 retailer-specific guides.
- `sessions/answer-feedback-log.md` — the running feedback list (your notes land here).
- `docs/GAP-LOG.md` — known gaps not yet solved.

Questions → ping **Vanessa (CXE Enablement)**. Thanks for helping make this accurate! 🙌
