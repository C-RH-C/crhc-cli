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
    print(json.dumps(response.json(), indent=4))


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
        print(json.dumps(response.json(), indent=4))


def inventory_list_search_by_name(fqdn):
    """
    This def will search the HBI entries by keyword
    """
    url = "https://console.redhat.com/api/inventory/v1/hosts?hostname_or_id=" + fqdn
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    print(json.dumps(response.json(), indent=4))


def swatch_list():
    """
    This def will collect the first 100 entries from Subscription Watch
    """
    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    return response.json()


def swatch_list_all():
    """
    This def will collect all the entries from Subscription Watch
    """
    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)
    num_of_pages = round(response.json()['meta']['count'] / 100 + 1)

    dic_full_list = {'data':''}
    full_list = []

    count = 0
    for page in range(0, num_of_pages):
        url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=" + str(count) + "&sort=display_name"
        count = count + 100

        response = requests.get(url, auth=(USER, PASSWORD))

        for entry in response.json()['data']:
            full_list.append(entry)

    dic_full_list['data'] = full_list
    return dic_full_list


def swatch_socket_summary():
    """
    This def will present all the usage information in socket and
    summary format from Subscription Watch
    """

    item_list = swatch_list_all()

    baremetal_count = 0
    hypervisor_count = 0
    vm_with_no_host_guest_mapping = 0
    cloud_count = 0
    total_socket_count = 0

    for server in item_list['data']:
        # Baremetal server
        if server['hardware_type'] == 'PHYSICAL' and server['is_hypervisor'] == False:
            baremetal_count = baremetal_count + server['sockets']
        # Hypervisor server
        if server['hardware_type'] == 'PHYSICAL' and server['is_hypervisor'] == True:
            hypervisor_count = hypervisor_count + server['sockets']
        # VM with no host guest mapping
        if server['hardware_type'] == 'VIRTUALIZED' and server['is_hypervisor'] == False and server['is_unmapped_guest'] == True:
            vm_with_no_host_guest_mapping = vm_with_no_host_guest_mapping + server['sockets']
        # Cloud server
        if server['hardware_type'] == 'CLOUD':
            cloud_count = cloud_count + server['sockets']
    
        total_socket_count = total_socket_count + server['sockets']


    print("Public Cloud ........: {}".format(cloud_count))
    print("Virtualized RHEL ....: {}".format(vm_with_no_host_guest_mapping))
    print("Physical RHEL .......: {}".format(baremetal_count))
    print("Hypervisors .........: {}".format(hypervisor_count))
    print("----------------------")
    print("Total # of Sockets ..: {}".format(total_socket_count))