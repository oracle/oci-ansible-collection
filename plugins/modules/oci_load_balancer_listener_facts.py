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
module: oci_load_balancer_listener_facts
short_description: Fetch details of all listeners of a load balancer
description:
    - Fetch details of all listeners of a load balancer.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer to which the listeners belongs.
        required: true
        aliases: ['id']
    name:
        description: The name of the listener whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all listener of a load balancer
- name: List all Listeners
  oci_load_balancer_listener_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'

#Fetch details of a specific listener in a load balancer
- name: List a specific Listener
  oci_load_balancer_listener_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      name: 'ansible_listener'
"""

RETURN = """
    listeners:
        description: Attributes of Listener.
        returned: success
        type: complex
        contains:
            name:
                description: Name of the Listener
                returned: always
                type: string
                sample: ansible_listener
            default_backend_set_name:
                description: The name of the associated backend set
                returned: always
                type: string
                sample: ansible_backend_set
            port:
                description: The communication port for the listener.
                returned: always
                type: string
                sample: 80
            protocol:
                description: The protocol on which the listener accepts connection requests.
                returned: always
                type: string
                sample: HTTP
            ssl_configuration:
                description: The load balancer SSL handling configuration details
                returned: always
                type: dict
                sample: {
                            "certificate_name": "certs1",
                            "verify_depth": 1,
                            "verify_peer_certificate": true
                        }
            connection_configuration:
                description: Configuration details for the connection between the client and backend servers.
                returned: always
                type: dict
                sample: {
                            "idle_timeout": 1200
                        }
            hostname_names:
                description: An array of hostname resource names.
                returned: always
                type: list
                sample: [
                            "hostname_001"
                        ]
            path_route_set_name:
                description: The name of the set of path-based routing rules, PathRouteSet, applied to this listener's traffic.
                returned: always
                type: string
                sample: "path_route_set_001"
        sample: [{
                    "default_backend_set_name": "ansible_backend",
                    "name": "ansible_listener",
                    "port": 87,
                    "protocol": "HTTP",
                    "hostname_names": [
                                        "hostname_001"
                                      ],
                    "path_route_set_name": "path_route_set_001",
                    "ssl_configuration": {
                        "certificate_name": "certs1",
                        "verify_depth": 1,
                        "verify_peer_certificate": true
                    },
                    "connection_configuration": {
                        "idle_timeout": 1200
                    }
               }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_load_balancer_listeners(lb_client, module):
    result = dict(listeners="")
    load_balancer_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    try:
        existing_load_balancer = to_dict(
            oci_lb_utils.get_existing_load_balancer(lb_client, module, load_balancer_id)
        )
        if name:
            get_logger().info(
                "Listing all attributes of  listener %s in load balancer %s",
                name,
                load_balancer_id,
            )
            if name in existing_load_balancer.get("listeners"):
                listeners = [existing_load_balancer["listeners"][name]]
            else:
                listeners = []
        else:
            get_logger().info(
                "Listing all attributes of  all listeners in load balancer %s",
                load_balancer_id,
            )
            listeners_list = []
            for key, value in existing_load_balancer["listeners"].items():
                listeners_list.append(value)
            listeners = listeners_list
    except ServiceError as ex:
        get_logger().error("Unable to list listeners due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    result["listeners"] = listeners
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_listener_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            name=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_listeners(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
