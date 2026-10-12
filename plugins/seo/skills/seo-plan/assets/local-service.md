<!-- Updated: 2026-07-06 -->
# Local Service Business SEO Strategy Template

Source of truth: `~/.claude/skills/references/shared-seo/local-seo-playbook-2026.md` (Whitespark 2026, Sterling Sky controlled testing, December 2025 core update analysis). Read it for the evidence behind these rules.

## Industry Characteristics

- Geographic-focused searches
- High intent, quick decision making
- Reviews heavily influence decisions
- Phone calls are primary conversion
- Mobile-first user behavior
- Emergency/urgent service needs

## 2026 Ranking Weights and Non-Factors

Where the controllable effort actually pays off (Whitespark 2026 local pack / Maps weighting):

| Signal category | Weight |
|-----------------|--------|
| GBP signals | 32% (largest controllable category) |
| Review signals | 20% (up from 16% in 2023) |
| On-page signals | 15-19% |
| Behavioural signals | ~9% (rising) |
| Link signals | ~8% |
| Citation signals | ~6% (rising, driven by AI) |
| Social signals | ~5% |

Proximity to the searcher is the single biggest factor overall (roughly **55%** of the decision) and is **uncontrollable** -- everything above is about maximising the controllable share.

**Confirmed non-factors -- stop spending time here:**

- **GBP posts** for ranking (Sterling Sky: zero movement across 441 keywords, 9 weeks -- engagement/CTR only)
- **The business description** (Google confirmed not used in ranking -- write it for customers)
- **Service-area settings** for a business with a listed address (Whitespark controlled test: no effect -- you rank from your verified address)
- **Keywords in review text** (Sterling Sky: no pack ranking impact -- still matter for AI surfacing and conversion)
- **Geotagged photos** (Google strips EXIF on upload -- the photos matter as content and E-E-A-T, not coordinates)

## Recommended Site Architecture

Hub-and-spoke, aligned with the canonical `local-seo-site-architecture` skill. Service pillars live at the root (one dedicated page per service is the #1 local organic ranking factor), location hubs live at the root, and service+location matrix pages are built **only** where you have real proof for that exact combination (jobs, reviews, and photos from that town for that service).

```
/
├── Home
├── /boiler-repairs/            ← service pillar (one per service, at root)
├── /boiler-servicing/
├── /[service]/                 ← ...one per service, always
├── /dartford/                  ← location hub (Primary tier only, proof-gated)
│   └── /dartford/boiler-repairs/  ← matrix page (ONLY with proof for this combo)
├── /gravesend/
├── /areas-we-cover/            ← every other served area, named not given a URL
├── /about
├── /reviews
├── /gallery (or /portfolio)
├── /blog
├── /contact
├── /emergency (if applicable)
└── /faq
```

Do **not** use a `/locations/{city}/{service}-{city}` pattern or a flat service directory. Service pillars sit at the root (`/[service]/`); location hubs sit at the root (`/[town]/`); matrix pages are location-first (`/[town]/[service]/`) and restricted. Everything else is named on `/areas-we-cover/`, not given its own URL.

## Quality Gates

### Location Page Limits

**Trades / local-service rule (apply this first).** For most trades, cap **primary location pages at 3-6**, gated on proof: you need reviews, completed jobs, and photos from that specific town before a town earns its own page. Two or three strong, evidenced city pages outperform fifteen templated ones, and templated location networks now actively hurt (doorway filtering, sitewide quality assessment, 60-80% traffic losses from March 2024 core update onward). Everything else is named on an "Areas We Cover" page, not given a URL.

**The removed-city-name test:** take the town name out of the page. Is it still obviously about that place? If not, it's a doorway page regardless of intent.

The generic gates below are an outer backstop, not a target -- most trades sites should be nowhere near them:
- ⚠️ **WARNING** at 30+ location pages
- 🛑 **HARD STOP** at 50+ location pages

### Unique Content Requirements

Benchmark: **roughly 50% genuinely locally-unique content minimum** for any location page (BrightLocal working benchmark). Content that survives the removed-city-name test.

| Page Type | Min Words | Locally-Unique % |
|-----------|-----------|------------------|
| Primary Location | 600 | ~50%+ |
| Service Area | 500 | ~50%+ |
| Service Page | 800 | 100% |

### What Makes Location Pages Unique
- Local landmarks and neighborhoods
- Specific services offered at that location
- Local team members
- Location-specific testimonials
- Community involvement
- Local regulations or considerations

## Schema Recommendations

| Page Type | Schema Types |
|-----------|-------------|
| Homepage | LocalBusiness, Organization, + `sameAs` array (GBP, social profiles, key directory listings) |
| Service Pages | Service, LocalBusiness |
| Location Pages | LocalBusiness (with geo) |
| Pages with genuine FAQs | FAQPage |
| Contact | ContactPage, LocalBusiness |
| Reviews | LocalBusiness (with AggregateRating) |

Use the **specific LocalBusiness subtype** for the trade (e.g. `Plumber`, `HVACBusiness`, `Electrician`), not the generic `LocalBusiness`. NAP (name, address, phone) in schema must be **character-identical to the GBP**. The `sameAs` property is how you explicitly tell Google that your GBP, social profiles, and directory listings are all the same entity.

### LocalBusiness Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "openingHours": "Mo-Fr 08:00-18:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "40.7128",
    "longitude": "-74.0060"
  },
  "areaServed": ["City 1", "City 2"],
  "priceRange": "$$"
}
```

## Google Business Profile Integration

- Ensure NAP consistency (Name, Address, Phone) -- character-identical across site schema, GBP, Bing Places, Apple Maps, and core directories
- Sync service categories; use Google's predefined services, then custom services
- **Website link (Diversity Update rule):** point the GBP website link at a **strong service or location page, not the homepage** if the homepage already ranks organically for your money terms. When a URL ranks in the local pack, Google may suppress that same URL from page-one organic (Sterling Sky, page-level demotion). UTM-tag the link so GBP traffic is measurable in analytics.
- **GBP posts have zero measured ranking effect** (Sterling Sky, 441 keywords, 9 weeks). Do them lightly for engagement and click-through only -- they are not a ranking lever.
- Photo uploads (real work, team, premises -- engagement and E-E-A-T evidence, not coordinates)
- Review response strategy (see "Reviews as a system" below)

### Google Business Profile Updates (2025-2026)

- **Video verification** is now standard: postcard verification has been largely phased out. Prepare for a short video verification process showing the business location or service area.
- **WhatsApp integration** replaced Google Business Chat (deprecated). Businesses can connect WhatsApp as their primary messaging channel.
- **Q&A removed from Maps**: replaced by AI-generated answers. Ensure your GBP description, services, and website FAQ are comprehensive, as Google AI uses them to answer queries.
- **Business hours are a top-5 ranking factor**: "Business is open at time of search" ranked as a top individual factor for the first time (Whitespark 2026 Local Search Ranking Factors Report). Keep hours accurate; consider extended hours if feasible.
- **Review "Stories" format**: Google Maps now shows review snippets in a swipeable Stories format on mobile. Encourage detailed, descriptive reviews with photos.

### Service Area Business (SAB) Update (June 2025)

Google updated SAB guidelines to **disallow entire states or countries** as service areas. SABs must specify: cities, postal/ZIP codes, or neighborhoods. If you serve an entire metro area, list the major cities within it rather than the state.

### AI Visibility for Local Businesses

AI Overviews now appear on roughly **68% of local business queries** (Whitespark 2026 testing), rising to **97% for mixed informational/transactional queries** ("best emergency plumber for a burst pipe in Dartford"). AI local packs surface roughly a **third as many businesses** as the traditional 3-pack (Sterling Sky), which makes AI visibility a winner-takes-more game and is why consistent citations and entity data came back into fashion.

Keep perspective, though: Darren Shaw's own caveat in the 2026 report is that AI's impact on local search is still **smaller than the hype suggests**. Google search still dominates local discovery. AI visibility is a layer on top of the fundamentals, not a replacement for them.

To optimize for AI local visibility:
- Ensure presence on expert-curated "best of" lists (ranked #1 AI visibility factor in Whitespark 2026 report)
- Maintain consistent NAP (Name, Address, Phone) across all platforms
- Build genuine review volume and quality
- Use LocalBusiness schema with complete properties (geo, openingHours, priceRange, areaServed)

## Reviews as a System

Reviews are 20% of pack ranking and climbing, plus the dominant conversion factor. Treat review generation as a marketing operation, not a customer-service afterthought.

- **Ask every satisfied customer immediately post-job**, with a direct review link (fewest possible taps). Make it an automation job -- e.g. a ServiceM8 job-completion trigger that fires the review request.
- **Coach the ask.** A review that says "George fixed our burst pipe in Dartford, brilliant service" is worth more than five that say "Great!" AI systems read review text to decide whether you match a query. Don't script customers, but the ask can mention the service and town ("it helps if you say what we did and where").
- **Velocity over volume.** A steady drip (say ~5 a month, forever) beats a large stale total -- review velocity jumped from #93 to #11 in the 2026 survey. Design the system for a steady monthly flow.
- **Respond to everything within 24-48h**, negatives especially. Responses are indexed, so mention the service performed and the town naturally in replies. Businesses responding to 80%+ of reviews see a measurable lift.
- **Diversify.** Reviews on Checkatrade-type industry platforms and Facebook feed the citation and AI-visibility signals, not just Google.

## Links and Citations

Link signals are ~8% of pack weight and matter more for local organic; citations came back into fashion in 2026 because AI answer engines lean heavily on them.

**Tier 1: the entity-verification layer.** GBP, Bing Places, Apple Maps, Facebook, plus the 10-20 directories that matter in your niche and country. For UK trades: Checkatrade, Trustpilot, Yell, the Gas Safe register listing, TrustATrader, the local chamber. Perfect, character-identical NAP. **Ten authoritative citations beat fifty junk ones**; mass directory submission is dead and mildly harmful.

**Tier 2: locally relevant editorial links** (these carry the real ranking weight):

- Sponsorships: junior football kits, charity runs, school fetes, club events -- the link is the byproduct of real participation, which is what makes it safe and valuable
- Local press: pitch genuinely newsworthy things; one local news mention outweighs dozens of directory links
- Trade and industry bodies: Gas Safe, manufacturer accredited-installer pages (Worcester Bosch, Vaillant installer finders are both links and entity confirmation)
- Partnerships with non-competing local businesses (the plumber recommends the electrician, both link)
- Chamber of commerce and business associations, where membership is real

**Tier 3: linkable assets.** One genuinely useful local resource earns links passively (a water-hardness map for North Kent, a "new boiler cost in [region]" data page). Original data is the most reliably linkable format.

**Avoid:** bought links and cheap guest-post networks; the 2026 flood of AI-generated sites built purely to sell links (plausible-looking, worthless); exact-match anchor text campaigns; chasing DR/DA over relevance (a relevant local link from a modest site beats an irrelevant DR70 placement).

## 90-Day Priority Sequence

Highest leverage first. Then maintenance.

**Weeks 1-2: Entity foundation**
1. GBP audit -- primary category, predefined services, hours, photos, no duplicates
2. GBP website link pointed at a strong non-homepage page, UTM tagged
3. LocalBusiness schema (specific subtype) with `sameAs` links, NAP matching GBP exactly
4. Bing Places claimed, IndexNow enabled

**Weeks 3-6: Core pages**
5. One dedicated page per service (the #1 organic factor), written from real experience with real photos
6. Proof-gated location pages only; kill or consolidate any templated ones
7. Homepage clearly stating who, what, where, with credentials visible

**Weeks 7-10: Reviews and Tier 1 citations**
8. Automated post-job review request flow
9. Response process: everything answered within 24-48h
10. Tier 1 citations built/corrected for NAP consistency

**Weeks 11-13: Authority**
11. Two or three local sponsorships or partnerships secured
12. One linkable local asset published
13. One local press angle pitched

Then it's maintenance: the GBP routine, monthly review velocity, one meaningful content or link win per month.

## Content Priorities

### High Priority
1. Homepage with clear service area
2. Core service pages
3. Primary city page
4. Contact page with all locations

### Medium Priority
1. Service + location combination pages
2. FAQ page
3. About/team page
4. Reviews/testimonials page

### Blog Topics
- Seasonal maintenance tips
- How to choose a [service provider]
- Warning signs of [problem]
- DIY vs professional comparisons
- Local regulations and permits

## Key Metrics to Track

- Local pack rankings
- Phone call volume from organic
- Direction requests
- Google Business Profile insights
- Reviews count and rating

## Generative Engine Optimization (GEO) for Local

- [ ] Include clear, quotable service descriptions and pricing ranges
- [ ] Use LocalBusiness schema with complete geo, openingHours, and areaServed
- [ ] Build presence on curated "best of" and local directory lists
- [ ] Maintain consistent NAP across all platforms (Google, Yelp, Apple Maps)
- [ ] Include original photos of work, team, and location
- [ ] Structure FAQ content for common local service questions
- [ ] Monitor AI citation in ChatGPT and Perplexity local recommendations
