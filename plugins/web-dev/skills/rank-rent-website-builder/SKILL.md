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
- Keep the **location** footprint tight by default. Use service x location matrix mode only with SERP, volume, and unique-content justification. The cap is on locations, not on the site: target **15+ genuinely distinct service intents** before considering any location expansion.
- New builds must clear the workspace niche gate in `AGENTS.md`: a **£1,500 minimum average job value**, a trade that genuinely travels 20-30 miles, and a place in a regional cluster. Do not scaffold a site in a sub-floor niche.
- Use placeholders only where clearly marked in internal specs, never as launch copy.
- For every public site, enforce the repo quality gates in `AGENTS.md`: dev server, browser screenshots, mobile/tablet/desktop, console/network checks, accessibility, production build.

## Cluster Model

New sites are built as part of a regional cluster, not as standalone assets. **A cluster is one
niche, one anchor city, and a set of satellite towns**, all within reach of a single vetted renter
with a 20-30 mile radius. The point is to scale one renter relationship rather than multiply
outreach. There is no target site count; growth is measured in clusters reaching renter-signed
status.

- The **anchor** is the first build and the cluster's centre of gravity, but it is **not a gate**.
  Build satellites out around it as capacity allows, without waiting for the anchor to rank.
  Satellite SERPs are weaker, so satellites often rank and produce leads sooner, and aggregate lead
  flow across the cluster is what signs a renter.
- The anchor is whichever town offers the best combination of demand and winnability, not the
  largest. Anchors need 80,000+ population and 10+ map-pack operators; satellites need 25,000+ and
  5+.
- Confirm a suitable renter **exists** before the first site goes up. A signed renter is not
  required, but a region with no contractor whose radius covers the cluster cannot host one.
- **Duplicate content control is the central technical risk and it is stricter here, not looser.**
  Building several sites in one niche concurrently raises cross-site duplication risk. Run
  `sibling-uniqueness-audit` before every satellite launch, write each satellite independently, never
  town-swap a source document, make H2/H3 outlines genuinely differ between towns, and never
  interlink cluster sites. Vary the design treatment rather than shipping visually identical
  properties.
- The same local operators see every site in a regional cluster, unlike a dispersed portfolio.
  Genuinely differentiated content and truthful trust claims are the only mitigation.

## Inputs

Collect or infer these before building:

- Primary keyword: e.g. `mobile mechanic Colchester`, `private physiotherapist Bath`, or `emergency locksmith York`
- Main service: e.g. `mobile mechanic`, `private physiotherapist`, or `emergency locksmith`
- Microvertical: e.g. `emergency mobile mechanics`, `sports injury physiotherapy`, or `lockouts`
- Location: e.g. `Colchester`
- Domain: exact/partial match if known
- Cluster ID, and whether this site is the cluster's anchor or a satellite
- Trade service radius in miles, evidenced from operator service-area pages
- Map-pack strength and organic opportunity
- Map-pack operator count: 10+ for an anchor, 5+ for a satellite
- Top-3 competitor indexed page count, counted from their `sitemap.xml`
- Competitor weakness score, 0-6, from `tools/niche-gate/`
- Volume/difficulty: DataForSEO when available, otherwise tool/source noted. Context only, never a gate
- Average job value, against the £1,500 floor for new builds, and likely lead value
- Close speed: fast, medium, or slow
- Renter supply: a vetted contractor whose radius covers the whole intended cluster
- Defensible rent, calculated by `tools/lead-readiness/lead_value.py`, not estimated
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

2. Niche gate. Cheap disqualifiers run first.

   **Hard floors. Fall below any one of these and the candidate is rejected before any scoring.**

   | Filter | Threshold |
   | --- | --- |
   | Average job value | **£1,500 minimum** |
   | Trade service radius | **Genuinely travels 20-30 miles** |
   | Anchor city population | **80,000+** |
   | Satellite town population | **25,000+** |
   | Map-pack operator count | **10+ in an anchor, 5+ in a satellite** |
   | Renter supply | **A vetted contractor whose radius covers the whole intended cluster** |

   The £1,500 floor is a settled decision about deal quality and renter economics: at £120 x 30%
   close x 10% commission the lead is worth £3.60, so a £400/month rent would need ~111 leads a
   month. Map-pack operator count is the demand proxy and carries the load population used to. It
   must not be relaxed alongside the 80k population floor.

   **Competitor weakness score, 0-6, on the top three to five organic results.** This is the real
   difficulty measure. Use `tools/niche-gate/` for the countable signals. One point each:

   1. Indexed pages <= 15. The strongest signal, and it sets your page target. Count from the
      competitor's `sitemap.xml`, not a `site:` query. No sitemap at all is itself a weakness signal.
   2. No exact or partial match domain in the top five.
   3. H1/H2/H3 structure absent, generic, or not keyword-aligned.
   4. Five or fewer service pages, built for utility rather than search.
   5. Low referring-domain counts.
   6. Directory/aggregator dominance (Checkatrade, Bark, Rated People). A mixed signal in the UK:
      weak local operators, but compressed organic slots. Treat with suspicion.

   **Demoted to supporting evidence, not gates.** Search volume is context only. Zero reported volume
   with a populated map pack is buildable. Keyword difficulty and domain rank are context only.

   **Niche shape.** Prefer obscure sub-niches over broad trades; avoid plumbing, HVAC, and general
   handyman. Avoid high-ticket-but-slow-closing work (kitchen and bathroom remodelling, ADU-type
   construction, driveways and patios) because leads close over months against heavy price-shopping
   and the renter never attributes revenue to you. Record close speed next to the ticket estimate.
   For clusters, radius beats urgency: favour booked, surveyed, or scheduled work. Emergency niches
   can be built, but only as standalone anchor-only sites.

   Record the cluster ID and anchor/satellite role, trade radius, map-pack operator count, top-3
   indexed page count, weakness score, close speed, renter supply status, calculated defensible rent,
   and the monetisation model.

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

Keep the **location** footprint tight. Do not create broad programmatic location pages until the
primary page is strong. Service breadth is the opposite case: it is the mechanism by which a site
outranks local competitors without backlinks, and it is not capped.

Minimum:

- `/` targeting the primary `[service] [location]` keyword
- `/contact/`
- `/privacy-policy/`
- `/terms/`

Service pages:

- **Target 15+ genuinely distinct service intents before considering any location expansion.** A
  distinct intent means a different searcher with a different problem and a different heading
  structure, not a synonym. Build a new page when the two queries are contextually distinct; fold
  them together when they are near-synonyms.
- **Competitor indexed page count is the practical difficulty signal.** If page-one competitors index
  around ten pages, 25-30 well-differentiated pages is a credible route to outranking them without
  backlinks.
- Cloning one page across twenty postcode villages is a doorway matrix and stays banned. Expanding
  service intent is not.

Optional when justified by SERP/content depth:

- `/services/[variant]/` for distinct high-intent service variants
- `/areas/[nearby-location]/` for nearby places with enough real search intent
- `/faqs/` only if FAQ depth would otherwise bloat the homepage

Avoid large service x location matrices for the first build unless research shows real demand and enough unique supportable content. Cap primary location pages at 3-6, and gate every one on genuinely unique local content: it must pass the removed-city-name test (take the town name out; if the page isn't still obviously about that place, it's a doorway page) with roughly 50% of the content genuinely location-specific. Document any matrix decision in `spec/keyword-map.md` and `spec/content-plan.md`. See `~/.claude/skills/references/shared-seo/local-seo-playbook-2026.md` for the reasoning behind this cap.

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
- Enable IndexNow before launch (trivial on Cloudflare: a toggle/API ping) so Bing indexes changes immediately.

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
   - Verify Core Web Vitals pass criteria: LCP under 2.5s and INP under 300ms, both measured at the 75th percentile (PageSpeed Insights field data).
   - Run production build and verify production rendering.

7. **Handoff**
   - Summarize pages built, keyword targets, lead routing status, contractor/renter status, agreement-before-release status, backlink opportunities, and remaining launch blockers.
   - Add the post-launch Google Search Console loop: review position 7-33 doorstep keywords and impression-rich queries, then improve existing pages or add justified support pages.

## Completion Criteria

Do not call a site complete until:

- Primary keyword intent is clearly targeted.
- Niche gate records microvertical, cluster ID and anchor/satellite role, trade radius, map-pack strength and operator count, top-3 competitor indexed page count, competitor weakness score, average job value against the £1,500 floor, close speed, renter supply status, calculated defensible rent, and monetisation model.
- Service breadth is planned to 15+ distinct service intents, and any location expansion is deferred until that floor is met.
- Top competitor/backlink notes exist.
- Matrix mode is either off or justified with SERP/volume/unique-content evidence, with primary location pages capped at 3-6 and each one passing the removed-city-name test (~50% genuinely location-specific content).
- No placeholder launch copy remains.
- No fake NAP, GBP, reviews, accreditations, named providers, staff, LocalBusiness schema, or review schema.
- No owned-site interlink/PBN-style footprint exists.
- Phone/form CTAs are wired or explicitly marked as awaiting real routing.
- Lead qualification fields and speed-to-lead target are documented.
- Contractor/renter status, agreement-before-release status, and intro offer status are documented.
- Metadata, schema, sitemap, privacy policy, and terms exist.
- IndexNow is enabled.
- Core Web Vitals pass criteria are met: LCP under 2.5s, INP under 300ms, at p75.
- `impeccable` frontend design guidance has been applied during shaping, implementation, and polish.
- Visual direction is niche-specific, production-grade, and not a generic local-service template.
- Typography, spacing, imagery, accessible contrast, mobile-first layout, and CTA hierarchy are verified.
- Any generated images have passed visual QC, are saved inside the site workspace, are documented with path/tool/prompt/QC status, and do not look AI-generated or misleading.
- Realistic long site names, phone numbers, service names, location strings, and nearby-area names have been tested at 375px, 768px, and 1440px.
- Post-launch GSC doorstep keyword loop is documented.
- Dev and production builds pass.
- Mobile, tablet, and desktop screenshots are clean.
- Console/network/accessibility checks have no blocking issues.
