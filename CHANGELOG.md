# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

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
