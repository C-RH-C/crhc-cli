"""
.. code-block:: text

    Module responsible for set the app credential
"""

import getpass
import os
import sys
import requests


def set_credential():
    """
    Responsible to set the credential, create the local file and also
    validade if the credential is working as expected
    """
    print(
        "setting the credential. At this moment, the credential will be \
saved as clear text in ~/.crhc.conf"
    )
    user = input("Type your console.redhat.com username: ")
    password = getpass.getpass("Type your console.redhat.com password: ")

    url = "https://console.redhat.com/api/inventory/v1/hosts"
    response = requests.get(url, auth=(user, password))

    if response.status_code == 200:
        print("Authenticated and ready to go!")
    else:
        print("Please, type again, wrong username or password")
        sys.exit()

    home_dir = os.path.expanduser("~")
    with open(home_dir + "/.crhc.conf", "w") as file_obj:
        file_obj.writelines("username:" + user)
        file_obj.writelines("\n")
        file_obj.writelines("password:" + str(password))


def read_credential():
    """
    Responsible to read the credential, and in case the credential
    is not present yet, a new file will be created with no valid
    username and/or password
    """
    home_dir = os.path.expanduser("~")

    try:
        with open(home_dir + "/.crhc.conf", "r") as file_obj:
            for line in file_obj:
                if "username" in line:
                    username = line.split(":")[1]
                if "password" in line:
                    password = line.split(":")[1]
        return username, password
    except FileNotFoundError:
        home_dir = os.path.expanduser("~")
        with open(home_dir + "/.crhc.conf", "w") as file_obj:
            file_obj.writelines("username:")
            file_obj.writelines("\n")
            file_obj.writelines("password:")
