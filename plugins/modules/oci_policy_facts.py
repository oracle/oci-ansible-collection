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
module: oci_policy_facts
short_description: Retrieve details about a policy or policies attached to a compartment or tenancy in OCI Identity
                   and Access Management service
description:
    - This module retrieves a specific policy or all the policies attached to a specified compartment in OCI Identity
      and Access Management service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment (remember that the tenancy is simply the root compartment). Required to
                     list all the policies in a compartment.
        required: false
    policy_id:
        description: The OCID of the policy. Required when retrieving a specific policy.
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get all the policies attached to a compartment or tenancy
  oci_policy_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get details of a specific policy
  oci_policy_facts:
    id: ocid1.policy.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
policies:
    description: Information of one or more policies
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the policy (either the tenancy or another compartment).
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        description:
            description: The description assigned to the policy.
            returned: always
            type: string
            sample: "GroupAdmins can add/remove users in Project-A compartment"
        id:
            description: The OCID of the policy.
            returned: always
            type: string
            sample: ocid1.policy.oc1..xxxxxEXAMPLExxxxx
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState.
            returned: always
            type: int
            sample: 5
        lifecycle_state:
            description: The policy's current state.
            returned: always
            type: string
            sample: ACTIVE
        name:
            description: The name assigned to the policy during creation.
            returned: always
            type: string
            sample: mypolicy
        statements:
            description: A list of one or more policy statements written in the policy language.
            returned: always
            type: list[string]
            sample: [
                        "Allow group GroupAdmins to manage users in compartment Project-A"
                    ]
        time_created:
            description: Date and time the policy was created, in the format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2017-11-01T14:59:51.728000+00:00
        version_date:
            description: The version of the policy. If null or set to an empty string, when a request comes in for \
                        authorization, the policy will be evaluated according to the current behavior of the services \
                        at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated \
                        according to the behavior of the services on that date.
            returned: always
            type: datetime
            sample: 2017-11-01T00:00:00+00:00
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
        "description": "GroupAdmins can add/remove users in Project-A compartment",
        "id": "ocid1.policy.oc1..xxxxxEXAMPLExxxxx",
        "inactive_status": null,
        "lifecycle_state": "ACTIVE",
        "name": "mypolicy",
        "statements": [
            "Allow group GroupAdmins to manage users in compartment Project-A"
        ],
        "time_created": "2017-11-01T14:59:51.728000+00:00",
        "version_date": "2017-11-01T00:00:00+00:00"
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


def main():
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            policy_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "policy_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    policy_id = module.params["policy_id"]

    try:
        if policy_id is None:
            result = to_dict(
                oci_utils.list_all_resources(
                    identity_client.list_policies,
                    compartment_id=module.params["compartment_id"],
                    name=module.params["name"],
                )
            )
        else:
            result = [to_dict(identity_client.get_policy(policy_id).data)]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(policies=result)


if __name__ == "__main__":
    main()
