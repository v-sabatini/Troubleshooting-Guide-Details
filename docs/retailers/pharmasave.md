# Pharmasave — Processing Guide

> **Source:** Pharmasave OneGuide (Google Doc `1UsAEhoYT8Jx98NuNKrc50EdQKlgNunfJVmn2fwjSBBo`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channel(s) | `#pharmasave`, `#pharmasave-scp` |
| Hosted URL | pharmasave.com/flyer/ |
| Flyer types | **Weekly Flyer** (3547 — zones F0, CM, GG, SS, CI) · **Bi-Weekly Medium/Dispensary** (FM, FD) · **West Weekly Flyer** clone (7633) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; Strategic Ops = No (Weekly) / Yes-Feedel (FM/FD) |

Two processing tracks: the **Weekly** flyer (cloned to West after FQC) and the **Bi-Weekly** FM/FD flyers (never cloned).

## Files & schedule

- **Weekly:** files received Thursday. Available From Thu, Valid From Fri; Available/Valid To following Thu (1-week run).
- **Bi-Weekly (FM/FD):** files received Friday. Available From Thu, Valid From Fri; Available/Valid To 2-weeks-Thursday (2-week run) — but only shows **1 week on Flipp**, full 2 weeks on Hosted (trigger required, see below).
- **Linking document:** none — but a **Schematic** (from FTP) carries insert links and must be attached to vendor tasks (new Jan 2025).
- **Workflow owners:** Weekly Upload/Setup = Vendor; Bi-Weekly Upload = Flex; Image QC = Flex; FQC = DOC.

## Upload & setup

### Weekly (config `generic`)
- Only upload under **Flyer Type 3547 - Weekly Flyer** — **do NOT** upload under the WEST run 7633. West is **cloned** from 3547 after all FQC steps (avoids double processing).
- FTP → search "Schematic" → download the Weekly codesheet (e.g. `Digital Schematic 24F006.xlsx`). Confirm run dates match the schematic.
- **Find & Replace:** `Regional_eFlyerSignupCreative_V3.pdf` → `Regional_eFlyerSignupCreative_V3.pdf.pdf`.
- Delete the extra info (links & dates) at the bottom of the codesheet. Save as CSV.
- Upload: Config **`generic`**, PDF Base Directory from FTP, **toggles checked: Store Assignment, Page Upload, PZ Creation, Page Pool, Combine Zones.** Save & Process. Mark Schematic uploaded in FTP.
- Confirm PZ count matches codesheet; mark "Flyer Creation" complete.
- **Setup QC:** Internal Run Name `YEARF0WEEK#` (e.g. 23F028); External Run Name "Weekly Flyer"; no theme, no preview date; all platforms; Standard 4 thumbnails. Attach Schematic sheet to vendor tasks. Geography tab shows added stores — OK to ignore.

### Bi-Weekly FM/FD (config `Generic`)
- FTP → search "Schematic" → download FM/FD codesheet (e.g. `Digital Schematic 24FM07.xlsx`). Same Find & Replace and bottom-info deletion; save CSV.
- Upload: Config **`Generic`**, base directory from FTP, **same 5 toggles** (Store Assignment, Page Upload, PZ Creation, Page Pool, Combine Zones). Save & Process.
- Common warning "Pages already uploaded" — **OK to ignore** (inserts are shared across Weekly/FM/FD).
- **Setup QC:** Internal Run Name `YEARFM/FDWEEK#`; no external run name; 2-week dates; Standard 4 thumbnails.

### ⚠️ Common errors / risk items (retailer-specific)
- **Store Selector / Store Closures:** Pharmasave store updates run only **once a day at 3am.** For a closure you **must backdate the Valid To date in Fadmin**, or the store selector delays the closure and **the retailer will always flag it** (e.g. request received Aug 29 → Fadmin date Aug 28).
- **Merged Pages:** insert pages are often larger than regular pages, so Fadmin **merges pages together.** At FQC / Storefront Spotcheck you must **unmerge** (select "Don't Merge" on every merged page). Do this per pricing zone.
- **Sign Up / "Sign Up & Save" insert:** tag as **"Show URL in iFrame"** (NOT Link) — Name "Sign Up", iFrame width 360, height 568.
- **Coupons:** must be tagged with item type **Coupon**, not as items; do not use PDF image; confirm valid dates.
- **Bi-Weekly hide-on-Flipp trigger:** FM/FD must be hidden on Flipp after week 1. Set trigger(s) — Trigger On: Flyer Run, Action: Update Attribute, Attribute: **Hide on Flipp** (and Hide in Distribution at setup), runs Thursday 12:00 AM. Create an OPTICS ticket to confirm the trigger ran; after it runs, confirm on Flipp via a Geography postal code that the flyer is hidden.

## QC specifics

### Box Draw (Weekly = Medium, FM/FD = Low — Auto-Box ON, Box QC bot ON)
- **Include:** retailer logo (Box QC-specific), sign-up page, social media, special weblinks. **Exclude:** coupons, packaged deals.
- Box all items separately; each item with a price boxed on its own; text boxes only if necessary.
- Special weblinks per the attachment (PDF names are far right in the schematic sheet).

### Tag / Tag QC (Low — Auto-tag OFF, PDF Image Auto-Select ON)
- **Include:** name (include brand in name), brand, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, URLs. **Exclude:** SKU, original price.
- Tag everything as seen on the PDF. Sale story as-is (e.g. "20% off").
- **URLs:** use the attachment — match the PDF name to its URL. AirMiles offers link to the AirMiles Pharmasave partner page; Sign Up page uses "Show URL in Frame" (see risk items).

### Image QC (owned by Flex/DOC)
- Prefer a PDF-extracted or composite image. **Unselect** Composites, PDFs, and Data Piped in the QC filter; grouping of items → leave as cutout; single item + clean PDF → use PDF image. (FM/FD leg heights 40/30.)

## Final QC & cloning
- Confirm dates & external run name; mark Auto-Stack Spotcheck complete.
- **Unmerge merged pages** (Storefront Spotcheck); verify coupons; verify URLs.
- **Weekly cloning to West** (also applies to Holiday Gift Guides, Super Savings Events, Cosmetics — NOT FM/FD):
  1. Complete Weekly FQC and mark **Auto Judge Go Live** complete **before** cloning.
  2. Overview → Clone → to "PharmaSave - West Weekly Flyer & Coupons" → select run (week code + WEST).
  3. On the clone (7633): set dates, Internal Run Name `YEARF0WEEK# WEST`, unmerge pages, verify URLs, **delete EAST pricing zones**, check Geo, complete FQC.
  4. Back on the Weekly run: remove stores from WEST pricing zones (Pricing Zones → West → Stores → Remove All). If a West PZ was deleted in the clone, re-run the codesheet to fix.
- **FM/FD:** do NOT clone. Set the hide-on-Flipp trigger + OPTICS ticket, then do the post-live trigger check.
- Flyer Review type: **Lite.**

---
*Source: Pharmasave OneGuide (Google Doc `1UsAEhoYT8Jx98NuNKrc50EdQKlgNunfJVmn2fwjSBBo`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
