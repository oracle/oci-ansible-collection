#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_migration_migration_actions
short_description: Perform actions on a Migration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Migration resource in Oracle Cloud Infrastructure
    - For I(action=add_migration_objects), add excluded/included object to the list.
    - For I(action=change_compartment), used to change the Migration compartment.
    - For I(action=remove_migration_objects), remove excluded/included objects.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    migration_id:
        description:
            - The OCID of the migration
        type: str
        aliases: ["id"]
        required: true
    items:
        description:
            - Database objects to exclude/include from migration
            - Required for I(action=add_migration_objects), I(action=remove_migration_objects).
        type: list
        elements: dict
        suboptions:
            owner:
                description:
                    - Owner of the object (regular expression is allowed)
                type: str
                required: true
            object_name:
                description:
                    - Name of the object (regular expression is allowed)
                type: str
                required: true
            type:
                description:
                    - Type of object to exclude.
                      If not specified, matching owners and object names of type TABLE would be excluded.
                type: str
            object_status:
                description:
                    - Object status.
                type: str
                choices:
                    - "EXCLUDE"
                    - "INCLUDE"
            is_omit_excluded_table_from_replication:
                description:
                    - Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and object
                      status EXCLUDE.
                type: bool
    csv_text:
        description:
            - Database objects to exclude/include from migration in CSV format. The items field will be ignored if this field is not null.
            - Applicable only for I(action=add_migration_objects)I(action=remove_migration_objects).
        type: str
    action:
        description:
            - The action to perform on the Migration.
        type: str
        required: true
        choices:
            - "add_migration_objects"
            - "change_compartment"
            - "remove_migration_objects"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add_migration_objects on migration
  oci_database_migration_migration_actions:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    items:
    - # required
      owner: owner_example
      object_name: object_name_example

      # optional
      type: type_example
      object_status: EXCLUDE
      is_omit_excluded_table_from_replication: true
    action: add_migration_objects

    # optional
    csv_text: csv_text_example

- name: Perform action change_compartment on migration
  oci_database_migration_migration_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_migration_objects on migration
  oci_database_migration_migration_actions:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    items:
    - # required
      owner: owner_example
      object_name: object_name_example

      # optional
      type: type_example
      object_status: EXCLUDE
      is_omit_excluded_table_from_replication: true
    action: remove_migration_objects

    # optional
    csv_text: csv_text_example

"""

RETURN = """
migration:
    description:
        - Details of the Migration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Migration Display Name
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - OCID of the compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - Migration type.
            returned: on success
            type: str
            sample: ONLINE
        wait_after:
            description:
                - Name of a migration phase. The Job will wait after executing this
                  phase until the Resume Job endpoint is called.
            returned: on success
            type: str
            sample: ODMS_VALIDATE_TGT
        agent_id:
            description:
                - The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        credentials_secret_id:
            description:
                - OCID of the Secret in the OCI vault containing the Migration credentials. Used to store GoldenGate administrator user credentials.
            returned: on success
            type: str
            sample: "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
        source_database_connection_id:
            description:
                - The OCID of the Source Database Connection.
            returned: on success
            type: str
            sample: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        source_container_database_connection_id:
            description:
                - The OCID of the Source Container Database Connection.
            returned: on success
            type: str
            sample: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id:
            description:
                - The OCID of the Target Database Connection.
            returned: on success
            type: str
            sample: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        executing_job_id:
            description:
                - OCID of the current ODMS Job in execution for the Migration, if any.
            returned: on success
            type: str
            sample: "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx"
        data_transfer_medium_details_v2:
            description:
                - ""
            returned: on success
            type: complex
            contains:
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
                type:
                    description:
                        - Type of the data transfer medium to use for the datapump
                    returned: on success
                    type: str
                    sample: DBLINK
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
        data_transfer_medium_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_link_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.
                            returned: on success
                            type: str
                            sample: name_example
                        wallet_bucket:
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
                object_storage_details:
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
                aws_s3_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - S3 bucket name.
                            returned: on success
                            type: str
                            sample: name_example
                        region:
                            description:
                                - "AWS region code where the S3 bucket is located.
                                  Region code should match the documented available regions:
                                  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions"
                            returned: on success
                            type: str
                            sample: us-phoenix-1
        dump_transfer_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
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
                shared_storage_mount_target_id:
                    description:
                        - OCID of the shared storage mount target
                    returned: on success
                    type: str
                    sample: "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx"
        datapump_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                job_mode:
                    description:
                        - Data Pump job mode.
                          Refer to L(Data Pump Export Modes ,https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-
                          utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4)
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
                                - Set to false to force Data Pump worker processes to run on one instance.
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
                metadata_remaps:
                    description:
                        - Defines remapping to be applied to objects as they are processed.
                          Refer to L(METADATA_REMAP Procedure ,https://docs.oracle.com/en/database/oracle/oracle-
                          database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)
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
                tablespace_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_auto_create:
                            description:
                                - True to auto-create tablespace in the target Database.
                            returned: on success
                            type: bool
                            sample: true
                        is_big_file:
                            description:
                                - True set tablespace to big file.
                            returned: on success
                            type: bool
                            sample: true
                        extend_size_in_mbs:
                            description:
                                - Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.
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
                                - Name of tablespace at target to which the source database tablespace need to be remapped.
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
        advisor_settings:
            description:
                - ""
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
        exclude_objects:
            description:
                - "Database objects to exclude from migration.
                  If 'includeObjects' are specified, only exclude object types can be specified with general wildcards (.*) for owner and objectName."
            returned: on success
            type: complex
            contains:
                owner:
                    description:
                        - Owner of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: owner_example
                object_name:
                    description:
                        - Name of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: object_name_example
                type:
                    description:
                        - Type of object to exclude.
                          If not specified, matching owners and object names of type TABLE would be excluded.
                    returned: on success
                    type: str
                    sample: type_example
                is_omit_excluded_table_from_replication:
                    description:
                        - Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and that are
                          included in the exludeObjects.
                    returned: on success
                    type: bool
                    sample: true
        include_objects:
            description:
                - Database objects to include from migration.
            returned: on success
            type: complex
            contains:
                owner:
                    description:
                        - Owner of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: owner_example
                object_name:
                    description:
                        - Name of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: object_name_example
                type:
                    description:
                        - Type of object to exclude.
                          If not specified, matching owners and object names of type TABLE would be excluded.
                    returned: on success
                    type: str
                    sample: type_example
                is_omit_excluded_table_from_replication:
                    description:
                        - Whether an excluded table should be omitted from replication. Only valid for database objects that have are of type TABLE and that are
                          included in the exludeObjects.
                    returned: on success
                    type: bool
                    sample: true
        golden_gate_service_details:
            description:
                - ""
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
                                - OCID of a GoldenGate Deployment
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
                        ggs_admin_credentials_secret_id:
                            description:
                                - OCID of a VaultSecret containing the Admin Credentials for the GGS Deployment
                            returned: on success
                            type: str
                            sample: "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
                settings:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
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
                                        - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the
                                          transaction is long-running.
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
                                map_parallelism:
                                    description:
                                        - Number of threads used to read trail files (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                                min_apply_parallelism:
                                    description:
                                        - Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_apply_parallelism:
                                    description:
                                        - Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                        acceptable_lag:
                            description:
                                - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                            returned: on success
                            type: int
                            sample: 56
        golden_gate_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                hub:
                    description:
                        - ""
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
                        source_db_admin_credentials:
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
                        source_container_db_admin_credentials:
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
                        target_db_admin_credentials:
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
                                - Oracle GoldenGate hub's REST endpoint.
                                  Refer to
                                  https://docs.oracle.com/en/middleware/goldengate/core/19.1/securing/network.html#GUID-A709DA55-111D-455E-8942-C9BDD1E38CAA
                            returned: on success
                            type: str
                            sample: url_example
                        source_microservices_deployment_name:
                            description:
                                - Name of GoldenGate deployment to operate on source database
                            returned: on success
                            type: str
                            sample: source_microservices_deployment_name_example
                        target_microservices_deployment_name:
                            description:
                                - Name of GoldenGate deployment to operate on target database
                            returned: on success
                            type: str
                            sample: target_microservices_deployment_name_example
                        compute_id:
                            description:
                                - OCID of GoldenGate compute instance.
                            returned: on success
                            type: str
                            sample: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
                settings:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
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
                                        - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the
                                          transaction is long-running.
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
                                map_parallelism:
                                    description:
                                        - Number of threads used to read trail files (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                                min_apply_parallelism:
                                    description:
                                        - Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                                max_apply_parallelism:
                                    description:
                                        - Defines the range in which Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    returned: on success
                                    type: int
                                    sample: 56
                        acceptable_lag:
                            description:
                                - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                            returned: on success
                            type: int
                            sample: 56
        vault_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - OCID of the compartment where the secret containing the credentials will be created.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - OCID of the vault
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                key_id:
                    description:
                        - OCID of the vault encryption key
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the Migration was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time of the last Migration details update. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_migration:
            description:
                - The time of last Migration. An RFC3339 formatted datetime string.
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
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "ONLINE",
        "wait_after": "ODMS_VALIDATE_TGT",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
        "credentials_secret_id": "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx",
        "source_database_connection_id": "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "source_container_database_connection_id": "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "target_database_connection_id": "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "executing_job_id": "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx",
        "data_transfer_medium_details_v2": {
            "region": "us-phoenix-1",
            "access_key_id": "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx",
            "secret_access_key": "secret_access_key_example",
            "name": "name_example",
            "type": "DBLINK",
            "object_storage_bucket": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            }
        },
        "data_transfer_medium_details": {
            "database_link_details": {
                "name": "name_example",
                "wallet_bucket": {
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example"
                }
            },
            "object_storage_details": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            },
            "aws_s3_details": {
                "name": "name_example",
                "region": "us-phoenix-1"
            }
        },
        "dump_transfer_details": {
            "source": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            },
            "target": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            },
            "shared_storage_mount_target_id": "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "datapump_settings": {
            "job_mode": "FULL",
            "data_pump_parameters": {
                "is_cluster": true,
                "estimate": "BLOCKS",
                "table_exists_action": "TRUNCATE",
                "exclude_parameters": [],
                "import_parallelism_degree": 56,
                "export_parallelism_degree": 56
            },
            "metadata_remaps": [{
                "type": "SCHEMA",
                "old_value": "old_value_example",
                "new_value": "new_value_example"
            }],
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
            }
        },
        "advisor_settings": {
            "is_skip_advisor": true,
            "is_ignore_errors": true
        },
        "exclude_objects": [{
            "owner": "owner_example",
            "object_name": "object_name_example",
            "type": "type_example",
            "is_omit_excluded_table_from_replication": true
        }],
        "include_objects": [{
            "owner": "owner_example",
            "object_name": "object_name_example",
            "type": "type_example",
            "is_omit_excluded_table_from_replication": true
        }],
        "golden_gate_service_details": {
            "ggs_deployment": {
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
                "ggs_admin_credentials_secret_id": "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "settings": {
                "extract": {
                    "performance_profile": "LOW",
                    "long_trans_duration": 56
                },
                "replicat": {
                    "performance_profile": "LOW",
                    "map_parallelism": 56,
                    "min_apply_parallelism": 56,
                    "max_apply_parallelism": 56
                },
                "acceptable_lag": 56
            }
        },
        "golden_gate_details": {
            "hub": {
                "rest_admin_credentials": {
                    "username": "username_example"
                },
                "source_db_admin_credentials": {
                    "username": "username_example"
                },
                "source_container_db_admin_credentials": {
                    "username": "username_example"
                },
                "target_db_admin_credentials": {
                    "username": "username_example"
                },
                "url": "url_example",
                "source_microservices_deployment_name": "source_microservices_deployment_name_example",
                "target_microservices_deployment_name": "target_microservices_deployment_name_example",
                "compute_id": "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "settings": {
                "extract": {
                    "performance_profile": "LOW",
                    "long_trans_duration": 56
                },
                "replicat": {
                    "performance_profile": "LOW",
                    "map_parallelism": 56,
                    "min_apply_parallelism": 56,
                    "max_apply_parallelism": 56
                },
                "acceptable_lag": 56
            }
        },
        "vault_details": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_migration": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "READY",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import MigrationObjectCollection
    from oci.database_migration.models import ChangeMigrationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_migration_objects
        change_compartment
        remove_migration_objects
    """

    @staticmethod
    def get_module_resource_id_param():
        return "migration_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_id")

    def get_get_fn(self):
        return self.client.get_migration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration,
            migration_id=self.module.params.get("migration_id"),
        )

    def add_migration_objects(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, MigrationObjectCollection
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_migration_objects,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                add_migration_objects_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMigrationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_migration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                change_migration_compartment_details=action_details,
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

    def remove_migration_objects(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, MigrationObjectCollection
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_migration_objects,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                remove_migration_objects_details=action_details,
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


MigrationActionsHelperCustom = get_custom_class("MigrationActionsHelperCustom")


class ResourceHelper(MigrationActionsHelperCustom, MigrationActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            migration_id=dict(aliases=["id"], type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    owner=dict(type="str", required=True),
                    object_name=dict(type="str", required=True),
                    type=dict(type="str"),
                    object_status=dict(type="str", choices=["EXCLUDE", "INCLUDE"]),
                    is_omit_excluded_table_from_replication=dict(type="bool"),
                ),
            ),
            csv_text=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_migration_objects",
                    "change_compartment",
                    "remove_migration_objects",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
