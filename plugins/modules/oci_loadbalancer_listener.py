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
module: oci_loadbalancer_listener
short_description: Manage a Listener resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Listener resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a listener to a load balancer.
version_added: "2.9.0"
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
            - This parameter is updatable.
        type: list
        elements: str
    path_route_set_name:
        description:
            - Deprecated. Please use `routingPolicies` instead.
            - The name of the set of path-based routing rules, L(PathRouteSet,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/),
              applied to this listener's traffic.
            - "Example: `example_path_route_set`"
            - This parameter is updatable.
        type: str
    routing_policy_name:
        description:
            - The name of the routing policy applied to this listener's traffic.
            - "Example: `example_routing_policy`"
            - This parameter is updatable.
        type: str
    ssl_configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            verify_depth:
                description:
                    - The maximum depth for peer certificate chain verification.
                    - "Example: `3`"
                type: int
            verify_peer_certificate:
                description:
                    - Whether the load balancer listener should verify peer certificates.
                    - "Example: `true`"
                type: bool
            trusted_certificate_authority_ids:
                description:
                    - Ids for OCI certificates service CA or CA bundles for the load balancer to trust.
                    - "Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`"
                type: list
                elements: str
            certificate_ids:
                description:
                    - Ids for OCI certificates service certificates. Currently only a single Id may be passed.
                    - "Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`"
                type: list
                elements: str
            certificate_name:
                description:
                    - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                      Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                      Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                    - "Example: `example_certificate_bundle`"
                type: str
            protocols:
                description:
                    - A list of SSL protocols the load balancer must support for HTTPS or SSL connections.
                    - The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure
                      connection ensures that all data passed between the client and the server is private.
                    - "The Load Balancing service supports the following protocols:"
                    - "*  TLSv1
                      *  TLSv1.1
                      *  TLSv1.2"
                    - If this field is not specified, TLSv1.2 is the default.
                    - "**Warning:** All SSL listeners created on a given port must use the same set of SSL protocols."
                    - "**Notes:**"
                    - "*  The handshake to establish an SSL connection fails if the client supports none of the specified protocols.
                      *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                         suite.
                      *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation
                         displays a list of SSL protocols currently used by those resources."
                    - "example: `[\\"TLSv1.1\\", \\"TLSv1.2\\"]`"
                type: list
                elements: str
            cipher_suite_name:
                description:
                    - The name of the cipher suite to use for HTTPS or SSL connections.
                    - If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.
                    - "**Notes:**"
                    - "*  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                         suite. Clients cannot perform an SSL handshake if there is an incompatible configuration.
                      *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured
                         certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA
                         certificates.
                      *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns
                         `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners
                         that predate this feature.
                      *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET`
                         operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for
                         existing listeners that predate this feature.
                      *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL
                         configuration for existing backend sets that predate this feature.
                      *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field,
                         you must specify an appropriate predefined or custom cipher suite name when updating the resource.
                      *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for
                         this field."
                    - "example: `example_cipher_suite`"
                type: str
            server_order_preference:
                description:
                    - When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
                      ciphers.
                    - "**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                                field is ignored when the `SSLConfiguration` object is associated with a backend set."
                type: str
                choices:
                    - "ENABLED"
                    - "DISABLED"
    connection_configuration:
        description:
            - ""
            - This parameter is updatable.
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
    rule_set_names:
        description:
            - The names of the L(rule sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.
            - "Example: [\\"example_rule_set\\"]"
            - This parameter is updatable.
        type: list
        elements: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a listener.
        type: str
        required: true
    name:
        description:
            - A friendly name for the listener. It must be unique and it cannot be changed.
              Avoid entering confidential information.
            - "Example: `example_listener`"
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
    # required
    default_backend_set_name: default_backend_set_name_example
    port: 56
    protocol: protocol_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    hostname_names: [ "hostname_names_example" ]
    path_route_set_name: path_route_set_name_example
    routing_policy_name: routing_policy_name_example
    ssl_configuration:
      # optional
      verify_depth: 56
      verify_peer_certificate: true
      trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
      certificate_ids: [ "certificate_ids_example" ]
      certificate_name: certificate_name_example
      protocols: [ "protocols_example" ]
      cipher_suite_name: cipher_suite_name_example
      server_order_preference: ENABLED
    connection_configuration:
      # required
      idle_timeout: 56

      # optional
      backend_tcp_proxy_protocol_version: 56
    rule_set_names: [ "rule_set_names_example" ]

- name: Update listener
  oci_loadbalancer_listener:
    # required
    default_backend_set_name: default_backend_set_name_example
    port: 56
    protocol: protocol_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    hostname_names: [ "hostname_names_example" ]
    path_route_set_name: path_route_set_name_example
    routing_policy_name: routing_policy_name_example
    ssl_configuration:
      # optional
      verify_depth: 56
      verify_peer_certificate: true
      trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
      certificate_ids: [ "certificate_ids_example" ]
      certificate_name: certificate_name_example
      protocols: [ "protocols_example" ]
      cipher_suite_name: cipher_suite_name_example
      server_order_preference: ENABLED
    connection_configuration:
      # required
      idle_timeout: 56

      # optional
      backend_tcp_proxy_protocol_version: 56
    rule_set_names: [ "rule_set_names_example" ]

- name: Delete listener
  oci_loadbalancer_listener:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
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
            sample: name_example
        default_backend_set_name:
            description:
                - The name of the associated backend set.
                - "Example: `example_backend_set`"
            returned: on success
            type: str
            sample: default_backend_set_name_example
        port:
            description:
                - The communication port for the listener.
                - "Example: `80`"
            returned: on success
            type: int
            sample: 56
        protocol:
            description:
                - The protocol on which the listener accepts connection requests.
                  To get a list of valid protocols, use the L(ListProtocols,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols)
                  operation.
                - "Example: `HTTP`"
            returned: on success
            type: str
            sample: protocol_example
        hostname_names:
            description:
                - An array of hostname resource names.
            returned: on success
            type: list
            sample: []
        path_route_set_name:
            description:
                - Deprecated. Please use `routingPolicies` instead.
                - The name of the set of path-based routing rules, L(PathRouteSet,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/),
                  applied to this listener's traffic.
                - "Example: `example_path_route_set`"
            returned: on success
            type: str
            sample: path_route_set_name_example
        ssl_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                verify_depth:
                    description:
                        - The maximum depth for peer certificate chain verification.
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 56
                verify_peer_certificate:
                    description:
                        - Whether the load balancer listener should verify peer certificates.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                trusted_certificate_authority_ids:
                    description:
                        - Ids for OCI certificates service CA or CA bundles for the load balancer to trust.
                        - "Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`"
                    returned: on success
                    type: list
                    sample: []
                certificate_ids:
                    description:
                        - Ids for OCI certificates service certificates. Currently only a single Id may be passed.
                        - "Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`"
                    returned: on success
                    type: list
                    sample: []
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: str
                    sample: certificate_name_example
                server_order_preference:
                    description:
                        - When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
                          ciphers.
                        - "**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                                    field is ignored when the `SSLConfiguration` object is associated with a backend set."
                    returned: on success
                    type: str
                    sample: ENABLED
                cipher_suite_name:
                    description:
                        - The name of the cipher suite to use for HTTPS or SSL connections.
                        - If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.
                        - "**Notes:**"
                        - "*  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                             suite. Clients cannot perform an SSL handshake if there is an incompatible configuration.
                          *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured
                             certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA
                             certificates.
                          *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns
                             `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners
                             that predate this feature.
                          *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET`
                             operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for
                             existing listeners that predate this feature.
                          *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL
                             configuration for existing backend sets that predate this feature.
                          *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field,
                             you must specify an appropriate predefined or custom cipher suite name when updating the resource.
                          *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for
                             this field."
                        - "example: `example_cipher_suite`"
                    returned: on success
                    type: str
                    sample: cipher_suite_name_example
                protocols:
                    description:
                        - A list of SSL protocols the load balancer must support for HTTPS or SSL connections.
                        - The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure
                          connection ensures that all data passed between the client and the server is private.
                        - "The Load Balancing service supports the following protocols:"
                        - "*  TLSv1
                          *  TLSv1.1
                          *  TLSv1.2"
                        - If this field is not specified, TLSv1.2 is the default.
                        - "**Warning:** All SSL listeners created on a given port must use the same set of SSL protocols."
                        - "**Notes:**"
                        - "*  The handshake to establish an SSL connection fails if the client supports none of the specified protocols.
                          *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                             suite.
                          *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation
                             displays a list of SSL protocols currently used by those resources."
                        - "example: `[\\"TLSv1.1\\", \\"TLSv1.2\\"]`"
                    returned: on success
                    type: list
                    sample: []
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
                    sample: 56
                backend_tcp_proxy_protocol_version:
                    description:
                        - The backend TCP Proxy Protocol version.
                        - "Example: `1`"
                    returned: on success
                    type: int
                    sample: 56
        rule_set_names:
            description:
                - The names of the L(rule sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the listener.
                - "Example: [\\"example_rule_set\\"]"
            returned: on success
            type: list
            sample: []
        routing_policy_name:
            description:
                - The name of the routing policy applied to this listener's traffic.
                - "Example: `example_routing_policy_name`"
            returned: on success
            type: str
            sample: routing_policy_name_example
    sample: {
        "name": "name_example",
        "default_backend_set_name": "default_backend_set_name_example",
        "port": 56,
        "protocol": "protocol_example",
        "hostname_names": [],
        "path_route_set_name": "path_route_set_name_example",
        "ssl_configuration": {
            "verify_depth": 56,
            "verify_peer_certificate": true,
            "trusted_certificate_authority_ids": [],
            "certificate_ids": [],
            "certificate_name": "certificate_name_example",
            "server_order_preference": "ENABLED",
            "cipher_suite_name": "cipher_suite_name_example",
            "protocols": []
        },
        "connection_configuration": {
            "idle_timeout": 56,
            "backend_tcp_proxy_protocol_version": 56
        },
        "rule_set_names": [],
        "routing_policy_name": "routing_policy_name_example"
    }
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
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateListenerDetails
    from oci.load_balancer.models import UpdateListenerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ListenerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update and delete"""

    def get_possible_entity_types(self):
        return super(ListenerHelperGen, self).get_possible_entity_types() + [
            "listener",
            "listeners",
            "loadBalancerlistener",
            "loadBalancerlisteners",
            "listenerresource",
            "listenersresource",
            "loadbalancer",
        ]

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
            hostname_names=dict(type="list", elements="str"),
            path_route_set_name=dict(type="str"),
            routing_policy_name=dict(type="str"),
            ssl_configuration=dict(
                type="dict",
                options=dict(
                    verify_depth=dict(type="int"),
                    verify_peer_certificate=dict(type="bool"),
                    trusted_certificate_authority_ids=dict(type="list", elements="str"),
                    certificate_ids=dict(type="list", elements="str"),
                    certificate_name=dict(type="str"),
                    protocols=dict(type="list", elements="str"),
                    cipher_suite_name=dict(type="str"),
                    server_order_preference=dict(
                        type="str", choices=["ENABLED", "DISABLED"]
                    ),
                ),
            ),
            connection_configuration=dict(
                type="dict",
                options=dict(
                    idle_timeout=dict(type="int", required=True),
                    backend_tcp_proxy_protocol_version=dict(type="int"),
                ),
            ),
            rule_set_names=dict(type="list", elements="str"),
            load_balancer_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
