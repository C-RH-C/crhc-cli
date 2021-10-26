Proxy Configuration
===================

If you have proxy in your environment, it will be necessary to add this configuration in your terminal. In order to do that, you can proceed as below:

To check the current configuration

.. code-block:: sh

    $ echo $http_proxy

To setup your proxy

.. code-block:: sh

    $ export http_proxy=http://SERVER:PORT/

or

.. code-block:: sh

    $ export http_proxy=http://USERNAME:PASSWORD@SERVER:PORT/

And if you would like to keep it permanent

.. code-block:: sh

    # echo "export http_proxy=http://proxy.local.domain:3128/" > /etc/profile.d/http_proxy.sh

Note. Please, change the values according to your environment. After that, you should be good to go and use the ``crhc`` with no problems.