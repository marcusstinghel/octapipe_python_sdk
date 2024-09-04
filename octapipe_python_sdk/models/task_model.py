from datetime import datetime, date, time
from pydantic import BaseModel, Field, constr
from typing import List, Dict, Any, Optional, Literal, Union
from uuid import UUID

from octapipe_python_sdk.models import UserModel


class TaskModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    title: str = Field(default=None, alias='title')
    start_date: str = Field(default=None, alias='start_date')
    end_date: str = Field(default=None, alias='end_date')
    start_time: str = Field(default=None, alias='start_time')
    end_time: str = Field(default=None, alias='end_time')
    status: Literal['pending', 'in_progress', 'completed'] = Field(default=None, alias='status')
    priority: Literal['low', 'medium', 'high'] = Field(default=None, alias='priority')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
    description: Optional[str] = Field(default=None, alias='description')
    pipeline_card_uuid: Optional[UUID] = Field(default=None, alias='pipeline_card_uuid')
    owner_user: UserModel = Field(default=None, alias='owner_user')
    creator_user: UserModel = Field(default=None, alias='creator_user')
