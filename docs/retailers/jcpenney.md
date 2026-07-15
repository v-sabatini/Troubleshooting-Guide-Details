# JCPenney — Processing Guide

> **Source:** JCPenney OneGuide (Google Doc `1ls1tJRSfaZ_xgJHcU7xP-YZY4HvZsGrs-BNTDBZqzNo`), updated Feb 10, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Standard / Core+ |
| Availability | Hosted only (2501); Flipp & Distro clone (7729) |
| Slack channels | `#jcpenneyops`, `#jcpenney`, `#jcpenney_mergil`, `#jcpenney-sep`, `#jcpenney-gma` |
| Hosted URL | jcpenney.com/m/digital-books |
| Flyer type(s) & cadence | **Mailer (2501)** — Hosted, all processing done here · **Mailer (7729)** — Flipp/Distro clone. **Ad-hoc** cadence. |
| Processing | Auto-stack |
| Who's involved | DOC does all processing; no Flex; Strategic Ops (retailer data services) |

## Files & schedule
- **Files received:** Ad-hoc (dates confirmed in the assets email). Store Ads / Circular publications are managed and processed by CP, not here.
- **Publication cadence:** all dates ad-hoc. **No customer preview** — internal/client preview set for **5 business days after files received**.
- **SKU document** is included in the assets email — it must be manipulated, emailed to OS, and attached to vendor tasks.
- **Schedule:** an emailed monthly schedule drives shell creation. Create flyer shells under **both** flyer types using the schedule dates (add " - Flipp" to the internal name of Flipp/Distro shells). Populate Flyer Run ID and Direct URL columns; return the updated schedule.

## Upload & setup

- **Assets** delivered via Egnyte: PDFs, pagination instructions, event code (= external run name), coupons (0-3 PDF versions), optional data sheet. Types: Mailer = hosted, Mailerflipp = flipp (**upload the hosted version first**).
- If Page 2 has coupons / an online-coupon link, it's often moved to the end of the flyer before the standard last pages.
- **Upload:** manual-upload all individual pages, index per instructions. One PZ "Base"; assign all stores and **remove Puerto Rico stores**.
- **Setup — dates (CST):** Available from 1 AM; Available to 12:59 AM the next day; Valid from 1 AM EST; Valid to unchanged. Confirm PDF dates match the schedule.
- **Toggles:** Hide on Flipp & Distro (Hosted only). **Theme: never apply to the Hosted clone (no theme always).** Set vendor tasks to HIGH.
- **SKU doc manipulation:** keep headers `page_name, sub, lot, feature_description` (delete other columns); remove rows with no sub/lot or description; add a `sku` column with `=TEXT(B2,"000") & "-" & TEXT(C2,"0000")` and paste as values; delete blank/0-SKU rows; rename pages if desired; save as `JCP_<adname>_skulist`; attach to tag & QC; email OS if there are special tagging instructions.

## QC specifics

### ⚠️ Risk items
- **Coupons:** "JCPenney" must be tagged in the **Brand field** so the coupon appears in the JCPenney search-results dashboard on Flipp Web.
- **Vertical publishing:** confirm vertical published via the Storefront Summary page.
- **Flyer sorting:** most recent on top; Store Ads over Puerto Rico over Mailers.

### Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc required)
- **Include** coupons, packaged deals, sign-up page, special weblinks. **Exclude** retailer logo, social media.
- Box: JCPenney App, Shop 24/7 at jcp.com, Fast + Free Same-Day Pickup, Special Financing, Coupon Direct Link, barcoded coupons (text box required for disclaimers/fine print). Exclude the JCPenney logo and Viznav/category pages.
- **Jewelry flyers:** if unclear what image relates to which price → box together; multiple prices lumped despite indexed items → box each pricing group; one price / multiple item sets → box each set with a "text" box over the price.

### Tag / Tag QC (Low; Auto-tag OFF; linking doc required)
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Jewelry:** one image / price range → tag prices as a RANGE listing all SKUs; multiple items in one box with one price → tag the price + title and add SKUs; one price / multiple items → tag by center title and price, SKUs from the images.
- **Coupons spotcheck:** item type Coupon; Brand JCPenney; Name "Featured Coupon"; apply override dates for Hosted; Categories = coupons & coupon; Category highlights = coupons; Google Category = Not Available.

### Image QC
- No image QC (Hosted 2.0); leg heights inconsequential.

## Post-processing (DOC)
- **Back cover line items:** if present, make front-cover images interactive using the back-cover tagging info.
- **Disclaimers:** ensure flyer-level "book disclaimers" aren't applied to adjacent items.
- **Coupons:** upload hosted image to S3 (OLPP, JPG); QA copy vs. PDF, "82" in Hosted barcode, discoloration; tag by copy/paste of the hosted image URL + apply override dates; add category copy to the right coupon's sale story. SFSC: 1 page/slice; include online code in the MAIN slice (do not hide in disclaimer); last page products on top, app callouts on bottom.
- **Item Category QC:** iFrame preview — QA that listed categories are actually in the ad and each links correctly.
- **Original Price QC:** item search Original Price is not blank — remove manually (small) or via item export/import (large).
- **SKU QC:** item search SKUs containing "/" → remove the "/" and the 3 numbers following (e.g. `272/472-8099` → `272-8099`); large batches via export/import find-and-replace.
- **URL/Links QC:** standard week-over-week URLs (Financing home/mattress, Jewelry financing, App, Curbside Pickup, Rewards — full URLs in the OneGuide); **Viznav page** category URLs change by mailer type — copy items from the most recent flyer of the same type via Pages → Copy Items.
- **Tracking codes:** Overview → Manage Tracking Codes at flyer-run level, dynamic variable, hosted, `utm_source`; change the two highlighted URL portions to match the pub name; Apply All Tracking Codes. **Must put `utm_source` in the tracking codes** or the utm code inserts in the wrong spot.
- **FQC:** normal checklist; **ignore "tracking URLs applied" and MISO**.

## Post-FQC → JCP review → clone
- **Item export:** remove flyer items; keep item_id, page, name, sku, url, description; **remove all coupons**; QA page numbers; add vertical preview URL to the top; save as XLS.
- **Preview link to JCP:** send export + preview link with the URL due date (in red/bold); note that changes in other columns must be highlighted.
- **Item import:** ~2 days to action & clone; changes highlighted yellow; item import (item_id, sku, url) as CSV with sku column cleared; re-verify URLs; re-apply tracking codes; confirm direct links become "Link" format.
- **Clone (2501 hosted → 7729 flipp):** into existing shell; check dates, toggles (Hidden in Hosted), external run name (EN only, from "event name"), theme (not applied to Hosted). Clone coupon if Flipp/Distro-specific (different barcode) — override images for all 3 platforms with the Flipp (84) JPEG, draw barcodes per interactive area, add valid override dates, tag "JCPenney" in Brand. Clone tracking codes (code #1 app, code #2 native). Clone FQC: normal checklist + confirm vertical published via Storefront Summary.
- **Flyer Review type: Lite.**

---
*Source: JCPenney OneGuide (Google Doc `1ls1tJRSfaZ_xgJHcU7xP-YZY4HvZsGrs-BNTDBZqzNo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
