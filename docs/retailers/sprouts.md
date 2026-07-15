# Sprouts — Processing Guide

> **Source:** Sprouts OneGuide (Google Doc `1Vj5THG-kTJpJ-LsTTj5a44oFrKhurtmkSi2ali132k8`), updated Apr 7, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier S2C2 (Standard 2) |
| Availability | All platforms |
| Slack channel(s) | `#sprouts` |
| Hosted URL | sprouts.com/weekly-ad |
| Flyer type(s) & cadence | **Weekly Ad** (files Wed; live Tue) + **Monthly Deals / DOTM** (type 2; files Tue) |
| Processing | Auto-stack; no Flex; no OS-outside-standard; no coupons; no Strategic Ops / Feedel. Owned by DOC |
| Linking document | **Sprouts Linking Document** — OS has direct access to tag links (must use their @flipp email) |

> **Timezone:** Available/Valid From = **3 AM** for both publications.

## Files & schedule

- **Weekly:** PDF files & codesheet sent Tuesday night (all info in the email); upload to FAdmin Friday once the data sheet is received (or upload earlier with a vendor note not to begin tagging until the data sheet is added). If a new store appears, reply to the email for store info and add to FAdmin. If the codesheet has missing pages / incorrect file names, request a revised codesheet from the files contact.
- **Monthly (DOTM):** files arrive Tuesday, ~2 weeks out; preview Monday.

## Upload & setup — Weekly (owned by DOC)

- **⚠️ "Pg00 INSERT ONLY, NO AD" callout:** this pricing zone is a **separate hosted-only ad** (one page, tagged with two links). Delete that PZ from the codesheet and create a new flyer shell named "**Month Date - Store# Hosted Only**"; manual-upload the one page; add the single store to that zone; mark **Available in Hosted Only**. FQC = standard steps + confirm links tagged.
- **Edit Details:** Available & Valid From @ 3 AM; available everywhere; no external run name; no theme.
- **Codesheet manipulation (in Google Sheets):** delete extra rows at the bottom; delete extra columns on the rightmost end (including any unusual characters); save as CSV (no other manipulation unless a hosted-only version is needed).
- **Upload codesheet:** Name = "Codesheet"; Config name **`sprouts`**; **Toggles 1, 3, 4, 5, 6.**
- Check Pricing Zones (# pages matches the email). Ledge Heights 30/20; Standard 4 thumbnails; Setup QC checklist.
- **URL vendor attachments:** URL document is attached to the email. For Vendor Tag & Tag QC, add a comment telling OS to use their Flipp email and scroll to the flyer name in the Sprouts Linking Document — **OS tags links directly from the source; do NOT copy the original sheet.**

## Upload & setup — Monthly / DOTM (owned by DOC)

- Create a flyer shell ("*Month* DOTM"). Edit Details: Avail/Valid @ 3 AM; available everywhere; **Secondary publication = checked; External Run Name = "Deals of the Month".**
- Manually upload pages; create base pricing zone; **add all stores → remove store 0**; Standard 4 thumbnails.
- Vendor comment: use Flipp email, DOTM tab, correct month for links.

## QC specifics

- **Box Draw (Low; Weekly Auto-Box ON / DOTM Auto-Box OFF; Box QC bot OFF; linking doc for Box + Tag):** exclude coupons, packaged deals, retailer logo, sign-up page, social media; **include special weblinks.** All items boxed. For special weblinks, use the Sprouts Linking Document (Weekly tab / DOTM tab), Image column (G), to see what to box.
- **Tag / Tag QC (Low; Auto-tag OFF; linking doc required):** include brand, name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, URLs; **exclude SKU.** DOTM additionally includes a **Page Link** field.
  - Brand/Name/Prefix/Postfix/Price/Sale Story/Description/Disclaimer as on the flyer. Items with only a deal (no price) → leave pricing blank.
  - **URLs:** use the Sprouts Linking Document — **Link Title must be used in the Name field** (risk item). Do NOT check "Link Title Double Checked" (processors do that).
  - Every item needs an Analytics Category **and** a Google Category.
  - **DOTM Page Link:** display type Page Link; Name = Link Title; Page Destination per the linking document.
- **Image QC:** choose a valid PDF image per item (one image for multi-item boxes); clean PDFs only (no weird backgrounds/shadows/cutoff) — cutout when the PDF isn't clean.

## Links QC / Final QC (owned by DOC)

- **⚠️ Links QC is a promise to the retailer:** open the Sprouts Linking Document (Weekly Ad / DOTM tab), go through each item confirming (1) the **Link Title** is in the name field and (2) the URL is applied correctly (OS sometimes doesn't copy the whole link). Then **mark off the "Link Title Double Checked" column** for each QC'd item.
- For URLs on many pages, use Item Search (Item Type = Link, Page Grouping Index) → Multi Edit Items to mass-update Name + URL, then mark off the column.
- Complete the FQC Checklist.

## Out-of-processing — Weekly Live SKU corrections

- Tuesday morning "Weekly Flipp Report" email lists SKU corrections. Download → keep only "Name" and "Problem" columns → Remove Duplicates → sort Problem ascending. Action each issue using the SKU datasheet:
  - **Empty SKU field** → add missing SKU.
  - **Bad SKU value** → fix formatting (usually add/remove a comma).
  - **SKU does not match a product / could not match to collection** → verify against the datasheet.
  - **Ignore** "SKU matches product but not a valid store-product" (Sprouts-owned).

## Flyer review

- **Flyer Review Type: Lite** (owned by DOL).

---
*Source: Sprouts OneGuide (Google Doc `1Vj5THG-kTJpJ-LsTTj5a44oFrKhurtmkSi2ali132k8`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
