# Info Product Launches on Low Budget (£50-100/day, 1+ ROAS)

### TL;DR
1. **Advantage+ Sales Campaigns** (the renamed/upgraded ASC successor) — `--objective outcome_sales`
2. Optimise on **Purchase** if you can hit ~50/week; otherwise **Initiate Checkout** as a proxy
3. **7-day click + 1-day view** (the only options post-Jan 2026)
4. Detailed Targeting > Advantage+ Audience under 50 weekly conversions
5. Single image / single video creative — **not** catalog (catalog is for 5+ SKUs)
6. 10-20 distinct creative concepts per ad set (see `andromeda-creative-system.md`)

### Why "info product on low budget" is harder than ecom on low budget
- One SKU, one price point — no catalog dynamics to lean on
- Higher AOV than typical ecom impulse buys (£47-997 typical) — 7-day click matters
- Buyer journey usually involves email or VSL between click and purchase — single-session attribution under-credits

So: optimise on a real conversion event, accept a longer evaluation window (10-14 days minimum), and treat the Meta dashboard as one input — not the only input. Cross-check with email signup rate, VSL view-through rate, and post-purchase survey.

### The 1+ ROAS math
Required CPA at typical info-product margin (digital good, ~95% margin):
- £47 product → £45 max CPA for 1 ROAS (most info launches die here)
- £97 product → £92 max CPA
- £197 product → £187 max CPA
- £497 product → £472 max CPA

Compounding: at £75/day = £2,250/month, you need to keep CPA below those numbers across the *full* spend, not just winning ads. Plan a 30-day evaluation horizon.

### Campaign settings
- **Objective**: Sales (`--objective outcome_sales`)
- **Budget**: ABO at this tier (£50-100/day) — see `current-state-2026.md` for why CBO starves below £30/day per set; even at £75-100/day single-set ABO usually wins for low-budget info launches
- **Optimisation event**:
  - Purchase if your funnel realistically does ≥50 purchases/week
  - **Initiate Checkout** as a proxy at lower volume (resist View Content — too noisy)
- **Audience**: Detailed Targeting at start. Switch to Advantage+ Audience (with custom + lookalikes as suggestions) once you have ~100 purchases of signal. At <£30/day or <50 conv/week, Advantage+ Audience usually under-performs ([Conversios](https://www.conversios.io/blog/meta-advantage-audience-vs-detailed-targeting-2026-guide/)).
- **Placements**: Advantage+ Placements
- **Attribution**: 7-day click + 1-day view (no longer optional)
- **Advantage+ Creative**: ON by default since Feb 2026. Selectively disable music if your VSL embeds music differently.

### Funnel structure (matters more than ad-account structure)
| Stage | Conversion event to track | Comments |
|-------|---------------------------|----------|
| Cold ad → VSL/sales page | ViewContent | Don't optimise on this |
| Sales page → email opt-in | Lead (custom event) | Useful proxy if you can't hit Purchase volume |
| Email/page → checkout | InitiateCheckout | **The good proxy event for low-budget launches** |
| Checkout → purchase | Purchase | The real one |

Send all events via **both Pixel and CAPI** with shared `event_id` for deduplication — see `conversions-api-setup.md`.

### Single-image/video vs catalog
| | Single creative | Catalog |
|--|------------------|---------|
| Best for | One info product, hook variations | 5+ SKUs / upsells / order-bump-rich funnels |
| Setup | `meta ads creative create ...` | `meta ads catalog ...` |
| Andromeda fit | Excellent — feeds it diversity | Underrated; needs catalog hygiene to win |

For most info products, single-image/video with 10-20 hook variations beats catalog. Catalog only earns its complexity when you have at least 5 SKUs.

### Concrete launch sequence
```bash
# 1. Sanity
meta auth status
meta ads adaccount current

# 2. Campaign (PAUSED by default)
meta ads campaign create \
  --name "SALES_InfoProduct_LaunchA_2026-05" \
  --objective outcome_sales \
  --daily-budget 7500   # $75 ≈ £60

# 3. Get the campaign ID
meta ads campaign list -o json | jq '.[] | select(.name | startswith("SALES_InfoProduct_LaunchA"))'

# 4. Finalise ad set in UI / SDK
#    — Optimise for Initiate Checkout (or Purchase if volume supports)
#    — Detailed Targeting (3-5 broad interest stacks)
#    — Single ad set, ABO

# 5. Build creatives — 10-20 distinct hooks
meta ads creative create --name "..." ...

# 6. Daily monitoring (use ROAS field)
meta ads insights get --date-preset last_7d \
  --fields spend,impressions,clicks,actions,cost_per_action_type,purchase_roas,frequency \
  --campaign-id <ID>
```

### Evaluation cadence
- **Day 0-3**: learning phase. Hands off.
- **Day 4-7**: kill ads with frequency >2.5 and zero ATC. Otherwise leave alone.
- **Day 7**: refresh bottom 30% of creatives. Add 3-5 new hooks.
- **Day 14**: ROAS check. If <0.7, problem is funnel/offer/creative — pause and review. If 0.8-1.2, scale 20%. If >1.5, scale 30-40% in one move (Andromeda tolerates bigger jumps than the old auction).

### When to give up vs keep iterating
| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Lots of ATC, no Purchase | Checkout friction (price, payment, trust) | Fix sales page, not ads |
| No ATC, decent CTR | Page or offer mismatch | Test alternative landing page / offer angle |
| No CTR | Creative or audience | Refresh creative + broaden audience |
| Good ROAS, can't scale | Audience saturation | Layer in lookalikes; introduce Advantage+ Audience |
| Erratic ROAS day-to-day | Below statistical threshold | Keep budget; lengthen evaluation window |

### Common pitfalls
- **Optimising on ViewContent** — too noisy at any spend tier; you'll get cheap clicks that never convert
- **Comparing to 7-day-view ROAS reports from 2025** — that window no longer exists; numbers will look "worse" by ~15-25%
- **Catalog before earning it** — overhead without the SKU diversity to feed it
- **Killing the launch at day 3** — info products almost always look broken in first 72h before email-driven purchases land
- **Ignoring email/VSL data** — Meta dashboard is one signal; cross-check funnel-level data weekly
