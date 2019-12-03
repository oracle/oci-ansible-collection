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
module: oci_dynamic_group_facts
short_description: Retrieve facts of dynamic groups
description:
    - This module retrieves information of the specified dynamic group or lists all the dynamic groups in a tenancy.
version_added: "2.5"
options:
    dynamic_group_id:
        description: The OCID of the dynamic group. I(dynamic_group_id) is required to get a specific dynamic group's
                     information.
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment (remember that the tenancy is simply the root compartment).
                     Required to list all the dynamic groups in a tenancy.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get all the dynamic groups in a tenancy
  oci_dynamic_group_facts:
    compartment_id: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a specific dynamic group
  oci_dynamic_group_facts:
    dynamic_group_id: ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
dynamic_groups:
    description: List of dynamic group details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the tenancy containing the group.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        description:
            description: The description you assign to the group. Does not have to be unique, and it's changeable.
            returned: always
            type: string
            sample: "Group for all instances with the tag namespace and tag key operations.department"
        id:
            description: The OCID of the group.
            returned: always
            type: string
            sample: ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState.
            returned: always
            type: int
            sample: 1
        lifecycle_state:
            description: The group's current state. After creating a group, make sure its lifecycleState changes from
                         CREATING to ACTIVE before using it.
            returned: always
            type: string
            sample: ACTIVE
        matching_rule:
            description: A rule string that defines which instance certificates will be matched. For syntax, see
                         U(https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm).
            returned: always
            type: string
            sample: tag.operations.department.value
        time_created:
            description: Date and time the group was created, in the format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2018-03-28T18:37:56.190000+00:00
        name:
            description: The name you assign to the group during creation. The name must be unique across all groups in
                         the tenancy and cannot be changed.
            returned: always
            type: string
            sample: Sample dynamic group
    sample: [{
            "compartment_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
            "description": "Group for all instances with the tag namespace and tag key operations.department",
            "id": "ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "matching_rule": "tag.operations.department.value",
            "name": "Sample dynamic group",
            "time_created": "2018-07-05T09:38:27.176000+00:00"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            dynamic_group_id=dict(type="str", required=False, aliases=["id"]),
            compartment_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    dynamic_group_id = module.params["dynamic_group_id"]

    try:
        if dynamic_group_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        identity_client.get_dynamic_group,
                        dynamic_group_id=dynamic_group_id,
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    identity_client.list_dynamic_groups,
                    compartment_id=module.params["compartment_id"],
                    name=module.params["name"],
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(dynamic_groups=result)


if __name__ == "__main__":
    main()
