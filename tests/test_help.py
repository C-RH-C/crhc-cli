"""
.. code-block:: text

    Module responsible for test the help menu content
"""

from crhc_cli.help import help_opt


def test_check_main_help_menu():
    """
    Responsible for test the main help menu
    """
    response = help_opt.help_main_menu()
    content = "\
CRHC Command Line Tool\n\
    \n\
Usage: \n\
    crhc [command]\n\
    \n\
Available Commands:\n\
    inventory       To list the Inventory data.\n\
    swatch          To list the Subscription data.\n\
    advisor         Retrieve Insights Information\n\
    patch           Retrieve Patch Information\n\
    vulnerability   Retrieve Vulnerability Information\n\
    ansible         Retrieve Ansible Managed Host Information\n\
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
    assert response == content


def test_check_inventory_help_menu():
    """
    Responsible for test the inventory help menu
    """
    response = help_opt.help_inventory_menu()
    content = "\
Usage: \n\
    crhc inventory [command]\n\
    \n\
Available Commands:\n\
    list            List the inventory entries, first 50\n\
    list_all        List all the inventory entries\n\
    display_name    Please, type the FQDN or Partial Hostname\n\
    list_stale      List all the machines in stale and stale_warning status\n\
    remove_stale    Remove all the stale entries based on the # of days\n\
    \n\
Flags: \n\
    --csv           This will generate the output in CSV format. By default, it will be JSON.\
"
    assert response == content


def test_check_swatch_help_menu():
    """
    Responsible for test the subscription help menu
    """
    response = help_opt.help_swatch_menu()
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
    assert response == content


def test_check_endpoint_help_menu():
    """
    Responsible for test the endpoint help menu
    """
    response = help_opt.help_endpoint_menu()
    content = "\
Usage: \n\
    crhc endpoint [command]\n\
    \n\
Available Commands:\n\
    list    List all the available endpoints\
"
    assert response == content


def test_check_get_help_menu():
    """
    Responsible for test the get help menu
    """
    response = help_opt.help_get_menu()
    content = "\
Usage: \n\
    crhc get [command]\n\
    \n\
Available Commands:\n\
    get <endpoint API URL HERE>     It will retrieve all the available methods\
"
    assert response == content


def test_check_login_help_menu():
    """
    Responsible for test the login help menu
    """
    response = help_opt.help_login_menu()
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
    assert response == content


def test_check_ts_help_menu():
    """
    Responsible for test the ts help menu
    """
    response = help_opt.help_ts_menu()
    content = "\
Usage: \n\
    crhc ts [command]\n\
    \n\
Available Commands:\n\
    dump            dump the json files, Inventory and Subscription\n\
    dump_current    dump the json files with current systems only, Inventory and Subscription\n\
    match           match the Inventory and Subscription information\n\
    clean           cleanup the local 'cache/temporary/dump' files\
"
    assert response == content


def test_check_patch_help_menu():
    """
    Responsible for test the patch help menu
    """
    response = help_opt.help_patch_menu()
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
    assert response == content


def test_check_vulnerability_help_menu():
    """
    Responsible for test the patch help menu
    """
    response = help_opt.help_vulnerability_menu()
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
    assert response == content


def test_check_advisor_help_menu():
    """
    Responsible for test the advisor help menu
    """
    response = help_opt.help_advisor_menu()
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
    assert response == content


def test_check_ansible_help_menu():
    """
    Responsible for test the advisor help menu
    """
    response = help_opt.help_ansible_menu()
    content = "\
Usage: \n\
    crhc ansible [command]\n\
    \n\
Available Commands:\n\
    unique_hosts   It will provide the list of unique hosts managed by ansible automation platform\n\
    \n\
"
    assert response == content
