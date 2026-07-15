# Walmart US — CP Processing SOP

> **What this covers:** Content Production processing steps for Walmart US
> weekly publications — manual/automated curation, banner and product data
> setup, Fadmin processing, tiles, and tracking codes.
> Source Confluence page id: **12102893588** (CP space).
> Credentials, contacts and pod names are intentionally omitted.

## Account at a glance

| | |
|---|---|
| Merchant ID | 2175 |
| Flyer Type ID | 10566 |
| Slack channel | `#walmartus-production` |
| Flyer validity | Wednesday → Tuesday |

Marketing assets (banners) are created weekly by the Walmart team and posted to
the Walmart US SharePoint. Walmart also provides all categories and product URLs
in an Excel sheet on SharePoint each week.

## Data & workflow — what you need

- Manual Collection Sheet
- `[PROD]` Curation Sheet — contains the Story Curation (templates) tab and the Product Data tab
- Marketing Assets (banner images) — sent via SharePoint weekly
- Template Selection (Excel with categories + product URLs, sent weekly)

## Monday processing

1. The Walmart contact sends an email (Monday evening, sometimes Tuesday morning) confirming weekly assets are uploaded to SharePoint. Use the link in that email to download assets.
2. Access the Excel file with product URLs from SharePoint. Download it as an Excel document and drop it in the shared drive under the Go-Live date.
3. Copy the product URLs from the Excel sheet into the **'Walmart USA'** tab of the Manual Collection Sheet. Delete any old info first. DSP collects the info Monday night; it is ready for review Tuesday morning.

## Tuesday processing

- Open the Manual Collection Sheet and review the collected data.
- Scan for products DSP could not collect (item not live at collection time). Open the URL to check availability; if the link is broken or item unavailable, request a replacement.
- Copy the URLs in **Column W** and paste as **values** into **Column K** — this ensures all product URLs have tracking URLs attached.
- Fill the **Lago Custom 21** column: product names collected are SEO-based; convert them into "simpler names" (Gemini prompt instructions are in the referenced Google Doc) so they display properly on the flyer.
- Macros auto-populate the product data sheet. TR takes over processing and tags you for review when done.
- After confirming, send to the PL for review (toolkit or message). Once approved, share the flyer run ID with BD in the Walmart channel.

## Story curation sheet build

Use the `[PROD]` Product Data and Story Curation tabs.

- Locate the WMUS shared-drive folder dated for the upcoming Wednesday. Download the weekly banner zip and convert files to **.png**, then drop into Cyberduck.
- An Excel file contains links for featured pages — use it to build the story curation sheet. Templates are based on the number of items per category (e.g. 8 products = 1 page, 16 products = 2 pages).
- Copy the category-page links from the Excel file into the appropriate position in the SC sheet.
- **Tracking-URL suffix** depending on whether the page URL already contains a `?`:
  - With `?`: `&adid=1500000020090000091548&veh=dsn&wmlspartner=pubw_flp&cn=fy27-pr-pr-rbme-brtr-3p_con_msp_dsn_dis_flp_n_n_n`
  - Without `?`: `?adid=1500000020090000091548&veh=dsn&wmlspartner=pubw_flp&cn=fy27-pr-pr-rbme-brtr-3p_con_msp_dsn_dis_flp_n_n_n`
- Edit the page-level disclaimer dates on Page 1 (flyer is live Wednesday to Tuesday).
- When the Product Data sheet is ready, download as CSV and run **Auto Image Processing** (mark off trim cropping).
- Run **Generate & Process Merged Datasheets**.

## Fadmin processing

- **Add All Stores.**
- **Draw tiles:** `Stock Premium` (2 pages), `Storefront Carousel Premium` (3 pages), `Storefront Carousel Organic` (2 pages), `Thumbnail_1065_x_600` (3 pages).
- Make sure images are **not cut-outs**.
- Flyer valid **Wed → Tues**.
- **Hidden in Hosted.**
- **No theme.**
- Change **Internal run name:** `CP_Walmart US Wk [No.+1] Go-Live`. The week number comes from the Go-Live folder name (e.g. folder "(Mar 11 - Mar 17) Wk 6" → internal run name `CP_Walmart US Wk 7 Go-Live`).
- **Add tracking URLs** (reference an old run): 1 event type = engagement, the other 2 = impressions; channel set to Flipp app:
  - Engagement (Flipp App): `https://ad.doubleclick.net/ddm/trackimp/N300005.2123309FLIPPCOPORATION/B35102418.438418330;dc_trk_aid=632247754;dc_trk_cid=248672531;ord=[[randomn]];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=;gdpr_consent=;ltd=;dc_tdv=1`
  - Impression (Flipp App): `https://d.agkn.com/pixel/10690/?che=[[randomn]]&cmid=35102418&sid=CP3885S__P3CQ972_4494286&pid=438418330&cgid=632247754&cid=248672531&aid=11298113`
  - Impression (Flipp App): `https://imtwjwoasak.com/trk?CNTRY=USA&SID=2500017826&TFID=12021&CMP_ID=179364&PUB_ID=490313&PUB_NM=FlippCorporation&PLC_ID=438418330&CTE=438418330_248672531&RND_NUM=[[randomn]]`
- Send to specialist for review.

---
*Source: Confluence "CP - Walmart US SOP" (CP, 12102893588). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
