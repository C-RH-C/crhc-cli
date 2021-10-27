Usage
=====

The main idea of this script is to collect the information from console.redhat.com in order to generate some reports and/or proceed with some troubleshooting. That said, we can:

* ``crhc inventory list`` - To list the first 50 entries of your RHEL Inventory
* ``crhc inventory list_all`` - To list all the entries of your RHEL Inventory
* ``crhc inventory --display_name`` - To search in RHEL Inventory by display_name
* ``crhc inventory list --csv`` - To generate the output in csv file. A new file /tmp/inventory_report.csv will be created.
* ``crhc inventory list_all --csv`` - To generate the output in csv file. A new file /tmp/inventory_report.csv will be created.
* ``crhc inventory --display_name <short name or fqdn> --csv`` - To generate the output in csv file. A new file /tmp/inventory_report.csv will be created.
* ``crhc swatch list`` - To list the first 100 entries of your Subscription Watch Inventory
* ``crhc swatch list_all`` - To list all the entries of your Subscription Watch Inventory
* ``crhc swatch list --csv`` - To generate the output in csv file. A new file /tmp/swatch_report.csv will be created.
* ``crhc swatch list_all --csv`` - To generate the output in csv file. A new file /tmp/swatch_report.csv will be created.
* ``crhc swatch socket_summary`` - To list a summary of sockets based on your Subscription Watch Inventory
* ``crhc endpoint list`` - To list all the available API endpoints on console.redhat.com
* ``crhc get <API ENDPOINT>`` - Here you should be able to query the API endpoint directly
* ``crhc login --token <user api token here>`` - The way to inform the token that you can obtain from https://console.redhat.com/openshift/token
* ``crhc logout`` - Used to cleanup the local conf file, removing all the token information
* ``crhc token`` - This will print the access_token. This can be used with curl, for example.
* ``crhc whoami`` - This option will show some information regarding to the user who requested the token
* ``crhc {--version|-v}`` - This option will present the app version
* ``crhc ts dump`` - Export the whole Inventory and Subscription information in json format. 2 files will be created.
* ``crhc ts match`` - If the files mentioned above are not around, this feature will call the dump and after that will check both files and will create the 3rd one with the whole information correlated accordingly.
* ``crhc ts clean`` - This will cleanup all the temporary/cache files.
* ``crhc --version`` - It will print out the current version of crhc.

Note. All of them will generate the output in a JSON format, so you can use the output as input for any of your own script or also to ``jq`` command.
