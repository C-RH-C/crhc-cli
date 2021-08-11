"""
Module responsible for execute all the API calls.
"""

import json
import sys
import requests
from credential import credential

credential_obj = credential.read_credential()

USER = ""
PASSWORD = ""

try:
    USER = credential_obj[0]
    PASSWORD = credential_obj[1]
except TypeError:
    ...


def check_authentication(response):
    """
    Check if the current credential is valid and authenticating, if not, will
    ask for the customer to rerun the command './crhc user set'
    """
    if response.status_code != 200:
        print("You are not authenticated yet.")
        print("Please, use './crhc user set', set the username and password and try again.")
        sys.exit()


def inventory_list():
    """
    This def will collect the first 50 HBI entries
    """
    url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    print(json.dumps(response.json(), indent=4, sort_keys=True))


def inventory_list_all():
    """
    This def will collect all the HBI entries
    """
    url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    num_of_pages = round(response.json()['total'] / 50 + 1)

    for page in range(1, num_of_pages + 1):
        url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=50&page=" + str(page)
        response = requests.get(url, auth=(USER, PASSWORD))
        print(json.dumps(response.json(), indent=4, sort_keys=True))


def inventory_list_search_by_name(fqdn):
    """
    This def will search the HBI entries by keyword
    """
    url = "https://console.redhat.com/api/inventory/v1/hosts?hostname_or_id=" + fqdn
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    print(json.dumps(response.json(), indent=4, sort_keys=True))


def swatch_list():
    """
    This def will collect the first 100 entries from Subscription Watch
    """
    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    print(json.dumps(response.json(), indent=4, sort_keys=True))


def swatch_list_all():
    """
    This def will collect all the entries from Subscription Watch
    """
    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    num_of_pages = round(response.json()['meta']['count'] / 100 + 1)

    count = 0
    for page in range(0, num_of_pages):
        url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=" + str(count) + "&sort=display_name"
        count = count + 100

        response = requests.get(url, auth=(USER, PASSWORD))
        print(json.dumps(response.json(), indent=4, sort_keys=True))
