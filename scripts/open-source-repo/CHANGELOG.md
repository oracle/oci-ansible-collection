# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.12.0] - 2019-10-14

### Added
- Added OCI Inventory Plugin
- Added modules to manage [Network Security Groups](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/networksecuritygroups.htm)
  - oci_network_security_group
  - oci_network_security_group_facts
- Added modules to manage [Budgets](https://docs.cloud.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm)
  - oci_budget
  - oci_budget_facts
  - oci_budget_alert_rule
  - oci_budget_alert_rule_facts
- Added the following action modules
  - oci_volume_backup_actions
  - oci_object_storage_bucket_actions
  - oci_image_actions
  - oci_identity_identity_provider_actions

## [1.11.0] - 2019-09-16

### Added
- Added modules to manage [Exadata DB Systems](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaoverview.htm)
  - oci_autonomous_exadata_infrastructure
  - oci_autonomous_exadata_infrastructure_facts
  - oci_autonomous_exadata_infrastructure_shape_facts
- Added modules to manage [Tag Defaults](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingtagdefaults.htm)
  - oci_tag_default
  - oci_tag_default_facts
- Added modules to manage [Audit](https://docs.cloud.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm)
  - oci_audit_event_facts
  - oci_configuration
  - oci_configuration_facts
- Added [Object Lifecycle Policy](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm) modules
  - oci_object_storage_object_lifecycle_policy
  - oci_object_storage_object_lifecycle_policy_facts
- Added [Autoscaling](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm) modules
  - oci_auto_scaling_configuration
  - oci_auto_scaling_configuration_facts
  - oci_auto_scaling_configuration_policy
  - oci_auto_scaling_configuration_policy_facts
- Added `oci_image_actions` module to support exporting an image.

### Changed
- Minimum supported OCI Python SDK to `2.2.21`

### Deprecated
- In `oci_instance` module, these options: exact_count, count_tag, max_thread_count and enable_parallel_requests are deprecated. Use oci_instance_pool module instead to create, update, terminate multiple instances.
- The `oci_swift_password` and `oci_swift_password_facts` modules have been removed. Use `oci_auth_token` and `oci_auth_token_facts` instead.

### Breaking Change
- In `oci_local_peering_gateway` module, the default value for skip_exhaustive_search_for_lpg_peerings is changed to True instead of False.

## [1.10.0] - 2019-07-12

### Added
- Fact modules `oci_namespace_facts` and `oci_namespace_metadata_facts` modules to fetch object storage namespace details.
- Added the following features in existing modules:
    - Add support for ObjectReadWithoutList access_type for buckets `oci_bucket` module.

### Changed
- Minimum supported OCI Python SDK to `2.2.13`

### Breaking Change
- In multiple volume modules, the type for the return value `attached_instance_information` is changed to a list instead of a dict.
  This will support returning multiple attached instances to a volume.
- In `oci_local_peering_gateway` module, the default value for `skip_exhaustive_search_for_lpg_peerings` is changed to `True` instead of `False`.
  
## [1.9.0] - 2019-06-01

### Added
- Added the following features in existing modules:
    - Added `iscsi_attach_commands` and `iscsi_detach_commands` return values to `oci_volume_attachment` and `oci_volume_attachment_facts` modules. 

### Fixed
- Fix installation script for Ansible 2.8.0 [issue](https://github.com/oracle/oci-ansible-modules/issues/53)
- Fix idempotency when updating a route table entry [issue](https://github.com/oracle/oci-ansible-modules/issues/52)
- Fix invalid options error for FQDN generation in inventory script [issue](https://github.com/oracle/oci-ansible-modules/pull/49)
- Fix error updating cross connects on a virtual circuit

## [1.8.0] - 2019-05-01

### Added
- Added modules to manage:
    - [Web Application Firewall Service](https://docs.cloud.oracle.com/iaas/Content/WAF/Concepts/overview.htm)
    - [Federating with Identity Providers](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/federation.htm)
    - [Oracle Identity Cloud Service Group Mapping](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm)
- Added the following features in existing modules:
    - New allowed values `approximateSize` and `approximateCount` for the `fields` parameter of `oci_bucket_facts` module.  These enable populating `approximate_size` and `approximate_count` in the response.
    - Adding 'primary_private_ip' and 'primary_public_ip' addresses to instance module
- Samples to demonstrate:
  - how to a launch compute instance using an app catalog image

### Changed
- Minimum supported OCI Python SDK to `2.1.7`

### Fixed
- Download an object from a bucket fails if file destination does not exists [issue](https://github.com/oracle/oci-ansible-modules/issues/46)
- OCI ansible module are not respecting LOG_PATH [issue](https://github.com/oracle/oci-ansible-modules/issues/43)
- Update version of Python SDK [issue](https://github.com/oracle/oci-ansible-modules/issues/42)
- 'oci_security_list' should handle int values for ports in playbook

## [1.7.0] - 2019-04-01

### Added
- Added the following features in existing modules:
    - Option to specify `boot_volume_size_in_gbs` with a create operation in `oci_instance` module
    - Options to specify `launch_mode` and `source_image_type` in `oci_image` module
    - Support for retrieving `primary_private_ip` and `primary_public_ip` in `oci_instance_facts` module
- Added the following features in OCI dynamic inventory script:
    - Option to pass hostname format as command line parameter and environment variable
    - Option to enable strict hostname checking
- Samples to demonstrate:
  - how to list objects from all the buckets in a compartment

## [1.6.0] - 2019-02-28

### Added
- Modules to manage
    - AppCatalog [Listings](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/AppCatalogListing/), [Subscriptions](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/AppCatalogSubscription/), and [Agreements](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/AppCatalogListingResourceVersionAgreements/) to work with Oracle and Partner images published in the Partner Images Catalog.
- Added the following features in existing modules:
    - Option to specify `route_table_id` with a create or an update operation in `oci_local_peering_gateway` module
    - Option to create and download a database wallet from Autonomous Transaction Processing and Autonomous Data Warehouse databases in `oci_autonomous_database` and `oci_autonomous_data_warehouse` modules
    - Option to create DB System from a source(backup) in `oci_db_system` module
- Added the following features in OCI dynamic inventory script:
    - Option to build inventory of a given compartment using its OCID

## [1.5.0] - 2019-01-28

### Added
- Modules to manage
    - [FastConnect](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm) resources
- Added the following features in existing modules:
    - [Pre-Authenticated Requests](https://docs.cloud.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm) in Object Storage Service.
    - `force` option in `oci_bucket` now also supports automatic deletion of bucket-level PARs
    - Support for listing multi-part uploads and multi-part upload parts, aborting a multi-part upload in `oci_object_facts` and `oci_object` modules
    - In modules having a module option that supports a list of items, a `delete_*` option is now supported to delete specified list items. See `delete_security_rules` in `oci_security_list` for an example
    - Options in `oci_tag` module to apply tags
    - Option to filter by `display_name` in `oci_instance_configuration_facts` module
- Added the following features in OCI dynamic inventory script:
    - Option to build inventory from multiple regions

### Changed
- Minimum supported OCI Python SDK to `2.1.3`

## [1.4.0] - 2018-12-19

### Added
- Modules to manage
    - [Cost tracking tags](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/taggingoverview.htm#UsingCostTrackingTags)
    - [Retrieving initial credentials of Windows instances](https://docs.cloud.oracle.com/iaas/Content/GSG/Tasks/launchinginstanceWindows.htm)
- Added the following features in existing modules:
    - Support for creating nested compartments and deleting compartments in `oci_compartment` module
    - Support for retrieving information of nested compartments in `oci_compartment_facts` module 
    - Support specification of cost-tracking during tag definition creation in the `oci_tags` module
    - Support for multi-part uploads and parallel uploads in `oci_object` module
- Added the following features in OCI dynamic inventory script:
    - Options to parallelise the inventory generation
    - Options to build inventory of only specific tagged instances
    - Option to build inventory of entire hierarchy under a given compartment
- Samples to demonstrate:
  - how to give compute instances private access to OCI Object Storage using Service Gateway
  - how to enable internet access to a private instance using NAT Gateway

## [1.3.0] - 2018-11-16

### Added
- Modules to manage
  - [NAT gateways](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)
  - [Volume groups](https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/volumegroups.htm)
  - [Volume group backups](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/VolumeGroupBackup)
  - [Policy-based volume backups](https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm)
  - [Auth Tokens](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm?Highlight=Auth%20tokens#two)
  - [Instance console connections](https://docs.cloud.oracle.com/iaas/Content/Compute/References/serialconsole.htm)
  - [Serial console data/Console history](https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/displayingconsole.htm)
  - [Instance Configurations and Instance Pools](https://docs.cloud.oracle.com/iaas/Content/Compute/Concepts/instancemanagement.htm)
- Support for the following services:
  - [Oracle Cloud Infrastructure File Storage Service](https://docs.cloud.oracle.com/iaas/Content/File/Concepts/filestorageoverview.htm)
  - [Oracle Cloud Infrastructure Email Delivery Service](https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm)
- Added the following features in existing modules:
  - Options in `oci_boot_volume` module to support creating boot volumes
  - Option in `oci_volume` module to support assigning a backup policy while creating a volume
  - Enhanced wait support in `oci_node_pool` module
  - Provision and terminate `exact_count` instances in parallel in the `oci_instance` module
  - `oci_route_table` and `oci_security_list` supports the specification of a Service (via a Service Gateway) as a
    destination/source for route and security rules.
  - The `oci_inventory.py` dynamic inventory script supports Instance Principal authorization.
- Samples to demonstrate:
  - creating a File System and mounting it in a Compute instance and how to create a File system snapshot
  - how a File System can be exported using two different export paths on two different mount targets
  - how a Serial and VNC connection can be created for a compute instance
  - how to create an instance pool to launch a set of compute instances based on an instance configuration

### Changed
- Minimum supported OCI Python SDK to `2.1.0`
- Type of module option `block_traffic` in oci_service_gateway module changed to `bool`

### Deprecated
- The `oci_swift_password` and `oci_swift_password_facts` modules have been deprecated. Use `oci_auth_token` and `oci_auth_token_facts` instead.
- The `cidr_block` sub-option in the `route_rules` option of `oci_route_rules` is deprecated. Use `destination` and `destination_type` (equal to `CIDR_BLOCK`) instead to specify a destination IP address in CIDR notation as the destination target for a route rule.

## [1.2.0] - 2018-10-03

### Added
- Modules to manage
  - [Dynamic Routing Gateways(DRGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm)
  - [Customer Premises Equipments(CPEs)](https://docs.cloud.oracle.com/iaas/api/#/en/iaas/20160918/Cpe/)
  - [IPSec Connections](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingIPsec.htm)
  - [Local Peering Gateways(LPGs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/localVCNpeering.htm)
  - [Remote Peering Connections(RPCs)](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
  - [Service Gateways](https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm)
- Support for the following services:
    - [Oracle Cloud Infrastructure Autonomous Transaction Processing](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/atpoverview.htm)
    - [Oracle Cloud Infrastructure Autonomous Data Warehouse](https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/adwoverview.htm)
    - [Oracle Cloud Infrastructure Search](https://docs.cloud.oracle.com/iaas/Content/Search/Concepts/queryoverview.htm)
- Samples to demonstrate:
    - provisioning and managing an Oracle Cloud Infrastructure Autonomous Transaction Processing Database and an
      Autonomous Data Warehouse
    - provisioning a virtual cloud network (VCN) with private subnets and an IPSec VPN(using a dynamic routing gateway,
      a customer premises equipment and an IPSec connection)
- Fact modules now support additional filter options (where applicable) for you to filter resources

## [1.1.0] - 2018-09-06

### Added
- Support for following services:
  - [Oracle Container Engine for Kubernetes Service (OKE)](https://docs.cloud.oracle.com/iaas/Content/ContEng/Concepts/contengoverview.htm)
  - [Oracle Domain Name System (DNS) Service](https://docs.cloud.oracle.com/iaas/Content/DNS/Concepts/dnszonemanagement.htm)
- Modules to manage [IAM dynamic groups](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
- Support for [instance principal authorization](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm)
- Support wait options in load balancer service modules
- Support filtering of resources in facts modules using `display_name` or `name`
- Support to automatically redirect IAM operations to home region of tenancy
- Support for [Fault Domains](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)
- Added samples to demonstrate:
  - the use of instance principal authorization
  - setting up prerequisites for OKE, provisioning OKE cluster and deploying a sample application
  - provisioning of a load balancer component in the Secure MongoDB deployment solution

### Changed
- Minimum supported OCI Python SDK to 2.0.2

## [1.0.0] - 2018-07-09

### Added
- In this first release of the OCI Ansible modules, the following Services are supported:
  - Compute
  - Block Storage
  - Object Storage
  - Networking
  - Load Balancer
  - Database Service
  - Identity and Access Management
- Provides a dynamic inventory script `oci_inventory.py` that helps you fetch the latest set of OCI compute instances and make them available for your playbooks to be executed upon.
- Includes a catalog of Oracle Cloud Infrastructure Ansible module samples, in the [samples](samples) directory, that illustrate using the modules to carry out common infrastructure provisioning and configuration tasks.
