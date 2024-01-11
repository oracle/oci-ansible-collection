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
module: oci_application_migration_migration_actions
short_description: Perform actions on a Migration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Migration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified migration into a different compartment within the same tenancy. For information about moving
      resources between compartments,
      see L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=migrate_application), starts migrating the specified application to Oracle Cloud Infrastructure.
      Before sending this request, ensure that you have provided configuration details to update the migration and the state of the migration
      is <code>READY</code>.
      After you send this request, the migration's state will temporarily be <code>MIGRATING</code>.
      To track the progress of the operation, you can monitor the status of the Migrate Application work request by using the
      <code>L(GetWorkRequest,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/applicationmigration/20191031/WorkRequest/GetWorkRequest)</code> REST API
      operation on the work request or by viewing the status of the work request in the console.
      When this work request is processed successfully, Application Migration creates the required resources in the target environment
      and the state of the migration changes to <code>MIGRATION_SUCCEEDED</code>.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    migration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the migration.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Migration.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "migrate_application"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on migration
  oci_application_migration_migration_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action migrate_application on migration
  oci_application_migration_migration_actions:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: migrate_application

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
        pre_created_target_database_type:
            description:
                - The pre-existing database type to be used in this migration. Currently, Application migration only supports Oracle Cloud
                  Infrastructure databases and this option is currently available only for `JAVA_CLOUD_SERVICE` and `WEBLOGIC_CLOUD_SERVICE` target instance
                  types.
            returned: on success
            type: str
            sample: DATABASE_SYSTEM
        is_selective_migration:
            description:
                - If set to `true`, Application Migration migrates only the application resources that you specify. If set to `false`, Application Migration
                  migrates the entire application. When you migrate the entire application, all the application resources are migrated to the target
                  environment. You can selectively migrate resources only for the Oracle Integration Cloud and Oracle Integration Cloud Service applications.
            returned: on success
            type: bool
            sample: true
        service_config:
            description:
                - Configuration required to migrate the application. In addition to the key and value, additional fields are provided
                  to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the
                  CreateMigration operation.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "application_name": "application_name_example",
        "application_type": "JCS",
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
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "migration_state": "DISCOVERING_APPLICATION",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.application_migration import ApplicationMigrationClient
    from oci.application_migration.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        migrate_application
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_migration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                change_migration_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def migrate_application(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.migrate_application,
            call_fn_args=(),
            call_fn_kwargs=dict(migration_id=self.module.params.get("migration_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationActionsHelperCustom = get_custom_class("MigrationActionsHelperCustom")


class ResourceHelper(MigrationActionsHelperCustom, MigrationActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            migration_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "migrate_application"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration",
        service_client_class=ApplicationMigrationClient,
        namespace="application_migration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
