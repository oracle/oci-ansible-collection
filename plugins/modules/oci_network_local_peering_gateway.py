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
module: oci_network_local_peering_gateway
short_description: Manage a LocalPeeringGateway resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a LocalPeeringGateway resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new local peering gateway (LPG) for the specified VCN.
    - "This resource has the following action operations in the M(oci_local_peering_gateway_actions) module: connect."
version_added: "2.5"
options:
    compartment_id:
        description:
            - The OCID of the compartment containing the local peering gateway (LPG).
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
              entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    route_table_id:
        description:
            - The OCID of the route table the LPG will use.
            - If you don't specify a route table here, the LPG is created without an associated route
              table. The Networking service does NOT automatically associate the attached VCN's default route table
              with the LPG.
            - "For information about why you would associate a route table with an LPG, see
              L(Advanced Scenario: Transit Routing,https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm)."
        type: str
    vcn_id:
        description:
            - The OCID of the VCN the LPG belongs to.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    local_peering_gateway_id:
        description:
            - The OCID of the local peering gateway.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the LocalPeeringGateway.
            - Use I(state=present) to create or update a LocalPeeringGateway.
            - Use I(state=absent) to delete a LocalPeeringGateway.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create local_peering_gateway
  oci_network_local_peering_gateway:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Update local_peering_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_local_peering_gateway:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    route_table_id: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx

- name: Update local_peering_gateway
  oci_network_local_peering_gateway:
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete local_peering_gateway
  oci_network_local_peering_gateway:
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete local_peering_gateway using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_local_peering_gateway:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    vcn_id: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
local_peering_gateway:
    description:
        - Details of the LocalPeeringGateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the LPG.
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
                - The LPG's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        is_cross_tenancy_peering:
            description:
                - Whether the VCN at the other end of the peering is in a different tenancy.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
        lifecycle_state:
            description:
                - The LPG's current lifecycle state.
            returned: on success
            type: string
            sample: PROVISIONING
        peer_advertised_cidr:
            description:
                - The smallest aggregate CIDR that contains all the CIDR routes advertised by the VCN
                  at the other end of the peering from this LPG. See `peerAdvertisedCidrDetails` for
                  the individual CIDRs. The value is `null` if the LPG is not peered.
                - "Example: `192.168.0.0/16`, or if aggregated with `172.16.0.0/24` then `128.0.0.0/1`"
            returned: on success
            type: string
            sample: 192.168.0.0/16
        peer_advertised_cidr_details:
            description:
                - The specific ranges of IP addresses available on or via the VCN at the other
                  end of the peering from this LPG. The value is `null` if the LPG is not peered.
                  You can use these as destination CIDRs for route rules to route a subnet's
                  traffic to this LPG.
                - "Example: [`192.168.0.0/16`, `172.16.0.0/24`]"
            returned: on success
            type: list
            sample: []
        peering_status:
            description:
                - Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been
                  peered. `PENDING` means the peering is being established. `REVOKED` means the
                  LPG at the other end of the peering has been deleted.
            returned: on success
            type: string
            sample: INVALID
        peering_status_details:
            description:
                - Additional information regarding the peering status, if applicable.
            returned: on success
            type: string
            sample: peering_status_details_example
        route_table_id:
            description:
                - The OCID of the route table the LPG is using.
                - "For information about why you would associate a route table with an LPG, see
                  L(Advanced Scenario: Transit Routing,https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm)."
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the LPG was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the LPG belongs to.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy_peering": false,
        "lifecycle_state": "PROVISIONING",
        "peer_advertised_cidr": "192.168.0.0/16",
        "peer_advertised_cidr_details": [],
        "peering_status": "INVALID",
        "peering_status_details": "peering_status_details_example",
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
    from oci.core.models import CreateLocalPeeringGatewayDetails
    from oci.core.models import UpdateLocalPeeringGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LocalPeeringGatewayHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "local_peering_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("local_peering_gateway_id")

    def get_get_fn(self):
        return self.client.get_local_peering_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_local_peering_gateway,
            local_peering_gateway_id=self.module.params.get("local_peering_gateway_id"),
        )

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
            "vcn_id",
        ]

        optional_list_method_params = []

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_local_peering_gateways, **kwargs
        )

    def get_create_model_class(self):
        return CreateLocalPeeringGatewayDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_local_peering_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(create_local_peering_gateway_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateLocalPeeringGatewayDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_local_peering_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                local_peering_gateway_id=self.module.params.get(
                    "local_peering_gateway_id"
                ),
                update_local_peering_gateway_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_local_peering_gateway,
            call_fn_args=(),
            call_fn_kwargs=dict(
                local_peering_gateway_id=self.module.params.get(
                    "local_peering_gateway_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


LocalPeeringGatewayHelperCustom = get_custom_class("LocalPeeringGatewayHelperCustom")


class ResourceHelper(LocalPeeringGatewayHelperCustom, LocalPeeringGatewayHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            route_table_id=dict(type="str"),
            vcn_id=dict(type="str"),
            local_peering_gateway_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="local_peering_gateway",
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
