"""
Module responsible for the main menu
"""

import csv
import sys
import json
from execution import execution
from report import report
from credential import token
access_token = token.get_token()


def inventory_sub_menu():
    """
    The inventory sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  list - List the inventory entries, first 50")
        print("  list_all - List all the inventory entries")
        print("  --display_name - Please, type the FQDN or Partial Hostname")

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list"):
                # execution.inventory_list()
                response = execution.inventory_list()
                # print(response)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list_all"):
                print("This process can spend some minutes according to the number of servers in your account.")
                response = execution.inventory_list_all()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "--display_name"):

                if len(sys.argv) == 3:
                    print("Please, pass the FQDN or Partial FQDN to --display_name, for example '--display_name virt-who-esxi'")
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...

    # To print in JSON format
    if len(sys.argv) == 4 and (sys.argv[2]) == "--display_name":
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "--display_name"):

                if len(sys.argv) == 3:
                    print("Please, pass the FQDN or Partial FQDN to --display_name, for example '--display_name virt-who-esxi'")
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...

    # To print in CSV format
    if len(sys.argv) == 5 and (sys.argv[2]) == "--display_name" and (sys.argv[4]) == "--csv":
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "--display_name"):

                if len(sys.argv) == 3:
                    print("Please, pass the FQDN or Partial FQDN to --display_name, for example '--display_name virt-who-esxi'")
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                report.csv_report_inventory(response)
                # print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...


    if len(sys.argv) == 4 and (sys.argv[3]) == "--help":
        print("  --csv - List the inventory entries in CSV format")


    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list") and (sys.argv[3] == "--csv"):
                # execution.inventory_list()
                response = execution.inventory_list()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError:
            ...

        # To print in CSV format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list_all") and (sys.argv[3] == "--csv"):
                # execution.inventory_list()
                print("This process can spend some minutes according to the number of servers in your account.")
                response = execution.inventory_list_all()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError:
            ...

        # To print in CSV format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "--display_name") and (sys.argv[4] == "--csv"):
                # execution.inventory_list()
                response = execution.inventory_list_search_by_name()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError:
            ...



def swatch_sub_menu():
    """
    The Subscription Watch sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  list - List the swatch entries, first 100")
        print("  list_all - List all the swatch entries")
        print("  socket_summary - List all the swatch entries")

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list"):
                response = execution.swatch_list()
                print(json.dumps(response, indent=4))

                sys.exit()
        except IndexError:
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list_all"):
                response = execution.swatch_list_all()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "socket_summary"):
                execution.swatch_socket_summary()
                sys.exit()
        except IndexError:
            ...


    if len(sys.argv) == 4 and (sys.argv[3]) == "--help":
        print("  --csv - List the swatch entries in CSV format")

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list") and (sys.argv[3] == "--csv"):
                response = execution.swatch_list()
                report.csv_report_swatch(response)
                # print(json.dumps(response, indent=4))

                sys.exit()
        except IndexError:
            ...

        # To print in CSV format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list_all") and (sys.argv[3] == "--csv"):
                response = execution.swatch_list_all()
                report.csv_report_swatch(response)
                # print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError:
            ...


def endpoint_sub_menu():
    """
    The endpoint sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  list - List all the endpoints available")

    try:
        if (sys.argv[1] == "endpoint") and (sys.argv[2] == "list"):
            # print("executing inventory list")
            response = execution.endpoint_list()
            print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError:
        ...


def get_sub_menu():
    """
    The get sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  get <endpoint API URL HERE> - It will retrieve all the available methods")

    try:
        if (sys.argv[1] == "get") and (sys.argv[2]):
            # print("executing inventory list")
            # response = execution.get_command(sys.argv[2])
            response = execution.get_command(sys.argv[2])
            if response:
                print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError:
        ...


def login_sub_menu():
    """
    Function responsible for pass the token and create the necessary configuration file
    that will be used from this point.
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  In order to log in it is mandatory to use '--token'")
        print("  You can obtain a token at: https://console.redhat.com/openshift/token .")

    try:
        if (sys.argv[1] == "login") and (sys.argv[2] == "--token"):
            secret = sys.argv[3]
            token.set_token(secret)
            sys.exit()
    except IndexError:
        ...


def logout_sub_menu():
    """
    Function responsile for remove all the content from the .conf file. This will remove all the
    current information available in the local machine.
    """
    try:
        if sys.argv[1] == "logout":
            token.delete_token()
            sys.exit()
    except IndexError:
        ...


def token_sub_menu():
    """
    Here you can see the full access_key and use it in order to access the API 
    endpoint, for example
    """
    try:
        if sys.argv[1] == "token":
            print(token.get_token())
            sys.exit()
    except IndexError:
        ...


def whoami_sub_menu():
    """
    Retrieving the user information from c.rh.c API endpoint
    """
    try:
        if sys.argv[1] == "whoami":
            response = execution.whoami()
            if response:
                print(json.dumps(response, indent=4))

            sys.exit()
    except IndexError:
        ...

def update_check():

    return execution.update_check()


def main_menu():
    """
    The Main menu
    """

    if len(sys.argv) > 1:
        if sys.argv[1] == "inventory":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("inventory help here")
                    sys.exit()
            except IndexError:
                ...

            # print("inventory")
            inventory_sub_menu()

        elif sys.argv[1] == "swatch":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("swatch help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            swatch_sub_menu()

        elif sys.argv[1] == "endpoint":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("endpoint help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            endpoint_sub_menu()

        elif sys.argv[1] == "get":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("get help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            get_sub_menu()

        elif sys.argv[1] == "login":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("user help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            login_sub_menu()

        elif sys.argv[1] == "logout":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("user help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            logout_sub_menu()

        elif sys.argv[1] == "token":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("user help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            token_sub_menu()

        elif sys.argv[1] == "whoami":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("user help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            whoami_sub_menu()

        elif (sys.argv[1] == "--help") or (sys.argv[1] == "-h"):
            print("This help!")
            # main_menu()

        else:
            print("invalid option")
    else:
        print("Command line tool for console.redhat.com API")
        print("")
        print("Usage:")
        print("  crhc [command]")
        print("")
        print("Available Commands:")
        print("  inventory")
        print("  swatch")
        print("  endpoint")
        print("  get")
        print("")
        print("  login")
        print("  logout")
        print("  token")
        print("  whoami")
        print("")
        print("Flags:")
        print("  -h, --help                         help for crhc")
        print("")
        print("Use \"crhc [command] --help\" for more information about a command.")
        print("")
        print("{}".format(update_check()))
