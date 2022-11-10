Troubleshooting Guide
=====================

.. contents::
    :local:
    :backlinks: entry
    :depth: 2


Troubleshooting Basics
----------------------
When troubleshooting or getting support for the Oracle Cloud
Infrastructure (OCI) Ansible, it is often useful to first check the
status of the `OCI
services <#checking-oci-service-status-and-outages>`__, `the version of
Ansible and the OCI Ansible
collections <#checking-the-ansible-oci-ansible-collections-oci-python-sdk-versions>`__,
and `enable and collect verbose
logging <#enabling-the-verbose-logging-for-oci-ansible-collections>`__.

.. code:: text

   Checking service status and verbose log output can help you determine
   whether an issue is related to the OCI Ansible Collection or the OCI service the provider is using.

Checking OCI Service Status and Outages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check on the latest status and whether there are any outages in OCI,
see `OCI Status. <https://ocistatus.oraclecloud.com/>`__

Checking the Ansible, OCI Ansible Collections, OCI Python-SDK Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ansible Version
^^^^^^^^^^^^^^^

.. code:: bash

   ansible --version

Ansible Collections Version
^^^^^^^^^^^^^^^^^^^^^^^^^^^

output of the below command will provide the ansible collection version
for oracle.oci

.. code:: bash

   ansible-galaxy collection list

OCI Python-SDK Version
^^^^^^^^^^^^^^^^^^^^^^

output of the below python script will provide the oci python-sdk
version.

.. code:: bash

   python3 -c "import oci;print(oci.__version__)"

Enabling the Verbose Logging for OCI Ansible Collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Set the log_requests variable in your ``~/.oci/config`` to True to
   `enable Request logging in the OCI python
   SDK <https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst>`__.
-  Export an environment variable named ``LOG_LEVEL`` with the value
   ``DEBUG`` to enable DEBUG mode for the OCI Ansible modules

.. code:: bash

   export LOG_LEVEL="DEBUG"

All subsequent debug messages from an Ansible playbook execution using
the OCI Ansible Cloud Modules would go to
``/tmp/oci_ansible_module.log``\ (the default logging location for the
OCI Ansible modules).

OCI Ansible Cloud Modules uses standard Python
logging facilities for logging. Use the environment variable
``LOG_PATH`` to change the directory where the log file should be placed
and ``LOG_LEVEL`` to change the log level. The default log level is
``INFO``.

Installation and Configuration Errors
-------------------------------------
module oracle.oci.xxx not found in path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^

OCI Ansible module ``oracle.oci.oci_some_module`` was
not found in configured module paths.

Solution:
^^^^^^^^^

-  Verify that the OCI Ansible is installed. Please refer to the
   `Getting
   Started <https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm>`__
   guide on how to install.
-  If OCI Ansible is already installed, verify that the name of the
   module is correct. You can check the `Module
   Index <https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/index.html>`__
   for a list of supported modules.
-  If OCI Ansible is installed, and the module name is correct, upgrade
   to the latest version of OCI Ansible Collections since the module
   might not be present in the version that customer is using.

oci python sdk required for this module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
``oci python sdk required for this module`` means
user is not on the latest version of python sdk.

Solution:
^^^^^^^^^

-  Verify whether ``OCI Python SDK`` is installed using the following commands:

    .. code:: bash

       python3 -c "import oci;print(oci.__version__)"
    -  If installed using yum please try the below command
    .. code:: bash

        yum info oci

    -  If ``OCI Python SDK`` is not installed, please refer
       to the `SDK Installation
       Guide <https://docs.oracle.com/en-us/iaas/tools/python/latest/installation.html#>`__
    -  If ``OCI Python SDK`` is already installed,

        -  First of all, it should be installed in the same execution environment where oci-ansible-collections is installed.
        -  It could be because you are using an older version. Please upgrade to the latest version. You can upgrade
           using the command: ``pip install -U oci``
        -  It can be because there can be multiple oci-python-sdk installed and it is not able
           to pick correct path. So you can set python interpreter as follows:
            -  To set python interpreter for individual hosts and groups, use the ``ansible_python_interpreter`` inventory variable
               and set the correct python-sdk path
            -  To set python interpreter globally, use the ``interpreter_python`` key in the ``[defaults]`` section of ``ansible.cfg``
            -  For a complete list of possible values for the two options above, please refer:
               https://docs.ansible.com/ansible/latest/reference_appendices/interpreter_discovery.html.
            -  To see the example of usage of ``ansible_python_interpreter`` variable please refer:
               https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html

Configuration file or profile errors
------------------------------------

Could not find config file at ``~/.oci/config``: please follow the `instructions <https://docs. cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm>`__ to setup the config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


-  If you are using API Key authentication

   -  Verify that the `Account
      Keys <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs>`__
      are generated correctly and uploaded to the user account with
      right permissions.
   -  Verify that the SDK configuration file is setup properly. Please
      refer SDK Configuration.
   -  The default location for the configuration file is
      ``~/.oci/config``. If you are have the configuration file in a
      custom path, please set the config_file_location module parameter
      or the ``OCI_CONFIG_FILE`` environment variable.
   -  The default profile name used is ``DEFAULT``. If you are using a
      custom profile, please set the config_profile_name module
      parameter or the ``OCI_CONFIG_PROFILE`` environment variable.

-  If you are using ``Instance Principal authentication``

   -  Verify that the instance has proper permissions and policies
      setup. Please refer `OCI Instance Principal
      Auth <https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm>`__.
   -  Set the authentication type as ``instance_principal`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable

-  If you are using ``Resource Principal``:

   -  Verify that the function has policies to grant the dynamic group
      access to the resource. Please refer `OCI Resource Principal
      Auth <https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm>`__
   -  Set the authentication type as ``resource_principal`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable

-  If you are using ``Delegation Token``:

   -  Verify that the token is expired. Please refer `OCI Delegation
      Token
      Auth <https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm>`__
   -  Set the authentication type as ``instance_obo_user`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable


Profile ``DEFAULT`` not found in config file ``~/.oci/config``: The OCI Ansible module is not able to read the information necessary for authentication.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If you are using API Key authentication

   -  Verify that the `Account
      Keys <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs>`__
      are generated correctly and uploaded to the user account with
      right permissions.
   -  Verify that the SDK configuration file is setup properly. Please
      refer SDK Configuration.
   -  The default location for the configuration file is
      ``~/.oci/config``. If you are have the configuration file in a
      custom path, please set the config_file_location module parameter
      or the ``OCI_CONFIG_FILE`` environment variable.
   -  The default profile name used is ``DEFAULT``. If you are using a
      custom profile, please set the config_profile_name module
      parameter or the ``OCI_CONFIG_PROFILE`` environment variable.

-  If you are using ``Instance Principal authentication``

   -  Verify that the instance has proper permissions and policies
      setup. Please refer `OCI Instance Principal
      Auth <https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm>`__.
   -  Set the authentication type as ``instance_principal`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable

-  If you are using ``Resource Principal``:

   -  Verify that the function has policies to grant the dynamic group
      access to the resource. Please refer `OCI Resource Principal
      Auth <https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm>`__
   -  Set the authentication type as ``resource_principal`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable

-  If you are using ``Delegation Token``:

   -  Verify that the token is expired. Please refer `OCI Delegation
      Token
      Auth <https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm>`__
   -  Set the authentication type as ``instance_obo_user`` using the
      ``auth_type`` module parameter or the ``OCI_ANSIBLE_AUTH_TYPE``
      environment variable

In a Mac OSX controller node, Error: “ImportError: No module named yaml” when executing a playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First make sure that ansible and its requirements including PyYAML are
installed. If you are running on macOS, and you have python installed by
brew, you may see a ImportError(for example:
``ImportError: No module named yaml``). To resolve this, you must
override the ``ansible_python_interpreter`` configuration option.
Setting the inventory variable ``ansible_python_interpreter`` on any
host will allow Ansible to auto-replace the interpreter used when
executing python modules.

``ansible_python_interpreter`` configuration option can be set in
inventory file. For example:

.. code:: sh

   [control-node]
   localhost ansible_python_interpreter="/usr/local/Cellar/python/2.7.14_3/bin/python2.7"

OR ``ansible_python_interpreter`` configuration option can be set using
``-e`` command line option:

.. code:: sh

   ansible-playbook sample-playbook.yml -e 'ansible_python_interpreter=/usr/local/Cellar/python/2.7.14_3/bin/python2.7'

Error: “Could not find config file at ~/.oci/config”
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Make sure you created a config file under ``~/.oci/config`` or you
   are using instance principal.
-  To create config file, check:
   `Configuration_File <https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>`__.
-  To use instance principal on a compute instance set the environment
   variable: ``OCI_ANSIBLE_AUTH_TYPE=instance_principal``.

Timeout Errors
--------------

Maximum wait time has been exceeded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Ansible module fails with error
``"Maximum wait time has been exceeded"``. By default, we use a wait
timeout of ``20 minutes`` and a longer timeout for some services like
database, waas etc. Sometimes the service takes more time than normal
and you would see this error.

Solution:
^^^^^^^^^

-  This error occurs when the operation takes more time than the
   timeout.
-  You can increase the timeout by following `configure
   wait-timeout <wait-timeout.md>`__.

Service Errors
--------------

OCI Ansible modules interacts with OCI services on your behalf. Many
error messages surfaced by the Ansible modules come directly from OCI
services. The `API
Errors <https://docs.oracle.com/en-us/iaas/Content/API/References/apierrors.htm#API_Errors>`__
reference lists common errors returned by all services.

Error: 400-LimitExceeded
~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Ansible module fails with the service error
400-LimitExceeded with the error message
``Fulfilling this request exceeds the Oracle-defined limit for this tenancy for this resource type``.

Solution:
^^^^^^^^^
Request a service limit increase for this resource.

To understand more about your OCI service limits and how to request a
limit increase, see `Service
Limits <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top>`__.

Error: 401-NotAuthenticated
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Ansible module fails with service error
``401-NotAuthenticated`` with error message
``The required information to complete authentication was not provided or was incorrect``.

Solution:
^^^^^^^^^
The required information to complete authentication
was not provided or was incorrect. Verify the below configurations.

-  Verify you have properly set ``user_ocid``, ``tenancy_ocid``, ``fingerprint`` and ``private_key_path``
-  Verify your ``private_key_path`` is pointing to your private key and not the corresponding public key.
-  Verify you have added the corresponding public key to the user account you have specified with ``user_ocid``.
-  Verify the public/private key pairs you are using are of the correct format. See `Required Keys <https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs>`__ for details on the correct format and how to generate keys.
-  Verify the user account is part of a group with the appropriate permissions to perform the actions in the plan you are executing.
-  Verify your Tenancy has been subscribed to the Region you are targeting in your plan.

Error: 404-NotAuthorizedOrNotFound
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Ansible module fails with service error
``404-NotAuthorizedOrNotFound`` with error message
``Authorization failed or requested resource not found``.

Solution:
^^^^^^^^^
Either the resource has been deleted or service need
policy to access this resource.

-  Verify the user account is part of a group with the appropriate
   permissions to perform the action. Refer to the `Policy
   Reference <https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference.htm>`__
   for your service for more information.
-  Verify if the resource which is giving the error
   ``404-NotAuthorizedOrNotFound`` indeed exists.
-  Verify the ``config file`` and ``region`` being configured is
   correct.

Error: 500-InternalError
~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Ansible module fails with service error
``500-InternalError`` and message ``Internal error occurred``.

Solution:
^^^^^^^^^
The service for this resource encountered an error. Please contact support for help with service.

The service responded to the request from the Ansible module with an
internal error. If you `contact
support <https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/contactingsupport.htm#Getting_Help_and_Contacting_Support>`__
for this issue, reference the information in the message.

Inventory Plugin errors
-----------------------

Inventory plugin does not return any data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
The OCI Ansible Inventory plugin does not return any hosts.

Solution:
^^^^^^^^^

-  First confirm that resources indeed exist in the OCI console.
-  If so, then the most likely reason is that the ``hostname_format``/
   ``hostname_format_preferences`` given in the configuration and the existing resources does
   not match.
-  Any instance/db host without a valid hostname_format_preferences are
   skipped. Update the hostname_format_preferences in the inventory
   config and try again.

Error: “No inventory plugins available to generate inventory, make sure you have at least one whitelisted.”
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Solution:
^^^^^^^^^

Enable the OCI Collection inventory plugin by adding it to your
``ansible.cfg`` file. For example:

.. code:: bash

   [inventory]
   enable_plugins = oracle.oci.oci

Ansible searches for ``ansible.cfg`` in this
`order <https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations>`__.
Verify you have your ``ansible.cfg`` in the correct location.

Error: “The oci dynamic inventory plugin requires oci python sdk”
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:
^^^^^^^^^

Inventory plugin requires ``OCI Python SDK`` to get the data.

-  Verify that the ``OCI Python SDK`` is installed. If not, please refer to the `SDK Installation Guide <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#downloading-and-installing-the-sdk>`__.
-  If it is already installed, it could be because you are using an older version. Please upgrade to the latest version. You can upgrade using the command: ``pip install -U oci``.

Error: Tenancy OCID required to get the compartments in the tenancy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
The OCI Ansible Inventory plugin fails with error ``Tenancy OCID required to get the compartments in the tenancy``. When ``compartments`` is not configured in the inventory config, inventory plugin gets the compartments in the tenancy.

Solution:
^^^^^^^^^

When ``compartments`` is not configured in the inventory config,
inventory plugin gets tenancy from ``oci config``. User has to atleast
pass one of the below:

-  configure tenancy in the ``oci config`` profile.
-  configure ``compartments`` in inventory config.

Error: Instance with OCID: ocid1.instance.XXXXX does not have a valid hostname
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
When ``strict`` is configured in the inventory config, inventory plugin expects all the hosts that inventory returns to have valid hostname based on configured ``hostname_format`` or
``hostname_format_preference``.

Solution:
^^^^^^^^^

The configured ``hostname_format`` or ``hostname_format_preference``
doesn’t return valid hostname for the instance. Disable ``strict`` or
pass the ``hostname_format`` or ``hostname_format_preference`` that
generates valid hostname for the instance.

Error:404-NotAuthorizedOrNotFound
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
The inventory plugin fails with service error ``404-NotAuthorizedOrNotFound``.

Solution:
^^^^^^^^^

-  Either the resource has been deleted or user doesn’t have the
   required policy to access the resource.
-  Verify if the resource which is giving the error
   ``404-NotAuthorizedOrNotFound`` indeed exists.
-  Verify the user account is part of a group with the
   `permissions <../inventory_plugin#permissions>`__ required for
   inventory plugin.
-  Verify the ``config file`` and ``region`` being configured is
   correct.
-  Either pass the /full/path/to/config/file in inventory plugin file
   (.oci.yaml).
-  Or pass the relative/path/to/config/file with respect to the
   directory from where inventory command is executed.
-  Relative path to config file should not be relative with respect to
   inventory plugin file (.oci.yml).

Error: Compartment with OCID ocid1.compartment.XX..XXXX either does not exist or you do not have permission to access it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:
^^^^^^^^^

-  Either the compartment ocid1.compartment.XX..XXXX is deleted or the
   user doesn’t have required policy to access the compartment.
-  Verify if the compartment ocid1.compartment.XX..XXXX exists in the
   configured region.
-  Verify if the user account is part of a group with the
   `permissions <../inventory_plugin#permissions>`__ required to access
   the compartment.
-  You can exclude this compartment by configuring
   ``exclude_compartments`` option.

Error: ansible_collections.oracle.oci.plugins.inventory.oci declined parsing <inventory_config> as it did not pass its verify_file() method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:
^^^^^^^^^

OCI Inventory plugin requires the file name to end with ``.oci.yml`` or
``.oci.yaml``. Set the file name to end with ``.oci.yml`` or
``.oci.yaml``.

Inventory plugin fails with Service error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem:
^^^^^^^^
OCI Inventory plugin interacts with OCI services on your behalf. Many error messages surfaced by the Inventory plugin come directly from OCI services.

Solution:
^^^^^^^^^
refer the `Service Errors <#service-errors>`__ for troubleshooting
common errors.
