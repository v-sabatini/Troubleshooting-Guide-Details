# Supermarche PA — Processing Guide

> **Source:** Supermarche PA OneGuide (Google Doc `1Y3nsoo_toFQzFlvimccaZq6FMgBV-pGicYWDkHhKnUQ`), updated Jul 9, 2026. Contacts/credentials omitted.

> French-language grocery banner. Runs **two flyer types** (Weekly + Nature) and up to **3 weekly versions** (V1/V2/V3).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview`, `#onboarding` |
| Hosted URL | supermarchepa.com |
| Flyer types | Weekly Flyer (11930) · Nature Flyer (12205) |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **When files arrive:** Thursday (always short notice — upload right away so files process overnight).
- **Cadence:** Available Mon→Sun, Valid Mon→Sun. Nature Flyer runs **2 weeks**.
- No linking document. **Full-Time Ops creates any additional flyer shells (V2, V3)** weekly per the retailer's email.

## Upload & setup (owned by Vendor)

**Weekly Flyer — same steps for V1, V2, V3 (only pages and stores differ; V1 gets V1 pages, etc.):**
- Flyer-run dates may differ between V1/V2/V3 — do not edit dates if the common section notes they're correct.
- **Manual upload:** Pages → Edit → select all pages (except whole-flyer files) from the SFTP. **Do NOT upload "PA Nature" files to the Weekly Flyer type** (they go to the Nature Flyer type). Auto-group or number pages; ensure language = **French**. Save & Confirm — do NOT process internally.
- **Pricing zones:** create a **Base** zone (toggle French to see pages); then create **"Base CL"** — select French so all pages get added, then toggle Cross Language + English. Save & Confirm.
- **Stores:** V1 → Add All; V2 → Add All; **V3 → add only Ave Donegani & de Courtrai.**
- Setup QC: confirm pages uploaded (no un-uploaded SFTP pages), confirm dates (Mon→Sun), thumbnails Standard 4, preview dates set.

**Nature Flyer:** navigate to the "Nature Flyer" type; manual-upload only pages labeled **"pa nature"** (dates on file name must match the run). Auto-group, French language. Create Base + "Base CL" (Cross Language) zones; **add 2 stores only — "du parc" and "Park Ave."** Nature flyer runs for 2 weeks.

## ⚠️ Common errors / risk items (retailer-specific)

- **Always short notice** with pages (usually Thursdays) — upload immediately.
- **Do NOT mix flyer types:** "PA Nature" files → Nature Flyer type only; other pages → Weekly Flyer type only.
- **Names:** all pages are French, but some items also include English on the PDF. For those, include the English name in the Name field using **French Name | English Name** (e.g. `FILETS DE MORUE FRAÎCHE | Fresh Cod Fillets`).
- **Page merging:** check that no pages have been merged (Storefront Spotcheck) — click "don't merge" to fix.
- **V3 stores** are limited to Ave Donegani & de Courtrai; Nature stores to "du parc" & "Park Ave."

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF; no linking doc):** Include packaged deals. Exclude coupons, retailer logo, sign-up page, social media, special weblinks. For single and multi items, box the whole item block.
- **Tag / Tag QC (Low; Auto-tag ON; PDF image auto-selection ON):** Include name, pre/postfix, valid dates (if different from the main flyer), description, price, sale story, categories, disclaimer, original price; brand used for both box/tag. **Exclude SKU and URLs.** Use the French | English name format above.
- **Image QC:** PDF preferred if clean; otherwise cutouts accepted.
- **Spotchecks:** standard pricing; usually a lot of spelling-related spotchecks.

## Post-processing / Final QC (owned by Vendor)

- **Pre-Final QC:** confirm dates (from PDF) and availability toggles; spotcheck pages for the French | English name format; thumbnails Standard 4 (include retailer logo); confirm no merged pages (Storefront Spotcheck); check the Cross-Language PZ has been cross-languaged to English with the same pages/stores as the French zone; standard flyer-review checks (all boxed/tagged, spotchecks 20% of PZs, previews clickable, sessions complete, geography correct).
- **FSA Check (owned by DOC):** Full-Time Ops checks FSAs match the retailer's email (common V1/V2/V3/Nature breakdowns are in the linked sheet); run the **Assign FSAs from CSV** custom action if needed.

## Flyer review

- **Flyer Review type: Lite** (owned by FLEX). Checks: flyer dates, sessions completed, previews correct, all items tagged accurately, geography correct, availability toggles correct.

---
*Source: Supermarche PA OneGuide (Google Doc `1Y3nsoo_toFQzFlvimccaZq6FMgBV-pGicYWDkHhKnUQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
