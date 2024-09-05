from pydantic import BaseModel, Field
from uuid import UUID


class PipelineStageModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    name: str = Field(default=None, alias='name')
