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
module: oci_database_autonomous_database_actions
short_description: Perform actions on an AutonomousDatabase resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AutonomousDatabase resource in Oracle Cloud Infrastructure
    - For I(action=autonomous_database_manual_refresh), initiates a data refresh for an Autonomous Database refreshable clone. Data is refreshed from the source
      database to the point of a specified timestamp.
    - For I(action=deregister_autonomous_database_data_safe), asynchronously deregisters this Autonomous Database with Data Safe.
    - For I(action=fail_over), initiates a failover the specified Autonomous Database to a standby.
    - For I(action=generate_autonomous_database_wallet), creates and downloads a wallet for the specified Autonomous Database.
    - For I(action=register_autonomous_database_data_safe), asynchronously registers this Autonomous Database with Data Safe.
    - For I(action=restart), restarts the specified Autonomous Database.
    - For I(action=restore), restores an Autonomous Database based on the provided request parameters.
    - For I(action=rotate_autonomous_database_encryption_key), rotate existing AutonomousDatabase L(Vault
      service,https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) key.
    - For I(action=start), starts the specified Autonomous Database.
    - For I(action=stop), stops the specified Autonomous Database.
    - For I(action=switchover), initiates a switchover of the specified Autonomous Database to the associated standby database. Applicable only to databases
      with Autonomous Data Guard enabled.
version_added: "2.9"
author: Oracle (@oracle)
options:
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    time_refresh_cutoff:
        description:
            - The timestamp to which the Autonomous Database refreshable clone will be refreshed. Changes made in the primary database after this timestamp are
              not part of the data refresh.
            - Applicable only for I(action=autonomous_database_manual_refresh).
        type: str
    pdb_admin_password:
        description:
            - "The admin password provided during the creation of the database. This password is between 12 and 30 characters long, and must contain at least 1
              uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\\") or the username \\"admin\\", regardless of
              casing."
            - Required for I(action=deregister_autonomous_database_data_safe), I(action=register_autonomous_database_data_safe).
        type: str
    generate_type:
        description:
            - The type of wallet to generate.
            - "**Shared Exadata infrastructure usage:**
              * `SINGLE` - used to generate a wallet for a single database
              * `ALL` - used to generate wallet for all databases in the region"
            - "**Dedicated Exadata infrastructure usage:** Value must be `NULL` if attribute is used."
            - Applicable only for I(action=generate_autonomous_database_wallet).
        type: str
        choices:
            - "ALL"
            - "SINGLE"
    password:
        description:
            - The password to encrypt the keys inside the wallet. The password must be at least 8 characters long and must include at least 1 letter and either
              1 numeric character or 1 special character.
            - Required for I(action=generate_autonomous_database_wallet).
        type: str
    timestamp:
        description:
            - The time to restore the database to.
            - Required for I(action=restore).
        type: str
    database_scn:
        description:
            - Restores using the backup with the System Change Number (SCN) specified.
            - Applicable only for I(action=restore).
        type: str
    latest:
        description:
            - Restores to the last known good state with the least possible data loss.
            - Applicable only for I(action=restore).
        type: bool
    wallet_file:
        description:
            - The destination file path with file name when downloading wallet. The file must have 'zip' extension. I(wallet_file) is required if
              I(state='generate_wallet').
        type: str
    force:
        description:
            - Force overwriting existing wallet file when downloading wallet.
        type: bool
        default: "true"
        aliases: ["overwrite"]
    action:
        description:
            - The action to perform on the AutonomousDatabase.
        type: str
        required: true
        choices:
            - "autonomous_database_manual_refresh"
            - "deregister_autonomous_database_data_safe"
            - "fail_over"
            - "generate_autonomous_database_wallet"
            - "register_autonomous_database_data_safe"
            - "restart"
            - "restore"
            - "rotate_autonomous_database_encryption_key"
            - "start"
            - "stop"
            - "switchover"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action autonomous_database_manual_refresh on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: autonomous_database_manual_refresh

- name: Perform action deregister_autonomous_database_data_safe on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    pdb_admin_password: pdb_admin_password_example
    action: deregister_autonomous_database_data_safe

- name: Perform action fail_over on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: fail_over

- name: Perform action generate_autonomous_database_wallet on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    password: password_example
    action: generate_autonomous_database_wallet

- name: Perform action register_autonomous_database_data_safe on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    pdb_admin_password: pdb_admin_password_example
    action: register_autonomous_database_data_safe

- name: Perform action restart on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: restart

- name: Perform action restore on autonomous_database
  oci_database_autonomous_database_actions:
    timestamp: 2018-04-11T01:59:07.032Z
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: restore

- name: Perform action rotate_autonomous_database_encryption_key on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: rotate_autonomous_database_encryption_key

- name: Perform action start on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: start

- name: Perform action stop on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: stop

- name: Perform action switchover on autonomous_database
  oci_database_autonomous_database_actions:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx
    action: switchover

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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import AutonomousDatabaseManualRefreshDetails
    from oci.database.models import DeregisterAutonomousDatabaseDataSafeDetails
    from oci.database.models import GenerateAutonomousDatabaseWalletDetails
    from oci.database.models import RegisterAutonomousDatabaseDataSafeDetails
    from oci.database.models import RestoreAutonomousDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        autonomous_database_manual_refresh
        deregister_autonomous_database_data_safe
        fail_over
        generate_autonomous_database_wallet
        register_autonomous_database_data_safe
        restart
        restore
        rotate_autonomous_database_encryption_key
        start
        stop
        switchover
    """

    def __init__(self, *args, **kwargs):
        super(AutonomousDatabaseActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
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

    def autonomous_database_manual_refresh(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AutonomousDatabaseManualRefreshDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.autonomous_database_manual_refresh,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                autonomous_database_manual_refresh_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def deregister_autonomous_database_data_safe(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeregisterAutonomousDatabaseDataSafeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deregister_autonomous_database_data_safe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                deregister_autonomous_database_data_safe_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def fail_over(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.fail_over_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def generate_autonomous_database_wallet(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateAutonomousDatabaseWalletDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_autonomous_database_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                generate_autonomous_database_wallet_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def register_autonomous_database_data_safe(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RegisterAutonomousDatabaseDataSafeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.register_autonomous_database_data_safe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                register_autonomous_database_data_safe_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restart(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreAutonomousDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                restore_autonomous_database_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def rotate_autonomous_database_encryption_key(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.rotate_autonomous_database_encryption_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def switchover(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.switchover_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousDatabaseActionsHelperCustom = get_custom_class(
    "AutonomousDatabaseActionsHelperCustom"
)


class ResourceHelper(
    AutonomousDatabaseActionsHelperCustom, AutonomousDatabaseActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            autonomous_database_id=dict(aliases=["id"], type="str", required=True),
            time_refresh_cutoff=dict(type="str"),
            pdb_admin_password=dict(type="str", no_log=True),
            generate_type=dict(type="str", choices=["ALL", "SINGLE"]),
            password=dict(type="str", no_log=True),
            timestamp=dict(type="str"),
            database_scn=dict(type="str"),
            latest=dict(type="bool"),
            wallet_file=dict(type="str"),
            force=dict(aliases=["overwrite"], type="bool", default="true"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "autonomous_database_manual_refresh",
                    "deregister_autonomous_database_data_safe",
                    "fail_over",
                    "generate_autonomous_database_wallet",
                    "register_autonomous_database_data_safe",
                    "restart",
                    "restore",
                    "rotate_autonomous_database_encryption_key",
                    "start",
                    "stop",
                    "switchover",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
