# Hosted Sites & Preview Links — Troubleshooting Guide

> **What this covers:** Preview links that don't work, Hosted (retailer-embedded)
> flyers not loading, iframe issues, and pages rendering cropped/incorrectly.
> ~15+ real OTS tickets. These frequently escalate to the **Hosted team (HS)**.
>
> **Audience:** Flyer-ops / CX staff triaging retailer/preview-link complaints.

---

## Background

**Hosted** is the retailer-embedded flyer experience (e.g. a flyer shown in an
iframe on the retailer's own website). **Preview links** let internal/external
folks view a flyer before or around go-live. Both depend on the flyer being fully
processed and correctly published.

---

## Issue: Preview links not working

**Symptom:** Preview links don't open, show the wrong flyer, "This site can't be
reached," or a full-screen preview isn't interactive. *(OTS-1961, OTS-1973,
OTS-1980, OTS-1995, OTS-2012.)*

**Try first:**
- Confirm the flyer is **actually live / fully processed** — previews for a flyer
  that isn't live yet (or is stuck pre-live) won't work. See
  `publishing-and-go-live.md`.
- Regenerate/copy the preview link fresh and confirm you're using the correct
  flyer run.

**If still broken:** escalate to the **Hosted team (HS)** with the flyer run and
the exact preview URL.

> **Note:** Providing a direct link to a **not-yet-live** flyer as a workaround is
> generally **not** advised — previews aren't meant for that use and it carries
> risk. *(OTS-1988: workaround declined for this reason.)*

---

## Issue: Hosted flyer not appearing / not loading

**Symptom:** A live flyer isn't appearing on the retailer's Hosted site, the
iframe won't load, or vertical previews can't be seen. *(OTS-1992 [urgent],
OTS-1971, "Cannot See Vertical Previews".)*

**Try first:** Confirm the flyer is live and Ops-complete (not stuck in
"preview ready" — see `publishing-and-go-live.md`).

**If still broken:** escalate to the **Hosted team (HS)** (e.g. OTS-1971 →
HS-3281). Mark **urgent** if it's a live flyer not appearing on the retailer site.

---

## Issue: Pages cropped / cut off / not rendering

**Symptom:** Flyer pages load but appear **cropped, cut off, or half-rendered**,
or certain pages don't display. *(OTS-1968 RCSS; OTS-1966 Tepperman's.)*

**Fix:** Re-run **page stitching** and **republish**. *(OTS-1966: "re-ran page
stitching and republished.")* If it persists, escalate to the Hosted team.

---

## Issue: Links/redirects wrong on Hosted only

**Symptom:** A page link doesn't redirect correctly, or item links don't reflect
— **on Hosted only** (fine on Flipp). *(OTS-1962, OTS-2012.)*

**Fix:** Since it's Hosted-specific, escalate to the **Hosted team (HS)** with the
specific links and where they should point.

---

## When to escalate & where

| Situation | Escalate to |
|---|---|
| Preview/iframe/**Hosted-only** rendering after confirming flyer is live | **Hosted team (HS)** |
| Page stitching didn't fix cropped pages (Hosted) | **Hosted team (HS)** |
| Same issue shows up **everywhere** on the front end (not Hosted-only) | Ask the **Enablement team in Slack**, then **CLSD** — not HS |
| Flyer isn't live yet (root cause is publishing) | See `publishing-and-go-live.md` |

> **HS is for Hosted-ONLY issues.** If the problem also appears outside the
> Hosted experience (i.e. everywhere on the front end), it routes to Slack
> (Enablement) → **CLSD**, not the Hosted team. **Confirm the scope** (Hosted-only
> vs everywhere) before routing — ask the user if it's unclear.

Always confirm live/processed status **before** escalating — many preview issues
are really "the flyer isn't live yet."

---

*Sources: OTS Jira board 315, incl. OTS-1961/1962/1966/1968/1971/1973/1980/1988/
1992/1995/2012; team SME review (answer-feedback-log FB-009). See
`sources/ots-ticket-inventory.md`. Last reviewed: 2026-07-22.*
