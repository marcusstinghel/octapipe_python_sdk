from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union
from uuid import UUID

from octapipe_python_sdk.models import UserModel


class DatabaseRecordModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    name: str = Field(default=None, alias='name')
    custom_fields_values: Optional[Union[Dict[str, Any], List[Any]]] = Field(default=None, alias='custom_fields_values')
    database_uuid: UUID = Field(default=None, alias='database_uuid')
    database_name: str = Field(default=None, alias='database_name')
    creator_user: UserModel = Field(default=None, alias='creator_user')
    owner_user: Optional[UserModel] = Field(default=None, alias='owner_user')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
