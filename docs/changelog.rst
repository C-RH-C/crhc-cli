Changelog
---------


**v1.13.13 - 09/06/2023**

- [ENHANCEMENT] Ansible report feature added - [`issue 179`]
- [ENHANCEMENT] adding dump_current feature under ts menu - [`issue 184`]
- [FIX] Fixing the endpoint that was changed on console.redhat.com side - [`issue 188`]


.. _issue 179: https://github.com/C-RH-C/crhc-cli/issues/179
.. _issue 184: https://github.com/C-RH-C/crhc-cli/issues/184
.. _issue 188: https://github.com/C-RH-C/crhc-cli/issues/188



**v1.12.12 - 06/23/2023**

- [ENHANCEMENT] changed inventory_list_all to collect details in batches of 50 - [`issue 180`_]

.. _issue 180: https://github.com/C-RH-C/crhc-cli/issues/180



**v1.11.12 - 01/26/2023**

- [ENHANCEMENT] Adding the new feature to remove stale entries based on the # of days - [`issue 24`_]
- [FIX] Fixing the syspurpose issue - [`issue 168`_]

.. _issue 168: https://github.com/C-RH-C/crhc-cli/issues/168
.. _issue 24: https://github.com/C-RH-C/crhc-cli/issues/24



**v1.10.11 - 08/16/2022**

- [FIX] Ordering the inventory output, avoiding wrong information - [`issue 163`_]
.. _issue 163: https://github.com/C-RH-C/crhc-cli/issues/163



**v1.10.10 - 03/25/2022**

- [ENHANCEMENT] Fixing linters warnings - [`issue 97`_]
- [ENHANCEMENT] Updating end to end test - [`issue 156`_]
- [FIX] #118 - Fixing the api endpoint list - [`issue 118`_]
- [ENHANCEMENT] Removing the square brackets and single quotations marks from installed product - [`issue 152`_]
- [FIX] fixing the kvm dup entries - [`issue 40`_]

.. _issue 97: https://github.com/C-RH-C/crhc-cli/issues/97
.. _issue 156: https://github.com/C-RH-C/crhc-cli/issues/156
.. _issue 118: https://github.com/C-RH-C/crhc-cli/issues/118
.. _issue 152: https://github.com/C-RH-C/crhc-cli/issues/152
.. _issue 40: https://github.com/C-RH-C/crhc-cli/issues/40



**v1.9.9 - 03/01/2022**

- [FIX] Issue when exporting the advisory data - [`issue 149`_]
- [FIX] test updated - [`issue 147`_]
- [ENHANCEMENT] MS version added
- [ENHANCEMENT] Total # of entries added to swatch list_all - [`issue 135`_]
- [ENHANCEMENT] Fixed the time to check for a new version - [`issue 127`_]
- [FIX] Fixing some issues when generating the ts dump - [`issue 136`_]
- [ENHANCEMENT] Adding the GPL 3 license - [`issue 134`_]
- [ENHANCEMENT] fix readme links
- [ENHANCEMENT] some update in the documentation
- [ENHANCEMENT] end to end test added

.. _issue 149: https://github.com/C-RH-C/crhc-cli/issues/149
.. _issue 147: https://github.com/C-RH-C/crhc-cli/issues/147
.. _issue 135: https://github.com/C-RH-C/crhc-cli/issues/135
.. _issue 127: https://github.com/C-RH-C/crhc-cli/issues/127
.. _issue 136: https://github.com/C-RH-C/crhc-cli/issues/136
.. _issue 134: https://github.com/C-RH-C/crhc-cli/pull/134



**v1.8.8 - 11/06/2021**

- [ENHANCEMENT] Docs updated and Feature page created - [`issue 125`_]
- [FIX] fixed the messages even when with no token - [`issue 116`_] | [`issue 117`_]
- [ENHANCEMENT] Advisor feature added - [`issue 121`_]
- [ENHANCEMENT] Adding total in the json, dumping the patch and vuln in JSON and also doing some additional stuff - [`issue 108`_]
- [ENHANCEMENT] Conf file added to the project - [`issue 114`_]
- [ENHANCEMENT] Added vulnerability feature - [`issue 108`_]
- [ENHANCEMENT] Adding the patch feature - [`issue 110`_]
- [ENHANCEMENT] Fixed the api endpoint information when using get /api/patch - [`issue 109`_]
- [FIX] requirements updated - [`issue 103`_]
- [ENHANCEMENT] Sphinx configuration + readthedocs ready - [`issue 102`_]

.. _issue 125: https://github.com/C-RH-C/crhc-cli/pull/125
.. _issue 116: https://github.com/C-RH-C/crhc-cli/issues/116
.. _issue 117: https://github.com/C-RH-C/crhc-cli/issues/117
.. _issue 121: https://github.com/C-RH-C/crhc-cli/issues/121
.. _issue 108: https://github.com/C-RH-C/crhc-cli/issues/108
.. _issue 114: https://github.com/C-RH-C/crhc-cli/issues/114
.. _issue 110: https://github.com/C-RH-C/crhc-cli/issues/110
.. _issue 109: https://github.com/C-RH-C/crhc-cli/issues/109
.. _issue 103: https://github.com/C-RH-C/crhc-cli/issues/103
.. _issue 102: https://github.com/C-RH-C/crhc-cli/issues/102



**v1.7.7 - 10/16/2021**

- [ENHANCEMENT] issue_summary_created - [`issue 76`_]
- [ENHANCEMENT] installed_product updated and some refactory - [`issue 81`_]
- [ENHANCEMENT] Added the compress feature - [`issue 83`_]
- [FIX] Fixing the message in inventory list_all - [`issue 87`_]
- [ENHANCEMENT] Adding proxy information on readme.md - [`issue 88`_]

.. _issue 76: https://github.com/C-RH-C/crhc-cli/issues/76
.. _issue 81: https://github.com/C-RH-C/crhc-cli/issues/81
.. _issue 83: https://github.com/C-RH-C/crhc-cli/issues/83
.. _issue 87: https://github.com/C-RH-C/crhc-cli/issues/87
.. _issue 88: https://github.com/C-RH-C/crhc-cli/issues/88



**v1.6.6 - 10/12/2021**

- [ENHANCEMENT] help redesigned and some tests added - [`issue 82`_]
- [ENHANCEMENT] unit test - inventory_report - [`issue 82`_]

.. _issue 82: https://github.com/C-RH-C/crhc-cli/issues/82



**v1.5.6 - 10/03/2021**

- [FIX] Fixed the correct # of pages and servers - [`issue 78`_]

.. _issue 78: https://github.com/C-RH-C/crhc-cli/issues/78



**v1.5.5 - 10/02/2021**

- [ENHANCEMENT] Stale fields added - [`issue 68`_]
- [ENHANCEMENT] Adding the # of guests on top of it - [`issue 65`_]
- [ENHANCEMENT] Added the new 3 fields, 2 of system_purpose and one of sca - [`issue 69`_]
- [FIX] Fixed issue with sw report - [`issue 64`_]
- [FIX] Fixing some issues related to columns/positioning - [`issue 63`_]
- [ENHANCEMENT] Checking the rhsm namespace for host-guest mapping - [`issue 61`_]
- [FIX] fixing the issue for customers with less then 50 entries on crhc - [`issue 59`_]

.. _issue 68: https://github.com/C-RH-C/crhc-cli/issues/68
.. _issue 65: https://github.com/C-RH-C/crhc-cli/issues/65
.. _issue 69: https://github.com/C-RH-C/crhc-cli/issues/69
.. _issue 64: https://github.com/C-RH-C/crhc-cli/issues/64
.. _issue 63: https://github.com/C-RH-C/crhc-cli/issues/63
.. _issue 61: https://github.com/C-RH-C/crhc-cli/issues/61
.. _issue 59: https://github.com/C-RH-C/crhc-cli/issues/59



**v1.4.4 - 09/23/2021**

- [FIX] Fixing the error caused by an empty conf file
- [FIX] fixing a minor typo that is causing keyerror issue for the inventory list - short version



**v1.4.3 - 09/11/2021**

- [ENHANCEMENT] Adding the troubleshooting feature - dump json files for inventory
- [ENHANCEMENT] Adding the troubleshooting feature - dump json files for subscriptions
- [ENHANCEMENT] Adding the troubleshooting feature - cleaning the temporary/cache files
- [ENHANCEMENT] Adding the version option
- [FIX] Improving and fixing the Inventory report with some additional fields
- [ENHANCEMENT] Adding the feature to load the 3rd party data and generate the match information to be used during the analysis/troubleshooting
- [FIX] Improving the exception when the token gets revoked



**v1.3.2 - 09/06/2021**

- [FEATURE] --csv option added to the current inventory and swatch reports
- [FEATURE] Checking for new releases based on the app version
- [FIX] Fixing some KeyErrors when running the app
- [FIX] Adding the cast for the field "sap_system" (when using the jq command)
- [ENHANCEMENT] Disclaimer added



**v1.2.1 - 08/31/2021**

- [ENHANCEMENT] Inventory with some new information
- [FEATURE] Authentication using Token



**v1.1.0 08/25/2021**

- [RFE] remove the sort keys in the JSON output
- [FEATURE] Supporting all the minor versions of python 3 (3.6.8+) when creating the binary file
- [FEATURE] # of sockets based on the swatch info - Summary
- [FEATURE] List all the available API endpoints in console.redhat.com
- [FEATURE] Way to query the API endpoint directly



**v1.0.0 - 08/07/2021**

 - Initial idea and first piece of code! :)
