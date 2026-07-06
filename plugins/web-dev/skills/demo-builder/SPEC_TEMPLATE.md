# Demo Builder Specification Template

You have two options for providing your website specification:

1. **Let the skill interview you (recommended):** Just run `/demo-builder` without a spec file. Claude will ask you questions in 5 quick rounds and generate the spec automatically.
2. **Fill this in manually:** Copy this template to your project's `/spec/brief.md` and fill it in before running the demo-builder. The interview will be skipped if a spec file already exists.

**Important:** This uses the same brief format as `/website-builder`, so the full build can pick up where the demo left off.

---

## Create: `/spec/brief.md`

```markdown
# Website Brief

## Business Information

**Business Name:** [e.g., Watermark Plumbing]
**Owner/Contact:** [e.g., Mark Green]
**Phone:** [e.g., 07954 153125]
**Email:** [e.g., mark@watermarkplumbing.co.uk]
**Address:** [e.g., 24 East Walk, Basildon, SS14 1HA]

**Business Description:**
[2-3 sentences about what the business does]

**Unique Selling Points:**
- [USP 1]
- [USP 2]
- [USP 3]

**Target Audience:**
[Who are the customers? Homeowners? Businesses? Location-specific?]

**Competitors:**
- [Competitor 1 URL - for reference]
- [Competitor 2 URL]

---

## Entity Consistency

**One source of truth the whole build, GBP, schema, and directories MUST match, character for character.** Google cross-checks these sources to validate the business as a single entity; inconsistency is a demotion signal. (Same fields as /website-builder so the full build inherits them.)

**Canonical Business Name:** [Exact legal/trading name, character for character. E.g., Watermark Plumbing]
**NAP (Name, Address, Phone):**
- Name: [must match Canonical Business Name exactly]
- Address: [exact format used on the GBP]
- Phone: [exact format used on the GBP]
**Canonical Services Terminology:** [The exact service names/descriptions to use everywhere: site, GBP services list, schema, directories]
**GBP Website Link Target:** [The STRONG service or location page the Google Business Profile links to, NOT the homepage if the homepage already ranks organically (Sterling Sky Diversity Update). E.g., /services/boiler-repairs/]
**GBP Link UTM Parameters:** [UTM string appended to the GBP link so its traffic is measurable. E.g., ?utm_source=google&utm_medium=organic&utm_campaign=gbp]

---

## Tech Stack

**Framework:** [Next.js 14 / Astro / etc.]
**UI Library:** [ShadCN / Tailwind / etc.]
**Styling:** [Tailwind CSS]
**Hosting:** [Vercel / Netlify / etc.]
**CMS:** [None / Sanity / Contentful / etc.]

---

## Design Requirements

**Style Direction:**
[Modern & clean / Traditional & trustworthy / Bold & energetic / etc.]

**Design Aesthetic:** [Premium Agency / Clean Editorial / Bold Industrial]

**Color Palette:**
- Primary: [e.g., #1E40AF - blue]
- Secondary: [e.g., #10B981 - green]
- Accent: [e.g., #F59E0B - amber]
- Background: [e.g., #FFFFFF]
- Text: [e.g., #1F2937]

**Typography:**
- Headings: [e.g., Inter, bold]
- Body: [e.g., Inter, regular]

**Reference Sites (for style inspiration):**
- [URL 1 - what you like about it]
- [URL 2 - what you like about it]

**Logo:** [Path to logo file or "to be provided"]

**Images:**
- [ ] Client will provide REAL photos (strongly preferred; original work/van/team/premises is an E-E-A-T signal)
- [ ] Use stock images (negative E-E-A-T signal; avoid where possible)
- [ ] Generate placeholder images (demo/build ONLY; MUST be flagged as launch blockers to replace with real photos before go-live)

---

## Services Offered

List ALL services the business provides (full list for brief compatibility):

1. **[Service Name]**
   - Description: [Brief description]
   - Key benefits: [What makes this valuable]

2. **[Service Name]**
   - Description: [Brief description]
   - Key benefits: [What makes this valuable]

[Add more as needed]

---

## Locations Served

List ALL locations/areas the business covers (full list for brief compatibility). Coverage alone does NOT earn a page; proof does.

1. [Location 1 - e.g., Basildon]
2. [Location 2 - e.g., Billericay]
3. [Location 3 - e.g., Brentwood]

[Add more as needed]

### Proof Per Location

**This table decides which towns get their own page in the full build.** A town earns a location page ONLY if it has real proof (reviews from there, jobs done there, original photos of that work). Cap primary location pages at 3-6 for most trades. Towns with no proof are named on the single "Areas We Cover" page. Captured at demo intake so /website-builder inherits it.

| Location | Reviews (from this town) | Jobs Completed (here) | Photos (of real work here) | Qualifies for own page? |
|----------|--------------------------|------------------------|-----------------------------|--------------------------|
| [Location 1] | [e.g., 4 Google reviews] | [e.g., 30+ boiler jobs] | [e.g., 6 job photos] | [Yes / No] |
| [Location 2] | [none yet] | [1-2 jobs] | [none] | [No, Areas We Cover] |

---

## Page Requirements

### Core Pages

| Page | URL | Purpose | Key Content |
|------|-----|---------|-------------|
| Homepage | / | Main landing page | Hero, services overview, trust signals, CTA |
| About | /about | Build trust | Business story, team, credentials |
| Contact | /contact | Lead capture | Form, phone, email, map, hours |
| Services | /services | Service overview | All services listed |

### Service Pages

| Service | URL | Key Content |
|---------|-----|-------------|
| [Service 1] | /services/[slug] | Description, benefits, process, CTA |
| [Service 2] | /services/[slug] | Description, benefits, process, CTA |

### Location Pages (PROOF-BACKED ONLY, cap 3-6)

Full build: only towns that qualify in the Proof Per Location table above. Every other town served goes on the single "Areas We Cover" page.

| Location | URL | Proof (why it earns a page) | Key Content |
|----------|-----|------------------------------|-------------|
| [Location 1] | /[location] | [reviews/jobs/photos evidence] | Local info, services in area, CTA |

### Matrix Pages (Service + Location) -- FULL BUILD ONLY, PROOF-BACKED COMBINATIONS ONLY

Do NOT build a full service × location grid; templated matrices now harm rankings (doorway-page filtering, Dec 2025 core update). Build a matrix page ONLY where there is real proof for that specific service in that specific town. Each must pass the removed-city-name test (roughly 50% locally-unique content).

| Combination | URL | Proof (why it earns a page) |
|-------------|-----|------------------------------|
| [Service] in [Location] | /[location]/[service] | [jobs/reviews/photos for this exact combo] |

### Areas We Cover Page

| Page | URL | Purpose |
|------|-----|---------|
| Areas We Cover | /areas-we-cover | Names every other town served (no proof yet) without giving each its own URL |

**Total Page Count:** [Calculate: core + services + proof-backed locations + proof-backed matrix + Areas We Cover. NOT services × locations]

---

## Content Requirements

### Testimonials
- [ ] Client will provide REAL testimonials (strongly preferred; named town, named job)
- [ ] Use placeholder testimonials (demo/build ONLY; MUST be flagged as launch blockers for the client to replace before go-live)
- Number needed: [e.g., 3-5]

### E-E-A-T Block (required per service and location page in the full build)

Post-December 2025 core update, this applies to competitive local queries, not just YMYL:
- **Named person + credential:** [e.g., Mark Green, Gas Safe reg. 123456, visible and linked]
- **Original photo:** [real job/van/premises photo, never stock]
- **Specific testimonial:** [named town, named job]

### Trust Signals
- [ ] Accreditations/certifications to display: [list them]
- [ ] Years in business: [number]
- [ ] Number of jobs completed: [number or approximate]
- [ ] Insurance/guarantee info: [details]

### FAQs
- [ ] Client will provide FAQs
- [ ] Generate common industry FAQs
- Number needed: [e.g., 5-10]

---

## Functionality Requirements

**Forms:**
- [ ] Contact form (name, email, phone, message)
- [ ] Quote request form
- [ ] Callback request form

**Integrations:**
- [ ] Google Maps embed
- [ ] Google Analytics
- [ ] Facebook Pixel
- [ ] Other: [specify]

**Special Features:**
- [ ] Blog/News section
- [ ] Service area map
- [ ] Before/after gallery
- [ ] Video embeds
- [ ] Other: [specify]

---

## SEO Requirements

**Primary Keywords:**
- [Keyword 1]
- [Keyword 2]
- [Keyword 3]

**Local SEO:**
- Google Business Profile: [URL if exists]
- GBP website link target + UTM: [see Entity Consistency block; strong non-homepage page, UTM-tagged]
- Bing Places: [claimed? ChatGPT local search runs on Bing's index]
- IndexNow: [enabled on Cloudflare? toggle so Bing indexes changes immediately]
- Target areas: [List main areas]

**Schema (structured data):**
- LocalBusiness subtype: [specific type, e.g. Plumber / HVACBusiness / Electrician, not generic LocalBusiness]
- NAP in schema must match the GBP character for character (see Entity Consistency block)
- sameAs array on homepage: [GBP, socials, key directory listings]

**Meta Information:**
- Default title format: [e.g., "Page Name | Business Name"]
- Default description: [Template for meta descriptions]

---

## Timeline & Priority

**Must Have (Launch Blockers):**
1. [Feature/page 1]
2. [Feature/page 2]

**Should Have (Important):**
1. [Feature/page 1]
2. [Feature/page 2]

**Nice to Have (Post-Launch):**
1. [Feature/page 1]
2. [Feature/page 2]

---

## Demo Build Scope

**Build Type:** Demo (built with /demo-builder)
**Demo Date:** [date]

### Pages Included in Demo
- Homepage (full effort)
- About page
- Contact page
- Service pages (demo samples): [service-1], [service-2], [service-3]
- Location pages (demo samples): [location-1], [location-2]
- Matrix pages: NONE (full build only)

### Pages Deferred to Full Build
- Service pages: [remaining services not in demo; one pillar page each]
- Location pages: [proof-backed towns not in demo, capped at 3-6 total]
- Proof-backed matrix pages: [only service+location combos with real jobs/reviews/photos, NOT a full grid]
- "Areas We Cover" page: [names every other town served without its own URL]
- Entity/GBP/schema work: entity consistency sheet, specific-subtype LocalBusiness schema with sameAs, GBP link + UTM, Bing Places + IndexNow
- Blog/news section (if applicable)

### Handoff Notes
This brief is fully compatible with /website-builder. To continue to full build:
1. Run /website-builder in this project directory
2. It will detect /spec/brief.md and skip Phase 0
3. It will detect existing /spec/content/ files and reuse them
4. It will detect existing code and extend it (not rebuild)

---

## Notes

[Any other relevant information, special requests, or context]
```
