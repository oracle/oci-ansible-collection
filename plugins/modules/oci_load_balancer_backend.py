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
module: oci_load_balancer_backend
short_description: Add, modify and remove a backend from a load balancer in
                   OCI Load Balancing Service
description:
    - Add a Backend server to OCI Load Balancer
    - Update a Backend server in a Load Balancer, if present, with any changed attribute
    - Delete a Backend server from OCI Load Balancer Backends, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer in which the Backend belongs.
        required: true
        aliases: ['id']
    backend_set_name:
        description: The name of the backend set to add the backend server to.
        required: true
    ip_address:
        description: The IP address of the backend server.
        required: true
    port:
        description: The communication port for the backend server.
        required: true
    backup:
        description: Whether the load balancer should treat this server as a backup unit. If true, the load balancer
                     forwards no ingress traffic to this backend server unless all other backend servers not marked as
                     "backup" fail the health check policy.
        required: false
        default: False
        type: bool
    drain:
        description: Whether the load balancer should drain this server. Servers marked "drain" receive no new incoming
                     traffic.
        required: false
        default: False
        type: bool
    offline:
        description: Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                     traffic.
        required: false
        default: False
        type: bool
    state:
        description: Create,update or delete Load Balancer Backend. For I(state=present),
                     if it does not exists, it gets added. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    weight:
        description: The load balancing policy weight assigned to the server. Backend
                     servers with a higher weight receive a larger proportion of incoming
                     traffic. For example, a server weighted 3 receives 3 times the number
                     of new connections as a server weighted 1.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [oracle, oracle_wait_options]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Load Balancer Backend
- name: Create Load Balancer Backend
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    backup: False
    drain: False
    offline: False
    weight: 3
    state: 'present'
# Update a Backend server by enabling drain
- name: Drain a backend server by updating the Backend and setting the 'drain' option
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    drain: True
    state: 'present'
# Update a Backend server to make it offline
- name: Make a backend server offline
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    offline: True
    state: 'present'
# Update a Backend server to backup state
- name: Change a backend server state as backup
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    backup: True
    state: 'present'
# Update Load Balancer Backend
- name: Update Load Balancer Backend
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    backup: True
    state: 'present'
# Delete Load Balancer Backend
- name: Update Load Balancer Backend
  oci_load_balancer_backend:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    backend_set_name: "backend1"
    ip_address: "10.50.121.69"
    port: 8080
    state: 'absent'
"""
RETURN = """
    backend:
        description: Attributes of the created/updated Load Balancer Backend.
                    For delete, deleted Load Balancer Backend description will
                    be returned.
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
        sample: {
                    "backup": false,
                    "drain": false,
                    "ip_address": "10.159.34.21",
                    "name":"10.159.34.21:8181",
                    "offline":false,
                    "port":8181,
                    "weight":3
                }
"""
from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.oracle import oci_utils, oci_lb_utils

try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import UpdateBackendDetails, CreateBackendDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_backend(lb_client, module):

    backend = None
    result = dict(changed=False, backend="")
    lb_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    backend = oci_utils.get_existing_resource(
        lb_client.get_backend,
        module,
        load_balancer_id=lb_id,
        backend_set_name=backend_set_name,
        backend_name=oci_lb_utils.get_backend_name(module),
    )
    try:
        if backend:
            result = update_backend(lb_client, module, backend, lb_id, backend_set_name)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="backend",
                create_fn=create_backend,
                kwargs_create={
                    "lb_client": lb_client,
                    "module": module,
                    "lb_id": lb_id,
                    "backend_set_name": backend_set_name,
                },
                list_fn=lb_client.list_backends,
                kwargs_list={
                    "load_balancer_id": lb_id,
                    "backend_set_name": backend_set_name,
                },
                module=module,
                model=CreateBackendDetails(),
            )
    except ServiceError as ex:
        get_logger().error("Unable to create/update backend due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update backend due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_backend(lb_client, module, lb_id, backend_set_name):
    backend_name = oci_lb_utils.get_backend_name(module)
    create_backend_details = CreateBackendDetails()
    for attribute in create_backend_details.attribute_map:
        create_backend_details.__setattr__(
            attribute, module.params.get(attribute, None)
        )
    get_logger().info(
        "Creating backend for backendset %s with parameters %s",
        backend_set_name,
        str(create_backend_details),
    )
    get_logger().debug(
        "backend ip_address: %s and port: %s",
        module.params["ip_address"],
        str(module.params["port"]),
    )
    result = oci_lb_utils.create_or_update_lb_resources_and_wait(
        resource_type="backend",
        function=lb_client.create_backend,
        kwargs_function={
            "create_backend_details": create_backend_details,
            "load_balancer_id": lb_id,
            "backend_set_name": backend_set_name,
        },
        lb_client=lb_client,
        get_fn=lb_client.get_backend,
        kwargs_get={
            "load_balancer_id": lb_id,
            "backend_set_name": backend_set_name,
            "backend_name": backend_name,
        },
        module=module,
    )
    get_logger().info(
        "Successfully created backend for backendset %s with parameters %s",
        backend_set_name,
        str(create_backend_details),
    )
    return result


def update_backend(lb_client, module, backend, lb_id, backend_set_name):
    changed = False
    result = dict(changed=changed, backend=to_dict(backend))
    backend_name = oci_lb_utils.get_backend_name(module)
    get_logger().info(
        "Updating backend %s for backendset %s in load balancer %s",
        backend_name,
        backend_set_name,
        lb_id,
    )
    update_backend_details = UpdateBackendDetails()
    for attribute in update_backend_details.attribute_map:
        changed = oci_utils.check_and_update_attributes(
            update_backend_details,
            attribute,
            module.params.get(attribute, None),
            getattr(backend, attribute),
            changed,
        )
    get_logger().debug(
        "Existing backend property values: %s, input property values: %s",
        backend,
        update_backend_details,
    )
    if changed:
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="backend",
            function=lb_client.update_backend,
            kwargs_function={
                "update_backend_details": update_backend_details,
                "load_balancer_id": lb_id,
                "backend_set_name": backend_set_name,
                "backend_name": backend_name,
            },
            lb_client=lb_client,
            get_fn=lb_client.get_backend,
            kwargs_get={
                "load_balancer_id": lb_id,
                "backend_set_name": backend_set_name,
                "backend_name": backend_name,
            },
            module=module,
        )
        get_logger().info(
            "Successfully updated backend %s for backendset %s in load balancer %s",
            backend_name,
            backend_set_name,
            lb_id,
        )
    else:
        get_logger().info(
            "No update to the backend %s for backendset %s in load balancer %s as no "
            + "attribute changed",
            backend_name,
            backend_set_name,
            lb_id,
        )

    return result


def delete_backend(lb_client, module):
    lb_id = module.params.get("load_balancer_id")
    backend_set_name = module.params.get("backend_set_name")
    backend_name = oci_lb_utils.get_backend_name(module)
    get_logger().info(
        "Deleting backend %s for backendset %s in load balancer %s",
        backend_name,
        backend_set_name,
        lb_id,
    )
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="backend",
        function=lb_client.delete_backend,
        kwargs_function={
            "backend_set_name": backend_set_name,
            "load_balancer_id": lb_id,
            "backend_name": backend_name,
        },
        lb_client=lb_client,
        get_fn=lb_client.get_backend,
        kwargs_get={
            "load_balancer_id": lb_id,
            "backend_set_name": backend_set_name,
            "backend_name": backend_name,
        },
        module=module,
    )
    get_logger().info(
        "Successfully Deleted backend %s for backendset %s in load balancer %s",
        backend_name,
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
    logger = oci_utils.get_logger("oci_load_balancer_backend")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            backend_set_name=dict(type="str", required=True),
            backup=dict(type="bool", required=False),
            ip_address=dict(type="str", required=True),
            drain=dict(type="bool", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            offline=dict(type="bool", required=False),
            port=dict(type="int", required=True),
            weight=dict(type="int", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_backend(lb_client, module)
    elif state == "absent":
        result = delete_backend(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
