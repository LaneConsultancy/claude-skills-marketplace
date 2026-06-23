---
name: rank-rent-website-builder
description: Build Astro rank-and-rent lead-generation websites around one main service + location keyword and close variants. Use for rank-and-rent niche sites, exact/partial-match domains, SERP competitor checks, lightweight backlink/citation research, local SEO architecture, lead capture, and launch quality gates.
---

# Rank & Rent Website Builder

Use this skill instead of the generic website-builder when the site is a rank-and-rent asset, not a website for an existing real business.

The goal is a focused local lead-generation site that can rank for a single service + location niche, capture calls/forms, and later rent leads to an operator. Default stack is Astro on Vercel; Cloudflare Pages is an optional static-hosting path for scale when the site does not need server routes.

## Core Rules

- Build around one primary keyword: `[service] [location]`.
- Use close variants only when they support the primary intent.
- Default framework: Astro. Do not switch stacks unless the user explicitly asks.
- Conversion comes first: visible phone CTA, short enquiry form, urgent/local intent above the fold.
- SEO, conversion, and design quality must work together: SERP reality, page intent, keyword map, schema, internal links, fast static pages, and production-grade frontend craft.
- Be truthful. Do not invent NAP, addresses, GBP, reviews, accreditations, business history, named technicians, staff, operators, clinicians, tradespeople, specialists, providers, years trading, certifications, or memberships.
- Do not use review schema unless reviews are real; use LocalBusiness schema only with truthful, publishable NAP/contact details.
- Do not interlink owned rank-and-rent sites or link them back to the agency/main domain as an owned network footprint.
- Default to a tight v1 site. Use service x location matrix mode only with SERP, volume, and unique-content justification.
- Use placeholders only where clearly marked in internal specs, never as launch copy.
- For every public site, enforce the repo quality gates in `AGENTS.md`: dev server, browser screenshots, mobile/tablet/desktop, console/network checks, accessibility, production build.

## Inputs

Collect or infer these before building:

- Primary keyword: e.g. `mobile mechanic Colchester`, `private physiotherapist Bath`, or `emergency locksmith York`
- Main service: e.g. `mobile mechanic`, `private physiotherapist`, or `emergency locksmith`
- Microvertical: e.g. `emergency mobile mechanics`, `sports injury physiotherapy`, or `lockouts`
- Location: e.g. `Colchester`
- Domain: exact/partial match if known
- Map-pack strength and organic opportunity
- Volume/difficulty: DataForSEO when available, otherwise tool/source noted
- Average job value and likely lead value
- Monetisation model: exclusive rental, per-lead, rev share, first-lead-free intro, or test-only
- Phone routing: Twilio number or temporary CTA state
- Form routing: custom Astro form or Tally
- Owner lead recipient: default `george@laneconsultancy.com`
- Contractor/renter status, including agreement-before-release status
- First-lead-free or intro offer status, if applicable
- Lead qualification fields and speed-to-lead target
- Renter details and routing destination: blank until a renter exists
- Nearby areas worth targeting, if genuinely supportable

If missing, create a brief with sensible defaults and mark unknown operational values as `To be confirmed`.

## Required Research

Before writing copy or code, create `spec/` research files.

1. Read the root strategy sources:
   - `../AGENTS.md` or root `AGENTS.md`
   - `Rank-and-Rent Local SEO for Generic Local Sites in 2026.pdf`
   - `rank-and-rent-playbook.pdf`
   - the relevant spreadsheet row, if available

2. Niche gate:
   - Record microvertical, map-pack strength, volume/difficulty, average job value, and monetisation model.
   - Record contractor/renter status, agreement status, intro offer status, and speed-to-lead requirements.

3. SERP check for the primary keyword:
   - Identify top organic competitors for the exact keyword.
   - Separate real service providers from directories, map packs, lead-gen sites, and national brands.
   - Record page type, title, content depth, backlink/citation clues, GBP/local strength, and obvious weaknesses.
   - Record whether matrix expansion is justified or should stay off.

4. Lightweight backlink/citation pass:
   - For the top 3 real competitors, use Apify/DataForSEO/SeoMCP when available to find referring domains or source URLs.
   - Use Open PageRank to score competitor and linking domains when `OPENPAGERANK_API_KEY` exists.
   - Use Common Crawl only for validation or deeper inspection, not as the default backlink source.
   - Classify opportunities as `directory`, `citation`, `local press`, `supplier`, `association`, `blog`, `spam`, or `unknown`.
   - Exclude owned-site interlinks, agency-domain links, and PBN-style footprint links.

5. Create these files:
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

Avoid large service x location matrices for the first build unless research shows real demand and enough unique supportable content. Document any matrix decision in `spec/keyword-map.md` and `spec/content-plan.md`.

## Content Standards

Write conversion-first local SEO copy:

- Hero: service + location obvious in the H1 or immediate supporting line.
- Above fold: phone CTA, form CTA, service area, fast reassurance.
- Sections: emergency/routine intent, services handled, how it works, service area, FAQs, trust/verification language, final CTA.
- Use realistic local language without pretending to have a physical office or named technicians, staff, operators, clinicians, tradespeople, specialists, or providers unless true.
- Include variant phrases naturally based on the niche, such as `emergency`, `same-day`, `at home`, `near me`, `diagnostics`, `repair`, `consultation`, `installation`, `maintenance`, and service/product variants where relevant.
- FAQs should answer buying-intent questions, not generic filler.
- Never claim guaranteed rankings, fake reviews, fake local address, fake GBP, fake named providers, fake staff, or fake memberships.
- Use transparent lead-gen wording until a real contractor/renter relationship exists.

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
  - Review/testimonial schema only when the reviews/testimonials are real and attributable.
- Add `sitemap.xml` support before launch.

Required env template values per site:

```bash
PUBLIC_SITE_NAME=
PUBLIC_SITE_URL=
PUBLIC_PRIMARY_PHONE=
PUBLIC_PRIMARY_PHONE_TEL=
PUBLIC_TALLY_FORM_ID=
OWNER_EMAIL=george@laneconsultancy.com
RENTER_EMAIL=
RENTER_FORWARDING_PHONE=
TWILIO_PHONE_NUMBER=
```

## Frontend Design Standard

New public-facing rank-and-rent sites must use the `impeccable` design skill/guidance during frontend shaping, implementation, and polish. Treat frontend craft as part of conversion and SEO quality, not afterthought polish.

- Produce production-grade, visually distinctive frontend work; avoid template-looking local-service pages.
- Choose the design direction from the niche, audience, physical service context, and search intent, not from category reflex.
- Use strong typography, spacing rhythm, image/art direction, accessible contrast, mobile-first layout, and deliberate CTA hierarchy.
- Use real, licensed, domain-relevant imagery or good generated imagery where appropriate; avoid decorative empty panels and vague stock atmospheres.
- Avoid AI-looking defaults: repeated card grids, tiny uppercase eyebrows on every section, beige/cream monoculture, generic stock atmospheres, gradient text, default glassmorphism, overflow, and weak contrast.
- First viewport must signal service + location + call action without making the page generic.
- Test mobile, tablet, and desktop with realistic long site names, phone numbers, service names, location strings, and nearby-area names.
- Keep conversion and local SEO strong throughout; design choices must make trust, clarity, and contact paths stronger.

## Image Asset Generation

When a rank-and-rent site needs generated raster imagery, the builder may invoke `imagegen` and/or `generate-image` according to the active runtime/tool availability and each image skill's own workflow. Use generated images only when they can support trust, clarity, conversion, and the niche-specific design direction.

- Generate or select domain-relevant assets: hero images, service imagery, textures, illustrations, or cutouts must support the specific service, location intent, audience, and conversion path.
- Do not use vague generic stock atmospheres, decorative empty panels, fake local scenes, fake staff/operators/providers, fake proof, fake reviews, fake NAP, fake logos, or misleading evidence of local presence.
- Prompts must include production constraints: no AI-looking artifacts, no garbled text/words/logos unless exact text is intentionally added later, realistic physical details for tools/equipment/people/places, truthful local context, accurate scale, and consistent lighting/shadows.
- For people, vehicles, tools, equipment, premises, technical scenes, or location cues, make physical details plausible enough that a trade professional, service provider, or client would not spot them as fake.
- Inspect each saved output visually with `view_image` or an equivalent image viewer when available before accepting it.
- Reject and regenerate images with weird artifacts, distorted anatomy/hands/faces, impossible tools/equipment/connections, phantom objects, garbled text, over-smooth/plastic skin, inconsistent lighting/shadows, broken scale, generic AI gloss, or anything a trade/professional/client would spot as fake.
- Save accepted project-bound images into the site workspace, such as `public/images/` or the appropriate Astro asset path. Never leave project-referenced assets only in a generated, temp, default tool, or external cache folder.
- Verify final accepted images inside the actual page/browser at 375px, 768px, and 1440px as part of visual QA, including crop, focal point, contrast with overlaid content, file loading, and performance.
- Record the final image path, generation skill/tool, prompt or source summary, and QC status in `spec/build-state.md` or a dedicated image asset note.
- If generated imagery still fails QC after reasonable attempts, switch to licensed stock, real photography, a simpler illustration/vector/code-native asset, or no image rather than shipping a bad AI-looking asset.

## Build Workflow

1. **Brief**
   - Create or update `spec/niche-brief.md`.
   - Confirm keyword, microvertical, service, location, domain, lead routing, monetisation model, contractor/renter status, and launch assumptions.

2. **Research**
   - Run SERP and backlink/citation checks.
   - Create keyword map and content plan.
   - Decide whether pages beyond homepage/contact/legal are justified.
   - Document matrix mode as `off` by default or justify it with SERP, volume, and unique-content evidence.

3. **Content**
   - Write page copy before coding.
   - Keep all launch copy free of placeholders and fake proof.

4. **Frontend Shaping**
   - Apply `impeccable` design guidance before coding public UI.
   - Define the niche-specific design direction, image/art direction, typography/spacing rhythm, CTA hierarchy, and mobile-first layout approach.
   - Decide whether imagery will be real/licensed, generated, illustrated/vector/code-native, or omitted; document the asset plan and truth constraints.
   - Reject template-looking or AI-default patterns before implementation.

5. **Astro Build**
   - Scaffold or update the Astro project.
   - Implement real content, forms/CTAs, metadata, schema, sitemap, and legal pages.
   - Keep owned-site interlinks and agency-network links out of launch pages.
   - Carry the `impeccable` design direction through components, spacing, imagery, contrast, and responsive states.
   - If generated images are used, save accepted project-bound assets into the site workspace and record image path, generation skill/tool, prompt or source summary, and QC status.

6. **Verification**
   - Start dev server before frontend edits.
   - Use browser automation to screenshot 375px, 768px, and 1440px.
   - Check console and failed network requests.
   - Run accessibility checks, including axe where possible.
   - If generated images are used, visually inspect saved outputs before acceptance, reject AI-looking or physically implausible images, and verify the accepted assets in the actual browser page at mobile/tablet/desktop.
   - Verify the frontend design standard: distinctive niche fit, strong typography/spacing, domain-relevant imagery, accessible contrast, deliberate CTA hierarchy, and no template/AI-default patterns.
   - Check realistic long site names, phone numbers, service names, location strings, and nearby-area names at each viewport.
   - Run production build and verify production rendering.

7. **Handoff**
   - Summarize pages built, keyword targets, lead routing status, contractor/renter status, agreement-before-release status, backlink opportunities, and remaining launch blockers.
   - Add the post-launch Google Search Console loop: review position 7-33 doorstep keywords and impression-rich queries, then improve existing pages or add justified support pages.

## Completion Criteria

Do not call a site complete until:

- Primary keyword intent is clearly targeted.
- Niche gate records microvertical, map-pack strength, volume/difficulty, average job value, and monetisation model.
- Top competitor/backlink notes exist.
- Matrix mode is either off or justified with SERP/volume/unique-content evidence.
- No placeholder launch copy remains.
- No fake NAP, GBP, reviews, accreditations, named providers, staff, LocalBusiness schema, or review schema.
- No owned-site interlink/PBN-style footprint exists.
- Phone/form CTAs are wired or explicitly marked as awaiting real routing.
- Lead qualification fields and speed-to-lead target are documented.
- Contractor/renter status, agreement-before-release status, and intro offer status are documented.
- Metadata, schema, sitemap, privacy policy, and terms exist.
- `impeccable` frontend design guidance has been applied during shaping, implementation, and polish.
- Visual direction is niche-specific, production-grade, and not a generic local-service template.
- Typography, spacing, imagery, accessible contrast, mobile-first layout, and CTA hierarchy are verified.
- Any generated images have passed visual QC, are saved inside the site workspace, are documented with path/tool/prompt/QC status, and do not look AI-generated or misleading.
- Realistic long site names, phone numbers, service names, location strings, and nearby-area names have been tested at 375px, 768px, and 1440px.
- Post-launch GSC doorstep keyword loop is documented.
- Dev and production builds pass.
- Mobile, tablet, and desktop screenshots are clean.
- Console/network/accessibility checks have no blocking issues.
