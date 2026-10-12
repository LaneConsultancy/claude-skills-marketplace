# Campaign Structure Best Practices

## Location-Based Campaigns

For businesses with multiple service areas:

```
Campaign: [Region] - [Service]
├── Ad Group: [City 1]
│   ├── Keywords: [service] [city1], [service] near [city1]
│   ├── RSA with [city1] in headlines
│   └── Negative: [city2], [city3] (cross-negatives)
├── Ad Group: [City 2]
│   └── ...
```

## Service-Based Campaigns

For businesses with multiple services:

```
Campaign: [Service Category]
├── Ad Group: [Specific Service 1]
│   ├── Keywords: specific service terms
│   └── RSA focused on that service
├── Ad Group: [Specific Service 2]
│   └── ...
```

## RSA Best Practices

- Pin location in position 1 for local businesses
- Include USP in position 2
- Mix headline types: benefit, feature, CTA, trust
- Use all 15 headline slots
- Use all 4 description slots

## Cross-Negative Keywords

Prevent location ad groups from competing:
- Each location ad group negatives the other locations
- Use EXACT match for cross-negatives
- Add at ad group level, not campaign level
