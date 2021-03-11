# Common Issues

## WARNING: "module oracle.oci.xxx not found in path"
Most likely reason is that the OCI Ansible Collection is not installed.

Please refer the [Installation Guide](https://github.com/oracle/oci-ansible-collection/blob/master/InstallationGuide.md) on different ways to install the OCI Ansible Collection.

If it is already installed, it could be because the version you are using might not have the module. Please upgrade to the latest version using the below command:

`ansible-galaxy collection install -f oracle.oci`

-----------------------------------
## Error: "oci python sdk required for this module"

Try first upgrading the OCI python SDK:
`pip install oci --upgrade`

If the python SDK is not installed correctly, check [Ansible Install Troubleshooting Guide](ansible-oci-customer-troubleshooting/ansible-install-troubleshooting-guide.md).

-----------------------------------
## Error: "Could not find config file at ~/.oci/config"

- Make sure you created a config file under '~/.oci/config' or you are using instance principal.
- To create config file, check: [Configuration_File](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File)
- To use instance principal on a compute instance set the environment variable: `OCI_ANSIBLE_AUTH_TYPE=instance_principal`

-----------------------------------
## Error: "{'code': 'NotAuthenticated', 'message': 'The required information to complete authentication was not provided.', 'status': 401}"

Check if the [Account Keys](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs)
 are generated correctly and uploaded to the user account with right permissions.

-----------------------------------
## Error: "No inventory plugins available to generate inventory, make sure you have at least one whitelisted."

Enable the OCI Collection inventory plugin by adding it to your ansible.cfg file. For example:<br>
[inventory]<br>
enable_plugins = oracle.oci.oci<br>

-----------------------------------
## In a Mac OSX controller node, Error: "ImportError: No module named yaml" when executing a playbook
 
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