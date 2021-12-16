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
module: oci_optimizer_resource_action
short_description: Manage a ResourceAction resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a ResourceAction resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resource_action_id:
        description:
            - The unique OCID associated with the resource action.
        type: str
        aliases: ["id"]
        required: true
    status:
        description:
            - The status of the resource action.
        type: str
        choices:
            - "PENDING"
            - "DISMISSED"
            - "POSTPONED"
            - "IMPLEMENTED"
        required: true
    time_status_end:
        description:
            - The date and time the current status will change. The format is defined by RFC3339.
            - "For example, \\"The current `postponed` status of the resource action will end and change to `pending` on this
              date and time.\\""
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the ResourceAction.
            - Use I(state=present) to update an existing a ResourceAction.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update resource_action
  oci_optimizer_resource_action:
    # required
    resource_action_id: "ocid1.resourceaction.oc1..xxxxxxEXAMPLExxxxxx"
    status: PENDING

    # optional
    time_status_end: time_status_end_example

"""

RETURN = """
resource_action:
    description:
        - Details of the ResourceAction resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID associated with the resource action.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        category_id:
            description:
                - The unique OCID associated with the category.
            returned: on success
            type: str
            sample: "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx"
        recommendation_id:
            description:
                - The unique OCID associated with the recommendation.
            returned: on success
            type: str
            sample: "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The unique OCID associated with the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name assigned to the resource.
            returned: on success
            type: str
            sample: name_example
        resource_type:
            description:
                - The kind of resource.
            returned: on success
            type: str
            sample: resource_type_example
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_name:
            description:
                - The name associated with the compartment.
            returned: on success
            type: str
            sample: compartment_name_example
        action:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The status of the resource action.
                    returned: on success
                    type: str
                    sample: KB_ARTICLE
                description:
                    description:
                        - Text describing the recommended action.
                    returned: on success
                    type: str
                    sample: description_example
                url:
                    description:
                        - The URL path to documentation that explains how to perform the action.
                    returned: on success
                    type: str
                    sample: url_example
        lifecycle_state:
            description:
                - The resource action's current state.
            returned: on success
            type: str
            sample: ACTIVE
        estimated_cost_saving:
            description:
                - The estimated cost savings, in dollars, for the resource action.
            returned: on success
            type: float
            sample: 1.2
        status:
            description:
                - The current status of the resource action.
            returned: on success
            type: str
            sample: PENDING
        time_status_begin:
            description:
                - The date and time that the resource action entered its current status. The format is defined by RFC3339.
                - "For example, \\"The status of the resource action changed from `pending` to `current(ignored)` on this date and time.\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_status_end:
            description:
                - The date and time the current status will change. The format is defined by RFC3339.
                - "For example, \\"The current `postponed` status of the resource action will end and change to `pending` on this
                  date and time.\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        metadata:
            description:
                - Custom metadata key/value pairs for the resource action.
                - "**Metadata Example**"
                - "     \\"metadata\\" : {
                           \\"cpuRecommendedShape\\": \\"VM.Standard1.1\\",
                           \\"computeMemoryUtilization\\": \\"26.05734124418388\\",
                           \\"currentShape\\": \\"VM.Standard1.2\\",
                           \\"instanceRecommendedShape\\": \\"VM.Standard1.1\\",
                           \\"computeCpuUtilization\\": \\"7.930035319720132\\",
                           \\"memoryRecommendedShape\\": \\"None\\"
                        }"
            returned: on success
            type: dict
            sample: {}
        extended_metadata:
            description:
                - Additional metadata key/value pairs that you provide.
                  They serve the same purpose and functionality as fields in the `metadata` object.
                - They are distinguished from `metadata` fields in that these can be nested JSON objects (whereas `metadata` fields are string/string maps
                  only).
                - "For example:"
                - "`{\\"CurrentShape\\": {\\"name\\":\\"VM.Standard2.16\\"}, \\"RecommendedShape\\": {\\"name\\":\\"VM.Standard2.8\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The date and time the resource action details were created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource action details were last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "recommendation_id": "ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "resource_type": "resource_type_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_name": "compartment_name_example",
        "action": {
            "type": "KB_ARTICLE",
            "description": "description_example",
            "url": "url_example"
        },
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "status": "PENDING",
        "time_status_begin": "2013-10-20T19:20:30+01:00",
        "time_status_end": "2013-10-20T19:20:30+01:00",
        "metadata": {},
        "extended_metadata": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.optimizer import OptimizerClient
    from oci.optimizer.models import UpdateResourceActionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceActionHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_module_resource_id_param(self):
        return "resource_action_id"

    def get_module_resource_id(self):
        return self.module.params.get("resource_action_id")

    def get_get_fn(self):
        return self.client.get_resource_action

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_resource_action,
            resource_action_id=self.module.params.get("resource_action_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "compartment_id_in_subtree",
            "recommendation_id",
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
            self.client.list_resource_actions, **kwargs
        )

    def get_update_model_class(self):
        return UpdateResourceActionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_resource_action,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resource_action_id=self.module.params.get("resource_action_id"),
                update_resource_action_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


ResourceActionHelperCustom = get_custom_class("ResourceActionHelperCustom")


class ResourceHelper(ResourceActionHelperCustom, ResourceActionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            resource_action_id=dict(aliases=["id"], type="str", required=True),
            status=dict(
                type="str",
                required=True,
                choices=["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"],
            ),
            time_status_end=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="resource_action",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
