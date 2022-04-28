# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.49.0]

## Added

- Support for creating Enterprise Manager-based zLinux host targets, creating alarms, and viewing top process analytics in the Operations Insights service
- Fixed the lifecycle state values for target databases in the Data Safe service
- Support for specifying database edition and maximum CPU core count when creating or updating an autonomous database in the Database service
- Support for enabling and disabling data collection options when creating or updating Exadata Cloud at Customer VM clusters in the Database service
- Support for diagnostic reboots on VM instances in the Compute service
- Support for returning the number of network ports as part of listing shapes in the Compute service
- Support for bringing your own IPv6 addresses in the Networking service
- Support for new parameters for BGP admin state and enabling/disabling BFD in the Networking service


## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.65.0

## [2.48.0]

## Added

- Support for creating database systems and database homes using customer-managed keys in the Database service
- Support for virtual machines, bare metal machines, and Exadata databases with private endpoints in the Operations Insights service
- Support for CPS offline reports in the Database service
- Support for multi-AVM on Exadata Cloud at Customer infrastructure in the Database service
- Support for heterogeneous (VM and AVM) clusters on Exadata Cloud at Customer infrastructure in the Database service
- Support for custom maintenance schedules for AVM clusters on Exadata Cloud at Customer infrastructure in the Database service
- Support for setting the RECO storage size when updating a database system in the Database service
- Support for infrastructure patching v2 features in the Database service
- Support for auto-scaling the storage of an autonomous database in the Database service
- Support for cross-region cloning in the Database service
- Support for reporting excluded objects based on static exclusion rules and dynamic exclusion settings in the Database Migration service
- Updated documentation for Cross Region ADG feature for Autonomous Database in the Database service
- Support for international customers to consume and launch third-party paid listings in the Marketplace service
- Support for Ubuntu platforms and unlimited installation keys in the Management Agent Cloud service
- Support for creating Enterprise Manager-based Solaris/SunOS Host targets in the Operations Insights service
- Support for automatic tablespace creation on non-autonomous and autonomous database dedicated targets in the Database Migration service
- Support for removing, listing, and adding database objects reported by the Cloud Premigration Advisor Tool (CPAT) in the Database Migration service
- Support for dataset actions and global export formats in snapshot datasets in the Data Labeling service
- Support for adding labeling instructions to datasets in the Data Labeling service
- Support for custom logs in the Java Management service
- Support for Private OKE Clusters and Blue-Green Deployments in Devops Service
- Support for shielded instances in the VMWare Solution service
- Support for the Sales Accelerator license option in the Content Management service
- Support for specifying an image count when creating or updating container scan recipes in the Vulnerability Scanning service
- Troubleshooting guides for common errors faced in inventory plugin and service errors.

## Breaking
- Optional argument `repository_type` has been made required in `oci_devops_repository` module

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.63.0

## [2.47.0]

## Added
- Support for the AI Vision service
- Support for Data Connectivity service
- Support for optionally specifying an admin username and password when creating a database system during a restore operation in the MySQL Database service
- Support for setting deletion policies on database systems in the MySQL Database service
- Support for returning storage utilization details for `Deployment` modules in Golden Gate service
- Support for VCN hostname cluster endpoints in the Container Engine service
- Support for querying additional fields of a resource using return clauses in the Resource Search service
- Sample to create an Autonomous Transaction Processing Database on dedicated infrastructure


## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.62.0

## [2.46.0]

## Added

- Support for DRG route distribution statements to be specified with a new match type 'MATCH_ALL' for matching criteria in the Networking service
- Support for VCN route types on DRG attachments for deciding whether to import VCN CIDRs or subnet CIDRs into route rules in the Networking service
- Support for Autonomous Database Create with Auto Scaling Storage
- Support for shrinking an Autonomous Database
- Support for managed egress via a default networking option on jobs and notebooks in the Data Science service
- Support Storage Management in Database Management service
- Support for more types of saved search enums in the Management Dashboard service


## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.60.1

## [2.45.0]

## Added

- Support for ai_speech service
- Support for RAC Databases in GoldenGate Service
- Support for customer managed encryption keys for secrets stored in Analytics service
- Support for Announcements Subscriptions feature
- Support for upgrading and managing payment for subscriptions in the Account Management service (osp_gateway)

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.59.0

## [2.44.0]

## Added

- Support for Threat Intelligence service
- Support for more VM shape configurations when listing shapes in the Compute service
- Support for FastConnect device information in the Networking service
- Support for creation of NoSQL database tables with on-demand throughput capacity in the NoSQL Database Cloud service
- Support for listing fast launch job configurations in the Data Science service
- Support for filtering using `associated_resource_id` in `oci_data_safe_target_database_facts` module in Data safe service
- Return attributes `data_safe_nat_gateway_ip_address` and `global_settings` in configuration modules in Data safe service
- Return attribute `source_data_retention` in detector recipe module in Cloud guard service
- Attribute `risk_level` is made optional in the attribute `detector_rules` in detector recipe module in Cloud guard service


## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.58.0

## [2.43.0]

# 
 ## Added

 - Support for the Visual Builder service
 - Support for the Console Dashboard service
 - Support for tagging in the Container Engine for Kubernetes service
 - Support for capacity reservation in the Container Engine for Kubernetes service
## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.57.0

## [2.42.0]

## Added

- Support for fetching listings by image OCID in the Marketplace service
- Support for underscores and hyphens in project resource names in the DevOps service
 
## Changed

- Minimum required [OCI Python SDK]([https://github.com/oracle/oci-python-sdk]) changed to 2.56.0

## [2.41.0]

## Added

- Support for OneSubscription usage and organization subscription services
- Support for automatic start/stop at scheduled times in the Database service.
- Support for updating autonomous dataguard associations for autonomous container databases in the Database service.
- Support for setting up automatic failover when creating autonomous container databases in the Database service.
- Support for cloud VM cluster resources on autonomous dedicated databases in the Database service.

## Breaking

- Deprecated support for  module param `model_artifact` in the module `oci_data_science_model_artifact` for  `data science` service.
 
## Changed

- Minimum required [OCI Python SDK]([https://github.com/oracle/oci-python-sdk]) changed to 2.55.1

## [2.40.0] - 2022-01-27

## Added
- Support for OneSubscription billing schedule and subscription services
- Support for cross-region replication of volume groups in the Block Storage service
- Support for reconnecting refreshable clone to source for autonomous database on shared infrastructure in Database service
- Support to check if an autonomous database on shared infrastructure can be reconnected to source in Database service
- Support for update dataguard & select active dataguard during dataguard setup in Database service
- Support for KMS support for key version, key version OCIDs for autonomous database in Database service
- Support for boot volume encryption in the Container Engine for Kubernetes service
- Support for multiple protocols on the same listener in the Network Load Balancing service
- IPv6 support in the Network Load Balancing service

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.55.0

## [2.39.0] - 2021-01-20

## Added
- Support for invoice operations in the Account Management service (osp_gateway)
- Support for AWR hub integration in the Operations Insights service

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.54.1

## [2.38.0] - 2022-01-06

## Added
- Support for `Identity data plane` service.
- Support for `Resource Discovery and Monitoring` service
- Support for option `default_groups` in inventory plugin.
- Support for Categories, listing Entity Topology and verifying Scheduled Task for Log Analytics service.
- Support for DB password for users, in IAM, to login to their cloud db accounts for Identity service.
- Adding a new response type enum to the List Service Environments and Get Service Environment for Service Manager Proxy service.
- Automatically generate logical entities from filename patterns, relationships between business terms across glossaries in Data Catalog service.
- Support for node replacement in the VMWare Solution service.
- Support for External Hive Metastore for BDS service.
- Support for custom CA trust stores in the API Gateway service
- Troubleshooting Guides for common issues

## Fixed
- Idempotence issue (#140) in `oci_database_pluggable_database_actions` module.

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.53.1

## [2.37.0] - 2021-12-16

## Added
- Support for standard tags in the Identity service
- Support for enabling and disabling Database Management features for Autonomous Database
- Support SQL Tuning Advisor in Database Management
- Support for List of Users and the  User Details features as a part of Database Management Service
- Support for Autonomous databases in Database Management service
- Support to fetch AllowedIkeIpSecParameters,IpSecConnectionTunnelError,TunnelRoute,
  TunnelSecurityAssociation resources in Network service
- Support for Solaris platform for Management Agent service.
- Support for the user and security assessment action modules in the Data Safe service.
- Support for choosing platformVersion while creating a platform instance in blockchain service
- Capability for upgrading a platform instance in blockchain service
- Support for listing deployment backups in the GoldenGate service

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.53.0


## [2.36.0] - 2021-12-02

## Added
- Support for Service Manager Proxy service.
- Support added to integrate with Object Storage for BDS service.
- Support for getting subnet topology in the Networking service.
- Support for encrypted FastConnect resources in the Networking service.
- Added new features like list-profile-levels, list-resource-action-queryable-fields, filter-resource-actions for cloud advisor service.
- TDE Wallet Password Optional for ExaCS and DBCS for Database service.
- Support for unprocessed data bucket actions for Logging Analytics service.
- Support for the user and security assessment features in the Data Safe service.
- Support for EM Managed Exadatas and EM Managed hosts In Operations Insights (OPSI) service.
- Cross-compartment support to Operations Insights (OPSI) service.

## Fixed
- Installation script issues. Fixes [#129](https://github.com/oracle/oci-ansible-collection/issues/129) and [#107](https://github.com/oracle/oci-ansible-collection/issues/107)
- Issue for modules having the message as a top-level module parameter. Fixes [#120](https://github.com/oracle/oci-ansible-collection/issues/120)

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.52.0


## [2.35.0] - 2021-11-18

## Added
- Support for devops build and repository
- Support for Database Tools service
- Support for Certificates service
- Support for Certificates Management service
- Support for Oracle support reward (usage_proxy) service
- Support for Identity domains
- Support for scan listener port TCP and TCP SSL on cloud VM clusters in the Database service
- Support for OCI Certificates integration with the Load Balancer Service
- Support for creating hosts in specific availability domains in the VMWare Solution service
- Support for drill-down metadata in the Management Dashboard service
- Support for Default homepage preference & unprocessed data bucket for Logging Analytics service.

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.51.0




## [2.34.0] - 2021-11-03

## Added
- Support for Web Application Firewall service
- Support for Application Performance Monitoring Configuration service
- Support for Data Labeling Service
- Support for `object_name_filters` to object collection rule and added `import_custom_content` action for Log Analytics service.
- Support for `publish_result` for ONS service.
- Support for Node subsetting feature for VmCluster resources for ExaCC.
- Support to optionally provide SID prefix during database creation in ExaCS and ExaCC.
- Support to optionally provide peer database unique name and SID prefix during creation of Data Guard association in ExaCS and ExaCC.
- Support for creating db system from the backup with database software image.

## Fixed
- Fixed documentation issue for oci_identity_customer_secret_key for key parameter.
- Earlier we had made secret_name & vault_id mandatory in release 2.33.0, which we have now made optional again.
- Added `source_autonomous_database_id` parameter in the `oci_database_autonomous_database` module, to support creating autonomous database when `source` is set as `BACKUP_FROM_TIMESTAMP`.

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.49.1


## [2.33.0] - 2021-10-20

## Added
- Support for excluding compartments from which hosts should be listed from
- Support for list and read DeploymentUpgrade, cancel and restore DeploymentBackup in the Golden Gate service
- Support for the run-once monitor feature and network data collection in the Application Performance Monitoring service
- Support new response value "OPERATOR" for backup creationType in list and get MDS backup api for Mysql.
- Support for `object_collection_rule` and `scheduled_task` for LogAnalytics service.
- Support for `get-auto-upgradable-config` and Additional `install-type` parameter added to List Management Agents, Images and Count operations for Management Agent service.
- Support for uploading Datapump logs into Object Storage bucket, and filtering Database Objects in the Database Migration service.

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.48.0

### Breaking
- Param `is_agent_auto_upgradable` is removed from Management Agent Service.


## [2.32.0] - 2021-10-07

## Added
- Support for creating autonomous database and clones on shared infrastructure that do not require mTLS
- Support to check if an autonomous database on shared infrastructure requires mTLS, with added field `is_mtls_connection_required`
- Support to get connection string profiles for an autonomous database on shared infrastructure, with added field profiles in connectionStrings
- Support for setting message format when creating and updating alarms in the Monitoring service.
- Support for network security groups in the Functions service.
- Support for signed container images in the Functions service.
- Support for using Network Security Groups with API Gateway
- Support for scheduled jobs in Database Management service
- Get a summary of job execution status for Database Management service
- Support for storage modules for Logging Analytics service.
- Support for software package search in os management

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.47.0
- Return None response for upload action in os management event content


## [2.31.0] - 2021-09-23

## Added
- Support for monitoring and management of OCI virtual machine, bare metal, and ExaCS databases in the Database Management service
- Support for metrics and Performance Hub on virtual machine, bare metal, and ExaCS databases in the Database Management service
- Support for monitoring critical OS events in OCI Instances
- Support for Oracle Analytics Cloud, OCI Vault integration for connections in Data Catalog
- Support for serviceHostKeyFingerprint property for InstanceConsoleConnection in Core service
- Support for Shielded Instances in Core service
- Support for Fetching Detailed Job Log Content in Resource Manager Service
- Support for ML Jobs in the Data Science service

## Fixed
- Issue with using `lifecycle_state` filter for listing compartments in `oci_identity_compartment_facts` module
- Issue with ansible-doc when installed using ansible galaxy not showing documentation. Note: Issue is fixed only for core services (core, database, dns, load balancer and object storage). Other services continue to have this issue.

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.45.0

### Breaking
- Parameter `oci_splat_generated_ocids` is removed from the module `oci_resource_manager_template` in the Resource Manager service

## [2.30.0] - 2021-09-09

## Added
- Support for Email DKIM feature
- Support for getting management agent hosts which are eligible to create Operations Insights host resources on, in the Operations Insights service
- Support to generate recommended vm cluster network and create vm cluster network with given customer listener port
- Support for getting summarized agent counts and summarized plugin counts in the Management Agent Cloud service

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.44.1

## [2.29.0] - 2021-08-26

## Added
- Support for DBAAS Exacs Network Bonding
- Support for Autonomous Database Create with Early Patching
- Support for manually copying volume group backups across regions in the Block Volume service
- Support for work requests for the copy volume backup and copy boot volume backup operations in the Block Volume service
- Support MDS Backup Change Compartment
- `metastoreId` property to specify external hive metastore during Application Creation for Data Flow. Add `metastoreId` property to override metastore during Run.
- Support for Model Catalog v2.0 features including Provenance, Metadata, Schema, Artifact introspection

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.43.2

## [2.28.0] - 2021-08-12

## Added
- Support added for server-side tag filter query parameters in Capacity Planning and SQL Warehouse APIs
- Support for creating cross-region autonomous data guards in the Database service
- Support for the customer contacts feature on cloud exadata infrastructure in the Database service
- Support for Exadata system network bonding in the Database service
- Support for creating autonomous databases with early patching enabled in the Database service
- Support for cost analysis custom tables in the Usage service

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.43.2

## [2.27.0] - 2021-07-29

## Added
- Support for Anomaly Detection service
- Support for fetching monitor result in APM Synthetics service
- Support for metastore and initial data asset import/export in the Data Catalog service
- Support for jobs in Database Migration service
- Support for retrieving a DNS zone as a zone file for DNS Service
- Support for searching Marketplace Listings for Marketplace Service
- Support for new cluster type ODH for BDS Service.
- Support for availability domain as an optional parameter when creating VLANs in the Networking service
- Support for search domain type on DHCP options, to support multi-level domain search in the Networking service
## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.43.0
- Oracle Linux installation instructions

## [2.26.0] - 2021-07-15

## Added
- Simplified installation of `oci-ansible-collection`. Check [README.md](https://github.com/oracle/oci-ansible-collection/blob/master/README.md) for more details
- Support for `Resource Principal authentication` in Inventory plugin
- Support for `Devops` Service
- Support for VMBM Pluggable Database feature as a part of the Database Service
- Support for configuring Network Security Groups for OKE Node Pools
- New lifecycle state "NEEDS_ATTENTION" to indicate issues with the bridge resource, and new field "objectStorageBucketStatusDetails" to provide detail in Operation Insights (opsi) service
- Support for Metastore and initial Data Asset import/export in Data Catalog
- Support for Fractional OCPU and GB storage in Autonomous Database
- Support for Email Domain
- Support for new OCE instance license type - Starter Edition. The new license type is: STARTER

## Changed
- Minimum required [OCI Python SDK](https://github.com/oracle/oci-python-sdk) changed to 2.41.1
- Removed generic_artifact_content_body option from generic_artifact_content module

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
