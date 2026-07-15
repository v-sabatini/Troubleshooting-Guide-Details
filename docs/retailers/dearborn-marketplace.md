# Dearborn Marketplace — Processing Guide

> **Source:** Dearborn OneGuide (Google Doc `1lMtCtwanMSv5dsoJ-5oKIUjhMDdWjxJu6fkUjQ5GLko`), updated Jul 22, 2024. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#wakefern` |
| Hosted URL | dearbornmarket.com |
| Flyer type(s) | Weekly Ad (ID 9341) |
| Processing | Auto-stack; Flex = 3FL + Flyer Review; no coupons; no Feedel |

## Files & schedule
- **Files received:** Monday.
- **Publication:** Available From Sunday / Valid From Saturday → Available To Sunday / Valid To Saturday.
- **Linking document:** Yes (blowline Excel — see below).

## Upload & setup (owned by Flex)
- **Pages:** Manual Upload → Pages → Edit → select all SFTP pages → Confirm & Upload → Auto-Group (or manual grouping numbers), correct language per page → Save & Confirm. **Do NOT process internally.**
- **Pricing zone:** create Base zone, select all pages → Save & Confirm → add all stores.
- **Blow Line document prep:** download the blowline Excel from the SFTP → delete column `AD_COPY` → create a second tab with the remaining 3 columns.
  - Sheet 1 = **"For OS"**: keep only `PROMO_NUM` + `BLOW_LINE` (delete `UPC_13_NUM`).
  - Sheet 2 = **"mi9"**: keep only `PROMO_NUM` + `UPC_13_NUM` (delete `BLOW_LINE`).
  - Save and **attach to all pipeline tasks.**
- **Setup QC:** confirm all pages uploaded (Pricing Zone → Items View; RISK — no un-uploaded SFTP pages); confirm dates (first/last page); Standard 4 thumbnails.

## Box Draw (Low — Auto-Box ON, Box QC bot OFF; linking-doc required)
- **Include:** coupons. **Exclude:** packaged deals, retailer logo, sign-up page, social media, special weblinks.

## Tag / Tag QC (Low; Auto-tag OFF; linking-doc required)
- **Include:** name, description, SKU, price, sale story, categories, original price. **Exclude:** pre/postfix, valid dates, disclaimer, URLs. Brand used for Box/Tag.
- **Tagging SKUs:** open the attached blowline Excel → search the item name in column B (`BLOW_LINE`) → the SKU is in column A (`PROMO_NUM`) → paste into the SKU field. If not found, leave SKU blank. **Never enter more than one PROMO_NUM in the SKU field.**

## Image QC
- Select clean PDF image whenever possible **except for coupons**; otherwise cutouts. **Coupons: cutout image only (no PDF image).**

## ⚠️ Common errors / risk items (retailer-specific)
- **Coupon check:** coupons (usually page 1) must have **Display Type = Coupon** (not Item) and **"do not select PDF image"** selected.
- **Mi9 custom action (post-processing):**
  - Before running, go to Image QC → **Generate Data Piping Groups** (if you see the generate screen rather than item images).
  - Copy the "mi9" sheet from the blowline file into a new Google Sheet (paste values only). **Ensure every `UPC_13_NUM` is a complete number with no commas, spaces, dashes, or special characters** (use Find & Replace).
  - Download as `.csv` → Flyers → Upload Files in FAdmin → copy the uploaded file ID.
  - System → Custom Actions → **mi9 sub item generator** (RISK: make sure **sub item generator** is selected, *not* sub item report). Paste the flyer run ID (first box) and uploaded file ID (second box) → Run Action.
  - Spot-check a few items to confirm sub items were added.
  - **Error "Flyer run has no sibling groups"** → go to Item Image QC and click **Generate Data Piping Groups**.

## FQC (owned by DOC)
- Standard FQC checklist. **Flyer Review type: Lite.**

---
*Source: Dearborn OneGuide (Google Doc `1lMtCtwanMSv5dsoJ-5oKIUjhMDdWjxJu6fkUjQ5GLko`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
