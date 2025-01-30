#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_loadbalancer_path_route_set_facts
short_description: Fetches details about one or multiple PathRouteSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PathRouteSet resources in Oracle Cloud Infrastructure
    - Lists all path route sets associated with the specified load balancer.
    - If I(path_route_set_name) is specified, the details of a single PathRouteSet will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    path_route_set_name:
        description:
            - The name of the path route set to retrieve.
            - "Example: `example_path_route_set`"
            - Required to get a specific path_route_set.
        type: str
        aliases: ["name"]
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific path_route_set
  oci_loadbalancer_path_route_set_facts:
    # required
    path_route_set_name: path_route_set_name_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: List path_route_sets
  oci_loadbalancer_path_route_set_facts:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
path_route_sets:
    description:
        - List of PathRouteSet resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name for this set of path route rules. Avoid entering confidential information.
                - "Example: `example_path_route_set`"
            returned: on success
            type: str
            sample: name_example
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
                    type: str
                    sample: path_example
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
                            type: str
                            sample: EXACT_MATCH
                backend_set_name:
                    description:
                        - The name of the target backend set for requests where the incoming URI matches the specified path.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: str
                    sample: backend_set_name_example
    sample: [{
        "name": "name_example",
        "path_routes": [{
            "path": "path_example",
            "path_match_type": {
                "match_type": "EXACT_MATCH"
            },
            "backend_set_name": "backend_set_name_example"
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PathRouteSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "path_route_set_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_path_route_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            path_route_set_name=self.module.params.get("path_route_set_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_path_route_sets,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


PathRouteSetFactsHelperCustom = get_custom_class("PathRouteSetFactsHelperCustom")


class ResourceFactsHelper(PathRouteSetFactsHelperCustom, PathRouteSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            path_route_set_name=dict(aliases=["name"], type="str"),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="path_route_set",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(path_route_sets=result)


if __name__ == "__main__":
    main()
