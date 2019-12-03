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
module: oci_user_facts
short_description: Fetches details of all the OCI users of a tenancy and
                   their group memberships
description:
    - Fetches details of all the OCI users of a tenancy and the group memberships.
version_added: "2.5"
options:
    user_id:
        description: Identifier of the user id whose details should be fetched
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
#Fetch users filtered by user id
- name: List user filtered by user id
  oci_user_facts:
      user_id: 'ocid1.user.oc1..xxxxxEXAMPLExxxxx'

#Fetch all existing users
- name: List all existing users
  oci_user_facts:
"""

RETURN = """
users:
    description: Attributes of the existing users.
    returned: success
    type: complex
    contains:
        compartment_id:
            description: The identifier of the tenancy containing the user
            returned: always
            type: string
            sample: ocid1.tenancy.oc1.xzvf..oifds
        description:
            description: The description assigned to the user
            returned: always
            type: string
            sample: Ansible User
        name:
            description: Name assigned to the user during creation
            returned: always
            type: string
            sample: ansible_user
        id:
            description: Identifier of the user
            returned: always
            type: string
            sample: ocid1.user.oc1.axdf
        inactive_status:
            description: The detailed status of INACTIVE life cycle state
            returned: when user's lifecycle_state is INACTIVE
            type: string
            sample: None
        lifecycle_state:
            description: The current state of the user
            returned: always
            type: string
            sample: ACTIVE
        time_created:
            description: Date and time when the user was created, in the format
                         defined by RFC3339
            returned: always
            type: datetime
            sample: 2016-08-25T21:10:29.600Z
        member_of_groups:
            description: The details of the groups the user
                         has memberships in
            returned: always
            type: string
            sample: [ { "id":"ocid1.group.oc1..xxxxxEXAMPLExxxxx",
                        "compartment_id":"ocidv1:tenancy:oc1:arz:146:aaa",
                        "name":"group_two",
                        "description":"Group Two",
                        "time_created":"2017-06-22T13:55:21.077000+00:00",
                        "lifecycle_state":"ACTIVE",
                        "inactive_status":"None"
                      }]
    sample: [{
                "compartment_id":"ocidv1:tenancy:oc1:arz:1461274726633:aa",
                "description":"Ansible User",
                "id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
                "inactive_status":"None",
                "lifecycle_state":"ACTIVE",
                "name":"ansible_user",
                "freeform_tags":{"user_type":"admin"},
                "defined_tags":{"department":{"division":"engineering"}},
                "time_created":"2017-11-04T14:45:27.358000+00:00",
                "member_of_groups":[
                                     {
                                        "id":"ocid1.group.oc1..xxxxxEXAMPLExxxxx",
                                        "compartment_id":"ocidv1:tenancy:oc1:arz:146:aaa",
                                        "name":"group_two",
                                        "description":"Group Two",
                                        "time_created":"2017-06-22T13:55:21.077000+00:00",
                                        "lifecycle_state":"ACTIVE",
                                        "freeform_tags":{"group_name":"designer"},
                                        "defined_tags":{"product":{"type":"server"}},
                                        "inactive_status":"None"
                                    },
                                    {
                                         "id":"ocid1.group.oc1..xxxxxEXAMPLExxxxx",
                                         "compartment_id":"ocidv1:tenancy:oc1:arz:145",
                                         "name":"group_one",
                                         "description":"Group One",
                                         "time_created":"2016-12-20T20:29:12.093000+00:00",
                                         "lifecycle_state":"ACTIVE",
                                         "freeform_tags":{"group_name":"documentation"},
                                         "defined_tags":{"product":{"type":"server"}},
                                         "inactive_status":"None"
                                     }
                                  ]
             }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_users(identity_client, module):
    compartment_id = module.params.get("compartment_id")
    user_id = module.params.get("user_id")
    name = module.params.get("name")
    try:
        if user_id:
            result = get_user(identity_client, user_id, module)
        else:
            result = get_all_users(identity_client, compartment_id, name)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return result


def get_user(identity_client, user_id, module):
    user_dict_list = []
    compartment_id = module.params.get("compartment_id")
    user = oci_utils.call_with_backoff(identity_client.get_user, user_id=user_id).data
    append_asociated_groups_with_user(
        identity_client, user, compartment_id, user_dict_list
    )
    return user_dict_list


def get_all_users(identity_client, compartment_id, name=None):
    user_dict_list = []
    user_list = oci_utils.list_all_resources(
        identity_client.list_users, compartment_id=compartment_id, name=name
    )
    for user in user_list:
        append_asociated_groups_with_user(
            identity_client, user, compartment_id, user_dict_list
        )
    return user_dict_list


def append_asociated_groups_with_user(
    identity_client, user, compartment_id, user_dict_list
):
    user_dict = to_dict(user)
    user_dict.update(get_associated_groups(identity_client, compartment_id, user.id))
    user_dict_list.append(user_dict)


def get_group_ids_from_existing_memberships(
    identity_client, compartment_id, existing_user_id
):
    existing_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, user_id=existing_user_id)
    )
    existing_group_ids = [
        existing_group_membership.group_id
        for existing_group_membership in existing_group_memberships
    ]
    return existing_group_ids


def get_associated_groups(identity_client, compartment_id, user_id):
    existing_group_memberships_dict = dict()
    groups_in_memberships = []
    existing_memberships_group_ids = get_group_ids_from_existing_memberships(
        identity_client, compartment_id, user_id
    )
    for group_id in existing_memberships_group_ids:
        try:
            response = oci_utils.call_with_backoff(
                identity_client.get_group, group_id=group_id
            )
            group = response.data
            groups_in_memberships.append(to_dict(group))
        except ServiceError as ex:
            if ex.status != 404:
                raise ex
    existing_group_memberships_dict["member_of_groups"] = groups_in_memberships
    return existing_group_memberships_dict


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            user_id=dict(type="str", required=False, aliases=["id"]),
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

    result = list_users(identity_client, module)

    module.exit_json(users=result)


if __name__ == "__main__":
    main()
