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
- [ ] Client will provide images
- [ ] Use stock images
- [ ] Generate placeholder images

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

List all locations/areas the business covers:

1. [Location 1 - e.g., Basildon]
2. [Location 2 - e.g., Billericay]
3. [Location 3 - e.g., Brentwood]

[Add more as needed]

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

### Location Pages

| Location | URL | Key Content |
|----------|-----|-------------|
| [Location 1] | /[location] | Local info, services in area, CTA |
| [Location 2] | /[location] | Local info, services in area, CTA |

### Matrix Pages (Service + Location)

| Combination | URL | Purpose |
|-------------|-----|---------|
| [Service] in [Location] | /[location]/[service] | Local SEO targeting |

**Total Page Count:** [Calculate: core + services + locations + matrix]

---

## Content Requirements

### Testimonials
- [ ] Client will provide real testimonials
- [ ] Use placeholder testimonials (mark for replacement)
- Number needed: [e.g., 3-5]

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
- Target areas: [List main areas]

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
├── services/
│   ├── [service-1-slug].md
│   ├── [service-2-slug].md
│   └── ...
├── locations/
│   ├── [location-1-slug].md
│   ├── [location-2-slug].md
│   └── ...
└── matrix/ (ALL service × location combinations)
    ├── greenhithe-boiler-repair.md
    ├── greenhithe-gas-safety-certificates.md
    ├── dartford-boiler-repair.md
    ├── dartford-gas-safety-certificates.md
    └── ... (every combination)

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
