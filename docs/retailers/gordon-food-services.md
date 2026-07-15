# Gordon Food Services — Processing Guide

> **Source:** Gordon Food Service OneGuide (Google Doc `1zZZzbkt_Z2Faf2y-xGEfrk2ePYNALUH-IQOaH-huucM`), updated May 1, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Premium |
| Availability | Flipp only |
| Slack channels | `#gordon-food-service-stores`, `#gordon-food-service-stores-nativex` |
| Hosted URL | None |
| Flyer type(s) & cadence | Weekly |
| Processing | Auto-stack |
| Who's involved | Flex owns processing; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Wednesday (retailer email contains the Link Sheet, distribution/store list for the week, and confirms dates). DOC forwards the email to PSS for processing.
- **Cadence:** Available From Sunday, Valid From Sunday; Available To Saturday, Valid To Saturday (1-week run).
- **Linking document:** Yes (link sheet + store assignment received by email).

## Upload & setup

- **Manual upload (OS):** Pages → Edit → select page(s) from FTP → Autogroup → Save & Complete.
- Create **pricing zones based on the retailer email & file names** (e.g. GO, NMI, BC, FL). **Select the LOWERCASE folder dropdown** so individual pages display and select all individual pages — do NOT select the uppercase files (those are entire PDFs). Autogroup, then assign pages to their pricing zones.
- **Generic store assignment** (store assignment varies week over week):
  1. Open the GFS_Generic Store Assignment spreadsheet; insert this week's store list.
  2. Duplicate the template tab, rename for this week.
  3. Each store has an "X" beside its version; sort right-to-left A-Z to group Xs per zone.
  4. Copy store numbers into the "stores" column; write the pricing zone name (page version) beside each. **⚠️ The pricing zone name must match Fadmin exactly — case sensitive, remove any spaces.**
  5. Download as `.csv`.
  6. Upload codesheet — **Name:** stores; **File:** the new CSV; **PDF Base Directory:** `/` (no spaces); **Toggles:** only Store Assignment. Save → Process.

### Setup QC
- **Attach link sheet** as a mass attachment to Box QC, Tag & Tag QC.
- Edit Details: dates per retailer email; **Hidden on Hosted**; no preview date; internal run name W01/W02/W03; no external run name; no theme.
- Thumbnails: Standard 4 (1065×600 2pg, stock premium 1pg, storefront carousel premium 2pg, organic 1pg).
- Reassign vendors as Urgent. **Mark Setup QC complete or vendor tasks will NOT be available.**
- Confirm all sessions ran & FSAs generated.
- **Submit 2 Urgent Processing Tickets** (reason: short lead time) — one for Box QC, one for Tag/Tag QC/Spot Check/Image QC.
- Flag any date changes to DOC/Lead, who notifies both GFS Slack channels.

## ⚠️ Common errors / risk items
- **Uppercase vs lowercase folders:** always select the lowercase folder (individual pages); uppercase are full PDFs.
- **Pricing zone names are case-sensitive and space-sensitive** — must match Fadmin exactly or store assignment fails.
- **FSA generation** may take a few minutes; if FSAs don't generate, re-run the "Flyer Creation" task → Mark Complete.
- **URL name mismatch:** product names on the link sheet are not exact matches — **use the closest product name** (e.g. flyer "Liquid Vanilla Bean Paste" → URL "Vanilla Bean").

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot OFF)
- **Include:** special weblinks (links in the spreadsheet, e.g. Shop Online). **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media. Linking doc required.

### Tag / Tag QC (Low complexity — Auto-tag ON)
- **Include all fields:** brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- **Brand:** use the product image to identify if not in the name (e.g. "Oishii"). For multi-item/brand boxes, select "Multi-Item" and separate brands with a `|` (pipe).
- Prefix: watch for multi-buy (e.g. `2/$5`). Postfix examples: LB., EA., BAG. Categories usually Grocery.
- **Every item will have a URL** (link sheet attached to all vendor tasks). Use the closest product name.
- **Images:** always choose the cleanest/most relevant; if two+ items in a box, select one image; if no clean image, select "do not use PDF image."

### Image QC (post-processing)
- Overview → Item Image QC → Generate All (usually <100 items). Always select PDF if available; lifestyle image OK; if multiple images, select 1.

## Post-processing / FQC
- **Link QC:** Overview → Items without URLs → add any missing links. Confirm CTA links (Item Display Type → Link → Add Link; Sessions → Verify URLs; Flyer Preview → confirm functioning).
- FQC: confirm vendor tasks complete; Edit Details (dates, hidden on hosted, internal run name, no external run name, no theme); thumbnails Standard 4; Tag/Tag QC both green; page categories none/only 1 page (clear any entered); sessions run & FSAs generated, re-verify URLs.
- Geography: some week-over-week variation is normal; confirm against the store assignment sheet if big variations. OK to ignore "Other Warnings"/stores not assigned.
- **Flyer Review type: Lite.**

---
*Source: Gordon Food Service OneGuide (Google Doc `1zZZzbkt_Z2Faf2y-xGEfrk2ePYNALUH-IQOaH-huucM`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
