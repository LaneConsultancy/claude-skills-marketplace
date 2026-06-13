# Conversions API Setup

The local `meta` CLI manages **Pixels (now called "datasets")** but does **not** send Conversions API events itself. CAPI events are sent server-to-server to `graph.facebook.com/v{version}/{pixel_id}/events`. Use the official Python or Node SDK for that, or a middleware (Stape, CAPI Gateway). There is no `meta ads dataset send-event` command — don't expect one.

## Why CAPI is non-optional now (2026)
- iOS 14.5 (2021) onward + ITP/ETP cookie restrictions: pixel-only setup loses 40-60% of attributable signal
- AEM 8-event cap was removed June 2025, but signal *quality* still depends on server-side events
- Meta's auction now penalises low-signal accounts (Andromeda needs match-quality data to retrieve correctly)
- The legacy Offline Conversions API was retired May 2025 — every offline event now flows through standard CAPI
- "Conversion Leads" performance goal *requires* CRM CAPI to work properly

If your account is pixel-only in 2026, fix this before optimising anything else. See `diagnose-performance.md` — it's the first thing to check on any "ads aren't working" diagnosis.

## Pixel vs Dataset terminology
Meta renamed the Facebook Pixel to **"Dataset"** in 2024. Same object, same ID space. The CLI uses `dataset`:
```bash
meta ads dataset list
meta ads dataset get <PIXEL_ID>
meta ads dataset create --name "Site Pixel"
meta ads dataset connect <PIXEL_ID> --ad-account-id act_XXX
```

## Setup options (pick one)
| Option | Effort | Cost | Match quality | Best for |
|--------|--------|------|--------------|----------|
| **CAPI Gateway (Meta-managed)** | Low (no-code) | Hosting £8-30/mo (Stape from $10/pixel/mo) | High | Most accounts |
| **Partner integration** (Shopify, Wix, GTM Server-side, Stape) | Low-medium | Plan-dependent | High | Existing platform users |
| **Manual server implementation** | Highest | Dev time only | Highest possible | Bespoke stacks / Next.js / Cloudflare Workers |

For the user's stack — Next.js on Vercel, Cloudflare Workers, Tally forms — **manual server implementation via a CF Worker** mirrors the existing Google Ads conversion importer (`ww-conversion-importer`). Cost: £0/mo extra; reuses existing infra patterns.

## Required events
**Lead-gen accounts:**
- `PageView`
- `Lead` (form submission — server-side from Tally webhook → Worker → CAPI)
- `CompleteRegistration` (if applicable)

**E-commerce / info product accounts:**
- `PageView`
- `ViewContent` (sales page view)
- `AddToCart` / `InitiateCheckout`
- `Purchase`

Send each event via **both Pixel (browser) and CAPI (server)** with a shared `event_id` so Meta can deduplicate within a 48-hour window.

## Event Match Quality (EMQ) benchmarks
Score 1-10 per event. Meta's stated baseline: 6/10. Diminishing returns above 8.

| Event tier | Target EMQ | Notes |
|-----------|-----------|-------|
| Top-funnel (PageView, ViewContent) | 4.5-7 | Hard to enrich; user often anonymous |
| Mid-funnel (AddToCart, InitiateCheckout) | 6-8 | Email/IP often available |
| Bottom-funnel (Purchase, Lead) | 7.5-9.3 | Should always have email + phone hashed |

Source: [Triple Whale](https://www.triplewhale.com/blog/event-match-quality)

## Parameters to pass (every event)
- `event_name` — standard (`Lead`, `Purchase`, etc.)
- `event_time` — Unix timestamp
- `event_id` — shared with the browser pixel for deduplication
- `event_source_url` — full URL where the event happened
- `action_source` — `website` / `system_generated` / `physical_store`
- **User data (all hashed SHA-256, lowercased, trimmed):**
  - `em` — email (always send if you have it)
  - `ph` — phone (E.164 format before hashing)
  - `fn`, `ln` — first/last name
  - `external_id` — your internal user ID
- **Browser-only enrichment (passed through from the pixel cookie):**
  - `fbp` — Facebook browser ID cookie
  - `fbc` — Facebook click ID cookie (built from `fbclid` URL param)
  - `client_ip_address`, `client_user_agent`

The two parameters that move EMQ most: hashed email + `fbc` (built from `fbclid`). Capture `fbclid` from URL on first touch into a long-TTL cookie (90 days, the same way Google's `gclid` is captured for Tally forms in Weather Wizard).

## Deduplication
- Same `event_name` + `event_id` from both pixel and CAPI within 48 hours = deduped
- Aim for **≥70% pixel/server overlap** ([Analyzify](https://analyzify.com/hub/event-deduplication-for-meta-conversions))
- Below 50% means dedup logic is broken — usually missing or mismatched `event_id`s

## Domain verification
Still required as of 2026 for any domain you optimise on. Without it you can't:
- Configure web events for that domain
- Use Conversion Leads performance goal
- Run remarketing audiences against page-level URL events

Add the meta tag or DNS TXT record per [Meta Domain Verification docs](https://www.facebook.com/business/help/286768115176155).

## Quick verification flow
```bash
# 1. List datasets/pixels
meta ads dataset list

# 2. Confirm the pixel is connected to the ad account
meta ads dataset get <PIXEL_ID>

# 3. Confirm events are arriving via CAPI in the Events Manager UI
#    (CLI does not surface event-level diagnostics yet — use Events Manager:
#    https://business.facebook.com/events_manager2/list/pixel/<PIXEL_ID>/test_events )
```

## Common mistakes
| Mistake | Symptom | Fix |
|---------|---------|-----|
| Pixel-only setup | CPL/CPA looks 2-3× higher than 2024 baseline | Add CAPI |
| Mismatched event_ids | Dedup overlap <50%; Meta double-counts | Generate one UUID, use in both pixel + CAPI |
| Sending unhashed PII | Events rejected | SHA-256 lowercase trimmed |
| Forgetting `fbclid` capture | EMQ stuck at 4-5 | Capture `fbclid` → `_fbc` cookie 90-day TTL |
| Skipping domain verification | Conversion Leads goal won't activate | Verify domain in Business Settings |
