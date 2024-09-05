from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID

from octapipe_python_sdk.models import UserModel, PipelineCardModel, TaskModel, DatabaseRecordModel


class NoteModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    entity: Literal['user', 'pipeline_card', 'task', 'database_record'] = Field(default=None, alias='entity')
    record_uuid: UUID = Field(default=None, alias='record_uuid')
    note: str = Field(default=None, alias='note')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
    user: Optional[UserModel] = Field(default=None, alias='user')
    pipeline_card: Optional[PipelineCardModel] = Field(default=None, alias='pipeline_card')
    task: Optional[TaskModel] = Field(default=None, alias='task')
    database_record: Optional[DatabaseRecordModel] = Field(default=None, alias='database_record')
