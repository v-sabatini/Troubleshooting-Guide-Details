# Item Import — File Format & Common Failures

> **What this covers:** The accepted file format for an **item import** (and
> **SKU update**) in FADMIN — required column order, the full set of accepted
> column headers, language prefixes, date formatting, and how to leave a value
> blank — plus the most common reasons an item import fails to run. Grounded in
> team SME review.
>
> **Audience:** Flyer processors doing item imports / SKU updates.
> **Escalation path:** If the file follows every rule below and still won't
> import, file a CLSD ticket with the `.csv` attached (see
> `escalation-and-tickets.md`).

---

## The rules that make an import run

An item import is a `.csv` of item data. Most "it won't run" failures come from
the file's **shape**, not its values. Check these first:

1. **Column order matters for the first two columns.**
   - **`item_id` must be column 1.**
   - **`sku` must be column 2.**
   - Everything after that can be in any order. A file whose columns are, say,
     `item_id, name, sku, …` **will fail** because `sku` is in position 3, not 2.
2. **A minimum of 3 columns is required.** `item_id` + `sku` alone will **not
   run** — even for a SKU-only update, where a two-column file fails with the
   error **`No fields to update!`**. Add at least one more valid header column;
   **it may be completely empty** (e.g. add a `url` column with just the header
   and no values, and the import will run).
3. **Dates must be `YYYY-MM-DD`.** Any date column (e.g. `valid_from`,
   `valid_to`) has to be in that format.
4. **To store a blank value, put `*blank*` in the cell.** `*blank*` explicitly
   saves the field as an empty string — use it to **clear** a field.
5. **Watch SKU formatting.** Spreadsheets can mangle long SKUs into scientific
   notation or insert commas. Confirm the SKU column is stored as text and the
   values are intact.

---

## Accepted column headers

The retailer OneGuides do **not** list the full set of accepted headers. These
are the accepted column headers for an item import:

```
analytics_categories, auto_play_video, bonus_offer_description, brand, brand_id,
data_piping_url, deferred, description, disclaimer_text, display_type,
display_url, external_override_image_source_url, feature_html,
google_category_id, id_1, id_2, id_3, id_4, id_5, id_6, iframe_display_height,
iframe_display_width, in_store_only, item_corrections, item_side_list_url_text,
keywords, name, overlay_url, page_destination, play_video_inline, pre_price_text,
price_text, qualifying_quantity, raw_current_price, raw_dollars_off,
raw_original_price, raw_percent_off, reward_quantity, sale_story, sku, url,
valid_from, valid_to, video_sound_on, youtube_embedded_url
```

…plus **`item_id`**. Remember the ordering rule: **`item_id` = column 1, `sku` =
column 2**; the rest may be in any order.

### `google_category_id`

`google_category_id` **is a valid header** — don't drop it just because its
value is a number. In FADMIN the Google Category is **displayed in words**, but
the **backend value is numeric**, so a value like `319` is legitimate.

### Language prefixes (`english_` / `french_`)

You can prepend **`english_`** or **`french_`** to any field so it applies only
to English or French items. Example header row:

```
"item_id","sku","english_url","french_url","keywords"
```

---

## Common item-import failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Import fails to run | **Wrong column order** — `item_id` not in column 1, or `sku` not in column 2 | Reorder so `item_id` is column 1 and `sku` is column 2 |
| SKU-update file won't run, error `No fields to update!` | **Fewer than 3 columns** (just `item_id` + `sku`) | Add any third valid header column — it may be empty (e.g. a blank `url` column) |
| Dates rejected / rows import wrong | Dates not in `YYYY-MM-DD` | Reformat all date columns to `YYYY-MM-DD` |
| A field won't clear / saves oddly | Empty cell where an explicit blank was intended | Put `*blank*` in the cell to save an empty string |
| Long SKUs corrupted | Spreadsheet converted them to scientific notation / added commas | Store the column as text; re-enter clean values |

---

## When to escalate

If the file follows all the rules above and still won't import, file a **CLSD**
ticket with the `.csv` attached and the exact error text. See
`escalation-and-tickets.md`.

---

*Sources: team SME review (answer-feedback-log FB-006, FB-007); Slack Help Desk
2026-08-12 (the `No fields to update!` error = a sub-3-column file). Cross-reference:
`codesheet-errors.md`, `common-live-flyer-issues.md`. See
`sources/source-map.md`. Last reviewed: 2026-08-17.*
