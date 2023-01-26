"""
.. code-block:: text

    Module responsible for execute all the API calls.
"""

# from distutils import core
import json

# from queue import Empty
# import socketserver
import sys
import os
import time
import requests
import datetime
from report import report
from credential import token
from conf import conf

# FIELDS_TO_RETRIEVE = "?fields[system_profile]=number_of_sockets"
FIELDS_TO_RETRIEVE = ""


def connection_request(url):
    """
    Definition responsible to receive the url, call it and send back the
    response, updating the token whenever necessary.
    """

    access_token = token.get_token()
    response = requests.get(
        url, headers={"Authorization": "Bearer {}".format(access_token)}
    )

    return response


def connection_request_delete(url):
    """
    Definition responsible to receive the url, call it and send back the
    response, updating the token whenever necessary.
    """

    access_token = token.get_token()
    response = requests.delete(
        url, headers={"Authorization": "Bearer {}".format(access_token)}
    )

    return response



def check_authentication(response=None):
    """
    Check if the current credential is valid and authenticating, if not, will
    ask for the customer to rerun the command './crhc user set'
    """
    if response is None:
        access_token = token.get_token()
        url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=1"
        response = requests.get(
            url, headers={"Authorization": "Bearer {}".format(access_token)}
        )
        if response.status_code != 200:
            print(
                "Error: Failed to create C.RH.C connection: Not logged in, \
credentials aren't set, run the 'crhc login' command"
            )
            sys.exit()
        else:
            return True

    elif response.status_code != 200:
        print(
            "Error: Failed to create C.RH.C connection: Not logged in, \
credentials aren't set, run the 'crhc login' command"
        )
        sys.exit()


def inventory_list():
    """
    This def will collect the first 50 HBI entries
    """

    url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=10"
    # url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = connection_request(url)
    check_authentication(response)

    list_of_servers = []
    inventory_full_detail = {"results": "", "total": response.json()["total"]}
    inventory_full_detail["results"] = list_of_servers

    stage_list = []
    stage_dic = {"server": stage_list}

    for server in response.json()["results"]:

        try:
            stage_dic["server"] = server
        except json.decoder.JSONDecodeError:
            stage_dic["server"] = {}

        server_id = server["id"]

        url = (
            "https://console.redhat.com/api/inventory/v1/hosts/"
            + server_id
            + "/system_profile"
            + FIELDS_TO_RETRIEVE
        )
        response_system_profile = connection_request(url)

        try:
            stage_dic["system_profile"] = response_system_profile.json()[
                "results"
            ][0]["system_profile"]
        except json.decoder.JSONDecodeError:
            stage_dic["system_profile"] = {}
        except KeyError:
            stage_dic["system_profile"] = {}

        list_of_servers.append(stage_dic)
        stage_dic = {}

    return inventory_full_detail


def inventory_list_all():
    """
    This def will collect all the HBI entries
    """

    url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=1"
    response = connection_request(url)
    check_authentication(response)

    # Here we are checking the total number of objects and setting the correct
    # number of pages based on that.
    # check_response = divmod(response.json()['total'], 50)
    # ITEMS_PER_PAGE = 10
    check_response = divmod(response.json()["total"], conf.ITEMS_PER_PAGE)

    if check_response[1] == 0:
        num_of_pages = check_response[0] + 1
    else:
        num_of_pages = check_response[0] + 2

    list_of_servers = []
    inventory_full_detail = {"results": "", "total": response.json()["total"]}
    inventory_full_detail["results"] = list_of_servers

    stage_list = []
    stage_dic = {"server": stage_list}

    # For debugin purposes
    # num_of_pages = 2

    for page in range(1, num_of_pages):
        url = (
            "https://console.redhat.com/api/inventory/v1/hosts?per_page="
            + str(conf.ITEMS_PER_PAGE)
            + "&page="
            + str(page)
            + "&order_by=display_name"
        )
        response = connection_request(url)

        for server in response.json()["results"]:

            try:
                stage_dic["server"] = server
            except json.decoder.JSONDecodeError:
                stage_dic["server"] = {}

            server_id = server["id"]
            url = (
                "https://console.redhat.com/api/inventory/v1/hosts/"
                + server_id
                + "/system_profile"
                + FIELDS_TO_RETRIEVE
            )
            response_system_profile = connection_request(url)

            try:
                stage_dic["system_profile"] = response_system_profile.json()[
                    "results"
                ][0]["system_profile"]
            except json.decoder.JSONDecodeError:
                stage_dic["system_profile"] = {}
            except KeyError:
                stage_dic["system_profile"] = {}

            list_of_servers.append(stage_dic)
            stage_dic = {}

    return inventory_full_detail


def inventory_list_all_no_system_profile():
    """
    This def will collect all the HBI entries. This call will be pretty quick
    once we are not consulting the system_profile endpoint, just the host one.
    """

    url = "https://console.redhat.com/api/inventory/v1/hosts?per_page=1"
    response = connection_request(url)
    check_authentication(response)

    # Here we are checking the total number of objects and setting the correct
    # number of pages based on that.
    # check_response = divmod(response.json()['total'], 50)
    # ITEMS_PER_PAGE = 10
    check_response = divmod(response.json()["total"], conf.ITEMS_PER_PAGE)

    if check_response[1] == 0:
        num_of_pages = check_response[0] + 1
    else:
        num_of_pages = check_response[0] + 2

    list_of_servers = []
    inventory_full_detail = {"results": "", "total": response.json()["total"]}
    inventory_full_detail["results"] = list_of_servers

    stage_list = []
    stage_dic = {"server": stage_list}

    # For debugin purposes
    # num_of_pages = 2

    for page in range(1, num_of_pages):
        url = (
            "https://console.redhat.com/api/inventory/v1/hosts?per_page="
            + str(conf.ITEMS_PER_PAGE)
            + "&page="
            + str(page)
            + "&order_by=display_name"
        )
        response = connection_request(url)

        # debug
        # print("page # {}".format(page))

        for server in response.json()["results"]:

            try:
                stage_dic["server"] = server
            except json.decoder.JSONDecodeError:
                stage_dic["server"] = {}

            list_of_servers.append(stage_dic)
            stage_dic = {}

    return inventory_full_detail


def inventory_list_search_by_name(fqdn):
    """
    This def will search the HBI entries by keyword
    """

    url = (
        "https://console.redhat.com/api/inventory/v1/hosts?hostname_or_id="
        + fqdn
    )
    response = connection_request(url)
    check_authentication(response)

    list_of_servers = []
    inventory_full_detail = {"results": "", "total": response.json()["total"]}
    inventory_full_detail["results"] = list_of_servers

    stage_list = []
    stage_dic = {"server": stage_list}

    for server in response.json()["results"]:

        stage_dic["server"] = server

        server_id = server["id"]

        url = (
            "https://console.redhat.com/api/inventory/v1/hosts/"
            + server_id
            + "/system_profile"
            + FIELDS_TO_RETRIEVE
        )
        response_system_profile = connection_request(url)

        try:
            stage_dic["system_profile"] = response_system_profile.json()[
                "results"
            ][0]["system_profile"]
        except json.decoder.JSONDecodeError:
            stage_dic["system_profile"] = {}
        except KeyError:
            stage_dic["system_profile"] = {}

        list_of_servers.append(stage_dic)
        stage_dic = {}

    return inventory_full_detail


def inventory_remove_stale(num_of_days):
    """
    Def responsible to receive the # of days and check
    all the servers currently in console.redhat.com, check the last
    update and compare with the current date - num_of_days passed
    by the customer.
    """

    print("The file with the server list to be removed will be created here: {}".format(conf.STALE_FILE))
    # Getting the current date and time
    current_date = datetime.datetime.now()
    # Calculating the date to be tested and removed before that
    date_to_test_and_remove = current_date - datetime.timedelta(days=int(num_of_days))

    print("Inside remove stale, # of days: {}".format(num_of_days))
    print("Please, wait while checking the information ...")
    list_server_with_no_system_profile = inventory_list_all_no_system_profile()

    # print("ready to go")
    stage_lst = []

    for srv in list_server_with_no_system_profile['results']:
        srv_last_update = srv['server']['updated'].split("T")[0]
        # To convert from string to format type
        srv_last_update_time_format = datetime.datetime.strptime(srv_last_update, "%Y-%m-%d")
        if srv_last_update_time_format < date_to_test_and_remove:
            stage_lst.append(srv)

    report.json_stale_systems(stage_lst)

    count = len(stage_lst)
    print("We got {} entries with date equal or less than {}.".format(count, date_to_test_and_remove.strftime("%Y-%m-%d")))
    print("if you wish, you can open a second terminal and double-check the file {} with the complete list of servers that will be removed, before you proceed.".format(conf.STALE_FILE))
    opt = input("Would you like to proceed and remove then? (y|Y|n|N): ")

    if (opt == "y") or (opt == "Y"):
        # print("proceed")
        inventory_remove_entry(stage_lst)
    elif (opt == "n") or (opt == "N"):
        print("Canceling")
    else:
        print("Invalid option")

    # print("ready to go")


def inventory_remove_entry(srv_to_be_removed):
    """
    Def responsible to remove the entry from console.redhat.com
    """
    # print("we are here to remove the entries")

    if len(srv_to_be_removed) == 0:
        print("Nothing to remove")
        sys.exit()

    for srv in srv_to_be_removed:
        print("here to check")
        srv_uuid = srv['server']['id']
        last_update = srv['server']['updated']
        # srv_uuid = "1784587a-a502-4b98-97ea-634e92e882e2"
        url = ("https://console.redhat.com/api/inventory/v1/hosts/" + srv_uuid)
        print("Removing .: {}, last update at: {}".format(url, last_update))
        response = connection_request_delete(url)
        check_authentication(response)


def swatch_list():
    """
    This def will collect the first 100 entries from Subscription Watch
    """

    # ITEMS_PER_PAGE = 10

    url = (
        "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit="
        + str(conf.ITEMS_PER_PAGE)
        + "&offset=0&sort=display_name"
    )
    response = connection_request(url)
    check_authentication(response)

    return response.json()


def swatch_list_all():
    """
    This def will collect all the entries from Subscription Watch
    """

    # ITEMS_PER_PAGE = 10

    url = (
        "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit="
        + str(conf.ITEMS_PER_PAGE)
        + "&offset=0&sort=display_name"
    )
    response = connection_request(url)
    check_authentication(response)

    num_of_pages = round(
        response.json()["meta"]["count"] / conf.ITEMS_PER_PAGE + 1
    )
    # num_of_pages = round(response.json()['meta']['count'] / 100 + 1)

    dic_full_list = {
        "data": "",
        "meta": {"count": response.json()["meta"]["count"]},
    }
    full_list = []
    dup_kvm_servers = []
    server_with_no_dupes = []

    count = 0
    for page in range(0, num_of_pages):
        url = (
            "https://console.redhat.com/api/rhsm-subscriptions/v1/hosts/products/RHEL?limit="
            + str(conf.ITEMS_PER_PAGE)
            + "&offset="
            + str(count)
            + "&sort=display_name"
        )
        response = connection_request(url)
        count = count + conf.ITEMS_PER_PAGE
        # count = count + 100

        for entry in response.json()["data"]:
            full_list.append(entry)

    # The piece below is just to check/remove the duplicate entries
    # caused by kvm/libvirt hypervisors. At this moment, swatch is
    # creating 2 entries with the same facts, except for the measurement_type.
    count = 0
    for entry in full_list:

        for element in full_list:
            if (
                (entry.get("inventory_id") == element.get("inventory_id"))
                and (entry.get("insights_id") == element.get("insights_id"))
                and (
                    entry.get("subscription_manager_id")
                    == element.get("subscription_manager_id")
                )
                and (entry.get("display_name") == element.get("display_name"))
                and (entry.get("sockets") == element.get("sockets"))
                and (entry.get("cores") == element.get("cores"))
                and (
                    entry.get("hardware_type") == element.get("hardware_type")
                )
                and (
                    entry.get("measurement_type")
                    != element.get("measurement_type")
                )
                and (entry.get("last_seen") == element.get("last_seen"))
                and (
                    entry.get("is_unmapped_guest")
                    == element.get("is_unmapped_guest")
                )
                and (
                    entry.get("is_hypervisor") == element.get("is_hypervisor")
                )
            ):
                # print("EQUAL for: {}".format(entry['display_name']))
                count = count + 1

        if count == 1:
            dup_kvm_servers.append(entry)
            count = 0
        else:
            # print("# of count: {}".format(count))
            count = 0

    # Updating the measurement_type to virtual, only for the servers
    # which everything else was the same value, except for the
    # measurement_type :)
    for server in dup_kvm_servers:
        server["measurement_type"] = "VIRTUAL"

    # Removing the duplicate entries and keeping only a single entry in the
    # server_with_no_dupes list
    for each_server in dup_kvm_servers:
        if len(server_with_no_dupes) == 0:
            server_with_no_dupes.append(each_server)
        else:
            count = 0
            for server in server_with_no_dupes:
                if each_server == server:
                    count = 1

            if count == 0:
                server_with_no_dupes.append(each_server)

    # At this moment checking for the complete list and anything that
    # has duplicate uuid will not be added to the final list called
    # server_with_no_dupes
    for each_server_fl in full_list:
        count = 0
        for each_server_no_dupe in server_with_no_dupes:
            if (
                each_server_fl["inventory_id"]
                == each_server_no_dupe["inventory_id"]
            ):
                count = 1
        if count == 0:
            server_with_no_dupes.append(each_server_fl)

    dic_full_list["data"] = server_with_no_dupes

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

    for server in item_list["data"]:
        # Baremetal server
        if (
            server["hardware_type"] == "PHYSICAL"
            and server["is_hypervisor"] is False
        ):
            baremetal_count = baremetal_count + server["sockets"]
        # Hypervisor server
        if (
            server["hardware_type"] == "PHYSICAL"
            and server["is_hypervisor"] is True
        ):
            hypervisor_count = hypervisor_count + server["sockets"]
        # VM with no host guest mapping
        if (
            server["hardware_type"] == "VIRTUALIZED"
            and server["is_hypervisor"] is False
            and server["is_unmapped_guest"] is True
        ):
            vm_with_no_host_guest_mapping = (
                vm_with_no_host_guest_mapping + server["sockets"]
            )
        # Cloud server
        if server["hardware_type"] == "CLOUD":
            cloud_count = cloud_count + server["sockets"]

        total_socket_count = total_socket_count + server["sockets"]

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

    url = "https://console.redhat.com/api"
    response = connection_request(url)
    check_authentication(response)

    dic_stage = {"services": []}

    # Removing in the app since the information is still
    # around in Red Hat backend
    # https://bugzilla.redhat.com/show_bug.cgi?id=2020877
    # https://issues.redhat.com/browse/RHCLOUD-18236
    TO_REMOVE = (
        "/api/aiops-clustering",
        "/api/aiops-idle-cost-savings",
        "/api/aiops-instance-type-validation",
        "/api/aiops-outlier-detection",
        "/api/aiops-volume-type-validation",
        "/api/automation-hub",
        "/api/cloudigrade",
        "/api/custom-policies",
        "/api/drift",
        "/api/echo",
        "/api/featureflags",
        "/api/gathering",
        "/api/historical-system-profiles",
        "/api/hooks",
        "/api/idp-configs-api",
        "/api/image-builder",
        "/api/leapp-data",
        "/api/malware-detection",
        "/api/marketplace-gateway",
        "/api/module-update-router",
        "/api/pes",
        "/api/platform-feedback",
        "/api/quickstarts",
        "/api/receptor-controller",
        "/api/rhsm",
        "/api/subscriptions",
        "/api/system-baseline",
        "/api/topological-inventory",
        "/api/upload",
        "/api/webhooks",
        "/api/xavier",
    )

    # The method below should be working as expected .... however, it's not.
    # for api_to_remove in TO_REMOVE:
    #     dic_stage.json()['services'].remove(api_to_remove)
    #     dic_stage.json()['services'].remove('/api/aiops-clustering')

    for api_endpoint in response.json()["services"]:
        count = 0
        for api_to_delete in TO_REMOVE:
            if api_endpoint == api_to_delete:
                count = 1

        if count == 0:
            dic_stage["services"].append(api_endpoint)

    return dic_stage


def get_command(api_url):
    """
    This def will call the API endpoint directly
    """

    # Testing if the customer is passing the full endpoint path or just the
    # initial endpoint url. When passing the short one, the script will test
    # and will show all the full url available.
    if len(api_url.split("/")) < 4:

        # retrieving the openapi json file
        url = "https://console.redhat.com/" + api_url + "/v1/openapi.json"
        response = connection_request(url)
        check_authentication(response)

        available_paths = response.json()["paths"].keys()

        # Testing "/api/patch" endoint, once this is the single one
        # causing problems with the paths (complete path and short path)
        if api_url == "/api/patch":
            for path in available_paths:
                print("{}".format(path))
        else:
            for path in available_paths:
                print("{}/v1{}".format(api_url, path))

    else:
        # retrieving the full url
        url = "https://console.redhat.com/" + api_url
        response = connection_request(url)
        check_authentication(response)

        return response.json()


def whoami():
    """
    Used to retrieve the current user information via API
    """

    url = "https://api.openshift.com/api/accounts_mgmt/v1/current_account"
    response = connection_request(url)
    check_authentication(response)

    return response.json()


def update_check():
    """
    Checking if there is any new available version on GitHub, if yes, it will
    let the user aware to download it.
    """

    home_dir = os.path.expanduser("~")

    # In case the file be not around yet.
    answer = ""

    if os.path.exists(home_dir + "/.crhc.version"):
        file_age = time.time() - (
            os.stat(home_dir + "/.crhc.version").st_mtime
        )
        # print(int(file_age))

        # If the file is older than `conf.TIME_TO_CHECK_THE_NEW_VERSION`,
        # then it will be updated.
        if int(file_age) < conf.TIME_TO_CHECK_THE_NEW_VERSION:
            file_ref = open(home_dir + "/.crhc.version")
            available_version = file_ref.read()

            if int(available_version.replace(".", "")) > int(
                conf.CURRENT_VERSION.replace(".", "")
            ):
                answer = "Please, download the latests version from \
https://github.com/C-RH-C/crhc-cli/releases/latest\n\
Current Version: {}\nNew Version: {}".format(
                    conf.CURRENT_VERSION, available_version
                )
            else:
                answer = ""
        else:
            os.remove(home_dir + "/.crhc.version")

    else:
        url = "https://github.com/C-RH-C/crhc-cli/releases/latest"
        response = connection_request(url)
        available_version = response.url.split("/")[7]

        file_obj = open(home_dir + "/.crhc.version", "w")
        file_obj.write(available_version)

        if int(available_version.replace(".", "")) > int(
            conf.CURRENT_VERSION.replace(".", "")
        ):
            answer = "Please, download the latests version from https://github.com/C-RH-C/crhc-cli/releases/latest\n\
Current Version: {}\nNew Version: {}".format(
                conf.CURRENT_VERSION, available_version
            )
        else:
            answer = ""

    return answer


def patch_systems():
    """
    This def will collect all the entries from patch systems
    """

    url = "https://console.redhat.com/api/patch/v1/systems"
    response = connection_request(url)
    check_authentication(response)

    # ITEMS_PER_PAGE = 10

    num_of_pages = int(
        response.json()["meta"]["total_items"] / conf.ITEMS_PER_PAGE + 1
    )
    # num_of_pages = int(response.json()['meta']['total_items'] / 20 + 1)

    dic_full_list = {
        "data": "",
        "total": response.json()["meta"]["total_items"],
    }
    full_list = []

    count = 0
    for page in range(0, num_of_pages):
        url = (
            "https://console.redhat.com/api/patch/v1/systems?limit="
            + str(conf.ITEMS_PER_PAGE)
            + "&offset="
            + str(count)
            + "&sort=-last_upload"
        )
        count = count + conf.ITEMS_PER_PAGE
        response = connection_request(url)

        for entry in response.json()["data"]:
            full_list.append(entry)

    dic_full_list["data"] = full_list
    return dic_full_list


def vulnerability_systems():
    """
    This def will collect all the entries from vulnerability systems
    """

    url = "https://console.redhat.com/api/vulnerability/v1/systems"
    response = connection_request(url)
    check_authentication(response)

    # ITEMS_PER_PAGE = 10

    # Here we are checking the total number of objects and setting the correct
    # number of pages based on that.
    check_response = divmod(
        response.json()["meta"]["total_items"], conf.ITEMS_PER_PAGE
    )
    # check_response = divmod(response.json()['meta']['total_items'], 20)

    if check_response[1] == 0:
        num_of_pages = check_response[0]
    else:
        num_of_pages = check_response[0] + 1

    dic_full_list = {
        "data": "",
        "total": response.json()["meta"]["total_items"],
    }
    full_list = []

    count = 0
    for page in range(0, num_of_pages):
        url = (
            "https://console.redhat.com/api/vulnerability/v1/systems?limit="
            + str(conf.ITEMS_PER_PAGE)
            + "&offset="
            + str(count)
            + "&sort=-last_upload"
        )
        count = count + conf.ITEMS_PER_PAGE
        response = connection_request(url)

        for entry in response.json()["data"]:
            full_list.append(entry)

    dic_full_list["data"] = full_list
    return dic_full_list


def advisor_systems():
    """
    This def will collect all the entries from advisor/insights systems
    """

    # ITEMS_PER_PAGE = 10

    url = "https://console.redhat.com/api/insights/v1/system"
    response = connection_request(url)
    check_authentication(response)

    num_of_pages = int(
        response.json()["meta"]["count"] / conf.ITEMS_PER_PAGE + 1
    )

    dic_full_list = {"data": "", "total": response.json()["meta"]["count"]}
    full_list = []

    count = 0
    for page in range(0, num_of_pages):
        url = (
            "https://console.redhat.com/api/insights/v1/system?limit="
            + str(conf.ITEMS_PER_PAGE)
            + "&offset="
            + str(count)
        )
        count = count + conf.ITEMS_PER_PAGE
        response = connection_request(url)

        for entry in response.json()["data"]:
            full_list.append(entry)

    dic_full_list["data"] = full_list
    return dic_full_list
