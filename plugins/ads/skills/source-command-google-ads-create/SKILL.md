---
name: "source-command-google-ads-create"
description: "Create new Google Ads campaigns with keyword research and ad copy"
---

# source-command-google-ads-create

Use this skill when the user asks to run the migrated source command `google-ads-create`.

## Command Template

# Google Ads Campaign Creation

Create new Google Ads campaigns with keyword research, ad copy generation, and proper structure.

## Workflow (Subagent Delegation)

This command coordinates 3 subagents to preserve context:

### Step 1: Load Configuration

Read `google-ads.config.json` from project root. Validate required fields.

### Step 2: Keyword Research (Subagent 1)

Spawn `general-purpose` subagent with prompt:
```
Research keywords for Google Ads campaigns using DataForSEO MCP.

Business: {config.business.name}
Industry: {config.business.industry}
Services: {config.services}
Locations: {config.locations.serviceAreas}

Tasks:
1. Use mcp__dataforseo__dataforseo_labs_google_keyword_ideas for each service + location combo
2. Use mcp__dataforseo__kw_data_google_ads_search_volume for volume data
3. Group keywords by service and location
4. Write full results to google-ads-keywords.json
5. Return summary: top 20 keywords by volume, total keyword count
```

### Step 3: Ad Copy Generation (Subagent 2)

Spawn `copywriter` subagent with prompt:
```
Generate Google Ads Responsive Search Ad copy.

Business: {config.business}
USPs: {config.usps}
Services: {config.services}
Locations: {config.locations.serviceAreas}

Character limits (STRICT):
- Headlines: 30 characters max (need 15 per ad)
- Descriptions: 90 characters max (need 4 per ad)
- Sitelink text: 25 characters
- Sitelink descriptions: 35 characters each
- Callouts: 25 characters

Create:
1. 15 headlines per service (mix of USP, service, location, CTA)
2. 4 descriptions per service
3. 6-8 sitelinks for account level
4. 8-10 callouts for account level

Write to google-ads-adcopy.json
Return: Sample of 5 headlines and 2 descriptions for preview
```

### Step 4: Preview and Confirm

Show user:
- Top keywords from research
- Sample ad copy
- Estimated campaign structure (X campaigns, Y ad groups)
- Confirmation: "Create campaigns? (All will be PAUSED)"

### Step 5: Campaign Creation (Subagent 3)

If confirmed, spawn `coder` subagent with prompt:
```
Create Google Ads campaigns using the standalone scripts.

Read:
- google-ads.config.json for business/account info
- google-ads-keywords.json for keywords
- google-ads-adcopy.json for ad copy

Run: npx tsx ~/.Codex/plugins/google-ads-skill/scripts/create-campaigns.ts

The script should:
1. Create campaigns (one per service or location, based on config)
2. Create ad groups with keywords (PHRASE match)
3. Create RSAs with headlines/descriptions
4. Add cross-negative keywords between location ad groups
5. Add account-level extensions

All campaigns MUST be created PAUSED.

Return: Campaign IDs and summary (X campaigns, Y ad groups, Z keywords)
```

## Dry Run Mode

If `--dry-run` flag provided, skip Step 5 and show what would be created.

## Safety

- All campaigns created PAUSED (mandatory, enforced in script)
- Preview before creation
- User must confirm before API calls
