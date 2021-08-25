"""
Module responsible for the main menu
"""

import sys
import json
from execution import execution
from credential import credential


def inventory_sub_menu():
    """
    The inventory sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  list - List the inventory entries, first 50")
        print("  list_all - List all the inventory entries")
        print("  --display_name - Please, type the FQDN or Partial Hostname")

    try:
        if (sys.argv[1] == "inventory") and (sys.argv[2] == "list"):
            execution.inventory_list()
            sys.exit()
    except IndexError:
        ...

    try:
        if (sys.argv[1] == "inventory") and (sys.argv[2] == "list_all"):
            execution.inventory_list_all()
            sys.exit()
    except IndexError:
        ...

    try:
        if (sys.argv[1] == "inventory") and (sys.argv[2] == "--display_name"):

            if len(sys.argv) == 3:
                print("Please, pass the FQDN or Partial FQDN to --display_name, for example '--display_name virt-who-esxi'")
                sys.exit()
            fqdn = sys.argv[3]
            execution.inventory_list_search_by_name(fqdn)
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

    try:
        if (sys.argv[1] == "swatch") and (sys.argv[2] == "list"):
            # print("executing inventory list")
            response = execution.swatch_list()
            print(json.dumps(response, indent=4))

            sys.exit()
    except IndexError:
        ...

    try:
        if (sys.argv[1] == "swatch") and (sys.argv[2] == "list_all"):
            # print("executing inventory list")
            response = execution.swatch_list_all()
            print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError:
        ...

    try:
        if (sys.argv[1] == "swatch") and (sys.argv[2] == "socket_summary"):
            # print("executing inventory list")
            execution.swatch_socket_summary()
            sys.exit()
    except IndexError:
        ...


def user_sub_menu():
    """
    The User sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        print("  set - Set the Username and Password. AT THIS MOMENT THE PASSWORD WILL BE STORED CLEAR TEXT!")

    try:
        if (sys.argv[1] == "user") and (sys.argv[2] == "set"):
            # print("executing inventory list")
            credential.set_credential()
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

        elif sys.argv[1] == "user":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    print("user help here")
                    sys.exit()
            except IndexError:
                ...

            # print("swatch")
            user_sub_menu()

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
        print("  user")
        print("")
        print("Flags:")
        print("  -h, --help                         help for crhc")
        print("")
        print("Use \"crhc [command] --help\" for more information about a command.")
