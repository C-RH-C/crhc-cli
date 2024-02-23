#!/usr/bin/env python
"""
.. code-block:: text

    App responsible for collect some information from
    console.redhat.com (Inventory, Subscription and much more)
"""

from crhc_cli.parse import parse

if __name__ == "__main__":
    parse.main_menu()
