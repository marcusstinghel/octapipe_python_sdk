from uuid import UUID
import requests
import json
import os
from .models import PipelineCardModel


class PipelineCard(PipelineCardModel):
    __url: str
    __pipeline_endpoint: str
    __card_endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__pipeline_endpoint = 'pipelines'
        self.__card_endpoint = 'cards'
        self.__get_environment_vars()

    @classmethod
    def get(cls, uuid: str):
        pipeline_card_uuid = UUID(uuid)
        pipeline_card = cls()
        pipeline_card.__get_environment_vars()
        url = f'{pipeline_card.__url}/{pipeline_card_uuid}'
        response = requests.get(url=url, headers=pipeline_card.__headers)
        pipeline_card_content = response.json()
        response_message = response.reason if response.reason else response.json()
        return cls(
            **pipeline_card_content) if response.status_code == 200 else f'{response.status_code} - {response_message}'

    @classmethod
    def get_all(cls, page: int = 1):
        pipeline_card = cls()
        pipeline_card.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=pipeline_card.__url, headers=pipeline_card.__headers, params=params)
        pipeline_cards = [cls(**pipeline_card) for pipeline_card in response.json()]
        response_message = response.reason if response.reason else response.json()
        return pipeline_cards if response.status_code == 200 else f'{response.status_code} - {response_message}'

    def post(self):
        self.__validate_attributes(is_post=True)
        pipeline_card_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.post(url=self.__url, headers=self.__headers, json=pipeline_card_data)
        response_message = response.reason if response.reason else response.json()
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response_message}'

    def update(self):
        self.__validate_attributes(is_update=True)
        url = f'{self.__url}/{self.uuid}'
        pipeline_card_data = json.loads(self.model_dump_json(exclude_none=True))
        response = requests.put(url=url, headers=self.__headers, json=pipeline_card_data)
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
        self.__url = f'{os.getenv("API_URL")}/{self.__pipeline_endpoint}/{self.pipeline_uuid}/{self.__card_endpoint}'
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}

    def __validate_attributes(self, is_post=False, is_update=False, is_delete=False):
        if is_update or is_delete:
            if not self.uuid:
                raise ValueError("pipeline_card_uuid is required for pipeline_card.")
        if is_update or is_post:
            if not self.pipeline_stage_uuid:
                raise ValueError("pipeline_stage_uuid is required for pipeline_card.")
            if not self.name:
                raise ValueError("name is required for pipeline_card.")
            if not self.sla:
                raise ValueError("sla is required for pipeline_card.")
            if not self.custom_fields_values:
                raise ValueError("custom_fields_values is required for pipeline_card.")
