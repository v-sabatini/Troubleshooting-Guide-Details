# Coupons Accuracy Checks — QC SOP

> **What this covers:** How to audit the quality of live coupon matchups on
> Flipp Web and hosted retailer sites — checking for both **False Positives**
> (wrong matchups) and **False Negatives** (items with a call-to-action that are
> missing a coupon badge). Sourced from Confluence page 8733982776.
>
> **Audience:** OS vendors / Coupon Ops. **Cadence:** every **Thursday and
> Sunday**. Start **no earlier than 5 AM ET**; notify Coupon Ops by email that
> the check is complete by **9 AM ET** (addresses in the source doc).

---

## Setup

- The Coupon Ops team pastes weekly templates into the **OS Coupon Accuracy
  Checks** spreadsheet. Each flyer listed must be checked for **both** False
  Positives and False Negatives; record both results in the same template.
- **Recommended method:** complete the False Positive and False Negative checks
  for one flyer before moving to the next.
- Open a browser to Flipp.com and enter the **ZIP code** of the flyer being
  checked. Search the merchant; if more than one flyer is available, open them
  all and match the **Flyer Type** in the URL to the template.
  - The Flyer Type is the segment **after** the retailer name. Example —
    CORRECT: `flipp.com/en-us/agawam-ma/weekly_ad/7864488-walgreens-weekly-ad?`
    (the `weekly-ad` after the name). Do not read the `weekly_ad` path segment
    before the ID.
  - **If the Flyer Type is listed as `(HOSTED SITE)`**, do the check on the
    retailer's own website instead: open the site, enter the listed ZIP, select
    the first store location, and open the **newest** weekly flyer. (Hosted
    retailers include Food Lion, Stop & Shop, Giant Carlisle, Martin's Foods,
    Giant Landover, Family Dollar.)

---

## False Positive check (are the existing matchups correct?)

1. **Count the matchups.** Open the flyer for the correct Flyer Type. Find items
   with coupon badges; for each, open the item, scroll down, and count all
   coupons matched to it. Record the total in the template under **"# of
   Matchups"**.
2. **Verify each matchup.** Open each badged item and apply the item-matching
   rules — **brand, type of item, sizing, and exclusions** — to decide whether
   each coupon is correctly matched. A matchup is a **False Positive** when the
   item's size/count falls outside the coupon's stated sizing. Examples:
   - Item size 90 oz. not within coupon sizing (25 oz, 40–60 ct, 9.7 oz) → FP
   - Item size 20 lbs. not within coupon sizing (12 lb – 13.5 lb) → FP
   - Item count 4 pk. not within coupon sizing (6 to 12 pk.) → FP
3. Repeat until all matchups on the flyer are evaluated; record each error.

**How to record a False Positive** — fill in: **Merchant, Issue, Flyer ID,
Flyer Item ID, Coupon ID.**
- **Flyer ID** — in the flyer URL with no item open.
- **Flyer Item ID** — in the URL once an item is opened.
- **Coupon ID** — click "Clipping/Redemption Help", then read it from the URL.
- **For hosted-site retailers:** record the **Item Name** under Flyer Item ID
  and the **coupon text** under Coupon ID.

---

## False Negative check (are any CTA items missing a badge?)

1. **Count and document the number of CTAs (calls-to-action)** in the flyer.
   Refer to each merchant's CTA definitions in their account-specific L2ID
   Vendor Guide. Record the total under **"Total # of CTAs in Flyers"**.
2. **Record any flyer item that has a CTA but no coupon badge** on it.

**How to record a False Negative** — fill in: **Merchant, Issue, Flyer ID, Flyer
Item ID.**
- **Flyer ID** — flyer URL with no item open.
- **Flyer Item ID** — URL with the item open.
- **For hosted retailers:** you do **not** need the Flyer ID. Record the **page
  number** where the item was found, plus the **Item Name** (click "Details" to
  open the item pop, copy the name) under Flyer Item ID.

---

## See also
- `coupon-ops-verification-matching-qc.md` — the upstream verification and
  item-matching tasks (and the full item-matching rules) that these checks audit.
- `escalation-and-tickets.md` — for issues needing dev/config follow-up.

---

*Source: Confluence "[NEW] Coupons Accuracy Checks" (VEN, 8733982776).
Contacts/credentials omitted. Last reviewed: 2026-07-15.*
