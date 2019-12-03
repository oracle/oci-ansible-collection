#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
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
module: oci_group
short_description: Create,update and delete OCI user groups and specified user associations
description:
    - Creates OCI group, if not present, without any user associations
    - Creates OCI group, if not present, with any specified user associations
    - Update OCI group, if present, with description
    - Update OCI group, if present, with new user(s) associations
    - Update OCI group, if present, removing all user associations
    - Delete OCI group, if present.
version_added: "2.5"
options:
    name:
        description: Name of the group. Must be unique within a tenancy.
        required: true
    group_id:
        description: Identifier of the Group. Mandatory for delete and update.
        required: false
        aliases: ['id']
    description:
        description: Description of the group. The value could be an empty string.
                     Mandatory for I(state=present). Not required for I(state=absent)
        required: false
    users:
        description: List of users to be associated with the group. The specified users must exist
                     while running this task. If a specified user does not exist, this task would fail.
        required: false
    state:
        description: Create,update or delete group. For I(state=present), if the group does not exists,
                     it gets created. If exists, it gets updated. For I(state=absent), group gets deleted.
        required: false
        default: 'present'
        choices: ['present','absent']
    purge_user_memberships:
        description: Purge users in existing memberships which are not present in the provided
                     users memberships. If I(purge_user_memberships=no), provided users would be
                     appended to existing user memberships. I(purge_user_memberships) and
                     I(delete_user_memberships) are mutually exclusive.
        required: false
        default: False
        type: bool
    delete_user_memberships:
        description: Delete users in existing memberships which are present in the
                     users memberships provided by I(users). If I(delete_user_memberships=yes), users
                     provided by I(users) would be deleted from existing user memberships, if they
                     are part of existing user memberships. If they are not part of existing user
                     memberships, they will be ignored. I(delete_user_memberships) and I(purge_user_memberships)
                     are mutually exclusive.
        required: false
        default: False
        type: bool
    force:
        description: If I(force='no') and group has any user assigned, then in the case of I(state=absent), group will
                     not be deleted. To delete a group which has user associations, I(force='yes') should be specified.
        required: false
        default: 'no'

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [oracle, oracle_wait_options, oracle_tags]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.

# Group creation
- name: Create group
  oci_group:
            name: 'AnsibleTestGroup'
            description: 'Group for Testing Ansible Module'
            users: ['user1','user2']
            freeform_tags:
                 group_name: 'designer'
            defined_tags:
                product:
                  type: 'server'
            state: 'present'

- name: Update group by purging existing user memberships
  oci_group:
            id: ocid1.group.oc1..xxxxxEXAMPLExxxxx
            description: 'Group for Testing Ansible Module'
            purge_user_memberships: True
            users: ['user1','user3']
            state: 'present'

- name: Update group by deleting existing user memberships
  oci_group:
            id: ocid1.group.oc1..xxxxxEXAMPLExxxxx
            description: 'Group for Testing Ansible Module'
            delete_user_memberships: True
            users: ['user1']
            state: 'present'

- name: Create group without users associations
  oci_group:
            name: 'AnsibleTestGroup'
            description: 'Group for Testing Ansible Module'
            state: 'present'

- name: Delete all User associations of a Group
  oci_group:
            id: ocid1.group.oc1..xxxxxEXAMPLExxxxx
            description: 'Group for Testing Ansible Module'
            users: []
            state: 'present'

# Delete group
- name :  Forcefully delete a group and any user associations it may have
  oci_group:
            id: ocid1.group.oc1..xxxxxEXAMPLExxxxx
            force: 'yes'
            state: 'absent'
"""

RETURN = """
group:
    description: Attributes of the created/updated group.
                 For delete, deleted group description will be returned.
    returned: success
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
            sample: Network Admin Group
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
    sample: [
   {
      "compartment_id":"ocidv1:tenancy:oc1:phx:xxxxxEXAMPLExxxxx",
      "description":"Network Admin Group",
      "id":"ocid1.group.oc1..xxxxxEXAMPLExxxxx",
      "inactive_status":null,
      "lifecycle_state":"ACTIVE",
      "name":"network_admin_group",
      "freeform_tags":{"group_name":"designer"},
      "defined_tags":{"product":{"type":"server"}},
      "time_created":"2017-10-31T16:38:22.289000+00:00"
   }
]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
    from oci.util import to_dict
    from oci.identity.models import CreateGroupDetails
    from oci.identity.models import UpdateGroupDetails
    from oci.identity.models import AddUserToGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_group(identity_client, module):
    group = None
    existing_group = None
    result = dict(changed=False, group="")
    group_id = module.params.get("group_id")
    exclude_attributes = {"compartment_id": True}
    try:
        if group_id:
            existing_group = oci_utils.get_existing_resource(
                identity_client.get_group, module, group_id=group_id
            )
            changed, group = update_group(identity_client, existing_group, module)
            result["changed"] = changed
            result["group"] = group
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="group",
                create_fn=create_group,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_groups,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateGroupDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=ex.args)
    return result


def create_group(identity_client, module):
    result = dict()
    users = module.params.get("users")
    create_group_details = CreateGroupDetails()
    for attribute in create_group_details.attribute_map:
        create_group_details.__setattr__(attribute, module.params.get(attribute))
    response = oci_utils.call_with_backoff(
        identity_client.create_group, create_group_details=create_group_details
    )
    group_id = response.data.id
    response = oci_utils.call_with_backoff(identity_client.get_group, group_id=group_id)
    oci.wait_until(identity_client, response, "lifecycle_state", "ACTIVE")
    group = response.data
    try:
        if users:
            user_ids = get_user_ids_from_user_names(identity_client, users, module)
            add_users_to_group(identity_client, group.id, user_ids)
    except (ServiceError, ClientError) as ex:
        message = None
        if isinstance(ex, ClientError):
            message = ex.args[0]
        else:
            message = ex.message
        module.params.update(dict({"id": group.id}))
        module.params.update(dict({"force": True}))
        delete_group(identity_client, module)
        module.fail_json(msg=message)
    result["group"] = to_dict(group)
    result["changed"] = True
    return result


def update_group(identity_client, existing_group, module):
    if existing_group is None:
        raise ClientError(
            Exception(
                "No Group with id "
                + module.params.get("group_id")
                + " is found for update"
            )
        )
    users = module.params["users"]
    compartment_id = module.params.get("compartment_id")
    existing_group, description_tags_changed = update_group_description_and_tags(
        identity_client, existing_group, module
    )
    user_changed = False
    if users is not None:
        existing_group_members = get_existing_group_members(
            identity_client, existing_group.compartment_id, existing_group.id
        )
        if users:
            user_changed = update_group_users(
                identity_client,
                compartment_id,
                users,
                existing_group_members,
                existing_group,
                module,
            )
        else:
            user_changed = delete_all_users_from_group(
                identity_client, compartment_id, existing_group
            )
    group_dict = to_dict(existing_group)
    return (description_tags_changed or user_changed), group_dict


def delete_all_users_from_group(identity_client, compartment_id, existing_group):
    user_changed = False
    existing_user_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, group_id=existing_group.id)
    )
    if existing_user_group_memberships:
        for existing_user_group_membership in existing_user_group_memberships:
            oci_utils.call_with_backoff(
                identity_client.remove_user_from_group,
                user_group_membership_id=existing_user_group_membership.id,
            )
        user_changed = True
    return user_changed


def delete_input_users_from_group(
    identity_client, compartment_id, existing_group, removable_user_ids
):
    user_changed = False
    existing_user_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, group_id=existing_group.id)
    )
    if existing_user_group_memberships:
        for existing_user_group_membership in existing_user_group_memberships:
            if existing_user_group_membership.user_id in removable_user_ids:
                oci_utils.call_with_backoff(
                    identity_client.remove_user_from_group,
                    user_group_membership_id=existing_user_group_membership.id,
                )
            user_changed = True
    return user_changed


def update_group_users(
    identity_client,
    compartment_id,
    users,
    existing_group_members,
    existing_group,
    module,
):
    purge_user_memberships = module.params["purge_user_memberships"]
    delete_user_memberships = module.params["delete_user_memberships"]
    user_changed = False

    user_ids = get_user_ids_from_user_names(identity_client, users, module)

    if delete_user_memberships:
        removable_user_ids = set(existing_group_members).intersection(set(user_ids))
        if removable_user_ids:
            user_changed = delete_input_users_from_group(
                identity_client,
                compartment_id,
                existing_group,
                list(removable_user_ids),
            )
        return user_changed

    if purge_user_memberships:
        if set(user_ids) ^ (set(existing_group_members)):
            delete_all_users_from_group(identity_client, compartment_id, existing_group)
            existing_group_members = []
    users_to_be_added = get_difference_from_existing_users(
        existing_group_members, user_ids
    )

    if user_ids and users_to_be_added:
        user_changed = True
        add_users_to_group(identity_client, existing_group.id, users_to_be_added)
    return user_changed


def add_users_to_group(identity_client, group_id, user_ids):
    add_user_to_group_details = AddUserToGroupDetails()
    add_user_to_group_details.group_id = group_id
    for user_id in user_ids:
        add_user_to_group_details.user_id = user_id
        oci_utils.call_with_backoff(
            identity_client.add_user_to_group,
            add_user_to_group_details=add_user_to_group_details,
        )


def update_group_description_and_tags(identity_client, existing_group, module):
    changed = False
    attributes_to_compare = ["description", "defined_tags", "freeform_tags"]
    update_group_details = UpdateGroupDetails()
    for attribute in attributes_to_compare:
        changed = oci_utils.check_and_update_attributes(
            update_group_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_group, attribute),
            changed,
        )
    if changed:
        result = oci_utils.update_and_wait(
            resource_type="group",
            update_fn=identity_client.update_group,
            kwargs_update={
                "group_id": existing_group.id,
                "update_group_details": update_group_details,
            },
            client=identity_client,
            get_fn=identity_client.get_group,
            get_param="group_id",
            module=module,
        )
        existing_group = result["group"]
        changed = result["changed"]
    return existing_group, changed


def get_user_ids_from_user_names(identity_client, user_names, module):
    user_ids = []
    users = oci_utils.list_all_resources(
        identity_client.list_users, compartment_id=module.params.get("compartment_id")
    )
    user_id_dict = dict(
        (user_name, user.id)
        for user in users
        for user_name in user_names
        if user.name.strip() == user_name.strip()
    )
    try:
        user_ids = [user_id_dict[user_name] for user_name in user_names]
    except KeyError as ex:
        raise ClientError("User " + ex.args[0] + " does not exists")
    return user_ids


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


def get_difference_from_existing_users(existing_users, users):
    if not existing_users:
        return users
    users_to_be_added = set(users).difference(set(existing_users))
    return users_to_be_added


def delete_group(identity_client, module):
    group_id = module.params.get("group_id")
    force = module.params.get("force")
    compartment_id = module.params.get("compartment_id")
    changed = False
    result = dict(changed=False)
    try:
        existing_group = oci_utils.get_existing_resource(
            identity_client.get_group, module, group_id=group_id
        )
        if existing_group:
            if force == "yes":
                delete_all_users_from_group(
                    identity_client, compartment_id, existing_group
                )
            oci_utils.call_with_backoff(
                identity_client.delete_group, group_id=existing_group.id
            )
            changed = True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=ex.args)

    result["changed"] = changed
    result["group"] = to_dict(existing_group)
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=False),
            group_id=dict(type="str", required=False, aliases=["id"]),
            description=dict(type="str", required=False, default=""),
            users=dict(type="list", required=False),
            purge_user_memberships=dict(type="bool", required=False, default=False),
            delete_user_memberships=dict(type="bool", required=False, default=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            force=dict(type="str", required=False, default="no"),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_user_memberships", "delete_user_memberships"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    oci_config = oci_utils.get_oci_config(module)
    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = oci_config["tenancy"]
    module.params.update(dict({"compartment_id": compartment_id}))
    state = module.params["state"]

    if state == "present":
        result = create_or_update_group(identity_client, module)
    elif state == "absent":
        result = delete_group(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
