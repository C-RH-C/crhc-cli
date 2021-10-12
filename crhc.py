#!/usr/bin/env python
"""
App responsible for collect some information from
console.redhat.com (Inventory and Subscription Watch)
"""

from parse import parse

CURRENT_VERSION = "1.6.6"

if __name__ == "__main__":
    parse.main_menu()
