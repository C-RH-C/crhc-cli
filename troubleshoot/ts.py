"""
Module responsible for troublheshooting
"""

import csv
import json
import os
from execution import execution
from report import report

INV_FILE = "/tmp/inventory.json"
SW_FILE = "/tmp/swatch.json"
MATCH_FILE = "/tmp/match_inv_sw.csv"


def dump_inv_json():
    """
    Function to dump only Inventory information
    """
    print("dumping the inventory information to '{}', this can take some time to finish".format(INV_FILE))
    inventory = execution.inventory_list_all()
    # inventory = execution.inventory_list()

    file_obj = open(INV_FILE, "w")
    file_obj.write(json.dumps(inventory, indent=4))


def dump_sw_json():
    """
    Function to dump only Swatch information
    """

    print("dumping the subscription information to '{}'".format(SW_FILE))
    swatch = execution.swatch_list_all()

    file_obj = open(SW_FILE, "w")
    file_obj.write(json.dumps(swatch, indent=4))


def compress_json_files():
    """
    Function to compress the JSON files
    """
    TAR_COMMAND = "tar cpfz /tmp/crhc_data.tgz /tmp/inventory.json /tmp/swatch.json 2>/dev/null"
    TGZ_FILE = "/tmp/crhc_data.tgz"

    if os.path.isfile(INV_FILE) and os.path.isfile(SW_FILE):
        os.system(TAR_COMMAND)

        if os.path.isfile(TGZ_FILE):
            print("File {} created.".format(TGZ_FILE))
    else:
        print("The file {} or {} is missing.".format(INV_FILE, SW_FILE))


def match_hbi_sw():
    """
    Function to cross both HBI and Swatch files and generate a single
    dataset that will be used for troubleshooting purposes.
    """

    final_lst = []
    stage_lst = []

    try:
        file_obj = open(INV_FILE, "r")
        inventory = json.load(file_obj)
        print("File {} already in place, using it.".format(INV_FILE))
    except FileNotFoundError:
        dump_inv_json()
        file_obj = open(INV_FILE, "r")
        inventory = json.load(file_obj)

    try:
        file_obj = open(SW_FILE, "r")
        swatch = json.load(file_obj)
        print("File {} already in place, using it.".format(SW_FILE))
    except FileNotFoundError:
        dump_sw_json()
        file_obj = open(SW_FILE, "r")
        swatch = json.load(file_obj)

    for inv_element in inventory['results']:
        count = 0
        for sw_element in swatch['data']:
            if inv_element['server']['id'] == sw_element['inventory_id']:
                # print("found it")
                # print("{},{}".format(inv_element,sw_element))
                stage_lst.append(inv_element)
                stage_lst.append(sw_element)
                final_lst.append(stage_lst)
                stage_lst = []
                count = count + 1
        if count == 0:
            stage_lst.append(inv_element)
            stage_lst.append("not in swatch")
            final_lst.append(stage_lst)
            stage_lst = []

    report.csv_match_report(final_lst)
    issue_summary_report(final_lst)


def clean():
    """
    Function to cleanup all the local cache/temporary files
    """

    if os.path.exists(INV_FILE):
        print("removing the file {}".format(INV_FILE))
        os.remove(INV_FILE)

    if os.path.exists(SW_FILE):
        print("removing the file {}".format(SW_FILE))
        os.remove(SW_FILE)

    if os.path.exists(MATCH_FILE):
        print("removing the file {}".format(MATCH_FILE))
        os.remove(MATCH_FILE)


def organize_list_by_column(list_obj, col):
    """
    Responsible for organize the list according to the column.
    """
    return sorted(list_obj, key=lambda x: x[col])


def issue_summary_report(final_lst):
    """
    Function to check everything that is wrong or not expected in
    Inventory and Subscriptions.
    """

    wrong_socket_inventory = []
    wrong_socket_subscription = []
    duplicate_fqdn = []
    duplicate_display_name = []
    different_fqdn_display_name = []
    server_with_no_socket_key = []
    installed_product_with_no_package_sat = []
    installed_product_with_no_package_cap = []
    installed_product_with_no_package_ocp = []

    for obj in final_lst:
        # Checking for 0 sockets in Inventory
        stage_lst = []
        try:
            if obj[0]['system_profile']['number_of_sockets'] == 0:
                wrong_socket_inventory.append(obj)
        except KeyError:
            # print("Machine {} sem socket key".format(obj[0]['server']['fqdn']))
            stage_lst.append(obj[0]['server']['id'])
            stage_lst.append(obj[0]['server']['fqdn'])
            stage_lst.append(obj[0]['server']['display_name'])
            stage_lst.append(obj[0]['server']['created'])
            stage_lst.append(obj[0]['server']['updated'])

            server_with_no_socket_key.append(stage_lst)
        # Checking for 0 sockets in Subscription
        try:
            if obj[1]['sockets'] == 0:
                wrong_socket_subscription.append(obj)
        except TypeError as e:
            # print(e)
            ...

        # Checking for duplicate FQDN
        fqdn = obj[0]['server']['fqdn']
        count = 0
        stage_lst = []
        for item in final_lst:
            if item[0]['server']['fqdn'] == fqdn:
                stage_lst.append(obj[0]['server']['id'])
                if obj[0]['server']['fqdn'] is None:
                    stage_lst.append("None")
                else:
                    stage_lst.append(obj[0]['server']['fqdn'])
                stage_lst.append(obj[0]['server']['display_name'])
                stage_lst.append(obj[0]['server']['created'])
                stage_lst.append(obj[0]['server']['updated'])
                count = count + 1
        
        if count > 1:
            duplicate_fqdn.append(stage_lst)

        
        # Checking for duplicate display_name
        display_name = obj[0]['server']['display_name']
        count = 0
        stage_lst = []
        for item in final_lst:
            if item[0]['server']['display_name'] == display_name:
                stage_lst.append(obj[0]['server']['id'])
                stage_lst.append(obj[0]['server']['fqdn'])
                if obj[0]['server']['display_name'] is None:
                    stage_lst.append("None")
                else:
                    stage_lst.append(obj[0]['server']['display_name'])
                stage_lst.append(obj[0]['server']['created'])
                stage_lst.append(obj[0]['server']['updated'])
                count = count + 1
        
        if count > 1:
            duplicate_display_name.append(stage_lst)



        # Checking for same server with different display_name and FQDN
        stage_lst = []

        fqdn = obj[0]['server']['fqdn']
        display_name = obj[0]['server']['display_name']
        if fqdn != display_name:
            stage_lst.append(obj[0]['server']['id'])
            stage_lst.append(fqdn)
            stage_lst.append(display_name)
            stage_lst.append(obj[0]['server']['created'])
            stage_lst.append(obj[0]['server']['updated'])
            

            different_fqdn_display_name.append(stage_lst)


        # Checking if the 250, 269 or 209 pem file is present
        stage_lst = []

        # Checking for the installed_products
        installed_products_response = report.check_for_installed_products(obj[0])

        # Checking for satellite packages
        installed_package_satellite_response = report.check_for_satellite_package(obj[0])

        # Checking for openshift packages
        installed_package_openshift_response = report.check_for_openshift_package(obj[0])

        if "250" in installed_products_response and installed_package_satellite_response != "TRUE":
            stage_lst.append(obj[0]['server']['id'])
            stage_lst.append(obj[0]['server']['fqdn'])
            stage_lst.append(obj[0]['server']['display_name'])
            stage_lst.append(installed_products_response)
            stage_lst.append(installed_package_satellite_response)

            installed_product_with_no_package_sat.append(stage_lst)

        if "269" in installed_products_response and installed_package_satellite_response != "TRUE":
            stage_lst.append(obj[0]['server']['id'])
            stage_lst.append(obj[0]['server']['fqdn'])
            stage_lst.append(obj[0]['server']['display_name'])
            stage_lst.append(installed_products_response)
            stage_lst.append(installed_package_satellite_response)

            installed_product_with_no_package_cap.append(stage_lst)

        if ("290" in installed_products_response) and (installed_package_openshift_response != "TRUE"):
            stage_lst.append(obj[0]['server']['id'])
            stage_lst.append(obj[0]['server']['fqdn'])
            stage_lst.append(obj[0]['server']['display_name'])
            stage_lst.append(installed_products_response)
            stage_lst.append(installed_package_openshift_response)

            installed_product_with_no_package_ocp.append(stage_lst)


    # Passing the list and also the column that will be used to order (column #1 is the FQDN one)
    organized_duplicate_fqdn = organize_list_by_column(duplicate_fqdn, 1)

    # Passing the list and also the column that will be used to order (column #2 is the Display Name one)
    organized_duplicate_display_name = organize_list_by_column(duplicate_display_name, 2)

    report.txt_issue_report(wrong_socket_inventory,
                            wrong_socket_subscription,
                            organized_duplicate_fqdn,
                            organized_duplicate_display_name,
                            different_fqdn_display_name,
                            server_with_no_socket_key,
                            installed_product_with_no_package_sat,
                            installed_product_with_no_package_cap,
                            installed_product_with_no_package_ocp)
