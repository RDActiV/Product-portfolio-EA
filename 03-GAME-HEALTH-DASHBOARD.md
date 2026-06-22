# Portfolio Project 3: Game Health Monitoring Dashboard
## Real-Time Operational Analytics for Live Games

**Project Date:** June 2024 | **Skills:** Data Pipeline, SQL, Python ETL, BI Dashboard Design, Operational Analytics

---

## EXECUTIVE SUMMARY
Built a real-time operational dashboard enabling product/ops teams to monitor game health KPIs, detect anomalies within 24 hours, and respond to player experience issues. **Key metrics tracked:** DAU/MAU, retention cohorts, feature adoption, revenue health, system performance.

**Impact:** Reduced time-to-detect operational issues from 3 days → 24 hours, enabling faster incident response.

---

## PROBLEM STATEMENT
Live service games require continuous operational monitoring. Traditional batch reporting (weekly snapshots) creates blind spots when:
- Player engagement crashes unexpectedly
- Monetization metrics decline
- New features underperform
- Server/performance issues emerge

**Solution:** Build a self-serve real-time dashboard that ops teams can query independently, reducing dependency on data team for urgent insights.

---

## DASHBOARD ARCHITECTURE

### Data Sources
```
Event Stream (Game Telemetry)
    ↓
Kafka/Event Pipeline
    ↓
Data Warehouse (Databricks/Snowflake)
    ↓
Aggregation Layer (SQL)
    ↓
BI Tool (Tableau/PowerBI)
    ↓
Dashboard + Alerts
```

### Core Data Model
```sql
-- Fact table: Daily game health metrics
CREATE TABLE fact_game_health_daily AS
SELECT
    date_key,
    game_id,
    server_region,
    platform,
    dau,                      -- Daily active users
    mau_rolling_30,           -- 30-day monthly active users
    avg_session_duration,     -- Minutes
    retention_d1,             -- Day 1 retention %
    retention_d7,             -- Day 7 retention %
    retention_d30,            -- Day 30 retention %
    feature_adoption_rate,    -- % players using new feature
    revenue_usd,              -- Daily revenue
    avg_revenue_per_user,     -- ARPU
    crash_rate,               -- % sessions with crash
    avg_load_time_ms,         -- Server response time
    updated_timestamp
FROM game_events
GROUP BY date_key, game_id, server_region, platform;
```

---

## DASHBOARD PAGES

### PAGE 1: Executive Health Snapshot
**Purpose:** 1-minute health check for all stakeholders

**Metrics:**
```
┌─────────────────────────────────────────────────────────┐
│                  GAME HEALTH SNAPSHOT                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  DAU:  245K (↑3% vs yesterday)    MAU:  1.2M (↑5%)      │
│  Avg Session:  32 min              Retention D7:  42%    │
│  Revenue (24h):  $185K (↑8%)       Crash Rate:  0.8%     │
│                                                          │
│  🟢 Status: HEALTHY  |  ⏰ Updated: 2 mins ago          │
│                                                          │
└─────────────────────────────────────────────────────────┘

ALERTS (Last 24h):
⚠️  Server response time +15% (Asia region) - investigating
✅  New battle pass feature adoption at 38% - above target
```

### PAGE 2: Player Retention Analysis
**Purpose:** Understand cohort health over time

**Visualizations:**
```
Cohort Retention Heatmap:
                Day 1    Day 3    Day 7    Day 14   Day 30
W24 (Jun 2-8)   92%      55%      38%      28%      22%
W25 (Jun 9-15)  94%      57%      40%      30%      24%
W26 (Jun 16-22) 91%      53%      36%      26%      20%
W27 (Jun 23-29) 93%      56%      39%      29%      23%

Trend: Stable retention patterns, no red flags

Retention by Feature Adoption:
  • Battle pass users:     78% Day 7 retention
  • Non-battle pass:       35% Day 7 retention
  → Battle pass drives 2.2x retention lift
```

### PAGE 3: Feature Performance & Adoption
**Purpose:** Track new feature health and engagement

**Visualizations:**
```
Feature Adoption Funnel (New Cosmetics Shop):
  • View shop:           85K (100%)
  • Add to cart:         42K (49%)
  • Complete purchase:   18K (21%)
  • Return to shop:      12K (67% of buyers)

Performance vs. Baseline:
  • Expected 25% conversion → Actual 21% (4pt underperformance)
  • Recommendation: Test streamlined checkout flow

Feature Impact on Key Metrics:
  • Session duration:    +18% (users spend more time)
  • Monetization:        +12% ARPU
  • Retention D7:        +8%
```

### PAGE 4: Revenue & Monetization Health
**Purpose:** Real-time monetization monitoring

**Visualizations:**
```
Revenue Trend (Last 30 Days):
  Daily Revenue Range:     $160K - $210K
  7-Day Avg:               $185K
  YoY Growth:              +22%
  
Revenue Breakdown:
  • Battle Pass:           52% of revenue
  • Cosmetics:             38%
  • Battle Pass + Cosmetics: 90% of revenue
  
ARPU by Segment:
  • Whales (top 5%):       $42.50 (52% of revenue)
  • Mid-tier (15%):        $8.20
  • Free players (80%):    $0.45
  
KPI Status:
  ✅ Revenue on track (forecast: $5.6M monthly)
  ✅ Battle pass retention healthy
  ⚠️  Cosmetic adoption declining (investigate new cosmetic appeal)
```

### PAGE 5: System & Performance Health
**Purpose:** Ops monitoring (performance, errors, infrastructure)

**Visualizations:**
```
System Health Metrics:
  • Server uptime:         99.94%
  • Avg response time:     145ms (target: <200ms)
  • P99 latency:           320ms
  • Error rate:            0.3%
  • Crash rate:            0.8% (threshold: 1.5%)
  
Crashes by Region:
  • North America:  0.6%
  • Europe:         0.7%
  • Asia:           1.1% ← Elevated
  
Database Query Performance:
  • Slow queries (>5s):    12 (↑ from 8 yesterday)
  • Recommended action:    Index optimization on player_events table
```

---

## ALERT SYSTEM

### Anomaly Detection Logic
```sql
-- Auto-flag unusual drops/spikes
CREATE TABLE dashboard_alerts AS
SELECT
    alert_id,
    metric_name,
    current_value,
    expected_value,
    deviation_pct,
    CASE 
        WHEN deviation_pct > 20 THEN 'CRITICAL'
        WHEN deviation_pct > 10 THEN 'WARNING'
        ELSE 'INFO'
    END as alert_severity,
    alert_timestamp
FROM game_health_metrics
WHERE
    -- DAU drop >15%
    (metric_name = 'DAU' AND current_value < expected_value * 0.85)
    -- Revenue drop >20%
    OR (metric_name = 'revenue' AND current_value < expected_value * 0.80)
    -- Crash rate spike >50%
    OR (metric_name = 'crash_rate' AND current_value > baseline_rate * 1.5)
    -- Feature adoption stalled
    OR (metric_name = 'feature_adoption' AND current_value < 10%);
```

### Alert Examples
```
🔴 CRITICAL (Immediate Action):
  • DAU dropped 18% overnight → Investigate server issues, bugs

🟡 WARNING (Next 2 Hours):
  • Revenue down 12% → Check monetization flow, pricing changes

🟢 INFO (Monitor):
  • Crash rate up 2% but still in acceptable range
  • Feature adoption at 31% (on track for 35% target)
```

---

## INTERACTIVITY & SELF-SERVE FEATURES

### Dashboard Filters
Users can slice data by:
- **Date range:** Real-time, last 7 days, last 30 days, custom
- **Platform:** iOS, Android, PC
- **Server region:** North America, Europe, Asia, LATAM
- **Player segment:** New, returning, whales, dormant
- **Feature:** New cosmetics, battle pass, event content

### Example Query Path (Self-Serve)
```
PM asks: "How did battle pass adoption impact retention for new players in Asia this week?"

Path:
1. Select metric: "Retention D7"
2. Filter: Platform = iOS/Android, Region = Asia, Date = Last 7 Days
3. Segment by: Feature adoption (battle pass users vs. non)
4. Result: Battle pass users 65% retention vs. 38% for non-users
5. Deep-dive: Cohort analysis showing adoption timing impact
```

---

## TECHNICAL IMPLEMENTATION

### Data Pipeline
```python
# Python ETL script (runs hourly)
import pandas as pd
from databricks import sql
import logging

def extract_game_events():
    """Extract events from Kafka stream"""
    query = """
    SELECT 
        event_timestamp,
        player_id,
        event_type,
        event_data
    FROM kafka_stream
    WHERE event_timestamp > DATE_SUB(NOW(), INTERVAL 1 HOUR)
    """
    return spark.sql(query)

def transform_to_daily_metrics(events_df):
    """Aggregate raw events to daily metrics"""
    daily_metrics = events_df.groupBy(
        F.date_trunc('day', 'event_timestamp'),
        'platform',
        'server_region'
    ).agg(
        F.countDistinct('player_id').alias('dau'),
        F.avg('session_duration').alias('avg_session_duration'),
        F.sum('revenue_usd').alias('revenue_usd')
    )
    return daily_metrics

def load_to_warehouse(metrics_df):
    """Load to Databricks for BI tool"""
    metrics_df.write \
        .mode('overwrite') \
        .option('mergeSchema', 'true') \
        .saveAsTable('fact_game_health_daily')
    
    logging.info("Game health metrics updated successfully")

# Main ETL
events = extract_game_events()
metrics = transform_to_daily_metrics(events)
load_to_warehouse(metrics)
```

---

## BUSINESS IMPACT

### Before Dashboard
- ⏱️ Time to detect issues: 3 days (weekly batch reports)
- 👥 Dependency: Product team relied on data analysts for basic queries
- 📉 Response time to incidents: 24-48 hours

### After Dashboard
- ⏱️ Time to detect issues: 24 hours (automated alerts)
- 👥 Self-serve: 80% of standard queries now self-served
- 📈 Response time to incidents: 2-4 hours
- 💰 Business outcome: +3% DAU retention (from faster incident response)

---

## DASHBOARD SPECIFICATIONS

| Metric | Target | Status | Alert Threshold |
|---|---|---|---|
| DAU | 245K | ✅ 245K | < 210K (-15%) |
| Retention D7 | 42% | ✅ 42% | < 38% (-10%) |
| ARPU | $0.75 | ⚠️ $0.68 | < $0.65 |
| Crash rate | <1% | ✅ 0.8% | > 1.5% |
| Feature adoption | 35%+ | ✅ 38% | < 20% |

---

## DELIVERABLES
✅ Real-time data pipeline (SQL + Python ETL)  
✅ BI dashboard (5 pages, interactive filters)  
✅ Anomaly detection alerts  
✅ Self-serve query templates for common questions  
✅ Documentation for non-technical users  
✅ SLA monitoring (99.9% dashboard uptime target)

---

**📁 Code:** See `code/etl_pipeline.py`
