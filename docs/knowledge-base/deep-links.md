# Deep Links — How to Build Them

> **What this covers:** How a flyer deep link is constructed — base domain,
> merchant identifier, and the URL parameters that target a specific run, page,
> store, postal code or language.
>
> **Audience:** Flyer-ops / CX staff building a link to send to a retailer,
> account team, or customer.
>
> **Grounded in:** Confluence "Deep Links" (XPTCXE 3129122303), restructured
> 2026-10-20.

> ⚠️ **Partial capture — confirm before relying on this for anything not listed.**
> This article reflects the **confirmed** portions of the 2026-10-20 rewrite of the
> source page. Roughly 22 further lines of that page were **not captured**, so the
> parameter table below is **not exhaustive**. For a parameter you don't see here,
> open the [source page](https://flippit.atlassian.net/wiki/spaces/XPTCXE/pages/3129122303/Deep+Links).

---

## Step 1 — Pick the base domain

There are two, and which you use depends on whether the merchant has its own
hosted experience:

- **Hosted domain (iframe / c-name)** — use this when the merchant **has** its own
  hosted experience. Go to the merchant's website and find their hosted
  experience; that's your base.
- **FlyerTown domain** — use this **only** for merchants that **don't have their
  own hosted** experience, or where it **isn't c-named**. This is the base for all
  FlyerTown links.

## Step 2 — Add the merchant identifier

After the base, add the **Merchant Name Identifier**, followed by a `' - '`.

> 🔄 **Changed 2026-10-20.** The page previously said to use the **Store Name**
> here. It now specifies the **Merchant Name Identifier**. If you're working from
> a saved link, an older doc, or muscle memory, this is the bit that changed.

## Step 3 — Add parameters

| Parameter | Accepted value | What it does | Example |
|---|---|---|---|
| `&flyer_run_id=` | 5-digit number | Directs to a specific flyer run | `&flyer_run_id=56721` |
| `&locale=` | `en` or `fr` | Sets the language | `&locale=en` |
| `&page=` | number | Directs to a specific page | `&page=4` |
| `&store_code=` | number | Targets the flyer assigned to that store | `&store_code=` |
| `&postal_code=` | CA — 6 characters, **no spaces** | Targets the flyer assigned to that postal code | `&postal_code=n3a1l3` |
| `&auto_locate=` | *(not captured)* | *(not captured)* | — |

> `&auto_locate=` appears on the source page but its accepted values and
> behaviour were **not captured** in the change digest — check the source page
> before using it.

---

## When to escalate

A deep link that is **built correctly but still doesn't resolve** is usually not a
link problem:

| Situation | Where to go |
|---|---|
| Link opens but the flyer reads "not available" | See `hosted-and-previews.md` — a preview with a **preview date set** is *not* gated by the availability window |
| Link works on Flipp but not on the retailer's site | **Hosted team (HS)** — Hosted-only issues |
| Link is wrong/redirects incorrectly everywhere | Ask the **Enablement team in `#helpme-cxe`**, then **CLSD** |

---

*Sources: Confluence "Deep Links" (XPTCXE 3129122303, updated 2026-10-20) via the
KB update digest for 2026-09-26 → 2026-10-26. **Partial capture** — see the
warning above. See `sources/source-map.md`. Last reviewed: 2026-10-26.*
