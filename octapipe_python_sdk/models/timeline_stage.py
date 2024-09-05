from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TimelineStage(BaseModel):
    pipeline_stage: str = Field(default=None, alias='pipeline_stage')
    pipeline_stage_index: int = Field(default=None, alias='pipeline_stage_index')
    total: int = Field(default=None, alias='total')
    moved_at: Optional[datetime] = Field(default=None, alias='moved_at')
