from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union
from uuid import UUID

from octapipe_python_sdk.models import UserModel
from octapipe_python_sdk.models.movement import Movement
from octapipe_python_sdk.models.pipeline_model import PipelineModel
from octapipe_python_sdk.models.pipeline_stage_model import PipelineStageModel
from octapipe_python_sdk.models.timeline_stage import TimelineStage


class PipelineCardModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    code: str = Field(default=None, alias='code')
    name: str = Field(default=None, alias='name')
    sla: int = Field(default=None, alias='sla')
    custom_fields_values: Optional[Union[Dict[str, Any], List[Any]]] = Field(default=None, alias='custom_fields_values')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
    tags: Optional[List[str]] = Field(default=None, alias='tags')
    last_stage_updated_at: Optional[datetime] = Field(default=None, alias='last_stage_updated_at')
    pipeline: PipelineModel = Field(default=None, alias='pipeline')
    pipeline_stage: PipelineStageModel = Field(default=None, alias='pipeline_stage')
    creator_user: UserModel = Field(default=None, alias='creator_user')
    owner_user: Optional[UserModel] = Field(default=None, alias='owner_user')
    movements: List[Movement] = Field(default=None, alias='movements')
    timeline: List[TimelineStage] = Field(default=None, alias='timeline')
