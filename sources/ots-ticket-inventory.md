# OTS (Ops Troubleshooting) — Ticket Inventory & Pattern Analysis

> **What this is:** A structured summary of the **Ops Troubleshooting (OTS)** Jira
> board (project OTS, board 315), covering **381 tickets created 2024-01-02 → 2026-07-08**
> (365 resolved/Done). This is the front-line help desk for flyer-processing
> issues. This document backs the troubleshooting articles in
> `docs/knowledge-base/` and is itself a useful NotebookLM source for "how often
> does X happen / show me examples."
>
> **Method:** Tickets were pulled via Jira (JQL `project = OTS AND created >=
> "2024-01-01"`), and the last comments of each were mined for resolution
> patterns. Categorization below is by keyword on the ticket summary (approximate;
> a ticket can span categories). A handful of TEST/example tickets are excluded
> from the guidance.

## Ticket types

- **Help Desk – Question** — the vast majority (~347); day-to-day processing
  issues raised by ops/CX.
- **Ad Hoc / Team Request** (~25) and **TMI Request** (~9).

## Status

Almost all tickets are **Done** (365 of 381). A small number sit in Triage/
Assigned/Escalated at any time.

## Resolution routing (where OTS tickets go when escalated)

Mining the resolution comments shows the common escalation destinations:

| Destination | What it's for | Seen in |
|---|---|---|
| **FD** (indexing/feed team, board 312) | Broken indexer, wrong scraping URL/dates | ~29 refs; "indexer" mentioned ~83× |
| **CLSD** (content escalation) | General content/pipeline issues needing backend help | ~35 refs |
| **PIA** (store/place data) | Harmonization, store location/duplicate data | several |
| **HS / Hosted team** (board 67) | Hosted site, iframe, preview, front-end rendering | several |
| Account team (via **DOC**) | Third-party app display (not Flipp-hosted) | a few |

Common **self-serve** resolutions (no escalation): re-run **AutoBox**/auto tag,
fix **valid dates** in FADMIN, **clone/re-process** a stuck run, **re-save** a
flyer run, toggle **simp pop** off, update **lat/long** and re-harmonize.

---

## Categories by volume (approx.)

| Category | ~Count | Article |
|---|---|---|
| Missing flyer / pages / indexing | ~80 | `missing-flyers-and-indexing.md` |
| Missing coverage (FSA/postal) + wrong-region | ~23 | `missing-flyers-and-indexing.md` |
| Clipping / AutoBox / cutouts | ~28 | `clipping-and-autobox.md` |
| Dates (wrong/expired/valid) | ~23 | `flyer-dates.md` |
| Front-end display | ~22 | `publishing-and-go-live.md` |
| Publishing / go-live | ~21 | `publishing-and-go-live.md` |
| Stores + harmonization | ~29 | `stores-and-harmonization.md` |
| Hosted / previews / links | ~15 | `hosted-and-previews.md` |
| Wrong content | ~15 | (covered across articles) |
| Images / thumbnails / tiles | ~11 | `clipping-and-autobox.md`, `hosted-and-previews.md` |
| Codesheet / upload | ~8 | `codesheet-errors.md` |
| Categorization / tagging | ~5 | `common-live-flyer-issues.md` |
| Duplicates | ~4 | (see missing/wrong content) |

---

## Representative tickets by category

### Missing flyers & indexing
- `OTS-1927` — Brookshire Brothers - Missing FSA
- `OTS-1928` — Bestco Foodmart - Flyer Missing
- `OTS-1929` — Pino's Get Fresh - Flyer Missing
- `OTS-1930` — Nardini Specialties - Flyer Missing
- `OTS-1931` — Sedano's - Flyer Missing
- `OTS-1933` — Quality Foods CAN  - flyer Missing
- `OTS-1939` — Pete's Fresh Market - Flyer Missing
- `OTS-1944` — Sellers Bros - Flyer Pages Missing
- `OTS-1948` — Food Fare broken indexer
- `OTS-1949` — Marche C&T - Duplicate Flyer and Missing Flyers

### Coverage: FSA / postal / wrong-region targeting
- `OTS-1927` — Brookshire Brothers - Missing FSA
- `OTS-1959` — Fruiticana - Displaying Alberta flyer to BC Postal codes
- `OTS-1964` — Metropolitan Market - Workflow Execution not showing future flyers
- `OTS-1969` — H Mart Alberta - Calgary Postal Codes are seeing the Edmonton Flyer Instead of the Calgary Flyer
- `OTS-1985` — Ingles Market - FSA Missing
- `OTS-1986` — Redner's Market - Flyer being shown to Virginia Zip Codes
- `OTS-1994` — Oceans Fresh Food Market - FSA Missing
- `OTS-1997` — Centra Foods - Showing Barrie Postal Codes the Aurora flyer

### Clipping / AutoBox / cutouts
- `OTS-1934` — Fareway - Not Clippable
- `OTS-1935` — Seasons Food Mart - Flyer Not Clippable
- `OTS-1936` — Rite Aid - Item Cutout Gen Failing
- `OTS-1941` — Terra Foodmart - Box Draw Off-Center on Second Page
- `OTS-1943` — El Rancho Supermercado - Box Draw Off-Center
- `OTS-1979` — Nations Fresh Foods - Flyer Not Fully Clippable, Some Boxes are Off
- `OTS-1981` — Rite Aid Item Cutout Generation Failing
- `OTS-1984` — Zion Market - some items not clippable
- `OTS-2005` — Supermarche PA - Flyer Not Clippable
- `OTS-2020` — Oceans Fresh Food Market - Some Items Not Clippable

### Stores & harmonization
- `OTS-1967` — Loblaws Store Not Appearing on PC Optimum App
- `OTS-1982` — Ashley Furniture Homestore no longer live, sessions won't run to allow Fadmin Publish
- `OTS-1991` — All Items in Sportsman's Warehouse flyer are appearing as "In-Store Only"
- `OTS-2002` — Pet Valu - 36 Stores Failing Harmonization with False Duplicate Store
- `OTS-2009` — Ashley Furniture Homestore CA/US Harmonization Failure- Stores already harmonized
- `OTS-2024` — Harmonization Audit: Wellwise SDM
- `OTS-2025` — Harmonization Audit: Proxim
- `OTS-2035` — Harmonization Audit: Nature' Emporium
- `OTS-2053` — Error encountered while trying to add a new store (Callaghan’s AG Foods, Store Code 183253). The system indicates that the Merchant store code has already been taken, although a search does not show this store code in use for AG Foods merchant.
- `OTS-2056` — [Due EOD Aug 1] Lidl US - Grand Opening store not appearing on hosted site

### Flyer dates
- `OTS-1932` — Marche C&T - Valid Dates are Thurs to Thurs instead of Thurs to Wed
- `OTS-1972` — Value Center Marketplace - Expired Flyer
- `OTS-1993` — Supermercado Teloloapan - Incorrect Flyer Valid Dates
- `OTS-2029` — Farm and Spice - Expired Flyer
- `OTS-2069` — Calgary Co-op Item Valid Dates not Showing correctly
- `OTS-2074` — CX Issue - BTrust Supermarket - Expired Flyer Visible
- `OTS-2083` — CX Issue - Vine Ripe Market - Incorrect Valid Dates
- `OTS-2091` — CX Issue - Vine Ripe Market - Incorrect Valid Dates

### Hosted & previews
- `OTS-1961` — [DUE 02.27 EOD] Sportsman's Warehouse Preview Links Not Working
- `OTS-1962` — Rite Aid - Page Link not re-directing to correct page on hosted only
- `OTS-1968` — The RCSS ONT and WEST flyers are not loading properly, with half of the page appearing cropped and cut off.
- `OTS-1971` — New items + links not reflecting in vertical preview
- `OTS-1973` — TRU - No available flyer in hosted preview link
- `OTS-1980` — "This site can't be reached" Error for Mondou Preview Links
- `OTS-1992` — [urgent] Live Lowes Food Flyer Not appearing On Hosted
- `OTS-1995` — Ranch Fresh Supermarket Full Screen Preview not interactive 
- `OTS-2012` — Dunham's Sports Guides - Preview Links not showing correct links 
- `OTS-2015` — NAPA Auto Parts - Preview Link not showing 'See More Info' button

### Publishing / go-live / clones / pipelines
- `OTS-1938` — Hannaford - Cloning Pipeline Stuck
- `OTS-1954` — RONA pages missing a track ID, processing blocked
- `OTS-1982` — Ashley Furniture Homestore no longer live, sessions won't run to allow Fadmin Publish
- `OTS-1988` — Providing Direct Link to Flyer that is not Live [Boscovs]
- `OTS-2006` — PetSmart Clone not showing Vendor, System & Ops Tasks
- `OTS-2027` — FQC Page Not Accessible
- `OTS-2030` — [DUE June 4] HH Clone Erroring Out Consistently
- `OTS-2047` — Sobeys ATL/West/ON and Safeway - Flyer Pipelines Stuck and Missing Slices
- `OTS-2048` — [DUE July 12] -  Walgreen flyer Stuck :( 
- `OTS-2060` — LIVE FLYER >>> FLYER BLOCKED 

### Front-end display
- `OTS-1964` — Metropolitan Market - Workflow Execution not showing future flyers
- `OTS-1966` — Tepperman's - certain flyer pages not displaying
- `OTS-1971` — New items + links not reflecting in vertical preview
- `OTS-1974` — Menards - New Boxes Create Not Showing On Front End
- `OTS-1978` — Safeway NOW and Health & Beauty publications are not displaying pre-price, price,  sale story text on Flipp only. 
- `OTS-1998` — Ingles Market - Flyer Item Title appear as 'Null'
- `OTS-2006` — PetSmart Clone not showing Vendor, System & Ops Tasks
- `OTS-2012` — Dunham's Sports Guides - Preview Links not showing correct links 

---

*Generated from OTS Jira export, 2024-01-02 → 2026-07-08. Last reviewed: 2026-07-14.*
