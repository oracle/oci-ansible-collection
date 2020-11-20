#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_database_autonomous_database
short_description: Manage an AutonomousDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Autonomous Database.
    - "This resource has the following action operations in the M(oci_autonomous_database_actions) module: autonomous_database_manual_refresh,
      deregister_autonomous_database_data_safe, disable_autonomous_database_operations_insights, enable_autonomous_database_operations_insights, fail_over,
      generate_autonomous_database_wallet, register_autonomous_database_data_safe, restart, restore, rotate_autonomous_database_encryption_key, start, stop,
      switchover."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Autonomous Database.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    db_name:
        description:
            - The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters
              are not permitted. The database name must be unique in the tenancy.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    cpu_core_count:
        description:
            - The number of OCPU cores to be made available to the database.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    db_workload:
        description:
            - "The Autonomous Database workload type. The following values are valid:"
            - "- OLTP - indicates an Autonomous Transaction Processing database
              - DW - indicates an Autonomous Data Warehouse database
              - AJD - indicates an Autonomous JSON Database"
            - This parameter is updatable.
        type: str
        choices:
            - "OLTP"
            - "DW"
            - "AJD"
    data_storage_size_in_tbs:
        description:
            - The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    is_free_tier:
        description:
            - Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of
              memory. For Always Free databases, memory and CPU cannot be scaled.
            - This parameter is updatable.
        type: bool
    admin_password:
        description:
            - "The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot
              contain the double quote symbol (\\") or the username \\"admin\\", regardless of casing."
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The user-friendly name for the Autonomous Database. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    license_model:
        description:
            - The Oracle license model that applies to the Oracle Autonomous Database. Note that when provisioning an Autonomous Database on L(dedicated Exadata
              infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm), this attribute must be null because the attribute is
              already set at the
              Autonomous Exadata Infrastructure level. When using L(shared Exadata
              infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI), if a value is not specified, the system will supply
              the value of `BRING_YOUR_OWN_LICENSE`.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    is_preview_version_with_service_terms_accepted:
        description:
            - If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have
              been accepted. Note that preview version software is only available for databases on L(shared Exadata
              infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI).
        type: bool
    is_auto_scaling_enabled:
        description:
            - Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.
            - This parameter is updatable.
        type: bool
    is_dedicated:
        description:
            - True if the database is on L(dedicated Exadata infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm).
        type: bool
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    whitelisted_ips:
        description:
            - The client IP access control list (ACL). This feature is available for databases on L(shared Exadata
              infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI) only.
              Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless
              Inter-Domain Routing) notations for a subnet or VCN OCID.
            - "To add the whitelist VCN specific subnet or IP, use a semicoln ';' as a deliminator to add the VCN specific subnets or IPs.
              For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
              Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.sea.<u
              nique_id2>;1.1.0.0/16\\"]`"
            - This parameter is updatable.
        type: list
    is_data_guard_enabled:
        description:
            - Indicates whether the Autonomous Database has Data Guard enabled.
            - This parameter is updatable.
        type: bool
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.
            - "**Subnet Restrictions:**
              - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
              - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
              - For Autonomous Database, setting this will disable public secure access to the database."
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and the backup subnet.
            - This parameter is updatable.
        type: str
    nsg_ids:
        description:
            - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
              resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs,
              see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
            - This parameter is updatable.
        type: list
    private_endpoint_label:
        description:
            - The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the
              same private endpoint database to the public endpoint database.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    db_version:
        description:
            - A valid Oracle Database version for Autonomous Database.
            - This parameter is updatable.
        type: str
    source:
        description:
            - "The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning
              an existing Autonomous Database."
            - "For Autonomous Databases on L(shared Exadata infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI), the
              following cloning options are available: Use `BACKUP_FROM_ID` for creating a new Autonomous Database from a specified backup. Use
              `BACKUP_FROM_TIMESTAMP` for creating a point-in-time Autonomous Database clone using backups. For more information, see L(Cloning an Autonomous
              Database,https://docs.cloud.oracle.com/Content/Database/Tasks/adbcloning.htm)."
        type: str
        choices:
            - "DATABASE"
            - "CLONE_TO_REFRESHABLE"
            - "BACKUP_FROM_ID"
            - "BACKUP_FROM_TIMESTAMP"
            - "NONE"
        default: "NONE"
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create
              a new Autonomous Database.
            - Required when source is one of ['DATABASE', 'CLONE_TO_REFRESHABLE']
        type: str
    clone_type:
        description:
            - The Autonomous Database clone type.
            - Required when source is one of ['BACKUP_FROM_TIMESTAMP', 'DATABASE', 'BACKUP_FROM_ID']
        type: str
        choices:
            - "FULL"
            - "METADATA"
    refreshable_mode:
        description:
            - The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.
            - This parameter is updatable.
            - Applicable when source is 'CLONE_TO_REFRESHABLE'
        type: str
        choices:
            - "AUTOMATIC"
            - "MANUAL"
    autonomous_database_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database Backup that you will clone to
              create a new Autonomous Database.
            - Required when source is 'BACKUP_FROM_ID'
        type: str
    autonomous_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create
              a new Autonomous Database.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required when source is 'BACKUP_FROM_TIMESTAMP'
        type: str
        aliases: ["id"]
    timestamp:
        description:
            - The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.
            - Required when source is 'BACKUP_FROM_TIMESTAMP'
        type: str
    is_refreshable_clone:
        description:
            - Indicates whether the Autonomous Database is a refreshable clone.
            - This parameter is updatable.
        type: bool
    open_mode:
        description:
            - The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.
            - This parameter is updatable.
        type: str
        choices:
            - "READ_ONLY"
            - "READ_WRITE"
    permission_level:
        description:
            - The Autonomous Database permission level. Restricted mode allows access only to admin users.
            - This parameter is updatable.
        type: str
        choices:
            - "RESTRICTED"
            - "UNRESTRICTED"
    state:
        description:
            - The state of the AutonomousDatabase.
            - Use I(state=present) to create or update an AutonomousDatabase.
            - Use I(state=absent) to delete an AutonomousDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_database
  oci_database_autonomous_database:
    compartment_id: ocid.compartment.oc1..<unique_ID>
    display_name: example_autonomous_database
    db_name: adatabasedb1
    admin_password: <password>
    cpu_core_count: 8
    data_storage_size_in_tbs: 1

- name: Update autonomous_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database:
    cpu_core_count: 20
    display_name: example_autonomous_database

- name: Update autonomous_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database:
    autonomous_database_id: ocid1.autonomousdatabase.oc1.iad.Example
    cpu_core_count: 20

- name: Update autonomous_database
  oci_database_autonomous_database:
    autonomous_database_id: ocid1.autonomousdatabase.oc1.iad.Example

- name: Delete autonomous_database
  oci_database_autonomous_database:
    autonomous_database_id: ocid1.autonomousdatabase.oc1.iad.Example
    state: absent

- name: Delete autonomous_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database:
    compartment_id: ocid.compartment.oc1..<unique_ID>
    display_name: example_autonomous_database
    state: absent

"""

RETURN = """
autonomous_database:
    description:
        - Details of the AutonomousDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the Autonomous Database.
            returned: on success
            type: string
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        db_name:
            description:
                - The database name.
            returned: on success
            type: string
            sample: db_name_example
        is_free_tier:
            description:
                - Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of
                  memory. For Always Free databases, memory and CPU cannot be scaled.
            returned: on success
            type: bool
            sample: true
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {}
        time_reclamation_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the
                  database will automatically be put into the STOPPED state.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_deletion_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and
                  without activity until this time, it will be deleted.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        cpu_core_count:
            description:
                - The number of OCPU cores to be made available to the database.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - The quantity of data in the database, in terabytes.
            returned: on success
            type: int
            sample: 56
        infrastructure_type:
            description:
                - The infrastructure type this resource belongs to.
            returned: on success
            type: string
            sample: CLOUD
        is_dedicated:
            description:
                - True if the database uses L(dedicated Exadata infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm).
            returned: on success
            type: bool
            sample: true
        autonomous_container_database_id:
            description:
                - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: string
            sample: ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the Autonomous Database was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        display_name:
            description:
                - The user-friendly name for the Autonomous Database. The name does not have to be unique.
            returned: on success
            type: string
            sample: display_name_example
        service_console_url:
            description:
                - The URL of the Service Console for the Autonomous Database.
            returned: on success
            type: string
            sample: service_console_url_example
        connection_strings:
            description:
                - The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered
                  when creating the Autonomous Database for the password value.
            returned: on success
            type: complex
            contains:
                high:
                    description:
                        - The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but
                          supports the fewest number of concurrent SQL statements.
                    returned: on success
                    type: string
                    sample: high_example
                medium:
                    description:
                        - The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of
                          performance, but supports more concurrent SQL statements.
                    returned: on success
                    type: string
                    sample: medium_example
                low:
                    description:
                        - The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: string
                    sample: low_example
                dedicated:
                    description:
                        - The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: string
                    sample: dedicated_example
                all_connection_strings:
                    description:
                        - Returns all connection strings that can be used to connect to the Autonomous Database.
                          For more information, please see L(Predefined Database Service Names for Autonomous Transaction
                          Processing,https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE)
                    returned: on success
                    type: dict
                    sample: {}
        connection_urls:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                sql_dev_web_url:
                    description:
                        - Oracle SQL Developer Web URL.
                    returned: on success
                    type: string
                    sample: sql_dev_web_url_example
                apex_url:
                    description:
                        - Oracle Application Express (APEX) URL.
                    returned: on success
                    type: string
                    sample: apex_url_example
                machine_learning_user_management_url:
                    description:
                        - Oracle Machine Learning user management URL.
                    returned: on success
                    type: string
                    sample: machine_learning_user_management_url_example
        license_model:
            description:
                - The Oracle license model that applies to the Oracle Autonomous Database. Note that when provisioning an Autonomous Database on L(dedicated
                  Exadata infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm), this attribute must be null because the
                  attribute is already set at the
                  Autonomous Exadata Infrastructure level. When using L(shared Exadata
                  infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI), if a value is not specified, the system will
                  supply the value of `BRING_YOUR_OWN_LICENSE`.
            returned: on success
            type: string
            sample: LICENSE_INCLUDED
        used_data_storage_size_in_tbs:
            description:
                - The amount of storage that has been used, in terabytes.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.
                - "**Subnet Restrictions:**
                  - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
                  - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
                  - For Autonomous Database, setting this will disable public secure access to the database."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and the backup subnet.
            returned: on success
            type: string
            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
        nsg_ids:
            description:
                - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
                  resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about
                  NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
            returned: on success
            type: list
            sample: []
        private_endpoint:
            description:
                - The private endpoint for the resource.
            returned: on success
            type: string
            sample: private_endpoint_example
        private_endpoint_label:
            description:
                - The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change
                  the same private endpoint database to the public endpoint database.
            returned: on success
            type: string
            sample: private_endpoint_label_example
        private_endpoint_ip:
            description:
                - The private endpoint Ip address for the resource.
            returned: on success
            type: string
            sample: private_endpoint_ip_example
        db_version:
            description:
                - A valid Oracle Database version for Autonomous Database.
            returned: on success
            type: string
            sample: db_version_example
        is_preview:
            description:
                - Indicates if the Autonomous Database version is a preview version.
            returned: on success
            type: bool
            sample: true
        db_workload:
            description:
                - "The Autonomous Database workload type. The following values are valid:"
                - "- OLTP - indicates an Autonomous Transaction Processing database
                  - DW - indicates an Autonomous Data Warehouse database
                  - AJD - indicates an Autonomous JSON Database"
            returned: on success
            type: string
            sample: OLTP
        whitelisted_ips:
            description:
                - The client IP access control list (ACL). This feature is available for databases on L(shared Exadata
                  infrastructure,https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI) only.
                  Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR
                  (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
                - "To add the whitelist VCN specific subnet or IP, use a semicoln ';' as a deliminator to add the VCN specific subnets or IPs.
                  For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.se
                  a.<unique_id2>;1.1.0.0/16\\"]`"
            returned: on success
            type: list
            sample: []
        is_auto_scaling_enabled:
            description:
                - Indicates if auto scaling is enabled for the Autonomous Database CPU core count.
            returned: on success
            type: bool
            sample: true
        data_safe_status:
            description:
                - Status of the Data Safe registration for this Autonomous Database.
            returned: on success
            type: string
            sample: REGISTERING
        operations_insights_status:
            description:
                - Status of the Operations Insights for this Autonomous Database.
            returned: on success
            type: string
            sample: ENABLING
        time_maintenance_begin:
            description:
                - The date and time when maintenance will begin.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_maintenance_end:
            description:
                - The date and time when maintenance will end.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        is_refreshable_clone:
            description:
                - Indicates whether the Autonomous Database is a refreshable clone.
            returned: on success
            type: bool
            sample: true
        time_of_last_refresh:
            description:
                - The date and time when last refresh happened.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_of_last_refresh_point:
            description:
                - The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the
                  refresh point is not included in the refresh.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_of_next_refresh:
            description:
                - The date and time of next refresh.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        open_mode:
            description:
                - The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.
            returned: on success
            type: string
            sample: READ_ONLY
        refreshable_status:
            description:
                - The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: string
            sample: REFRESHING
        refreshable_mode:
            description:
                - The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: string
            sample: AUTOMATIC
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that was cloned to create
                  the current Autonomous Database.
            returned: on success
            type: string
            sample: ocid1.source.oc1..xxxxxxEXAMPLExxxxxx
        permission_level:
            description:
                - The Autonomous Database permission level. Restricted mode allows access only to admin users.
            returned: on success
            type: string
            sample: RESTRICTED
        time_of_last_switchover:
            description:
                - The timestamp of the last switchover operation for the Autonomous Database.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_of_last_failover:
            description:
                - The timestamp of the last failover operation.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        is_data_guard_enabled:
            description:
                - Indicates whether the Autonomous Database has Data Guard enabled.
            returned: on success
            type: bool
            sample: true
        failed_data_recovery_in_seconds:
            description:
                - Indicates the number of seconds of data loss for a Data Guard failover.
            returned: on success
            type: int
            sample: 56
        standby_db:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                lag_time_in_seconds:
                    description:
                        - The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine
                          the potential data loss in the event of a failover.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the Autonomous Database.
                    returned: on success
                    type: string
                    sample: PROVISIONING
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycle state.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
        available_upgrade_versions:
            description:
                - List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "db_name": "db_name_example",
        "is_free_tier": true,
        "system_tags": {},
        "time_reclamation_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "time_deletion_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "cpu_core_count": 56,
        "data_storage_size_in_tbs": 56,
        "infrastructure_type": "CLOUD",
        "is_dedicated": true,
        "autonomous_container_database_id": "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "service_console_url": "service_console_url_example",
        "connection_strings": {
            "high": "high_example",
            "medium": "medium_example",
            "low": "low_example",
            "dedicated": "dedicated_example",
            "all_connection_strings": {}
        },
        "connection_urls": {
            "sql_dev_web_url": "sql_dev_web_url_example",
            "apex_url": "apex_url_example",
            "machine_learning_user_management_url": "machine_learning_user_management_url_example"
        },
        "license_model": "LICENSE_INCLUDED",
        "used_data_storage_size_in_tbs": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "private_endpoint": "private_endpoint_example",
        "private_endpoint_label": "private_endpoint_label_example",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "db_version": "db_version_example",
        "is_preview": true,
        "db_workload": "OLTP",
        "whitelisted_ips": [],
        "is_auto_scaling_enabled": true,
        "data_safe_status": "REGISTERING",
        "operations_insights_status": "ENABLING",
        "time_maintenance_begin": "2013-10-20T19:20:30+01:00",
        "time_maintenance_end": "2013-10-20T19:20:30+01:00",
        "is_refreshable_clone": true,
        "time_of_last_refresh": "2013-10-20T19:20:30+01:00",
        "time_of_last_refresh_point": "2013-10-20T19:20:30+01:00",
        "time_of_next_refresh": "2013-10-20T19:20:30+01:00",
        "open_mode": "READ_ONLY",
        "refreshable_status": "REFRESHING",
        "refreshable_mode": "AUTOMATIC",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "permission_level": "RESTRICTED",
        "time_of_last_switchover": "2013-10-20T19:20:30+01:00",
        "time_of_last_failover": "2013-10-20T19:20:30+01:00",
        "is_data_guard_enabled": true,
        "failed_data_recovery_in_seconds": 56,
        "standby_db": {
            "lag_time_in_seconds": 56,
            "lifecycle_state": "PROVISIONING",
            "lifecycle_details": "lifecycle_details_example"
        },
        "available_upgrade_versions": []
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateAutonomousDatabaseBase
    from oci.database.models import UpdateAutonomousDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(AutonomousDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "autonomous_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_database_id")

    def get_get_fn(self):
        return self.client.get_autonomous_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["autonomous_container_database_id", "display_name"]
            if self._use_name_as_identifier()
            else [
                "autonomous_container_database_id",
                "db_workload",
                "db_version",
                "is_free_tier",
                "display_name",
                "is_refreshable_clone",
                "is_data_guard_enabled",
            ]
        )

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_autonomous_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateAutonomousDatabaseBase

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_autonomous_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutonomousDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                update_autonomous_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousDatabaseHelperCustom = get_custom_class("AutonomousDatabaseHelperCustom")


class ResourceHelper(AutonomousDatabaseHelperCustom, AutonomousDatabaseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            db_name=dict(type="str"),
            cpu_core_count=dict(type="int"),
            db_workload=dict(type="str", choices=["OLTP", "DW", "AJD"]),
            data_storage_size_in_tbs=dict(type="int"),
            is_free_tier=dict(type="bool"),
            admin_password=dict(type="str", no_log=True),
            display_name=dict(aliases=["name"], type="str"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            is_preview_version_with_service_terms_accepted=dict(type="bool"),
            is_auto_scaling_enabled=dict(type="bool"),
            is_dedicated=dict(type="bool"),
            autonomous_container_database_id=dict(type="str"),
            whitelisted_ips=dict(type="list"),
            is_data_guard_enabled=dict(type="bool"),
            subnet_id=dict(type="str"),
            nsg_ids=dict(type="list"),
            private_endpoint_label=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            db_version=dict(type="str"),
            source=dict(
                type="str",
                default="NONE",
                choices=[
                    "DATABASE",
                    "CLONE_TO_REFRESHABLE",
                    "BACKUP_FROM_ID",
                    "BACKUP_FROM_TIMESTAMP",
                    "NONE",
                ],
            ),
            source_id=dict(type="str"),
            clone_type=dict(type="str", choices=["FULL", "METADATA"]),
            refreshable_mode=dict(type="str", choices=["AUTOMATIC", "MANUAL"]),
            autonomous_database_backup_id=dict(type="str"),
            autonomous_database_id=dict(aliases=["id"], type="str"),
            timestamp=dict(type="str"),
            is_refreshable_clone=dict(type="bool"),
            open_mode=dict(type="str", choices=["READ_ONLY", "READ_WRITE"]),
            permission_level=dict(type="str", choices=["RESTRICTED", "UNRESTRICTED"]),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
