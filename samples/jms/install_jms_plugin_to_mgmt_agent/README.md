# Overview

This sample shows how a Management Agent with Java Management System (JMS) plugins can be installed on a free-tier compute instance in OCI. 

The sample
- downloads a Management Agent .rpm file to the compute instance
- installs the Management Agent from the .rpm file
- configures the Management Agent
- sets up the Java Usage Tracker
- installs logrotate
- removes all miscellaneous files created during installation process
- removes the created Management Agent

# Instructions

This sample has been tested for Oracle Linux 7 / 8 environments and may work differently in other Linux distributions. 

## Prerequisites
Java 1.8 is required to install the management agent and the environment variable should have the path set in JAVA_HOME. Indicate this in the `mgmt_agent_jdk_home` variable in the **Usage** section. 

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

To run the sample, please provide values specific to your tenancy for the following variable in the `vars` section of `sample.yaml`:

- `compute_compartment_id` OCID
- `mgmt_agent_jdk_home`