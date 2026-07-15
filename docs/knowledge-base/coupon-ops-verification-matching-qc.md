# Coupon Ops Daily Queues — Verification, Item Matching & OS Match QC — Guide

> **What this covers:** The three linked Coupon Ops baseline tasks that form the
> coupon pipeline — **Coupon Verification**, **Item Matching**, and **OS Match
> QC** — including what each queue is, its daily target, and the risk items to
> watch. Sourced from Confluence pages 13536002653 (Coupon Verification),
> 13536002854 (Vendor Guide: Item Matching), and 13536003039 (OS Match QC).
>
> **Audience:** Coupon Ops team and OS vendors.

---

## Pipeline order

These three tasks run in sequence. **OS Match QC** explicitly lists **Coupon
Verification** and **Item Matching** as its prerequisites:

1. **Coupon Verification** — verify incoming coupons (assign brands) so they are
   eligible to be matched.
2. **Item Matching** — match flyer items to the verified coupons.
3. **OS Match QC** — QC the matches for discrepancies flagged by OS.

All three queues **should be cleared by EOD every day.**

---

## 1. Coupon Verification

**What it is:** The most important baseline task. Coupons arrive in FADMIN via
multiple feeds and **must be verified before they can be matched** to flyer
items. Queue: `admin.flipp.com/coupons/next_to_verify`.

**Target:** Clear the queue by EOD every day.

**Risk items and how to mitigate:**

| Risk | Detail / fix |
|---|---|
| **Incorrect brand and/or not all brands assigned** | The correct brand(s) must be assigned so all possible item matches are gathered for matching and L2ID badging. For a **multi-brand coupon, assign all brands.** |
| **Brand not in system** | Brands must be added to coupons and each brand must be tied to a manufacturer. In some cases you must **create a new manufacturer and a new brand** before you can assign it. |

**Exceptions — Meijer coupons** follow the same general process, with two
differences:
- **Storewide is allowed** (e.g. "10% off general merchandise"). *Note: Family
  Dollar can also have storewide coupons.*
- **Final Price = Disallowed**, and **High Risk = No**.

---

## 2. Item Matching

**What it is:** The process where items from flyers are matched to applicable
coupons. Executed by **OS** and monitored by the Coupon Ops team so thresholds
are not exceeded.

**Target:** Match items as soon as they are added to the Item Matching queue;
ideally the queue is cleared by EOD every day.

**Matching rules** consider **brand, type of item, sizing, and exclusions.**
(An OS Decision Chart for Matching accompanies the source page.)

**Watch for common name variations** — the same product category appears under
many labels. Match across all of these:

- **Toilet Paper** = Bathroom Tissue / Bath Tissue / Toilet Tissue
- **Dish Detergent** = Dishwashing Liquid / Liquid Dish Detergent / Dish Soap /
  Dish Liquid. *Note: Dawn Dish Detergent may be labelled "Dawn Ultra"; Gain
  also has a "Gain Ultra" dish detergent.*
- **Fabric Softener** = Fabric Conditioner / Fabric Enhancer / Liquid Fabric
  Softener / Liquid Fabric Conditioner / Liquid Fabric Enhancer
- **Dryer Sheets** = Fabric Softener Sheets / Fabric Softener Dryer Sheets /
  Fabric Sheets
- **In-Wash Scent Booster** = In-Wash Fragrance Booster / In-Wash Scent Booster
  Beads / Laundry Scented Beads / Laundry Scented Booster / Fragrance Booster /
  Scent Booster Beads / Scent Booster
- **Invisible Spray** = Dry Spray / Body Spray / Antiperspirant / Deodorant
- **Clear Gel** = Antiperspirant / Deodorant

---

## 3. OS Match QC

**What it is:** A queue populated by coupons that have an **item-match
discrepancy flagged by OS.** Owned by the Coupon Ops team.

**Target:** Both the Coupon Item Match and OS Match QC queues should be cleared
by EOD every day.

**Risk items and mitigation:**

| Risk | Mitigation |
|---|---|
| **Incorrect items matched to a coupon** | Thoroughly read all inclusions and exclusions (size, type, count); Google items when unsure what they are or what size (e.g. loads vs. oz for laundry items); run the OS Accuracy Check. |
| **Not all applicable items matched to a coupon** | Run the OS Accuracy Check. |

**Prerequisites before starting:** Coupon Verification and Item Matching.

---

## See also
- `coupon-accuracy-checks.md` — the downstream False Positive / False Negative
  audit of live coupon matchups on Flipp Web and hosted sites.
- `escalation-and-tickets.md` — where to raise issues that need dev/config help.

---

*Source: Confluence "Copy of Coupon Verification" (VEN, 13536002653), "Copy of
Vendor Guide: Item Matching" (VEN, 13536002854), and "Copy of OS Match QC" (VEN,
13536003039). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
