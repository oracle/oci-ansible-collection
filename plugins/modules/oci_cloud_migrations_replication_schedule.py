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
module: oci_cloud_migrations_replication_schedule
short_description: Manage a ReplicationSchedule resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ReplicationSchedule resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a replication schedule.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_migrations_replication_schedule_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the replication schedule should be
              created.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name for a replication schedule. Does not have to be unique, and is mutable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    execution_recurrences:
        description:
            - Recurrence specification for replication schedule execution.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    replication_schedule_id:
        description:
            - Unique replication schedule identifier in path
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ReplicationSchedule.
            - Use I(state=present) to create or update a ReplicationSchedule.
            - Use I(state=absent) to delete a ReplicationSchedule.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create replication_schedule
  oci_cloud_migrations_replication_schedule:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    execution_recurrences: execution_recurrences_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update replication_schedule
  oci_cloud_migrations_replication_schedule:
    # required
    replication_schedule_id: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    execution_recurrences: execution_recurrences_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update replication_schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_replication_schedule:
    # required
    display_name: display_name_example

    # optional
    execution_recurrences: execution_recurrences_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete replication_schedule
  oci_cloud_migrations_replication_schedule:
    # required
    replication_schedule_id: "ocid1.replicationschedule.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete replication_schedule using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_migrations_replication_schedule:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
replication_schedule:
    description:
        - Details of the ReplicationSchedule resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication schedule.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A name of the replication schedule.
            returned: on success
            type: str
            sample: display_name_example
        execution_recurrences:
            description:
                - Recurrence specification for the replication schedule execution.
            returned: on success
            type: str
            sample: execution_recurrences_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the replication schedule
                  exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Current state of the replication schedule.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - The detailed state of the replication schedule.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The time when the replication schedule was created in RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the replication schedule was last updated in RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "execution_recurrences": "execution_recurrences_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_migrations import MigrationClient
    from oci.cloud_migrations.models import CreateReplicationScheduleDetails
    from oci.cloud_migrations.models import UpdateReplicationScheduleDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ReplicationScheduleHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ReplicationScheduleHelperGen, self).get_possible_entity_types() + [
            "ocmreplicationschedule",
            "ocmreplicationschedules",
            "cloudMigrationsocmreplicationschedule",
            "cloudMigrationsocmreplicationschedules",
            "ocmreplicationscheduleresource",
            "ocmreplicationschedulesresource",
            "replicationschedule",
            "replicationschedules",
            "cloudMigrationsreplicationschedule",
            "cloudMigrationsreplicationschedules",
            "replicationscheduleresource",
            "replicationschedulesresource",
            "cloudmigrations",
        ]

    def get_module_resource_id_param(self):
        return "replication_schedule_id"

    def get_module_resource_id(self):
        return self.module.params.get("replication_schedule_id")

    def get_get_fn(self):
        return self.client.get_replication_schedule

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_schedule,
            replication_schedule_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_replication_schedule,
            replication_schedule_id=self.module.params.get("replication_schedule_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "replication_schedule_id",
        ]

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
            self.client.list_replication_schedules, **kwargs
        )

    def get_create_model_class(self):
        return CreateReplicationScheduleDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_replication_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(create_replication_schedule_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateReplicationScheduleDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_replication_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_schedule_id=self.module.params.get(
                    "replication_schedule_id"
                ),
                update_replication_schedule_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_replication_schedule,
            call_fn_args=(),
            call_fn_kwargs=dict(
                replication_schedule_id=self.module.params.get(
                    "replication_schedule_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ReplicationScheduleHelperCustom = get_custom_class("ReplicationScheduleHelperCustom")


class ResourceHelper(ReplicationScheduleHelperCustom, ReplicationScheduleHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            execution_recurrences=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            replication_schedule_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="replication_schedule",
        service_client_class=MigrationClient,
        namespace="cloud_migrations",
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
