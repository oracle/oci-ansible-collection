#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
                - Returned for get operation
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
                - Returned for get operation
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
        data_transfer_medium_details:
            description:
                - ""
                - Returned for get operation
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
        dump_transfer_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
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
        datapump_settings:
            description:
                - ""
                - Returned for get operation
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
        exclude_objects:
            description:
                - "Database objects to exclude from migration.
                  If 'includeObjects' are specified, only exclude object types can be specified with general wildcards (.*) for owner and objectName."
                - Returned for get operation
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
        include_objects:
            description:
                - Database objects to include from migration.
                - Returned for get operation
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
        golden_gate_details:
            description:
                - ""
                - Returned for get operation
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
    sample: [{
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
                "name": "name_example",
                "wallet_bucket": {
                    "namespace_name": "namespace_name_example",
                    "bucket_name": "bucket_name_example"
                }
            },
            "object_storage_details": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            }
        },
        "dump_transfer_details": {
            "source": {
                "kind": "CURL",
                "oci_home": "oci_home_example"
            },
            "target": {
                "kind": "CURL",
                "oci_home": "oci_home_example"
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
        "advisor_settings": {
            "is_skip_advisor": true,
            "is_ignore_errors": true
        },
        "exclude_objects": [{
            "owner": "owner_example",
            "object_name": "object_name_example",
            "type": "type_example"
        }],
        "include_objects": [{
            "owner": "owner_example",
            "object_name": "object_name_example",
            "type": "type_example"
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
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

    module = AnsibleModule(argument_spec=module_args)

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
