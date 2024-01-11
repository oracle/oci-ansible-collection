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
module: oci_cloud_migrations_migration_actions
short_description: Perform actions on a Migration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Migration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a migration resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
    - For I(action=refresh), refreshes migration based on the migration ID.
    - For I(action=start_migration_replication), starts replication for a migration or for some asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    migration_id:
        description:
            - Unique migration identifier
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
            - "refresh"
            - "start_migration_replication"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on migration
  oci_cloud_migrations_migration_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action refresh on migration
  oci_cloud_migrations_migration_actions:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh

- name: Perform action start_migration_replication on migration
  oci_cloud_migrations_migration_actions:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    action: start_migration_replication

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
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Migration Identifier that can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of migration.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when the migration project was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the migration project was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        replication_schedule_id:
            description:
                - Replication schedule identifier
            returned: on success
            type: str
            sample: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
        is_completed:
            description:
                - Indicates whether migration is marked as completed.
            returned: on success
            type: bool
            sample: true
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
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
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "replication_schedule_id": "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "is_completed": true,
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
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import ChangeMigrationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        refresh
        start_migration_replication
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
            self.module.params, ChangeMigrationCompartmentDetails
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

    def refresh(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_migration,
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

    def start_migration_replication(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_migration_replication,
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
                choices=[
                    "change_compartment",
                    "refresh",
                    "start_migration_replication",
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
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
