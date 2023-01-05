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
module: oci_database_management_consumer_group_privilege_facts
short_description: Fetches details about one or multiple ConsumerGroupPrivilege resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ConsumerGroupPrivilege resources in Oracle Cloud Infrastructure
    - Gets the list of consumer group privileges granted to a specific user.
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
- name: List consumer_group_privileges
  oci_database_management_consumer_group_privilege_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    user_name: user_name_example

    # optional
    name: name_example
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
consumer_group_privileges:
    description:
        - List of ConsumerGroupPrivilege resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the granted consumer group privilege.
            returned: on success
            type: str
            sample: name_example
        grant_option:
            description:
                - Indicates whether the privilege is granted with the GRANT option (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
        initial_group:
            description:
                - Indicates whether the consumer group is designated as the default for this user or role (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
    sample: [{
        "name": "name_example",
        "grant_option": "YES",
        "initial_group": "YES"
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


class ConsumerGroupPrivilegeFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_consumer_group_privileges,
            managed_database_id=self.module.params.get("managed_database_id"),
            user_name=self.module.params.get("user_name"),
            **optional_kwargs
        )


ConsumerGroupPrivilegeFactsHelperCustom = get_custom_class(
    "ConsumerGroupPrivilegeFactsHelperCustom"
)


class ResourceFactsHelper(
    ConsumerGroupPrivilegeFactsHelperCustom, ConsumerGroupPrivilegeFactsHelperGen
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
        resource_type="consumer_group_privilege",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(consumer_group_privileges=result)


if __name__ == "__main__":
    main()
