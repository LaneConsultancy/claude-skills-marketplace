# Lead Gen on Low Budgets (£20-100/day)

### TL;DR
1. Use the **Leads** objective with **Advantage+ Leads** defaults
2. Set performance goal to **"conversion leads"** with CAPI feeding lead events
3. Send to **Instant Form with conditional logic + Higher Intent** unless you have a strong landing-page reason not to
4. **ABO** at this budget tier (CBO starves ad sets <£30/day)
5. **One ad set, 10-20 distinct creatives** (Andromeda — see `andromeda-creative-system.md`)
6. If you can't hit 50 leads/week, optimise on Lead Form Open (proxy event) instead of Lead

### The math: why your budget matters
Meta's learning phase wants ~50 conversions per ad set per week. Weekly budget should therefore be **~50 × target CPA** to exit learning cleanly.

| Target CPL | Min weekly budget | Min daily |
|-----------|-------------------|-----------|
| £10 | £500 | £70 |
| £20 | £1,000 | £143 |
| £30 | £1,500 | £215 |
| £50 | £2,500 | £360 |

If you're below this, you have two choices:
- **Optimise on a higher-funnel event** (Lead Form Open, Landing Page View) so you hit 50/week of *something*. Less perfect signal, but you'll exit learning.
- **Accept long horizons.** 7-14 day evaluation windows minimum; metrics under 50 weekly conversions are statistically thin. Don't kill ads early.

### Campaign settings (the defaults that work)
- **Objective**: Leads (`--objective outcome_leads`)
- **Performance goal**: "Conversion leads" (set in Ads Manager — not exposed in `meta ads campaign create`; the CLI creates the campaign, you finalise lead-gen specifics in the UI or via SDK)
- **Budget**: ABO. Set at adset level. CBO only when you have a confirmed winner you want to scale.
- **Audience**: Advantage+ Audience with custom audiences + lookalikes as *suggestions* (don't trip "Advantage+ Off"). At <£30/day with no signal yet, use Detailed Targeting until you have ~100 leads, then switch.
- **Placements**: Advantage+ Placements (default). Almost never disable.
- **Optimisation event**: Lead (or Lead Form Open if volume too low — see math above).
- **Attribution**: 7-day click + 1-day view (no longer optional — see `current-state-2026.md`).

### Instant Form vs Landing Page
| Use Instant Form when... | Use Landing Page when... |
|--------------------------|--------------------------|
| You want max volume / minimal friction | You need lead quality > volume |
| Mobile-first audience | Desktop-heavy / B2B audience |
| Form completion is the conversion | You can run remarketing pixels & longer storytelling |
| Lead value <£100 | Lead value >£200 (CPQO usually wins on landing page) |

If using Instant Forms:
- **Higher Intent** form type by default (review step before submit) — slows accidental submits
- **Conditional logic** — Meta cites +62% lead-to-customer rate vs plain forms ([SMK](https://smk.co/meta-releases-new-lead-generation-guidelines/))
- **Rich Creative Instant Forms** for product-style or social-proof sections ([Leadsync](https://leadsync.me/blog/rich-creative-instant-forms/))
- **CRM integration**: native partner > Zapier > webhook. Send Lead event back via CAPI for the conversion-leads performance goal to work.

### Concrete launch sequence (the actual flow)
```bash
# 1. Sanity check
meta auth status
meta ads adaccount current

# 2. Create campaign (PAUSED by default — good)
meta ads campaign create \
  --name "LEADS_LowBudget_2026-05_Cold" \
  --objective outcome_leads \
  --daily-budget 3000   # = $30.00 ≈ £24

# 3. List to grab the new campaign ID
meta ads campaign list -o json | jq '.[] | select(.name=="LEADS_LowBudget_2026-05_Cold")'

# 4. Finalise ad set in UI or SDK (CLI doesn't yet expose all lead-gen knobs)
#    — Conversion Leads performance goal
#    — Instant Form with Higher Intent + conditional logic
#    — Audience suggestions
#    — Optimisation event: Lead

# 5. Build creatives (10-20 distinct concepts — see andromeda-creative-system.md)
meta ads creative create --name "..." --image ... --page-id ... --body "..." --link-url ...

# 6. Daily monitoring
meta ads insights get --date-preset last_7d \
  --fields spend,impressions,clicks,ctr,cpc,actions,cost_per_action_type,frequency \
  --campaign-id <ID>
```

### What to do in week 1
- Day 0-3: do nothing. Learning phase. Resist the urge to edit.
- Day 4: check frequency, CTR, and whether you have any leads at all. Do not kill ads with <£20 spend.
- Day 7: full review. Cut bottom 30% of creatives. Add 3-5 new concepts.
- Day 14: full review. If CPL is within 1.5× target, scale by 20% (no more — large jumps reset learning). If 2-3× target, refresh creative + check signal (see `diagnose-performance.md`).

### Common low-budget mistakes
| Mistake | Why it kills you | Fix |
|---------|------------------|-----|
| 5 ad sets × £6/day each | None exit learning | One ad set, full budget |
| Optimising on Purchase with 5 leads/week | No signal | Optimise on Lead Form Open until 50/week |
| Killing ads at day 3 | Learning phase | Wait 7+ days |
| Editing budget by >20% | Resets learning | Smaller increments |
| Pixel-only signal | Lost 40-60% post-iOS 14.5 | Set up CAPI — see `conversions-api-setup.md` |
| 3-6 creatives | Andromeda starves | 10-20 distinct concepts |
| CBO at £30/day | Starves ad sets | ABO until winners proven |

### When to escalate
- **No leads after £100 spent**: signal/audience problem (likely CAPI not firing). Run `meta ads insights get --fields spend,actions,cost_per_action_type` to confirm zero `actions`. See `diagnose-performance.md`.
- **CPL >2× target after 7 days**: creative problem first, then offer second. Refresh creative before changing audience.
- **CPL good but lead quality bad**: switch performance goal from "leads" to "conversion leads" if not already; tighten Instant Form (add qualifying questions; switch to landing page).
