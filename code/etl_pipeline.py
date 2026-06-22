"""
Game Health Monitoring — ETL Pipeline
Portfolio Project 3 — Anvesh Singh
EA Product Analyst Portfolio

Simulates a real-time ETL pipeline for live-service game health dashboards.
Architecture: Event Stream → Transform → Aggregate → Data Warehouse → Alerts
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
import json
import warnings
warnings.filterwarnings('ignore')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# 1. EXTRACT — Simulate event stream
# ─────────────────────────────────────────────

def extract_game_events(hours_back=1, n_events=50000, seed=None):
    """
    Extract raw game telemetry events.
    In production: queries Kafka stream or event warehouse.
    
    Args:
        hours_back: How many hours of events to pull
        n_events: Number of events to simulate
        seed: Random seed for reproducibility
    """
    if seed:
        np.random.seed(seed)
    
    now = datetime.now()
    start = now - timedelta(hours=hours_back)
    
    event_types = ['session_start', 'session_end', 'level_complete', 'purchase',
                   'feature_viewed', 'feature_used', 'battle_pass_offer', 'crash']
    platforms   = ['iOS', 'Android', 'PC']
    regions     = ['North America', 'Europe', 'Asia', 'LATAM']
    
    events = pd.DataFrame({
        'event_id':         [f'evt_{i:08d}' for i in range(n_events)],
        'event_timestamp':  [start + timedelta(seconds=np.random.randint(0, hours_back * 3600))
                             for _ in range(n_events)],
        'player_id':        [f'player_{np.random.randint(0, 245000):06d}' for _ in range(n_events)],
        'event_type':       np.random.choice(event_types, n_events,
                                              p=[0.20, 0.20, 0.18, 0.05,
                                                 0.15, 0.12, 0.07, 0.03]),
        'platform':         np.random.choice(platforms, n_events, p=[0.40, 0.35, 0.25]),
        'server_region':    np.random.choice(regions, n_events, p=[0.40, 0.30, 0.22, 0.08]),
        'session_duration': np.random.exponential(32, n_events).clip(1, 180),
        'revenue_usd':      0.0,
    })
    
    # Set revenue only on purchase events
    purchase_mask = events['event_type'] == 'purchase'
    events.loc[purchase_mask, 'revenue_usd'] = np.random.choice(
        [7.99, 9.99, 14.99, 4.99], purchase_mask.sum(), p=[0.40, 0.30, 0.20, 0.10]
    )
    
    logger.info(f"Extracted {len(events):,} events from last {hours_back}h "
                f"({events['event_timestamp'].min().strftime('%H:%M')} → "
                f"{events['event_timestamp'].max().strftime('%H:%M')})")
    return events


# ─────────────────────────────────────────────
# 2. TRANSFORM — Aggregate to daily metrics
# ─────────────────────────────────────────────

def transform_to_daily_metrics(events_df):
    """
    Aggregate raw events into game health KPIs.
    Produces one row per (date, platform, region).
    """
    events_df = events_df.copy()
    events_df['date'] = events_df['event_timestamp'].dt.date
    
    # Sessions
    sessions = events_df[events_df['event_type'].isin(['session_start', 'session_end'])]
    
    # Daily active users
    dau = (events_df.groupby(['date', 'platform', 'server_region'])['player_id']
           .nunique().reset_index(name='dau'))
    
    # Avg session duration
    session_dur = (events_df.groupby(['date', 'platform', 'server_region'])['session_duration']
                   .mean().reset_index(name='avg_session_duration_min'))
    
    # Revenue
    revenue = (events_df.groupby(['date', 'platform', 'server_region'])['revenue_usd']
               .sum().reset_index(name='revenue_usd'))
    
    # Crash rate: crashes / total events
    events_df['is_crash'] = (events_df['event_type'] == 'crash').astype(int)
    crash_rate = (events_df.groupby(['date', 'platform', 'server_region'])
                  .apply(lambda x: x['is_crash'].sum() / len(x))
                  .reset_index(name='crash_rate'))
    
    # Feature adoption
    feature_events = events_df[events_df['event_type'].isin(['feature_viewed', 'feature_used'])]
    feature_users = (feature_events.groupby(['date', 'platform', 'server_region'])['player_id']
                     .nunique().reset_index(name='feature_users'))
    
    # Merge all metrics
    metrics = dau.merge(session_dur, on=['date','platform','server_region'], how='left')
    metrics = metrics.merge(revenue, on=['date','platform','server_region'], how='left')
    metrics = metrics.merge(crash_rate, on=['date','platform','server_region'], how='left')
    metrics = metrics.merge(feature_users, on=['date','platform','server_region'], how='left')
    
    # Derived KPIs
    metrics['arpu']              = metrics['revenue_usd'] / metrics['dau'].clip(1)
    metrics['feature_adopt_rate'] = metrics['feature_users'] / metrics['dau'].clip(1)
    metrics['updated_timestamp'] = datetime.now()
    
    logger.info(f"Transformed → {len(metrics):,} rows | "
                f"{metrics['dau'].sum():,} total player-sessions | "
                f"${metrics['revenue_usd'].sum():,.2f} revenue")
    return metrics


# ─────────────────────────────────────────────
# 3. LOAD — Write to warehouse
# ─────────────────────────────────────────────

def load_to_warehouse(metrics_df, table_name='fact_game_health_daily'):
    """
    Load aggregated metrics to data warehouse.
    In production: writes to Databricks / Snowflake / BigQuery.
    Here: prints summary and returns in-memory.
    """
    logger.info(f"Loading {len(metrics_df):,} rows → {table_name}")
    
    # Validate required columns
    required = ['date','platform','server_region','dau','revenue_usd','crash_rate']
    missing = [c for c in required if c not in metrics_df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # Data quality checks
    assert metrics_df['dau'].min() >= 0,     "DAU must be non-negative"
    assert metrics_df['crash_rate'].max() < 1, "Crash rate must be < 100%"
    assert metrics_df['revenue_usd'].min() >= 0, "Revenue must be non-negative"
    
    logger.info(f"✅ Data quality checks passed → {table_name} updated successfully")
    return metrics_df


# ─────────────────────────────────────────────
# 4. ALERT SYSTEM — Anomaly detection
# ─────────────────────────────────────────────

ALERT_THRESHOLDS = {
    'dau':              {'drop_pct': 0.15,   'direction': 'below', 'severity': 'CRITICAL'},
    'revenue_usd':      {'drop_pct': 0.20,   'direction': 'below', 'severity': 'CRITICAL'},
    'crash_rate':       {'spike_pct': 0.50,  'direction': 'above', 'severity': 'WARNING'},
    'avg_session_duration_min': {'drop_pct': 0.20, 'direction': 'below', 'severity': 'WARNING'},
    'feature_adopt_rate': {'drop_pct': 0.30, 'direction': 'below', 'severity': 'INFO'},
}

def run_anomaly_detection(current_df, baseline_df=None):
    """
    Compare current metrics to baseline and fire alerts on anomalies.
    In production: compares to 7-day rolling average.
    """
    # Simulate baseline (current + random noise)
    if baseline_df is None:
        baseline_df = current_df.copy()
        baseline_df['dau']           = (current_df['dau'] * np.random.uniform(0.95, 1.05, len(current_df))).astype(int)
        baseline_df['revenue_usd']   = current_df['revenue_usd'] * np.random.uniform(0.95, 1.08, len(current_df))
        baseline_df['crash_rate']    = current_df['crash_rate'] * np.random.uniform(0.85, 1.0, len(current_df))
    
    alerts = []
    
    current_agg = current_df[['dau','revenue_usd','crash_rate',
                               'avg_session_duration_min','feature_adopt_rate']].mean()
    baseline_agg = baseline_df[['dau','revenue_usd','crash_rate',
                                 'avg_session_duration_min','feature_adopt_rate']].mean()
    
    for metric, config in ALERT_THRESHOLDS.items():
        if metric not in current_agg.index:
            continue
        curr = current_agg[metric]
        base = baseline_agg[metric]
        if base == 0:
            continue
        deviation = (curr - base) / base
        
        fired = False
        if config['direction'] == 'below' and deviation < -config['drop_pct']:
            fired = True
        elif config['direction'] == 'above' and deviation > config.get('spike_pct', 0):
            fired = True
        
        if fired:
            alerts.append({
                'metric':       metric,
                'current':      round(curr, 4),
                'baseline':     round(base, 4),
                'deviation_pct': round(deviation * 100, 1),
                'severity':     config['severity'],
            })
    
    return alerts


def print_game_health_snapshot(metrics_df, alerts):
    """Print executive health snapshot to console."""
    agg = metrics_df.agg({
        'dau': 'sum', 'revenue_usd': 'sum',
        'avg_session_duration_min': 'mean',
        'crash_rate': 'mean', 'arpu': 'mean',
        'feature_adopt_rate': 'mean',
    })
    
    status = "🔴 CRITICAL" if any(a['severity'] == 'CRITICAL' for a in alerts) else \
             "🟡 WARNING"  if any(a['severity'] == 'WARNING'  for a in alerts) else \
             "🟢 HEALTHY"
    
    print("\n" + "="*60)
    print("GAME HEALTH SNAPSHOT")
    print("="*60)
    print(f"  Status: {status}  |  Updated: {datetime.now().strftime('%H:%M:%S')}")
    print(f"\n  DAU:                  {int(agg['dau']):,}")
    print(f"  Revenue (period):     ${agg['revenue_usd']:,.0f}")
    print(f"  ARPU:                 ${agg['arpu']:.3f}")
    print(f"  Avg session:          {agg['avg_session_duration_min']:.1f} min")
    print(f"  Crash rate:           {agg['crash_rate']:.2%}")
    print(f"  Feature adoption:     {agg['feature_adopt_rate']:.1%}")
    
    if alerts:
        print(f"\n  ALERTS ({len(alerts)}):")
        for a in alerts:
            icon = '🔴' if a['severity'] == 'CRITICAL' else '🟡' if a['severity'] == 'WARNING' else '🟢'
            print(f"  {icon} [{a['severity']}] {a['metric']}: {a['deviation_pct']:+.1f}% vs baseline")
    else:
        print("\n  ✅ No alerts — all metrics within normal range")


# ─────────────────────────────────────────────
# 5. FULL PIPELINE RUNNER
# ─────────────────────────────────────────────

def run_pipeline(hours_back=1):
    """
    Execute the full ETL pipeline:
    Extract → Transform → Load → Alert
    """
    logger.info("="*50)
    logger.info("Starting game health ETL pipeline")
    logger.info("="*50)
    
    # E
    raw = extract_game_events(hours_back=hours_back, n_events=50000, seed=42)
    
    # T
    metrics = transform_to_daily_metrics(raw)
    
    # L
    loaded = load_to_warehouse(metrics)
    
    # Alert
    alerts = run_anomaly_detection(loaded)
    print_game_health_snapshot(loaded, alerts)
    
    logger.info("Pipeline complete ✅")
    return loaded, alerts


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    metrics, alerts = run_pipeline(hours_back=24)
    print(f"\n📊 Metrics table: {len(metrics):,} rows × {len(metrics.columns)} columns")
    print(f"   Columns: {list(metrics.columns)}")
