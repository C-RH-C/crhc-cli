"""
.. code-block:: text

    Module responsible for all the helps on crhc-cli app
"""


def help_main_menu():
    """
    Main help menu
    """
    content = "\
CRHC Command Line Tool\n\
    \n\
Usage: \n\
    crhc [command]\n\
    \n\
Available Commands:\n\
    inventory       To list the Inventory data.\n\
    swatch          To list the Subscription data.\n\
    endpoint        To list all the available API endpoints on `console.redhat.com`\n\
    get             To consume the API endpoint directly.\n\
    login           To authenticate using your offline token.\n\
    logout          To cleanup the local conf file, removing all the token information.\n\
    token           To print the access_token. This can be used with `curl`, for example.\n\
    whoami          To show some information regarding to the user who requested the token.\n\
    ts              To execute some advanced options / Troubleshooting.\n\
    \n\
Flags: \n\
    --version, -v   This option will present the app version.\n\
    --help, -h      This option will present the help.\n\
"

    print(content)
    return content


def help_inventory_menu():
    """
    Main inventory menu
    """
    content = "\
Usage: \n\
    crhc inventory [command]\n\
    \n\
Available Commands:\n\
    list            List the inventory entries, first 50\n\
    list_all        List all the inventory entries\n\
    display_name    Please, type the FQDN or Partial Hostname\n\
    remove_stale    Remove all the stale entries based on the # of days\n\
    \n\
Flags: \n\
    --csv           This will generate the output in CSV format. By default, it will be JSON.\
"
    print(content)
    return content


def help_swatch_menu():
    """
    Main subscription menu
    """
    content = "\
Usage: \n\
    crhc swatch [command]\n\
    \n\
Available Commands:\n\
    list            List the swatch entries, first 100\n\
    list_all        List all the swatch entries\n\
    socket_summary  Print the socket summary\n\
    \n\
Flags: \n\
    --csv           This will generate the output in CSV format. By default, it will be JSON.\
"
    print(content)
    return content


def help_endpoint_menu():
    """
    Main endpoint menu
    """
    content = "\
Usage: \n\
    crhc endpoint [command]\n\
    \n\
Available Commands:\n\
    list    List all the available endpoints\
"
    print(content)
    return content


def help_get_menu():
    """
    Main get menu
    """
    content = "\
Usage: \n\
    crhc get [command]\n\
    \n\
Available Commands:\n\
    get <endpoint API URL HERE>     It will retrieve all the available methods\
"
    print(content)
    return content


def help_login_menu():
    """
    Main login menu
    """
    content = "\
Usage: \n\
    crhc login [flags]\n\
    \n\
Flags:\n\
    --token     Setting the offline token in order to get access to the content.\n\
    \n\
Info:\n\
    You can obtain a token at: https://console.redhat.com/openshift/token\n\
    \n\
    The command will be something similar to 'crhc login --token eyJhbGciOiJIUzI1NiIsIn...'\
"
    print(content)
    return content


def help_logout_menu():
    """
    Main logout menu
    """
    content = ""
    print(content)
    return content


def help_whoami_menu():
    """
    Main whoami menu
    """
    content = ""
    print(content)
    return content


def help_ts_menu():
    """
    Main ts/troubleshooting menu
    """
    content = "\
Usage: \n\
    crhc ts [command]\n\
    \n\
Available Commands:\n\
    dump    dump the json files, Inventory and Subscription\n\
    match   match the Inventory and Subscription information\n\
    clean   cleanup the local 'cache/temporary/dump' files\
"
    print(content)
    return content


def help_patch_menu():
    """
    Main patch menu
    """
    content = "\
Usage: \n\
    crhc patch [command]\n\
    \n\
Available Commands:\n\
    systems   It will provide some patch information\n\
    \n\
Flags:\n\
    --csv     This will generate the output in CSV format. By default, it will be JSON.\
"
    print(content)
    return content


def help_vulnerability_menu():
    """
    Main vulnerability menu
    """
    content = "\
Usage: \n\
    crhc vulnerability [command]\n\
    \n\
Available Commands:\n\
    systems   It will provide some vulnerability information\n\
    \n\
Flags:\n\
    --csv     This will generate the output in CSV format. By default, it will be JSON.\
"
    print(content)
    return content


def help_advisor_menu():
    """
    Main advisor menu
    """
    content = "\
Usage: \n\
    crhc advisor [command]\n\
    \n\
Available Commands:\n\
    systems   It will provide some insights information\n\
    \n\
Flags:\n\
    --csv     This will generate the output in CSV format. By default, it will be JSON.\
"
    print(content)
    return content
