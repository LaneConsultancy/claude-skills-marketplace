# Competitor Classification Reference

Detailed criteria for automatically classifying SERP results to identify relevant direct competitors.

## Auto-Exclude Domain List

These domains are automatically excluded when `business_type = "local"`:

### Trade Directories
```
checkatrade.com
ratedpeople.com
mybuilder.com
bark.com
trustatrader.com
which.co.uk/trusted-traders
freeindex.co.uk
yell.com
thomsonlocal.com
yelp.co.uk
cylex-uk.co.uk
hotfrog.co.uk
192.com
thebestof.co.uk
misterwhat.co.uk
```

### National Service Providers (UK)
```
britishgas.co.uk
homeserve.com
dyno.com
pimlico.co.uk
aspect.co.uk
fantastic-services.com
householdquotes.co.uk
myjobquote.co.uk
```

### Lead Generation / Comparison
```
quotezone.co.uk
comparethemarket.com
moneysupermarket.com
confused.com
gocompare.com
uswitch.com
checkatrader.com
priceyourjob.co.uk
```

### Forums & Community
```
reddit.com
mumsnet.com
diynot.com
moneysavingexpert.com/forums
avforums.com
pistonheads.com
```

### Informational
```
wikipedia.org
wikihow.com
diy.com/ideas
screwfix.com/help
```

### E-commerce (category pages)
```
amazon.co.uk
ebay.co.uk
screwfix.com
toolstation.com
```

## URL Pattern Matching

Exclude URLs matching these patterns (regex):

```
/find-a-.*
/directory/
/business-directory/
/local-services/
/search\?
/listings/
/traders/
/professionals/
/pros/
/compare/
/quotes/
```

## Title Pattern Matching

Exclude results with titles matching these patterns:

```
"10 Best..."
"Top [0-9]+ ..."
"Best ... Near You"
"Find a ... in"
"... Quotes from"
"Compare ... Prices"
"[0-9]+ ... Companies in"
"Hire a ... "
"... Services Near Me"
"Find Local ..."
```

## Classification Categories

### Category: local_business
**Include when:**
- Domain is a business website (not a directory)
- URL structure suggests company site (/, /services/, /about/)
- Title contains business name or service description
- Description mentions specific location or area served

**Signals:**
- .co.uk single business domain
- Local area codes in URL or visible text
- "Serving [specific area]" language
- Owner/tradesperson name in branding
- Limited geographic service area mentioned

### Category: regional_business
**Include when:**
- Business serves multiple areas but not nationwide
- Clear regional focus (e.g., "South East London")
- Multiple branch locations but not a national chain

### Category: national_chain
**Exclude when business_type = "local"**

**Identification:**
- Well-known brand names
- 0800, 0333, or other national phone patterns
- "Find your local branch" language
- Franchise indicators
- Corporate structure evident in footer/about

### Category: directory
**Always exclude for competitor analysis**

**Identification:**
- Domain in auto-exclude list
- URL matches directory patterns
- Title matches directory patterns
- Multiple businesses listed on single page
- "Get quotes" or "Compare" prominence

### Category: lead_generation
**Exclude when business_type = "local"**

**Identification:**
- Primary purpose is collecting contact info
- Quote forms prominent above fold
- "Get 3 Free Quotes" or similar
- No actual service delivery, just lead selling

### Category: informational
**Always exclude for competitor analysis**

**Identification:**
- Editorial content (how-to, guides)
- Forum threads
- News articles
- Wikipedia/reference sites
- Government/council pages

### Category: ecommerce
**Exclude for service-based local SEO**

**Identification:**
- Product listings
- Shopping cart functionality
- Price comparisons
- Marketplace listings (Amazon, eBay)

## Classification Output Format

```json
{
  "included_competitors": [
    {
      "position": 1,
      "url": "https://smithplumbing-dartford.co.uk/",
      "domain": "smithplumbing-dartford.co.uk",
      "title": "Smith Plumbing Dartford - 24/7 Emergency Plumber",
      "classification": "local_business",
      "confidence": "high",
      "reason": "Single-location plumber with Dartford in domain, local phone number, serves defined area"
    },
    {
      "position": 3,
      "url": "https://kentplumbers.co.uk/dartford",
      "domain": "kentplumbers.co.uk",
      "title": "Kent Plumbers - Dartford Branch",
      "classification": "regional_business",
      "confidence": "high",
      "reason": "Regional business with multiple Kent locations, Dartford-specific landing page"
    }
  ],
  "excluded_results": [
    {
      "position": 2,
      "url": "https://checkatrade.com/trades/plumbers/dartford",
      "domain": "checkatrade.com",
      "classification": "directory",
      "confidence": "high",
      "reason": "Auto-excluded: Domain in directory blocklist"
    },
    {
      "position": 4,
      "url": "https://britishgas.co.uk/plumbing",
      "domain": "britishgas.co.uk",
      "classification": "national_chain",
      "confidence": "high",
      "reason": "National service provider - not a direct local competitor"
    },
    {
      "position": 7,
      "url": "https://reddit.com/r/plumbing/comments/...",
      "domain": "reddit.com",
      "classification": "informational",
      "confidence": "high",
      "reason": "Forum discussion - not a competitor"
    }
  ],
  "summary": {
    "total_results": 10,
    "included_count": 5,
    "excluded_count": 5,
    "exclusion_breakdown": {
      "directory": 2,
      "national_chain": 1,
      "informational": 2
    }
  }
}
```

## Business Type Behaviours

### business_type = "local"
- Apply all exclusion rules
- Focus on identifying true local competitors
- Filter aggressively to ensure relevance

### business_type = "national"
- Include national businesses as competitors
- Still exclude directories and informational content
- Include regional businesses

### business_type = "any"
- Minimal filtering
- Only exclude obvious non-competitors (forums, Wikipedia)
- Include directories if they have useful content to analyse

## Edge Cases

### Franchise with Local Operator
If a franchise has a genuinely local operator page (not just a branch finder):
- Check if page has local content, local reviews, local contact
- If yes, may include as it represents local competition
- If just a landing page, exclude as national

### Local Business with National Ambitions
If a business started local but is expanding:
- Check current page being analysed
- If page targets specific local area, include
- If page is generic national, consider excluding

### Directory with Featured Business Content
If a directory page has substantial content about a specific business:
- Still exclude for competitor analysis
- Note that the featured business may be worth analysing directly

## Confidence Levels

- **high**: Clear match to exclusion list or obvious local business
- **medium**: Pattern matching but not definitive
- **low**: Uncertain classification, may need manual review

For automated processing, treat medium and low confidence as included to avoid missing competitors. The analysis phase will reveal if they're truly relevant.
