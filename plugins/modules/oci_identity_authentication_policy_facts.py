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
module: oci_identity_authentication_policy_facts
short_description: Fetches details about a AuthenticationPolicy resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AuthenticationPolicy resource in Oracle Cloud Infrastructure
    - Gets the authentication policy for the given tenancy. You must specify your tenant's OCID as the value for
      the compartment ID (remember that the tenancy is simply the root compartment).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific authentication_policy
  oci_identity_authentication_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
authentication_policy:
    description:
        - AuthenticationPolicy resource
    returned: on success
    type: complex
    contains:
        password_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                minimum_password_length:
                    description:
                        - Minimum password length required.
                    returned: on success
                    type: int
                    sample: 56
                is_uppercase_characters_required:
                    description:
                        - At least one uppercase character required.
                    returned: on success
                    type: bool
                    sample: true
                is_lowercase_characters_required:
                    description:
                        - At least one lower case character required.
                    returned: on success
                    type: bool
                    sample: true
                is_numeric_characters_required:
                    description:
                        - At least one numeric character required.
                    returned: on success
                    type: bool
                    sample: true
                is_special_characters_required:
                    description:
                        - At least one special character required.
                    returned: on success
                    type: bool
                    sample: true
                is_username_containment_allowed:
                    description:
                        - User name is allowed to be part of the password.
                    returned: on success
                    type: bool
                    sample: true
        compartment_id:
            description:
                - Compartment OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        network_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                network_source_ids:
                    description:
                        - Network Source ids
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "password_policy": {
            "minimum_password_length": 56,
            "is_uppercase_characters_required": true,
            "is_lowercase_characters_required": true,
            "is_numeric_characters_required": true,
            "is_special_characters_required": true,
            "is_username_containment_allowed": true
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "network_policy": {
            "network_source_ids": []
        }
    }
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


class AuthenticationPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_authentication_policy,
            compartment_id=self.module.params.get("compartment_id"),
        )


AuthenticationPolicyFactsHelperCustom = get_custom_class(
    "AuthenticationPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    AuthenticationPolicyFactsHelperCustom, AuthenticationPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="authentication_policy",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(authentication_policy=result)


if __name__ == "__main__":
    main()
