from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Literal, Union
from uuid import UUID


class UserModel(BaseModel):
    uuid: UUID = Field(default=None, alias='uuid')
    first_name: str = Field(default=None, alias='first_name')
    last_name: str = Field(default=None, alias='last_name')
    initial_password: str = Field(default=None, alias='initial_password')
    enabled_pipelines: List[UUID] = Field(default=None, alias='enabled_pipelines')
    role: Literal['admin', 'user'] = Field(default=None, alias='role')
    email: str = Field(default=None, alias='email')
    is_data_access_restricted: bool = Field(default=None, alias='is_data_access_restricted')
    is_active: bool = Field(default=None, alias='is_active')
    created_at: datetime = Field(default=None, alias='created_at')
    updated_at: Optional[datetime] = Field(default=None, alias='updated_at')
    deleted_at: Optional[datetime] = Field(default=None, alias='deleted_at')
    job: Optional[str] = Field(default=None, alias='job')
    phone1: Optional[str] = Field(default=None, alias='phone1')
    phone2: Optional[str] = Field(default=None, alias='phone2')
    custom_fields_values: Optional[Union[Dict[str, Any], List[Any]]] = Field(default=None, alias='custom_fields_values')
    picture: Optional[str] = Field(default=None, alias='picture')
    recover_code: Optional[str] = Field(default=None, alias='recover_code')
    auth_code: Optional[str] = Field(default=None, alias='auth_code')
    email_verified_at: Optional[str] = Field(default=None, alias='email_verified_at')
