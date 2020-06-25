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
module: oci_loadbalancer_health_checker_facts
short_description: Fetches details about a HealthChecker resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a HealthChecker resource in Oracle Cloud Infrastructure
    - Gets the health check policy information for a given load balancer and backend set.
version_added: "2.5"
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer associated with the health check policy to
              be retrieved.
        type: str
        aliases: ["id"]
        required: true
    backend_set_name:
        description:
            - The name of the backend set associated with the health check policy to be retrieved.
            - "Example: `example_backend_set`"
        type: str
        required: true
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific health_checker
  oci_loadbalancer_health_checker_facts:
    load_balancer_id: ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx
    backend_set_name: example_backend_set

"""

RETURN = """
health_checker:
    description:
        - HealthChecker resource
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
    sample: {
        "protocol": "HTTP",
        "url_path": "/healthcheck",
        "port": 0,
        "return_code": 0,
        "retries": 3,
        "timeout_in_millis": 3000,
        "interval_in_millis": 10000,
        "response_body_regex": "^((?!false).|\\\\s)*$"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HealthCheckerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "backend_set_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_health_checker,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )


HealthCheckerFactsHelperCustom = get_custom_class("HealthCheckerFactsHelperCustom")


class ResourceFactsHelper(HealthCheckerFactsHelperCustom, HealthCheckerFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="health_checker",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(health_checker=result)


if __name__ == "__main__":
    main()
