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
module: oci_apigateway_usage_plan_actions
short_description: Perform actions on an UsagePlan resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an UsagePlan resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), changes the usage plan compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    usage_plan_id:
        description:
            - The ocid of the usage plan.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
        type: str
        required: true
    action:
        description:
            - The action to perform on the UsagePlan.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on usage_plan
  oci_apigateway_usage_plan_actions:
    # required
    usage_plan_id: "ocid1.usageplan.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
usage_plan:
    description:
        - Details of the UsagePlan resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a usage plan
                  resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: str
            sample: display_name_example
        entitlements:
            description:
                - A collection of entitlements currently assigned to the usage plan.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - An entitlement name, unique within a usage plan.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - A user-friendly description. To provide some insight about the resource.
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: description_example
                rate_limit:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        value:
                            description:
                                - The number of requests that can be made per time period.
                            returned: on success
                            type: int
                            sample: 56
                        unit:
                            description:
                                - "The unit of time over which rate limits are calculated.
                                  Example: `SECOND`"
                            returned: on success
                            type: str
                            sample: SECOND
                quota:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        value:
                            description:
                                - The number of requests that can be made per time period.
                            returned: on success
                            type: int
                            sample: 56
                        unit:
                            description:
                                - "The unit of time over which quotas are calculated.
                                  Example: `MINUTE` or `MONTH`"
                            returned: on success
                            type: str
                            sample: MINUTE
                        reset_policy:
                            description:
                                - "The policy that controls when quotas will reset.
                                  Example: `CALENDAR`"
                            returned: on success
                            type: str
                            sample: CALENDAR
                        operation_on_breach:
                            description:
                                - "What the usage plan will do when a quota is breached:
                                  `REJECT` will allow no further requests
                                  `ALLOW` will continue to allow further requests"
                            returned: on success
                            type: str
                            sample: REJECT
                targets:
                    description:
                        - A collection of targeted deployments that the entitlement will be applied to.
                    returned: on success
                    type: complex
                    contains:
                        deployment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a deployment
                                  resource.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the usage plan.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair
                  with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "entitlements": [{
            "name": "name_example",
            "description": "description_example",
            "rate_limit": {
                "value": 56,
                "unit": "SECOND"
            },
            "quota": {
                "value": 56,
                "unit": "MINUTE",
                "reset_policy": "CALENDAR",
                "operation_on_breach": "REJECT"
            },
            "targets": [{
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import UsagePlansClient
    from oci.apigateway.models import ChangeUsagePlanCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayUsagePlanActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    @staticmethod
    def get_module_resource_id_param():
        return "usage_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("usage_plan_id")

    def get_get_fn(self):
        return self.client.get_usage_plan

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_usage_plan,
            usage_plan_id=self.module.params.get("usage_plan_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeUsagePlanCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_usage_plan_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                usage_plan_id=self.module.params.get("usage_plan_id"),
                change_usage_plan_compartment_details=action_details,
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


ApigatewayUsagePlanActionsHelperCustom = get_custom_class(
    "ApigatewayUsagePlanActionsHelperCustom"
)


class ResourceHelper(
    ApigatewayUsagePlanActionsHelperCustom, ApigatewayUsagePlanActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            usage_plan_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="usage_plan",
        service_client_class=UsagePlansClient,
        namespace="apigateway",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
