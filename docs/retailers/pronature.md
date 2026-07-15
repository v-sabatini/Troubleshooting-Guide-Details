# ProNature — Processing Guide

> **Source:** ProNature OneGuide (Google Doc `16LV2O10Ueq3FUL5KqOj4q_7JaSN4H17_7dY-GLY-NzI`), updated Sep 18, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 4 Standard |
| Availability | All platforms |
| Slack channels | `#heinens` |
| Hosted URL | EN: groupepronature.ca/en/flyer · FR: groupepronature.ca/fr/circulaires |
| Flyer types | Weekly (6484) — runs **bi-weekly (2-week run)** |
| Processing | Auto-stack; Vendor + DOC setup, Flex FQC; no coupons, no Feedel |

Bilingual (EN + FR). Files received Monday; preview Thursday; live Monday. Works mostly with a third party (Turbulence). No retailer-specific risk items called out.

## Files & schedule
- **Cadence:** Available Mon 12am → Sun 11:59pm; Valid Mon → Sun; **2-week run.** Preview Thursday before go-live (external preview Friday, so corrections may land on the live Monday).
- **Linking document:** Yes (URL spreadsheet).

## Upload & setup (Vendor / DOC)
- Retailer emails when files are dropped; confirm receipt, update the Vendor Setup Tracker with FlyerID, mark ready. Files on S3 can be hard to open — use coreFTP to download and save locally.
- **Manual upload:** Pages → Edit → select files. Equal numbers of English ("**An**") and French ("**Fr**") pages. **Do not Auto-Group** — manually set page numbers per the file name (two page 1s, two page 2s, etc.). Manually set language for each French page and **Save only**; re-check that French pages didn't revert before **Save & Complete**.
- **Pricing zones:** create **EN** (all "An" pages) and **FR** (all "Fr" pages), correct page order. Add **all stores to both zones.**

### Setup QC
- Dates: Available/Valid Mon 12am → Sun 11:59pm, 2-week run. Available on all platforms. Preview Thursday. Internal run name = **FLYER/THEME IN ALL CAPS - Live Date**; no external run name; no theme. **Leg heights 40/20.** Thumbnails Standard 4 (1065x600 – 2pg, stock premium – 1pg, storefront carousel premium – 2pg, organic – 1pg). Confirm sessions ran and FSAs generated.

## QC specifics
- **Box Draw** (Low; Auto-Box **ON**, Box QC bot **OFF**; linking doc used for both Box/Tag): box the retailer logo; box all items separately, but keep **differently-sized variations of one item in a single box**; items with multiple prices in the description → box as separate items. **Do NOT box QR codes.** Exclude coupons, packaged deals, sign-up page, social media.
- **Tag / Tag QC** (Low; Auto-tag **OFF**; PDF image auto-selection ON): include brand, name, pre/postfix, valid dates, description, SKU, price, sale story, categories, original price, URLs. **Exclude disclaimer** (except: include the disclaimer only when it's inside the box, e.g. "(Accessories sold separately)", "Limit of 4 per client", and all warranty messaging like "1-YEAR IN-STORE WARRANTY").
  - Name exactly as in flyer (bold text); don't include quantities in Name unless multiple items with different quantities. One brand → enter exactly; multiple brands → leave Brand blank. Common prefix "STARTING AT"; if no current price, put the sales-story text in prefix and the amount in Current Price. Common postfixes "EACH", "PER PAIR".
  - **Do NOT tag** suggested retail price as original price (leave original price blank, but fill $/% off if applicable); don't tag words like "UNBEATABLE".
  - **Store locator** on the last page → tag with EN `groupepronature.ca/en/store-locator-hunting-outdoor-fishing/`, FR `groupepronature.ca/magasins-plein-air-chasse-peche/`.
  - **Style guide:** no original pricing is to be displayed.

## FQC / Flyer Review (Flex)
- **Page categories:** per the category chart — choose by the theme of items on each page; front page always titled "Front Page".
- URL/Links QC: no links need inserting for this merchant. Spotchecks; mark Auto-Stack complete; confirm vendor tasks done. Dates/leg heights/thumbnails as above; page categories per chart; vertical preview; sessions run and re-verify URLs; geography doesn't change week to week. Clean images where possible; mark items **In-Store Only**; store finder links out. OK to ignore "Other Warnings"/unassigned stores.
- **Flyer Review type: Lite.**

## Out-of-processing
- Post-live page swaps per the baseline page-swap process.

---
*Source: ProNature OneGuide (Google Doc `16LV2O10Ueq3FUL5KqOj4q_7JaSN4H17_7dY-GLY-NzI`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
