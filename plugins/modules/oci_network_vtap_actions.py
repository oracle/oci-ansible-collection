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
module: oci_network_vtap_actions
short_description: Perform actions on a Vtap resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Vtap resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a VTAP to a new compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vtap_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VTAP.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the destination compartment for the VTAP move.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Vtap.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on vtap
  oci_network_vtap_actions:
    # required
    vtap_id: "ocid1.vtap.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
vtap:
    description:
        - Details of the Vtap resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN containing the `Vtap` resource.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The VTAP's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The VTAP's administrative lifecycle state.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_state_details:
            description:
                - The VTAP's current running state.
            returned: on success
            type: str
            sample: RUNNING
        time_created:
            description:
                - The date and time the VTAP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2020-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source point where packets are captured.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the destination resource where mirrored packets are
                  sent.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        target_ip:
            description:
                - The IP address of the destination resource where mirrored packets are sent.
            returned: on success
            type: str
            sample: target_ip_example
        capture_filter_id:
            description:
                - The capture filter's Oracle ID (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx"
        encapsulation_protocol:
            description:
                - Defines an encapsulation header type for the VTAP's mirrored traffic.
            returned: on success
            type: str
            sample: VXLAN
        vxlan_network_identifier:
            description:
                - The virtual extensible LAN (VXLAN) network identifier (or VXLAN segment ID) that uniquely identifies the VXLAN.
            returned: on success
            type: int
            sample: 56
        is_vtap_enabled:
            description:
                - Used to start or stop a `Vtap` resource.
                - "* `TRUE` directs the VTAP to start mirroring traffic.
                  * `FALSE` (Default) directs the VTAP to stop mirroring traffic."
            returned: on success
            type: bool
            sample: true
        source_type:
            description:
                - The source type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        traffic_mode:
            description:
                - Used to control the priority of traffic. It is an optional field. If it not passed, the value is DEFAULT
            returned: on success
            type: str
            sample: DEFAULT
        max_packet_size:
            description:
                - The maximum size of the packets to be included in the filter.
            returned: on success
            type: int
            sample: 56
        target_type:
            description:
                - The target type for the VTAP.
            returned: on success
            type: str
            sample: VNIC
        source_private_endpoint_ip:
            description:
                - The IP Address of the source private endpoint.
            returned: on success
            type: str
            sample: source_private_endpoint_ip_example
        source_private_endpoint_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet that source private endpoint belongs to.
            returned: on success
            type: str
            sample: "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_state_details": "RUNNING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "target_ip": "target_ip_example",
        "capture_filter_id": "ocid1.capturefilter.oc1..xxxxxxEXAMPLExxxxxx",
        "encapsulation_protocol": "VXLAN",
        "vxlan_network_identifier": 56,
        "is_vtap_enabled": true,
        "source_type": "VNIC",
        "traffic_mode": "DEFAULT",
        "max_packet_size": 56,
        "target_type": "VNIC",
        "source_private_endpoint_ip": "source_private_endpoint_ip_example",
        "source_private_endpoint_subnet_id": "ocid1.sourceprivateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import ChangeVtapCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VtapActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(VtapActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "vtap_id"

    def get_module_resource_id(self):
        return self.module.params.get("vtap_id")

    def get_get_fn(self):
        return self.client.get_vtap

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vtap, vtap_id=self.module.params.get("vtap_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVtapCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_vtap_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vtap_id=self.module.params.get("vtap_id"),
                change_vtap_compartment_details=action_details,
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


VtapActionsHelperCustom = get_custom_class("VtapActionsHelperCustom")


class ResourceHelper(VtapActionsHelperCustom, VtapActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vtap_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vtap",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
