---
name: "source-command-google-ads-optimize"
description: "Get optimization suggestions for Google Ads campaigns"
---

# source-command-google-ads-optimize

Use this skill when the user asks to run the migrated source command `google-ads-optimize`.

## Command Template

# Google Ads Optimization

Get actionable optimization suggestions for Google Ads campaigns.

## Workflow

### Step 1: Load Configuration

Read `google-ads.config.json` for account details.

### Step 2: Analyze Account (Subagent)

Spawn `general-purpose` subagent with prompt:
```
Analyze Google Ads account for optimization opportunities.

Account: {config.account.customerId}

Run performance report script, then analyze:

1. Search Terms Analysis
   - Identify irrelevant search terms to add as negatives
   - Find high-converting terms to add as keywords

2. Quality Score Review
   - Keywords with QS < 6
   - Landing page issues
   - Ad relevance problems

3. Budget Optimization
   - Campaigns limited by budget
   - Campaigns with unspent budget
   - Bid adjustment opportunities

4. Ad Performance
   - RSAs with poor asset performance
   - Headlines/descriptions to replace

5. Structure Review
   - Ad groups with too many keywords
   - Missing ad group themes

Prioritize recommendations by impact (high/medium/low).

Return: Top 10 actionable recommendations with priority and expected impact.
```

### Step 3: Present Recommendations

Show user prioritized list:
1. [HIGH] Add negative keywords: "free", "diy" (saving ~£X/month)
2. [HIGH] Increase budget for Campaign X (limited by budget, high ROAS)
3. [MEDIUM] Improve QS for keyword Y (current: 4, target: 7+)
...

Offer to implement specific recommendations.
