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
module: oci_optimizer_recommendation_actions
short_description: Perform actions on a Recommendation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Recommendation resource in Oracle Cloud Infrastructure
    - For I(action=bulk_apply), applies the specified recommendations to the resources.
version_added: "2.9"
author: Oracle (@oracle)
options:
    recommendation_id:
        description:
            - The unique OCID associated with the recommendation.
        type: str
        aliases: ["id"]
        required: true
    resource_action_ids:
        description:
            - The unique OCIDs of the resource actions that recommendations are applied to. The recommendation will be applied to the given OCIDs irrespective
              of the existing status.
        type: list
    actions:
        description:
            - The unique resource actions that recommendations are applied to.
        type: list
        suboptions:
            resource_action_id:
                description:
                    - The unique OCIDs of the resource actions that recommendations are applied to.
                type: str
                required: true
            status:
                description:
                    - The current status of the recommendation.
                type: str
                choices:
                    - "PENDING"
                    - "DISMISSED"
                    - "POSTPONED"
                    - "IMPLEMENTED"
            time_status_end:
                description:
                    - The date and time the current status will change. The format is defined by RFC3339.
                    - "For example, \\"The current `postponed` status of the resource action will end and change to `pending` on this
                      date and time.\\""
                type: str
            parameters:
                description:
                    - "Additional parameter key-value pairs defining the resource action.
                      For example:"
                    - "`{\\"timeAmount\\": 15, \\"timeUnit\\": \\"seconds\\"}`"
                type: dict
            strategy_name:
                description:
                    - The name of the strategy.
                type: str
    status:
        description:
            - The current status of the recommendation.
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
        type: str
    action:
        description:
            - The action to perform on the Recommendation.
        type: str
        required: true
        choices:
            - "bulk_apply"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action bulk_apply on recommendation
  oci_optimizer_recommendation_actions:
    recommendation_id: ocid1.recommendation.oc1..xxxxxxEXAMPLExxxxxx
    status: PENDING
    action: bulk_apply

"""

RETURN = """
recommendation:
    description:
        - Details of the Recommendation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique OCID associated with the recommendation.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the tenancy. The tenancy is the root compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        category_id:
            description:
                - The unique OCID associated with the category.
            returned: on success
            type: string
            sample: ocid1.category.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name assigned to the recommendation.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - Text describing the recommendation.
            returned: on success
            type: string
            sample: description_example
        importance:
            description:
                - The level of importance assigned to the recommendation.
            returned: on success
            type: string
            sample: CRITICAL
        resource_counts:
            description:
                - An array of `ResourceCount` objects grouped by the status of the resource actions.
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - The recommendation status of the resource.
                    returned: on success
                    type: string
                    sample: PENDING
                count:
                    description:
                        - The count of resources.
                    returned: on success
                    type: int
                    sample: 56
        lifecycle_state:
            description:
                - The recommendation's current state.
            returned: on success
            type: string
            sample: ACTIVE
        estimated_cost_saving:
            description:
                - The estimated cost savings, in dollars, for the recommendation.
            returned: on success
            type: float
            sample: 1.2
        status:
            description:
                - The current status of the recommendation.
            returned: on success
            type: string
            sample: PENDING
        time_status_begin:
            description:
                - The date and time that the recommendation entered its current status. The format is defined by RFC3339.
                - "For example, \\"The status of the recommendation changed from `pending` to `current(ignored)` on this date and time.\\""
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_status_end:
            description:
                - The date and time the current status will change. The format is defined by RFC3339.
                - "For example, \\"The current `postponed` status of the recommendation will end and change to `pending` on this
                  date and time.\\""
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - The date and time the recommendation details were created, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the recommendation details were last updated, in the format defined by RFC3339.
            returned: on success
            type: string
            sample: 2020-08-25T21:10:29.600Z
        supported_levels:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the profile level.
                    returned: on success
                    type: string
                    sample: name_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "category_id": "ocid1.category.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "importance": "CRITICAL",
        "resource_counts": [{
            "status": "PENDING",
            "count": 56
        }],
        "lifecycle_state": "ACTIVE",
        "estimated_cost_saving": 1.2,
        "status": "PENDING",
        "time_status_begin": "2013-10-20T19:20:30+01:00",
        "time_status_end": "2013-10-20T19:20:30+01:00",
        "time_created": "2020-08-25T21:10:29.600Z",
        "time_updated": "2020-08-25T21:10:29.600Z",
        "supported_levels": {
            "name": "name_example"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.optimizer import OptimizerClient
    from oci.optimizer.models import BulkApplyRecommendationsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecommendationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_apply
    """

    @staticmethod
    def get_module_resource_id_param():
        return "recommendation_id"

    def get_module_resource_id(self):
        return self.module.params.get("recommendation_id")

    def get_get_fn(self):
        return self.client.get_recommendation

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_recommendation,
            recommendation_id=self.module.params.get("recommendation_id"),
        )

    def bulk_apply(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkApplyRecommendationsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_apply_recommendations,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recommendation_id=self.module.params.get("recommendation_id"),
                bulk_apply_recommendations_details=action_details,
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


RecommendationActionsHelperCustom = get_custom_class(
    "RecommendationActionsHelperCustom"
)


class ResourceHelper(RecommendationActionsHelperCustom, RecommendationActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            recommendation_id=dict(aliases=["id"], type="str", required=True),
            resource_action_ids=dict(type="list"),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    resource_action_id=dict(type="str", required=True),
                    status=dict(
                        type="str",
                        choices=["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"],
                    ),
                    time_status_end=dict(type="str"),
                    parameters=dict(type="dict"),
                    strategy_name=dict(type="str"),
                ),
            ),
            status=dict(
                type="str",
                required=True,
                choices=["PENDING", "DISMISSED", "POSTPONED", "IMPLEMENTED"],
            ),
            time_status_end=dict(type="str"),
            action=dict(type="str", required=True, choices=["bulk_apply"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="recommendation",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
