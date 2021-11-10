Contribution
============

I really hope this helps you.

If you need anything else of if you are facing issues trying to use it, please let me know via email or feel free to open a repository issue `here`_

Also, if you believe this project is valuable for you, feel free to share your feedback via contacts below. This will help to push this project forward.

waldirio@redhat.com / waldirio@gmail.com


.. _here: https://github.com/C-RH-C/crhc-cli/issues/new

If you would like to play around with the Code, let's proceed as below

------

**Source_Code**

In your RHEL/CentOS/Fedora/etc with Python 3.x installed, let's execute the commands in a sequence

.. code-block::

    $ git clone https://github.com/C-RH-C/crhc-cli.git
    $ cd crhc-cli
    $ python3 -m venv ~/.virtualenv/crhc-cli
    $ source ~/.virtualenv/crhc-cli/bin/activate

Now, you should be in your virtual environment. You can realize your prompt will change

.. code-block::

    (crhc-cli) [user@server crhc-cli]$


We can continue

.. code-block::

    (crhc-cli) [user@server crhc-cli]$ pip install --upgrade pip
    (crhc-cli) [user@server crhc-cli]$ pip install -r requirements.txt


And finally, we are good to go.

.. code-block::

    (crhc-cli) [user@server crhc-cli]$ ./crhc.py


The menu will be as below

.. code-block::

    (crhc-cli) [user@server crhc-cli]$ ./crhc.py 
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


Great, now it's time to generate the binary file, please, execute the step below yet in your virtual environment

.. code-block::

    (crhc-cli) [user@server crhc-cli]$ pyinstaller --onefile crhc.py


At the end of this process, the binary file will be available under the `dist` dir, then you can redistribute or copy to any other machine running the same python version and everything will be running with no issues.

.. code-block:: sh

    (crhc-cli) [user@server crhc-cli]$  file dist/crhc 
    dist/crhc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), BuildID[sha1]=f6af5bc244c001328c174a6abf855d682aa7401b, for GNU/Linux 2.6.32, stripped



Thank you in advance! :)