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
module: oci_load_balancer_hostname_facts
short_description: Fetch details of all hostnames of a load balancer
description:
    - Fetch details of all hostnames of a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the hostnames belongs.
        required: true
        aliases: ['id']
    name:
        description: The name of the hostname whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all hostname of a load balancer
- name: List all hostnames
  oci_load_balancer_hostname_facts:
      load_balancer_id: 'ocid1.loadbalancer.xxxxxEXAMPLExxxxx'

#Fetch details of a specific hostname in a load balancer
- name: List a specific hostname
  oci_load_balancer_hostname_facts:
      load_balancer_id: 'ocid1.loadbalancer.xxxxxEXAMPLExxxxx'
      name: 'ansible_hostname'
"""

RETURN = """
    hostnames:
        description: Attributes of the Hostnames fecthed.
        returned: success
        type: complex
        contains:
            hostname:
                description: A virtual hostname
                returned: always
                type: string
                sample: app.example.com
            name:
                description: Name assigned to the Load Balancer Hostname during creation
                returned: always
                type: string
                sample: ansible_hostname
        sample: {"hostname":{
                              "hostname":"app.example.com",
                              "name":"ansible_hostname"
                            }
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


def list_load_balancer_hostnames(lb_client, module):
    result = dict(hostnames="")
    name = module.params.get("name")
    load_balancer_id = module.params["load_balancer_id"]
    try:
        if not name:
            get_logger().debug(
                "Listing all Hostnames under load balancer %s", load_balancer_id
            )
            existing_hostnames = oci_utils.list_all_resources(
                lb_client.list_hostnames, load_balancer_id=load_balancer_id
            )
        else:
            get_logger().debug(
                "Listing Backend Set %s on load balancer %s", name, load_balancer_id
            )
            response = oci_utils.call_with_backoff(
                lb_client.get_hostname, load_balancer_id=load_balancer_id, name=name
            )
            existing_hostnames = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list Hostnames due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["hostnames"] = to_dict(existing_hostnames)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_hostname_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="str", required=False),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_hostnames(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
