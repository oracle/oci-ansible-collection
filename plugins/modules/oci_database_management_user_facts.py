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
module: oci_database_management_user_facts
short_description: Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
    - Gets the list of users for the specified managedDatabaseId.
    - If I(user_name) is specified, the details of a single User will be returned.
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
            - Required to get a specific user.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
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
- name: Get a specific user
  oci_database_management_user_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    user_name: user_name_example

- name: List users
  oci_database_management_user_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
users:
    description:
        - List of User resources
    returned: on success
    type: complex
    contains:
        time_locked:
            description:
                - The date the account was locked if account status was LOCKED.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        local_temp_tablespace:
            description:
                - The default local temporary tablespace for the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: local_temp_tablespace_example
        consumer_group:
            description:
                - The initial resource consumer group for the User.
                - Returned for get operation
            returned: on success
            type: str
            sample: consumer_group_example
        external_name:
            description:
                - The external name of the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: external_name_example
        password_versions:
            description:
                - "The list of existing versions of the password hashes (also known as \\"verifiers\\") for the account."
                - Returned for get operation
            returned: on success
            type: str
            sample: password_versions_example
        editions_enabled:
            description:
                - Indicates whether editions have been enabled for the corresponding user (Y) or not (N).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        authentication:
            description:
                - The authentication mechanism for the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: NONE
        proxy_connect:
            description:
                - "Indicates whether a user can connect directly (N) or whether the account can only be proxied (Y) by users who have proxy privileges
                  for this account (that is, by users who have been granted the \\"connect through\\" privilege for this account)."
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        common:
            description:
                - Indicates whether a given user is common(Y) or local(N).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        time_last_login:
            description:
                - The date and time of the last user login.
                  This column is not populated when a user connects to the database with administrative privileges, that is, AS { SYSASM | SYSBACKUP | SYSDBA |
                  SYSDG | SYSOPER | SYSRAC | SYSKM }.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        oracle_maintained:
            description:
                - Indicates whether the user was created and is maintained by Oracle-supplied scripts (such as catalog.sql or catproc.sql).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        inherited:
            description:
                - Indicates whether the user definition is inherited from another container (YES) or not (NO).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        default_collation:
            description:
                - The default collation for the user schema.
                - Returned for get operation
            returned: on success
            type: str
            sample: default_collation_example
        implicit:
            description:
                - Indicates whether the user is a common user created by an implicit application (YES) or not (NO).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        all_shared:
            description:
                - In a sharded database, indicates whether the user is created with shard DDL enabled (YES) or not (NO).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        external_shared:
            description:
                - In a federated sharded database, indicates whether the user is an external shard user (YES) or not (NO).
                - Returned for get operation
            returned: on success
            type: str
            sample: YES
        time_password_changed:
            description:
                - The date and time when the user password was last set.
                  This column is populated only when the value of the AUTHENTICATION_TYPE column is PASSWORD. Otherwise, this column is null.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        name:
            description:
                - The name of the User.
            returned: on success
            type: str
            sample: name_example
        status:
            description:
                - The status of the user account.
            returned: on success
            type: str
            sample: OPEN
        time_expiring:
            description:
                - The date and time of the expiration of the user account.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        default_tablespace:
            description:
                - The default tablespace for data.
            returned: on success
            type: str
            sample: default_tablespace_example
        temp_tablespace:
            description:
                - The name of the default tablespace for temporary tables or the name of a tablespace group.
            returned: on success
            type: str
            sample: temp_tablespace_example
        time_created:
            description:
                - The date and time the user was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        profile:
            description:
                - The User resource profile name.
            returned: on success
            type: str
            sample: profile_example
    sample: [{
        "time_locked": "2013-10-20T19:20:30+01:00",
        "local_temp_tablespace": "local_temp_tablespace_example",
        "consumer_group": "consumer_group_example",
        "external_name": "external_name_example",
        "password_versions": "password_versions_example",
        "editions_enabled": "YES",
        "authentication": "NONE",
        "proxy_connect": "YES",
        "common": "YES",
        "time_last_login": "2013-10-20T19:20:30+01:00",
        "oracle_maintained": "YES",
        "inherited": "YES",
        "default_collation": "default_collation_example",
        "implicit": "YES",
        "all_shared": "YES",
        "external_shared": "YES",
        "time_password_changed": "2013-10-20T19:20:30+01:00",
        "name": "name_example",
        "status": "OPEN",
        "time_expiring": "2013-10-20T19:20:30+01:00",
        "default_tablespace": "default_tablespace_example",
        "temp_tablespace": "temp_tablespace_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "profile": "profile_example"
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


class UserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "user_name",
        ]

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user,
            managed_database_id=self.module.params.get("managed_database_id"),
            user_name=self.module.params.get("user_name"),
        )

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
            self.client.list_users,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


UserFactsHelperCustom = get_custom_class("UserFactsHelperCustom")


class ResourceFactsHelper(UserFactsHelperCustom, UserFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            user_name=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(users=result)


if __name__ == "__main__":
    main()
