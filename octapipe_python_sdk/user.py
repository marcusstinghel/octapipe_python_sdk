from uuid import UUID
import requests
import json
import os
from .models import UserModel


class User(UserModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = 'users'
        self.__get_environment_vars()

    @classmethod
    def get(cls, uuid: str):
        user_uuid = UUID(uuid)
        user = cls()
        user.__get_environment_vars()
        url = f'{user.__url}/{user_uuid}'
        response = requests.get(url=url, headers=user.__headers)
        user_content = response.json()
        response_message = response.reason if response.reason else response.json()
        return cls(**user_content) if response.status_code == 200 else f'{response.status_code} - {response_message}'

    @classmethod
    def get_all(cls, page: int = 1):
        user = cls()
        user.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=user.__url, headers=user.__headers, params=params)
        users = [cls(**user) for user in response.json()['data']]
        response_message = response.reason if response.reason else response.json()
        return users if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes(is_post=True)
        user_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=user_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response_message}'

    def update(self):
        self.__validate_attributes(is_update=True)
        url = f'{self.__url}/{self.uuid}'
        user_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.put(url=url, headers=self.__headers, json=user_data)
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
        self.__url = f'{os.getenv("API_URL")}/{self.__endpoint}'
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}

    def __validate_attributes(self, is_post=False, is_update=False, is_delete=False):
        if is_post:
            if not self.initial_password:
                raise ValueError("initial_password is required for user.")
        if is_update or is_delete:
            if not self.uuid:
                raise ValueError("user_uuid is required for user.")
        if is_update or is_post:
            if not self.first_name:
                raise ValueError("first_name is required for user.")
            if not self.last_name:
                raise ValueError("last_name is required for user.")
            if not self.enabled_pipelines:
                raise ValueError("enabled_pipelines is required for user.")
            if not self.role:
                raise ValueError("role is required for user.")
            if not self.email:
                raise ValueError("email is required for user.")
