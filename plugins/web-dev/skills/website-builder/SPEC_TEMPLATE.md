# Website Specification Template

You have two options for providing your website specification:

1. **Let the skill interview you (recommended):** Just run `/website-builder` without a spec file. Claude will ask you questions in 5 quick rounds and generate the spec automatically.
2. **Fill this in manually:** Copy this template to your project's `/spec/brief.md` and fill it in before running the website-builder. The interview will be skipped if a spec file already exists.

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

**One source of truth the whole build, GBP, schema, and directories MUST match, character for character.** Google cross-checks these sources to validate the business as a single entity; inconsistency is a demotion signal.

**Canonical Business Name:** [Exact legal/trading name, character for character. E.g., Watermark Plumbing]
**NAP (Name, Address, Phone):**
- Name: [must match Canonical Business Name exactly]
- Address: [exact format used on the GBP]
- Phone: [exact format used on the GBP]
**Canonical Services Terminology:** [The exact service names/descriptions to use everywhere: site, GBP services list, schema, directories. E.g., "Boiler Repairs" not "boiler fixing" on one page and "boiler repair" on another]
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
- [ ] Generate placeholder images (build ONLY; MUST be flagged as launch blockers to replace with real photos before go-live)

---

## Services Offered

List all services the business provides:

1. **[Service Name]**
   - Description: [Brief description]
   - Key benefits: [What makes this valuable]

2. **[Service Name]**
   - Description: [Brief description]
   - Key benefits: [What makes this valuable]

[Add more as needed]

---

## Locations Served

List all locations/areas the business covers. Coverage alone does NOT earn a page; proof does.

1. [Location 1 - e.g., Basildon]
2. [Location 2 - e.g., Billericay]
3. [Location 3 - e.g., Brentwood]

[Add more as needed]

### Proof Per Location

**This table decides which towns get their own page.** A town earns a location page ONLY if it has real proof (reviews from there, jobs done there, original photos of that work). Cap primary location pages at 3-6 for most trades. Towns with no proof are named on the single "Areas We Cover" page, not given their own URL.

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

Only towns that qualify in the Proof Per Location table above. Every other town served goes on the single "Areas We Cover" page.

| Location | URL | Proof (why it earns a page) | Key Content |
|----------|-----|------------------------------|-------------|
| [Location 1] | /[location] | [reviews/jobs/photos evidence] | Local info, services in area, CTA |

### Matrix Pages (Service + Location): PROOF-BACKED COMBINATIONS ONLY

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
- [ ] Use placeholder testimonials (build ONLY; MUST be flagged as launch blockers for the client to replace before go-live)
- Number needed: [e.g., 3-5]

### E-E-A-T Block (required per service and location page)

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

## Notes

[Any other relevant information, special requests, or context]
```

---

## Workflow Summary

```
1. Create project folder
2. Start Claude Code: claude
3. Run the build (recommended — ralph-loop for auto-resumption):
   /ralph-loop [prompt from PROMPT_TEMPLATE.md] --max-iterations 30 --completion-promise "BUILD COMPLETE"

   OR for small sites (< 10 pages): /website-builder

4. Claude will:
   - Phase 0: Interview you to gather requirements (skipped if spec exists)
   - Phase 1: Research competitors & SERP to determine content requirements
   - Phase 2: Write ALL content AND generate images in parallel
   - Phase 3-9: Build the site with real content and images from the start
   - All phases run autonomously after Phase 0 — no user input needed
   - Progress tracked in /spec/build-state.md for auto-resumption
```

---

## Files Generated During Build

The website-builder skill will create these files during the research and content phases:

### Research Phase Output (Phase 1)
```
/spec/content-requirements.md
├── Minimum word counts per page type
├── Required content sections (FAQs, process steps, etc.)
├── Content gaps/opportunities identified
└── Recommended FAQs from "People Also Ask"

/spec/keyword-mapping.md
├── Primary keyword per page
├── Secondary keywords (2-3 per page)
├── LSI/related terms
└── Search intent per page
```

### Content Writing Phase Output (Phase 2 - Track A)
```
/spec/content/
├── homepage.md
├── about.md
├── contact.md
├── areas-we-cover.md          (every town served without its own page)
├── services/                  (one per service, ALWAYS)
│   ├── [service-1-slug].md
│   ├── [service-2-slug].md
│   └── ...
├── locations/                 (ONLY proof-backed towns, capped at 3-6)
│   ├── [location-1-slug].md
│   ├── [location-2-slug].md
│   └── ...
└── matrix/ (ONLY proof-backed service × location combinations, NOT a full grid)
    ├── greenhithe-boiler-repair.md          (jobs/reviews/photos exist here)
    ├── dartford-gas-safety-certificates.md  (jobs/reviews/photos exist here)
    └── ... (proof-backed combinations only)

Each content file contains:
- Meta title
- Meta description
- H1
- Full page content with H2/H3 structure
- CTA text
```

### Image Generation Phase Output (Phase 2 - Track B)
```
/public/images/ (or /src/assets/images/)
├── hero-homepage.jpg
├── hero-[service-1-slug].jpg
├── hero-[service-2-slug].jpg
├── hero-[location-slug].jpg (if distinct location images needed)
├── about-team.jpg
└── ...

/spec/image-manifest.md
├── List of all generated images
├── Purpose of each image
├── Dimensions
└── Recommended alt text for each
```

**IMPORTANT**: Coding does NOT begin until all content AND images are ready.
