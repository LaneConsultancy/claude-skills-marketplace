# Local Schema Types (2026)

LocalBusiness subtypes by industry, required/recommended properties, `sameAs` and NAP rules, multi-location and SAB patterns.

Source of truth: `~/.claude/skills/references/shared-seo/local-seo-playbook-2026.md` (Part 2, schema and entity consistency).

---

## Core Rules

- **Use the specific subtype, never generic `LocalBusiness`** where a subtype exists (see table below). The subtype is an entity classification signal.
- **NAP character-identical to the GBP.** Name, address, and phone in schema must match the Google Business Profile exactly, character for character. Google validates markup against visible content and external sources; inconsistency is a demotion signal.
- **`sameAs` is not optional.** It is how you explicitly tell Google that your GBP, social profiles, and key directory listings are all the same entity. Include: GBP (Maps place URL), primary social profiles, and the key niche/country directory listings (for UK trades: Checkatrade, Trustpilot, Yell, Gas Safe register).
- Schema confirms an entity Google already recognises; it does not create recognition from nothing. Consistency does that.

---

## LocalBusiness Subtypes by Industry

| Vertical | Correct subtype | Do NOT use |
|----------|-----------------|------------|
| Restaurant | `Restaurant` | generic `LocalBusiness` |
| Legal | `LegalService` (+ `Attorney` as a `Person`) | deprecated `Attorney` as the business type |
| Automotive dealer | `AutoDealer` | deprecated `VehicleListing` as the business |
| Healthcare | `MedicalClinic` / `Hospital` / `Dentist` / `Physician` | generic `MedicalBusiness` |
| Home services -- plumbing | `Plumber` | generic `LocalBusiness` |
| Home services -- HVAC/heating | `HVACBusiness` | generic `LocalBusiness` |
| Home services -- electrical | `Electrician` | generic `LocalBusiness` |
| Real estate | `RealEstateAgent` | generic `LocalBusiness` |

If no specific subtype exists for the trade, use `LocalBusiness` -- but check Schema.org first; most trades have a dedicated type.

---

## Required and Recommended Properties

**Required:**
- `name`
- `address` (with `PostalAddress` sub-properties: `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`)

**Recommended:**
- `geo` (`GeoCoordinates`, minimum 5 decimal places)
- `openingHoursSpecification`
- `telephone`
- `url`
- `priceRange` (under 100 characters)
- `image`
- `aggregateRating` / `review` (only where reviews are legitimately displayed on the page)
- **`sameAs`** (GBP, social profiles, key directory listings -- see Core Rules)

---

## Page-Type Schema Map

| Page | Schema |
|------|--------|
| Homepage | LocalBusiness (specific subtype) with NAP matching GBP + `sameAs` array + Organization |
| Location pages | LocalBusiness (subtype) with NAP matching GBP, unique `@id`, `geo` |
| Service pages | `Service` |
| Pages with genuine FAQs | `FAQPage` |
| Pages legitimately displaying reviews | `Review` / `AggregateRating` |

---

## Multi-Location Pattern

- Each location page has its own `LocalBusiness` node with a **unique `@id`**.
- Each location links to the parent Organization via **`branchOf`**.
- The homepage carries the parent `Organization` (or the head-office `LocalBusiness`).
- NAP per location must match that location's GBP listing exactly.

---

## Service Area Business (SAB) Pattern

- Use `areaServed` with **named cities, postal/ZIP codes, or neighbourhoods** -- not entire states or countries (June 2025 Google SAB guideline).
- SABs may omit `address.streetAddress` if the address is not public, but still declare `areaServed` and the geographic centre.
- `areaServed` is Schema.org-supported and recommended even though it is not in Google's official required list.

---

## Industry-Specific Schema Patterns

| Vertical | Pattern |
|----------|---------|
| Restaurant | `Menu` + `MenuSection` + `MenuItem` + `ReserveAction` |
| Healthcare | `Physician` (`Person`) + `MedicalSpecialty` + `sameAs` to NPI |
| Legal | `LegalService` + `Person` (attorney) + `Service` (practice areas) |
| Home Services | subtype (`Plumber` / `HVACBusiness` / `Electrician`) + `areaServed` + `Service` |
| Real Estate | `RealEstateAgent` + `Person` + `RealEstateListing` |
| Automotive | `AutoDealer` + `Car` + `Offer` (separate department schemas) |
