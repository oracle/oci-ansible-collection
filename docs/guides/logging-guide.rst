Logging In OCI Ansible Module
=============================

.. contents::
    :local:
    :backlinks: entry
    :depth: 2

OCI Ansible Collection uses Python's logging facilities for logging.

By default, logging will be disabled.

**Note: Logging using environment variables takes higher priority**

What determines Logging is enabled
----------------------------------
- Logging level & where the logs will be shown or captured, determines logging is enabled or not.
- Logging level is determined based on `environment variable <#set-logging-level-using-environment-variable>`__
  or `verbosity levels of OCI Ansible Module <#set-logging-level-using-verbosity-of-oci-ansible-module>`__
- By default, logs will be shown on `console <#logs-on-console>`__. To capture
  `logs in a file <#capture-logs-in-a-file-using-environment-variable>`__ instead of console, use environment variable to
  set the path to a directory where the log file containing logs should be placed.


Set Logging level Using Environment variable
--------------------------------------------
- To set the logging level, export environment variable named ``OCI_ANSIBLE_LOG_LEVEL``. ``LOG_LEVEL``  **is deprecated**.

.. code:: bash

   $ export OCI_ANSIBLE_LOG_LEVEL="INFO"

- If ``OCI_ANSIBLE_LOG_LEVEL`` is not set, then logging level is determined using
  `verbosity of OCI Ansible Module <#set-logging-level-using-verbosity-of-oci-ansible-module>`__ and if
  verbosity is not set then logging will be disabled
- If ``OCI_ANSIBLE_LOG_LEVEL`` = "WARNING", then logging level will be ``WARNING``
- If ``OCI_ANSIBLE_LOG_LEVEL`` = "INFO", then logging level will be ``INFO``
- If ``OCI_ANSIBLE_LOG_LEVEL`` = "DEBUG", then logging level will be ``DEBUG``.
  **At this level, request logging in OCI-Python-Sdk will be enabled**

Set Logging level Using Verbosity of OCI Ansible Module
-------------------------------------------------------
- Set the verbosity for OCI Ansible modules to set the logging level. On console, use -v flag while executing ansible
  playbook or calling OCI Ansible modules using adhoc commands. Look at the below example to see how to pass -v flag on
  console while executing ansible playbook and adhoc command respectively

.. code-block:: bash

   #playbook
   ansible-playbook -v sample.yaml
   #ansible adhoc command
   ansible -v localhost -m oracle.oci.some_module -a 'param1="val1" param2="val2"'

- If verbosity is 0(i.e. -v flag is not passed), then logging level will be based on either
  `environment variable <#set-logging-level-using-environment-variable>`__ and if environment variable is not set then
  logging will be disabled
- If verbosity is 1(i.e. -v can be passed), then logging level will be ``WARNING``
- If verbosity is 2(i.e. -vv can be passed), then logging level will be ``INFO``
- If verbosity is 3 or higher(i.e. -vvv, -vvvv, etc. can be passed), then logging level will be ``DEBUG``.
  **At this level, request logging in OCI-Python-Sdk will be enabled**

Logs on Console
---------------
By default, log will be shown on console. Logs will be collected in a list & will be shown in ``oci_ansible_logs`` key
together with the result of OCI Ansible module

Capture logs in a file using environment variable
-------------------------------------------------
- Export environment variable named ``OCI_ANSIBLE_LOG_DIR``. ``LOG_PATH`` **is deprecated**
- Logs will be collected in a file called ``oci_ansible_module.log`` instead of console.
- Set ``OCI_ANSIBLE_LOG_DIR`` to a path to the directory where the log file ``oci_ansible_module.log`` will be placed.

.. code:: bash

   $ export OCI_ANSIBLE_LOG_DIR="path_to_the_directory"

- If ``OCI_ANSIBLE_LOG_DIR`` exists, then

    - If ``oci_ansible_module.log`` file doesn't exist in the directory set above, then ``oci_ansible_module.log`` file
      will be created in the directory set above and all the logs will be collected in that file. So logs can be accessed at
      ``path_to_the_directory/oci_ansible_module.log``
    - If ``oci_ansible_module.log`` file exists in the directory set above and the file has a write access, then logs
      will be appended in that file. So logs can be accessed at ``path_to_the_directory/oci_ansible_module.log``
    - If ``oci_ansible_module.log`` file exists in the directory set above and the file doesn't have a write access,
      then logs won't be captured in a file. Logging will be disabled in this case

- Else logs won't be captured in a file & logging will be disabled in this case

Enable Request Logging in OCI-Python-Sdk
----------------------------------------
Set the logging level to ``DEBUG`` either using environment variables or verbosity of Ansible Modules to enable request
logging in OCI-Python-Sdk
