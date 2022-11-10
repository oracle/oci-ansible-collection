#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_apigateway_usage_plan_facts
short_description: Fetches details about one or multiple UsagePlan resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UsagePlan resources in Oracle Cloud Infrastructure
    - Returns a list of usage plans.
    - If I(usage_plan_id) is specified, the details of a single UsagePlan will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    usage_plan_id:
        description:
            - The ocid of the usage plan.
            - Required to get a specific usage_plan.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ocid of the compartment in which to list resources.
            - Required to list multiple usage_plans.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - "A filter to return only resources that match the given lifecycle state.
              Example: `ACTIVE`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for `timeCreated` is descending. Default order for
              `displayName` is ascending. The `displayName` sort order is case
              sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific usage_plan
  oci_apigateway_usage_plan_facts:
    # required
    usage_plan_id: "ocid1.usageplan.oc1..xxxxxxEXAMPLExxxxxx"

- name: List usage_plans
  oci_apigateway_usage_plan_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
usage_plans:
    description:
        - List of UsagePlan resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import UsagePlansClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayUsagePlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "usage_plan_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_usage_plan,
            usage_plan_id=self.module.params.get("usage_plan_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_usage_plans,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApigatewayUsagePlanFactsHelperCustom = get_custom_class(
    "ApigatewayUsagePlanFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayUsagePlanFactsHelperCustom, ApigatewayUsagePlanFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            usage_plan_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="usage_plan",
        service_client_class=UsagePlansClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(usage_plans=result)


if __name__ == "__main__":
    main()
