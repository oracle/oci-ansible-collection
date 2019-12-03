#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_load_balancer_health_checker_facts
short_description: Fetch details of all health checker details of load balancer backend sets of a load balancer
description:
    - Fetch details of all health checker details of load balancer backend sets of a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the Backends belongs.
        required: true
        aliases: ['id']
    backend_set_name:
        description: The name of the backend set under which the backend exists.
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all health checker details of load balancer backends of a load balancer
- name: List a specific Health Checker Details of a Backend Set
  oci_load_balancer_health_checker_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      backend_set_name: 'backend_set'

#Fetch details of all health checkers  in a load balancer
- name: List all Health Checker Details
  oci_load_balancer_health_checker_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    health_checkers:
        description: Attributes of the health checker
        returned: success
        type: complex
        contains:
            interval_in_millis:
                description: The interval between health checks, in milliseconds.
                returned: always
                type: integer
                sample: 3000
            port:
                description: Port of the Load Balancer Backend
                returned: always
                type: string
                sample: 8080
            protocol:
                description: The protocol the health check must use
                returned: always
                type: string
                sample: HTTP
            response_body_regex:
                description: A regular expression for parsing the response body from the backend server.
                returned: always
                type: string
                sample: ^(500|40[1348])$
            retries:
                description: The number of retries to attempt before a backend server is considered unhealthy
                returned: always
                type: integer
                sample: 3
            return_code:
                description: The status code a healthy backend server should return
                returned: always
                type: integer
                sample: 200
            timeout_in_millis:
                description: The maximum time, in milliseconds, to wait for a reply to a health check
                returned: always
                type: integer
                sample: 60000
            url_path:
                description: The path against which to run the health check.
                returned: always
                type: string
                sample: /healthcheck
        sample: [
                 {
                    "interval_in_millis": 30000,
                    "port": 8080,
                    "protocol": "HTTP",
                    "response_body_regex": "^(500|40[1348])$",
                    "retries": 3,
                    "return_code": 200,
                    "timeout_in_millis": 6000,
                    "url_path": "/healthcheck"
                 },
                                  {
                    "interval_in_millis": 30000,
                    "port": 8282,
                    "protocol": "HTTP",
                    "response_body_regex": ".*",
                    "retries": 3,
                    "return_code": 200,
                    "timeout_in_millis": 6000,
                    "url_path": "/healthcheck"
                 }
                ]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

from ansible.module_utils import six

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_load_balancer_health_checker(lb_client, module):
    result = dict(health_checkers="")
    load_balancer_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    try:
        if backend_set_name is not None or backend_set_name:
            get_logger().info(
                "Listing all attributes of health checker for backendset %s \
                               in load balancer %s",
                backend_set_name,
                load_balancer_id,
            )
            response = oci_utils.call_with_backoff(
                lb_client.get_health_checker,
                load_balancer_id=load_balancer_id,
                backend_set_name=backend_set_name,
            )
            health_checkers = [response.data]
        else:
            get_logger().info(
                "Listing all attributes of  all health checkers \
                               in load balancer %s",
                load_balancer_id,
            )
            load_balancer = oci_lb_utils.get_existing_load_balancer(
                lb_client, module, load_balancer_id
            )
            health_checkers = []
            for key, value in six.iteritems(load_balancer.backend_sets):
                health_checkers.append(value.health_checker)
            result["health_checkers"] = health_checkers
    except ServiceError as ex:
        get_logger().error("Unable to list health checkers due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    result["health_checkers"] = to_dict(health_checkers)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_health_checker_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backend_set_name=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_health_checker(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
