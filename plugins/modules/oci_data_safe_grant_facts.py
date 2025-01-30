#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_safe_grant_facts
short_description: Fetches details about one or multiple Grant resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Grant resources in Oracle Cloud Infrastructure
    - Gets a list of grants for a particular user in the specified user assessment. A user grant contains details such as the
      privilege name, type, category, and depth level. The depth level indicates how deep in the hierarchy of roles granted to
      roles a privilege grant is. The userKey in this operation is a system-generated identifier. Perform the operation ListUsers
      to get the userKey for a particular user.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_assessment_id:
        description:
            - The OCID of the user assessment.
        type: str
        required: true
    user_key:
        description:
            - The unique user key. This is a system-generated identifier. ListUsers gets the user key for a user.
        type: str
        required: true
    grant_key:
        description:
            - A filter to return only items that match the specified user grant key.
        type: str
    grant_name:
        description:
            - A filter to return only items that match the specified user grant name.
        type: str
    privilege_type:
        description:
            - A filter to return only items that match the specified privilege grant type.
        type: str
    privilege_category:
        description:
            - A filter to return only items that match the specified user privilege category.
        type: str
    depth_level:
        description:
            - A filter to return only items that match the specified user grant depth level.
        type: int
    depth_level_greater_than_or_equal_to:
        description:
            - A filter to return only items that are at a level greater than or equal to the specified user grant depth level.
        type: int
    depth_level_less_than:
        description:
            - A filter to return only items that are at a level less than the specified user grant depth level.
        type: int
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order (sortOrder). The default order for grantName is ascending.
        type: str
        choices:
            - "grantName"
            - "grantType"
            - "privilegeCategory"
            - "depthLevel"
            - "key"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List grants
  oci_data_safe_grant_facts:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    user_key: user_key_example

    # optional
    grant_key: grant_key_example
    grant_name: grant_name_example
    privilege_type: privilege_type_example
    privilege_category: privilege_category_example
    depth_level: 56
    depth_level_greater_than_or_equal_to: 56
    depth_level_less_than: 56
    sort_order: ASC
    sort_by: grantName

"""

RETURN = """
grants:
    description:
        - List of Grant resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key of a user grant.
            returned: on success
            type: str
            sample: key_example
        grant_name:
            description:
                - The name of a user grant.
            returned: on success
            type: str
            sample: grant_name_example
        privilege_type:
            description:
                - The type of a user grant.
            returned: on success
            type: str
            sample: SYSTEM_PRIVILEGE
        privilege_category:
            description:
                - The privilege category.
            returned: on success
            type: str
            sample: CRITICAL
        depth_level:
            description:
                - The grant depth level of the indirect grant.
                  An indirectly granted role/privilege is granted to the user through another role.
                  The depth level indicates how deep a privilege is within the grant hierarchy.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "key": "key_example",
        "grant_name": "grant_name_example",
        "privilege_type": "SYSTEM_PRIVILEGE",
        "privilege_category": "CRITICAL",
        "depth_level": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeGrantFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "user_assessment_id",
            "user_key",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "grant_key",
            "grant_name",
            "privilege_type",
            "privilege_category",
            "depth_level",
            "depth_level_greater_than_or_equal_to",
            "depth_level_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_grants,
            user_assessment_id=self.module.params.get("user_assessment_id"),
            user_key=self.module.params.get("user_key"),
            **optional_kwargs
        )


DataSafeGrantFactsHelperCustom = get_custom_class("DataSafeGrantFactsHelperCustom")


class ResourceFactsHelper(DataSafeGrantFactsHelperCustom, DataSafeGrantFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_assessment_id=dict(type="str", required=True),
            user_key=dict(type="str", required=True, no_log=True),
            grant_key=dict(type="str", no_log=True),
            grant_name=dict(type="str"),
            privilege_type=dict(type="str"),
            privilege_category=dict(type="str"),
            depth_level=dict(type="int"),
            depth_level_greater_than_or_equal_to=dict(type="int"),
            depth_level_less_than=dict(type="int"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "grantName",
                    "grantType",
                    "privilegeCategory",
                    "depthLevel",
                    "key",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="grant",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(grants=result)


if __name__ == "__main__":
    main()
