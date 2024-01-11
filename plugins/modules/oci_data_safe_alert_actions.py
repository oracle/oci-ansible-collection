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
module: oci_data_safe_alert_actions
short_description: Perform actions on an Alert resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Alert resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the specified alert into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alert_id:
        description:
            - The OCID of alert.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the new compartment to move the alert to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Alert.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on alert
  oci_data_safe_alert_actions:
    # required
    alert_id: "ocid1.alert.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
alert:
    description:
        - Details of the Alert resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the alert.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the alert.
            returned: on success
            type: str
            sample: OPEN
        severity:
            description:
                - Severity level of the alert.
            returned: on success
            type: str
            sample: CRITICAL
        display_name:
            description:
                - The display name of the alert.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the alert.
            returned: on success
            type: str
            sample: description_example
        operation_time:
            description:
                - Creation date and time of the operation that triggered alert, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        operation:
            description:
                - The operation (event) that triggered alert.
            returned: on success
            type: str
            sample: operation_example
        operation_status:
            description:
                - The result of the operation (event) that triggered alert.
            returned: on success
            type: str
            sample: SUCCEEDED
        target_ids:
            description:
                - Array of OCIDs of the target database which are associated with the alert.
            returned: on success
            type: list
            sample: []
        target_names:
            description:
                - Array of names of the target database.
            returned: on success
            type: list
            sample: []
        policy_id:
            description:
                - The OCID of the policy that triggered alert.
            returned: on success
            type: str
            sample: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
        alert_type:
            description:
                - Type of the alert. Indicates the Data Safe feature triggering the alert.
            returned: on success
            type: str
            sample: AUDITING
        resource_name:
            description:
                - The resource endpoint that triggered the alert.
            returned: on success
            type: str
            sample: resource_name_example
        feature_details:
            description:
                - "Map that contains maps of values.
                   Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {}
        comment:
            description:
                - A comment for the alert. Entered by the user.
            returned: on success
            type: str
            sample: comment_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the alert.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the alert.
            returned: on success
            type: str
            sample: UPDATING
        time_created:
            description:
                - Creation date and time of the alert, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Last date and time the alert was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "OPEN",
        "severity": "CRITICAL",
        "display_name": "display_name_example",
        "description": "description_example",
        "operation_time": "2013-10-20T19:20:30+01:00",
        "operation": "operation_example",
        "operation_status": "SUCCEEDED",
        "target_ids": [],
        "target_names": [],
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "alert_type": "AUDITING",
        "resource_name": "resource_name_example",
        "feature_details": {},
        "comment": "comment_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "UPDATING",
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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ChangeAlertCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeAlertActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "alert_id"

    def get_module_resource_id(self):
        return self.module.params.get("alert_id")

    def get_get_fn(self):
        return self.client.get_alert

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert, alert_id=self.module.params.get("alert_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAlertCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_alert_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alert_id=self.module.params.get("alert_id"),
                change_alert_compartment_details=action_details,
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


DataSafeAlertActionsHelperCustom = get_custom_class("DataSafeAlertActionsHelperCustom")


class ResourceHelper(DataSafeAlertActionsHelperCustom, DataSafeAlertActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            alert_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="alert",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
