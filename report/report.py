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
                   "system_purpose_sla",
                   "system_purpose_role",
                   "system_purpose_usage",
                   "is_simple_content_access",
                   "installed_product",
                   "has_satellite_package",
                   "has_openshift_package",
                   "hypervisor_fqdn",
                   "hypervisor_uuid",
                   "number_of_guests"]

    report_list.append(stage_lst)
    stage_lst = []

    for entries in json_obj['results']:
        pass
        try:
            stage_lst.append(entries['server']['id'])
        except KeyError:
            stage_lst.append("No_id_key_available")

        try:
            stage_lst.append(entries['server']['updated'])
        except KeyError:
            stage_lst.append("No_updated_key_available")

        try:
            stage_lst.append(entries['server']['fqdn'])
        except KeyError:
            stage_lst.append("No_fqdn_key_available")

        try:
            stage_lst.append(entries['server']['display_name'])
        except KeyError:
            stage_lst.append("No_display_name_key_available")

        try:
            stage_lst.append(entries['server']['ansible_host'])
        except KeyError:
            stage_lst.append("No_ansible_host_key_available")

        try:
            stage_lst.append(entries['system_profile']['cpu_model'])
        except KeyError:
            stage_lst.append("No_cpu_model_key_available")

        try:
            stage_lst.append(entries['system_profile']['number_of_cpus'])
        except KeyError:
            stage_lst.append("No_number_of_cpus_key_available")

        try:
            stage_lst.append(entries['system_profile']['number_of_sockets'])
        except KeyError:
            stage_lst.append("No_number_of_sockets_key_available")

        try:
            stage_lst.append(entries['system_profile']['core_socket'])
        except KeyError:
            stage_lst.append("No_core_socket_available")

        try:
            stage_lst.append(entries['system_profile']['system_memory_bytes'])
        except KeyError:
            stage_lst.append("No_system_memory_bytes_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_vendor'])
        except KeyError:
            stage_lst.append("No_bios_vendor_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_version'])
        except KeyError:
            stage_lst.append("No_bios_version_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_release_date'])
        except KeyError:
            stage_lst.append("No_bios_release_date_key_available")

        try:
            stage_lst.append(entries['system_profile']['os_release'])
        except KeyError:
            stage_lst.append("No_os_release_key_available")

        try:
            stage_lst.append(entries['system_profile']['os_kernel_version'])
        except KeyError:
            stage_lst.append("No_os_kernel_version_key_available")

        try:
            stage_lst.append(entries['system_profile']['arch'])
        except KeyError:
            stage_lst.append("No_arch_key_available")

        try:
            stage_lst.append(entries['system_profile']['last_boot_time'])
        except KeyError:
            stage_lst.append("No_last_boot_time_key_available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_type'])
        except KeyError:
            stage_lst.append("No_infrastructure_type_key_available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_vendor'])
        except KeyError:
            stage_lst.append("No_infrastructure_vendor_key_available")

        try:
            stage_lst.append(entries['system_profile']['insights_client_version'])
        except KeyError:
            stage_lst.append("No_insights_client_version_key_available")

        try:
            stage_lst.append(entries['server']['created'])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries['server']['insights_id'])
        except KeyError:
            stage_lst.append("No_insights_id_key_available")

        try:
            stage_lst.append(entries['server']['reporter'])
        except KeyError:
            stage_lst.append("No_reporter_key_available")

        try:
            stage_lst.append(entries['server']['rhel_machine_id'])
        except KeyError:
            stage_lst.append("No_rhel_machine_id_key_available")

        try:
            stage_lst.append(entries['system_profile']['tuned_profile'])
        except KeyError:
            stage_lst.append("No_tuned_profile_key_available")

        try:
            stage_lst.append(entries['system_profile']['sap_system'])
        except KeyError:
            stage_lst.append("No_sap_system_key_available")

        try:
            stage_lst.append(entries['system_profile']['sap_version'])
        except KeyError:
            stage_lst.append("No_sap_version_key_available")


        # Checking for syspurpose_sla information that came via fact
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['SYSPURPOSE_SLA']:
                        stage_lst.append(source['facts']['SYSPURPOSE_SLA'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_syspurpose_sla_key_available")

        # Checking for system_purpose_role
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['system_purpose_role']:
                        stage_lst.append(source['facts']['system_purpose_role'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_system_purpose_role_key_available")

        # Checking for system_purpose_usage
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['system_purpose_usage']:
                        stage_lst.append(source['facts']['system_purpose_usage'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_system_purpose_usage_key_available")

        # Checking for is_simple_content_access
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['is_simple_content_access']:
                        stage_lst.append(source['facts']['is_simple_content_access'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_is_simple_content_access_key_available")

        # Checking for installed products
        if (entries['server']['reporter'] == "puptoo") or (entries['server']['reporter'] == "yupana"):
            try:
                if len(entries['system_profile']['installed_products']) > 0:
                    for ids in entries['system_profile']['installed_products']:
                        installed_product_lst.append(ids['id'])

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No_installed_products_key_available")

        elif entries['server']['reporter'] == "rhsm-conduit":
            try:
                if len(entries['server']['facts'][0]['facts']['RH_PROD']) > 0:
                    for ids in entries['server']['facts'][0]['facts']['RH_PROD']:
                        installed_product_lst.append(ids)

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
                elif len(entries['server']['facts'][0]['facts']['RH_PROD']) == 0:
                    stage_lst.append("No_installed_products_key_available")
            except KeyError:
                stage_lst.append("No_installed_products_key_available")
        else:
            stage_lst.append("reporter {}".format(entries['server']['reporter']))

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
            stage_lst.append("No_installed_packages_key_available")

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
            stage_lst.append("No_installed_packages_key_available")

        # Checking the hypervisor that this guest belongs
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
            stage_lst.append("No_facts_key_available")
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
                if source['namespace'] == "rhsm":
                    try:
                        if source['facts']['VM_HOST']:
                            stage_lst.append(source['facts']['VM_HOST'])
                            stage_lst.append(source['facts']['VM_HOST_UUID'])
                            count = count + 1
                    except KeyError:
                        ...

            if count == 0:
                stage_lst.append("No_hypervisor_fqdn")
                stage_lst.append("No_hypervisor_uuid")
        
        # Counting the number of guests on top of the hypervisor
        number_of_guests = 0
        for each_server in json_obj['results']:
            if len(each_server['server']['facts']) > 0:
                for elements in each_server['server']['facts']:

                    if elements['namespace'] == "satellite":
                        try:
                            if elements['facts']['virtual_host_name']:
                                if elements['facts']['virtual_host_uuid'] == entries['server']['satellite_id']:
                                    number_of_guests = number_of_guests + 1
                        except KeyError:
                            ...

                    if elements['namespace'] == "rhsm":
                        try:
                            if elements['facts']['VM_HOST']:
                                if elements['facts']['VM_HOST_UUID'] == entries['server']['subscription_manager_id']:
                                    number_of_guests = number_of_guests + 1
                        except KeyError:
                            ...

        if number_of_guests == 0:
            stage_lst.append("No guests")
        else:
            stage_lst.append(number_of_guests)


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
                   "system_purpose_sla",
                   "system_purpose_role",
                   "system_purpose_usage",
                   "is_simple_content_access",
                   "installed_product",
                   "has_satellite_package",
                   "has_openshift_package",
                   "hypervisor_fqdn",
                   "hypervisor_uuid",
                   "number_of_guests",  # added
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

    for elements in match_obj:
        entries = elements[0]
        sw_entries = elements[1]
        pass
        try:
            stage_lst.append(entries['server']['id'])
        except KeyError:
            stage_lst.append("No_id_key_available")

        try:
            stage_lst.append(entries['server']['updated'])
        except KeyError:
            stage_lst.append("No_updated_key_available")

        try:
            stage_lst.append(entries['server']['fqdn'])
        except KeyError:
            stage_lst.append("No_fqdn_key_available")

        try:
            stage_lst.append(entries['server']['display_name'])
        except KeyError:
            stage_lst.append("No_display_name_key_available")

        try:
            stage_lst.append(entries['server']['ansible_host'])
        except KeyError:
            stage_lst.append("No_ansible_host_key_available")

        try:
            stage_lst.append(entries['system_profile']['cpu_model'])
        except KeyError:
            stage_lst.append("No_cpu_model_key_available")

        try:
            stage_lst.append(entries['system_profile']['number_of_cpus'])
        except KeyError:
            stage_lst.append("No_number_of_cpus_key_available")

        try:
            stage_lst.append(entries['system_profile']['number_of_sockets'])
        except KeyError:
            stage_lst.append("No_number_of_sockets_key_available")

        try:
            stage_lst.append(entries['system_profile']['core_socket'])
        except KeyError:
            stage_lst.append("No_core_socket_available")

        try:
            stage_lst.append(entries['system_profile']['system_memory_bytes'])
        except KeyError:
            stage_lst.append("No_system_memory_bytes_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_vendor'])
        except KeyError:
            stage_lst.append("No_bios_vendor_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_version'])
        except KeyError:
            stage_lst.append("No_bios_version_key_available")

        try:
            stage_lst.append(entries['system_profile']['bios_release_date'])
        except KeyError:
            stage_lst.append("No_bios_release_date_key_available")

        try:
            stage_lst.append(entries['system_profile']['os_release'])
        except KeyError:
            stage_lst.append("No_os_release_key_available")

        try:
            stage_lst.append(entries['system_profile']['os_kernel_version'])
        except KeyError:
            stage_lst.append("No_os_kernel_version_key_available")

        try:
            stage_lst.append(entries['system_profile']['arch'])
        except KeyError:
            stage_lst.append("No_arch_key_available")

        try:
            stage_lst.append(entries['system_profile']['last_boot_time'])
        except KeyError:
            stage_lst.append("No_last_boot_time_key_available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_type'])
        except KeyError:
            stage_lst.append("No_infrastructure_type_key_available")

        try:
            stage_lst.append(entries['system_profile']['infrastructure_vendor'])
        except KeyError:
            stage_lst.append("No_infrastructure_vendor_key_available")

        try:
            stage_lst.append(entries['system_profile']['insights_client_version'])
        except KeyError:
            stage_lst.append("No_insights_client_version_key_available")

        try:
            stage_lst.append(entries['server']['created'])
        except KeyError:
            stage_lst.append("No_created_key_available")

        try:
            stage_lst.append(entries['server']['insights_id'])
        except KeyError:
            stage_lst.append("No_insights_id_key_available")

        try:
            stage_lst.append(entries['server']['reporter'])
        except KeyError:
            stage_lst.append("No_reporter_key_available")

        try:
            stage_lst.append(entries['server']['rhel_machine_id'])
        except KeyError:
            stage_lst.append("No_rhel_machine_id_key_available")

        try:
            stage_lst.append(entries['system_profile']['tuned_profile'])
        except KeyError:
            stage_lst.append("No_tuned_profile_key_available")

        try:
            stage_lst.append(entries['system_profile']['sap_system'])
        except KeyError:
            stage_lst.append("No_sap_system_key_available")

        try:
            stage_lst.append(entries['system_profile']['sap_version'])
        except KeyError:
            stage_lst.append("No_sap_version_key_available")
        
        # Checking for syspurpose_sla information that came via fact
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['SYSPURPOSE_SLA']:
                        stage_lst.append(source['facts']['SYSPURPOSE_SLA'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_syspurpose_sla_key_available")

        # Checking for system_purpose_role
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['system_purpose_role']:
                        stage_lst.append(source['facts']['system_purpose_role'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_system_purpose_role_key_available")

        # Checking for system_purpose_usage
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['system_purpose_usage']:
                        stage_lst.append(source['facts']['system_purpose_usage'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_system_purpose_usage_key_available")

        # Checking for is_simple_content_access
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
        elif len(entries['server']['facts']) > 0:
            count = 0
            for source in entries['server']['facts']:
                try:
                    if source['facts']['is_simple_content_access']:
                        stage_lst.append(source['facts']['is_simple_content_access'])
                        count = 1
                except KeyError:
                    ...

            if count == 0:
                stage_lst.append("No_is_simple_content_access_key_available")

        # Checking for installed products
        if (entries['server']['reporter'] == "puptoo") or (entries['server']['reporter'] == "yupana"):
            try:
                if len(entries['system_profile']['installed_products']) > 0:
                    for ids in entries['system_profile']['installed_products']:
                        installed_product_lst.append(ids['id'])

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
            except KeyError:
                stage_lst.append("No_installed_products_key_available")

        elif entries['server']['reporter'] == "rhsm-conduit":
            try:
                if len(entries['server']['facts'][0]['facts']['RH_PROD']) > 0:
                    for ids in entries['server']['facts'][0]['facts']['RH_PROD']:
                        installed_product_lst.append(ids)

                    stage_lst.append(installed_product_lst)
                    installed_product_lst = []
                elif len(entries['server']['facts'][0]['facts']['RH_PROD']) == 0:
                    stage_lst.append("No_installed_products_key_available")
            except KeyError:
                stage_lst.append("No_installed_products_key_available")
        else:
            stage_lst.append("reporter {}".format(entries['server']['reporter']))

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
            stage_lst.append("No_installed_packages_key_available")

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
            stage_lst.append("No_installed_packages_key_available")

        # Checking the hypervisor that this guest belongs
        if len(entries['server']['facts']) == 0:
            stage_lst.append("No_facts_key_available")
            stage_lst.append("No_facts_key_available")
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
                if source['namespace'] == "rhsm":
                    try:
                        if source['facts']['VM_HOST']:
                            stage_lst.append(source['facts']['VM_HOST'])
                            stage_lst.append(source['facts']['VM_HOST_UUID'])
                            count = count + 1
                    except KeyError:
                        ...

            if count == 0:
                stage_lst.append("No_hypervisor_fqdn")
                stage_lst.append("No_hypervisor_uuid")
        
        # Counting the number of guests on top of the hypervisor
        number_of_guests = 0
        for each_server in match_obj:
            if len(each_server[0]['server']['facts']) > 0:
                for elements in each_server[0]['server']['facts']:

                    if elements['namespace'] == "satellite":
                        try:
                            if elements['facts']['virtual_host_name']:
                                if elements['facts']['virtual_host_uuid'] == entries['server']['satellite_id']:
                                    number_of_guests = number_of_guests + 1
                        except KeyError:
                            ...

                    if elements['namespace'] == "rhsm":
                        try:
                            if elements['facts']['VM_HOST']:
                                if elements['facts']['VM_HOST_UUID'] == entries['server']['subscription_manager_id']:
                                    number_of_guests = number_of_guests + 1
                        except KeyError:
                            ...

        if number_of_guests == 0:
            stage_lst.append("No guests")
        else:
            stage_lst.append(number_of_guests)


        if sw_entries == "not in swatch":
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
                stage_lst.append(sw_entries['display_name'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['hardware_type'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['inventory_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['insights_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['is_hypervisor'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['number_of_guests'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['is_unmapped_guest'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['last_seen'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['measurement_type'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['sockets'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['cores'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['subscription_manager_id'])
            except KeyError:
                stage_lst.append("Not in sw")

            try:
                stage_lst.append(sw_entries['cloud_provider'])
            except KeyError:
                stage_lst.append("Not in sw")

        report_list.append(stage_lst)
        stage_lst = []

    with open(MATCH_FILE, "w") as file_obj:
        writer = csv.writer(file_obj)
        writer.writerows(report_list)

    print("File {} created".format(MATCH_FILE))
