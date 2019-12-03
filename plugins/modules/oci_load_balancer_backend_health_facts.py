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
module: oci_load_balancer_backend_health_facts
short_description: Fetch details of Backend Health in a load balancer backend set of a load balancer
description:
    - Fetch details of Backend Health in a load balancer backend set of a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the Backends belongs.
        required: true
        aliases: ['id']
    backend_set_name:
        description: The name of the backend set under which the backend exists.
        required: true
    ip_address:
        description: The IP address of the backend server.
        required: true
    port:
        description: The communication port for the backend server.
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of the backend health of a backend set
- name: List a specific Load Balancer Backend's Health
  oci_load_balancer_backend_health_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      backend_set_name: 'ansible_backend_set'
      ip_address: '10.159.121.55'
      port: '8181'
"""

RETURN = """
    backend_health:
        description: Attributes of the Backend Health
        returned: success
        type: complex
        contains:
            health_check_results:
                description: A list of the most recent health check results
                             returned for the specified backend server. Element
                             of the list represent instance of HealthCheckResult
                returned: always
                type: string
                sample: [
                            {
                                "health_check_status": "OK",
                                "source_ip_address": "10.0.0.64",
                                "subnet_id": "oci1.subnet.aaaa",
                                "timestamp": "2018-01-27T15:41:19.188000+00:00"
                            }
                        ]
            status:
                description: The general health status of the specified backend server as
                             reported by the primary and standby load balancers. Allowed
                             values -
                                - OK
                                - WARNING
                                - CRITICAL
                                - UNKWON
                returned: always
                type: string
                sample: OK
        sample: {
                    "health_check_results": [
                                                {
                                                    "health_check_status": "OK",
                                                    "source_ip_address": "10.1.253.55",
                                                    "subnet_id": "ocid1.subnet.aaaa",
                                                    "timestamp": "2018-01-27T15:41:19.188000+00:00"
                                                }

                                              ],
                    "status": "CRITICAL"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def get_load_balancer_backend_health(lb_client, module):
    result = dict(backend_health="")
    load_balancer_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    backend_name = (
        module.params.get("ip_address") + ":" + str(module.params.get("port"))
    )
    get_logger().info(
        "Retrieving Backend Health for Backend %s of Backend Set %s in Load Balancer %s",
        backend_name,
        backend_set_name,
        load_balancer_id,
    )
    try:
        response = oci_utils.call_with_backoff(
            lb_client.get_backend_health,
            load_balancer_id=load_balancer_id,
            backend_set_name=backend_set_name,
            backend_name=backend_name,
        )
        result["backend_health"] = to_dict(response.data)
    except ServiceError as ex:
        get_logger().error("Unable to get backend health due to: %s", ex.message)
        module.fail_json(msg=ex.message)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_backend_health_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backend_set_name=dict(type="str", required=True),
            ip_address=dict(type="str", required=True),
            port=dict(type=int, required=True),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)

    result = get_load_balancer_backend_health(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
