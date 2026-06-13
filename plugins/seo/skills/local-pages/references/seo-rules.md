# SEO Rules for Local Pages

On-page SEO optimisation for service pages and location pages.

## Core Principle

**SEO should be invisible to the reader.**

If a reader can tell your copy was written for search engines, you've done it wrong. Write for humans first, then verify SEO requirements are met.

---

## Keyword Placement Requirements

### Primary Keyword Must Appear In:

| Location | Priority | Notes |
|----------|----------|-------|
| Title tag | Critical | Front-loaded where possible |
| H1 heading | Critical | Natural, not stuffed |
| First 100 words | Critical | In opening paragraph |
| At least one H2 | High | Natural variation acceptable |
| Meta description | High | For SERP matching |
| URL slug | High | Short, readable |

### Secondary Keywords Should Appear In:

| Location | Notes |
|----------|-------|
| Other H2 headings | Variations, not exact match |
| H3 headings | Where natural |
| Body copy | Distributed throughout |
| Image alt text | Descriptive, includes keywords |

---

## Keyword-Rich Heading Strategy

### H1 Heading

One per page. Includes primary keyword with benefit or differentiator.

**Formula:** [Primary Keyword] + [Benefit/Differentiator]

**Examples:**
- "Boiler Repair in Dartford — Same-Day Service"
- "Emergency Plumber in Dartford — 24/7 Call-Outs"
- "Local Heating Engineer in Dartford & North Kent"

### H2 Headings

Major sections. Include keyword variations.

**For Service Pages:**
```
H2: How Our [Keyword Variation] Works
H2: Why Choose [Business] for [Keyword Variation]
H2: Common [Related Keyword] Problems We Fix
H2: [Primary Keyword] FAQ
H2: [Service] in [Location] Areas
```

**For Location Pages:**
```
H2: [Service 1] in [Location]
H2: [Service 2] in [Location]
H2: [Service 3] in [Location]
H2: Why [Location] Residents Choose [Business]
H2: Areas Near [Location] We Cover
```

### H3 Headings

Subsections. Focused on reader clarity; keywords secondary.

Use H3s for:
- FAQ questions
- Specific problems/situations
- Service sub-types
- Process steps

---

## Natural Keyword Usage

### Don't Stuff

**Bad:** "Looking for boiler repair in Dartford? Our Dartford boiler repair service provides boiler repair Dartford residents can trust."

**Good:** "When your boiler breaks down in Dartford, you need someone local who can fix it fast. I'm based 10 minutes away and carry common parts in the van."

The second version:
- Mentions location naturally
- Includes the service contextually
- Sounds like a real person
- Still signals relevance to search engines

### Use Variations

Search engines understand synonyms and related terms. Don't repeat the exact same phrase.

| Primary | Natural Variations |
|---------|-------------------|
| "boiler repair Dartford" | "fix your boiler", "boiler breakdown", "heating engineer Dartford" |
| "plumber in Bexley" | "plumbing services", "local plumber", "Bexley plumbing" |
| "emergency electrician" | "24/7 electrician", "electrical emergency", "call-out electrician" |

---

## Title Tag Optimisation

### Format

**[Primary Keyword] + [Benefit/Location] | [Business Name]**

### Requirements

- **Length:** 50-60 characters (displays ~60 on desktop)
- **Primary keyword:** Front-loaded where possible
- **Differentiator:** What makes you click-worthy
- **Brand:** At end, after pipe character

### Examples

```
Boiler Repair Dartford — Same-Day Service | Lane Heating
Emergency Plumber Bexley — 24/7 Call-Outs | Lane Plumbing
Heating Engineer in Greenhithe | Gas Safe Registered
```

---

## Meta Description Optimisation

### Format

**[Problem/Solution]. [Proof/Differentiator]. [CTA].**

### Requirements

- **Length:** 150-155 characters
- **Primary keyword:** Include for SERP bolding
- **Benefit:** Why click this result
- **CTA:** Soft call to action

### Examples

```
Boiler broken? Fixed same-day with upfront pricing. Gas Safe registered
engineer serving Dartford & North Kent. Call now for fast response.
(155 chars)

Local plumber in Bexley for emergencies, repairs & installations.
Fixed prices, no call-out fee. 4.9★ from 120+ reviews. Book online.
(153 chars)
```

---

## Local SEO Signals

### Geographic Terms

Include naturally throughout:
- Town/city names
- Neighbourhoods or areas
- Nearby locations
- Postcodes (in contact section)

### Local Proof

- Testimonials mentioning specific locations
- References to local landmarks or areas
- Photos with local context
- "Based in [Location]" statements

### NAP Consistency

Name, Address, Phone must be:
- Present on every page
- Consistent with Google Business Profile
- In text (not just images)

---

## Schema Markup Recommendations

### LocalBusiness Schema (Required)

```json
{
  "@type": "LocalBusiness",
  "name": "Business Name",
  "telephone": "+44...",
  "address": {...},
  "geo": {...},
  "openingHours": "...",
  "priceRange": "££",
  "areaServed": [...]
}
```

### FAQ Schema (For FAQ Sections)

Wrap FAQ sections with FAQPage schema. Increases SERP real estate.

### Review Schema (If Displaying Reviews)

Aggregate or individual review markup.

### Service Schema (Optional)

For detailed service descriptions.

---

## Internal Linking

### Link Strategically To:

- Related service pages
- Location pages for mentioned areas
- Contact/booking page
- Cornerstone content

### Anchor Text

**Good:** "Learn more about our [boiler servicing plans] for year-round peace of mind."

**Bad:** "Click [here] to learn more."

Descriptive anchor text helps readers and search engines.

---

## URL Structure

### Requirements

- Short and readable
- Includes primary keyword
- Lowercase, hyphens between words
- No dates, IDs, or parameters

### Examples

```
/boiler-repair-dartford/
/plumber-in-bexley/
/heating-services/
```

---

## Image Optimisation

### Alt Text

Descriptive, includes keyword where natural.

**Examples:**
- "Gas Safe engineer repairing boiler in Dartford home"
- "New Worcester boiler installation in Bexley"

### File Names

Descriptive, keyword-rich.

**Examples:**
- `boiler-repair-dartford.jpg`
- `gas-safe-engineer-working.jpg`

---

## Content Length for Rankings

### Minimum Targets

| Page Type | Minimum | Optimal |
|-----------|---------|---------|
| Service page | 1000 words | 1200-1500 words |
| Location page | 1000 words | 1200-1500 words |

### Quality Over Length

Every word must earn its place:
- Does it add value for the reader?
- Does it support the persuasive argument?
- Would you include it if paying per word?

Long content that doesn't convert is worse than short content that does. But for competitive local terms, 1000+ words is typically needed to rank.

---

## Indexing & Differentiation

Content must pass Google's quality signals to be indexed and rank. See `../../copywriting/references/seo-indexing-guidelines.md` for full principles.

### The Duplicate Content Problem

Location pages are high-risk for thin/duplicate content. Google will not index pages that are:
- Too similar to each other (just location names swapped)
- Too similar to competitors (generic service descriptions)
- Lacking genuine unique value

### Differentiation Requirements

**Every location page must have:**
- 3+ locally-specific details (landmarks, neighbourhoods, local issues)
- Area-specific proof (testimonials mentioning location, jobs completed there)
- Unique content that couldn't apply to any other location

**Every service page must have:**
- Specific examples, scenarios, or case studies
- Genuine expertise competitors haven't covered
- Unique angle (specialisation, approach, experience)

### Content Quality Signals

| Signal | Good | Bad |
|--------|------|-----|
| Language | Natural, conversational | Robotic, overly formal |
| Specificity | Real numbers, examples | Vague generalisations |
| Entity focus | Clear primary topic | Unfocused, mixed topics |
| Intent match | Matches SERP results | Wrong content type |

### Pre-Publish Test

Before any page goes live:
1. **Read aloud test** — Does it sound like a human wrote it?
2. **Competitor test** — Could they copy this by changing the business name?
3. **Same-site test** — Is this significantly different from our other pages?
4. **Intent test** — Does this match what's ranking for our target keyword?

If any test fails, revise before publishing.

---

## SEO Checklist

Before delivering any page:

### On-Page
- [ ] Primary keyword in title, H1, first 100 words, one H2
- [ ] Primary keyword in meta description
- [ ] Keyword variations in other H2/H3 headings
- [ ] Natural keyword density (not stuffed)
- [ ] Heading hierarchy logical (H1 → H2 → H3)
- [ ] URL is short, readable, includes keyword

### Meta
- [ ] Title tag 50-60 characters, keyword front-loaded
- [ ] Meta description 150-155 characters with CTA
- [ ] Both written for clicks, not just keywords

### Local
- [ ] Location in title, H1, first paragraph
- [ ] Nearby areas mentioned
- [ ] NAP details present and consistent
- [ ] Local proof elements included

### Technical
- [ ] Images have descriptive alt text
- [ ] Internal links to related pages
- [ ] Schema markup recommendations noted
- [ ] Mobile-friendly structure (short paragraphs, scannable)
