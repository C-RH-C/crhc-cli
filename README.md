# C.RH.C API Command Line Tool

This project contains the `crhc` command line tool that simplifies the use of the C.RH.C API available at `console.redhat.com`

---

**Disclaimer**: This project or the binary files available in the `Releases` area are `NOT` delivered and/or released by Red Hat. This is an independent project to help customers and Red Hat Support team to collect the data from `console.redhat.com` for reporting or troubleshooting purposes.

---

## Table of Content
 - [link](#Binary_File) - You can download the binary file
 - [link](#Usage) - Usage
 - [link](#Proxy) - Proxy Configuration
 - [link](#Contribution) - Contribution
 - [link](#Source_Code) - You can clone the repository and use from the source code
---

## Binary_File
Please, access the release page [here](https://github.com/C-RH-C/crhc-cli/releases/latest) and check the version that you would like to use.

If for any reason the binary didn't run properly in your machine also with python3.6, as below example, probably you are using a bit old version of 3.6. In this case, you can create the virtual environment following the steps below, and generate a new binary file that will be 100% compatible with your current python version.
```
$ ./crhc 
[9554] Error loading Python lib '/tmp/_MEIWS0hNs/libpython3.6m.so.1.0': dlopen: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by /tmp/_MEIWS0hNs/libpython3.6m.so.1.0)
```
## Proxy
If you have proxy in your environment, it will be necessary to add this configuration in your terminal. In order to do that, you can proceed as below:

To check the current configuration
```
$ echo $http_proxy
```

To setup your proxy
```
$ export http_proxy=http://SERVER:PORT/
```
or
```
$ export http_proxy=http://USERNAME:PASSWORD@SERVER:PORT/
```

And if you would like to keep it permanent
```
# echo "export http_proxy=http://proxy.local.domain:3128/" > /etc/profile.d/http_proxy.sh
```

Note. Please, change the values according to your environment. After that, you should be good to go and use the `crhc` with no problems.

---
## Usage

The main idea of this script is to collect the information from `console.redhat.com` in order to generate some reports and/or proceed with some troubleshooting. That said, we can:

- `crhc inventory list` - To list the first 50 entries of your RHEL Inventory
- `crhc inventory list_all` - To list all the entries of your RHEL Inventory
- `crhc inventory --display_name` - To search in RHEL Inventory by `display_name`
- `crhc inventory list --csv` - To generate the output in csv file. A new file `/tmp/inventory_report.csv` will be created.
- `crhc inventory list_all --csv` - To generate the output in csv file. A new file `/tmp/inventory_report.csv` will be created.
- `crhc inventory --display_name <short name or fqdn> --csv` - To generate the output in csv file. A new file `/tmp/inventory_report.csv` will be created.
- `crhc swatch list` - To list the first 100 entries of your Subscription Watch Inventory
- `crhc swatch list_all` - To list all the entries of your Subscription Watch Inventory
- `crhc swatch list --csv` - To generate the output in csv file. A new file `/tmp/swatch_report.csv` will be created.
- `crhc swatch list_all --csv` - To generate the output in csv file. A new file `/tmp/swatch_report.csv` will be created.
- `crhc swatch socket_summary` - To list a summary of sockets based on your Subscription Watch Inventory
- `crhc endpoint list` - To list all the available API endpoints on `console.redhat.com`
- `crhc get <API ENDPOINT>` - Here you should be able to query the API endpoint directly
- `crhc login --token <user api token here>` - The way to inform the token that you can obtain from [https://console.redhat.com/openshift/token](https://console.redhat.com/openshift/token)
- `crhc logout` - Used to cleanup the local conf file, removing all the token information
- `crhc token` - This will print the access_token. This can be used with `curl`, for example.
- `crhc whoami` - This option will show some information regarding to the user who requested the token
- `crhc {--version|-v}` - This option will present the app version
- `crhc ts dump` - Export the whole Inventory and Subscription information in json format. 2 files will be created.
- `crhc ts match` - If the files mentioned above are not around, this feature will call the `dump` and after that will check both files and will create the 3rd one with the whole information correlated accordingly.
- `crhc ts clean` - This will cleanup all the temporary/cache files.
- `crhc --version` - It will print out the current version of `crhc`.

Note. All of them will generate the output in a `JSON` format, so you can use the output as input for any of your own script or also to `jq` command.

---

## Examples

### Subscriptions Socket Summary
```
$ ./crhc swatch socket_summary
Public Cloud ........: 14
Virtualized RHEL ....: 2968
Physical RHEL .......: 1306
Hypervisors .........: 154
----------------------
Total # of Sockets ..: 4444
```


### Querying the API, we can first check the available API endpoints using the command below
```
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
```

In a sequence, we can check the API endpoint using the `get` option
```
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
```
And after that, we can see all the available methods. From now, we can call them directly, for example
```
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
```

### Using the token with the curl command
```
$ curl -s -H "Authorization: Bearer $(./crhc token)" https://api.openshift.com/api/accounts_mgmt/v1/current_account | json_reformat
```


---

### Exporting Inventory data to CSV

**Easy and Simple Way?**
```
$ ./crhc inventory list_all --csv
```
This should be enough to export the data and create the file `/tmp/inventory_report.csv` with some Inventory information. In a sequence you can see the fields
- id
- created
- updated
- stale_timestamp
- stale_warning_timestamp
- culled_timestamp
- fqdn
- display_name
- ansible_host
- cpu_model
- number_of_cpus
- number_of_sockets
- core_socket
- system_memory_bytes
- bios_vendor
- bios_version
- bios_release_date
- os_release
- os_kernel_version
- arch
- last_boot_time
- infrastructure_type
- infrastructure_vendor
- insights_client_version
- created
- insights_id
- reporter
- rhel_machine_id
- tuned_profile
- sap_system
- sap_version
- system_purpose_sla
- system_purpose_role
- system_purpose_usage
- is_simple_content_access
- installed_product
- has_satellite_package
- has_openshift_package
- hypervisor_fqdn
- hypervisor_uuid
- number_of_guests


### Exporting Subscription Watch data to CSV
**Easy and Simple Way?**
```
$ ./crhc swatch list_all --csv
```
This should be enough to export the data and create the file `/tmp/swatch_report.csv` with the whole Subscription Watch information. In a sequence you can see the fields
- display_name
- hardware_type
- inventory_id
- insights_id
- is_hypervisor
- number_of_guests
- is_unmapped_guest
- last_seen
- measurement_type
- sockets
- cores
- subscription_manager_id
- cloud_provider

---
### Analysing the Customer Data
Please, copy the files sent by the customer according to below. Let's assume the customer sent two files `full_inventory.json` and `full_swatch.json`, once you received them, let's execute the commands below
```
$ cp full_inventory.json /tmp/inventory.json
$ cp full_swatch.json /tmp/swatch.json
```
After that, you can execute the command `crhc ts match` and the output will be as below
```
$ ./crhc ts match
File /tmp/inventory.json already in place, using it.
File /tmp/swatch.json already in place, using it.
File /tmp/match_inv_sw.csv created
```
Note. Once the files `/tmp/inventory.json` and `/tmp/swatch.json` are in place, they will be used for this analysis and as result, the file `/tmp/match_inv_sw.csv` will be created. This is the file that will be used for troubleshooting process.

## **ATTENTION**
This is an awesome report because will combine both information from Inventory and Subscriptions in a single dataset. The final result will be the file `/tmp/match_inv_sw.csv` with the respective fields.
- id
- created
- updated
- stale_timestamp
- stale_warning_timestamp
- culled_timestamp
- fqdn
- display_name
- ansible_host
- cpu_model
- number_of_cpus
- number_of_sockets
- core_socket
- system_memory_bytes
- bios_vendor
- bios_version
- bios_release_date
- os_release
- os_kernel_version
- arch
- last_boot_time
- infrastructure_type
- infrastructure_vendor
- insights_client_version
- created
- insights_id
- reporter
- rhel_machine_id
- tuned_profile
- sap_system
- sap_version
- system_purpose_sla
- system_purpose_role
- system_purpose_usage
- is_simple_content_access
- installed_product
- has_satellite_package
- has_openshift_package
- hypervisor_fqdn
- hypervisor_uuid
- number_of_guests
- display_name
- hardware_type
- inventory_id
- insights_id
- is_hypervisor
- number_of_guests
- is_unmapped_guest
- last_seen
- measurement_type
- sockets
- cores
- subscription_manager_id
- cloud_provider

---
### New Versions
Once a new version get available, the `crhc` will let you know.
```
...
Use "crhc [command] --help" for more information about a command.

Please, download the latests version from https://github.com/C-RH-C/crhc-cli/releases/latest
Current Version: 1.3.1
New Version: 1.3.2
```

You can safely download the latest version in the [link](https://github.com/C-RH-C/crhc-cli/releases/latest) and overwrite the current one. All the fix and new features will be already available.

Note. The current `token` configuration will still valid. It's not necessary to rerun the `token` process when updating the `crhc` version.

---
## Contribution

I really hope this helps you.

If you need anything else of if you are facing issues trying to use it, please let me know via email or feel free to open a repository issue [here](https://github.com/C-RH-C/crhc-cli/issues)

Also, if you believe this project is valuable for you, feel free to share your feedback via contacts below. This will help to push this project forward.

waldirio@redhat.com / waldirio@gmail.com

Thank you in advance! :)

---
## Source_Code
Please, proceed with the steps below

In your RHEL/CentOS/Fedora/etc with Python 3.x installed, let's execute the commands in a sequence
```
$ git clone https://github.com/C-RH-C/crhc-cli.git
$ cd crhc-cli
$ python3 -m venv ~/.virtualenv/crhc-cli
$ source ~/.virtualenv/crhc-cli/bin/activate
```

Now, you should be in your virtual environment. You can realize your prompt will change
```
(crhc-cli) [user@server crhc-cli]$
```

We can continue
```
(crhc-cli) [user@server crhc-cli]$ pip install --upgrade pip
(crhc-cli) [user@server crhc-cli]$ pip install -r requirements.txt
```

And finally, we are good to go.
```
(crhc-cli) [user@server crhc-cli]$ ./crhc.py
```

The menu will be as below
```
(crhc-cli) [user@server crhc-cli]$ ./crhc.py 
Command line tool for console.redhat.com API

Usage:
  crhc [command]

Available Commands:
  inventory      Get information about Inventory
  swatch         Get information about Subscriptions
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
```

Great, now it's time to generate the binary file, please, execute the step below yet in your virtual environment
```
(crhc-cli) [user@server crhc-cli]$ pyinstaller --onefile crhc.py
```

At the end of this process, the binary file will be available under the `dist` dir, then you can redistribute or copy to any other machine running the same python version and everything will be running with no issues.
```
(crhc-cli) [user@server crhc-cli]$  file dist/crhc 
dist/crhc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), BuildID[sha1]=f6af5bc244c001328c174a6abf855d682aa7401b, for GNU/Linux 2.6.32, stripped
```