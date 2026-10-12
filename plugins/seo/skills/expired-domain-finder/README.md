# Expired Domain Finder Skill

A comprehensive Claude Code skill for discovering and evaluating expired domains suitable for Private Blog Network (PBN) building.

## Quick Start

**Trigger the skill with any of these phrases:**
- "find expired domains"
- "expired domain finder"
- "pbn domains"
- "find domains for plumbing" (or any niche)

## What It Does

This skill automates the entire expired domain discovery workflow:

1. **Discovers** expired domains using Apify scrapers
2. **Enriches** each domain with SEO metrics from DataForSEO
3. **Scores** domains based on comprehensive quality criteria
4. **Generates** a detailed CSV report with registration links
5. **Presents** top recommendations with actionable insights

## Files in This Skill

### Main Skill File
- **SKILL.md** - Complete workflow instructions for Claude to execute

### Reference Files
- **references/domain-scoring.md** - Detailed scoring algorithm and red flag detection
- **references/niche-keywords.md** - Pre-built keyword lists for 20+ service niches
- **references/apify-setup.md** - Apify actor configuration and troubleshooting

## Output

The skill generates two outputs:

### 1. CSV Export
Located in: `/Users/georgelane/.claude/scratchpad/expired-domains-[niche]-[timestamp].csv`

Columns include:
- Domain name
- Quality score (0-100)
- Rating (Excellent/Good/Fair/Poor)
- Domain Rating (DR)
- Referring domains count
- Top anchor texts
- Red flags detected
- Direct Namecheap registration link

### 2. Console Summary
Top 10 domain recommendations with:
- Score breakdown
- Key metrics
- Red flags/warnings
- Direct registration links

## Supported Niches

Pre-configured keyword lists for:
- Heating & Boilers
- Plumbing
- Electrical
- Roofing
- Building & Construction
- Carpentry & Joinery
- Painting & Decorating
- Gardening & Landscaping
- Cleaning Services
- Locksmith
- Pest Control
- Handyman Services
- And many more...

Custom niches are also supported - just specify your industry and Claude will adapt.

## Default Filters

- **TLD**: .co.uk only
- **Minimum DR**: 5
- **Minimum Referring Domains**: 5
- **Max Results**: 100 domains to check

All filters can be customized when triggering the skill.

## MCP Tools Required

This skill uses the following MCP integrations:

- **Apify** - For domain discovery (expireddomains.net scrapers)
- **DataForSEO** - For backlink metrics and anchor text analysis

Make sure these MCP servers are configured in your Claude Code setup.

## Example Usage

```
You: find expired domains for heating

Claude: What niche or industry are you targeting? 
        I see you mentioned "heating" - I'll search for domains 
        related to heating, boilers, and gas engineering.
        
        Would you like to customize filters? Current defaults:
        - TLD: .co.uk
        - Min DR: 5
        - Min Referring Domains: 5
        
        Reply 'continue' to proceed or 'yes' to customize.

You: continue

Claude: [Executes workflow]
        
        Found 47 expired domains for heating
        
        Top 10 Recommendations:
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        
        1. gas-heating-london.co.uk (Score: 89 - Excellent)
           DR: 28 | RDs: 52 | Age: 14 years
           Top Anchors: gas heating, london heating, naked URL
           ✓ Clean backlink profile
           ✓ Niche relevant
           Register: https://namecheap.com/...
        
        [... continues with full report and CSV export]
```

## Scoring Methodology

Domains are scored 0-100 based on:

**Positive Factors:**
- Domain age (older = better)
- Domain Rating/Authority
- Number of referring domains
- Clean anchor text distribution
- Niche relevance
- TLD quality

**Negative Factors:**
- Spammy anchors (gambling, pharma, adult)
- PBN footprints
- Foreign language spam
- Suspicious backlink patterns
- Thin backlink profiles

**Score Ranges:**
- 80-100: Excellent (strong PBN candidate)
- 60-79: Good (worth considering)
- 40-59: Fair (proceed with caution)
- 0-39: Poor (avoid)

## Fallback Handling

The skill gracefully handles common issues:

- **No Apify results**: Suggests broadening search criteria
- **DataForSEO failures**: Marks domains as "metrics unavailable" but still includes
- **Rate limits**: Implements batching and delays
- **Actor unavailable**: Provides manual search instructions

## Advanced Features

- **Parallel processing**: Enriches domains in batches for speed
- **Red flag detection**: Automatically flags spam indicators
- **Niche matching**: Cross-references keywords for relevance scoring
- **Registration links**: Direct Namecheap links for instant purchase

## Customization

Edit reference files to customize:

- **domain-scoring.md**: Adjust scoring weights and red flag keywords
- **niche-keywords.md**: Add new niches or keyword variations
- **apify-setup.md**: Configure different actors or parameters

## Contributing

This skill can be extended with:
- Additional data sources (Wayback Machine, WHOIS)
- Bulk availability checking
- Competitive analysis features
- Alternative TLD support

## Version

**v1.0** - Initial release (2026-01-25)

---

**Created by**: Claude Code
**Skill Type**: Domain Research & SEO
**MCP Dependencies**: Apify, DataForSEO
