import os
from dotenv import load_dotenv
import requests


def login(domain: str, email: str, password: str):
    __dotenv_file_path = os.path.dirname(os.path.abspath(__file__)) + '/.env'
    load_dotenv(__dotenv_file_path)
    __api_url = 'https://api.octapipe.dev'
    __url = __api_url + '/login'
    __body = {
        "domain": domain,
        "email": email,
        "password": password
    }
    __response = requests.post(url=__url, json=__body)
    if __response.status_code == 200:
        __key = 'BEARER_TOKEN='
        __value = __response.json()['authorization']['token']
        with open(__dotenv_file_path, 'w') as __file:
            __file.writelines(f"{'API_URL='}{__api_url}\n")
        with open(__dotenv_file_path, "r") as __file:
            __lines = __file.readlines()
        __found = False
        for i, line in enumerate(__lines):
            if line.startswith(f"{__key}"):
                __lines[i] = f"{__key}{__value}\n"
                __found = True
                break
        if not __found:
            __lines.append(f"{__key}{__value}\n")
        with open(__dotenv_file_path, "w") as __file:
            __file.writelines(__lines)
        load_dotenv(__dotenv_file_path)
    else:
        raise ValueError(f'login was not done - {__response.status_code} - {__response.reason}')
