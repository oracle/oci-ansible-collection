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
module: oci_log_analytics_log_group_actions
short_description: Perform actions on a LogAnalyticsLogGroup resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LogAnalyticsLogGroup resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified log group to a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    log_analytics_log_group_id:
        description:
            - unique logAnalytics log group identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment where the log analytics entity should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the LogAnalyticsLogGroup.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on log_analytics_log_group
  oci_log_analytics_log_group_actions:
    # required
    namespace_name: namespace_name_example
    log_analytics_log_group_id: "ocid1.loganalyticsloggroup.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
log_analytics_log_group:
    description:
        - Details of the LogAnalyticsLogGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
                  a resource that is provisioned and managed by the customer on their premises or on the cloud.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name that is changeable and that does not have to be unique.
                  Format: a leading alphanumeric, followed by zero or more
                  alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
                  No trailing spaces allowed."
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the resource was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.log_analytics import LogAnalyticsClient
    from oci.log_analytics.models import ChangeLogAnalyticsLogGroupCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsLogGroupActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "log_analytics_log_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("log_analytics_log_group_id")

    def get_get_fn(self):
        return self.client.get_log_analytics_log_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_log_group,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_log_group_id=self.module.params.get(
                "log_analytics_log_group_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLogAnalyticsLogGroupCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_log_analytics_log_group_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                namespace_name=self.module.params.get("namespace_name"),
                log_analytics_log_group_id=self.module.params.get(
                    "log_analytics_log_group_id"
                ),
                change_log_analytics_log_group_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


LogAnalyticsLogGroupActionsHelperCustom = get_custom_class(
    "LogAnalyticsLogGroupActionsHelperCustom"
)


class ResourceHelper(
    LogAnalyticsLogGroupActionsHelperCustom, LogAnalyticsLogGroupActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            log_analytics_log_group_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="log_analytics_log_group",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
