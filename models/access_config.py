from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class CloudAccessConfig(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    client_id: int = Field(foreign_key="client.id")
    provider: str
    credential_reference: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_used_at: Optional[datetime] = None
