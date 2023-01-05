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
module: oci_database_management_proxied_for_user_facts
short_description: Fetches details about one or multiple ProxiedForUser resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProxiedForUser resources in Oracle Cloud Infrastructure
    - Gets the list of users on whose behalf the current user acts as proxy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    user_name:
        description:
            - The name of the user whose details are to be viewed.
        type: str
        required: true
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'NAME' is ascending. The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List proxied_for_users
  oci_database_management_proxied_for_user_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    user_name: user_name_example

    # optional
    name: name_example
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
proxied_for_users:
    description:
        - List of ProxiedForUser resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of a proxy user or the name of the client user.
            returned: on success
            type: str
            sample: name_example
        authentication:
            description:
                - Indicates whether the proxy is required to supply the client credentials (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
        flags:
            description:
                - The flags associated with the proxy/client pair.
            returned: on success
            type: str
            sample: PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES
    sample: [{
        "name": "name_example",
        "authentication": "YES",
        "flags": "PROXY_MAY_ACTIVATE_ALL_CLIENT_ROLES"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProxiedForUserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "user_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_proxied_for_users,
            managed_database_id=self.module.params.get("managed_database_id"),
            user_name=self.module.params.get("user_name"),
            **optional_kwargs
        )


ProxiedForUserFactsHelperCustom = get_custom_class("ProxiedForUserFactsHelperCustom")


class ResourceFactsHelper(
    ProxiedForUserFactsHelperCustom, ProxiedForUserFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            user_name=dict(type="str", required=True),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="proxied_for_user",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(proxied_for_users=result)


if __name__ == "__main__":
    main()
