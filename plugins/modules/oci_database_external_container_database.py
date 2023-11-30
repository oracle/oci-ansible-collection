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
module: oci_database_external_container_database
short_description: Manage an ExternalContainerDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ExternalContainerDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new external container database resource.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_external_container_database_actions) module: change_compartment,
      disable_external_container_database_database_management, disable_external_container_database_stack_monitoring,
      enable_external_container_database_database_management, enable_external_container_database_stack_monitoring,
      scan_external_container_database_pluggable_databases."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The user-friendly name for the external database. The name does not have to be unique.
            - Required for create using I(state=present), update using I(state=present) with external_container_database_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    external_container_database_id:
        description:
            - The ExternalContainerDatabase L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ExternalContainerDatabase.
            - Use I(state=present) to create or update an ExternalContainerDatabase.
            - Use I(state=absent) to delete an ExternalContainerDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create external_container_database
  oci_database_external_container_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update external_container_database
  oci_database_external_container_database:
    # required
    display_name: display_name_example
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update external_container_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_container_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete external_container_database
  oci_database_external_container_database:
    # required
    external_container_database_id: "ocid1.externalcontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete external_container_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_external_container_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
external_container_database:
    description:
        - Details of the ExternalContainerDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - The user-friendly name for the external database. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure external database
                  resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the Oracle Cloud Infrastructure external database resource.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_unique_name:
            description:
                - The `DB_UNIQUE_NAME` of the external database.
            returned: on success
            type: str
            sample: db_unique_name_example
        db_id:
            description:
                - The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.
            returned: on success
            type: str
            sample: "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx"
        database_version:
            description:
                - The Oracle Database version.
            returned: on success
            type: str
            sample: database_version_example
        database_edition:
            description:
                - The Oracle Database edition.
            returned: on success
            type: str
            sample: STANDARD_EDITION
        time_zone:
            description:
                - The time zone of the external database.
                  It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name,
                  depending on how the time zone value was specified when the database was created / last altered.
            returned: on success
            type: str
            sample: time_zone_example
        character_set:
            description:
                - The character set of the external database.
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character of the external database.
            returned: on success
            type: str
            sample: ncharacter_set_example
        db_packs:
            description:
                - The database packs licensed for the external Oracle Database.
            returned: on success
            type: str
            sample: db_packs_example
        database_configuration:
            description:
                - The Oracle Database configuration
            returned: on success
            type: str
            sample: RAC
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_management_status:
                    description:
                        - The status of the Database Management service.
                    returned: on success
                    type: str
                    sample: ENABLING
                database_management_connection_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: str
                    sample: "ocid1.databasemanagementconnection.oc1..xxxxxxEXAMPLExxxxxx"
                license_model:
                    description:
                        - The Oracle license model that applies to the external database.
                    returned: on success
                    type: str
                    sample: LICENSE_INCLUDED
        stack_monitoring_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                stack_monitoring_status:
                    description:
                        - The status of Stack Monitoring.
                    returned: on success
                    type: str
                    sample: ENABLING
                stack_monitoring_connector_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                          L(external database connector,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/database/latest/datatypes/CreateExternalDatabaseConnectorDetails).
                    returned: on success
                    type: str
                    sample: "ocid1.stackmonitoringconnector.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "db_unique_name": "db_unique_name_example",
        "db_id": "ocid1.db.oc1..xxxxxxEXAMPLExxxxxx",
        "database_version": "database_version_example",
        "database_edition": "STANDARD_EDITION",
        "time_zone": "time_zone_example",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "db_packs": "db_packs_example",
        "database_configuration": "RAC",
        "database_management_config": {
            "database_management_status": "ENABLING",
            "database_management_connection_id": "ocid1.databasemanagementconnection.oc1..xxxxxxEXAMPLExxxxxx",
            "license_model": "LICENSE_INCLUDED"
        },
        "stack_monitoring_config": {
            "stack_monitoring_status": "ENABLING",
            "stack_monitoring_connector_id": "ocid1.stackmonitoringconnector.oc1..xxxxxxEXAMPLExxxxxx"
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateExternalContainerDatabaseDetails
    from oci.database.models import UpdateExternalContainerDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalContainerDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(ExternalContainerDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(
            ExternalContainerDatabaseHelperGen, self
        ).get_possible_entity_types() + [
            "externalcontainerdatabase",
            "externalcontainerdatabases",
            "databaseexternalcontainerdatabase",
            "databaseexternalcontainerdatabases",
            "externalcontainerdatabaseresource",
            "externalcontainerdatabasesresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "external_container_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("external_container_database_id")

    def get_get_fn(self):
        return self.client.get_external_container_database

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_container_database,
            external_container_database_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_container_database,
            external_container_database_id=self.module.params.get(
                "external_container_database_id"
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
            self.client.list_external_container_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateExternalContainerDatabaseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_external_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_external_container_database_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateExternalContainerDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_external_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
                ),
                update_external_container_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_external_container_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                external_container_database_id=self.module.params.get(
                    "external_container_database_id"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ExternalContainerDatabaseHelperCustom = get_custom_class(
    "ExternalContainerDatabaseHelperCustom"
)


class ResourceHelper(
    ExternalContainerDatabaseHelperCustom, ExternalContainerDatabaseHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            external_container_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="external_container_database",
        service_client_class=DatabaseClient,
        namespace="database",
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
