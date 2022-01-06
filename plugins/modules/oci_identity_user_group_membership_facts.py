#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_identity_user_group_membership_facts
short_description: Fetches details about one or multiple UserGroupMembership resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UserGroupMembership resources in Oracle Cloud Infrastructure
    - "Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID
      as the value for the compartment ID
      (see L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five)).
      You must also then filter the list in one of these ways:"
    - "- You can limit the results to just the memberships for a given user by specifying a `userId`.
      - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`.
      - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group.
      If the answer is no, the response is an empty list.
      - Although`userId` and `groupId` are not individually required, you must set one of them."
    - If I(user_group_membership_id) is specified, the details of a single UserGroupMembership will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_group_membership_id:
        description:
            - The OCID of the userGroupMembership.
            - Required to get a specific user_group_membership.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple user_group_memberships.
        type: str
    user_id:
        description:
            - The OCID of the user.
        type: str
    group_id:
        description:
            - The OCID of the group.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific user_group_membership
  oci_identity_user_group_membership_facts:
    # required
    user_group_membership_id: "ocid1.usergroupmembership.oc1..xxxxxxEXAMPLExxxxxx"

- name: List user_group_memberships
  oci_identity_user_group_membership_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
user_group_memberships:
    description:
        - List of UserGroupMembership resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the membership.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the user, group, and membership object.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        group_id:
            description:
                - The OCID of the group.
            returned: on success
            type: str
            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the membership was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes
                  from CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserGroupMembershipFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "user_group_membership_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_group_membership,
            user_group_membership_id=self.module.params.get("user_group_membership_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "user_id",
            "group_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_user_group_memberships,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


UserGroupMembershipFactsHelperCustom = get_custom_class(
    "UserGroupMembershipFactsHelperCustom"
)


class ResourceFactsHelper(
    UserGroupMembershipFactsHelperCustom, UserGroupMembershipFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_group_membership_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            user_id=dict(type="str"),
            group_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user_group_membership",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(user_group_memberships=result)


if __name__ == "__main__":
    main()
