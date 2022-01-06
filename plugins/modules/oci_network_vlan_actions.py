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
module: oci_network_vlan_actions
short_description: Perform actions on a Vlan resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Vlan resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a VLAN into a different compartment within the same tenancy.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vlan_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VLAN.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the VLAN to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Vlan.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on vlan
  oci_network_vlan_actions:
    # required
    vlan_id: "ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
vlan:
    description:
        - Details of the Vlan resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The VLAN's availability domain. This attribute will be null if this is a regional VLAN
                  rather than an AD-specific VLAN.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The range of IPv4 addresses that will be used for layer 3 communication with
                  hosts outside the VLAN.
                - "Example: `192.168.1.0/24`"
            returned: on success
            type: str
            sample: cidr_block_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VLAN.
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
                - The VLAN's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The VLAN's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        nsg_ids:
            description:
                - A list of the OCIDs of the network security groups (NSGs) to use with this VLAN.
                  All VNICs in the VLAN belong to these NSGs. For more
                  information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        vlan_tag:
            description:
                - The IEEE 802.1Q VLAN tag of this VLAN.
                - "Example: `100`"
            returned: on success
            type: int
            sample: 56
        route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that the VLAN uses.
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the VLAN was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the VLAN is in.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "nsg_ids": [],
        "vlan_tag": 56,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import ChangeVlanCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VlanActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(VlanActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "vlan_id"

    def get_module_resource_id(self):
        return self.module.params.get("vlan_id")

    def get_get_fn(self):
        return self.client.get_vlan

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vlan, vlan_id=self.module.params.get("vlan_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVlanCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vlan_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vlan_id=self.module.params.get("vlan_id"),
                change_vlan_compartment_details=action_details,
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


VlanActionsHelperCustom = get_custom_class("VlanActionsHelperCustom")


class ResourceHelper(VlanActionsHelperCustom, VlanActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vlan_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vlan",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
