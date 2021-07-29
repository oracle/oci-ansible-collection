# Oracle Cloud Infrastructure Ansible Collection

Oracle Cloud Infrastructure Ansible Collection provides an easy way to provision and manage resources in Oracle Cloud using Ansible.

> **This collection replaces the [legacy modules](https://github.com/oracle/oci-ansible-modules). Refer to the [Migration Guide](https://github.com/oracle/oci-ansible-collections/blob/master/MigrationGuide.md) for best migration practices.**

Ansible [released Collections](https://www.ansible.com/blog/getting-started-with-ansible-collections) as part of the Ansible 2.9 release.
Ansible recommends Collections as the recommended method of packaging and releasing modules. 
With the creation of Oracle Cloud Ansible Collection, we are providing two user benefits:
 * **Faster Availability** - Oracle Cloud Ansible Modules will now be available to users at a faster pace on Ansible Galaxy. 
 * **Wider Coverage** - Support for the majority of the Oracle Cloud services.

We have also added a new [User Guide](https://github.com/oracle/oci-ansible-collections/blob/master/UserGuide.md) to highlight new features and best practices for using the new modules.

### Migration from Legacy Modules

We recommend migrating from the [legacy modules](https://github.com/oracle/oci-ansible-modules) since they will be deprecated in the near future.
Please expect a few breaking changes while migrating from legacy modules to the new collection modules.
We recommend you to refer to the [Migration Guide](https://github.com/oracle/oci-ansible-collections/blob/master/MigrationGuide.md) for breaking changes.
Also, the new modules are renamed to use the service name as a prefix.

#### Currently Supported Services 
We support almost all the of [OCI Cloud services](https://docs.cloud.oracle.com/en-us/iaas/Content/services.htm) with very few exceptions.
For the complete list of supported services, please check the [modules list](https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/index.html).

## Installation

### Pre-requisites
**python>=3.6**
#### Oracle Linux 7

```
sudo yum-config-manager --enable ol7_developer
sudo yum-config-manager --enable ol7_developer_EPEL
sudo yum install oci-ansible-collection
```
#### Oracle Linux 8

```
sudo yum-config-manager --enable ol8_developer
sudo yum-config-manager --enable ol8_developer_EPEL
sudo yum install oci-ansible-collection
```

#### Linux/macOS

```
curl -L https://raw.githubusercontent.com/oracle/oci-ansible-collection/master/scripts/install.sh | bash -s -- --verbose
```
#### For more info about installation and troubleshooting check the [Installation Guide](https://github.com/oracle/oci-ansible-collections/blob/master/InstallationGuide.md).

## Samples and Solutions

The project includes a catalog of Oracle Cloud Infrastructure Ansible module samples that illustrate using the modules 
to carry out common infrastructure provisioning and configuration tasks.
* The samples are organized in groups associated with Oracle Cloud Infrastructure services under [the samples directory on GitHub](https://github.com/oracle/oci-ansible-collections/tree/master/samples).
Begin by reviewing the Readme.md file that you will find in each sample's root directory.
* The solutions are available under [the solutions directory on GitHub](https://github.com/oracle/oci-ansible-collections/tree/master/solutions)

## Documentation
Module HTML documentation is available on [readthedocs.io](https://oci-ansible-collection.readthedocs.io/en/latest/collections/oracle/oci/index.html).

To view the module documentation, use this command:
  ``` bash
ansible-doc oracle.oci.[module_name]
  ```
General documentation can be found [here](https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/ansible.htm).

## Ansible Tower and AWX
Oracle Cloud Infrastructure Ansible Collection supports Ansible Tower and AWX. For more information on how to setup the collection with Ansible Tower, follow the [instructions in this blog](https://blogs.oracle.com/cloud-infrastructure/using-oracle-cloud-infrastructure-with-ansible-tower-and-awx).
To install the Ansible Tower free version (AWX) on an OCI instance, use this [solution](https://github.com/oracle-quickstart/oci-ansible-awx).

## Help
- For FAQs, check the [Frequently Asked Questions](https://github.com/oracle/oci-ansible-collections/blob/master/FAQ.md) page.
- For commmon issues, check the [Common Issues](https://github.com/oracle/oci-ansible-collections/blob/master/COMMON_ISSUES.md) page.
- To file bugs or feature requests, use [GitHub issues](https://github.com/oracle/oci-ansible-collections/issues).
- For other channels, check the ["Questions or Feedback"](https://docs.cloud.oracle.com/en-us/iaas/Content/API/SDKDocs/ansible.htm#questions) section.

## Changes

See [CHANGELOG](https://github.com/oracle/oci-ansible-collections/blob/master/CHANGELOG.md).

## Contributing

This is an open source project. See [CONTRIBUTING](https://github.com/oracle/oci-ansible-collections/blob/master/CONTRIBUTING.md) for details.

Oracle gratefully acknowledges the contributions to `oci-ansible-collections` that have been made by the community.

## Known Issues

You can find information on any known issues on [Known Issues](https://github.com/oracle/oci-ansible-collections/blob/master/KNOWN_ISSUES.md) or [GitHub issues](https://github.com/oracle/oci-ansible-collections/issues) page.

## License

Copyright (c) 2020, Oracle and/or its affiliates.

This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.

See [LICENSE.txt](https://github.com/oracle/oci-ansible-collections/blob/master/LICENSE.txt) for more details.
