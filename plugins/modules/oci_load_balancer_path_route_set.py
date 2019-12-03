#!/usr/bin/python
# Copyright (c) 2018, 2019,  Oracle and/or its affiliates.
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
module: oci_load_balancer_path_route_set
short_description: Create, update and delete a path route set of a load balancer.
description:
    - Create an OCI Load Balancer Path Route Set
    - Update OCI Load Balancers Path Route Set, if present.
    - Delete OCI Load Balancers Path Route Set, if present.
version_added: "2.5"
options:
    load_balancer_id:
        description: Identifier of the Load Balancer. Mandatory for create,delete and update.
        required: true
        aliases: ['id']
    name:
        description: The name for this set of path route rules. It must be unique and it can not be changed.
        required: false
    state:
        description: Create,update or delete Load Balancer Path Route Set. For I(state=present), if it does not exists,
                     it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    path_routes:
        description: The set of path route rules. Mandatory for create and update.
        required: false
        suboptions:
           backend_set_name:
              description: The name of the target backend set for requests where the incoming URI matches the
                           specified path.
              required: true
           path:
              description: The path string to match against the incoming URI path.
                           - Path strings are case-insensitive.
                           - Asterisk (*) wildcards are not supported.
                           - Regular expressions are not supported.
              required: true
           path_match_type:
              description: The type of matching to apply to incoming URIs. This should be a dict/hash that
                            consists of the key [match_type describes how the load balancing service compares
                            a PathRoute object's path string against the incoming URI. The choices for the value
                            are EXACT_MATCH, FORCE_LONGEST_PREFIX_MATCH, PREFIX_MATCH, SUFFIX_MATCH. required - true]
              required: true
    purge_path_routes:
        description: Purge any Path Route in the  Path Route Set named I(name) that is not specified in I(path_routes).
                     This is only applicable in case of updating path route set.If I(purge_path_routes=no), provided
                     path_routes would be appended to existing path_routes.  I(purge_path_routes) and I(delete_path_routes)
                     are mutually exclusive.
        required: false
        default: 'yes'
        type: bool
    delete_path_routes:
        description: Delete any Path Route in the  Path Route Set named I(name) that is specified in I(path_routes).
                     This is only applicable in case of updating path route set.If I(delete_path_routes=yes), path
                     routes provided by I(path_routes) would be deleted from existing path routes, if they are part
                     of existing path route. If they are not part of existing path routes, they will be ignored.
                     I(delete_path_routes) and I(purge_path_routes) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create a backend set named "ansible_path_route_set" in a load balancer
- name: Create Load Balancer Path Route Set
  oci_load_balancer_path_route_set:
    name: "ansible_path_route_set"
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    path_routes:
          - backend_set_name: "ansible_backend_set"
            path: "/admin"
            path_match_type:
                 match_type: 'EXACT_MATCH'
    state: 'present'

# Update Load Balancer Path Route Set
- name: Update Load Balancer Path Route Set
  oci_load_balancer_path_route_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    path_routes:
          - backend_set_name: "ansible_backend_set"
            path: "/admin"
            path_match_type:
                 match_type: 'FORCE_LONGEST_PREFIX_MATCH'
    state: 'present'

# Update Load Balancer Path Route Set by appending a new path route
- name: Update Load Balancer Path Route Set by appending a new path route
  oci_load_balancer_path_route_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    path_routes:
          - backend_set_name: "ansible_backend_set"
            path: "/admin"
            path_match_type:
                 match_type: 'FORCE_LONGEST_PREFIX_MATCH'
    purge_path_routes: False
    state: 'present'

# Update Load Balancer Path Route Set by deleting a path route
- name: Update Load Balancer Path Route Set by deleting a path route
  oci_load_balancer_path_route_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_backend_set"
    path_routes:
          - backend_set_name: "ansible_backend_set"
            path: "/admin"
            path_match_type:
                 match_type: 'FORCE_LONGEST_PREFIX_MATCH'
    delete_path_routes: True
    state: 'present'

# Delete Load Balancer Path Route Set
- name: Delete Load Balancer Path Route Set
  oci_load_balancer_path_route_set:
    load_balancer_id: "ocid1.loadbalancer.oc1.iad.xxxxxEXAMPLExxxxx"
    name: "ansible_path_route_set"
    state: 'absent'
"""

RETURN = """
    path_route_set:
        description: Attributes of the created/updated Load Balancer Path Route Set.
                    For delete, deleted Load Balancer Path Route Set description will
                    be returned.
        returned: success
        type: complex
        contains:
            path_routes:
                description: The set of path route rules.
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
        sample: {
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
"""
from ansible.module_utils.basic import AnsibleModule

from ansible.module_utils.oracle import oci_utils, oci_lb_utils


try:
    from oci.load_balancer.load_balancer_client import LoadBalancerClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.load_balancer.models import (
        CreatePathRouteSetDetails,
        UpdatePathRouteSetDetails,
        PathRoute,
        PathMatchType,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def create_or_update_path_route_set(lb_client, module):
    path_route_set = None
    result = dict(changed=False, path_route_set="")
    load_balancer_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    path_route_set = oci_utils.get_existing_resource(
        lb_client.get_path_route_set,
        module,
        load_balancer_id=load_balancer_id,
        path_route_set_name=name,
    )
    try:
        if path_route_set:
            result = update_path_route_set(
                lb_client, module, load_balancer_id, path_route_set, name
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="path_route_set",
                create_fn=create_path_route_set,
                kwargs_create={"lb_client": lb_client, "module": module},
                list_fn=lb_client.list_path_route_sets,
                kwargs_list={"load_balancer_id": module.params.get("load_balancer_id")},
                module=module,
                model=CreatePathRouteSetDetails(),
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update path route set due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update path route set due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_path_route_set(lb_client, module):
    path_route_set_input_details = dict(
        {"path_routes": module.params.get("path_routes", None)}
    )
    name = module.params.get("name")
    lb_id = module.params.get("load_balancer_id")
    get_logger().info("Creating path route set %s in the load balancer %s", name, lb_id)
    path_route_set_details = oci_lb_utils.create_path_route_sets(
        dict({name: path_route_set_input_details})
    ).get(name)
    create_path_route_set_details = CreatePathRouteSetDetails()
    create_path_route_set_details.name = name
    create_path_route_set_details.path_routes = path_route_set_details.path_routes
    result = oci_lb_utils.create_or_update_lb_resources_and_wait(
        resource_type="path_route_set",
        function=lb_client.create_path_route_set,
        kwargs_function={
            "create_path_route_set_details": create_path_route_set_details,
            "load_balancer_id": lb_id,
        },
        lb_client=lb_client,
        get_fn=lb_client.get_path_route_set,
        kwargs_get={"load_balancer_id": lb_id, "path_route_set_name": name},
        module=module,
    )
    get_logger().info(
        "Successfullt created path route set %s in the load balancer %s", name, lb_id
    )

    return result


def update_path_route_set(lb_client, module, lb_id, path_route_set, name):
    result = dict(path_route_set=to_dict(path_route_set), changed=False)
    update_path_route_set_details = UpdatePathRouteSetDetails()
    purge_path_routes = module.params.get("purge_path_routes")
    delete_path_routes = module.params.get("delete_path_routes")
    input_path_routes = oci_lb_utils.create_path_routes(
        module.params.get("path_routes", None)
    )
    existing_path_routes = oci_utils.get_hashed_object_list(
        PathRoute, path_route_set.path_routes, attributes_class_type=[PathMatchType]
    )
    get_logger().info("Updating path route set %s in the load balancer %s", name, lb_id)
    changed = False
    if input_path_routes is not None:
        path_routes, changed = oci_utils.check_and_return_component_list_difference(
            input_path_routes,
            existing_path_routes,
            purge_path_routes,
            delete_path_routes,
        )
    if changed:
        update_path_route_set_details.path_routes = path_routes
    else:
        update_path_route_set_details.path_routes = existing_path_routes

    if changed:
        result = oci_lb_utils.create_or_update_lb_resources_and_wait(
            resource_type="path_route_set",
            function=lb_client.update_path_route_set,
            kwargs_function={
                "update_path_route_set_details": update_path_route_set_details,
                "load_balancer_id": lb_id,
                "path_route_set_name": name,
            },
            lb_client=lb_client,
            get_fn=lb_client.get_path_route_set,
            kwargs_get={"load_balancer_id": lb_id, "path_route_set_name": name},
            module=module,
        )
        get_logger().info(
            "Successfully updated path route set %s in the load balancer %s",
            name,
            lb_id,
        )
    else:
        get_logger().info(
            "No update to the path route set %s in the load balancer %s as no attribute changed",
            name,
            lb_id,
        )

    return result


def delete_path_route_set(lb_client, module):
    lb_id = module.params.get("load_balancer_id")
    name = module.params.get("name")
    get_logger().info(
        "Deleting path route set %s from the load balancer %s", name, lb_id
    )
    result = oci_lb_utils.delete_lb_resources_and_wait(
        resource_type="path_route_set",
        function=lb_client.delete_path_route_set,
        kwargs_function={"path_route_set_name": name, "load_balancer_id": lb_id},
        lb_client=lb_client,
        get_fn=lb_client.get_path_route_set,
        kwargs_get={"load_balancer_id": lb_id, "path_route_set_name": name},
        module=module,
    )
    get_logger().info(
        "Successfully deleted path route set %s from the load balancer %s", name, lb_id
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_load_balancer_path_route_set")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            load_balancer_id=dict(type="str", required=True, aliases=["id"]),
            path_routes=dict(type="list", required=False),
            purge_path_routes=dict(type="bool", required=False, default=True),
            delete_path_routes=dict(type="bool", required=False, default=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        required_if=[["state", "present", ["path_routes"]]],
        mutually_exclusive=[["purge_path_routes", "delete_path_routes"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    lb_client = oci_utils.create_service_client(module, LoadBalancerClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_path_route_set(lb_client, module)
    elif state == "absent":
        result = delete_path_route_set(lb_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
