# What Changed Recently — Meta Ads 2025-2026

## 1. Andromeda (Oct 2025 global rollout)

Meta's new personalised ads retrieval engine on NVIDIA Grace Hopper. 10,000× model complexity at the retrieval stage. Effect: shifts the system from audience-first to creative-first.

- 1 ad set × 25 creatives → +17% conversions, -16% cost (Meta internal)
- Advantage+ Creative users → +22% ROAS
- The old "max 6 ads per ad set" guidance is dead — feed it variety

Sources: [Meta Engineering](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/), [Jon Loomer](https://www.jonloomer.com/meta-andromeda/).

## 2. Attribution windows (Jan 2026)

| Status | Window |
|---|---|
| ❌ Removed | 7-day view |
| ❌ Removed | 28-day view |
| ✅ Default + only options | 7-day click + 1-day view |

Don't compare 2026 reports to 2025 directly — the windows are not equivalent. Source: [DOJO AI](https://www.dojoai.com/blog/meta-ads-attribution-2026-changes-fixes).

## 3. AEM 8-event limit removed (Jun 2025)

The Aggregated Event Measurement event-prioritisation cap is gone. AEM is now fully automated. You no longer need to manually prioritise eight events per domain. Source: [Conversios](https://www.conversios.io/blog/meta-aggregated-event-measurement/).

## 4. Offline Conversions API retired (May 2025)

All offline events now flow through standard Conversions API (CAPI). The legacy Offline Conversions endpoint no longer accepts new events. See `conversions-api-setup.md`.

## 5. ASC / AAC API deprecation (May 2026)

- **API v24.0 (Oct 2025):** blocks new Advantage+ Shopping (ASC) and Advantage+ App Campaign (AAC) creation
- **v25.0 (Q1 2026):** prohibits across all versions
- **Full enforcement: 19 May 2026** — any code creating these breaks
- Replacement: Advantage+ Sales Campaigns (the renamed/upgraded successor); for app installs use the standard App Promotion objective with Advantage+ defaults

Source: [PPC.land](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/).

## 6. Advantage+ Creative ON by default (Feb 2026)

All new Sales / Leads / App campaigns launch with every creative enhancement enabled. Toggle individual ones (music, text overlays) off when off-brand or non-compliant. Source: [AdMove](https://www.admove.ai/blog/meta-advantage-creative-best-practices-for-2026).

## 7. Advantage+ Leads is the new default for lead-gen

Auto-enables Advantage+ audience, placements, CBO. Pair with **"conversion leads" performance goal + CRM via CAPI** → Meta reports -15% cost per quality lead, +44% lead-to-quality-lead. Source: [Meta Help](https://www.facebook.com/business/help/992035952809423).

## 8. Low-budget rule shift: ABO beats CBO at <£30/day

2025 Lebesgue analysis: 94% ROAS (ABO) vs 81% (CBO) at low spend. Below ~£30/day CBO starves some ad sets before they exit learning. Switch to CBO once a winner is proven and you want to scale. Sources: [AdAmigo](https://www.adamigo.ai/blog/cbo-best-practices-meta-ads), [Rebootiq](https://rebootiq.com/abo-vs-cbo-meta-ads/).

## 9. UGC / native creative outperforms polished

Roughly +35% performance vs. polished under Andromeda's preference for native-looking content. Source: [VideoAI](https://videoai.me/blog/meta-ads-creative-ugc-framework-roas-2026).

## 10. What this means in practice

Three things drive performance now: creative volume + diversity, signal quality (CAPI / EMQ), and not over-segmenting on small budgets. Almost every "Meta ads aren't working" diagnosis traces to one of those three.

---

*As of 2026-05-04.*
