# Provigo — Processing Guide

> **Source:** Provigo OneGuide (Google Doc `1khEVVNokD5U6hfym-SjS8TahCK5h4v6E_EFtGuLCte0`), updated Dec 18, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account segment | Core+ (Relationship: Excellent) |
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#loblawops`, `#loblaw-lcl` |
| Flyer types | Weekly (5592 / flyer type 6006) |
| Processing | Auto-stack; Vendor setup, OS setup, Flex + DOC QC; Feedel (retailer data services) yes; no coupons |

Loblaw banner, bilingual (FR + EN). Files received Monday.

## Files & schedule
- **Cadence:** Available Tue → Mon; Valid Thu → Tue. **Preview: Sunday.**

## Upload & setup (Flex)
- **⚠️ NEW 2026 — set pixel height to 4096 BEFORE any pages are uploaded.** Open flyer run → Edit Details → show/hide rarely-used fields → Height dropdown → select **4096.0 pixels** → OK. If pages were already added before this step, flag the Full-Time Ops stakeholder and continue.
- Weekly flyer = codesheet upload with manual-stores troubleshooting.
- **Set the Sunday preview:** flyer run → Overview → Edit details → Preview start date = the Sunday before the available date → OK.

## ⚠️ Common errors / risk items
- **Tag all "PC Optimum" buttons** with the `pcoptimum.ca` link.
- **Joe Fresh pages:** tag all Joe Fresh items as **ONE box** and as a **direct link** (Joe Fresh diff-groups URL in the OneGuide).

## QC specifics
- **Box Draw** (**Medium**; Auto-Box **ON**, Box QC bot **ON**): draw a box wherever there's a unique price. Box special weblinks. **Include** coupons, packaged deals, special weblinks; **exclude** retailer logo, sign-up page, social media.
- **Tag / Tag QC** (Low; Auto-tag **OFF**): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Name:** `[FRENCH NAME], [SIZE] | [ENGLISH NAME]` — bold text, tagged in **both FR and EN** if both are on the PDF, separated by `|`, in **all caps**. Do NOT include in the name: alternative unit pricing (e.g. "6.59/kg"), "Product of…", "No 1 Grade", "Frozen", "Selected varieties".
  - **Description:** non-bold text; first letter capitalized; put alternate unit prices and the "Product of…/No 1 Grade/Frozen/Selected varieties" items here. **Do not put the SKU in the description.**
  - **Article Number fields** (special tagging fields at the bottom): paste the Product SKU into the Article Number field — one SKU per field. Article Number 1 = the same number as SKU and Fetch URL. Include the unit of measure (`_KG`, `_EA`, `_LB`, `_C12`, `_C24`, etc.). Multiple SKUs → first→Article Number 1, second→2, third→3, fourth→4.

## FQC (DOC)
- Merge any remaining flaps. Check dates, no theme, toggles (available everywhere). External run name = **"Weekly Flyer - Valid Thursday, (Month + day) - Wednesday, (Month + day)"**. Thumbnails, geography, FQC checklist.
- **Flyer Review type: Lite.**

## Out-of-processing
- **Page swap:** standard page swap.

---
*Source: Provigo OneGuide (Google Doc `1khEVVNokD5U6hfym-SjS8TahCK5h4v6E_EFtGuLCte0`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
