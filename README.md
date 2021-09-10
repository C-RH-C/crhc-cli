# C.RH.C API Command Line Tool

This project contains the `crhc` command line tool that simplifies the use of the C.RH.C API available at `console.redhat.com`

---

**Disclaimer**: This project or the binary files available in the `Releases` area are `NOT` delivered and/or released by Red Hat. This is an independent project to help customers and Red Hat Support team to collect the data from `console.redhat.com` for reporting or troubleshooting purposes.

---

## Table of Content
 - [link](#Binary_File) - You can download the binary file
 - [link](#Source_Code) - You can clone the repository and use from the source code
 - [link](#Usage) - Usage
 - [link](#Contribution) - Contribution
 
---

## Binary_File
Please, access the release page [here](https://github.com/C-RH-C/crhc-cli/releases/latest) and check the version that you would like to use.

If for any reason the binary didn't run properly in your machine also with python3.6, as below example, probably you are using a bit old version of 3.6. In this case, you can create the virtual environment following the steps below, and generate a new binary file that will be 100% compatible with your current python version.
```
$ ./crhc 
[9554] Error loading Python lib '/tmp/_MEIWS0hNs/libpython3.6m.so.1.0': dlopen: /lib64/libm.so.6: version `GLIBC_2.29' not found (required by /tmp/_MEIWS0hNs/libpython3.6m.so.1.0)
```

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
  inventory
  swatch
  endpoint
  get

  login
  logout
  token
  whoami

Flags:
  -h, --help                         help for crhc

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

Or if you would like to do a similar process using the `jq` parser, you can copy/paste the commands below.
```
$ echo "id,updated,fqdn,display_name,ansible_host,cpu_model,number_of_cpus,number_of_sockets,core_socket,system_memory_bytes,bios_vendor,bios_version,bios_release_date,os_release,os_kernel_version,arch,last_boot_time,infrastructure_type,infrastructure_vendor,insights_client_version,created,insights_id,reporter,rhel_machine_id,tuned_profile,sap_system,sap_version" >/tmp/inventory_report.csv

$ ./crhc inventory list_all | jq .results[] | jq -r '.server.id + "," + .server.updated + "," + .server.fqdn + "," + .server.display_name + "," + .server.ansible_host + ",\"" + .system_profile.cpu_model + "\"," + (.system_profile.number_of_cpus|tostring) + "," + (.system_profile.number_of_sockets|tostring) + "," + (.system_profile.core_socket|tostring) + "," + (.system_profile.system_memory_bytes|tostring) + ",\"" + .system_profile.bios_vendor + "\"," + .system_profile.bios_version + "," + .system_profile.bios_release_date + "," + .system_profile.os_release + "," + .system_profile.os_kernel_version + "," + .system_profile.arch + "," + .system_profile.last_boot_time + "," + .system_profile.infrastructure_type + "," + .system_profile.infrastructure_vendor + "," + .system_profile.insights_client_version + "," + .server.created + "," + .server.insights_id + "," + .server.reporter + "," + .server.rhel_machine_id + "," + .system_profile.tuned_profile + "," + (.system_profile.sap_system|tostring) + "," + .system_profile.sap_version' >>/tmp/inventory_report.csv
```
This should be enough to export the data and create the file `/tmp/inventory_report.csv` with some Inventory information. In a sequence you can see the fields
- id
- updated
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


### Exporting Subscription Watch data to CSV
**Easy and Simple Way?**
```
$ ./crhc swatch list_all --csv
```

Or if you would like to do a similar process using the `jq` parser, you can copy/paste the commands below.
```
$ echo "display_name,hardware_type,inventory_id,insights_id,is_hypervisor,number_of_guests,is_unmapped_guest,last_seen,measurement_type,sockets,cores,subscription_manager_id,cloud_provider" >/tmp/swatch_report.csv

$ ./crhc swatch list_all | jq -r '.data[] | .display_name + "," + .hardware_type + "," + .inventory_id + "," + (.insights_id|tostring) + "," + (.is_hypervisor|tostring) + "," + (.number_of_guests|tostring) + "," + (.is_unmapped_guest|tostring) + "," + .last_seen + "," + .measurement_type + "," + (.sockets|tostring) + "," + (.cores|tostring) + "," + .subscription_manager_id + "," + .cloud_provider' >>/tmp/swatch_report.csv
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
## Contribution

I really hope this helps you.

If you need anything else of if you are facing issues trying to use it, please let me know via email or feel free to open a repository issue [here](https://github.com/C-RH-C/crhc-cli/issues)

waldirio@redhat.com / waldirio@gmail.com
