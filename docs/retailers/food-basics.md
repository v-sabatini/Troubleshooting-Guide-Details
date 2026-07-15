# Food Basics — Processing Guide

> **Source:** Food Basics OneGuide (Google Doc `1fqKyEdsqosH06CllQ0v4VCovyCIpD7a2AscF1HsEsXU`), updated May 19, 2026. Contacts/credentials omitted.

## Account at a glance

| | |
|---|---|
| Account tier | Tier 3 Standard (Metro banner) |
| Availability | All platforms |
| Slack channels | `#metro`, `#metro-ops` |
| Flyer types | Weekly |
| Processing | Auto-stack; Flex (Flyer Review); no coupons, no Feedel |

> **Account flags:** Short lead times — files sent 4 days in advance. High organic UEVs due to price matching, so inaccurate tagging/distribution often triggers CX flags. **DO NOT toggle "hide in hosted" — we don't power their hosted but we power their app, and hiding in hosted stops it appearing in-app.**

## Files & schedule
- **When files arrive:** Thursday.
- **Publication cadence:** Available From Wednesday, Valid From Thursday, Available To Wednesday, Valid To Wednesday.
- **Linking document:** No. **Processing type:** Auto-stack.

## Upload & setup (owned by DOC)

### ⚠️ Common errors / risk items (setup)
- **Use the Flipp codesheet if available.** The external contact usually sends two codesheets — one with "Flipp" in the name, one without. **The Flipp codesheet is often in the FTP, not attached to the email** (she says "no Flipp codes" in the email if there isn't one). The Flipp codesheet includes merged-pages files. **Using the wrong codesheet may cause: pricing zones not created, incorrect pages pulled, and/or pages missed during upload.** Two identical file-drop emails are sent — reply to the Flipp one.

### Codesheet steps
- Manipulate the spreadsheet: Page Size row has numbers; Version row has the page name (**always delete the first name**); the empty row before the store list has the file names; **if merged pages cover 2 rows, delete 1 row so it's a single page.** Copy from the edited doc and paste "values only" into a Google Sheet. Save as **xls**.
- **Upload codesheet:** Name: codesheet; upload xlsx; **Config name: `food_basics`**; PDF Base Directory = copy the file name up to the end of the date, e.g. `/73486_FB_12052022` (not the full `_DIGITAL/...` path). If that errors, try just `/73486_FB`.
- **Toggles: 1, 3, 4, 5, 6.** Save + Process. (If it errors, see Troubleshooting below.)
- Let sessions run; check pricing zones look correct; mark off unused files in the FTP (there will be a lot); file part-time ticket for Img QC & Category QC.
- **Complete Setup QC — if files aren't marked off in the FTP you'll get an error that pages are still un-uploaded.**

### Setup QC checklist (owned by DOC)
- **There WILL be extra pages in the SFTP:** when merged pages are used (e.g. `FB1_FB2_V1.pdf`), Food Basics also uploads the non-merged pages (`FB1.pdf`, `FB2.pdf`). Confirm these extras are unused and mark them off as uploaded.

## QC specifics

### Box Draw (Medium complexity — Auto-Box OFF, Box QC bot OFF)
- **Include:** social media.
- **Exclude:** coupons, packaged deals, retailer logo, sign-up page, special weblinks.
- Box each item separately, including multi-item boxes, using **text boxes**. **Box ALL text together** (regardless of language, even if it contains another item name) and include the price in that box. **Capture the whole product image in the box so text extraction works.**
- If an item is alone in a box, box as normal (no text boxes).
- **If text is in multiple languages, box all text together (EN & FR).** If they can't be boxed together, place the text box around the text matching the flyer language (FR text at the bottom for FR flyers).
- Box and tag the two **App Store links** on DOTT13/D13 (Google Play + Apple App Store).

### Tag / Tag QC (Low complexity — Auto-tag OFF)
- **Include:** brand, name, valid dates, description, SKU (**BLOCK ID**), price, sale story, categories, disclaimer.
- **Exclude:** pre/postfix (enter from drop-down only), original price (**not used in this flyer**), URLs.
- **French tagging:** prioritize French titles/descriptions; if no French title, use English.
- **Brand:** enter in Brand & Name when in copy — **do NOT take brand from product packaging.**
- **Multiple items:** tag using ALL text in the same box. Both items get the same tagging (price, name, description, SKU). **Do NOT tag each item individually — tag each with both item names.**
- **SKU = Block ID** (from text extraction field, upper case). Multi Block IDs separated by comma. **Retailer updated SKU formatting — SKUs often contain spaces now; INCLUDE the space** (e.g. "122z FL16"). If Block ID is cut off or says NOBLOCKID, leave SKU blank. **If no Block IDs appear in text extraction, notify the Flipp team immediately.**
- **Prefix (drop-down only). Do NOT tag as prefix:** "8 CRAZY", "THIS WEEK ONLY", "LOCKED DOWN", "EVERYDAY LOW PRICE", "INCREDIBLE", "ALWAYS GREAT PRICE".
- **Sale story:** enter as shown (including capitalization); include any points callouts (e.g. "50 points").
- **Disclaimer:** enter disclaimers inside the item box. **"Selected Varieties" is NOT a disclaimer** (it's a description).
- **Categories:** every item needs an Analytics AND a Google category. For multiple items, use categories for the first item named. Coupons → "coupons". **Peanut Butter → Grocery.**

### Image QC
- **DO NOT select images with a grey/black background — use cutout instead.**
- Always choose the image of the **item listed first**; if it doesn't meet criteria or isn't available, use the cutout.

## Post-processing / Final QC (owned by DOC unless noted)
- **Item Category QC** (owned by Flex): review Fish/Seafood, Meat/Deli, Dairy/Cheese, Snacks, Household, Fruit/Veg, Bread/Bakery, Frozen, Beverages, Grocery.
- **Item Image QC** (owned by Flex): same rules as above.
- **SKU QC** (owned by DOC): Overview → Item search SKU IS blank; open items with no SKU, add Block ID from text extraction if missed.
- **Links QC** (owned by DOC).
- Final QC: action spotchecks; **reference the external email for special per-page tagging instructions**; add any extra links; complete Category QC (check Grocery + Frozen); complete SKU QC.
- **Complete Custom Action "Set Metro Banners Items URLs"** (file under `/ZPO400 + Google Feeds` in the FTP).
- **Only add tracking codes after SKU QC and custom actions are complete.** Add Metro Banners tracking codes for Food Basics (Code Type: Affiliate URL Substitution; Source: Distribution; Variable: blank; Value: the DoubleClick trackclk URL). Note: a second tracking URL exists for "Wowza" events — add it to Wowza flyers.
- No theme; **External Run Name = Weekly Ad**; available everywhere; standard 4 thumbnails; click auto-stack complete; wait for publishing, check vertical preview; check geography; complete FQC checklist.

## ⚠️ Troubleshooting — codesheet reused/duplicate page error
- Different REVISION folders can cause a codesheet error where multiple pages share the same name. Fix:
  1. Open the FTP; create a folder on your computer; download all PDFs for the week (original folder + all REV folders).
  2. Find overlapping pages, delete the oldest and keep the newest.
  3. Create a new folder in the sFTP, add all the most-up-to-date pages.
  4. Retry the codesheet with the new path.

## Flyer Review (owned by Flex)
- **Flyer Review type: Lite.**

---
*Source: Food Basics OneGuide (Google Doc `1fqKyEdsqosH06CllQ0v4VCovyCIpD7a2AscF1HsEsXU`). Contacts/credentials omitted. Last reviewed: 2026-07-15.*
