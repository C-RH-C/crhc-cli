"""
.. code-block:: text

    Module responsible for keep all the configuration paths and also
    the app version
"""

# Current Version
CURRENT_VERSION = "1.8.8"

#  Some file references

#  Report Info
INVENTORY_FILE = "/tmp/inventory_report.csv"
SWATCH_FILE = "/tmp/swatch_report.csv"
MATCH_FILE = "/tmp/match_inv_sw.csv"
ISSUE_SUMMARY = "/tmp/issue_summary.log"
PATCH_SYSTEMS_FILE = "/tmp/patch_systems.csv"
VULNERABILITY_SYSTEMS_FILE = "/tmp/vulnerability_systems.csv"
ADVISOR_FILE = "/tmp/advisor_systems.csv"
STALE_HOSTS_LIST = "/tmp/stale_hosts.csv"


# TS Info
INV_JSON_FILE = "/tmp/inventory.json"
SW_JSON_FILE = "/tmp/swatch.json"
MATCH_FILE = "/tmp/match_inv_sw.csv"
PATCH_JSON_FILE = "/tmp/patch.json"
VULNERABILITY_JSON_FILE = "/tmp/vulnerability.json"
ADVISOR_JSON_FILE = "/tmp/advisor.json"

TGZ_FILE = "/tmp/crhc_data.tgz"


# App conf file

# 43200 sec == 12h
# 21600 sec == 6h
TIME_TO_CHECK_THE_NEW_VERSION = 21600