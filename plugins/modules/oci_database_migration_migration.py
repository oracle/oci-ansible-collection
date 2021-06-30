#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_migration_migration
short_description: Manage a Migration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Migration resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Migration resource that contains all the details to perform the
      database migration operation, such as source and destination database
      details, credentials, etc.
    - "This resource has the following action operations in the M(oci_migration_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    type:
        description:
            - Migration type.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "ONLINE"
            - "OFFLINE"
    display_name:
        description:
            - Migration Display Name
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - OCID of the compartment
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    agent_id:
        description:
            - The OCID of the registered ODMS Agent. Only valid for Offline Logical Migrations.
            - This parameter is updatable.
        type: str
    source_database_connection_id:
        description:
            - The OCID of the Source Database Connection.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    source_container_database_connection_id:
        description:
            - The OCID of the Source Container Database Connection. Only used for Online migrations.
              Only Connections of type Non-Autonomous can be used as source container databases.
            - This parameter is updatable.
        type: str
    target_database_connection_id:
        description:
            - The OCID of the Target Database Connection.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    data_transfer_medium_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            database_link_details:
                description:
                    - ""
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of database link from OCI database to on-premise database. ODMS will create link, if the link does not already exist.
                            - This parameter is updatable.
                        type: str
                        required: true
            object_storage_details:
                description:
                    - ""
                type: dict
                suboptions:
                    namespace_name:
                        description:
                            - Namespace name of the object store bucket.
                            - This parameter is updatable.
                        type: str
                    bucket_name:
                        description:
                            - Bucket name.
                            - This parameter is updatable.
                        type: str
    datapump_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            job_mode:
                description:
                    - Data Pump job mode.
                      Refer to L(link text,https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-export-
                      utility.html#GUID-8E497131-6B9B-4CC8-AA50-35F480CAC2C4)
                    - This parameter is updatable.
                type: str
                choices:
                    - "FULL"
                    - "SCHEMA"
                    - "TABLE"
                    - "TABLESPACE"
                    - "TRANSPORTABLE"
            data_pump_parameters:
                description:
                    - ""
                type: dict
                suboptions:
                    is_cluster:
                        description:
                            - Set to false to force Data Pump worker process to run on one instance.
                            - This parameter is updatable.
                        type: bool
                    estimate:
                        description:
                            - Estimate size of dumps that will be generated.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "BLOCKS"
                            - "STATISTICS"
                    table_exists_action:
                        description:
                            - "IMPORT: Specifies the action to be performed when data is loaded into a preexisting table."
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "TRUNCATE"
                            - "REPLACE"
                            - "APPEND"
                            - "SKIP"
                    exclude_parameters:
                        description:
                            - Exclude paratemers for Export and Import.
                            - This parameter is updatable.
                        type: list
                    import_parallelism_degree:
                        description:
                            - Maximum number of worker processes that can be used for a Data Pump Import job.
                              For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.
                            - This parameter is updatable.
                        type: int
                    export_parallelism_degree:
                        description:
                            - Maximum number of worker processes that can be used for a Data Pump Export job.
                            - This parameter is updatable.
                        type: int
            metadata_remaps:
                description:
                    - Defines remapping to be applied to objects as they are processed.
                      Refer to L(DATA_REMAP,https://docs.oracle.com/en/database/oracle/oracle-
                      database/19/arpls/DBMS_DATAPUMP.html#GUID-E75AAE6F-4EA6-4737-A752-6B62F5E9D460)
                type: list
                suboptions:
                    type:
                        description:
                            - Type of remap. Refer to L(METADATA_REMAP Procedure ,https://docs.oracle.com/en/database/oracle/oracle-
                              database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)
                        type: str
                        choices:
                            - "SCHEMA"
                            - "TABLESPACE"
                            - "DATAFILE"
                            - "TABLE"
                        required: true
                    old_value:
                        description:
                            - Specifies the value which needs to be reset.
                        type: str
                        required: true
                    new_value:
                        description:
                            - Specifies the new value that oldValue should be translated into.
                        type: str
                        required: true
            export_directory_object:
                description:
                    - ""
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of directory object in database
                            - This parameter is updatable.
                        type: str
                    path:
                        description:
                            - Absolute path of directory on database server
                            - This parameter is updatable.
                        type: str
            import_directory_object:
                description:
                    - ""
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of directory object in database
                            - This parameter is updatable.
                        type: str
                    path:
                        description:
                            - Absolute path of directory on database server
                            - This parameter is updatable.
                        type: str
    exclude_objects:
        description:
            - Database objects to exclude from migration.
            - This parameter is updatable.
        type: list
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
    golden_gate_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            hub:
                description:
                    - ""
                type: dict
                suboptions:
                    rest_admin_credentials:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            username:
                                description:
                                    - Administrator username
                                    - This parameter is updatable.
                                type: str
                            password:
                                description:
                                    - Administrator password
                                    - This parameter is updatable.
                                type: str
                    source_db_admin_credentials:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            username:
                                description:
                                    - Administrator username
                                    - This parameter is updatable.
                                type: str
                            password:
                                description:
                                    - Administrator password
                                    - This parameter is updatable.
                                type: str
                    source_container_db_admin_credentials:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            username:
                                description:
                                    - Administrator username
                                    - This parameter is updatable.
                                type: str
                            password:
                                description:
                                    - Administrator password
                                    - This parameter is updatable.
                                type: str
                    target_db_admin_credentials:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            username:
                                description:
                                    - Administrator username
                                    - This parameter is updatable.
                                type: str
                            password:
                                description:
                                    - Administrator password
                                    - This parameter is updatable.
                                type: str
                    url:
                        description:
                            - Oracle GoldenGate Microservices hub's REST endpoint.
                              Refer to
                              https://docs.oracle.com/en/middleware/goldengate/core/19.1/securing/network.html#GUID-A709DA55-111D-455E-8942-C9BDD1E38CAA
                            - This parameter is updatable.
                        type: str
                    source_microservices_deployment_name:
                        description:
                            - Name of GoldenGate Microservices deployment to operate on source database
                            - This parameter is updatable.
                        type: str
                    target_microservices_deployment_name:
                        description:
                            - Name of GoldenGate Microservices deployment to operate on target database
                            - This parameter is updatable.
                        type: str
                    compute_id:
                        description:
                            - OCID of GoldenGate Microservices compute instance.
                            - This parameter is updatable.
                        type: str
            settings:
                description:
                    - ""
                type: dict
                suboptions:
                    extract:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            performance_profile:
                                description:
                                    - Extract performance.
                                    - This parameter is updatable.
                                type: str
                                choices:
                                    - "LOW"
                                    - "MEDIUM"
                                    - "HIGH"
                            long_trans_duration:
                                description:
                                    - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction
                                      is long-running.
                                      If not specified, Extract will not generate a warning on long-running transactions.
                                    - This parameter is updatable.
                                type: int
                    replicat:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            map_parallelism:
                                description:
                                    - Number of threads used to read trail files (valid for Parallel Replicat)
                                    - This parameter is updatable.
                                type: int
                            min_apply_parallelism:
                                description:
                                    - Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    - This parameter is updatable.
                                type: int
                            max_apply_parallelism:
                                description:
                                    - Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)
                                    - This parameter is updatable.
                                type: int
                    acceptable_lag:
                        description:
                            - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                            - This parameter is updatable.
                        type: int
    vault_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            compartment_id:
                description:
                    - OCID of the compartment where the secret containing the credentials will be created.
                    - This parameter is updatable.
                type: str
            vault_id:
                description:
                    - OCID of the vault
                    - This parameter is updatable.
                type: str
            key_id:
                description:
                    - OCID of the vault encryption key
                    - This parameter is updatable.
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    migration_id:
        description:
            - The OCID of the migration
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Migration.
            - Use I(state=present) to create or update a Migration.
            - Use I(state=absent) to delete a Migration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create migration
  oci_database_migration_migration:
    type: ONLINE
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_migration:
    type: ONLINE
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    exclude_objects:
    - owner: owner_example
      object_name: object_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update migration
  oci_database_migration_migration:
    type: ONLINE
    display_name: display_name_example
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete migration
  oci_database_migration_migration:
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_migration:
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Migration Display Name
            returned: on success
            type: string
            sample: display_name_example
        compartment_id:
            description:
                - OCID of the compartment
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - Migration type.
            returned: on success
            type: string
            sample: ONLINE
        wait_after:
            description:
                - Name of a migration phase. The Job will wait after executing this
                  phase until the Resume Job endpoint is called.
            returned: on success
            type: string
            sample: ODMS_VALIDATE_TGT
        agent_id:
            description:
                - The OCID of the registered on-premises ODMS Agent. Only valid for Offline Migrations.
            returned: on success
            type: string
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        credentials_secret_id:
            description:
                - OCID of the Secret in the OCI vault containing the Migration credentials. Used to store GoldenGate administrator user credentials.
            returned: on success
            type: string
            sample: "ocid1.credentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
        source_database_connection_id:
            description:
                - The OCID of the Source Database Connection.
            returned: on success
            type: string
            sample: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        source_container_database_connection_id:
            description:
                - The OCID of the Source Container Database Connection.
            returned: on success
            type: string
            sample: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id:
            description:
                - The OCID of the Target Database Connection.
            returned: on success
            type: string
            sample: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        executing_job_id:
            description:
                - OCID of the current ODMS Job in execution for the Migration, if any.
            returned: on success
            type: string
            sample: "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx"
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
                            type: string
                            sample: name_example
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
                            type: string
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Bucket name.
                            returned: on success
                            type: string
                            sample: bucket_name_example
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
                    type: string
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
                            type: string
                            sample: BLOCKS
                        table_exists_action:
                            description:
                                - "IMPORT: Specifies the action to be performed when data is loaded into a preexisting table."
                            returned: on success
                            type: string
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
                            type: string
                            sample: SCHEMA
                        old_value:
                            description:
                                - Specifies the value which needs to be reset.
                            returned: on success
                            type: string
                            sample: old_value_example
                        new_value:
                            description:
                                - Specifies the new value that oldValue should be translated into.
                            returned: on success
                            type: string
                            sample: new_value_example
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
                            type: string
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: string
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
                            type: string
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: string
                            sample: path_example
        exclude_objects:
            description:
                - Database objects to exclude from migration.
            returned: on success
            type: complex
            contains:
                owner:
                    description:
                        - Owner of the object (regular expression is allowed)
                    returned: on success
                    type: string
                    sample: owner_example
                object_name:
                    description:
                        - Name of the object (regular expression is allowed)
                    returned: on success
                    type: string
                    sample: object_name_example
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
                                    type: string
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
                                    type: string
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
                                    type: string
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
                                    type: string
                                    sample: username_example
                        url:
                            description:
                                - Oracle GoldenGate hub's REST endpoint.
                                  Refer to
                                  https://docs.oracle.com/en/middleware/goldengate/core/19.1/securing/network.html#GUID-A709DA55-111D-455E-8942-C9BDD1E38CAA
                            returned: on success
                            type: string
                            sample: url_example
                        source_microservices_deployment_name:
                            description:
                                - Name of GoldenGate deployment to operate on source database
                            returned: on success
                            type: string
                            sample: source_microservices_deployment_name_example
                        target_microservices_deployment_name:
                            description:
                                - Name of GoldenGate deployment to operate on target database
                            returned: on success
                            type: string
                            sample: target_microservices_deployment_name_example
                        compute_id:
                            description:
                                - OCID of GoldenGate compute instance.
                            returned: on success
                            type: string
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
                                    type: string
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
                    type: string
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - OCID of the vault
                    returned: on success
                    type: string
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                key_id:
                    description:
                        - OCID of the vault encryption key
                    returned: on success
                    type: string
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the Migration was created. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time of the last Migration details update. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_migration:
            description:
                - The time of last Migration. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the Migration resource.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - Additional status related to the execution and current state of the Migration.
            returned: on success
            type: string
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
        "data_transfer_medium_details": {
            "database_link_details": {
                "name": "name_example"
            },
            "object_storage_details": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            }
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
            "export_directory_object": {
                "name": "name_example",
                "path": "path_example"
            },
            "import_directory_object": {
                "name": "name_example",
                "path": "path_example"
            }
        },
        "exclude_objects": [{
            "owner": "owner_example",
            "object_name": "object_name_example"
        }],
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
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import CreateMigrationDetails
    from oci.database_migration.models import UpdateMigrationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_migrations, **kwargs
        )

    def get_create_model_class(self):
        return CreateMigrationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_migration_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMigrationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                update_migration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(migration_id=self.module.params.get("migration_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationHelperCustom = get_custom_class("MigrationHelperCustom")


class ResourceHelper(MigrationHelperCustom, MigrationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            type=dict(type="str", choices=["ONLINE", "OFFLINE"]),
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            agent_id=dict(type="str"),
            source_database_connection_id=dict(type="str"),
            source_container_database_connection_id=dict(type="str"),
            target_database_connection_id=dict(type="str"),
            data_transfer_medium_details=dict(
                type="dict",
                options=dict(
                    database_link_details=dict(
                        type="dict", options=dict(name=dict(type="str", required=True))
                    ),
                    object_storage_details=dict(
                        type="dict",
                        options=dict(
                            namespace_name=dict(type="str"),
                            bucket_name=dict(type="str"),
                        ),
                    ),
                ),
            ),
            datapump_settings=dict(
                type="dict",
                options=dict(
                    job_mode=dict(
                        type="str",
                        choices=[
                            "FULL",
                            "SCHEMA",
                            "TABLE",
                            "TABLESPACE",
                            "TRANSPORTABLE",
                        ],
                    ),
                    data_pump_parameters=dict(
                        type="dict",
                        options=dict(
                            is_cluster=dict(type="bool"),
                            estimate=dict(type="str", choices=["BLOCKS", "STATISTICS"]),
                            table_exists_action=dict(
                                type="str",
                                choices=["TRUNCATE", "REPLACE", "APPEND", "SKIP"],
                            ),
                            exclude_parameters=dict(type="list"),
                            import_parallelism_degree=dict(type="int"),
                            export_parallelism_degree=dict(type="int"),
                        ),
                    ),
                    metadata_remaps=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=["SCHEMA", "TABLESPACE", "DATAFILE", "TABLE"],
                            ),
                            old_value=dict(type="str", required=True),
                            new_value=dict(type="str", required=True),
                        ),
                    ),
                    export_directory_object=dict(
                        type="dict",
                        options=dict(name=dict(type="str"), path=dict(type="str")),
                    ),
                    import_directory_object=dict(
                        type="dict",
                        options=dict(name=dict(type="str"), path=dict(type="str")),
                    ),
                ),
            ),
            exclude_objects=dict(
                type="list",
                elements="dict",
                options=dict(
                    owner=dict(type="str", required=True),
                    object_name=dict(type="str", required=True),
                ),
            ),
            golden_gate_details=dict(
                type="dict",
                options=dict(
                    hub=dict(
                        type="dict",
                        options=dict(
                            rest_admin_credentials=dict(
                                type="dict",
                                options=dict(
                                    username=dict(type="str"),
                                    password=dict(type="str", no_log=True),
                                ),
                            ),
                            source_db_admin_credentials=dict(
                                type="dict",
                                options=dict(
                                    username=dict(type="str"),
                                    password=dict(type="str", no_log=True),
                                ),
                            ),
                            source_container_db_admin_credentials=dict(
                                type="dict",
                                options=dict(
                                    username=dict(type="str"),
                                    password=dict(type="str", no_log=True),
                                ),
                            ),
                            target_db_admin_credentials=dict(
                                type="dict",
                                options=dict(
                                    username=dict(type="str"),
                                    password=dict(type="str", no_log=True),
                                ),
                            ),
                            url=dict(type="str"),
                            source_microservices_deployment_name=dict(type="str"),
                            target_microservices_deployment_name=dict(type="str"),
                            compute_id=dict(type="str"),
                        ),
                    ),
                    settings=dict(
                        type="dict",
                        options=dict(
                            extract=dict(
                                type="dict",
                                options=dict(
                                    performance_profile=dict(
                                        type="str", choices=["LOW", "MEDIUM", "HIGH"]
                                    ),
                                    long_trans_duration=dict(type="int"),
                                ),
                            ),
                            replicat=dict(
                                type="dict",
                                options=dict(
                                    map_parallelism=dict(type="int"),
                                    min_apply_parallelism=dict(type="int"),
                                    max_apply_parallelism=dict(type="int"),
                                ),
                            ),
                            acceptable_lag=dict(type="int"),
                        ),
                    ),
                ),
            ),
            vault_details=dict(
                type="dict",
                options=dict(
                    compartment_id=dict(type="str"),
                    vault_id=dict(type="str"),
                    key_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            migration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
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
