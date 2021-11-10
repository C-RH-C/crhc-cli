Quick Start
===========

Please, access the release page `here`_ and check the version that you would like to use.

If for any reason the binary didn't run properly in your machine also with python3.6, as below example, probably you are using a bit old version of 3.6. In this case, you can create the virtual environment following the steps below, and generate a new binary file that will be 100% compatible with your current python version.

.. _here: https://github.com/C-RH-C/crhc-cli/releases/latest

If you see something as below, it seems that you have a python version older than 3.6.8

.. code-block::

    $ ./crhc
    [9554] Error loading Python lib '/tmp/_MEIWS0hNs/libpython3.6m.so.1.0': dlopen: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by /tmp/_MEIWS0hNs/libpython3.6m.so.1.0)

After downloaded, you just need to download the offline token from `https://console.redhat.com/openshift/token`_ and proceed via ``cli`` as below.

.. code-block:: sh

    $ ./crhc login --token eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiS...

The output below is expected

.. code-block:: sh

    Authenticated and ready to go!


From now, you are good to go and proceed with your queries based on the options available in the tool.

.. code-block::

    $ ./crhc
    Command line tool for console.redhat.com API

    Usage:
    crhc [command]

    Available Commands:
    inventory      Retrieve Inventory information
    swatch         Retrieve Subscriptions information
    advisor        Retrieve Insights Information
    patch          Retrieve Patch Information
    vulnerability  Retrieve Vulnerability Information
    endpoint       List all the available endpoints
    get            Send a GET request
    ts             Troubleshooting tasks

    login          Log in
    logout         Log out
    token          Generates a token
    whoami         Prints user information

    Flags:
    -h, --help                         help for crhc
    -v, --version                      crhc version

    Use "crhc [command] --help" for more information about a command.


.. _https://console.redhat.com/openshift/token: https://console.redhat.com/openshift/token