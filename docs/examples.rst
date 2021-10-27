Some Examples
=============

**Subscriptions Socket Summary**

.. code-block:: sh

    $ ./crhc swatch socket_summary
    Public Cloud ........: 14
    Virtualized RHEL ....: 2968
    Physical RHEL .......: 1306
    Hypervisors .........: 154
    ----------------------
    Total # of Sockets ..: 4444

**API Queries**

Querying the API, we can first check the available API endpoints using the command below

.. code-block:: sh

    $ ./crhc endpoint list
    {
        "services": [
            "/api/aiops-clustering",
            "/api/aiops-idle-cost-savings",
    ...
            "/api/inventory",
    ...
            "/api/rhsm",
            "/api/rhsm-subscriptions",
            "/api/ros",
            "/api/sources",
            "/api/subscriptions",
            "/api/system-baseline",
            "/api/topological-inventory",
            "/api/tower-analytics",
            "/api/upload",
    ...
        ]
    }

In a sequence, we can check the API endpoint using the ``get`` option

.. code-block:: sh

    $ ./crhc.py get /api/inventory
    /api/inventory/v1/hosts
    /api/inventory/v1/hosts/checkin
    /api/inventory/v1/hosts/{host_id_list}
    /api/inventory/v1/hosts/{host_id_list}/facts/{namespace}
    /api/inventory/v1/hosts/{host_id_list}/system_profile
    /api/inventory/v1/hosts/{host_id_list}/tags
    /api/inventory/v1/hosts/{host_id_list}/tags/count
    /api/inventory/v1/system_profile/sap_sids
    /api/inventory/v1/system_profile/sap_system
    /api/inventory/v1/system_profile/validate_schema
    /api/inventory/v1/tags

And after that, we can see all the available methods. From now, we can call them directly, for example

.. code-block:: sh

    $ ./crhc.py get /api/inventory/v1/hosts
    {
        "total": 6221,
        "count": 50,
        "page": 1,
        "per_page": 50,
        "results": [
            {
                "insights_id": "1f959a58-9e13-4d60-8cef-33a452d2303b",
                "rhel_machine_id": null,
                ...

**Using the token with the curl command**

.. code-block:: sh

    $ curl -s -H "Authorization: Bearer $(./crhc token)" https://api.openshift.com/api/accounts_mgmt/v1/current_account | json_reformat

**Exporting Inventory data to CSV**

.. code-block:: sh

    $ ./crhc inventory list_all --csv

This should be enough to export the data and create the file ``/tmp/inventory_report.csv`` with some Inventory information. In a sequence you can see the fields


* id
* created
* updated
* stale_timestamp
* stale_warning_timestamp
* culled_timestamp
* fqdn
* display_name
* ansible_host
* cpu_model
* number_of_cpus
* number_of_sockets
* core_socket
* system_memory_bytes
* bios_vendor
* bios_version
* bios_release_date
* os_release
* os_kernel_version
* arch
* last_boot_time
* infrastructure_type
* infrastructure_vendor
* insights_client_version
* created
* insights_id
* reporter
* rhel_machine_id
* tuned_profile
* sap_system
* sap_version
* system_purpose_sla
* system_purpose_role
* system_purpose_usage
* is_simple_content_access
* installed_product
* has_satellite_package
* has_openshift_package
* hypervisor_fqdn
* hypervisor_uuid
* number_of_guests


**Exporting Subscription Watch data to CSV**

.. code-block:: sh

    $ ./crhc swatch list_all --csv


This should be enough to export the data and create the file ``/tmp/swatch_report.csv`` with the whole Subscription Watch information. In a sequence you can see the fields


* display_name
* hardware_type
* inventory_id
* insights_id
* is_hypervisor
* number_of_guests
* is_unmapped_guest
* last_seen
* measurement_type
* sockets
* cores
* subscription_manager_id
* cloud_provider


**Analysing the Customer Data**

Please, copy the files sent by the customer according to below. Let's assume the customer sent two files ``inventory.json`` and ``swatch.json``, once you received them, let's execute the commands below

.. code-block:: sh

    $ cp full_inventory.json /tmp/inventory.json
    $ cp full_swatch.json /tmp/swatch.json


After that, you can execute the command ``crhc ts match`` and the output will be as below

.. code-block:: sh

    $ ./crhc ts match
    File /tmp/inventory.json already in place, using it.
    File /tmp/swatch.json already in place, using it.
    File /tmp/match_inv_sw.csv created


Note. Once the files ``/tmp/inventory.json`` and ``/tmp/swatch.json`` are in place, they will be used for this analysis and as result, the file /tmp/match_inv_sw.csv will be created. This is the file that will be used for troubleshooting process.


**ATTENTION**

This is an awesome report because will combine both information from Inventory and Subscriptions in a single dataset. The final result will be the file ``/tmp/match_inv_sw.csv`` with the respective fields.

* id
* created
* updated
* stale_timestamp
* stale_warning_timestamp
* culled_timestamp
* fqdn
* display_name
* ansible_host
* cpu_model
* number_of_cpus
* number_of_sockets
* core_socket
* system_memory_bytes
* bios_vendor
* bios_version
* bios_release_date
* os_release
* os_kernel_version
* arch
* last_boot_time
* infrastructure_type
* infrastructure_vendor
* insights_client_version
* created
* insights_id
* reporter
* rhel_machine_id
* tuned_profile
* sap_system
* sap_version
* system_purpose_sla
* system_purpose_role
* system_purpose_usage
* is_simple_content_access
* installed_product
* has_satellite_package
* has_openshift_package
* hypervisor_fqdn
* hypervisor_uuid
* number_of_guests
* display_name
* hardware_type
* inventory_id
* insights_id
* is_hypervisor
* number_of_guests
* is_unmapped_guest
* last_seen
* measurement_type
* sockets
* cores
* subscription_manager_id
* cloud_provider

