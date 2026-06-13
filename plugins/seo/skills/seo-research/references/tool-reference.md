# Tool Reference

Quick reference for DataForSEO and Apify MCP tools used in this skill.

## DataForSEO Tools

### 1. SERP Organic Live Advanced

**Tool:** `mcp__dataforseo__serp_organic_live_advanced`

**Purpose:** Get organic search results for a keyword

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| keyword | string | Yes | - | Search keyword |
| location_name | string | No | "United States" | Location for search (e.g., "United Kingdom") |
| language_code | string | Yes | - | Language code (e.g., "en") |
| device | string | No | "desktop" | Device type: "desktop" or "mobile" |
| depth | number | No | 10 | Number of results (10-700) |
| max_crawl_pages | number | No | 1 | Pages to crawl (1-7) |
| people_also_ask_click_depth | number | No | - | PAA expansion depth (1-4) |
| search_engine | string | No | "google" | Search engine: "google", "yahoo", "bing" |

**Example Call:**
```json
{
  "keyword": "boiler repair dartford",
  "location_name": "United Kingdom",
  "language_code": "en",
  "device": "desktop",
  "depth": 10,
  "people_also_ask_click_depth": 2
}
```

**Response Data Points:**
- `items[].url` - Result URL
- `items[].domain` - Domain name
- `items[].title` - SERP title
- `items[].description` - Meta description shown
- `items[].rank_group` - Position in SERP
- `items[].type` - Result type (organic, featured_snippet, etc.)
- `people_also_ask` - PAA questions array
- `related_searches` - Related search terms

---

### 2. On-Page Content Parsing

**Tool:** `mcp__dataforseo__on_page_content_parsing`

**Purpose:** Parse page content and structure

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL to parse |
| enable_javascript | boolean | No | false | Enable JS rendering |
| custom_user_agent | string | No | - | Custom user agent |
| accept_language | string | No | - | Accept-Language header |

**Example Call:**
```json
{
  "url": "https://example.com/services/plumbing",
  "enable_javascript": true
}
```

**Response Data Points:**
- `page_content.title` - Title tag
- `page_content.meta_description` - Meta description
- `page_content.h1` - H1 headings array
- `page_content.h2` - H2 headings array
- `page_content.h3` - H3 headings array
- `page_content.plain_text_word_count` - Total word count
- `page_content.text` - Full page text
- `page_content.links.internal` - Internal links array
- `page_content.links.external` - External links array
- `page_content.images` - Images array with alt text

---

### 3. On-Page Lighthouse

**Tool:** `mcp__dataforseo__on_page_lighthouse`

**Purpose:** Get Lighthouse performance audit

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL to audit |
| enable_javascript | boolean | No | false | Enable JS rendering |
| custom_user_agent | string | No | - | Custom user agent |
| accept_language | string | No | - | Accept-Language header |

**Example Call:**
```json
{
  "url": "https://example.com/services/plumbing"
}
```

**Response Data Points:**
- `categories.performance.score` - Performance score (0-100)
- `categories.accessibility.score` - Accessibility score
- `categories.best_practices.score` - Best practices score
- `categories.seo.score` - SEO score
- `audits.largest-contentful-paint.numericValue` - LCP in ms
- `audits.cumulative-layout-shift.numericValue` - CLS score
- `audits.first-contentful-paint.numericValue` - FCP in ms
- `audits.total-blocking-time.numericValue` - TBT in ms

---

### 4. On-Page Instant Pages

**Tool:** `mcp__dataforseo__on_page_instant_pages`

**Purpose:** Detailed page analysis with SEO factors

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| url | string | Yes | - | URL to analyse |
| enable_javascript | boolean | No | false | Enable JS rendering |
| custom_js | string | No | - | Custom JS to execute |
| custom_user_agent | string | No | - | Custom user agent |
| accept_language | string | No | - | Accept-Language header |

**Response Data Points:**
- `meta.title` - Title tag
- `meta.description` - Meta description
- `meta.canonical` - Canonical URL
- `meta.htags` - Heading tags object
- `content.plain_text_word_count` - Word count
- `content.plain_text_rate` - Text to HTML ratio
- `page_timing` - Page load timing data
- `onpage_score` - Overall on-page SEO score
- `checks` - Detailed SEO checks results

---

## Apify Tools

### RAG Web Browser

**Tool:** `mcp__apify__apify-slash-rag-web-browser`

**Purpose:** Fallback web scraping when DataForSEO parsing fails

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| query | string | Yes | - | URL or search query |
| maxResults | integer | No | 3 | Number of results |
| outputFormats | array | No | ["markdown"] | Output formats: "text", "markdown", "html" |

**Example Call:**
```json
{
  "query": "https://example.com/services/plumbing",
  "maxResults": 1,
  "outputFormats": ["markdown"]
}
```

**When to Use:**
- Primary parsing tool returns incomplete data
- JavaScript-heavy pages that DataForSEO struggles with
- Need cleaner markdown content for analysis

**Response Data Points:**
- `text` - Plain text content
- `markdown` - Markdown formatted content
- `metadata.title` - Page title
- `metadata.description` - Meta description

---

## SERP Location Reference

### UK Locations (Common)

| Location Name | Use For |
|---------------|---------|
| United Kingdom | National UK searches |
| England | England-wide searches |
| London,England,United Kingdom | London searches |
| Manchester,England,United Kingdom | Manchester searches |
| Birmingham,England,United Kingdom | Birmingham searches |

### Location Format

For specific areas, use hierarchical format:
```
City,Region,Country
```

Examples:
- `Dartford,England,United Kingdom`
- `Edinburgh,Scotland,United Kingdom`
- `Cardiff,Wales,United Kingdom`

Use `mcp__dataforseo__serp_locations` to find exact location names:
```json
{
  "country_iso_code": "GB",
  "location_name": "Dartford"
}
```

---

## Error Handling Patterns

### SERP Collection Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| No results returned | Keyword too specific or location mismatch | Try broader keyword, check location spelling |
| Rate limit exceeded | Too many requests | Wait and retry, reduce parallelism |
| Invalid location | Location name not recognised | Use serp_locations tool to verify |

**Recovery Code Pattern:**
```
If SERP returns empty results:
1. Note in report: "No results found for [keyword]"
2. Suggest alternative keywords based on related_searches
3. Continue with remaining keywords
```

### Page Parsing Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Timeout | Page too slow or large | Enable JS, increase timeout, try Apify |
| 403/401 | Blocked by site | Try Apify with different user agent |
| Empty content | JS-rendered content | Enable JavaScript, use Apify fallback |
| SSL error | Certificate issues | Note and skip, or try http:// |

**Recovery Code Pattern:**
```
If on_page_content_parsing fails:
1. Retry with enable_javascript: true
2. If still fails, use apify-slash-rag-web-browser
3. If Apify fails, log URL as "analysis unavailable" and continue
```

### Lighthouse Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Timeout | Very slow page | Skip technical analysis, note in report |
| Page unreachable | Site down or blocking | Skip technical analysis |

**Recovery Code Pattern:**
```
If on_page_lighthouse fails:
1. Set performance metrics to null
2. Note in report: "Technical analysis unavailable for [URL]"
3. Continue with content analysis only
```

---

## Tool Selection Logic

```
┌─────────────────────────────────────────────────────────┐
│                    SERP COLLECTION                       │
│                                                         │
│  Always use: serp_organic_live_advanced                 │
│  No fallback available                                  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   CONTENT PARSING                        │
│                                                         │
│  Primary: on_page_content_parsing                       │
│     └─→ If fails: apify-slash-rag-web-browser          │
│                                                         │
│  Alternative: on_page_instant_pages                     │
│     └─→ More detailed but slower                        │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                 TECHNICAL ANALYSIS                       │
│                                                         │
│  Primary: on_page_lighthouse                            │
│     └─→ If fails: Skip technical metrics                │
│                                                         │
│  No fallback - Lighthouse data is optional              │
└─────────────────────────────────────────────────────────┘
```

---

## Response Size Management

To preserve context window, extract only needed fields:

### From SERP Response
```json
{
  "keyword": "string",
  "results": [
    {
      "position": "number",
      "url": "string",
      "domain": "string",
      "title": "string",
      "description": "string"
    }
  ],
  "paa_questions": ["string"],
  "related_searches": ["string"],
  "serp_features": {
    "featured_snippet": "boolean",
    "local_pack": "boolean"
  }
}
```

### From Content Parsing Response
```json
{
  "url": "string",
  "title": "string",
  "meta_description": "string",
  "h1": ["string"],
  "h2": ["string"],
  "h3_count": "number",
  "word_count": "number",
  "internal_links_count": "number",
  "external_links_count": "number",
  "images_count": "number",
  "images_with_alt": "number"
}
```

### From Lighthouse Response
```json
{
  "performance_score": "number",
  "lcp_seconds": "number",
  "cls": "number",
  "fcp_seconds": "number",
  "mobile_friendly": "boolean"
}
```

---

## Parallel Execution Guidelines

### Safe Parallel Limits

| Operation | Max Parallel | Reason |
|-----------|--------------|--------|
| SERP collection | 5 | API rate limits |
| Content parsing | 3 | Response size, processing time |
| Lighthouse | 2 | Heavy operation |

### Execution Pattern

```
Phase 1: SERP Collection
├─→ Keyword 1 ──┐
├─→ Keyword 2 ──┼─→ Wait for all ──→ Phase 2
├─→ Keyword 3 ──┤
├─→ Keyword 4 ──┤
└─→ Keyword 5 ──┘

Phase 3: Analysis (Batch 1)
├─→ Competitor 1 ──┐
├─→ Competitor 2 ──┼─→ Wait ──→ Batch 2
└─→ Competitor 3 ──┘

Phase 3: Analysis (Batch 2)
├─→ Competitor 4 ──┐
├─→ Competitor 5 ──┼─→ Wait ──→ Phase 4
└─→ Competitor 6 ──┘
```

---

## Schema Detection

When parsing pages, look for these schema types in the page source:

### Priority Schema Types

| Schema Type | Indicates | Value for Local SEO |
|-------------|-----------|---------------------|
| LocalBusiness | Local business info | High |
| FAQPage | FAQ content | High |
| Review/AggregateRating | Customer reviews | High |
| Service | Service offerings | Medium |
| BreadcrumbList | Navigation structure | Medium |
| Organization | Company info | Low |

### Detection Pattern

Schema can be found in:
1. `<script type="application/ld+json">` tags
2. Microdata attributes (`itemtype`, `itemprop`)
3. RDFa attributes

When using content parsing, check `page_content` for JSON-LD scripts and extract schema types.

---

## Quick Reference Card

### Essential Tool Calls

**Get SERP data:**
```
mcp__dataforseo__serp_organic_live_advanced
├── keyword: "target keyword"
├── location_name: "United Kingdom"
├── language_code: "en"
├── depth: 10
└── people_also_ask_click_depth: 2
```

**Parse page content:**
```
mcp__dataforseo__on_page_content_parsing
├── url: "https://competitor.com/page"
└── enable_javascript: true
```

**Get performance data:**
```
mcp__dataforseo__on_page_lighthouse
└── url: "https://competitor.com/page"
```

**Fallback scraping:**
```
mcp__apify__apify-slash-rag-web-browser
├── query: "https://competitor.com/page"
├── maxResults: 1
└── outputFormats: ["markdown"]
```
