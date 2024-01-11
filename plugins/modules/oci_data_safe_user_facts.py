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
module: oci_data_safe_user_facts
short_description: Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
    - Gets a list of users of the specified user assessment. The result contains the database user details for each user, such
      as user type, account status, last login time, user creation time, authentication type, user profile, and the date and time
      of the latest password change. It also contains the user category derived from these user details as well as privileges
      granted to each user.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_assessment_id:
        description:
            - The OCID of the user assessment.
        type: str
        required: true
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    user_category:
        description:
            - A filter to return only items that match the specified user category.
        type: str
    user_role:
        description:
            - A filter to return only items that match the specified user role.
        type: str
    user_profile:
        description:
            - A filter to return only items that match the specified user profile.
        type: str
    user_type:
        description:
            - "A filter to return only items that match the specified user type. The possible values can be
                - ADMIN_PRIVILEGED
                - APPLICATION
                - PRIVILEGED
                - SCHEMA
                - NON_PRIVILEGED
              as specified by '#/definitions/userTypes'."
        type: str
    user_key:
        description:
            - A filter to return only items that match the specified user key.
        type: str
    account_status:
        description:
            - A filter to return only items that match the specified account status.
        type: str
    authentication_type:
        description:
            - A filter to return only items that match the specified authentication type.
        type: str
    user_name:
        description:
            - A filter to return only items that match the specified user name.
        type: str
    target_id:
        description:
            - A filter to return only items related to a specific target OCID.
        type: str
    time_last_login_greater_than_or_equal_to:
        description:
            - A filter to return users whose last login time in the database is greater than or equal to the date and time specified, in the format defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_last_login_less_than:
        description:
            - "A filter to return users whose last login time in the database is less than the date and time specified, in the format defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
              **Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_user_created_greater_than_or_equal_to:
        description:
            - "A filter to return users whose creation time in the database is greater than or equal to the date and time specified, in the format defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
              **Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_user_created_less_than:
        description:
            - "A filter to return users whose creation time in the database is less than the date and time specified, in the format defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
              **Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_password_last_changed_greater_than_or_equal_to:
        description:
            - A filter to return users whose last password change in the database is greater than or equal to the date and time specified, in the format defined
              by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_password_last_changed_less_than:
        description:
            - A filter to return users whose last password change in the database is less than the date and time specified, in the format defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order (sortOrder). The default order for userName is ascending.
        type: str
        choices:
            - "userName"
            - "userCategory"
            - "accountStatus"
            - "timeLastLogin"
            - "targetId"
            - "timeUserCreated"
            - "authenticationType"
            - "timePasswordChanged"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List users
  oci_data_safe_user_facts:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    user_category: user_category_example
    user_role: user_role_example
    user_profile: user_profile_example
    user_type: user_type_example
    user_key: user_key_example
    account_status: account_status_example
    authentication_type: authentication_type_example
    user_name: user_name_example
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    time_last_login_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_last_login_less_than: 2013-10-20T19:20:30+01:00
    time_user_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_user_created_less_than: 2013-10-20T19:20:30+01:00
    time_password_last_changed_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_password_last_changed_less_than: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: userName

"""

RETURN = """
users:
    description:
        - List of User resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique user key. This is a system-generated identifier. Use ListUsers to get the user key for a user.
            returned: on success
            type: str
            sample: key_example
        user_name:
            description:
                - The database user name.
            returned: on success
            type: str
            sample: user_name_example
        user_category:
            description:
                - The user category based on the privileges and other details of the user.
            returned: on success
            type: str
            sample: CRITICAL
        account_status:
            description:
                - The status of the user account.
            returned: on success
            type: str
            sample: OPEN
        target_id:
            description:
                - The OCID of the target database.
            returned: on success
            type: str
            sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
        time_last_login:
            description:
                - The date and time the user last logged in, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_user_created:
            description:
                - The date and time the user was created in the database, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        authentication_type:
            description:
                - The user authentication method.
            returned: on success
            type: str
            sample: PASSWORD
        user_profile:
            description:
                - The user profile name.
            returned: on success
            type: str
            sample: user_profile_example
        time_password_changed:
            description:
                - The date and time the user password was last changed, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        user_types:
            description:
                - "The user type, which can be a combination of the following:"
                - "'Admin Privileged': The user has administrative privileges.
                  'Application': The user is an Oracle E-Business Suite Applications (EBS) or Fusion Applications (FA) user.
                  'Privileged': The user is a privileged user.
                  'Schema': The user is EXPIRED & LOCKED / EXPIRED / LOCKED, or a schema-only account (authentication type is NONE).
                  'Non-privileged': The user is a non-privileged user."
            returned: on success
            type: list
            sample: []
        admin_roles:
            description:
                - The admin roles granted to the user.
            returned: on success
            type: list
            sample: []
    sample: [{
        "key": "key_example",
        "user_name": "user_name_example",
        "user_category": "CRITICAL",
        "account_status": "OPEN",
        "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
        "time_last_login": "2013-10-20T19:20:30+01:00",
        "time_user_created": "2013-10-20T19:20:30+01:00",
        "authentication_type": "PASSWORD",
        "user_profile": "user_profile_example",
        "time_password_changed": "2013-10-20T19:20:30+01:00",
        "user_types": [],
        "admin_roles": []
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


class DataSafeUserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "user_assessment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "access_level",
            "user_category",
            "user_role",
            "user_profile",
            "user_type",
            "user_key",
            "account_status",
            "authentication_type",
            "user_name",
            "target_id",
            "time_last_login_greater_than_or_equal_to",
            "time_last_login_less_than",
            "time_user_created_greater_than_or_equal_to",
            "time_user_created_less_than",
            "time_password_last_changed_greater_than_or_equal_to",
            "time_password_last_changed_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_users,
            user_assessment_id=self.module.params.get("user_assessment_id"),
            **optional_kwargs
        )


DataSafeUserFactsHelperCustom = get_custom_class("DataSafeUserFactsHelperCustom")


class ResourceFactsHelper(DataSafeUserFactsHelperCustom, DataSafeUserFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_assessment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            user_category=dict(type="str"),
            user_role=dict(type="str"),
            user_profile=dict(type="str"),
            user_type=dict(type="str"),
            user_key=dict(type="str", no_log=True),
            account_status=dict(type="str"),
            authentication_type=dict(type="str"),
            user_name=dict(type="str"),
            target_id=dict(type="str"),
            time_last_login_greater_than_or_equal_to=dict(type="str"),
            time_last_login_less_than=dict(type="str"),
            time_user_created_greater_than_or_equal_to=dict(type="str"),
            time_user_created_less_than=dict(type="str"),
            time_password_last_changed_greater_than_or_equal_to=dict(
                type="str", no_log=True
            ),
            time_password_last_changed_less_than=dict(type="str", no_log=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "userName",
                    "userCategory",
                    "accountStatus",
                    "timeLastLogin",
                    "targetId",
                    "timeUserCreated",
                    "authenticationType",
                    "timePasswordChanged",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(users=result)


if __name__ == "__main__":
    main()
