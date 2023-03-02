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
module: oci_database_management_external_db_system
short_description: Manage an ExternalDbSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalDbSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an external DB system and its related resources.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_external_db_system_actions) module: change_compartment,
      disable_external_db_system_database_management, enable_external_db_system_database_management."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the external DB system resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    db_system_discovery_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system discovery.
            - Required for create using I(state=present).
        type: str
    database_management_config:
        description:
            - ""
        type: dict
        suboptions:
            license_model:
                description:
                    - The Oracle license model that applies to the external database.
                type: str
                choices:
                    - "LICENSE_INCLUDED"
                    - "BRING_YOUR_OWN_LICENSE"
                required: true
    display_name:
        description:
            - The user-friendly name for the DB system. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalDbSystem.
            - Use I(state=present) to create or update an ExternalDbSystem.
            - Use I(state=absent) to delete an ExternalDbSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_db_system
  oci_database_management_external_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    db_system_discovery_id: "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_management_config:
      # required
      license_model: LICENSE_INCLUDED
    display_name: display_name_example

- name: Update external_db_system
  oci_database_management_external_db_system:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example

- name: Update external_db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

- name: Delete external_db_system
  oci_database_management_external_db_system:
    # required
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_external_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
external_db_system:
    description:
        - Details of the ExternalDbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_discovery_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system discovery.
            returned: on success
            type: str
            sample: "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx"
        discovery_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management agent used during the discovery of the DB
                  system.
            returned: on success
            type: str
            sample: "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx"
        is_cluster:
            description:
                - Indicates whether the DB system is a cluster DB system or not.
            returned: on success
            type: bool
            sample: true
        home_directory:
            description:
                - The Oracle Grid home directory in case of cluster-based DB system and
                  Oracle home directory in case of single instance-based DB system.
            returned: on success
            type: str
            sample: home_directory_example
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB system resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external DB system was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB system was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_discovery_id": "ocid1.dbsystemdiscovery.oc1..xxxxxxEXAMPLExxxxxx",
        "discovery_agent_id": "ocid1.discoveryagent.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cluster": true,
        "home_directory": "home_directory_example",
        "database_management_config": {
            "license_model": "LICENSE_INCLUDED"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateExternalDbSystemDetails
    from oci.database_management.models import UpdateExternalDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ExternalDbSystemHelperGen, self).get_possible_entity_types() + [
            "externaldbsystem",
            "externaldbsystems",
            "databaseManagementexternaldbsystem",
            "databaseManagementexternaldbsystems",
            "externaldbsystemresource",
            "externaldbsystemsresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "external_db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_db_system_id")

    def get_get_fn(self):
        return self.client.get_external_db_system

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system, external_db_system_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_system,
            external_db_system_id=self.module.params.get("external_db_system_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_external_db_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalDbSystemDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_external_db_system_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExternalDbSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_id=self.module.params.get("external_db_system_id"),
                update_external_db_system_details=update_details,
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
            call_fn=self.client.delete_external_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_db_system_id=self.module.params.get("external_db_system_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalDbSystemHelperCustom = get_custom_class("ExternalDbSystemHelperCustom")


class ResourceHelper(ExternalDbSystemHelperCustom, ExternalDbSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            db_system_discovery_id=dict(type="str"),
            database_management_config=dict(
                type="dict",
                options=dict(
                    license_model=dict(
                        type="str",
                        required=True,
                        choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"],
                    )
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            external_db_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_db_system",
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
