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
module: oci_loadbalancer_backend
short_description: Manage a Backend resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Backend resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a backend server to a backend set.
version_added: "2.5"
options:
    ip_address:
        description:
            - The IP address of the backend server.
            - "Example: `10.0.0.3`"
        type: str
        required: true
    port:
        description:
            - The communication port for the backend server.
            - "Example: `8080`"
        type: int
        required: true
    weight:
        description:
            - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
              proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
              as a server weighted '1'.
              For more information on load balancing policies, see
              L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
            - "Example: `3`"
            - Required for update using I(state=present) with  present.
        type: int
    backup:
        description:
            - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
              traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
            - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
            - "Example: `false`"
            - Required for update using I(state=present) with  present.
        type: bool
    drain:
        description:
            - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
              incoming traffic."
            - "Example: `false`"
            - Required for update using I(state=present) with  present.
        type: bool
    offline:
        description:
            - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
              traffic.
            - "Example: `false`"
            - Required for update using I(state=present) with  present.
        type: bool
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the backend set and
              servers.
        type: str
        required: true
    backend_set_name:
        description:
            - The name of the backend set to add the backend server to.
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
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backend
  oci_loadbalancer_backend:
    ip_address: 10.0.0.3
    port: 8080
    weight: 3
    backup: false
    drain: false
    offline: false
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    backend_set_name: example_backend_set

- name: Update backend
  oci_loadbalancer_backend:
    weight: 3
    backup: false
    drain: false
    offline: false
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    backend_set_name: example_backend_set

- name: Delete backend
  oci_loadbalancer_backend:
    ip_address: 10.0.0.3
    port: 8080
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    backend_set_name: example_backend_set
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
                - A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.
                - "Example: `10.0.0.3:8080`"
            returned: on success
            type: string
            sample: 10.0.0.3:8080
        ip_address:
            description:
                - The IP address of the backend server.
                - "Example: `10.0.0.3`"
            returned: on success
            type: string
            sample: 10.0.0.3
        port:
            description:
                - The communication port for the backend server.
                - "Example: `8080`"
            returned: on success
            type: int
            sample: 8080
        weight:
            description:
                - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                  proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
                  as a server weighted '1'.
                  For more information on load balancing policies, see
                  L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                - "Example: `3`"
            returned: on success
            type: int
            sample: 3
        drain:
            description:
                - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                  incoming traffic."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
        backup:
            description:
                - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                  traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
        offline:
            description:
                - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                  traffic.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
    sample: {
        "name": "10.0.0.3:8080",
        "ip_address": "10.0.0.3",
        "port": 8080,
        "weight": 3,
        "drain": false,
        "backup": false,
        "offline": false
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
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateBackendDetails
    from oci.load_balancer.models import UpdateBackendDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_get_fn(self):
        return self.client.get_backend

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
            backend_name=self.module.params.get("backend_name"),
        )

    def list_resources(self):
        required_list_method_params = [
            "load_balancer_id",
            "backend_set_name",
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

        return oci_common_utils.list_all_resources(self.client.list_backends, **kwargs)

    def get_create_model_class(self):
        return CreateBackendDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_backend,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_backend_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("backend_set_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
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
                update_backend_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("backend_set_name"),
                backend_name=self.module.params.get("backend_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backend,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("backend_set_name"),
                backend_name=self.module.params.get("backend_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BackendHelperCustom = get_custom_class("BackendHelperCustom")


class ResourceHelper(BackendHelperCustom, BackendHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            ip_address=dict(type="str", required=True),
            port=dict(type="int", required=True),
            weight=dict(type="int"),
            backup=dict(type="bool"),
            drain=dict(type="bool"),
            offline=dict(type="bool"),
            load_balancer_id=dict(type="str", required=True),
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
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
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
