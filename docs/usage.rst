Usage
=====

The main idea of this script is to collect the information from console.redhat.com in order to generate some reports and/or proceed with some troubleshooting. That said, we can:

.. list-table:: 
    :header-rows: 1

    * - Command
      - Description
    * - crhc inventory list
      - To list the first 50 entries of your Inventory
    * - crhc inventory list \-\-csv
      - To generate the output in csv file. A new file ``/tmp/inventory_report.csv`` will be created.
    * - crhc inventory list_all
      - To list the whole entries of your Inventory
    * - crhc inventory list_all \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/inventory_report.csv`` will be created.
    * - crhc inventory display_name <host_or_fqdn>
      - To search entries by ``display_name``
    * - crhc inventory display_name <host_or_fqdn> \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/inventory_report.csv`` will be created.
    * - crhc swatch list 
      - To list the first 100 entries of your Subscription Watch Inventory
    * - crhc swatch list \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/swatch_report.csv`` will be created.
    * - crhc swatch list_all 
      - To list all the entries of your Subscription Watch Inventory
    * - crhc swatch list_all \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/swatch_report.csv`` will be created.
    * - crhc swatch socket_summary 
      - To list a summary of sockets based on your Subscription Watch Inventory
    * - crhc advisor systems 
      - To list the Advisor systems information, for example, ``critical, important, moderate ...``
    * - crhc advisor systems \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/advisor_systems.csv`` will be created.
    * - crhc patch systems 
      - To list the Patch systems information, for example, ``Security Advisory``, ``Bug Advisory`` and/or ``Enhancement Advisory``
    * - crhc patch systems \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/patch_systems.csv`` will be created.
    * - crhc vulnerability systems 
      - To list the Vulnerabilities systems information, for example, ``CVE's``
    * - crhc vulnerability systems \-\-csv 
      - To generate the output in csv file. A new file ``/tmp/vulnerability_systems.csv`` will be created.
    * - crhc endpoint list 
      - To list all the available API endpoints on console.redhat.com
    * - crhc get ``<API ENDPOINT>`` 
      - Here you should be able to query the API endpoint directly
    * - crhc login \-\-token ``<offline token here>`` 
      - The way to inform the token that you can obtain from https://console.redhat.com/openshift/token
    * - crhc logout 
      - Used to cleanup the local conf file, removing all the token information
    * - crhc token 
      - This will print the access_token. This can be used with curl, for example.
    * - crhc whoami 
      - This option will show some information regarding to the user who requested the token
    * - crhc ts dump 
      - Export the whole Inventory and Subscription information in json format. Some files will be created.
    * - crhc ts match 
      - If the files mentioned above are not around, this feature will call the dump and after that will check both files and will create the 3rd one with the whole information correlated accordingly.
    * - crhc ts clean 
      - This will cleanup all the temporary/cache files.
    * - crhc {\-\-version|\-v} 
      - This option will present the app version
    * - crhc {\-\-help|\-h} 
      - This option will present the help

Note. All of them will generate the output in a JSON format, so you can use the output as input for any of your own script or also to ``jq`` command.

