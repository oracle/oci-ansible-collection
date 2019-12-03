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
module: oci_user
short_description: Create,update and delete OCI user with specified group associations
description:
    - Creates OCI user, if not present, without any group associations
    - Creates OCI user, if not present, with ui password
    - Creates OCI user, if not present, with specified group associations
    - Update OCI user, if present, with a new description
    - Update OCI user, if present, with new group(s) associations
    - Update OCI user, if present, removing all group associations
    - Update OCI user, if present, and reset the ui password of the user
    - Unblock a blocked user
    - Delete OCI user, if present.
version_added: "2.5"
options:
    name:
        description: Name of the user. Must be unique for a tenancy.
        required: true
    user_id:
        description: Identifier of the User. Mandatory for delete and update.
        required: false
        aliases: ['id']
    description:
        description: Description of the user. The value could be an empty string. If not provided explicitly while
                     creating an user, the value defaults to an empty string. Not required for I(state=absent)
        required: false
    user_groups:
        description: List of groups to which the user should be associated  with.The specified groups must exist while
                     running this task. If a specified group does not exist, this task would fail.If a user already
                     exists, and their current group associations are different from the specified group associations,
                     the task would change the user to ensure that the group associations of the user reflect the
                     specified group associations.
        required: false
    state:
        description: Create,update or delete user. For I(state=present), if the user does not exists,
                     it gets created. If exists, it gets updated.. For I(state=absent), user gets deleted.
        required: false
        default: 'present'
        choices: ['present','absent']
    force:
        description: If I(force='no') and if the user is part of a group, user will not be deleted.
                     To delete a user associated with group(s), use I(state=yes).
        required: false
        default: False
        type: bool
    create_or_reset_ui_password:
        description: Create UI password for an user who has no UI password or reset password of an user having UI
                     password.
        required: false
        default: False
        type: bool
    purge_group_memberships:
        description: Purge groups from existing memberships which are not present in provided group memberships. If
                     I(purge_group_memberships=False), provided groups would be appended to existing group memberships.
                     I(purge_group_memberships) and I(delete_group_memberships) are mutually exclusive.
        required: false
        default: False
        type: bool
    delete_group_memberships:
        description: Delete groups from existing memberships which are present in group memberships provided by I(user_groups).
                     If I(delete_group_memberships=True), groups provided by I(user_groups) would be deleted from existing group
                     memberships, if they are part of existing group memberships. If they are not part of existing group memberships,
                     they will be ignored. I(delete_group_memberships) and I(purge_group_memberships) are mutually
                     exclusive.
        required: false
        default: False
        type: bool
    blocked:
        description: Change the state of an blocked user to unblocked.Only applied on existing blocked user. If the
                     user is already unblocked, then I(blocked=no) will not change the state. I(blocked=yes) is not
                     supported in this version.If the value is not specified explicitly, no action should be taken.
        required: false
        choices: ["yes", "no"]

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [oracle, oracle_wait_options, oracle_tags]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.

# User creation or update
- name: Create User with ui password and  group memberships
  oci_user:
      name: 'ansible_user'
      description: 'Ansible  User'
      user_groups: ['ansible_group_A']
      freeform_tags:
            usert_type: 'admin'
      defined_tags:
          department:
              division: 'engineering'
      create_or_reset_ui_password: True
      state: 'present'

- name: Create user without group memberships
  oci_user:
      name: 'ansible_user'
      description: 'Ansible  User'
      create_or_reset_ui_password: True
      state: 'present'

- name: Reset ui password of an existing user
  oci_user:
      id: 'ocid1.user..abuwd'
      create_or_reset_ui_password: True
      state: 'present'

- name: Unblock User
  oci_user:
      id: 'ocid1.user..abuwd'
      blocked: 'no'
      state: 'present'
  register: result

- name: Update user with removing all group memberships
  oci_user:
      id: 'ocid1.user..abuwd'
      description: 'Ansible  User'
      user_groups: []
      state: 'present'

- name: Update user by replacing group memberships, after this
        operation user would become member of ansible_group_B
  oci_user:
      user_id: "ocid1.user..abuwd"
      description: 'Ansible User'
      purge_group_memberships: True
      user_groups: ['ansible_group_B']
      create_or_reset_ui_password: True
      state: 'present'

- name: Update user by deleting group memberships, after this
        operation user would not longer be a member of ansible_group_B
  oci_user:
      user_id: "ocid1.user..abuwd"
      description: 'Ansible User'
      delete_group_memberships: True
      user_groups: ['ansible_group_B']
      create_or_reset_ui_password: True
      state: 'present'

# Delete group
- name: Delete user with no force
  oci_user:
      id: 'ocid1.user..abuwd'
      state: 'absent'

- name: Delete user with  force
  oci_user:
      user_id: 'ocid1.user..abuwd'
      force: 'yes'
      state: 'absent'

"""

RETURN = """
user:
    description: Attributes of the created/updated user.
                 For delete, deleted user description will be returned.
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
        password:
            description: The ui password of the user
            returned: when I(create_or_reset_ui_password=True) and a new user created and when
                      I(create_or_reset_ui_password=True) and new user created or an existing user is updated
            type: string
            sample: _09erf4
    sample: {
        "compartment_id":"ocidv1:tenancy:oc1:arz:1461274726633:aa",
        "description":"Ansible User",
        "id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
        "inactive_status":"None",
        "lifecycle_state":"ACTIVE",
        "password":"PJ+p>u1&u",
        "name":"ansible_user",
        "freeform_tags":{"user_type":"admin"},
        "defined_tags":{"department":{"division":"engineering"}},
        "time_created":"2017-11-04T14:45:27.358000+00:00"
    }

"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded, ClientError
    from oci.util import to_dict
    from oci.identity.models import CreateUserDetails
    from oci.identity.models import UpdateUserDetails, UpdateStateDetails
    from oci.identity.models import AddUserToGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_user(identity_client, module):
    existing_user = None
    user = None
    result = dict(changed=False, user="")
    user_id = module.params.get("user_id")
    try:
        if user_id:
            existing_user = oci_utils.get_existing_resource(
                identity_client.get_user, module, user_id=user_id
            )
            changed, user = update_user(identity_client, existing_user, module)
            result["changed"] = changed
            result["user"] = user
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="user",
                create_fn=create_user,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_users,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                model=CreateUserDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=ex.args)
    return result


def create_user(identity_client, module):
    result = dict()
    ui_password = None
    create_user_details = CreateUserDetails()
    for attribute in create_user_details.attribute_map:
        create_user_details.__setattr__(attribute, module.params.get(attribute))
    result = oci_utils.create_and_wait(
        resource_type="user",
        create_fn=identity_client.create_user,
        kwargs_create={"create_user_details": create_user_details},
        client=identity_client,
        get_fn=identity_client.get_user,
        get_param="user_id",
        module=module,
        states=[module.params.get("wait_until"), "ACTIVE"],
    )
    user = result["user"]
    user_id = user["id"]
    try:
        create_password = module.params["create_or_reset_ui_password"]
        if create_password:
            ui_password = create_or_reset_password(identity_client, user_id)
        groups = module.params.get("user_groups")
        if groups:
            group_ids = get_group_ids_from_group_names(identity_client, groups, module)
            add_user_to_groups(identity_client, user_id, group_ids)
        if ui_password:
            user.update({"password": ui_password})
    except (ServiceError, ClientError) as ex:
        message = None
        if isinstance(ex, ClientError):
            message = ex.args[0]
        else:
            message = ex.message
        module.params.update(dict({"user_id": user_id}))
        module.params.update(dict({"force": True}))
        delete_user(identity_client, module)
        module.fail_json(msg=message)

    result["user"] = user
    return result


def update_user(identity_client, existing_user, module):
    if existing_user is None:
        raise ClientError(
            Exception(
                "No User with id "
                + module.params.get("user_id")
                + " is found for update"
            )
        )
    groups = module.params["user_groups"]
    reset_password = module.params["create_or_reset_ui_password"]
    blocked = module.params["blocked"]
    ui_password = None

    group_changed = modify_group_memberships(
        identity_client, groups, existing_user, module
    )
    existing_user, state_changed = unblock_user(identity_client, blocked, existing_user)
    ui_password, password_changed = reset_ui_password(
        identity_client, existing_user, reset_password
    )
    existing_user, description_tags_changed = update_user_description_and_tags(
        identity_client, existing_user, module
    )
    if not description_tags_changed:
        existing_user = to_dict(existing_user)
    if password_changed:
        existing_user.update({"password": ui_password})

    user_changed = (
        description_tags_changed or group_changed or password_changed or state_changed
    )
    return user_changed, existing_user


def unblock_user(identity_client, blocked, existing_user):
    user_unblocked = False
    if blocked and blocked == "no":
        update_state_details = UpdateStateDetails()
        update_state_details.blocked = False
        response = oci_utils.call_with_backoff(
            identity_client.update_user_state,
            user_id=existing_user.id,
            update_state_details=update_state_details,
        )
        existing_user = response.data
        user_unblocked = True
    return existing_user, user_unblocked


def reset_ui_password(identity_client, existing_user, reset_ui_password):
    password_changed = False
    ui_password = None
    if reset_ui_password:
        ui_password = create_or_reset_password(identity_client, existing_user.id)
        password_changed = True
    return ui_password, password_changed


def modify_group_memberships(identity_client, groups, existing_user, module):
    group_memberships_changed = False
    compartment_id = module.params.get("compartment_id")
    if groups is not None:
        existing_memberships_group_ids = get_group_ids_from_existing_memberships(
            identity_client, compartment_id, existing_user.id
        )
        if groups:
            group_memberships_changed = update_group_memberships(
                identity_client,
                compartment_id,
                groups,
                existing_memberships_group_ids,
                existing_user.id,
                module,
            )
        else:
            group_memberships_changed = delete_all_group_memberships(
                identity_client, compartment_id, existing_user.id
            )
    return group_memberships_changed


def update_group_memberships(
    identity_client,
    compartment_id,
    group_names,
    existing_memberships_group_ids,
    user_id,
    module,
):
    group_membership_changed = False
    purge_group_memberships = module.params.get("purge_group_memberships")
    delete_group_memberships = module.params.get("delete_group_memberships")
    group_ids = get_group_ids_from_group_names(identity_client, group_names, module)

    if delete_group_memberships:
        removable_group_ids = set(existing_memberships_group_ids).intersection(
            set(group_ids)
        )
        if removable_group_ids:
            group_membership_changed = delete_input_group_memberships(
                identity_client, compartment_id, user_id, list(removable_group_ids)
            )
        return group_membership_changed

    if purge_group_memberships:
        if set(group_ids) ^ (set(existing_memberships_group_ids)):
            delete_all_group_memberships(identity_client, compartment_id, user_id)
            existing_memberships_group_ids = []

    groups_to_add_memberships = get_difference_from_existing_memberships(
        existing_memberships_group_ids, group_ids
    )
    if group_ids and groups_to_add_memberships:
        print("groups to add membership")
        add_user_to_groups(identity_client, user_id, groups_to_add_memberships)
        group_membership_changed = True
    return group_membership_changed


def get_group_ids_from_group_names(identity_client, group_names, module):
    group_ids = []
    compartment_id = module.params.get("compartment_id")
    all_existing_groups = oci_utils.list_all_resources(
        identity_client.list_groups, compartment_id=compartment_id
    )
    group_id_dict = dict(
        (group_name, group.id)
        for group in all_existing_groups
        for group_name in group_names
        if group.name == group_name
    )
    try:
        group_ids = [group_id_dict[group_name] for group_name in group_names]
    except KeyError as ex:
        raise ClientError("Group " + ex.args[0] + " does not exists")

    return group_ids


def delete_all_group_memberships(identity_client, compartment_id, existing_user_id):
    group_membership_changed = False
    existing_user_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, user_id=existing_user_id)
    )
    if existing_user_group_memberships:
        group_membership_changed = True
    for existing_user_group_membership in existing_user_group_memberships:
        oci_utils.call_with_backoff(
            identity_client.remove_user_from_group,
            user_group_membership_id=existing_user_group_membership.id,
        )
    return group_membership_changed


def delete_input_group_memberships(
    identity_client, compartment_id, existing_user_id, removable_group_ids
):
    group_membership_changed = False
    existing_user_group_memberships = oci_utils.list_all_resources(
        identity_client.list_user_group_memberships,
        **dict(compartment_id=compartment_id, user_id=existing_user_id)
    )

    for existing_user_group_membership in existing_user_group_memberships:
        if existing_user_group_membership.group_id in removable_group_ids:
            oci_utils.call_with_backoff(
                identity_client.remove_user_from_group,
                user_group_membership_id=existing_user_group_membership.id,
            )
            group_membership_changed = True
    return group_membership_changed


def add_user_to_groups(identity_client, user_id, group_ids):
    add_user_to_group_details = AddUserToGroupDetails()
    add_user_to_group_details.user_id = user_id
    for group_id in group_ids:
        add_user_to_group_details.group_id = group_id
        oci_utils.call_with_backoff(
            identity_client.add_user_to_group,
            add_user_to_group_details=add_user_to_group_details,
        )


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


def update_user_description_and_tags(identity_client, existing_user, module):
    changed = False
    attributes_to_compare = ["description", "defined_tags", "freeform_tags"]
    update_user_details = UpdateUserDetails()
    for attribute in attributes_to_compare:
        changed = oci_utils.check_and_update_attributes(
            update_user_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_user, attribute),
            changed,
        )
    if changed:
        result = oci_utils.update_and_wait(
            resource_type="user",
            update_fn=identity_client.update_user,
            kwargs_update={
                "user_id": existing_user.id,
                "update_user_details": update_user_details,
            },
            client=identity_client,
            get_fn=identity_client.get_user,
            get_param="user_id",
            module=module,
        )
        existing_user = result["user"]
        changed = result["changed"]
    return existing_user, changed


def create_or_reset_password(identity_client, user_id):
    response = oci_utils.call_with_backoff(
        identity_client.create_or_reset_ui_password, user_id=user_id
    )
    ui_password = response.data.password
    return ui_password


def get_difference_from_existing_memberships(existing_memberships_group_ids, groups):
    if not existing_memberships_group_ids:
        return groups
    groups_to_add_memberships = set(groups).difference(
        set(existing_memberships_group_ids)
    )
    return groups_to_add_memberships


def delete_user(identity_client, module):
    result = dict(changed=False, user="")
    user_id = module.params.get("user_id")
    force = module.params.get("force")
    compartment_id = module.params.get("compartment_id")
    try:
        existing_user = oci_utils.get_existing_resource(
            identity_client.get_user, module, user_id=user_id
        )
        if existing_user:
            if force:
                delete_all_group_memberships(
                    identity_client, compartment_id, existing_user.id
                )
            result = oci_utils.delete_and_wait(
                resource_type="user",
                client=identity_client,
                get_fn=identity_client.get_user,
                kwargs_get={"user_id": module.params["user_id"]},
                delete_fn=identity_client.delete_user,
                kwargs_delete={"user_id": module.params["user_id"]},
                module=module,
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            name=dict(type="str", required=False),
            user_id=dict(type="str", required=False, aliases=["id"]),
            description=dict(type="str", required=False, default=""),
            user_groups=dict(type="list", required=False),
            blocked=dict(type="str", required=False, choices=["yes", "no"]),
            create_or_reset_ui_password=dict(
                type="bool", required=False, default=False
            ),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            purge_group_memberships=dict(type="bool", required=False, default=False),
            delete_group_memberships=dict(type="bool", required=False, default=False),
            force=dict(type="bool", required=False, default=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["purge_group_memberships", "delete_group_memberships"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    oci_config = oci_utils.get_oci_config(module)
    identity_client = oci_utils.create_service_client(module, IdentityClient)

    compartment_id = oci_config["tenancy"]
    module.params.update(dict({"compartment_id": compartment_id}))
    state = module.params["state"]
    if state == "present":
        result = create_or_update_user(identity_client, module)
    elif state == "absent":
        result = delete_user(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
