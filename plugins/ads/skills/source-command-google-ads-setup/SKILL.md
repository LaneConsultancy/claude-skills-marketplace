---
name: "source-command-google-ads-setup"
description: "Configure Google Ads credentials and business settings"
---

# source-command-google-ads-setup

Use this skill when the user asks to run the migrated source command `google-ads-setup`.

## Command Template

# Google Ads Setup

Configure Google Ads credentials and business settings for the current project.

## Current Status

Google Ads is **already configured** for the Lane Consultancy project:
- **Customer ID**: `8819246831` (sub-account under MCC `5151905694`)
- **Credentials**: All stored in `.env.local`
- **Config**: `google-ads.config.json` in project root
- **Library**: `src/lib/google-ads/` with campaigns, keywords, and reporting modules
- **Test script**: `npx tsx scripts/test-google-ads.ts`

## If Re-Setup Is Needed

### Step 1: Check Connection

Run: `npx tsx scripts/test-google-ads.ts`

### Step 2: If Token Expired (invalid_grant error)

Run: `npx tsx scripts/get-google-ads-token.ts`
- Opens browser for OAuth consent
- Generates new refresh token
- Update `GOOGLE_ADS_REFRESH_TOKEN` in `.env.local`

### Step 3: For a New Project

Look for `.env.local` with required variables:
- `GOOGLE_ADS_CLIENT_ID`
- `GOOGLE_ADS_CLIENT_SECRET`
- `GOOGLE_ADS_DEVELOPER_TOKEN`
- `GOOGLE_ADS_CUSTOMER_ID`
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID`
- `GOOGLE_ADS_REFRESH_TOKEN`

Copy credentials from an existing project if using the same MCC account. Only the `GOOGLE_ADS_CUSTOMER_ID` changes per sub-account.

### Step 4: Verify

Run test script to confirm connection and list campaigns.

## Using the API in Code

```ts
import { listCampaigns, getKeywordIdeas, getAccountOverview, DateRanges } from '@/lib/google-ads';
```

The plugin scripts at `~/.Codex/plugins/google-ads-skill/scripts/` also work — they auto-detect `.env.local` in the cwd.
