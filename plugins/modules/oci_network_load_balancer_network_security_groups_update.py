#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_network_load_balancer_network_security_groups_update
short_description: Manage a NetworkSecurityGroupsUpdate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a NetworkSecurityGroupsUpdate resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        aliases: ["id"]
        required: true
    network_security_group_ids:
        description:
            - An array of network security group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with the network
              load
              balancer.
            - During the creation of the network load balancer, the service adds the new network load balancer to the specified network security groups.
            - "The benefits of associating the network load balancer with network security groups include:"
            - "*  Network security groups define network security rules to govern ingress and egress traffic for the network load balancer."
            - "*  The network security rules of other resources can reference the network security groups associated with the network load balancer
                 to ensure access."
            - This parameter is updatable.
        type: list
        elements: str
    state:
        description:
            - The state of the NetworkSecurityGroupsUpdate.
            - Use I(state=present) to update an existing a NetworkSecurityGroupsUpdate.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update network_security_groups_update
  oci_network_load_balancer_network_security_groups_update:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    network_security_group_ids: [ "network_security_group_ids_example" ]

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
    from oci.network_load_balancer import NetworkLoadBalancerClient
    from oci.network_load_balancer.models import UpdateNetworkSecurityGroupsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperGen(OCIResourceHelperBase):
    """Supported operations: update"""

    def get_possible_entity_types(self):
        return super(
            NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperGen, self
        ).get_possible_entity_types() + [
            "networksecuritygroupsupdate",
            "networksecuritygroupsupdates",
            "networkLoadBalancernetworksecuritygroupsupdate",
            "networkLoadBalancernetworksecuritygroupsupdates",
            "networksecuritygroupsupdateresource",
            "networksecuritygroupsupdatesresource",
            "networksecuritygroup",
            "networksecuritygroups",
            "networkLoadBalancernetworksecuritygroup",
            "networkLoadBalancernetworksecuritygroups",
            "networksecuritygroupresource",
            "networksecuritygroupsresource",
            "networkloadbalancer",
        ]

    def get_module_resource_id_param(self):
        return "network_load_balancer_id"

    def get_module_resource_id(self):
        return self.module.params.get("network_load_balancer_id")

    def get_update_model_class(self):
        return UpdateNetworkSecurityGroupsDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_security_groups,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_network_security_groups_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperCustom = get_custom_class(
    "NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperCustom,
    NetworkLoadBalancerNetworkSecurityGroupsUpdateHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            network_security_group_ids=dict(type="list", elements="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_security_groups_update",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
