#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_management_managed_database_group
short_description: Manage a ManagedDatabaseGroup resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagedDatabaseGroup resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a Managed Database Group. The group does not contain any
      Managed Databases when it is created, and they must be added later.
    - "This resource has the following action operations in the M(oci_managed_database_group_actions) module: add_managed_database, change_compartment,
      remove_managed_database."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - "The name of the Managed Database Group. Valid characters are uppercase or
              lowercase letters, numbers, and \\"_\\". The name of the Managed Database Group
              cannot be modified. It must be unique in the compartment and must begin with
              an alphabetic character."
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The information specified by the user about the Managed Database Group.
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              in which the Managed Database Group resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagedDatabaseGroup.
            - Use I(state=present) to create or update a ManagedDatabaseGroup.
            - Use I(state=absent) to delete a ManagedDatabaseGroup.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create managed_database_group
  oci_database_management_managed_database_group:
    compartment_id: "ocid1.tenancy.oc1..unique_ID"
    name: "TestGroup"
    description: "Sales test database group"

- name: Update managed_database_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_managed_database_group:
    description: "Test database group"

- name: Update managed_database_group
  oci_database_management_managed_database_group:
    description: "Test database group"
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete managed_database_group
  oci_database_management_managed_database_group:
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete managed_database_group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_managed_database_group:
    name: TestGroup
    compartment_id: "ocid1.tenancy.oc1..unique_ID"
    state: absent

"""

RETURN = """
managed_database_group:
    description:
        - Details of the ManagedDatabaseGroup resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the Managed Database Group.
            returned: on success
            type: str
            sample: name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The information specified by the user about the Managed Database Group.
            returned: on success
            type: str
            sample: description_example
        managed_databases:
            description:
                - A list of Managed Databases in the Managed Database Group.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the Managed Database.
                    returned: on success
                    type: str
                    sample: name_example
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the Managed Database
                          resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                deployment_type:
                    description:
                        - The infrastructure used to deploy the Oracle Database.
                    returned: on success
                    type: str
                    sample: ONPREMISE
                database_type:
                    description:
                        - The type of Oracle Database installation.
                    returned: on success
                    type: str
                    sample: EXTERNAL_SIDB
                database_sub_type:
                    description:
                        - The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container
                          Database.
                    returned: on success
                    type: str
                    sample: CDB
                time_added:
                    description:
                        - The date and time the Managed Database was added to the group.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current lifecycle state of the Managed Database Group.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the Managed Database Group was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the Managed Database Group was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "name": "name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "managed_databases": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "deployment_type": "ONPREMISE",
            "database_type": "EXTERNAL_SIDB",
            "database_sub_type": "CDB",
            "time_added": "2013-10-20T19:20:30+01:00"
        }],
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateManagedDatabaseGroupDetails
    from oci.database_management.models import UpdateManagedDatabaseGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedDatabaseGroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "managed_database_group_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_group_id")

    def get_get_fn(self):
        return self.client.get_managed_database_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_managed_database_group,
            managed_database_group_id=self.module.params.get(
                "managed_database_group_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_managed_database_groups, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagedDatabaseGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_managed_database_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_managed_database_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagedDatabaseGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_managed_database_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_group_id=self.module.params.get(
                    "managed_database_group_id"
                ),
                update_managed_database_group_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_managed_database_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_group_id=self.module.params.get(
                    "managed_database_group_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagedDatabaseGroupHelperCustom = get_custom_class("ManagedDatabaseGroupHelperCustom")


class ResourceHelper(ManagedDatabaseGroupHelperCustom, ManagedDatabaseGroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            managed_database_group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="managed_database_group",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
