import os
import json
from uuid import uuid4
from vvrest import Vault


def get_vault_object():
    """
    :return: Vault
    """
    credentials_file = os.getcwd() + '/tests/credentials.json'
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)

    vault = Vault(credentials['url'], credentials['customer_alias'], credentials['database_alias'],
                  credentials['client_id'], credentials['client_secret'])

    return vault


def generate_random_uuid():
    """
    :return: string uuid4
    """
    uuid = str(uuid4())

    return uuid
