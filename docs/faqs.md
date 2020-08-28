# OCI Ansible Modules Frequently Asked Questions (FAQs)

**1. How do I install the latest released version of the Ansible Cloud Collection?**

- You can install it from [Ansible Galaxy](https://galaxy.ansible.com/oracle) using the command:
  ``` bash
  $ ansible-galaxy collection install oracle.oci
  ```
- Notes:
    * Collections is supported in Ansible 2.9+.
    * For more information about collections, please check [Ansible Collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
    * To update the modules to latest version, use the install --force flag.

**2. How do I enable `debug` mode for the OCI Ansible Cloud Modules?**

-  Set the `log_requests` variable in your ~/.oci/config to `True` to enable Request logging in the OCI python SDK as described in https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst
-  Export an environment variable named `LOG_LEVEL` with the value `DEBUG` to enable DEBUG mode for the OCI Ansible modules
```sh
$ export LOG_LEVEL="DEBUG"
```

All subsequent debug messages from an ansible playbook execution using the OCI Ansible Cloud Modules
```sh
$ ansible-playbook ....
```
would go to `/tmp/oci_ansible_module.log` (the default logging location for the OCI Ansible modules).

OCI Ansible Cloud Modules uses standard Python logging facilities for logging. Use the environment variable `LOG_PATH` to change the directory where the log file should be placed and `LOG_LEVEL` to change the log level. The default log level is `INFO`.

**3. In a Mac OSX controller node, I am seeing "ImportError: No module named yaml" when executing a playbook, in spite of observing that I have ansible and its requirements including PyYAML installed in my python setup.**

If you are running on macOS, and you have python installed by brew, you may see a ImportError(for example: `ImportError: No module named yaml`).
To resolve this, you must override the `ansible_python_interpreter` configuration option. Setting the inventory variable `ansible_python_interpreter` on any host will allow Ansible to auto-replace the interpreter used when executing python modules.

`ansible_python_interpreter` configuration option can be set in inventory file. For example:

```sh
[control-node]
localhost ansible_python_interpreter="/usr/local/Cellar/python/2.7.14_3/bin/python2.7"
```

OR `ansible_python_interpreter` configuration option can be set using `-e` command line option:

```sh
$ ansible-playbook sample-playbook.yml -e 'ansible_python_interpreter=/usr/local/Cellar/python/2.7.14_3/bin/python2.7'
```

**4. Any security guidelines or best practices?**

1. The OCI Ansible Cloud Collection uses the authentication information specified in the standard OCI SDK configuration file (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#configuring-the-sdk) while creating and configuring OCI resources.

> *Caution*: IAM credentials referenced in the OCI SDK configuration file, grants access to resources. It is important to secure these credentials to prevent unauthorized access to Oracle Cloud Infrastructure resources. Follow the guidelines in https://docs.us-phoenix-1.oraclecloud.com/Content/Security/Reference/iam_security.htm#IAMCredentials to secure the IAM credentials in the controller node where you run ansible playbooks that uses these modules.

The OCI Ansible Cloud Modules allows the authentication information specified in the OCI SDK configuration file to be overridden using module options and environment variables. Please refer to the ansible module documentation of the OCI Ansible Cloud Modules for more details. Oracle recommends the use of OCI SDK configuration file to specify authentication information. Use the "profiles" feature in the OCI SDK configuration file to support different users. The use of environment variables and ansible module options to override Authentication information must be avoided in production scenarios. While distributing roles that use the OCI Ansible Cloud Modules, ensure that no IAM credentials are included with the roles.

2. Logging of OCI Ansible Cloud Collection may be configured using the a file through the `LOG_CONFIG` environment variable, as discussed in FAQ #3 above. It is recommended that the file pointed to by `LOG_CONFIG` environment variable be only access-able (Unix file permissions 400 or 600) by the user running the `ansible-playbook` that uses OCI Ansible Cloud Modules.


**5. How to Force Create resources?**

Ansible recommends that all the modules be idempotent, so that repeated playbook executions by users result in reaching the desired state quickly and reliably. Unless documented explicitly in the module's `ansible-doc`, all resource lifecycle operations initiated through OCI Ansible Modules are idempotent. To forcefully perform a non-idempotent creation of a resource, use the `force_create` option.

