# Overview

This sample shows how a Management Agent with the Java Management System (JMS) enabled can be installed in OCI using the Oracle Cloud Agent (OCA) plugin.

The sample
- enables the Oracle Cloud Agent (OCA) Management Agent plugin
- enables JMS Service Plugin for all instances
- sets up the Java Usage Tracker
- installs logrotate
- removes all miscellaneous files created during installation process
- disables the Oracle Cloud Agent (OCA) Management Agent plugin

# Instructions

This sample has been tested for Oracle Linux 7 / 8 environments and may work differently in other Linux distributions. 

## Prerequisites
The Oracle CLI set up is required to run this sample including the config file. Instructions can be found [here](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm). You may skip to the next section if you have already configured the Oracle CLI setup.

Ensure a config file is correctly set up on your local machine. Select `User Settings` from the Profile button on the top right of the console, select `API Keys` and then click `Add API Key`. You may choose to generate a new key pair or use an existing one. After adding the API Key, select `View Configuration File` and then paste this information as a text file in ~/.oci and name the file as 'config'. Specify the location of your private key in the config file. For more information, see [SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm).

## Usage
Create an **ansible inventory file** to configure the environment required to run the playbook. 

**Take note:** In sample.yaml the ansible `hosts` are named as 'agents'. In the inventory file, add public IP address under [agents] so that the management agent will be installed in each compute instance. 

Example `.ini` file

```
[all:vars]
ansible_connection=ssh
ansible_port=22
ansible_user=opc
ansible_ssh_private_key_file=~/.ssh/id_rsa

[agents]
144.25.37.79
132.226.39.153
```
To run the sample, please provide values specific to your tenancy for the following variables in the `vars` section of `sample.yaml`:

- `instance_id_list` which contains instance OCIDs
- Do note that all compute instances should belong to the same compartment. If instances belong to multiple compartments, in each run of the ansible playbook, provide the OCID of the instances for a particular compartment.  