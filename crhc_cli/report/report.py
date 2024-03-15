"""
.. code-block:: text

    Module responsible for report
"""
# from os import write
import csv
import os
import json
from crhc_cli.conf import conf


def check_for_installed_products(entries):
    """
    Function responsible for extract the installed_product
    """

    # Checking for installed products
    count = 0
    count_product = 0
    stage_lst = []
    installed_product_lst = []
    stage_str = ""

    if (
        (entries["server"]["reporter"] == "puptoo")
        or (entries["server"]["reporter"] == "yupana")
        or entries["server"]["reporter"] == "rhsm-conduit"
    ):
        try:
            if len(entries["system_profile"]["installed_products"]) > 0:
                for ids in entries["system_profile"]["installed_products"]:
                    installed_product_lst.append(ids["id"])
                    count_product = count_product + 1

                stage_lst.append(installed_product_lst)
                installed_product_lst = []
        except KeyError:
            count = count + 1

    if entries["server"]["reporter"] == "rhsm-conduit":
        try:
            if len(entries["server"]["facts"][0]["facts"]["RH_PROD"]) > 0:
                for ids in entries["server"]["facts"][0]["facts"]["RH_PROD"]:
                    installed_product_lst.append(ids)
                    count_product = count_product + 1

                stage_lst.append(installed_product_lst)
                installed_product_lst = []
            elif len(entries["server"]["facts"][0]["facts"]["RH_PROD"]) == 0:
                stage_lst.append("No_installed_products_key_available")
        except KeyError:
            count = count + 1

    # if count != 0 and count_product == 0:
    #     stage_lst.append("No_installed_products_key_available")

    # TODO
    # else:
    #     stage_lst.append("reporter {}".format(entries['server']['reporter']))
    # print("oie")

    if (len(stage_lst) == 0) or (
        stage_lst[0] == "No_installed_products_key_available"
    ):
        stage_lst = "No_installed_products_key_available"

    elif stage_lst[0] != "No_installed_products_key_available":
        # Operation to turn the nested list flat
        # TODO
        stage_lst = [x for l in stage_lst for x in l]

        # Operation to remove the duplicate entries
        stage_lst = list(set(stage_lst))

    # Now, removing the "[" and " ' " characters from it.
    stage_str = (
        str(stage_lst).replace("[", "").replace("]", "").replace("'", "")
    )

    return stage_str


def check_for_syspurpose_sla(entries):
    """
    Function responsible for extract the system_purpose_sla
    """

    # Checking for syspurpose_sla information that came via fact
    if len(entries["server"]["facts"]) == 0:
        stage_lst = "No_facts_key_available"
    elif len(entries["server"]["facts"]) > 0:
        count = 0
        for source in entries["server"]["facts"]:
            try:
                if source["facts"]["SYSPURPOSE_SLA"]:
                    stage_lst = source["facts"]["SYSPURPOSE_SLA"]
                    count = 1
            except KeyError:
                ...

            try:
                if source["facts"]["system_purpose_sla"]:
                    stage_lst = source["facts"]["system_purpose_sla"]
                    count = 1
            except KeyError:
                ...

        if count == 0:
            stage_lst = "No_syspurpose_sla_key_available"

    return stage_lst


def check_for_system_purpose_role(entries):
    """
    Function responsible for extract the system_purpose_role
    """

    # Checking for system_purpose_role
    if len(entries["server"]["facts"]) == 0:
        stage_lst = "No_facts_key_available"
    elif len(entries["server"]["facts"]) > 0:
        count = 0
        for source in entries["server"]["facts"]:
            try:
                if source["facts"]["SYSPURPOSE_ROLE"]:
                    stage_lst = source["facts"]["SYSPURPOSE_ROLE"]
                    count = 1
            except KeyError:
                ...

            try:
                if source["facts"]["system_purpose_role"]:
                    stage_lst = source["facts"]["system_purpose_role"]
                    count = 1
            except KeyError:
                ...

        if count == 0:
            stage_lst = "No_system_purpose_role_key_available"

    return stage_lst


def check_for_system_purpose_usage(entries):
    """
    Function responsible for extract the system_purpose_usage
    """

    # Checking for system_purpose_usage
    if len(entries["server"]["facts"]) == 0:
        stage_lst = "No_facts_key_available"
    elif len(entries["server"]["facts"]) > 0:
        count = 0
        for source in entries["server"]["facts"]:
            try:
                if source["facts"]["SYSPURPOSE_USAGE"]:
                    stage_lst = source["facts"]["SYSPURPOSE_USAGE"]
                    count = 1
            except KeyError:
                ...

            try:
                if source["facts"]["system_purpose_usage"]:
                    stage_lst = source["facts"]["system_purpose_usage"]
                    count = 1
            except KeyError:
                ...

        if count == 0:
            stage_lst = "No_system_purpose_usage_key_available"

    return stage_lst


def check_is_simple_content_access(entries):
    """
    Function responsible for check the SCA
    """

    # Checking for is_simple_content_access
    if len(entries["server"]["facts"]) == 0:
        stage_lst = "No_facts_key_available"
    elif len(entries["server"]["facts"]) > 0:
        count = 0
        for source in entries["server"]["facts"]:
            try:
                if source["facts"]["is_simple_content_access"]:
                    stage_lst = source["facts"]["is_simple_content_access"]
                    count = 1
            except KeyError:
                ...

        if count == 0:
            stage_lst = "No_is_simple_content_access_key_available"

    return stage_lst


def check_for_satellite_package(entries):
    """
    Function responsible for check if the satellite package is around
    """

    # Checking for satellite packages
    try:
        count = 0
        for pkg in entries["system_profile"]["installed_packages"]:
            if "satellite" in pkg:
                count = count + 1
        if count > 0:
            stage_lst = "TRUE"
        else:
            stage_lst = "FALSE"
    except KeyError:
        stage_lst = "No_installed_packages_key_available"

    return stage_lst


def check_for_openshift_package(entries):
    """
    Function responsible for check if the openshift package is around
    """

    # Checking for openshift packages
    try:
        count = 0
        for pkg in entries["system_profile"]["installed_packages"]:
            if "openshift" in pkg:
                count = count + 1
        if count > 0:
            stage_lst = "TRUE"
        else:
            stage_lst = "FALSE"
    except KeyError:
        stage_lst = "No_installed_packages_key_available"

    return stage_lst


def check_for_hypervisor_that_this_guest_belongs(entries):
    """
    Function responsible for check if the openshift package is around
    """

    # TODO

    stage_lst = []

    # Checking the hypervisor that this guest belongs
    if len(entries["server"]["facts"]) == 0:
        stage_lst.append("No_facts_key_available")
        stage_lst.append("No_facts_key_available")
    elif len(entries["server"]["facts"]) > 0:
        count = 0
        for source in entries["server"]["facts"]:
            if source["namespace"] == "satellite":
                try:
                    if source["facts"]["virtual_host_name"]:
                        stage_lst.append(source["facts"]["virtual_host_name"])
                        stage_lst.append(source["facts"]["virtual_host_uuid"])
                        # stage_lst.append(source['facts']['satellite_instance_id'])
                        count = count + 1
                except KeyError:
                    # count = count + 1
                    ...
            if source["namespace"] == "rhsm":
                try:
                    if source["facts"]["VM_HOST"]:
                        stage_lst.append(source["facts"]["VM_HOST"])
                        stage_lst.append(source["facts"]["VM_HOST_UUID"])
                        count = count + 1
                except KeyError:
                    ...

        if count == 0:
            stage_lst.append("No_hypervisor_fqdn")
            stage_lst.append("No_hypervisor_uuid")

    return stage_lst


def check_for_number_of_guests_on_top_of_the_hypervisor_inventory(
    entries, json_obj
):
    """
    Function responsible for check the # of guests on each hypervisor
    """

    # Counting the number of guests on top of the hypervisor
    number_of_guests = 0
    for each_server in json_obj["results"]:
        if len(each_server["server"]["facts"]) > 0:
            for elements in each_server["server"]["facts"]:

                if elements["namespace"] == "satellite":
                    try:
                        if elements["facts"]["virtual_host_name"]:
                            if (
                                elements["facts"]["virtual_host_uuid"]
                                == entries["server"]["satellite_id"]
                            ):
                                number_of_guests = number_of_guests + 1
                    except KeyError:
                        ...

                if elements["namespace"] == "rhsm":
                    try:
                        if elements["facts"]["VM_HOST"]:
                            if (
                                elements["facts"]["VM_HOST_UUID"]
                                == entries["server"]["subscription_manager_id"]
                            ):
                                number_of_guests = number_of_guests + 1
                    except KeyError:
                        ...

    if number_of_guests == 0:
        stage_lst = "No guests"
    else:
        stage_lst = number_of_guests

    return stage_lst


def check_for_number_of_guests_on_top_of_the_hypervisor_match(
    entries, match_obj
):
    """
    Function responsible for check the # of guests on each hypervisor
    """

    # Counting the number of guests on top of the hypervisor
    number_of_guests = 0
    for each_server in match_obj:
        if len(each_server[0]["server"]["facts"]) > 0:
            for elements in each_server[0]["server"]["facts"]:

                if elements["namespace"] == "satellite":
                    try:
                        if elements["facts"]["virtual_host_name"]:
                            if (
                                elements["facts"]["virtual_host_uuid"]
                                == entries["server"]["satellite_id"]
                            ):
                                number_of_guests = number_of_guests + 1
                    except KeyError:
                        ...

                if elements["namespace"] == "rhsm":
                    try:
                        if elements["facts"]["VM_HOST"]:
                            if (
                                elements["facts"]["VM_HOST_UUID"]
                                == entries["server"]["subscription_manager_id"]
                            ):
                                number_of_guests = number_of_guests + 1
                    except KeyError:
                        ...

    if number_of_guests == 0:
        stage_lst = "No guests"
    else:
        stage_lst = number_of_guests

    return stage_lst


def csv_report_inventory(json_obj):
    """
    Function to generate the CSV report for inventory
    """

    report_list = []
    # installed_product_lst = []

    stage_lst = [
        "id",
        "created",
        "updated",
        "stale_timestamp",
        "stale_warning_timestamp",
        "culled_timestamp",
        "fqdn",
        "display_name",
        "ansible_host",
        "cpu_model",
        "number_of_cpus",
        "number_of_sockets",
        "core_socket",
        "system_memory_bytes",
        "bios_vendor",
        "bios_version",
        "bios_release_date",
        "os_release",
        "os_kernel_version",
        "arch",
        "last_boot_time",
        "infrastructure_type",
        "infrastructure_vendor",
        "insights_client_version",
        "created",
        "insights_id",
        "reporter",
        "bios_uuid",
        "tuned_profile",
        "sap_system",
        "sap_version",
        "system_purpose_sla",
        "system_purpose_role",
        "system_purpose_usage",
        "is_simple_content_access",
        "installed_product",
        "has_satellite_package",
        "has_openshift_package",
        "hypervisor_fqdn",
        "hypervisor_uuid",
        "number_of_guests",
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj["results"]:

        try:
            stage_lst.append(entries["server"]["id"])
        except KeyError:
            stage_lst.append("No_id_key_available")

        try:
            stage_lst.append(entries["server"]["created"])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries["server"]["updated"])
        except KeyError:
            stage_lst.append("No_updated_key_available")

        try:
            stage_lst.append(entries["server"]["stale_timestamp"])
        except KeyError:
            stage_lst.append("No_stale_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["stale_warning_timestamp"])
        except KeyError:
            stage_lst.append("No_stale_warning_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["culled_timestamp"])
        except KeyError:
            stage_lst.append("No_culled_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["fqdn"])
        except KeyError:
            stage_lst.append("No_fqdn_key_available")

        try:
            stage_lst.append(entries["server"]["display_name"])
        except KeyError:
            stage_lst.append("No_display_name_key_available")

        try:
            stage_lst.append(entries["server"]["ansible_host"])
        except KeyError:
            stage_lst.append("No_ansible_host_key_available")

        try:
            stage_lst.append(entries["system_profile"]["cpu_model"])
        except KeyError:
            stage_lst.append("No_cpu_model_key_available")

        try:
            stage_lst.append(entries["system_profile"]["number_of_cpus"])
        except KeyError:
            stage_lst.append("No_number_of_cpus_key_available")

        try:
            stage_lst.append(entries["system_profile"]["number_of_sockets"])
        except KeyError:
            stage_lst.append("No_number_of_sockets_key_available")

        try:
            stage_lst.append(entries["system_profile"]["core_socket"])
        except KeyError:
            stage_lst.append("No_core_socket_available")

        try:
            stage_lst.append(entries["system_profile"]["system_memory_bytes"])
        except KeyError:
            stage_lst.append("No_system_memory_bytes_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_vendor"])
        except KeyError:
            stage_lst.append("No_bios_vendor_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_version"])
        except KeyError:
            stage_lst.append("No_bios_version_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_release_date"])
        except KeyError:
            stage_lst.append("No_bios_release_date_key_available")

        try:
            stage_lst.append(entries["system_profile"]["os_release"])
        except KeyError:
            stage_lst.append("No_os_release_key_available")

        try:
            stage_lst.append(entries["system_profile"]["os_kernel_version"])
        except KeyError:
            stage_lst.append("No_os_kernel_version_key_available")

        try:
            stage_lst.append(entries["system_profile"]["arch"])
        except KeyError:
            stage_lst.append("No_arch_key_available")

        try:
            stage_lst.append(entries["system_profile"]["last_boot_time"])
        except KeyError:
            stage_lst.append("No_last_boot_time_key_available")

        try:
            stage_lst.append(entries["system_profile"]["infrastructure_type"])
        except KeyError:
            stage_lst.append("No_infrastructure_type_key_available")

        try:
            stage_lst.append(
                entries["system_profile"]["infrastructure_vendor"]
            )
        except KeyError:
            stage_lst.append("No_infrastructure_vendor_key_available")

        try:
            stage_lst.append(
                entries["system_profile"]["insights_client_version"]
            )
        except KeyError:
            stage_lst.append("No_insights_client_version_key_available")

        try:
            stage_lst.append(entries["server"]["created"])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries["server"]["insights_id"])
        except KeyError:
            stage_lst.append("No_insights_id_key_available")

        try:
            stage_lst.append(entries["server"]["reporter"])
        except KeyError:
            stage_lst.append("No_reporter_key_available")

        try:
            stage_lst.append(entries["server"]["bios_uuid"])
        except KeyError:
            stage_lst.append("No_bios_uuid_key_available")

        try:
            stage_lst.append(entries["system_profile"]["tuned_profile"])
        except KeyError:
            stage_lst.append("No_tuned_profile_key_available")

        try:
            stage_lst.append(entries["system_profile"]["sap_system"])
        except KeyError:
            stage_lst.append("No_sap_system_key_available")

        try:
            stage_lst.append(entries["system_profile"]["sap_version"])
        except KeyError:
            stage_lst.append("No_sap_version_key_available")

        # Checking for system_purpose_role
        stage_lst.append(check_for_syspurpose_sla(entries))

        # Checking for system_purpose_role
        stage_lst.append(check_for_system_purpose_role(entries))

        # Checking for system_purpose_role
        stage_lst.append(check_for_system_purpose_usage(entries))

        # Checking for is_simple_content_access
        stage_lst.append(check_is_simple_content_access(entries))

        # Checking for the installed_products
        stage_lst.append(check_for_installed_products(entries))

        # Checking for satellite packages
        stage_lst.append(check_for_satellite_package(entries))

        # Checking for openshift packages
        stage_lst.append(check_for_openshift_package(entries))

        # Checking the hypervisor that this guest belongs
        hyper_info = check_for_hypervisor_that_this_guest_belongs(entries)
        hyper_fqdn = hyper_info[0]
        hyper_uuid = hyper_info[1]
        stage_lst.append(hyper_fqdn)
        stage_lst.append(hyper_uuid)

        # Counting the number of guests on top of the hypervisor
        stage_lst.append(
            check_for_number_of_guests_on_top_of_the_hypervisor_inventory(
                entries, json_obj
            )
        )

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.INVENTORY_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)
        # writer.writerow(report_list)

    print("File {} created".format(conf.INVENTORY_FILE))


def csv_report_swatch(json_obj):
    """
    Function to generate the CSV report for swatch
    """

    report_list = []

    stage_lst = [
        "display_name",
        "inventory_id",
        "number_of_guests",
        "last_seen",
        "category",
        "sockets",
        "subscription_manager_id",
        "cloud_provider",
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj["data"]:

        try:
            stage_lst.append(entries["display_name"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["inventory_id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["number_of_guests"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["last_seen"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["category"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            # using the int to remove the decimal value and to keep
            # this output as integer
            stage_lst.append(int(entries["measurements"][0]))
        except KeyError:
            stage_lst.append("Not in sw - check")

        try:
            stage_lst.append(entries["subscription_manager_id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["cloud_provider"])
        except KeyError:
            stage_lst.append("Not available")

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.SWATCH_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(conf.SWATCH_FILE))


def csv_match_report(match_obj):
    """
    Function responsible for match the information from
    Inventory and Subscription data, creating a single
    dataset (CSV)
    """
    report_list = []
    # installed_product_lst = []

    stage_lst = [
        "id",
        "created",  # added
        "updated",
        "stale_timestamp",  # added
        "stale_warning_timestamp",  # added
        "culled_timestamp",  # added
        "fqdn",
        "display_name",
        "ansible_host",
        "cpu_model",
        "number_of_cpus",
        "number_of_sockets",
        "core_socket",
        "system_memory_bytes",
        "bios_vendor",
        "bios_version",
        "bios_release_date",
        "os_release",
        "os_kernel_version",
        "arch",
        "last_boot_time",
        "infrastructure_type",
        "infrastructure_vendor",
        "insights_client_version",
        "created",
        "insights_id",
        "reporter",
        "bios_uuid",
        "tuned_profile",
        "sap_system",
        "sap_version",
        "system_purpose_sla",
        "system_purpose_role",
        "system_purpose_usage",
        "is_simple_content_access",
        "installed_product",
        "has_satellite_package",
        "has_openshift_package",
        "hypervisor_fqdn",
        "hypervisor_uuid",
        "number_of_guests",
        "sw_display_name",
        "sw_inventory_id",
        "sw_number_of_guests",
        "sw_last_seen",
        "sw_category",
        "sw_sockets",
        "sw_subscription_manager_id",
        "sw_cloud_provider",
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for elements in match_obj:
        entries = elements[0]
        sw_entries = elements[1]

        # if ( elements[0]["server"]["id"] == "12708bed-125b-46d7-bf81-66e46a33de1c" ):
        #     print("here again")

        try:
            stage_lst.append(entries["server"]["id"])
        except KeyError:
            stage_lst.append("No_id_key_available")

        try:
            stage_lst.append(entries["server"]["created"])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries["server"]["updated"])
        except KeyError:
            stage_lst.append("No_updated_key_available")

        try:
            stage_lst.append(entries["server"]["stale_timestamp"])
        except KeyError:
            stage_lst.append("No_stale_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["stale_warning_timestamp"])
        except KeyError:
            stage_lst.append("No_stale_warning_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["culled_timestamp"])
        except KeyError:
            stage_lst.append("No_culled_timestamp_key_available")

        try:
            stage_lst.append(entries["server"]["fqdn"])
        except KeyError:
            stage_lst.append("No_fqdn_key_available")

        try:
            stage_lst.append(entries["server"]["display_name"])
        except KeyError:
            stage_lst.append("No_display_name_key_available")

        try:
            stage_lst.append(entries["server"]["ansible_host"])
        except KeyError:
            stage_lst.append("No_ansible_host_key_available")

        try:
            stage_lst.append(entries["system_profile"]["cpu_model"])
        except KeyError:
            stage_lst.append("No_cpu_model_key_available")

        try:
            stage_lst.append(entries["system_profile"]["number_of_cpus"])
        except KeyError:
            stage_lst.append("No_number_of_cpus_key_available")

        try:
            stage_lst.append(entries["system_profile"]["number_of_sockets"])
        except KeyError:
            stage_lst.append("No_number_of_sockets_key_available")

        try:
            stage_lst.append(entries["system_profile"]["core_socket"])
        except KeyError:
            stage_lst.append("No_core_socket_available")

        try:
            stage_lst.append(entries["system_profile"]["system_memory_bytes"])
        except KeyError:
            stage_lst.append("No_system_memory_bytes_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_vendor"])
        except KeyError:
            stage_lst.append("No_bios_vendor_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_version"])
        except KeyError:
            stage_lst.append("No_bios_version_key_available")

        try:
            stage_lst.append(entries["system_profile"]["bios_release_date"])
        except KeyError:
            stage_lst.append("No_bios_release_date_key_available")

        try:
            stage_lst.append(entries["system_profile"]["os_release"])
        except KeyError:
            stage_lst.append("No_os_release_key_available")

        try:
            stage_lst.append(entries["system_profile"]["os_kernel_version"])
        except KeyError:
            stage_lst.append("No_os_kernel_version_key_available")

        try:
            stage_lst.append(entries["system_profile"]["arch"])
        except KeyError:
            stage_lst.append("No_arch_key_available")

        try:
            stage_lst.append(entries["system_profile"]["last_boot_time"])
        except KeyError:
            stage_lst.append("No_last_boot_time_key_available")

        try:
            stage_lst.append(entries["system_profile"]["infrastructure_type"])
        except KeyError:
            stage_lst.append("No_infrastructure_type_key_available")

        try:
            stage_lst.append(
                entries["system_profile"]["infrastructure_vendor"]
            )
        except KeyError:
            stage_lst.append("No_infrastructure_vendor_key_available")

        try:
            stage_lst.append(
                entries["system_profile"]["insights_client_version"]
            )
        except KeyError:
            stage_lst.append("No_insights_client_version_key_available")

        try:
            stage_lst.append(entries["server"]["created"])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries["server"]["insights_id"])
        except KeyError:
            stage_lst.append("No_insights_id_key_available")

        try:
            stage_lst.append(entries["server"]["reporter"])
        except KeyError:
            stage_lst.append("No_reporter_key_available")

        try:
            stage_lst.append(entries["server"]["bios_uuid"])
        except KeyError:
            stage_lst.append("No_bios_uuid_key_available")

        try:
            stage_lst.append(entries["system_profile"]["tuned_profile"])
        except KeyError:
            stage_lst.append("No_tuned_profile_key_available")

        try:
            stage_lst.append(entries["system_profile"]["sap_system"])
        except KeyError:
            stage_lst.append("No_sap_system_key_available")

        try:
            stage_lst.append(entries["system_profile"]["sap_version"])
        except KeyError:
            stage_lst.append("No_sap_version_key_available")

        # Checking for system_purpose_role
        stage_lst.append(check_for_syspurpose_sla(entries))

        # Checking for system_purpose_role
        stage_lst.append(check_for_system_purpose_role(entries))

        # Checking for system_purpose_role
        stage_lst.append(check_for_system_purpose_usage(entries))

        # Checking for is_simple_content_access
        stage_lst.append(check_is_simple_content_access(entries))

        # Checking for the installed_products
        stage_lst.append(check_for_installed_products(entries))

        # Checking for satellite packages
        stage_lst.append(check_for_satellite_package(entries))

        # Checking for openshift packages
        stage_lst.append(check_for_openshift_package(entries))

        # Checking the hypervisor that this guest belongs
        hyper_info = check_for_hypervisor_that_this_guest_belongs(entries)
        hyper_fqdn = hyper_info[0]
        hyper_uuid = hyper_info[1]
        stage_lst.append(hyper_fqdn)
        stage_lst.append(hyper_uuid)

        # Counting the number of guests on top of the hypervisor
        stage_lst.append(
            check_for_number_of_guests_on_top_of_the_hypervisor_match(
                entries, match_obj
            )
        )

        if sw_entries == "not in swatch":
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")

        else:
            try:
                stage_lst.append(sw_entries["display_name"])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries["instance_id"])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries["number_of_guests"])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries["last_seen"])
            except KeyError:
                stage_lst.append("Not in sw")

            # Category
            try:
                stage_lst.append(sw_entries["category"])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                # using the int to remove the decimal value and to keep
                # this output as integer
                stage_lst.append(int(sw_entries["measurements"][0]))
            except KeyError:
                stage_lst.append("Not in sw - check")

            try:
                stage_lst.append(sw_entries["subscription_manager_id"])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries["cloud_provider"])
            except KeyError:
                stage_lst.append("Not in sw")

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.MATCH_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(conf.MATCH_FILE))


def txt_issue_report(
    wrong_socket_inventory,
    wrong_socket_subscription,
    duplicate_fqdn,
    duplicate_display_name,
    different_fqdn_display_name,
    server_with_no_socket_key,
    installed_product_with_no_package_sat,
    installed_product_with_no_package_cap,
    installed_product_with_no_package_ocp,
):
    """
    Responsible to reveive the analysis and generate the issue_summary file.
    """

    with open(conf.ISSUE_SUMMARY, "w", newline="") as file_obj:

        file_obj.write("## Wrong Sockets in Inventory\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,sockets\n")
        for elements in wrong_socket_inventory:
            id = elements[0]["server"]["id"]
            fqdn = elements[0]["server"]["fqdn"]
            sockets = elements[0]["system_profile"]["number_of_sockets"]
            pass
            file_obj.write("{},{},{}\n".format(id, fqdn, sockets))
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write("## Wrong Sockets in Subscriptions\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,sockets\n")
        for elements in wrong_socket_subscription:
            id = elements[1]["inventory_id"]
            fqdn = elements[1]["display_name"]
            sockets = elements[1]["sockets"]
            pass
            file_obj.write("{},{},{}\n".format(id, fqdn, sockets))
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write("## Duplicate FQDN\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,display_name,created,updated\n")
        for elements in duplicate_fqdn:
            file_obj.write(
                "{},{},{},{},{}\n".format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write("## Duplicate Display Name\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,display_name,created,updated\n")
        for elements in duplicate_display_name:
            file_obj.write(
                "{},{},{},{},{}\n".format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write("## Different FQDN and Display Name\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,display_name,created,updated\n")
        for elements in different_fqdn_display_name:
            file_obj.write(
                "{},{},{},{},{}\n".format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write("## Server with no socket_key\n")
        file_obj.write("---\n")
        file_obj.write("id,fqdn,display_name,created,updated\n")
        for elements in server_with_no_socket_key:
            file_obj.write(
                "{},{},{},{},{}\n".format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        file_obj.write("---\n")

        file_obj.write("\n")

        file_obj.write(
            "## Installed Product with no Installed Package \
(Satellite, Capsule and OpenShift)\n"
        )
        file_obj.write("---\n")
        file_obj.write(
            "id,fqdn,display_name,installed_product,is_package_installed\n"
        )
        for elements in installed_product_with_no_package_sat:
            file_obj.write(
                '{},{},{},"{}",{}\n'.format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        for elements in installed_product_with_no_package_cap:
            file_obj.write(
                '{},{},{},"{}",{}\n'.format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )
        for elements in installed_product_with_no_package_ocp:
            file_obj.write(
                '{},{},{},"{}",{}\n'.format(
                    elements[0],
                    elements[1],
                    elements[2],
                    elements[3],
                    elements[4],
                )
            )

        file_obj.write("---\n")

    if os.path.isfile(conf.ISSUE_SUMMARY):
        print("File {} created".format(conf.ISSUE_SUMMARY))
    else:
        print("File {} was not created".format(conf.ISSUE_SUMMARY))


def csv_report_patch(json_obj):
    """
    Function to generate the CSV report for patch
    """

    report_list = []

    stage_lst = [
        "id",
        "type",
        "created",
        "culled_timestamp",
        "display_name",
        "insights_id",
        "last_evaluation",
        "last_upload",
        "os",
        "os_major",
        "os_minor",
        "os_name",
        "other_count",
        "packages_installed",
        "packages_updatable",
        "rhba_count",
        "rhea_count",
        "rhsa_count",
        "rhsm",
        "stale",
        "stale_timestamp",
        "stale_warning_timestamp",
        "third_party",
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj["data"]:

        try:
            stage_lst.append(entries["id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["type"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["created"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["culled_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["display_name"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["insights_id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["last_evaluation"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["last_upload"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["os"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["os_major"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["os_minor"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["os_name"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["other_count"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["packages_installed"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["packages_updatable"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["rhba_count"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["rhea_count"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["rhsa_count"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["rhsm"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["stale"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["stale_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["stale_warning_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["third_party"])
        except KeyError:
            stage_lst.append("Not available")

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.PATCH_SYSTEMS_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(conf.PATCH_SYSTEMS_FILE))


def csv_report_vulnerability(json_obj):
    """
    Function to generate the CSV report for vulnerability
    """

    report_list = []

    stage_lst = [
        "type",
        "culled_timestamp",
        "cve_count",
        "display_name",
        "insights_id",
        "inventory_id",
        "last_evaluation",
        "last_upload",
        "opt_out",
        "os",
        "rules_evaluation",
        "stale_timestamp",
        "stale_warning_timestamp",
        "updated",
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj["data"]:

        try:
            stage_lst.append(entries["type"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["culled_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["cve_count"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["display_name"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["insights_id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["inventory_id"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["last_evaluation"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["last_upload"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["opt_out"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["os"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["rules_evaluation"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["stale_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["stale_warning_timestamp"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["attributes"]["updated"])
        except KeyError:
            stage_lst.append("Not available")

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.VULNERABILITY_SYSTEMS_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(conf.VULNERABILITY_SYSTEMS_FILE))


def csv_report_advisor(json_obj):
    """
    Function to generate the CSV report for advisor/insights
    """

    report_list = []

    stage_lst = [
        "system_uuid",
        "display_name",
        "last_seen",
        "stale_at",
        "recommendations",  # hits
        "critical",  # critical_hits
        "important",  # important_hits
        "moderate",  # moderate_hits
        "low",  # low_hits
        "incident"  # incident_hits
        #  "all_pathway_hits",
        #  "pathway_filter_hits"
    ]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj["data"]:

        try:
            stage_lst.append(entries["system_uuid"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["display_name"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["last_seen"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["stale_at"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["hits"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["critical_hits"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["important_hits"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["moderate_hits"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["low_hits"])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries["incident_hits"])
        except KeyError:
            stage_lst.append("Not available")

        # doesn't seem to be necessary.

        # try:
        #     stage_lst.append(entries['all_pathway_hits'])
        # except KeyError:
        #     stage_lst.append("Not available")

        # try:
        #     stage_lst.append(entries['pathway_filter_hits'])
        # except KeyError:
        #     stage_lst.append("Not available")

        report_list.append(stage_lst)
        stage_lst = []

    with open(conf.ADVISOR_FILE, "w", newline="") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(conf.ADVISOR_FILE))


def json_stale_systems(stale_srv_list):
    """
    Responsible for write down the entries that will be removed. Note,
    it will be in JSON format.
    """
    # print("inside the report")
    # print(json.dumps(stale_srv_list, indent=4))

    with open(conf.STALE_FILE, "w") as file_obj:
        file_obj.write(json.dumps(stale_srv_list, indent=4))
