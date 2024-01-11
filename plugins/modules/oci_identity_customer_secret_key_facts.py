#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_identity_customer_secret_key_facts
short_description: Fetches details about one or multiple CustomerSecretKey resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CustomerSecretKey resources in Oracle Cloud Infrastructure
    - Lists the secret keys for the specified user. The returned object contains the secret key's OCID, but not
      the secret key itself. The actual secret key is returned only upon creation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List customer_secret_keys
  oci_identity_customer_secret_key_facts:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
customer_secret_keys:
    description:
        - List of CustomerSecretKey resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the secret key.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user the password belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The displayName you assign to the secret key. Does not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_expires:
            description:
                - Date and time when this password will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
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
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomerSecretKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "user_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_customer_secret_keys,
            user_id=self.module.params.get("user_id"),
            **optional_kwargs
        )


CustomerSecretKeyFactsHelperCustom = get_custom_class(
    "CustomerSecretKeyFactsHelperCustom"
)


class ResourceFactsHelper(
    CustomerSecretKeyFactsHelperCustom, CustomerSecretKeyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(user_id=dict(type="str", required=True), display_name=dict(type="str"),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="customer_secret_key",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(customer_secret_keys=result)


if __name__ == "__main__":
    main()
