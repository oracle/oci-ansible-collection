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
module: oci_network_public_ip_pool_actions
short_description: Perform actions on a PublicIpPool resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PublicIpPool resource in Oracle Cloud Infrastructure
    - For I(action=add_public_ip_pool_capacity), adds some or all of a CIDR block to a public IP pool.
      The CIDR block (or subrange) must not overlap with any other CIDR block already added to this or any other public IP pool.
    - For I(action=change_compartment), moves a public IP pool to a different compartment. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=remove_public_ip_pool_capacity), removes a CIDR block from the referenced public IP pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    byoip_range_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR block
              belongs.
            - Required for I(action=add_public_ip_pool_capacity).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the public IP pool
              move.
            - Required for I(action=change_compartment).
        type: str
    public_ip_pool_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.
        type: str
        aliases: ["id"]
        required: true
    cidr_block:
        description:
            - "The CIDR block to add to the public IP pool. It could be all of the CIDR block identified in `byoipRangeId`, or a subrange.
              Example: `10.0.1.0/24`"
            - Required for I(action=add_public_ip_pool_capacity), I(action=remove_public_ip_pool_capacity).
        type: str
    action:
        description:
            - The action to perform on the PublicIpPool.
        type: str
        required: true
        choices:
            - "add_public_ip_pool_capacity"
            - "change_compartment"
            - "remove_public_ip_pool_capacity"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_public_ip_pool_capacity on public_ip_pool
  oci_network_public_ip_pool_actions:
    # required
    byoip_range_id: "ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx"
    public_ip_pool_id: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    cidr_block: cidr_block_example
    action: add_public_ip_pool_capacity

- name: Perform action change_compartment on public_ip_pool
  oci_network_public_ip_pool_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    public_ip_pool_id: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_public_ip_pool_capacity on public_ip_pool
  oci_network_public_ip_pool_actions:
    # required
    public_ip_pool_id: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    cidr_block: cidr_block_example
    action: remove_public_ip_pool_capacity

"""

RETURN = """
public_ip_pool:
    description:
        - Details of the PublicIpPool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        cidr_blocks:
            description:
                - The CIDR blocks added to this pool. This could be all or a portion of a BYOIP CIDR block.
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing this pool.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the public IP pool.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The public IP pool's current state.
            returned: on success
            type: str
            sample: INACTIVE
        time_created:
            description:
                - The date and time the public IP pool was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "cidr_blocks": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "INACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import AddPublicIpPoolCapacityDetails
    from oci.core.models import ChangePublicIpPoolCompartmentDetails
    from oci.core.models import RemovePublicIpPoolCapacityDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicIpPoolActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_public_ip_pool_capacity
        change_compartment
        remove_public_ip_pool_capacity
    """

    @staticmethod
    def get_module_resource_id_param():
        return "public_ip_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("public_ip_pool_id")

    def get_get_fn(self):
        return self.client.get_public_ip_pool

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_public_ip_pool,
            public_ip_pool_id=self.module.params.get("public_ip_pool_id"),
        )

    def add_public_ip_pool_capacity(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddPublicIpPoolCapacityDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_public_ip_pool_capacity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                public_ip_pool_id=self.module.params.get("public_ip_pool_id"),
                add_public_ip_pool_capacity_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePublicIpPoolCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_public_ip_pool_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                public_ip_pool_id=self.module.params.get("public_ip_pool_id"),
                change_public_ip_pool_compartment_details=action_details,
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

    def remove_public_ip_pool_capacity(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemovePublicIpPoolCapacityDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_public_ip_pool_capacity,
            call_fn_args=(),
            call_fn_kwargs=dict(
                public_ip_pool_id=self.module.params.get("public_ip_pool_id"),
                remove_public_ip_pool_capacity_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


PublicIpPoolActionsHelperCustom = get_custom_class("PublicIpPoolActionsHelperCustom")


class ResourceHelper(PublicIpPoolActionsHelperCustom, PublicIpPoolActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            byoip_range_id=dict(type="str"),
            compartment_id=dict(type="str"),
            public_ip_pool_id=dict(aliases=["id"], type="str", required=True),
            cidr_block=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_public_ip_pool_capacity",
                    "change_compartment",
                    "remove_public_ip_pool_capacity",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="public_ip_pool",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
