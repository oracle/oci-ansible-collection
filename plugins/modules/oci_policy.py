#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
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
module: oci_policy
short_description: Manage policies in OCI Identity and Access Management
description:
    - This module allows the user to create, delete and update policies in OCI Identity and Access Management service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the policy (either the tenancy or another compartment).
                     Required when creating a policy with I(state=present).
        required: false
    description:
        description: The description you assign to the policy. Does not have to be unique, and it's changeable. Required
                     when creating a policy with I(state=present).
        required: false
    name:
        description: The name you assign to the policy during creation. The name must be unique across all policies in
                     the tenancy and cannot be changed. Required when creating a policy with I(state=present).
        required: false
    policy_document:
        description: The path to the policy file. This option is mutually exclusive with I(statements). Either
                     I(statements) or I(policy_document) must be specified when creating a policy with I(state=present).
        required: false
    policy_id:
        description: The OCID of the policy. Required to update or delete a policy.
        required: false
        aliases: ['id']
    state:
        description: Create or update a policy with I(state=present). Delete a policy with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
    statements:
        description: An array of policy statements written in the policy language. This option is mutually exclusive
                     with I(policy_document). Either I(statements) or I(policy_document) must be specified when
                     creating a policy with I(state=present).
        required: false
    version_date:
        description: The version of the policy. The version of the policy. If null or set to an empty string, when a
                     request comes in for authorization, the policy will be evaluated according to the current behavior
                     of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be
                     evaluated according to the behavior of the services on that date.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_tags, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a policy
  oci_policy:
    name: mypolicy
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    description: 'GroupAdmins can add/remove users in Project-A compartment'
    statements: 'Allow group GroupAdmins to manage users in compartment Project-A'

- name: Update a policy
  oci_policy:
    id: ocid1.policy.oc1..xxxxxEXAMPLExxxxx
    name: mypolicy
    description: 'GroupAdmins can add/remove users in Project-A compartment'
    policy_document: '/home/ansible/samples/policy/trial_policy.txt'

- name: Delete a policy
  oci_policy:
    id: ocid1.policy.oc1..xxxxxEXAMPLExxxxx
    state: 'absent'
"""

RETURN = """
policy:
    description: OCI policy details
    returned: On successful operation
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "description": "GroupAdmins can add/remove users in Project-A compartment",
            "id": "ocid1.policy.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "name": "mypolicy",
            "statements": [
                "Allow group GroupAdmins to manage users in compartment Project-A"
            ],
            "time_created": "2017-11-01T19:19:36.700000+00:00",
            "version_date": "2017-11-01T00:00:00+00:00"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreatePolicyDetails
    from oci.identity.models import UpdatePolicyDetails
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
    from oci.exceptions import ServiceError
except ImportError:
    HAS_OCI_PY_SDK = False


def get_policy_statements(file_path):
    policy_statements = None
    with open(to_bytes(file_path), "r") as policy_file:
        policy_statements = []
        for stmt in policy_file:
            policy_statements.append(stmt.strip())

    return policy_statements


def create_policy(identity_client, module):
    create_policy_details = CreatePolicyDetails()
    for attribute in create_policy_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_policy_details, attribute, module.params[attribute])

    if module.params["policy_document"] is not None:
        create_policy_details.statements = get_policy_statements(
            module.params["policy_document"]
        )

    result = oci_utils.create_and_wait(
        resource_type="policy",
        create_fn=identity_client.create_policy,
        kwargs_create={"create_policy_details": create_policy_details},
        client=identity_client,
        get_fn=identity_client.get_policy,
        get_param="policy_id",
        module=module,
    )
    return result


def delete_policy(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="policy",
        client=identity_client,
        get_fn=identity_client.get_policy,
        kwargs_get={"policy_id": module.params["policy_id"]},
        delete_fn=identity_client.delete_policy,
        kwargs_delete={"policy_id": module.params["policy_id"]},
        module=module,
    )
    return result


def update_policy(identity_client, module):
    result = dict()
    changed = False
    try:
        update_policy_details = UpdatePolicyDetails()
        existing_policy = oci_utils.call_with_backoff(
            identity_client.get_policy, policy_id=module.params["policy_id"]
        ).data
        if not oci_utils.are_attrs_equal(
            current_resource=existing_policy,
            module=module,
            attributes=update_policy_details.attribute_map.keys(),
        ):
            update_policy_details = oci_utils.update_model_with_user_options(
                curr_model=existing_policy,
                update_model=update_policy_details,
                module=module,
            )
            # If policy statements are provided using policy document option
            if module.params["policy_document"] is not None:
                update_policy_details.statements = get_policy_statements(
                    module.params["policy_document"]
                )

            response = oci_utils.call_with_backoff(
                identity_client.update_policy,
                policy_id=existing_policy.id,
                update_policy_details=update_policy_details,
            )
            changed = True
            result["policy"] = to_dict(response.data)
        else:
            # No change needed, return the exising policy
            result["policy"] = to_dict(existing_policy)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            description=dict(type="str", required=False),
            name=dict(type="str", required=False),
            policy_document=dict(type="str", required=False),
            policy_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            statements=dict(type="list", required=False),
            version_date=dict(type="datetime", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["policy_document", "statements"]],
        required_if=[["state", "absent", ["policy_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params["state"]
    policy_id = module.params["policy_id"]
    exclude_attributes = {"version_date": True}
    if state == "absent":
        result = delete_policy(identity_client, module)

    else:
        if policy_id is not None:
            result = update_policy(identity_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="policy",
                create_fn=create_policy,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_policies,
                kwargs_list={"compartment_id": module.params["compartment_id"]},
                module=module,
                model=CreatePolicyDetails(),
                exclude_attributes=exclude_attributes,
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
