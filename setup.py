from typing import List
from setuptools import setup, find_packages

NAME = 'octapipe_python_sdk'
SDK = 'octapipe_python_sdk'
REQUIREMENTS_FILE = 'requirements.txt'
LONG_DESCRIPTION_FILE = 'README.md'
VERSION = '1.0.0'


def get_requirements(requirements_file_path: str) -> List[str]:
    """
    Obtém todas as dependências listadas em um arquivo de dependências.
    :param requirements_file_path: caminho para o arquivo de dependências.
    :return: lista de strings contendo as dependências.
    """
    with open(requirements_file_path, 'r', encoding='utf-8-sig') as requirements_file:
        return [req.strip() for req in requirements_file.readlines()]


def get_long_description(long_description_file: str) -> str:
    with open(long_description_file, "r", encoding="utf-8") as fh:
        long_description = fh.read()
    return long_description


all_requirements = get_requirements(requirements_file_path=REQUIREMENTS_FILE)
long_description = get_long_description(long_description_file=LONG_DESCRIPTION_FILE)

setup(
    name=NAME,
    version=VERSION,
    install_requires=all_requirements,
    long_description=long_description,
    packages=find_packages()
)
