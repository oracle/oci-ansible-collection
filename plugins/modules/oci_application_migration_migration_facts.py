#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_application_migration_migration_facts
short_description: Fetches details about one or multiple Migration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Migration resources in Oracle Cloud Infrastructure
    - Retrieves details of all the migrations that are available in the specified compartment.
    - If I(migration_id) is specified, the details of a single Migration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the migration.
            - Required to get a specific migration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of a compartment. Retrieves details of objects in the
              specified compartment.
            - Required to list multiple migrations.
        type: str
    sort_order:
        description:
            - The sort order, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field on which to sort.
              By default, `TIMECREATED` is ordered descending.
              By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    display_name:
        description:
            - Display name on which to query.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - This field is not supported. Do not use.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "SUCCEEDED"
            - "DELETING"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific migration
  oci_application_migration_migration_facts:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List migrations
  oci_application_migration_migration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    display_name: display_name_example
    lifecycle_state: CREATING

"""

RETURN = """
migrations:
    description:
        - List of Migration resources
    returned: on success
    type: complex
    contains:
        pre_created_target_database_type:
            description:
                - The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
                  Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance
                  types.
                - Returned for get operation
            returned: on success
            type: str
            sample: DATABASE_SYSTEM
        is_selective_migration:
            description:
                - If set to `true`, Application Migration migrates only the application resources that you specify. If set to `false`, Application Migration
                  migrates the entire application. When you migrate the entire application, all the application resources are migrated to the target
                  environment. You can selectively migrate resources only for the Oracle Integration Cloud and Oracle Integration Cloud Service applications.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        service_config:
            description:
                - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
                  to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
                  CreateMigration operation.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the configuration field.
                    returned: on success
                    type: str
                    sample: name_example
                group:
                    description:
                        - The name of the group to which this field belongs, if any.
                    returned: on success
                    type: str
                    sample: group_example
                type:
                    description:
                        - The type of the configuration field.
                    returned: on success
                    type: str
                    sample: type_example
                value:
                    description:
                        - The value of the field.
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Help text to guide the user in setting the configuration value.
                    returned: on success
                    type: str
                    sample: description_example
                resource_list:
                    description:
                        - A list of resources associated with a specific configuration object.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The display name of the resource field.
                            returned: on success
                            type: str
                            sample: name_example
                        group:
                            description:
                                - The name of the group to which this field belongs to.
                            returned: on success
                            type: str
                            sample: group_example
                        type:
                            description:
                                - The type of the resource field.
                            returned: on success
                            type: str
                            sample: type_example
                        value:
                            description:
                                - The value of the field.
                            returned: on success
                            type: str
                            sample: value_example
                is_required:
                    description:
                        - Indicates whether or not the field is required (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
                is_mutable:
                    description:
                        - Indicates whether or not the field may be modified (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
        application_config:
            description:
                - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
                  to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
                  CreateMigration operation.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the configuration field.
                    returned: on success
                    type: str
                    sample: name_example
                group:
                    description:
                        - The name of the group to which this field belongs, if any.
                    returned: on success
                    type: str
                    sample: group_example
                type:
                    description:
                        - The type of the configuration field.
                    returned: on success
                    type: str
                    sample: type_example
                value:
                    description:
                        - The value of the field.
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Help text to guide the user in setting the configuration value.
                    returned: on success
                    type: str
                    sample: description_example
                resource_list:
                    description:
                        - A list of resources associated with a specific configuration object.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The display name of the resource field.
                            returned: on success
                            type: str
                            sample: name_example
                        group:
                            description:
                                - The name of the group to which this field belongs to.
                            returned: on success
                            type: str
                            sample: group_example
                        type:
                            description:
                                - The type of the resource field.
                            returned: on success
                            type: str
                            sample: type_example
                        value:
                            description:
                                - The value of the field.
                            returned: on success
                            type: str
                            sample: value_example
                is_required:
                    description:
                        - Indicates whether or not the field is required (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
                is_mutable:
                    description:
                        - Indicates whether or not the field may be modified (defaults to `true`).
                    returned: on success
                    type: bool
                    sample: true
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the migration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the migration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name of the migration.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the migration.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The date and time at which the migration was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the source with which this migration is associated.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        application_name:
            description:
                - Name of the application which is being migrated. This is the name of the application in the source environment.
            returned: on success
            type: str
            sample: application_name_example
        application_type:
            description:
                - The type of application being migrated.
            returned: on success
            type: str
            sample: JCS
        lifecycle_state:
            description:
                - The current state of the migration.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current lifecycle state of the migration.
            returned: on success
            type: str
            sample: lifecycle_details_example
        migration_state:
            description:
                - The current state of the overall migration process.
            returned: on success
            type: str
            sample: DISCOVERING_APPLICATION
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example:
                  `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "pre_created_target_database_type": "DATABASE_SYSTEM",
        "is_selective_migration": true,
        "service_config": {
            "name": "name_example",
            "group": "group_example",
            "type": "type_example",
            "value": "value_example",
            "description": "description_example",
            "resource_list": [{
                "name": "name_example",
                "group": "group_example",
                "type": "type_example",
                "value": "value_example"
            }],
            "is_required": true,
            "is_mutable": true
        },
        "application_config": {
            "name": "name_example",
            "group": "group_example",
            "type": "type_example",
            "value": "value_example",
            "description": "description_example",
            "resource_list": [{
                "name": "name_example",
                "group": "group_example",
                "type": "type_example",
                "value": "value_example"
            }],
            "is_required": true,
            "is_mutable": true
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "application_name": "application_name_example",
        "application_type": "JCS",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "migration_state": "DISCOVERING_APPLICATION",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.application_migration import ApplicationMigrationClient

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
            "sort_order",
            "sort_by",
            "display_name",
            "lifecycle_state",
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
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "SUCCEEDED",
                    "DELETING",
                    "DELETED",
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
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
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
