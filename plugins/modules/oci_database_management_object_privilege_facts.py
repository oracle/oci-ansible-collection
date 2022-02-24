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
module: oci_database_management_object_privilege_facts
short_description: Fetches details about one or multiple ObjectPrivilege resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ObjectPrivilege resources in Oracle Cloud Infrastructure
    - Gets the list of object privileges granted to a specific user.
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
- name: List object_privileges
  oci_database_management_object_privilege_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    user_name: user_name_example

    # optional
    name: name_example
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
object_privileges:
    description:
        - List of ObjectPrivilege resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the privilege on the object.
            returned: on success
            type: str
            sample: name_example
        schema_type:
            description:
                - The type of object.
            returned: on success
            type: str
            sample: schema_type_example
        owner:
            description:
                - The owner of the object.
            returned: on success
            type: str
            sample: owner_example
        grantor:
            description:
                - The name of the user who granted the object privilege.
            returned: on success
            type: str
            sample: grantor_example
        hierarchy:
            description:
                - Indicates whether the privilege is granted with the HIERARCHY OPTION (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
        object:
            description:
                - The name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on.
            returned: on success
            type: str
            sample: object_example
        grant_option:
            description:
                - Indicates whether the privilege is granted with the GRANT OPTION (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
        common:
            description:
                - "Indicates how the object privilege was granted. Possible values:
                  YES if the role is granted commonly (CONTAINER=ALL is used)
                  NO if the role is granted locally (CONTAINER=ALL is not used)"
            returned: on success
            type: str
            sample: YES
        inherited:
            description:
                - Indicates whether the granted privilege is inherited from another container (YES) or not (NO).
            returned: on success
            type: str
            sample: YES
    sample: [{
        "name": "name_example",
        "schema_type": "schema_type_example",
        "owner": "owner_example",
        "grantor": "grantor_example",
        "hierarchy": "YES",
        "object": "object_example",
        "grant_option": "YES",
        "common": "YES",
        "inherited": "YES"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ObjectPrivilegeFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_object_privileges,
            managed_database_id=self.module.params.get("managed_database_id"),
            user_name=self.module.params.get("user_name"),
            **optional_kwargs
        )


ObjectPrivilegeFactsHelperCustom = get_custom_class("ObjectPrivilegeFactsHelperCustom")


class ResourceFactsHelper(
    ObjectPrivilegeFactsHelperCustom, ObjectPrivilegeFactsHelperGen
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

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="object_privilege",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(object_privileges=result)


if __name__ == "__main__":
    main()
