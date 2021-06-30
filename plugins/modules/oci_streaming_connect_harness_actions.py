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
module: oci_streaming_connect_harness_actions
short_description: Perform actions on a ConnectHarness resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ConnectHarness resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9"
author: Oracle (@oracle)
options:
    connect_harness_id:
        description:
            - The OCID of the connect harness.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ConnectHarness.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on connect_harness
  oci_streaming_connect_harness_actions:
    connect_harness_id: "ocid1.connectharness.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
connect_harness:
    description:
        - Details of the ConnectHarness resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the connect harness. Avoid entering confidential information.
                - "Example: `JDBCConnector`"
            returned: on success
            type: string
            sample: TelemetryEvents
        id:
            description:
                - The OCID of the connect harness.
            returned: on success
            type: string
            sample: ocid1.connectharness.realm.region.mnopqr789
        compartment_id:
            description:
                - The OCID of the compartment that contains the connect harness.
            returned: on success
            type: string
            sample: ocid1.compartment.realm.region.zxcvbn432765
        lifecycle_state:
            description:
                - The current state of the connect harness.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_state_details:
            description:
                - Any additional details about the current state of the connect harness.
            returned: on success
            type: string
            sample: lifecycle_state_details_example
        time_created:
            description:
                - The date and time the connect harness was created, expressed in in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2018-04-20T00:00:07.405Z`"
            returned: on success
            type: string
            sample: 2018-04-20T00:00:07.405Z
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. Exists for cross-
                  compatibility only.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}'"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "name": "TelemetryEvents",
        "id": "ocid1.connectharness.realm.region.mnopqr789",
        "compartment_id": "ocid1.compartment.realm.region.zxcvbn432765",
        "lifecycle_state": "CREATING",
        "lifecycle_state_details": "lifecycle_state_details_example",
        "time_created": "2018-04-20T00:00:07.405Z",
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
    from oci.streaming import StreamAdminClient
    from oci.streaming.models import ChangeConnectHarnessCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectHarnessActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "connect_harness_id"

    def get_module_resource_id(self):
        return self.module.params.get("connect_harness_id")

    def get_get_fn(self):
        return self.client.get_connect_harness

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connect_harness,
            connect_harness_id=self.module.params.get("connect_harness_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeConnectHarnessCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_connect_harness_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connect_harness_id=self.module.params.get("connect_harness_id"),
                change_connect_harness_compartment_details=action_details,
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


ConnectHarnessActionsHelperCustom = get_custom_class(
    "ConnectHarnessActionsHelperCustom"
)


class ResourceHelper(ConnectHarnessActionsHelperCustom, ConnectHarnessActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            connect_harness_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connect_harness",
        service_client_class=StreamAdminClient,
        namespace="streaming",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
