"""
Module responsible for execute all the API calls.
"""

import json
import sys
import os
import time
import requests
from credential import token
from crhc import CURRENT_VERSION

# FIELDS_TO_RETRIEVE = "?fields[system_profile]=number_of_cpus,number_of_sockets,cores_per_socket,system_memory_bytes,bios_release_date,bios_vendor,bios_version,operating_system,os_kernel_version,os_release,infrastructure_type,infrastructure_vendor,insights_client_version"
# FIELDS_TO_RETRIEVE = "?fields[system_profile]=number_of_sockets"
FIELDS_TO_RETRIEVE = ""


def check_authentication(response):
    """
    Check if the current credential is valid and authenticating, if not, will
    ask for the customer to rerun the command './crhc user set'
    """
    if response.status_code != 200:
        # print("You are not authenticated yet.")
        # print("Please, use './crhc user set', set the username and password and try again.")
        print("Error: Failed to create C.RH.C connection: Not logged in, credentials aren't set, run the 'crhc login' command")
        sys.exit()


def inventory_list():
    """
    This def will collect the first 50 HBI entries
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    # response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)

    list_of_servers = []
    inventory_full_detail = {'results': '', 'total': response.json()['total']}
    inventory_full_detail['results'] = list_of_servers

    stage_list = []
    stage_dic = {'server': stage_list}

    for server in response.json()['results']:

        access_token = token.get_token()

        try:
            stage_dic['server'] = server
        except json.decoder.JSONDecodeError:
            stage_dic['server'] = {}

        server_id = server['id']
        url = "https://console.redhat.com/api/inventory/v1/hosts/" + server_id + "/system_profile" + FIELDS_TO_RETRIEVE

        response_system_profile = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        try:
            stage_dic['system_profile'] = response_system_profile.json()['results'][0]['system_profile']
        except json.decoder.JSONDecodeError:
            stage_dic['system_profile'] = {}
        except KeyError:
            stage_dic['system_profile'] = {}

        list_of_servers.append(stage_dic)
        stage_dic = {}

    return inventory_full_detail


def inventory_list_all():
    """
    This def will collect all the HBI entries
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=1"
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    # response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)

    num_of_pages = int(response.json()['total'] / 50 + 1)

    list_of_servers = []
    inventory_full_detail = {'results': '', 'total': response.json()['total']}
    inventory_full_detail['results'] = list_of_servers

    stage_list = []
    stage_dic = {'server': stage_list}

    # Just to collect the information when the # of hosts is up to 50, num_of_pages should never be lower than 2.
    num_of_pages = max(2, num_of_pages)

    for page in range(1, num_of_pages):
        url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=50&page=" + str(page)
        # response = requests.get(url, auth=(USER, PASSWORD))
        response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        # print(json.dumps(response.json(), indent=4))

        for server in response.json()['results']:

            access_token = token.get_token()

            try:
                stage_dic['server'] = server
            except json.decoder.JSONDecodeError:
                stage_dic['server'] = {}

            server_id = server['id']
            url = "https://console.redhat.com/api/inventory/v1/hosts/" + server_id + "/system_profile" + FIELDS_TO_RETRIEVE

            response_system_profile = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
            try:
                stage_dic['system_profile'] = response_system_profile.json()['results'][0]['system_profile']
            except json.decoder.JSONDecodeError:
                stage_dic['system_profile'] = {}
            except KeyError:
                stage_dic['system_profile'] = {}

            list_of_servers.append(stage_dic)
            stage_dic = {}

    return inventory_full_detail


def inventory_list_search_by_name(fqdn):
    """
    This def will search the HBI entries by keyword
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api/inventory/v1/hosts?hostname_or_id=" + fqdn

    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    # response = requests.get(url, auth=(USER, PASSWORD))
    check_authentication(response)

    list_of_servers = []
    inventory_full_detail = {'results': '', 'total': response.json()['total']}
    inventory_full_detail['results'] = list_of_servers

    stage_list = []
    stage_dic = {'server': stage_list}

    for server in response.json()['results']:

        access_token = token.get_token()

        stage_dic['server'] = server

        server_id = server['id']
        url = "https://console.redhat.com/api/inventory/v1/hosts/" + server_id + "/system_profile" + FIELDS_TO_RETRIEVE

        response_system_profile = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        try:
            stage_dic['system_profile'] = response_system_profile.json()['results'][0]['system_profile']
        except json.decoder.JSONDecodeError:
            stage_dic['system_profile'] = {}
        except KeyError:
            stage_dic['system_profile'] = {}

        list_of_servers.append(stage_dic)
        stage_dic = {}

    return inventory_full_detail


def swatch_list():
    """
    This def will collect the first 100 entries from Subscription Watch
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    # response = requests.get(url, auth=(USER, PASSWORD))
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    check_authentication(response)
    return response.json()


def swatch_list_all():
    """
    This def will collect all the entries from Subscription Watch
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=0&sort=display_name"
    # response = requests.get(url, auth=(USER, PASSWORD))
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    check_authentication(response)
    num_of_pages = round(response.json()['meta']['count'] / 100 + 1)

    dic_full_list = {'data': ''}
    full_list = []

    count = 0
    for page in range(0, num_of_pages):
        url = "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit=100&offset=" + str(count) + "&sort=display_name"
        count = count + 100

        # response = requests.get(url, auth=(USER, PASSWORD))
        response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})

        for entry in response.json()['data']:
            full_list.append(entry)

    dic_full_list['data'] = full_list
    return dic_full_list


def swatch_socket_summary():
    """
    This def will present all the usage information in socket and
    summary format from Subscription Watch
    """
    access_token = token.get_token()

    item_list = swatch_list_all()

    baremetal_count = 0
    hypervisor_count = 0
    vm_with_no_host_guest_mapping = 0
    cloud_count = 0
    total_socket_count = 0

    for server in item_list['data']:
        # Baremetal server
        if server['hardware_type'] == 'PHYSICAL' and server['is_hypervisor'] is False:
            baremetal_count = baremetal_count + server['sockets']
        # Hypervisor server
        if server['hardware_type'] == 'PHYSICAL' and server['is_hypervisor'] is True:
            hypervisor_count = hypervisor_count + server['sockets']
        # VM with no host guest mapping
        if server['hardware_type'] == 'VIRTUALIZED' and server['is_hypervisor'] is False and server['is_unmapped_guest'] is True:
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


def endpoint_list():
    """
    This def will collect the API endpoints and will list them
    """
    access_token = token.get_token()

    url = "https://console.redhat.com/api"
    # response = requests.get(url, auth=(USER, PASSWORD))
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    check_authentication(response)
    return response.json()
    # print(json.dumps(response.json(), indent=4))


def get_command(api_url):
    """
    This def will call the API endpoint directly
    """
    access_token = token.get_token()

    # Testing if the customer is passing the full endpoint path or just the
    # initial endpoint url. When passing the short one, the script will test
    # and will show all the full url available.
    if len(api_url.split("/")) < 4:

        # retrieving the openapi json file
        url = "https://console.redhat.com/" + api_url + "/v1/openapi.json"
        # response = requests.get(url, auth=(USER, PASSWORD))
        response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        check_authentication(response)

        available_paths = response.json()['paths'].keys()
        for path in available_paths:
            print("{}/v1{}".format(api_url, path))

    else:
        # retrieving the full url
        url = "https://console.redhat.com/" + api_url
        # response = requests.get(url, auth=(USER, PASSWORD))
        response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        check_authentication(response)
        return response.json()


def whoami():
    """
    Used to retrieve the current user information via API
    """
    access_token = token.get_token()

    url = "https://api.openshift.com/api/accounts_mgmt/v1/current_account"
    # response = requests.get(url, auth=(USER, PASSWORD))
    response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
    check_authentication(response)
    return response.json()
    # print(json.dumps(response.json(), indent=4))


def update_check():
    """
    Checking if there is any new available version on GitHub, if yes, it will
    let the user aware to download it.
    """

    home_dir = os.path.expanduser('~')

    # In case the file be not around yet.
    answer = ""

    if os.path.exists(home_dir + "/.crhc.version"):
        file_age = (time.time() - (os.stat(home_dir + "/.crhc.version").st_mtime))
        # print(int(file_age))

        # 43200 sec == 12h
        if int(file_age) < 43200:
            file_ref = open(home_dir + "/.crhc.version")
            available_version = file_ref.read()

            if int(available_version.replace(".", "")) > int(CURRENT_VERSION.replace(".", "")):
                answer = "Please, download the latests version from https://github.com/C-RH-C/crhc-cli/releases/latest\n\
Current Version: {}\nNew Version: {}".format(CURRENT_VERSION, available_version)
            else:
                answer = ""
        else:
            os.remove(home_dir + "/.crhc.version")

    else:
        access_token = token.get_token()

        url = "https://github.com/C-RH-C/crhc-cli/releases/latest"
        response = requests.get(url, headers={"Authorization": "Bearer {}".format(access_token)})
        available_version = response.url.split("/")[7]

        file_obj = open(home_dir + "/.crhc.version", "w")
        file_obj.write(available_version)

        if int(available_version.replace(".", "")) > int(CURRENT_VERSION.replace(".", "")):
            answer = "Please, download the latests version from https://github.com/C-RH-C/crhc-cli/releases/latest\n\
Current Version: {}\nNew Version: {}".format(CURRENT_VERSION, available_version)
        else:
            answer = ""

    return answer
