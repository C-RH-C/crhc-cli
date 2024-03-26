"""
.. code-block:: text

    Module responsible for keep all the configuration paths and also
    the app version
"""

import tempfile
from pathlib import Path


# Current Version
CURRENT_VERSION = "1.16.16"

#  Some file references

p = Path(tempfile.gettempdir())

#  Report Info
INVENTORY_FILE = (p / "inventory_report.csv").resolve()
SWATCH_FILE = (p / "swatch_report.csv").resolve()
MATCH_FILE = (p / "match_inv_sw.csv").resolve()

ISSUE_SUMMARY = (p / "issue_summary.log").resolve()
PATCH_SYSTEMS_FILE = (p / "patch_systems.csv").resolve()
VULNERABILITY_SYSTEMS_FILE = (p / "vulnerability_systems.csv").resolve()
ADVISOR_FILE = (p / "advisor_systems.csv").resolve()

STALE_FILE = (p / "stale_systems_based_on_date.json").resolve()

# TS Info
INV_JSON_FILE = (p / "inventory.json").resolve()
SW_JSON_FILE = (p / "swatch.json").resolve()
MATCH_FILE = (p / "match_inv_sw.csv").resolve()
PATCH_JSON_FILE = (p / "patch.json").resolve()
VULNERABILITY_JSON_FILE = (p / "vulnerability.json").resolve()
ADVISOR_JSON_FILE = (p / "advisor.json").resolve()

# TGZ_FILE = (p / "crhc_data.tgz").resolve()
ZIP_FILE = (p / "crhc_data.zip").resolve()


# App conf file

# 43200 sec == 12h
# 21600 sec == 6h
TIME_TO_CHECK_THE_NEW_VERSION = 21600

# Items per page when doing the API call
ITEMS_PER_PAGE = 50

# Ansible has a max limit of 25 Items per page when doing the API call
ANSIBLE_ITEMS_PER_PAGE = 25
