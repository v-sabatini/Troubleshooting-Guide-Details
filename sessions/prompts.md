# Session Prompts — Copy/Paste to Start & End Every Working Session

This file exists so you never have to re-explain the project. At the **start** of
a session, paste the **Resume prompt**. At the **end**, paste a **Wrap-up
prompt** so the next session can pick up instantly.

The flow is a loop:

```
Start session  →  paste RESUME prompt
   ... do work ...
End session    →  paste WRAP-UP prompt  →  Claude writes a new session log + updated next steps
Next session   →  paste RESUME prompt (it reads the latest log)  →  you're instantly up to speed
```

---

## ▶️ 1. RESUME PROMPT — paste this at the START of a new session

> We are continuing to build the **Flyer Processing Troubleshooting knowledge
> base** in the GitHub repo `troubleshooting-guide-details` (branch
> `claude/flyer-chatbot-knowledge-base-yhsxxb`). It's a prototype CXE Help Center
> that will eventually be migrated into **NotebookLM** to power a chatbot that
> helps my team troubleshoot flyer-processing issues and errors.
>
> Before doing anything else:
> 1. Read `sessions/CURRENT-STATUS.md` — the single always-current snapshot of
>    where we are, key facts, and prioritized next steps.
> 2. Skim `docs/00-index.md` for the current article list.
> 3. Give me a 5-line summary of: what already exists, the top open next steps,
>    and what you recommend we do today.
>
> Then wait for me to confirm today's focus before making changes. My sources are
> Confluence + Jira (`flippit.atlassian.net`), Google Drive, and Slack. Stay on
> the designated branch and commit when we finish a unit of work.

---

## ⏹️ 2. WRAP-UP PROMPT — paste this at the END of a session

> We're wrapping up this session. Please:
> 1. Create a new session log at `sessions/logs/YYYY-MM-DD-session-NN.md` (use
>    today's date; increment NN if there's already a log for today) using the
>    structure of the existing logs.
> 2. In it, capture: **what we did today**, **decisions made**, **new
>    articles/sources added**, **open questions**, and a concrete **"Next steps"**
>    list ordered by priority.
> 3. Update `docs/00-index.md` (coverage status table) and
>    `sources/source-map.md` if we added or changed anything.
> 4. Commit everything to the branch with a clear message and push.
> 5. Finally, give me a short plain-English recap I can read on my phone.

---

## 🧩 3. ADD-A-SOURCE PROMPT — when you want to fold in new material

> I want to add a new source to the CXE Help Center: **[describe it — e.g. "the
> Processing Support ClickUp space", a Confluence page URL, a Jira filter, a
> Google Doc, or a Slack channel]**.
>
> Please: pull the relevant content, tell me what you found before writing,
> then turn it into one or more knowledge-base articles using
> `docs/templates/kb-article-template.md`. Keep exact error strings verbatim,
> cite the source in the article and in `sources/source-map.md`, and update the
> index. Don't guess — if something is ambiguous, ask me.

---

## ➕ 4. NEW-ARTICLE PROMPT — when you know the topic already

> Create a new knowledge-base article on **[topic / error]** using
> `docs/templates/kb-article-template.md`. Ground it in **[source]**. Follow the
> symptom → cause → fix → escalate structure, keep error text verbatim, add any
> new terms to `docs/knowledge-base/glossary.md`, cite the source, and update the
> index and source map.

---

## 🔎 5. GAP-CHECK PROMPT — periodically, to find what's missing

> Review the CXE Help Center against my connected sources. Search Jira (TOSS and
> any relevant projects) and Confluence for **recurring flyer-processing errors
> that we don't yet have an article for**, and search `#helpme-ops` /
> `#flex-processingsupport` for common questions we don't cover. Give me a
> prioritized list of gaps and offer to draft the top ones.

---

## 🚚 6. NOTEBOOKLM-PREP PROMPT — when ready to migrate

> We're ready to move this into NotebookLM. Read `NOTEBOOKLM.md` and confirm the
> CXE Help Center is in good shape to upload: check that every article is
> self-contained, error strings are verbatim, and the index is current. Flag
> anything that won't translate well as NotebookLM sources, and give me the
> upload order and suggested notebook settings.

---

## 🧪 7. REVIEWER / VETTING PROMPT — for teammates testing the bot

> I'm a member of the flyer-processing team helping vet the **CXE Help Center**
> assistant. Act as the assistant, answering **only** from this repo
> (`docs/knowledge-base/`, `docs/retailers/`, and — only as a last resort —
> `docs/processing-sops/`), and **cite the source article** for each answer.
> Follow the bot rules in `docs/notebooklm/README.md` (attribute to the CXE Help
> Center; if it's not documented, reason it out and clearly label guesses; keep
> answers at a processor's level; never surface contacts/credentials).
>
> I'll ask real troubleshooting questions. **After each answer, ask me if it was
> correct.** When I tell you something is wrong or incomplete, **log my feedback**
> to `sessions/answer-feedback-log.md` (append a dated entry: the question, what
> the bot said, what's actually correct/my note, and the article it affects),
> then commit and push. **Do not change the knowledge-base articles themselves** —
> just capture the feedback so the owner can apply fixes. If a fix is obvious and
> I explicitly ask you to apply it, you may, but default to logging only.

---

*Tip: You can tweak these prompts anytime. If our workflow changes, update this
file so it always reflects how we actually work.*
