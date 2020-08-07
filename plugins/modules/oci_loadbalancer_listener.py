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
module: oci_loadbalancer_listener
short_description: Manage a Listener resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Listener resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a listener to a load balancer.
version_added: "2.9"
author: Oracle (@oracle)
options:
    default_backend_set_name:
        description:
            - The name of the associated backend set.
            - "Example: `example_backend_set`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: str
    port:
        description:
            - The communication port for the listener.
            - "Example: `80`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: int
    protocol:
        description:
            - The protocol on which the listener accepts connection requests.
              To get a list of valid protocols, use the L(ListProtocols,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols)
              operation.
            - "Example: `HTTP`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: str
    hostname_names:
        description:
            - An array of hostname resource names.
        type: list
    path_route_set_name:
        description:
            - The name of the set of path-based routing rules, L(PathRouteSet,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/),
              applied to this listener's traffic.
            - "Example: `example_path_route_set`"
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
    connection_configuration:
        description:
            - ""
        type: dict
        suboptions:
            idle_timeout:
                description:
                    - The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
                      between the client and backend servers. A send operation does not reset the timer for receive operations. A
                      receive operation does not reset the timer for send operations.
                    - For more information, see L(Connection
                      Configuration,https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration).
                    - "Example: `1200`"
                type: int
                required: true
            backend_tcp_proxy_protocol_version:
                description:
                    - The backend TCP Proxy Protocol version.
                    - "Example: `1`"
                type: int
    name:
        description:
            - A friendly name for the listener. It must be unique and it cannot be changed.
              Avoid entering confidential information.
            - "Example: `example_listener`"
        type: str
        required: true
    rule_set_names:
        description:
            - The names of the L(rule sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.
            - "Example: [\\"example_rule_set\\"]"
        type: list
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a listener.
        type: str
        required: true
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
  oci_loadbalancer_listener:
    default_backend_set_name: example_backend_set
    port: 80
    protocol: HTTP
    name: example_listener
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Update listener
  oci_loadbalancer_listener:
    default_backend_set_name: example_backend_set
    port: 80
    protocol: HTTP
    name: example_listener
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete listener
  oci_loadbalancer_listener:
    name: example_listener
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: example_listener
        default_backend_set_name:
            description:
                - The name of the associated backend set.
                - "Example: `example_backend_set`"
            returned: on success
            type: string
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
                  To get a list of valid protocols, use the L(ListProtocols,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols)
                  operation.
                - "Example: `HTTP`"
            returned: on success
            type: string
            sample: HTTP
        hostname_names:
            description:
                - An array of hostname resource names.
            returned: on success
            type: list
            sample: []
        path_route_set_name:
            description:
                - The name of the set of path-based routing rules, L(PathRouteSet,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/),
                  applied to this listener's traffic.
                - "Example: `example_path_route_set`"
            returned: on success
            type: string
            sample: example_path_route_set
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
        connection_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                idle_timeout:
                    description:
                        - The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
                          between the client and backend servers. A send operation does not reset the timer for receive operations. A
                          receive operation does not reset the timer for send operations.
                        - For more information, see L(Connection
                          Configuration,https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration).
                        - "Example: `1200`"
                    returned: on success
                    type: int
                    sample: 1200
                backend_tcp_proxy_protocol_version:
                    description:
                        - The backend TCP Proxy Protocol version.
                        - "Example: `1`"
                    returned: on success
                    type: int
                    sample: 1
        rule_set_names:
            description:
                - The names of the L(rule sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.
                - "Example: [\\"example_rule_set\\"]"
            returned: on success
            type: list
            sample: []
    sample: {
        "name": "example_listener",
        "default_backend_set_name": "example_backend_set",
        "port": 0,
        "protocol": "HTTP",
        "hostname_names": [],
        "path_route_set_name": "example_path_route_set",
        "ssl_configuration": {
            "certificate_name": "example_certificate_bundle",
            "verify_peer_certificate": true,
            "verify_depth": 3
        },
        "connection_configuration": {
            "idle_timeout": 1200,
            "backend_tcp_proxy_protocol_version": 1
        },
        "rule_set_names": []
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
    from oci.load_balancer.models import CreateListenerDetails
    from oci.load_balancer.models import UpdateListenerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ListenerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

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
                create_listener_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
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
                update_listener_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
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
                load_balancer_id=self.module.params.get("load_balancer_id"),
                listener_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ListenerHelperCustom = get_custom_class("ListenerHelperCustom")


class ResourceHelper(ListenerHelperCustom, ListenerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            default_backend_set_name=dict(type="str"),
            port=dict(type="int"),
            protocol=dict(type="str"),
            hostname_names=dict(type="list"),
            path_route_set_name=dict(type="str"),
            ssl_configuration=dict(
                type="dict",
                options=dict(
                    certificate_name=dict(type="str", required=True),
                    verify_peer_certificate=dict(type="bool"),
                    verify_depth=dict(type="int"),
                ),
            ),
            connection_configuration=dict(
                type="dict",
                options=dict(
                    idle_timeout=dict(type="int", required=True),
                    backend_tcp_proxy_protocol_version=dict(type="int"),
                ),
            ),
            name=dict(type="str", required=True),
            rule_set_names=dict(type="list"),
            load_balancer_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="listener",
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
