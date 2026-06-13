---
name: rank-rent-website-builder
description: Build Astro rank-and-rent lead-generation websites around one main service + location keyword and close variants. Use for rank-and-rent niche sites, exact/partial-match domains, SERP competitor checks, lightweight backlink/citation research, local SEO architecture, lead capture, and launch quality gates.
---

# Rank & Rent Website Builder

Use this skill instead of the generic website-builder when the site is a rank-and-rent asset, not a website for an existing real business.

The goal is a focused local lead-generation site that can rank for a single service + location niche, capture calls/forms, and later rent leads to an operator. Default stack is Astro on Vercel.

## Core Rules

- Build around one primary keyword: `[service] [location]`.
- Use close variants only when they support the primary intent.
- Default framework: Astro. Do not switch stacks unless the user explicitly asks.
- Conversion comes first: visible phone CTA, short enquiry form, urgent/local intent above the fold.
- SEO comes before design polish: SERP reality, page intent, keyword map, schema, internal links, fast static pages.
- Be truthful. Do not invent real reviews, accreditations, business history, engineers, addresses, or certifications.
- Use placeholders only where clearly marked in internal specs, never as launch copy.
- For every public site, enforce the repo quality gates in `AGENTS.md`: dev server, browser screenshots, mobile/tablet/desktop, console/network checks, accessibility, production build.

## Inputs

Collect or infer these before building:

- Primary keyword: e.g. `mobile mechanic Colchester`
- Main service: e.g. `mobile mechanic`
- Location: e.g. `Colchester`
- Domain: exact/partial match if known
- Phone routing: Twilio number or temporary CTA state
- Form routing: custom Astro form or Tally
- Owner lead recipient: default `george@laineconsultancy.com`
- Renter details: blank until a renter exists
- Nearby areas worth targeting, if genuinely supportable

If missing, create a brief with sensible defaults and mark unknown operational values as `To be confirmed`.

## Required Research

Before writing copy or code, create `spec/` research files.

1. Read the root strategy sources:
   - `../AGENTS.md` or root `AGENTS.md`
   - `Rank-and-Rent Local SEO for Generic Local Sites in 2026.pdf`
   - the relevant spreadsheet row, if available

2. SERP check for the primary keyword:
   - Identify top organic competitors for the exact keyword.
   - Separate real service providers from directories, map packs, lead-gen sites, and national brands.
   - Record page type, title, content depth, backlink/citation clues, GBP/local strength, and obvious weaknesses.

3. Lightweight backlink/citation pass:
   - For the top 3 real competitors, use Apify/DataForSEO/SeoMCP when available to find referring domains or source URLs.
   - Use Open PageRank to score competitor and linking domains when `OPENPAGERANK_API_KEY` exists.
   - Use Common Crawl only for validation or deeper inspection, not as the default backlink source.
   - Classify opportunities as `directory`, `citation`, `local press`, `supplier`, `association`, `blog`, `spam`, or `unknown`.

4. Create these files:
   - `spec/niche-brief.md`
   - `spec/serp-competitors.md`
   - `spec/backlink-opportunities.csv`
   - `spec/keyword-map.md`
   - `spec/content-plan.md`
   - `spec/lead-routing.md`
   - `spec/build-state.md`

## Recommended Sitemap

Keep sites tight. Do not create broad programmatic pages until the primary page is strong.

Minimum:

- `/` targeting the primary `[service] [location]` keyword
- `/contact/`
- `/privacy-policy/`
- `/terms/`

Optional when justified by SERP/content depth:

- `/services/[variant]/` for distinct high-intent service variants
- `/areas/[nearby-location]/` for nearby places with enough real search intent
- `/faqs/` only if FAQ depth would otherwise bloat the homepage

Avoid large service x location matrices for the first build unless research shows real demand and enough unique supportable content.

## Content Standards

Write conversion-first local SEO copy:

- Hero: service + location obvious in the H1 or immediate supporting line.
- Above fold: phone CTA, form CTA, service area, fast reassurance.
- Sections: emergency/routine intent, services handled, how it works, service area, FAQs, trust/verification language, final CTA.
- Use realistic local language without pretending to have a physical office or named mechanics unless true.
- Include variant phrases naturally: `emergency`, `diagnostics`, `at home`, `near me`, `same-day`, `car repair`, and model/service variants where relevant.
- FAQs should answer buying-intent questions, not generic filler.
- Never claim guaranteed rankings, fake reviews, fake local address, or fake memberships.

## Astro Implementation

Default site setup:

- Astro static or hybrid only if needed.
- Put reusable layout/components in `src/layouts` and `src/components`.
- Keep content/data structured in `src/data` or content collections when the site has multiple services/areas.
- Use semantic HTML, accessible forms, real labels, and proper focus states.
- Add metadata per page: title, description, canonical, Open Graph, and robots defaults.
- Add JSON-LD where truthful:
  - `WebSite`
  - `Service`
  - `FAQPage`
  - `LocalBusiness` only when the lead-gen brand has truthful NAP/contact details to publish.
- Add `sitemap.xml` support before launch.

Required env template values per site:

```bash
PUBLIC_SITE_NAME=
PUBLIC_SITE_URL=
PUBLIC_PRIMARY_PHONE=
PUBLIC_PRIMARY_PHONE_TEL=
PUBLIC_TALLY_FORM_ID=
OWNER_EMAIL=george@laineconsultancy.com
RENTER_EMAIL=
RENTER_FORWARDING_PHONE=
TWILIO_PHONE_NUMBER=
```

## Design Direction

Rank-and-rent sites should feel like practical local service sites, not speculative startups.

- First viewport must signal service + location + call action.
- Use domain-relevant imagery or generated assets; avoid vague stock atmospheres.
- Prioritize scan speed, trust, and contact paths.
- Keep design distinctive but restrained. A small local service site should not look like a SaaS landing page.
- Test long business names, phone numbers, service names, and nearby-location names on mobile.

## Build Workflow

1. **Brief**
   - Create or update `spec/niche-brief.md`.
   - Confirm keyword, service, location, domain, lead routing, and launch assumptions.

2. **Research**
   - Run SERP and backlink/citation checks.
   - Create keyword map and content plan.
   - Decide whether pages beyond homepage/contact/legal are justified.

3. **Content**
   - Write page copy before coding.
   - Keep all launch copy free of placeholders and fake proof.

4. **Astro Build**
   - Scaffold or update the Astro project.
   - Implement real content, forms/CTAs, metadata, schema, sitemap, and legal pages.

5. **Verification**
   - Start dev server before frontend edits.
   - Use browser automation to screenshot 375px, 768px, and 1440px.
   - Check console and failed network requests.
   - Run accessibility checks, including axe where possible.
   - Run production build and verify production rendering.

6. **Handoff**
   - Summarize pages built, keyword targets, lead routing status, backlink opportunities, and remaining launch blockers.

## Completion Criteria

Do not call a site complete until:

- Primary keyword intent is clearly targeted.
- Top competitor/backlink notes exist.
- No placeholder launch copy remains.
- Phone/form CTAs are wired or explicitly marked as awaiting real routing.
- Metadata, schema, sitemap, privacy policy, and terms exist.
- Dev and production builds pass.
- Mobile, tablet, and desktop screenshots are clean.
- Console/network/accessibility checks have no blocking issues.
