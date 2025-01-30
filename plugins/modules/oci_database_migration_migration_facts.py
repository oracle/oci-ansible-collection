#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_database_migration_migration_facts
short_description: Fetches details about one or multiple Migration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Migration resources in Oracle Cloud Infrastructure
    - List all Migrations.
    - If I(migration_id) is specified, the details of a single Migration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_id:
        description:
            - The OCID of the migration
            - Required to get a specific migration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple migrations.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - The lifecycle state of the Migration.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "IN_PROGRESS"
            - "ACCEPTED"
            - "SUCCEEDED"
            - "CANCELED"
            - "WAITING"
            - "NEEDS_ATTENTION"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    lifecycle_details:
        description:
            - The lifecycle detailed status of the Migration.
        type: str
        choices:
            - "READY"
            - "ABORTING"
            - "VALIDATING"
            - "VALIDATED"
            - "WAITING"
            - "MIGRATING"
            - "DONE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific migration
  oci_database_migration_migration_facts:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List migrations
  oci_database_migration_migration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC
    lifecycle_state: CREATING
    lifecycle_details: READY

"""

RETURN = """
migrations:
    description:
        - List of Migration resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - A user-friendly description. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        wait_after:
            description:
                - You can optionally pause a migration after a job phase.
                  This property allows you to optionally specify the phase after which you can pause the migration.
                - Returned for get operation
            returned: on success
            type: str
            sample: ODMS_VALIDATE_TGT
        data_transfer_medium_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the data transfer medium to use.
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                object_storage_bucket:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        namespace_name:
                            description:
                                - Namespace name of the object store bucket.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Bucket name.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                region:
                    description:
                        - "AWS region code where the S3 bucket is located.
                          Region code should match the documented available regions:
                          https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions"
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                access_key_id:
                    description:
                        - "AWS access key credentials identifier
                          Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    returned: on success
                    type: str
                    sample: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
                secret_access_key:
                    description:
                        - "AWS secret access key credentials
                          Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    returned: on success
                    type: str
                    sample: secret_access_key_example
                name:
                    description:
                        - S3 bucket name.
                    returned: on success
                    type: str
                    sample: name_example
                shared_storage_mount_target_id:
                    description:
                        - OCID of the shared storage mount target
                    returned: on success
                    type: str
                    sample: "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx"
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        wallet_location:
                            description:
                                - Directory path to OCI SSL wallet location on Db server node.
                            returned: on success
                            type: str
                            sample: wallet_location_example
                        kind:
                            description:
                                - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                            returned: on success
                            type: str
                            sample: CURL
                        oci_home:
                            description:
                                - Path to the OCI CLI installation in the node.
                            returned: on success
                            type: str
                            sample: oci_home_example
                target:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        wallet_location:
                            description:
                                - Directory path to OCI SSL wallet location on Db server node.
                            returned: on success
                            type: str
                            sample: wallet_location_example
                        kind:
                            description:
                                - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                            returned: on success
                            type: str
                            sample: CURL
                        oci_home:
                            description:
                                - Path to the OCI CLI installation in the node.
                            returned: on success
                            type: str
                            sample: oci_home_example
        initial_load_settings:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_consistent:
                    description:
                        - Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.
                    returned: on success
                    type: bool
                    sample: true
                is_tz_utc:
                    description:
                        - Include a statement at the start of the dump to set the time zone to UTC.
                    returned: on success
                    type: bool
                    sample: true
                compatibility:
                    description:
                        - Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump
                          output, altering the dump files as necessary.
                    returned: on success
                    type: list
                    sample: []
                primary_key_compatibility:
                    description:
                        - Primary key compatibility option
                    returned: on success
                    type: str
                    sample: NONE
                is_ignore_existing_objects:
                    description:
                        - Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.
                    returned: on success
                    type: bool
                    sample: true
                handle_grant_errors:
                    description:
                        - The action taken in the event of errors related to GRANT or REVOKE errors.
                    returned: on success
                    type: str
                    sample: ABORT
                job_mode:
                    description:
                        - MySql Job Mode
                    returned: on success
                    type: str
                    sample: FULL
                data_pump_parameters:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_cluster:
                            description:
                                - Set to false to force Data Pump worker process to run on one instance.
                            returned: on success
                            type: bool
                            sample: true
                        estimate:
                            description:
                                - Estimate size of dumps that will be generated.
                            returned: on success
                            type: str
                            sample: BLOCKS
                        table_exists_action:
                            description:
                                - "IMPORT: Specifies the action to be performed when data is loaded into a preexisting table."
                            returned: on success
                            type: str
                            sample: TRUNCATE
                        exclude_parameters:
                            description:
                                - Exclude paratemers for Export and Import.
                            returned: on success
                            type: list
                            sample: []
                        import_parallelism_degree:
                            description:
                                - Maximum number of worker processes that can be used for a Data Pump Import job.
                                  For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.
                            returned: on success
                            type: int
                            sample: 56
                        export_parallelism_degree:
                            description:
                                - Maximum number of worker processes that can be used for a Data Pump Export job.
                            returned: on success
                            type: int
                            sample: 56
                tablespace_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_auto_create:
                            description:
                                - "Set this property to true to auto-create tablespaces in the target Database.
                                  Note: This is not applicable for Autonomous Database Serverless databases."
                            returned: on success
                            type: bool
                            sample: true
                        is_big_file:
                            description:
                                - Set this property to true to enable tablespace of the type big file.
                            returned: on success
                            type: bool
                            sample: true
                        extend_size_in_mbs:
                            description:
                                - "Size to extend the tablespace in MB.
                                  Note: Only applicable if 'isBigFile' property is set to true."
                            returned: on success
                            type: int
                            sample: 56
                        block_size_in_kbs:
                            description:
                                - Size of Oracle database blocks in KB.
                            returned: on success
                            type: str
                            sample: SIZE_8K
                        target_type:
                            description:
                                - Type of Database Base Migration Target.
                            returned: on success
                            type: str
                            sample: ADB_S_REMAP
                        remap_target:
                            description:
                                - Name of the tablespace on the target database to which the source database tablespace is to be remapped.
                            returned: on success
                            type: str
                            sample: remap_target_example
                export_directory_object:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of directory object in database
                            returned: on success
                            type: str
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: str
                            sample: path_example
                import_directory_object:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of directory object in database
                            returned: on success
                            type: str
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: str
                            sample: path_example
                metadata_remaps:
                    description:
                        - Defines remapping to be applied to objects as they are processed.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of remap. Refer to L(METADATA_REMAP Procedure ,https://docs.oracle.com/en/database/oracle/oracle-
                                  database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)
                            returned: on success
                            type: str
                            sample: SCHEMA
                        old_value:
                            description:
                                - Specifies the value which needs to be reset.
                            returned: on success
                            type: str
                            sample: old_value_example
                        new_value:
                            description:
                                - Specifies the new value that oldValue should be translated into.
                            returned: on success
                            type: str
                            sample: new_value_example
        advisor_settings:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                is_skip_advisor:
                    description:
                        - True to skip the Pre-Migration Advisor execution. Default is false.
                    returned: on success
                    type: bool
                    sample: true
                is_ignore_errors:
                    description:
                        - True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.
                    returned: on success
                    type: bool
                    sample: true
        hub_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rest_admin_credentials:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        username:
                            description:
                                - Administrator username
                            returned: on success
                            type: str
                            sample: username_example
                url:
                    description:
                        - Endpoint URL.
                    returned: on success
                    type: str
                    sample: url_example
                compute_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                key_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
                extract:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Extract performance.
                            returned: on success
                            type: str
                            sample: LOW
                        long_trans_duration:
                            description:
                                - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                                  long-running.
                                  If not specified, Extract will not generate a warning on long-running transactions.
                            returned: on success
                            type: int
                            sample: 56
                replicat:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Replicat performance.
                            returned: on success
                            type: str
                            sample: LOW
                acceptable_lag:
                    description:
                        - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    returned: on success
                    type: int
                    sample: 56
        ggs_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ggs_deployment:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        deployment_id:
                            description:
                                - The OCID of the resource being referenced.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
                        ggs_admin_credentials_secret_id:
                            description:
                                - The OCID of the resource being referenced.
                            returned: on success
                            type: str
                            sample: "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
                replicat:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Replicat performance.
                            returned: on success
                            type: str
                            sample: LOW
                acceptable_lag:
                    description:
                        - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    returned: on success
                    type: int
                    sample: 56
                extract:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Extract performance.
                            returned: on success
                            type: str
                            sample: LOW
                        long_trans_duration:
                            description:
                                - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                                  long-running.
                                  If not specified, Extract will not generate a warning on long-running transactions.
                            returned: on success
                            type: int
                            sample: 56
        source_container_database_connection_id:
            description:
                - The OCID of the resource being referenced.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        advanced_parameters:
            description:
                - List of Migration Parameter objects.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                value:
                    description:
                        - If a STRING data type then the value should be an array of characters,
                          if a INTEGER data type then the value should be an integer value,
                          if a FLOAT data type then the value should be an float value,
                          if a BOOLEAN data type then the value should be TRUE or FALSE.
                    returned: on success
                    type: str
                    sample: value_example
                name:
                    description:
                        - Parameter name.
                    returned: on success
                    type: str
                    sample: name_example
                data_type:
                    description:
                        - Parameter data type.
                    returned: on success
                    type: str
                    sample: STRING
        id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        database_combination:
            description:
                - "The combination of source and target databases participating in a migration.
                  Example: ORACLE means the migration is meant for migrating Oracle source and target databases."
            returned: on success
            type: str
            sample: MYSQL
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - "The type of the migration to be performed.
                  Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication."
            returned: on success
            type: str
            sample: ONLINE
        source_database_connection_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        executing_job_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_migration:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Migration resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional status related to the execution and current state of the Migration.
            returned: on success
            type: str
            sample: READY
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see Resource Tags. Example: {\\"Department\\": \\"Finance\\"}"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "description": "description_example",
        "wait_after": "ODMS_VALIDATE_TGT",
        "data_transfer_medium_details": {
            "type": "OBJECT_STORAGE",
            "object_storage_bucket": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            },
            "region": "us-phoenix-1",
            "access_key_id": "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx",
            "secret_access_key": "secret_access_key_example",
            "name": "name_example",
            "shared_storage_mount_target_id": "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx",
            "source": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            },
            "target": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            }
        },
        "initial_load_settings": {
            "is_consistent": true,
            "is_tz_utc": true,
            "compatibility": [],
            "primary_key_compatibility": "NONE",
            "is_ignore_existing_objects": true,
            "handle_grant_errors": "ABORT",
            "job_mode": "FULL",
            "data_pump_parameters": {
                "is_cluster": true,
                "estimate": "BLOCKS",
                "table_exists_action": "TRUNCATE",
                "exclude_parameters": [],
                "import_parallelism_degree": 56,
                "export_parallelism_degree": 56
            },
            "tablespace_details": {
                "is_auto_create": true,
                "is_big_file": true,
                "extend_size_in_mbs": 56,
                "block_size_in_kbs": "SIZE_8K",
                "target_type": "ADB_S_REMAP",
                "remap_target": "remap_target_example"
            },
            "export_directory_object": {
                "name": "name_example",
                "path": "path_example"
            },
            "import_directory_object": {
                "name": "name_example",
                "path": "path_example"
            },
            "metadata_remaps": [{
                "type": "SCHEMA",
                "old_value": "old_value_example",
                "new_value": "new_value_example"
            }]
        },
        "advisor_settings": {
            "is_skip_advisor": true,
            "is_ignore_errors": true
        },
        "hub_details": {
            "rest_admin_credentials": {
                "username": "username_example"
            },
            "url": "url_example",
            "compute_id": "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
            "extract": {
                "performance_profile": "LOW",
                "long_trans_duration": 56
            },
            "replicat": {
                "performance_profile": "LOW"
            },
            "acceptable_lag": 56
        },
        "ggs_details": {
            "ggs_deployment": {
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
                "ggs_admin_credentials_secret_id": "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "replicat": {
                "performance_profile": "LOW"
            },
            "acceptable_lag": 56,
            "extract": {
                "performance_profile": "LOW",
                "long_trans_duration": 56
            }
        },
        "source_container_database_connection_id": "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "advanced_parameters": [{
            "value": "value_example",
            "name": "name_example",
            "data_type": "STRING"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "database_combination": "MYSQL",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "ONLINE",
        "source_database_connection_id": "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "target_database_connection_id": "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "executing_job_id": "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_migration": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "READY",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "migration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration,
            migration_id=self.module.params.get("migration_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "lifecycle_details",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_migrations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MigrationFactsHelperCustom = get_custom_class("MigrationFactsHelperCustom")


class ResourceFactsHelper(MigrationFactsHelperCustom, MigrationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            migration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "IN_PROGRESS",
                    "ACCEPTED",
                    "SUCCEEDED",
                    "CANCELED",
                    "WAITING",
                    "NEEDS_ATTENTION",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            lifecycle_details=dict(
                type="str",
                choices=[
                    "READY",
                    "ABORTING",
                    "VALIDATING",
                    "VALIDATED",
                    "WAITING",
                    "MIGRATING",
                    "DONE",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="migration",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(migrations=result)


if __name__ == "__main__":
    main()
