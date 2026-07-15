# Turbo & CP-Legacy — Error Guide

> **What this covers:** The processor-facing errors seen in **Turbo** and
> **CP Legacy** import/custom-action jobs, with the exact error strings, the
> usual cause, and the self-serve fix. Source Confluence page id: 13617366001
> (space CP, "Error Guide: Turbo & CP-Legacy [2026]").
>
> **Audience:** Content Production processors.
> **Escalation path:** If self-serve steps fail, escalate per
> `escalation-and-tickets.md`.

---

## Turbo errors

### `Invalid Flyer Type for Merchant`

- **Symptom:** The error log reads `Invalid Flyer Type for Merchant`.
- **Likely cause:** The wrong **Flyer Type ID** was entered for that specific
  retailer.
- **Fix:** Double-check the Flyer Type ID, correct it as required, and submit the
  **Import Job** again.

---

## CP Legacy errors

### `Error processing image: Request was blocked by retailer. Please try with proxy option. HTTP 403 - Forbidden`

- **Symptom:** A CP Legacy job errors with, verbatim:
  `"Error processing image: Request was blocked by retailer. Please try with proxy option. HTTP 403 - Forbidden"`
- **Likely cause:** More often than not, the URL for the problematic SKU is
  incorrect or invalid.
- **Fix:**
  1. Copy the problematic **SKU / Ecom ID** and look it up in the **product data
     sheet**.
  2. Click the product **image URL** link to confirm it works.
  3. If the link is invalid, update it with the correct URL and **rerun the
     custom action**.

### `ERROR: Not enough rows in Product CSV for zone [Insert Store Set here]`

- **Symptom:** A CP Legacy job errors with, verbatim:
  `"ERROR: Not enough rows in Product CSV for zone [Insert Store Set here]"`
- **Likely causes:**
  - An invalid/incorrect SKU image URL (same class as above); **and/or**
  - A **mismatch** between the **"Store Sets"** and **"Sale Story"** values.
- **Fix:**
  1. Check the problematic SKU/Ecom ID against the product data sheet and fix any
     invalid image URL (as above).
  2. In the preview, confirm the **Store Sets** and the **Sale Story** are correct
     and **match the expected values in the Story Curation Sheet**.
  3. Resubmit the **Import Job**.

---

## See also

- `home-depot-us-troubleshooting.md` — retailer-specific CP Legacy / Snicket /
  Fadmin errors.
- `escalation-and-tickets.md` — when and how to escalate.

---

*Source: Confluence "Error Guide: Turbo & CP-Legacy [2026]" (CP, 13617366001). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
