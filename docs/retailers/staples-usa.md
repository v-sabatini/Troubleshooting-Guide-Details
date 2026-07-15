# Staples USA (Manual Indexed) — Processing Guide

> **Source:** Staples USA OneGuide (Indexed) (Google Doc `11FB5Jqu8c_YYwnfGY-QKMZkG37Rdv5TwkzAwqnF8npE`), updated May 6, 2024. Contacts/credentials omitted.

> **Flipp has NO external relationship with Staples USA — the flyer is Indexed.** Flyer type: Flyer (10472). Owned by FLEX.

## Account at a glance

| | |
|---|---|
| Account tier | Indexed |
| Availability | Flipp only |
| Slack channels | `#flex-processingsupport` |
| Hosted URL (for Flex to retrieve flyer) | staples.com/stores/weeklyad (also staplesconnect.com/weeklyad) |
| Processing | Auto-stack; FLEX owns processing; no coupons; no Feedel/Strategic Ops |
| Cadence | Available/Valid **Saturday → Friday** |

## Files & schedule

- **When files arrive:** the next week's ad is retrieved from the website (available Thu/Fri/Sat). They should have it up Fridays but it sometimes slips to Saturday — retrieve and upload when available.
- SOP: Confluence "Staples USA Indexing Processes / Manual Indexed Content."

## Upload & setup (indexing workflow — owned by FLEX)

**Collect the flyer:**
- Open the weekly-ad link (shows current ad). Scroll to "Browse Other Ads" and click the ad with the red **"Upcoming Ad"** badge.
- Click **"Print ad"** → set destination to **Save as PDF** → save.
- **Check ad pages:** scroll all pages to confirm product images loaded correctly. If pages have large blank space or text/prices with no product, wait 5 minutes and re-download; if it persists, contact the Skeleton Team.

**Crop + separate pages (uses [GIMP](https://www.gimp.org/downloads/)):** the flyer has white-space edges and is a single PDF; Fadmin needs one PDF per page.
- Enable the setting **"delete cropped pixels."**
- Open each page individually at **resolution 300** (default is 100; it resets to 100 when GIMP closes).
- Crop slightly inside the grey page square so the grey line isn't on the page; press Enter. Undo with CTRL+Z if needed.
- **Export each page individually** as PDF, adding the page number to the filename to preserve order.

**Upload & setup in Fadmin:**
- Open the pre-made flyer run for the correct valid dates (Staples USA merchant → Weekly Flyer type 10472).
- **Edit details → show/hide rarely-used fields → enable "Automation enabled?"** Confirm valid/available dates match the downloaded ad.
- Upload cropped pages, number them under "grouping" 1..N, Save and complete → submit. **Do not** check "process internally" or change the conversion library.
- **Flyer creation:** create a single pricing zone (description e.g. "weekly"); confirm all pages are listed.
- **Add FSAs:** on the pricing-zone tab, click the FSA count → select **"weekly indexed ad"** (pre-built list; adds ~17,721 FSAs). Reload to confirm.
- Draw thumbnail; set legibility heights (first number smaller than second).
- Setup QC checklist owned by FLEX.

## ⚠️ Common errors / risk items (retailer-specific)

- **Upload timing:** the flyer is often published Friday but can slip to Saturday — retrieve and upload as soon as it's available.
- Saved-PDF pages sometimes drop product images — always scroll all pages before uploading (re-download if a page looks blank/misaligned).

## QC specifics

- **Pipeline tasks (Box Draw, Box QC, Tag, Tag QC)** run automatically after Setup QC.
- **Auto Spot Check:** if it appears as "available," run it to let tasks finish and make FQC available.

## Final QC (owned by FLEX)

- Fill the top dates with the flyer's live/valid start & end dates.
- Add "n/a" to the flag "not all tagged items have been QC'd" (not needed for this content). Save and complete; the "errors of missing fields" warning is expected due to the n/a — click OK.

## Flyer review

- **Flyer Review type: Lite** (owned by DOL).

---
*Source: Staples USA (Manual Indexed) OneGuide (Google Doc `11FB5Jqu8c_YYwnfGY-QKMZkG37Rdv5TwkzAwqnF8npE`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
