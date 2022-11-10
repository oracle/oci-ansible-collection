#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_network_load_balancer_health_checker
short_description: Manage a HealthChecker resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a HealthChecker resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network load balancer to update.
        type: str
        aliases: ["id"]
        required: true
    protocol:
        description:
            - The protocol that the health check must use; either HTTP, UDP, or TCP.
            - "Example: `HTTP`"
            - This parameter is updatable.
        type: str
        choices:
            - "HTTP"
            - "HTTPS"
            - "TCP"
            - "UDP"
    port:
        description:
            - The backend server port against which to run the health check.
            - "Example: `8080`"
            - This parameter is updatable.
        type: int
    retries:
        description:
            - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
              when recovering a server to the \\"healthy\\" state."
            - "Example: `3`"
            - This parameter is updatable.
        type: int
    timeout_in_millis:
        description:
            - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
              returns within this timeout period.
            - "Example: `3000`"
            - This parameter is updatable.
        type: int
    interval_in_millis:
        description:
            - The interval between health checks, in milliseconds.
            - "Example: `10000`"
            - This parameter is updatable.
        type: int
    url_path:
        description:
            - The path against which to run the health check.
            - "Example: `/healthcheck`"
            - This parameter is updatable.
        type: str
    response_body_regex:
        description:
            - A regular expression for parsing the response body from the backend server.
            - "Example: `^((?!false).|\\\\s)*$`"
            - This parameter is updatable.
        type: str
    return_code:
        description:
            - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
              then you can use common HTTP status codes such as \\"200\\"."
            - "Example: `200`"
            - This parameter is updatable.
        type: int
    request_data:
        description:
            - Base64 encoded pattern to be sent as UDP or TCP health check probe.
            - This parameter is updatable.
        type: str
    response_data:
        description:
            - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
            - This parameter is updatable.
        type: str
    backend_set_name:
        description:
            - The name of the backend set associated with the health check policy to be retrieved.
            - "Example: `example_backend_set`"
        type: str
        required: true
    state:
        description:
            - The state of the HealthChecker.
            - Use I(state=present) to update an existing a HealthChecker.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update health_checker
  oci_network_load_balancer_health_checker:
    # required
    network_load_balancer_id: "ocid1.networkloadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: backend_set_name_example

    # optional
    protocol: HTTP
    port: 56
    retries: 56
    timeout_in_millis: 56
    interval_in_millis: 56
    url_path: url_path_example
    response_body_regex: response_body_regex_example
    return_code: 56
    request_data: request_data_example
    response_data: response_data_example

"""

RETURN = """
health_checker:
    description:
        - Details of the HealthChecker resource acted upon by the current operation
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
            sample: 56
        retries:
            description:
                - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                  when recovering a server to the \\"healthy\\" state. The default value is 3."
                - "Example: `3`"
            returned: on success
            type: int
            sample: 56
        timeout_in_millis:
            description:
                - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                  returns within this timeout period. The default value is 3000 (3 seconds).
                - "Example: `3000`"
            returned: on success
            type: int
            sample: 56
        interval_in_millis:
            description:
                - The interval between health checks, in milliseconds. The default value is 10000 (10 seconds).
                - "Example: `10000`"
            returned: on success
            type: int
            sample: 56
        url_path:
            description:
                - The path against which to run the health check.
                - "Example: `/healthcheck`"
            returned: on success
            type: str
            sample: url_path_example
        response_body_regex:
            description:
                - A regular expression for parsing the response body from the backend server.
                - "Example: `^((?!false).|\\\\s)*$`"
            returned: on success
            type: str
            sample: response_body_regex_example
        return_code:
            description:
                - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                  then you can use common HTTP status codes such as \\"200\\"."
                - "Example: `200`"
            returned: on success
            type: int
            sample: 56
        request_data:
            description:
                - Base64 encoded pattern to be sent as UDP or TCP health check probe.
            returned: on success
            type: str
            sample: "null"

        response_data:
            description:
                - Base64 encoded pattern to be validated as UDP or TCP health check probe response.
            returned: on success
            type: str
            sample: "null"

    sample: {
        "protocol": "HTTP",
        "port": 56,
        "retries": 56,
        "timeout_in_millis": 56,
        "interval_in_millis": 56,
        "url_path": "url_path_example",
        "response_body_regex": "response_body_regex_example",
        "return_code": 56,
        "request_data": null,
        "response_data": null
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
    from oci.network_load_balancer import NetworkLoadBalancerClient
    from oci.network_load_balancer.models import UpdateHealthCheckerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkLoadBalancerHealthCheckerHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_possible_entity_types(self):
        return super(
            NetworkLoadBalancerHealthCheckerHelperGen, self
        ).get_possible_entity_types() + [
            "healthchecker",
            "healthcheckers",
            "networkLoadBalancerhealthchecker",
            "networkLoadBalancerhealthcheckers",
            "healthcheckerresource",
            "healthcheckersresource",
            "networkloadbalancer",
        ]

    def get_module_resource_id_param(self):
        return "backend_set_name"

    def get_module_resource_id(self):
        return self.module.params.get("backend_set_name")

    def get_get_fn(self):
        return self.client.get_health_checker

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_health_checker,
            network_load_balancer_id=self.module.params.get("network_load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )

    def get_update_model_class(self):
        return UpdateHealthCheckerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_health_checker,
            call_fn_args=(),
            call_fn_kwargs=dict(
                network_load_balancer_id=self.module.params.get(
                    "network_load_balancer_id"
                ),
                update_health_checker_details=update_details,
                backend_set_name=self.module.params.get("backend_set_name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkLoadBalancerHealthCheckerHelperCustom = get_custom_class(
    "NetworkLoadBalancerHealthCheckerHelperCustom"
)


class ResourceHelper(
    NetworkLoadBalancerHealthCheckerHelperCustom,
    NetworkLoadBalancerHealthCheckerHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            network_load_balancer_id=dict(aliases=["id"], type="str", required=True),
            protocol=dict(type="str", choices=["HTTP", "HTTPS", "TCP", "UDP"]),
            port=dict(type="int"),
            retries=dict(type="int"),
            timeout_in_millis=dict(type="int"),
            interval_in_millis=dict(type="int"),
            url_path=dict(type="str"),
            response_body_regex=dict(type="str"),
            return_code=dict(type="int"),
            request_data=dict(type="str"),
            response_data=dict(type="str"),
            backend_set_name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="health_checker",
        service_client_class=NetworkLoadBalancerClient,
        namespace="network_load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
