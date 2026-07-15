# Guardian & I.D.A. — Processing Guide

> **Source:** Guardian & I.D.A. OneGuide (Google Doc `1mbyu9utChEpXbzbMhRs_FsOY-_elP0sMhLnBngWCJ7Q`), updated Jun 11, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | All platforms |
| Slack channels | `#mckesson` |
| Hosted URL | guardian-ida-remedysrx.ca/en/flyer-search |
| Flyer types | Promotional Flyer 25 km (4978) · Promotional Flyer 5 km (6376, clone of 4978) · Prescription Centre Flyer 25 km (5128) · Prescription Centre Flyer 5 km (6381, clone of 5128) |
| Processing | Auto-stack |
| Who's involved | DOC owns processing; Flex (Flyer Review); no coupons; no Strategic Ops |

## Files & schedule

- **Files:** arrive well ahead of time via FTP (can be uploaded early), but watch for new inserts via email. Store list also arrives early — **always double-check for an updated version on the FTP before go-live.**
- **Cadence:** Available From Wednesday, Valid From Friday; Available To Thursday, Valid To Thursday.
- **Preview date:** set an internal preview date of **Monday** to allow extra FQC time — this retailer's process is finicky and shouldn't be left to the last minute.
- No linking document.

## Overview & cloning (KEY structural rule)

Guardian and I.D.A. get a **Weekly** flyer (with **Plus** and **Pro** versions) plus a **Monthly** flyer (**Prescription Center**). Same processes/codesheets (with manipulations) apply to both. **Every version is uploaded to a 25 km flyer type, then cloned into a 5 km flyer type** so the shorter-range version can be promoted independently.
- Clone all 25 km flyers to 5 km. Weekly only → **4 flyers total**; with the Monthly → **8 total.** Open all 4 (or 8) in separate tabs for FQC and store-adding.

## Upload & setup (owned by DOC)

**Pricing zones & pages (codesheet):**
- Download the **Tracking Sheet** from email/FTP (search "tracking" or the cycle date, e.g. "1018").
- Use the **Guardian & I.D.A. Pages Codesheet Template**; name it by valid date. Paste page names into matching slots; **copy the PLUS page 1s into the PRO zone page-1 cells** (codesheet won't run if blank — extra pages removed later). Paste the "size" column from the Tracking Sheet (every cell needs a number or the codesheet won't run). Add/delete rows for extra/fewer pages. Update cells B4–B6 per the Tracking Sheet. Download as `.csv`.
- **Weekly:** create the shell from the **Plus 25 km** flyer type (6786) — **NOT** the Promotional 25 km type. Use dates from cell B6 (Valid Friday–Thursday; Available From = Wednesday, two-day preview). Upload with config **`guardian_pages`** and the **3rd, 4th, 5th and 6th toggles**. Process and wait for sessions (done when Flyer Creation task becomes available — don't mark complete yet). This creates the 4 Plus pricing zones.
- **Switch flyer type** to the **Promotional 25 km** type (4978): Overview → Edit Details → move flyer run to "Promotional Flyer 25 km" → OK. **Rerun the codesheet** (ignore "pages already uploaded" — hit **Force Processing**). Now 8 pricing zones exist.
- **Delete all PZs with "FR" in the name**, then kick off flyer creation.
- **Delete the first PPLUS page** from each PRO pricing zone (`####_01_PPLUS…`).
- **BIL** zones set to English → cross-language to French during Pre-FQC.
- **Monthly:** upload the codesheet as above but **no need to switch flyer type or rerun** — only 2 PZs (one English, one Bilingual), uploaded once to the **Prescription Center 25 km** type (5128).
- **Option+ pages** (Weekly): if the Tracking Sheet name includes `OPTION+` (and has an OPTION+ WEB tab), manually upload both pages listed (English), mark Flyer Creation complete, and manually add to all pricing zones per the tab instructions.

**Setup QC:** confirm dates on page 1 of a PZ; No Theme applied (unless seasonal); thumbnails Standard 4; legibility heights Scan 35 / Read 25. The orange codesheet warning can be ignored.

## ⚠️ Common errors / risk items
- **Upload to the Plus 25 km flyer type first — NOT the Promotional type** — then switch type and rerun to generate the Pro zones.
- **Codesheet won't run if PRO page-1 cells or any size cell is blank** — fill PRO page 1s with the PLUS page 1s and put a number in every size cell.
- **Delete FR zones and the first PPLUS page from PRO zones**; cross-language BIL zones to French.
- **Store filtering (Pre-FQC):** in the Digital Posting Run List, filter Flipp Km = **25** and Flipp Zone to Guardian zones (start with "G:"). **Do NOT include PCN zones** (e.g. `GPC_OAW`) in Weekly runs — those go to the Monthly (PCN) tabs.
- **Boxing:** Guardian doesn't use data piping; images are mainly cutouts — box **every individual item** with the info on the flyer; **one box per item** even if boxes overlap. Don't merge items into one box.
- Look out for **item- or page-level valid date overrides** — rare and easy to miss.

## QC specifics

### Box Draw (Low complexity — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo, sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals. No linking doc.

### Tag / Tag QC (Low complexity — Auto-tag OFF; PDF Image Auto Selection ON)
- **Include:** brand, name, description, SKU, price, sale story, categories, disclaimer, original price, URLs. **Exclude:** pre/postfix, valid dates.
- **Name/Brand:** tag brand as it appears (multiple brands → both in brand field); Name = BRAND NAME + NAME + ITEM (often bold full caps).
- **Description:** fully bilingual (English + French) as in flyer; include any quantity/number.
- **Pre/Postfix:** most often "CH./EA."
- **SKU:** generally none; if present, enter as shown.
- **Disclaimer:** enter item exclusions into disclaimer.

### Image QC
- Use clean PDFs wherever possible. If a clean PDF is unavailable, select **Do Not Use PDF Images**.

## Post-processing / FQC (owned by DOC)

**Assign stores (Pre-FQC):**
- Download the **Digital Posting Run List** from email/FTP. Duplicate the GuarIDA store codesheets TEMPLATE, name by valid date.
- Filter the Run List (Flipp Km = 25; Flipp Zone = Guardian "G:" zones; isolate PCN "GPC_" for the Monthly tabs). Build generic codesheets in the Guar 25 km tab (SAP codes → stores header; isolated Flipp Zones → pricing zone header). Repeat for 5 km.
- Find & Replace `PPLUS` → `PLUS` so PZ names match Fadmin. Download tabs as `.csv`.
- Upload codesheet — config **`generic_stores`**, **first toggle only**. If a store can't be found, add it at the merchant level with the SAP# as the merchant code, then rerun.
- Delete PZs with no stores (0/0); cross-language remaining BIL zones to French.

**Inserts:** Guardian, I.D.A. and RemedysRx get the same insert style; McKesson emails monthly which 2–3 of 5 to post at the end of each live flyer. Download that month's inserts, upload in English, and add them as the last pages in all PZs in the order listed (Pages → Layout tab).

**FQC:** mark Auto-Stack Spotcheck complete; Edit Details (Weekly: Available From Wed, Valid From Fri, both To next Thursday — check page 1; Monthly: confirm against assets; no theme, available everywhere, no external run name); thumbnails Standard 4; legibility Scan 35 / Read 25; verify PPLUS removed from PRO zones and BIL zones cross-languaged; Geography — stores opt in/out so vary slightly (1–4 store difference OK; investigate larger gaps against the Run List). Ignore categories and unassigned-stores warnings.

**Post-FQC clone:** clone all 25 km flyers into the 5 km types (Weekly → Promotional 5 km; Monthly → Prescription Centre 5 km). On the cloned run remove all stores from all PZs, upload the **Guar 5 km** `.csv` codesheet, confirm stores added, delete 0/0 zones, and re-complete FQC.

- **Flyer Review type: Lite** (owned by Flex).

---
*Source: Guardian & I.D.A. OneGuide (Google Doc `1mbyu9utChEpXbzbMhRs_FsOY-_elP0sMhLnBngWCJ7Q`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
