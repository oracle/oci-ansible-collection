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
module: oci_network_virtual_circuit_actions
short_description: Perform actions on a VirtualCircuit resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VirtualCircuit resource in Oracle Cloud Infrastructure
    - For I(action=bulk_add_virtual_circuit_public_prefixes), adds one or more customer public IP prefixes to the specified public virtual circuit.
      Use this operation (and not L(UpdateVirtualCircuit,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/VirtualCircuit/UpdateVirtualCircuit))
      to add prefixes to the virtual circuit. Oracle must verify the customer's ownership
      of each prefix before traffic for that prefix will flow across the virtual circuit.
    - For I(action=bulk_delete_virtual_circuit_public_prefixes), removes one or more customer public IP prefixes from the specified public virtual circuit.
      Use this operation (and not L(UpdateVirtualCircuit,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/VirtualCircuit/UpdateVirtualCircuit))
      to remove prefixes from the virtual circuit. When the virtual circuit's state switches
      back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.
    - For I(action=change_compartment), moves a virtual circuit into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    virtual_circuit_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual circuit.
        type: str
        aliases: ["id"]
        required: true
    public_prefixes:
        description:
            - The public IP prefixes (CIDRs) to add to the public virtual circuit.
            - Required for I(action=bulk_add_virtual_circuit_public_prefixes), I(action=bulk_delete_virtual_circuit_public_prefixes).
        type: list
        elements: dict
        suboptions:
            cidr_block:
                description:
                    - An individual public IP prefix (CIDR) to add to the public virtual circuit.
                      All prefix sizes are allowed.
                type: str
                required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              virtual circuit to.
            - Required for I(action=change_compartment).
        type: str
    action:
        description:
            - The action to perform on the VirtualCircuit.
        type: str
        required: true
        choices:
            - "bulk_add_virtual_circuit_public_prefixes"
            - "bulk_delete_virtual_circuit_public_prefixes"
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action bulk_add_virtual_circuit_public_prefixes on virtual_circuit
  oci_network_virtual_circuit_actions:
    # required
    virtual_circuit_id: "ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx"
    public_prefixes:
    - # required
      cidr_block: cidr_block_example
    action: bulk_add_virtual_circuit_public_prefixes

- name: Perform action bulk_delete_virtual_circuit_public_prefixes on virtual_circuit
  oci_network_virtual_circuit_actions:
    # required
    virtual_circuit_id: "ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx"
    public_prefixes:
    - # required
      cidr_block: cidr_block_example
    action: bulk_delete_virtual_circuit_public_prefixes

- name: Perform action change_compartment on virtual_circuit
  oci_network_virtual_circuit_actions:
    # required
    virtual_circuit_id: "ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
virtual_circuit:
    description:
        - Details of the VirtualCircuit resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        public_prefixes:
            description:
                - The public IP prefixes (CIDRs) to add to the public virtual circuit.
            returned: on success
            type: complex
            contains:
                cidr_block:
                    description:
                        - An individual public IP prefix (CIDR) to add to the public virtual circuit.
                          All prefix sizes are allowed.
                    returned: on success
                    type: str
                    sample: cidr_block_example
    sample: {
        "public_prefixes": [{
            "cidr_block": "cidr_block_example"
        }]
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import BulkAddVirtualCircuitPublicPrefixesDetails
    from oci.core.models import BulkDeleteVirtualCircuitPublicPrefixesDetails
    from oci.core.models import ChangeVirtualCircuitCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualCircuitActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_add_virtual_circuit_public_prefixes
        bulk_delete_virtual_circuit_public_prefixes
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "virtual_circuit_id"

    def get_module_resource_id(self):
        return self.module.params.get("virtual_circuit_id")

    def get_get_fn(self):
        return self.client.get_virtual_circuit

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_circuit,
            virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
        )

    def bulk_add_virtual_circuit_public_prefixes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkAddVirtualCircuitPublicPrefixesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_add_virtual_circuit_public_prefixes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                bulk_add_virtual_circuit_public_prefixes_details=action_details,
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

    def bulk_delete_virtual_circuit_public_prefixes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkDeleteVirtualCircuitPublicPrefixesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_delete_virtual_circuit_public_prefixes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                bulk_delete_virtual_circuit_public_prefixes_details=action_details,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeVirtualCircuitCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_virtual_circuit_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                change_virtual_circuit_compartment_details=action_details,
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


VirtualCircuitActionsHelperCustom = get_custom_class(
    "VirtualCircuitActionsHelperCustom"
)


class ResourceHelper(VirtualCircuitActionsHelperCustom, VirtualCircuitActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            virtual_circuit_id=dict(aliases=["id"], type="str", required=True),
            public_prefixes=dict(
                type="list",
                elements="dict",
                options=dict(cidr_block=dict(type="str", required=True)),
            ),
            compartment_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "bulk_add_virtual_circuit_public_prefixes",
                    "bulk_delete_virtual_circuit_public_prefixes",
                    "change_compartment",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="virtual_circuit",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
