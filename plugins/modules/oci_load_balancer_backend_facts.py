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
module: oci_load_balancer_backend_facts
short_description: Fetch details of all Backends in a load balancer backend set of a load balancer
description:
    - Fetch details of all Backends in a load balancer backend set of a load balancer.
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
        required: false
    port:
        description: The communication port for the backend server.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
#Fetch details of all load balancer backends of a load balancer
- name: List all Load Balancer Backends
  oci_load_balancer_backend_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      backend_set_name: 'backend1'

#Fetch details of a specific load balancer backend in a load balancer
- name: List a specific Load Balancer Backend
  oci_load_balancer_backend_facts:
      load_balancer_id: 'ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx'
      backend_set_name: 'backend1'
      ip_address: '10.159.121.55'
      port: '8181'
"""

RETURN = """
    backends:
        description: Attributes of the Load Balancer Backend.
        returned: success
        type: complex
        contains:
            name:
                description: Name of the Load Balancer Backend
                returned: always
                type: string
                sample: 10.45.121.59:8080
            ip_address:
                description: Ip Address of the Load Balancer Backend
                returned: always
                type: string
                sample: 10.45.121.69
            port:
                description: Port of the Load Balancer Backend
                returned: always
                type: string
                sample: 8080
            backup:
                description: The backup state of the Load Balancer Backend
                returned: always
                type: boolean
                sample: False
            drain:
                description: The drain state of the Load Balancer Backend
                returned: always
                type: boolean
                sample: False
            offline:
                description: The offline state of the Load Balancer Backend
                returned: always
                type: boolean
                sample: False
            weight:
                description: The weight of the Load Balancer Backend
                returned: always
                type: integer
                sample: 1
        sample: [{
                    "backup":false,
                    "drain":false,
                    "ip_address":"10.159.34.21",
                    "name":"10.159.34.21:8181",
                    "offline":false,
                    "port":8181,
                    "weight":3
                },
                {
                    "backup":false,
                    "drain":false,
                    "ip_address":"10.159.34.55",
                    "name":"10.159.34.21:1234",
                    "offline":false,
                    "port":1234,
                    "weight":1
                }]
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


def list_load_balancer_backends(lb_client, module):
    result = dict(backends="")
    load_balancer_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    ip_address = module.params.get("ip_address", None)
    port = module.params.get("port", None)
    try:
        if ip_address and port:
            backend_name = ip_address + ":" + str(port)
            get_logger().info(
                "Listing all attributes of  backend %s for backendset %s \
                               in load balancer %s",
                backend_name,
                backend_set_name,
                load_balancer_id,
            )
            response = lb_client.get_backend(
                load_balancer_id, backend_set_name, backend_name
            )
            backends = [response.data]
        else:
            get_logger().info(
                "Listing all attributes of  all backends of backendset %s \
                               in load balancer %s",
                backend_set_name,
                load_balancer_id,
            )
            backends = oci_utils.list_all_resources(
                lb_client.list_backends,
                load_balancer_id=load_balancer_id,
                backend_set_name=backend_set_name,
            )
    except ServiceError as ex:
        get_logger().error("Unable to list backends due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    result["backends"] = to_dict(backends)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_backend_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backend_set_name=dict(type="str", required=True),
            ip_address=dict(type="str", required=False),
            port=dict(type=int, required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    result = list_load_balancer_backends(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
