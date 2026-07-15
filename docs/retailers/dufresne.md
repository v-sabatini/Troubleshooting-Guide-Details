# Dufresne — Processing Guide

> **Source:** Dufresne OneGuide (Google Doc `1ECTSom1Eg16EZ58s5-spBkSQeClSgagWS_ZrmNPVjgU`), updated Dec 17, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#dufresne` |
| Hosted URL | dufresne.ca |
| Flyer type(s) & cadence | **Flyer** — ad hoc |
| Processing | **Trim Stack**; Flex (Flyer Review); OS (Setup); no coupons; **Feedel / retailer data services: Yes** |

## Files & schedule

- **When files arrive:** Monday. Available From Monday · Valid From Tuesday · Available To Monday · Valid To Tuesday. Preview date: Monday.

## Upload & setup (owned by FLEX)

- **Manual upload:** files are dropped as a whole flyer; FAdmin splits it — choose the split-up pages.
- Create **one pricing zone (Base)**; add all stores.
- **Mass-attach the Links document** (from the FTP) to all vendor tasks (Box Draw, Box QC, Item Tag, Item Tag QC).
- **Setup QC:** confirm the dates on the flyer cover match the flyer run dates; not hidden anywhere; **set theme**.

### ⚠️ Common errors / risk items (retailer-specific)

- **Look for multiple products** in a single image/block.
- **Do NOT add Thunder Bay (store 40) to any Pricing Zone.**
- **URLs will not appear in the preview** due to merchant settings, but should appear once the flyer goes live (don't flag as missing).

## QC specifics

- **Box Draw (Low; Auto-Box ON, Box QC bot ON).** Linking doc required (Box-specific). **Box each product SKU individually; box banners.** **Include** special weblinks. **Exclude** coupons, packaged deals, retailer logo, sign-up page, social media.
- **Tag / Tag QC (Low; Auto-tag OFF; PDF Image Auto Selection ON).** Linking doc required (Tag-specific). Include name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude pre/postfix and valid dates.** Brand handled via Box Draw/Box QC.
  - Add the postfix **"after savings"** where applicable.

## Final QC / go-live (owned by DOC)

- **Tracking codes (Weekly Ad):** flyer-type codes are preset; manually add one at the **Flyer Run level** → Manage Tracking Codes → Add Code under Flyer Run: Type Dynamic Variable, Code Source All, Variable Name `utm_campaign`, Variable Value = the highlighted `utm_campaign` value from the URL in the flyer notes (**changes month over month**, e.g. `housepartysale`). Confirm, then **Apply All Tracking Codes.**
- Item-without-URL search; verify non-items (headings/callouts) that need tagging/linking; spotchecks.
- Legibility meets **50/30**; QC thumbnails + custom tiles; Item Image QC; page categories.
- Spotlights: ensure external name matches the spotlights; storefront spot check; confirm live dates match page 1; check storefront sale story; category thumbnails; **Mark In-Store Only**; add all tracking codes.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: Dufresne OneGuide (Google Doc `1ECTSom1Eg16EZ58s5-spBkSQeClSgagWS_ZrmNPVjgU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
