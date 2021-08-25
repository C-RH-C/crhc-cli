# C.RH.C API Command Line Tool

This project contains the `crhc` command line tool that simplifies the use of the C.RH.C API available at `console.redhat.com`

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

  user

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

- `crhc user set` - To set the credentials that will be used to authenticate on console.redhat.com
- `crhc inventory list` - To list the first 50 entries of your RHEL Inventory
- `crhc inventory list_all` - To list all the entries of your RHEL Inventory
- `crhc inventory --display_name` - To search in RHEL Inventory by `display_name`
- `crhc swatch list` - To list the first 100 entries of your Subscription Watch Inventory
- `crhc swatch list_all` - To list all the entries of your Subscription Watch Inventory
- `crhc swatch socket_summary` - To list a summary of sockets based on your Subscription Watch Inventory
- `crhc endpoint list` - To list all the available API endpoints on `console.redhat.com`
- `crhc get <API ENDPOINT>` - Here you should be able to query the API endpoint directly

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

---

### Exporting Inventory data to CSV
If you would like to export the Inventory data to a `CSV` file, follow the steps below
```
$ echo "account,ansible_host,bios_uuid,created,culled_timestamp,display_name,external_id,fqdn,id,insights_id,provider_id,provider_type,reporter,rhel_machine_id,satellite_id,stale_timestamp,stale_warning_timestamp,subscription_manager_id,updated" >/tmp/inventory_report.csv

$ ./crhc inventory list_all | jq -r '.results[] | .account + "," + .ansible_host + "," + .bios_uuid + "," + .created + "," + .culled_timestamp + "," + .display_name + "," + .external_id + "," + .fqdn + "," + .id + "," + .insights_id + "," + .provider_id + "," + .provider_type + "," + .reporter + "," + .rhel_machine_id + "," + .satellite_id + "," + .stale_timestamp + "," + .stale_warning_timestamp + "," + .subscription_manager_id + "," + .updated' >>/tmp/inventory_report.csv
```
This should be enough to export the data and create the file `/tmp/inventory_report.csv` with some Inventory information. In a sequence you can see the fields
- account
- ansible_host
- bios_uuid
- created
- culled_timestamp
- display_name
- external_id
- fqdn
- id
- insights_id
- provider_id
- provider_type
- reporter
- rhel_machine_id
- satellite_id
- stale_timestamp
- stale_warning_timestamp
- subscription_manager_id
- updated

Note. The Inventory report will be improved very soon, just to add some additional and important fields as `sockets` and `installed products`, for example.

### Exporting Subscription Watch data to CSV
If you would like to export the Subscription Watch to a `CSV` file, follow the steps below
```
$ echo "cores,display_name,hardware_type,inventory_id,is_hypervisor,is_unmapped_guest,last_seen,measurement_type,sockets,subscription_manager_id" >/tmp/swatch_report.csv

$ ./crhc swatch list_all | jq -r '.data[] | (.cores|tostring) + "," + .display_name + "," + .hardware_type + "," + .inventory_id + "," + (.is_hypervisor|tostring) + "," + (.is_unmapped_guest|tostring) + "," + .last_seen + "," + .measurement_type + "," + (.sockets|tostring) + "," + .subscription_manager_id' >>/tmp/swatch_report.csv
```
This should be enough to export the data and create the file `/tmp/swatch_report.csv` with the whole Subscription Watch information. In a sequence you can see the fields
- cores
- display_name
- hardware_type
- inventory_id
- is_hypervisor
- is_unmapped_guest
- last_seen
- measurement_type
- sockets
- subscription_manager_id

---
## Contribution

I really hope this helps you.

If you need anything else of if you are facing issues trying to use it, please let me know via email or feel free to open a repository issue [here](https://github.com/C-RH-C/crhc-cli/issues)

waldirio@redhat.com / waldirio@gmail.com
