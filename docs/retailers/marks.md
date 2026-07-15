# Mark's — Processing Guide

> **Source:** Party City CAN / Mark's OneGuide (Google Doc `1r7d4NSK1zUephrsRRNTVFI3yWcEFR-huZ70R72c3SQc`), updated May 11, 2024. Contacts/credentials omitted.

> This OneGuide is shared between **Party City Canada (3632 Local Ad)** and **Mark's / L'Équipeur (LEQ)**. This article covers the Mark's family; Party City CAN specifics are summarized at the end.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel | `#partycitycanada` |
| Hosted URL | partycity.ca (Mark's shares marks.com / lequipeur.com) |
| Flyer types | **Mark's** (weekly, EN) · **L'Équipeur / LEQ** (EN + FR, hosted, then cloned Flipp-only) |
| Processing | Auto-stack; Strategic Ops **Yes (Feedel)**; no coupons |

### Mark's three-flyer structure (all go live together)
- **Mark's merchant → Mark's flyer type** — EN.
- **Mark's merchant → L'Équipeur flyer type** — EN + FR (Hosted).
- **Clone to L'Équipeur merchant → LEQ flyer type** — EN + FR (Flipp only, hide in hosted).
- Two different merchants share the same website.

## Files & schedule (Mark's / LEQ)
- **Files received:** Monday. **Cadence:** Available From Tuesday, Valid From Wednesday → Available/Valid To Tuesday. One-day preview.
- **Linking document:** Yes — SKU "SN" document (pages with SKUs printed on images) + a URL document emailed weekly.

## Upload & setup

### Mark's (EN) — owned by DOC
1. Manually upload pages (select `nat` folder, uncheck `sn`) → Auto-group.
2. **1 PZ: Base.**
3. Assign stores from the **generic codesheet** (Marks tab), download as CSV.
4. **Codesheet upload:** Config **`generic_stores`**, PDF base directory `/`, **check off first toggle only**.
5. **SN process:** upload the "NAT-WK xx -SN" PDF (SKUs on images) to the shared Google Drive. ⚠️ **RISK: FTP breaks it into multiple pages — attach the one large document.**
6. **URL document manipulation:** delete columns *Family ID/Web ID*, *Overarching offer URL - LEQ*, *Product Landing Page URL - LEQ*; delete top rows (Project, Docket Number, contacts); save as `.xlsx`; attach to all vendor tasks with the note referencing pages 31–32 of the OneGuide.
7. **Edit Details:** available everywhere; one-day preview; no theme (Black Friday/Holiday occasionally). 4 standard thumbnails.

### L'Équipeur / LEQ — owned by Flex
- Manually upload pages (select `leq` folder, uncheck `sn`), ENG toggle; upload same pages again toggled FR. ⚠️ **RISK: sometimes LEQ has FR pages only — that's fine, upload FR only (no need to confirm).**
- Auto-group. **PZs: EN + FR** (or just FR if only FR names).
- Assign stores from generic codesheet (LEQ tab). ⚠️ If FR-only zone, delete EN stores/PZ from codesheet.
- Codesheet upload: Config **`generic_stores`**, base `/`, first toggle only.
- SN + URL document process as above (delete Mark's columns, keeping both if LEQ has EN+FR content).
- **Edit Details:** available **only on hosted**; one-day preview; no theme usually. 4 standard thumbnails.

## QC specifics (Mark's / LEQ)
- **Box Draw (Low; Auto-Box ON, Box QC bot ON):** linking doc required. **Include** packaged deals, retailer logo, sign-up page, special weblinks; exclude coupons, social media. Also **box the sale-callout section** (prices + callout). Sign-up pages link to marks.com / lequipeur.com.
- **Tag / Tag QC (Low; Auto-tag OFF):** include name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price. **Exclude URLs** (applied via item import).
  - Name/Brand = bolded text or per SN document. SKU from SN/URL doc. Usually 1 price (Current).
  - **Sale-callout section:** URL = overarching offer URL (column F); tag **ALL** SKUs in the callout.
  - **Regular items:** URL = Product Landing Page URL (column H); tag only individual SKUs. If a Product Landing Page URL is blank/N/A, use the Overarching offer URL.
- **Image QC:** **clean PDF preferred**, cutout otherwise.

## ⚠️ Common errors / risk items
- FTP splits the SN document into many pages — attach the single large file, not the split pages.
- Keep EN pages → EN links and FR pages → FR links (LEQ).
- URL doc: copy/paste as values to remove formulas; delete blank rows (triangle banner, email sign-up); ensure search-link URLs are reflected.

## URL/Links & SKU QC (owned by DOC)
- Build the import: dedupe/clean the URL sheet; replace *Style Number* → *SKU*; add `item_id` column; duplicate into Mark's (`item_id, sku, url`) and LEQ (`item_id, sku, english_url, french_url`); download CSV → item import. If doing a trigger import, mark items in-store after the trigger runs.
- **SKU QC:** item search SKU IS blank — ensure no missing SKUs (cross-reference EN/FR page or SN document).

## FQC / flyer review
- **Mark's FQC:** SKU check (all items have SKUs if applicable); items without URL → fill from URL doc; sign-up page → marks.com/en.html; Image QC clean PDF/datapipe first; page categories skip p.1; mark items in-store via Sessions.
- **LEQ FQC:** as above (EN↔EN, FR↔FR links) then **clone LEQ flyer to the LEQ merchant** (uncheck Clone to Mark's; add "(Flipp)" to name; no tracking codes; hide in hosted + avail in distribution & Flipp; assign stores via codesheet; 4 thumbnails).
- **Post-FQC:** send preview link to retailer (Mark's + LEQ) per email template.
- **Flyer Review type: Lite.**

## Party City Canada (3632 Local Ad) — summary (shared doc)
- **Cadence:** files Monday; Available/Valid From Friday → Available To Monday / Valid To Tuesday. Strategic Ops (Feedel).
- **Upload (Flex):** upload FR pages first (toggle FR, Save & refresh — toggles can revert), then EN pages; auto-group (watch FC=front/BC=back cover); 2 PZs (EN, FR); assign **all regions excluding MB & QC**; Standard 4 thumbnails. Invalid-stores-assigned warning can be ignored.
- **Box Draw (Auto-Box ON, Box QC bot ON):** include retailer logo, sign-up page, special weblinks; exclude coupons, packaged deals, social media. Box last-page banners (Celebrate Life's Moments → partycity.ca; Triangle → triangle.canadiantire.ca; Financing links); box SKU'd items.
- **Tag (Auto-tag OFF):** **no linking doc going forward — search SKUs on partycity.ca** and box/tag per the site. Name matches website; **do not include website description**; URL = the item's page from the SKU search. Exclude description; include SKU.
- **FQC:** Standard 4 thumbnails; mark items in-store; UTM tracking codes for promoted flyer only (reapply after page swaps); Page Level Modifier → Zoom Always Page Fit; check EN/FR last-page banners.
- **Cloning:** Party City has a promoted and a non-promoted version. Clone under ad-hoc processing, prefix `[NOT PROMOTED]`, do not copy tracking codes; set EN & FR stores to **Manitoba and Quebec** only.
- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Party City CAN / Mark's OneGuide (Google Doc `1r7d4NSK1zUephrsRRNTVFI3yWcEFR-huZ70R72c3SQc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
