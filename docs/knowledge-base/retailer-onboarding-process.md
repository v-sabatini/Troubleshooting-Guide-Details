# Retailer Onboarding & Offboarding — Process Guide

> **What this covers:** How the Ops Onboarding (OBQB) team takes a retailer from
> assignment to go-live — direct (full-processing) onboarding, indexed
> onboarding, rebranding, and offboarding — including the exact FAdmin/MAdmin
> merchant-setup steps and workflow toggles processors must set. Source
> Confluence page id: 3129144452 (space XPTCXE).
>
> **Audience:** Onboarding quarterbacks (OBQBs) and flyer processors setting up
> new or returning merchants.

---

## Who owns onboarding

The **Onboarding Quarterbacks (OBQBs)** are an Operations team that makes retailer
onboarding fast and seamless for Ops, BD, and retail partners. **Hosted owner:**
Technical Enablement Team.

**Loop in an OBQB when:**
- The retailer is a **net-new onboarding**.
- A retailer is returning to Flipp after an extended absence.
- A retailer is **adding a banner** to an existing merchant group.
- There is a one-off, pre-approved campaign for a net-new retailer.
- A CPG/Brand requires new merchant setup.

**The OBQB team is NOT responsible for:** setting up Hosted 2.0, Hosted
troubleshooting, budget/revenue, Salesforce, reporting, or NativeX (outside
campaign setup).

**How to include an OBQB:**
1. File an **Onboarding Ticket** in Jira on the **Operations Onboarding Board
   (project `MM`, board 274)**.
2. Post in the **#onboardings** Slack channel and tag **@qbs**.
3. Include: retailer name, ideal launch date, and the ticket link.
4. An OBQB picks up the ticket within **24–48 hours** and follows up for details.

---

## Direct (full-processing) onboarding — end-to-end

### 1. Assignment & Jira ticket
New onboardings are posted in **#onboardings** by BD with an accompanying ticket
on the Operations Onboarding Board (MM). Tickets are picked up within 24–48 hours.

### 2. Intro to retailer
Once assigned, the QB is introduced to the retailer by email and establishes
timelines, expectations, and relationship details. This can be informal (Slack /
email) — it does not need to be a formal meeting. Use the Internal Kickoff
Discussion Checklist (link in source doc).

### 3. SFTP creation
1. Create SFTP credentials using the **SFTP Automation** (via AWS Chatbot — see the
   EF1 SOP "How to Create or Retrieve SFTP Credentials via AWS Chatbot").
   *(credentials in the source doc — not stored here)*
2. After the merchant is created in FAdmin, add SFTP credentials:
   **Merchant Page > Details > Edit Merchant > FTP Username, Base Path, toggle ON
   FTP Sync Enabled > Save Changes.**
3. After the external intro: send the retailer a **one-time URL** with their SFTP
   credentials, ask them to drop assets to the SFTP, and confirm receipt.

### 4. Create the merchant in FAdmin (new client)
**Salesforce is the single source of truth** for newly created retailers. Country
information is entered via Salesforce; flag discrepancies to BD (they update or
create a net-new merchant).

1. Open the **Merchant Admin (MAdmin)** interface.
2. Search the incoming retailer name; it appears under **Account Name** with
   **(To Be Filled)** in the Name column. *(Sync can take ~1 hour; if not visible
   after 1–2 hours, flag to BD.)*
3. Click the **To Be Filled** hyperlink to open the Merchant page.
4. Fill in:
   - **Internal Name** — pre-filled from Salesforce; editable if needed.
   - **Relationship?** → **Direct**
   - **Distribution Channels?** / Only Show In → **All Channels**
   - **Supported Language?** → English (add French only if there is French content).
   - **Display Name** — input language, Name, and Display Name for all languages.
   - **Name Identifier** — all lowercase, no spaces (e.g. `IGA Southwest` → `igasouthwest`).
5. **Upload logos:** main logo (any shape, rectangular recommended; Vector or
   transparent PNG, HD) and **Storefront Logo** (square `.jpg`, min 60×60,
   max 120×120 px). Input SFTP details and toggle ON Sync Enabled if not done.
6. **Details > Processing Settings:** URL = merchant website; enter Salesforce ID
   (from BD); enter the store locator URL in **Default Store Locator URL**.
7. **Custom tab:** disable **Show Simplified Pop** (if enabled); set default
   **chrome setting to "flatsheet."**
8. **Details tab > Edit Store Settings:** Harmonize stores with Foursquare → Yes;
   select a Foursquare Venue Category; Update.
   *(Note: Harmonize/Venue Category no longer function in this UI — see the "Add
   Stores to Merchant" flow / stores-and-harmonization.md.)*
9. Add categories from the retailer's website.
10. Assign yourself as **DOC and DOL** on the merchant.
11. Post in **#osteam** to determine vendors to auto-assign, providing: Content
    Type (Grocery/Electronics), Language, Processing Type (Simp Pop or Full),
    Budget (Y/N), flyer cadence (weekly/monthly), approx. items per publication,
    and lead time.

### 5. Workflow settings (all retailers)
Set every retailer up with these Merchant Workflow toggles:
- Use PDF image extraction
- Use PDF Image Auto Selection
- Uses auto box draw **(do NOT skip Box QC)**
- Vendor Tag
- Tag QC
- Vendor Spot Check
- Auto Tag Enhanced
- **Auto Tag Fields → All**

> **Always ensure Flyer Type settings match Merchant Workflow settings** — Flyer
> Type overrides the merchant level.

### 6. Build the Flyer Type
1. Create Flyer Type name.
2. Create SEO Name (Flyer Type name, no spaces).
3. Enable store selection.
4. Enable **Geo-Awareness (GA)** if confirmed in IKO (**US retailers only**).
5. Enable **max store distance** (Canadian retailers, or US retailers not using GA).
6. Add Hosted URL.
7. Submit a ticket to add any Flyer Type to stacks.
8. Move the Jira ticket to **Content Processing** when files are received.

### 7. Process & prep assets
- Upload received files and begin processing.
- Create a **OneGuide 2.0** from the template.
- If proceeding with an OKO, prep the OKO deck (separate CA / USA templates).
- Tier 1/2 retailers may get an end-to-end analysis from the Content Strategy
  team — confirm with them before offering externally.

### 8. Codesheet creation (if a codesheet is provided)
- First understand the codesheet and build 1–2 versions of the ad yourself.
- File a **TOSS** ticket to automate the codesheet process, including: how to read
  and version the pages, how to determine stores per version, and any info needed
  to paginate correctly.
- Create a Merchant Code Sheet page (Confluence OP space).
- See `codesheet-errors.md` for troubleshooting once it's live.

### 9. Links check (tracking codes)
- Check received links for tracking codes (**quick check: look for `utm` in the
  URL**). If present, inform the account team — BD communicates that only promoted
  retailers receive tracking codes.
- Tracking codes on **product URLs** are removed automatically when the "Buy Now"
  button turns off.
- **Direct links** keep tracking codes even when budget runs out — but if the
  retailer is launching **organic**, remove direct-link tracking codes before go-live.

### 10. Vendor assignment & store upload
- Confirm vendors via **#osteam** and auto-assign on the merchant page.
- Upload the most recent store list. As long as the **merchant store code matches**,
  data updates in place; if the code does not match, upload then delete duplicates.
- **Systematically build all lat/longs using the Geocode Google Sheets add-on**
  (see the Lat/Long SOP and `stores-and-harmonization.md`). For many mall stores,
  an OS ticket can be filed to audit Geocode lat/longs (front-entrance inaccuracy);
  use internal resources to audit when possible.

### 11. Dry run (optional — account team's discretion)
Process the publication in full and set up a walkthrough with retailer + BD.
Consider a dry run when: the retailer is integrating Hosted, is very unfamiliar
with Flipp, has confusing/specific tagging needs, or is an enterprise retailer.

### 12. Go-live walkthrough
- Present OKO deck and risk items (e.g. clean images cannot be extracted from the
  files provided).
- Update Vendor Guide and merchant-specific FQC per feedback.
- Follow up with preview link and OKO deck, then next steps.
- Get sign-off on the preview and confirm go-live.
- Update the Audit Cycle Spreadsheet.

### 13. Go-live checklist
- [ ] Stacks assigned
- [ ] Stores have lat/longs and **≥90% harmonized**
- [ ] Turn off Indexer (if required)
- [ ] **Always un-check "Indexed?" when transitioning a retailer from Indexed to Direct**
- [ ] Upload Merchant Schedule to FAdmin
- [ ] Links set up correctly
- [ ] Confirm distribution with retailer + BD
- [ ] Add retailer to Capacity Allocation
- [ ] Close Jira ticket

---

## Onboarding a client that already exists in FAdmin

Open **Merchant Page > Details > Edit Merchant Information** and update as needed:
- Name — ensure Name Identifier has **no spaces**.
- Upload Logo and Storefront Logo (square `.jpg`, 60×60 to 120×120 px).
- Merchant website URL; Salesforce ID (from BD); SFTP credentials; store locator URL.
- If currently indexed, disable **"Flipp-Only?"**
- **Whitelist** the retailer so it appears in Flipp web search.
- **Mobile tab:** ensure "Use new mobile experience" is enabled.
- **Custom tab:** disable Show Simplified Pop (if enabled); set default chrome to
  **"flatsheet."**
- Add categories from the retailer's website.
- Assign yourself as **Lead**; confirm vendors via #osteam.

> **DO NOT un-check "Indexed?" at this stage of the process.**

Then apply the same **Workflow Settings** and **Flyer Type** steps as a new client.

---

## Indexed content — onboarding & disabling

Before indexing, confirm content is scrapable and does **not** fall into the
do-not-index categories:
- Content is from a competitor's hosted iframe.
- Content is not on the retailer's own domain but on a third party (Facebook,
  Adobe, blog domain).
- Content fails content policy: no shoppable items, advertises a service only,
  consistently too few items, or contains prohibited content.

If you doubt scrapability, file an **"Ops Request" FD ticket** (OS Eng confirms).
Otherwise proceed and get final confirmation after filing a **"New Indexer" FD
ticket**.

**Indexed merchant setup mirrors the direct flow, with one key difference:**
- **Relationship? → Indirect.** *(If this is not "Indirect," the retailer will
  not appear in Tesseract.)*
- Complete the remaining steps: determine task workflow, build Flyer Type, assign
  stacks, add stores, **file New Indexer ticket**, and **confirm the indexer is up
  and running**.

**What makes content ideal to index:** downloadable PDF/JPEG pages; valid dates on
the same page the flyer lives; same URL week over week; consistently meets content
policy. **Less ideal:** dates only on the flyer page(s) (needs extra QA — indexers
can't pull dates from pages); URL changes week to week; interactive/link-out pages
(case-by-case, e.g. Costco, Whole Foods).

**Requests to index new content come from** (most→least common) Business
Development (Flipp Lite / Tier 5), Customer Experience (user CX tickets), and
internal requests. Explore any option unless previously asked to stop indexing
that retailer.

**Flipp Lite (Tier 5):** low-cost indexed package, **minimum $500/month**. Ads get
daily live/valid-date/function checks by part-time staff. The participating-merchant
list ("Indexed Flipp Lite + Top 50" sheet) is maintained by the Skeleton Team via
**#flipplite** (no direct edit access).

**Support channels for indexing:**

| Channel | Purpose |
|---|---|
| #onboardings | OBQB team; onboarding questions (tag @QB) |
| #helpme-cxe | Skeleton Team; confirm correct escalation for indexing issues (tag @SkeletonTeam) |
| #ops-stack-support | Support adjusting flyer-type stacks |

> The escalation path for indexing was noted as changing soon (indexing revamp in
> progress) — confirm the current process in the channels above.

See also `missing-flyers-and-indexing.md` and `indexing-ci-baseline-tasks.md`.

---

## Rebranding a retailer (manual changes)

**Prerequisites:**
- Confirm the go-live date of the rebrand before changing merchant name & logo.
- Request the updated merchant name and updated logos for both **Logo** and
  **Storefront Logo** fields (Details page).
- If the Hosted experience is moving to a different website, involve the account PT
  (or file a Technical Enablement (TE) Support Ticket) to determine whether new
  credentials are needed or the retailer reuses the same integration code — this
  depends on whether a **new name identifier** is generated. A new name identifier
  implies new SFTP credentials and a new codesheet config name.
- Confirm the new Hosted URL; if changing, update it in FAdmin and in the Account &
  Vendor Guides, and inform OS for live-check purposes.
- **File a Harmonization Troubleshooting (HTS) ticket** to determine whether to
  re-harmonize existing stores or ask Foursquare to rename stores.
  **DO NOT re-harmonize existing stores before confirmation — you will lose
  existing store trip reporting.**
- Connect with BD to confirm past-flyer reporting is unaffected (they check with
  the PIA team).
- Connect with Marketing to update the merchant name in push notifications.
- If the retailer has a US/Canadian counterpart with an account team, give that
  Ops team visibility.

**Day of the rebrand:**
- Update & live-check logos and name on **both Hosted and Flipp App/Web**.
- To reflect changes on the Storefront scrolling interface, **unmark Autostack
  Spotcheck / Spotcheck QC complete, then re-mark complete.**
- Live-check that the flyer is live on the correct Hosted URL and verify any other
  changes.

---

## Offboarding

**Offboard a retailer when:**
1. Ops has not received content in **6 months** (and the retailer is not seasonal).
2. The account team has had no communication / indication of assets in 6 months.
3. The retailer advises they will no longer send assets.

**If the account stops sending files:**
1. Notify the account team.
2. Advise the **Content Improvement team** to start assessing whether content can
   be indexed. Provide: Merchant Name, FAdmin Merchant ID, Merchant Website URL,
   and the **content cutoff date** (last day Flipp will have content).

**BD cutting a retailer for budget reasons:** processing stops if the retailer
won't meet the BD-proposed **Minimum Spend** (typically $2–5k monthly to stay
live). Stay looped in, ensure the Minimum Spend Operations Progress Tracker fields
are filled, and the Ops Lead should confirm via Slack that BD has notified Content
Improvement to assess indexing.

**Content becoming indexed** (cost-analysis initiative): BD reaches out to the Ops
Lead. Action items: confirm the indexer turn-on date with BD, confirm BD is filing
the indexer ticket (BD tells the retailer), and email the retailer confirming their
last processed publication and that you'll no longer be on the account (a template
is in the source doc — contacts/addresses omitted here).

---

*See also: `codesheet-errors.md`, `stores-and-harmonization.md`,
`missing-flyers-and-indexing.md`, `indexing-ci-baseline-tasks.md`,
`hosted-and-previews.md`, `publishing-and-go-live.md`, `escalation-and-tickets.md`.*

*Source: Confluence "Retailer Onboardings" (XPTCXE, 3129144452). Contacts/credentials
omitted. Channel #helpme-ops renamed to #helpme-cxe (2026-07). Last reviewed: 2026-07-22.*
