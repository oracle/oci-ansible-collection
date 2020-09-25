# Frequently Asked Questions (FAQs)

### Common errors:

#### WARNING: "module oracle.oci.xxx not found in path"
Check if the `oracle.oci` collection is installed using this command:
`ansible-galaxy collection list`
The collection is installed under the default paths: `~/.ansible/collections` or `/usr/share/ansible/collections`

-----------------------------------
#### Error: "oci python sdk required for this module"

Try first upgrading the OCI python SDK:
`pip install oci --upgrade`

If the python SDK is not installed correctly, check [Ansible Install Troubleshooting Guide](ansible-oci-customer-troubleshooting/ansible-install-troubleshooting-guide.md).

-----------------------------------
#### Error: "Could not find config file at ~/.oci/config"

- Make sure you created a config file under '~/.oci/config' or you are using instance principal.
- To create config file, check: [Configuration_File](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File)
- To use instance principal on a compute instance set the environment variable: `OCI_ANSIBLE_AUTH_TYPE=instance_principal`

-----------------------------------
#### Error: "{'code': 'NotAuthenticated', 'message': 'The required information to complete authentication was not provided.', 'status': 401}"

Check if the [Account Keys](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs)
 are generated correctly and uploaded to the user account with right permissions.

-----------------------------------
#### Error: "No inventory plugins available to generate inventory, make sure you have at least one whitelisted."

Enable the OCI Collection inventory plugin by adding it to your ansible.cfg file. For example:<br>
[inventory]<br>
enable_plugins = oracle.oci.oci<br>

For the legacy modules, use enable_plugins = oci

-----------------------------------

#### In a Mac OSX controller node, Error: "ImportError: No module named yaml" when executing a playbook
 
First make sure that ansible and its requirements including PyYAML are installed.
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

-----------------------------------

### Enable `debug` mode for the OCI Ansible Cloud Modules

-  Set the `log_requests` variable in your ~/.oci/config to `True` to [enable Request logging in the OCI python SDK](https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst)
-  Export an environment variable named `LOG_LEVEL` with the value `DEBUG` to enable DEBUG mode for the OCI Ansible modules
```sh
$ export LOG_LEVEL="DEBUG"
```

All subsequent debug messages from an Ansible playbook execution using the OCI Ansible Cloud Modules 
would go to `/tmp/oci_ansible_module.log` (the default logging location for the OCI Ansible modules).

OCI Ansible Cloud Modules uses standard Python logging facilities for logging.
Use the environment variable `LOG_PATH` to change the directory where the log file should be placed and `LOG_LEVEL` to change the log level. 
The default log level is `INFO`.
