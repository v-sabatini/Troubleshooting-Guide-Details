# Westlake Ace Hardware / WL Ace Hardware — Processing Guide

> **Source:** Westlake Ace Hardware OneGuide (Google Doc `155UmcVbOSyiD_Ng4CcuzDGVyQgGccTipCPr5INSVM7Y`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment / tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#westlakeace`, `#westlakeace_nativex` |
| Flyer types | Circular, WL Ace Hardware Hosted, Dennis, Circular (Flyer Types 1–4) |
| Processing | Auto-stack; Flex = Flyer Review; OS = Setup; **Strategic Ops: yes** (Feedel); no coupons |

## Files & schedule

- **Files received:** Monday. Available Mon→Mon; Valid Tue→Tue. **No consumer preview.**

## Upload & setup

- When files arrive, open page 1 in the SFTP to check publication dates. Create a new flyer run in the **Circular** flyer type; Valid/Available dates = what's on the publication.
- **Manual upload** all SFTP pages; build a pricing zone **based on the file name** — the location abbreviation sits between the first `_` and `_Final` (e.g. `2241001ml_fn_final_p0005.pdf` → **FN** pricing zone). Confirm all pages uploaded.
- Standard 4 thumbnails; confirm dates match; complete Setup QC checklist.

### Pricing-zone store distribution (from the XLS)

- SFTP → search XLS → open the XLS matching the file name.
- Delete rows down to and including the "Store #" row; delete "Store location", "Store brand", "Ad Market" columns.
- Format column A → Numbers → **Generic** (removes leading zeros). Insert a header row: column A = `stores`, column B = `pricing zone` (lowercase, no quotes).
- **Find-and-replace the pricing-zone name so it EXACTLY matches the flyer-run PZ naming (CA, Core, Dennis, etc.) — otherwise stores will not be assigned.**
- Download as CSV → Codesheet tab → upload with **config `generic_stores`**, PDF base directory `/`, **toggles 1 and 6 only**.

## QC specifics

- **Box Draw — Low; Auto-Box OFF, Box QC bot OFF.** Include **social media**; exclude coupons, packaged deals, retailer logo, sign-up page, special weblinks.
- **Tag / Tag QC — Low; Auto-tag OFF.** Include name, pre/postfix, description, price, sale story, categories, disclaimer, original price, **URLs**. Exclude valid dates, SKU.
- **Image QC:** clean white PDF where possible, otherwise cutout. Generate images if none appear, untoggle "data pipped" + "PDF images" and re-check.

## FQC / out-of-processing

- Category QC (DOC): Google category on all items. Ad-hoc: file dates = flyer-run dates (flag mismatch to full-time processor); external run name = publication name on page 1.
- **Out-of-processing — clone 3×:** after FQC, clone the run for **CA FLIPP, CA HOSTED, and Dennis**. For each: verify image QC/thumbnail/category copied; open the PZs NOT being distributed to and remove all stores; re-run the store-distribution XLS + `generic_stores` codesheet; complete FQC checklist.
- **Flyer Review type: Lite.**

---
*Source: Westlake Ace Hardware OneGuide (Google Doc `155UmcVbOSyiD_Ng4CcuzDGVyQgGccTipCPr5INSVM7Y`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
