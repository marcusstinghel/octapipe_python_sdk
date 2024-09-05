import requests
import json
import os
from .models import NotificationModel


class Notification(NotificationModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = 'notifications'
        self.__get_environment_vars()

    @classmethod
    def get_all(cls, page: int = 1):
        notification = cls()
        notification.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=notification.__url, headers=notification.__headers, params=params)
        notifications = [cls(**notification) for notification in response.json()['data']]
        response_message = response.reason if response.reason else response.json()
        return notifications if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes()
        notification_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=notification_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response_message}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_sdk.auth.login()')
        self.__url = f'{os.getenv("API_URL")}/{self.__endpoint}'
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}

    def __validate_attributes(self):
        if not self.owner_user_uuid:
            raise ValueError("owner_user_uuid is required for notification.")
        if not self.entity:
            raise ValueError("entity is required for notification.")
        if not self.record_uuid:
            raise ValueError("record_uuid is required for notification.")
        if not self.message:
            raise ValueError("message is required for notification.")
