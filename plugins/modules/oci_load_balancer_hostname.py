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
module: oci_load_balancer_hostname
short_description: Create, update and delete a hostname resource in the specified load balancer.
description:
    - Create an OCI Load Balancer Hostname
    - Update OCI Load Balancers Hostname, if present.
    - Delete OCI Load Balancers Hostname, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer. Mandatory for create,delete and update.
        required: true
        aliases: ['id']
    name:
        description: A friendly name for the hostname resource. It must be unique and it cannot be
                     changed. Avoid entering confidential information.Mandatory for create,update and delete.
        required: true
    hostname:
        description: A virtual hostname. Mandatory for create and update.
        required: false
    state:
        description: Create,update or delete Load Balancer Hostname. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [oracle, oracle_wait_options]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create a hostname named "ansible_hostname" in a load balancer
- name: Create Load Balancer Hostname
  oci_load_balancer_hostname:
    name: "ansible_hostname"
    load_balancer_id: "ocid1.loadbalancer.xxxxxEXAMPLExxxxx"
    hostname: "app.example.com"
    state: 'present'

# Update Load Balancer Hostname
- name: Update Load Balancer Hostname
  oci_load_balancer_backend_set:
    load_balancer_id: "ocid1.loadbalancer.xxxxxEXAMPLExxxxx"
    name: "ansible_hostname"
    hostname: "app.production.com"

# Deleted Load Balancer Hostname
- name: Delete Load Balancer Hostname
  oci_load_balancer_hostname:
    load_balancer_id: "ocid1.loadbalancer.xxxxxEXAMPLExxxxx"
    name: "ansible_hostname"
    state: 'absent'
"""

RETURN = """
    hostname:
        description: Attributes of the created/updated Load Balancer Hostname.
                    For delete, deleted Load Balancer Hostname description will
                    be returned.
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
        sample: [{
                   "hostname":"app.example.com",
                   "name":"ansible_hostname"
                 },
                 {
                   "hostname":"app.production.com",
                   "name":"ansible_hostname_002"
                 }
                ]
"""
from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.oracle import oci_utils, oci_lb_utils


try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.util import to_dict
    from oci.load_balancer.models import CreateHostnameDetails, UpdateHostnameDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_hostname(lb_client, module):
    hostname = None
    result = dict(changed=False, hostname="")
    load_balancer_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    hostname = oci_utils.get_existing_resource(
        lb_client.get_hostname, module, load_balancer_id=load_balancer_id, name=name
    )
    if hostname:
        result = update_hostname(lb_client, module, load_balancer_id, hostname, name)
    else:
        result = oci_utils.check_and_create_resource(
            resource_type="hostname",
            create_fn=create_hostname,
            kwargs_create={"lb_client": lb_client, "module": module},
            list_fn=lb_client.list_hostnames,
            kwargs_list={"load_balancer_id": module.params.get("load_balancer_id")},
            module=module,
            model=CreateHostnameDetails(),
        )

    return result


def create_hostname(lb_client, module):
    hostname_input_details = dict(
        {
            "name": module.params.get("name", None),
            "hostname": module.params.get("hostname"),
        }
    )
    name = module.params.get("name")
    lb_id = module.params.get("load_balancer_id")
    get_logger().info("Creating hostname %s in the load balancer %s", name, lb_id)
    hostname_details = oci_lb_utils.create_hostnames(
        dict({name: hostname_input_details})
    ).get(name)
    create_hostname_details = CreateHostnameDetails()
    for attribute in create_hostname_details.attribute_map:
        create_hostname_details.__setattr__(
            attribute, getattr(hostname_details, attribute)
        )
    result = oci_lb_utils.create_or_update_lb_resources_and_wait(
        resource_type="hostname",
        function=lb_client.create_hostname,
        kwargs_function={
            "create_hostname_details": create_hostname_details,
            "load_balancer_id": lb_id,
        },
        lb_client=lb_client,
        get_fn=lb_client.get_hostname,
        kwargs_get={"load_balancer_id": lb_id, "name": name},
        module=module,
    )
    get_logger().info(
        "Successfully created hostname %s in the load balancer %s", name, lb_id
    )

    return result


def update_hostname(lb_client, module, lb_id, hostname, name):
    result = dict(hostname=to_dict(hostname), changed=False)
    update_hostname_details = UpdateHostnameDetails()
    get_logger().info("Updating hostname %s in the load balancer %s", name, lb_id)
    changed = False
    changed = oci_utils.check_and_update_attributes(
        update_hostname_details,
        "hostname",
        module.params.get("hostname"),
        hostname.hostname,
        changed,
    )
    if changed:
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="hostname",
            function=lb_client.update_hostname,
            kwargs_function={
                "update_hostname_details": update_hostname_details,
                "load_balancer_id": lb_id,
                "name": name,
            },
            lb_client=lb_client,
            get_fn=lb_client.get_hostname,
            kwargs_get={"load_balancer_id": lb_id, "name": name},
            module=module,
        )
        get_logger().info(
            "Successfully updated hostname %s  in load balancer %s", hostname, lb_id
        )
    else:
        get_logger().info(
            "No update to the hostname %s  in load balancer %s as no attribute changed",
            hostname,
            lb_id,
        )

    return result


def delete_hostname(lb_client, module):
    lb_id = module.params.get("load_balancer_id", None)
    name = module.params.get("name", None)
    get_logger().info("Deleting hostname %s from the load balancer %s", name, lb_id)
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="hostname",
        function=lb_client.delete_hostname,
        kwargs_function={"name": name, "load_balancer_id": lb_id},
        lb_client=lb_client,
        get_fn=lb_client.get_hostname,
        kwargs_get={"load_balancer_id": lb_id, "name": name},
        module=module,
    )
    get_logger().info(
        "Successfully deleted hostname %s from the load balancer %s", name, lb_id
    )
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_hostname")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            hostname=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_hostname(lb_client, module)
    elif state == "absent":
        result = delete_hostname(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
