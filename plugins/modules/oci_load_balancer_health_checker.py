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
module: oci_load_balancer_health_checker
short_description: Update health checker details of a backend set in a load balancer in
                   OCI Load Balancing Service
description:
    - Update health checker details of a backend set in a load balancer in OCI Load Balancing Service.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer in which the backend set
                     containing the health checker details belongs
        required: true
        aliases: ['id']
    backend_set_name:
        description: The name of the backend set containing health checker details.
        required: true
    interval_in_millis:
        description: The interval between health checks, in milliseconds.
        required: true
    port:
        description: The communication port for the backend server.
        required: true
    protocol:
        description: The protocol the health check must use, either HTTP or TCP.
        required: true
    response_body_regex:
        description:  regular expression for parsing the response body from the backend server.
        required: true
    retries:
        description: The number of retries to attempt before a backend server is considered unhealthy.
        required: true
    return_code:
        description: The status code a healthy backend server should return.
        required: true
    timeout_in_millis:
        description: The maximum time, in milliseconds, to wait for a reply to
                     a health check. A health check is successful only if a reply
                     returns within this timeout period.
        required: true
    url_path :
        description: The path against which to run the health check..
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Update Health Checker of a Backend Set
- name: Update Health Checker of a Backend Set
  oci_load_balancer_health_checker:
    load_balancer_id: 'ocid1.loadbalalncer.aaaa'
    backend_set_name: 'backend_set'
    interval_in_millis: 30000
    port: 8080
    protocol: "HTTP"
    response_body_regex: "^(500|40[1348])$"
    retries: 3
    timeout_in_millis: 6000
    return_code: 200
    url_path: "/healthcheckupdated"
"""

RETURN = """
    health_checker:
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
        sample: {
                    "interval_in_millis": 30000,
                    "port": 8080,
                    "protocol": "HTTP",
                    "response_body_regex": "^(500|40[1348])$",
                    "retries": 3,
                    "return_code": 200,
                    "timeout_in_millis": 6000,
                    "url_path": "/healthcheck"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.util import to_dict
    from oci.load_balancer.models import UpdateHealthCheckerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def update_health_checker(lb_client, module):
    health_checker = None
    result = dict(changed=False, health_checker="")
    lb_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    health_checker = oci_utils.get_existing_resource(
        lb_client.get_health_checker,
        module,
        load_balancer_id=lb_id,
        backend_set_name=backend_set_name,
    )
    if health_checker:
        changed = False
        result = dict(health_checker=to_dict(health_checker), changed=changed)
        get_logger().info(
            "Updating healtch checker details for backendset %s in load balancer %s",
            backend_set_name,
            lb_id,
        )
        input_health_checker = UpdateHealthCheckerDetails()
        for attribute in input_health_checker.attribute_map:
            input_attribute_value = module.params.get(attribute)
            changed = oci_utils.check_and_update_attributes(
                input_health_checker,
                attribute,
                input_attribute_value,
                getattr(health_checker, attribute),
                changed,
            )
        get_logger().debug(
            "Existing health checker property values: %s, input property values: %s",
            health_checker,
            input_health_checker,
        )
        if changed:
            result = oci_lb_utils.create_or_update_lb_resources_and_wait(
                resource_type="health_checker",
                function=lb_client.update_health_checker,
                kwargs_function={
                    "health_checker": input_health_checker,
                    "load_balancer_id": lb_id,
                    "backend_set_name": backend_set_name,
                },
                lb_client=lb_client,
                get_fn=lb_client.get_health_checker,
                kwargs_get={
                    "load_balancer_id": lb_id,
                    "backend_set_name": backend_set_name,
                },
                module=module,
            )
            get_logger().info(
                "Updating health checker details for backendset %s in load balancer %s",
                backend_set_name,
                lb_id,
            )
        else:
            get_logger().info(
                "No update to the health checker details for backendset %s in load balancer %s as "
                + "no attribute changed",
                backend_set_name,
                lb_id,
            )
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_health_checker")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backend_set_name=dict(type="str", required=True),
            interval_in_millis=dict(type=int, required=False),
            response_body_regex=dict(type="str", required=True),
            protocol=dict(type="str", required=True),
            port=dict(type=int, required=True),
            retries=dict(type=int, required=True),
            return_code=dict(type=int, required=True),
            timeout_in_millis=dict(type=int, required=True),
            url_path=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = update_health_checker(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
