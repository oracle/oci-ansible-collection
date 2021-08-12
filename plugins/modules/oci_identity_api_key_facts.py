#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_identity_api_key_facts
short_description: Fetches details about one or multiple ApiKey resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ApiKey resources in Oracle Cloud Infrastructure
    - Lists the API signing keys for the specified user. A user can have a maximum of three keys.
    - "Every user has permission to use this API call for *their own user ID*.  An administrator in your
      organization does not need to write a policy to give users this ability."
version_added: "2.9"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List api_keys
  oci_identity_api_key_facts:
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
api_keys:
    description:
        - List of ApiKey resources
    returned: on success
    type: complex
    contains:
        key_id:
            description:
                - "An Oracle-assigned identifier for the key, in this format:
                  TENANCY_OCID/USER_OCID/KEY_FINGERPRINT."
            returned: on success
            type: string
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        key_value:
            description:
                - The key's value.
            returned: on success
            type: string
            sample: key_value_example
        fingerprint:
            description:
                - The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).
            returned: on success
            type: string
            sample: fingerprint_example
        user_id:
            description:
                - The OCID of the user the key belongs to.
            returned: on success
            type: string
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the `ApiKey` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The API key's current state. After creating an `ApiKey` object, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "key_value": "key_value_example",
        "fingerprint": "fingerprint_example",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
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


class ApiKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "user_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_api_keys,
            user_id=self.module.params.get("user_id"),
            **optional_kwargs
        )


ApiKeyFactsHelperCustom = get_custom_class("ApiKeyFactsHelperCustom")


class ResourceFactsHelper(ApiKeyFactsHelperCustom, ApiKeyFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(user_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="api_key",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(api_keys=result)


if __name__ == "__main__":
    main()
