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
module: oci_load_balancer_backend_set_facts
short_description: Fetches details of backend set(s) that are associated with a load balancer
description:
    - Fetches details of all backend sets, or a specific backend set, that are associated with a load balancer.
version_added: "2.5"
options:
    name:
        description: Name of the Backend Set
        required: false
    load_balancer_id:
        description: Identifier of the Load Balancer where the Backend Set belongs
        required: true
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch Load Balancer Backend Set
- name: List all backend sets that are associated with a load balancer
  oci_load_balancer_backend_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'


#Fetch specific Load Balancer Backend Set
- name: List a specific Load Balancer Backend Set
  oci_load_balancer_backend_set_facts:
       name: 'ansible_backend_set'
       load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    backend_sets:
        description: Attributes of the  Load Balancer Backend Set.
        returned: success
        type: complex
        contains:
            backends:
                description: A list of configurations related to Backends that are part of the backend set
                returned: always
                type: list
                sample: [
                            {
                                "backup": false,
                                "drain": false,
                                "ip_address": "10.159.34.21",
                                "name": "10.159.34.21:8080",
                                "offline": false,
                                "port": 8080,
                                "weight": 1
                            },
                            {
                                "backup": false,
                                "drain": false,
                                "ip_address": "10.159.34.21",
                                "name": "10.159.34.21:8282",
                                "offline": false,
                                "port": 8282,
                                "weight": 1
                            }
                        ]
            name:
                description: Name assigned to the Load Balancer Backend Set during creation
                returned: always
                type: string
                sample: ansible_backend_set
            health_checker:
                description: Health check policy for a backend set.
                returned: always
                type: dict
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
            policy:
                description: The load balancer policy for the backend set.
                returned: always
                type: string
                sample: LEAST_CONNECTIONS
            session_persistence_configuration:
                description: The configuration details for implementing session persistence
                returned: always
                type: dict
                sample: {
                            "cookie_name": "first_backend_set_cookie",
                            "disable_fallback": true
                        }
            ssl_configuration:
                description: The load balancer's SSL handling configuration details.
                returned: always
                type: dict
                sample: {
                            "certificate_name": "certs1",
                            "verify_depth": 1,
                            "verify_peer_certificate": true
                        }
        sample: [
        {
            "backends": [
                {
                    "backup": false,
                    "drain": false,
                    "ip_address": "10.159.34.21",
                    "name": "10.159.34.21:8080",
                    "offline": false,
                    "port": 8080,
                    "weight": 1
                },
                {
                    "backup": false,
                    "drain": false,
                    "ip_address": "10.159.34.21",
                    "name": "10.159.34.21:8282",
                    "offline": false,
                    "port": 8282,
                    "weight": 1
                }
            ],
            "health_checker": {
                "interval_in_millis": 30000,
                "port": 8080,
                "protocol": "HTTP",
                "response_body_regex": "^(500|40[1348])$",
                "retries": 3,
                "return_code": 500,
                "timeout_in_millis": 6000,
                "url_path": "/healthcheck"
            },
            "name": "backend_set_1",
            "policy": "IP_HASH",
            "session_persistence_configuration": {
                "cookie_name": "first_backend_set_cookie_updated",
                "disable_fallback": true
            },
            "ssl_configuration": {
                "certificate_name": "certs1",
                "verify_depth": 3,
                "verify_peer_certificate": true
            }
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


def list_load_balancer_backend_sets(lb_client, module):
    result = dict(backend_sets="")
    name = module.params.get("name")
    load_balancer_id = module.params["load_balancer_id"]
    try:
        if not name:
            get_logger().debug(
                "Listing all Backend Sets under \
            load balancer %s",
                load_balancer_id,
            )
            existing_backend_sets = oci_utils.list_all_resources(
                lb_client.list_backend_sets, load_balancer_id=load_balancer_id
            )
        else:
            get_logger().debug(
                "Listing Backend Set %s on load balancer %s", name, load_balancer_id
            )
            response = oci_utils.call_with_backoff(
                lb_client.get_backend_set,
                load_balancer_id=load_balancer_id,
                backend_set_name=name,
            )
            existing_backend_sets = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list Backend Sets due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["backend_sets"] = to_dict(existing_backend_sets)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_backend_set_facts")
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
    result = list_load_balancer_backend_sets(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
