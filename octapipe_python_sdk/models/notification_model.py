from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID


class NotificationModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    owner_user_uuid: UUID = Field(default=None, alias='owner_user_uuid')
    record_uuid: UUID = Field(default=None, alias='record_uuid')
    entity: Literal['user', 'pipeline_card', 'task', 'database_record'] = Field(default=None, alias='entity')
    message: str = Field(default=None, alias='message')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    read_at: Optional[datetime] = Field(default=None, alias='read_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
