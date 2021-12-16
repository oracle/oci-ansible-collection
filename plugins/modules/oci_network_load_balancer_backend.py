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
module: oci_network_load_balancer_backend
short_description: Manage a Backend resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Backend resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a backend server to a backend set.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        aliases: ["id"]
        required: true
    name:
        description:
            - "Optional unique name identifying the backend within the backend set. If not specified, then one will be generated.
              Example: `webServer1`"
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
    ip_address:
        description:
            - "The IP address of the backend server.
              Example: `10.0.0.3`"
        type: str
    target_id:
        description:
            - "The IP OCID/Instance OCID associated with the backend server.
              Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`"
        type: str
    port:
        description:
            - The communication port for the backend server.
            - "Example: `8080`"
            - Required for create using I(state=present).
        type: int
    weight:
        description:
            - The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
              proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
              as a server weighted '1'.
              For more information about load balancing policies, see
              L(How Network Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
            - "Example: `3`"
            - This parameter is updatable.
        type: int
    is_drain:
        description:
            - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
              incoming traffic."
            - "Example: `false`"
            - This parameter is updatable.
        type: bool
    is_backup:
        description:
            - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
              traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
            - "Example: `false`"
            - This parameter is updatable.
        type: bool
    is_offline:
        description:
            - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
              traffic.
            - "Example: `false`"
            - This parameter is updatable.
        type: bool
    backend_set_name:
        description:
            - The name of the backend set to which to add the backend server.
            - "Example: `example_backend_set`"
        type: str
        required: true
    state:
        description:
            - The state of the Backend.
            - Use I(state=present) to create or update a Backend.
            - Use I(state=absent) to delete a Backend.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backend
  oci_network_load_balancer_backend:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    port: 56
    backend_set_name: backend_set_name_example

    # optional
    name: name_example
    ip_address: ip_address_example
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    weight: 56
    is_drain: true
    is_backup: true
    is_offline: true

- name: Update backend
  oci_network_load_balancer_backend:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    backend_set_name: backend_set_name_example

    # optional
    weight: 56
    is_drain: true
    is_backup: true
    is_offline: true

- name: Delete backend
  oci_network_load_balancer_backend:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    backend_set_name: backend_set_name_example
    state: absent

"""

RETURN = """
backend:
    description:
        - Details of the Backend resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set.
                - "Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`"
            returned: on success
            type: str
            sample: name_example
        ip_address:
            description:
                - "The IP address of the backend server.
                  Example: `10.0.0.3`"
            returned: on success
            type: str
            sample: ip_address_example
        target_id:
            description:
                - "The IP OCID/Instance OCID associated with the backend server.
                  Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`"
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        port:
            description:
                - The communication port for the backend server.
                - "Example: `8080`"
            returned: on success
            type: int
            sample: 56
        weight:
            description:
                - The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                  proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
                  as a server weighted '1'.
                  For more information about load balancing policies, see
                  L(How Network Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                - "Example: `3`"
            returned: on success
            type: int
            sample: 56
        is_drain:
            description:
                - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
                  incoming traffic."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        is_backup:
            description:
                - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
                  traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        is_offline:
            description:
                - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
                  traffic.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
    sample: {
        "name": "name_example",
        "ip_address": "ip_address_example",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "port": 56,
        "weight": 56,
        "is_drain": true,
        "is_backup": true,
        "is_offline": true
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
    from oci.network_load_balancer.models import CreateBackendDetails
    from oci.network_load_balancer.models import UpdateBackendDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerBackendHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_backend

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "network_load_balancer_id",
            "backend_set_name",
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
        return oci_common_utils.list_all_resources(self.client.list_backends, **kwargs)

    def get_create_model_class(self):
        return CreateBackendDetails

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
            call_fn=self.client.create_backend,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                create_backend_details=create_details,
                backend_set_name=self.module.params.get("backend_set_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBackendDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backend,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_backend_details=update_details,
                backend_set_name=self.module.params.get("backend_set_name"),
                backend_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backend,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                backend_set_name=self.module.params.get("backend_set_name"),
                backend_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerBackendHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerBackendHelperCustom, NetworkLoadBalancerBackendHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
            ip_address=dict(type="str"),
            target_id=dict(type="str"),
            port=dict(type="int"),
            weight=dict(type="int"),
            is_drain=dict(type="bool"),
            is_backup=dict(type="bool"),
            is_offline=dict(type="bool"),
            backend_set_name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backend",
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
