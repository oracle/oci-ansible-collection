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
module: oci_load_balancer_path_route_set_facts
short_description: Fetches details of path route set(s) that are associated with a load balancer
description:
    - Fetches details of all path route sets, or a specific path route set, that are associated with a load balancer.
version_added: "2.5"
options:
    path_route_set_name:
        description: Name of the Path Route Set
        required: false
        aliases: ['name']
    load_balancer_id:
        description: Identifier of the Load Balancer where the Path Route Set belongs
        required: true
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch Load Balancer Path Route Set
- name: List all path route sets that are associated with a load balancer
  oci_load_balancer_path_route_set_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'


#Fetch specific Load Balancer Path Route Set
- name: List a specific Load Balancer Path Route Set
  oci_load_balancer_path_route_set_facts:
       name: 'ansible_path_route_set'
       load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    path_route_sets:
        description: Attributes of the  Load Balancer Path Route Set.
        returned: success
        type: complex
        contains:
            path_routes:
                description: A list of all path route sets associated with the specified load balancer.
                returned: always
                type: list
                sample: [
                          {
                            "backend_set_name":"ansible_backend_set",
                            "path":"/admin",
                            "path_match_type":{
                                    "match_type":"EXACT_MATCH"
                             }
                           }
                        ]
            name:
                description: Name assigned to the Load Balancer Path Route Set during creation
                returned: always
                type: string
                sample: ansible_path_route_set
        sample: [
                 {
                  "name":"ansible_path_route_set",
                  "path_routes":[
                                 {
                                   "backend_set_name":"ansible_backend_set",
                                   "path":"/admin",
                                   "path_match_type":{
                                          "match_type":"EXACT_MATCH"
                                    }
                                  }
                                ]
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


def list_load_balancer_path_route_sets(lb_client, module):
    result = dict(path_route_sets="")
    name = module.params.get("path_route_set_name")
    load_balancer_id = module.params["load_balancer_id"]
    try:
        if not name:
            get_logger().debug(
                "Listing all Path Route Sets under load balancer %s", load_balancer_id
            )
            existing_path_route_sets = oci_utils.list_all_resources(
                lb_client.list_path_route_sets, load_balancer_id=load_balancer_id
            )
        else:
            get_logger().debug(
                "Listing Path Route Set %s on load balancer %s", name, load_balancer_id
            )
            response = oci_utils.call_with_backoff(
                lb_client.get_path_route_set,
                load_balancer_id=load_balancer_id,
                path_route_set_name=name,
            )
            existing_path_route_sets = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list Path Route Sets due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["path_route_sets"] = to_dict(existing_path_route_sets)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_path_route_set_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            path_route_set_name=dict(type="str", required=False, aliases=["name"]),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_path_route_sets(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
