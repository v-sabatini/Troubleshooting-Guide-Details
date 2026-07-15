# Lowe's USA — Processing Guide

> **Source:** Lowe's USA OneGuide (Google Doc `1rgRoHU7d0Vpc1VF-Y3F8HEz1lCMu0MGWn5FXg9osSs0`), updated Feb 25, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard |
| Availability | All platforms (DIY + Pro; "Lowe's For Pros" Pro ad is **hosted only**) |
| Slack channels | `#lowesus`, `#flex-processingsupport` |
| Hosted URL | lowes.com/weekly-ad |
| Flyer types | **Weekly/PRO** (flyer type #4679/8755), weekly · plus a monthly type |
| Processing | Auto-stack; Strategic Ops **yes** (retailer data / Feedel); no coupons; Flex flyer review |

## Files & schedule (Weekly)

- **Files received:** Monday (via SFTP; codesheet named `MMDDYYVV_Recap.xls`).
- **Cadence:** Available Wed–Wed; Valid Thu–Wed. One-day consumer preview on lowes.com only.
- **Preview date:** Friday prior to launch (allow time for FQC). Preview email sent the day before go-live (usually Tuesday).
- **Linking document:** **Yes** — shared before PDFs, found in the VAST tracker. Match the Flyer Run ID to the correct tab.

## Upload & setup

- Download codesheet from SFTP, **no manipulations**, save as `.csv`.
- Upload — Config **`lowes_usa`**, base path `/MMDDYYVV`.
- Attach the linking document to all vendor tasks with a comment: everything in the linking document is a **DIRECT LINK** except items marked "DO NOT TAG URL". If an item reads "Find in Store", replace it with "DO NOT TAG URL" for OS. If no links provided, leave a note for the vendor teams.
- **Edit details:** Available Wed–Wed, Valid Thu–Wed; toggle **hidden on Flipp & distribution** (hosted only); external run name **"Weekly Ad"** (Pro = "Pro Ad"); four standard thumbnails; **no theme**.
- **Create a trigger** to unhide on Flipp/distribution on the valid date (Thursday, 12:01 AM).

### ⚠️ Common errors (retailer-specific)

- **Codesheet "invalid value for integer" error** — caused by a leading `0` on the number at the top (it's meant to be a date). Remove the `0`; if it still errors, ensure there are only **6 digits total**.
- **Incorrect page-naming error** — page names in the codesheet must exactly match the SFTP file names (e.g. an extra `-` in one and not the other). Fix so names match.
- Links in the linking document sometimes get processed as **items** by mistake (often "starting at" items) — change display type to **Link**.

## QC specifics

- **Box Draw (Low; Auto-Box OFF → regular tagging, Box QC bot OFF).** Linking doc required (Box/Tag specific tab). Include packaged deals, retailer logo, sign-up page, social media, special weblinks; **exclude coupons**.
  - Single items (bolded name) each get a box. Multiple SKUs + **one** image → box together; multiple SKUs + **multiple** images → box **separately**. "YOUR CHOICE" items boxed separately (don't text-box over the "YOUR CHOICE" text). "Combo Price" items boxed separately with the combo price its own box. "BUY ONE GET ONE FREE" boxed **together**. Box sale-story/promo items (they appear in the linking doc — if a link is attached, tag as Link not Item).
  - A **banners/special-items spreadsheet** tells you which banners to box per page (Column A = page, Column C = items). When no spreadsheet is provided, box known banners as shown in the examples.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-selection ON).** Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs; **exclude disclaimer**. Do **not** tag brand in the name field.
  - **SKU:** tag without the `#`; first SKU only for multi-SKU items; number SKU only (not model number); blank if none.
  - **URLs:** search the item SKU on lowes.com (USA site); copy the **product page** URL (never a search page). No SKU → leave blank. "DO NOT PUT LINK" / "Find in Store" → leave blank.
- **Image QC:** prioritize clean PDFs / data-piped images; select a **cutout** for combo items (e.g. washer + dryer).

## Post-processing (DOC-owned)

- **Links QC:** everything in the linking doc is a direct link; "Find in Store" items get no URL and are marked in-store only; ensure items with a SKU have a URL.
- **Item Category QC:** item-level categories must match the Lowe's website (top-most category). Export items, clean to `item_id, name, sku, analytics_categories`, review the key category buckets (Outdoor Power Equipment, Outdoor Tools & Equipment, Hardware, Home Decor & Furniture, Bathroom, Grills, Kitchen, Seasonal Living, Smart Home), re-import and QC. Send the item export (named `XX.XX-DIY_CategoryReport.csv` / `XX.XX-PRO_CategoryReport.csv`) to the retailer Mon / early Tue.
- **Tracking codes:** fill tracker columns A–F, apply the resulting variable, mark applied.
- **Mark In Store Only (MISO):** do this **before** running the custom action, otherwise URLs may populate on SKU-tagged items not meant to have one.
- **Custom action — "Lowes USA Product Feed":** matches page items by SKU and updates name/URL/image/rating/description from a retailer text file. Run **after** Links QC, Item Category QC, and MISO.
- Check **item-level valid dates**; **store check** — ensure required stores are in their pricing zones.

## FQC / flyer review

- Complete: autostack spotcheck, Links QC, Item Category QC, tracking codes, MISO, multi-product examples, custom action, standard-4 thumbnails, triggers created (valid Thursday 12:01 AM), edit details (no theme, external run name "Weekly Ad", **hidden in distribution & Flipp with triggers set**). Send preview link + category report.
- **Flyer Review type: Lite.** Three ads exist: DIY (everywhere), Pro (everywhere), Lowe's For Pros Pro (hosted only); all live one day before valid. Pro ads need lowesforpros.com URLs; tracking URL uses the Lowe's merchant only. ~214 pricing zones; FSA geography consistent WoW; **Grand Openings are priority 1** — dedupe overlapping FSAs.

---
*Source: Lowe's USA OneGuide (Google Doc `1rgRoHU7d0Vpc1VF-Y3F8HEz1lCMu0MGWn5FXg9osSs0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
