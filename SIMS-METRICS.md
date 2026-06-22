# The Sims: Game-Specific Metrics & Analytics Framework
## KPIs, Measurement Methodologies, and Analytical Approaches

---

## 🎮 The Sims Unique Positioning

**The Sims is NOT a competitive game.** It's a creative sandbox that monetizes *self-expression* and *lifestyle simulation.*

- **Player motivation:** Creative expression, story building, customization, progression through life stages
- **Monetization model:** DLC packs (seasons, expansions, stuff packs), cosmetics, premium currency
- **Playstyles:** Builders (house design focus), Storytellers (relationships/narrative focus), Completionists, Casual players
- **Retention drivers:** Progression clarity, creative tools quality, DLC value, community engagement, seasonal content
- **Churn signals:** Progression blockers, DLC fatigue, lack of creative tools, repetitive content

**Analytics implication:** Metrics must reflect playstyle diversity. Don't optimize for one cohort at the expense of another.

---

## 📊 Core Metrics Framework

### **1. ENGAGEMENT HEALTH**

#### Acquisition & Activation
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Installs/Downloads** | New players entering the game | Growth target: +10% MoM | Decline >5% |
| **Day 1 Activation** | % of installers who complete first session | 75%+ | <60% |
| **Tutorial Completion** | % reaching first house customization | 65%+ | <50% |
| **Time to First Progression** | Avg minutes until Sim reaches Level 5 | <30 min | >45 min |

#### Daily/Monthly Activity
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **DAU (Daily Active Users)** | Unique players with ≥1 session that day | Baseline: 245K | Drop >15% YoY |
| **MAU (Monthly Active Users)** | Unique players with ≥1 session that month | Baseline: 1.2M | Flat/declining |
| **DAU/MAU Ratio** | Engagement stickiness (DAU ÷ MAU) | 20%+ | <15% (users leaving) |

#### Session Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Avg Session Duration** | Mean session length (minutes) | 30-45 min | <20 min (disengagement) |
| **Sessions per DAU** | Avg sessions per active user/day | 1.8-2.2 | <1.5 (single session then leaves) |
| **Session Frequency** | % of players with 2+ sessions/day | 35%+ | <20% |

#### Retention (Cohort-Based)
| Cohort Day | Definition | Target | Red Flag |
|---|---|---|---|
| **Day 1 Retention** | % of D0 players active on Day 1 | 92%+ | <80% |
| **Day 3 Retention** | % of D0 players active on Day 3 | 55%+ | <45% (onboarding friction) |
| **Day 7 Retention** | % of D0 players active on Day 7 | 40%+ | <35% (weak tutorial or early feature issue) |
| **Day 30 Retention** | % of D0 players active on Day 30 | 22%+ | <18% (mid-game pacing problem) |
| **Day 90 Retention** | % of D0 players active on Day 90 | 12%+ | <9% (endgame retention issue) |

**Nuance:** Retention differs by playstyle:
- Builders: Longer Day 3-7 retention (content exploration), may drop off after building is "done"
- Storytellers: Steadier Day 7-30 retention (relationships keep them engaged), sensitive to narrative content updates
- Completionists: Highest Day 90 retention (always something to complete), but churn hard when running out of goals

---

### **2. MONETIZATION HEALTH**

#### Revenue Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Daily Revenue (DAR)** | Total USD revenue per day | $165K-$210K | <$160K or >swings (instability) |
| **Monthly Revenue (MAR)** | Total USD revenue per month | $5.0M-$6.5M | Declining |
| **Revenue Forecast** | Projected annual revenue | $60M+ | Declining projections |

#### Conversion Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Free-to-Paid Conversion** | % of free players who ever spend | 8-12% | <6% (weak monetization funnel) |
| **Day 1 Conversion** | % converting within first day | 0.5-1.5% | <0.3% (monetization appears too early/hard to find) |
| **Day 7 Conversion** | % converting within first week | 3-5% | <2% |
| **DLC Purchase Rate** | % purchasing specific DLC pack | Varies by pack; 15-25% typical | <10% (pricing, value, or discovery issue) |

#### Customer Value Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **ARPU (Avg Revenue Per User)** | Total revenue ÷ DAU | $0.65-$0.85 | <$0.60 (monetization decline) |
| **ARPPU (Avg Revenue Per Paying User)** | Total revenue ÷ paying players | $7-$12 | <$6 (whale value declining) |
| **LTV (Lifetime Value)** | Total expected revenue per player | $8-$15 | Declining (churn issue) |
| **LTV:CAC Ratio** | LTV ÷ customer acquisition cost | 3:1 minimum | <2:1 (unprofitable) |

#### Player Segmentation (By Spend)
| Segment | % of Players | % of Revenue | Avg Spend | Characteristics |
|---|---|---|---|---|
| **Whales (Top 5%)** | 5% | 50-55% | $40-150 | High DLC ownership, frequent purchases, buy cosmetics regularly |
| **Mid-Tier (10-15%)** | 10% | 30-35% | $5-15 | Monthly/seasonal purchases, selective about packs |
| **Light Spenders (5-10%)** | 20% | 10-15% | $1-5 | One-time purchasers, often cosmetics |
| **Free Players (70%)** | 65% | 0% | $0 | No spend, but critical for network effects, engagement signals |

**Strategy:** Track each segment separately. A change benefiting whales might hurt free players' engagement (and thus whale engagement).

---

### **3. RETENTION & CHURN**

#### Churn Analysis
| Metric | Definition | When to Investigate |
|---|---|---|
| **Churn Rate** | % of active players not returning in 7 days | >10% Week-over-Week increase |
| **Churn by Progression Level** | % churning at each level (1-10-20-30, etc.) | Spikes at specific levels indicate blockers |
| **Churn by Time in Game** | % churning by tenure (Week 1, 2, 3, etc.) | Early churn = onboarding; late churn = endgame |
| **Churn by Last Action** | % churning after completing specific content | High churn after endgame = need new content |

#### Progression Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Time to Max Level** | Days to reach max progression level | 15-30 days median | <10 days (too easy) or >60 days (too grindy) |
| **Progression Completion %** | % of players reaching max level | 25-35% | <15% (progression too hard or unclear) |
| **Blocked Players** | Players stuck at same level for 7+ days | <5% | >10% (progression blocker, balance issue) |
| **Aspiration Completion** | % completing character aspiration goals | 40-50% | <30% (goals unclear or too hard) |

#### DLC-Specific Retention
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **DLC Owner Retention D7** | Day 7 retention for players who own DLC | 50-60% | <40% (DLC value unclear) |
| **Non-Owner Retention D7** | Day 7 retention for free players | 35-45% | <30% (non-owners churning) |
| **DLC Adoption Lift** | D7 retention improvement from owning DLC | +10-15% | <5% (DLC not driving engagement) |
| **DLC Cannibalization** | % of DLC revenue from existing players vs. new spend | <20% from new players = concern | Analyze if DLC is converting new players or just extracting from existing |

---

### **4. FEATURE ADOPTION & ENGAGEMENT**

#### New Feature Adoption (Use for every feature launch)
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Feature Discovery** | % of players who see new feature prompt | 80%+ | <60% (discovery issue) |
| **Feature Try Rate** | % of players who click/interact with feature | 40-60% | <25% (value proposition unclear) |
| **Feature Usage Rate** | % actively using feature after Day 1 | 25-35% | <15% (feature not sticky) |
| **Feature DAU/MAU** | Daily ÷ monthly feature users | 30%+ | <15% (one-time use only) |

#### Creative Tools Engagement (Unique to Sims)
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **House Builder Adoption** | % of players customizing home | 60-70% | <50% (builder tools too complex/unintuitive) |
| **Build Mode Session Duration** | Avg time in build mode per session | 15-20 min | <8 min (not engaging with building) |
| **Shared Creations Volume** | # of houses/Sims shared by players | Growth target: +20% MoM | Declining (community engagement issue) |
| **Community Content Discovery** | % of players viewing shared creations | 25-35% | <15% (discovery algorithm issue) |

---

### **5. CONTENT & SEASONAL ENGAGEMENT**

#### Content Performance
| Metric | Definition | Use Case |
|---|---|---|
| **Event DAU Lift** | Increase in DAU during special events | Track whether events drive engagement |
| **Event Engagement Rate** | % of DAU participating in event | Target 40%+; <20% = event not resonating |
| **Event-Specific Monetization** | Revenue attributed to event content | Measure ROI of event investment |
| **Content Consumption Velocity** | Days to consume new content | If players beat content in 3 days, add more |

#### Seasonal Patterns (Critical for Sims)
| Season | Expected Behavior | Forecasting |
|---|---|---|
| **Holiday Season (Nov-Dec)** | +30-50% DAU increase, +40-60% revenue | Key revenue period; plan major updates |
| **Summer (Jun-Aug)** | Flat to slight dip (players outside); strong creative content engagement | Focus on creative tools, not time-gated events |
| **Back-to-School (Sep)** | Smaller spike, younger demographic increase | Family-friendly content performs well |
| **Regular months** | Seasonal content updates maintain engagement | Predictable baseline; use to test features |

**Warning:** If seasonal patterns disappear, something is broken (or game lost appeal with seasonal audiences).

---

### **6. TECHNICAL & OPERATIONAL HEALTH**

#### Performance Metrics
| Metric | Definition | Target | Red Flag |
|---|---|---|---|
| **Server Uptime** | % of time game is playable | 99.9%+ | <99.5% (impacts player trust) |
| **Avg Load Time** | Average time to load into game | <5 seconds | >10 seconds (players quit before playing) |
| **Crash Rate** | % of sessions ending in crash | <1% | >2% (severe technical issue) |
| **Bug Report Volume** | New bugs reported per day | Trending down | Sudden spike (new bugs in latest update) |

#### Quality Metrics
| Metric | Definition | Target |
|---|---|---|
| **Critical Bug Resolution Time** | Days to fix game-breaking bugs | <24 hours |
| **Hotfix Deployment Time** | Time from identifying critical issue to deployment | <12 hours |
| **Player-Reported Issues** | Count of same bug reported by multiple players | <10% of bugs (good detection) |

---

## 📈 Analytical Approaches

### **1. Cohort Analysis (Most Important for Sims)**

**Why:** Sims has strong seasonal patterns and playstyle diversity. Must track cohorts separately.

```
Example: How did Seasons DLC launch affect retention?

Cohort A (Pre-Seasons): Players who joined before DLC
  Day 7 retention: 42%
  
Cohort B (Post-Seasons): Players who joined after DLC
  Day 7 retention: 48%
  
Lift: +6 percentage points (or +14% relative improvement)
```

**Action:** If Cohort B retention is higher, DLC successfully attracts/retains new players.

---

### **2. Segmentation Analysis**

**Why:** Builders, Storytellers, and Completionists have different engagement patterns. Optimize for all three or risk alienating cohorts.

```
Example: How does new progression system affect retention?

Builders:
  - Session duration: 45 min (focused on building)
  - Retention D7: 38%
  - DLC adoption: 65% (builders buy building tools)
  
Storytellers:
  - Session duration: 25 min (shorter, frequent sessions)
  - Retention D7: 45%
  - DLC adoption: 45% (less interested in tools, more in narratives)
  
Free Players:
  - Session duration: 18 min
  - Retention D7: 35%
  - DLC adoption: 0%
```

**Action:** New progression system might favor builders but alienate storytellers. Test separately.

---

### **3. Funnel Analysis (for Monetization)**

```
Free Players: 100,000
  ↓ (8% discover premium)
Discover Premium: 8,000 (8%)
  ↓ (40% click to learn more)
Explore DLC: 3,200 (40% of discoverers)
  ↓ (50% add to cart)
Cart: 1,600 (50% of explorers)
  ↓ (90% complete purchase)
Purchase: 1,440 (90% of cart)

**Conversion Rate: 1.44% of free players**
**Bottleneck:** Explore step (only 40% click). Improve DLC description/visuals.
```

---

### **4. Retention Curve Decomposition**

```
Day 1: 92% retain (strong launch day)
Day 2: 85% retain (drop: -7pp) [First repeat play]
Day 3: 55% retain (drop: -30pp) [CRITICAL CLIFF - tutorial frustration]
Day 7: 40% retain (drop: -15pp) [Early content fatigue]
Day 14: 28% retain (drop: -12pp) [Midgame engagement dip]
Day 30: 22% retain (drop: -6pp) [Endgame players still engaged]

**Where to intervene:** Day 2-3 (biggest drop, highest ROI)
**Intervention:** Streamline tutorial, provide guidance, reduce friction
```

---

### **5. A/B Testing Framework for Sims**

**Example:** Should new DLC pack cost $9.99 or $14.99?

```
Group A (Control): $9.99
  - 8% conversion rate
  - 500K players in offer
  - Revenue: $399,600/week

Group B (Treatment): $14.99
  - 4.5% conversion rate (expected: lower conversion, higher ARPU)
  - 500K players in offer
  - Revenue: $337,350/week

Result: Group A wins ($62K more revenue/week)
```

**Key:** For Sims, monitor not just conversion but also:
- Day 7 retention (does DLC affect staying power?)
- Gameplay engagement (does higher price feel expensive/predatory?)
- Player sentiment (community feedback on pricing)

---

## 🎯 Key Insights for Decision-Making

### **1. Creative Tools Drive Retention**
Players with frequent build mode access retain 2-3x longer than non-builders. Prioritize build tools quality.

### **2. DLC Cannibalization is Real**
When new DLC launches, always check if it's converting new players or just extracting from existing players. If 90% of DLC revenue is from existing players, it's not growth.

### **3. Seasonal Content > Evergreen Content**
Sims players want fresh experiences tied to real seasons (holidays, summer). Plan seasonal roadmap 6 months ahead.

### **4. Community Amplifies Engagement**
Shared creations (houses, Sims) drive discovery and retention. Players with shared content visible retain 2x longer than those without.

### **5. Free Players Matter**
Free players who convert to paying players become your whales. Nurture free player experience = future monetization.

---

## 🔍 Questions to Ask When Analyzing Sims Data

1. **"Are we optimizing for one playstyle and alienating others?"** (Builders vs. Storytellers)
2. **"Is this DLC growth or cannibalization?"**
3. **"Why did Day 3 retention drop 30pp this week?"** (Tutorial change? Bug? Content issue?)
4. **"Are whales satisfied?"** (Sentiment + retention; price hikes risk alienating top spenders)
5. **"Did seasonal content perform as expected?"** (vs. historical seasonal patterns)

---

**This framework should guide your analysis. Always think: engagement → retention → monetization → sustainability.**
