"""
.. code-block:: text

    Module responsible for the main menu
"""

import sys
import json
from crhc_cli.conf import conf
from crhc_cli.execution import execution
from crhc_cli.report import report
from crhc_cli.credential import token
from crhc_cli.troubleshoot import ts
from crhc_cli.help import help_opt

access_token = token.get_token()


def inventory_sub_menu():
    """
    The inventory sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only inventory, the help menu will be presented.
        help_opt.help_inventory_menu()

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list"):
                # execution.inventory_list()
                response = execution.inventory_list()
                # print(response)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list_all"):
                # print("This process can spend some minutes according to the
                # number of servers in your account.")
                response = execution.inventory_list_all()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (
                sys.argv[2] == "display_name"
            ):

                if len(sys.argv) == 3:
                    print(
                        "Please, pass the FQDN or Partial FQDN to display_name, \
for example 'crhc inventory display_name virt-who-esxi'"
                    )
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "list_stale"):
                response = execution.inventory_list_stale()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


        # To print in JSON format
        try:
            if (sys.argv[1] == "inventory") and (sys.argv[2] == "remove_stale"):
                response = execution.inventory_remove_stale()
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    # To print in JSON format
    if len(sys.argv) == 4 and (sys.argv[2]) == "display_name":
        try:
            if (sys.argv[1] == "inventory") and (
                sys.argv[2] == "display_name"
            ):

                if len(sys.argv) == 3:
                    print(
                        "Please, pass the FQDN or Partial FQDN to display_name, \
for example 'crhc inventory display_name virt-who-esxi'"
                    )
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    # To print in CSV format
    if (
        len(sys.argv) == 5
        and (sys.argv[2]) == "display_name"
        and (sys.argv[4]) == "--csv"
    ):
        try:
            if (sys.argv[1] == "inventory") and (
                sys.argv[2] == "display_name"
            ):

                if len(sys.argv) == 3:
                    print(
                        "Please, pass the FQDN or Partial FQDN to display_name, \
for example 'crhc inventory display_name virt-who-esxi'"
                    )
                    sys.exit()
                fqdn = sys.argv[3]
                response = execution.inventory_list_search_by_name(fqdn)
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    if len(sys.argv) == 4 and (sys.argv[3]) == "--help":
        print("  --csv - List the inventory entries in CSV format")

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "inventory")
                and (sys.argv[2] == "list")
                and (sys.argv[3] == "--csv")
            ):
                # execution.inventory_list()
                response = execution.inventory_list()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "inventory")
                and (sys.argv[2] == "list_all")
                and (sys.argv[3] == "--csv")
            ):
                # Checking if the connection still alive before
                # printing sometihng
                if execution.check_authentication():
                    print(
                        "This process can spend some minutes according to \
the number of servers in your account."
                    )
                response = execution.inventory_list_all()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "inventory")
                and (sys.argv[2] == "display_name")
                and (sys.argv[4] == "--csv")
            ):
                # execution.inventory_list()
                response = execution.inventory_list_search_by_name()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "inventory")
                and (sys.argv[2] == "list_stale")
                and (sys.argv[3] == "--csv")
            ):
                # Checking if the connection still alive before
                # printing sometihng
                if execution.check_authentication():
                    print(
                        "This process can spend some minutes according to \
the number of servers in your account."
                    )
                response = execution.inventory_list_stale()
                report.csv_report_inventory(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


def swatch_sub_menu():
    """
    The Subscription Watch sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only swatch, the help menu will be presented.
        help_opt.help_swatch_menu()

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list"):
                response = execution.swatch_list()
                print(json.dumps(response, indent=4))

                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "list_all"):
                response = execution.swatch_list_all()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in JSON format
        try:
            if (sys.argv[1] == "swatch") and (sys.argv[2] == "socket_summary"):
                execution.swatch_socket_summary()
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    if len(sys.argv) == 4 and (sys.argv[3]) == "--help":
        print("  --csv - List the swatch entries in CSV format")

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "swatch")
                and (sys.argv[2] == "list")
                and (sys.argv[3] == "--csv")
            ):
                response = execution.swatch_list()
                report.csv_report_swatch(response)

                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "swatch")
                and (sys.argv[2] == "list_all")
                and (sys.argv[3] == "--csv")
            ):
                response = execution.swatch_list_all()
                report.csv_report_swatch(response)
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


def endpoint_sub_menu():
    """
    The endpoint sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only endpoint, the help menu will be presented.
        help_opt.help_endpoint_menu()

    try:
        if (sys.argv[1] == "endpoint") and (sys.argv[2] == "list"):
            response = execution.endpoint_list()
            print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def patch_sub_menu():
    """
    The patch sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only swatch, the help menu will be presented.
        help_opt.help_patch_menu()

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "patch") and (sys.argv[2] == "systems"):
                response = execution.patch_systems()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    if len(sys.argv) == 4 and (
        (sys.argv[3]) == "--help" or (sys.argv[3]) == "-h"
    ):
        help_opt.help_patch_menu()

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "patch")
                and (sys.argv[2] == "systems")
                and (sys.argv[3] == "--csv")
            ):
                response = execution.patch_systems()
                report.csv_report_patch(response)

                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


def vulnerability_sub_menu():
    """
    The vulnerability sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only swatch, the help menu will be presented.
        help_opt.help_vulnerability_menu()

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "vulnerability") and (sys.argv[2] == "systems"):
                response = execution.vulnerability_systems()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    if len(sys.argv) == 4 and (
        (sys.argv[3]) == "--help" or (sys.argv[3]) == "-h"
    ):
        help_opt.help_vulnerability_menu()

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "vulnerability")
                and (sys.argv[2] == "systems")
                and (sys.argv[3] == "--csv")
            ):
                response = execution.vulnerability_systems()
                report.csv_report_vulnerability(response)

                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


def advisor_sub_menu():
    """
    The advisor/insights sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only swatch, the help menu will be presented.
        help_opt.help_advisor_menu()

    if len(sys.argv) == 3:

        # To print in JSON format
        try:
            if (sys.argv[1] == "advisor") and (sys.argv[2] == "systems"):
                response = execution.advisor_systems()
                print(json.dumps(response, indent=4))
                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...

    if len(sys.argv) == 4 and (
        (sys.argv[3]) == "--help" or (sys.argv[3]) == "-h"
    ):
        help_opt.help_advisor_menu()

    if len(sys.argv) == 4:

        # To print in CSV format
        try:
            if (
                (sys.argv[1] == "advisor")
                and (sys.argv[2] == "systems")
                and (sys.argv[3] == "--csv")
            ):
                response = execution.advisor_systems()
                report.csv_report_advisor(response)

                sys.exit()
        except IndexError as e:
            # print("Error: {}".format(e))
            ...


def get_sub_menu():
    """
    The get sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only the get, the help menu will be presented.
        help_opt.help_get_menu()

    try:
        if (sys.argv[1] == "get") and (sys.argv[2]):
            response = execution.get_command(sys.argv[2])
            if response:
                print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def login_sub_menu():
    """
    Function responsible for pass the token and create the
    necessary configuration file that will be used from this point.
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only login, the help menu will be presented.
        help_opt.help_login_menu()

    try:
        if (sys.argv[1] == "login") and (sys.argv[2] == "--token"):
            secret = sys.argv[3]
            token.set_token(secret)
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def logout_sub_menu():
    """
    Function responsile for remove all the content from the .conf file.
    This will remove all the current information available in the local
    machine.
    """
    try:
        if sys.argv[1] == "logout":
            token.delete_token()
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def token_sub_menu():
    """
    Here you can see the full access_key and use it in order to access
    the API endpoint, for example
    """
    try:
        if sys.argv[1] == "token":
            print(token.get_token())
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
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
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def ansible_sub_menu():

    if len(sys.argv) == 2:
        # Passing only ansible, the help menu will be presented.
        help_opt.help_ansible_menu()

    """
    Retrieving the ansible managed host information from c.rh.c API endpoint
    """
    try:
        if (sys.argv[1] == "ansible") and (sys.argv[2] == "unique_hosts"):
            response = execution.get_ansible_unique_hosts()
            print(json.dumps(response, indent=4))
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def troubleshoot_sub_menu():
    """
    The troubleshooting sub menu
    """

    # To present the available options
    if len(sys.argv) == 2:
        # Passing only ts, the help menu will be presented.
        help_opt.help_ts_menu()

    try:
        if (sys.argv[1] == "ts") and (sys.argv[2] == "dump"):
            ts.dump_inv_json(False)
            ts.dump_sw_json(False)
            ts.dump_patch_json()
            ts.dump_vulnerability_json()
            ts.dump_advisor_json()
            ts.compress_json_files()
            sys.exit()
    except IndexError as e:
        # print("Error1: {}".format(e))
        ...

    try:
        if (sys.argv[1] == "ts") and (sys.argv[2] == "dump_current"):
            ts.dump_inv_json(True)
            ts.dump_sw_json(True)
            ts.dump_patch_json()
            ts.dump_vulnerability_json()
            ts.dump_advisor_json()
            ts.compress_json_files()
            sys.exit()
    except IndexError as e:
        # print("Error1: {}".format(e))
        ...

    try:
        if (sys.argv[1] == "ts") and (sys.argv[2] == "match"):
            ts.match_hbi_sw()
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...

    try:
        if (sys.argv[1] == "ts") and (sys.argv[2] == "clean"):
            ts.clean()
            sys.exit()
    except IndexError as e:
        # print("Error: {}".format(e))
        ...


def update_check():
    """
    Function to check the app version according to the latest available version
    in GitHub
    """
    return execution.update_check()


def troubleshoot():
    """
    Function to call the troubleshoot submenu
    """
    troubleshoot_sub_menu()


def main_menu():
    """
    The Main menu
    """

    if len(sys.argv) > 1:
        if sys.argv[1] == "inventory":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_inventory_menu()
                    sys.exit()
            except IndexError:
                ...

            # print("inventory")
            inventory_sub_menu()

        elif sys.argv[1] == "swatch":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_swatch_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            swatch_sub_menu()

        elif sys.argv[1] == "endpoint":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_endpoint_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            endpoint_sub_menu()

        elif sys.argv[1] == "patch":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_patch_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            patch_sub_menu()

        elif sys.argv[1] == "vulnerability":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_vulnerability_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            vulnerability_sub_menu()

        elif sys.argv[1] == "advisor":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_advisor_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            advisor_sub_menu()

        elif sys.argv[1] == "get":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_get_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            get_sub_menu()

        elif sys.argv[1] == "login":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_login_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            login_sub_menu()

        elif sys.argv[1] == "logout":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_logout_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            logout_sub_menu()

        elif sys.argv[1] == "token":
            token_sub_menu()

        elif sys.argv[1] == "whoami":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_whoami_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            whoami_sub_menu()

        elif sys.argv[1] == "ansible":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_ansible_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...

            # print("swatch")
            ansible_sub_menu()

        elif (sys.argv[1] == "--help") or (sys.argv[1] == "-h"):
            help_opt.help_main_menu()

        elif (sys.argv[1] == "--version") or (sys.argv[1] == "-v"):
            print(conf.CURRENT_VERSION)

        elif sys.argv[1] == "ts":
            try:
                if (sys.argv[2] == "--help") or (sys.argv[2] == "-h"):
                    help_opt.help_ts_menu()
                    sys.exit()
            except IndexError as e:
                # print("Error: {}".format(e))
                ...
            troubleshoot()

        else:
            print("invalid option")
    else:
        print("Command line tool for console.redhat.com API")
        print("")
        print("Usage:")
        print("  crhc [command]")
        print("")
        print("Available Commands:")
        print("  inventory      Retrieve Inventory information")
        print("  swatch         Retrieve Subscriptions information")
        print("  advisor        Retrieve Insights Information")
        print("  patch          Retrieve Patch Information")
        print("  vulnerability  Retrieve Vulnerability Information")
        print("  ansible        Retrieve Ansible Managed Host Information")
        print("  endpoint       List all the available endpoints")
        print("  get            Send a GET request")
        print("  ts             Troubleshooting tasks")
        print("")
        print("  login          Log in")
        print("  logout         Log out")
        print("  token          Generates a token")
        print("  whoami         Prints user information")
        print("")
        print("Flags:")
        print("  -h, --help                         help for crhc")
        print("  -v, --version                      crhc version")
        print("")
        print(
            'Use "crhc [command] --help" for more information about a command.'
        )
        print("")
        print("{}".format(update_check()))
