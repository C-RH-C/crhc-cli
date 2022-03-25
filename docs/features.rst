Features
========

In this section you can see all the available features in ``crhc-cli``

* Export of Inventory data, in ``JSON`` and ``CSV`` format.
* Export of Subscription data, in ``JSON`` and ``CSV`` format.
* Creation of a Single Dataset including ``Inventory`` and ``Subscription`` data in ``CSV`` format.
* Export of Advisor data, in ``JSON`` and ``CSV`` format.
* Export of Vulnerability data, in ``JSON`` and ``CSV`` format.
* Export of Patch data, in ``JSON`` and ``CSV`` format.
* Subscription Socket summary (spliting the sockets from hypervisors and VM's with no host-guest mapping).
* Easy way to present the available API endpoints.
* Easy way to consume the API endpoints listed above.
* Access Token generation to be used with 3rd party software, for example ``curl -H 'Authorization: Bearer $(./crhc token) ...'`` 
* Currently supporting both platforms, ``Linux`` and ``MS Windows`` with python 3.6+
* Export the whole information easily via ``./crhc ts dump`` to help the ``Red Hat Support team`` during the troubleshooting process.

Are you looking for something new that is not listed above? Click `here`_ and let us know.

.. _here: https://github.com/C-RH-C/crhc-cli/issues/new