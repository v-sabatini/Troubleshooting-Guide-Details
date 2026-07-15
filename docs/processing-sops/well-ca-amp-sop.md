# Well.ca — CP Processing SOP : AMP

> **What this covers:** The Content Production processing workflow for Well.ca AMP
> publications on the Agile Storefronts workflow — Cyberduck asset handling, product
> data via custom action, merged datasheet generation, and Fadmin QC/delivery.
> Processed on LAGO 6.
> Source Confluence page id: `13472301057` (CP space; page titled "[AMP] Well.ca
> Processing SOP").
>
> **See also:** no Well.ca OneGuide currently exists in `docs/retailers/`.
>
> **Note:** This SOP is relatively thin/in-progress — several conversion-tool names
> and the Tracking Codes section are left as placeholders on the source page.

## At a glance

| | |
|---|---|
| Merchant ID | 285 |
| Flyer Type ID | 8027 |
| Slack channel | `#wellca-amp-production` |
| Workflow | Agile Storefronts; processed on **LAGO 6** |
| Assets | Retailer-supplied via Cyberduck SFTP |

## Cyberduck
- Protocol SFTP; Server `sftp.flipp.com`; retailer credentials `circulars_wellca` (password not stored here — see the source page / credential store).

## Processing

### Assets (Cyberduck)
- **Banners:** convert to 72dpi PNG; upload to the Cyberduck banners folder.
- **Backgrounds (optional):** convert to 72dpi PNG; upload to the banners folder.
- **Product images:** convert to 72dpi JPG/PNG.

### Custom actions
- Dataformatter: **Create Product Data** / **Upload Data Feed**.
- Image ingestion: **Auto Image Processing**.

### Generate merged datasheet
- After all product images and banners sync in Lago, run **Generate and Process Merged Datasheet**: Merchant ID 285, Flyer Type ID 8027.

## Fadmin
- **Edit Details:** dates, availability.
- Assign stores; add any additional inserts or pricing zones.
- **Images:** uncheck Composites & PDF Images to reveal items without a clean session-extracted image; select PDF images for items with cutouts.
- **Thumbnails (Proofs, Go-Lives, ECR):** `thumbnail_1065_x_600` 3 pages; `stock-premium` 2 pages; `storefront_carousel_premium` 3 pages; `storefront_carousel_organic` 2 pages; `thumbnail` 3 pages.
- **Tracking codes:** (not specified on the source page).

## Delivery
- Download Low-Res PDF (Pricing Zones → more), rename `WKXXX Go-Live/Proof X PDF`. Send the PDF and flyer run link to the specialist and fill in the FQC Checklist.
- QC in the FQC checklist (spot-check items xls vs PDF/flyer run; spot-check banners/product images from the RAW folder; for go-live also thumbnails, PDF images, tracking codes, category page, preview). Request revisions if needed.
- Remove your account from the Direct Processing Schedule; upload the PDF; send the confirmation email.

## Retailer-specific troubleshooting
- None documented.

---
*Source: Confluence "[AMP] Well.ca Processing SOP" (CP, 13472301057). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
