from uuid import UUID
import requests
import json
import os
from .models import DatabaseRecordModel


class DatabaseRecord(DatabaseRecordModel):
    __url: str
    __database_endpoint: str
    __record_endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__database_endpoint = 'databases'
        self.__record_endpoint = 'records'
        self.__get_environment_vars()

    @classmethod
    def get(cls, uuid: str):
        database_record_uuid = UUID(uuid)
        database_record = cls()
        database_record.__get_environment_vars()
        url = f'{database_record.__url}/{database_record_uuid}'
        response = requests.get(url=url, headers=database_record.__headers)
        database_record_content = response.json()
        response_message = response.reason if response.reason else response.json()
        return cls(
            **database_record_content) if response.status_code == 200 else f'{response.status_code} - {response_message}'

    @classmethod
    def get_all(cls, page: int = 1):
        database_record = cls()
        database_record.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=database_record.__url, headers=database_record.__headers, params=params)
        database_records = [cls(**database_record) for database_record in response.json()]
        response_message = response.reason if response.reason else response.json()
        return database_records if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes(is_post=True)
        database_record_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=database_record_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response_message}'

    def update(self):
        self.__validate_attributes(is_update=True)
        url = f'{self.__url}/{self.uuid}'
        database_record_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.put(url=url, headers=self.__headers, json=database_record_data)
        response_message = response.reason if response.reason else response.json()
        return f'{response.status_code} - {response_message}'

    def delete(self):
        self.__validate_attributes(is_delete=True)
        url = f'{self.__url}/{self.uuid}'
        response = requests.delete(url=url, headers=self.__headers)
        response_message = response.reason if response.reason else response.json()
        return f'{response.status_code} - {response_message}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_sdk.auth.login()')
        self.__url = f'{os.getenv("API_URL")}/{self.__database_endpoint}/{self.database_uuid}/{self.__record_endpoint}'
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}

    def __validate_attributes(self, is_post=False, is_update=False, is_delete=False):
        if is_update or is_delete:
            if not self.uuid:
                raise ValueError("database_record_uuid is required for database_record.")
        if is_update or is_post:
            if not self.database_uuid:
                raise ValueError("database_uuid is required for database_record.")
            if not self.name:
                raise ValueError("name is required for database_record.")
            if not self.custom_fields_values:
                raise ValueError("custom_fields_values is required for database_record.")
