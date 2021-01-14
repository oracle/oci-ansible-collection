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
module: oci_network_byoip_range_actions
short_description: Perform actions on a ByoipRange resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ByoipRange resource in Oracle Cloud Infrastructure
    - For I(action=advertise), initiate route advertisements for the Byoip Range prefix.
      the prefix must be in PROVISIONED state
    - For I(action=validate), submit the Byoip Range for validation. This presumes the user has
      updated their IP registry record in accordance to validation requirements
    - For I(action=withdraw), stop route advertisements for the Byoip Range prefix.
version_added: "2.9"
author: Oracle (@oracle)
options:
    byoip_range_id:
        description:
            - The OCID of the Byoip Range object.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ByoipRange.
        type: str
        required: true
        choices:
            - "advertise"
            - "validate"
            - "withdraw"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action advertise on byoip_range
  oci_network_byoip_range_actions:
    byoip_range_id: ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx
    action: advertise

- name: Perform action validate on byoip_range
  oci_network_byoip_range_actions:
    byoip_range_id: ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx
    action: validate

- name: Perform action withdraw on byoip_range
  oci_network_byoip_range_actions:
    byoip_range_id: ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx
    action: withdraw

"""

RETURN = """
byoip_range:
    description:
        - Details of the ByoipRange resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        cidr_block:
            description:
                - The address range the user is on-boarding.
            returned: on success
            type: string
            sample: cidr_block_example
        compartment_id:
            description:
                - The OCID of the compartment containing the Byoip Range.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The Oracle ID (OCID) of the Byoip Range.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_details:
            description:
                - The Byoip Range's current substate.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_state:
            description:
                - The Byoip Range's current state.
            returned: on success
            type: string
            sample: INACTIVE
        time_created:
            description:
                - The date and time the Byoip Range was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_validated:
            description:
                - The date and time the Byoip Range was validated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_advertised:
            description:
                - The date and time the Byoip Range was advertised, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_withdrawn:
            description:
                - The date and time the Byoip Range was withdrawn, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        validation_token:
            description:
                - This is an internally generated ASCII string that the user will then use as part of the validation process. Specifically, they will need to
                  add the token string generated by the service to their Internet Registry record.
            returned: on success
            type: string
            sample: validation_token_example
    sample: {
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "CREATING",
        "lifecycle_state": "INACTIVE",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_validated": "2016-08-25T21:10:29.600Z",
        "time_advertised": "2016-08-25T21:10:29.600Z",
        "time_withdrawn": "2016-08-25T21:10:29.600Z",
        "validation_token": "validation_token_example"
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
    from oci.work_requests import WorkRequestClient
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ByoipRangeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        advertise
        validate
        withdraw
    """

    def __init__(self, *args, **kwargs):
        super(ByoipRangeActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "byoip_range_id"

    def get_module_resource_id(self):
        return self.module.params.get("byoip_range_id")

    def get_get_fn(self):
        return self.client.get_byoip_range

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_byoip_range,
            byoip_range_id=self.module.params.get("byoip_range_id"),
        )

    def advertise(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.advertise_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
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

    def validate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def withdraw(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.withdraw_byoip_range,
            call_fn_args=(),
            call_fn_kwargs=dict(
                byoip_range_id=self.module.params.get("byoip_range_id"),
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


ByoipRangeActionsHelperCustom = get_custom_class("ByoipRangeActionsHelperCustom")


class ResourceHelper(ByoipRangeActionsHelperCustom, ByoipRangeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            byoip_range_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["advertise", "validate", "withdraw"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="byoip_range",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
