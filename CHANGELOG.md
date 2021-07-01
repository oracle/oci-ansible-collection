# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.25.0] - 2021-07-01

## Added
- Elastic Storage feature for Exadata Infrastructure and Vm Cluster resources for ExaCC
- Support for migrating OKE cluster with a public Kubernetes API Endpoint that is not integrated with your VCN to a VCN-Native cluster (more secure)
- Support for managing container scan recipes and targets in Vulnerability Scanning Service
- Support to update iscsiLoginState for a VolumeAttachment
- `encryption_in_transit_type` parameter in `oci_compute_volume_attachment` module
- `parameters_config` parameter in `oci_management_dashboard_actions` module.
- `parameters_map` sub-parameter under `tiles` parameter in `oci_management_dashboard_actions` module
- Support for 'host_name' and 'is_database_instance_level_metrics' parameters in Operations Insights (opsi) service
- Data Safe support for registration and management of target databases.
- support for sparkVersion property in the DataFlow Application
- support for `is_data_ever_ingested` return parameter for `log_analytics_namespace` modules.

## Fixed
- Instance configuration creation from instance issue
- logging file permission issue

## Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## Breaking
- For Management Dashboard Service, fields `freeform_tags` and `defined_tags` removed from the response for the action `export_dashboard`.
- For DataFlow Application, property spark_version is required for create

## [2.24.0] - 2021-06-17

## Added
- Support for filtering options `exclude_host_filters` and `include_host_filters` in the Inventory plugin. Both 
  options take a list of Jinja2 conditional expressions.
- Support for Java Management Service
- Support for Database Migration Service
- Support for Application Performance Monitoring Control Plane
- Support for Application Performance Monitoring Synthetic Monitoring
- Support for configure autonomous database KMS key
- Support for creating database software images from an existing db-home
- Support for listing Secret Bundles by secret name and valultId

## Fixed
- Inventory plugin issue for VMWare instances.
- Idempotency for Generic Artifact Content upload.

## Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## [2.23.0] - 2021-06-03

## Added
- Option hostname_format_preferences in inventory plugin which allows a list of preferred hostname formats which can be specified using jinja 2 template expressions
- Support for OCI Bastion service
- Support for Generic Artifacts Service
- Support in Database Management Service for getting the AWR database report for the specific database
- Support in Database Management Service for getting the AWR SQL report for a specific SQL
- Support in Database Management Service to list the AWR snapshots of the specified database
- Support in Database Management Service to list AWR database information on snapshot
- Support for getting Automatic Workload Repository (AWR) data on external databases in the Database Management service
- Support for new field `isDynamic` in the response objects of (`oci limits definition list`) command
- Support for creation of Notebook Sessions with larger block volumes through the Data Science service
- Support for the VM.Standard.E3.Flex Flexible Compute Shape with customizable OCPUs and memory for Data Science Notebooks
- Support for getting billable image sizes in the Compute service
- Support for Object Storage Configuration Source for Resource Manager Service
- Support for database maintenance run patch modes in the Database service
- Support for spark-submit compatible options in DataFlow service
- Support for the HCX Enterprise add-on in the VMware Solution service

## Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## [2.22.0] - 2021-05-20

## Added
- Support for Golden Gate service
- Support for Marketplace Service Catalog
- Operations Insights support for Enterprise Manager external databases and Management Agent Service managed external databases and hosts
- Support for enabling and disabling Operations Insights for External Non-Container and External Pluggable Databases.
- Support for Data Masking in cloud guard
- Support for autonomous database on Exadata Cloud at Customer infrastructure patching in the Database service
- Support for getting a list of tablespaces for a specified Managed Database
- Support for getting the list of database parameters for the specified Managed Database. The parameters are listed in alphabetical order, along with their current values.
- Support for changing the database parameters' values for the specified Managed Database
- Support for resetting the database parameters' values to their default or startup values for the specified Managed Database.
- Support for getting RAC related details for a fleet of databases, managed database, and summary metrics as part of Database Management Service
- Improved announcement email preferences by introducing preference types Opt-In Tenant Announcement, Opt-In Tenant And Informational Announcements, and Opt-Out All Announcements options
- Support for SDK resource in Apigatway service
- Support `change_compartment` action in `compute_management_instance_configuration`
- Added db_system_display_name, region hostvars for db hosts in inventory plugin
- Support for Vault actions - `create_vault_replica`, `delete_vault_replica` and `change_compartment`
- `oci_database_db_node_facts` module now returns `primary_public_ip` and `primary_private_ip` as well

## Fixed
- DB Home patching with database software image issue
- Duplicate aliases for parameters `instance_pool_id` and `instance_id` in the module `oci_compute_management_instance_pool_instance_facts` module. Now only `instance_pool_id` has the alias `id`
- Idempotence issue for `remove_export_drg_route_distribution` action in `oci_network_drg_attachment_actions` module

## Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## [2.21.0] - 2021-05-06

## Added
- Support for `delegation_token` based authentication for Inventory Plugin
- Support for forceful deletion of a non-empty Object Storage bucket
- Support for business name annotation of harvested objects in Data Catalog
- Support to customer contacts feature for autonomous database
- Support for `display_name` to be used in the hostname_format of the inventory plugin for compute instances
- Introducing Graph Studio Url option in the connection urls
- Expanding DRG functionality in the Networking Service
     - More than one VCN can be attached to a DRG
     - Flexible routing inside DRG enables packet flow between any two attachments
     - Routing policy to customize dynamic import/export of routes
- Support for opt out of DNS record during instance launch, as well as attaching secondary VNICs
- Support for option to opt-in and opt-out of live migration at an instance level
- Support for mutable sizes on cluster networks 
- Support for SDK generation feature in the API Gateway service
- Support for KMS Cross Regional Replication of Keys
- Support for request validation policies within the deployment specification in the API Gateway service
- Support to configure an API Gateway with an external RESP-compliant response cache and to configure response caching on a per-route basis for Deployments
- `purge_route_rules` and `delete_route_rules` options to `oci_network_route_table` module to allow adding and deleting specific rules
- Support for setting the auto-tiering property for a bucket
- Support for creation, updation and deletion of `entity_type` for Log Analytics.
- Support for `resource_action` in `policies` declaration in `autoscaling` service

## Fixed
- Idempotence issue for `bulk_add_virtual_circuit_public_prefixes` and `bulk_delete_virtual_circuit_public_prefixes` actions in `oci_network_virtual_circuit_actions` module
- Issue with logging exceptions in inventory plugin

## Changed
- Updated python supported versions to >=3.6 in the documentation
- Parameter `specification` is marked optional for API deployment create in the API Gateway service
- `vcn_id` is now optional for listing vlans in `oci_network_vlan_facts` module
- corporate proxy field is now optional when a creating exadata infrastructure
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## [2.20.0] - 2021-04-22

## Added
- Support for Ipv6
- Support for Network Topology service
- Support for [preemptible instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/preemptible.htm) in the Compute service
- Support for burstable instances in the Compute service
- Support for `routing_policy` in virtual circuit
- Support for configuring APM tracing functionality for Application and Functions resources.
- Support for Streaming Analytics feature in Service Connector Hub.
- Support for Read/Write-Any object from buckets using Pre-authenticated Request (PAR) in Object Storage. Support for restricting PARs by prefix and for listing object.
- Support for showing if a contact for Exadata Infrastructure is valid in MOS (My Oracle Support) and if Exadata Infrastructure is in Degraded SLO state.
- Support for os updating cloud vm cluster
- Support for Data Guard with Autonomous Container Databases on Exadata Cloud @ Customer Infrastructure
- Support to specify Peer ACD unique name when creating Data Guard enabled Autonomous Container Database on Exadata Cloud@Customer
- Access Control List support for Autonomous Database with Data Guard enabled on Exadata Cloud@Customer
- Support for `scan_dns_name` and `zone_id` as part of Dbsystem/CloudVmCluster/AutonomousExadataInfrastructure API response.
- Support for additional upgrade options supported by DBUA(Database Upgrade Assistant)
- Support for fractional support for resource usage and availability service limit api
- Support for data_science model_deployment module and model_deployment_shape_facts module
- Support for container image signing
- Support for cluster features as a part of the Container Engine for Kubernetes Service
- Support for Oracle Cloud VMware Solution Flexible Billing
- compartment name to the hostvars of OCI Inventory Plugin

## Fixed
- Issue with debug logging in inventory plugin when there is a service error

## Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## Deprecated:
- Module `oci_load_balancer_routing_policy` is deprecated,  
  use `oci_loadbalancer_routing_policy` instead
- Module `oci_load_balancer_routing_policy_facts` is deprecated,  
  use `oci_loadbalancer_routing_policy_facts` instead

## [2.19.0] - 2021-04-08

## Added
- Support for resource principal authentication
- Support for Network Load Balancer
- Support for OCI Vulnerability Scanning Service
- Support for compute capacity reservation
- Support for attaching and detaching compute instance to an instance pool
- Support for vSphere 7.0 in the VMware Solution service
- Support for Marketplace Publications
- Support for highly-available MySQL DB Systems
- Support for private_access_channel and vanity_url in Analytics service
- HeatWave (in-memory analytics accelerator) support for the MySQL Database Service. (Renaming Analytics Service to HeatWave)
- Support for Oracle Enterprise Manager bridges, source auto-association, source event type mappings, and plugins to upload data in the Logging Analytics service
- Support for nosql table change compartment

## Fixed
- Updated the modules `oci_resource_manager_stack_tf_state_facts` and `oci_resource_manager_job_tf_state_facts` to write the output to the given file
- Idempotence for resource manager stack creation `oci_resource_manager_stack` via private templates
- Inventory plugin to return hostsvars for db hosts

### Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)
- pyyaml requirement version from 5.1.2 to 5.4 in oci-cloudnative solution

## [2.18.0] - 2021-03-25

## Added

- Support change compartment for all the supported services (except database)
- Support for [Database groups](https://docs.oracle.com/en-us/iaas/database-management/doc/create-and-use-database-groups.html) in Database management service
- Support for Routing Policies in Load Balancer Service
- Support for Auto-Scale Configs in Big Data Service
- Support for Log Analytics Log groups and entities
- Support for File System Service Clones Feature
- Support for enabling disabling message map flag on SCH Service
- Support for SMS subscriptions through the Oracle Cloud Infrastructure Notifications service
- Support for searching OCI resources in another tenancy
- Support updating OCE instance usage type
- Support for private clusters to the Container Engine for Kubernetes service
- Modules `oci_opsi_database_insights_facts` and `oci_opsi_sql_searches_facts` in opsi service

### Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

### Deprecated:
- Module `oci_apigateway_waas_certificate_facts` is deprecated use `oci_apigateway_certificate_facts` instead
- Module `oci_apigateway_waas_certificate` is deprecated use `oci_apigateway_certificate` instead

## [2.17.0] - 2021-03-11

### Added
- Support for the OCI Registry Service
- Support for enabling and disabling database management for external database
- Support for listing recommendation strategies in the optimizer service
- Support for providing target tags and target compartments on profiles in the optimizer service
- Support for custom endpoint feature in the Integration Service
- Support for change network endpoint for integration instance in Integration Service
- `primary_vnic_only` option in inventory plugin to process only the primary vnic of a compute instance

### Fixed
- Return documentation for `oci_object_storage_object_actions` module

### Changed
- Python 2 reached end of life on 1st January, 2020 and [OCI Python SDK](https://github.com/oracle/oci-python-sdk) stopped support for Python 2 long back. We cannot support Python 2 since we have a hard dependency on [OCI Python SDK](https://github.com/oracle/oci-python-sdk). We strongly recommend you to move to Python 3 if you are still using Python 2
- `resource_action_ids` parameter is made optional in `oci_optimizer_recommendation_actions` module
- Parameter `name` is now updatable in `oci_optimizer_profile`
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk)

## [2.16.0] - 2021-2-25

### Added
- Support for [external databases](https://docs.oracle.com/en-us/iaas/Content/Database/Concepts/externaloverview.htm)
- Support for importing and exporting Management Dashboards.
- Support for exporting an existing running VM, or a copy of VM, into a VMDK, QCOW2, VDI, VHD, or OCI formatted image in the Compute service
- Support for platform configurations on instances in the Compute service
- Support for enabling and disabling Oracle Cloud Agent plugins in the Compute service
- Support for NG-VPN Multiple Encryption Domain and Public Logging
- Support for listing available plugins and for getting the status of plugins in the Oracle Cloud Agent service
- Support for listing errata in the OS Management service
- Support for returning object metadata and other header information in object modules. Resolves [Github Issue](https://github.com/oracle/oci-ansible-collection/issues/37)
- Support for load balancer shape update for a BlockchainPlatform

### Fixed
- Issue with re-encrypt object action return value.
- Issue with inventory plugin generating inventory for instances with multiple vnics having valid hostname_format for secondary vnics but not the primary vnic.

### Changed
- Please update to the latest version of [OCI Python SDK](https://github.com/oracle/oci-python-sdk).
- Disabled the logs for inventory plugin by default to reduce the noise. Can be enabled using the `debug` flag.

### Breaking Changes
- Parameter idcs_access_token is now required to create a blockchain platform in `oci_blockchain_platform` module


## [2.15.0] - 2021-2-11

### Added
- Support for [Cloud Advisor](https://docs.oracle.com/en-us/iaas/Content/CloudAdvisor/Tasks/cloudadvisor-getting_started.htm).
- Support for [Resource Manager Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm)
- Support for update_object_storage_tier action in Object Module of Object Storage service.
- Support for assigning volume backup policies to volume groups.
- Added [verified](https://docs.oracle.com/en-us/iaas/api/#/en/key/release/VerifiedData/Verify) and [signed](https://docs.oracle.com/en-us/iaas/api/#/en/key/release/SignedData/Sign) data modules for key management service
- Added new param `fetch_compute_hosts` in inventory plugin, to fix [this issue](https://github.com/oracle/oci-ansible-collection/issues/40)
- Support for creating dataguard association on existing standby existing database home. Added new parameter `peer_db_home_id` to module `oci_database_data_guard_association`.
- Support for listing database homes by version.
- Support for Autonomous Data Guard for Autonomous Infrastructure.
- Sample to create boot-volume from an existing instance.
- Sample to create and connect local peering gateways.

### Changed:
- Please update to the latest version of OCI Python SDK


## [2.14.0] - 2021-1-28

### Added
- Added modules to manage [Data Safe On-Premises Connector](https://docs.oracle.com/en-us/iaas/data-safe/doc/register-onpremises-oracle-databases-using-oracle-data-safe-onpremises-connector.html)
- Support for resetting and resuming mysql channel (`oci_mysql_channel_actions` module)
- Create dataguard association with standby database from given database software image.
- Support for precheck, upgrade and rollback in `oci_database_database_actions`
- `oci_marketplace_tax_facts` module
- `oci_data_catalog_custom_property_facts` module
- Added parameters `batch_rollover_size_in_mbs`, `batch_rollover_time_in_ms` and `log_group_id` in `oci_sch_service_connector`
- Sample to create a custom image from an instance
- Sample to create a vlan
- Sample to create a Private Load Balancer
- Sample to create public and private DNS

### Fixed
- Issue https://github.com/oracle/oci-ansible-collection/issues/15
- Issue https://github.com/oracle/oci-ansible-collection/issues/35

### Breaking changes
- Parameters `freeform_tags` and `defined_tags` are **removed** from `oci_data_safe_configuration` module
- Parameter compartment_id is **required** to list multiple `data_safe_private_endpoint`s in `oci_data_safe_private_endpoint_facts` module

### Changed:
- Please update to the latest version of OCI Python SDK (2.28.0)


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
