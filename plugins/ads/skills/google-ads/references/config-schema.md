# Configuration Schema

## google-ads.config.json

```typescript
interface GoogleAdsBusinessConfig {
  business: {
    name: string;           // Business name
    industry: string;       // Industry/niche
    website: string;        // Main website URL
    phone: string;          // Contact phone
  };

  locations: {
    primaryRegion: string;  // Main region name
    geoTargetIds: string[]; // Google Geo Target IDs
    serviceAreas: Array<{
      slug: string;         // URL-safe identifier
      name: string;         // Display name
      priority: "high" | "medium" | "low";
      landingPage?: string; // Landing page path
    }>;
  };

  services: Array<{
    slug: string;           // URL-safe identifier
    name: string;           // Service name
    keywords: string[];     // Seed keywords
    isEmergency?: boolean;  // Emergency service flag
  }>;

  usps: {
    experience?: string;    // Years of experience
    availability?: string;  // Service hours
    warranty?: string;      // Warranty offered
    rating?: {
      score: number;
      platform: string;
    };
    freeQuote?: boolean;
    familyOwned?: boolean;
  };

  campaigns: {
    defaultBudget: number;  // Daily budget in GBP
    startPaused: boolean;   // Always true
  };

  account: {
    customerId: string;     // Google Ads customer ID
    loginCustomerId?: string; // MCC account ID if applicable
  };
}
```

## .env Credentials

```
GOOGLE_ADS_CLIENT_ID=your-client-id.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=your-client-secret
GOOGLE_ADS_DEVELOPER_TOKEN=your-developer-token
GOOGLE_ADS_CUSTOMER_ID=123-456-7890
GOOGLE_ADS_REFRESH_TOKEN=your-refresh-token
```
