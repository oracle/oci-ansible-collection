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
module: oci_group_facts
short_description: Fetches details of all the OCI groups of a tenancy and the users
                   associated
description:
    - Fetches details of all the OCI groups of a tenancy and the users associated with them.
version_added: "2.5"
options:
    group_id:
        description: Identifier of the group whose details should be fetched
        required: false
        aliases: ['id']
    compartment_id:
        description: The OCID of the compartment (remember that the tenancy is simply the root compartment). If
                     unspecified, the module automatically picks up tenancy information from your OCI SDK configuration.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
#Fetch a specific group details
- name : List OCI user group facts
  oci_group_facts:
            group_id: 'ocid1.group.oci.asdx'

#Fetch all groups
- name : List all OCI user groups
  oci_group_facts:

"""

RETURN = """
groups:
    description: List of group details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: Identifier of the tenancy containing the group
            returned: always
            type: string
            sample: ocid1.xzvf..oifds
        description:
            description: Description of the group
            returned: always
            type: string
            sample: Network Admin group
        name:
            description: Unique name of the group
            returned: always
            type: string
            sample: network_admin
        id:
            description: Identifier of the group
            returned: always
            type: string
            sample: ocid1.group.oc1.axdf
        inactive_status:
            description: The detailed status of INACTIVE life cycle state
            returned: when group's lifecycle_state is INACTIVE
            type: string
            sample: null
        lifecycle_state:
            description: Current state of the group
            returned: always
            type: string
            sample: ACTIVE
        time_created:
            description: Date and time the group was created, in the format
                         defined by RFC3339
            returned: always
            type: datetime
            sample: 2016-08-25T21:10:29.600Z
        members:
            description: A list of all members that are part of this group.
            returned: always
            type: list
            sample: [{
                      "compartment_id":"ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx",
                      "description":"Test User One",
                      "id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
                      "inactive_status":null,
                      "lifecycle_state":"ACTIVE",
                      "name":"test_user1",
                      "time_created":"2017-09-25T09:20:10.768000+00:00"
                     }]
    sample: [
   {
      "compartment_id":"ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx",
      "description":"Test Ansible Group",
      "id":"ocid1.group.oc1..xxxxxEXAMPLExxxxx",
      "inactive_status":null,
      "freeform_tags":{"group_name":"designer"},
      "defined_tags":{"product":{"type":"server"}},
      "lifecycle_state":"ACTIVE",
      "members":[
         {
            "compartment_id":"ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx",
            "description":"Test User One",
            "id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status":null,
            "lifecycle_state":"ACTIVE",
            "name":"test_user1",
            "freeform_tags":{"user_type":"admin"},
            "defined_tags":{"department":{"division":"engineering"}},
            "time_created":"2017-09-25T09:20:10.768000+00:00"
         },
         {
            "compartment_id":"ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx",
            "description":"Test User Two",
            "id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status":null,
            "lifecycle_state":"ACTIVE",
            "name":"test_user2",
            "freeform_tags":{"user_type":"admin"},
            "defined_tags":{"department":{"division":"engineering"}},
            "time_created":"2017-03-22T04:28:34.943000+00:00"
         }
      ],
      "name":"test_ansible_group",
      "time_created":"2017-10-31T16:38:22.289000+00:00"
   }
]

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_user_groups(identity_client, module):
    group_id = module.params.get("group_id")
    compartment_id = module.params.get("compartment_id")
    name = module.params["name"]
    try:
        if group_id:
            result = get_group(identity_client, group_id, module)
        else:
            result = get_all_groups(identity_client, compartment_id, name)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=ex.args)
    return result


def get_group(identity_client, group_id, module):
    group_dict_list = []
    compartment_id = module.params.get("compartment_id")
    group = oci_utils.call_with_backoff(
        identity_client.get_group, group_id=group_id
    ).data
    append_group_with_associated_users(
        identity_client, group, compartment_id, group_dict_list
    )
    return group_dict_list


def get_all_groups(identity_client, compartment_id, name=None):
    group_dict_list = []
    group_list = oci_utils.list_all_resources(
        identity_client.list_groups, compartment_id=compartment_id, name=name
    )
    for group in group_list:
        append_group_with_associated_users(
            identity_client, group, compartment_id, group_dict_list
        )
    return group_dict_list


def append_group_with_associated_users(
    identity_client, group, compartment_id, group_dict_list
):
    group_dict = to_dict(group)
    group_dict.update(get_associated_users(identity_client, compartment_id, group.id))
    group_dict_list.append(group_dict)


def get_existing_group_members(identity_client, compartment_id, existing_group_id):
    user_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, group_id=existing_group_id)
    )
    existing_group_user_ids = [
        user_group_membership.user_id
        for user_group_membership in user_group_memberships
    ]
    return existing_group_user_ids


def get_associated_users(identity_client, compartment_id, group_id):
    existing_group_member_dict = dict()
    existing_user_list = []
    existing_group_members = get_existing_group_members(
        identity_client, compartment_id, group_id
    )
    for existing_group_member in existing_group_members:
        try:
            response = oci_utils.call_with_backoff(
                identity_client.get_user, user_id=existing_group_member
            )
            user = response.data
            existing_user_list.append(to_dict(user))
        except ServiceError as ex:
            if ex.status != 404:
                raise ex
    existing_group_member_dict["members"] = existing_user_list
    return existing_group_member_dict


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            group_id=dict(type="str", required=False, aliases=["id"]),
            compartment_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    oci_config = oci_utils.get_oci_config(module)
    identity_client = oci_utils.create_service_client(module, IdentityClient)

    # automatically fill in compartment_id if it not specified by user
    if module.params.get("compartment_id") is None:
        compartment_id = oci_config["tenancy"]
        module.params.update(dict({"compartment_id": compartment_id}))

    result = list_user_groups(identity_client, module)

    module.exit_json(groups=result)


if __name__ == "__main__":
    main()
