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
module: oci_network_load_balancer_listener
short_description: Manage a Listener resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Listener resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a listener to a network load balancer.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        required: true
    name:
        description:
            - A friendly name for the listener. It must be unique and it cannot be changed.
            - "Example: `example_listener`"
        type: str
        required: true
    default_backend_set_name:
        description:
            - The name of the associated backend set.
            - "Example: `example_backend_set`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    port:
        description:
            - The communication port for the listener.
            - "Example: `80`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    protocol:
        description:
            - The protocol on which the listener accepts connection requests.
              For public network load balancers, ANY protocol refers to TCP/UDP.
              For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true).
              To get a list of valid protocols, use the L(ListNetworkLoadBalancersProtocols,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/NetworkLoadBalancer/20200501/networkLoadBalancerProtocol/ListNetworkLoadBalancersProtocols)
              operation.
            - "Example: `TCP`"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "ANY"
            - "TCP"
            - "UDP"
    state:
        description:
            - The state of the Listener.
            - Use I(state=present) to create or update a Listener.
            - Use I(state=absent) to delete a Listener.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create listener
  oci_network_load_balancer_listener:
    default_backend_set_name: "example_backend_set"
    port: 80
    protocol: "HTTP"
    name: "example_listener"
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update listener
  oci_network_load_balancer_listener:
    default_backend_set_name: "example_backend_set"
    port: 80
    protocol: "HTTP"
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete listener
  oci_network_load_balancer_listener:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: example_listener
    state: absent

"""

RETURN = """
listener:
    description:
        - Details of the Listener resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A friendly name for the listener. It must be unique and it cannot be changed.
                - "Example: `example_listener`"
            returned: on success
            type: str
            sample: example_listener
        default_backend_set_name:
            description:
                - The name of the associated backend set.
                - "Example: `example_backend_set`"
            returned: on success
            type: str
            sample: example_backend_set
        port:
            description:
                - The communication port for the listener.
                - "Example: `80`"
            returned: on success
            type: int
            sample: 0
        protocol:
            description:
                - The protocol on which the listener accepts connection requests.
                  For public network load balancers, ANY protocol refers to TCP/UDP.
                  For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to
                  true).
                  To get a list of valid protocols, use the L(ListNetworkLoadBalancersProtocols,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/NetworkLoadBalancer/20200501/networkLoadBalancerProtocol/ListNetworkLoadBalancersProtocols)
                  operation.
                - "Example: `TCP`"
            returned: on success
            type: str
            sample: TCP
    sample: {
        "name": "example_listener",
        "default_backend_set_name": "example_backend_set",
        "port": 0,
        "protocol": "TCP"
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
    from oci.network_load_balancer import NetworkLoadBalancerClient
    from oci.network_load_balancer.models import CreateListenerDetails
    from oci.network_load_balancer.models import UpdateListenerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerListenerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_listener

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_listener,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            listener_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "network_load_balancer_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_listeners, **kwargs)

    def get_create_model_class(self):
        return CreateListenerDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_listener,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                create_listener_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateListenerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_listener,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_listener_details=update_details,
                listener_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_listener,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                listener_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerListenerHelperCustom = get_custom_class(
    "NetworkLoadBalancerListenerHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerListenerHelperCustom, NetworkLoadBalancerListenerHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            default_backend_set_name=dict(type="str"),
            port=dict(type="int"),
            protocol=dict(type="str", choices=["ANY", "TCP", "UDP"]),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="listener",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
