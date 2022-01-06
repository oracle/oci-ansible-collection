
## Troubleshooting OCI Ansible Issues
This page contains troubleshooting guides for the common OCI Ansible issues.

Start with [Troubleshooting Basics](#troubleshooting-basics) and then refer to the following sections:
- [Installation and Configuration Errors](#installation-and-configuration-errors)
- [Timeout Errors](#timeout-errors)
- [Inventory Plugin Errors](#inventory-plugin-errors)

### Troubleshooting Basics
When troubleshooting or getting support for the Oracle Cloud Infrastructure (OCI) Ansible, it is often useful to first check the status of the [OCI services](#checking-oci-service-status-and-outages), [the version of Ansible and the OCI Ansible collections](#checking-the-ansible-oci-ansible-collections-oci-python-sdk-versions), and [enable and collect verbose logging](#enabling-the-verbose-logging-for-oci-ansible-collections).
```
Checking service status and verbose log output can help you determine 
whether an issue is related to the OCI Ansible Collection or the OCI service the provider is using.
```

#### Checking OCI Service Status and Outages
To check on the latest status and whether there are any outages in OCI, see [OCI Status.](https://ocistatus.oraclecloud.com/)

#### Checking the Ansible, OCI Ansible Collections, OCI Python-SDK Versions
***Ansible Version***
```
ansible --version
```

***Ansible Collections Version***
```
output of the below command for oracle.oci
ansible-galaxy collection list
```

***OCI Python-SDK Version***
```
output of the below python script 
python -c "import oci;print(oci.__version__)"
```

#### Enabling the Verbose Logging for OCI Ansible Collections
- set the log_requests variable in your ```~/.oci/config``` to True to [enable Request logging in the OCI python SDK](https://github.com/oracle/oci-python-sdk/blob/master/docs/logging.rst).
- Export an environment variable named ```LOG_LEVEL``` with the value ```DEBUG``` to enable DEBUG mode for the OCI Ansible modules
```
export LOG_LEVEL="DEBUG"
```
All subsequent debug messages from an Ansible playbook execution using the OCI Ansible Cloud Modules would go to ```/tmp/oci_ansible_module.log ```(the default logging location for the OCI Ansible modules).<br>
OCI Ansible Cloud Modules uses standard Python logging facilities for logging. Use the environment variable ```LOG_PATH``` to change the directory where the log file should be placed and ```LOG_LEVEL``` to change the log level. The default log level is ```INFO```.

### Installation and Configuration Errors
#### module oracle.oci.xxx not found in path
****Problem:****
OCI Ansible module oracle.oci.oci_some_module was not found in configured module paths.

****Solution:****
- Verify that the OCI Ansible is installed. Please refer to the [Getting Started](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm) guide on how to install.
- If OCI Ansible is already installed, verify that the name of the module is correct. You can check the [Module Index](https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/index.html) for a list of supported modules.
- If OCI Ansible is installed, and the module name is correct, upgrade to the latest version of OCI Ansible Collections since the module might not be present in the version that customer is using.

#### oci python sdk required for this module
****Problem:****
"```oci python sdk required for this module```" means user is not on the latest version of python sdk.

****Solution:****
- Verify that the ```OCI Python SDK``` is installed. If not, please refer to the [SDK Installation Guide](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#downloading-and-installing-the-sdk)
- If it is already installed, it could be because you are using an older version. Please upgrade to the latest version. You can upgrade using the command:
    ```pip install -U oci```

#### Configuration file or profile errors
****Problem:****
The error could be either of these below errors:
- Could not find config file at ```~/.oci/config```:
        please follow the [instructions](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm) to setup the config file.
- Profile ```DEFAULT``` not found in config file ```~/.oci/config```:
        The OCI Ansible module is not able to read the information necessary for authentication.

****Solution:****
- If you are using API Key authentication
  - Verify that the [Account Keys](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs) are generated correctly and uploaded to the user account with right permissions.
  - Verify that the SDK configuration file is setup properly. Please refer SDK Configuration.
  - The default location for the configuration file is ```~/.oci/config```. If you are have the configuration file in a custom path, please set the config_file_location module parameter or the ```OCI_CONFIG_FILE``` environment variable.
  - The default profile name used is ```DEFAULT```. If you are using a custom profile, please set the config_profile_name module parameter or the ```OCI_CONFIG_PROFILE``` environment variable.
- If you are using ```Instance Principal authentication```
  - Verify that the instance has proper permissions and policies setup. Please refer [OCI Instance Principal Auth](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).
  - Set the authentication type as ```instance_principal``` using the ```auth_type``` module parameter or the ```OCI_ANSIBLE_AUTH_TYPE``` environment variable
- If you are using ```Resource Principal```:
  - Verify that the function has policies to grant the dynamic group access to the resource. Please refer [OCI Resource Principal Auth](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm)
  - Set the authentication type as ```resource_principal``` using the ```auth_type``` module parameter or the ```OCI_ANSIBLE_AUTH_TYPE``` environment variable
- If you are using ```Delegation Token```:
  - Verify that the token is expired. Please refer [OCI Delegation Token Auth](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/clitoken.htm)
  - Set the authentication type as ```instance_obo_user``` using the ```auth_type``` module parameter or the ```OCI_ANSIBLE_AUTH_TYPE``` environment variable

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

#### Error: "Could not find config file at ~/.oci/config"

- Make sure you created a config file under ```~/.oci/config``` or you are using instance principal.
- To create config file, check: [Configuration_File](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File)
- To use instance principal on a compute instance set the environment variable: `OCI_ANSIBLE_AUTH_TYPE=instance_principal`

#### Timeout Errors
#### Maximum wait time has been exceeded
****Problem:****
OCI Ansible module fails with error ```"Maximum wait time has been exceeded"```.
By default, we use a wait timeout of ```20 minutes``` and a longer timeout for some services like database, waas etc. Sometimes the service takes more time than normal and you would see this error.

****Solution:****
- This error occurs when the operation takes more time than the timeout.
- You can increase the timeout by following [configure wait-timeout](wait-timeout.md)

### Inventory Plugin errors
#### Inventory plugin does not return any data
****Problem:****
The OCI Ansible Inventory plugin does not return any hosts.

****Solution:****
- First confirm that resources indeed exist in the OCI console.
- If so, then the most likely reason is that the hostname_format/hostname_format_preferences given in the configuration and the existing resources does not match.
- Any instance/db host without a valid hostname_format_preferences are skipped. Update the hostname_format_preferences in the inventory config and try again.

#### Error: "No inventory plugins available to generate inventory, make sure you have at least one whitelisted."

Enable the OCI Collection inventory plugin by adding it to your ```ansible.cfg``` file. For example:<br>
[inventory]<br>
```enable_plugins = oracle.oci.oci```<br>