#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_public_ip_actions
short_description: Perform actions on a PublicIp resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PublicIp resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a public IP into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      This operation applies only to reserved public IPs. Ephemeral public IPs always belong to the
      same compartment as their VNIC and move accordingly.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    public_ip_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the public IP.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              public IP to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the PublicIp.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on public_ip
  oci_network_public_ip_actions:
    public_ip_id: "ocid1.publicip.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
public_ip:
    description:
        - Details of the PublicIp resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        assigned_entity_id:
            description:
                - The OCID of the entity the public IP is assigned to, or in the process of
                  being assigned to.
            returned: on success
            type: str
            sample: "ocid1.assignedentity.oc1..xxxxxxEXAMPLExxxxxx"
        assigned_entity_type:
            description:
                - The type of entity the public IP is assigned to, or in the process of being
                  assigned to.
            returned: on success
            type: str
            sample: PRIVATE_IP
        availability_domain:
            description:
                - The public IP's availability domain. This property is set only for ephemeral public IPs
                  that are assigned to a private IP (that is, when the `scope` of the public IP is set to
                  AVAILABILITY_DOMAIN). The value is the availability domain of the assigned private IP.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The OCID of the compartment containing the public IP. For an ephemeral public IP, this is
                  the compartment of its assigned entity (which can be a private IP or a regional entity such
                  as a NAT gateway). For a reserved public IP that is currently assigned,
                  its compartment can be different from the assigned private IP's.
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
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
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
                - The public IP's Oracle ID (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ip_address:
            description:
                - The public IP address of the `publicIp` object.
                - "Example: `203.0.113.2`"
            returned: on success
            type: str
            sample: 203.0.113.2
        lifecycle_state:
            description:
                - The public IP's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        lifetime:
            description:
                - Defines when the public IP is deleted and released back to Oracle's public IP pool.
                - "* `EPHEMERAL`: The lifetime is tied to the lifetime of its assigned entity. An ephemeral
                  public IP must always be assigned to an entity. If the assigned entity is a private IP,
                  the ephemeral public IP is automatically deleted when the private IP is deleted, when
                  the VNIC is terminated, or when the instance is terminated. If the assigned entity is a
                  L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/), the ephemeral public IP is automatically
                  deleted when the NAT gateway is terminated."
                - "* `RESERVED`: You control the public IP's lifetime. You can delete a reserved public IP
                  whenever you like. It does not need to be assigned to a private IP at all times."
                - For more information and comparison of the two types,
                  see L(Public IP Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingpublicIPs.htm).
            returned: on success
            type: str
            sample: EPHEMERAL
        private_ip_id:
            description:
                - Deprecated. Use `assignedEntityId` instead.
                - The OCID of the private IP that the public IP is currently assigned to, or in the
                  process of being assigned to.
                - "**Note:** This is `null` if the public IP is not assigned to a private IP, or is
                  in the process of being assigned to one."
            returned: on success
            type: str
            sample: "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx"
        scope:
            description:
                - Whether the public IP is regional or specific to a particular availability domain.
                - "* `REGION`: The public IP exists within a region and is assigned to a regional entity
                  (such as a L(NatGateway,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/NatGateway/)), or can be assigned to a private
                  IP in any availability domain in the region. Reserved public IPs and ephemeral public IPs
                  assigned to a regional entity have `scope` = `REGION`."
                - "* `AVAILABILITY_DOMAIN`: The public IP exists within the availability domain of the entity
                  it's assigned to, which is specified by the `availabilityDomain` property of the public IP object.
                  Ephemeral public IPs that are assigned to private IPs have `scope` = `AVAILABILITY_DOMAIN`."
            returned: on success
            type: str
            sample: REGION
        time_created:
            description:
                - The date and time the public IP was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        public_ip_pool_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pool object created in the current tenancy.
            returned: on success
            type: str
            sample: "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "assigned_entity_id": "ocid1.assignedentity.oc1..xxxxxxEXAMPLExxxxxx",
        "assigned_entity_type": "PRIVATE_IP",
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ip_address": "203.0.113.2",
        "lifecycle_state": "PROVISIONING",
        "lifetime": "EPHEMERAL",
        "private_ip_id": "ocid1.privateip.oc1..xxxxxxEXAMPLExxxxxx",
        "scope": "REGION",
        "time_created": "2016-08-25T21:10:29.600Z",
        "public_ip_pool_id": "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import ChangePublicIpCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicIpActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "public_ip_id"

    def get_module_resource_id(self):
        return self.module.params.get("public_ip_id")

    def get_get_fn(self):
        return self.client.get_public_ip

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_public_ip,
            public_ip_id=self.module.params.get("public_ip_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePublicIpCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_public_ip_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                public_ip_id=self.module.params.get("public_ip_id"),
                change_public_ip_compartment_details=action_details,
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


PublicIpActionsHelperCustom = get_custom_class("PublicIpActionsHelperCustom")


class ResourceHelper(PublicIpActionsHelperCustom, PublicIpActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            public_ip_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="public_ip",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
