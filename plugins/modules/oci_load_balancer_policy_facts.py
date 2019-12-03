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
module: oci_load_balancer_policy_facts
short_description: Fetches details of all load balancer policies supported in the OCI Load Balancer Service.
description:
    - Fetches details of all load balancer policies supported in the OCI Load Balancer Service.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the Compartment containing all Load Balancer
        required: true
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
#Fetch details of policy of all load balancer
- name: List all Load Balancer Policy in a Compartment
  oci_load_balancer_policy_facts:
      compartment_id: 'ocid1.compartment..xcds'
"""

RETURN = """
    load_balancer_policies:
        description: Attributes of all Load Balancer Policy
        returned: success
        type: complex
        contains:
          name:
                description: The name of the load balancer policy.
                returned: always
                type: string
                sample: IP_HASH
        sample: [{
                    "name":"IP_HASH"
                },
                {
                    "name":"LEAST_CONNECTIONS"
                }
                ]

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


def list_load_balancer_policies(lb_client, module):
    result = dict(load_balancer_policies="")
    compartment_id = module.params.get("compartment_id")
    get_logger().info(
        "Retrieving Policies for all Load Balancers in Compartment %s", compartment_id
    )
    try:
        result["load_balancer_policies"] = to_dict(
            oci_utils.list_all_resources(
                lb_client.list_policies,
                compartment_id=compartment_id,
                name=module.params["name"],
            )
        )
    except ServiceError as ex:
        get_logger().error(
            "Unable to list all load balancer policies due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_policy_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(compartment_id=dict(type="str", required=True, aliases=["id"]))
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)

    result = list_load_balancer_policies(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
