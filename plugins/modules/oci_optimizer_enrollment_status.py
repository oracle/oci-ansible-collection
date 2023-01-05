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
module: oci_optimizer_enrollment_status
short_description: Manage an EnrollmentStatus resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an EnrollmentStatus resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    enrollment_status_id:
        description:
            - The unique OCID associated with the enrollment status.
        type: str
        aliases: ["id"]
        required: true
    status:
        description:
            - The Cloud Advisor enrollment status.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
        required: true
    state:
        description:
            - The state of the EnrollmentStatus.
            - Use I(state=present) to update an existing an EnrollmentStatus.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update enrollment_status
  oci_optimizer_enrollment_status:
    # required
    enrollment_status_id: "ocid1.enrollmentstatus.oc1..xxxxxxEXAMPLExxxxxx"
    status: ACTIVE

"""

RETURN = """
enrollment_status:
    description:
        - Details of the EnrollmentStatus resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the enrollment status.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The enrollment status' current state.
            returned: on success
            type: str
            sample: ACTIVE
        status:
            description:
                - The current Cloud Advisor enrollment status.
            returned: on success
            type: str
            sample: ACTIVE
        status_reason:
            description:
                - The reason for the enrollment status of the tenancy.
            returned: on success
            type: str
            sample: status_reason_example
        time_created:
            description:
                - The date and time the enrollment status was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the enrollment status was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "status": "ACTIVE",
        "status_reason": "status_reason_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.optimizer import OptimizerClient
    from oci.optimizer.models import UpdateEnrollmentStatusDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnrollmentStatusHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(EnrollmentStatusHelperGen, self).get_possible_entity_types() + [
            "enrollmentstatus",
            "enrollmentstatuses",
            "optimizerenrollmentstatus",
            "optimizerenrollmentstatuses",
            "enrollmentstatusresource",
            "enrollmentstatusesresource",
            "optimizer",
        ]

    def get_module_resource_id_param(self):
        return "enrollment_status_id"

    def get_module_resource_id(self):
        return self.module.params.get("enrollment_status_id")

    def get_get_fn(self):
        return self.client.get_enrollment_status

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_enrollment_status, enrollment_status_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_enrollment_status,
            enrollment_status_id=self.module.params.get("enrollment_status_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["status"]

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
            self.client.list_enrollment_statuses, **kwargs
        )

    def get_update_model_class(self):
        return UpdateEnrollmentStatusDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_enrollment_status,
            call_fn_args=(),
            call_fn_kwargs=dict(
                enrollment_status_id=self.module.params.get("enrollment_status_id"),
                update_enrollment_status_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


EnrollmentStatusHelperCustom = get_custom_class("EnrollmentStatusHelperCustom")


class ResourceHelper(EnrollmentStatusHelperCustom, EnrollmentStatusHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            enrollment_status_id=dict(aliases=["id"], type="str", required=True),
            status=dict(type="str", required=True, choices=["ACTIVE", "INACTIVE"]),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="enrollment_status",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
