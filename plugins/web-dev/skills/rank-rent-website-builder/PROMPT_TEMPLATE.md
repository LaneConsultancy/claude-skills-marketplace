# Rank & Rent Website Builder Prompt

Use this prompt when running a long autonomous build.

```text
Use the rank-rent-website-builder skill.

Build an Astro rank-and-rent lead-generation website for:

Primary keyword: [service location]
Service: [service]
Microvertical: [microvertical]
Location: [location]
Domain: [domain or To be confirmed]
Monetisation model: [exclusive rental / per-lead / rev share / intro offer / test-only / To be confirmed]
Average job value: [value or To be confirmed]
Contractor/renter status: [none / prospecting / agreed / To be confirmed]

Follow the repo `AGENTS.md` instructions, enforce all frontend quality gates, and apply the `impeccable` frontend design guidance to public UI.

Required workflow:
1. Create/update `spec/niche-brief.md`.
2. Record the niche gate: microvertical, map-pack strength, DataForSEO volume/difficulty when available, average job value, monetisation model, and contractor/renter status.
3. Research the SERP for the primary keyword.
4. Identify the top 3 real competitor sites.
5. Pull lightweight backlink/citation opportunities for those competitors using available tools.
6. Create `spec/serp-competitors.md`, `spec/backlink-opportunities.csv`, `spec/keyword-map.md`, `spec/content-plan.md`, and `spec/lead-routing.md`.
7. Keep matrix mode off unless SERP, volume, and unique-content evidence justify service x location expansion.
8. Apply `impeccable` frontend design guidance: choose a niche-specific visual direction, avoid template/AI-default patterns, and verify typography, spacing, imagery, contrast, mobile layout, CTA hierarchy, and realistic long strings.
9. If generated raster imagery is needed, use `imagegen` and/or `generate-image` according to active runtime/tool availability and each skill's own workflow. Prompt for domain-relevant, production-grade assets with no AI-looking artifacts, no garbled text/logos, realistic physical details, truthful local context, and no fake staff/operators/proof. Visually inspect saved outputs with `view_image` or equivalent, reject/regenerate anything fake-looking or physically implausible, save accepted project-bound files into the site workspace, and document path, tool, prompt/source, and QC status in `spec/build-state.md` or an image asset note. If QC fails after reasonable attempts, use licensed stock, real photography, simpler illustration/vector/code-native assets, or no image instead.
10. Build the Astro site with real launch copy, metadata, truthful schema, sitemap, contact page, privacy policy, and terms.
11. Document lead qualification, speed-to-lead, agreement-before-release status, intro offer status, image asset/QC status where relevant, and post-launch GSC position 7-33 doorstep keyword loop.
12. Verify dev and production builds at 375px, 768px, and 1440px with browser screenshots, console/network checks, accessibility checks, generated-image browser checks where relevant, and the frontend design standard.

Do not fabricate NAP, GBP, reviews, accreditations, addresses, business history, named technicians, staff, operators, clinicians, tradespeople, specialists, or providers. Do not use review schema unless reviews are real. Do not use LocalBusiness schema unless truthful publishable NAP/contact details exist. Do not interlink owned rank-and-rent sites or link them to the agency/main domain as a network footprint.
```
