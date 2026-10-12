# Apify Setup & Configuration Guide

This document provides detailed instructions for using Apify MCP tools to discover expired domains.

---

## Overview

Apify provides web scraping actors that can extract expired domain listings from sources like expireddomains.net. This guide covers:

1. Finding the right actor
2. Configuring input parameters
3. Handling results
4. Troubleshooting common issues

---

## Step 1: Finding the Expired Domains Actor

### Using MCP Tool: `mcp__apify__search-actors`

**Query Options**:
```
"expireddomains.net scraper"
"expired domains"
"domain scraper"
"deleted domains"
```

### Example Tool Call

```typescript
mcp__apify__search-actors({
  query: "expireddomains.net scraper"
})
```

### Expected Response Structure

```json
{
  "results": [
    {
      "id": "username/expireddomains-scraper",
      "name": "Expired Domains Scraper",
      "description": "Scrapes expireddomains.net for recently expired domains with backlinks",
      "stats": {
        "runs": 1234,
        "users": 56
      }
    }
  ]
}
```

### Selection Criteria

Choose an actor based on:
1. **High run count** (indicates reliability)
2. **Recent updates** (check lastModified date)
3. **Good user ratings** (if available)
4. **Clear documentation** (read description)

### Recommended Actors (as of 2026-01)

If you find multiple options, prioritize actors that specifically mention:
- expireddomains.net as source
- Backlink filtering capabilities
- TLD filtering
- Deleted/pending domain support

---

## Step 2: Configuring Actor Input

### Using MCP Tool: `mcp__apify__call-actor`

### Standard Input Schema

Most expireddomains.net scrapers accept these parameters:

```typescript
{
  actorId: "username/expireddomains-scraper",
  input: {
    // REQUIRED
    "keyword": string,           // Search keyword or phrase
    
    // FILTERING
    "tld": string,               // Top-level domain (e.g., "co.uk", "com")
    "minBacklinks": number,      // Minimum backlink count
    "minRefDomains": number,     // Minimum referring domains
    "minDomainPop": number,      // Minimum domain popularity score
    
    // LIMITS
    "maxResults": number,        // Maximum domains to return
    
    // OPTIONS
    "includeDeleted": boolean,   // Include deleted domains
    "includePending": boolean,   // Include pending delete domains
    "sortBy": string,            // Sort order: "bl", "rd", "dp", "age"
  },
  waitForFinish: number          // Timeout in seconds (max 300)
}
```

### Parameter Details

#### `keyword` (Required)
The search term used to filter domains. Can use Boolean operators:

**Single keyword**:
```json
"keyword": "plumber"
```

**Multiple keywords (OR)**:
```json
"keyword": "plumber OR plumbing OR drainage"
```

**Exact phrase**:
```json
"keyword": "emergency plumber"
```

**Complex query**:
```json
"keyword": "(plumber OR plumbing) AND (london OR manchester)"
```

---

#### `tld` (Recommended)
Filter by top-level domain extension:

**Common values**:
- `"co.uk"` - UK commercial domains
- `"com"` - Generic commercial
- `"org"` - Organizations
- `"net"` - Network domains
- `"uk"` - All UK domains

**Tip**: For UK PBN building, use `"co.uk"` exclusively for local authority.

---

#### `minBacklinks` (Recommended)
Minimum number of backlinks the domain must have:

**Recommended values**:
- **Strict**: `10` - High-quality domains only
- **Moderate**: `5` - Good balance (default)
- **Broad**: `1` - Maximum discovery

**Note**: Higher values reduce results but improve quality.

---

#### `minRefDomains` (Recommended)
Minimum unique referring domains:

**Recommended values**:
- **Strict**: `10`
- **Moderate**: `5` (default)
- **Broad**: `3`

**Why this matters**: More referring domains = more diverse backlink profile = better PBN candidate.

---

#### `minDomainPop` (Optional)
Popularity score from expireddomains.net (0-10 scale):

**Recommended**: `1` (avoid completely unknown domains)

---

#### `maxResults` (Recommended)
Limit the number of domains returned:

**Recommended values**:
- **Quick scan**: `20-50`
- **Standard**: `100` (default)
- **Deep search**: `200-500`

**Note**: Higher values increase runtime and API costs.

---

#### `includeDeleted` (Recommended: `true`)
Include domains that have already been deleted.

**Why enable**: These are available for immediate registration.

---

#### `includePending` (Recommended: `true`)
Include domains pending deletion.

**Why enable**: You can prepare to register these domains as they become available.

---

#### `sortBy` (Optional)
Sort order for results:

**Options**:
- `"bl"` - Backlinks (descending)
- `"rd"` - Referring domains (descending)
- `"dp"` - Domain popularity (descending)
- `"age"` - Domain age (descending)

**Recommended**: `"rd"` for quality-focused search.

---

## Step 3: Example Configurations

### Configuration 1: High-Quality Plumbing Domains

**Use case**: Finding premium .co.uk domains for plumbing PBN

```json
{
  "actorId": "username/expireddomains-scraper",
  "input": {
    "keyword": "plumber OR plumbing OR drainage OR leak",
    "tld": "co.uk",
    "minBacklinks": 10,
    "minRefDomains": 8,
    "minDomainPop": 2,
    "maxResults": 50,
    "includeDeleted": true,
    "includePending": true,
    "sortBy": "rd"
  },
  "waitForFinish": 120
}
```

**Expected results**: 5-20 high-quality domains

---

### Configuration 2: Broad Heating Discovery

**Use case**: Casting wide net to find any heating-related domains

```json
{
  "actorId": "username/expireddomains-scraper",
  "input": {
    "keyword": "boiler OR heating OR gas OR central heating OR radiator",
    "tld": "co.uk",
    "minBacklinks": 3,
    "minRefDomains": 3,
    "maxResults": 150,
    "includeDeleted": true,
    "includePending": true,
    "sortBy": "bl"
  },
  "waitForFinish": 180
}
```

**Expected results**: 30-80 domains for further filtering

---

### Configuration 3: Multi-TLD Search

**Use case**: Accepting both .com and .co.uk domains

```json
{
  "actorId": "username/expireddomains-scraper",
  "input": {
    "keyword": "electrician OR electrical OR wiring",
    "tld": "com|co.uk",  // Note: Syntax may vary by actor
    "minBacklinks": 5,
    "minRefDomains": 5,
    "maxResults": 100,
    "includeDeleted": true,
    "includePending": true
  },
  "waitForFinish": 150
}
```

**Note**: Multi-TLD support depends on the specific actor. Check documentation.

---

### Configuration 4: Minimal Filtering (Discovery Mode)

**Use case**: Find all possible niche domains for manual review

```json
{
  "actorId": "username/expireddomains-scraper",
  "input": {
    "keyword": "roofer OR roofing",
    "tld": "co.uk",
    "minBacklinks": 1,
    "minRefDomains": 1,
    "maxResults": 200,
    "includeDeleted": true,
    "includePending": true
  },
  "waitForFinish": 240
}
```

**Expected results**: 50-150 domains (many will need filtering)

---

## Step 4: Executing the Actor

### Full MCP Tool Call Example

```typescript
// Step 1: Call the actor
const run = await mcp__apify__call-actor({
  actorId: "username/expireddomains-scraper",
  input: {
    keyword: "plumber OR plumbing",
    tld: "co.uk",
    minBacklinks: 5,
    minRefDomains: 5,
    maxResults: 100,
    includeDeleted: true,
    includePending: true,
    sortBy: "rd"
  },
  waitForFinish: 120  // Wait up to 2 minutes
});

// Response: { runId: "abc123xyz..." }

// Step 2: Get the results
const results = await mcp__apify__get-actor-output({
  runId: run.runId
});
```

### Monitoring Progress

If the actor is still running after `waitForFinish` timeout:

```typescript
// Check run status
const status = await mcp__apify__get-actor-run({
  runId: run.runId
});

// status.status values:
// "RUNNING" - Still processing
// "SUCCEEDED" - Completed successfully
// "FAILED" - Error occurred
// "ABORTED" - Manually stopped
```

---

## Step 5: Processing Results

### Expected Output Format

```json
{
  "items": [
    {
      "domain": "example-plumbing.co.uk",
      "tld": "co.uk",
      "backlinks": 234,
      "refDomains": 28,
      "domainPop": 5,
      "age": "12 years",
      "status": "deleted",
      "deletionDate": "2026-01-20",
      "availableDate": "2026-01-25"
    },
    // ... more domains
  ]
}
```

### Field Mapping

| Apify Field | Our Usage | Notes |
|-------------|-----------|-------|
| `domain` | Domain name | Primary identifier |
| `backlinks` | Initial filter | Cross-check with DataForSEO |
| `refDomains` | Initial filter | Cross-check with DataForSEO |
| `domainPop` | Popularity score | expireddomains.net metric |
| `age` | Scoring factor | Parse to years |
| `status` | Availability | "deleted", "pending", "available" |
| `deletionDate` | Registration timing | When domain was/will be deleted |

### Data Extraction

```typescript
// Extract domain list for DataForSEO enrichment
const domains = results.items.map(item => item.domain);

// Filter by minimum criteria (optional pre-filter)
const filteredDomains = results.items
  .filter(item => item.refDomains >= 5)
  .filter(item => item.status === "deleted")
  .map(item => item.domain);
```

---

## Step 6: Handling Rate Limits

### Apify Rate Limits

**Free tier**:
- 10,000 platform credits/month
- Actor runtime varies (typically 1-10 credits per run)

**Paid tier**:
- Higher limits based on subscription

### Best Practices

1. **Batch processing**: Don't run multiple actors simultaneously
2. **Wait between calls**: Add 2-3 second delays between actor calls
3. **Use reasonable maxResults**: Don't request 1000+ results in one run
4. **Cache results**: Save actor output to avoid re-running

### Example Rate Limit Handling

```typescript
// Process with delay
async function runActorWithDelay(config) {
  const run = await mcp__apify__call-actor(config);
  
  // Wait for completion
  await delay(5000);  // 5 second buffer
  
  return await mcp__apify__get-actor-output({ runId: run.runId });
}
```

---

## Troubleshooting

### Problem 1: No Results Returned

**Possible causes**:
1. Search criteria too strict
2. No domains match keyword
3. TLD filter too restrictive

**Solutions**:

**A. Broaden keyword search**
```json
// Before (too specific)
"keyword": "emergency plumber london"

// After (broader)
"keyword": "plumber OR plumbing"
```

**B. Relax filters**
```json
// Before (too strict)
{
  "minBacklinks": 20,
  "minRefDomains": 15,
  "tld": "co.uk"
}

// After (relaxed)
{
  "minBacklinks": 3,
  "minRefDomains": 3,
  "tld": "co.uk|com"
}
```

**C. Increase maxResults**
```json
"maxResults": 200  // Instead of 50
```

---

### Problem 2: Actor Timeout

**Symptoms**: `waitForFinish` expires before completion

**Solutions**:

**A. Increase timeout**
```json
"waitForFinish": 300  // Maximum 5 minutes
```

**B. Check status separately**
```typescript
// Don't wait immediately
const run = await mcp__apify__call-actor({
  actorId: "...",
  input: {...},
  waitForFinish: 0  // Return immediately
});

// Check later
await delay(30000);  // Wait 30 seconds
const results = await mcp__apify__get-actor-output({
  runId: run.runId
});
```

**C. Reduce maxResults**
```json
"maxResults": 50  // Process in smaller batches
```

---

### Problem 3: Actor Not Found

**Error**: "Actor with ID 'xyz' not found"

**Solutions**:

**A. Re-search for actor**
```typescript
const actors = await mcp__apify__search-actors({
  query: "expired domains"
});

// Use a different actor ID
const actorId = actors.results[0].id;
```

**B. Check for typos in actorId**

**C. Use alternative actor**

**D. Fallback to manual search** (see below)

---

### Problem 4: Unexpected Result Format

**Issue**: Output structure differs from expected

**Solution**: Inspect actual output and adapt

```typescript
const results = await mcp__apify__get-actor-output({runId});

// Log to understand structure
console.log(JSON.stringify(results, null, 2));

// Adapt field mapping
const domains = results.items.map(item => ({
  domain: item.Domain || item.domain || item.name,
  backlinks: item.Backlinks || item.backlinks || item.bl,
  refDomains: item.RefDomains || item.refDomains || item.rd
}));
```

---

## Fallback Strategy: Manual Search

If Apify actors are unavailable or failing, provide manual instructions:

### Manual Process

**Inform user**:
```
I'm unable to access Apify actors at the moment. Here's how to manually search for expired domains:

1. Visit: https://www.expireddomains.net/deleted-domains/

2. Apply these filters:
   - Keyword: [niche keyword]
   - TLD: .co.uk
   - Min Backlinks: 5
   - Min Referring Domains: 5

3. Sort by: Referring Domains (descending)

4. Export the results (CSV download)

5. Share the CSV with me and I'll run DataForSEO enrichment and scoring.
```

### Processing Manual CSV

If user provides a CSV:

```typescript
// Parse CSV (assuming standard format)
const domains = csvData
  .split('\n')
  .slice(1)  // Skip header
  .map(row => {
    const [domain, bl, rd, ...rest] = row.split(',');
    return {
      domain: domain.trim(),
      backlinks: parseInt(bl),
      refDomains: parseInt(rd)
    };
  });

// Proceed with DataForSEO enrichment
```

---

## Alternative Data Sources

If expireddomains.net actors fail, consider these alternatives:

### 1. FreshDrop.net Scrapers
Search Apify for: `"freshdrop" OR "freshdrop.net"`

### 2. Wayback Machine + Namecheap
- Use Wayback Machine to find historical sites
- Check Namecheap for availability

### 3. Manual Monitoring Services
- ExpiredDomains.net (manual use)
- DomCop
- FreshDrop.com

---

## Cost Optimization

### Minimizing Apify Costs

1. **Use precise keywords** - Fewer irrelevant results
2. **Set appropriate maxResults** - Don't over-request
3. **Cache results** - Save to file, don't re-run
4. **Batch processing** - Run once per niche, not multiple times
5. **Use filters aggressively** - Pre-filter before DataForSEO enrichment

### Example Cost-Efficient Workflow

```typescript
// Run once per niche
const plumbingDomains = await runApifyActor({
  keyword: "plumber OR plumbing",
  maxResults: 100
});

// Save to file
await saveToFile('plumbing-domains.json', plumbingDomains);

// Only enrich top candidates (based on Apify metrics)
const topDomains = plumbingDomains.items
  .filter(d => d.refDomains >= 8)
  .slice(0, 30);  // Only top 30

// Run DataForSEO only on these
for (const domain of topDomains) {
  const metrics = await getDataForSEOMetrics(domain);
  // ... score and save
}
```

---

## Testing & Validation

### Test Actor Configuration

Before running with strict filters, test with broad settings:

```json
{
  "keyword": "test",
  "tld": "co.uk",
  "minBacklinks": 1,
  "maxResults": 5,
  "waitForFinish": 60
}
```

**Expected**: Should return 5 domains quickly (validates actor works)

### Validate Results

Check that returned domains:
1. Match the keyword (at least loosely)
2. Have the correct TLD
3. Meet minimum backlink criteria
4. Are actually expired/available

---

## Version History

- **v1.0** (2026-01-25): Initial Apify setup documentation
