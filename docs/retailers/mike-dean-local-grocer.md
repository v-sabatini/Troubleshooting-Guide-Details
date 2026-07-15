# Mike Dean Local Grocer — Processing Guide

> **Source:** Mike Dean Local Grocer OneGuide (Google Doc `1DEVGAjapLodeG9ohzdLgv3JlMGf0mydq8Uh4zZfe5kQ`), last updated Jun 20, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#flex-processingsupport`, `#flexflyerreview` |
| Hosted URL | mikedeans.com/pages/weekly-flyer |
| Flyer types & cadence | Flyer Type 1 — Weekly Ad (11787) |
| Processing | Auto-stack |
| Who's involved | Flex (Processing Support + Flyer Review); OS N/A; no coupons; no Strategic Ops (no Feedel) |

## Files & schedule

- **Files received:** Wednesday.
- **Publication cadence:** Available From Friday; Valid From Thursday; Available To Thursday; Valid To Friday.
- **Short lead time** — Box QC must be done by Flipp immediately after the task activates.

## Upload & setup (owned by Flex)

- Pages may need to be added to the SFTP by the processor if the client sends files by email.
- **Manual upload:** Pages tab → Edit → select all pages from the SFTP menu → Confirm & Upload → Auto-Group → Save → Save & Confirm. **Do NOT Process Internally.**
- **Pricing zone creation:** create EN pricing zone, select all applicable pages, Save & Next; click "Cross language," then FR; Save & Confirm. **Add all stores to both pricing zones.**

**Setup QC:** confirm all pages uploaded (Pricing Zone tab → Items View; if uploading from SFTP, confirm no un-uploaded pages remain); confirm flyer dates (usually last page, bottom); complete 4 Standard thumbnails; complete Setup QC checklist. **Geography will say FSAs are missing — this is expected.**

## ⚠️ Common errors / risk items

- **Short lead time** — Box QC all items immediately after task activation, paying extra attention to items at the **bottom of page 2.**

## QC specifics

### Box Draw / Box QC — Low complexity
- **Auto-Box Draw: ON. Box QC bot: OFF.** No linking document.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, social media, special weblinks. (Also exclude banners.)

### Tag / Tag QC — Low complexity
- **Auto-tag: ON.** No linking document.
- **Include:** name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. **Exclude: SKU and URLs.**

### Image QC
- Standard pricing spotchecks in pipeline.

## Post-processing (owned by Flex)

**⚠️ FSA custom action (Pre-Final QC).** Run the custom action **"Assign FSAs From CSV"**:
- Use the linked "Mike Dean additional FSA's (Sharbot Lake location)" sheet.
- On the flyer run's Pricing Zones page, copy the ID for each Pricing Zone and paste both numbers into the sheet (correct rows).
- Download as CSV, run "Assign FSAs From CSV" with the correct CSV and flyer run ID.
- **Confirm there are 14 FSAs in each pricing zone** once complete.

Then confirm dates (per PDF), availability toggles (all unchecked), thumbnails include the retailer logo, and standard flyer review checks (all items boxed/tagged, spotchecks complete at 20% of PZs, previews published/clickable, sessions accurate, geography correct).

## Flyer review

- **Flyer Review type: Lite** (owned by Flex). Confirm flyer dates, sessions complete, previews correct, items tagged accurately, geography correct, availability toggles unchecked, **and 14 FSAs in each pricing zone.**

---
*Source: Mike Dean Local Grocer OneGuide (Google Doc `1DEVGAjapLodeG9ohzdLgv3JlMGf0mydq8Uh4zZfe5kQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
