# Woodmans Food Market — Processing Guide

> **Source:** Woodmans Food Market OneGuide (Google Doc `1-h50Q0j7laZa4OPEDzHaEpAEKZQBRbLadoHHvqeKf-4`). Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 5 Standard |
| Availability | **Flipp only** |
| Merchant ID | 2893 (config `m1000`) |
| Flyer type / cadence | Weekly |
| Processing | Auto-stack; **M1000** (auto-processed); DOC upload/FQC; no coupons; no Strategic Ops / Feedel |

## Files & schedule

- **Files received:** Thursday.
- **Cadence:** Available From Thursday, Valid From Thursday; Available To Wednesday, Valid To Wednesday (Thu–Wed).
- Upload and FQC happen on the **live date** (M1000 retailer, processed post-live-dates).

## Upload & setup

> **Only upload the codesheet if the codesheet processed with errors / did not process.** As an M1000 account it normally auto-processes.

- Create the flyer shell for Thu–Wed, available everywhere.
- Check the codesheet for errors and troubleshoot **before** uploading.
- **Codesheet upload:** Name = `Codesheet`; **Config `m1000`**; PDF Base Directory = `/` (FTP folder where the codesheet was located); **check boxes 1, 3, 4, 5, 6**; Save Code Sheet → Process Code Sheet.
- Mark Flyer Creation and Setup QC as complete.
- Sessions should all run completely; once Setup, Autobox, Autotag and Autopublish are done, FQC can begin.

### ⚠️ Common errors (retailer-specific)
- Because it auto-processes, only touch the codesheet if it errored or didn't process.
- In FQC, mark the **error as `m1000`**.

## QC specifics

- **Box Draw:** box each item. (Auto-box handles this as an M1000 account.)
- Tag / Image QC: not detailed in the OneGuide (auto-processed).

## Final QC / go-live notes (owned by Flex)
- Mark thumbnails complete (nothing to change).
- **Republish the flyer** on the overview page.
- Confirm the flyer published on the Pricing Zones tab.
- Go to FQC checklist and mark **error as `m1000`**.
- **Flyer Review:** Woodmans is an M1000 retailer processed post-live — it rarely (if ever) shows on the Flyer Review panel and goes live without review.

---
*Source: Woodmans Food Market OneGuide (Google Doc `1-h50Q0j7laZa4OPEDzHaEpAEKZQBRbLadoHHvqeKf-4`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
