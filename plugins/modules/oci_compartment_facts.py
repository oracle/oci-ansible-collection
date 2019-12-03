#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_compartment_facts
short_description: Retrieve details of a compartment or all the subcompartments in the specified compartment in OCI
description:
    - This module allows the user to retrieve information of a specific compartment or all the subcompartments in a
      specified compartment in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: OCID of a compartment.
                     Use OCID of a root compartment with I(depth) to get details of all the subcompartments which
                     are upto I(depth) deep in the root compartment.
                     Use OCID of a root compartment with I(fetch_subcompartments=False) to retrieve information of only
                     the root compartment.
                     Use OCID of a non-root compartment to get details of only the compartment.
                     Use OCID of a non-root compartment with I(fetch_subcompartments=True) and I(depth) to retrieve
                     information of all the subcompartments which are upto I(depth) deep in the non-root compartment.
        required: true
    fetch_subcompartments:
        description: Whether to fetch information of subcompartments under I(compartment_id). When I(compartment_id) is
                     set to OCID of a root compartment, I(fetch_subcompartments) defaults to True. When
                     I(compartment_id) is set to OCID of a non-root compartment, I(fetch_subcompartments) defaults to
                     False.
        required: false
        type: bool
    depth:
        description: Specify the hierarchy level upto which subcompartments under I(compartment_id) should be retrieved.
                     Use this option with I(fetch_subcompartments=True) to fetch details of all the subcompartments
                     which are upto I(depth) deep under I(compartment_id).
        required: false
        default: 1
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get details of all the first-level child compartments of a root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'

- name: Get details of a root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    fetch_subcompartments: False

- name: Get details of all the compartments in a tenancy
  oci_compartment_facts:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    depth: 100

- name: Get details of all first-level child compartments of a non-root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    fetch_subcompartments: True

- name: Get details of a non-root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get details of all the subcompartments under a non-root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    fetch_subcompartments: True
    depth: 100

- name: Filter subcompartments by name under a root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
    name: test_compartment

- name: Filter subcompartments by name under a non-root compartment
  oci_compartment_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    fetch_subcompartments: True
    name: test_compartment
"""

RETURN = """
compartments:
    description: List of compartment details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the tenancy containing the compartment
            returned: always
            type: string
            sample: 'ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx'
        id:
            description: The OCID of the compartment
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        description:
            description: The description assigned to the compartment
            returned: always
            type: string
            sample: Compartment for Project-A
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState
            returned: always
            type: string
            sample: null
        lifecycle_state:
            description: The compartment's current state
            returned: always
            type: string
            sample: ACTIVE
        name:
            description: The name assigned to the compartment
            returned: always
            type: string
            sample: "Project-A"
        time_created:
            description: Date and time the compartment was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: "2017-02-01T03:20:22.160000+00:00"
    sample: [{"compartment_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
            "description": "Compartment for Project-Ansible",
            "id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "name": "Project-Ansible",
            "time_created": "2017-02-01T03:20:22.160000+00:00"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
    from oci.exceptions import ServiceError
except ImportError:
    HAS_OCI_PY_SDK = False

# OCI supports creating subcompartments inside of compartments to create hierarchies that are six levels deep.
MAXIMUM_DEPTH_OF_NESTED_COMPARTMENT = 6


def list_subcompartments_upto_depth(identity_client, compartment_id, depth):
    if depth == 1:
        return oci_utils.list_all_resources(
            identity_client.list_compartments, compartment_id=compartment_id
        )

    subcompartments = []

    immediate_subcompartments = oci_utils.list_all_resources(
        identity_client.list_compartments, compartment_id=compartment_id
    )

    if immediate_subcompartments:
        subcompartments.extend(immediate_subcompartments)

    for comp in immediate_subcompartments:
        subcompartments.extend(
            list_subcompartments_upto_depth(identity_client, comp.id, depth - 1)
        )
    return subcompartments


def list_subcompartments(identity_client, module, tenancy):
    # 1. If only root compartment OCID is provided, list all the first-level child compartments in the root
    # compartment as depth defaults to 1.
    # 2. If root compartment OCID is provided with fetch_subcompartments=False, retrieve information of root
    # compartment.
    # 3. If root compartment OCID is provided with depth, list only child compartments upto depth.

    # 1. If only non-root compartment OCID is provided, retrieve information of the non-root compartment.
    # 2. If non-root compartment OCID is provided with fetch_subcompartments=True, list all the first-level
    # child compartments in the non-root compartment as depth defaults to 1.
    # 3. If non-root compartment OCID is provided with depth, list only child compartments upto depth.

    compartment_id = module.params["compartment_id"]

    if module.params["depth"] >= MAXIMUM_DEPTH_OF_NESTED_COMPARTMENT:
        # Using API to list all compartment under tenancy using parameter `compartment_id_in_subtree`.
        if tenancy:
            result = to_dict(
                oci_utils.list_all_resources(
                    identity_client.list_compartments,
                    compartment_id=compartment_id,
                    compartment_id_in_subtree=True,
                )
            )
        # API doesn't support listing entire hierarchy under a non-root compartment.
        else:
            result = to_dict(
                list_subcompartments_upto_depth(
                    identity_client, compartment_id, module.params["depth"]
                )
            )

    elif module.params["depth"] == 1:
        result = to_dict(
            oci_utils.list_all_resources(
                identity_client.list_compartments, compartment_id=compartment_id
            )
        )
    # Retrieve all subcompartments under compartment_id which are at depth <= module.params["depth"].
    else:
        result = to_dict(
            list_subcompartments_upto_depth(
                identity_client, compartment_id, module.params["depth"]
            )
        )

    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            fetch_subcompartments=dict(type="bool", required=False),
            depth=dict(type="int", required=False, default=1),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = module.params["compartment_id"]
    tenancy = None

    # Try to retrieve the tenancy information using the compartment_id to check if the provided compartment_id is OCID
    # of a tenancy(root compartment).
    try:
        tenancy = oci_utils.call_with_backoff(
            identity_client.get_tenancy, tenancy_id=compartment_id
        ).data
    except ServiceError:
        pass

    try:
        # Use `True` as default value for `fetch_subcompartments` when root compartment OCID is provided. Decided on
        # this for backward compatibility while supporting feature to list nested compartments.
        if tenancy is not None:
            if module.params["fetch_subcompartments"] is None:
                module.params["fetch_subcompartments"] = True

        # For a non-root compartment, set default value for `fetch_subcompartments` to False.
        else:
            if module.params["fetch_subcompartments"] is None:
                module.params["fetch_subcompartments"] = False

        if module.params["fetch_subcompartments"]:
            result = list_subcompartments(identity_client, module, tenancy)
            # If name is provided, return only the matching compartments from the result.
            if module.params["name"]:
                result = [
                    comp for comp in result if comp["name"] == module.params["name"]
                ]
        else:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        identity_client.get_compartment, compartment_id=compartment_id
                    ).data
                )
            ]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(compartments=result)


if __name__ == "__main__":
    main()
