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
module: oci_fusion_apps_admin_user_facts
short_description: Fetches details about one or multiple AdminUser resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AdminUser resources in Oracle Cloud Infrastructure
    - List all FusionEnvironment admin users
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    fusion_environment_id:
        description:
            - unique FusionEnvironment identifier
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List admin_users
  oci_fusion_apps_admin_user_facts:
    # required
    fusion_environment_id: "ocid1.fusionenvironment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
admin_users:
    description:
        - List of AdminUser resources
    returned: on success
    type: complex
    contains:
        username:
            description:
                - Admin username
            returned: on success
            type: str
            sample: username_example
        email_address:
            description:
                - Admin users email address
            returned: on success
            type: str
            sample: email_address_example
        first_name:
            description:
                - Admin users first name
            returned: on success
            type: str
            sample: first_name_example
        last_name:
            description:
                - Admin users last name
            returned: on success
            type: str
            sample: last_name_example
    sample: [{
        "username": "username_example",
        "email_address": "email_address_example",
        "first_name": "first_name_example",
        "last_name": "last_name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.fusion_apps import FusionApplicationsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AdminUserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "fusion_environment_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_admin_users,
            fusion_environment_id=self.module.params.get("fusion_environment_id"),
            **optional_kwargs
        )


AdminUserFactsHelperCustom = get_custom_class("AdminUserFactsHelperCustom")


class ResourceFactsHelper(AdminUserFactsHelperCustom, AdminUserFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(fusion_environment_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="admin_user",
        service_client_class=FusionApplicationsClient,
        namespace="fusion_apps",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(admin_users=result)


if __name__ == "__main__":
    main()
