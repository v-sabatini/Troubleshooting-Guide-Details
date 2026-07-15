# Vallarta Supermarkets — Processing Guide

> **Source:** Vallarta Supermarkets OneGuide (Google Doc `1caY_nXaCSQhnDrDr53KK_TfjAZrtMyFzWemdp94i-RQ`), updated Apr 16, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard |
| Availability | All platforms |
| Slack channels | `#vallartasupermarkets` |
| Hosted URL | https://vallartasupermarkets.com/en/weekly-specials/ |
| Flyer types | **Weekly Flyer** (pub 7955) |
| Processing | Auto-stack; Flex (Processing Support); no coupons; no Feedel/Strategic Ops |

## Files & schedule

- **Files received:** Tuesday.
- **Cadence:** Available From Wednesday · Valid From Wednesday · Available To Tuesday · Valid To Tuesday.
- **Preview date:** N/A. **Linking document:** N/A.
- **Workflow:** Upload & Setup (5 days out, Flex) → add to VAST for FQC (4 days out, DOC) → FQC (2 days out, Vendor) → Retailer Preview time-permitting (live date, DOC).

## Upload & setup

Two documented paths; the older codesheet-manipulation path is marked **OUTDATED – DO NOT USE**. Current process:

1. Download the codesheet from the FTP.
2. Run it through the account's Gemini gem ("Run Vallarta", select **Pro**) to produce the manipulated CSV.
3. Upload the codesheet to the flyer run:
   - Name: `codesheet`; Upload File: manipulated CSV from Gemini.
   - **Config Name: `generic`**.
   - PDF Base Directory: found in FTP (e.g. `/0422`).
   - **Check:** Store Assignment, Page Upload, Allow Pricing Zone Creation, Use Page Pool, Tile Generate Afterwards.
   - **Uncheck:** Region Assignment, Combine Zones.
   - Save & Process.
4. Confirm codesheet page names match the SFTP; pages tagged "common" are often named differently in the SFTP — flag missing pages proactively.

**Setup details:** Mark Flyer Creation complete. Overview → Edit Details: Available/Valid Wed→Tue, all platforms, **External Run Name = "Grocery Savings"**, No Theme. Thumbnail QC = Standard 4 (1065x600 ×2, Stock premium ×1, Storefront carousel premium ×2, Storefront carousel organic ×1). Confirm all sessions ran, then complete Setup QC.

### ⚠️ Common errors (retailer-specific)

- **Stores upload incorrectly / empty zones:** A PZ may be created with stores but no pages, or vice versa. Manually assign stores by PZ name — e.g. a PZ named `(43)(54)` needs stores V43 and V54 added manually.
- **"Files Match Multiple Files on the FTP" yellow warning:** OK to ignore. Close the warning, click **Force Processing**; sheet stays yellow but pages/PZs still upload. Add comment "Ok to ignore Codesheet warning."
- **"Store does not exist" warning — two causes:**
  - *Formatting:* remove spaces before the first store number and after the last, but keep the space after commas between store numbers.
  - *Grand opening (uncommunicated):* Vallarta usually does not announce new store openings. If a store code doesn't exist, delete that row and upload **without** it, then flag the grand opening. Once store info is confirmed, create the store in FAdmin (Merchant → Stores/Store Sets → Create new store; get lat/long from Google Maps). Create a **separate Grand Opening flyer run** (same dates; internal name "Grand Opening - DATE"; hide in Flipp & Distribution if <6 purchasable items; External Run Name "Grocery Savings"; no theme) and upload the new store only.

## QC specifics

**Box Draw (Low; Auto-Box ON, Box QC bot OFF):** Include coupons, packaged deals, retailer logo, special weblinks. Exclude sign-up page, social media. Box each product with a price.

**Tag / Tag QC (Low; Auto-tag ON):** Include name, pre/postfix, valid dates, description, price, sale story, categories, disclaimer, original price. Brand = Tag/QC-specific. **Exclude SKU and URLs** (URL: always box the retailer logo, Display type Link → vallartasupermarkets.com).
- **Name (bilingual):** Tag the large bold English name first; if small Spanish (red/green) text exists it **must** be included, separated by a forward slash ( / ). Multiple items in a box → tag the first item's name; add the rest to description.
- **Description:** all non-bold words/measurements; tag "Fresh" when shown; "from Mexico" and "Chiquita" when the corresponding badge appears.
- **Multi-buy pre/postfix:** watch for "### FOR $$$" and "### LBS. FOR $$$"; postfixes include LB., +CRV, "+CRV when you buy multiples of ### in a single transaction" (blue banner).
- **Disclaimer:** often in blue/yellow banners, e.g. "SINGLE PURCHASE $X.XX EACH" or "W/O COUPON $X.XX +CRV".
- **Valid dates:** watch for special sale dates in blue banners / "TWO DAY SALE" callouts; all items in the banner must get those valid from/to dates.

**Image QC:** PDFs must be clear with white background; lifestyle images are OK. **If more than one product in a box, select "do not use PDF image" — even if the products are identical.** Watch for cut-off / non-white-background images.

## FQC / go-live

- Mark Auto-Stack complete; Pages tab Tagged & Tag QC all green; first page of every version is always empty (add categories as needed); check PZ dates + vertical scroll; confirm special item dates.
- Edit Details as above (Available=Valid dates, all platforms, External Run Name "Grocery Savings", no theme, no preview date).
- OK to ignore "Show Unassigned Stores" warning; if PZs lack stores/FSAs, compare to this week's codesheet and add missing stores.
- Sessions: "Mark items in store only"; verify URLs. Run FQC checklist (dates, pages, external run name, valid-date items, leg heights, categories). OK to ignore Other Errors/Warnings (e.g. "Store # not assigned", "not all categories have thumbnails").
- **Preview (Flex):** Monday, only if files were received the prior Monday.
- **Flyer Review type: Lite.**
- **Out-of-processing:** standard baseline page swap.

---
*Source: Vallarta Supermarkets OneGuide (Google Doc `1caY_nXaCSQhnDrDr53KK_TfjAZrtMyFzWemdp94i-RQ`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
