"""
Module responsible for troublheshooting
"""

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
