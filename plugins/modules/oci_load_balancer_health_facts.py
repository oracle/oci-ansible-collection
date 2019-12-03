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
module: oci_load_balancer_health_facts
short_description: Fetch details of a Load Balancer Health
description:
    - Fetch details of a Load Balancer Health.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer
        required: true
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of health of a load balancer
- name: List a specific Load Balancer Health
  oci_load_balancer_health_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    load_balancer_health:
        description: Attributes of the Load Balancer Health
        returned: success
        type: complex
        contains:
          critical_state_backend_set_names:
                description: A list of backend sets that are currently in
                             the CRITICAL health state. The list identifies
                             each backend set by the friendly name which was
                             assigned when it was created .
                returned: always
                type: list
                sample: 10.1.2.3:80
          status:
                description: The overall health status of the load balancer.
                             Allowed values -
                                - OK
                                - WARNING
                                - CRITICAL
                                - UNKWON
                returned: always
                type: string
                sample: OK
          total_backend_set_count:
                description: The total number of backend sets in this load balancer.
                returned: always
                type: integer
                sample: 2
          unknown_state_backend_set_names:
                description: A list of backend sets that are currently in
                             the UNKWON health state. The list identifies
                             each backend set by the friendly name which was
                             assigned when it was created .
                returned: always
                type: list
                sample: 10.1.2.4:80
          warning_state_backend_set_names:
                description: A list of backend sets that are currently in
                             the WARNING health state. The list identifies
                             each backend set by the friendly name which was
                             assigned when it was created .
                returned: always
                type: list
                sample: 10.1.55.2:80
        sample: {
                    "critical_state_backend_set_names":[
                                                "test_backend_one",
                                                "test_backend_two"
                                                ],
                    "status":"CRITICAL",
                    "total_backend_set_count":3,
                    "unknown_state_backend_set_names":[

                    ],
                    "warning_state_backend_set_names":[

                    ]
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


def get_load_balancer_health(lb_client, module):
    result = dict(load_balancer_health="")
    load_balancer_id = module.params.get("load_balancer_id")
    get_logger().info("Retrieving Health for Load Balancer %s", load_balancer_id)
    try:
        response = oci_utils.call_with_backoff(
            lb_client.get_load_balancer_health, load_balancer_id=load_balancer_id
        )
        result["load_balancer_health"] = to_dict(response.data)
    except ServiceError as ex:
        get_logger().error("Unable to get load balancer health due to: %s", ex.message)
        module.fail_json(msg=ex.message)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_health_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(load_balancer_id=dict(type="str", required=True, aliases=["id"]))
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)

    result = get_load_balancer_health(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
