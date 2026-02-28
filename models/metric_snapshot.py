from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class MetricSnapshot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    period_start: datetime
    period_end: datetime
    ai_cost_usd: float
    estimated_kwh: float
    estimated_co2_kg: float
    gpu_hours: float
    model_family: str
    score: str
    oversize_ratio: float
    estimated_monthly_waste_usd: float
    created_at: datetime = Field(default_factory=datetime.utcnow)
