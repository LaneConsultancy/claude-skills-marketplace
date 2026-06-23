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

Follow the repo `AGENTS.md` instructions and enforce all frontend quality gates.

Required workflow:
1. Create/update `spec/niche-brief.md`.
2. Record the niche gate: microvertical, map-pack strength, DataForSEO volume/difficulty when available, average job value, monetisation model, and contractor/renter status.
3. Research the SERP for the primary keyword.
4. Identify the top 3 real competitor sites.
5. Pull lightweight backlink/citation opportunities for those competitors using available tools.
6. Create `spec/serp-competitors.md`, `spec/backlink-opportunities.csv`, `spec/keyword-map.md`, `spec/content-plan.md`, and `spec/lead-routing.md`.
7. Keep matrix mode off unless SERP, volume, and unique-content evidence justify service x location expansion.
8. Build the Astro site with real launch copy, metadata, truthful schema, sitemap, contact page, privacy policy, and terms.
9. Document lead qualification, speed-to-lead, agreement-before-release status, intro offer status, and post-launch GSC position 7-33 doorstep keyword loop.
10. Verify dev and production builds at 375px, 768px, and 1440px with browser screenshots, console/network checks, and accessibility checks.

Do not fabricate NAP, GBP, reviews, accreditations, addresses, business history, operators, or named staff. Do not use review schema unless reviews are real. Do not use LocalBusiness schema unless truthful publishable NAP/contact details exist. Do not interlink owned rank-and-rent sites or link them to the agency/main domain as a network footprint.
```
