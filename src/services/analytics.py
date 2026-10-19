import os
from typing import List, Dict, Any, Optional
from src.database import Database
from src.config import config
from queries import get_query

class AnalyticsService:
    """Analytics report generation orchestrator."""

    def __init__(self, db: Optional[Database] = None):
        self.db = db or Database(config.db_path)

    def get_daily_cost_per_user(self) -> List[Dict[str, Any]]:
        sql = get_query("daily_cost_per_user")
        cursor = self.db.execute(sql)
        return [dict(row) for row in cursor.fetchall()]

    def get_model_utilization(self) -> List[Dict[str, Any]]:
        sql = get_query("model_utilization_breakdown")
        cursor = self.db.execute(sql)
        return [dict(row) for row in cursor.fetchall()]

    def get_cost_spikes(self, threshold: Optional[float] = None) -> List[Dict[str, Any]]:
        sql = get_query("cost_spike_detector")
        cursor = self.db.execute(sql)
        rows = [dict(row) for row in cursor.fetchall()]
        if threshold is not None:
            rows = [r for r in rows if r["daily_spend"] > threshold]
        return rows

    def get_token_trends(self) -> List[Dict[str, Any]]:
        sql = get_query("token_trend_analysis")
        cursor = self.db.execute(sql)
        return [dict(row) for row in cursor.fetchall()]
