# Diagnose Meta Ad Performance

### How to use this file
Symptoms in the left column → likely causes → specific commands to run. Work top-down; the order reflects how often each cause is the actual culprit on low-budget accounts.

### The five diagnostic axes
Every "ads aren't working" issue is one (or more) of:
1. **Signal** — pixel/CAPI not firing properly, EMQ too low
2. **Creative** — under-volume, under-diverse, fatigued
3. **Audience** — too narrow, wrong intent
4. **Offer / page** — the ad worked, the page didn't
5. **Patience** — not yet out of learning phase

If you can't immediately tell which, **always check signal first** (see `conversions-api-setup.md`). It's the most common root cause and breaks every metric downstream.

### Decision tree — the five common symptoms

#### A) "No conversions / no leads at all"
1. **Signal check first.** Run:
   ```bash
   meta ads insights get --date-preset last_14d \
     --fields spend,impressions,clicks,actions,cost_per_action_type \
     --campaign-id <ID> -o json | jq '.[].actions'
   ```
   If `actions` is empty or missing your conversion event entirely → Pixel/CAPI broken. Open Events Manager test-events tab, fix CAPI before doing anything else. See `conversions-api-setup.md`.
2. If `actions` shows clicks/impressions but no `lead` or `purchase` → page or form broken. Test the form yourself. Check that the conversion event fires on submit.
3. If `actions` shows the event but spend ≥ £100 with zero conversions → wrong audience or wrong offer. Refresh creative angle (try the *objection* angle from `andromeda-creative-system.md`); broaden audience.

#### B) "CPL / CPA is 2-3× target"
Order of investigation:
1. **Out of learning phase?** Frequency <2.0 and ad set has <50 conversions/week → still learning. Don't conclude anything yet. Wait 7-14 days.
2. **Creative diversity** — count distinct concepts in the ad set:
   ```bash
   meta ads ad list --campaign-id <ID> -o json | jq 'length'
   ```
   <10 distinct concepts → under-fed Andromeda. Add 5-10 new hooks (see `andromeda-creative-system.md`).
3. **Frequency check** — break down by ad:
   ```bash
   meta ads insights get --date-preset last_7d \
     --fields spend,frequency,ctr,cost_per_action_type \
     --campaign-id <ID> --breakdown publisher_platform
   ```
   Frequency >3 and CTR dropping → fatigue. Refresh bottom 30%.
4. **Optimisation event volume** — if optimising on Purchase/Lead with <50/week, you're starving the algo. Switch to higher-funnel proxy (Initiate Checkout / Lead Form Open).
5. **Audience tightness** — if Detailed Targeting reach <500K and CPM rising, audience is too narrow. Broaden or move to Advantage+ Audience.

#### C) "CTR is low (<1.0% Feed / <1.5% Reels)"
Almost always creative. Order:
1. **Hooks** — first 3 seconds. Check the literal first frame / opening line of bottom-CTR ads. Replace generic hooks with specific ones (see `andromeda-creative-system.md`).
2. **Format mix** — break down by placement:
   ```bash
   meta ads insights get --date-preset last_14d \
     --fields ctr,cpc,actions \
     --campaign-id <ID> --breakdown publisher_platform
   ```
   If Reels CTR >> Feed CTR → ship more 9:16. If Feed >> Reels → reverse.
3. **Audience-creative mismatch** — testimonials at cold audiences, pain-point hooks at warm audiences. Re-map angle to funnel stage.

#### D) "Good CTR but no conversions"
The ad worked; the page didn't. Order:
1. **Page load + mobile UX** — open on real mobile. >3s load time = problem. Check Core Web Vitals.
2. **Promise mismatch** — does the page deliver what the ad implied? Run an audit pass.
3. **Form / checkout friction** — too many fields, hidden costs, slow checkout. See `form-cro` skill.
4. **Trust signals** — reviews, guarantees, named human. Cold ad traffic needs more trust than the ad alone provides.

#### E) "ROAS / CPL was good, now it isn't"
1. **Frequency creep**:
   ```bash
   meta ads insights get --date-preset last_30d \
     --time-increment weekly \
     --fields frequency,ctr,cost_per_action_type \
     --campaign-id <ID>
   ```
   Frequency rising weekly → audience saturation. Add net-new creative or expand audience.
2. **Algorithm reset** — recent edits (budget >20%, audience, optimisation event) restart learning. Check change history in Ads Manager.
3. **External factor** — major news/event in the niche, seasonality, competitor launching. Cross-check with web traffic dashboards.

### Field cheatsheet
```bash
# Always-useful baseline
--fields spend,impressions,clicks,ctr,cpc,reach,frequency

# Lead-gen diagnostic
--fields spend,actions,cost_per_action_type,frequency

# E-com / info product
--fields spend,actions,cost_per_action_type,purchase_roas,frequency

# Cross-platform breakdown (Reels vs Feed vs Stories)
--breakdown publisher_platform   # facebook|instagram
--breakdown platform_position    # feed|reels|story|...
```

### What never works
- Pausing ads under £20 spend
- Editing budget by >20% mid-learning
- Killing the lowest-CTR ad without checking its conversions
- "Just add more audiences" — you're rarely audience-limited; usually creative-limited
- Comparing 2026 7-day-click ROAS to 2025 7-day-view ROAS (different denominator — see `current-state-2026.md`)

### Escalation order
If after 14 days at adequate spend you've:
- Verified signal (CAPI healthy, EMQ ≥6)
- Run 15+ distinct creatives
- Tried both Detailed Targeting and Advantage+ Audience
- Refreshed creative twice

…and CPL/ROAS is still off — the problem is the **offer or the page**, not the ads. Stop iterating on Meta and audit the funnel.
