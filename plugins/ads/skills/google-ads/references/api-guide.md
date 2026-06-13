# Google Ads API Guide

## Authentication

Uses OAuth 2.0 with refresh tokens. Required credentials:
- Client ID and Secret (from Google Cloud Console)
- Developer Token (from Google Ads account)
- Refresh Token (obtained via OAuth flow)
- Customer ID (Google Ads account ID)

## Client Setup

```typescript
import { GoogleAdsApi } from 'google-ads-api';

const client = new GoogleAdsApi({
  client_id: process.env.GOOGLE_ADS_CLIENT_ID,
  client_secret: process.env.GOOGLE_ADS_CLIENT_SECRET,
  developer_token: process.env.GOOGLE_ADS_DEVELOPER_TOKEN,
});

const customer = client.Customer({
  customer_id: process.env.GOOGLE_ADS_CUSTOMER_ID,
  refresh_token: process.env.GOOGLE_ADS_REFRESH_TOKEN,
});
```

## Common Operations

### List Campaigns
```typescript
const campaigns = await customer.query(`
  SELECT campaign.id, campaign.name, campaign.status
  FROM campaign
  WHERE campaign.status != 'REMOVED'
`);
```

### Create Campaign
```typescript
const campaign = await customer.campaigns.create({
  name: 'Campaign Name',
  advertising_channel_type: 'SEARCH',
  status: 'PAUSED',
  campaign_budget: budgetResourceName,
  // ...
});
```

## Rate Limits

- 15,000 operations per day for basic access
- Batch operations where possible
- Use GAQL for efficient queries
