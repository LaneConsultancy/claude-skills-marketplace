# Local SEO Playbook 2026

**For building and optimising sites for local service businesses**
Compiled July 2026 from Whitespark's 2026 Local Search Ranking Factors report (47 experts, 187 factors, published November 2025), Sterling Sky's controlled testing, Google's December 2025 core update analysis, and current Google spam policy guidance.

---

## Part 1: What actually changed (and what didn't)

### The two beliefs you came in with, corrected

**"I should have been optimising for entities, not keywords."** Half right. Google has been entity-based since Hummingbird (2013), and by now the Knowledge Graph model is the operating reality, not a trend. But entity optimisation doesn't replace keyword-targeted pages. It changes how those pages earn trust. Google evaluates the business as a unified entity across GBP, website, citations, and reviews. A page targeting "boiler repairs Dartford" still works, but it works because the entity behind it (the business) is understood, consistent, and trusted, not because the phrase appears eleven times. The practical shift: stop thinking "which keywords does this page contain" and start thinking "does everything Google can see about this business tell the same story about what it is, where it operates, and what it's good at."

**"Local landing pages don't work anymore."** Wrong, and importantly wrong. The Whitespark 2026 survey puts "dedicated page for each service" as the number one local organic ranking factor, and it's number two for AI search visibility. A city-specific landing page linked from the GBP remains one of the confirmed factors that moves local pack rankings. What died is the templated version: thirty pages with the town name swapped. Google's doorway page policy has been enforced since 2015 and the December 2025 core update raised the quality floor further. Case studies from the March 2024 core update onward show templated location page networks losing 60-80% of traffic. The rule now: fewer pages, each one earning its existence with local proof that can't be copied.

### The updates that matter

**December 2025 core update (11-29 December).** Extended E-E-A-T expectations well beyond YMYL into all competitive queries, including local services. Local sites saw roughly a 31% impact rate. Winners had detailed service descriptions written by people who do the work, staff profiles, original job photos, and specific testimonials. Losers had generic "SEO-optimised" service pages. Core Web Vitals also got heavier weighting: sites with LCP over 3 seconds lost roughly 23% more traffic than faster competitors with equivalent content.

**The "Diversity Update" (rolled out quietly from August 2024, documented by Joy Hawkins at Sterling Sky).** If a URL ranks in the local pack, Google may suppress that same URL from page one of the organic results. The demotion is page-level, which gives you the workaround: don't link your GBP to your homepage if your homepage also ranks organically. Link it to a strong service or location page instead. Test with UTM tagging so you can measure the effect.

**AI Overviews and AI Mode.** AI Overviews now appear on roughly 68% of local business queries in Whitespark's testing, and mixed informational/transactional queries ("best emergency plumber for a burst pipe in Dartford") trigger them 97% of the time. AI local packs surface far fewer businesses than the traditional 3-pack (Sterling Sky tracked roughly a third as many). This makes AI visibility a winner-takes-more game, and it's why citations and consistent entity data came back into fashion after years of being written off.

### The 2026 ranking weight breakdown (Whitespark)

For the local pack / Maps:

| Signal category | Weight |
|---|---|
| GBP signals | 32% |
| Review signals | 20% (up from 16% in 2023) |
| On-page signals | 15-19% |
| Behavioural signals | ~9% (rising) |
| Link signals | ~8% |
| Citation signals | ~6% (rising, driven by AI) |
| Social signals | ~5% (back on the board) |

Proximity to the searcher remains the single biggest factor overall (roughly 55% of the decision) and you can't control it. Everything below is about maximising the controllable share.

---

## Part 2: Site architecture

### Core structure (largely unchanged, with corrections)

The hub-and-spoke model still applies:

1. **Service pillar pages** at the root: `/boiler-repairs/`, `/boiler-servicing/`. One dedicated page per service. This is the single highest-value on-page move you can make. Number one local organic factor.
2. **Location hub pages** for genuinely served areas: `/dartford/`, `/gravesend/`.
3. **Service + location pages** only for the combinations where you have real proof: jobs done there, reviews from there, photos from there.
4. **Everything else** named on an "Areas We Cover" page, not given its own URL.

### What changes from the old approach

**Fewer location pages, more proof per page.** The old logic was "one URL = one ranking opportunity, so build the full matrix." The 2026 logic is "one URL = one liability unless it earns its place." Two or three strong city pages with genuine local evidence outperform fifteen templated ones, and the fifteen can now actively hurt you (doorway filtering, sitewide quality assessment under the helpful content system, which is now baked into core ranking).

**The removed-city-name test.** Take the town name out of the page. Is it still obviously about that place? If not, it's a doorway page regardless of your intentions. Aim for roughly 50% genuinely unique, location-specific content per page (BrightLocal's working benchmark).

**Local proof elements that can't be copied between pages:**

- Reviews from customers in that specific town, quoted with context
- Photos of actual jobs in that area (Google strips EXIF data, so geotagging does nothing; the photos matter as content and E-E-A-T evidence, not as coordinates)
- Housing stock context ("the Victorian terraces off the high street typically have...")
- Local data: water hardness, common boiler types, council schemes, flue regulations that bite locally
- Real response times from your base
- Area-specific FAQs in natural conversational language ("Do you cover emergency call-outs in Swanscombe on Sundays?")

**Entity consistency across the site.** Same business name, same service terminology, same descriptions of what you do, everywhere: site, GBP, schema, directories. Inconsistency is now a demotion signal because Google cross-checks these sources to validate the entity. If the GBP says one thing, the website another, and the reviews a third, confidence drops and so do rankings.

### Schema (structured data)

Non-negotiable now, because it feeds both the Knowledge Graph and AI answer engines:

- **LocalBusiness schema** (or the specific subtype, e.g. Plumber, HVACBusiness) on the homepage and location pages, with NAP exactly matching the GBP
- **Service schema** on service pages
- **FAQPage schema** where you have genuine FAQs
- **sameAs** properties linking to your GBP, social profiles, and key directory listings. This is how you explicitly tell Google "these profiles are all the same entity"
- **Review/AggregateRating** where you legitimately display reviews

Google validates markup against visible content and external sources. Schema confirms an entity Google already recognises; it doesn't create recognition from nothing. Consistency does that.

### E-E-A-T for trades sites (post-December 2025)

This used to be a health-and-finance concern. It now applies to competitive local queries. Concretely:

- Named people with real credentials. Gas Safe registration number visible and linked. Years trading. Photos of the actual team.
- Service content written from experience, not from a keyword brief. "What we find when we service back boilers in older Gravesend properties" beats "boiler servicing is important because..."
- Original photography of work, van, premises. Stock photos are a negative signal a human quality rater (and increasingly the algorithm) can spot.
- Case studies with specific detail: the job, the problem, the fix, the town.

### Technical floor

- LCP under 3 seconds (under 2.5 to be safe), INP under 300ms, measured at the 75th percentile in field data (PageSpeed Insights)
- Mobile-first everything; most local searches are mobile
- Crawlable text NAP in the footer, not an image
- Astro static builds on Cloudflare Pages already put you ahead of most WordPress competitors here; this is a genuine advantage, keep it

---

## Part 3: Google Business Profile

GBP is 32% of local pack ranking weight, the largest controllable category. Within it, factors are not equal. Here's what controlled testing and the 2026 survey confirm actually moves rankings, versus what's folklore.

### Confirmed high-impact factors

**1. Primary category.** The single most important individual factor. Choosing the wrong one is the second most common reason businesses fail to rank. Be as specific as the category list allows ("Heating contractor" or "Boiler supplier" rather than "Contractor"). Add secondary categories for every legitimate service line, but know the primary carries most of the weight. The category functions as a gatekeeper: it grants structural permission to appear for a query class at all.

**2. Business hours: being open at the time of search.** Fifth most important local pack factor, new to prominence in the 2026 survey. Rankings measurably degrade in the final listed hour and while closed. If you genuinely take emergency calls out of hours, list hours accordingly. Never leave a profile marked temporarily closed.

**3. Services section, using Google's predefined services.** Jumped from #81 to #22 in importance. Add every predefined service Google suggests for your category, then add custom services with keyword-aligned descriptions. These feed Google's structured data parser and AI Overview answers directly.

**4. Review velocity.** Jumped from #93 to #11. A steady drip of fresh reviews (say five a month, every month) now beats a large stale total. Consistency is the signal: it says "active, healthy business."

**5. Review responses.** Google has confirmed responding improves rankings. Businesses responding to 80%+ of reviews see a measurable lift, amplified when responses land within 24-48 hours. Your response text gets indexed: mention the service performed and the town naturally in replies.

**6. The website link.** Link the GBP to a strong, relevant page, and because of the Diversity Update, preferably not a homepage that already ranks organically for your money terms. A dedicated location or primary service page is the current best practice. Tag it with UTM parameters so GBP traffic is measurable in analytics.

**7. Photos.** Regular uploads of real work, team, and premises. They influence engagement and conversion (behavioural signals, ~9% and rising) and act as E-E-A-T evidence. Skip the geotagging ritual: Google strips EXIF metadata on upload, confirmed by testing and by a former Google employee.

**8. NAP consistency.** Name, address, phone identical (character for character) across website schema, GBP, Bing Places, Apple Maps, and your core directories. Google cross-references these to verify the entity.

### Confirmed non-factors (stop spending time here)

- **GBP posts for ranking.** A nine-week Sterling Sky study across 441 keywords found zero ranking movement. Posts help click-through rate and make the profile look alive, so do them lightly, but they are engagement tools, not ranking levers.
- **The business description.** Google has directly confirmed it's not used in ranking. Write it for customers.
- **Service area settings (for businesses with a listed address).** Whitespark's controlled test found no ranking effect. You rank from your verified address.
- **Keywords in review text.** Sterling Sky tested this; no ranking impact. (Review sentiment and specificity still matter for AI surfacing and conversion, just not as a pack ranking lever.)
- **Geotagged photos.** Dead, as above.

### The uncomfortable one

Keywords in the business name remain a strong ranking factor (Hawkins' "salad bar" test moved a business from unranked to fourth almost immediately). Adding keywords to a GBP name you don't legally trade under violates Google's guidelines and invites suspension, so the legitimate version of this insight is: if you're ever naming a business or sub-brand, the name itself is an entity signal. "Thames Boilers" already does this job for you. Note the flipside from the Search Engine Land entity analysis: a niche name creates an entity boundary. Google reads the name as a classification, so a name that screams one service can suppress visibility for broader queries.

### Ongoing GBP routine

| Frequency | Task |
|---|---|
| Weekly | Respond to all new reviews within 48h; upload 1-2 real photos |
| Monthly | Check hours (including bank holidays); review Q&A; light post if there's something genuine to say |
| Quarterly | Re-check primary/secondary categories against Google's evolving list; audit services section; check for duplicate or "permanently closed" listings; verify NAP across top citations |

---

## Part 4: Reviews as a system

Reviews are 20% of pack ranking and climbing, plus the dominant conversion factor (BrightLocal 2026: 41% of consumers always read reviews, 68% won't use anything under four stars). Treat review generation as a marketing operation, not a customer service afterthought.

- **Ask every satisfied customer, immediately after the job**, with a direct review link (fewest possible taps). This is an automation job: ServiceM8 job completion → review request. You've built this pattern before with postcards; the same trigger works here.
- **Coach the ask.** A review that says "George fixed our burst pipe in Dartford, brilliant service" is worth more than five that say "Great!" AI systems read review text to decide whether you match a query. Don't script customers, but the ask can mention "it helps if you say what we did for you."
- **Velocity over volume.** Design the system for a steady monthly flow, forever.
- **Respond to everything**, negatives especially. A well-handled negative review measurably improves consumer behaviour toward the business.
- **Diversify.** Reviews on Yelp-equivalents, Checkatrade-type industry platforms, and Facebook feed the citation and AI-visibility signals, not just Google.

---

## Part 5: Links and citations

Link signals are ~8% of pack weight and matter more for local organic. Citations were declared dead for years; the 2026 survey brings them back, because AI answer engines lean heavily on them. The top-rated citation-related factors this year: presence on expert-curated "best of" lists, prominence on industry-relevant domains, quality of unstructured citations (mentions in news, blogs, association sites), and quantity of unlinked brand mentions.

### What to build

**Tier 1: the entity-verification layer.** GBP, Bing Places, Apple Maps, Facebook, and the 10-20 directories that matter in your niche and country (for UK trades: Checkatrade, Trustpilot, Yell, Gas Safe register listing, TrustATrader, local chamber). Perfect NAP consistency. This is table stakes for entity trust and for AI visibility. Ten authoritative citations beat fifty junk ones; mass directory submission is dead and mildly harmful.

**Tier 2: locally relevant editorial links.** These carry the real ranking weight:

- Sponsorships: junior football kits, charity runs, school fetes, BJJ club events. The link from the event or club site is the byproduct of real participation, which is exactly what makes it safe and valuable.
- Local press: pitch genuinely newsworthy things (community initiative, unusual job, expert comment when a national heating story breaks). One local news mention outweighs dozens of directory links, and unstructured news citations are specifically credited in AI visibility.
- Trade and industry bodies: Gas Safe, manufacturer accredited-installer pages (Worcester Bosch, Vaillant etc. installer finders are both links and entity confirmation).
- Partnerships with non-competing local businesses: the plumber recommends the electrician, both link, both benefit.
- Chamber of commerce and business associations, where membership is real.

**Tier 3: linkable assets.** One genuinely useful local resource earns links passively: a water hardness map for North Kent, a "new boiler cost in [region]" data page, an annual survey of local heating costs. Original data is the most reliably linkable format.

### What to avoid

- Bought links and cheap guest post networks. Google increasingly just ignores them (wasted money) or filters the site (worse). 2026 has seen a flood of AI-generated sites built purely to sell links; they look plausible and are worthless.
- Chasing DR/DA numbers over relevance. A relevant local link from a modest site beats an irrelevant DR70 placement.
- Exact-match anchor text campaigns. Natural mix: mostly branded and generic.

Benchmark competitively rather than chasing a number: check the referring domains of whoever ranks top three for your main term in Ahrefs and aim to match the profile, not the internet's average.

---

## Part 6: AI visibility (the new layer)

This is now a formal category in the ranking factors survey. The good news: it mostly rewards the same work, weighted toward structured, consistent data. The specifics:

- **Consistent entity data everywhere.** Same name, same service descriptions, same terminology across GBP, site, schema, and directories. AI systems favour businesses that look real, active, and consistently referenced across multiple sources.
- **Be summarisable.** Clear, extractable answers on service pages: prices or price ranges, hours, coverage areas, FAQs in conversational language. If an AI can't confidently state what you do, where, and for how much, it recommends someone it can summarise.
- **Don't ignore Bing.** ChatGPT's live web search runs on Bing's index. Claim and complete Bing Places, and implement IndexNow (trivial on Cloudflare, it's a toggle/API ping) so Bing indexes page changes immediately. Businesses optimising only for Google are invisible to ChatGPT's local recommendations.
- **Reviews with substance** are what AI systems quote when recommending a business.
- **Keep perspective.** Darren Shaw's own caveat in the 2026 report: AI's impact on local search is still smaller than the hype suggests. Google search still dominates local discovery. AI visibility is a layer on top of the fundamentals, not a replacement for them.

---

## Part 7: Priority order for a new or rebuilt site

A 90-day sequence, highest leverage first:

**Weeks 1-2: Entity foundation**
1. GBP audit: primary category, predefined services, hours, photos, no duplicates
2. GBP website link pointed at a strong non-homepage page, UTM tagged
3. LocalBusiness schema with sameAs links, NAP matching GBP exactly
4. Bing Places claimed, IndexNow enabled

**Weeks 3-6: Core pages**
5. One dedicated page per service (the #1 organic factor), written from real experience with real photos
6. Location pages only for towns with genuine proof; kill or consolidate any templated ones
7. Homepage clearly stating who, what, where, with credentials visible

**Weeks 7-10: Reviews and citations**
8. Automated post-job review request flow
9. Response process: everything answered within 48h
10. Tier 1 citations built/corrected for NAP consistency

**Weeks 11-13: Authority**
11. Two or three local sponsorships or partnerships secured
12. One linkable local asset published
13. One local press angle pitched

Then it's maintenance: the GBP routine, monthly review velocity, one meaningful content or link win per month.

---

## Part 8: Notes against your existing `local-seo-site-architecture` skill

What still holds: the hub-and-spoke structure, one page per service, the content differentiation table, the "never swap the town name" rule, separating repairs from servicing by intent. That skill was more right than the "location pages are dead" narrative suggests.

What to update in it:

1. **Cut the matrix harder.** The current tiering allows up to 15 city page sets. Post-December 2025, the constraint isn't crawl budget, it's proof. Cap primary locations at however many towns you can evidence with reviews, photos, and jobs. For most trades that's 3-6, not 15.
2. **Add the GBP link rule** (Diversity Update): the GBP should point at one of these pages, not the homepage.
3. **Add schema requirements** per page type, including sameAs.
4. **Add the entity consistency check** as a deliverable: a single source of truth for name, services terminology, and NAP that every page and profile must match.
5. **Add an E-E-A-T block** per page: named person, credential, original photo, specific testimonial.
6. **Add Bing/IndexNow** to the launch checklist.

---

## Sources

- Whitespark, Local Search Ranking Factors 2026 (Darren Shaw, Nov 2025): whitespark.ca/local-search-ranking-factors
- Whitespark blog, "7 Local Search Ranking Factors That May Challenge Your Current Thinking"
- Sterling Sky / Joy Hawkins, "Google's New Diversity Update" and controlled GBP tests: sterlingsky.ca
- Search Engine Land, "The local SEO gatekeeper: How Google defines your entity" (Jan 2026)
- ReplyOnTheFly, "Local SEO Ranking Factors: What Actually Works in 2026" (summary of Whitespark/Sterling Sky data)
- BrightLocal, location pages guidance and 2026 Local Consumer Review Survey
- Digital Applied, "Local SEO + Core Updates: GBP Strategy May 2026" (AI Overviews local query data)
- ALM Corp / ThatWare / Dataslayer, December 2025 core update analyses
- Advice Local, "The 2026 Local Search Ranking Factors on Maps, Organic & AI"
- Google spam policies (doorway pages), Search Central
