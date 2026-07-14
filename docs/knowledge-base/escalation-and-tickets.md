# Escalation & Ticketing — When Self-Serve Isn't Enough

> **What this covers:** When and how to escalate a flyer-processing problem, what
> to include so it gets resolved fast, and who owns what. Grounded in the
> codesheet & data-piping troubleshooting guides, the Processing Support KB, and
> `#helpme-ops` practice.

---

## Decision guide: fix it, wait, or file a ticket?

1. **Is it a delay or an error?**
   - Indexed flyers can take **24–48 hours** to process; retailers sometimes
     release late. If it's a delay, **wait / re-run** before escalating.
2. **Have you run the self-serve checklist for that error type?**
   - Codesheet → `codesheet-errors.md`
   - Live-flyer issue → `common-live-flyer-issues.md`
   - Storefront → `storefront-publishing-errors.md`
3. **Does the fix require a code/config change or access you don't have?**
   (new pricing zones, word-bank exceptions, filename-matching bugs, backend
   beacon queries) → **file a ticket.**
4. **Is it blocking a go-live within 1–2 days?** → mark it **urgent** and say so.

---

## Where to ask first (Slack)

- **`#helpme-ops`** — general flyer-ops troubleshooting. Tag **`@enable-cxe`**
  (the **Enablement pod** — the team that absorbed the former Skeleton Team's
  support function; includes Vanessa, Kayla, Han…).
- **`#flex-processingsupport`** — Processing Support retailer/run questions; tag
  **`@psflex`** (the on-shift Scrum Master).
- **`#helpme-flex`** — higher-level PS process / onboarding / retailer-change
  questions; tag **`@flex`**.
- **`#sf-auditor-alerts`** — storefront publishing audit alerts.
- **`#content-public`** — republish / thumbnail / processing-completion asks
  (per the Live Flyer Check runbook).

> Keep troubleshooting **in channels, not DMs**, so others have visibility and
> can help.

---

## Filing a CLSD / Ops Troubleshooting ticket

**CLSD** is the escalation ticket type for issues that block or affect a flyer
and need the Content Collection / CI / dev team to investigate.

**Always include:**
- The **flyer run link** (`fadmin.flippback.com/flyer_runs/<id>`) and flyer ID.
- A clear **description of the error** and the **exact error text**.
- A **screenshot of the full error backtrace** (not just the first line).
- **What you already tried** (re-ran sessions, republished, compared to a
  working codesheet, etc.).
- For codesheet issues: the **failing codesheet** *and* a **previously-working
  codesheet**, plus **FADMIN and pipeline backups**.
- **Time sensitivity:** when it goes live, and whether it's urgent.

**Urgency guidance:**
- Mark **urgent** only when it blocks a go-live within ~1–2 days or blocks Final
  QC before go-live.
- Note: some ticket classes (e.g. data-piping) are generally **not** urgent
  because they don't block a flyer from going live — check the norm for the
  issue type before flagging urgent.

---

## Ownership map (who fixes what)

| Problem area | First responder | Likely fixer if code/config change needed |
|---|---|---|
| Codesheet won't process | `#helpme-ops` / `@enable-cxe` | CI/dev team via `wishabi/fadmin` (config, word bank, filename matching) |
| Live-flyer issue (tiles, images, pricing, categorization, harmonization) | `#helpme-ops` / `@enable-cxe` | CLSD → Content Collection / CI team |
| Storefront load errors | `#sf-auditor-alerts` / on-call | Content / platform on-call (republish on FADMIN) |
| Processing Support run/task | `#flex-processingsupport` / `@psflex` | PS Scrum Master |
| PS onboarding / retailer changes | `#helpme-flex` / `@flex` | Vendor Solutions / Flex MGMT |

---

*Sources: Confluence "Code sheet Troubleshooting Guide" (XPTCXE); "Data Piping
Troubleshooting Guide" (XPTCXE); "Processing Support - Knowledge Base" (FLX);
"How to troubleshoot Storefront errors" (QKB); `#helpme-ops` Slack practice. See
`sources/source-map.md`. Last reviewed: 2026-07-14.*
