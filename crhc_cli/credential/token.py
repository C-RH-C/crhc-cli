"""
.. code-block:: text

    Module responsible for the token feature
"""

import os
import json
import sys
# import datetime
from time import time as timetime
import jwt
import requests


# Conf file used to store the access_key and some additional information
CONF_FILE = "/.crhc.conf"


def set_token(token):
    """
    Responsible for receive the customer token and
    create the access_key via API request
    """

    token_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

    body = {}
    body["client_id"] = "cloud-services"
    body["grant_type"] = "refresh_token"
    body["refresh_token"] = token

    refresh = requests.post(token_url, data=body)
    full_response = refresh.json()
    try:
        access_token = refresh.json()["access_token"]
    except KeyError:
        access_token = None

    # Testing the access and credentials
    url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = requests.get(
        url, headers={"Authorization": "Bearer {}".format(access_token)}
    )

    if response.status_code == 200:
        print("Authenticated and ready to go!")
    else:
        print("Please, type again, wrong token")
        sys.exit()

    home_dir = os.path.expanduser("~")
    with open(home_dir + CONF_FILE, "w") as file_obj:
        file_obj.write(json.dumps(full_response, indent=4))


def get_token():
    """
    Used to return the access_token, also, this is the definition responsible
    to check the expiration time, once the current time is == or >, the
    refresh call will be made.
    """

    home_dir = os.path.expanduser("~")

    #  temporary workaround for when the file is not present and the script
    # is called.
    token_info = {}

    try:
        file_obj = open(home_dir + CONF_FILE, "r")
        token_info = json.load(file_obj)
    except FileNotFoundError:
        delete_token()
    except json.decoder.JSONDecodeError:
        delete_token()

    try:
        access_token = token_info["access_token"]
    except KeyError:
        access_token = "Error: Failed to create C.RH.C connection: Not logged in, \
credentials aren't set, run the 'crhc login' command"

    try:
        # Using jwt to collect some information from the local token file
        exp_date_from_token = jwt.decode(
            access_token, options={"verify_signature": False}
        )["exp"]
        # current_time = datetime.datetime.now()

        # Modified to support MS Windows & Linux.
        # current_time_epoch = int(current_time.strftime('%s'))
        current_time_epoch = int(timetime())

        # Conditional to check if the token is expired. In case of
        # affirmative, the same will be refreshed.

        # Setting the incremental to 500 in oder to avoid issues when
        # executing the `ts dump`. It's working with no issues.
        if (current_time_epoch + 800) >= exp_date_from_token:
            refresh_token()

    except jwt.exceptions.DecodeError:
        ...

    return access_token


def refresh_token():
    """
    Responsible for refresh the token and update the local file with the fresh
    information
    """

    home_dir = os.path.expanduser("~")
    file_obj = open(home_dir + CONF_FILE, "r")
    token_info = json.load(file_obj)
    refresh_tk = token_info["refresh_token"]

    token_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

    body = {}
    body["client_id"] = "cloud-services"
    body["grant_type"] = "refresh_token"
    body["refresh_token"] = refresh_tk

    refresh = requests.post(token_url, data=body)
    full_response = refresh.json()
    try:
        access_token = refresh.json()["access_token"]
    except KeyError:
        access_token = "Error: Failed to create C.RH.C connection: Not logged in, \
credentials aren't set, run the 'crhc login' command"

    home_dir = os.path.expanduser("~")
    with open(home_dir + CONF_FILE, "w") as file_obj:
        file_obj.write(json.dumps(full_response, indent=4))

    return access_token


def delete_token():
    """
    Responsible for delete the local information from CONF_FILE
    """

    home_dir = os.path.expanduser("~")
    with open(home_dir + CONF_FILE, "w") as file_obj:
        file_obj.write("{}")
