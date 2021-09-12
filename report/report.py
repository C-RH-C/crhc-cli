# from os import write
import csv

INVENTORY_FILE = "/tmp/inventory_report.csv"
SWATCH_FILE = "/tmp/swatch_report.csv"
MATCH_FILE = "/tmp/match_inv_sw.csv"


def csv_report_inventory(json_obj):
    """
    Function to generate the CSV report for inventory
    """

    report_list = []
    installed_product_lst = []

    stage_lst = ["id",
                   "updated",
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
                   "rhel_machine_id",
                   "tuned_profile",
                   "sap_system",
                   "sap_version",
                   "syspurpose_sla",
                   "installed_product",
                   "has_satellite_package",
                   "has_openshift_package",
                   "hypervisor_fqdn",
                   "hypervisor_uuid"]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj['results']:
        pass
        try:
            stage_lst.append(entries['server']['id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['updated'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['fqdn'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['display_name'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['ansible_host'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['cpu_model'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['number_of_cpus'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['number_of_sockets'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['core_socket'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['system_memory_bytes'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['bios_vendor'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['bios_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['bios_release_date'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['os_release'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['os_kernel_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['arch'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['last_boot_time'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_type'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_vendor'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['insights_client_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['created'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['insights_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['reporter'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['server']['rhel_machine_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['tuned_profile'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['sap_system'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['system_profile']['sap_version'])
        except KeyError:
            stage_lst.append("Not available")

        # Checking for syspurpose_sla information that came via fact
        if len(entries['server']['facts']) == 0:
            stage_lst.append("Not available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['SYSPURPOSE_SLA']:
                        stage_lst.append(source['facts']['SYSPURPOSE_SLA'])
                except KeyError:
                    count = count + 1

            if count != 0:
                stage_lst.append("Not available")

        # Checking for installed products
        if (entries['server']['reporter'] == "puptoo") or (entries[0]['server']['reporter'] == "yupana"):
            try:
                if len(entries['system_profile']['installed_products']) > 0:
                    for ids in entries['system_profile']['installed_products']:
                        installed_product_lst.append(ids['id'])

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No installed product key available")

        elif entries['server']['reporter'] == "rhsm-conduit":
            try:
                if len(entries['server']['facts'][0]['facts']['RH_PROD']) > 0:
                    for ids in entries['server']['facts'][0]['facts']['RH_PROD']:
                        installed_product_lst.append(ids)

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No installed product key available")

        # Checking for satellite packages
        try:
            count = 0
            for pkg in entries['system_profile']['installed_packages']:
                if "satellite" in pkg:
                    count = count + 1
            if count > 0:
                stage_lst.append("TRUE")
            else:
                stage_lst.append("FALSE")
        except KeyError:
            stage_lst.append("No installed packages key available")

        # Checking for openshift packages
        try:
            count = 0
            for pkg in entries['system_profile']['installed_packages']:
                if "openshift" in pkg:
                    count = count + 1
            if count > 0:
                stage_lst.append("TRUE")
            else:
                stage_lst.append("FALSE")
        except KeyError:
            stage_lst.append("No installed packages key available")

        # Checking the hypervisor that this guest belongs
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No facts")
            stage_lst.append("No facts")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                if source['namespace'] == "satellite":
                    try:
                        if source['facts']['virtual_host_name']:
                            stage_lst.append(source['facts']['virtual_host_name'])
                            stage_lst.append(source['facts']['satellite_instance_id'])
                            count = count + 1
                    except KeyError:
                        # count = count + 1
                        ...

            if count == 0:
                stage_lst.append("No hypervisor fqdn")
                stage_lst.append("No hypervisor uuid")

        report_list.append(stage_lst)
        stage_lst = []

    with open(INVENTORY_FILE, "w") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(INVENTORY_FILE))


def csv_report_swatch(json_obj):
    """
    Function to generate the CSV report for swatch
    """

# echo "display_name,hardware_type,inventory_id,insights_id,is_hypervisor,number_of_guests,is_unmapped_guest,last_seen,measurement_type,sockets,cores,subscription_manager_id,cloud_provider" >/tmp/swatch_report.csv
# ./crhc swatch list_all | jq -r '.data[] | .display_name + "," + .hardware_type + "," + .inventory_id + "," + (.insights_id|tostring) + "," + (.is_hypervisor|tostring) + "," + (.number_of_guests|tostring) + "," + (.is_unmapped_guest|tostring) + "," + .last_seen + "," + .measurement_type + "," + (.sockets|tostring) + "," + (.cores|tostring) + "," + .subscription_manager_id + "," + .cloud_provider' >>/tmp/swatch_report.csv
    report_list = []

    stage_lst = ["display_name",
                 "hardware_type",
                 "inventory_id",
                 "insights_id",
                 "is_hypervisor",
                 "number_of_guests",
                 "is_unmapped_guest",
                 "last_seen",
                 "measurement_type",
                 "sockets",
                 "cores",
                 "subscription_manager_id",
                 "cloud_provider"]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj['data']:
        pass

        try:
            stage_lst.append(entries['display_name'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['hardware_type'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['inventory_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['insights_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['is_hypervisor'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['number_of_guests'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['is_unmapped_guest'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['last_seen'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['measurement_type'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['sockets'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['cores'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['subscription_manager_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries['cloud_provider'])
        except KeyError:
            stage_lst.append("Not available")

        report_list.append(stage_lst)
        stage_lst = []

    with open(SWATCH_FILE, "w") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(SWATCH_FILE))


def csv_match_report(match_obj):
    # print("here")

    report_list = []
    installed_product_lst = []

    stage_lst = ["id",
                   "updated",
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
                   "rhel_machine_id",
                   "tuned_profile",
                   "sap_system",
                   "sap_version",
                   "syspurpose_sla",
                   "installed_product",
                   "has_satellite_package",
                   "has_openshift_package",
                   "hypervisor_fqdn",
                   "hypervisor_uuid",
                   "sw_display_name",
                   "sw_hardware_type",
                   "sw_inventory_id",
                   "sw_insights_id",
                   "sw_is_hypervisor",
                   "sw_number_of_guests",
                   "sw_is_unmapped_guest",
                   "sw_last_seen",
                   "sw_measurement_type",
                   "sw_sockets",
                   "sw_cores",
                   "sw_subscription_manager_id",
                   "sw_cloud_provider"]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in match_obj:
        pass
        try:
            stage_lst.append(entries[0]['server']['id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['updated'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['fqdn'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['display_name'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['ansible_host'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['cpu_model'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['number_of_cpus'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['number_of_sockets'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['core_socket'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['system_memory_bytes'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['bios_vendor'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['bios_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['bios_release_date'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['os_release'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['os_kernel_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['arch'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['last_boot_time'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['infrastructure_type'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['infrastructure_vendor'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['insights_client_version'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['created'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['insights_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['reporter'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['server']['rhel_machine_id'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['tuned_profile'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['sap_system'])
        except KeyError:
            stage_lst.append("Not available")

        try:
            stage_lst.append(entries[0]['system_profile']['sap_version'])
        except KeyError:
            stage_lst.append("Not available")

        # Checking for syspurpose_sla information that came via fact
        if len(entries[0]['server']['facts']) == 0:
            stage_lst.append("Not available")
        elif len(entries[0]['server']['facts']) > 0:
            count = 0
            for source in entries[0]['server']['facts']:
                try:
                    if source['facts']['SYSPURPOSE_SLA']:
                        stage_lst.append(source['facts']['SYSPURPOSE_SLA'])
                except KeyError:
                    count = count + 1

            if count != 0:
                stage_lst.append("Not available")

        # Checking for installed products
        if (entries[0]['server']['reporter'] == "puptoo") or (entries[0]['server']['reporter'] == "yupana"):
            try:
                if len(entries[0]['system_profile']['installed_products']) > 0:
                    for ids in entries[0]['system_profile']['installed_products']:
                        installed_product_lst.append(ids['id'])

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No installed product key available")

        elif entries[0]['server']['reporter'] == "rhsm-conduit":
            try:
                if len(entries[0]['server']['facts'][0]['facts']['RH_PROD']) > 0:
                    for ids in entries[0]['server']['facts'][0]['facts']['RH_PROD']:
                        installed_product_lst.append(ids)

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No installed product key available")

        # Checking for satellite packages
        try:
            count = 0
            for pkg in entries[0]['system_profile']['installed_packages']:
                if "satellite" in pkg:
                    count = count + 1
            if count > 0:
                stage_lst.append("TRUE")
            else:
                stage_lst.append("FALSE")
        except KeyError:
            stage_lst.append("No installed packages key available")

        # Checking for openshift packages
        try:
            count = 0
            for pkg in entries[0]['system_profile']['installed_packages']:
                if "openshift" in pkg:
                    count = count + 1
            if count > 0:
                stage_lst.append("TRUE")
            else:
                stage_lst.append("FALSE")
        except KeyError:
            stage_lst.append("No installed packages key available")

        # Checking the hypervisor that this guest belongs
        if len(entries[0]['server']['facts']) == 0:
            stage_lst.append("No facts")
            stage_lst.append("No facts")
        elif len(entries[0]['server']['facts']) > 0:
            count = 0
            for source in entries[0]['server']['facts']:
                if source['namespace'] == "satellite":
                    try:
                        if source['facts']['virtual_host_name']:
                            stage_lst.append(source['facts']['virtual_host_name'])
                            stage_lst.append(source['facts']['satellite_instance_id'])
                            count = count + 1
                    except KeyError:
                        # count = count + 1
                        ...

            if count == 0:
                stage_lst.append("No hypervisor fqdn")
                stage_lst.append("No hypervisor uuid")

        if entries[1] == "not in swatch":
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
            stage_lst.append("Not in sw")
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
                stage_lst.append(entries[1]['display_name'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['hardware_type'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['inventory_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['insights_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['is_hypervisor'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['number_of_guests'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['is_unmapped_guest'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['last_seen'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['measurement_type'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['sockets'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['cores'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['subscription_manager_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(entries[1]['cloud_provider'])
            except KeyError:
                stage_lst.append("Not in sw")

        report_list.append(stage_lst)
        stage_lst = []

    with open(MATCH_FILE, "w") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(MATCH_FILE))
