# The Grocery People — Processing Guide

> **Source:** The Grocery People OneGuide (Google Doc `1aZek4ch2DbXrECkasLSiTpmnjBhIRolxEd8Jmhpm0Fk`), updated Nov 11, 2025. Contacts/credentials omitted.

Two flyers on one flyer type (**3789**): **Weekly** (codesheet upload) and **Wholesale Market** (manual upload).

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | Hosted only |
| Slack channels | `#thegrocerypeople` |
| Hosted URL | (Hosted only) |
| Flyer type(s) & cadence | Weekly (+ occasional ad-hocs) and Wholesale Market; Flyer Type 3789 |
| Processing | Auto-stack |
| Who's involved | DOC upload/setup; Vendor FQC; Flex Flyer Review; no coupons; **yes** Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Monday.
- **Cadence — Weekly & Wholesale:** Available Wednesday → Wednesday; Valid Thursday → Wednesday.
- **Linking document:** Weekly generally gets one; Wholesale Market generally does not (see Setup QC).

## Upload & setup (owned by Vendor/DOC)

### Weekly (codesheet upload)
- Email notification that files dropped in the SFTP ("Flipp On Line MediaRun List Ad[#] [Year].xlsx").
- **Codesheet manipulations** (best learned via the upload video):
  1. Copy from cell E5 (File Name) to Q5 (Store Ad Stop Date), down to the bottom text row.
  2. Paste special (values only) into a new tab; delete the two "If Statement" columns (J and K).
  3. Format Store Ad Start/End Date columns (L, M) as MM/DD/YYYY; format Acct column (B) as Automatic.
  4. In column A, Find & Replace "_#" with "_AD_#" (e.g. "_21" → "_AD_21"); file name becomes `TGP_AD_21_AA`.
  5. Insert a column right of F; in B2 enter `=CONCAT(A2," FLIPP")`; apply to all rows.
  6. Copy the filled cells from B2 down; paste special (values only) into A2.
  7. Save the tab as `.csv` and upload — **Config name: `the_grocery_people`**; PDF base directory; **uncheck region and combine zones**.

### Wholesale Market (manual upload)
- Retailer contact provides a 4-page flyer plus 2 unique versions of page 1. Before a new month, you also get 2 Commercial pages (upload with the others only if this is the first publication of the month; otherwise add them Pre-FQC and copy items from the previous run).
- Upload all lowercase-folder pages plus the two PZ-specific cover pages (Lloyd and HP) from the uppercase folder.
- **Flyer creation — 3 pricing zones:** "Wholesale Market" (all lowercase pages + both Commercial pages if applicable), "Lloyd" (Lloyd cover as page 1, then pages 2–4), "HP" (HP cover as page 1, then pages 2–4).
- **Assign 1 store per PZ** (per the distribution doc): Wholesale Market = code **1984**; Lloyd = code **872** ("Cash and Carry"); HP = code **10453** ("High Prairie Super A Foods").
- Holiday-specific Wholesale content (e.g. Ramadan): one Base PZ with all Wholesale stores (1984, 872, 10453), use PDF dates, no links generally sent.
- **FSA generation error?** Check the Pricing Zone tab — if zones exist but no stores are assigned, add stores (task reruns automatically); if zones weren't created, rerun Flyer Creation and create the 3 zones.

### Setup QC (both flyers)
- Attach the linking document, or comment "no linking doc this week" (OS won't tag otherwise). Wholesale Market generally has no linking doc. Weekly usually gets one — but open it first; if blank, comment that there's no linking doc.
- Geography same WOW (compare to the right flyer type). Edit Details: one-day consumer preview; Available everywhere; Weekly no external run name; Wholesale Market external run name "Wholesale Market". Standard 4 thumbnails; leg heights preset 40/20.
- **IMPORTANT (Weekly):** a staggered-dates warning appears in red under Platform Availability — click it, select all PZs, and set the Available From date to the one-day consumer preview (Wednesday).

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot ON; linking doc Box-specific — sometimes)**
- Include: special weblinks. Exclude: coupons, packaged deals, retailer logo, sign-up page, social media.
- Box all priced items; text boxes only when necessary. Box callout/contest blocks. Box & tag social icons (Facebook `facebook.com/TGPGrocer/`, Instagram `instagram.com/tgpgrocer/`).

**Tag / Tag QC — Tag Lite retailer (Low; Auto-tag OFF; linking doc Tag-specific)**
- **Do NOT tag Name, Brand, Description, SKU, Sale Story.** Include: pre/postfix, valid dates, price, categories, disclaimer, original price, URLs.
- **Meat/Produce price-per-KG:** where a price is preceded by a number + KG, enter `$###KG` into the **SKU and description** fields (only when the number+KG is in the price box, not the description); the per-pound price is the current price.
- **Valid dates:** tag only if item dates differ from the flyer's (e.g. green-bordered "SAVE — Stock up on Savings!" pages at the end have overriding dates).
- Categories are required for all items (see chart: Floral = Flowers; Grocery = everything else; Meat = non-packaged meats; Produce = fresh fruit/veg).

**Image QC:** select an image for ALL items, PDF where possible; if there are black/grainy shadows, default to the **cutout**.

## Final QC / go-live notes

- Mark Autostack Spotcheck complete. Edit Details (per Setup QC dates/preview/external-name rules). Leg heights 40/20; Standard 4 thumbnails; Item Image QC done by OS.
- **Staggered-dates error** under Platform Availability → click the red text → select all zones → set Available From = Wednesday (so the preview applies at the PZ level).
- Pages: all items QC'd; all linking-doc links added. Pricing Zone: horizontal/vertical + item-view check (watch for 3-Day Sale items — update their valid dates). Sessions: verify links. Geography: no stores/FSAs added/removed (compare same run type).
- **Wholesale Market unique step:** first run of a new month has 2 Commercial pages — confirm both are in the "Wholesale Market" PZ only. If not uploaded, download the relevant commercial pages from the SFTP (lowercase, `_p000#.pdf`), upload manually, copy items from the previous Wholesale run, then add them to the end of the Wholesale Market PZ (positions 5 & 6) and Verify URLs.
- Complete FQC checklist (ignore the "not all categories… have thumbnails" warning).
- **Flyer Review type: Lite.**
- **Out-of-processing:** page swaps (Weekly & Wholesale); Triggers & OPTICS ticket creation for monthly Wholesale Commercial pages; updating the external flyer link sheet ("TGP Direct Links") — create new runs, input IDs in Column D, confirm, send the link to the requesting contact.

---
*Source: The Grocery People OneGuide (Google Doc `1aZek4ch2DbXrECkasLSiTpmnjBhIRolxEd8Jmhpm0Fk`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
