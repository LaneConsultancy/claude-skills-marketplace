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
- [ ] Client will provide images
- [ ] Use stock images
- [ ] Generate placeholder images

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

List ALL locations/areas the business covers (full list for brief compatibility):

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

### Matrix Pages (Service + Location) -- FULL BUILD ONLY

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
- Service pages: [remaining services not in demo...]
- Location pages: [remaining locations not in demo...]
- ALL matrix pages ([N services] x [M locations] = [total] pages)
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
