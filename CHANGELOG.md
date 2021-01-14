# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.13.0] - 2021-1-13

### Added
- Added new modules and features in core service
- Added new modules and features in database service
- Added new modules and features in load balancer service
- Added new features in identity service
- Added new features in resource manager service
- Added new features in key management service
- Added new features in usage service
- Added new features and modules in mysql
- Added new features in object_storage service

### Solutions and Samples
- Updated Database Patching solution
- Added sample for creating autoscaling configuration
- Refactored the name of the muShop solution

### Changed:
- Please update to the latest version of OCI Python SDK (2.27.0)


## [2.12.0] - 2020-12-23

### Added
- Added support for multiple CIDRs in `oci_network_vcn`
- Added `instance_options` parameter in `oci_compute_instance` and related modules
- Added `oci_management_agent_availability_history_facts` module
- New modules and features in MySQL service. Added modules to manage MySQL Analytics Engine.
- Added new modules and features in Database service.
- Added new features to Load Balancing service.
- Added new features to functions service.
- Added new module and features to Identity service.
- Added new features to Container Engine service.
- Added new features to Blockchain service.
- Added new features to NoSQL service
- Added the `debug` option to inventory plugin

### Fixes
- Fixed the logging for inventory plugin and added warnings

### Solutions
- Added Database Patching solution

### Changed:
- Please update to the latest version of OCI Python SDK (2.26.0)

## [2.11.0] - 2020-11-19

### Added
- Support for Private DNS
- Support for BYOIP
- New Compute Samples
- New always-free solutions
- New samples for File Storage, Load Balancing & Networking.
- Added Compute-Instance-Agent service (Oracle Cloud Agent API)
- Added new modules and features to Data-Catalog service
- Added features to multiple core and vmware (ocvp) modules
- Added new features to Integration modules.
- Added new features and modules to Data Flow service.
- Added `oci_management_agent_plugin_facts` module

### Fixes
- Password return issue on creation of SMTP_credential creation [Github issue link](https://github.com/oracle/oci-ansible-collection/issues/29)
- Fixed the `oci_identity_compartment` create example in the module

### Changed:
- Please update to the latest version of OCI Python SDK (2.24.0)

### Deprecated:
- Module `oci_monitoring_suppression_actions` is deprecated use `oci_monitoring_alarm_actions` instead.

## [2.10.0] - 2020-10-29

### Added:
- New modules & features for database service. Added support for resources cloud exdata infrastructure, cloud vm cluster, database software image
- New modules and features in KMS service. Added support for protection_mode.
- New features added for container engine (OKE) service.
- New features added for object storage service.
- New features and modules added for apigateway service.
- Added options to set the api_user_private_key and api_user_pass_phrase in the oci_inventory plugin
- New Identity samples.

### Fixes
- Inventory plugin issues: [fetch_hosts_from_subcompartments](https://github.com/oracle/oci-ansible-collection/issues/25)

### Changed:
- Please update to the latest version of OCI Python SDK (2.23.2)

## [2.9.0] - 2020-10-15

### Added:
- Modules for management agent service
- Modules for cloud-guard service
- Modules for unified agent configuration
- Add logging analytics - namespace modules
- Add availability_config parameter in instance modules
- New [samples](https://github.com/oracle/oci-ansible-collection/tree/v2.8.0/samples/compute)

### Fixes
- Inventory plugin issues: Filtering options, Host FQDN lookup
- Updated the description and current use of flags for `compartments` in inventory plugin

### Changed:
- Please update to the latest version of OCI Python SDK (2.23.0)

## [2.8.0] - 2020-9-24

### Added:
- Added [Blockchain](https://docs.cloud.oracle.com/en-us/iaas/blockchain-platform/index.html) service modules
- Added [Service Connector Hub (SCH)](https://docs.cloud.oracle.com/en-us/iaas/Content/service-connector-hub/overview.htm) modules
- Added new features in [Inventory Plugin](https://github.com/oracle/oci-ansible-collection/blob/master/plugins/inventory/oci.py) (List Database VMs and other enhancements)
- Added new [samples](https://github.com/oracle/oci-ansible-collection/tree/master/samples)
- Added [Logging service](https://docs.cloud.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm) modules
- Added new features for Identity (bulk_delete_tags and cascade_delete_tag_namespace)
- Added new features for load_balancer service

### Changed:
- Please update to the latest version of OCI Python SDK (2.21.5).

## [2.7.0] - 2020-9-10

### Added:
- Added VMWare (ocvp) modules
- Added Data Integration Workspace modules
- Added multiple Database modules and features
- Added Network modules, features and support for it
- Added features for Budget service
- Added multiple Identity modules and features
- Added support for auto_backup_window in Database service

### Changed:
- Please update to the latest version of OCI Python SDK (2.21.3).

### Fixes:
- Removed the redirect to home region in these modules oci_identity_fault_domain_facts 
and oci_identity_availability_domain_facts.

## [2.6.0] - 2020-8-27

### Added:
- Added Big Data modules
- Added Usage modules
- Added multiple Database modules and features
- Added support for Database VM cluster and Exadata Infrastructure
- Added multiple Identity modules and features

### Changed:
- Please update to the latest version of OCI Python SDK.


## [2.5.0] - 2020-8-6

### Added:
- Added Analytics modules
- Added Web Application Acceleration and Security Services modules
- Added Limits modules
- Added Data Science modules
- Added Data Safe modules
- Added Data Catalog modules
- Added Data Flow modules
- Added Search modules
- Added Digital Assistant Instance modules
- Added MySQL modules
- Added `oci_monitoring_alarm_actions` module
- Added multiple loadbalancer features.
- Added `oci_loadbalancer_network_security_groups`, `oci_loadbalancer_listener_rule_facts` modules

### Changed:
- Please update to the latest version of OCI Python SDK.


## [2.4.0] - 2020-7-16

### Added:
- Added Resource Manager modules
- Added Announcement modules
- Added Integration modules
- Added NoSQL modules
- Added Events modules
- Added Service Limits modules
- Added API Gateway modules
- Added Content and Experience modules
- Added samples for Container Engine and Block Volume

### Changed:
- Please update to the latest version of OCI Python SDK.


## [2.3.0] - 2020-7-2

### Added:
- Added OS Management modules

### Fixed:
- `name` parameter in `oci_healthchecks_health_checks_vantage_point_facts` previously did not work because there was a conflict between the `name` alias for `display_name` parameter and the `name` module parameter.  This resulted in no results being returned when `name` parameter was specified, this issue is now resolved.

## [2.2.0] - 2020-6-25

### Added:
- Added Domain Name System (DNS) modules
- Added Email modules
- Added Marketplace modules
- Added Monitoring modules
- Added Notifications modules
- Added Streaming modules
- Added Functions modules
- Added Database Data Guard modules
- Added new modules for Compute and Network
- Added subparameter `admission_controller_options` in the options parameter of module `oci_container_engine_cluster`
- Added `node_source_details` parameter in the `oci_container_engine_node_pool module`

### Changed:
- Please update to the latest version of OCI Python SDK.
- `compartment_id` parameter removed from `oci_database_maintenance_run.py`
  - This parameter was optional and was unused by the module so is being removed

## [2.1.2-Beta] - 2020-6-9

### Changed:
- Updated the README and MigrationGuide

## [2.1.0-Beta] - 2020-6-8

### Added:
- Added Database modules
- Added the following modules:
    - oci_blockstorage_boot_volume_kms_key
    - oci_blockstorage_boot_volume_kms_key_facts
    - oci_blockstorage_volume_kms_key
    - oci_blockstorage_volume_kms_key_facts
    - oci_compute_management_instance_pool_load_balancer_attachment_facts
    - oci_vault_secret
    - oci_vault_secret_version_facts
    - oci_vault_secret_facts
    - oci_vault_secret_version_actions
    - oci_vault_secret_actions
    - oci_secrets_secret_bundle_facts
    - oci_secrets_secret_bundle_version_facts

- Added new parameters to the following modules:
    - `backup_policy_id` in oci_blockstorage_boot_volume
    - `is_shareable` in oci_compute_volume_attachment
    - `fault_domains` in oci_compute_management_instance_pool
    - `purge_security_rules` and `delete_security_rules` in `oci_network_security_list`

### Changed:
- Removed the parameter `launch_options` in the module oci_compute_image.

## [2.0.0-Beta] - 2020-5-14

### Added:
New release of collection modules.

### Changed:
- Please update to the latest version of OCI Python SDK.
- Please expect a few breaking changes as we transition from legacy modules to the new collection modules.
We recommend you to refer to the [Migration Guide](https://github.com/oracle/oci-ansible-collections/blob/master/MigrationGuide.md) as you plan to migrate.
