#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_network_vlan
short_description: Manage a Vlan resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Vlan resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a VLAN in the specified VCN and the specified compartment.
version_added: "2.9"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain of the VLAN.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
        type: str
    cidr_block:
        description:
            - The range of IPv4 addresses that will be used for layer 3 communication with
              hosts outside the VLAN. The CIDR must maintain the following rules -
            - a. The CIDR block is valid and correctly formatted.
              b. The new range is within one of the parent VCN ranges.
            - "Example: `192.0.2.0/24`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment to contain the VLAN.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A descriptive name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    nsg_ids:
        description:
            - A list of the OCIDs of the network security groups (NSGs) to add all VNICs in the VLAN to. For more
              information about NSGs, see
              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            - This parameter is updatable.
        type: list
    route_table_id:
        description:
            - The OCID of the route table the VLAN will use. If you don't provide a value,
              the VLAN uses the VCN's default route table.
            - This parameter is updatable.
        type: str
    vcn_id:
        description:
            - The OCID of the VCN to contain the VLAN.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vlan_tag:
        description:
            - The IEEE 802.1Q VLAN tag for this VLAN. The value must be unique across all
              VLANs in the VCN. If you don't provide a value, Oracle assigns one.
              You cannot change the value later. VLAN tag 0 is reserved for use by Oracle.
        type: int
    vlan_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Vlan.
            - Use I(state=present) to create or update a Vlan.
            - Use I(state=absent) to delete a Vlan.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vlan
  oci_network_vlan:
    availability_domain: Uocm:PHX-AD-1
    cidr_block: 192.0.2.0/24
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Update vlan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vlan:
    cidr_block: 192.0.2.0/24
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    route_table_id: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Update vlan
  oci_network_vlan:
    cidr_block: 192.0.2.0/24
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    vlan_id: ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete vlan
  oci_network_vlan:
    vlan_id: ocid1.vlan.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete vlan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vlan:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
                - The availability domain of the VLAN.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The range of IPv4 addresses that will be used for layer 3 communication with
                  hosts outside the VLAN.
                - "Example: `192.168.1.0/24`"
            returned: on success
            type: string
            sample: 192.168.1.0/24
        compartment_id:
            description:
                - The OCID of the compartment containing the VLAN.
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
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
                - The VLAN's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The VLAN's current state.
            returned: on success
            type: string
            sample: PROVISIONING
        nsg_ids:
            description:
                - A list of the OCIDs of the network security groups (NSGs) to use with this VLAN.
                  All VNICs in the VLAN belong to these NSGs. For more
                  information about NSGs, see
                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
            returned: on success
            type: list
            sample: []
        vlan_tag:
            description:
                - The IEEE 802.1Q VLAN tag of this VLAN.
                - "Example: `100`"
            returned: on success
            type: int
            sample: 100
        route_table_id:
            description:
                - The OCID of the route table that the VLAN uses.
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the VLAN was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the VLAN is in.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "192.168.1.0/24",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "nsg_ids": [],
        "vlan_tag": 100,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateVlanDetails
    from oci.core.models import UpdateVlanDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VlanHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "vlan_id"

    def get_module_resource_id(self):
        return self.module.params.get("vlan_id")

    def get_get_fn(self):
        return self.client.get_vlan

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vlan, vlan_id=self.module.params.get("vlan_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "vcn_id",
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
        return oci_common_utils.list_all_resources(self.client.list_vlans, **kwargs)

    def get_create_model_class(self):
        return CreateVlanDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vlan,
            call_fn_args=(),
            call_fn_kwargs=dict(create_vlan_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVlanDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vlan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vlan_id=self.module.params.get("vlan_id"),
                update_vlan_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_vlan,
            call_fn_args=(),
            call_fn_kwargs=dict(vlan_id=self.module.params.get("vlan_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VlanHelperCustom = get_custom_class("VlanHelperCustom")


class ResourceHelper(VlanHelperCustom, VlanHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            cidr_block=dict(type="str"),
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            nsg_ids=dict(type="list"),
            route_table_id=dict(type="str"),
            vcn_id=dict(type="str"),
            vlan_tag=dict(type="int"),
            vlan_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
