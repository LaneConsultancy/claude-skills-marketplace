# Domain Scoring Criteria for PBN Quality Assessment

This document defines the scoring methodology for evaluating expired domains for Private Blog Network (PBN) use.

## Scoring System Overview

**Base Score**: 50 points  
**Range**: 0-100 points  
**Minimum Recommended**: 60+ points for PBN inclusion

---

## Positive Factors (Add Points)

### Domain Age
Domain age indicates establishment and trustworthiness. Older domains typically have more stable backlink profiles.

- **15+ years old**: +20 points
- **10-14 years old**: +15 points  
- **5-9 years old**: +10 points
- **2-4 years old**: +5 points
- **Under 2 years**: 0 points

**Data Source**: First seen date from DataForSEO or domain registration history

---

### Domain Rating (DR) / Domain Authority (DA)
Higher DR/DA indicates stronger domain authority and link equity potential.

- **DR 40+**: +30 points
- **DR 30-39**: +25 points
- **DR 20-29**: +20 points
- **DR 10-19**: +10 points
- **DR 5-9**: +5 points
- **DR < 5**: 0 points

**Data Source**: DataForSEO `backlinks_summary` rank field

---

### Referring Domains Count
More diverse referring domains indicate natural link acquisition and broader authority.

- **100+ referring domains**: +20 points
- **50-99 referring domains**: +15 points
- **20-49 referring domains**: +10 points
- **10-19 referring domains**: +5 points
- **5-9 referring domains**: +2 points
- **< 5 referring domains**: -10 points (red flag for thin profile)

**Data Source**: DataForSEO `referring_domains` count

---

### Anchor Text Quality
Natural, branded anchor text distribution indicates organic link building rather than manipulation.

**Analysis Methodology**:
1. Calculate percentage distribution of anchor types:
   - Branded (company/domain name)
   - Naked URL (example.com)
   - Generic (click here, visit website, read more)
   - Exact match (keyword-rich)
   - Other

2. Apply scoring:
   - **Branded + Naked URL > 70%**: +15 points (excellent, natural profile)
   - **Branded + Naked URL 50-70%**: +10 points (good)
   - **Branded + Naked URL 30-49%**: +5 points (acceptable)
   - **Exact match > 40%**: -20 points (over-optimized, unnatural)
   - **Generic only > 60%**: -10 points (suspicious pattern)

**Data Source**: DataForSEO `backlinks_anchors`

---

### Niche Relevance
Domains with backlinks from niche-relevant sources provide better contextual authority.

**Detection Method**:
1. Extract top 10 referring domains
2. Check anchor text for niche keywords
3. Analyze referring page content (if available)

**Scoring**:
- **Strong relevance** (3+ niche mentions in top anchors): +15 points
- **Moderate relevance** (1-2 niche mentions): +10 points
- **Weak relevance** (keyword in domain name only): +5 points
- **No relevance**: 0 points

---

### TLD Premium Bonus
Certain TLDs carry more authority and trust.

- **.co.uk**: +5 points (local authority for UK)
- **.com**: +5 points (global trust)
- **.org**: +3 points (perceived authority)
- **.net**: +2 points
- **Other ccTLDs**: +1 point
- **New gTLDs** (.xyz, .online, etc.): 0 points

---

### Follow vs. NoFollow Ratio
Higher percentage of dofollow links indicates better link equity transfer.

- **Dofollow > 80%**: +10 points
- **Dofollow 60-80%**: +5 points
- **Dofollow 40-60%**: 0 points
- **Dofollow < 40%**: -5 points

**Data Source**: DataForSEO backlink attributes

---

### Backlink Profile Growth Pattern
Steady, organic growth is preferable to sudden spikes.

**Ideal Pattern**: Gradual increase over years  
**Red Flag Pattern**: Sudden spike then drop-off

- **Steady organic growth**: +10 points
- **Stable plateau**: +5 points
- **Recent spike (last 6 months)**: -20 points (potential spam attack)
- **Declining trend**: -10 points

**Data Source**: DataForSEO historical backlink data (if available)

---

## Negative Factors (Subtract Points)

### Spammy Anchor Text Detection
Presence of spam-related keywords in anchor text is a critical red flag.

**Red Flag Anchor Keywords** (case-insensitive matching):

#### Gambling & Casino (-30 points each category)
- casino, poker, gambling, slots, bet, betting, bookmaker, jackpot, roulette, blackjack, bingo, lottery

#### Pharmaceutical (-30 points)
- viagra, cialis, levitra, pharmacy, pills, drugs, prescription, kamagra, medication, pharmaceutical

#### Adult Content (-40 points)
- porn, xxx, adult, sex, escort, dating, webcam, nude, erotic
- (This is an immediate disqualifier - set score to 0)

#### Payday Loans & Finance Spam (-25 points)
- payday, loan, credit, debt, mortgage, insurance, forex, binary options, cryptocurrency scam

#### Foreign Language Spam (-20 points)
- Detecting Cyrillic, Chinese, or Arabic characters in > 30% of anchors
- Common foreign spam terms: раскрутка, продвижение, казино, 在线, 賭場

#### E-commerce Spam (-15 points)
- Unnatural density of: cheap, buy, discount, sale, price, deal, offer, coupon
- **Detection**: If > 20% of anchors contain these terms in unnatural combinations

#### Link Farm Indicators (-25 points)
- "click here", "read more", "visit website" > 40% of total anchors
- Repeated exact anchor patterns across multiple domains
- Generic anchors with no variation

---

### PBN Footprint Indicators

Domains that were previously part of PBNs carry devaluation risk.

**Detection Signals** (-25 points each):

1. **Cross-linking patterns**:
   - Same IP addresses in referring domains
   - Same registrar patterns across referrers
   - Similar WHOIS privacy patterns

2. **Template footprints**:
   - Multiple referring sites using identical WordPress themes
   - Identical site structures across referrers

3. **Unnatural anchor distribution**:
   - Exact match anchors from multiple sites with different IPs but same anchor text

4. **Sudden link drops**:
   - Historical data shows 50%+ backlink loss in short period (indicates deindexing)

**Data Source**: Manual analysis of top referring domains + DataForSEO referring domain details

---

### Domain History Red Flags

#### Previous Redirects (-15 points)
- Domain previously 301'd to another domain
- **Detection**: Check historical DNS records, referring page patterns

#### Penalized or Deindexed (-40 points - likely disqualifier)
- Evidence of Google penalty
- Complete drop in backlinks/traffic
- **Detection**: Sudden cliff in backlink history, archive.org shows thin content

#### Blacklisted (-50 points - absolute disqualifier)
- Domain appears on spam blacklists
- Malware history
- **Check against**: Google Safe Browsing, Spamhaus, SURBL

---

### Link Quality Issues

#### Low-Quality Referring Domains (-15 points)
- **Detection**: Top 10 referring domains have average DR < 10
- Referring domains from known link farms
- Sitewide footer/sidebar links (diluted value)

#### Excessive Reciprocal Linking (-10 points)
- More than 30% of backlinks appear to be reciprocal
- **Detection**: Check if referring domains also receive links from target

#### Thin Backlink Profile (-10 points)
- Fewer than 5 unique referring domains
- Total backlinks < 20
- Single-source dependency (>50% from one domain)

---

### Foreign Language Content Issues

#### High Foreign Language Anchor Percentage (-15 points)
- **Threshold**: > 30% of anchors in non-English languages (for .co.uk domains)
- **Exception**: If targeting foreign language PBN, reverse this rule

#### Mismatched Language Context (-10 points)
- Domain is .co.uk but majority of content/anchors are non-English
- Indicates potential hijacking or spam usage

---

### Content Quality Indicators (from Wayback Machine)

#### Thin or Auto-Generated Content (-20 points)
- Historical snapshots show thin content pages
- Auto-generated doorway pages
- Spun content

#### Frequent Topic Changes (-15 points)
- Domain changed topics frequently (e.g., tech blog → gambling → health)
- Indicates domain flipping or spam usage

---

## Scoring Calculation Process

### Step-by-Step Methodology

1. **Initialize**: Start with base score of 50

2. **Domain Age**: 
   - Calculate age from first seen date
   - Apply age bonus (+0 to +20)

3. **Domain Rating**:
   - Extract DR from DataForSEO
   - Apply DR bonus (+0 to +30)

4. **Referring Domains**:
   - Count unique RDs
   - Apply RD bonus (+2 to +20) or penalty (-10)

5. **Anchor Text Analysis**:
   - Fetch top 100 anchors
   - Calculate distribution percentages
   - Check against red flag keywords
   - Apply anchor quality bonus (+0 to +15) or penalties (-15 to -40)

6. **Niche Relevance**:
   - Compare anchors/referring domains to niche keywords
   - Apply relevance bonus (+0 to +15)

7. **TLD Bonus**:
   - Apply based on extension (+0 to +5)

8. **Dofollow Ratio**:
   - Calculate percentage
   - Apply bonus/penalty (-5 to +10)

9. **Red Flag Scan**:
   - Check for spam anchors → apply penalties (-15 to -40)
   - Check for PBN footprints → apply penalty (-25)
   - Check for domain history issues → apply penalties (-10 to -50)

10. **Calculate Final Score**:
    - Sum all positive and negative factors
    - Clamp to range [0, 100]

11. **Assign Rating**:
    - 80-100: "Excellent"
    - 60-79: "Good"
    - 40-59: "Fair"
    - 0-39: "Poor"

---

## Score Interpretation & Recommendations

### Excellent (80-100 points)
**Strong PBN Candidate**

- Clean backlink profile
- High authority metrics
- Established domain age
- Niche-relevant (likely)
- No significant red flags

**Recommendation**: 
- Priority purchase
- Thoroughly verify with manual checks
- Worth paying premium price

**Next Steps**:
1. Check domain availability immediately
2. Review Wayback Machine for content history
3. Verify with manual backlink audit
4. Secure registration ASAP

---

### Good (60-79 points)
**Viable PBN Candidate**

- Decent authority metrics
- Minor issues present but manageable
- Generally clean profile
- May require some cleanup

**Recommendation**:
- Worth considering
- Review specific red flags before purchase
- Acceptable for tier 2 PBN positions

**Next Steps**:
1. Identify specific issues (review penalty details)
2. Assess if issues are fixable (e.g., disavow spam links)
3. Check availability
4. Proceed if issues are acceptable

---

### Fair (40-59 points)
**Proceed with Caution**

- Significant concerns present
- Authority may be weak
- Red flags require investigation
- May be salvageable with work

**Recommendation**:
- Manual review required
- Only purchase if very cheap
- Plan for extensive cleanup (disavow file)
- Better suited for testing or low-priority use

**Next Steps**:
1. Deep dive into specific red flags
2. Estimate cleanup effort
3. Only proceed if price is very low (<$20)
4. Consider opportunity cost vs. finding better domain

---

### Poor (0-39 points)
**Not Recommended**

- Critical red flags present
- High spam indicators
- Thin or manipulated profile
- Likely penalized or will be

**Recommendation**:
- **Avoid purchase**
- High risk of no SEO value
- Could harm your PBN if included
- Time better spent finding quality domains

**Next Steps**:
- Skip this domain
- Move to next candidate
- If score is close to 40, consider re-checking in future

---

## Special Cases & Exceptions

### Brand Name Domains
If domain is an exact match for a legitimate business name:
- **Add +10 points** for brand authority
- **Ignore** generic e-commerce spam keywords if contextually appropriate

### Local Business Domains
For local service domains (plumber-cityname.co.uk):
- **Add +10 points** for local relevance
- **Forgive** some generic anchors (they're natural for local businesses)

### News/Editorial Domains
Former news sites or blogs:
- **Accept lower DR** (journalism sites often have lower metrics)
- **Prioritize** diversity of referring domains over total DR

### Seasonal/Event Domains
Domains related to specific events or timeframes:
- **Subtract -5 points** (limited long-term relevance)
- Only consider if niche-aligned

---

## Red Flag Keyword Master List

Use this master list for automated detection:

### Immediate Disqualifiers (Score = 0)
```
porn, xxx, adult, sex, escort, nude, erotic, sexual, hardcore, 
webcam girls, cam girls, live sex, porn videos
```

### Critical Penalties (-30 to -40)
```
casino, poker, gambling, slots, bet, betting, jackpot, roulette,
viagra, cialis, levitra, pharmacy, pills, drugs, prescription,
payday loan, quick loan, bad credit, debt consolidation
```

### Moderate Penalties (-15 to -25)
```
cheap, buy now, discount, sale, price, best price, 
replica, fake, counterfeit, 
seo services, link building, backlinks for sale,
essay writing, paper writing, homework help
```

### Detection Method
For each domain:
1. Extract all anchor texts
2. Convert to lowercase
3. Check for substring matches against red flag lists
4. Count occurrences
5. If ANY immediate disqualifier found → Score = 0
6. If critical penalty keywords > 5% of anchors → Apply penalty
7. If moderate penalty keywords > 20% of anchors → Apply penalty

---

## Scoring Examples

### Example 1: Excellent Domain

**Domain**: oldplumbingcompany.co.uk  
**Base Score**: 50

**Positive Factors**:
- Age: 15 years → +20
- DR: 32 → +25
- Referring Domains: 78 → +15
- Anchors: 75% branded/naked URLs → +15
- Niche: Strong plumbing relevance → +15
- TLD: .co.uk → +5
- Dofollow: 85% → +10

**Negative Factors**:
- None detected

**Final Score**: 50 + 105 = **155 → Clamped to 100** ✓ Excellent

---

### Example 2: Good Domain with Minor Issues

**Domain**: heating-services-uk.co.uk  
**Base Score**: 50

**Positive Factors**:
- Age: 8 years → +10
- DR: 18 → +10
- Referring Domains: 32 → +10
- Niche: Moderate relevance → +10
- TLD: .co.uk → +5

**Negative Factors**:
- Foreign anchors 35% → -15
- Anchors: Only 45% branded → +5 (instead of +15)

**Final Score**: 50 + 45 - 15 = **80** → Good ✓

---

### Example 3: Fair Domain Requiring Review

**Domain**: ukbuilders.co.uk  
**Base Score**: 50

**Positive Factors**:
- Age: 6 years → +10
- DR: 12 → +10
- Referring Domains: 15 → +5

**Negative Factors**:
- Thin profile (only 15 RDs for age) → -10
- Exact match anchors 45% → -20
- Recent backlink spike → -20

**Final Score**: 50 + 25 - 50 = **25** → Poor ✗

---

### Example 4: Disqualified Domain

**Domain**: cheap-deals.co.uk  
**Base Score**: 50

**Positive Factors**:
- Age: 10 years → +15
- DR: 22 → +20

**Negative Factors**:
- Spammy anchors detected: "casino", "cheap viagra" → -30
- E-commerce spam density → -15
- Anchor text over-optimization → -20

**Final Score**: 50 + 35 - 65 = **20** → Poor ✗ (Avoid)

---

## Implementation Notes

### For Automated Scoring Scripts

1. **Always clamp final score** to [0, 100] range
2. **Round to nearest integer** for display
3. **Log penalty reasons** for user review
4. **Flag disqualifiers prominently** in output
5. **Sort results by score DESC** in final output

### For Manual Review

Even high-scoring domains should be:
- Cross-referenced with Wayback Machine
- Checked for current availability
- Verified against Google Safe Browsing
- Reviewed for WHOIS history (if accessible)

### Continuous Improvement

This scoring model should be refined based on:
- Actual PBN performance data
- Changing Google algorithm signals
- New spam pattern detection
- User feedback on domain quality

---

## Version History

- **v1.0** (2026-01-25): Initial scoring criteria document
