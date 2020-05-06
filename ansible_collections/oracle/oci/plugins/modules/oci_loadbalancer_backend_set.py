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
module: oci_loadbalancer_backend_set
short_description: Manage a BackendSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BackendSet resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a backend set to a load balancer.
version_added: "2.5"
options:
    name:
        description:
            - A friendly name for the backend set. It must be unique and it cannot be changed.
            - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
              contain spaces. Avoid entering confidential information.
            - "Example: `example_backend_set`"
        type: str
        required: true
    policy:
        description:
            - The load balancer policy for the backend set. To get a list of available policies, use the
              L(ListPolicies,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
            - "Example: `LEAST_CONNECTIONS`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: str
    backends:
        description:
            - ""
            - Required for update using I(state=present) with name present.
        type: list
        suboptions:
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
                type: int
            backup:
                description:
                    - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                      traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                    - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                    - "Example: `false`"
                type: bool
            drain:
                description:
                    - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                      incoming traffic."
                    - "Example: `false`"
                type: bool
            offline:
                description:
                    - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                      traffic.
                    - "Example: `false`"
                type: bool
    health_checker:
        description:
            - ""
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: dict
        suboptions:
            protocol:
                description:
                    - The protocol the health check must use; either HTTP or TCP.
                    - "Example: `HTTP`"
                type: str
                required: true
            url_path:
                description:
                    - The path against which to run the health check.
                    - "Example: `/healthcheck`"
                type: str
            port:
                description:
                    - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                      port information from the `Backend` object.
                    - "Example: `8080`"
                type: int
            return_code:
                description:
                    - The status code a healthy backend server should return.
                    - "Example: `200`"
                type: int
            retries:
                description:
                    - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                      when recovering a server to the \\"healthy\\" state."
                    - "Example: `3`"
                type: int
            timeout_in_millis:
                description:
                    - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                      returns within this timeout period.
                    - "Example: `3000`"
                type: int
            interval_in_millis:
                description:
                    - The interval between health checks, in milliseconds.
                    - "Example: `10000`"
                type: int
            response_body_regex:
                description:
                    - A regular expression for parsing the response body from the backend server.
                    - "Example: `^((?!false).|\\\\s)*$`"
                type: str
    ssl_configuration:
        description:
            - ""
        type: dict
        suboptions:
            certificate_name:
                description:
                    - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                      Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                      Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                    - "Example: `example_certificate_bundle`"
                type: str
                required: true
            verify_peer_certificate:
                description:
                    - Whether the load balancer listener should verify peer certificates.
                    - "Example: `true`"
                type: bool
            verify_depth:
                description:
                    - The maximum depth for peer certificate chain verification.
                    - "Example: `3`"
                type: int
    session_persistence_configuration:
        description:
            - ""
        type: dict
        suboptions:
            cookie_name:
                description:
                    - "The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
                      that any cookie set by the backend causes the session to persist."
                    - "Example: `example_cookie`"
                type: str
                required: true
            disable_fallback:
                description:
                    - Whether the load balancer is prevented from directing traffic from a persistent session client to
                      a different backend server if the original server is unavailable. Defaults to false.
                    - "Example: `false`"
                type: bool
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a backend set.
        type: str
        required: true
    state:
        description:
            - The state of the BackendSet.
            - Use I(state=present) to create or update a BackendSet.
            - Use I(state=absent) to delete a BackendSet.
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
- name: Create backend_set
  oci_loadbalancer_backend_set:
    name: example_backend_set
    policy: LEAST_CONNECTIONS
    health_checker:
      protocol: HTTP
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Update backend_set
  oci_loadbalancer_backend_set:
    name: example_backend_set
    policy: LEAST_CONNECTIONS
    backends:
    - ip_address: 10.0.0.3
      port: 8080
    health_checker:
      protocol: HTTP
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete backend_set
  oci_loadbalancer_backend_set:
    name: example_backend_set
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
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
                - A friendly name for the backend set. It must be unique and it cannot be changed.
                - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
                  contain spaces. Avoid entering confidential information.
                - "Example: `example_backend_set`"
            returned: on success
            type: string
            sample: example_backend_set
        policy:
            description:
                - The load balancer policy for the backend set. To get a list of available policies, use the
                  L(ListPolicies,https://docs.cloud.oracle.com/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
                - "Example: `LEAST_CONNECTIONS`"
            returned: on success
            type: string
            sample: LEAST_CONNECTIONS
        backends:
            description:
                - ""
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
        health_checker:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                protocol:
                    description:
                        - The protocol the health check must use; either HTTP or TCP.
                        - "Example: `HTTP`"
                    returned: on success
                    type: string
                    sample: HTTP
                url_path:
                    description:
                        - The path against which to run the health check.
                        - "Example: `/healthcheck`"
                    returned: on success
                    type: string
                    sample: /healthcheck
                port:
                    description:
                        - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                          port information from the `Backend` object.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 0
                return_code:
                    description:
                        - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                          you can use common HTTP status codes such as \\"200\\"."
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 0
                retries:
                    description:
                        - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                          when recovering a server to the \\"healthy\\" state. Defaults to 3."
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
                timeout_in_millis:
                    description:
                        - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                          returns within this timeout period. Defaults to 3000 (3 seconds).
                        - "Example: `3000`"
                    returned: on success
                    type: int
                    sample: 3000
                interval_in_millis:
                    description:
                        - The interval between health checks, in milliseconds. The default is 10000 (10 seconds).
                        - "Example: `10000`"
                    returned: on success
                    type: int
                    sample: 10000
                response_body_regex:
                    description:
                        - A regular expression for parsing the response body from the backend server.
                        - "Example: `^((?!false).|\\\\s)*$`"
                    returned: on success
                    type: string
                    sample: ^((?!false).|\\s)*$
        ssl_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: string
                    sample: example_certificate_bundle
                verify_peer_certificate:
                    description:
                        - Whether the load balancer listener should verify peer certificates.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                verify_depth:
                    description:
                        - The maximum depth for peer certificate chain verification.
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
        session_persistence_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                cookie_name:
                    description:
                        - "The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
                          that any cookie set by the backend causes the session to persist."
                        - "Example: `example_cookie`"
                    returned: on success
                    type: string
                    sample: example_cookie
                disable_fallback:
                    description:
                        - Whether the load balancer is prevented from directing traffic from a persistent session client to
                          a different backend server if the original server is unavailable. Defaults to false.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
    sample: {
        "name": "example_backend_set",
        "policy": "LEAST_CONNECTIONS",
        "backends": [{
            "name": "10.0.0.3:8080",
            "ip_address": "10.0.0.3",
            "port": 8080,
            "weight": 3,
            "drain": false,
            "backup": false,
            "offline": false
        }],
        "health_checker": {
            "protocol": "HTTP",
            "url_path": "/healthcheck",
            "port": 0,
            "return_code": 0,
            "retries": 3,
            "timeout_in_millis": 3000,
            "interval_in_millis": 10000,
            "response_body_regex": "^((?!false).|\\\\s)*$"
        },
        "ssl_configuration": {
            "certificate_name": "example_certificate_bundle",
            "verify_peer_certificate": true,
            "verify_depth": 3
        },
        "session_persistence_configuration": {
            "cookie_name": "example_cookie",
            "disable_fallback": false
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
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateBackendSetDetails
    from oci.load_balancer.models import UpdateBackendSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendSetHelperGen(OCIResourceHelperBase):
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
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("name"),
        )

    def list_resources(self):
        required_list_method_params = [
            "load_balancer_id",
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
                create_backend_set_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
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
                update_backend_set_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BackendSetHelperCustom = get_custom_class("BackendSetHelperCustom")


class ResourceHelper(BackendSetHelperCustom, BackendSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            policy=dict(type="str"),
            backends=dict(
                type="list",
                elements="dict",
                options=dict(
                    ip_address=dict(type="str", required=True),
                    port=dict(type="int", required=True),
                    weight=dict(type="int"),
                    backup=dict(type="bool"),
                    drain=dict(type="bool"),
                    offline=dict(type="bool"),
                ),
            ),
            health_checker=dict(
                type="dict",
                options=dict(
                    protocol=dict(type="str", required=True),
                    url_path=dict(type="str"),
                    port=dict(type="int"),
                    return_code=dict(type="int"),
                    retries=dict(type="int"),
                    timeout_in_millis=dict(type="int"),
                    interval_in_millis=dict(type="int"),
                    response_body_regex=dict(type="str"),
                ),
            ),
            ssl_configuration=dict(
                type="dict",
                options=dict(
                    certificate_name=dict(type="str", required=True),
                    verify_peer_certificate=dict(type="bool"),
                    verify_depth=dict(type="int"),
                ),
            ),
            session_persistence_configuration=dict(
                type="dict",
                options=dict(
                    cookie_name=dict(type="str", required=True),
                    disable_fallback=dict(type="bool"),
                ),
            ),
            load_balancer_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backend_set",
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
