#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_identity_ui_password_information_facts
short_description: Fetches details about a UiPasswordInformation resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a UiPasswordInformation resource in Oracle Cloud Infrastructure
    - Gets the specified user's console password information. The returned object contains the user's OCID,
      but not the password itself. The actual password is returned only when created or reset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ui_password_information
  oci_identity_ui_password_information_facts:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ui_password_information:
    description:
        - UiPasswordInformation resource
    returned: on success
    type: complex
    contains:
        user_id:
            description:
                - The OCID of the user.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the password was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The password's current state. After creating a password, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
    sample: {
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING"
    }
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


class UiPasswordInformationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "user_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_ui_password_information,
            user_id=self.module.params.get("user_id"),
        )


UiPasswordInformationFactsHelperCustom = get_custom_class(
    "UiPasswordInformationFactsHelperCustom"
)


class ResourceFactsHelper(
    UiPasswordInformationFactsHelperCustom, UiPasswordInformationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(user_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ui_password_information",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(ui_password_information=result)


if __name__ == "__main__":
    main()
