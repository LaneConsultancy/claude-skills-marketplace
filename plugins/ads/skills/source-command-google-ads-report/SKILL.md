---
name: "source-command-google-ads-report"
description: "Generate Google Ads performance reports"
---

# source-command-google-ads-report

Use this skill when the user asks to run the migrated source command `google-ads-report`.

## Command Template

# Google Ads Performance Report

Generate performance reports for Google Ads campaigns.

## Workflow

### Step 1: Load Configuration

Read `google-ads.config.json` for account details.

### Step 2: Generate Report (Subagent)

Spawn `general-purpose` subagent with prompt:
```
Generate Google Ads performance report.

Account: {config.account.customerId}

First try the project's local library (if src/lib/google-ads/ exists):
  npx tsx -e "import { getAccountOverview, DateRanges } from './src/lib/google-ads'; ..."

Otherwise fall back to: npx tsx ~/.Codex/plugins/google-ads-skill/scripts/performance-report.ts

Analyze the data and provide:
1. Account overview (spend, clicks, conversions, CPA)
2. Top 5 performing campaigns
3. Bottom 3 performing campaigns (need attention)
4. Top 10 keywords by conversions
5. Keywords with high spend, low conversions
6. Quality score distribution
7. 3-5 actionable recommendations

Write full report to google-ads-report.json
Return summary only (key metrics and recommendations)
```

### Step 3: Present Summary

Show user:
- Key metrics (7-day and 30-day)
- Top/bottom performers
- Recommendations
- Path to full report JSON

## Report Options

- `--days 30` - Report period (default: 30)
- `--campaign "Campaign Name"` - Filter to specific campaign
- `--export csv` - Export to CSV format
