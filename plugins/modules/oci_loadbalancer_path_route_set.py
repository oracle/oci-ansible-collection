#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_loadbalancer_path_route_set
short_description: Manage a PathRouteSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PathRouteSet resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a path route set to a load balancer. For more information, see
      L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name for this set of path route rules. It must be unique and it cannot be changed. Avoid entering
              confidential information.
            - "Example: `example_path_route_set`"
        type: str
        required: true
    path_routes:
        description:
            - The set of path route rules.
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: list
        suboptions:
            path:
                description:
                    - The path string to match against the incoming URI path.
                    - "*  Path strings are case-insensitive."
                    - "*  Asterisk (*) wildcards are not supported."
                    - "*  Regular expressions are not supported."
                    - "Example: `/example/video/123`"
                type: str
                required: true
            path_match_type:
                description:
                    - The type of matching to apply to incoming URIs.
                type: dict
                required: true
                suboptions:
                    match_type:
                        description:
                            - Specifies how the load balancing service compares a L(PathRoute,https://docs.cloud.oracle.com/en-
                              us/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute)
                              object's `path` string against the incoming URI.
                            - "*  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path."
                            - "*  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
                                 portion of the incoming URI path."
                            - "*  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path."
                            - "*  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path."
                            - For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
                              L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
                        type: str
                        choices:
                            - "EXACT_MATCH"
                            - "FORCE_LONGEST_PREFIX_MATCH"
                            - "PREFIX_MATCH"
                            - "SUFFIX_MATCH"
                        required: true
            backend_set_name:
                description:
                    - The name of the target backend set for requests where the incoming URI matches the specified path.
                    - "Example: `example_backend_set`"
                type: str
                required: true
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to add the path route set to.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the PathRouteSet.
            - Use I(state=present) to create or update a PathRouteSet.
            - Use I(state=absent) to delete a PathRouteSet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create path_route_set
  oci_loadbalancer_path_route_set:
    name: "example_path_route_set"
    path_routes:
    - path: "/example/video/123"
      path_match_type:
        match_type: "EXACT_MATCH"
      backend_set_name: "example_backend_set"
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update path_route_set
  oci_loadbalancer_path_route_set:
    path_routes:
    - path: "/example/video/123"
      path_match_type:
        match_type: "EXACT_MATCH"
      backend_set_name: "example_backend_set"
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete path_route_set
  oci_loadbalancer_path_route_set:
    name: example_path_route_set
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
path_route_set:
    description:
        - Details of the PathRouteSet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name for this set of path route rules. Avoid entering confidential information.
                - "Example: `example_path_route_set`"
            returned: on success
            type: string
            sample: example_path_route_set
        path_routes:
            description:
                - The set of path route rules.
            returned: on success
            type: complex
            contains:
                path:
                    description:
                        - The path string to match against the incoming URI path.
                        - "*  Path strings are case-insensitive."
                        - "*  Asterisk (*) wildcards are not supported."
                        - "*  Regular expressions are not supported."
                        - "Example: `/example/video/123`"
                    returned: on success
                    type: string
                    sample: /example/video/123
                path_match_type:
                    description:
                        - The type of matching to apply to incoming URIs.
                    returned: on success
                    type: complex
                    contains:
                        match_type:
                            description:
                                - Specifies how the load balancing service compares a L(PathRoute,https://docs.cloud.oracle.com/en-
                                  us/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute)
                                  object's `path` string against the incoming URI.
                                - "*  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path."
                                - "*  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
                                     portion of the incoming URI path."
                                - "*  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path."
                                - "*  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path."
                                - For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
                                  L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
                            returned: on success
                            type: string
                            sample: EXACT_MATCH
                backend_set_name:
                    description:
                        - The name of the target backend set for requests where the incoming URI matches the specified path.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: string
                    sample: example_backend_set
    sample: {
        "name": "example_path_route_set",
        "path_routes": [{
            "path": "/example/video/123",
            "path_match_type": {
                "match_type": "EXACT_MATCH"
            },
            "backend_set_name": "example_backend_set"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreatePathRouteSetDetails
    from oci.load_balancer.models import UpdatePathRouteSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PathRouteSetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_path_route_set

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_route_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            path_route_set_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "load_balancer_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_path_route_sets, **kwargs
        )

    def get_create_model_class(self):
        return CreatePathRouteSetDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_path_route_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_path_route_set_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePathRouteSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_path_route_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_path_route_set_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                path_route_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_path_route_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                path_route_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


PathRouteSetHelperCustom = get_custom_class("PathRouteSetHelperCustom")


class ResourceHelper(PathRouteSetHelperCustom, PathRouteSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str", required=True),
            path_routes=dict(
                type="list",
                elements="dict",
                options=dict(
                    path=dict(type="str", required=True),
                    path_match_type=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            match_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "EXACT_MATCH",
                                    "FORCE_LONGEST_PREFIX_MATCH",
                                    "PREFIX_MATCH",
                                    "SUFFIX_MATCH",
                                ],
                            )
                        ),
                    ),
                    backend_set_name=dict(type="str", required=True),
                ),
            ),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="path_route_set",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
