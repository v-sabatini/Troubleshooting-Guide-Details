# Walgreens — Processing Guide

> **Source:** Walgreens OneGuide (Google Doc `1JnxLguiLaOp1C8YFvWUWFpCPRXszRhuO_vdIcnSUmJs`), updated Dec 1, 2025. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 1 Premium |
| Availability | **Flipp only** (hidden in hosted) |
| Slack channels | `#walgreens`, `#flex-walgreens` |
| Flyer types | **Weekly Ad** (2550) · **Monthly Savings Book** (3893) |
| Processing | Auto-stack; Flex (3FL); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Wednesday. **Linking document:** Yes.
- **Cadence (Weekly):** Available From Wednesday · Valid From Sunday · Available To Saturday · Valid To Saturday.
- **Workflow:** Upload & Setup (5 days out, Vendor) → Image QC (2 days out, Flex) → Pre-FQC (FTE) → FQC (1 day out, DOC + FTE).

## Upload & setup

### Weekly Ad (2550) — Vendor
- In FTP: use the version xls (**ignore PURERED_WEEKLY.xls**). Linking doc = `Flipp_URL.xlsx`; codesheet = `schematics/version.xlsx`.
- **Codesheet manipulations:** Column A = pricing zones → highlight → "!" → Convert to Number (removes leading 0s). Column B = stores → sort descending, then Convert to Number on numbers with leading 0s. **Remove rows with stores 21237 and 21275.** Save as .csv.
- **Codesheet upload:** cross-reference the last number in the "Adv Event" column against FTP pages to confirm all pages present. **Config name: `walgreens`**; Base path `/mmddyyyy` (no underscore); **NEW — uncheck Region Assignment and Combine Zones; MUST toggle "Use Page Pool".** Note in comments which zones the 5 main pricing zones are in: Houston, Chicago, Dallas, Phoenix, El Paso.
- **Setup QC:** URL doc + PDF page file sent to Tiderise team for an updated URL doc; attach updated linking doc; complete Setup QC; **hide in hosted.**

### Monthly Savings Book (3893) — Vendor
- Manual upload: Pages → Edit → find that month's savings-book pages (file name has the month + "ivc"). Upload all pages. Create one Base pricing zone; assign all stores, then **remove the PR store set**.
- **Setup QC:** crop blank space from the cover page (download → pdfcandy.com crop → re-upload → replace original cover in PZ tab). Hidden in hosted, available Distribution/Flipp. External Run Name "[Month] Savings Book"; no theme. Complete Setup QC.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF; linking doc required):** Include packaged deals, retailer logo, sign-up page, social media, special weblinks. Exclude coupons. Items are in a grid — **box each item individually**; reference the Flipp URL doc in the vendor task to ensure all banners and callouts are boxed.

**Tag / Tag QC (Low; Auto-tag ON; PDF image auto-select ON; linking doc required):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price, **URLs**. Brand = No; **SKU = N/A**.
- **Gift cards:** e.g. Name "$5 Walgreens Gift Card", Sale Story "$5 Walgreens Gift Card with myWalgreens", Disclaimer "Limit 2. No limits in NM."
- **Store rewards:** Name = "select cosmetics, beauty accessories, skin, sun or hair care"; Description = "Mix & match … thru [date] with myWalgreens"; Sale Story = "Earn $10 In-Store rewards when you spend $25 or more".
- **Walgreens Cash rewards:** Description "Earn $X W Cash rewards on $Y+ … thru [date]"; Sale Story "Spend $50, Get $10 W Cash rewards".

**Image QC:** **Use cutout images.**

## FQC / go-live

### Pre-FQC (FTE)
- **Page Category QC:** all pages get 1–3 categories except **page 1 (0 categories)** — filter grouping = 1, clear categories, "Copy to Same Index". Filter by grouping index for versioned pages; select the categories that appear most on the page.
- **URL/Links QC:** for each URL in the linking doc, Item Search "URL contains [URL]", match banners to the linking-doc image, confirm names/sale stories/categories, multi-edit as needed; banners with no items → Display Type "Link". Direct-Links section of the linking doc → Display Type "Link". **Then add a URL for all items not in the linking doc:** Item Search "URL is blank" per page grouping (usually 25–60), add `https://www.walgreens.com/offers/offers.jsp/weeklyad?enhancedDWA=true`. **No item or link may be left without a URL.**
- Create 4 standard thumbnails.

### Final QC — Weekly (Flex)
- **Geography:** ensure no stores/FSAs added/removed. If stores changed, check with DOC for **store closures**; if confirmed, close the store in FAdmin (Merchant → Stores/Sets → View Stores → set "valid to" = day before the flyer goes live).
- Rerun the **"remove FSAs" custom action** (also on the currently-live flyer). Check "View Item Boxes" for the 5 main PZs — all items boxed/tagged. Add the weekly-ad URL to any items without URLs.
- **Remove FSAs** from the weekly run via the "remove FSAs" custom action — must run in 2 chunks (text exceeds the character limit). Run this on **three flyers**: the one going live, the currently-live one, and the most recent no-longer-live one.
- Edit Details: Available From Wednesday, Available To Saturday, Valid From Sunday, Valid To Saturday; Internal Name = valid dates (e.g. "June 15 - June 21"); available everywhere; no theme.
- Flyer sorting: Weekly Ads, then Monthly Savings Book, then everything else (earliest publication on top).

### Final QC — Monthly Savings Book (Flex)
- All products with a barcode → **Display Type Item** (use item export/import for bulk). All items boxed/tagged; no blank space around the front cover; run dates match front cover. Complete FQC checklist.

- **Ad-hoc QC (DOC):** item correction notices.
- **Flyer Review type: Lite** (Flex-owned).
- **Out-of-processing:** standard baseline page swap.

---
*Source: Walgreens OneGuide (Google Doc `1JnxLguiLaOp1C8YFvWUWFpCPRXszRhuO_vdIcnSUmJs`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
