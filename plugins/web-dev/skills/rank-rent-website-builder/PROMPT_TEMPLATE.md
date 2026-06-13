# Rank & Rent Website Builder Prompt

Use this prompt when running a long autonomous build.

```text
Use the rank-rent-website-builder skill.

Build an Astro rank-and-rent lead-generation website for:

Primary keyword: [service location]
Service: [service]
Location: [location]
Domain: [domain or To be confirmed]

Follow the repo `AGENTS.md` instructions and enforce all frontend quality gates.

Required workflow:
1. Create/update `spec/niche-brief.md`.
2. Research the SERP for the primary keyword.
3. Identify the top 3 real competitor sites.
4. Pull lightweight backlink/citation opportunities for those competitors using available tools.
5. Create `spec/serp-competitors.md`, `spec/backlink-opportunities.csv`, `spec/keyword-map.md`, `spec/content-plan.md`, and `spec/lead-routing.md`.
6. Build the Astro site with real launch copy, metadata, schema, sitemap, contact page, privacy policy, and terms.
7. Verify dev and production builds at 375px, 768px, and 1440px with browser screenshots, console/network checks, and accessibility checks.

Do not fabricate reviews, accreditations, addresses, business history, or named staff.
```
