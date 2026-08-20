# Sitemap Output Template

Use this format when documenting a local business site architecture.

## [Business Name] Sitemap

### Entity Consistency Sheet (fill first — everything below must match it)

| Field | Canonical value |
|-------|-----------------|
| Business name | [exact, character for character] |
| Address | [as on GBP] |
| Phone | [as on GBP] |
| Services terminology | [same service names used on site, GBP services list, schema, directories] |
| GBP link target | [strong service or location page, NOT the homepage] + UTM parameters |

### Homepage
`/` - [Business Name] | [Primary Service] in [Region]

---

### Tier 1: Core Service Pages (Pillar Content) — one per service, always

```
/[service-1]/
/[service-2]/
/[service-3]/
```

---

### Tier 2: Location Hub Pages — Primary tier only, cap 3-6, proof required

| URL | Proof (reviews / jobs / photos from this town) |
|-----|------------------------------------------------|
| `/[location-1]/` | [evidence] |
| `/[location-2]/` | [evidence] |

---

### Tier 3: Service + Location Matrix — only combos with real proof

| URL | Proof for this exact combo |
|-----|----------------------------|
| `/[location-1]/[service-1]/` | [evidence] |

---

### Supporting Pages

```
/about/
/contact/
/areas-we-cover/   ← every served town without its own page, named and linked
/reviews/
/blog/
```

---

## Page Count Summary

| Category | Pages | Justification |
|----------|-------|---------------|
| Homepage | 1 | |
| Core Service Pillars | X | one per service |
| Location Hubs | X (max 6) | proof listed above |
| Service + Location (matrix) | X | proof listed above |
| Supporting Pages | X | |
| **Total** | **X** | |

---

## Internal Linking Strategy

### Homepage links to:
- All service pillar pages (primary navigation)
- All location hub pages (primary navigation)
- Contact, About (footer)

### Service Pillar pages link to:
- Location-specific versions of that service (where they exist)
- Related service pages

### Location Hub pages link to:
- All service+location pages for that area
- Nearby location hubs

### Service+Location pages link to:
- Parent service pillar page
- Parent location hub page
- Same service in adjacent locations
- Related services in same location

---

## Per-Page Requirements Checklist

For each location and matrix page:

**Differentiation (~50% locally unique; passes the removed-city-name test), at least 3 of:**
- [ ] Local testimonial from that town, quoted with context
- [ ] Photo of job completed in that area
- [ ] Housing stock context specific to area
- [ ] Local data (water hardness, common boiler types, council schemes)
- [ ] Response time from business base
- [ ] Area-specific FAQs in conversational language
- [ ] Local landmark references

**E-E-A-T block (required):**
- [ ] Named person with real credential (e.g. Gas Safe number, visible and linked)
- [ ] Original photo (never stock)
- [ ] Specific testimonial (named town, named job)

**Schema:**
- [ ] LocalBusiness subtype with NAP matching GBP exactly (location pages)
- [ ] Service schema (service pages)
- [ ] FAQPage where genuine FAQs exist
- [ ] `sameAs` on homepage LocalBusiness (GBP, socials, key directories)

**Launch:**
- [ ] Bing Places claimed, IndexNow enabled
- [ ] GBP link → chosen non-homepage page, UTM tagged
- [ ] LCP < 2.5s, INP < 300ms (p75 field data)
- [ ] Crawlable text NAP in footer
