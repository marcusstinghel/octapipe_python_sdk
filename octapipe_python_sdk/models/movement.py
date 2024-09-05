from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class Movement(BaseModel):
    pipeline_card_uuid: UUID = Field(default=None, alias='pipeline_card_uuid')
    user_uuid: UUID = Field(default=None, alias='user_uuid')
    from_pipeline_stage_uuid: UUID = Field(default=None, alias='from_pipeline_stage_uuid')
    to_pipeline_stage_uuid: UUID = Field(default=None, alias='to_pipeline_stage_uuid')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
