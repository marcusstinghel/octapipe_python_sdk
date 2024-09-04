from uuid import UUID
import requests
import json
import os
from .models import TaskModel


class Task(TaskModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = 'tasks'
        self.__get_environment_vars()

    @classmethod
    def get(cls, uuid: str):
        task_uuid = UUID(uuid)
        task = cls()
        task.__get_environment_vars()
        url = f'{task.__url}/{task_uuid}'
        response = requests.get(url=url, headers=task.__headers)
        task_content = response.json()
        response_message = response.reason if response.reason else response.json()
        return cls(**task_content) if response.status_code == 200 else f'{response.status_code} - {response_message}'

    @classmethod
    def get_all(cls, page: int = 1):
        task = cls()
        task.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=task.__url, headers=task.__headers, params=params)
        tasks = [cls(**task) for task in response.json()['data']]
        response_message = response.reason if response.reason else response.json()
        return tasks if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes(is_post=True)
        self.__remove_seconds_for_create_or_update()
        task_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=task_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response_message}'

    def update(self):
        self.__validate_attributes(is_update=True)
        url = f'{self.__url}/{self.uuid}'
        self.__remove_seconds_for_create_or_update()
        task_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.put(url=url, headers=self.__headers, json=task_data)
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
        if is_update or is_delete:
            if not self.uuid:
                raise ValueError("task_uuid is required for task.")
        if is_update or is_post:
            if not self.title:
                raise ValueError("title is required for task.")
            if not self.start_date:
                raise ValueError("start_date is required for task.")
            if not self.end_date:
                raise ValueError("end_date is required for task.")
            if not self.start_time:
                raise ValueError("start_time is required for task.")
            if not self.end_time:
                raise ValueError("end_time is required for task.")
            if not self.status:
                raise ValueError("status is required for task.")
            if not self.priority:
                raise ValueError("priority is required for task.")

    def __remove_seconds_for_create_or_update(self):
        if len(self.start_time) == 8:
            self.start_time = self.start_time[:5]
        if len(self.end_time) == 8:
            self.end_time = self.end_time[:5]
