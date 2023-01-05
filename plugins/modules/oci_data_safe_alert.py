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
module: oci_data_safe_alert
short_description: Manage an Alert resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an Alert resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_alert_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    alert_id:
        description:
            - The OCID of alert.
        type: str
        aliases: ["id"]
        required: true
    comment:
        description:
            - A comment can be entered to track the alert changes done by the user.
            - This parameter is updatable.
        type: str
    status:
        description:
            - The status of the alert.
            - This parameter is updatable.
        type: str
        choices:
            - "OPEN"
            - "CLOSED"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    state:
        description:
            - The state of the Alert.
            - Use I(state=present) to update an existing an Alert.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update alert
  oci_data_safe_alert:
    # required
    alert_id: "ocid1.alert.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    comment: comment_example
    status: OPEN
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import UpdateAlertDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeAlertHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(DataSafeAlertHelperGen, self).get_possible_entity_types() + [
            "alert",
            "alerts",
            "dataSafealert",
            "dataSafealerts",
            "alertresource",
            "alertsresource",
            "datasafe",
        ]

    def get_module_resource_id_param(self):
        return "alert_id"

    def get_module_resource_id(self):
        return self.module.params.get("alert_id")

    def get_get_fn(self):
        return self.client.get_alert

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert, alert_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_alert, alert_id=self.module.params.get("alert_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_alerts, **kwargs)

    def get_update_model_class(self):
        return UpdateAlertDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_alert,
            call_fn_args=(),
            call_fn_kwargs=dict(
                alert_id=self.module.params.get("alert_id"),
                update_alert_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DataSafeAlertHelperCustom = get_custom_class("DataSafeAlertHelperCustom")


class ResourceHelper(DataSafeAlertHelperCustom, DataSafeAlertHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            alert_id=dict(aliases=["id"], type="str", required=True),
            comment=dict(type="str"),
            status=dict(type="str", choices=["OPEN", "CLOSED"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
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

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
