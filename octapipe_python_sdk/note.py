from uuid import UUID
import requests
import json
import os
from .models import NoteModel


class Note(NoteModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = 'notes'
        self.__get_environment_vars()

    @classmethod
    def get_all(cls, entity: str, record_uuid: str, page: int = 1):
        note = cls()
        note.__get_environment_vars()
        params = {'entity': entity, 'record_uuid': record_uuid, 'page': page}
        response = requests.get(url=note.__url, headers=note.__headers, params=params)
        notes = [cls(**note) for note in response.json()]
        response_message = response.reason if response.reason else response.json()
        return notes if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes(is_post=True)
        note_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=note_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
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
        self.__url = f'{os.getenv("API_URL")}/{self.__endpoint}'
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}

    def __validate_attributes(self, is_post=False, is_delete=False):
        if is_post:
            if not self.entity:
                raise ValueError("entity is required for note.")
            if not self.record_uuid:
                raise ValueError("record_uuid is required for note.")
            if not self.note:
                raise ValueError("note is required for note.")
        if is_delete:
            if not self.uuid:
                raise ValueError("note_uuid is required for note.")
