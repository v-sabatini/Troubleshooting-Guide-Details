# Sponsored Product Ads — What's in CXE's Scope

> **What this covers:** Whether a Sponsored Product Ads (SPA) problem is CXE's to
> troubleshoot, what to check when it is, and the known pitfall that SKUs are not
> priced nationally.
>
> **Audience:** Flyer-ops / CX staff triaging a "the campaign isn't delivering"
> or "these items aren't returning in search" request.
>
> **Grounded in:** Confluence "Sponsored Product Ads - CXE" (XPTCXE 13880197171),
> new page 2026-10-21.

> ⚠️ **Partial capture.** The **in-scope** list and the scope note below are
> complete as published. The page's **out-of-scope list** and most of its
> **scenario catalog** were **not captured** in the change digest — so treat "not
> listed here" as *unknown*, not as *out of scope*. Open the
> [source page](https://flippit.atlassian.net/wiki/spaces/XPTCXE/pages/13880197171/Sponsored+Product+Ads+-+CXE)
> for the full picture.

---

## ✅ In scope for CXE

**Campaign non-delivery caused by setup, tagging, or other CXE/Ops-controlled
parameters.** Examples:

- Incorrect or missing **brand ID**
- Incorrect or missing **tagging for flyer items**
- **E-commerce item** issues
- **Online deal** errors
- **Curator** issues

## ❌ Out of scope for CXE

The source page carries an explicit out-of-scope list. It was **not captured** —
check the source page rather than inferring from the in-scope list above.

## Scope note — single-retailer vs multi-retailer campaigns

> CXE can investigate and troubleshoot issues with **single-retailer campaigns**.
> For **multi-retailer brand campaigns**, provide the **top impacted retailers**
> so support can be prioritised.

---

## Known pitfall: same SKUs, different pricing

- **Scenario:** An opportunity was created to promote **Rollback** items for the
  Walmart campaign **using SKUs**. CXE was then asked to **de-duplicate SKUs** in
  the Walmart CA campaign report.
- **Why it happened:** SKUs **can be shared across provinces, but they are not
  always priced the same** or carrying the same promotion in each one. The team
  that pitched the idea **was unaware that Walmart runs 10 pricing zones** with
  different flyer versions — those versions **correspond to provinces**, and
  **pricing across Canada is not national**.
- **What to do about it:** Get **sign-off from the CXE team before pitching any
  campaign** that keys on SKUs, and use the escalation path on the source page.
  **Account teams can give insight into flyer setup and versioning** — ask them
  first when you need to know how a retailer is zoned.

## Open scenario: parent company vs specific product line

Walmart reported that specific flyer items — **Cheerios** and **Cinnamon Toast
Crunch** — **weren't returning in search** when customers searched those brand
names. The source page frames this as a *"PDF stating parent company vs. specific
product line"* problem (i.e. the brand recorded is the parent company rather than
the product line). **The documented root cause and resolution were not captured** —
see the source page before answering this one.

---

## When to escalate

| Situation | Where to go |
|---|---|
| Non-delivery traced to brand ID / tagging / curator / online deal | **In scope** — fix in FAdmin, then confirm delivery |
| Multi-retailer brand campaign | Provide the **top impacted retailers** for prioritised support |
| Anything you can't place as in-scope | Ask the **Enablement team in `#helpme-cxe`** tagging **`@enable-cxe`** before filing |
| Campaign pitch that depends on SKU-level pricing | Get **CXE sign-off first** — see the pitfall above |

---

*Sources: Confluence "Sponsored Product Ads - CXE" (XPTCXE 13880197171, created
2026-10-21 by Kim Potashner) via the KB update digest for 2026-09-26 → 2026-10-26.
**Partial capture** — see the warning above. See `sources/source-map.md`.
Last reviewed: 2026-10-26.*
