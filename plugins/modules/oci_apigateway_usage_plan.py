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
module: oci_apigateway_usage_plan
short_description: Manage an UsagePlan resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an UsagePlan resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new usage plan.
    - "This resource has the following action operations in the M(oracle.oci.oci_apigateway_usage_plan_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - "Example: `My new resource`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    entitlements:
        description:
            - A collection of entitlements to assign to the newly created usage plan.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - An entitlement name, unique within a usage plan.
                type: str
                required: true
            description:
                description:
                    - A user-friendly description. To provide some insight about the resource.
                      Avoid entering confidential information.
                type: str
            rate_limit:
                description:
                    - ""
                type: dict
                suboptions:
                    value:
                        description:
                            - The number of requests that can be made per time period.
                        type: int
                        required: true
                    unit:
                        description:
                            - "The unit of time over which rate limits are calculated.
                              Example: `SECOND`"
                        type: str
                        choices:
                            - "SECOND"
                        required: true
            quota:
                description:
                    - ""
                type: dict
                suboptions:
                    value:
                        description:
                            - The number of requests that can be made per time period.
                        type: int
                        required: true
                    unit:
                        description:
                            - "The unit of time over which quotas are calculated.
                              Example: `MINUTE` or `MONTH`"
                        type: str
                        choices:
                            - "MINUTE"
                            - "HOUR"
                            - "DAY"
                            - "WEEK"
                            - "MONTH"
                        required: true
                    reset_policy:
                        description:
                            - "The policy that controls when quotas will reset.
                              Example: `CALENDAR`"
                        type: str
                        choices:
                            - "CALENDAR"
                        required: true
                    operation_on_breach:
                        description:
                            - "What the usage plan will do when a quota is breached:
                              `REJECT` will allow no further requests
                              `ALLOW` will continue to allow further requests"
                        type: str
                        choices:
                            - "REJECT"
                            - "ALLOW"
                        required: true
            targets:
                description:
                    - A collection of targeted deployments that the entitlement will be applied to.
                type: list
                elements: dict
                suboptions:
                    deployment_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of a deployment
                              resource.
                        type: str
                        required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair
              with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    usage_plan_id:
        description:
            - The ocid of the usage plan.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the UsagePlan.
            - Use I(state=present) to create or update an UsagePlan.
            - Use I(state=absent) to delete an UsagePlan.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create usage_plan
  oci_apigateway_usage_plan:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    entitlements:
    - # required
      name: name_example

      # optional
      description: description_example
      rate_limit:
        # required
        value: 56
        unit: SECOND
      quota:
        # required
        value: 56
        unit: MINUTE
        reset_policy: CALENDAR
        operation_on_breach: REJECT
      targets:
      - # required
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update usage_plan
  oci_apigateway_usage_plan:
    # required
    usage_plan_id: "ocid1.usageplan.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    entitlements:
    - # required
      name: name_example

      # optional
      description: description_example
      rate_limit:
        # required
        value: 56
        unit: SECOND
      quota:
        # required
        value: 56
        unit: MINUTE
        reset_policy: CALENDAR
        operation_on_breach: REJECT
      targets:
      - # required
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update usage_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_usage_plan:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    entitlements:
    - # required
      name: name_example

      # optional
      description: description_example
      rate_limit:
        # required
        value: 56
        unit: SECOND
      quota:
        # required
        value: 56
        unit: MINUTE
        reset_policy: CALENDAR
        operation_on_breach: REJECT
      targets:
      - # required
        deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete usage_plan
  oci_apigateway_usage_plan:
    # required
    usage_plan_id: "ocid1.usageplan.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete usage_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_usage_plan:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import UsagePlansClient
    from oci.apigateway.models import CreateUsagePlanDetails
    from oci.apigateway.models import UpdateUsagePlanDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayUsagePlanHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(ApigatewayUsagePlanHelperGen, self).get_possible_entity_types() + [
            "usageplan",
            "usageplans",
            "apigatewayusageplan",
            "apigatewayusageplans",
            "usageplanresource",
            "usageplansresource",
            "apigateway",
        ]

    def get_module_resource_id_param(self):
        return "usage_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("usage_plan_id")

    def get_get_fn(self):
        return self.client.get_usage_plan

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_usage_plan, usage_plan_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_usage_plan,
            usage_plan_id=self.module.params.get("usage_plan_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_usage_plans, **kwargs
        )

    def get_create_model_class(self):
        return CreateUsagePlanDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_usage_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(create_usage_plan_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateUsagePlanDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_usage_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                usage_plan_id=self.module.params.get("usage_plan_id"),
                update_usage_plan_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_usage_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(usage_plan_id=self.module.params.get("usage_plan_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayUsagePlanHelperCustom = get_custom_class("ApigatewayUsagePlanHelperCustom")


class ResourceHelper(ApigatewayUsagePlanHelperCustom, ApigatewayUsagePlanHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            entitlements=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    description=dict(type="str"),
                    rate_limit=dict(
                        type="dict",
                        options=dict(
                            value=dict(type="int", required=True),
                            unit=dict(type="str", required=True, choices=["SECOND"]),
                        ),
                    ),
                    quota=dict(
                        type="dict",
                        options=dict(
                            value=dict(type="int", required=True),
                            unit=dict(
                                type="str",
                                required=True,
                                choices=["MINUTE", "HOUR", "DAY", "WEEK", "MONTH"],
                            ),
                            reset_policy=dict(
                                type="str", required=True, choices=["CALENDAR"]
                            ),
                            operation_on_breach=dict(
                                type="str", required=True, choices=["REJECT", "ALLOW"]
                            ),
                        ),
                    ),
                    targets=dict(
                        type="list",
                        elements="dict",
                        options=dict(deployment_id=dict(type="str", required=True)),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            usage_plan_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
