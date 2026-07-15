# London Drugs — Processing Guide

> **Source:** London Drugs OneGuide (Google Doc `1nvWGfMpn83Lg6itzC18wfvJxa31fW84y-YiJ8qMHTcw`), updated Jul 16, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | **Special (West): Flipp only.** Pharmacy/Baby & Kid/Electronics/Home & Garden (West): **Hosted only** |
| Slack channels | `#londondrugs`, `#3fl-london-drugs` |
| Hosted URL | londondrugs.com/store-flyers/eflyer.html (West) |
| Publications | Special (Weekly, West) · Pharmacy/Baby & Kid/Electronics/Home & Garden (Weekly/Monthly, West) · Luxury (insert) |
| Processing | Auto-stack; Flex 3FL; no coupons; Feedel/retailer data services |

## Files & schedule

- **Files received:** Friday.
- **Cadence:** Available From Thursday, Valid From Friday; Available/Valid To Thursday. **⚠️ Dates vary** — sometimes Thursday–Wednesday, sometimes monthly/weekly; always check flyer dates.
- **Preview date:** Thursday. Linking doc = Workfront/ecomm proof (numbered files) sent by email, attached to vendor tasks.

## Upload & setup (owned by DOC)

- Confirm the page-1 valid date matches the run; set available date one day before valid (1-day consumer preview). No theme. External run name = "Weekly Flyer", or for ad-hoc use the page-1 main heading (e.g. "Showcase"). Check availability per flyer type.
- Upload files for corresponding flyers (may be multiple). **Ignore files labelled "numbered".** File names follow "first letter of month + Day + Page #" (e.g. `M01P1` = May 1 page 1). SFTP manual upload (Friday). One zone = **West**; add the West store zone.

### Setup QC checklist
- Check dates; sessions run; legibility heights **60/40**; geography (no missing/added stores); 4 thumbnails; preview date Sunday after upload. Update the flyer-links file (proof link + relevant pages), download as XLS, attach to all vendor tasks. Add flyer run ID to the London Drugs Flex Tracker (working-doc + Workfront tabs).

## ⚠️ Common errors / risk items

- **Setup QC:** flyer dates sometimes Thursday–Wednesday at random — verify.
- **Image QC:** data-piped images (see Image QC / revisions below).
- **Multiple-revision ecomm proofs:** if revised page proofs arrive, email the vendor teams (Invensis + DSP) with the corrected numbered-file links per the template.
- **Electronics pages** (TVs, computers/laptops, cellphones, cameras) are risk items with dedicated rules (see Live-dates risk items).

## QC specifics — box/tag driven by the Numbered Files (Workfront proof)

**How to box/tag from the proof link:** hover over items and click the comment bubbles:
- One bubble over multiple items = box & tag all with the SKU in the bubble.
- Multiple bubbles on a group = box & tag each with the SKU in its bubble, **NOT** the SKUs on the page.
- No bubble, SKU on page = box & tag normally.
- Clicking a bubble highlights (yellow) where boxes go and crosses out SKUs that should NOT be tagged; nearby non-highlighted items with un-crossed SKUs are boxed separately. Bubbles can be **yellow, red, or black** — don't miss any.

- **Box Draw (Low; Auto-Box ON, Box QC bot OFF):** linking doc required. Exclude coupons; include packaged deals, retailer logo, sign-up page, social media, special weblinks. Use text boxes, box close to the image. Box FREE/BONUS items if they have a SKU/FLV/bubble (else include in the parent item's box). Box all "shop online", londondrugs.com and LDExtras.com callouts, and inserts (Workshops, Top Picks, Newsletter, digital blades).
  - Insert links (tag as Link): LD Extras `ldextras.com`, "Over 10,000 items on SALE" `londondrugs.com/on-sale-every-week.html`, londondrugs.com callouts `londondrugs.com/ldhome/`, plus Newsletter/Workshops/Shop Online and the PL/Cerave/Safety/Apple digital-blade URLs listed in the guide.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF image auto-select ON):** linking doc required. Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
  - **Description must match the flyer verbatim** (case, periods, bullet points). Model # always on its own line at the bottom.
  - **SKU** taken only from the Numbered Files (never the website). Format: "L" SKUs keep the L and drop `.PSD`; remove the FLV.
  - **Sale story** copied word-for-word, character-for-character (often a red banner around the price); combine multiple stories.
  - **Disclaimer:** add "*Plus deposit and enviro fees where applicable.*" for food/beverage items whose price ends in `*`.
  - URLs fetched using SKU (all items with SKUs).
  - **Page categories** from the title at the top of each page (page 1 needs none). Item categories chart: Appliances, Babycare, Beauty, Cameras, Computers, Electronics, Food & Pantry, Health & Personal Care, Home & Lifestyle, Outdoor Living, Toys & Recreation.
  - **Luxury flyers** ("luxury" in the name): specific sales-story / disclaimer / description rules — "Luxury Event"/"Derm Event" callouts add a sales story + disclaimer to ALL items on the page; green-circle callouts go at the bottom of the description; red-box callouts = sales story on all items.
- **Image QC:** clean no-background PDF where possible; when the PDF has a black background use "do not use pdf image" (cutout).

## Post-processing (owned by Flex)

- **Item Category QC:** verify Name/Description/Sales Story/Disclaimer match the PDF; multi-product items list all bold names + descriptions in Name; watch hero sales stories outside the boxed area; **disclaimer should NEVER be entered in tagging** (data-piped image shows it digitally); food pages often lack names (follow the link); electronics pages are risk items.
- **SKU/URL QC (Flex):** Export Items report → build a corrections CSV (item_id, sku, url) → Import Items. URL structures: `londondrugs.com/products/l/p/` for L/M SKUs; `londondrugs.com/search?q=` for hypernym/FLV SKUs; brand-specific links from the Workfront proof. Flyer proof takes precedence over these rules.
- **Description export/import cleanup:** highlight rows with description errors (line breaks, model # placement, spacing, bullets), edit, import.

## FQC / flyer review (owned by DOC)

- External name "Weekly Flyer" or ad-hoc page-1 heading; Standard 4 thumbnails; data-pipe images as much as possible; add inserts (Proudly Canadian last in all PZs; digital blades per email); Protection Plan link; apply tracking codes (Dynamic Variable, Source All, Variable **utm_content**, value = lowercase month/day, e.g. `feb10`).
- **Flyer Review type: Simple** (owned by DOL).
- **Live-dates: flag** incorrect images, links to wrong pages, incorrect sales stories.
- **Electronics risk items** (detailed rules in guide): TVs (multiple sizes), computers (specs one per line, "Windows 10 Home" above specs, model # at bottom), cell phones (carrier in name, bonus in sales story, "$0" → current price 0), cameras (body-only tagged separately; added lens appended to name with "-", price = camera + lens).

## Out-of-processing

- **Preview:** send to the London Drugs team by Wednesday/Thursday; expect multiple revision rounds.
- **Image revisions:** if asked to use the cutout instead of a data-piped image, save the cutout, upload via Flyer → Upload File, and paste the generated URL into the item's "Generated Image URL" field.
- **Flyer sorting:** newest weekly (West then East), old weekly, ad-hoc, magazines last.
- West→East clone is **[DNU]** (do not use).

---
*Source: London Drugs OneGuide (Google Doc `1nvWGfMpn83Lg6itzC18wfvJxa31fW84y-YiJ8qMHTcw`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
