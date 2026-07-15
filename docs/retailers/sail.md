# SAIL — Processing Guide

> **Source:** SAIL OneGuide (Google Doc `1R_8uughtXaTKKM9AcGUzIJm2s7wYpvI-g9PPZHJc-rc`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#1plat_sail`, `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | https://www.sail.ca/en/sales/online-flyer |
| Flyer types | Flyer Type 1 — Weekly |
| Processing | Auto-stack; Flex (Processing Support + Flyer Review); **linking document required**; no coupons; no Feedel; OS N/A |

## Files & schedule

- **Files received:** Monday
- **Available From:** Monday · **Valid From:** Tuesday · **Available To:** Monday · **Valid To:** Tuesday
- **Linking document:** YES — REQUIRED (also contains the weekly UTM code).
- **Workflow:** Upload & Setup (Vendor, 5 days out) → Image QC (FLEX, 2 days out) → FQC (DOC, 1 day out).

## Upload & setup (owned by Vendor)

- **⚠️ Pages may need to be added to the SFTP by the processor if the client sends files over email.**

**Ontario flyer run:**
- Manual upload of **English** pages from SFTP; Auto-Group or manually paginate; ensure correct language. Save & Confirm; **do NOT Process Internally.**
- Create Base pricing zone, select all pages, add **all Ontario stores**.
- Linking doc: before uploading, ensure only Ontario-specific URLs are visible.

**Quebec flyer run:**
- Manual upload of **ALL** pages; Auto-Group or paginate; ensure correct language (English vs French). Save & Confirm; do NOT Process Internally.
- Create **English & French** pricing zones, select all pages, add **all Quebec stores to both**.
- Linking doc: before uploading, ensure only Quebec-specific URLs are visible.

### Setup QC
- Confirm all pages uploaded (Items View); **RISK:** confirm no un-uploaded pages remain in SFTP. Confirm dates (first/last page); 4 Standard thumbnails; preview dates set.

## ⚠️ Common errors / risk items (retailer-specific)

- **Cloning + UTM codes:** original flyer runs are for **Flipp & Distribution only**. Flyers must be **cloned** and labelled "- Hosted" in the new name, and **all URLs updated with that week's UTM code** (found in the linking document). **Ontario and Quebec UTMs are different.**

## QC specifics

### Box Draw (Low complexity; Auto-Box OFF, Box QC bot OFF)
- Linking document required (used for both Box and Tag).
- **Include:** coupons, packaged deals, retailer logo, sign-up page, special weblinks. **Exclude** social media.
- Box each item with a price; box the retailer logo; box any sale-story banners.

### Tag / Tag QC (Low complexity; Auto-tag OFF)
- Linking document required (used for both Box and Tag).
- Include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, disclaimer, original price, URLs.
- Tag logo, promotions, category callouts, standard items, callouts, rewards program.

### Image QC
- Standard — PDF preferred if clean; otherwise cutouts accepted.

## Cloning (owned by DOC)

SAIL has platform-specific URLs with UTM codes at the end. Clone the original runs into 2nd versions so there are **FOUR** runs total:
- Ontario – Flipp & Distro (hidden on Hosted) + Ontario – Hosted only
- Quebec – Flipp & Distro (hidden on Hosted) + Quebec – Hosted only

For each clone, retrieve the UTM from the original linking document (Ontario and Quebec UTMs differ) and add it to all URLs:
- Export Items → delete the 2nd/lower section → keep only Item_id, SKU, URL → add the UTM to ALL URLs → save as CSV → import updated URLs. Repeat for the 2nd clone.
- Confirm UTMs added: Overview → Item Search → Apply Filters (all items populate) → Ctrl+F the specific UTM. Then complete the FQC checklist for both clones.

## FQC / Flyer review
- Pre-FQC (FLEX) / FQC (DOC): confirm dates vs PDF, availability toggles, thumbnails incl. logo; all items boxed/tagged; spotchecks complete (20% of pricing zones); previews clickable; sessions completed; geography correct.
- **Flyer Review type: Lite** (owned by FLEX).

---
*Source: SAIL OneGuide (Google Doc `1R_8uughtXaTKKM9AcGUzIJm2s7wYpvI-g9PPZHJc-rc`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
