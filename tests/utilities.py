import json
from uuid import uuid4
from random import choice

from vvrest.vault import Vault

from .settings import credentials_file, parameters_file


def get_vault_object(user_web_token=None, jwt=None):
    """
    :param user_web_token: string UUID(version=4), used for user impersonation
    :param jwt: str, JSON Web Token
    :return: Vault
    """
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)

    vault = Vault(credentials['url'], credentials['customer_alias'], credentials['database_alias'],
                  credentials['client_id'], credentials['client_secret'], user_web_token, jwt)

    return vault


def generate_random_uuid():
    """
    :return: string uuid4
    """
    uuid = str(uuid4())

    return uuid


def get_parameters_json():
    """
    :return: dict
    """
    with open(parameters_file) as parameters_json:
        parameters = json.load(parameters_json)

    return parameters


def get_test_email_address():
    """
    :return: string
    """
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)

    return credentials['email_address']


def get_random_string(length):
    """
    :param length: int
    :return: string
    """
    char_choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # TODO: use random.choices with python upgrade
    random_string = ''.join(choice(char_choices) for i in range(length))

    return random_string
