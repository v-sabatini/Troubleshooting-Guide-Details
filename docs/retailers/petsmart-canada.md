# PetSmart Canada — Processing Guide

> **Source:** PetSmart Canada OneGuide (Google Doc `1L6F2uSm19mIlJnoqA6oRca72oMCnxSzwxn4TRgdl5uM`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | **Tier 1 Premium** |
| Availability | All platforms |
| Slack channels | `#petsmart-can` |
| Hosted URL | pets.petsmart.com/local-ad/canada.shtml |
| Flyer types | Monthly Flyer (8047) · Weekend Flyer (131) · Lookbooks (109) |
| Processing | Auto-stack; Flex does Flyer Review; OS does Setup; **Feedel/Strategic Ops: Yes**; no coupons |

## Files & schedule

- **When files arrive:** Monday. All 3 publications get a 1-day preview (communicated via email).
  - **Monthly (ML)** = the "weekly" · **Lookbooks** = ad-hocs · **Weekend flyer** = anything that isn't ML or Lookbook.
- **Bilingual account** — EN and FR pages/pricing zones (**163 stores total**).
- **Workflow:** Upload & Setup (DOC) → FQC (DOC).

## Upload & setup (owned by DOC)

- Pages → Edit → select the ad folder → add English pages → **re-upload the same pages and mark them French** → auto-group all pages → save and complete.
- Create **EN** and **FR** pricing zones; add all 163 stores.
- **Linking document (via email):** open in Google Sheets, add a column to the right of "offer"; label the offer column "English" and the new column "FR translation." Use `=GOOGLETRANSLATE(cell,"en","fr")` down the column, then copy/paste as values. Replace any text in the JBP column with "Y" (leave blank cells blank). Append "EN and FR" to the document name, download as `.xlsx`, attach to all vendor tasks.
- Apply tracking codes and tracking URLs (can be done at FQC).

### Setup QC (owned by DOC)
- Standard 4 thumbnails.
- **UTM campaign codes** vary per publication (tracked in the campaign sheet; ad types colour-coded: green = Monthlong Planners, yellow = ad-hoc Lookbooks, blue = Weekend Events). To find the code, copy the last code for that flyer type and increment the trailing digit (e.g. `ca-mplan-fy25p2` → `ca-mplan-fy25p3`). Apply as: Code Type Dynamic Variable, Source Distribution, Variable `utm_campaign`, Value from the sheet.
- **Tracking URLs (do NOT change):** apply the Impression, Open, and Engagement DoubleClick URLs (Flipp App) — grab them from a previous live flyer.

## QC specifics

**Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF; linking doc required):**
- **Include:** retailer logo, sign-up page, social media (Instagram/TikTok/Facebook PetSmart Canada), special weblinks.
- **Exclude:** coupons, packaged deals.
- Items with "Y" in the JBP offer column get one box around every item. **Treats Rewards pages:** one item box around the image and one text box around the product description, consistently across the page; a "5X points" callout on a new line in the linking doc must be boxed itself. Ecomm flyers that don't meet content policy — box so they do and tag using the linking-doc links (Display Type Item).

**Tag / Tag QC (Low; Auto-tag ON; linking doc required):**
- Include: name, description, price, sale story, categories, disclaimer, original price, URLs. Brand is Box-specific. **Exclude pre/postfix, valid dates, SKU.**
- **JBP Offer custom field:** for all item names with "Y" in the JBP Offer column, tag "Y" in the JBP field at the bottom of the tagging interface (EN and FR); Display Type Item even if it's just a URL.
- **Brand:** from the linking doc; if "N/A" don't tag; if "Various" don't tag the brand field.
- **Name:** use English Item Name for EN pages and French Translation Item Name for FR pages — **the PDF shows English but FR pages must be tagged with the French translation.**
- **Description:** add the measurement (kg, g, lb, etc.) from the linking doc.
- **⚠️ #1 risk — price ranges:** tag the *lower* value as Current Price and *-upper* value in the postfix. **Do NOT put the range in the sale story** (e.g. $14.99–19.99 → Current Price $14.99, Postfix -19.99).
- **Sale Story (Ecomm Event only):** for shop-animal banners at the bottom, tag with the big sale story ("Spend $100+ Save…") plus the disclaimer to meet CP (Display Type Item).

**Image QC:** use cutouts for ad blocks with multi-items; clean PDFs where available for single-item ad cells.

## Final QC (owned by DOC)

- Item Search — Name Contains "Dog"/"Cat"/"Small Pet"/"Fish"/"Bird"/"Reptile", Language French: ensure no truly-English item names (brand names like "Tiki Dog" are OK to skip); fix true English results via Google Translate.
- Item Search — Sale Story Contains "-", all languages: **ensure no price ranges are tagged in the sale story** (must use Current Price + Postfix).
- QC categories complete; image QC (cutouts for multi-item cells); tracking codes (Dynamic Variable → Distribution → `utm_campaign`); tracking URLs (same 3 for all pubs). Apply any triggers for alternate covers/pages/inserts.
- **Assign FSAs from CSV:** System → custom actions → assign FSAs from CSV, using the template; update flyer_id columns with EN and FR PZ IDs, download each as its own CSV, **run the custom action twice** (both zones; should yield 1675 FSAs). **Re-run after any page swaps.**
- Complete FQC; send a preview email listing publication + preview link, live/valid dates, and ad title (external run name); action revisions.

### Monthlong Planners only
- For the Week 1 / Hosted flyer, create triggers to **hide in Flipp** and **hide in distribution**, effective the first Sunday at 11:59 pm after week 1. Don't change valid dates (Hosted runs the full duration).
- Every Friday, **clone** the monthly publications (name them week 2, 3, 4…), select **copy tracking codes**, change available dates Monday–Sunday, hide hosted for clones (valid dates unchanged), and create triggers for the clones (they don't copy over). Reassign FSAs if page changes are made.

## Flyer Review

- **Type: Lite** (owned by Flex).

---
*Source: PetSmart Canada OneGuide (Google Doc `1L6F2uSm19mIlJnoqA6oRca72oMCnxSzwxn4TRgdl5uM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
