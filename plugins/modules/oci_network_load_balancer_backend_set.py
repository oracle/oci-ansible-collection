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
module: oci_network_load_balancer_backend_set
short_description: Manage a BackendSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BackendSet resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a backend set to a network load balancer.
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
            - A user-friendly name for the backend set that must be unique and cannot be changed.
            - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
              contain spaces. Avoid entering confidential information.
            - "Example: `example_backend_set`"
        type: str
        required: true
    policy:
        description:
            - The network load balancer policy for the backend set.
            - "Example: `FIVE_TUPLE``"
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "TWO_TUPLE"
            - "THREE_TUPLE"
            - "FIVE_TUPLE"
    is_preserve_source:
        description:
            - If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
              Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this
              parameter cannot be disabled.
              The value is true by default.
            - This parameter is updatable.
        type: bool
    backends:
        description:
            - An array of backends to be associated with the backend set.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - A read-only field showing the IP address/OCID and port that uniquely identify this backend server in the backend set.
                    - "Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`"
                type: str
            ip_address:
                description:
                    - The IP address of the backend server.
                    - "Example: `10.0.0.3`"
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
                type: int
                required: true
            weight:
                description:
                    - The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                      proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
                      as a server weighted '1'.
                      For more information about load balancing policies, see
                      L(How Network Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                    - "Example: `3`"
                type: int
            is_backup:
                description:
                    - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no
                      ingress
                      traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
                    - "Example: `false`"
                type: bool
            is_drain:
                description:
                    - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
                      incoming traffic."
                    - "Example: `false`"
                type: bool
            is_offline:
                description:
                    - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
                      traffic.
                    - "Example: `false`"
                type: bool
    health_checker:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            protocol:
                description:
                    - The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP.
                    - "Example: `HTTP`"
                type: str
                choices:
                    - "HTTP"
                    - "HTTPS"
                    - "TCP"
                    - "UDP"
                required: true
            port:
                description:
                    - The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the
                      port information from the `Backend` object. The port must be specified if the backend port is 0.
                    - "Example: `8080`"
                type: int
            retries:
                description:
                    - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                      when recovering a server to the \\"healthy\\" state. The default value is 3."
                    - "Example: `3`"
                type: int
            timeout_in_millis:
                description:
                    - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                      returns within this timeout period. The default value is 3000 (3 seconds).
                    - "Example: `3000`"
                type: int
            interval_in_millis:
                description:
                    - The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).
                    - "Example: `10000`"
                type: int
            url_path:
                description:
                    - The path against which to run the health check.
                    - "Example: `/healthcheck`"
                type: str
            response_body_regex:
                description:
                    - A regular expression for parsing the response body from the backend server.
                    - "Example: `^((?!false).|\\\\s)*$`"
                type: str
            return_code:
                description:
                    - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                      then you can use common HTTP status codes such as \\"200\\"."
                    - "Example: `200`"
                type: int
            request_data:
                description:
                    - Base64 encoded pattern to be sent as UDP or TCP health check probe.
                type: str
            response_data:
                description:
                    - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
                type: str
    state:
        description:
            - The state of the BackendSet.
            - Use I(state=present) to create or update a BackendSet.
            - Use I(state=absent) to delete a BackendSet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backend_set
  oci_network_load_balancer_backend_set:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: example_backend_set
    policy: FIVE_TUPLE
    health_checker:
      protocol: HTTP

- name: Update backend_set
  oci_network_load_balancer_backend_set:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: example_backend_set

- name: Delete backend_set
  oci_network_load_balancer_backend_set:
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: example_backend_set
    state: absent

"""

RETURN = """
backend_set:
    description:
        - Details of the BackendSet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A user-friendly name for the backend set that must be unique and cannot be changed.
                - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
                  contain spaces. Avoid entering confidential information.
                - "Example: `example_backend_set`"
            returned: on success
            type: str
            sample: example_backend_set
        policy:
            description:
                - The network load balancer policy for the backend set.
                - "Example: `FIVE_TUPLE`"
            returned: on success
            type: str
            sample: FIVE_TUPLE
        is_preserve_source:
            description:
                - If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
                  Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this
                  parameter cannot be disabled.
                  The value is true by default.
            returned: on success
            type: bool
            sample: true
        backends:
            description:
                - Array of backends.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set.
                        - "Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`"
                    returned: on success
                    type: str
                    sample: 10.0.0.3:8080
                ip_address:
                    description:
                        - "The IP address of the backend server.
                          Example: `10.0.0.3`"
                    returned: on success
                    type: str
                    sample: 10.0.0.3
                target_id:
                    description:
                        - "The IP OCID/Instance OCID associated with the backend server.
                          Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`"
                    returned: on success
                    type: str
                    sample: "ocid1.privateip..oc1.unique_ID"
                port:
                    description:
                        - The communication port for the backend server.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 8080
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
                    sample: 3
                is_drain:
                    description:
                        - "Whether the network load balancer should drain this server. Servers marked \\"isDrain\\" receive no
                          incoming traffic."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
                is_backup:
                    description:
                        - "Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no
                          ingress
                          traffic to this backend server unless all other backend servers not marked as \\"isBackup\\" fail the health check policy."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
                is_offline:
                    description:
                        - Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
                          traffic.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
        health_checker:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                protocol:
                    description:
                        - The protocol the health check must use; either HTTP or HTTPS, or UDP or TCP.
                        - "Example: `HTTP`"
                    returned: on success
                    type: str
                    sample: HTTP
                port:
                    description:
                        - The backend server port against which to run the health check. If the port is not specified, then the network load balancer uses the
                          port information from the `Backend` object. The port must be specified if the backend port is 0.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 8080
                retries:
                    description:
                        - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                          when recovering a server to the \\"healthy\\" state. The default value is 3."
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
                timeout_in_millis:
                    description:
                        - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                          returns within this timeout period. The default value is 3000 (3 seconds).
                        - "Example: `3000`"
                    returned: on success
                    type: int
                    sample: 3000
                interval_in_millis:
                    description:
                        - The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).
                        - "Example: `10000`"
                    returned: on success
                    type: int
                    sample: 10000
                url_path:
                    description:
                        - The path against which to run the health check.
                        - "Example: `/healthcheck`"
                    returned: on success
                    type: str
                    sample: /healthcheck
                response_body_regex:
                    description:
                        - A regular expression for parsing the response body from the backend server.
                        - "Example: `^((?!false).|\\\\s)*$`"
                    returned: on success
                    type: str
                    sample: "^((?!false).|\\\\s)*$"
                return_code:
                    description:
                        - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                          then you can use common HTTP status codes such as \\"200\\"."
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 0
                request_data:
                    description:
                        - Base64 encoded pattern to be sent as UDP or TCP health check probe.
                    returned: on success
                    type: str
                    sample: "example_request_data"
                response_data:
                    description:
                        - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
                    returned: on success
                    type: str
                    sample: "example_response_data"
    sample: {
        "name": "example_backend_set",
        "policy": "FIVE_TUPLE",
        "is_preserve_source": true,
        "backends": [{
            "name": "10.0.0.3:8080",
            "ip_address": "10.0.0.3",
            "target_id": "ocid1.privateip..oc1.unique_ID",
            "port": 8080,
            "weight": 3,
            "is_drain": false,
            "is_backup": false,
            "is_offline": false
        }],
        "health_checker": {
            "protocol": "HTTP",
            "port": 8080,
            "retries": 3,
            "timeout_in_millis": 3000,
            "interval_in_millis": 10000,
            "url_path": "/healthcheck",
            "response_body_regex": "^((?!false).|\\\\s)*$",
            "return_code": 0,
            "request_data": UNKNOWN TYPE - str,
            "response_data": UNKNOWN TYPE - str
        }
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
    from oci.network_load_balancer.models import CreateBackendSetDetails
    from oci.network_load_balancer.models import UpdateBackendSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerBackendSetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_backend_set

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("name"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_backend_sets, **kwargs
        )

    def get_create_model_class(self):
        return CreateBackendSetDetails

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
            call_fn=self.client.create_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                create_backend_set_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBackendSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_backend_set_details=update_details,
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerBackendSetHelperCustom = get_custom_class(
    "NetworkLoadBalancerBackendSetHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerBackendSetHelperCustom, NetworkLoadBalancerBackendSetHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str", required=True),
            policy=dict(type="str", choices=["TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"]),
            is_preserve_source=dict(type="bool"),
            backends=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str"),
                    ip_address=dict(type="str"),
                    target_id=dict(type="str"),
                    port=dict(type="int", required=True),
                    weight=dict(type="int"),
                    is_backup=dict(type="bool"),
                    is_drain=dict(type="bool"),
                    is_offline=dict(type="bool"),
                ),
            ),
            health_checker=dict(
                type="dict",
                options=dict(
                    protocol=dict(
                        type="str",
                        required=True,
                        choices=["HTTP", "HTTPS", "TCP", "UDP"],
                    ),
                    port=dict(type="int"),
                    retries=dict(type="int"),
                    timeout_in_millis=dict(type="int"),
                    interval_in_millis=dict(type="int"),
                    url_path=dict(type="str"),
                    response_body_regex=dict(type="str"),
                    return_code=dict(type="int"),
                    request_data=dict(type="str"),
                    response_data=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backend_set",
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
